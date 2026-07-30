#!/usr/bin/env python3
"""Auditoría reproducible de cierre para la presentación de la Unidad 02."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image
from pypdf import PdfReader


SLIDE_RE = re.compile(r"ppt/slides/slide(\d+)\.xml$")
NOTE_RE = re.compile(r"ppt/notesSlides/notesSlide(\d+)\.xml$")
MASTER_RE = re.compile(r"ppt/slideMasters/slideMaster(\d+)\.xml$")
LAYOUT_RE = re.compile(r"ppt/slideLayouts/slideLayout(\d+)\.xml$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def xml_root(archive: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(archive.read(name))


def text_runs(root: ET.Element) -> list[str]:
    return [
        element.text or ""
        for element in root.iter()
        if local_name(element.tag) == "t"
    ]


def numbered_entries(names: list[str], pattern: re.Pattern[str]) -> list[tuple[int, str]]:
    entries: list[tuple[int, str]] = []
    for name in names:
        match = pattern.fullmatch(name)
        if match:
            entries.append((int(match.group(1)), name))
    return sorted(entries)


def resolve_manifest_path(unit_dir: Path, raw_path: str) -> Path:
    normalized = Path(raw_path.replace("\\", "/"))
    if normalized.parts[:2] == ("units", "unit_02"):
        return unit_dir.parents[1] / normalized
    return unit_dir / normalized


def audit_pptx(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        slides = numbered_entries(names, SLIDE_RE)
        notes = numbered_entries(names, NOTE_RE)
        masters = numbered_entries(names, MASTER_RE)
        layouts = numbered_entries(names, LAYOUT_RE)

        presentation = xml_root(archive, "ppt/presentation.xml")
        slide_size = next(
            (
                {
                    "cx": int(element.attrib["cx"]),
                    "cy": int(element.attrib["cy"]),
                }
                for element in presentation.iter()
                if local_name(element.tag) == "sldSz"
            ),
            {},
        )

        slide_numbers_ok = 0
        slides_with_number_placeholder = 0
        alt_descriptions = 0
        slide_object_counts = Counter()
        autofit_counts = Counter()
        fonts: set[str] = set()

        for expected_number, slide_name in slides:
            root = xml_root(archive, slide_name)
            has_number_placeholder = False
            visible_numbers: list[str] = []
            for element in root.iter():
                name = local_name(element.tag)
                if name in {"sp", "pic", "graphicFrame", "cxnSp", "grpSp"}:
                    slide_object_counts[name] += 1
                if name in {"noAutofit", "spAutoFit", "normAutofit"}:
                    autofit_counts[name] += 1
                if name == "ph" and element.attrib.get("type") == "sldNum":
                    has_number_placeholder = True
                if name == "cNvPr" and element.attrib.get("descr", "").strip():
                    alt_descriptions += 1
                if name in {"latin", "ea", "cs"}:
                    typeface = element.attrib.get("typeface", "").strip()
                    if typeface and not typeface.startswith("+"):
                        fonts.add(typeface)
                if name == "fld" and element.attrib.get("type") == "slidenum":
                    visible_numbers.extend(text_runs(element))
            if has_number_placeholder:
                slides_with_number_placeholder += 1
            if str(expected_number) in visible_numbers:
                slide_numbers_ok += 1

        notes_nonempty = 0
        notes_with_sources = 0
        for _, note_name in notes:
            note_text = "\n".join(text_runs(xml_root(archive, note_name))).strip()
            if note_text:
                notes_nonempty += 1
            if "[Sources]" in note_text:
                notes_with_sources += 1

        external_targets: set[str] = set()
        for name in names:
            if not name.endswith(".rels"):
                continue
            root = xml_root(archive, name)
            for element in root.iter():
                if (
                    local_name(element.tag) == "Relationship"
                    and element.attrib.get("TargetMode") == "External"
                ):
                    external_targets.add(element.attrib.get("Target", ""))

        media_names = [
            name
            for name in names
            if name.startswith("ppt/media/") and not name.endswith("/")
        ]
        media_by_extension = Counter(Path(name).suffix.lower() for name in media_names)

    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "slides": len(slides),
        "notes": len(notes),
        "notes_nonempty": notes_nonempty,
        "notes_with_sources": notes_with_sources,
        "masters": len(masters),
        "layouts": len(layouts),
        "slide_size_emu": slide_size,
        "aspect_ratio": (
            round(slide_size["cx"] / slide_size["cy"], 6) if slide_size else None
        ),
        "slides_with_number_placeholder": slides_with_number_placeholder,
        "slide_numbers_matching": slide_numbers_ok,
        "alt_descriptions": alt_descriptions,
        "media_files": len(media_names),
        "media_by_extension": dict(sorted(media_by_extension.items())),
        "external_links": sorted(target for target in external_targets if target),
        "slide_objects": dict(sorted(slide_object_counts.items())),
        "autofit": dict(sorted(autofit_counts.items())),
        "fonts": sorted(fonts),
    }


def audit_unit(unit_dir: Path, pdf_path: Path | None) -> dict:
    required = [
        "brief.md",
        "storyboard.md",
        "slide_text.md",
        "speaker_notes.md",
        "asset_manifest.csv",
        "review.md",
        "consistency_report.md",
    ]
    required_status = {}
    for name in required:
        path = unit_dir / name
        required_status[name] = {
            "exists": path.is_file(),
            "bytes": path.stat().st_size if path.is_file() else 0,
        }

    scripts = sorted(path.name for path in (unit_dir / "scripts").glob("*") if path.is_file())
    chart_families = sorted(
        path.name for path in (unit_dir / "assets/generated/charts").glob("*") if path.is_dir()
    )
    diagram_variants = sorted(
        path.name
        for path in (unit_dir / "assets/generated/diagrams").glob("*")
        if path.is_dir()
    )
    renders = sorted(
        (unit_dir / "output/render_v02").glob("*.png"),
        key=lambda path: int(re.search(r"(\d+)", path.stem).group(1)),
    )
    render_sizes = Counter()
    for render in renders:
        with Image.open(render) as image:
            render_sizes[f"{image.width}x{image.height}"] += 1

    manifest_path = unit_dir / "asset_manifest.csv"
    manifest_rows: list[dict[str, str]] = []
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle))
    active_statuses = {
        "downloaded",
        "generated_validated",
        "implemented_as_validated_variants",
    }
    active_rows = [row for row in manifest_rows if row.get("status") in active_statuses]
    missing_active_paths = []
    for row in active_rows:
        raw_path = row.get("local_path", "").strip()
        if raw_path and not resolve_manifest_path(unit_dir, raw_path).exists():
            missing_active_paths.append(
                {"asset_id": row.get("asset_id"), "local_path": raw_path}
            )
    asset_ids = [row.get("asset_id", "") for row in manifest_rows]
    duplicate_asset_ids = sorted(
        asset_id for asset_id, count in Counter(asset_ids).items() if asset_id and count > 1
    )
    external_sources = [
        {
            "asset_id": row.get("asset_id"),
            "source_url": row.get("source_url"),
            "creator": row.get("creator"),
            "license": row.get("license"),
            "status": row.get("status"),
        }
        for row in manifest_rows
        if row.get("source_url", "").startswith(("http://", "https://"))
    ]

    pdf_result = None
    if pdf_path is not None:
        reader = PdfReader(str(pdf_path))
        first_box = reader.pages[0].mediabox
        pdf_result = {
            "path": str(pdf_path),
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            "pages": len(reader.pages),
            "encrypted": reader.is_encrypted,
            "page_size_points": [
                float(first_box.width),
                float(first_box.height),
            ],
        }

    return {
        "required_files": required_status,
        "scripts": {"count": len(scripts), "files": scripts},
        "charts": {"families": len(chart_families), "names": chart_families},
        "diagrams": {"variants": len(diagram_variants)},
        "render": {
            "count": len(renders),
            "sizes": dict(sorted(render_sizes.items())),
        },
        "manifest": {
            "rows": len(manifest_rows),
            "active_rows": len(active_rows),
            "missing_active_paths": missing_active_paths,
            "duplicate_asset_ids": duplicate_asset_ids,
            "external_sources": external_sources,
            "status_counts": dict(
                sorted(Counter(row.get("status", "") for row in manifest_rows).items())
            ),
        },
        "pdf": pdf_result,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pptx", required=True, type=Path)
    parser.add_argument("--unit-dir", required=True, type=Path)
    parser.add_argument("--source-pptx", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    result = {
        "pptx": audit_pptx(args.pptx.resolve()),
        "unit": audit_unit(args.unit_dir.resolve(), args.pdf.resolve() if args.pdf else None),
    }
    if args.source_pptx:
        source = args.source_pptx.resolve()
        result["source_pptx"] = {
            "path": str(source),
            "bytes": source.stat().st_size,
            "sha256": sha256(source),
            "binary_identical": sha256(source) == result["pptx"]["sha256"],
        }

    serialized = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.write_text(serialized + "\n", encoding="utf-8")
    print(serialized)


if __name__ == "__main__":
    main()
