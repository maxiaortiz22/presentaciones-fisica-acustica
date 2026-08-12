#!/usr/bin/env python3
"""Recorta el área útil de diagramas U08 sin alterar sus fuentes maestras."""

from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "units" / "unit_08" / "assets" / "generated" / "diagrams"
OUTPUT = ROOT / "units" / "unit_08" / ".tmp_pptx_build" / "diagram_crops"


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for folder in sorted(SOURCE.glob("U08-DG-*")):
        candidates = [p for p in folder.glob("*.png") if "preview" not in p.name.lower() and "layout" not in p.name.lower()]
        if not candidates:
            continue
        with Image.open(candidates[0]) as image:
            width, height = image.size
            # Los maestros 16:9 incluyen rail, título y disclaimer. Se conserva
            # únicamente el área central validada del diagrama.
            box = (round(width * 0.0625), round(height * 0.18), round(width * 0.9375), round(height * 0.845))
            cropped = image.crop(box)
            draw = ImageDraw.Draw(cropped)
            if folder.name == "U08-DG-001":
                draw.rectangle((0, 0, round(cropped.width * 0.33), round(cropped.height * 0.13)), fill="white")
            else:
                draw.rectangle((0, 0, cropped.width, round(cropped.height * 0.115)), fill="white")
            draw.rectangle((0, round(cropped.height * 0.92), cropped.width, cropped.height), fill="white")
            cropped.save(OUTPUT / f"{folder.name}.png", optimize=True)
        count += 1
    print(f"Diagramas preparados: {count}")


if __name__ == "__main__":
    main()
