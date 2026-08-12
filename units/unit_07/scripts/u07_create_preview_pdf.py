from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfReader
from reportlab.pdfgen import canvas


def slide_number(path: Path) -> int:
    match = re.search(r"(\d+)$", path.stem)
    if not match:
        raise ValueError(f"Nombre de render sin número: {path.name}")
    return int(match.group(1))


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Uso: u07_create_preview_pdf.py <render_dir> <output.pdf>")
    render_dir = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    images = sorted(render_dir.glob("*.png"), key=slide_number)
    if len(images) != 134:
        raise ValueError(f"Se esperaban 134 renders y se encontraron {len(images)}")

    output.parent.mkdir(parents=True, exist_ok=True)
    page_size = (13.333333 * 72, 7.5 * 72)
    pdf = canvas.Canvas(str(output), pagesize=page_size, pageCompression=1)
    pdf.setTitle("Unidad 7 - Psicoacustica - vista previa")
    pdf.setAuthor("UCASAL - Fisica Acustica")
    for image in images:
        pdf.drawImage(str(image), 0, 0, width=page_size[0], height=page_size[1], preserveAspectRatio=True)
        pdf.showPage()
    pdf.save()

    reader = PdfReader(str(output))
    if len(reader.pages) != 134:
        raise ValueError(f"PDF incompleto: {len(reader.pages)} páginas")
    print(f"PDF verificado: {output} ({len(reader.pages)} páginas)")


if __name__ == "__main__":
    main()
