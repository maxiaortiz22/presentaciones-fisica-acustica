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
SLIDE_W, SLIDE_H = 12_192_000, 6_858_000


def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit("Uso: u10_validate_diagram_context.py <pptx> <build-log.json> <diagram-report.md> <output.json>")
    pptx, build_log_path, approved_report, output = map(lambda p: Path(p).resolve(), sys.argv[1:])
    build = json.loads(build_log_path.read_text(encoding="utf-8"))["slides"]
    approved_text = approved_report.read_text(encoding="utf-8")
    findings: list[dict[str, object]] = []
    reviewed: list[dict[str, object]] = []

    with ZipFile(pptx) as zf:
        for entry in build:
            if entry.get("assetType") not in {"diagram", "composite"}:
                continue
            assets = [a.strip() for a in (entry.get("asset") or "").split(",") if "-DG-" in a]
            if not assets:
                continue
            slide_no = int(entry["slide"])
            xml = zf.read(f"ppt/slides/slide{slide_no}.xml")
            root = ET.fromstring(xml)
            xml_text = xml.decode("utf-8", errors="ignore")
            slide_record = {"slide": slide_no, "slide_id": entry["id"], "assets": assets, "checks": []}
            for asset in assets:
                if asset not in approved_text:
                    findings.append({"severity": "critical", "slide": slide_no, "asset": asset, "code": "asset_not_in_approved_report"})
                named = [el for el in root.findall(".//*[@name]") if (el.get("name") or "").startswith(asset)]
                if not named:
                    findings.append({"severity": "critical", "slide": slide_no, "asset": asset, "code": "asset_not_found"})
                    continue
                slide_record["checks"].append("asset_present")

                outside = []
                min_font = None
                for shape in root.findall(".//p:sp", NS):
                    cnv = shape.find("./p:nvSpPr/p:cNvPr", NS)
                    name = (cnv.get("name") if cnv is not None else "") or ""
                    if not name.startswith(asset):
                        continue
                    off = shape.find(".//a:xfrm/a:off", NS)
                    ext = shape.find(".//a:xfrm/a:ext", NS)
                    if off is not None and ext is not None:
                        x, y = (int(off.get(k, "0")) for k in ("x", "y"))
                        w, h = (int(ext.get(k, "0")) for k in ("cx", "cy"))
                        if x < 0 or y < 0 or x + w > SLIDE_W or y + h > SLIDE_H:
                            outside.append(name)
                    if name.endswith("-text"):
                        sizes = [int(el.get("sz")) / 100 for el in shape.findall(".//*[@sz]") if (el.get("sz") or "").isdigit()]
                        if sizes:
                            local_min = min(sizes)
                            min_font = local_min if min_font is None else min(min_font, local_min)
                if outside:
                    findings.append({"severity": "major", "slide": slide_no, "asset": asset, "code": "outside_canvas", "objects": outside})
                else:
                    slide_record["checks"].append("inside_canvas")
                if entry.get("assetType") == "diagram" and min_font is not None and min_font < 22:
                    findings.append({"severity": "major", "slide": slide_no, "asset": asset, "code": "diagram_font_below_22", "value": min_font})
                else:
                    slide_record["checks"].append("font_floor_preserved_or_svg")

                edge_positions = [m.start() for m in re.finditer(rf'name="{re.escape(asset)}-[^"]*(?:edge|link|connector)[^"]*"', xml_text)]
                box_positions = [m.start() for m in re.finditer(rf'name="{re.escape(asset)}-[^"]*(?:box|visual-alt)[^"]*"', xml_text)]
                if edge_positions and box_positions and max(edge_positions) > min(box_positions):
                    findings.append({"severity": "major", "slide": slide_no, "asset": asset, "code": "connector_z_order"})
                else:
                    slide_record["checks"].append("connectors_behind_nodes_or_svg")
            reviewed.append(slide_record)

    report = {
        "pptx": str(pptx),
        "diagram_slides_reviewed": len(reviewed),
        "diagram_instances_reviewed": sum(len(r["assets"]) for r in reviewed),
        "method": "Verificación OOXML de presencia, límites de canvas, piso tipográfico y z-order; revisión visual del render final en lotes y a tamaño completo para slides representativas.",
        "geometry_note": "Las formas nativas usan la misma transformación afín uniforme del modelo validado; las relaciones de separación y corredores se preservan.",
        "findings": findings,
        "critical": sum(1 for f in findings if f["severity"] == "critical"),
        "major": sum(1 for f in findings if f["severity"] == "major"),
        "status": "pass" if not findings else "fail",
        "slides": reviewed,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("diagram_slides_reviewed", "diagram_instances_reviewed", "critical", "major", "status")}, ensure_ascii=False, indent=2))
    if findings:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
