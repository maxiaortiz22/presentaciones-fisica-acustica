from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


UNIT_DIR = Path(__file__).resolve().parents[1]
SCRIPT_DIR = UNIT_DIR / "scripts"
OUTPUT_ROOT = UNIT_DIR / "assets" / "generated" / "charts"
REVIEW_DIR = UNIT_DIR / "assets" / "generated" / "_review"

COLORS = {
    "bordo": "#4D1434",
    "bordo_2": "#903163",
    "carbon": "#3D3D3D",
    "gris": "#969FA7",
    "gris_2": "#D9DCE0",
    "marfil": "#F7F6F2",
    "fisico": "#2F7E83",
    "fisico_bg": "#E7F1F1",
    "clinico": "#9F541A",
    "alerta": "#9A641E",
    "white": "#FFFFFF",
}

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Calibri", "Arial", "DejaVu Sans"],
        "font.size": 18,
        "axes.labelsize": 20,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "text.color": COLORS["carbon"],
        "axes.edgecolor": COLORS["carbon"],
        "axes.labelcolor": COLORS["carbon"],
        "xtick.color": COLORS["carbon"],
        "ytick.color": COLORS["carbon"],
        "svg.fonttype": "none",
        "figure.dpi": 200,
        "savefig.dpi": 200,
    }
)


def comma_formatter(decimals: int = 1):
    def _format(value, _position):
        if abs(value - round(value)) < 1e-9:
            return f"{int(round(value))}"
        return f"{value:.{decimals}f}".replace(".", ",")

    return FuncFormatter(_format)


def base_axes(figsize=(12, 5.5)):
    fig, ax = plt.subplots(figsize=figsize, facecolor=COLORS["white"])
    # Deja espacio para rótulos verticales largos en el render de aula.
    fig.subplots_adjust(left=0.19, right=0.975, bottom=0.23, top=0.95)
    ax.set_facecolor(COLORS["white"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.2)
    ax.spines["bottom"].set_linewidth(1.2)
    ax.grid(True, color=COLORS["gris_2"], linewidth=0.8, alpha=0.75)
    ax.set_axisbelow(True)
    return fig, ax


def package_dir(chart_id: str, slug: str) -> Path:
    folder = OUTPUT_ROOT / f"{chart_id.lower().replace('-', '_')}_{slug}"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def export_chart(
    *,
    fig,
    chart_id: str,
    number: int,
    slug: str,
    rows: list[dict],
    fieldnames: list[str],
    title: str,
    slides: str,
    question: str,
    caption: str,
    alt_text: str,
    source: str,
    scale: str,
    validation: list[str],
    wrapper_name: str,
    extra: dict | None = None,
):
    folder = package_dir(chart_id, slug)
    stem = f"u02_fig_{number:03d}_{slug}"
    svg_path = folder / f"{stem}.svg"
    png_path = folder / f"{stem}.png"
    csv_path = folder / "data.csv"
    fig.savefig(svg_path, format="svg", facecolor=COLORS["white"])
    fig.savefig(png_path, format="png", facecolor=COLORS["white"], dpi=200)
    plt.close(fig)
    write_csv(csv_path, fieldnames, rows)

    shutil.copy2(SCRIPT_DIR / wrapper_name, folder / "script.py")
    (folder / "caption.txt").write_text(caption + "\n", encoding="utf-8")
    (folder / "alt_text.txt").write_text(alt_text + "\n", encoding="utf-8")
    (folder / "source.txt").write_text(source + "\n", encoding="utf-8")
    metadata = {
        "asset_id": chart_id,
        "classification": "gráfico cuantitativo",
        "title": title,
        "slides": slides,
        "question": question,
        "scale": scale,
        "source": source,
        "validation": validation,
        "outputs": {
            "svg": svg_path.name,
            "png": png_path.name,
            "data": csv_path.name,
            "script": "script.py",
        },
    }
    if extra:
        metadata["parameters_and_checks"] = extra
    (folder / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    readme = f"""# {chart_id} — {title}

**Clasificación obligatoria:** gráfico cuantitativo.

## Pregunta pedagógica

{question}

## Datos y modelo

{source}

## Escala

{scale}

## Archivos

- `script.py`: regeneración reproducible desde la raíz del repositorio.
- `data.csv`: valores exactos usados por el gráfico.
- `{stem}.svg`: salida vectorial principal.
- `{stem}.png`: respaldo de 2400 × 1100 px.
- `caption.txt`, `alt_text.txt` y `source.txt`: textos de montaje y accesibilidad.
- `metadata.json`: parámetros y verificaciones.

## Caption sugerido

{caption}

## Validación

{chr(10).join(f"- {item}" for item in validation)}
"""
    (folder / "README.md").write_text(readme, encoding="utf-8")
    return metadata


def finish_axes(ax):
    ax.tick_params(axis="both", which="major", length=5, width=1)
    ax.margins(x=0.02, y=0.04)
