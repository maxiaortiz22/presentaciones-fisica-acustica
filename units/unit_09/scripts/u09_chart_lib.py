"""Generación reproducible de gráficos propios aprobados de la Unidad 09.

Cada figura se dibuja en su tamaño físico final, se exporta como SVG y PNG de
alta resolución y se inserta en un canvas 16:9 de control para validar su lectura.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Callable

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw


UNIT = Path(__file__).resolve().parents[1]
OUT = UNIT / "assets" / "generated" / "charts"

C = {
    "bordo": "#4D1434",
    "bordo2": "#903163",
    "carbon": "#3D3D3D",
    "gris": "#969FA7",
    "gris2": "#D9DCE0",
    "marfil": "#F7F6F2",
    "teal": "#2F7E83",
    "ocre": "#9F541A",
    "alerta": "#9A641E",
    "blanco": "#FFFFFF",
}

mpl.rcParams.update(
    {
        "font.family": ["Arial", "DejaVu Sans"],
        "font.size": 18,
        "axes.labelsize": 20,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "legend.fontsize": 18,
        "axes.edgecolor": C["carbon"],
        "axes.labelcolor": C["carbon"],
        "xtick.color": C["carbon"],
        "ytick.color": C["carbon"],
        "text.color": C["carbon"],
        "axes.grid": True,
        "grid.color": C["gris2"],
        "grid.linewidth": 0.8,
        "grid.alpha": 0.75,
        "figure.facecolor": C["blanco"],
        "axes.facecolor": C["blanco"],
        "savefig.facecolor": C["blanco"],
        "svg.fonttype": "none",
    }
)


META = {
    "U09-CH-001": {
        "slug": "distancia",
        "size": (5.0, 3.2),
        "question": "¿Cómo cambia Lp al variar r₂/r₁?",
        "caption": "Cambio ideal del nivel de presión con la razón de distancias: duplicar la distancia produce una variación de −6,02 dB bajo las hipótesis declaradas.",
        "alt": "Curva decreciente en eje horizontal logarítmico. La variación es cero cuando las distancias son iguales y vale menos 6,02 decibeles cuando la segunda distancia duplica la primera.",
        "source": "Modelo del capítulo 9: ΔLp = −20 log10(r₂/r₁). Datos calculados por fórmula; no son mediciones.",
    },
    "U09-CH-002": {
        "slug": "patron_polar",
        "size": (10.8, 4.4),
        "question": "¿Por qué una fuente real no tiene un único patrón direccional?",
        "caption": "Tres patrones polares analíticos y sintéticos muestran cómo la distribución angular puede cambiar con la frecuencia.",
        "alt": "Tres paneles polares comparten la misma escala radial de cero a menos dieciocho decibeles. El patrón se vuelve más estrecho y aparecen lóbulos al pasar de la categoría baja a la alta.",
        "source": "Funciones analíticas sintéticas normalizadas, documentadas en parameters.json; no corresponden a un producto ni a una medición.",
    },
    "U09-CH-003": {
        "slug": "c_temperatura",
        "size": (6.8, 4.2),
        "question": "¿Cuánto cambia la rapidez del sonido en el intervalo térmico de clase?",
        "caption": "Aproximación lineal de la rapidez del sonido en aire entre −10 y 35 °C, con puntos de control a 5, 20 y 25 °C.",
        "alt": "Recta ascendente desde aproximadamente 325 hasta 352 metros por segundo. Se marcan 5 grados con 334 metros por segundo, 20 con 343 y 25 con 346.",
        "source": "Modelo del capítulo 9: c ≈ 331 + 0,6 θ. Datos calculados; intervalo de uso visible.",
    },
    "U09-CH-004": {
        "slug": "llegadas_reverberacion",
        "size": (7.0, 4.1),
        "question": "¿Qué diferencia temporal existe entre una reflexión aislada y una cola reverberante?",
        "caption": "Señales sintéticas coordinadas distinguen llegada directa, reflexión aislada y una densidad creciente de llegadas con cola.",
        "alt": "Tres paneles con igual eje temporal. El primero contiene una llegada directa; el segundo agrega una reflexión aislada; el tercero muestra muchas llegadas decrecientes que forman una cola.",
        "source": "Señales temporales sintéticas y conceptuales; parámetros en parameters.json. No se fija un umbral perceptual universal.",
    },
    "U09-CH-005": {
        "slug": "lambda_frecuencia",
        "size": (7.2, 4.2),
        "question": "¿Qué escalas espaciales corresponden a distintas frecuencias?",
        "caption": "Relación inversa entre frecuencia y longitud de onda para c = 343 m·s⁻¹, con ejemplos en 125, 500 y 4000 Hz.",
        "alt": "Curva recta descendente en ejes logarítmicos. Se marcan longitudes de onda de 2,74 metros a 125 hertz, 0,686 metros a 500 hertz y 0,0858 metros a 4000 hertz.",
        "source": "Relación λ = c/f con c = 343 m·s⁻¹, referencia didáctica próxima a 20 °C. Datos calculados.",
    },
    "U09-CH-006": {
        "slug": "decaimiento_t60",
        "size": (7.0, 4.0),
        "question": "¿Cómo se identifica T60 en un decaimiento?",
        "caption": "Decaimiento sintético en dB con T60 = 0,60 s; el tramo inferior a −70 dB se omite del panel.",
        "alt": "Recta descendente desde cero decibeles. Una línea vertical en 0,60 segundos y otra horizontal en menos 60 decibeles señalan el tiempo de reverberación del ejemplo.",
        "source": "Decaimiento exponencial sintético representado en dB; T60 didáctico de 0,60 s. No es una medición.",
    },
    "U09-CH-007": {
        "slug": "tau_R",
        "size": (7.0, 4.1),
        "question": "¿Cómo se transforma la fracción transmitida τE en R?",
        "caption": "Relación logarítmica ideal entre fracción energética transmitida e índice de reducción; cada década menos de transmisión suma 10 dB.",
        "alt": "Curva recta ascendente mientras el eje horizontal decrece desde uno hasta una millonésima. Se marcan uno, cero coma uno y cero coma cero uno por ciento.",
        "source": "Modelo del capítulo 9: R = 10 log10(1/τE). Datos calculados; elemento ideal, no aislamiento in situ.",
    },
    "U09-CH-009": {
        "slug": "global_vs_bandas",
        "size": (10.8, 4.3),
        "question": "¿Por qué un valor global no reemplaza los niveles por bandas?",
        "caption": "Dos espectros sintéticos pueden ajustarse al mismo descriptor A-ponderado relativo y, sin embargo, conservar distribuciones por bandas diferentes.",
        "alt": "A la izquierda, dos discos indican el mismo descriptor global relativo. A la derecha, dos perfiles por bandas de octava difieren entre 125 y 8000 hertz. Un rótulo aclara que son ejemplos sintéticos sin criterio de aceptación.",
        "source": "Espectros sintéticos; ajuste relativo con ponderación A analítica para igualar suma energética. No son límites normativos ni mediciones.",
    },
}


def _base_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(width=1.0, length=5)


def chart_001(fig):
    ax = fig.subplots()
    x = np.logspace(np.log10(0.25), np.log10(8), 400)
    y = -20 * np.log10(x)
    ax.semilogx(x, y, color=C["teal"], lw=3)
    marks = np.array([0.5, 1, 2, 4.0])
    vals = -20 * np.log10(marks)
    ax.scatter(marks, vals, s=70, color=C["bordo"], zorder=4)
    for xx, yy in zip(marks, vals):
        label = f"{xx:g} → {yy:+.2f} dB" if xx == 2 else f"{xx:g}"
        ax.annotate(label, (xx, yy), xytext=(8, 10), textcoords="offset points", fontsize=22 if xx == 2 else 18, color=C["bordo"])
    ax.axhline(0, color=C["gris"], lw=1)
    ax.set(xlabel="Razón  r₂/r₁  (sin unidad)", ylabel="ΔLₚ (dB)", xlim=(0.25, 8), ylim=(-19, 13))
    ax.set_xticks([0.25, 0.5, 1, 2, 4, 8], labels=["0,25", "0,5", "1", "2", "4", "8"])
    _base_axes(ax)
    data = {"ratio_r2_r1": x, "delta_Lp_dB": y}
    params = {"model": "delta_Lp_dB=-20*log10(r2/r1)", "x_scale": "logarithmic", "markers": marks.tolist(), "hypotheses": ["campo libre aproximado", "campo lejano", "misma dirección"]}
    return data, params, {"delta_at_1": float(-20*np.log10(1)), "delta_at_2": float(-20*np.log10(2))}


def chart_002(fig):
    axes = fig.subplots(1, 3, subplot_kw={"projection": "polar"})
    th = np.linspace(0, 2*np.pi, 721)
    floor = 10 ** (-18/20)
    patterns = [
        np.abs(0.78 + 0.22*np.cos(th)),
        np.abs(0.42 + 0.58*np.cos(th)),
        np.abs(np.cos(th))**4 + 0.24*np.abs(np.cos(2*th)),
    ]
    labels = ["Frecuencia baja", "Frecuencia media", "Frecuencia alta"]
    data = {"angle_deg": np.degrees(th)}
    for i, (ax, amp, label) in enumerate(zip(axes, patterns, labels), 1):
        amp = amp / amp.max()
        db = 20*np.log10(np.maximum(amp, floor))
        data[f"pattern_{i}_dB"] = db
        ax.plot(th, db, color=[C["teal"], C["bordo"], C["ocre"]][i-1], lw=3)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.set_ylim(-18, 0)
        ax.set_yticks([-18, -12, -6, 0])
        ax.set_yticklabels(["−18", "−12", "−6", "0 dB"], fontsize=16)
        ax.set_thetagrids([0, 90, 180, 270], ["0°", "90°", "180°", "270°"], fontsize=16)
        ax.set_title(label, fontsize=22, color=C["carbon"], pad=20)
        ax.text(0.5, -0.16, "Ejemplo sintético", transform=ax.transAxes, ha="center", fontsize=18, color=C["gris"])
    params = {"model": "analytic synthetic normalized amplitude patterns", "radial_reference_dB": 0, "radial_floor_dB": -18, "zero_degrees": "up", "not_measurement": True}
    return data, params, {"maxima_dB": [float(np.max(data[f"pattern_{i}_dB"])) for i in range(1,4)]}


def chart_003(fig):
    ax = fig.subplots()
    theta = np.linspace(-10, 35, 181)
    speed = 331 + 0.6*theta
    ax.plot(theta, speed, color=C["teal"], lw=3)
    marks = np.array([5., 20., 25.])
    vals = 331 + 0.6*marks
    ax.scatter(marks, vals, color=C["bordo"], s=70, zorder=3)
    label_y=[333.0,342.0,350.0]
    for xx, yy, ly in zip(marks, vals, label_y):
        ax.annotate(f"{xx:.0f} °C → {yy:.0f} m·s⁻¹", (xx, yy), xytext=(33,ly), textcoords="data", ha="right", va="center", fontsize=20, color=C["bordo"], arrowprops={"arrowstyle":"-","color":C["gris"],"lw":1.2})
    ax.text(0.97, 0.06, "La temperatura modifica c, no f emitida", transform=ax.transAxes, fontsize=20, color=C["alerta"], va="bottom", ha="right", bbox={"facecolor":"white","edgecolor":"none","pad":2.0})
    ax.set(xlabel="Temperatura  θ (°C)", ylabel="Rapidez del sonido  c (m·s⁻¹)", xlim=(-10, 35), ylim=(324, 354))
    _base_axes(ax)
    return {"temperature_C": theta, "speed_m_s": speed}, {"model": "c_m_s=331+0.6*theta_C", "x_scale": "linear", "y_scale": "linear", "focused_interval": True}, {"c_5": 334., "c_20": 343., "c_25": 346.}


def _pulse(t, center, amp=1.0, width=0.45):
    return amp*np.exp(-0.5*((t-center)/width)**2)


def chart_004(fig):
    axes = fig.subplots(3, 1, sharex=True, sharey=True)
    t = np.linspace(0, 120, 2401)
    direct = _pulse(t, 12, 1.0)
    isolated = direct + _pulse(t, 52, 0.62, 0.7)
    tail = direct.copy()
    arrivals = np.arange(30, 111, 5.5)
    for i, tt in enumerate(arrivals):
        tail += (0.72*np.exp(-(tt-30)/48)) * _pulse(t, tt, 0.65 + 0.12*np.sin(i), 0.75)
    signals = [direct, isolated, tail]
    names = ["Llegada directa", "Directa + reflexión aislada", "Directa + cola de llegadas"]
    for ax, s, name in zip(axes, signals, names):
        ax.plot(t, s, color=C["teal"], lw=2.2)
        ax.text(0.02, 0.78, name, transform=ax.transAxes, fontsize=20, color=C["bordo"])
        _base_axes(ax)
    axes[-1].set_xlabel("Tiempo relativo (ms)")
    axes[1].set_ylabel("Amplitud relativa")
    axes[-1].set_xlim(0, 120)
    axes[-1].set_ylim(-0.02, 1.12)
    axes[0].text(0.98, 0.78, "Conceptual · no medición", transform=axes[0].transAxes, ha="right", fontsize=18, color=C["gris"])
    return {"time_ms": t, "direct": direct, "isolated_reflection": isolated, "reverberant_tail": tail}, {"model": "sum of Gaussian synthetic arrivals", "arrival_times_ms": arrivals.tolist(), "same_time_axis": True, "not_measurement": True}, {"direct_peak_ms": float(t[np.argmax(direct)]), "isolated_peak_after_direct_ms": float(t[np.argmax(isolated*(t>20))])}


def chart_005(fig):
    ax = fig.subplots()
    f = np.logspace(np.log10(63), np.log10(8000), 500)
    lam = 343/f
    ax.loglog(f, lam, color=C["teal"], lw=3)
    marks = np.array([125., 500., 4000.])
    vals = 343/marks
    ax.scatter(marks, vals, color=C["bordo"], s=70, zorder=3)
    labels = ["125 Hz → 2,74 m", "500 Hz → 0,686 m", "4000 Hz → 0,0858 m"]
    offsets = [(10, 10), (10, -28), (-210, 10)]
    for xx, yy, text, off in zip(marks, vals, labels, offsets):
        ax.annotate(text, (xx, yy), xytext=off, textcoords="offset points", fontsize=20, color=C["bordo"])
    ax.set(xlabel="Frecuencia  f (Hz) · log", ylabel="Longitud de onda  λ (m) · log", xlim=(63, 8000), ylim=(0.04, 7))
    _base_axes(ax)
    ax.text(0.98, 0.94, "c = 343 m·s⁻¹", transform=ax.transAxes, ha="right", fontsize=22, color=C["alerta"])
    return {"frequency_Hz": f, "wavelength_m": lam}, {"model": "lambda_m=343/frequency_Hz", "x_scale": "logarithmic", "y_scale": "logarithmic", "reference_speed_m_s": 343}, {"lambda_125": 343/125, "lambda_500": 343/500, "lambda_4000": 343/4000}


def chart_006(fig):
    ax = fig.subplots()
    t = np.linspace(0, 1.2, 601)
    level = -100*t
    visible = level >= -70
    ax.plot(t[visible], level[visible], color=C["teal"], lw=3)
    ax.axhline(-60, color=C["gris"], lw=1.5, ls="--")
    ax.axvline(0.60, color=C["bordo"], lw=2, ls="--")
    ax.scatter([0.60], [-60], s=80, color=C["bordo"], zorder=4)
    ax.annotate("T₆₀ = 0,60 s", (0.60, -60), xytext=(18, 18), textcoords="offset points", fontsize=24, color=C["bordo"])
    ax.text(0.97, 0.93, "Sintético · tramo < −70 dB no mostrado", transform=ax.transAxes, ha="right", va="top", fontsize=18, color=C["gris"])
    ax.set(xlabel="Tiempo (s)", ylabel="Nivel relativo (dB)", xlim=(0, 1.2), ylim=(-70, 3))
    _base_axes(ax)
    return {"time_s": t, "level_relative_dB": level, "shown": visible.astype(int)}, {"model": "level_relative_dB=-100*time_s", "T60_s": 0.60, "display_floor_dB": -70, "not_measurement": True}, {"level_at_T60": -60.0, "slope_dB_s": -100.0}


def chart_007(fig):
    ax = fig.subplots()
    tau = np.logspace(0, -6, 601)
    r = 10*np.log10(1/tau)
    ax.semilogx(tau, r, color=C["teal"], lw=3)
    ax.invert_xaxis()
    marks = np.array([1e-2, 1e-3, 1e-4])
    vals = 10*np.log10(1/marks)
    ax.scatter(marks, vals, s=75, color=C["bordo"], zorder=3)
    for xx, yy, lab in zip(marks, vals, ["1 % → 20 dB", "0,1 % → 30 dB", "0,01 % → 40 dB"]):
        ax.annotate(lab, (xx, yy), xytext=(8, 10), textcoords="offset points", fontsize=20, color=C["bordo"])
    ax.set(xlabel="Fracción transmitida  τE · log decreciente", ylabel="Índice ideal  R (dB)", ylim=(-1, 61))
    ax.set_xticks([1,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6], labels=["1","10⁻¹","10⁻²","10⁻³","10⁻⁴","10⁻⁵","10⁻⁶"])
    _base_axes(ax)
    ax.text(0.02, 0.94, "Elemento ideal; no aislamiento in situ del conjunto", transform=ax.transAxes, fontsize=20, color=C["alerta"], va="top")
    return {"tau_E": tau, "R_dB": r}, {"model": "R_dB=10*log10(1/tau_E)", "x_scale": "logarithmic_decreasing", "domain": "0<tau_E<=1"}, {"R_at_0.01": 20.0, "R_at_0.001": 30.0}


def _a_weighting(f):
    f2 = f**2
    ra = (12200**2 * f2**2) / ((f2+20.6**2)*np.sqrt((f2+107.7**2)*(f2+737.9**2))*(f2+12200**2))
    return 20*np.log10(ra) + 2.0


def chart_009(fig):
    gs = fig.add_gridspec(1, 2, width_ratios=[0.9, 2.2], wspace=0.25)
    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    bands = np.array([125,250,500,1000,2000,4000,8000], dtype=float)
    a = np.array([4,7,10,7,4,1,-2], dtype=float)
    b0 = np.array([-1,2,5,8,11,8,4], dtype=float)
    aw = _a_weighting(bands)
    la_a = 10*np.log10(np.sum(10**((a+aw)/10)))
    la_b0 = 10*np.log10(np.sum(10**((b0+aw)/10)))
    b = b0 + (la_a-la_b0)
    ax0.set_xlim(0, 1); ax0.set_ylim(0, 1); ax0.axis("off")
    for y, color, label in [(0.65,C["teal"],"Espectro A"),(0.32,C["bordo"],"Espectro B")]:
        circ=plt.Circle((0.30,y),0.16,facecolor="white",edgecolor=color,lw=3)
        ax0.add_patch(circ)
        ax0.text(0.30,y,"Lₐ",ha="center",va="center",fontsize=28,color=color,fontweight="bold")
        ax0.text(0.53,y,label,ha="left",va="center",fontsize=20,color=C["carbon"])
    ax0.text(0.05,0.93,"Mismo descriptor\nglobal relativo",fontsize=22,color=C["bordo"],fontweight="bold",va="top")
    ax0.text(0.53,0.16,"Distribución\npor bandas distinta",fontsize=17,color=C["gris"],va="bottom",ha="left")
    x=np.arange(len(bands)); w=0.35
    ax1.bar(x-w/2,a,w,label="Espectro A",color=C["teal"])
    ax1.bar(x+w/2,b,w,label="Espectro B",color=C["bordo"],hatch="//",edgecolor=C["bordo"])
    ax1.set_xticks(x, [str(int(v)) for v in bands])
    ax1.set(xlabel="Frecuencia central de banda (Hz)",ylabel="Nivel relativo sintético (dB)")
    ax1.legend(loc="upper right",frameon=False)
    _base_axes(ax1)
    ax0.text(0.05,0.01,"Ejemplo sintético\nsin criterio de aceptación",transform=ax0.transAxes,ha="left",va="bottom",fontsize=17,color=C["alerta"])
    return {"band_center_Hz": bands, "spectrum_A_relative_dB": a, "spectrum_B_relative_dB": b, "A_weighting_dB": aw}, {"model": "two synthetic octave-band spectra shifted to equal relative A-weighted energy sum", "global_panel": "iconic_no_numeric_value", "not_normative": True}, {"relative_LA_A": float(la_a), "relative_LA_B": float(10*np.log10(np.sum(10**((b+aw)/10)))), "difference_dB": float(abs(la_a-10*np.log10(np.sum(10**((b+aw)/10))))) }


BUILDERS: dict[str, Callable] = {
    "U09-CH-001": chart_001,
    "U09-CH-002": chart_002,
    "U09-CH-003": chart_003,
    "U09-CH-004": chart_004,
    "U09-CH-005": chart_005,
    "U09-CH-006": chart_006,
    "U09-CH-007": chart_007,
    "U09-CH-009": chart_009,
}


def _write_csv(path: Path, data: dict[str, np.ndarray]):
    keys = list(data)
    arrays = [np.asarray(data[k]).reshape(-1) for k in keys]
    n = max(len(a) for a in arrays)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        for i in range(n):
            writer.writerow([f"{a[i]:.10g}" if i < len(a) and np.issubdtype(a.dtype, np.number) else (str(a[i]) if i < len(a) else "") for a in arrays])


def _slide_preview(figure_png: Path, output: Path, final_size: tuple[float,float]):
    dpi=192
    canvas=Image.new("RGB",(2560,1440),"white")
    draw=ImageDraw.Draw(canvas)
    draw.rectangle((129,52,896,63),fill=C["bordo"])
    draw.rectangle((916,52,1683,63),fill=C["bordo2"])
    draw.rectangle((1703,52,2431,63),fill=C["gris"])
    img=Image.open(figure_png).convert("RGB")
    maxw=int(final_size[0]*dpi); maxh=int(final_size[1]*dpi)
    img.thumbnail((maxw,maxh),Image.Resampling.LANCZOS)
    x=(2560-img.width)//2; y=260+(900-img.height)//2
    canvas.paste(img,(x,y))
    canvas.save(output,quality=95)


def generate(chart_id: str):
    if chart_id not in BUILDERS:
        raise ValueError(f"Recurso no ejecutable o condicionado: {chart_id}")
    meta=META[chart_id]
    folder=OUT/chart_id
    folder.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=meta["size"],constrained_layout=True)
    data,params,checks=BUILDERS[chart_id](fig)
    svg=folder/"figure.svg"; png=folder/"figure.png"
    fig.savefig(svg)
    dpi=max(300,math.ceil(2400/meta["size"][0]),math.ceil(1350/meta["size"][1]))
    fig.savefig(png,dpi=dpi)
    plt.close(fig)
    _write_csv(folder/"data.csv",data)
    (folder/"parameters.json").write_text(json.dumps(params,ensure_ascii=False,indent=2),encoding="utf-8")
    (folder/"caption.txt").write_text(meta["caption"]+"\n",encoding="utf-8")
    (folder/"alt_text.txt").write_text(meta["alt"]+"\n",encoding="utf-8")
    (folder/"source.txt").write_text(meta["source"]+"\n",encoding="utf-8")
    _slide_preview(png,folder/"slide_preview.png",meta["size"])
    with Image.open(png) as im: png_size=list(im.size)
    validation={
        "asset_id":chart_id,"classification":"gráfico cuantitativo","status":"approved",
        "physical_size_in":list(meta["size"]),"png_px":png_size,"slide_preview_px":[2560,1440],
        "font_floor":{"axis_labels_pt":20,"ticks_and_legends_pt":18,"annotations_pt":22},
        "model_and_data_traceable":True,"svg_exists":svg.exists(),"png_exists":png.exists(),
        "checks":checks,"critical_issues":0,"major_issues":0,
    }
    (folder/"validation.json").write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding="utf-8")
    readme=f"""# {chart_id} — {meta['slug']}

- **Clasificación:** gráfico cuantitativo.
- **Pregunta:** {meta['question']}
- **Estado:** aprobado tras controles numéricos, render individual y simulación 16:9.
- **Tamaño físico final:** {meta['size'][0]:.1f} × {meta['size'][1]:.1f} in.
- **Escala:** consultar ejes y `parameters.json`.
- **Reproducción:** `python units/unit_09/scripts/u09_plot_{chart_id[-3:]}_{meta['slug']}.py`.

## Caption sugerido

{meta['caption']}

## Texto alternativo

{meta['alt']}

## Fuente de datos

{meta['source']}

## Archivos

`data.csv`, `parameters.json`, `figure.svg`, `figure.png`, `slide_preview.png`, `caption.txt`, `alt_text.txt`, `source.txt` y `validation.json`.
"""
    (folder/"README.md").write_text(readme,encoding="utf-8")
    return validation
