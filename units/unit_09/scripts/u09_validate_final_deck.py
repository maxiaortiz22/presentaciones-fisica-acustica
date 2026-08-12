from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Uso: u09_validate_final_deck.py <pptx> <render_dir> <output.json>")
    pptx = Path(sys.argv[1]).resolve()
    render_dir = Path(sys.argv[2]).resolve()
    output = Path(sys.argv[3]).resolve()
    findings: list[dict[str, object]] = []

    with ZipFile(pptx) as zf:
        names = set(zf.namelist())
        slide_parts = sorted(
            (n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"\d+", n).group()),
        )
        note_parts = [n for n in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)]
        masters = [n for n in names if re.fullmatch(r"ppt/slideMasters/slideMaster\d+\.xml", n)]
        layouts = [n for n in names if re.fullmatch(r"ppt/slideLayouts/slideLayout\d+\.xml", n)]
        if len(slide_parts) != 96:
            findings.append({"severity": "critical", "code": "slide_count", "value": len(slide_parts)})
        if len(note_parts) != 96:
            findings.append({"severity": "major", "code": "notes_count", "value": len(note_parts)})

        empty_placeholders = []
        missing_alt_slides = []
        full_slide_images = []
        for idx, part in enumerate(slide_parts, 1):
            root = ET.fromstring(zf.read(part))
            for shape in root.findall(".//p:sp", NS):
                if shape.find("./p:nvSpPr/p:nvPr/p:ph", NS) is not None:
                    text = "".join(shape.itertext()).strip()
                    if not text:
                        empty_placeholders.append(idx)
            images = root.findall(".//p:pic", NS)
            for picture in images:
                cnv = picture.find("./p:nvPicPr/p:cNvPr", NS)
                descr = (cnv.get("descr") if cnv is not None else "") or ""
                if not descr.strip():
                    missing_alt_slides.append(idx)
                ext = picture.find(".//a:xfrm/a:ext", NS)
                if ext is not None and int(ext.get("cx", "0")) >= 11_500_000 and int(ext.get("cy", "0")) >= 6_400_000:
                    full_slide_images.append(idx)

        if empty_placeholders:
            findings.append({"severity": "major", "code": "empty_placeholders", "slides": sorted(set(empty_placeholders))})
        if missing_alt_slides:
            findings.append({"severity": "major", "code": "missing_image_alt", "slides": sorted(set(missing_alt_slides))})
        if full_slide_images:
            findings.append({"severity": "critical", "code": "flattened_slides", "slides": sorted(set(full_slide_images))})

        pres = ET.fromstring(zf.read("ppt/presentation.xml"))
        size = pres.find("p:sldSz", NS)
        cx, cy = int(size.get("cx")), int(size.get("cy"))
        ratio = cx / cy
        if abs(ratio - 16 / 9) > 0.001:
            findings.append({"severity": "critical", "code": "aspect_ratio", "value": ratio})

    renders = list(render_dir.glob("slide-*.png"))
    if len(renders) != 96:
        findings.append({"severity": "major", "code": "render_count", "value": len(renders)})

    report = {
        "pptx": str(pptx),
        "slides": len(slide_parts),
        "notes": len(note_parts),
        "masters": len(masters),
        "layouts": len(layouts),
        "rendered_slides": len(renders),
        "slide_size_emu": [cx, cy],
        "aspect_ratio": ratio,
        "findings": findings,
        "critical": sum(1 for f in findings if f["severity"] == "critical"),
        "major": sum(1 for f in findings if f["severity"] == "major"),
        "status": "pass" if not findings else "fail",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if findings:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
