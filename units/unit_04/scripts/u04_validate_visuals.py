"""Validación de integridad de entregables visuales de la Unidad 4."""
from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CHARTS = ROOT / "assets" / "generated" / "charts"
DIAGRAMS = ROOT / "assets" / "generated" / "diagrams"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_chart(cid: str) -> dict:
    d = CHARTS / cid
    require((d / "README.md").exists(), f"{cid}: falta README")
    require((d / "data.csv").exists(), f"{cid}: faltan datos")
    pngs = sorted(d.glob("*.png")); svgs = sorted(d.glob("*.svg"))
    require(pngs and len(pngs) == len(svgs), f"{cid}: variantes PNG/SVG incompletas")
    sizes = []
    for p in pngs:
        with Image.open(p) as im:
            require(im.width >= 1800 and im.height >= 1200, f"{cid}: PNG insuficiente {p.name} {im.size}")
            sizes.append(im.size)
    for p in svgs:
        ET.parse(p)
    return {"id": cid, "variants": len(pngs), "png_sizes": sizes}


def validate_diagram(did: str) -> dict:
    d = DIAGRAMS / did
    require((d / "README.md").exists(), f"{did}: falta README")
    require((d / "validation.json").exists(), f"{did}: falta validación")
    png = next(d.glob("u04_fig_*.png")); svg = next(d.glob("u04_fig_*.svg")); pptx = next(d.glob("*_editable.pptx"))
    with Image.open(png) as im:
        require(im.size == (2560, 1440), f"{did}: render no está a 2560×1440")
    ET.parse(svg)
    require(pptx.stat().st_size > 10_000, f"{did}: PPTX editable inválido")
    report = json.loads((d / "validation.json").read_text(encoding="utf-8"))
    require(report["status"] == "approved" and report["critical"] == 0 and report["major"] == 0, f"{did}: no aprobado")
    require(report["minimum_main_font_pt"] >= 22, f"{did}: fuente insuficiente")
    return {"id": did, "status": report["status"], "objects": report["objects"]}


def main() -> None:
    chart_ids = [f"U04-CH-{n:03d}" for n in list(range(1, 12)) + [13, 14, 15]]
    diagram_ids = [f"U04-DG-{n:03d}" for n in range(1, 23)]
    result = {
        "charts": [validate_chart(cid) for cid in chart_ids],
        "diagrams": [validate_diagram(did) for did in diagram_ids],
        "pending": {"U04-CH-012": "Descarga del dataset de 326–466 MB no autorizada."},
    }
    (ROOT / "visual_validation_summary.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {len(chart_ids)} gráficos, {len(diagram_ids)} diagramas; CH-012 pendiente por aprobación externa.")


if __name__ == "__main__":
    main()
