from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if SCRIPT_DIR.name != "scripts":
    UNIT_DIR = next(parent for parent in Path(__file__).resolve().parents if parent.name == "unit_02")
    SCRIPT_DIR = UNIT_DIR / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from u02_chart_style import COLORS, base_axes, comma_formatter, export_chart, finish_axes


def generate():
    k_s = 20.0
    x_mm = np.arange(-20.0, 20.0 + 5.0, 5.0)
    force = -k_s * x_mm / 1000.0
    fig, ax = base_axes()
    ax.axhline(0, color=COLORS["gris"], linewidth=1.2)
    ax.axvline(0, color=COLORS["gris"], linewidth=1.2)
    ax.plot(x_mm, force, color=COLORS["fisico"], linewidth=3.2, marker="o", markersize=7)
    ax.set_xlim(-21, 21)
    ax.set_ylim(-0.45, 0.45)
    ax.set_xticks([-20, -10, 0, 10, 20])
    ax.set_yticks([-0.4, -0.2, 0, 0.2, 0.4])
    ax.set_xlabel(r"Desplazamiento, $x$ (mm)", labelpad=12)
    ax.set_ylabel(r"Fuerza elástica, $F_{\mathrm{el}}$ (N)", labelpad=12)
    ax.text(1.2, 0.035, "equilibrio", fontsize=20, color=COLORS["carbon"])
    ax.annotate(
        "x = +20 mm\nF_el = −0,40 N",
        xy=(20, -0.4),
        xytext=(4.5, -0.22),
        fontsize=21,
        ha="left",
        arrowprops=dict(arrowstyle="-", color=COLORS["carbon"], lw=1.5),
        bbox=dict(facecolor="white", edgecolor="none", pad=2),
    )
    ax.annotate(
        "x = −20 mm\nF_el = +0,40 N",
        xy=(-20, 0.4),
        xytext=(-7.5, 0.20),
        fontsize=21,
        ha="right",
        arrowprops=dict(arrowstyle="-", color=COLORS["carbon"], lw=1.5),
        bbox=dict(facecolor="white", edgecolor="none", pad=2),
    )
    ax.text(0.97, 0.96, "Modelo lineal ideal · kₛ = 20 N/m", transform=ax.transAxes, ha="right", va="top", fontsize=20)
    ax.xaxis.set_major_formatter(comma_formatter())
    ax.yaxis.set_major_formatter(comma_formatter(1))
    finish_axes(ax)
    rows = [{"desplazamiento_mm": f"{x:.1f}", "fuerza_elastica_N": f"{f:.3f}"} for x, f in zip(x_mm, force)]
    return export_chart(
        fig=fig,
        chart_id="U02-CH002",
        number=2,
        slug="fuerza_elastica",
        rows=rows,
        fieldnames=list(rows[0]),
        title="Fuerza elástica frente a desplazamiento",
        slides="U02-038",
        question="¿Por qué la fuerza elástica apunta hacia el equilibrio y qué representa la pendiente?",
        caption="En el modelo lineal, la fuerza elástica cambia de signo con el desplazamiento y apunta al equilibrio.",
        alt_text="Recta descendente de fuerza elástica frente a desplazamiento. Cruza el origen y alcanza más o menos 0,40 newtons en desplazamientos de menos o más 20 milímetros.",
        source="Valores calculados con F_el = −k_s x, k_s = 20 N/m; modelo lineal ideal, no mediciones de tejido.",
        scale="Ambos ejes lineales y simétricos; x en milímetros y F_el en newtons.",
        validation=[
            "Conversión explícita de milímetros a metros en el cálculo.",
            "Pendiente negativa igual a −20 N/m.",
            "Fuerza y desplazamiento tienen signos opuestos.",
        ],
        wrapper_name="u02_plot_002_fuerza_elastica.py",
        extra={"k_s_N_m": k_s, "endpoint_force_N": 0.4},
    )


if __name__ == "__main__":
    generate()
