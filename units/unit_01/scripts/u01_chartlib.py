from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from matplotlib.animation import FuncAnimation, PillowWriter
from PIL import Image, ImageDraw, ImageFont


UNIT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = UNIT_DIR / "assets" / "generated"
WIDE_FIGSIZE = (40 / 3, 7.5)

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
    "clinico_bg": "#F8EDE2",
    "ok": "#2F6F55",
    "alerta": "#9A641E",
    "error": "#A33A3A",
    "white": "#FFFFFF",
}

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Calibri", "Arial", "DejaVu Sans"],
        "font.size": 16,
        "axes.labelsize": 17,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "text.color": COLORS["carbon"],
        "axes.edgecolor": COLORS["carbon"],
        "axes.labelcolor": COLORS["carbon"],
        "xtick.color": COLORS["carbon"],
        "ytick.color": COLORS["carbon"],
        "svg.fonttype": "none",
        "figure.dpi": 160,
        "savefig.dpi": 180,
    }
)


def meta(
    chart_id: str,
    slug: str,
    title: str,
    slides: str,
    question: str,
    caption: str,
    alt: str,
    source: str,
    scale: str,
    validation: str,
):
    return {
        "id": chart_id,
        "slug": slug,
        "title": title,
        "slides": slides,
        "question": question,
        "caption": caption,
        "alt": alt,
        "source": source,
        "scale": scale,
        "validation": validation,
    }


METADATA = {
    "U01-CH001": meta(
        "U01-CH001",
        "fuente_medio_receptor",
        "Fuente–medio–receptor",
        "U01-001; U01-007–U01-009; U01-012; U01-014; U01-079",
        "¿Qué origina, transmite y recibe la perturbación?",
        "Modelo mínimo de una situación acústica: la fuente origina la perturbación, el medio permite su propagación y el receptor produce una respuesta.",
        "Tres bloques conectados de izquierda a derecha: fuente, medio y receptor. Debajo aparecen ejemplos y al final se distingue la respuesta del receptor.",
        "Libro del curso, Unidad 1, figura fuente–medio–receptor; elaboración propia.",
        "Diagrama cualitativo; no aplica escala.",
        "Tres roles diferenciados, conectores sin cruces y ninguna inferencia diagnóstica.",
    ),
    "U01-CH002": meta(
        "U01-CH002",
        "propagacion_particulas",
        "Propagación y oscilación local",
        "U01-010",
        "¿La materia viaja junto con la perturbación?",
        "La perturbación avanza por el medio mientras cada partícula oscila localmente alrededor de su posición de equilibrio.",
        "Tres estados temporales de una cadena de partículas. Una partícula roja se desplaza poco y vuelve cerca de su posición, mientras una zona comprimida avanza.",
        "Modelo conceptual propio basado en la sección sonido como perturbación mecánica del libro.",
        "Posición horizontal lineal, unidades arbitrarias; esquema conceptual no a escala.",
        "La partícula marcada no deriva con el frente y el GIF tiene una figura estática equivalente.",
    ),
    "U01-CH003": meta(
        "U01-CH003",
        "magnitud_valor_unidad",
        "Anatomía de una medición",
        "U01-017",
        "¿Qué función cumple cada parte de d = 2 m?",
        "En una medición, magnitud, símbolo, valor numérico y unidad cumplen funciones diferentes.",
        "Expresión d igual a 2 metros con cuatro llamadas que identifican magnitud, símbolo, valor numérico y unidad.",
        "Libro del curso, Unidad 1, sección magnitud, valor y unidad; elaboración propia.",
        "Diagrama tipográfico; no aplica escala.",
        "Variable en cursiva, unidad en redonda y espacio entre valor y unidad.",
    ),
    "U01-CH004": meta(
        "U01-CH004",
        "si_base_derivadas",
        "Magnitudes fundamentales y derivadas",
        "U01-019",
        "¿Cómo se construyen magnitudes derivadas desde magnitudes base?",
        "Tiempo, longitud y masa permiten construir varias magnitudes derivadas usadas en acústica.",
        "Tres magnitudes base en la parte superior se conectan con rapidez, aceleración, fuerza, presión y densidad.",
        "BIPM, SI Brochure, 9.ª edición, actualización 2026; NIST SP 1247; elaboración propia.",
        "Árbol conceptual; no aplica escala.",
        "Relaciones coherentes con SI y sin unidades fuera del alcance de la unidad.",
    ),
    "U01-CH005": meta(
        "U01-CH005",
        "construccion_unidades",
        "Construcción de unidades derivadas",
        "U01-021",
        "¿Qué operaciones producen m/s, N y Pa?",
        "Las operaciones entre magnitudes se conservan en las unidades derivadas.",
        "Tres cadenas muestran metro dividido segundo, kilogramo por metro sobre segundo cuadrado y newton dividido metro cuadrado.",
        "BIPM, SI Brochure, 9.ª edición; elaboración propia.",
        "Diagrama algebraico; no aplica escala.",
        "1 N = 1 kg·m/s² y 1 Pa = 1 N/m².",
    ),
    "U01-CH006": meta(
        "U01-CH006",
        "mapa_magnitudes",
        "Mapa de magnitudes de la Unidad 1",
        "U01-022",
        "¿Qué magnitudes, símbolos y unidades usaremos?",
        "El mapa reúne las magnitudes centrales sin reemplazar su explicación progresiva.",
        "Tabla de ocho filas con magnitud, símbolo, relación introductoria y unidad SI.",
        "Libro del curso, Unidad 1, tabla de magnitudes derivadas; elaboración propia.",
        "Tabla; no aplica escala.",
        "Símbolos y unidades coherentes con la guía de notación y máximo de ocho filas.",
    ),
    "U01-CH007": meta(
        "U01-CH007",
        "cinematica_propagacion",
        "Rapidez, velocidad y propagación",
        "U01-025–U01-027",
        "¿Cómo se distinguen rapidez, velocidad y propagación?",
        "Rapidez, velocidad vectorial y rapidez de propagación responden preguntas diferentes.",
        "Tres paneles muestran un trayecto sin dirección, un vector con sentido y un frente de perturbación que avanza mientras una partícula permanece local.",
        "Libro del curso, Unidad 1, sección rapidez, velocidad y velocidad de propagación; elaboración propia.",
        "Esquema conceptual lineal; no a escala.",
        "La partícula local no recorre el trayecto del frente y la rapidez no incluye dirección.",
    ),
    "U01-CH008": meta(
        "U01-CH008",
        "tiempo_propagacion",
        "Tiempo de propagación",
        "U01-028–U01-029",
        "¿Cómo se obtiene y verifica un tiempo de propagación?",
        "Para un modelo de rapidez constante, t = d/c y las unidades confirman que el resultado es un tiempo.",
        "Una fuente y un receptor separados 100 metros acompañan el cálculo 100 metros dividido 343 metros por segundo igual a 0,29 segundos.",
        "Libro del curso, Unidad 1, ejemplo de tiempo de propagación; valor c citado allí a partir de Cramer (1993).",
        "Trayecto conceptual; cálculo numérico exacto antes del redondeo.",
        "100/343 = 0,291545... s, redondeado a 0,29 s; c condicionado a aire cercano a 20 °C.",
    ),
    "U01-CH009": meta(
        "U01-CH009",
        "masa_peso",
        "Masa y peso",
        "U01-030–U01-031",
        "¿Qué cambia entre masa y peso?",
        "La masa caracteriza inercia y se expresa en kilogramos; el peso es una fuerza y se expresa en newtons.",
        "Dos paneles comparan un cuerpo ante una fuerza horizontal y el mismo cuerpo con una flecha gravitatoria vertical.",
        "Libro del curso, Unidad 1, sección masa y peso; elaboración propia.",
        "Esquema conceptual; no a escala.",
        "No se define masa como cantidad de materia; F_g se expresa en newtons.",
    ),
    "U01-CH010": meta(
        "U01-CH010",
        "fuerza_presion_densidad",
        "Fuerza, presión y densidad",
        "U01-032–U01-034",
        "¿Qué relación física expresa cada producto o cociente?",
        "Fuerza, presión y densidad relacionan magnitudes diferentes y conservan unidades específicas.",
        "Tres paneles: fuerza neta y aceleración, igual fuerza sobre áreas distintas, y masas distintas en volúmenes iguales.",
        "Libro del curso, Unidad 1, magnitudes derivadas; elaboración propia.",
        "Comparaciones conceptuales; no a escala.",
        "F = ma para masa constante y fuerza neta; p = F⊥/S; ρ = m/V.",
    ),
    "U01-CH011": meta(
        "U01-CH011",
        "red_magnitudes",
        "Red de magnitudes conectadas",
        "U01-024; U01-035",
        "¿Cómo se conectan las magnitudes de la unidad?",
        "Las relaciones forman una red y no una lista independiente de fórmulas.",
        "Red con distancia y tiempo hacia rapidez, masa y aceleración hacia fuerza, fuerza y área hacia presión, y masa y volumen hacia densidad.",
        "Libro del curso, Unidad 1, dependencias dimensionales; elaboración propia.",
        "Red conceptual; no aplica escala.",
        "Operaciones rotuladas y conectores sin cruces sobre etiquetas.",
    ),
    "U01-CH012": meta(
        "U01-CH012",
        "notacion_20uPa",
        "Notación científica y 20 µPa",
        "U01-036–U01-038",
        "¿Cómo representan el mismo valor el decimal, la potencia y el prefijo?",
        "0,000020 Pa, 2,0×10⁻⁵ Pa y 20 µPa representan el mismo valor.",
        "Tres tarjetas equivalentes muestran escritura decimal, científica y con prefijo micro.",
        "Libro del curso, Unidad 1, ejemplo de notación científica; elaboración propia.",
        "Potencias de diez; no aplica eje.",
        "Igualdad numérica exacta, coma decimal y prefijo micro correcto.",
    ),
    "U01-CH013": meta(
        "U01-CH013",
        "prefijos",
        "Prefijos frecuentes",
        "U01-039–U01-040",
        "¿Qué factor introduce cada prefijo?",
        "Kilo, mili y micro representan factores de 10³, 10⁻³ y 10⁻⁶.",
        "Escalera horizontal de potencias de diez con kilo, unidad, mili y micro, acompañada por ejemplos.",
        "BIPM, SI Brochure, 9.ª edición, actualización 2026; elaboración propia.",
        "Escala conceptual por potencias de diez.",
        "Mayúsculas y minúsculas correctas; la conversión no cambia la magnitud.",
    ),
    "U01-CH014": meta(
        "U01-CH014",
        "dependencias_dimensionales",
        "Dependencias dimensionales",
        "U01-041–U01-043; U01-087",
        "¿Qué expresiones tienen dimensiones compatibles?",
        "Las dimensiones [M], [L] y [T] permiten construir y controlar magnitudes derivadas.",
        "Mapa dimensional desde masa, longitud y tiempo hacia rapidez, aceleración, fuerza, presión y densidad, más una comparación de d/c, dc y c/d.",
        "Libro del curso, Unidad 1, figura de dependencias dimensionales; elaboración propia.",
        "Álgebra dimensional exacta.",
        "[d/c] = T; [dc] = L²T⁻¹; [c/d] = T⁻¹; compatibilidad es necesaria pero no suficiente.",
    ),
    "U01-CH015": meta(
        "U01-CH015",
        "funcion_distancia",
        "Distancia como función del tiempo",
        "U01-046–U01-047",
        "¿Cómo cuentan tabla, ecuación y gráfico la misma relación?",
        "Para c = 4,0 m/s, la tabla, la ecuación d(t)=ct y la recta representan el mismo modelo.",
        "Tabla de pares tiempo-distancia, ecuación central y gráfico lineal de 0 a 5 segundos y 0 a 20 metros.",
        "Modelo matemático exacto del libro; datos calculados, no medidos.",
        "Ejes lineales: t de 0 a 5 s; d de 0 a 20 m.",
        "d(5 s)=20 m, pendiente 4,0 m/s y dominio t≥0.",
    ),
    "U01-CH016": meta(
        "U01-CH016",
        "funcion_inversa",
        "Función directa e inversa",
        "U01-044–U01-051",
        "¿Cómo recupera la inversa la entrada?",
        "La función inversa intercambia entrada y salida cuando la correspondencia es única.",
        "Diagrama de ida d(t)=ct y vuelta t(d)=d/c, más un contraejemplo donde dos entradas llegan a la misma salida.",
        "Libro del curso, Unidad 1, figura función directa e inversa; elaboración propia.",
        "Diagrama de correspondencia; no aplica escala.",
        "Unicidad de salida, dominio indicado y unidades correctamente intercambiadas.",
    ),
    "U01-CH017": meta(
        "U01-CH017",
        "inversa_reciproco",
        "Inversa frente a recíproco",
        "U01-052",
        "¿Por qué f⁻¹ no es 1/f?",
        "Para f(x)=2x, la inversa es x/2 y el recíproco es 1/(2x).",
        "Dos tarjetas comparan la función inversa y el recíproco; una comprobación por composición recupera x.",
        "Libro del curso, Unidad 1, ejercicio sobre inversa y recíproco; elaboración propia.",
        "Álgebra exacta; variables adimensionales.",
        "f(f⁻¹(x))=x y el recíproco excluye x=0.",
    ),
    "U01-CH018": meta(
        "U01-CH018",
        "triangulo_razones",
        "Triángulo rectángulo y razones",
        "U01-053–U01-057; U01-090",
        "¿Qué lados compara cada razón trigonométrica?",
        "Seno, coseno y tangente comparan lados de un triángulo rectángulo respecto de un ángulo.",
        "Triángulo 3–4–5 con ángulo theta, lados opuesto, adyacente e hipotenusa, y las tres razones.",
        "Libro del curso, Unidad 1, sección trigonometría; elaboración propia.",
        "Geometría exacta en unidades relativas; razones adimensionales.",
        "Hipotenusa opuesta al ángulo recto y razones 3/5, 4/5 y 3/4.",
    ),
    "U01-CH019": meta(
        "U01-CH019",
        "circulo_unitario",
        "Círculo unitario y radianes",
        "U01-053; U01-058–U01-061; U01-090",
        "¿Cómo conectan grados, radianes y proyecciones?",
        "En el círculo unitario, cos θ y sin θ son proyecciones y una vuelta equivale a 2π rad.",
        "Círculo de radio uno con un ángulo de 45 grados, arco, proyecciones sobre ambos ejes y marcas de ángulos notables.",
        "Libro del curso, Unidad 1, figura círculo trigonométrico; elaboración propia.",
        "Ejes lineales adimensionales de -1,2 a 1,2.",
        "Radio unitario, 360°=2π rad y cos²θ+sin²θ=1.",
    ),
    "U01-CH020": meta(
        "U01-CH020",
        "exponencial_log",
        "Exponencial y logaritmo",
        "U01-062–U01-067",
        "¿Cómo se relacionan exponencial y logaritmo?",
        "Las funciones y=10ˣ e y=log₁₀(x) son inversas y sus gráficas se reflejan respecto de y=x.",
        "Gráfico común con curva exponencial, curva logarítmica, recta y=x y pares de puntos intercambiados.",
        "Funciones matemáticas exactas; elaboración propia.",
        "Ejes lineales comunes; ventana recortada para mostrar la inversión.",
        "Dominios correctos, pares (0,1)/(1,0) y reflejo respecto de y=x.",
    ),
    "U01-CH021": meta(
        "U01-CH021",
        "escalas_lineal_log",
        "Escala lineal y logarítmica",
        "U01-069",
        "¿Qué cambia al ubicar razones en una escala logarítmica?",
        "En una escala logarítmica, 1, 10, 100 y 1000 quedan igualmente separados.",
        "Dos ejes horizontales de igual ancho muestran las mismas cuatro razones en escala lineal y logarítmica.",
        "Valores matemáticos exactos; reconstrucción conceptual de la figura del libro.",
        "Panel superior lineal 0–1000; panel inferior log base 10 de 1 a 1000.",
        "Posiciones y rótulos exactos; no vincular la escala con percepción automática.",
    ),
    "U01-CH022": meta(
        "U01-CH022",
        "razon_db",
        "Razón de potencia y decibel",
        "U01-070–U01-071",
        "¿Cómo se transforma una razón de potencia en dB?",
        "Para una magnitud de tipo potencia, cada factor de diez agrega 10 dB.",
        "Gráfico de razón Q sobre Q0 igual a 1, 10, 100 y 1000 frente a niveles 0, 10, 20 y 30 dB.",
        "L_Q=10 log10(Q/Q0), modelo matemático exacto del libro.",
        "Eje x logarítmico de 1 a 1000; eje y lineal de 0 a 30 dB.",
        "Coeficiente 10, argumento adimensional y sin rótulos SPL, HL o SL.",
    ),
    "U01-CH023": meta(
        "U01-CH023",
        "matriz_clasificacion",
        "Físico, referido, perceptual y clínico",
        "U01-072–U01-080",
        "¿Qué tipo de dato representa cada elemento?",
        "Una medición física, un nivel referido, un atributo perceptual y una respuesta o conclusión clínica no son equivalentes.",
        "Cuatro columnas clasifican ejemplos: frecuencia, dB HL, altura tonal, respuesta detectado y conclusión clínica.",
        "Libro del curso, Unidad 1, tabla físico–perceptual y ejercicios F1–F3; elaboración propia.",
        "Matriz cualitativa; no aplica escala.",
        "Sin flechas deterministas y con color más rótulo textual.",
    ),
    "U01-CH024": meta(
        "U01-CH024",
        "caso_integrador",
        "Caso integrador de vocal al micrófono",
        "U01-081–U01-083",
        "¿Qué permite resolver el caso y qué queda fuera?",
        "El caso permite calcular tiempo, frecuencia y una relación en dB, pero no autoriza inferencias perceptuales o clínicas automáticas.",
        "Cadena vocalización–aire–micrófono con datos d, c, N, intervalo y razón Q/Q0; debajo se muestran tres resultados y tres límites.",
        "Libro del curso, Unidad 1, ejercicio integrador I1; elaboración propia.",
        "Escena conceptual; cálculos exactos.",
        "t=0,020 s, f=200 Hz, L_Q=20 dB y límites de calibración, pitch y clínica.",
    ),
    "U01-CH025": meta(
        "U01-CH025",
        "dependencias_curso",
        "Dependencias de la Unidad 1",
        "U01-084",
        "¿Qué conceptos de U1 necesita cada unidad futura?",
        "La Unidad 1 prepara mecánica, ondas y magnitudes acústicas.",
        "Unidad 1 en el centro se conecta con Unidad 2, Unidad 3 y Unidad 4, cada una con sus prerrequisitos principales.",
        "course_map.md y course_dependency_map.md; elaboración propia.",
        "Mapa curricular; no aplica escala.",
        "Solo dependencias documentadas y máximo cuatro nodos.",
    ),
    "U01-CH026": meta(
        "U01-CH026",
        "espectros_conceptuales",
        "Dos espectros conceptuales",
        "U01-076",
        "¿Por qué un espectro físico no equivale a timbre?",
        "Dos espectros físicos diferentes pueden compararse, pero el gráfico no predice por sí solo el timbre percibido.",
        "Dos gráficos de barras muestran componentes sintéticos entre 250 y 3000 Hz, con amplitud relativa normalizada.",
        "Datos sintéticos controlados, no mediciones; elaboración propia.",
        "Frecuencia lineal 0–4000 Hz; amplitud relativa 0–1.",
        "Datos declarados sintéticos, normalización explícita y máximo seis componentes.",
    ),
}


def new_canvas(figsize=WIDE_FIGSIZE):
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def box(ax, xy, width, height, text, fc="white", ec=None, color=None, fontsize=18, lw=1.5, ha="center"):
    ec = ec or COLORS["gris_2"]
    color = color or COLORS["carbon"]
    rect = patches.FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.012",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
    )
    ax.add_patch(rect)
    tx = xy[0] + (width / 2 if ha == "center" else 0.03)
    ax.text(tx, xy[1] + height / 2, text, ha=ha, va="center", fontsize=fontsize, color=color)
    return rect


def arrow(ax, start, end, text=None, color=None, lw=2.0, style="-|>"):
    color = color or COLORS["bordo_2"]
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={"arrowstyle": style, "lw": lw, "color": color, "shrinkA": 2, "shrinkB": 2},
    )
    if text:
        ax.text(
            (start[0] + end[0]) / 2,
            (start[1] + end[1]) / 2 + 0.035,
            text,
            ha="center",
            va="bottom",
            fontsize=14,
            color=color,
        )


def note(ax, text="Esquema conceptual · no a escala"):
    ax.text(0.99, 0.02, text, ha="right", va="bottom", fontsize=11, color=COLORS["gris"])


def chart01():
    fig, ax = new_canvas()
    boxes = [
        (0.06, "FUENTE", "origina la perturbación\nvoz · parlante · diapasón", COLORS["fisico_bg"], COLORS["fisico"]),
        (0.37, "MEDIO", "permite la propagación\naire · agua · sólido", COLORS["marfil"], COLORS["bordo"]),
        (0.68, "RECEPTOR", "responde a la perturbación\noído · micrófono · instrumento", COLORS["clinico_bg"], COLORS["clinico"]),
    ]
    for x, title, body, fc, ec in boxes:
        box(ax, (x, 0.38), 0.25, 0.28, f"{title}\n\n{body}", fc=fc, ec=ec, fontsize=17)
    arrow(ax, (0.31, 0.52), (0.37, 0.52), "perturbación")
    arrow(ax, (0.62, 0.52), (0.68, 0.52), "se propaga")
    ax.text(0.805, 0.26, "respuesta física, instrumental\no perceptual", ha="center", fontsize=15, color=COLORS["clinico"])
    arrow(ax, (0.805, 0.38), (0.805, 0.31), color=COLORS["clinico"])
    return fig, [
        ["role", "function", "examples"],
        ["Fuente", "Origina la perturbación", "voz; parlante; diapasón"],
        ["Medio", "Permite la propagación", "aire; agua; sólido"],
        ["Receptor", "Responde a la perturbación", "oído; micrófono; instrumento"],
    ]


def displacement(x, center, amp=0.16, width=0.65):
    return amp * np.exp(-((x - center) / width) ** 2)


def chart02():
    fig, ax = new_canvas()
    x = np.linspace(0.08, 0.92, 38)
    marked = int(np.argmin(np.abs(x - 0.52)))
    centers = [0.28, 0.52, 0.76]
    ys = [0.75, 0.50, 0.25]
    rows = [["state", "pulse_center_relative", "marked_particle_displacement_relative"]]
    for idx, (center, y0) in enumerate(zip(centers, ys), start=1):
        xi = displacement(x, center, amp=0.025, width=0.07)
        xp = x + xi
        ax.hlines(y0, 0.06, 0.94, color=COLORS["gris_2"], lw=1, linestyle="--")
        ax.scatter(xp, np.full_like(xp, y0), s=65, color=COLORS["fisico"], edgecolors="white", zorder=3)
        ax.scatter([xp[marked]], [y0], s=120, color=COLORS["bordo_2"], edgecolors="white", zorder=4)
        ax.axvspan(center - 0.035, center + 0.055, ymin=y0 - 0.045, ymax=y0 + 0.045, color=COLORS["fisico_bg"], alpha=0.9)
        ax.text(0.02, y0, f"t{idx}", ha="left", va="center", fontsize=16, color=COLORS["bordo"])
        ax.text(center, y0 + 0.075, "zona comprimida", ha="center", fontsize=13, color=COLORS["fisico"])
        rows.append([f"t{idx}", f"{center:.2f}", f"{xi[marked]:.5f}"])
    arrow(ax, (0.22, 0.90), (0.82, 0.90), "avance de la perturbación", color=COLORS["fisico"])
    ax.text(0.52, 0.10, "la partícula marcada oscila localmente", ha="center", fontsize=16, color=COLORS["bordo_2"])
    note(ax)
    return fig, rows


def chart03():
    fig, ax = new_canvas()
    ax.text(0.50, 0.58, r"$d = 2\ \mathrm{m}$", ha="center", va="center", fontsize=54, color=COLORS["carbon"])
    labels = [
        ((0.29, 0.74), (0.39, 0.61), "símbolo\nde la magnitud"),
        ((0.44, 0.31), (0.48, 0.53), "signo de\nigualdad"),
        ((0.61, 0.74), (0.56, 0.61), "valor\nnumérico"),
        ((0.73, 0.31), (0.62, 0.53), "unidad"),
    ]
    for pos, target, text in labels:
        box(ax, (pos[0] - 0.09, pos[1] - 0.06), 0.18, 0.12, text, fc=COLORS["marfil"], ec=COLORS["gris"], fontsize=15)
        arrow(ax, pos, target, color=COLORS["bordo_2"], lw=1.5, style="->")
    ax.text(0.50, 0.16, "magnitud: distancia", ha="center", fontsize=18, color=COLORS["fisico"])
    return fig, [
        ["component", "example", "meaning"],
        ["Magnitud", "distancia", "propiedad medida"],
        ["Símbolo", "d", "representa la magnitud"],
        ["Valor numérico", "2", "cantidad expresada en la unidad"],
        ["Unidad", "m", "metro"],
    ]


def chart04():
    fig, ax = new_canvas()
    base = [("TIEMPO", "s", 0.14), ("LONGITUD", "m", 0.42), ("MASA", "kg", 0.70)]
    for title, unit, x in base:
        box(ax, (x, 0.74), 0.18, 0.14, f"{title}\n{unit}", fc=COLORS["fisico_bg"], ec=COLORS["fisico"], fontsize=17)
    derived = [
        ("rapidez", "m/s", 0.05),
        ("aceleración", "m/s²", 0.23),
        ("fuerza", "N", 0.41),
        ("presión", "Pa", 0.59),
        ("densidad", "kg/m³", 0.77),
    ]
    for title, unit, x in derived:
        box(ax, (x, 0.20), 0.15, 0.15, f"{title}\n{unit}", fc="white", ec=COLORS["bordo_2"], fontsize=16)
    links = [
        ((0.23, 0.74), (0.125, 0.35)),
        ((0.51, 0.74), (0.125, 0.35)),
        ((0.23, 0.74), (0.305, 0.35)),
        ((0.51, 0.74), (0.305, 0.35)),
        ((0.79, 0.74), (0.485, 0.35)),
        ((0.305, 0.35), (0.485, 0.35)),
        ((0.485, 0.20), (0.665, 0.35)),
        ((0.51, 0.74), (0.665, 0.35)),
        ((0.79, 0.74), (0.845, 0.35)),
        ((0.51, 0.74), (0.845, 0.35)),
    ]
    for start, end in links:
        arrow(ax, start, end, color=COLORS["gris"], lw=1.2)
    ax.text(0.5, 0.52, "las magnitudes derivadas se definen mediante relaciones", ha="center", fontsize=18, color=COLORS["bordo"])
    return fig, [
        ["category", "quantity", "unit"],
        ["base", "tiempo", "s"],
        ["base", "longitud", "m"],
        ["base", "masa", "kg"],
        ["derived", "rapidez", "m/s"],
        ["derived", "aceleración", "m/s²"],
        ["derived", "fuerza", "N"],
        ["derived", "presión", "Pa"],
        ["derived", "densidad", "kg/m³"],
    ]


def chart05():
    fig, ax = new_canvas()
    entries = [
        (0.72, r"$\mathrm{m}\ /\ \mathrm{s}$", "distancia ÷ tiempo", "rapidez"),
        (0.45, r"$\mathrm{kg}\cdot\mathrm{m}/\mathrm{s}^{2}=\mathrm{N}$", "masa × aceleración", "fuerza"),
        (0.18, r"$\mathrm{N}/\mathrm{m}^{2}=\mathrm{Pa}$", "fuerza ÷ área", "presión"),
    ]
    for y, formula, operation, result in entries:
        box(ax, (0.09, y - 0.08), 0.52, 0.16, formula, fc=COLORS["marfil"], ec=COLORS["gris_2"], fontsize=25)
        arrow(ax, (0.62, y), (0.72, y), operation, color=COLORS["fisico"])
        box(ax, (0.73, y - 0.07), 0.18, 0.14, result, fc=COLORS["fisico_bg"], ec=COLORS["fisico"], fontsize=18)
    ax.text(0.50, 0.91, "la operación física también aparece en la unidad", ha="center", fontsize=19, color=COLORS["bordo"])
    return fig, [
        ["quantity", "relation", "unit_identity"],
        ["rapidez", "distancia/tiempo", "m/s"],
        ["fuerza", "masa×aceleración", "kg·m/s²=N"],
        ["presión", "fuerza/área", "N/m²=Pa"],
    ]


def chart06():
    fig, ax = new_canvas()
    ax.axis("off")
    cols = ["Magnitud", "Símbolo", "Relación introductoria", "Unidad SI"]
    rows = [
        ["Distancia", "d", "—", "m"],
        ["Tiempo", "t, Δt", "—", "s"],
        ["Rapidez media", "v_med", "d/Δt", "m/s"],
        ["Aceleración", "a", "Δv/Δt", "m/s²"],
        ["Fuerza / peso", "F, F_g", "ma, mg", "N"],
        ["Presión", "p", r"$F_{\perp}/S$", "Pa"],
        ["Densidad", "ρ", "m/V", "kg/m³"],
        ["Frecuencia", "f", "N/Δt", "Hz"],
    ]
    table = ax.table(cellText=rows, colLabels=cols, loc="center", cellLoc="center", colWidths=[0.22, 0.16, 0.34, 0.20])
    table.auto_set_font_size(False)
    table.set_fontsize(16)
    table.scale(1, 2.1)
    for (r, c), cell in table.get_celld().items():
        cell.set_linewidth(0.8)
        cell.set_edgecolor(COLORS["gris_2"])
        if r == 0:
            cell.set_facecolor(COLORS["bordo"])
            cell.get_text().set_color("white")
            cell.get_text().set_weight("bold")
        elif r % 2 == 0:
            cell.set_facecolor(COLORS["marfil"])
    return fig, [["quantity", "symbol", "relation", "unit"]] + rows


def chart07():
    fig, ax = new_canvas()
    panel_x = [0.04, 0.36, 0.68]
    titles = ["RAPIDEZ", "VELOCIDAD", "PROPAGACIÓN"]
    subtitles = ["cuánto por unidad de tiempo", "módulo, dirección y sentido", "avance de la perturbación"]
    for x0, title, subtitle in zip(panel_x, titles, subtitles):
        box(ax, (x0, 0.16), 0.28, 0.68, "", fc="white", ec=COLORS["gris_2"])
        ax.text(x0 + 0.14, 0.76, title, ha="center", fontsize=19, color=COLORS["bordo"], weight="bold")
        ax.text(x0 + 0.14, 0.68, subtitle, ha="center", fontsize=13, color=COLORS["carbon"])
    ax.plot([0.09, 0.27], [0.40, 0.40], color=COLORS["fisico"], lw=4)
    ax.scatter([0.09, 0.27], [0.40, 0.40], color=COLORS["fisico"], s=60)
    ax.text(0.18, 0.32, r"$v_\mathrm{med}=d/\Delta t$", ha="center", fontsize=18)
    arrow(ax, (0.41, 0.38), (0.59, 0.55), color=COLORS["bordo_2"], lw=3)
    ax.text(0.50, 0.30, "vector", ha="center", fontsize=17)
    particles = np.linspace(0.72, 0.92, 13)
    ax.scatter(particles, np.full_like(particles, 0.40), s=45, color=COLORS["fisico"])
    ax.axvspan(0.80, 0.84, ymin=0.34, ymax=0.50, color=COLORS["fisico_bg"])
    arrow(ax, (0.76, 0.56), (0.90, 0.56), "frente", color=COLORS["fisico"])
    ax.scatter([0.83], [0.40], s=100, color=COLORS["bordo_2"], zorder=4)
    ax.text(0.82, 0.27, "partícula local", ha="center", fontsize=14, color=COLORS["bordo_2"])
    note(ax)
    return fig, [
        ["concept", "includes_direction", "description"],
        ["rapidez", "no", "distancia por intervalo"],
        ["velocidad", "sí", "módulo, dirección y sentido"],
        ["rapidez de propagación", "no en el uso introductorio", "avance de la perturbación"],
    ]


def chart08():
    fig, ax = new_canvas()
    ax.scatter([0.10], [0.66], s=550, color=COLORS["bordo_2"], marker="o")
    ax.text(0.10, 0.54, "fuente", ha="center", fontsize=16)
    ax.scatter([0.90], [0.66], s=550, color=COLORS["clinico"], marker="s")
    ax.text(0.90, 0.54, "receptor", ha="center", fontsize=16)
    arrow(ax, (0.14, 0.66), (0.86, 0.66), r"$d=100\ \mathrm{m}$", color=COLORS["fisico"], lw=3)
    box(ax, (0.18, 0.18), 0.64, 0.24, r"$t=\dfrac{d}{c}=\dfrac{100\ \mathrm{m}}{343\ \mathrm{m/s}}=0{,}29\ \mathrm{s}$", fc=COLORS["marfil"], ec=COLORS["bordo_2"], fontsize=25)
    ax.text(0.50, 0.10, r"$\mathrm{m}\div(\mathrm{m/s})=\mathrm{s}$", ha="center", fontsize=19, color=COLORS["ok"])
    ax.text(0.50, 0.86, "modelo: rapidez constante · aire cercano a 20 °C", ha="center", fontsize=15, color=COLORS["gris"])
    return fig, [
        ["distance_m", "speed_m_s", "time_s_exact", "time_s_rounded"],
        ["100", "343", f"{100/343:.9f}", "0.29"],
    ]


def chart09():
    fig, ax = new_canvas()
    box(ax, (0.05, 0.16), 0.42, 0.68, "", fc=COLORS["fisico_bg"], ec=COLORS["fisico"])
    box(ax, (0.53, 0.16), 0.42, 0.68, "", fc=COLORS["clinico_bg"], ec=COLORS["clinico"])
    ax.text(0.26, 0.75, "MASA", ha="center", fontsize=22, color=COLORS["fisico"], weight="bold")
    ax.text(0.74, 0.75, "PESO", ha="center", fontsize=22, color=COLORS["clinico"], weight="bold")
    ax.add_patch(patches.Rectangle((0.19, 0.38), 0.14, 0.16, fc="white", ec=COLORS["carbon"], lw=2))
    arrow(ax, (0.12, 0.46), (0.18, 0.46), "F", color=COLORS["fisico"])
    ax.text(0.26, 0.29, "inercia\nkg", ha="center", fontsize=18)
    ax.add_patch(patches.Rectangle((0.67, 0.45), 0.14, 0.16, fc="white", ec=COLORS["carbon"], lw=2))
    arrow(ax, (0.74, 0.45), (0.74, 0.30), r"$F_g$", color=COLORS["clinico"], lw=3)
    ax.text(0.74, 0.22, r"$F_g=mg$ · N", ha="center", fontsize=19)
    ax.text(0.50, 0.07, "la masa puede conservarse aunque cambie g; el peso cambia", ha="center", fontsize=17, color=COLORS["bordo"])
    return fig, [
        ["quantity", "meaning", "unit", "relation"],
        ["masa", "caracteriza la inercia", "kg", "—"],
        ["peso", "fuerza gravitatoria", "N", "F_g=m g"],
    ]


def chart10():
    fig, axes = plt.subplots(1, 3, figsize=WIDE_FIGSIZE)
    fig.patch.set_facecolor("white")
    titles = ["FUERZA", "PRESIÓN", "DENSIDAD"]
    for ax, title in zip(axes, titles):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
        ax.text(0.5, 0.92, title, ha="center", fontsize=21, color=COLORS["bordo"], weight="bold")
    a = axes[0]
    a.add_patch(patches.Rectangle((0.36, 0.38), 0.28, 0.22, fc=COLORS["fisico_bg"], ec=COLORS["fisico"], lw=2))
    arrow(a, (0.18, 0.49), (0.34, 0.49), r"$F_\mathrm{neta}$", color=COLORS["fisico"], lw=3)
    arrow(a, (0.66, 0.49), (0.84, 0.49), r"$a$", color=COLORS["bordo_2"], lw=3)
    a.text(0.5, 0.24, r"$F=ma$", ha="center", fontsize=24)
    b = axes[1]
    for x, w in [(0.10, 0.28), (0.62, 0.10)]:
        b.add_patch(patches.Rectangle((x, 0.32), w, 0.12, fc=COLORS["fisico_bg"], ec=COLORS["fisico"], lw=2))
        arrow(b, (x + w / 2, 0.72), (x + w / 2, 0.47), r"$F_\perp$", color=COLORS["bordo_2"], lw=3)
    b.text(0.5, 0.20, r"$p=F_\perp/S$", ha="center", fontsize=24)
    b.text(0.24, 0.50, "área mayor", ha="center", fontsize=13)
    b.text(0.67, 0.50, "área menor", ha="center", fontsize=13)
    c = axes[2]
    for x, count in [(0.12, 5), (0.62, 10)]:
        c.add_patch(patches.Rectangle((x, 0.30), 0.26, 0.26, fc="white", ec=COLORS["fisico"], lw=2))
        rng = np.random.default_rng(count)
        pts = rng.uniform([x + 0.03, 0.33], [x + 0.23, 0.53], size=(count, 2))
        c.scatter(pts[:, 0], pts[:, 1], s=35, color=COLORS["bordo_2"])
    c.text(0.5, 0.20, r"$\rho=m/V$", ha="center", fontsize=24)
    c.text(0.50, 0.08, "comparaciones conceptuales · no a escala", ha="center", fontsize=11, color=COLORS["gris"])
    fig.tight_layout(w_pad=1.2)
    return fig, [
        ["panel", "relation", "unit"],
        ["fuerza", "F=m a", "N"],
        ["presión", "p=F_perp/S", "Pa"],
        ["densidad", "rho=m/V", "kg/m³"],
    ]


def chart11():
    fig, ax = new_canvas()
    nodes = {
        "d": (0.08, 0.72, "distancia\nd · m"),
        "t": (0.08, 0.30, "tiempo\nΔt · s"),
        "v": (0.32, 0.52, "rapidez\nv · m/s"),
        "a": (0.32, 0.18, "aceleración\na · m/s²"),
        "m": (0.54, 0.78, "masa\nm · kg"),
        "F": (0.58, 0.48, "fuerza\nF · N"),
        "S": (0.80, 0.72, "área\nS · m²"),
        "p": (0.82, 0.42, "presión\np · Pa"),
        "V": (0.58, 0.16, "volumen\nV · m³"),
        "rho": (0.82, 0.16, "densidad\nρ · kg/m³"),
    }
    for key, (x, y, text) in nodes.items():
        fc = COLORS["fisico_bg"] if key in {"d", "t", "m", "S", "V"} else "white"
        box(ax, (x, y), 0.14, 0.11, text, fc=fc, ec=COLORS["fisico"] if fc != "white" else COLORS["bordo_2"], fontsize=13)
    arrows = [
        ("d", "v", "÷ Δt"),
        ("t", "v", ""),
        ("v", "a", "÷ Δt"),
        ("m", "F", "× a"),
        ("F", "p", "÷ S"),
        ("S", "p", ""),
        ("m", "rho", "÷ V"),
        ("V", "rho", ""),
    ]
    for s, e, txt in arrows:
        sx, sy, _ = nodes[s]
        ex, ey, _ = nodes[e]
        arrow(ax, (sx + 0.14, sy + 0.055), (ex, ey + 0.055), txt, color=COLORS["gris"], lw=1.5)
    note(ax, "Relaciones introductorias · esquema conceptual")
    return fig, [["node", "label", "unit"]] + [[k, v[2].split("\n")[0], v[2].split("·")[-1].strip()] for k, v in nodes.items()]


def chart12():
    fig, ax = new_canvas()
    cards = [
        (0.06, "ESCRITURA DECIMAL", r"$0{,}000020\ \mathrm{Pa}$"),
        (0.37, "NOTACIÓN CIENTÍFICA", r"$2{,}0\times10^{-5}\ \mathrm{Pa}$"),
        (0.68, "CON PREFIJO", r"$20\ \mathrm{\mu Pa}$"),
    ]
    for x, title, value in cards:
        box(ax, (x, 0.34), 0.25, 0.32, "", fc=COLORS["marfil"], ec=COLORS["gris_2"])
        ax.text(x + 0.125, 0.58, title, ha="center", fontsize=14, color=COLORS["bordo"], weight="bold")
        ax.text(x + 0.125, 0.45, value, ha="center", fontsize=25)
    ax.text(0.50, 0.78, "tres escrituras · el mismo valor", ha="center", fontsize=23, color=COLORS["fisico"])
    arrow(ax, (0.31, 0.50), (0.37, 0.50), "=", color=COLORS["bordo_2"])
    arrow(ax, (0.62, 0.50), (0.68, 0.50), "=", color=COLORS["bordo_2"])
    ax.text(0.50, 0.20, r"$\mu=10^{-6}$", ha="center", fontsize=20, color=COLORS["bordo"])
    return fig, [["decimal_Pa", "scientific_Pa", "microPa"], ["0.000020", "2.0e-5", "20"]]


def chart13():
    fig, ax = new_canvas()
    xs = [0.12, 0.38, 0.64, 0.88]
    labels = [("kilo", "k", "10³"), ("unidad", "—", "10⁰"), ("mili", "m", "10⁻³"), ("micro", "µ", "10⁻⁶")]
    ax.plot([0.12, 0.88], [0.52, 0.52], color=COLORS["gris_2"], lw=4)
    for x, (name, symbol, factor) in zip(xs, labels):
        ax.scatter([x], [0.52], s=230, color=COLORS["fisico"] if name != "unidad" else COLORS["bordo_2"], zorder=3)
        ax.text(x, 0.68, name, ha="center", fontsize=18, color=COLORS["bordo"], weight="bold")
        ax.text(x, 0.58, symbol, ha="center", fontsize=20)
        ax.text(x, 0.38, factor, ha="center", fontsize=22)
    ax.text(0.50, 0.18, "cada paso hacia la derecha divide por 10³", ha="center", fontsize=18, color=COLORS["fisico"])
    return fig, [["prefix", "symbol", "factor"]] + [[a, b, c] for a, b, c in labels]


def chart14():
    fig, ax = new_canvas()
    top = [("[M]", 0.12), ("[L]", 0.34), ("[T]", 0.56)]
    for text, x in top:
        box(ax, (x, 0.78), 0.14, 0.10, text, fc=COLORS["fisico_bg"], ec=COLORS["fisico"], fontsize=21)
    derived = [
        ("rapidez", r"$LT^{-1}$", 0.08, 0.52),
        ("aceleración", r"$LT^{-2}$", 0.29, 0.52),
        ("fuerza", r"$MLT^{-2}$", 0.50, 0.52),
        ("presión", r"$ML^{-1}T^{-2}$", 0.71, 0.52),
        ("densidad", r"$ML^{-3}$", 0.71, 0.27),
    ]
    for name, dim, x, y in derived:
        box(ax, (x, y), 0.17, 0.12, f"{name}\n{dim}", fc="white", ec=COLORS["bordo_2"], fontsize=15)
    for start, end in [
        ((0.41, 0.78), (0.165, 0.64)),
        ((0.63, 0.78), (0.165, 0.64)),
        ((0.41, 0.78), (0.375, 0.64)),
        ((0.63, 0.78), (0.375, 0.64)),
        ((0.19, 0.78), (0.585, 0.64)),
        ((0.375, 0.52), (0.585, 0.64)),
        ((0.585, 0.52), (0.795, 0.64)),
        ((0.41, 0.78), (0.795, 0.64)),
        ((0.19, 0.78), (0.795, 0.39)),
        ((0.41, 0.78), (0.795, 0.39)),
    ]:
        arrow(ax, start, end, color=COLORS["gris"], lw=1.2)
    box(ax, (0.08, 0.12), 0.55, 0.13, r"$[d/c]=T\quad [dc]=L^2T^{-1}\quad [c/d]=T^{-1}$", fc=COLORS["marfil"], ec=COLORS["gris_2"], fontsize=20)
    ax.text(0.68, 0.15, "solo d/c puede representar tiempo", fontsize=15, color=COLORS["ok"], ha="left")
    note(ax, "Compatibilidad dimensional: necesaria, no suficiente")
    return fig, [
        ["quantity", "dimension"],
        ["rapidez", "L T^-1"],
        ["aceleración", "L T^-2"],
        ["fuerza", "M L T^-2"],
        ["presión", "M L^-1 T^-2"],
        ["densidad", "M L^-3"],
        ["d/c", "T"],
        ["d*c", "L^2 T^-1"],
        ["c/d", "T^-1"],
    ]


def chart15():
    fig = plt.figure(figsize=WIDE_FIGSIZE, facecolor="white")
    gs = fig.add_gridspec(1, 3, width_ratios=[0.85, 0.8, 1.7], wspace=0.35)
    ax_table = fig.add_subplot(gs[0, 0])
    ax_eq = fig.add_subplot(gs[0, 1])
    ax = fig.add_subplot(gs[0, 2])
    t = np.array([0, 1, 2, 3, 4, 5], dtype=float)
    d = 4.0 * t
    ax_table.axis("off")
    table = ax_table.table(
        cellText=[[f"{ti:.0f}", f"{di:.0f}"] for ti, di in zip(t, d)],
        colLabels=["t (s)", "d (m)"],
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(16)
    table.scale(1.1, 1.9)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor(COLORS["gris_2"])
        if r == 0:
            cell.set_facecolor(COLORS["bordo"])
            cell.get_text().set_color("white")
    ax_eq.axis("off")
    ax_eq.text(0.5, 0.58, r"$d(t)=ct$", ha="center", fontsize=31, color=COLORS["bordo"])
    ax_eq.text(0.5, 0.43, r"$c=4{,}0\ \mathrm{m/s}$", ha="center", fontsize=23)
    ax_eq.text(0.5, 0.28, r"$t\geq 0$", ha="center", fontsize=18, color=COLORS["gris"])
    ax.plot(t, d, color=COLORS["fisico"], lw=3, marker="o", ms=7)
    ax.set_xlabel("tiempo, t (s)")
    ax.set_ylabel("distancia, d (m)")
    ax.set_xlim(0, 5.2)
    ax.set_ylim(0, 21)
    ax.set_xticks(np.arange(0, 6, 1))
    ax.set_yticks(np.arange(0, 21, 4))
    ax.grid(True, color=COLORS["gris_2"], lw=0.8)
    ax.annotate("4 m por cada 1 s", xy=(3, 12), xytext=(1.9, 17), arrowprops={"arrowstyle": "->", "color": COLORS["bordo_2"]}, color=COLORS["bordo_2"], fontsize=15)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    return fig, [["time_s", "distance_m"]] + [[f"{ti:.1f}", f"{di:.1f}"] for ti, di in zip(t, d)]


def chart16():
    fig, ax = new_canvas()
    box(ax, (0.05, 0.58), 0.18, 0.14, r"$t$ (s)", fc=COLORS["fisico_bg"], ec=COLORS["fisico"], fontsize=24)
    box(ax, (0.41, 0.58), 0.18, 0.14, r"$d=ct$ (m)", fc=COLORS["marfil"], ec=COLORS["bordo_2"], fontsize=23)
    box(ax, (0.77, 0.58), 0.18, 0.14, r"$d$ (m)", fc=COLORS["fisico_bg"], ec=COLORS["fisico"], fontsize=24)
    arrow(ax, (0.23, 0.65), (0.41, 0.65), "entrada", color=COLORS["fisico"])
    arrow(ax, (0.59, 0.65), (0.77, 0.65), "salida", color=COLORS["fisico"])
    arrow(ax, (0.86, 0.54), (0.14, 0.54), r"inversa: $t=d/c$", color=COLORS["bordo_2"])
    ax.text(0.50, 0.43, "la inversa recupera la entrada", ha="center", fontsize=18, color=COLORS["bordo"])
    box(ax, (0.10, 0.12), 0.80, 0.20, "", fc="white", ec=COLORS["gris_2"])
    ax.text(0.18, 0.25, "contraejemplo", fontsize=15, color=COLORS["alerta"], weight="bold")
    ax.text(0.38, 0.22, "−2", ha="center", fontsize=18)
    ax.text(0.38, 0.14, "+2", ha="center", fontsize=18)
    ax.text(0.72, 0.18, "4", ha="center", fontsize=20)
    arrow(ax, (0.42, 0.24), (0.68, 0.19), color=COLORS["gris"], lw=1.3)
    arrow(ax, (0.42, 0.15), (0.68, 0.17), color=COLORS["gris"], lw=1.3)
    ax.text(0.82, 0.18, "dos entradas\npara una salida", ha="center", fontsize=14, color=COLORS["error"])
    return fig, [
        ["model", "input", "rule", "output", "invertible"],
        ["propagación constante", "t (s)", "d=c t", "d (m)", "sí para c>0 y t≥0"],
        ["square example", "-2;2", "x²", "4", "no en todo R"],
    ]


def chart17():
    fig, ax = new_canvas()
    box(ax, (0.05, 0.24), 0.42, 0.56, "", fc=COLORS["fisico_bg"], ec=COLORS["fisico"])
    box(ax, (0.53, 0.24), 0.42, 0.56, "", fc=COLORS["clinico_bg"], ec=COLORS["clinico"])
    ax.text(0.26, 0.70, "FUNCIÓN INVERSA", ha="center", fontsize=21, color=COLORS["fisico"], weight="bold")
    ax.text(0.74, 0.70, "RECÍPROCO", ha="center", fontsize=21, color=COLORS["clinico"], weight="bold")
    ax.text(0.26, 0.54, r"$f(x)=2x$", ha="center", fontsize=25)
    ax.text(0.26, 0.42, r"$f^{-1}(x)=x/2$", ha="center", fontsize=28, color=COLORS["bordo"])
    ax.text(0.26, 0.31, r"$f(f^{-1}(x))=x$", ha="center", fontsize=19, color=COLORS["ok"])
    ax.text(0.74, 0.54, r"$f(x)=2x$", ha="center", fontsize=25)
    ax.text(0.74, 0.42, r"$1/f(x)=1/(2x)$", ha="center", fontsize=27, color=COLORS["bordo"])
    ax.text(0.74, 0.31, r"$x\neq 0$", ha="center", fontsize=19, color=COLORS["alerta"])
    ax.text(0.50, 0.12, "recuperar una entrada no es invertir un valor", ha="center", fontsize=19, color=COLORS["bordo"])
    return fig, [
        ["expression", "result", "meaning"],
        ["inverse of f(x)=2x", "x/2", "recovers input"],
        ["reciprocal of f(x)=2x", "1/(2x)", "inverse of function value"],
    ]


def chart18():
    fig, ax = new_canvas()
    pts = np.array([[0.12, 0.18], [0.12, 0.78], [0.72, 0.18]])
    tri = patches.Polygon(pts, closed=True, fc=COLORS["fisico_bg"], ec=COLORS["fisico"], lw=3)
    ax.add_patch(tri)
    ax.add_patch(patches.Rectangle((0.12, 0.18), 0.06, 0.06, fc="white", ec=COLORS["carbon"], lw=1.5))
    ax.text(0.16, 0.83, "opuesto = 3", fontsize=17, color=COLORS["bordo"])
    ax.text(0.37, 0.10, "adyacente = 4", fontsize=17, color=COLORS["bordo"])
    ax.text(0.43, 0.52, "hipotenusa = 5", fontsize=17, color=COLORS["fisico"], rotation=-45)
    ax.text(0.64, 0.22, r"$\theta$", fontsize=24, color=COLORS["bordo_2"])
    formulas = [(r"$\sin\theta=3/5$", 0.82, 0.66), (r"$\cos\theta=4/5$", 0.82, 0.48), (r"$\tan\theta=3/4$", 0.82, 0.30)]
    for formula, x, y in formulas:
        box(ax, (x - 0.14, y - 0.06), 0.28, 0.12, formula, fc=COLORS["marfil"], ec=COLORS["gris_2"], fontsize=21)
    ax.text(0.82, 0.16, "razones adimensionales", ha="center", fontsize=15, color=COLORS["gris"])
    return fig, [
        ["side_or_ratio", "value"],
        ["opposite", "3"],
        ["adjacent", "4"],
        ["hypotenuse", "5"],
        ["sin(theta)", "0.6"],
        ["cos(theta)", "0.8"],
        ["tan(theta)", "0.75"],
    ]


def chart19():
    fig, ax = plt.subplots(figsize=WIDE_FIGSIZE, facecolor="white")
    theta = np.deg2rad(45)
    ax.set_aspect("equal")
    circle = patches.Circle((0, 0), 1, fc="none", ec=COLORS["fisico"], lw=3)
    ax.add_patch(circle)
    ax.axhline(0, color=COLORS["gris"], lw=1)
    ax.axvline(0, color=COLORS["gris"], lw=1)
    x, y = np.cos(theta), np.sin(theta)
    ax.plot([0, x], [0, y], color=COLORS["bordo_2"], lw=3)
    ax.plot([x, x], [0, y], color=COLORS["clinico"], lw=2, linestyle="--")
    ax.plot([0, x], [y, y], color=COLORS["fisico"], lw=2, linestyle="--")
    arc = patches.Arc((0, 0), 0.45, 0.45, theta1=0, theta2=45, color=COLORS["bordo"], lw=2)
    ax.add_patch(arc)
    ax.text(0.25, 0.10, r"$\theta$", fontsize=22, color=COLORS["bordo"])
    ax.text(x / 2, y + 0.08, "radio = 1", ha="center", fontsize=16)
    ax.text(x / 2, y - 0.12, r"$\cos\theta$", ha="center", fontsize=18, color=COLORS["fisico"])
    ax.text(x + 0.10, y / 2, r"$\sin\theta$", ha="left", fontsize=18, color=COLORS["clinico"])
    labels = [(1.08, 0, "0\n2π"), (0, 1.12, "π/2"), (-1.12, 0, "π"), (0, -1.15, "3π/2")]
    for lx, ly, text in labels:
        ax.text(lx, ly, text, ha="center", va="center", fontsize=15)
    ax.set_xlim(-1.35, 1.65)
    ax.set_ylim(-1.25, 1.25)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel("coordenada horizontal (adimensional)")
    ax.set_ylabel("coordenada vertical (adimensional)")
    ax.grid(True, color=COLORS["gris_2"], lw=0.6)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.text(1.35, -1.08, "360° = 2π rad", ha="center", fontsize=19, color=COLORS["bordo"])
    return fig, [
        ["theta_deg", "theta_rad", "cos_theta", "sin_theta"],
        ["45", f"{theta:.9f}", f"{x:.9f}", f"{y:.9f}"],
    ]


def chart20():
    fig, ax = plt.subplots(figsize=WIDE_FIGSIZE, facecolor="white")
    x_exp = np.linspace(-1.3, 0.40, 400)
    y_exp = 10 ** x_exp
    x_log = np.linspace(0.05, 2.5, 400)
    y_log = np.log10(x_log)
    ax.plot(x_exp, y_exp, color=COLORS["fisico"], lw=3, label=r"$y=10^x$")
    ax.plot(x_log, y_log, color=COLORS["clinico"], lw=3, label=r"$y=\log_{10}(x)$")
    ax.plot([-1.3, 2.5], [-1.3, 2.5], color=COLORS["gris"], lw=1.5, linestyle="--", label=r"$y=x$")
    pairs = [((0, 1), (1, 0)), ((math.log10(2), 2), (2, math.log10(2)))]
    for p1, p2 in pairs:
        ax.scatter(*p1, color=COLORS["fisico"], s=75, zorder=5)
        ax.scatter(*p2, color=COLORS["clinico"], s=75, zorder=5)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=COLORS["gris_2"], lw=1)
    ax.axhline(0, color=COLORS["carbon"], lw=1)
    ax.axvline(0, color=COLORS["carbon"], lw=1)
    ax.set_xlim(-1.3, 2.5)
    ax.set_ylim(-1.3, 2.5)
    ax.set_xlabel("entrada, x (adimensional)")
    ax.set_ylabel("salida, y (adimensional)")
    ax.grid(True, color=COLORS["gris_2"], lw=0.7)
    ax.legend(frameon=False, loc="upper left", fontsize=16)
    ax.text(1.56, 1.36, "intercambiar entrada y salida\nrefleja los puntos respecto de y=x", fontsize=15, color=COLORS["bordo"])
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    data_x = np.array([-1.0, -0.5, 0.0, math.log10(2), 0.4])
    rows = [["x", "10^x", "log10_domain_x", "log10(x)_if_positive"]]
    for v in data_x:
        rows.append([f"{v:.6f}", f"{10**v:.6f}", f"{v:.6f}", f"{math.log10(v):.6f}" if v > 0 else "not_defined"])
    return fig, rows


def chart21():
    fig, axes = plt.subplots(2, 1, figsize=WIDE_FIGSIZE, facecolor="white", gridspec_kw={"hspace": 0.65})
    vals = np.array([1, 10, 100, 1000], dtype=float)
    ax = axes[0]
    ax.set_xlim(0, 1000)
    ax.set_ylim(-0.2, 0.2)
    ax.hlines(0, 0, 1000, color=COLORS["carbon"], lw=2)
    ax.scatter(vals, np.zeros_like(vals), s=110, color=COLORS["fisico"], zorder=3)
    for v in vals:
        ax.text(v, 0.06, f"{int(v)}", ha="center", fontsize=15)
    ax.set_title("ESCALA LINEAL", loc="left", fontsize=18, color=COLORS["bordo"], weight="bold")
    ax.set_xlabel("razón Q/Q₀ (adimensional) · escala lineal")
    ax.set_yticks([])
    ax.grid(axis="x", color=COLORS["gris_2"], lw=0.7)
    for spine in ["top", "left", "right"]:
        ax.spines[spine].set_visible(False)
    ax2 = axes[1]
    ax2.set_xscale("log")
    ax2.set_xlim(1, 1000)
    ax2.set_ylim(-0.2, 0.2)
    ax2.hlines(0, 1, 1000, color=COLORS["carbon"], lw=2)
    ax2.scatter(vals, np.zeros_like(vals), s=110, color=COLORS["clinico"], zorder=3)
    for v in vals:
        ax2.text(v, 0.06, f"{int(v)}", ha="center", fontsize=15)
    ax2.set_xticks(vals, labels=["1", "10", "100", "1000"])
    ax2.set_title("ESCALA LOGARÍTMICA", loc="left", fontsize=18, color=COLORS["bordo"], weight="bold")
    ax2.set_xlabel("razón Q/Q₀ (adimensional) · escala logarítmica base 10")
    ax2.set_yticks([])
    ax2.grid(axis="x", color=COLORS["gris_2"], lw=0.7)
    for spine in ["top", "left", "right"]:
        ax2.spines[spine].set_visible(False)
    return fig, [["ratio", "linear_position", "log10_position"]] + [[str(int(v)), str(v), str(math.log10(v))] for v in vals]


def chart22():
    fig, ax = plt.subplots(figsize=WIDE_FIGSIZE, facecolor="white")
    ratio = np.array([1, 10, 100, 1000], dtype=float)
    level = 10 * np.log10(ratio)
    ax.set_xscale("log")
    ax.plot(ratio, level, color=COLORS["fisico"], lw=3, marker="o", ms=9)
    for r, l in zip(ratio, level):
        ax.annotate(f"{int(r)} → {int(l)} dB", (r, l), xytext=(0, 13), textcoords="offset points", ha="center", fontsize=15, color=COLORS["bordo"])
    ax.set_xlim(0.8, 1300)
    ax.set_ylim(-2, 34)
    ax.set_xticks(ratio, labels=["1", "10", "100", "1000"])
    ax.set_yticks([0, 10, 20, 30])
    ax.set_xlabel("razón Q/Q₀ (adimensional) · escala logarítmica")
    ax.set_ylabel("nivel, L_Q (dB) · escala lineal")
    ax.grid(True, color=COLORS["gris_2"], lw=0.8)
    ax.text(1.1, 30.5, r"$L_Q=10\log_{10}(Q/Q_0)$", fontsize=22, color=COLORS["bordo"])
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    return fig, [["ratio_Q_Q0", "level_dB"]] + [[f"{r:.0f}", f"{l:.1f}"] for r, l in zip(ratio, level)]


def chart23():
    fig, ax = new_canvas()
    cols = [
        ("MEDICIÓN\nFÍSICA", COLORS["fisico_bg"], COLORS["fisico"], ["frecuencia: 1000 Hz", "amplitud digital", "presión: Pa"]),
        ("NIVEL\nREFERIDO", COLORS["marfil"], COLORS["bordo"], ["35 dB HL", "requiere referencia", "no es valor absoluto"]),
        ("ATRIBUTO\nPERCEPTUAL", COLORS["clinico_bg"], COLORS["clinico"], ["altura tonal", "sonoridad", "timbre"]),
        ("RESPUESTA / \nCONCLUSIÓN", "#F3F3F3", COLORS["carbon"], ["“detectado”", "conducta observada", "clínica: requiere más datos"]),
    ]
    xvals = [0.03, 0.275, 0.52, 0.765]
    for x, (title, fc, ec, items) in zip(xvals, cols):
        box(ax, (x, 0.16), 0.205, 0.70, "", fc=fc, ec=ec)
        ax.text(x + 0.1025, 0.75, title, ha="center", fontsize=17, color=ec, weight="bold")
        for idx, item in enumerate(items):
            ax.text(x + 0.025, 0.59 - idx * 0.13, "• " + item, ha="left", fontsize=14.5, color=COLORS["carbon"])
    ax.text(0.50, 0.07, "se relacionan, pero no son equivalentes", ha="center", fontsize=20, color=COLORS["bordo"])
    return fig, [
        ["category", "examples"],
        ["medición física", "frecuencia 1000 Hz; amplitud digital; presión Pa"],
        ["nivel referido", "35 dB HL"],
        ["atributo perceptual", "altura tonal; sonoridad; timbre"],
        ["respuesta o conclusión", "detectado; conducta; conclusión clínica"],
    ]


def chart24():
    fig, ax = new_canvas()
    nodes = [
        (0.05, "VOCALIZACIÓN\nfuente", COLORS["fisico_bg"], COLORS["fisico"]),
        (0.37, "AIRE\nmedio", COLORS["marfil"], COLORS["bordo"]),
        (0.69, "MICRÓFONO\nreceptor", COLORS["clinico_bg"], COLORS["clinico"]),
    ]
    for x, text, fc, ec in nodes:
        box(ax, (x, 0.65), 0.24, 0.18, text, fc=fc, ec=ec, fontsize=18)
    arrow(ax, (0.29, 0.74), (0.37, 0.74), r"$d=6{,}8\ \mathrm{m}$")
    arrow(ax, (0.61, 0.74), (0.69, 0.74), r"$c=340\ \mathrm{m/s}$")
    data_boxes = [
        (0.05, r"$t=d/c=0{,}020\ \mathrm{s}$", COLORS["fisico_bg"], COLORS["fisico"]),
        (0.37, r"$f=N/\Delta t=200\ \mathrm{Hz}$", COLORS["fisico_bg"], COLORS["fisico"]),
        (0.69, r"$L_Q=10\log_{10}(100)=20\ \mathrm{dB}$", COLORS["marfil"], COLORS["bordo"]),
    ]
    for x, text, fc, ec in data_boxes:
        box(ax, (x, 0.38), 0.24, 0.16, text, fc=fc, ec=ec, fontsize=17)
    limits = [
        (0.05, "amplitud digital\nsin calibración en Pa"),
        (0.37, "200 Hz no determina\npor sí solo el pitch"),
        (0.69, "los datos no producen\nun diagnóstico"),
    ]
    for x, text in limits:
        box(ax, (x, 0.12), 0.24, 0.14, text, fc=COLORS["clinico_bg"], ec=COLORS["clinico"], fontsize=14)
    ax.text(0.93, 0.74, r"$N=100$ en $\Delta t=0{,}50\ \mathrm{s}$", ha="right", fontsize=14, color=COLORS["gris"])
    return fig, [
        ["variable", "value", "unit_or_type"],
        ["d", "6.8", "m"],
        ["c", "340", "m/s"],
        ["N", "100", "adimensional"],
        ["delta_t", "0.50", "s"],
        ["amplitude", "not calibrated", "digital units"],
        ["Q/Q0", "100", "adimensional"],
        ["propagation_time", f"{6.8/340:.3f}", "s"],
        ["frequency", f"{100/0.50:.0f}", "Hz"],
        ["level", f"{10*np.log10(100):.0f}", "dB"],
    ]


def chart25():
    fig, ax = new_canvas()
    box(
        ax,
        (0.34, 0.38),
        0.32,
        0.22,
        "UNIDAD 1\nlenguaje físico\ny matemático",
        fc=COLORS["bordo"],
        ec=COLORS["bordo"],
        color="white",
        fontsize=18,
    )
    future = [
        (0.06, 0.66, "UNIDAD 2\nmasa · fuerza · presión\nanálisis dimensional"),
        (0.70, 0.66, "UNIDAD 3\nfunciones · trigonometría\nradianes · propagación"),
        (0.38, 0.10, "UNIDAD 4\npresión · razones · logaritmos\ndecibel y referencia"),
    ]
    for x, y, text in future:
        box(ax, (x, y), 0.24, 0.17, text, fc=COLORS["marfil"], ec=COLORS["fisico"], fontsize=15)
    arrow(ax, (0.39, 0.57), (0.28, 0.66), color=COLORS["fisico"])
    arrow(ax, (0.61, 0.57), (0.72, 0.66), color=COLORS["fisico"])
    arrow(ax, (0.50, 0.38), (0.50, 0.27), color=COLORS["fisico"])
    ax.text(0.50, 0.90, "lo aprendido vuelve a usarse con mayor profundidad", ha="center", fontsize=20, color=COLORS["bordo"])
    return fig, [
        ["destination", "prerequisites_from_U1"],
        ["U2", "masa; fuerza; presión; análisis dimensional"],
        ["U3", "funciones; trigonometría; radianes; propagación"],
        ["U4", "presión; razones; logaritmos; decibel; referencia"],
    ]


def chart26():
    fig, axes = plt.subplots(2, 1, figsize=WIDE_FIGSIZE, facecolor="white", sharex=True, gridspec_kw={"hspace": 0.28})
    f1 = np.array([250, 500, 1000, 1500, 2000, 3000])
    a1 = np.array([1.00, 0.72, 0.48, 0.30, 0.18, 0.10])
    f2 = np.array([250, 500, 1000, 1500, 2000, 3000])
    a2 = np.array([0.32, 0.48, 1.00, 0.58, 0.42, 0.22])
    for ax, freqs, amps, label, color in [
        (axes[0], f1, a1, "ESPECTRO A", COLORS["fisico"]),
        (axes[1], f2, a2, "ESPECTRO B", COLORS["clinico"]),
    ]:
        markerline, stemlines, baseline = ax.stem(freqs, amps, basefmt=" ")
        plt.setp(stemlines, color=color, linewidth=3)
        plt.setp(markerline, marker="o", markersize=7, markerfacecolor=color, markeredgecolor=color)
        ax.set_ylim(0, 1.12)
        ax.set_xlim(0, 4000)
        ax.set_ylabel("amplitud relativa\n(adimensional)")
        ax.grid(axis="y", color=COLORS["gris_2"], lw=0.7)
        ax.text(0.02, 0.86, label, transform=ax.transAxes, fontsize=18, color=COLORS["bordo"], weight="bold")
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)
    axes[1].set_xlabel("frecuencia (Hz) · escala lineal")
    axes[1].set_xticks(np.arange(0, 4001, 500))
    fig.text(0.995, 0.02, "Datos sintéticos normalizados · no son mediciones", ha="right", fontsize=11, color=COLORS["gris"])
    rows = [["spectrum", "frequency_Hz", "relative_amplitude"]]
    rows += [["A", str(int(f)), f"{a:.2f}"] for f, a in zip(f1, a1)]
    rows += [["B", str(int(f)), f"{a:.2f}"] for f, a in zip(f2, a2)]
    return fig, rows


GENERATORS = {
    "U01-CH001": chart01,
    "U01-CH002": chart02,
    "U01-CH003": chart03,
    "U01-CH004": chart04,
    "U01-CH005": chart05,
    "U01-CH006": chart06,
    "U01-CH007": chart07,
    "U01-CH008": chart08,
    "U01-CH009": chart09,
    "U01-CH010": chart10,
    "U01-CH011": chart11,
    "U01-CH012": chart12,
    "U01-CH013": chart13,
    "U01-CH014": chart14,
    "U01-CH015": chart15,
    "U01-CH016": chart16,
    "U01-CH017": chart17,
    "U01-CH018": chart18,
    "U01-CH019": chart19,
    "U01-CH020": chart20,
    "U01-CH021": chart21,
    "U01-CH022": chart22,
    "U01-CH023": chart23,
    "U01-CH024": chart24,
    "U01-CH025": chart25,
    "U01-CH026": chart26,
}


def write_csv(path: Path, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def readme_text(m, basename):
    return f"""# {m['id']} — {m['title']}

## Uso

- Slides: {m['slides']}
- Pregunta: {m['question']}
- Escala: {m['scale']}

## Archivos

- `script.py`: regenera este recurso.
- `{basename}.svg`: salida vectorial editable/importable.
- `{basename}.png`: salida raster de alta resolución.
- `data.csv`: datos, relaciones o nodos usados.
- `caption.txt`: caption sugerido.
- `alt_text.txt`: texto alternativo.
- `source.txt`: fuente del modelo o de los datos.

## Reproducción

Ejecutar desde esta carpeta:

```powershell
python script.py
```

## Fuente

{m['source']}

## Validación específica

{m['validation']}
"""


def make_wrapper(chart_id: str, outdir: Path):
    text = f"""from pathlib import Path
import sys

scripts_dir = Path(__file__).resolve().parents[3] / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from u01_chartlib import generate_one

generate_one("{chart_id}")
"""
    (outdir / "script.py").write_text(text, encoding="utf-8")


def generate_animation_ch002(outdir: Path):
    fig, ax = plt.subplots(figsize=WIDE_FIGSIZE, facecolor="white")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.35, 0.35)
    ax.axis("off")
    x = np.linspace(0.3, 9.7, 46)
    marked = int(np.argmin(np.abs(x - 5.0)))
    scatter = ax.scatter(x, np.zeros_like(x), s=70, color=COLORS["fisico"], edgecolors="white")
    marked_scatter = ax.scatter([x[marked]], [0], s=150, color=COLORS["bordo_2"], edgecolors="white", zorder=4)
    ax.hlines(0, 0.2, 9.8, color=COLORS["gris_2"], lw=1, linestyle="--")
    ax.text(0.2, 0.25, "La perturbación avanza; la partícula marcada oscila localmente", fontsize=17, color=COLORS["bordo"])
    ax.text(9.8, -0.27, "Modelo conceptual · no a escala", ha="right", fontsize=11, color=COLORS["gris"])

    centers = np.concatenate([np.linspace(-0.5, 10.5, 46), np.linspace(10.5, -0.5, 2)])

    def update(frame):
        center = centers[frame]
        xi = 0.20 * np.exp(-((x - center) / 0.70) ** 2)
        xp = x + xi
        scatter.set_offsets(np.column_stack([xp, np.zeros_like(xp)]))
        marked_scatter.set_offsets(np.array([[xp[marked], 0]]))
        return scatter, marked_scatter

    anim = FuncAnimation(fig, update, frames=len(centers), interval=120, blit=True)
    anim.save(outdir / "u01_media_002_propagacion_particulas.gif", writer=PillowWriter(fps=8))
    plt.close(fig)


def generate_one(chart_id: str):
    if chart_id not in GENERATORS:
        raise KeyError(f"Unknown chart id: {chart_id}")
    m = METADATA[chart_id]
    number = int(chart_id[-3:])
    folder = OUTPUT_ROOT / f"u01_ch{number:03d}_{m['slug']}"
    folder.mkdir(parents=True, exist_ok=True)
    basename = f"u01_fig_{number:03d}_{m['slug']}"
    fig, rows = GENERATORS[chart_id]()
    svg_path = folder / f"{basename}.svg"
    png_path = folder / f"{basename}.png"
    fig.savefig(svg_path, format="svg", facecolor="white")
    fig.savefig(png_path, format="png", facecolor="white", dpi=180)
    plt.close(fig)
    write_csv(folder / "data.csv", rows)
    (folder / "caption.txt").write_text(m["caption"] + "\n", encoding="utf-8")
    (folder / "alt_text.txt").write_text(m["alt"] + "\n", encoding="utf-8")
    (folder / "source.txt").write_text(m["source"] + "\n", encoding="utf-8")
    (folder / "README.md").write_text(readme_text(m, basename), encoding="utf-8")
    make_wrapper(chart_id, folder)
    if chart_id == "U01-CH002":
        generate_animation_ch002(folder)
    return {
        "chart_id": chart_id,
        "folder": str(folder.relative_to(UNIT_DIR)),
        "svg": str(svg_path.relative_to(UNIT_DIR)),
        "png": str(png_path.relative_to(UNIT_DIR)),
        "svg_bytes": svg_path.stat().st_size,
        "png_bytes": png_path.stat().st_size,
    }


def make_contact_sheets(results, columns=4, rows_per_sheet=4):
    review_dir = OUTPUT_ROOT / "_review"
    review_dir.mkdir(parents=True, exist_ok=True)
    thumbs = []
    for result in results:
        image = Image.open(UNIT_DIR / result["png"]).convert("RGB")
        image.thumbnail((440, 248), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (460, 290), "white")
        x = (460 - image.width) // 2
        y = 26 + (248 - image.height) // 2
        canvas.paste(image, (x, y))
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("arial.ttf", 18)
        except OSError:
            font = ImageFont.load_default()
        draw.text((10, 4), result["chart_id"], fill=COLORS["bordo"], font=font)
        thumbs.append(canvas)
    per_sheet = columns * rows_per_sheet
    sheet_paths = []
    for idx in range(0, len(thumbs), per_sheet):
        chunk = thumbs[idx : idx + per_sheet]
        sheet = Image.new("RGB", (columns * 460, rows_per_sheet * 290), "#E8E8E8")
        for j, thumb in enumerate(chunk):
            sheet.paste(thumb, ((j % columns) * 460, (j // columns) * 290))
        path = review_dir / f"u01_charts_contact_sheet_{idx // per_sheet + 1:02d}.png"
        sheet.save(path)
        sheet_paths.append(path)
    return sheet_paths


def generate_all():
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    results = [generate_one(chart_id) for chart_id in sorted(GENERATORS)]
    sheets = make_contact_sheets(results)
    report = {
        "generated": results,
        "contact_sheets": [str(p.relative_to(UNIT_DIR)) for p in sheets],
        "python": sys.version,
        "numpy": np.__version__,
        "matplotlib": matplotlib.__version__,
    }
    (OUTPUT_ROOT / "generation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    index_lines = ["# Figuras generadas — Unidad 1", "", "Ejecutar `python units/unit_01/scripts/u01_generate_all_charts.py` para regenerar todo.", ""]
    for item in results:
        index_lines.append(f"- **{item['chart_id']}** — `{item['folder']}`")
    (OUTPUT_ROOT / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    generate_all()
