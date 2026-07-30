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
    b = 2.0
    velocity = np.arange(-0.20, 0.20 + 0.05, 0.05)
    force = -b * velocity
    fig, ax = base_axes()
    ax.axhline(0, color=COLORS["gris"], linewidth=1.2)
    ax.axvline(0, color=COLORS["gris"], linewidth=1.2)
    ax.plot(
        velocity,
        force,
        color=COLORS["bordo"],
        linewidth=3.2,
        linestyle="--",
        marker="s",
        markersize=7,
    )
    ax.set_xlim(-0.21, 0.21)
    ax.set_ylim(-0.45, 0.45)
    ax.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
    ax.set_yticks([-0.4, -0.2, 0, 0.2, 0.4])
    ax.set_xlabel(r"Velocidad, $v$ (m/s)", labelpad=12)
    ax.set_ylabel(r"Fuerza de amortiguamiento, $F_{\mathrm{amort}}$ (N)", labelpad=12)
    ax.annotate(
        "v = +0,20 m/s\nF_amort = −0,40 N",
        xy=(0.2, -0.4),
        xytext=(0.020, -0.18),
        fontsize=21,
        arrowprops=dict(arrowstyle="-", color=COLORS["carbon"], lw=1.5),
        bbox=dict(facecolor="white", edgecolor="none", pad=2),
    )
    ax.text(-0.195, -0.31, "Se opone a v", fontsize=22, color=COLORS["bordo"])
    ax.text(0.97, 0.96, "Modelo viscoso lineal · b = 2,0 N·s/m", transform=ax.transAxes, ha="right", va="top", fontsize=20)
    ax.xaxis.set_major_formatter(comma_formatter(2))
    ax.yaxis.set_major_formatter(comma_formatter(1))
    finish_axes(ax)
    rows = [{"velocidad_m_s": f"{v:.2f}", "fuerza_amortiguamiento_N": f"{f:.3f}"} for v, f in zip(velocity, force)]
    return export_chart(
        fig=fig,
        chart_id="U02-CH003",
        number=3,
        slug="fuerza_amortiguamiento",
        rows=rows,
        fieldnames=list(rows[0]),
        title="Fuerza de amortiguamiento frente a velocidad",
        slides="U02-040",
        question="¿Cómo depende la fuerza de amortiguamiento de la velocidad?",
        caption="El modelo viscoso lineal produce una fuerza proporcional y opuesta a la velocidad.",
        alt_text="Recta descendente de fuerza de amortiguamiento frente a velocidad. Cruza el origen y llega a menos 0,40 newtons cuando la velocidad es más 0,20 metros por segundo.",
        source="Valores calculados con F_amort = −b v, b = 2,0 N·s/m; modelo viscoso lineal, no ley universal de tejidos.",
        scale="Ambos ejes lineales y simétricos; v en m/s y F_amort en N.",
        validation=[
            "Pendiente negativa igual a −b.",
            "El producto b·v conserva unidad de newton.",
            "La figura declara el alcance del modelo.",
        ],
        wrapper_name="u02_plot_003_fuerza_amortiguamiento.py",
        extra={"b_N_s_m": b, "endpoint_force_N": -0.4},
    )


if __name__ == "__main__":
    generate()
