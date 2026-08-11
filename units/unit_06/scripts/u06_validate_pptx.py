from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


def numeric_key(name: str) -> int:
    match = re.search(r"(\d+)(?=\.xml$)", name)
    return int(match.group(1)) if match else 0


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Uso: python u06_validate_pptx.py <deck.pptx> <report.json>")
    deck = Path(sys.argv[1]).resolve()
    report_path = Path(sys.argv[2]).resolve()
    with ZipFile(deck) as archive:
        names = archive.namelist()
        slides = sorted(
            (n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)), key=numeric_key
        )
        notes = sorted(
            (n for n in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)), key=numeric_key
        )
        masters = [n for n in names if re.fullmatch(r"ppt/slideMasters/slideMaster\d+\.xml", n)]
        layouts = [n for n in names if re.fullmatch(r"ppt/slideLayouts/slideLayout\d+\.xml", n)]
        presentation = etree.fromstring(archive.read("ppt/presentation.xml"))
        ns_p = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"}
        size = presentation.find("p:sldSz", ns_p)
        slide_size = [int(size.get("cx")), int(size.get("cy"))]
        ns = {
            "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
            "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        }
        picture_count = 0
        descriptions = []
        local_placeholders = 0
        sources_notes = 0
        alt_notes = 0
        out_of_canvas = []
        for index, slide_name in enumerate(slides, 1):
            root = etree.fromstring(archive.read(slide_name))
            picture_count += len(root.xpath(".//p:pic", namespaces=ns))
            local_placeholders += len(root.xpath(".//p:ph", namespaces=ns))
            for node in root.xpath(".//p:cNvPr", namespaces=ns):
                if node.get("descr"):
                    descriptions.append({"slide": index, "name": node.get("name"), "descr": node.get("descr")})
            for xfrm in root.xpath(".//a:xfrm[not(ancestor::p:grpSp)]", namespaces=ns):
                off = xfrm.find("a:off", ns)
                ext = xfrm.find("a:ext", ns)
                if off is None or ext is None:
                    continue
                x, y = int(off.get("x", "0")), int(off.get("y", "0"))
                cx, cy = int(ext.get("cx", "0")), int(ext.get("cy", "0"))
                tolerance = 20000
                if x < -tolerance or y < -tolerance or x + cx > slide_size[0] + tolerance or y + cy > slide_size[1] + tolerance:
                    out_of_canvas.append({"slide": index, "x": x, "y": y, "cx": cx, "cy": cy})
        for note_name in notes:
            root = etree.fromstring(archive.read(note_name))
            text = " ".join(root.xpath(".//a:t/text()", namespaces=ns))
            sources_notes += int("[Sources]" in text)
            alt_notes += int("[Alt text]" in text)
        external_links = 0
        for name in names:
            if re.fullmatch(r"ppt/slides/_rels/slide\d+\.xml\.rels", name):
                root = etree.fromstring(archive.read(name))
                external_links += sum(1 for rel in root if rel.get("TargetMode") == "External")

    report = {
        "deck": str(deck),
        "slides": len(slides),
        "notes_slides": len(notes),
        "masters": len(masters),
        "layouts": len(layouts),
        "slide_size_emu": slide_size,
        "ratio": round(slide_size[0] / slide_size[1], 6),
        "pictures": picture_count,
        "objects_with_alt_text": len(descriptions),
        "notes_with_sources": sources_notes,
        "notes_with_alt_text": alt_notes,
        "local_placeholders": local_placeholders,
        "external_links": external_links,
        "out_of_canvas_objects": out_of_canvas,
        "status": "pass" if (
            len(slides) == 117
            and len(notes) == 117
            and len(masters) == 2
            and len(layouts) == 27
            and sources_notes == 117
            and alt_notes == 117
            and local_placeholders == 0
            and not out_of_canvas
            and len(descriptions) >= picture_count
        ) else "review",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
