from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from u02_chart_style import OUTPUT_ROOT, REVIEW_DIR


MODULES = [
    "u02_plot_001_aceleracion_fuerza",
    "u02_plot_002_fuerza_elastica",
    "u02_plot_003_fuerza_amortiguamiento",
    "u02_plot_004_velocidad_temperatura",
]


def contact_sheet(pngs: list[Path]):
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", (2400, 1350), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype("arial.ttf", 28)
    for index, path in enumerate(pngs):
        image = Image.open(path).convert("RGB")
        image.thumbnail((1120, 515))
        x = 80 + (index % 2) * 1200
        y = 90 + (index // 2) * 620
        canvas.paste(image, (x, y))
        draw.text((x, y - 42), path.parent.name, fill="#3D3D3D", font=font)
    out = REVIEW_DIR / "u02_charts_contact_sheet.png"
    canvas.save(out)
    return out


def main():
    results = []
    for module_name in MODULES:
        module = importlib.import_module(module_name)
        results.append(module.generate())
    pngs = sorted(OUTPUT_ROOT.glob("*/u02_fig_*.png"))
    sheet = contact_sheet(pngs)
    report = {
        "generated": len(results),
        "expected": 4,
        "assets": results,
        "contact_sheet": str(sheet.relative_to(OUTPUT_ROOT.parents[1])),
    }
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    (REVIEW_DIR / "u02_charts_generation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"generated": len(results), "contact_sheet": str(sheet)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
