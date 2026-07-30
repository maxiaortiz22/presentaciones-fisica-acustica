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
    theta = np.array([0.0, 10.0, 20.0, 30.0])
    speed = 331.0 + 0.6 * theta
    fig, ax = base_axes()
    ax.plot(theta, speed, color=COLORS["fisico"], linewidth=3.2, marker="o", markersize=9)
    ax.set_xlim(-0.7, 30.7)
    ax.set_ylim(325, 355)
    ax.set_xticks([0, 10, 20, 30])
    ax.set_yticks([325, 331, 337, 343, 349, 355])
    ax.set_xlabel(r"Temperatura ambiental, $\vartheta$ (°C)", labelpad=12)
    ax.set_ylabel(r"Velocidad de propagación, $c$ (m/s)", labelpad=12)
    ax.scatter([20, 30], [343, 349], s=165, facecolor="white", edgecolor=COLORS["bordo"], linewidth=2, zorder=5)
    ax.text(20, 341.4, "20 °C → 343 m/s", fontsize=21, ha="center", va="top")
    ax.text(29.4, 350.5, "30 °C → 349 m/s", fontsize=21, ha="right", va="bottom")
    ax.text(
        0.02,
        0.96,
        "Modelo para aire seco y rango ambiental",
        transform=ax.transAxes,
        fontsize=20,
        ha="left",
        va="top",
        color=COLORS["fisico"],
    )
    ax.text(
        0.98,
        0.05,
        "El eje vertical no comienza en 0",
        transform=ax.transAxes,
        fontsize=20,
        ha="right",
        va="bottom",
        color=COLORS["alerta"],
        bbox=dict(facecolor=COLORS["marfil"], edgecolor=COLORS["alerta"], pad=5),
    )
    ax.xaxis.set_major_formatter(comma_formatter())
    ax.yaxis.set_major_formatter(comma_formatter())
    finish_axes(ax)

    times = []
    for temp in [5.0, 25.0]:
        c = 331.0 + 0.6 * temp
        times.append({"temperatura_C": temp, "c_m_s": c, "t_100m_s": 100.0 / c})
    rows = [
        {"temperatura_C": f"{t:.1f}", "velocidad_m_s": f"{c:.1f}"}
        for t, c in zip(theta, speed)
    ]
    return export_chart(
        fig=fig,
        chart_id="U02-CH004",
        number=4,
        slug="velocidad_temperatura",
        rows=rows,
        fieldnames=list(rows[0]),
        title="Velocidad del sonido frente a temperatura",
        slides="U02-080; U02-081; U02-103",
        question="¿Cuánto aumenta c en el rango ambiental y qué no permite concluir el gráfico?",
        caption="Aproximación para aire seco en rango ambiental; el eje vertical 325–355 m/s no comienza en cero.",
        alt_text="Recta de velocidad de propagación frente a temperatura desde 331 metros por segundo a cero grados Celsius hasta 349 metros por segundo a treinta grados.",
        source="Valores calculados con c ≈ 331 m/s + [0,6 (m/s)/°C]·ϑ, modelo del libro; no son mediciones.",
        scale="Eje horizontal lineal de 0 a 30 °C. Eje vertical lineal truncado de 325 a 355 m/s, declarado en la figura.",
        validation=[
            "Se verifican 331, 337, 343 y 349 m/s.",
            "Pendiente exacta del modelo: 0,6 (m/s)/°C.",
            "No se infiere frecuencia, longitud de onda ni altura tonal sin datos adicionales.",
        ],
        wrapper_name="u02_plot_004_velocidad_temperatura.py",
        extra={
            "model": "c = 331 + 0.6 theta",
            "time_check_100m": times,
            "delta_t_5C_25C_ms": (times[0]["t_100m_s"] - times[1]["t_100m_s"]) * 1000,
            "U02-CH005": "reemplazado por tabla; cálculo conservado aquí",
        },
    )


if __name__ == "__main__":
    generate()
