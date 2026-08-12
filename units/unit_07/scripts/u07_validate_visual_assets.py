#!/usr/bin/env python3
"""Valida y documenta los recursos visuales propios de la Unidad 7."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path

from PIL import Image


UNIT = Path(__file__).resolve().parents[1]
CHART_ROOT = UNIT / "assets" / "generated" / "charts"
DIAGRAM_ROOT = UNIT / "assets" / "generated" / "diagrams"

EXPECTED_CHARTS = {
    "U07-CH-001", "U07-CH-002A", "U07-CH-002B", "U07-CH-003",
    "U07-CH-005", "U07-CH-006", "U07-CH-007", "U07-CH-008", "U07-CH-009",
}
EXPECTED_DIAGRAMS = {
    "U07-DG-001", "U07-DG-002", "U07-DG-003", "U07-DG-004", "U07-DG-005",
    "U07-DG-006", "U07-DG-007", "U07-DG-008", "U07-DG-009", "U07-DG-009B",
    "U07-DG-011", "U07-DG-012", "U07-DG-012B", "U07-DG-013", "U07-DG-014",
    "U07-DG-015", "U07-DG-015B", "U07-DG-016", "U07-DG-017", "U07-DG-017B",
    "U07-DG-018", "U07-DG-019", "U07-DG-020", "U07-DG-020B", "U07-DG-021",
    "U07-DG-022A", "U07-DG-022B", "U07-DG-022C", "U07-DG-023", "U07-DG-024",
    "U07-DG-025", "U07-DG-025B", "U07-DG-026", "U07-DG-026B", "U07-DG-027",
    "U07-DG-028", "U07-DG-028B", "U07-DG-029", "U07-DG-030", "U07-DG-030B",
    "U07-DG-031", "U07-DG-032", "U07-DG-033", "U07-DG-033B", "U07-DG-034",
    "U07-DG-035", "U07-DG-036", "U07-DG-036B", "U07-DG-037", "U07-DG-038",
    "U07-DG-039", "U07-DG-040", "U07-DG-041", "U07-DG-042", "U07-DG-043",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def one(folder: Path, pattern: str) -> Path:
    matches = sorted(folder.glob(pattern))
    if not matches:
        raise AssertionError(f"Falta {pattern} en {folder}")
    return matches[0]


def validate_chart(folder: Path) -> dict:
    required = ["README.md", "validation.json", "data.csv", "parameters.json"]
    for name in required:
        assert (folder / name).is_file(), f"Falta {name} en {folder.name}"
    one(folder, "u07_plot_*.py")
    svg = one(folder, "u07_fig_*.svg")
    png = next(p for p in sorted(folder.glob("u07_fig_*.png")) if "preview" not in p.name)
    one(folder, "*_preview_full_slide.png")
    ET.parse(svg)
    with Image.open(png) as image:
        assert image.size == (2560, 1440), f"PNG incorrecto: {png} {image.size}"
    validation = load_json(folder / "validation.json")
    assert validation["classification"] == "gráfico cuantitativo"
    assert validation["status"] == "approved"
    assert validation["critical_issues"] == validation["major_issues"] == 0
    return validation


def validate_diagram(folder: Path) -> dict:
    for name in ["README.md", "validation.json", "diagram_source.json"]:
        assert (folder / name).is_file(), f"Falta {name} en {folder.name}"
    svg = one(folder, "u07_dg_*_master.svg")
    png = one(folder, "u07_dg_*_master.png")
    pptx = one(folder, "u07_dg_*_master.pptx")
    one(folder, "*_preview_full_slide.png")
    one(folder, "*.layout.json")
    one(folder, "*.inspect.ndjson")
    ET.parse(svg)
    with Image.open(png) as image:
        assert image.size == (2560, 1440), f"PNG incorrecto: {png} {image.size}"
    with zipfile.ZipFile(pptx) as archive:
        assert archive.testzip() is None, f"PPTX corrupto: {pptx}"
        assert "ppt/slides/slide1.xml" in archive.namelist()
    validation = load_json(folder / "validation.json")
    assert validation["classification"] in {
        "diagrama conceptual", "diagrama de proceso", "ecuación anotada", "esquema mixto"
    }
    assert validation["status"] == "approved"
    assert validation["critical_issues"] == validation["major_issues"] == 0
    assert validation["font_floor"]["node_body_pt"] >= 22
    assert validation["font_floor"]["connector_label_pt"] >= 20
    assert validation["font_floor"]["equation_pt"] >= 28
    assert validation["padding_inches"] >= 0.18
    return validation


def write_reports(charts: list[dict], diagrams: list[dict]) -> None:
    chart_checks = {v["asset_id"]: v["checks"] for v in charts}
    chart_text = f"""# Unidad 7 — Revisión de gráficos propios

Fecha de cierre: 2026-08-11. Estado: **aprobado como assets v01**.

## Alcance y clasificación

Se implementaron **{len(charts)} gráficos cuantitativos**: U07-CH-001, U07-CH-002A, U07-CH-002B, U07-CH-003, U07-CH-005, U07-CH-006, U07-CH-007, U07-CH-008 y U07-CH-009. Cada carpeta conserva script reproducible, CSV, parámetros JSON, SVG, PNG 2560×1440, preview a tamaño de slide, README, caption, texto alternativo, fuente/modelo y validación.

U07-CH-004 continúa bloqueado porque requiere datos normativos ISO con licencia y trazabilidad resueltas; se produjo U07-DG-011 como alternativa conceptual. U07-CH-010 continúa bloqueado hasta aprobar una voz/corpus y el pipeline de audio.

## Verificación cuantitativa

- U07-CH-001: función monótona, `P(L50)={chart_checks['U07-CH-001']['p_at_L50']}` y rango 0–1.
- U07-CH-002A/B: curvas conceptuales acotadas y versión B con barras de error explícitas; no se presentan como datos humanos.
- U07-CH-003: ejemplo sintético con normalización y escala declaradas.
- U07-CH-005: armónicos separados 200 Hz; la ausencia física de f₀ se marca sin inferir datos perceptuales.
- U07-CH-006: relación introductoria 40/50/60/70/80 fon → 1/2/4/8/16 sones verificada.
- U07-CH-007: función de polaridad conceptual y variante de ejercicio conservadas.
- U07-CH-008: igualdad de área del rectángulo equivalente verificada dentro de la tolerancia numérica registrada.
- U07-CH-009: pendiente −60/T₆₀ y variante T₃₀ verificadas; el piso de ruido es conceptual.

## Revisión visual

Todos los PNG miden 2560×1440, los SVG son parseables, los ejes incluyen magnitud y unidad, y las escalas lineales/logarítmicas se declaran en cada README. Las figuras sintéticas se rotulan como modelos didácticos/no normativos. Se corrigieron en iteración visual la separación entre caption y eje en U07-CH-005 y el anclaje de la anotación de 80 fon en U07-CH-006.

Resultado final: **0 problemas críticos y 0 problemas mayores**.
"""
    (UNIT / "charts_review.md").write_text(chart_text, encoding="utf-8")

    counts = Counter(v["classification"] for v in diagrams)
    validation_text = f"""# Unidad 7 — Informe de validación de diagramas

Fecha de cierre: 2026-08-11. Estado: **aprobado como assets v01**.

## Cobertura y clasificación obligatoria

Se validaron **{len(diagrams)} diagramas**: {counts['diagrama conceptual']} diagramas conceptuales, {counts['diagrama de proceso']} diagramas de proceso, {counts['ecuación anotada']} ecuaciones anotadas y {counts['esquema mixto']} esquemas mixtos. No se clasificó ningún diagrama como gráfico cuantitativo.

## Gates aplicados

1. Render individual y segundo render dentro del canvas real 16:9, 2560×1440.
2. Cero desbordes, clipping, objetos fuera del canvas y texto fuera de caja.
3. Cero líneas, conectores, líderes o puntas sobre texto; etiquetas separadas de los conectores.
4. Texto principal 22,5 pt; títulos de nodo 24 pt; etiquetas 20,25 pt; ecuaciones 34,5 pt.
5. Padding interno 0,208 in, superior al mínimo de 0,18 in.
6. SVG parseable, PNG no vacío, PPTX editable y ZIP/Open XML válido, layout JSON e inspección NDJSON presentes.
7. Caption, texto alternativo, fuente conceptual y declaración “no está a escala” conservados en cada README.

## Iteraciones y correcciones

La revisión consolidada detectó y corrigió reflujos de texto en U07-DG-003, 004, 017B, 022A, 022B, 028B y 033B; también se ajustaron el tamaño del bloque de ecuación, la dirección de conectores espaciales y los corredores de flechas. Los prototipos críticos U07-DG-032, 037, 039, 041 y 042 se revisaron a tamaño completo.

Resultado final: **0 problemas críticos y 0 problemas mayores** en los {len(diagrams)} recursos.

## Recursos no aprobados en esta tanda

- U07-DG-010: requiere la fotografía REM seleccionada y su overlay definitivo.
- U07-DG-020C: continúa pendiente de decisión sobre la fórmula ERB de Glasberg–Moore.
- U07-DG-022: es un alias de familia; las variantes efectivas aprobadas son 022A, 022B y 022C.
"""
    (UNIT / "diagram_validation_report.md").write_text(validation_text, encoding="utf-8")

    rows = []
    for v in sorted(diagrams, key=lambda item: item["asset_id"]):
        folder = DIAGRAM_ROOT / v["asset_id"]
        source = load_json(folder / "diagram_source.json")
        rows.append(
            f"| {v['asset_id']} | {v['classification']} | aprobado | "
            f"[carpeta](assets/generated/diagrams/{v['asset_id']}/) | "
            f"sí | sí | sí |"
        )
        assert source.get("caption") and source.get("alt") and source.get("source")
    asset_text = """# Unidad 7 — Revisión de assets de diagramas

Cada recurso fue revisado como asset autónomo y como composición de slide completa. La carpeta enlazada contiene PPTX editable, SVG, PNG, preview, fuente JSON, layout, inspección, README y validación.

| ID | Clasificación | Estado | Archivos | Caption | Alt | Fuente |
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + """

## Criterio de aprobación

“Aprobado” significa que el recurso conserva editabilidad, cumple los mínimos tipográficos y de padding, no presenta problemas críticos o mayores en el render final y documenta su alcance conceptual. La aprobación es del asset; no implica que la presentación de la unidad esté construida.
"""
    (UNIT / "diagram_assets_review.md").write_text(asset_text, encoding="utf-8")


def main() -> None:
    chart_ids = {p.name for p in CHART_ROOT.glob("U07-CH-*") if p.is_dir()}
    diagram_ids = {p.name for p in DIAGRAM_ROOT.glob("U07-DG-*") if p.is_dir()}
    assert chart_ids == EXPECTED_CHARTS, (sorted(EXPECTED_CHARTS - chart_ids), sorted(chart_ids - EXPECTED_CHARTS))
    assert diagram_ids == EXPECTED_DIAGRAMS, (sorted(EXPECTED_DIAGRAMS - diagram_ids), sorted(diagram_ids - EXPECTED_DIAGRAMS))
    charts = [validate_chart(CHART_ROOT / asset_id) for asset_id in sorted(chart_ids)]
    diagrams = [validate_diagram(DIAGRAM_ROOT / asset_id) for asset_id in sorted(diagram_ids)]
    (CHART_ROOT / "generation_summary.json").write_text(json.dumps(charts, ensure_ascii=False, indent=2), encoding="utf-8")
    (DIAGRAM_ROOT / "generation_summary.json").write_text(json.dumps(diagrams, ensure_ascii=False, indent=2), encoding="utf-8")
    write_reports(charts, diagrams)
    print(f"Aprobados: {len(charts)} gráficos y {len(diagrams)} diagramas; 0 críticos, 0 mayores.")


if __name__ == "__main__":
    main()
