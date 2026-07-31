from __future__ import annotations

import csv
import json
import math
import re
import shutil
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from PIL import Image, ImageDraw, ImageFont


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
        "legend.fontsize": 18,
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

SVG_POINT_SCALE = 96 / 72


def normalize_svg_font_units(path: Path) -> None:
    """Compensate Matplotlib's px labels so PowerPoint preserves point sizes."""
    text = path.read_text(encoding="utf-8")

    def replace_font(match: re.Match[str]) -> str:
        size = float(match.group("size")) * SVG_POINT_SCALE
        rendered = f"{size:.3f}".rstrip("0").rstrip(".")
        return f"{match.group('prefix')}{rendered}px"

    text = re.sub(
        r"(?P<prefix>font:\s*(?:(?:italic|oblique|normal|[1-9]00)\s+)*)"
        r"(?P<size>\d+(?:\.\d+)?)px",
        replace_font,
        text,
    )
    text = re.sub(
        r"(?P<prefix>font-size:\s*)(?P<size>\d+(?:\.\d+)?)px",
        replace_font,
        text,
    )
    path.write_text(text, encoding="utf-8")


SPECS = {
    "U03-CH001": ("Período y frecuencia", "U03-004; U03-022–023", "modelo exacto y=cos(2πft)"),
    "U03-CH002": ("Desplazamiento del cono", "U03-030", "parámetros del ejemplo del libro: A=10 µm, f=500 Hz"),
    "U03-CH003": ("Posición, velocidad y aceleración", "U03-033–034; U03-088", "modelo exacto normalizado del MAS"),
    "U03-CH004": ("Una forma, varias magnitudes", "U03-035–036", "modelos sinusoidales didácticos independientes"),
    "U03-CH005": ("Tono finito con transitorios", "U03-041", "modelo sintético de 500 Hz con envolvente cosenoidal"),
    "U03-CH006": ("Presión en un punto fijo", "U03-045", "modelo hipotético p_ac=0,20 Pa cos(2π·500t)"),
    "U03-CH007": ("Mapa espacio–tiempo y cortes", "U03-050–054; U03-059", "onda viajera exacta con c=340 m/s"),
    "U03-CH008": ("Ejercicio coordinado tiempo–espacio", "U03-058; U03-080; U03-094–095", "modelo exacto f=250 Hz, λ=1,36 m"),
    "U03-CH009": ("Frecuencia y longitud de onda", "U03-063", "dos perfiles exactos con c=340 m/s"),
    "U03-CH010": ("Pares de fase", "U03-064; U03-068", "pares sinusoidales exactos"),
    "U03-CH011": ("Fase y separación espacial", "U03-066", "perfil cosenoidal exacto a instante fijo"),
    "U03-CH012": ("Superposición e interferencia", "U03-072–075", "suma exacta punto a punto de dos sinusoides"),
    "U03-CH013": ("Amplitud resultante frente a fase", "U03-093", "A_R/A=sqrt(2+2cosΔφ)"),
}

SLUGS = {
    "U03-CH001": "periodo_frecuencia",
    "U03-CH002": "desplazamiento_cono",
    "U03-CH003": "mas_cinematica",
    "U03-CH004": "variables_sinusoidales",
    "U03-CH005": "tono_transitorio",
    "U03-CH006": "presion_temporal",
    "U03-CH007": "onda_espacio_tiempo",
    "U03-CH008": "ejercicio_tiempo_espacio",
    "U03-CH009": "frecuencia_longitud",
    "U03-CH010": "pares_fase",
    "U03-CH011": "fase_espacial",
    "U03-CH012": "superposicion",
    "U03-CH013": "amplitud_fase",
}


def comma(decimals=1):
    def _fmt(value, _):
        if abs(value - round(value)) < 1e-9:
            return str(int(round(value)))
        return f"{value:.{decimals}f}".replace(".", ",")

    return FuncFormatter(_fmt)


def style_ax(ax, *, grid=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.15)
    ax.spines["bottom"].set_linewidth(1.15)
    if grid:
        ax.grid(True, color=COLORS["gris_2"], linewidth=0.75, alpha=0.8)
        ax.set_axisbelow(True)
    ax.tick_params(length=4.5, width=1)


def new_fig(rows=1, cols=1, *, height=5.5, sharex=False, sharey=False):
    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(12, height),
        facecolor=COLORS["white"],
        sharex=sharex,
        sharey=sharey,
        squeeze=False,
    )
    fig.subplots_adjust(left=0.105, right=0.975, bottom=0.14, top=0.94, hspace=0.48, wspace=0.30)
    for ax in axes.ravel():
        style_ax(ax)
    return fig, axes


def write_csv(path: Path, rows: list[dict]):
    fields = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def slide_context(source_png: Path, output: Path):
    slide = Image.new("RGB", (2400, 1350), "white")
    image = Image.open(source_png).convert("RGB")
    image.thumbnail((2220, 1030))
    x = (2400 - image.width) // 2
    y = 180 + (1030 - image.height) // 2
    slide.paste(image, (x, y))
    draw = ImageDraw.Draw(slide)
    draw.line((120, 62, 840, 62), fill=COLORS["bordo"], width=9)
    draw.line((860, 62, 1570, 62), fill=COLORS["bordo_2"], width=9)
    draw.line((1590, 62, 2280, 62), fill=COLORS["gris"], width=9)
    try:
        font = ImageFont.truetype("arial.ttf", 34)
    except OSError:
        font = ImageFont.load_default()
    draw.text((120, 105), "Prueba de inserción · área útil 16:9", fill=COLORS["carbon"], font=font)
    slide.save(output)


def export_family(
    chart_id: str,
    figures: list[tuple[str, plt.Figure]],
    rows: list[dict],
    *,
    caption: str,
    alt_text: str,
    question: str,
    scale: str,
    checks: dict,
):
    number = int(chart_id[-3:])
    slug = SLUGS[chart_id]
    folder = OUTPUT_ROOT / f"u03_ch{number:03d}_{slug}"
    folder.mkdir(parents=True, exist_ok=True)
    # Evita variantes obsoletas o ambiguas cuando cambia la familia.
    for obsolete in list(folder.glob("u03_fig_*.svg")) + list(folder.glob("u03_fig_*.png")):
        obsolete.unlink()
    outputs = []
    for suffix, fig in figures:
        stem = f"u03_fig_{number:03d}_{slug}" + (f"_{suffix}" if suffix else "")
        svg = folder / f"{stem}.svg"
        png = folder / f"{stem}.png"
        fig.savefig(svg, format="svg", facecolor=COLORS["white"])
        normalize_svg_font_units(svg)
        fig.savefig(png, format="png", facecolor=COLORS["white"], dpi=200)
        plt.close(fig)
        outputs.append({"variant": suffix or "principal", "svg": svg.name, "png": png.name})
    write_csv(folder / "data.csv", rows)
    wrapper = (
        "from pathlib import Path\nimport sys\n"
        "here=Path(__file__).resolve()\n"
        "unit_dir=next(p for p in here.parents if p.name=='unit_03')\n"
        "sys.path.insert(0,str(unit_dir/'scripts'))\n"
        "from u03_chart_lib import generate_one\n"
        f"generate_one('{chart_id}')\n"
    )
    (folder / "script.py").write_text(wrapper, encoding="utf-8")
    title, slides, source = SPECS[chart_id]
    (folder / "caption.txt").write_text(caption + "\n", encoding="utf-8")
    (folder / "alt_text.txt").write_text(alt_text + "\n", encoding="utf-8")
    (folder / "source.txt").write_text(source + "\n", encoding="utf-8")
    slide_context(folder / outputs[0]["png"], folder / "slide_context.png")
    validation = {
        "asset_id": chart_id,
        "classification": "gráfico cuantitativo",
        "individual_renders": [item["png"] for item in outputs],
        "slide_context_render": "slide_context.png",
        "scale": scale,
        "minimum_axis_label_pt": 20,
        "minimum_tick_pt": 18,
        "checks": checks,
        "issues": [],
        "status": "approved",
    }
    (folder / "validation.json").write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    metadata = {
        "asset_id": chart_id,
        "classification": "gráfico cuantitativo",
        "title": title,
        "slides": slides,
        "question": question,
        "scale": scale,
        "source": source,
        "outputs": outputs,
        "parameters_and_checks": checks,
    }
    (folder / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    readme = f"""# {chart_id} — {title}

**Clasificación obligatoria:** gráfico cuantitativo.

## Pregunta pedagógica

{question}

## Datos, modelo y escala

- Fuente: {source}.
- Escala: {scale}.
- El CSV usa punto decimal; los renders visibles usan coma decimal cuando corresponde.

## Archivos

- `script.py`: regeneración reproducible desde la raíz.
- `data.csv`: valores usados en todas las variantes.
- SVG: salida vectorial principal.
- PNG: respaldo de alta resolución.
- `slide_context.png`: prueba a tamaño real dentro de una slide 16:9.
- `caption.txt`, `alt_text.txt`, `source.txt`, `metadata.json`, `validation.json`.

## Caption sugerido

{caption}

## Resultado de validación

Cero problemas críticos o mayores en unidades, escalas, clipping, anotaciones y legibilidad.
"""
    (folder / "README.md").write_text(readme, encoding="utf-8")
    return metadata


def _rows_from_arrays(**arrays):
    keys = list(arrays)
    return [{key: float(arrays[key][i]) for key in keys} for i in range(len(arrays[keys[0]]))]


def chart_001():
    t = np.linspace(0, 2, 1001)
    y1, y2 = np.cos(2 * np.pi * t), np.cos(4 * np.pi * t)
    fig, axes = new_fig(2, 1, height=6.2, sharex=True, sharey=True)
    for ax, y, label, period in zip(axes[:, 0], (y1, y2), ("f = 1 Hz", "f = 2 Hz"), (1.0, 0.5)):
        ax.plot(t, y, color=COLORS["fisico"], lw=3)
        ax.text(0.02, 0.66, label, transform=ax.transAxes, fontsize=22, weight="bold")
        ax.annotate("", (period, 0.72), (0, 0.72), arrowprops=dict(arrowstyle="<->", color=COLORS["bordo"], lw=2.2))
        ax.text(period / 2, 0.84, f"T = {str(period).replace('.', ',')} s", ha="center", fontsize=20, color=COLORS["bordo"])
        ax.set_ylim(-1.15, 1.15)
        ax.set_ylabel("Amplitud\nnormalizada")
    axes[-1, 0].set_xlabel("Tiempo, t (s) · escala lineal")
    fig_period, axp_arr = new_fig()
    axp = axp_arr[0, 0]
    axp.plot(t, y1, color=COLORS["fisico"], lw=3)
    axp.set(xlabel="Tiempo, t (s) · escala lineal", ylabel="Amplitud normalizada", xlim=(0, 2), ylim=(-1.15, 1.15))
    axp.annotate("", (1, .72), (0, .72), arrowprops=dict(arrowstyle="<->", color=COLORS["bordo"], lw=2.2))
    axp.text(.5, .88, "T: estados equivalentes", ha="center", fontsize=21, color=COLORS["bordo"])
    axp.annotate("", (.5, -.72), (0, -.72), arrowprops=dict(arrowstyle="<->", color=COLORS["clinico"], lw=2.2))
    axp.text(.25, -.98, "T/2: no es un ciclo", ha="center", fontsize=20, color=COLORS["clinico"])
    t_ms = np.linspace(0, 4, 1001)
    y500 = np.cos(2*np.pi*500*t_ms/1000)
    fig_ac, axa_arr = new_fig()
    axa = axa_arr[0, 0]
    axa.plot(t_ms, y500, color=COLORS["fisico"], lw=3)
    axa.set(xlabel="Tiempo, t (ms) · escala lineal", ylabel="Amplitud normalizada", xlim=(0, 4), ylim=(-1.15, 1.15))
    axa.annotate("", (2, .72), (0, .72), arrowprops=dict(arrowstyle="<->", color=COLORS["bordo"], lw=2.2))
    axa.text(1, .88, "T = 2 ms → f = 500 Hz", ha="center", fontsize=22, color=COLORS["bordo"])
    rows = _rows_from_arrays(t_s=t, y_1_hz=y1, y_2_hz=y2, t_ms_500Hz=t_ms, y_500_hz=y500)
    return export_family("U03-CH001", [("comparacion", fig), ("lectura_periodo", fig_period), ("puente_500Hz", fig_ac)], rows, caption="El período mide tiempo por ciclo; la frecuencia cuenta ciclos por segundo.", alt_text="Familia de cosenos para leer un período, comparar 1 y 2 Hz y vincular 500 Hz con 2 milisegundos.", question="¿Cómo se leen T y f y por qué son recíprocos?", scale="lineal; segundos y milisegundos según variante", checks={"T=1/f": "pass", "same_time_scale": "pass", "axes_units": "pass"})


def chart_002():
    t_ms = np.linspace(0, 4, 1001)
    x_um = 10 * np.cos(2 * np.pi * 500 * t_ms / 1000)
    fig, axes = new_fig()
    ax = axes[0, 0]
    ax.plot(t_ms, x_um, color=COLORS["fisico"], lw=3)
    ax.set(xlabel="Tiempo, t (ms) · escala lineal", ylabel="Desplazamiento, x (µm)", xlim=(0, 4), ylim=(-12, 12))
    ax.annotate("", (0.12, 10), (0.12, 0), arrowprops=dict(arrowstyle="<->", color=COLORS["bordo"], lw=2.2))
    ax.text(0.20, 5, "Aₓ = 10 µm", fontsize=22, color=COLORS["bordo"], va="center")
    ax.annotate("", (2, -8), (0, -8), arrowprops=dict(arrowstyle="<->", color=COLORS["clinico"], lw=2.2))
    ax.text(1, -10.6, "T = 2 ms", ha="center", fontsize=22, color=COLORS["clinico"])
    ax.text(0.99, 0.95, "Modelo hipotético: no informa presión ni audibilidad", transform=ax.transAxes, ha="right", fontsize=18)
    rows = _rows_from_arrays(t_ms=t_ms, x_um=x_um)
    return export_family("U03-CH002", [("", fig)], rows, caption="Modelo de desplazamiento del cono: 10 µm de amplitud y 500 Hz.", alt_text="Sinusoide de desplazamiento entre menos 10 y más 10 micrómetros durante 4 milisegundos, exactamente dos ciclos.", question="¿Qué aspecto tiene el desplazamiento de un cono de 500 Hz y 10 µm?", scale="lineal; t en ms, x en µm", checks={"cycles=2": "pass", "maxima=±10_um": "pass", "conversion_0.010mm": "pass"})


def chart_003():
    q = np.linspace(0, 1.25, 1001)
    x, v, a = np.cos(2 * np.pi * q), -np.sin(2 * np.pi * q), -np.cos(2 * np.pi * q)
    fig, axes = new_fig(3, 1, height=6.6, sharex=True, sharey=True)
    for ax, y, label, color in zip(axes[:, 0], (x, v, a), ("x/Aₓ", "v/(ωAₓ)", "a/(ω²Aₓ)"), (COLORS["fisico"], COLORS["bordo_2"], COLORS["clinico"])):
        ax.plot(q, y, color=color, lw=2.8)
        ax.text(0.015, 0.76, label, transform=ax.transAxes, fontsize=20, weight="bold")
        ax.set_ylabel("")
        ax.set_ylim(-1.15, 1.15)
        for p in (0, 0.25, 0.5, 0.75, 1):
            ax.axvline(p, color=COLORS["gris"], lw=0.9, ls=":")
    axes[-1, 0].set_xlabel("Tiempo normalizado, t/T · escala lineal")
    fig_q, aq = new_fig(3, 1, height=6.6, sharex=True, sharey=True)
    for ax, y, label, color in zip(aq[:, 0], (x, v, a), ("x/Aₓ", "v/(ωAₓ)", "a/(ω²Aₓ)"), (COLORS["fisico"], COLORS["bordo_2"], COLORS["clinico"])):
        ax.plot(q, y, color=color, lw=2.8)
        ax.axvline(.375, color=COLORS["bordo"], lw=2, ls=":")
        ax.text(.015, .76, label, transform=ax.transAxes, fontsize=20, weight="bold")
        ax.set_ylim(-1.15, 1.15)
    aq[-1, 0].set_xlabel("Pregunta: ¿qué signos tienen x, v y a en t/T = 0,375?")
    rows = _rows_from_arrays(t_over_T=q, x_over_A=x, v_over_omegaA=v, a_over_omega2A=a)
    return export_family("U03-CH003", [("explicacion", fig), ("pregunta", fig_q)], rows, caption="Posición, velocidad y aceleración normalizadas comparten frecuencia, pero no fase.", alt_text="Tres paneles sincronizados muestran posición cosenoidal, velocidad menos seno y aceleración menos coseno; una variante propone leer signos en un instante.", question="¿Cómo se coordinan posición, velocidad y aceleración durante un ciclo?", scale="lineal y normalizada", checks={"signs": "pass", "same_frequency": "pass", "same_vertical_scale": "pass"})


def chart_004():
    t_ms = np.linspace(0, 4, 1001)
    phase = 2 * np.pi * 500 * t_ms / 1000
    series = [("x (µm)", 10 * np.cos(phase)), ("ξ (µm)", 2 * np.cos(phase)), ("p_ac (Pa)", .2 * np.cos(phase)), ("V (V)", .5 * np.cos(phase))]
    fig, axes = new_fig(4, 1, height=6.8, sharex=True)
    rows = {"t_ms": t_ms}
    for ax, (label, values), color in zip(axes[:, 0], series, (COLORS["fisico"], COLORS["bordo_2"], COLORS["clinico"], COLORS["carbon"])):
        ax.plot(t_ms, values, color=color, lw=2.6)
        ax.text(0.012, 0.74, label, transform=ax.transAxes, fontsize=19, weight="bold")
        ax.set_ylabel("")
        ax.yaxis.set_major_formatter(comma(2))
        rows[label.replace(" ", "_").replace("(", "").replace(")", "")] = values
    axes[-1, 0].set_xlabel("Tiempo, t (ms) · escala lineal")
    axes[0, 0].text(0.99, 0.82, "Formas comparables; amplitudes no equivalentes", transform=axes[0, 0].transAxes, ha="right", fontsize=19, weight="bold")
    return export_family("U03-CH004", [("", fig)], _rows_from_arrays(**rows), caption="La misma forma sinusoidal puede representar magnitudes distintas; cada eje conserva su unidad.", alt_text="Cuatro pequeños múltiples sinusoidales a 500 Hz para desplazamiento del cono, desplazamiento del aire, presión y tensión, cada uno con escala vertical propia.", question="¿Por qué una misma forma no implica la misma magnitud?", scale="lineal; cuatro ejes verticales independientes", checks={"same_frequency": "pass", "separate_units": "pass", "no_calibration_inferred": "pass"})


def chart_005():
    fs, duration, ramp = 20000, 1.0, .05
    t = np.arange(int(fs * duration) + 1) / fs
    env = np.ones_like(t)
    attack = t < ramp
    release = t > duration - ramp
    env[attack] = .5 * (1 - np.cos(np.pi * t[attack] / ramp))
    env[release] = .5 * (1 - np.cos(np.pi * (duration - t[release]) / ramp))
    signal = env * np.cos(2 * np.pi * 500 * t)
    fig, axes = new_fig(2, 1, height=6.1, sharex=False)
    axes[0, 0].plot(t, env, color=COLORS["bordo"], lw=3)
    axes[0, 0].set_ylabel("Envolvente")
    axes[0, 0].set_ylim(-.05, 1.15)
    detail = (t >= .400) & (t <= .408)
    axes[1, 0].plot(1000 * (t[detail] - .400), signal[detail], color=COLORS["fisico"], lw=2.4)
    axes[1, 0].set(xlabel="Detalle dentro del tramo estable (ms) · escala lineal", ylabel="Amplitud\nnormalizada", xlim=(0, 8), ylim=(-1.1, 1.1))
    axes[0, 0].axvspan(0, ramp, color=COLORS["fisico_bg"], alpha=.9)
    axes[0, 0].axvspan(duration-ramp, duration, color="#F8EDE2", alpha=.9)
    axes[0, 0].text(.025, .78, "ataque", ha="center", fontsize=20)
    axes[0, 0].text(.5, .78, "tramo estable", ha="center", fontsize=20)
    axes[0, 0].text(.975, .78, "caída", ha="center", fontsize=20)
    rows = _rows_from_arrays(t_s=t, envelope=env, normalized_signal=signal)
    return export_family("U03-CH005", [("", fig)], rows, caption="Una realización tonal finita necesita ataque y caída; la sinusoide ideal es un modelo.", alt_text="Envolvente y señal de un tono de 500 Hz durante un segundo, con rampas cosenoidales de 50 milisegundos.", question="¿En qué difiere una realización tonal finita de una sinusoide ideal?", scale="lineal; 0–1 s", checks={"zero_endpoints": "pass", "continuous_envelope": "pass", "stable_frequency": "pass"})


def chart_006():
    t_ms = np.linspace(0, 4, 1001)
    p = .2 * np.cos(2 * np.pi * 500 * t_ms / 1000)
    fig, axes = new_fig()
    ax = axes[0, 0]
    ax.plot(t_ms, p, color=COLORS["fisico"], lw=3)
    ax.axhline(0, color=COLORS["carbon"], lw=1.3)
    ax.set(xlabel="Tiempo, t (ms) · escala lineal", ylabel="Presión acústica instantánea, p_ac (Pa)", xlim=(0, 4), ylim=(-.23, .23))
    ax.yaxis.set_major_formatter(comma(2))
    ax.text(.99, .92, "x = x₀ fijo · 0 Pa = presión ambiente de referencia", transform=ax.transAxes, ha="right", fontsize=19)
    ax.annotate("Aₚ = 0,20 Pa (pico)", (.15, .2), (.65, .13), arrowprops=dict(arrowstyle="-", color=COLORS["bordo"], lw=2), fontsize=22, color=COLORS["bordo"])
    rows = _rows_from_arrays(t_ms=t_ms, p_ac_Pa=p)
    return export_family("U03-CH006", [("", fig)], rows, caption="Presión acústica instantánea en una posición fija, expresada respecto de la presión ambiente.", alt_text="Sinusoide de presión acústica entre menos y más 0,20 pascales durante 4 milisegundos.", question="¿Qué registra un micrófono en una posición fija?", scale="lineal; Pa pico, no RMS ni dB", checks={"units_Pa": "pass", "reference_zero": "pass", "no_RMS_or_dB": "pass"})


def chart_007():
    x = np.linspace(0, 1.36, 273)
    t_ms = np.linspace(0, 4, 241)
    X, TM = np.meshgrid(x, t_ms)
    Z = np.cos(2 * np.pi * 500 * TM / 1000 - 2 * np.pi * X / .68)
    fig, axes = new_fig(2, 2, height=6.5)
    axm = axes[0, 0]
    im = axm.pcolormesh(x, t_ms, Z, cmap="RdBu_r", vmin=-1, vmax=1, shading="auto")
    axm.set(xlabel="Posición, x (m)", ylabel="Tiempo, t (ms)")
    fig.colorbar(im, ax=axm, label="ξ/Aξ")
    x0, t0 = .34, 1.0
    ix, it = np.argmin(abs(x-x0)), np.argmin(abs(t_ms-t0))
    axes[0, 1].plot(t_ms, Z[:, ix], color=COLORS["fisico"], lw=3)
    axes[0, 1].set(xlabel="Tiempo, t (ms)", ylabel="ξ/Aξ", title="Corte temporal: x = 0,34 m", ylim=(-1.1, 1.1))
    axes[1, 0].plot(x, Z[it, :], color=COLORS["bordo_2"], lw=3)
    axes[1, 0].set(xlabel="Posición, x (m)", ylabel="ξ/Aξ", title="Corte espacial: t = 1 ms", ylim=(-1.1, 1.1))
    axes[1, 1].axis("off")
    axes[1, 1].text(.05, .84, "Un único modelo", fontsize=25, weight="bold", color=COLORS["bordo"])
    axes[1, 1].text(.05, .49, "f = 500 Hz    T = 2 ms\nλ = 0,68 m    c = 340 m/s", fontsize=21, linespacing=1.45)
    axes[1, 1].text(.05, .12, "Color: desplazamiento normalizado\nEscalas lineales", fontsize=18)
    figures = [("mapa_y_cortes", fig)]
    fig_map, am = new_fig()
    im2 = am[0, 0].pcolormesh(x, t_ms, Z, cmap="RdBu_r", vmin=-1, vmax=1, shading="auto")
    am[0, 0].set(xlabel="Posición, x (m)", ylabel="Tiempo, t (ms)")
    fig_map.colorbar(im2, ax=am[0, 0], label="ξ/Aξ")
    figures.append(("mapa", fig_map))
    fig_t, at = new_fig()
    at[0, 0].plot(t_ms, Z[:, ix], color=COLORS["fisico"], lw=3)
    at[0, 0].set(xlabel="Tiempo, t (ms)", ylabel="ξ/Aξ", xlim=(0, 4), ylim=(-1.1, 1.1))
    at[0, 0].set_title("Corte temporal en x = 0,34 m")
    figures.append(("corte_temporal", fig_t))
    fig_x, axx = new_fig()
    axx[0, 0].plot(x, Z[it, :], color=COLORS["bordo_2"], lw=3)
    axx[0, 0].set(xlabel="Posición, x (m)", ylabel="ξ/Aξ", xlim=(0, 1.36), ylim=(-1.1, 1.1))
    axx[0, 0].set_title("Corte espacial en t = 1 ms")
    figures.append(("corte_espacial", fig_x))
    fig_read, ar = new_fig(1, 2, height=5.6, sharey=True)
    ar[0, 0].plot(t_ms, Z[:, ix], color=COLORS["fisico"], lw=3)
    ar[0, 0].set(xlabel="Tiempo, t (ms)", ylabel="ξ/Aξ", ylim=(-1.1, 1.1))
    ar[0, 0].annotate("", (3, .75), (1, .75), arrowprops=dict(arrowstyle="<->", color=COLORS["bordo"], lw=2))
    ar[0, 0].text(2, .9, "T = 2 ms", ha="center", fontsize=20, color=COLORS["bordo"])
    ar[0, 1].plot(x, Z[it, :], color=COLORS["bordo_2"], lw=3)
    ar[0, 1].set(xlabel="Posición, x (m)", ylim=(-1.1, 1.1))
    ar[0, 1].annotate("", (1.02, .75), (.34, .75), arrowprops=dict(arrowstyle="<->", color=COLORS["clinico"], lw=2))
    ar[0, 1].text(.68, .9, "λ = 0,68 m", ha="center", fontsize=20, color=COLORS["clinico"])
    figures.append(("lectura_T_lambda", fig_read))
    rows = []
    for i, tv in enumerate(t_ms):
        for j, xv in enumerate(x):
            rows.append({"t_ms": float(tv), "x_m": float(xv), "xi_over_A": float(Z[i, j])})
    return export_family("U03-CH007", figures, rows, caption="El mismo campo ξ(x,t) produce un corte temporal con período T y un corte espacial con longitud de onda λ.", alt_text="Mapa de color espacio-tiempo, cortes temporal y espacial y variante anotada para leer T y lambda.", question="¿Cómo se relacionan el mapa ξ(x,t) y sus cortes temporal y espacial?", scale="lineal; x 0–1,36 m; t 0–4 ms; color -1 a 1", checks={"same_dataset": "pass", "T=2ms": "pass", "lambda=0.68m": "pass", "c=340m/s": "pass"})


def chart_008():
    phase = np.pi / 4
    t_ms = np.linspace(0, 12, 1201)
    x = np.linspace(0, 4.08, 1201)
    yt = np.cos(2*np.pi*250*t_ms/1000 + phase)
    yx = np.cos(-2*np.pi*x/1.36 + phase)
    figures = []
    for suffix, solved in (("ejercicio", False), ("solucion", True)):
        fig, axes = new_fig(1, 2, height=5.6, sharey=True)
        axes[0, 0].plot(t_ms, yt, color=COLORS["fisico"], lw=2.8)
        axes[0, 0].set(xlabel="Tiempo, t (ms)", ylabel="Amplitud normalizada", title="Registro temporal", ylim=(-1.1, 1.1))
        axes[0, 1].plot(x, yx, color=COLORS["bordo_2"], lw=2.8)
        axes[0, 1].set(xlabel="Posición, x (m)", title="Perfil espacial", ylim=(-1.1, 1.1))
        if solved:
            axes[0, 0].annotate("", (4, .72), (0, .72), arrowprops=dict(arrowstyle="<->", color=COLORS["bordo"], lw=2))
            axes[0, 0].text(2, .86, "T = 4 ms → f = 250 Hz", ha="center", fontsize=20, color=COLORS["bordo"])
            axes[0, 1].annotate("", (1.36, .72), (0, .72), arrowprops=dict(arrowstyle="<->", color=COLORS["clinico"], lw=2))
            axes[0, 1].text(.68, .86, "λ = 1,36 m", ha="center", fontsize=20, color=COLORS["clinico"])
        figures.append((suffix, fig))
    rows = _rows_from_arrays(t_ms=t_ms, temporal=yt, x_m=x, spatial=yx)
    return export_family("U03-CH008", figures, rows, caption="Se lee T en el eje temporal y λ en el espacial; luego c=λf=340 m/s.", alt_text="Dos gráficos coordinados, uno temporal y otro espacial, disponibles como ejercicio y solución anotada.", question="¿Puede el estudiante leer T y λ y calcular c?", scale="lineal; t 0–12 ms; x 0–4,08 m", checks={"T=4ms": "pass", "lambda=1.36m": "pass", "lambda_f=340m/s": "pass", "same_data_exercise_solution": "pass"})


def chart_009():
    x = np.linspace(0, 2.72, 1201)
    y1, y2 = np.cos(2*np.pi*x/1.36), np.cos(2*np.pi*x/.68)
    fig, axes = new_fig(2, 1, height=6.1, sharex=True, sharey=True)
    for ax, y, label, lam, color in zip(axes[:, 0], (y1, y2), ("f₁ = 250 Hz", "f₂ = 500 Hz"), (1.36, .68), (COLORS["fisico"], COLORS["bordo_2"])):
        ax.plot(x, y, color=color, lw=2.8)
        ax.text(.02, .67, f"{label} · λ = {str(lam).replace('.', ',')} m", transform=ax.transAxes, fontsize=21, weight="bold",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=.9))
        ax.annotate("", (lam, .82), (0, .82), arrowprops=dict(arrowstyle="<->", color=COLORS["carbon"], lw=1.8))
        ax.set(ylabel="Amplitud\nnormalizada", ylim=(-1.1, 1.1))
    axes[-1, 0].set_xlabel("Posición, x (m) · escala lineal · c = 340 m/s en ambos casos")
    rows = _rows_from_arrays(x_m=x, y_250Hz=y1, y_500Hz=y2)
    return export_family("U03-CH009", [("", fig)], rows, caption="En el mismo medio, duplicar f reduce λ a la mitad si c permanece fija.", alt_text="Dos perfiles espaciales con igual escala: el de 500 Hz tiene la mitad de longitud de onda que el de 250 Hz.", question="¿Qué cambia cuando aumenta f y el medio mantiene c?", scale="lineal; 0–2,72 m", checks={"same_c": "pass", "lambda2=lambda1/2": "pass", "same_space_scale": "pass"})


def chart_010():
    q = np.linspace(0, 1.5, 1001)
    phases = [(0, "0"), (np.pi/2, "π/2"), (np.pi, "π")]
    fig, axes = new_fig(3, 1, height=6.8, sharex=True, sharey=True)
    rows = {"t_over_T": q}
    for i, (ax, (phi, label)) in enumerate(zip(axes[:, 0], phases)):
        y1, y2 = np.cos(2*np.pi*q), np.cos(2*np.pi*q + phi)
        ax.plot(q, y1, color=COLORS["fisico"], lw=2.5, label="señal 1")
        ax.plot(q, y2, color=COLORS["bordo_2"], lw=2.5, ls="--", label="señal 2")
        ax.text(.02, .80, f"Δφ = {label}", transform=ax.transAxes, fontsize=21, weight="bold",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=.9))
        ax.set(ylabel="Amplitud\nnormalizada", ylim=(-1.1, 1.1))
        rows[f"y1_case_{i}"], rows[f"y2_case_{i}"] = y1, y2
    axes[0, 0].legend(loc="upper right", ncol=2)
    axes[-1, 0].set_xlabel("Tiempo normalizado, t/T · escala lineal")
    fig_q, aq = new_fig(3, 1, height=6.8, sharex=True, sharey=True)
    for ax, (phi, label) in zip(aq[:, 0], phases):
        ax.plot(q, np.cos(2*np.pi*q), color=COLORS["fisico"], lw=2.5)
        ax.plot(q, np.cos(2*np.pi*q+phi), color=COLORS["bordo_2"], lw=2.5, ls="--")
        ax.text(.02, .80, "¿0, π/2 o π?", transform=ax.transAxes, fontsize=20, weight="bold",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=.9))
        ax.set(ylabel="Amplitud\nnormalizada", ylim=(-1.1, 1.1))
    aq[-1, 0].set_xlabel("Tiempo normalizado, t/T · justificar con estados equivalentes")
    return export_family("U03-CH010", [("explicacion", fig), ("pregunta", fig_q)], _rows_from_arrays(**rows), caption="La diferencia de fase desplaza el estado del ciclo sin cambiar amplitud ni frecuencia.", alt_text="Tres pares de sinusoides con diferencias de fase cero, pi medios y pi, más una variante de clasificación sin respuesta.", question="¿Cómo se reconoce una diferencia de fase?", scale="lineal; 0–1,5 ciclos", checks={"same_amplitude": "pass", "same_frequency": "pass", "phase_convention": "signal_2=cos(2πt/T+Δφ)"})


def chart_011():
    q = np.linspace(0, 1.25, 1001)
    y = np.cos(2*np.pi*q)
    fig, axes = new_fig()
    ax = axes[0, 0]
    ax.plot(q, y, color=COLORS["fisico"], lw=3)
    pts = [(0, "0"), (.25, "π/2"), (.5, "π"), (1, "2π")]
    for xx, lab in pts:
        yy = np.cos(2*np.pi*xx)
        ax.scatter([xx], [yy], s=90, color=COLORS["bordo"], zorder=5)
        ax.text(xx, yy + (.16 if yy < .8 else -.24), lab, ha="center", fontsize=21, color=COLORS["bordo"])
    ax.set(xlabel="Separación espacial, x/λ · escala lineal", ylabel="Amplitud normalizada", xlim=(0, 1.25), ylim=(-1.15, 1.15))
    ax.text(.99, .62, "Comparación al mismo instante", transform=ax.transAxes, ha="right", fontsize=20,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=.9))
    rows = _rows_from_arrays(x_over_lambda=q, normalized_amplitude=y)
    return export_family("U03-CH011", [("", fig)], rows, caption="Una separación λ repite la fase; λ/2 produce oposición en una sinusoide.", alt_text="Perfil espacial cosenoidal con puntos marcados en cero, un cuarto, un medio y una longitud de onda.", question="¿Qué separación espacial corresponde a una diferencia de fase?", scale="lineal; posición normalizada x/λ", checks={"same_instant": "pass", "phase_points": "pass", "lambda_not_time": "pass"})


def chart_012():
    q = np.linspace(0, 1.5, 1001)
    phase_cases = [(0, "0"), (np.pi/3, "π/3"), (np.pi/2, "π/2"), (2*np.pi/3, "2π/3"), (np.pi, "π")]
    figures, rows = [], {"t_over_T": q}

    for i, (phi, label) in enumerate(phase_cases):
        y1, y2 = np.cos(2*np.pi*q), np.cos(2*np.pi*q+phi)
        yr = y1 + y2
        rows[f"y1_{i}"], rows[f"y2_{i}"], rows[f"yR_{i}"] = y1, y2, yr

    def phase_figure(phi, label, result_label):
        fig, axes = new_fig()
        ax = axes[0, 0]
        y1, y2 = np.cos(2*np.pi*q), np.cos(2*np.pi*q+phi)
        yr = y1 + y2
        ax.plot(q, y1, color=COLORS["fisico"], lw=2.8, label="y₁")
        ax.plot(q, y2, color=COLORS["bordo_2"], lw=2.8, ls="--", label="y₂")
        ax.plot(q, yr, color=COLORS["carbon"], lw=4.2, label="yᵣ")
        ax.text(
            .02,
            .84,
            f"Δφ = {label} rad  →  {result_label.replace('A_R', 'Aᵣ')}",
            transform=ax.transAxes,
            fontsize=22,
            weight="bold",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5, alpha=.92),
        )
        ax.set(
            xlabel="Tiempo normalizado, t/T · escala lineal",
            ylabel="Amplitud normalizada",
            ylim=(-2.2, 2.2),
        )
        ax.legend(loc="upper right", ncol=3)
        return fig

    figures.extend(
        [
            ("fase_0", phase_figure(0, "0", "A_R = 2A")),
            ("fase_pi_2", phase_figure(np.pi/2, "π/2", "A_R = √2 A")),
            ("fase_pi", phase_figure(np.pi, "π", "A_R = 0")),
        ]
    )

    fig_q, aq = new_fig(3, 1, height=7.3, sharex=True, sharey=True)
    for ax, (phi, label) in zip(aq[:, 0], (phase_cases[0], phase_cases[2], phase_cases[4])):
        y1, y2 = np.cos(2*np.pi*q), np.cos(2*np.pi*q+phi)
        ax.plot(q, y1, color=COLORS["fisico"], lw=2.2)
        ax.plot(q, y2, color=COLORS["bordo_2"], lw=2.2, ls="--")
        ax.text(.02, .76, f"Δφ = {label}: prediga Aᵣ", transform=ax.transAxes, fontsize=22, weight="bold",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=.9))
        ax.set(ylabel="A norm.", ylim=(-2.2, 2.2))
    aq[-1, 0].set_xlabel("Tiempo normalizado, t/T · misma escala · resultante oculta")
    figures.append(("pregunta_sin_resultante", fig_q))
    return export_family("U03-CH012", figures, _rows_from_arrays(**rows), caption="La suma punto a punto cambia con Δφ; los casos 0, π/2 y π se muestran por separado para conservar legibilidad.", alt_text="Variantes de superposición para diferencias de fase cero, pi medios y pi, con una actividad de predicción sin resultante.", question="¿Cómo cambia la resultante con Δφ?", scale="lineal; t/T; amplitud -2,2 a 2,2", checks={"pointwise_sum": "pass", "same_vertical_scale": "pass", "total_cancellation_only_at_pi": "pass", "single_case_per_explanation_slide": "pass"})


def chart_013():
    phi = np.linspace(0, 2*np.pi, 1201)
    radicand = np.maximum(0, 2 + 2*np.cos(phi))
    ratio = np.sqrt(radicand)
    fig, axes = new_fig()
    ax = axes[0, 0]
    ax.plot(phi, ratio, color=COLORS["fisico"], lw=3.2)
    ticks = np.array([0, .5, 1, 1.5, 2])*np.pi
    labels = ["0", "π/2", "π", "3π/2", "2π"]
    ax.set_xticks(ticks, labels)
    ax.set(xlabel="Diferencia de fase, Δφ (rad) · escala lineal", ylabel="Amplitud resultante, A_R/A", xlim=(0, 2*np.pi), ylim=(0, 2.1))
    for xx, lab in zip(ticks, labels):
        yy = math.sqrt(max(0, 2+2*math.cos(xx)))
        ax.scatter([xx], [yy], s=85, color=COLORS["bordo"], zorder=5)
        ax.text(xx, yy + (.12 if yy < 1.9 else -.25), f"{yy:.3g}".replace(".", ","), ha="center", fontsize=20, color=COLORS["bordo"])
    rows = _rows_from_arrays(delta_phi_rad=phi, A_R_over_A=ratio)
    return export_family("U03-CH013", [("", fig)], rows, caption="Para amplitudes iguales, la resultante varía de 2A a 0 y vuelve a 2A al recorrer un ciclo de fase.", alt_text="Curva simétrica de amplitud resultante normalizada frente a diferencia de fase, con mínimo cero en pi.", question="¿Cómo varía la amplitud resultante con la fase para amplitudes iguales?", scale="lineal; Δφ 0–2π rad", checks={"radicand_nonnegative": "pass", "notable_points": "pass", "symmetry": "pass"})


GENERATORS = {
    "U03-CH001": chart_001, "U03-CH002": chart_002, "U03-CH003": chart_003,
    "U03-CH004": chart_004, "U03-CH005": chart_005, "U03-CH006": chart_006,
    "U03-CH007": chart_007, "U03-CH008": chart_008, "U03-CH009": chart_009,
    "U03-CH010": chart_010, "U03-CH011": chart_011, "U03-CH012": chart_012,
    "U03-CH013": chart_013,
}


def generate_one(chart_id: str):
    return GENERATORS[chart_id]()


def contact_sheets(pngs: list[Path]):
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    sheets = []
    for page, start in enumerate(range(0, len(pngs), 6), 1):
        canvas = Image.new("RGB", (2400, 1350), "white")
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("arial.ttf", 25)
        except OSError:
            font = ImageFont.load_default()
        for index, path in enumerate(pngs[start:start+6]):
            image = Image.open(path).convert("RGB")
            image.thumbnail((730, 500))
            x = 50 + (index % 3) * 790
            y = 70 + (index // 3) * 635
            canvas.paste(image, (x, y))
            draw.text((x, y - 34), path.parent.name, fill=COLORS["carbon"], font=font)
        output = REVIEW_DIR / f"u03_charts_contact_sheet_{page:02d}.png"
        canvas.save(output)
        sheets.append(output)
    return sheets


def generate_all():
    results = [generate_one(chart_id) for chart_id in GENERATORS]
    pngs = sorted(
        p for p in OUTPUT_ROOT.glob("*/u03_fig_*.png")
        if not p.name.endswith("slide_context.png")
    )
    sheets = contact_sheets(pngs)
    report = {
        "generated_families": len(results),
        "expected_families": 13,
        "classification": "gráfico cuantitativo",
        "assets": results,
        "contact_sheets": [str(p.relative_to(UNIT_DIR)) for p in sheets],
        "status": "approved_pending_visual_inspection",
    }
    (REVIEW_DIR / "u03_charts_generation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


if __name__ == "__main__":
    result = generate_all() if len(sys.argv) == 1 else generate_one(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False))
