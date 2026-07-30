from __future__ import annotations

import csv
import json
from pathlib import Path


UNIT_DIR = Path(__file__).resolve().parents[1]
MANIFEST = UNIT_DIR / "asset_manifest.csv"
REVIEW = UNIT_DIR / "assets" / "generated" / "_review"


def read_rows():
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames, list(reader)


def chart_paths():
    paths = {}
    for metadata_path in (UNIT_DIR / "assets" / "generated" / "charts").glob("*/metadata.json"):
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        svg = next(metadata_path.parent.glob("u02_fig_*.svg"))
        paths[metadata["asset_id"]] = str(svg.relative_to(UNIT_DIR)).replace("\\", "/")
    return paths


def variant_rows(report):
    rows = []
    for asset in report["assets"]:
        classification = asset["classification"]
        manifest_type = {
            "diagrama conceptual": "diagram_conceptual",
            "diagrama de proceso": "diagram_process",
            "ecuación anotada": "annotated_equation",
            "esquema mixto": "mixed_scheme",
        }[classification]
        rows.append(
            {
                "asset_id": asset["asset_id"],
                "unit": "02",
                "slide_id": asset["slide_id"],
                "type": manifest_type,
                "title": asset["title"],
                "description": f"{classification.capitalize()} vectorial diseñado y validado en tamaño final.",
                "pedagogical_purpose": "Implementar la función visual definida en el storyboard y el plan de diagramas.",
                "source_url": "",
                "creator": "Equipo docente",
                "organization": "UCASAL",
                "license": "Elaboración propia",
                "access_date": "2026-07-29",
                "local_path": asset["local_path"],
                "status": "generated_validated",
                "credit_text": "Elaboración propia a partir del libro del curso.",
                "notes": f"Familia {asset['family']}; paquete {asset['package_path']}; SVG y source.json editables; PNG y slide_context validados.",
            }
        )
    return rows


def main():
    fieldnames, rows = read_rows()
    report = json.loads((REVIEW / "u02_diagrams_generation_report.json").read_text(encoding="utf-8"))
    chart_local_paths = chart_paths()
    updated = []
    for row in rows:
        asset_id = row["asset_id"]
        if asset_id.startswith("U02-DG") and "-S" not in asset_id:
            row["status"] = "implemented_as_validated_variants"
            row["local_path"] = "units/unit_02/assets/generated/diagrams"
            row["notes"] = row["notes"].rstrip(".") + "; ver variantes por slide con sufijo -Snnn."
        elif asset_id in chart_local_paths:
            row["status"] = "generated_validated"
            row["local_path"] = chart_local_paths[asset_id]
            row["notes"] = row["notes"].rstrip(".") + "; paquete reproducible con CSV, SVG, PNG, README, caption, alt text y fuente."
        elif asset_id == "U02-CH005":
            row["status"] = "replaced_by_table"
            row["local_path"] = "units/unit_02/assets/generated/charts/u02_ch004_velocidad_temperatura/metadata.json"
            row["notes"] = "Reemplazado por tabla y dos trayectos; cálculo de control conservado en U02-CH004."
        updated.append(row)
    updated.extend(variant_rows(report))
    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(updated)
    print(json.dumps({"rows": len(updated), "diagram_variants": len(report["assets"]), "charts": len(chart_local_paths)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
