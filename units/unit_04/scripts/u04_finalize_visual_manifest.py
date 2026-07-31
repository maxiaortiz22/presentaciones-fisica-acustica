"""Actualiza rutas y estados de recursos visuales propios en asset_manifest.csv."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "asset_manifest.csv"

CHART_PRIMARY = {
    "U04-CH-001": "u04_fig_001_presion_total_acustica.svg",
    "U04-CH-002": "u04_fig_002_presion_velocidad_intensidad.svg",
    "U04-CH-003": "u04_fig_003_6_media.svg",
    "U04-CH-004": "u04_fig_004_media_cero.svg",
    "U04-CH-005": "u04_fig_005_construccion_rms.svg",
    "U04-CH-006": "u04_fig_006_igual_rms.svg",
    "U04-CH-007": "u04_fig_007_presion_nivel_horizontal.svg",
    "U04-CH-008": "u04_fig_008_resumen_fases.svg",
    "U04-CH-009": "u04_fig_009_zoom_25ms.svg",
    "U04-CH-010": "u04_fig_010_geometrias_loglog.svg",
    "U04-CH-011": "u04_fig_011_nivel_distancia.svg",
    "U04-CH-013": "u04_fig_013_reflexion_impedancias.svg",
    "U04-CH-014": "u04_fig_014_incremento_suma_niveles.svg",
    "U04-CH-015": "u04_fig_015_suma_cuadratura.svg",
}

DIAGRAM_SLUGS = {
    1: (16, "situacion_inicial"), 2: (17, "mapa_unidad"), 3: (18, "cadena_acustica"),
    4: (19, "generacion"), 5: (20, "propagacion_longitudinal"), 6: (21, "rapidez_medio"),
    7: (22, "campo_magnitudes"), 8: (23, "impedancia_reflexion"), 9: (24, "intensidad_ecuaciones"),
    10: (25, "flujo_energia_medicion"), 11: (26, "descriptores_callouts"), 12: (27, "proceso_rms"),
    13: (28, "niveles_referencias"), 14: (29, "logica_suma"), 15: (30, "geometrias_campos"),
    16: (31, "ley_distancia"), 17: (32, "directividad"), 18: (33, "caso_integrador"),
    19: (34, "errores"), 20: (35, "distancia_directividad"), 21: (36, "microvisuales"),
    22: (37, "ejemplos_ecuaciones"),
}


def main() -> None:
    with MANIFEST.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0])
    for row in rows:
        aid = row["asset_id"]
        if aid in CHART_PRIMARY:
            row["local_path"] = f"units/unit_04/assets/generated/charts/{aid}/{CHART_PRIMARY[aid]}"
            row["status"] = "approved"
            base_note = row["notes"].split(" SVG/PNG")[0].strip()
            row["notes"] = (base_note + " SVG/PNG, datos, README y validación disponibles en la carpeta del recurso.").strip()
        elif aid == "U04-CH-012":
            row["local_path"] = ""
            row["status"] = "pending_approval"
            row["notes"] = "No generado: los archivos útiles del dataset pesan 326–466 MB y el plan exige autorización previa. No se sustituyó por datos fabricados."
        elif aid.startswith("U04-DG-"):
            n = int(aid[-3:]); fig, slug = DIAGRAM_SLUGS[n]
            row["local_path"] = f"units/unit_04/assets/generated/diagrams/{aid}/u04_fig_{fig:03d}_{slug}.svg"
            row["status"] = "approved"
            row["notes"] = f"Editable nativo en u04_fig_{fig:03d}_{slug}_editable.pptx; PNG, SVG, README y validation.json disponibles."
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    main()
