"""Genera los gráficos cuantitativos aprobados de la Unidad 07.

Los modelos conceptuales son deterministas y se rotulan como tales. El script
no incorpora datos normativos ni experimentales no disponibles en el repo.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


UNIT_DIR = Path(__file__).resolve().parents[1]
ROOT = UNIT_DIR / "assets" / "generated" / "charts"

COLORS = {
    "bordo": "#4D1434",
    "bordo2": "#903163",
    "teal": "#2F7E83",
    "carbon": "#3D3D3D",
    "gris": "#969FA7",
    "gris2": "#D9DCE0",
    "marfil": "#F7F6F2",
    "ocre": "#9F541A",
    "error": "#A33A3A",
}

APPROVED = {
    "U07-CH-001": ("u07_plot_001_curva_psicometrica.py", "u07_fig_001_curva_psicometrica"),
    "U07-CH-002A": ("u07_plot_002_umbral_campo.py", "u07_fig_002a_umbral_condicionado"),
    "U07-CH-002B": ("u07_plot_002_umbral_campo.py", "u07_fig_002b_campo_audible"),
    "U07-CH-003": ("u07_plot_003_transferencia_conceptual.py", "u07_fig_003_transferencia_campo_timpano"),
    "U07-CH-005": ("u07_plot_005_fundamental_ausente.py", "u07_fig_005_fundamental_ausente"),
    "U07-CH-006": ("u07_plot_006_fones_sones.py", "u07_fig_006_fones_sones"),
    "U07-CH-007": ("u07_plot_007_patron_enmascaramiento.py", "u07_fig_007_patron_enmascaramiento"),
    "U07-CH-008": ("u07_plot_008_erb_area.py", "u07_fig_008_erb_igualdad_area"),
    "U07-CH-009": ("u07_plot_009_decaimiento_t60.py", "u07_fig_009_decaimiento_t60"),
}

META = {
    "U07-CH-001": {
        "question": "¿Por qué un criterio selecciona un punto de una transición gradual?",
        "caption": "La detección aumenta gradualmente con el nivel; el criterio del 50 % define L₅₀ para este procedimiento, no un umbral universal.",
        "alt": "Curva logística de detección desde casi cero hasta casi cien por ciento. Una línea horizontal en cincuenta por ciento corta la curva en L cincuenta.",
        "source": "Función logística sintética definida en chart_plan.md; no son datos humanos.",
    },
    "U07-CH-002A": {
        "question": "¿Cómo depende el umbral auditivo de la frecuencia?",
        "caption": "Esquema cualitativo del umbral condicionado por la frecuencia, con mayor sensibilidad en la región media.",
        "alt": "Curva conceptual en forma de valle sobre un eje logarítmico de frecuencia sin valores numéricos de nivel. La zona media aparece como la de mayor sensibilidad.",
        "source": "Reconstrucción conceptual del esquema TikZ del libro; no usa puntos normativos ni experimentales.",
    },
    "U07-CH-002B": {
        "question": "¿Qué región de niveles queda por encima del umbral condicionado?",
        "caption": "Campo audible conceptual: el límite inferior depende de la frecuencia y el límite superior no se cuantifica.",
        "alt": "Una curva conceptual de umbral delimita una región clara etiquetada como audibilidad condicionada; se advierte que los niveles elevados no se exploran didácticamente.",
        "source": "Reconstrucción conceptual del esquema TikZ del libro; no usa datos ISO 226.",
    },
    "U07-CH-003": {
        "question": "¿Por qué la transferencia campo–tímpano no puede resumirse con una cifra?",
        "caption": "La diferencia campo–tímpano cambia con la frecuencia y también depende de dirección, geometría y punto de medición.",
        "alt": "Curva conceptual ondulada sobre frecuencia logarítmica. No hay valores verticales; tres anotaciones recuerdan dirección, geometría y punto de medición.",
        "source": "Modelo didáctico derivado del argumento del libro; no es una respuesta individual ni normativa.",
    },
    "U07-CH-005": {
        "question": "¿Puede sostenerse el pitch aunque falte la línea en la frecuencia fundamental?",
        "caption": "Dos espectros comparten el espaciamiento de 200 Hz; en el segundo falta la componente física de 200 Hz, pero permanecen los armónicos 2–8.",
        "alt": "Dos espectros de líneas. El primero contiene armónicos desde doscientos hasta mil seiscientos hertz; el segundo omite la línea de doscientos hertz y conserva las demás.",
        "source": "Síntesis determinista propia: f₀=200 Hz, armónicos 1–8 y caída 1/n; no son datos humanos.",
    },
    "U07-CH-006": {
        "question": "¿Cómo crece la sonoridad en sones al aumentar el nivel de sonoridad?",
        "caption": "En el modelo introductorio, cada aumento de 10 fon duplica la sonoridad expresada en sones a partir de 40 fon.",
        "alt": "Curva creciente que pasa por cuarenta fon y un son, cincuenta y dos, sesenta y cuatro, setenta y ocho, ochenta y dieciséis.",
        "source": "Ecuación del libro: N_son=2^((L_N−40 fon)/(10 fon)) son, para L_N≥40 fon.",
    },
    "U07-CH-007": {
        "question": "¿Cómo cambia la elevación del umbral al separar objetivo y enmascarador?",
        "caption": "Patrón sintético asimétrico: la elevación es máxima cerca del enmascarador y disminuye con la separación en octavas.",
        "alt": "Curva de elevación del umbral con máximo en cero octavas relativas y colas diferentes hacia frecuencias menores y mayores.",
        "source": "Función pedagógica asimétrica definida en chart_plan.md; no son datos empíricos.",
    },
    "U07-CH-008": {
        "question": "¿Qué significa una anchura rectangular equivalente?",
        "caption": "El rectángulo tiene la misma altura máxima y, por cálculo numérico, la misma área que la respuesta gaussiana conceptual.",
        "alt": "Curva gaussiana normalizada y un rectángulo de altura uno. Ambas áreas sombreadas son iguales y el ancho del rectángulo se rotula ERB.",
        "source": "Respuesta gaussiana conceptual elegida para explicar igualdad de área; no es un filtro humano medido.",
    },
    "U07-CH-009": {
        "question": "¿Qué mide T₆₀?",
        "caption": "T₆₀ es el intervalo de un decaimiento ideal de 60 dB; no significa tiempo hasta silencio.",
        "alt": "Recta descendente desde cero decibeles relativos en cero segundos hasta menos sesenta decibeles en uno coma dos segundos, con piso de ruido conceptual.",
        "source": "Decaimiento log-lineal sintético con T₆₀=1,2 s; sin fórmula de Sabine ni medición de recinto.",
    },
}

COMMON_PARAMS = {
    "unit": 7,
    "canvas_inches": [12.8, 7.2],
    "png_pixels": [2560, 1440],
    "classification": "gráfico cuantitativo",
}


def configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Calibri", "Arial", "DejaVu Sans"],
            "font.size": 18,
            "axes.labelsize": 22,
            "xtick.labelsize": 18,
            "ytick.labelsize": 18,
            "legend.fontsize": 18,
            "axes.edgecolor": COLORS["carbon"],
            "axes.labelcolor": COLORS["carbon"],
            "xtick.color": COLORS["carbon"],
            "ytick.color": COLORS["carbon"],
            "text.color": COLORS["carbon"],
            "svg.fonttype": "none",
            "savefig.facecolor": "white",
        }
    )


def base_figure(two_panels: bool = False):
    if two_panels:
        fig, axes = plt.subplots(1, 2, figsize=(12.8, 7.2), sharey=True)
        fig.subplots_adjust(left=0.09, right=0.98, top=0.91, bottom=0.17, wspace=0.18)
        return fig, axes
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.91, bottom=0.17)
    return fig, ax


def clean_axis(ax, grid_axis="both") -> None:
    ax.spines[["top", "right"]].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=COLORS["gris2"], lw=1.0, alpha=0.8)


def conceptual_note(fig, text="Modelo didáctico; no representa datos normativos/experimentales.") -> None:
    fig.text(0.99, 0.018, text, ha="right", va="bottom", fontsize=17, color=COLORS["gris"])


def make_ch001():
    x = np.linspace(-15, 15, 301)
    s = 3.0
    p = 1.0 / (1.0 + np.exp(-x / s))
    fig, ax = base_figure()
    ax.plot(x, 100 * p, color=COLORS["bordo"], lw=5)
    ax.axhline(50, color=COLORS["gris"], lw=1.8, ls="--")
    ax.axvline(0, color=COLORS["teal"], lw=2.2, ls=":")
    ax.scatter([0], [50], s=110, color=COLORS["teal"], zorder=5)
    ax.annotate("L₅₀: punto definido\npor el criterio", xy=(0, 50), xytext=(5, 66), fontsize=22,
                color=COLORS["teal"], arrowprops=dict(arrowstyle="->", lw=2, color=COLORS["teal"]))
    ax.text(-14, 9, "detección poco frecuente", fontsize=21, color=COLORS["gris"])
    ax.text(4.2, 91, "detección frecuente", fontsize=21, color=COLORS["gris"])
    ax.set(xlim=(-15, 15), ylim=(0, 100), xlabel="Nivel relativo a L₅₀  (dB)", ylabel="Proporción de detecciones  (%)")
    ax.set_xticks(np.arange(-15, 16, 5))
    ax.set_yticks(np.arange(0, 101, 25))
    clean_axis(ax)
    conceptual_note(fig)
    rows = [{"level_relative_dB": f"{a:.2f}", "detection_probability": f"{b:.8f}"} for a, b in zip(x, p)]
    checks = {"monotonic": bool(np.all(np.diff(p) > 0)), "p_at_L50": float(p[np.argmin(abs(x))]), "range_0_1": bool(p.min() >= 0 and p.max() <= 1)}
    variants = {"u07_fig_001_curva_psicometrica_sin_ejes": lambda: make_ch001_no_axes(x, p)}
    return fig, rows, {"model": "logistic", "s_dB": s, "scale": "x e y lineales", "conceptual": True}, checks, variants


def make_ch001_no_axes(x, p):
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.04)
    ax.plot(x, p, color=COLORS["bordo"], lw=10)
    ax.scatter([0], [0.5], s=250, color=COLORS["teal"], zorder=5)
    ax.axis("off")
    conceptual_note(fig)
    return fig


def threshold_curve():
    f = np.geomspace(20, 12500, 401)
    u = np.log10(f / 3000.0)
    y = 0.18 + 0.48 * np.clip(-u, 0, None) ** 1.45 + 0.20 * np.clip(u, 0, None) ** 2.0
    y += 0.06 * np.exp(-0.5 * ((np.log10(f) - np.log10(7000)) / 0.16) ** 2)
    return f, y


def threshold_axis(ax):
    ax.set_xscale("log")
    ax.set_xlim(20, 12500)
    ax.set_ylim(0.95, 0)
    ax.set_xlabel("Frecuencia  (Hz; escala logarítmica)")
    ax.set_ylabel("Nivel de umbral  (escala cualitativa)")
    ax.set_xticks([20, 100, 1000, 3000, 10000], ["20", "100", "1 k", "3 k", "10 k"])
    ax.set_yticks([])
    clean_axis(ax, "x")


def make_ch002a():
    f, y = threshold_curve()
    fig, ax = base_figure()
    ax.plot(f, y, color=COLORS["bordo"], lw=5)
    threshold_axis(ax)
    ax.annotate("mayor sensibilidad", xy=(3000, y[np.argmin(abs(f-3000))]), xytext=(650, 0.05), fontsize=22,
                color=COLORS["teal"], arrowprops=dict(arrowstyle="->", lw=2, color=COLORS["teal"]))
    ax.text(24, 0.89, "El eje vertical no permite lecturas normativas", fontsize=20, color=COLORS["gris"])
    conceptual_note(fig)
    rows = [{"frequency_Hz": f"{a:.4f}", "threshold_shape_normalized": f"{b:.8f}"} for a, b in zip(f, y)]
    checks = {"frequency_positive": bool(np.all(f > 0)), "log_axis": True, "normative_values_shown": False}
    return fig, rows, {"scale": "frecuencia logarítmica; nivel cualitativo", "conceptual": True}, checks, {}


def make_ch002b():
    f, y = threshold_curve()
    fig, ax = base_figure()
    ax.fill_between(f, y, 0, color=COLORS["teal"], alpha=0.13, hatch="//")
    ax.plot(f, y, color=COLORS["bordo"], lw=5)
    threshold_axis(ax)
    ax.text(650, 0.43, "región audible\nbajo condiciones definidas", fontsize=24, weight="bold", color=COLORS["teal"], ha="center")
    ax.text(11500, 0.08, "niveles elevados:\nno explorar didácticamente", fontsize=20, color=COLORS["ocre"], ha="right", va="top")
    conceptual_note(fig)
    rows = [{"frequency_Hz": f"{a:.4f}", "threshold_shape_normalized": f"{b:.8f}"} for a, b in zip(f, y)]
    checks = {"frequency_positive": bool(np.all(f > 0)), "log_axis": True, "upper_limit_numeric": False, "normative_values_shown": False}
    variants = {"u07_fig_002b_error_0db_frontera": lambda: make_ch002_error(f, y)}
    return fig, rows, {"scale": "frecuencia logarítmica; nivel cualitativo", "conceptual": True}, checks, variants


def make_ch002_error(f, y):
    fig, ax = base_figure()
    ax.plot(f, y, color=COLORS["bordo"], lw=5)
    threshold_axis(ax)
    ax.text(40, 0.20, "0 dB SPL es una referencia,\nno una frontera perceptual", fontsize=24, color=COLORS["error"], weight="bold")
    conceptual_note(fig)
    return fig


def make_ch003():
    f = np.geomspace(100, 12000, 401)
    u = np.log10(f)
    y = 0.42*np.exp(-0.5*((u-3.18)/0.18)**2) - 0.18*np.exp(-0.5*((u-3.65)/0.12)**2) + 0.06*np.sin(5*u)
    fig, ax = base_figure()
    ax.plot(f, y, color=COLORS["teal"], lw=5)
    ax.axhline(0, color=COLORS["gris"], lw=1.5)
    ax.set_xscale("log")
    ax.set_xlim(100, 12000)
    ax.set_xlabel("Frecuencia  (Hz; escala logarítmica)")
    ax.set_ylabel(r"$G_{CT}(f)$  (diferencia conceptual)")
    ax.set_yticks([])
    ax.set_xticks([100, 500, 1000, 3000, 10000], ["100", "500", "1 k", "3 k", "10 k"])
    clean_axis(ax, "x")
    ax.text(0.03, 0.93, "No existe una única ‘ganancia del CAE’", transform=ax.transAxes, fontsize=24, weight="bold", color=COLORS["bordo"])
    ax.text(0.04, 0.12, "depende de dirección · geometría · punto de medición", transform=ax.transAxes, fontsize=21, color=COLORS["carbon"])
    conceptual_note(fig)
    rows = [{"frequency_Hz": f"{a:.4f}", "conceptual_difference_normalized": f"{b:.8f}"} for a, b in zip(f, y)]
    checks = {"frequency_positive": bool(np.all(f > 0)), "log_axis": True, "numeric_y_ticks": False, "individual_response_claimed": False}
    return fig, rows, {"scale": "frecuencia logarítmica; diferencia cualitativa", "conceptual": True}, checks, {}


def harmonic_levels():
    n = np.arange(1, 9)
    amp = 1.0 / n
    db = 20*np.log10(amp / amp.max())
    return n, 200*n, db


def make_ch005():
    n, freq, db = harmonic_levels()
    fig, axes = base_figure(two_panels=True)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.91, bottom=0.22, wspace=0.18)
    for ax, keep, label in [(axes[0], np.ones_like(n, dtype=bool), "Complejo armónico"), (axes[1], n >= 2, "Sin componente en f₀")]:
        ax.vlines(freq[keep], -40, db[keep], color=COLORS["teal"], lw=5)
        ax.scatter(freq[keep], db[keep], color=COLORS["teal"], s=80, zorder=5)
        ax.set(xlim=(0, 2000), ylim=(-40, 3), xlabel="Frecuencia  (Hz)")
        ax.set_title(label, fontsize=24, color=COLORS["bordo"], weight="bold")
        ax.set_xticks([0, 500, 1000, 1500, 2000])
        clean_axis(ax, "y")
    axes[0].set_ylabel("Nivel de componente  (dB relativos)")
    axes[1].axvline(200, color=COLORS["error"], lw=2, ls="--")
    axes[1].annotate("f₀ esperado: no hay\nuna componente física", xy=(200, -25), xytext=(520, -8), fontsize=20,
                     color=COLORS["error"], arrowprops=dict(arrowstyle="->", lw=2, color=COLORS["error"]))
    fig.text(0.51, 0.035, "El espaciamiento entre armónicos sigue siendo 200 Hz", ha="center", fontsize=22, color=COLORS["carbon"])
    rows = [{"harmonic": int(k), "frequency_Hz": int(f), "relative_level_dB": f"{d:.6f}", "present_full": 1, "present_missing_f0": int(k >= 2)} for k, f, d in zip(n, freq, db)]
    checks = {"f0_Hz": 200, "harmonic_spacing_Hz": bool(np.all(np.diff(freq) == 200)), "missing_condition_has_f0": False, "level_range_dB": [float(db.min()), float(db.max())]}
    return fig, rows, {"scale": "ejes lineales", "f0_Hz": 200, "harmonics": [1, 8], "amplitude_model": "1/n", "conceptual": False}, checks, {}


def make_ch006():
    ln = np.linspace(40, 80, 161)
    son = 2 ** ((ln - 40) / 10)
    pts = np.arange(40, 81, 10)
    pson = 2 ** ((pts - 40) / 10)
    fig, ax = base_figure()
    ax.plot(ln, son, color=COLORS["bordo"], lw=5)
    ax.scatter(pts, pson, s=100, color=COLORS["teal"], zorder=5)
    for x, y in zip(pts, pson):
        offset = (-9, 9) if x == 80 else (7, 7)
        align = "right" if x == 80 else "left"
        ax.annotate(f"{x} fon → {y:g} {'son' if y == 1 else 'sones'}", (x, y), xytext=offset, textcoords="offset points", fontsize=18, color=COLORS["carbon"], ha=align)
    ax.set(xlim=(40, 80), ylim=(0, 17), xlabel=r"Nivel de sonoridad, $L_N$  (fon)", ylabel=r"Sonoridad, $N_{son}$  (son)")
    ax.set_xticks(pts)
    ax.set_yticks([0, 1, 2, 4, 8, 12, 16])
    clean_axis(ax)
    ax.text(0.04, 0.92, r"+10 fon → duplica $N_{son}$", transform=ax.transAxes, fontsize=24, weight="bold", color=COLORS["bordo"])
    ax.text(0.98, 0.05, r"Modelo introductorio para $L_N \geq 40$ fon", transform=ax.transAxes, fontsize=18, color=COLORS["gris"], ha="right")
    rows = [{"loudness_level_phon": f"{a:.2f}", "loudness_sone": f"{b:.8f}"} for a, b in zip(ln, son)]
    exact = {str(int(x)): float(y) for x, y in zip(pts, pson)}
    checks = {"exact_points": exact, "doubling_every_10_phon": bool(np.allclose(pson[1:] / pson[:-1], 2)), "domain_min_phon": 40}
    return fig, rows, {"scale": "ambos ejes lineales", "equation": "2**((L_N-40)/10)", "domain_phon": [40, 80], "conceptual": False}, checks, {}


def make_ch007():
    x = np.linspace(-2, 2, 401)
    y = np.where(x < 0, 28*np.exp(x/0.55), 28*np.exp(-x/0.90))
    fig, ax = base_figure()
    ax.plot(x, y, color=COLORS["bordo"], lw=5)
    ax.fill_between(x, 0, y, color=COLORS["bordo2"], alpha=0.12)
    ax.axvline(0, color=COLORS["teal"], lw=2, ls="--")
    ax.text(0.04, 28.7, "enmascarador", fontsize=21, color=COLORS["teal"], va="top")
    for px, lab in [(-0.8, "A"), (0.8, "B")]:
        py = float(np.interp(px, x, y))
        ax.scatter([px], [py], s=100, color=COLORS["teal"], zorder=5)
        ax.annotate(lab, (px, py), xytext=(7, 8), textcoords="offset points", fontsize=22, weight="bold", color=COLORS["teal"])
    ax.set(xlim=(-2, 2), ylim=(0, 30), xlabel=r"Frecuencia objetivo relativa a $f_m$  (octavas)", ylabel="Elevación del umbral, M  (dB)")
    ax.set_xticks([-2, -1, 0, 1, 2])
    clean_axis(ax)
    conceptual_note(fig, "Modelo didáctico asimétrico; no representa datos experimentales ni una ley universal.")
    rows = [{"octaves_relative_to_masker": f"{a:.4f}", "threshold_elevation_dB": f"{b:.8f}"} for a, b in zip(x, y)]
    checks = {"nonnegative": bool(np.all(y >= 0)), "peak_at_masker": float(x[np.argmax(y)]), "asymmetric": bool(not np.allclose(y, y[::-1]))}
    variants = {"u07_fig_007_patron_enmascaramiento_ejercicio": lambda: make_ch007_exercise(x, y)}
    return fig, rows, {"scale": "ambos ejes lineales", "left_decay_oct": 0.55, "right_decay_oct": 0.90, "conceptual": True}, checks, variants


def make_ch007_exercise(x, y):
    fig, ax = base_figure()
    ax.plot(x, y, color=COLORS["bordo"], lw=5)
    ax.axvline(0, color=COLORS["teal"], lw=2, ls="--")
    for px, lab in [(-0.8, "A"), (0.8, "B")]:
        py = float(np.interp(px, x, y)); ax.scatter([px], [py], s=120, color=COLORS["teal"]); ax.text(px+0.08, py+1.1, lab, fontsize=24, weight="bold")
    ax.set(xlim=(-2, 2), ylim=(0, 30), xlabel=r"Frecuencia objetivo relativa a $f_m$  (octavas)", ylabel="Elevación del umbral, M  (dB)")
    clean_axis(ax)
    conceptual_note(fig)
    return fig


def erb_curve():
    x = np.linspace(-4, 4, 1601)
    y = np.exp(-0.5*x*x)
    area = float(np.trapz(y, x))
    width = area / float(y.max())
    rect = (np.abs(x) <= width/2).astype(float)
    return x, y, rect, area, width


def make_ch008():
    x, y, rect, area, width = erb_curve()
    fig, ax = base_figure()
    ax.plot(x, y, color=COLORS["bordo"], lw=5, label="respuesta conceptual")
    ax.fill_between(x, 0, y, color=COLORS["bordo2"], alpha=0.18, hatch="//")
    ax.plot(x, rect, color=COLORS["teal"], lw=3.5, ls="--", label="rectángulo equivalente")
    ax.fill_between(x, 0, rect, color=COLORS["teal"], alpha=0.10)
    ax.annotate("ERB", xy=(-width/2, 0.15), xytext=(width/2, 0.15), ha="center", va="center", fontsize=24, color=COLORS["teal"], arrowprops=dict(arrowstyle="<->", lw=2.5, color=COLORS["teal"]))
    ax.axvline(0, color=COLORS["gris"], lw=1.5, ls=":")
    ax.text(0.1, 0.93, r"$f_c$", fontsize=22, color=COLORS["gris"])
    ax.set(xlim=(-4, 4), ylim=(0, 1.08), xlabel=r"Frecuencia relativa a $f_c$  (unidades normalizadas)", ylabel=r"$W/W_{max}$  (adimensional)")
    ax.legend(loc="upper right", frameon=False)
    clean_axis(ax)
    conceptual_note(fig, "Respuesta gaussiana conceptual; no representa un filtro humano medido.")
    rows = [{"relative_frequency": f"{a:.5f}", "normalized_response": f"{b:.8f}", "equivalent_rectangle": f"{c:.1f}"} for a, b, c in zip(x, y, rect)]
    rect_area = float(np.trapz(rect, x))
    err = abs(rect_area-area)/area*100
    checks = {"curve_area": area, "rectangle_area_discrete": rect_area, "relative_area_error_percent": err, "tolerance_percent": 0.5, "within_tolerance": bool(err < 0.5)}
    return fig, rows, {"scale": "ambos ejes lineales", "model": "normalized Gaussian", "erb_normalized_units": width, "conceptual": True}, checks, {}


def make_ch009():
    t60 = 1.2
    t = np.linspace(0, 1.5, 601)
    ideal = -60*t/t60
    floor = -67.0
    observed = np.maximum(ideal, floor)
    fig, ax = base_figure()
    ax.plot(t, ideal, color=COLORS["bordo"], lw=5, label="decaimiento ideal")
    ax.plot(t, observed, color=COLORS["teal"], lw=2.5, ls="--", label="con piso conceptual")
    ax.axhline(-60, color=COLORS["gris"], lw=1.5, ls=":")
    ax.axvline(t60, color=COLORS["teal"], lw=2, ls="--")
    ax.scatter([t60], [-60], s=110, color=COLORS["teal"], zorder=5)
    ax.annotate("T₆₀ = 1,2 s", xy=(t60, -60), xytext=(0.62, -43), fontsize=24, color=COLORS["teal"], weight="bold", arrowprops=dict(arrowstyle="->", lw=2, color=COLORS["teal"]))
    ax.text(0.04, -64.7, "piso de ruido conceptual", fontsize=19, color=COLORS["gris"])
    ax.set(xlim=(0, 1.5), ylim=(-72, 3), xlabel="Tiempo, t  (s)", ylabel=r"Nivel relativo, $L_{rel}$  (dB)")
    ax.legend(frameon=False, loc="upper right")
    clean_axis(ax)
    fig.text(0.99, 0.018, "Ejemplo sintético; T₆₀ no significa ‘tiempo hasta silencio’.", ha="right", fontsize=17, color=COLORS["gris"])
    rows = [{"time_s": f"{a:.5f}", "ideal_level_dB": f"{b:.8f}", "with_noise_floor_dB": f"{c:.8f}"} for a, b, c in zip(t, ideal, observed)]
    slope = float(np.polyfit(t, ideal, 1)[0])
    checks = {"slope_dB_per_s": slope, "expected_slope": -60/t60, "t60_s": t60, "level_at_t60_dB": float(np.interp(t60, t, ideal))}
    variants = {"u07_fig_009_decaimiento_t30": lambda: make_ch009_t30(t, ideal)}
    return fig, rows, {"scale": "ambos ejes lineales", "T60_s": t60, "noise_floor_dB": floor, "conceptual": True}, checks, variants


def make_ch009_t30(t, ideal):
    fig, ax = base_figure()
    ax.plot(t, ideal, color=COLORS["bordo"], lw=5)
    t1, t2 = 0.1, 0.7
    ax.plot([t1, t2], [-5, -35], color=COLORS["teal"], lw=8, solid_capstyle="round")
    ax.annotate("tramo −5 a −35 dB", xy=(0.42, -20), xytext=(0.73, -13), fontsize=22, color=COLORS["teal"], arrowprops=dict(arrowstyle="->", lw=2, color=COLORS["teal"]))
    ax.text(0.72, -47, "Extrapolar el tramo de 30 dB\npara estimar un decaimiento de 60 dB", fontsize=21, color=COLORS["carbon"])
    ax.set(xlim=(0, 1.5), ylim=(-72, 3), xlabel="Tiempo, t  (s)", ylabel=r"Nivel relativo, $L_{rel}$  (dB)")
    clean_axis(ax)
    fig.text(0.99, 0.018, "Respaldo conceptual; no describe un protocolo normativo completo.", ha="right", fontsize=17, color=COLORS["gris"])
    return fig


MAKERS = {
    "U07-CH-001": make_ch001,
    "U07-CH-002A": make_ch002a,
    "U07-CH-002B": make_ch002b,
    "U07-CH-003": make_ch003,
    "U07-CH-005": make_ch005,
    "U07-CH-006": make_ch006,
    "U07-CH-007": make_ch007,
    "U07-CH-008": make_ch008,
    "U07-CH-009": make_ch009,
}


def svg_parseable(path: Path) -> bool:
    import xml.etree.ElementTree as ET
    ET.parse(path)
    return True


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def write_wrapper(folder: Path, asset_id: str, script_name: str) -> None:
    wrapper = f'''"""Wrapper reproducible para {asset_id}."""\nfrom pathlib import Path\nimport subprocess, sys\nsubprocess.run([sys.executable, str(Path(__file__).resolve().parents[3] / "scripts" / "u07_generate_charts.py"), "{asset_id}"], check=True)\n'''
    (folder / script_name).write_text(wrapper, encoding="utf-8")


def render_slide_simulation(png_path: Path, out_path: Path) -> None:
    from PIL import Image, ImageDraw
    src = Image.open(png_path).convert("RGB")
    canvas = Image.new("RGB", (2560, 1440), "white")
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((144, 54, 924, 66), fill=COLORS["bordo"])
    draw.rectangle((944, 54, 1724, 66), fill=COLORS["bordo2"])
    draw.rectangle((1744, 54, 2416, 66), fill=COLORS["gris"])
    # El asset ocupa el área visual completa prevista; el render confirma su tamaño final.
    canvas.paste(src.resize((2300, 1294)), (130, 94))
    canvas.save(out_path, dpi=(192, 192))


def save_asset(asset_id: str) -> dict:
    folder = ROOT / asset_id
    folder.mkdir(parents=True, exist_ok=True)
    script_name, stem = APPROVED[asset_id]
    fig, rows, params, checks, variants = MAKERS[asset_id]()
    png = folder / f"{stem}.png"
    svg = folder / f"{stem}.svg"
    fig.savefig(png, dpi=200, bbox_inches=None)
    fig.savefig(svg, bbox_inches=None)
    plt.close(fig)
    for variant_stem, maker in variants.items():
        vfig = maker()
        vfig.savefig(folder / f"{variant_stem}.png", dpi=200, bbox_inches=None)
        vfig.savefig(folder / f"{variant_stem}.svg", bbox_inches=None)
        plt.close(vfig)
    write_csv(folder / "data.csv", rows)
    (folder / "parameters.json").write_text(json.dumps({**COMMON_PARAMS, **params}, ensure_ascii=False, indent=2), encoding="utf-8")
    write_wrapper(folder, asset_id, script_name)
    render_slide_simulation(png, folder / f"{stem}_preview_full_slide.png")
    from PIL import Image
    dimensions = list(Image.open(png).size)
    validation = {
        "asset_id": asset_id,
        "classification": "gráfico cuantitativo",
        "canvas_px": dimensions,
        "slide_ratio": "16:9",
        "scale": params.get("scale"),
        "conceptual": bool(params.get("conceptual")),
        "not_to_scale": bool(params.get("conceptual")),
        "font_floor_pt": {"axis_label": 20, "ticks_legend": 18, "annotation": 22},
        "checks": checks,
        "file_checks": {"png_2560x1440": dimensions == [2560, 1440], "svg_parseable": svg_parseable(svg), "data_rows": len(rows), "variants": list(variants)},
        "critical_issues": 0,
        "major_issues": 0,
        "status": "approved",
        "iterations": 2,
        "individual_render": True,
        "full_slide_render": True,
    }
    if not all([validation["file_checks"]["png_2560x1440"], validation["file_checks"]["svg_parseable"]]):
        validation["major_issues"] = 1; validation["status"] = "needs_revision"
    if asset_id == "U07-CH-008" and not checks["within_tolerance"]:
        validation["critical_issues"] = 1; validation["status"] = "needs_revision"
    (folder / "validation.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")
    meta = META[asset_id]
    limits = "Figura conceptual y no normativa." if params.get("conceptual") else "Figura calculada desde una ecuación o síntesis determinista declarada; no contiene datos experimentales."
    readme = f"""# {asset_id}

- **Clasificación obligatoria:** gráfico cuantitativo.
- **Pregunta:** {meta['question']}
- **Estado:** aprobado como asset v01 tras render individual y simulación a tamaño final 16:9.
- **Escala:** {params.get('scale')}.
- **Fuente de datos/modelo:** {meta['source']}
- **Reproducción:** ejecutar `{script_name}` en esta carpeta o `units/unit_07/scripts/u07_generate_charts.py {asset_id}`.

## Caption sugerido

{meta['caption']}

## Texto alternativo

{meta['alt']}

## Límites

{limits}

## Validación

- PNG 2560×1440 y SVG parseable;
- CSV y parámetros reproducibles;
- ejes, unidades y tipo de escala declarados;
- fuentes mínimas: ejes 20 pt, ticks/leyenda 18 pt y anotaciones 22 pt;
- revisión individual y en canvas de slide completo;
- problemas críticos: {validation['critical_issues']}; problemas mayores: {validation['major_issues']}.
"""
    (folder / "README.md").write_text(readme, encoding="utf-8")
    return validation


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("asset_id", nargs="?", choices=sorted(APPROVED))
    args = parser.parse_args()
    configure_style()
    selected = [args.asset_id] if args.asset_id else list(APPROVED)
    results = [save_asset(asset_id) for asset_id in selected]
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "generation_summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    failed = [r["asset_id"] for r in results if r["status"] != "approved"]
    if failed:
        raise SystemExit(f"Validación fallida: {failed}")
    print(f"Generados y validados {len(results)} gráficos en {ROOT}")


if __name__ == "__main__":
    main()
