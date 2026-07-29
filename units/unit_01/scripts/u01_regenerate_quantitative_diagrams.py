from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


UNIT_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = UNIT_DIR / "assets" / "generated" / "diagram_fix"

COLORS = {
    "bordo": "#4D1434",
    "bordo_2": "#903163",
    "carbon": "#3D3D3D",
    "gris": "#76818A",
    "gris_2": "#D9DCE0",
    "fisico": "#2F7E83",
    "clinico": "#9F541A",
    "white": "#FFFFFF",
}

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Calibri", "Arial", "DejaVu Sans"],
        "font.size": 22,
        "axes.labelsize": 22,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "legend.fontsize": 20,
        "text.color": COLORS["carbon"],
        "axes.edgecolor": COLORS["carbon"],
        "axes.labelcolor": COLORS["carbon"],
        "xtick.color": COLORS["carbon"],
        "ytick.color": COLORS["carbon"],
        "svg.fonttype": "none",
    }
)


def _save(fig: plt.Figure, stem: str, width_px: int, height_px: int) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.set_size_inches(width_px / 96, height_px / 96)
    fig.savefig(
        OUT_DIR / f"{stem}.svg",
        format="svg",
        facecolor="white",
        dpi=96,
        bbox_inches=None,
    )
    fig.savefig(
        OUT_DIR / f"{stem}.png",
        format="png",
        facecolor="white",
        dpi=96,
        bbox_inches=None,
    )
    plt.close(fig)


def chart_015() -> None:
    t = np.arange(0, 6, dtype=float)
    d = 4.0 * t
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(t, d, color=COLORS["fisico"], linewidth=4, marker="o", markersize=10)
    ax.set_xlabel("tiempo, t (s)")
    ax.set_ylabel("distancia, d (m)")
    ax.set_xlim(0, 5.2)
    ax.set_ylim(0, 21)
    ax.set_xticks(np.arange(0, 6, 1))
    ax.set_yticks(np.arange(0, 21, 4))
    ax.grid(True, color=COLORS["gris_2"], linewidth=1)
    ax.annotate(
        "pendiente = 4,0 m/s",
        xy=(3, 12),
        xytext=(1.2, 17.5),
        arrowprops={"arrowstyle": "->", "color": COLORS["bordo_2"], "linewidth": 2},
        color=COLORS["bordo_2"],
        fontsize=20,
    )
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    _save(fig, "u01_fig_015_funcion_distancia_diagram_fix", 700, 394)


def chart_019() -> None:
    theta = np.deg2rad(45)
    x, y = np.cos(theta), np.sin(theta)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.set_aspect("equal")
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color=COLORS["fisico"], linewidth=4))
    ax.axhline(0, color=COLORS["gris"], linewidth=1.5)
    ax.axvline(0, color=COLORS["gris"], linewidth=1.5)
    ax.plot([0, x], [0, y], color=COLORS["bordo_2"], linewidth=4)
    ax.plot([x, x], [0, y], color=COLORS["clinico"], linewidth=2.5, linestyle="--")
    ax.plot([0, x], [y, y], color=COLORS["fisico"], linewidth=2.5, linestyle="--")
    ax.text(0.26, 0.10, "θ", fontsize=26, color=COLORS["bordo"])
    ax.text(x / 2, y + 0.10, "radio = 1", ha="center", fontsize=20)
    ax.text(x / 2, y - 0.16, "cos θ", ha="center", fontsize=22, color=COLORS["fisico"])
    ax.text(x + 0.12, y / 2, "sin θ", fontsize=22, color=COLORS["clinico"])
    ax.text(1.15, -1.06, "360° = 2π rad", ha="center", fontsize=22, color=COLORS["bordo"])
    ax.set_xlim(-1.25, 1.55)
    ax.set_ylim(-1.18, 1.18)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel("coordenada horizontal")
    ax.set_ylabel("coordenada vertical")
    ax.grid(True, color=COLORS["gris_2"], linewidth=0.8)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    _save(fig, "u01_fig_019_circulo_unitario_diagram_fix", 700, 394)


def chart_020() -> None:
    x_exp = np.linspace(-1.2, 0.4, 400)
    y_exp = 10**x_exp
    x_log = np.linspace(0.06, 2.4, 400)
    y_log = np.log10(x_log)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(x_exp, y_exp, color=COLORS["fisico"], linewidth=4, label="y = 10ˣ")
    ax.plot(x_log, y_log, color=COLORS["clinico"], linewidth=4, label="y = log₁₀(x)")
    ax.plot([-1.2, 2.4], [-1.2, 2.4], color=COLORS["gris"], linewidth=2, linestyle="--", label="y = x")
    ax.scatter([0, 1], [1, 0], s=90, color=[COLORS["fisico"], COLORS["clinico"]], zorder=5)
    ax.axhline(0, color=COLORS["carbon"], linewidth=1.3)
    ax.axvline(0, color=COLORS["carbon"], linewidth=1.3)
    ax.set_xlim(-1.2, 2.4)
    ax.set_ylim(-1.2, 2.4)
    ax.set_xlabel("entrada, x (adimensional)")
    ax.set_ylabel("salida, y (adimensional)")
    ax.grid(True, color=COLORS["gris_2"], linewidth=0.8)
    ax.legend(frameon=False, loc="upper left")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    _save(fig, "u01_fig_020_exponencial_log_diagram_fix", 700, 394)


def chart_021() -> None:
    vals = np.array([1, 10, 100, 1000], dtype=float)
    fig, axes = plt.subplots(2, 1, constrained_layout=True)
    for ax, scale, color, title in [
        (axes[0], "linear", COLORS["fisico"], "ESCALA LINEAL"),
        (axes[1], "log", COLORS["clinico"], "ESCALA LOGARÍTMICA"),
    ]:
        if scale == "log":
            ax.set_xscale("log")
            ax.set_xlim(1, 1000)
        else:
            ax.set_xlim(0, 1000)
        ax.set_ylim(-0.2, 0.2)
        ax.hlines(0, ax.get_xlim()[0], ax.get_xlim()[1], color=COLORS["carbon"], linewidth=2)
        ax.scatter(vals, np.zeros_like(vals), s=130, color=color, zorder=3)
        for value in vals:
            ax.text(value, 0.065, f"{int(value)}", ha="center", fontsize=20)
        ax.set_title(title, loc="left", fontsize=22, color=COLORS["bordo"], weight="bold")
        ax.set_yticks([])
        ax.set_xticks(vals, labels=["1", "10", "100", "1000"])
        ax.grid(axis="x", color=COLORS["gris_2"], linewidth=0.8)
        for spine in ["top", "left", "right"]:
            ax.spines[spine].set_visible(False)
    axes[0].set_xlabel("razón Q/Q₀ · diferencias iguales")
    axes[1].set_xlabel("razón Q/Q₀ · razones iguales")
    _save(fig, "u01_fig_021_escalas_lineal_log_diagram_fix", 810, 456)


def chart_022() -> None:
    ratio = np.array([1, 10, 100, 1000], dtype=float)
    level = 10 * np.log10(ratio)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.set_xscale("log")
    ax.plot(ratio, level, color=COLORS["fisico"], linewidth=4, marker="o", markersize=10)
    for r, value in zip(ratio, level):
        ax.annotate(
            f"{int(r)} → {int(value)} dB",
            (r, value),
            xytext=(0, 14),
            textcoords="offset points",
            ha="center",
            fontsize=18,
            color=COLORS["bordo"],
        )
    ax.set_xlim(0.8, 1300)
    ax.set_ylim(-2, 34)
    ax.set_xticks(ratio, labels=["1", "10", "100", "1000"])
    ax.set_yticks([0, 10, 20, 30])
    ax.set_xlabel("razón Q/Q₀ (adimensional)")
    ax.set_ylabel("nivel LQ (dB)")
    ax.grid(True, color=COLORS["gris_2"], linewidth=0.8)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    _save(fig, "u01_fig_022_razon_db_diagram_fix", 620, 349)


def chart_026() -> None:
    freqs = np.array([250, 500, 1000, 1500, 2000, 3000])
    spectra = [
        ("ESPECTRO A", np.array([1.00, 0.72, 0.48, 0.30, 0.18, 0.10]), COLORS["fisico"]),
        ("ESPECTRO B", np.array([0.32, 0.48, 1.00, 0.58, 0.42, 0.22]), COLORS["clinico"]),
    ]
    fig, axes = plt.subplots(2, 1, sharex=True, constrained_layout=True)
    for ax, (label, amps, color) in zip(axes, spectra):
        markerline, stemlines, _ = ax.stem(freqs, amps, basefmt=" ")
        plt.setp(stemlines, color=color, linewidth=4)
        plt.setp(markerline, marker="o", markersize=9, markerfacecolor=color, markeredgecolor=color)
        ax.set_ylim(0, 1.12)
        ax.set_xlim(0, 4000)
        ax.set_ylabel("amplitud\nrelativa")
        ax.grid(axis="y", color=COLORS["gris_2"], linewidth=0.8)
        ax.text(0.02, 0.82, label, transform=ax.transAxes, fontsize=22, color=COLORS["bordo"], weight="bold")
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
    axes[1].set_xlabel("frecuencia (Hz) · escala lineal")
    axes[1].set_xticks(np.arange(0, 4001, 1000))
    _save(fig, "u01_fig_026_espectros_conceptuales_diagram_fix", 810, 456)


def animation_002() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.5, 3.55), dpi=96, facecolor="white")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.9, 0.9)
    ax.axis("off")
    equilibrium = np.linspace(0.4, 9.6, 28)
    marked = int(np.argmin(np.abs(equilibrium - 5.0)))
    scatter = ax.scatter(equilibrium, np.zeros_like(equilibrium), s=150, color=COLORS["fisico"], edgecolors="white")
    marked_scatter = ax.scatter([equilibrium[marked]], [0], s=260, color=COLORS["bordo_2"], edgecolors="white", zorder=4)
    ax.hlines(0, 0.3, 9.7, color=COLORS["gris_2"], linewidth=2, linestyle="--")
    front = ax.axvline(1, ymin=0.30, ymax=0.70, color=COLORS["fisico"], linewidth=5, alpha=0.35)
    ax.text(0.4, 0.62, "zona de compresión", fontsize=22, color=COLORS["fisico"])
    ax.text(9.6, -0.68, "partícula marcada", ha="right", fontsize=22, color=COLORS["bordo_2"])
    centers = np.linspace(-0.5, 10.5, 48)

    def update(index: int):
        center = centers[index]
        displacement = 0.22 * np.exp(-((equilibrium - center) / 0.70) ** 2)
        positions = equilibrium + displacement
        scatter.set_offsets(np.column_stack([positions, np.zeros_like(positions)]))
        marked_scatter.set_offsets(np.array([[positions[marked], 0]]))
        front.set_xdata([center, center])
        return scatter, marked_scatter, front

    animation = FuncAnimation(fig, update, frames=len(centers), interval=120, blit=True)
    animation.save(
        OUT_DIR / "u01_media_002_propagacion_particulas_diagram_fix.gif",
        writer=PillowWriter(fps=8),
    )
    update(24)
    fig.savefig(
        OUT_DIR / "u01_fig_002_propagacion_particulas_diagram_fix.png",
        dpi=96,
        facecolor="white",
    )
    plt.close(fig)


def main() -> None:
    chart_015()
    chart_019()
    chart_020()
    chart_021()
    chart_022()
    chart_026()
    animation_002()
    print(f"Recursos regenerados en {OUT_DIR}")


if __name__ == "__main__":
    main()
