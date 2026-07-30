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
    force = np.arange(0.0, 4.0 + 1.0, 1.0)
    a_1 = force / 1.0
    a_2 = force / 2.0
    fig, ax = base_axes()
    ax.plot(force, a_1, color=COLORS["fisico"], linewidth=3.2, marker="o", markersize=8)
    ax.plot(
        force,
        a_2,
        color=COLORS["bordo"],
        linewidth=3.2,
        linestyle="--",
        marker="s",
        markersize=7,
    )
    ax.set_xlim(0, 4.15)
    ax.set_ylim(0, 4.5)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xlabel(r"Fuerza neta, $F_{\mathrm{neta}}$ (N)", labelpad=12)
    ax.set_ylabel(r"Aceleración, $a$ (m/s$^2$)", labelpad=12)
    ax.annotate(
        "m = 1,0 kg\npendiente = 1/m",
        xy=(3.25, 3.25),
        xytext=(2.45, 3.88),
        fontsize=22,
        color=COLORS["fisico"],
        arrowprops=dict(arrowstyle="-", color=COLORS["fisico"], lw=1.5),
    )
    ax.annotate(
        "m = 2,0 kg\npendiente = 1/m",
        xy=(3.35, 1.675),
        xytext=(2.58, 0.42),
        fontsize=22,
        color=COLORS["bordo"],
        arrowprops=dict(arrowstyle="-", color=COLORS["bordo"], lw=1.5),
        bbox=dict(facecolor="white", edgecolor="none", pad=2),
    )
    ax.scatter([2, 2], [2, 1], s=135, facecolor="white", edgecolor=COLORS["carbon"], zorder=5)
    ax.text(1.86, 2.12, "2,0 m/s²", fontsize=20, ha="right", va="bottom")
    ax.text(1.86, 0.45, "1,0 m/s²", fontsize=20, ha="right", va="center")
    ax.xaxis.set_major_formatter(comma_formatter())
    ax.yaxis.set_major_formatter(comma_formatter())
    finish_axes(ax)
    rows = [
        {
            "fuerza_neta_N": f"{f:.1f}",
            "aceleracion_m1_kg_m_s2": f"{v1:.1f}",
            "aceleracion_m2_kg_m_s2": f"{v2:.1f}",
        }
        for f, v1, v2 in zip(force, a_1, a_2)
    ]
    return export_chart(
        fig=fig,
        chart_id="U02-CH001",
        number=1,
        slug="aceleracion_fuerza",
        rows=rows,
        fieldnames=list(rows[0]),
        title="Aceleración frente a fuerza neta",
        slides="U02-018; U02-036",
        question="¿Cómo cambia la aceleración al aumentar la fuerza neta y qué cambia al duplicar la masa?",
        caption="Modelo exacto a = F_neta/m: con la misma fuerza neta, la masa de 2,0 kg acelera la mitad que la de 1,0 kg.",
        alt_text="Gráfico lineal de aceleración frente a fuerza neta para masas de uno y dos kilogramos. Ambas rectas parten del origen; la masa menor tiene el doble de pendiente.",
        source="Valores calculados exactamente con a = F_neta/m; no son mediciones.",
        scale="Ambos ejes lineales. F_neta de 0 a 4 N; a de 0 a 4,5 m/s².",
        validation=[
            "Ambas rectas pasan por el origen.",
            "Para F_neta = 2 N se verifican 2,0 m/s² y 1,0 m/s².",
            "La codificación combina color, trazo y marcador.",
        ],
        wrapper_name="u02_plot_001_aceleracion_fuerza.py",
        extra={"masses_kg": [1.0, 2.0], "max_absolute_error": 0.0},
    )


if __name__ == "__main__":
    generate()
