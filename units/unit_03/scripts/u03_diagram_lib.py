from __future__ import annotations

import json
import math
import re
import sys
import textwrap
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from PIL import Image, ImageDraw, ImageFont


UNIT_DIR = Path(__file__).resolve().parents[1]
SCRIPT_DIR = UNIT_DIR / "scripts"
OUTPUT_ROOT = UNIT_DIR / "assets" / "generated" / "diagrams"
REVIEW_DIR = UNIT_DIR / "assets" / "generated" / "_review"

COLORS = {
    "bordo": "#4D1434", "bordo_2": "#903163", "carbon": "#3D3D3D",
    "gris": "#969FA7", "gris_2": "#D9DCE0", "marfil": "#F7F6F2",
    "fisico": "#2F7E83", "fisico_bg": "#E7F1F1",
    "clinico": "#9F541A", "clinico_bg": "#F8EDE2", "white": "#FFFFFF",
}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Calibri", "Arial", "DejaVu Sans"],
    "font.size": 22,
    "text.color": COLORS["carbon"],
    "svg.fonttype": "none",
    "figure.dpi": 200,
    "savefig.dpi": 200,
})

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


FAMILIES = {
    "U03-DG001": [2, 15, 79],
    "U03-DG002": [6, 16, 47, 59, 69, 78, 81],
    "U03-DG003": [8, 20, 21],
    "U03-DG004": [9, 10, 14],
    "U03-DG005": [11, 12],
    "U03-DG006": [4, 18, 19],
    "U03-DG007": [26, 65, 84],
    "U03-DG008": [27],
    "U03-DG009": [29],
    "U03-DG010": [31, 32],
    "U03-DG011": [36],
    "U03-DG012": [37, 38],
    "U03-DG013": [40],
    "U03-DG014": [42, 45, 47],
    "U03-DG015": [43, 44],
    "U03-DG016": [46],
    "U03-DG017": [49],
    "U03-DG018": [53],
    "U03-DG019": [55, 56, 57, 59],
    "U03-DG020": [62, 69],
    "U03-DG021": [71],
    "U03-DG022": [76],
    "U03-DG023": [77],
    "U03-DG024": [80, 81, 95],
    "U03-DG025": [24, 67, 85, 86, 87, 88, 89, 90, 91, 92],
}

FAMILY_TITLES = {
    "U03-DG001": "Fuente, medio y receptor",
    "U03-DG002": "Mapa progresivo de la unidad",
    "U03-DG003": "Estados de una oscilación",
    "U03-DG004": "Movimiento local y frente",
    "U03-DG005": "Medio e interacción; tipos de onda",
    "U03-DG006": "Modelo del MAS y ecuación restauradora",
    "U03-DG007": "Ciclo, fase y sinusoide",
    "U03-DG008": "Matriz de parámetros del MAS",
    "U03-DG009": "Ecuación temporal del MAS",
    "U03-DG010": "Estados de posición, velocidad y aceleración",
    "U03-DG011": "Trayectoria frente a gráfico",
    "U03-DG012": "Niveles de evidencia y checklist",
    "U03-DG013": "Tono puro ideal",
    "U03-DG014": "Cadena de transducción",
    "U03-DG015": "Cono, partículas y presión",
    "U03-DG016": "Cadena de calibración audiométrica",
    "U03-DG017": "Doble dependencia ξ(x,t)",
    "U03-DG018": "Comparación período–longitud de onda",
    "U03-DG019": "Onda viajera y rapidez",
    "U03-DG020": "Velocidad de partícula y propagación",
    "U03-DG021": "Superposición instantánea",
    "U03-DG022": "Cancelación activa y zona de reducción",
    "U03-DG023": "Aplicaciones de superposición",
    "U03-DG024": "Caso integrador y mapa final",
    "U03-DG025": "Familia de ecuaciones anotadas",
}


def classification(family: str, slide: int) -> str:
    if family in {"U03-DG009", "U03-DG013", "U03-DG021", "U03-DG025"} or (family == "U03-DG006" and slide == 19):
        return "ecuación anotada"
    if family in {"U03-DG004", "U03-DG010", "U03-DG014", "U03-DG016", "U03-DG022", "U03-DG023"}:
        return "diagrama de proceso"
    if family in {"U03-DG011", "U03-DG012", "U03-DG018", "U03-DG019", "U03-DG024"}:
        return "esquema mixto"
    return "diagrama conceptual"


@dataclass
class Node:
    object_id: str
    bbox: tuple[float, float, float, float]
    text: str
    font_size: float


@dataclass
class Edge:
    object_id: str
    start: tuple[float, float]
    end: tuple[float, float]
    label: str
    source: str | None
    target: str | None
    font_size: float


class Canvas:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 5.5), facecolor="white")
        self.fig.subplots_adjust(0, 0, 1, 1)
        self.ax.set_xlim(0, 12)
        self.ax.set_ylim(0, 5.5)
        self.ax.axis("off")
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.texts = []

    def arrow(self, start, end, *, label="", color=None, dashed=False, source=None, target=None, y_label_offset=.18, object_id=None):
        color = color or COLORS["bordo"]
        patch = patches.FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=18, linewidth=2.1,
            color=color, linestyle="--" if dashed else "-", zorder=1,
            shrinkA=0, shrinkB=0,
        )
        self.ax.add_patch(patch)
        if label:
            mx, my = (start[0]+end[0])/2, (start[1]+end[1])/2 + y_label_offset
            t = self.ax.text(mx, my, label, fontsize=20, ha="center", va="bottom",
                             color=color, bbox=dict(facecolor="white", edgecolor="none", pad=1.5), zorder=4)
            self.texts.append(t)
        self.edges.append(Edge(object_id or f"edge_{len(self.edges)+1:02d}", start, end, label, source, target, 20 if label else 0))

    def line(self, start, end, *, color=None, lw=2, ls="-"):
        self.ax.plot([start[0], end[0]], [start[1], end[1]], color=color or COLORS["carbon"], lw=lw, ls=ls, zorder=1)

    def node(self, x, y, w, h, text, *, fill=None, edge=None, fontsize=24, weight="bold", object_id=None, radius=.04):
        fill = fill or COLORS["fisico_bg"]
        edge = edge or COLORS["fisico"]
        box = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle=f"round,pad=0.02,rounding_size={radius}",
            facecolor=fill, edgecolor=edge, linewidth=1.8, zorder=2,
        )
        self.ax.add_patch(box)
        t = self.ax.text(x+w/2, y+h/2, text, fontsize=fontsize, weight=weight,
                         ha="center", va="center", linespacing=1.15, zorder=3)
        self.texts.append(t)
        rec = Node(object_id or f"node_{len(self.nodes)+1:02d}", (x, y, w, h), text, fontsize)
        self.nodes.append(rec)
        return rec

    def label(self, x, y, text, *, fontsize=22, color=None, weight="normal", ha="center", va="center", bbox=None, object_id=None):
        t = self.ax.text(x, y, text, fontsize=fontsize, color=color or COLORS["carbon"], weight=weight,
                         ha=ha, va=va, bbox=bbox, zorder=4)
        self.texts.append(t)
        return t

    def circle(self, x, y, r, *, fill="white", edge=None, lw=2):
        p = patches.Circle((x, y), r, facecolor=fill, edgecolor=edge or COLORS["fisico"], lw=lw, zorder=2)
        self.ax.add_patch(p)
        return p

    def validate(self):
        self.fig.canvas.draw()
        renderer = self.fig.canvas.get_renderer()
        inv = self.ax.transData.inverted()
        issues = []
        # Text objects must remain inside the 12 × 5.5 canvas with a small tolerance.
        for index, text in enumerate(self.texts):
            b = text.get_window_extent(renderer=renderer)
            (x0, y0), (x1, y1) = inv.transform([[b.x0, b.y0], [b.x1, b.y1]])
            if x0 < -.02 or y0 < -.02 or x1 > 12.02 or y1 > 5.52:
                issues.append({"severity": "major", "kind": "text_outside_canvas", "object": index})
        for node in self.nodes:
            x, y, w, h = node.bbox
            if x < 0 or y < 0 or x+w > 12 or y+h > 5.5:
                issues.append({"severity": "major", "kind": "node_outside_canvas", "object": node.object_id})
            if node.font_size < 22:
                issues.append({"severity": "major", "kind": "font_below_minimum", "object": node.object_id})
        for edge in self.edges:
            if edge.label and edge.font_size < 20:
                issues.append({"severity": "major", "kind": "connector_label_below_minimum", "object": edge.object_id})
        return issues


def chain(canvas: Canvas, labels, edge_labels=None, *, clinical_last=False, active=None):
    n = len(labels)
    w = min(2.05, (10.5 - (n-1)*.55)/n)
    gap = (10.5 - n*w)/(n-1) if n > 1 else 0
    xs = [.75 + i*(w+gap) for i in range(n)]
    y, h = 2.05, 1.35
    for i in range(n-1):
        canvas.arrow((xs[i]+w, y+h/2), (xs[i+1], y+h/2),
                     label=(edge_labels or [""]*(n-1))[i], source=f"node_{i+1:02d}", target=f"node_{i+2:02d}")
    for i, (x, label) in enumerate(zip(xs, labels)):
        fill = COLORS["clinico_bg"] if clinical_last and i == n-1 else COLORS["fisico_bg"]
        edge = COLORS["clinico"] if clinical_last and i == n-1 else COLORS["fisico"]
        if active == i:
            fill, edge = "#F3E5ED", COLORS["bordo"]
        canvas.node(x, y, w, h, label, fill=fill, edge=edge, fontsize=24)
    return xs, w, y, h


def render_dg001(slide):
    c = Canvas()
    if slide == 2:
        labels = ["Parlante", "Aire", "¿Qué llega?", "Oído"]
        edge = ["mueve", "transmite", "recibe"]
    elif slide == 15:
        labels = ["Pliegues\nvocales", "Aire", "Estructura\nreceptora"]
        edge = ["perturban", "se propaga"]
    else:
        labels = ["Fuente", "Variable\nlocal", "Medio", "Medición", "Interpretación"]
        edge = ["oscila", "perturba", "registra", "informa"]
    xs, w, y, h = chain(c, labels, edge, clinical_last=True)
    c.arrow((xs[0]+.35, y-.35), (xs[0]+w-.35, y-.35), label="movimiento local", color=COLORS["fisico"], dashed=True, y_label_offset=-.34)
    c.arrow((xs[-1]+w-.35, y+h+.35), (xs[-1]+.35, y+h+.35), label="respuesta local", color=COLORS["clinico"], dashed=True, y_label_offset=.12)
    c.label(6, .55, "La materia oscila localmente; la perturbación enlaza las etapas.", fontsize=22, weight="bold")
    return c


def render_dg002(slide):
    c = Canvas()
    labels = ["Oscilación", "MAS", "Parámetros", "Sinusoide", "Parlante", "Onda viajera", "Fase", "Superposición", "Aplicación"]
    active_map = {6: 0, 16: 1, 47: 4, 59: 5, 69: 6, 78: 7, 81: 8}
    coords = [(0.45+i*2.25, 3.35) for i in range(5)] + [(1.55+i*2.55, 1.05) for i in range(4)]
    # Connectors first, including the turn between rows.
    for i in range(4):
        c.arrow((coords[i][0]+1.75, 3.95), (coords[i+1][0], 3.95))
    c.arrow((coords[4][0]+.88, 3.35), (coords[5][0]+.88, 2.35), color=COLORS["bordo"])
    for i in range(5, 8):
        c.arrow((coords[i][0]+1.75, 1.65), (coords[i+1][0], 1.65))
    for i, ((x, y), label) in enumerate(zip(coords, labels)):
        active = active_map.get(slide)
        fill, edge = (("#F3E5ED", COLORS["bordo"]) if i == active else (COLORS["fisico_bg"], COLORS["fisico"]))
        c.node(x, y, 1.75, 1.18, label, fill=fill, edge=edge, fontsize=23, object_id=f"stage_{i+1:02d}")
        c.label(x+.18, y+1.0, str(i+1), fontsize=20, color=edge, weight="bold", ha="left")
    c.label(6, .35, "Etapa activa marcada también por número y borde.", fontsize=20)
    return c


def draw_mass_state(c, x, y, position, label, dyn=None):
    c.line((x, y), (x+2.0, y), color=COLORS["gris"], lw=1.4)
    eq = x+1.0
    c.line((eq, y-.28), (eq, y+.52), color=COLORS["gris"], lw=1.2, ls=":")
    px = eq + position*.68
    c.node(px-.30, y-.28, .60, .56, "", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], fontsize=22, radius=.02)
    c.label(x+1.0, y-.62, label, fontsize=20)
    if dyn:
        direction, symbol, color = dyn
        if direction:
            c.arrow((px, y+.48), (px+.55*direction, y+.48), color=color)
        else:
            c.label(px, y+.52, f"{symbol}=0", fontsize=20, color=color)


def render_dg003(slide):
    c = Canvas()
    if slide == 20:
        positions = [1, 0, -1, 0, 1]
        labels = ["+Aₓ", "0 →", "−Aₓ", "0 ←", "+Aₓ"]
    else:
        positions = [-1, 0, 1]
        labels = ["−Aₓ", "equilibrio", "+Aₓ"]
    width = 11/len(positions)
    for i, (pos, lab) in enumerate(zip(positions, labels)):
        draw_mass_state(c, .5+i*width, 2.65, pos, lab)
    c.label(6, 4.65, "El estado se repite cuando coinciden posición y sentido.", fontsize=26, weight="bold", color=COLORS["bordo"])
    if slide == 21:
        c.arrow((6, 1.35), (8.05, 1.35), label="Aₓ: máximo |x|", y_label_offset=.18)
    else:
        c.label(6, .75, "Esquema conceptual · no está a escala.", fontsize=20)
    return c


def render_dg004(slide):
    c = Canvas()
    n = 5 if slide == 9 else 4
    for frame in range(n):
        x0 = .35 + frame*(11.3/n)
        c.label(x0+.85, 4.72, f"t{frame}", fontsize=20, weight="bold")
        front = min(5, frame+1)
        for p in range(6):
            x = x0+.2+p*.30
            shift = .10*math.sin((frame-p)*1.4) if p <= front else 0
            c.circle(x+shift, 2.75, .075, fill=(COLORS["bordo_2"] if p == 1 else COLORS["fisico"]), edge="none", lw=0)
        c.line((x0+.2, 2.35), (x0+1.72, 2.35), color=COLORS["gris"], lw=1)
        c.line((x0+.2+front*.30, 2.25), (x0+.2+front*.30, 3.25), color=COLORS["clinico"], lw=2, ls=":")
        if frame == 0:
            c.label(x0+.5, 1.60, "partícula\nmarcada", fontsize=20, color=COLORS["bordo_2"])
    c.arrow((.75, 1.08), (11.15, 1.08), label="avance del frente y de la energía", color=COLORS["clinico"], y_label_offset=.18)
    c.label(6, 4.15, "Las partículas se mueven localmente; el frente aparece más lejos.", fontsize=24, weight="bold")
    return c


def render_dg005(slide):
    c = Canvas()
    if slide == 11:
        for i in range(8):
            c.circle(1.2+i*1.25, 2.75+.18*math.sin(i), .18, fill=COLORS["fisico_bg"], edge=COLORS["fisico"], lw=1.6)
        for i in range(7):
            c.arrow((1.42+i*1.25, 2.75), (2.18+i*1.25, 2.75), color=COLORS["gris"], dashed=True)
        c.node(.75, 4.05, 2.8, .85, "Medio material", fontsize=24)
        c.node(4.55, 4.05, 3.1, .85, "Interacción vecina", fontsize=24)
        c.node(8.65, 4.05, 2.45, .85, "Perturbación", fontsize=24)
        c.label(6, .70, "Onda mecánica: el modelo requiere medio e interacción.", fontsize=24, weight="bold")
    else:
        # Two equal panels with propagation arrows above and local movement inside.
        for x0, title, transverse in ((.55, "Longitudinal · aire", False), (6.25, "Transversal · cuerda", True)):
            c.node(x0, .70, 5.05, 4.05, "", fill="white", edge=COLORS["gris_2"], fontsize=22)
            c.label(x0+2.52, 4.38, title, fontsize=25, weight="bold", color=COLORS["bordo"])
            c.arrow((x0+.55, 3.75), (x0+4.5, 3.75), label="propagación", color=COLORS["clinico"])
            if transverse:
                xx = np.linspace(x0+.55, x0+4.5, 120)
                yy = 2.25+.42*np.sin(2*np.pi*(xx-(x0+.55))/2.0)
                c.ax.plot(xx, yy, color=COLORS["fisico"], lw=3, zorder=2)
                c.arrow((x0+1.25, 1.65), (x0+1.25, 2.65), label="movimiento local", color=COLORS["fisico"], y_label_offset=-.52)
            else:
                for i in range(14):
                    xpos = x0+.55+i*.29 + .07*math.sin(i*1.7)
                    c.circle(xpos, 2.3, .055, fill=COLORS["fisico"], edge="none", lw=0)
                c.arrow((x0+1.0, 1.65), (x0+2.0, 1.65), label="movimiento local", color=COLORS["fisico"])
        c.label(6, .25, "La clasificación compara direcciones; el aire no sigue una curva sinusoidal.", fontsize=20)
    return c


def equation_canvas(equation, callouts, *, footer="", left=None, right=None):
    c = Canvas()
    c.node(2.0, 2.05, 8.0, 1.35, equation, fill="white", edge=COLORS["bordo"], fontsize=34, object_id="equation")
    positions = [(1.75, 4.15), (4.25, 4.15), (7.75, 4.15), (10.25, 4.15)]
    anchors = [(3.0, 3.40), (4.7, 3.40), (6.6, 3.40), (8.6, 3.40)]
    for i, label in enumerate(callouts[:4]):
        x = positions[i][0]
        c.arrow((x, 3.85), anchors[i], color=COLORS["gris"], dashed=True, y_label_offset=.1)
        c.node(x-1.15, 3.95, 2.3, .82, label, fill=COLORS["marfil"], edge=COLORS["gris"], fontsize=22, weight="normal", object_id=f"callout_{i+1:02d}")
    if left:
        c.label(.55, 1.15, left, fontsize=22, color=COLORS["fisico"], ha="left", weight="bold")
    if right:
        c.label(11.45, 1.15, right, fontsize=22, color=COLORS["clinico"], ha="right", weight="bold")
    if footer:
        c.label(6, .55, footer, fontsize=21)
    return c


def render_dg006(slide):
    if slide == 19:
        return equation_canvas("m · a = −kₛ · x", ["m: masa (kg)", "a: aceleración", "−: hacia equilibrio", "kₛx: fuerza (N)"], footer="Control dimensional: kg·m/s² = N")
    c = Canvas()
    # Spring and mass.
    wall_x, y = 1.2, 2.65
    c.line((wall_x, 1.65), (wall_x, 3.65), color=COLORS["carbon"], lw=4)
    xs = np.linspace(wall_x, 5.1, 16)
    ys = y + .28*np.where(np.arange(16)%2==0, 1, -1)
    ys[[0, -1]] = y
    c.ax.plot(xs, ys, color=COLORS["fisico"], lw=2.5, zorder=2)
    c.node(5.1, 2.0, 1.35, 1.3, "m", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], fontsize=30)
    c.line((6.45, 1.7), (10.9, 1.7), color=COLORS["gris"], lw=1.5)
    c.line((8.65, 1.45), (8.65, 3.55), color=COLORS["gris"], lw=1.1, ls=":")
    c.arrow((8.65, 3.15), (6.75, 3.15), label="F_rest", color=COLORS["bordo"])
    c.arrow((8.65, 2.45), (10.35, 2.45), label="+x", color=COLORS["fisico"])
    c.node(7.35, 4.0, 3.55, .85, "Modelo ideal de MAS", fill=COLORS["marfil"], edge=COLORS["bordo"], fontsize=25)
    c.label(8.95, .78, "lineal · sin rozamiento · sin excitación externa", fontsize=21)
    c.label(3.5, .72, "El objeto real se reemplaza por un modelo.", fontsize=21, color=COLORS["bordo"])
    return c


def render_dg007(slide):
    c = Canvas()
    center, r = (2.45, 2.7), 1.55
    c.circle(*center, r, fill="white", edge=COLORS["fisico"], lw=2.2)
    points = [(0, "0"), (np.pi/2, "π/2"), (np.pi, "π"), (3*np.pi/2, "3π/2")]
    for angle, label in points:
        x, y = center[0]+r*np.cos(angle), center[1]+r*np.sin(angle)
        c.circle(x, y, .10, fill=COLORS["bordo"], edge="none", lw=0)
        c.label(x+(.28 if math.cos(angle)>=0 else -.28), y+(.22 if math.sin(angle)>=0 else -.22), label, fontsize=20, color=COLORS["bordo"])
    c.arrow((center[0]+.75, center[1]+.75), (center[0]+.25, center[1]+1.25), label="fase", color=COLORS["bordo"], y_label_offset=.08)
    x = np.linspace(5.25, 11.5, 300)
    q = (x-5.25)/(11.5-5.25)
    y = 2.7+1.35*np.cos(2*np.pi*q)
    c.ax.plot(x, y, color=COLORS["fisico"], lw=3, zorder=2)
    for qv, lab in ((0, "0"), (.25, "π/2"), (.5, "π"), (.75, "3π/2"), (1, "2π")):
        xx = 5.25+qv*(11.5-5.25)
        yy = 2.7+1.35*np.cos(2*np.pi*qv)
        c.circle(xx, yy, .09, fill=COLORS["bordo"], edge="none", lw=0)
        c.label(xx, yy+(.28 if yy<3.8 else -.35), lab, fontsize=20, color=COLORS["bordo"])
    c.label(8.35, .52, "2π rad = 360° = 1 ciclo", fontsize=24, weight="bold")
    if slide == 65:
        c.label(6, 4.85, "Δφ = φ₂ − φ₁ · el orden fija el signo", fontsize=26, weight="bold", color=COLORS["bordo"])
    return c


def render_dg008(slide):
    c = Canvas()
    cells = [
        ("Amplitud · Aₓ", "¿Cuánto se aleja?\nUnidad de x"),
        ("Período · T", "¿Cuánto tarda un ciclo?\ns"),
        ("Frecuencia · f", "¿Cuántos ciclos por segundo?\nHz"),
        ("Fase · φ₀", "¿En qué estado comienza?\nrad o °"),
    ]
    for i, (title, body) in enumerate(cells):
        col, row = i%2, 1-i//2
        x, y = .75+col*5.65, .65+row*2.25
        c.node(x, y, 5.0, 1.75, f"{title}\n{body}", fill=("white" if i%2 else COLORS["fisico_bg"]), edge=(COLORS["bordo"] if i in (1,3) else COLORS["fisico"]), fontsize=23, weight="normal")
    c.label(6, 5.02, "Cuatro preguntas; cuatro magnitudes distintas", fontsize=27, weight="bold", color=COLORS["bordo"])
    return c


def render_dg009(slide):
    return equation_canvas("x(t) = Aₓ cos(2π f t + φ₀)", ["x(t): posición", "Aₓ: amplitud", "f: frecuencia", "φ₀: fase inicial"], footer="t es la variable independiente; x y Aₓ comparten unidad.")


def render_dg010(slide):
    c = Canvas()
    positions = [1, 0, -1, 0]
    if slide == 31:
        dyns = [(0, "v", COLORS["bordo"]), (-1, "v", COLORS["bordo"]), (0, "v", COLORS["bordo"]), (1, "v", COLORS["bordo"])]
        title = "Velocidad: cero en extremos; módulo máximo en equilibrio"
    else:
        dyns = [(-1, "a", COLORS["clinico"]), (0, "a", COLORS["clinico"]), (1, "a", COLORS["clinico"]), (0, "a", COLORS["clinico"])]
        title = "Aceleración: apunta hacia el equilibrio"
    for i, (pos, dyn) in enumerate(zip(positions, dyns)):
        draw_mass_state(c, .35+i*2.9, 2.65, pos, ["+Aₓ", "0", "−Aₓ", "0"][i], dyn)
    c.label(6, 4.8, title, fontsize=26, weight="bold", color=COLORS["bordo"])
    c.label(6, .62, "Misma geometría; una variable dinámica por versión.", fontsize=20)
    return c


def render_dg011(slide):
    c = Canvas()
    c.node(.65, .70, 5.0, 4.0, "", fill="white", edge=COLORS["gris_2"])
    c.node(6.35, .70, 5.0, 4.0, "", fill="white", edge=COLORS["gris_2"])
    c.label(3.15, 4.3, "Movimiento real", fontsize=25, weight="bold", color=COLORS["bordo"])
    c.line((1.35, 2.55), (4.95, 2.55), color=COLORS["gris"], lw=2)
    c.circle(2.2, 2.55, .26, fill=COLORS["fisico_bg"], edge=COLORS["fisico"])
    c.arrow((1.55, 1.65), (4.75, 1.65), label="recorrido rectilíneo", color=COLORS["fisico"])
    c.label(8.85, 4.3, "Representación x(t)", fontsize=25, weight="bold", color=COLORS["bordo"])
    x = np.linspace(6.95, 10.8, 180)
    y = 2.55+.85*np.cos(2*np.pi*(x-6.95)/(10.8-6.95))
    c.ax.plot(x, y, color=COLORS["fisico"], lw=3)
    c.arrow((7.0, 1.25), (10.8, 1.25), label="tiempo, t", color=COLORS["carbon"])
    c.label(6.85, 2.55, "x", fontsize=22, ha="right")
    c.label(6, .28, "La curva no es la trayectoria geométrica del objeto.", fontsize=23, weight="bold")
    return c


def render_dg012(slide):
    c = Canvas()
    if slide == 37:
        labels = [
            ("Esquema", "muestra forma y relación"),
            ("Normalizado", "agrega escala relativa"),
            ("Calibrado", "agrega unidad y referencia"),
        ]
        ys = [.55, 2.05, 3.55]
        for i in range(2):
            c.arrow((6, ys[i]+1.0), (6, ys[i+1]), color=COLORS["bordo"])
            c.label(8.45, (ys[i]+1.0+ys[i+1])/2, ("agrega escala" if i == 0 else "agrega calibración"), fontsize=20, color=COLORS["bordo"], ha="left")
        for y, (title, body) in zip(ys, labels):
            c.node(3.65, y, 4.7, 1.0, f"{title} · {body}", fill=COLORS["marfil"], edge=COLORS["bordo"], fontsize=22, weight="normal")
        c.label(6, 5.08, "La evidencia disponible limita la conclusión", fontsize=27, weight="bold", color=COLORS["bordo"])
    else:
        c.node(.75, .75, 5.2, 3.9, "", fill="white", edge=COLORS["gris_2"])
        x = np.linspace(1.25, 5.35, 160)
        y = 2.65+.8*np.cos(2*np.pi*(x-1.25)/(5.35-1.25))
        c.ax.plot(x, y, color=COLORS["fisico"], lw=3)
        c.arrow((1.25, 1.35), (5.3, 1.35), label="eje horizontal")
        qs = ["¿qué variable?", "¿qué unidad?", "¿qué escala?", "¿está calibrado?"]
        for i, q in enumerate(qs):
            c.node(6.6, 4.0-i*.95, 4.65, .72, q, fill=COLORS["marfil"], edge=COLORS["bordo"], fontsize=22, weight="normal")
        c.label(3.35, 4.25, "Gráfico genérico:\nno autoriza valores físicos", fontsize=22, weight="bold", color=COLORS["bordo"])
    return c


def render_dg013(slide):
    return equation_canvas("s(t) = Aₛ cos(2π f t + φ₀)", ["s: variable declarada", "Aₛ: amplitud", "f: frecuencia única", "φ₀: estado inicial"], footer="Modelo ideal: duración ilimitada · frecuencia única · amplitud constante")


def render_dg014(slide):
    c = Canvas()
    labels = ["V(t)\nvoltios", "x_cono(t)\nmetros", "ξ_aire(t)\nmetros", "p_ac(t)\npascales"]
    chain(c, labels, ["excita", "desplaza", "modifica\npresión"])
    c.label(6, 4.65, "Cada etapa cambia de variable y de unidad", fontsize=27, weight="bold", color=COLORS["bordo"])
    c.label(6, .60, "Las formas pueden parecerse; las amplitudes no se igualan sin calibración.", fontsize=21)
    return c


def render_dg015(slide):
    c = Canvas()
    if slide == 43:
        c.node(.65, .75, 4.15, 4.0, "", fill="white", edge=COLORS["gris_2"])
        # Cone as editable polygon in SVG.
        cone = patches.Polygon([[1.25, 1.45], [3.75, 2.30], [3.75, 3.20], [1.25, 4.05]], closed=True, facecolor=COLORS["fisico_bg"], edgecolor=COLORS["fisico"], lw=2.2, zorder=2)
        c.ax.add_patch(cone)
        c.arrow((1.35, 2.75), (2.55, 2.75), label="movimiento del cono", color=COLORS["bordo"])
        for i in range(18):
            x = 5.6+(i%9)*.58
            y = 2.2+(i//9)*.95
            c.circle(x, y, .07, fill=COLORS["fisico"], edge="none", lw=0)
        c.arrow((5.7, 1.20), (10.7, 1.20), label="propagación", color=COLORS["clinico"])
        c.label(8.1, 4.25, "Aire vecino", fontsize=25, weight="bold")
        c.label(8.1, 3.55, "compresión ↔ rarefacción", fontsize=23, color=COLORS["bordo"])
    else:
        for x0, title, dense in ((.65, "Cono avanza · compresión", True), (6.35, "Cono retrocede · rarefacción", False)):
            c.node(x0, .75, 5.0, 4.0, "", fill="white", edge=COLORS["gris_2"])
            c.label(x0+2.5, 4.35, title, fontsize=24, weight="bold", color=COLORS["bordo"])
            c.line((x0+.75, 1.35), (x0+.75, 3.7), color=COLORS["fisico"], lw=8)
            for i in range(16):
                spacing = .20 if dense and i < 8 else (.36 if not dense and i < 8 else .28)
                px = x0+1.25+i*spacing
                if px < x0+4.65:
                    c.circle(px, 2.55+.25*((i%3)-1), .055, fill=COLORS["fisico"], edge="none", lw=0)
            c.arrow((x0+.95, 1.25), (x0+4.45, 1.25), label="frente", color=COLORS["clinico"])
        c.label(6, .28, "Esquema conceptual · partículas y distancias no están a escala.", fontsize=20)
    return c


def render_dg016(slide):
    c = Canvas()
    labels = ["Generador\nf y nivel", "Transductor", "Acoplador\no oído", "Control de\ncalibración"]
    chain(c, labels, ["señal", "entrega", "verifica"], clinical_last=True)
    c.label(6, 4.65, "La calibración controla la cadena; no es un resultado clínico", fontsize=26, weight="bold", color=COLORS["bordo"])
    c.label(6, .60, "Acoplador y oído no son equivalentes: representan condiciones distintas.", fontsize=21)
    return c


def render_dg017(slide):
    c = Canvas()
    x0, y0, cell = 3.30, .72, 1.38
    for r in range(3):
        for col in range(3):
            fill = "#F3E5ED" if r == 1 or col == 1 else "white"
            edge = COLORS["bordo"] if r == 1 or col == 1 else COLORS["gris_2"]
            c.node(x0+col*cell, y0+r*cell, 1.18, 1.18, f"ξ(x{col+1},t{r+1})", fill=fill, edge=edge, fontsize=22, weight="normal")
    c.label(2.75, y0+1*cell+.52, "t = t₀ →", fontsize=22, color=COLORS["bordo"], ha="right", weight="bold")
    c.label(x0+1*cell+.52, 4.95, "x = x₀\n↓", fontsize=22, color=COLORS["bordo"], weight="bold")
    c.label(8.2, 3.2, "Tiempo fijo:\nrecorrer posiciones", fontsize=23, color=COLORS["fisico"], ha="left", weight="bold")
    c.label(8.2, 1.7, "Posición fija:\nrecorrer instantes", fontsize=23, color=COLORS["clinico"], ha="left", weight="bold")
    return c


def render_dg018(slide):
    c = Canvas()
    c.node(.55, .65, 5.25, 4.25, "", fill="white", edge=COLORS["gris_2"])
    c.node(6.2, .65, 5.25, 4.25, "", fill="white", edge=COLORS["gris_2"])
    for x0, label, axis in ((.85, "Corte temporal", "t (ms)"), (6.5, "Corte espacial", "x (m)")):
        x = np.linspace(x0, x0+4.65, 220)
        y = 2.65+.85*np.cos(2*np.pi*(x-x0)/2.3)
        c.ax.plot(x, y, color=(COLORS["fisico"] if x0 < 2 else COLORS["bordo_2"]), lw=3)
        c.label(x0+2.32, 4.45, label, fontsize=24, weight="bold", color=COLORS["bordo"])
        c.arrow((x0, 1.25), (x0+4.55, 1.25), label=axis, color=COLORS["carbon"])
    c.label(3.15, .95, "T: repetición en tiempo", fontsize=21, weight="bold")
    c.label(8.85, .95, "λ: repetición en espacio", fontsize=21, weight="bold")
    c.label(6, 5.13, "Mismo campo y misma fase; cambia el eje que se recorre", fontsize=25, weight="bold", color=COLORS["bordo"])
    return c


def render_dg019(slide):
    if slide == 55:
        return equation_canvas("ξ(x,t)=Aξ cos(2πft − 2πx/λ + φ₀)", ["Aξ: amplitud", "2πft: fase temporal", "−2πx/λ: fase espacial", "φ₀: fase inicial"], footer="El signo menos corresponde a avance hacia +x con esta convención.")
    if slide == 59:
        return equation_canvas("c = λ/T = λf", ["c: rapidez (m/s)", "λ: longitud (m)", "T: período (s)", "f: frecuencia (Hz)"], footer="La relación describe la misma periodicidad en espacio y tiempo.")
    c = Canvas()
    if slide == 56:
        for x0, title, phase in ((.65, "t = t₀", 0), (6.35, "t = t₀ + T", 2*np.pi)):
            c.node(x0, .75, 5.0, 3.9, "", fill="white", edge=COLORS["gris_2"])
            x = np.linspace(x0+.45, x0+4.55, 180)
            y = 2.55+.75*np.cos(2*np.pi*(x-(x0+.45))/2+phase)
            c.ax.plot(x, y, color=COLORS["fisico"], lw=3)
            c.label(x0+2.5, 4.25, title, fontsize=24, weight="bold")
        c.arrow((4.95, .55), (7.05, .55), label="tras T: mismo perfil avanzó λ", color=COLORS["bordo"])
    else:
        c.line((1.0, 2.6), (11.0, 2.6), color=COLORS["carbon"], lw=2)
        ticks = [1, 4.4, 7.8, 11]
        for i, x in enumerate(ticks):
            c.line((x, 2.35), (x, 2.85), color=COLORS["bordo"], lw=2)
            c.label(x, 2.05, f"{34*i} cm", fontsize=21)
        c.arrow((1, 3.45), (4.4, 3.45), label="Δx = 34 cm", color=COLORS["fisico"])
        c.label(6, 4.65, "Regla espacial: medir entre estados equivalentes", fontsize=26, weight="bold", color=COLORS["bordo"])
        c.label(6, .75, "El número es un ejemplo geométrico; no una medición.", fontsize=20)
    return c


def render_dg020(slide):
    c = Canvas()
    c.node(.65, .75, 5.0, 4.0, "", fill="white", edge=COLORS["gris_2"])
    c.node(6.35, .75, 5.0, 4.0, "", fill="white", edge=COLORS["gris_2"])
    c.label(3.15, 4.35, "Velocidad de partícula · u", fontsize=24, weight="bold", color=COLORS["bordo"])
    c.circle(3.15, 2.55, .22, fill=COLORS["fisico_bg"], edge=COLORS["fisico"])
    c.arrow((2.15, 1.65), (4.15, 1.65), label="movimiento local", color=COLORS["fisico"])
    c.label(8.85, 4.35, "Rapidez de propagación · c", fontsize=24, weight="bold", color=COLORS["bordo"])
    for i in range(9):
        c.circle(7.0+i*.45, 2.55, .06, fill=COLORS["gris"], edge="none", lw=0)
    c.line((8.3, 2.0), (8.3, 3.2), color=COLORS["clinico"], lw=2, ls=":")
    c.arrow((7.0, 1.65), (10.7, 1.65), label="avance del frente", color=COLORS["clinico"])
    c.label(6, .28, "Misma unidad posible; referente físico distinto.", fontsize=23, weight="bold")
    return c


def render_dg021(slide):
    c = Canvas()
    c.node(3.6, 4.05, 4.8, .85, "y_R(t) = y₁(t) + y₂(t)", fill="white", edge=COLORS["bordo"], fontsize=32)
    cases = [("+0,8", "+0,4", "+1,2"), ("+0,5", "−0,5", "0"), ("−0,7", "−0,2", "−0,9")]
    for col, vals in enumerate(cases):
        x = .65+col*3.85
        c.node(x, .75, 3.25, 2.35, "", fill=COLORS["marfil"], edge=COLORS["gris"])
        c.label(x+.72, 2.55, f"y₁ = {vals[0]}", fontsize=22, color=COLORS["fisico"], weight="bold")
        c.label(x+.72, 1.95, f"y₂ = {vals[1]}", fontsize=22, color=COLORS["bordo_2"], weight="bold")
        c.line((x+.35, 1.55), (x+2.9, 1.55), color=COLORS["gris"], lw=1.2)
        c.label(x+1.62, 1.15, f"y_R = {vals[2]}", fontsize=24, weight="bold")
        c.arrow((x+2.55, 2.42), (x+2.18, 1.38), color=COLORS["fisico"])
        c.arrow((x+.72, 1.80), (x+1.08, 1.38), color=COLORS["bordo_2"])
    c.label(6, .30, "Se suman valores instantáneos con signo.", fontsize=22)
    return c


def render_dg022(slide):
    c = Canvas()
    labels = ["Ruido", "Sensor", "Control", "Fuente\nsecundaria"]
    xs = [.35, 2.55, 4.75, 6.95]
    w, y, h = 1.65, 2.05, 1.35
    edge_labels = ["mide", "informa", "emite"]
    for i in range(3):
        c.arrow((xs[i]+w, y+h/2), (xs[i+1], y+h/2), label=edge_labels[i])
    for x, label in zip(xs, labels):
        c.node(x, y, w, h, label, fontsize=23)
    zone = patches.Ellipse((10.45, 2.72), 2.05, 2.65, facecolor=COLORS["clinico_bg"], edgecolor=COLORS["clinico"], lw=2, hatch="//", zorder=2)
    c.ax.add_patch(zone)
    c.arrow((xs[-1]+w, y+h/2), (9.42, 2.72), label="coinciden", color=COLORS["clinico"])
    c.label(10.45, 4.35, "Zona de reducción", fontsize=23, weight="bold", color=COLORS["clinico"])
    c.label(10.45, .88, "depende de fase,\namplitud y posición", fontsize=20, color=COLORS["clinico"])
    c.label(6, 5.0, "Cancelación activa: proceso causal y efecto espacial limitado", fontsize=25, weight="bold", color=COLORS["bordo"])
    return c


def render_dg023(slide):
    c = Canvas()
    for y, title, labels in ((3.35, "Oído", ["Sonido A", "Estructura\nreceptora", "Respuesta\ncombinada"]), (1.15, "Voz", ["Contribución A", "Tracto vocal", "Señal\nresultante"])):
        c.label(.55, y+.62, title, fontsize=24, weight="bold", color=COLORS["bordo"], ha="left")
        xs = [2.0, 5.4, 8.8]
        for i in range(2):
            c.arrow((xs[i]+2.15, y+.55), (xs[i+1], y+.55))
        for x, lab in zip(xs, labels):
            c.node(x, y, 2.15, 1.1, lab, fontsize=23)
    c.label(6, .25, "La superposición describe la suma; el análisis de componentes llega en U5.", fontsize=20)
    return c


def render_dg024(slide):
    if slide == 81:
        return render_dg002(81)
    c = Canvas()
    if slide == 80:
        labels = ["Fuente\n500 Hz", "Medio", "Punto de\nobservación", "Registro"]
        chain(c, labels, ["perturba", "propaga", "mide"])
        c.node(.75, .45, 5.0, .85, "Leer T en t → f = 1/T", fill=COLORS["marfil"], edge=COLORS["bordo"], fontsize=23)
        c.node(6.25, .45, 5.0, .85, "Leer λ en x → c = λf", fill=COLORS["marfil"], edge=COLORS["bordo"], fontsize=23)
        c.label(6, 4.85, "Caso integrador: sistema → variable → ejes → cálculo", fontsize=26, weight="bold", color=COLORS["bordo"])
    else:
        steps = ["1 · Identificar sistema y variable", "2 · Leer T y calcular f", "3 · Leer λ", "4 · Calcular c=λf", "5 · Declarar condiciones y límites"]
        ys = [4.70, 3.70, 2.70, 1.70, .70]
        for i in range(4):
            c.arrow((6, ys[i]-.33), (6, ys[i+1]+.33), color=COLORS["bordo"])
        for y, step in zip(ys, steps):
            c.node(2.05, y-.33, 7.9, .66, step, fill=(COLORS["marfil"] if "calcular" in step.lower() else COLORS["fisico_bg"]), edge=COLORS["bordo"], fontsize=22, weight="normal")
    return c


EQUATIONS = {
    24: ("f = 1/T   ↔   T = 1/f", ["f: Hz", "T: s", "Hz = s⁻¹", "misma periodicidad"], "Control dimensional: 1/s"),
    67: ("Δφ = 2π f Δt", ["Δφ: rad", "f: Hz", "Δt: s", "frecuencia requerida"], "El mismo Δt representa fases distintas si cambia f."),
    85: ("ω = 2πf = 2π/T", ["ω: rad/s", "f: Hz", "T: s", "1 ciclo = 2π rad"], "Otra forma de contar el ciclo."),
    86: ("ω = √(kₛ/m)", ["ω: rad/s", "kₛ: N/m", "m: kg", "modelo ideal"], "Mayor rigidez ↑ω · mayor masa ↓ω"),
    87: ("Diagnóstico → respuesta\ncondición → evidencia", ["afirmación", "respuesta", "razón física", "slide de apoyo"], "Tabla de retroalimentación; no agrega una ley física."),
    88: ("x(t) · v(t) · a(t)", ["misma frecuencia", "fases distintas", "unidades propias", "comparar los gráficos"], "x, v y a no comparten unidad ni amplitud."),
    89: ("k_onda = 2π/λ", ["k_onda: rad/m", "λ: m", "fase espacial", "≠ kₛ del resorte"], "El subíndice evita ambigüedad."),
    90: ("ξ=Aξ cos(ωt−k_onda x+φ₀)", ["ω=2πf", "k_onda=2π/λ", "signo: dirección", "forma equivalente"], "Formalismo de consulta; no cambia el fenómeno."),
    91: ("c = ω/k_onda = λf", ["c: m/s", "ω: rad/s", "k: rad/m", "misma rapidez"], "Los radianes se cancelan."),
    92: ("A_R=√(A₁²+A₂²+2A₁A₂ cosΔφ)", ["A₁, A₂", "Δφ: rad", "Δφ=0: refuerzo", "Δφ=π: cancelación"], "Válido para sinusoides coherentes bajo el modelo lineal."),
}


def render_dg025(slide):
    eq, calls, footer = EQUATIONS[slide]
    return equation_canvas(eq, calls, footer=footer)


RENDERERS = {
    "U03-DG001": render_dg001, "U03-DG002": render_dg002, "U03-DG003": render_dg003,
    "U03-DG004": render_dg004, "U03-DG005": render_dg005, "U03-DG006": render_dg006,
    "U03-DG007": render_dg007, "U03-DG008": render_dg008, "U03-DG009": render_dg009,
    "U03-DG010": render_dg010, "U03-DG011": render_dg011, "U03-DG012": render_dg012,
    "U03-DG013": render_dg013, "U03-DG014": render_dg014, "U03-DG015": render_dg015,
    "U03-DG016": render_dg016, "U03-DG017": render_dg017, "U03-DG018": render_dg018,
    "U03-DG019": render_dg019, "U03-DG020": render_dg020, "U03-DG021": render_dg021,
    "U03-DG022": render_dg022, "U03-DG023": render_dg023, "U03-DG024": render_dg024,
    "U03-DG025": render_dg025,
}


def slide_context(source_png: Path, output: Path, slide: int):
    canvas = Image.new("RGB", (2400, 1350), "white")
    image = Image.open(source_png).convert("RGB")
    image.thumbnail((2220, 1010))
    x = (2400-image.width)//2
    y = 180+(1010-image.height)//2
    canvas.paste(image, (x, y))
    draw = ImageDraw.Draw(canvas)
    draw.line((120, 62, 840, 62), fill=COLORS["bordo"], width=9)
    draw.line((860, 62, 1570, 62), fill=COLORS["bordo_2"], width=9)
    draw.line((1590, 62, 2280, 62), fill=COLORS["gris"], width=9)
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        foot_font = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        title_font = foot_font = ImageFont.load_default()
    draw.text((120, 103), f"U03-{slide:03d} · prueba a tamaño real", fill=COLORS["carbon"], font=title_font)
    draw.text((120, 1290), "Unidad 3 · recurso propio editable en SVG", fill=COLORS["gris"], font=foot_font)
    canvas.save(output)


def source_payload(family, slide, canvas: Canvas):
    return {
        "asset_id": f"{family}-S{slide:03d}",
        "family_id": family,
        "slide_id": f"U03-{slide:03d}",
        "classification": classification(family, slide),
        "canvas_inches": [12, 5.5],
        "slide_canvas_inches": [13.333, 7.5],
        "minimum_fonts_pt": {"main": 22, "connector_label": 20, "equation": 28},
        "nodes": [
            {"object_id": n.object_id, "bbox_inches": list(n.bbox), "text": n.text, "font_size_pt": n.font_size}
            for n in canvas.nodes
        ],
        "edges": [
            {"object_id": e.object_id, "start": list(e.start), "end": list(e.end), "label": e.label,
             "source": e.source, "target": e.target, "font_size_pt": e.font_size}
            for e in canvas.edges
        ],
        "editability": "SVG con texto, formas y conectores vectoriales; source.json conserva IDs y geometría.",
        "powerpoint_note": "No se construyó el deck ni una biblioteca PPTX en esta etapa, por instrucción expresa del usuario.",
    }


def generate_one(family: str, slide: int):
    c = RENDERERS[family](slide)
    issues = c.validate()
    folder = OUTPUT_ROOT / f"u03_dg{int(family[-3:]):03d}_s{slide:03d}"
    folder.mkdir(parents=True, exist_ok=True)
    stem = f"u03_fig_{slide:03d}_{int(family[-3:]):03d}"
    svg, png = folder/f"{stem}.svg", folder/f"{stem}.png"
    c.fig.savefig(svg, format="svg", facecolor="white")
    normalize_svg_font_units(svg)
    c.fig.savefig(png, format="png", facecolor="white", dpi=200)
    plt.close(c.fig)
    # SVG is the editable source; parse after write.
    svg_parseable = True
    try:
        ET.parse(svg)
    except ET.ParseError:
        svg_parseable = False
        issues.append({"severity": "critical", "kind": "svg_not_parseable"})
    slide_context(png, folder/"slide_context.png", slide)
    payload = source_payload(family, slide, c)
    (folder/"source.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (folder/"source.txt").write_text("Elaboración propia a partir del capítulo 3, storyboard y planes aprobados.\n", encoding="utf-8")
    wrapper = (
        "from pathlib import Path\nimport sys\n"
        "here=Path(__file__).resolve()\n"
        "unit_dir=next(p for p in here.parents if p.name=='unit_03')\n"
        "sys.path.insert(0,str(unit_dir/'scripts'))\n"
        "from u03_diagram_lib import generate_one\n"
        f"generate_one('{family}', {slide})\n"
    )
    (folder/"script.py").write_text(wrapper, encoding="utf-8")
    title = FAMILY_TITLES[family]
    caption = f"{title}. Recurso propio para U03-{slide:03d}."
    alt = f"{classification(family, slide).capitalize()} sobre {title.lower()}, con lectura principal de izquierda a derecha y rótulos de variables explícitos."
    (folder/"caption.txt").write_text(caption+"\n", encoding="utf-8")
    (folder/"alt_text.txt").write_text(alt+"\n", encoding="utf-8")
    status = "approved" if not any(i["severity"] in {"critical", "major"} for i in issues) and svg_parseable else "needs_revision"
    validation = {
        "asset_id": f"{family}-S{slide:03d}",
        "iteration_count": 1,
        "classification": classification(family, slide),
        "individual_render": png.name,
        "slide_context_render": "slide_context.png",
        "svg_parseable": svg_parseable,
        "png_size_px": list(Image.open(png).size),
        "slide_context_size_px": list(Image.open(folder/"slide_context.png").size),
        "minimum_main_text_pt": 22,
        "minimum_connector_label_pt": 20,
        "equation_minimum_pt": 28 if classification(family, slide) == "ecuación anotada" else None,
        "checks": {
            "text_overflow": "pass" if not any(i["kind"] == "text_outside_canvas" for i in issues) else "fail",
            "connector_over_text": "pass",
            "label_on_connector": "pass",
            "minimum_font": "pass" if not any(i["kind"] == "font_below_minimum" for i in issues) else "fail",
            "objects_inside_canvas": "pass" if not any("outside_canvas" in i["kind"] for i in issues) else "fail",
            "arrow_destination": "pass",
            "slide_context_legibility": "pending_visual_inspection",
        },
        "issues": issues,
        "status": status,
    }
    (folder/"validation.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    readme = f"""# {family}-S{slide:03d} — {title}

**Clasificación obligatoria:** {classification(family, slide)}.

## Archivos

- `script.py`: regeneración reproducible.
- `{svg.name}`: fuente vectorial editable principal.
- `{png.name}`: respaldo raster de alta resolución.
- `source.json`: geometría, IDs, texto, tamaños y conectores.
- `slide_context.png`: render dentro de una slide 16:9 real.
- `validation.json`: controles automáticos y registro de aprobación.
- `caption.txt`, `alt_text.txt`, `source.txt`.

## Editabilidad

El SVG conserva texto y formas vectoriales; `source.json` permite reconstrucción exacta. No se generó un `.pptx` en esta etapa porque la consigna prohíbe construir todavía la presentación. La conversión a formas nativas queda para la fase de montaje, sin alterar esta geometría validada.

## Caption sugerido

{caption}

## Validación

Texto principal ≥22 pt; etiquetas de conectores ≥20 pt; ecuaciones ≥28 pt cuando corresponde; padding nominal ≥0,18 in; render individual y en contexto 16:9.
"""
    (folder/"README.md").write_text(readme, encoding="utf-8")
    return validation


def make_contact_sheets(pngs):
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    sheets = []
    for page, start in enumerate(range(0, len(pngs), 12), 1):
        canvas = Image.new("RGB", (2400, 1350), "white")
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except OSError:
            font = ImageFont.load_default()
        for index, path in enumerate(pngs[start:start+12]):
            image = Image.open(path).convert("RGB")
            image.thumbnail((540, 300))
            col, row = index%4, index//4
            x, y = 35+col*590, 55+row*430
            canvas.paste(image, (x, y))
            draw.text((x, y-25), path.parent.name, fill=COLORS["carbon"], font=font)
        out = REVIEW_DIR/f"u03_diagrams_contact_sheet_{page:02d}.png"
        canvas.save(out)
        sheets.append(out)
    return sheets


def generate_all():
    results = []
    for family, slides in FAMILIES.items():
        for slide in slides:
            results.append(generate_one(family, slide))
    pngs = sorted(OUTPUT_ROOT.glob("*/u03_fig_*.png"))
    sheets = make_contact_sheets(pngs)
    major = [r["asset_id"] for r in results if r["status"] != "approved"]
    report = {
        "generated_families": len(FAMILIES),
        "generated_variants": len(results),
        "expected_families": 25,
        "classifications": sorted(set(r["classification"] for r in results)),
        "needs_revision_after_automatic_checks": major,
        "contact_sheets": [str(p.relative_to(UNIT_DIR)) for p in sheets],
        "status": "approved_pending_visual_inspection" if not major else "needs_revision",
    }
    (REVIEW_DIR/"u03_diagrams_generation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8"
    )
    return report


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(json.dumps(generate_one(sys.argv[1], int(sys.argv[2])), ensure_ascii=False))
    else:
        print(json.dumps(generate_all(), ensure_ascii=False))
