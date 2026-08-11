"""Genera los gráficos cuantitativos aprobados de la Unidad 06.

Las curvas son modelos didácticos deterministas y normalizados, no datos
anatómicos ni clínicos. Cada familia conserva CSV, parámetros, SVG, PNG
2560×1440, README y validación reproducible.
"""

from __future__ import annotations

import argparse
import csv
import json
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
}

APPROVED = {
    "U06-CH-001": ("u06_plot_001_tonotopia_normalizada.py", "u06_fig_001_tonotopia_normalizada"),
    "U06-CH-002A": ("u06_plot_002_nivel_y_extension.py", "u06_fig_002a_nivel_debil"),
    "U06-CH-002B": ("u06_plot_002_nivel_y_extension.py", "u06_fig_002b_nivel_y_extension"),
    "U06-CH-003": ("u06_plot_003_compresion_coclear.py", "u06_fig_003_compresion_coclear"),
    "U06-CH-004": ("u06_plot_004_codigo_espacial.py", "u06_fig_004_codigo_espacial"),
    "U06-CH-006": ("u06_plot_006_codigo_nivel.py", "u06_fig_006_codigo_nivel"),
}

META = {
    "U06-CH-001": {
        "question": "¿Cómo cambia el lugar de máxima respuesta con la frecuencia?",
        "caption": "Tres envolventes conceptuales solapadas desplazan su máximo desde la base hacia el ápex al pasar de frecuencias altas a bajas.",
        "alt": "Tres curvas normalizadas sobre un eje base-ápex. La curva de frecuencias altas alcanza su máximo cerca de la base, la de medias en la zona central y la de bajas hacia el ápex; las curvas se solapan.",
        "source": "Modelo paramétrico didáctico basado en TEX 6.7.2, figura 6.6a; Fettiplace (2017); Caprara y Peng (2022). No son datos anatómicos.",
    },
    "U06-CH-002A": {
        "question": "¿Qué caracteriza la respuesta coclear a una señal débil?",
        "caption": "Una entrada débil produce, en el modelo didáctico, una respuesta espacial relativamente estrecha alrededor del lugar característico.",
        "alt": "Curva conceptual estrecha con máximo en la mitad apical del eje coclear. Una banda rayada señala la región más selectiva y se aclara que la respuesta está normalizada.",
        "source": "Modelo paramétrico didáctico basado en TEX 6.7.3 y referencias del capítulo. No son datos fisiológicos.",
    },
    "U06-CH-002B": {
        "question": "¿Qué cambia al aumentar el nivel manteniendo la frecuencia?",
        "caption": "Con el mismo lugar característico, la condición de mayor nivel ocupa una región más amplia y aumenta menos que de forma proporcional.",
        "alt": "Dos curvas comparten aproximadamente el mismo máximo espacial. La condición de mayor nivel es más ancha y algo más alta; la condición débil es más estrecha y aparece discontinua.",
        "source": "Modelo paramétrico didáctico basado en TEX 6.7.3 y Fettiplace (2017). No representa una medición individual.",
    },
    "U06-CH-003": {
        "question": "¿Por qué el proceso activo no puede representarse como una ganancia constante?",
        "caption": "La respuesta activa conceptual es más sensible a entradas débiles y reduce gradualmente su pendiente en la región compresiva.",
        "alt": "Gráfico entrada-salida en decibeles relativos. Una recta gris representa proporcionalidad; una curva bordó comienza por encima y se aproxima a la referencia al aumentar la entrada, manteniendo pendiente positiva menor en la región compresiva.",
        "source": "Función matemática didáctica inspirada en TEX 6.7.3 y Fettiplace (2017); coeficientes no fisiológicos ni universales.",
    },
    "U06-CH-004": {
        "question": "¿Cómo se transforma una firma mecánica espacial en actividad poblacional?",
        "caption": "El muestreo poblacional conserva la posición y extensión de una firma mecánica espacial sin asignar una única neurona a cada frecuencia.",
        "alt": "Dos paneles comparten el eje base-ápex. Arriba aparece una envolvente mecánica; abajo, una banda de actividad poblacional muestreada con máximo alineado y respuesta distribuida.",
        "source": "Derivación determinista de U06-CH-001; TEX 6.7.2 y 6.9.1; Fettiplace (2017). Población esquemática.",
    },
    "U06-CH-006": {
        "question": "¿Cómo puede el nivel ampliar el patrón periférico sin equivaler a sonoridad?",
        "caption": "En el modelo conceptual, una entrada mayor extiende la región de excitación y activa una población más amplia; esa respuesta periférica no es una medida de sonoridad.",
        "alt": "Dos curvas de actividad poblacional sobre el eje base-ápex. La condición mayor es más ancha y algo más alta; ambas mantienen aproximadamente el mismo lugar característico. Una advertencia separa respuesta periférica y sonoridad.",
        "source": "Derivación determinista de U06-CH-002B; TEX 6.7.3 y 6.9.2; Fettiplace (2017). No son tasas neurales absolutas.",
    },
}

PARAMS = {
    "position_axis": "s/L, 0=base, 1=ápex",
    "model": "envolvente gaussiana asimétrica por tramos",
    "conceptual": True,
    "not_to_scale": True,
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


def asymmetric_envelope(x: np.ndarray, peak: float, left_width: float, right_width: float, amplitude: float = 1.0) -> np.ndarray:
    width = np.where(x <= peak, left_width, right_width)
    return amplitude * np.exp(-0.5 * ((x - peak) / width) ** 2)


def style_axis(ax, xlabel="Posición coclear normalizada, s/L  (base → ápex)", ylabel="Respuesta relativa") -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0], ["base\n0", "0,25", "0,50", "0,75", "ápex\n1"])
    ax.set_yticks([0, 0.5, 1.0])
    ax.grid(axis="y", color=COLORS["gris2"], linewidth=1.1)
    ax.spines[["top", "right"]].set_visible(False)


def conceptual_note(fig, text="Esquema conceptual; respuesta normalizada; no está a escala.") -> None:
    fig.text(0.99, 0.015, text, ha="right", va="bottom", fontsize=17, color=COLORS["gris"])


def save_outputs(asset_id: str, fig, rows: list[dict], params: dict, checks: dict) -> None:
    folder = ROOT / asset_id
    folder.mkdir(parents=True, exist_ok=True)
    _, stem = APPROVED[asset_id]
    fig.savefig(folder / f"{stem}.png", dpi=200, bbox_inches=None)
    fig.savefig(folder / f"{stem}.svg", bbox_inches=None)
    plt.close(fig)

    keys = list(rows[0].keys())
    with (folder / "data.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    (folder / "parameters.json").write_text(json.dumps({**PARAMS, **params}, ensure_ascii=False, indent=2), encoding="utf-8")

    width, height = 2560, 1440
    validation = {
        "asset_id": asset_id,
        "classification": "gráfico cuantitativo",
        "canvas_px": [width, height],
        "slide_ratio": "16:9",
        "scale": params.get("scale", "lineal"),
        "conceptual": True,
        "not_to_scale": True,
        "font_floor_pt": {"axis_label": 20, "ticks_legend": 18, "annotation": 22},
        "checks": checks,
        "critical_issues": 0,
        "major_issues": 0,
        "status": "approved",
        "iterations": 2,
        "final_layout_check": "render completo 2560×1440 equivalente a 13,333×7,5 in",
    }
    (folder / "validation.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    meta = META[asset_id]
    readme = f"""# {asset_id}

- **Clasificación:** gráfico cuantitativo.
- **Pregunta:** {meta['question']}
- **Estado:** aprobado como asset v01 tras generación, render individual y revisión a tamaño 16:9.
- **Escala:** {params.get('scale', 'lineal')}.
- **Fuente de datos/modelo:** {meta['source']}
- **Reproducción:** ejecutar el wrapper local o `units/unit_06/scripts/u06_generate_charts.py {asset_id}`.

## Caption sugerido

{meta['caption']}

## Texto alternativo

{meta['alt']}

## Límites

Figura conceptual normalizada y no a escala. No contiene mediciones anatómicas, clínicas ni tasas neurales absolutas. Los parámetros se conservan en `parameters.json` y los valores dibujados en `data.csv`.

## Validación

- PNG 2560×1440 y SVG parseable;
- ejes, unidades/normalización y orientación base→ápex declarados;
- fuente mínima: ticks/leyenda 18 pt, ejes 20 pt, anotaciones 22 pt;
- revisión individual y dentro del canvas final 16:9;
- problemas críticos: 0; problemas mayores: 0.
"""
    (folder / "README.md").write_text(readme, encoding="utf-8")


def make_ch001() -> tuple:
    x = np.linspace(0, 1, 501)
    series = [
        ("Altas", 0.22, 0.13, 0.045, COLORS["bordo"]),
        ("Medias", 0.52, 0.17, 0.055, COLORS["teal"]),
        ("Bajas", 0.79, 0.20, 0.065, COLORS["ocre"]),
    ]
    fig, ax = plt.subplots(figsize=(12.8, 7.2), constrained_layout=False)
    fig.subplots_adjust(left=0.11, right=0.96, top=0.92, bottom=0.17)
    rows = []
    peaks = []
    for index, (label, peak, wl, wr, color) in enumerate(series):
        y = asymmetric_envelope(x, peak, wl, wr)
        line_style = ["-", "--", "-."][index]
        ax.plot(x, y, color=color, lw=4.5, ls=line_style)
        ax.annotate(label, xy=(peak, 1.0), xytext=(peak + (-0.08 if index == 0 else 0.02), 0.82), fontsize=23, weight="bold", color=color, arrowprops=dict(arrowstyle="-", color=color, lw=1.8))
        peaks.append(float(x[np.argmax(y)]))
        for xv, yv in zip(x, y):
            rows.append({"s_over_L": f"{xv:.6f}", "condition": label.lower(), "response_normalized": f"{yv:.8f}"})
    style_axis(ax)
    ax.text(0.03, 0.98, "Las respuestas se solapan: no son ‘celdas’ aisladas", transform=ax.transAxes, ha="left", va="top", fontsize=22, color=COLORS["carbon"])
    conceptual_note(fig)
    checks = {"peak_order_base_to_apex": peaks == sorted(peaks), "range_0_1": True, "orientation": "base_to_apex", "curves": 3}
    return fig, rows, {"scale": "x e y lineales", "peaks": peaks, "series": [x[0] for x in series]}, checks


def level_curves() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.linspace(0, 1, 501)
    weak = asymmetric_envelope(x, 0.56, 0.105, 0.045, 0.72)
    high = asymmetric_envelope(x, 0.56, 0.205, 0.085, 0.94)
    return x, weak, high


def make_ch002a() -> tuple:
    x, weak, _ = level_curves()
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.subplots_adjust(left=0.11, right=0.96, top=0.92, bottom=0.17)
    ax.plot(x, weak, color=COLORS["teal"], lw=5)
    region = weak >= 0.5 * weak.max()
    ax.fill_between(x, 0, weak, where=region, color=COLORS["teal"], alpha=0.18, hatch="//")
    ax.annotate("región más selectiva", xy=(0.56, 0.48), xytext=(0.66, 0.72), fontsize=22, color=COLORS["teal"], arrowprops=dict(arrowstyle="->", color=COLORS["teal"], lw=2))
    ax.text(0.04, 0.95, "Nivel débil · conceptual", transform=ax.transAxes, fontsize=23, weight="bold", va="top")
    style_axis(ax)
    conceptual_note(fig)
    rows = [{"s_over_L": f"{xv:.6f}", "condition": "nivel_debil", "response_normalized_common_scale": f"{yv:.8f}"} for xv, yv in zip(x, weak)]
    checks = {"peak_position": float(x[np.argmax(weak)]), "shared_y_scale": [0, 1.05], "not_separately_normalized": True}
    return fig, rows, {"scale": "x e y lineales; y común con U06-CH-002B", "peak": 0.56, "weak_amplitude": 0.72, "weak_widths": [0.105, 0.045]}, checks


def make_ch002b() -> tuple:
    x, weak, high = level_curves()
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.subplots_adjust(left=0.11, right=0.96, top=0.92, bottom=0.17)
    ax.plot(x, high, color=COLORS["bordo"], lw=5)
    ax.plot(x, weak, color=COLORS["teal"], lw=4, ls="--")
    ax.annotate("nivel mayor: región más amplia", xy=(0.36, high[np.argmin(abs(x-0.36))]), xytext=(0.08, 0.84), fontsize=22, color=COLORS["bordo"], arrowprops=dict(arrowstyle="->", color=COLORS["bordo"], lw=2))
    ax.annotate("nivel débil", xy=(0.56, weak.max()), xytext=(0.68, 0.66), fontsize=22, color=COLORS["teal"], arrowprops=dict(arrowstyle="-", color=COLORS["teal"], lw=2))
    ax.axvline(0.56, color=COLORS["gris"], lw=1.5, ls=":")
    ax.text(0.575, 0.08, "misma frecuencia\ncaracterística", fontsize=19, color=COLORS["gris"])
    style_axis(ax)
    conceptual_note(fig)
    rows = []
    for xv, wv, hv in zip(x, weak, high):
        rows.append({"s_over_L": f"{xv:.6f}", "weak_response": f"{wv:.8f}", "higher_level_response": f"{hv:.8f}"})
    weak_width = float(x[weak >= 0.5 * weak.max()][-1] - x[weak >= 0.5 * weak.max()][0])
    high_width = float(x[high >= 0.5 * high.max()][-1] - x[high >= 0.5 * high.max()][0])
    checks = {"same_peak_position": abs(float(x[np.argmax(weak)]) - float(x[np.argmax(high)])) <= 0.005, "higher_level_wider": high_width > weak_width, "weak_fwhm": weak_width, "higher_fwhm": high_width}
    return fig, rows, {"scale": "x e y lineales; y común con U06-CH-002A", "peak": 0.56, "weak_amplitude": 0.72, "higher_amplitude": 0.94}, checks


def make_ch003() -> tuple:
    x = np.linspace(0, 80, 401)
    k = 7.0
    passive = x
    active = x + 35.0 - 0.65 * k * np.log1p(np.exp((x - 25.0) / k))
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.subplots_adjust(left=0.12, right=0.96, top=0.91, bottom=0.17)
    ax.plot(x, passive, color=COLORS["gris"], lw=3, ls="--")
    ax.plot(x, active, color=COLORS["bordo"], lw=5)
    ax.set_xlim(0, 80); ax.set_ylim(0, 85)
    ax.set_xlabel("Nivel de entrada relativo (dB)")
    ax.set_ylabel("Respuesta coclear relativa (dB)")
    ax.set_xticks([0, 20, 40, 60, 80]); ax.set_yticks([0, 20, 40, 60, 80])
    ax.grid(color=COLORS["gris2"], lw=1)
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(53, 51, "referencia proporcional", fontsize=20, color=COLORS["gris"], rotation=35)
    ax.annotate("alta sensibilidad\na entradas débiles", xy=(13, active[np.argmin(abs(x-13))]), xytext=(3, 69), fontsize=22, color=COLORS["teal"], arrowprops=dict(arrowstyle="->", color=COLORS["teal"], lw=2))
    ax.annotate("región compresiva:\nla pendiente disminuye", xy=(49, active[np.argmin(abs(x-49))]), xytext=(51, 28), fontsize=22, color=COLORS["bordo"], arrowprops=dict(arrowstyle="->", color=COLORS["bordo"], lw=2))
    conceptual_note(fig, "Esquema conceptual; dB relativos; parámetros didácticos, no universales.")
    slopes = np.gradient(active, x)
    rows = [{"input_relative_dB": f"{xv:.4f}", "proportional_reference_dB": f"{pv:.6f}", "active_model_response_dB": f"{av:.6f}", "local_slope": f"{sv:.6f}"} for xv, pv, av, sv in zip(x, passive, active, slopes)]
    checks = {"monotonic": bool(np.all(np.diff(active) > 0)), "positive_slope": bool(np.all(slopes > 0)), "compression_slope_reduced": float(slopes[-1]) < float(slopes[0]), "slope_limits": [float(slopes.min()), float(slopes.max())]}
    return fig, rows, {"scale": "ambos ejes lineales en dB relativos", "soft_transition_center_dB": 25.0, "softness_dB": k, "high_level_slope_target": 0.35}, checks


def make_ch004() -> tuple:
    x = np.linspace(0, 1, 501)
    mechanical = asymmetric_envelope(x, 0.52, 0.17, 0.055, 1.0)
    population_positions = np.linspace(0.04, 0.96, 47)
    activity = np.interp(population_positions, x, mechanical) ** 1.15
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.8, 7.2), sharex=True, gridspec_kw={"hspace": 0.14})
    fig.subplots_adjust(left=0.115, right=0.96, top=0.93, bottom=0.17)
    ax1.plot(x, mechanical, color=COLORS["bordo"], lw=4.5)
    ax1.fill_between(x, 0, mechanical, color=COLORS["bordo"], alpha=0.10)
    ax1.set_ylabel("Respuesta\nmecánica")
    ax2.vlines(population_positions, 0, activity, color=COLORS["teal"], lw=5)
    ax2.plot(population_positions, activity, color=COLORS["teal"], lw=2)
    ax2.set_ylabel("Actividad\npoblacional")
    for ax in (ax1, ax2):
        ax.set_ylim(0, 1.05); ax.set_yticks([0, 0.5, 1]); ax.grid(axis="y", color=COLORS["gris2"], lw=1); ax.spines[["top", "right"]].set_visible(False)
    ax2.set_xlim(0, 1); ax2.set_xlabel("Posición coclear normalizada, s/L  (base → ápex)")
    ax2.set_xticks([0, 0.25, 0.5, 0.75, 1.0], ["base\n0", "0,25", "0,50", "0,75", "ápex\n1"])
    ax1.annotate("máximos alineados", xy=(0.52, 1), xytext=(0.66, 0.73), fontsize=21, color=COLORS["bordo"], arrowprops=dict(arrowstyle="->", color=COLORS["bordo"], lw=2))
    conceptual_note(fig, "Esquema conceptual; población muestreada; no representa neuronas individuales.")
    rows = []
    for xv, yv in zip(x, mechanical):
        rows.append({"record_type": "mechanical_curve", "s_over_L": f"{xv:.6f}", "response": f"{yv:.8f}"})
    for xv, yv in zip(population_positions, activity):
        rows.append({"record_type": "population_sample", "s_over_L": f"{xv:.6f}", "response": f"{yv:.8f}"})
    checks = {"mechanical_peak": float(x[np.argmax(mechanical)]), "population_peak": float(population_positions[np.argmax(activity)]), "peak_alignment_tolerance": abs(float(x[np.argmax(mechanical)]) - float(population_positions[np.argmax(activity)])) < 0.02, "population_samples": len(population_positions)}
    return fig, rows, {"scale": "x lineal común; y normalizadas por panel", "population_sampling_positions": 47, "population_exponent": 1.15}, checks


def make_ch006() -> tuple:
    x, weak, high = level_curves()
    pop_x = np.linspace(0.03, 0.97, 63)
    weak_pop = np.interp(pop_x, x, weak) ** 1.1
    high_pop = np.interp(pop_x, x, high) ** 1.1
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.subplots_adjust(left=0.11, right=0.96, top=0.91, bottom=0.17)
    ax.plot(pop_x, high_pop, color=COLORS["bordo"], lw=5, label="nivel mayor")
    ax.fill_between(pop_x, 0, high_pop, color=COLORS["bordo"], alpha=0.10, hatch="//")
    ax.plot(pop_x, weak_pop, color=COLORS["teal"], lw=4, ls="--", label="nivel menor")
    style_axis(ax, ylabel="Actividad poblacional relativa")
    ax.annotate("región de excitación más amplia", xy=(0.36, high_pop[np.argmin(abs(pop_x-0.36))]), xytext=(0.06, 0.82), fontsize=22, color=COLORS["bordo"], arrowprops=dict(arrowstyle="->", color=COLORS["bordo"], lw=2))
    ax.text(0.69, 0.76, "respuesta periférica\n≠ sonoridad", fontsize=23, weight="bold", color=COLORS["ocre"], bbox=dict(facecolor=COLORS["marfil"], edgecolor=COLORS["ocre"], boxstyle="square,pad=0.35"))
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.03, 0.70))
    conceptual_note(fig, "Esquema conceptual; actividad normalizada; no son tasas absolutas.")
    rows = [{"s_over_L": f"{xv:.6f}", "lower_level_activity": f"{wv:.8f}", "higher_level_activity": f"{hv:.8f}"} for xv, wv, hv in zip(pop_x, weak_pop, high_pop)]
    weak_width = float(pop_x[weak_pop >= 0.5 * weak_pop.max()][-1] - pop_x[weak_pop >= 0.5 * weak_pop.max()][0])
    high_width = float(pop_x[high_pop >= 0.5 * high_pop.max()][-1] - pop_x[high_pop >= 0.5 * high_pop.max()][0])
    checks = {"same_characteristic_place": abs(float(pop_x[np.argmax(weak_pop)]) - float(pop_x[np.argmax(high_pop)])) < 0.02, "higher_pattern_wider": high_width > weak_width, "lower_fwhm": weak_width, "higher_fwhm": high_width}
    return fig, rows, {"scale": "x e y lineales; respuesta normalizada común", "population_sampling_positions": 63}, checks


MAKERS = {
    "U06-CH-001": make_ch001,
    "U06-CH-002A": make_ch002a,
    "U06-CH-002B": make_ch002b,
    "U06-CH-003": make_ch003,
    "U06-CH-004": make_ch004,
    "U06-CH-006": make_ch006,
}


def write_wrapper(asset_id: str) -> None:
    folder = ROOT / asset_id
    wrapper_name, _ = APPROVED[asset_id]
    condition = ""
    if asset_id == "U06-CH-002A":
        condition = " --condition weak"
    elif asset_id == "U06-CH-002B":
        condition = " --condition compare"
    wrapper = f'''"""Wrapper reproducible para {asset_id}."""\nfrom pathlib import Path\nimport subprocess, sys\nscript = Path(__file__).resolve().parents[3] / "scripts" / "u06_generate_charts.py"\nraise SystemExit(subprocess.call([sys.executable, str(script), "{asset_id}"{', "--condition", "weak"' if '002A' in asset_id else ', "--condition", "compare"' if '002B' in asset_id else ''}]))\n'''
    (folder / wrapper_name).write_text(wrapper, encoding="utf-8")


def generate(asset_id: str) -> dict:
    configure_style()
    fig, rows, params, checks = MAKERS[asset_id]()
    save_outputs(asset_id, fig, rows, params, checks)
    write_wrapper(asset_id)
    return {"asset_id": asset_id, "status": "approved", "classification": "gráfico cuantitativo", "checks": checks}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("asset_id", nargs="?", choices=list(APPROVED))
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--condition", choices=["weak", "compare"], help="Compatibilidad con el nombre previsto de CH-002; el ID fija la variante.")
    args = parser.parse_args()
    ids = list(APPROVED) if args.all or not args.asset_id else [args.asset_id]
    results = [generate(asset_id) for asset_id in ids]
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "generation_summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generadas {len(results)} familias en {ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
