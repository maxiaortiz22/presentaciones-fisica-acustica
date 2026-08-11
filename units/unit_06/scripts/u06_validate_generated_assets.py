"""Valida integridad, dimensiones y gates de los assets generados de U06."""

from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image


UNIT_DIR = Path(__file__).resolve().parents[1]
ROOT = UNIT_DIR / "assets" / "generated"
CHARTS = ["U06-CH-001", "U06-CH-002A", "U06-CH-002B", "U06-CH-003", "U06-CH-004", "U06-CH-006"]
DIAGRAMS = [
    "U06-DG-001", "U06-DG-002", "U06-DG-003", "U06-DG-004", "U06-DG-006", "U06-DG-008",
    "U06-DG-009", "U06-DG-009B", "U06-DG-010", "U06-DG-012", "U06-DG-013", "U06-DG-016",
    "U06-DG-017", "U06-DG-019", "U06-DG-021", "U06-DG-022", "U06-DG-023", "U06-DG-024",
    "U06-DG-025", "U06-DG-026", "U06-DG-026B", "U06-DG-027", "U06-DG-028", "U06-DG-030",
    "U06-DG-031", "U06-DG-033", "U06-DG-037", "U06-DG-038", "U06-DG-039", "U06-DG-040",
    "U06-DG-042", "U06-DG-043", "U06-DG-044", "U06-DG-045", "U06-DG-046", "U06-DG-047",
    "U06-DG-048", "U06-DG-049", "U06-DG-051", "U06-DG-052", "U06-DG-053", "U06-DG-054",
    "U06-DG-055", "U06-DG-056", "U06-DG-057", "U06-DG-058", "U06-DG-058B", "U06-DG-059",
    "U06-DG-059B", "U06-DG-060", "U06-DG-062", "U06-DG-063", "U06-DG-064",
]


def require(condition: bool, message: str, issues: list[dict], asset_id: str) -> None:
    if not condition:
        issues.append({"asset_id": asset_id, "severity": "major", "message": message})


def validate_png(path: Path, issues: list[dict], asset_id: str) -> None:
    require(path.exists(), f"falta PNG: {path.name}", issues, asset_id)
    if path.exists():
        with Image.open(path) as image:
            require(image.size == (2560, 1440), f"PNG {image.size}, esperado 2560x1440", issues, asset_id)


def validate_svg(path: Path, issues: list[dict], asset_id: str) -> None:
    require(path.exists(), f"falta SVG: {path.name}", issues, asset_id)
    if path.exists():
        try:
            root = ET.parse(path).getroot()
            require(root.tag.endswith("svg"), "raíz SVG inválida", issues, asset_id)
        except Exception as exc:  # pragma: no cover - diagnóstico
            issues.append({"asset_id": asset_id, "severity": "major", "message": f"SVG no parseable: {exc}"})


def validate_chart(asset_id: str) -> dict:
    folder = ROOT / "charts" / asset_id
    issues: list[dict] = []
    pngs, svgs, scripts = list(folder.glob("*.png")), list(folder.glob("*.svg")), list(folder.glob("*.py"))
    require(len(pngs) == 1, "debe existir un PNG", issues, asset_id)
    require(len(svgs) == 1, "debe existir un SVG", issues, asset_id)
    require(len(scripts) == 1, "debe existir un wrapper Python", issues, asset_id)
    if pngs:
        validate_png(pngs[0], issues, asset_id)
    if svgs:
        validate_svg(svgs[0], issues, asset_id)
    for name in ["data.csv", "parameters.json", "README.md", "validation.json"]:
        require((folder / name).exists(), f"falta {name}", issues, asset_id)
    if (folder / "data.csv").exists():
        with (folder / "data.csv").open(encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
        require(len(rows) > 10, "data.csv vacío o insuficiente", issues, asset_id)
    validation = json.loads((folder / "validation.json").read_text(encoding="utf-8"))
    require(validation.get("classification") == "gráfico cuantitativo", "clasificación incorrecta", issues, asset_id)
    require(validation.get("status") == "approved", "validation no aprobada", issues, asset_id)
    require(validation.get("critical_issues") == 0 and validation.get("major_issues") == 0, "issues declarados", issues, asset_id)
    return {"asset_id": asset_id, "kind": "chart", "issues": issues, "status": "approved" if not issues else "needs_revision"}


def validate_diagram(asset_id: str) -> dict:
    folder = ROOT / "diagrams" / asset_id
    issues: list[dict] = []
    pngs, svgs, pptxs = list(folder.glob("*.png")), list(folder.glob("*.svg")), list(folder.glob("*.pptx"))
    require(len(pngs) == 1, "debe existir un PNG", issues, asset_id)
    require(len(svgs) == 1, "debe existir un SVG", issues, asset_id)
    require(len(pptxs) == 1, "debe existir un PPTX editable", issues, asset_id)
    if pngs:
        validate_png(pngs[0], issues, asset_id)
    if svgs:
        validate_svg(svgs[0], issues, asset_id)
    for pattern in ["diagram_source.json", "README.md", "validation.json"]:
        require((folder / pattern).exists(), f"falta {pattern}", issues, asset_id)
    require(len(list(folder.glob("*.layout.json"))) == 1, "falta layout JSON", issues, asset_id)
    require(len(list(folder.glob("*.inspect.ndjson"))) == 1, "falta inspección estructural", issues, asset_id)
    if pptxs:
        require(zipfile.is_zipfile(pptxs[0]), "PPTX no es un contenedor ZIP válido", issues, asset_id)
        if zipfile.is_zipfile(pptxs[0]):
            with zipfile.ZipFile(pptxs[0]) as archive:
                names = set(archive.namelist())
            require("ppt/slides/slide1.xml" in names, "PPTX sin slide editable", issues, asset_id)
    validation = json.loads((folder / "validation.json").read_text(encoding="utf-8"))
    require(validation.get("classification") in {"diagrama conceptual", "diagrama de proceso", "ecuación anotada", "esquema mixto"}, "clasificación incorrecta", issues, asset_id)
    require(validation.get("status") == "approved", "validation no aprobada", issues, asset_id)
    require(validation.get("critical_issues") == 0 and validation.get("major_issues") == 0, "issues declarados", issues, asset_id)
    checks = validation.get("checks", {})
    require(all(checks.get(key) == 0 for key in ["text_overflow", "text_clipping", "connector_over_text", "label_on_line", "arrowhead_over_text", "objects_outside_canvas"]), "gate geométrico no satisfecho", issues, asset_id)
    return {"asset_id": asset_id, "kind": "diagram", "issues": issues, "status": "approved" if not issues else "needs_revision"}


def main() -> int:
    results = [validate_chart(asset_id) for asset_id in CHARTS] + [validate_diagram(asset_id) for asset_id in DIAGRAMS]
    manifest_ids = set()
    with (UNIT_DIR / "asset_manifest.csv").open(encoding="utf-8-sig") as handle:
        manifest_ids = {row["asset_id"] for row in csv.DictReader(handle)}
    missing_manifest = sorted((set(CHARTS) | set(DIAGRAMS)) - manifest_ids)
    all_issues = [issue for result in results for issue in result["issues"]]
    if missing_manifest:
        all_issues.append({"asset_id": "asset_manifest.csv", "severity": "major", "message": f"faltan IDs: {missing_manifest}"})
    summary = {
        "unit": "06",
        "charts_approved": len(CHARTS),
        "diagrams_approved": len(DIAGRAMS),
        "assets_checked": len(results),
        "critical_issues": sum(issue["severity"] == "critical" for issue in all_issues),
        "major_issues": sum(issue["severity"] == "major" for issue in all_issues),
        "manifest_missing": missing_manifest,
        "status": "approved" if not all_issues else "needs_revision",
        "results": results,
    }
    (ROOT / "asset_validation_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: summary[key] for key in ["assets_checked", "charts_approved", "diagrams_approved", "critical_issues", "major_issues", "status"]}, ensure_ascii=False))
    return 0 if not all_issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
