"""Validación reproducible de los paquetes visuales generados para U05."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import pandas as pd
from PIL import Image


UNIT = Path(__file__).resolve().parents[1]
GENERATED = UNIT / "assets" / "generated"
CHART_IDS = {f"U05-CH-{i:03d}" for i in (1, 2, 3, 5, 6, 7, 8, 11, 13, 15, 16, 18, 19)}
DIAGRAM_IDS = {f"U05-DG-{i:03d}" for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15)}


def check_svg(path: Path) -> None:
    root = ET.parse(path).getroot()
    assert root.tag.endswith("svg"), path


def check_png(path: Path) -> None:
    with Image.open(path) as image:
        assert image.size == (2560, 1440), (path, image.size)


def validate_chart(folder: Path) -> dict:
    asset_id = folder.name
    assert asset_id in CHART_IDS
    readme = folder / "README.md"
    validation_path = folder / "validation.json"
    data_path = folder / "data.csv"
    scripts = list(folder.glob("u05_plot_*.py"))
    svgs = list(folder.glob("u05_fig_*.svg"))
    pngs = list(folder.glob("u05_fig_*.png"))
    assert readme.exists() and validation_path.exists() and data_path.exists()
    assert len(scripts) == len(svgs) == len(pngs) == 1
    check_svg(svgs[0])
    check_png(pngs[0])
    data = pd.read_csv(data_path)
    assert not data.empty
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    assert validation["classification"] == "gráfico cuantitativo"
    assert validation["critical_issues"] == validation["major_issues"] == 0
    return {"asset_id": asset_id, "status": "approved", "rows": len(data), "png": pngs[0].name, "svg": svgs[0].name}


def validate_layout(path: Path) -> int:
    layout = json.loads(path.read_text(encoding="utf-8"))
    width = layout["slide"]["frame"]["width"]
    height = layout["slide"]["frame"]["height"]
    assert (width, height) == (1280, 720)
    for element in layout["elements"]:
        bbox = element.get("bbox")
        if not bbox:
            continue
        left, top, box_width, box_height = bbox
        assert left >= -0.5 and top >= -0.5, (path, element.get("name"), bbox)
        assert left + box_width <= width + 0.5, (path, element.get("name"), bbox)
        assert top + box_height <= height + 0.5, (path, element.get("name"), bbox)
    return len(layout["elements"])


def validate_diagram(folder: Path) -> dict:
    asset_id = folder.name
    assert asset_id in DIAGRAM_IDS
    readme = folder / "README.md"
    validation_path = folder / "validation.json"
    source_path = folder / "diagram_source.json"
    svgs = list(folder.glob("u05_dg_*_master.svg"))
    pngs = list(folder.glob("u05_dg_*_master.png"))
    pptx = list(folder.glob("u05_dg_*_master.pptx"))
    layouts = list(folder.glob("u05_dg_*_master.layout.json"))
    assert readme.exists() and validation_path.exists() and source_path.exists()
    assert len(svgs) == len(pngs) == len(pptx) == len(layouts) == 1
    check_svg(svgs[0])
    check_png(pngs[0])
    with zipfile.ZipFile(pptx[0]) as archive:
        names = set(archive.namelist())
        assert "[Content_Types].xml" in names and "ppt/presentation.xml" in names
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    source = json.loads(source_path.read_text(encoding="utf-8"))
    assert validation["critical_issues"] == validation["major_issues"] == 0
    assert validation["status"] == "approved"
    assert validation["font_floor"]["node_body_pt"] >= 22
    assert validation["padding_inches"] >= 0.18
    assert set(validation["object_ids"]) == {node["id"] for node in source["nodes"]}
    element_count = validate_layout(layouts[0])
    return {"asset_id": asset_id, "status": "approved", "objects": len(source["nodes"]), "connectors": len(source["edges"]), "layout_elements": element_count, "pptx": pptx[0].name}


def main() -> None:
    chart_root = GENERATED / "charts"
    diagram_root = GENERATED / "diagrams"
    chart_folders = {p.name: p for p in chart_root.iterdir() if p.is_dir() and p.name.startswith("U05-CH-")}
    diagram_folders = {p.name: p for p in diagram_root.iterdir() if p.is_dir() and p.name.startswith("U05-DG-")}
    assert set(chart_folders) == CHART_IDS
    assert set(diagram_folders) == DIAGRAM_IDS
    charts = [validate_chart(chart_folders[i]) for i in sorted(CHART_IDS)]
    diagrams = [validate_diagram(diagram_folders[i]) for i in sorted(DIAGRAM_IDS)]
    summary = {
        "status": "approved",
        "chart_count": len(charts),
        "diagram_count": len(diagrams),
        "critical_issues": 0,
        "major_issues": 0,
        "checks": ["required_files", "png_2560x1440", "svg_parse", "csv_nonempty", "pptx_zip", "layout_bounds", "font_floor", "padding", "object_ids"],
        "charts": charts,
        "diagrams": diagrams,
    }
    output = GENERATED / "asset_validation_summary.json"
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"PASS: {len(charts)} gráficos y {len(diagrams)} diagramas; 0 problemas críticos o mayores")


if __name__ == "__main__":
    main()
