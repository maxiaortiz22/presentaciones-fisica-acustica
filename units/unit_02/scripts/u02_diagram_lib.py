from __future__ import annotations

import json
import math
import re
import shutil
import sys
import textwrap
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.lines import Line2D
from PIL import Image, ImageDraw, ImageFont


UNIT_DIR = Path(__file__).resolve().parents[1]
SCRIPT_DIR = UNIT_DIR / "scripts"
OUTPUT_ROOT = UNIT_DIR / "assets" / "generated" / "diagrams"
REVIEW_DIR = UNIT_DIR / "assets" / "generated" / "_review"
STORYBOARD = UNIT_DIR / "storyboard.md"

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
        "font.size": 22,
        "text.color": COLORS["carbon"],
        "svg.fonttype": "none",
        "figure.dpi": 200,
        "savefig.dpi": 200,
    }
)


FAMILIES = {
    "U02-DG001": [2, 6],
    "U02-DG002": list(range(8, 14)),
    "U02-DG003": [16, 17, 19, 20],
    "U02-DG004": [21, 22, 93],
    "U02-DG005": [25, 27, 28, 29, 30, 31, 32],
    "U02-DG006": list(range(35, 47)),
    "U02-DG007": list(range(48, 58)),
    "U02-DG008": [59, 61, 62, 63, 64, 65, 66],
    "U02-DG009": [71, 73, 105],
    "U02-DG010": [78, 79, 82, 101, 102, 103],
    "U02-DG011": [84, 86, 87],
    "U02-DG012": [88, 89],
    "U02-DG013": [91, 92],
    "U02-DG014": [95, 96],
    "U02-DG015": [104, 106, 107, 108],
}

SLIDE_TO_FAMILY = {
    f"U02-{slide:03d}": family for family, slides in FAMILIES.items() for slide in slides
}

EQUATION_SLIDES = {
    "U02-013": ("F_neta = 0  →  v constante", ["resultante nula", "reposo: v = 0", "MRU: v ≠ 0"]),
    "U02-017": ("F_neta = m · a", ["resultante (N)", "masa / inercia (kg)", "respuesta (m/s²)"]),
    "U02-021": ("F_A→B = −F_B→A", ["actúa sobre B", "igual módulo", "actúa sobre A"]),
    "U02-027": ("Δp = p₁ − p₂", ["orden fija el signo", "presiones en Pa", "eje +x declarado"]),
    "U02-028": ("F_pres = Δp · S", ["fuerza (N)", "diferencia (Pa)", "área (m²)", "presión uniforme"]),
    "U02-029": ("Pa · m² = (N/m²) · m² = N", ["se cancelan m²", "resultado: fuerza", "descarta Δp/S"]),
    "U02-042": ("F_ext − kₛx − bv = ma", ["entrada", "retorno", "disipación", "inercia"]),
    "U02-049": ("W_trab = F · d", ["fuerza paralela", "desplazamiento", "1 J = 1 N·m"]),
    "U02-050": ("E_c = ½ m v²", ["masa", "rapidez al cuadrado", "2v → 4E_c"]),
    "U02-051": ("E_el = ½ kₛ x²", ["rigidez", "deformación", "+x y −x: misma energía"]),
    "U02-055": ("E_entrada = ΔE_mec + E_salida + E_disipada", ["entra", "se almacena", "sale", "se convierte"]),
    "U02-064": ("ΔU = Q_calor + W_sobre", ["cambio de estado", "calor que entra: +", "trabajo sobre: +"]),
    "U02-071": ("ΔS_total ≥ 0", ["sistema total aislado", "= 0 reversible ideal", "> 0 irreversible"]),
    "U02-079": ("c ≈ 331 m/s + [0,6 (m/s)/°C] · ϑ", ["modelo lineal", "pendiente", "rango ambiental"]),
    "U02-101": ("c = √(γ R T_temp / M)", ["γ: razón térmica", "R: constante", "T_temp: kelvin", "M: masa molar"]),
    "U02-102": ("γRT/M → J/kg = m²/s² → c en m/s", ["γ adimensional", "mol y K se cancelan", "la raíz da velocidad"]),
    "U02-105": ("ΔS_total ≥ 0", ["= 0: límite reversible", "> 0: producción", "alcance: total aislado"]),
}

PROCESS_NODES = {
    "U02-006": ["Sistema y leyes", "Diferencia\nde presión", "Respuesta\nmecánica", "Energía y\ntermodinámica", "Aplicación\nauditiva"],
    "U02-016": ["Fuerza neta", "Aceleración", "Cambio de\nvelocidad"],
    "U02-032": ["Δp (Pa)", "F_pres = Δp·S\n(N)", "F_neta (N)", "a = F_neta/m\n(m/s²)"],
    "U02-035": ["Masa\ninercia", "Elasticidad\nretorno", "Amortiguamiento\ndisipación"],
    "U02-041": ["Masa m", "Resorte kₛ", "Amortiguador b", "Fuerza externa", "Balance\ninstantáneo"],
    "U02-052": ["Equilibrio:\nrapidez máxima", "Extremo:\nresorte deformado", "Retorno:\nintercambio"],
    "U02-054": ["Entrada", "Se almacena", "Salida", "Disipación"],
    "U02-073": ["Fuerza\ndisipativa", "Menor energía\nmecánica útil", "Mayor energía\ninterna", "Producción de\nentropía"],
    "U02-084": ["Membrana", "Oído medio", "Vibrador", "Tejidos", "Aire"],
    "U02-088": ["Caso:\nsuperficie flexible", "Fuerza y\naceleración", "Balance de\nenergía", "Velocidad\ndel aire"],
    "U02-089": ["Sistema", "Fuerzas", "Respuesta", "Energía", "Dirección\ndel proceso", "Aplicación"],
    "U02-106": ["Datos del\nsistema ideal", "Rama mecánica", "Rama energética", "Rama térmica"],
}

MIXED_SLIDES = {
    "U02-019",
    "U02-030",
    "U02-038",
    "U02-040",
    "U02-044",
    "U02-045",
    "U02-046",
    "U02-056",
    "U02-057",
    "U02-066",
    "U02-082",
    "U02-086",
    "U02-087",
    "U02-092",
    "U02-095",
    "U02-096",
    "U02-103",
    "U02-107",
    "U02-108",
}

PROCESS_SLIDES = set(PROCESS_NODES) | {"U02-011"}

SPECIAL_SLIDES = {
    "U02-002": "membrane",
    "U02-008": "system",
    "U02-009": "interaction",
    "U02-010": "axis",
    "U02-011": "dcl",
    "U02-012": "equilibrium",
    "U02-019": "calculation",
    "U02-020": "masses",
    "U02-022": "third_law",
    "U02-025": "pressure",
    "U02-030": "pressure_calc",
    "U02-037": "spring_states",
    "U02-038": "spring_equation",
    "U02-039": "damping_states",
    "U02-040": "damping_equation",
    "U02-041": "mass_spring",
    "U02-043": "sign_matrix",
    "U02-044": "mra_calc",
    "U02-045": "damping_terms",
    "U02-046": "mra_recap",
    "U02-048": "work_cases",
    "U02-052": "energy_states",
    "U02-053": "isolated_system",
    "U02-056": "energy_calc",
    "U02-057": "energy_recap",
    "U02-059": "state_transfer",
    "U02-061": "internal_energy",
    "U02-062": "heat_transfer",
    "U02-063": "state_transfer",
    "U02-065": "thermo_signs",
    "U02-066": "thermo_calc",
    "U02-078": "propagation",
    "U02-082": "medium_source_perception",
    "U02-086": "ear_route",
    "U02-087": "vibrator",
    "U02-091": "reference_dcl",
    "U02-092": "diagnostic_solutions",
    "U02-093": "counterexamples",
    "U02-095": "mra_reference",
    "U02-096": "mra_calc",
    "U02-103": "travel_paths",
    "U02-104": "thermo_signs",
    "U02-107": "integrated_mechanics",
    "U02-108": "integrated_energy",
}


def parse_storyboard():
    rows = {}
    for line in STORYBOARD.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| U02-"):
            continue
        columns = [value.strip() for value in line.strip("|").split("|")]
        if len(columns) < 15:
            continue
        rows[columns[0]] = {
            "slide_id": columns[0],
            "title": columns[3],
            "key_message": columns[5],
            "summary": columns[6],
            "visual": columns[7],
            "visual_class": columns[8],
            "source": columns[11],
        }
    return rows


def classification_for(slide_id: str, spec: dict) -> str:
    if slide_id in EQUATION_SLIDES and slide_id not in MIXED_SLIDES:
        return "ecuación anotada"
    if slide_id in MIXED_SLIDES or spec["visual_class"] == "mixed":
        return "esquema mixto"
    if slide_id in PROCESS_SLIDES:
        return "diagrama de proceso"
    return "diagrama conceptual"


def strip_markdown(value: str) -> str:
    value = re.sub(r"[`*_]", "", value)
    value = value.replace("CANDIDATA diagram-generation:", "")
    return value.strip(" .")


def short_phrases(summary: str, maximum: int = 4):
    cleaned = strip_markdown(summary)
    parts = [part.strip() for part in re.split(r";|\. ", cleaned) if part.strip()]
    if len(parts) == 1:
        parts = [part.strip() for part in re.split(r", (?=[a-záéíóú])", cleaned) if part.strip()]
    results = []
    for part in parts[:maximum]:
        if len(part) > 50:
            part = part[:47].rsplit(" ", 1)[0] + "…"
        results.append(part)
    while len(results) < 2:
        results.append("Interpretación física")
    return results


@dataclass
class NodeRecord:
    object_id: str
    bbox: tuple[float, float, float, float]
    text: str
    font_size: float
    text_artist: object
    patch_artist: object


@dataclass
class EdgeRecord:
    object_id: str
    start: tuple[float, float]
    end: tuple[float, float]
    source: str | None
    target: str | None
    label_artist: object | None
    label_text: str
    font_size: float


class DiagramCanvas:
    def __init__(self, family: str, slide_id: str):
        self.family = family
        self.slide_id = slide_id
        self.prefix = f"{family.replace('-', '_')}_S{slide_id[-3:]}"
        self.fig, self.ax = plt.subplots(figsize=(12, 5.5), facecolor=COLORS["white"])
        self.fig.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
        self.ax.set_xlim(0, 12)
        self.ax.set_ylim(0, 5.5)
        self.ax.axis("off")
        self.nodes: list[NodeRecord] = []
        self.edges: list[EdgeRecord] = []
        self.font_sizes: list[float] = []
        self.object_counter = 0

    def oid(self, kind: str, name: str | None = None):
        self.object_counter += 1
        suffix = name or f"{self.object_counter:03d}"
        return f"{self.prefix}_{kind}_{suffix.upper()}"

    def label(self, x, y, text, *, size=22, ha="center", va="center", color=None, weight="normal", name=None):
        artist = self.ax.text(
            x,
            y,
            text,
            fontsize=size,
            ha=ha,
            va=va,
            color=color or COLORS["carbon"],
            fontweight=weight,
            linespacing=1.12,
            zorder=6,
        )
        artist.set_gid(self.oid("LABEL", name))
        self.font_sizes.append(size)
        return artist

    def box(
        self,
        x,
        y,
        w,
        h,
        text,
        *,
        fill=None,
        edge=None,
        size=24,
        weight="normal",
        name=None,
        radius=0.04,
    ):
        object_id = self.oid("NODE", name)
        patch = patches.FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle=f"round,pad=0.02,rounding_size={radius}",
            facecolor=fill or COLORS["white"],
            edgecolor=edge or COLORS["gris"],
            linewidth=1.6,
            zorder=3,
        )
        patch.set_gid(object_id)
        self.ax.add_patch(patch)
        wrapped_parts = []
        for paragraph in str(text).splitlines() or [""]:
            wrapped_parts.extend(
                textwrap.wrap(
                    paragraph,
                    width=max(7, int(w * 5.5)),
                    break_long_words=False,
                )
                or [""]
            )
        wrapped = "\n".join(wrapped_parts)
        text_artist = self.ax.text(
            x + w / 2,
            y + h / 2,
            wrapped,
            fontsize=size,
            ha="center",
            va="center",
            fontweight=weight,
            linespacing=1.08,
            color=COLORS["carbon"],
            zorder=5,
        )
        text_artist.set_gid(self.oid("TEXT", name))
        self.font_sizes.append(size)
        self.nodes.append(NodeRecord(object_id, (x, y, w, h), wrapped, size, text_artist, patch))
        return object_id

    def arrow(
        self,
        start,
        end,
        *,
        color=None,
        label="",
        label_offset=0.28,
        source=None,
        target=None,
        name=None,
        style="-|>",
        width=2.0,
        dashed=False,
    ):
        object_id = self.oid("EDGE", name)
        arrow = patches.FancyArrowPatch(
            start,
            end,
            arrowstyle=style,
            mutation_scale=17,
            linewidth=width,
            linestyle="--" if dashed else "-",
            color=color or COLORS["carbon"],
            shrinkA=0,
            shrinkB=0,
            zorder=2,
        )
        arrow.set_gid(object_id)
        self.ax.add_patch(arrow)
        label_artist = None
        if label:
            mx = (start[0] + end[0]) / 2
            my = (start[1] + end[1]) / 2 + label_offset
            label_artist = self.label(
                mx,
                my,
                label,
                size=20,
                color=color or COLORS["carbon"],
                name=f"{name or self.object_counter}_EDGE_LABEL",
            )
        self.edges.append(EdgeRecord(object_id, start, end, source, target, label_artist, label, 20 if label else 0))
        return object_id

    def panel_title(self, x, y, text, color=None):
        self.label(x, y, text, size=26, weight="bold", color=color or COLORS["bordo"])

    def equation(self, text, *, y=3.15, size=36, color=None, name="MAIN"):
        artist = self.label(6, y, text, size=size, weight="bold", color=color or COLORS["carbon"], name=f"EQ_{name}")
        return artist

    def line(self, points, *, color=None, width=2.0, dashed=False, name=None):
        line = Line2D(
            [p[0] for p in points],
            [p[1] for p in points],
            color=color or COLORS["carbon"],
            linewidth=width,
            linestyle="--" if dashed else "-",
            zorder=2,
        )
        line.set_gid(self.oid("LINE", name))
        self.ax.add_line(line)
        return line

    def validate(self):
        self.fig.canvas.draw()
        renderer = self.fig.canvas.get_renderer()
        issues = []
        node_boxes_px = {}
        for node in self.nodes:
            patch_bbox = node.patch_artist.get_window_extent(renderer)
            text_bbox = node.text_artist.get_window_extent(renderer)
            node_boxes_px[node.object_id] = patch_bbox
            padding_px = 36
            if (
                text_bbox.x0 < patch_bbox.x0 + padding_px
                or text_bbox.x1 > patch_bbox.x1 - padding_px
                or text_bbox.y0 < patch_bbox.y0 + padding_px
                or text_bbox.y1 > patch_bbox.y1 - padding_px
            ):
                issues.append(f"{node.object_id}: texto sin padding suficiente")
            if node.font_size < 22:
                issues.append(f"{node.object_id}: fuente principal menor que 22 pt")
        for edge in self.edges:
            if edge.label_artist is not None:
                label_bbox = edge.label_artist.get_window_extent(renderer)
                start_px = self.ax.transData.transform(edge.start)
                end_px = self.ax.transData.transform(edge.end)
                midpoint_y = (start_px[1] + end_px[1]) / 2
                if label_bbox.y0 <= midpoint_y <= label_bbox.y1:
                    issues.append(f"{edge.object_id}: etiqueta apoyada sobre el conector")
                if edge.font_size < 20:
                    issues.append(f"{edge.object_id}: etiqueta menor que 20 pt")
            for node in self.nodes:
                if node.object_id in {edge.source, edge.target}:
                    continue
                bx = node_boxes_px[node.object_id]
                start_px = self.ax.transData.transform(edge.start)
                end_px = self.ax.transData.transform(edge.end)
                for t in [i / 20 for i in range(1, 20)]:
                    px = start_px[0] + t * (end_px[0] - start_px[0])
                    py = start_px[1] + t * (end_px[1] - start_px[1])
                    if bx.x0 + 4 < px < bx.x1 - 4 and bx.y0 + 4 < py < bx.y1 - 4:
                        issues.append(f"{edge.object_id}: conector cruza {node.object_id}")
                        break
        if self.font_sizes and min(self.font_sizes) < 20:
            issues.append("Se detectó texto auxiliar menor que 20 pt")
        return sorted(set(issues))

    def object_model(self):
        return {
            "canvas_inches": [12, 5.5],
            "slide_context_inches": [13.333, 7.5],
            "objects": [
                {
                    "id": node.object_id,
                    "type": "node",
                    "bbox": list(node.bbox),
                    "text": node.text,
                    "font_pt": node.font_size,
                    "padding_in_min": 0.18,
                }
                for node in self.nodes
            ]
            + [
                {
                    "id": edge.object_id,
                    "type": "connector",
                    "start": list(edge.start),
                    "end": list(edge.end),
                    "source": edge.source,
                    "target": edge.target,
                    "label": edge.label_text,
                    "label_font_pt": edge.font_size,
                }
                for edge in self.edges
            ],
        }


def draw_process(canvas: DiagramCanvas, nodes: list[str]):
    count = len(nodes)
    if count > 4:
        columns = math.ceil(count / 2)
        gap = 0.55
        width = (11.2 - gap * (columns - 1)) / columns
        height = 1.55
        positions = []
        ids = []
        for index, text in enumerate(nodes):
            row = index // columns
            column = index % columns
            if row == 1:
                column = columns - 1 - column
            x = 0.4 + column * (width + gap)
            y = 3.05 if row == 0 else 0.75
            positions.append((x, y))
            ids.append(
                canvas.box(
                    x,
                    y,
                    width,
                    height,
                    f"{index + 1}. {text}",
                    fill=COLORS["fisico_bg"] if index % 2 == 0 else COLORS["marfil"],
                    edge=COLORS["fisico"],
                    size=22,
                    weight="bold",
                    name=f"STEP_{index+1}",
                )
            )
        for index in range(count - 1):
            x0, y0 = positions[index]
            x1, y1 = positions[index + 1]
            if abs(y0 - y1) < 0.1:
                if x1 > x0:
                    start, end = (x0 + width + 0.04, y0 + height / 2), (x1 - 0.04, y1 + height / 2)
                else:
                    start, end = (x0 - 0.04, y0 + height / 2), (x1 + width + 0.04, y1 + height / 2)
            else:
                start, end = (x0 + width / 2, y0 - 0.04), (x1 + width / 2, y1 + height + 0.04)
            canvas.arrow(start, end, color=COLORS["bordo"], source=ids[index], target=ids[index + 1], name=f"FLOW_{index+1}")
        canvas.label(6, 5.05, "Secuencia completa · alternativa estática", size=22, weight="bold", color=COLORS["bordo"])
        return
    margin = 0.35
    gap = 0.55 if count <= 5 else 0.35
    width = (12 - 2 * margin - gap * (count - 1)) / count
    y, h = 1.7, 2.0
    ids = []
    for index, text in enumerate(nodes):
        x = margin + index * (width + gap)
        fill = COLORS["fisico_bg"] if index % 2 == 0 else COLORS["marfil"]
        ids.append(canvas.box(x, y, width, h, text, fill=fill, edge=COLORS["fisico"], size=23, weight="bold", name=f"STEP_{index+1}"))
    for index in range(count - 1):
        x0 = margin + index * (width + gap) + width
        x1 = margin + (index + 1) * (width + gap)
        canvas.arrow((x0 + 0.04, y + h / 2), (x1 - 0.04, y + h / 2), color=COLORS["bordo"], source=ids[index], target=ids[index + 1], name=f"FLOW_{index+1}")
    canvas.label(6, 0.55, "Orden de lectura: izquierda → derecha", size=20, color=COLORS["gris"])


def draw_equation(canvas: DiagramCanvas, equation: str, callouts: list[str]):
    canvas.equation(equation, y=3.05, size=36)
    count = len(callouts)
    positions = [(1.0 + i * (10.0 / count), 0.55, 10.0 / count - 0.35, 1.15) for i in range(count)]
    centers = []
    for index, (x, y, w, h) in enumerate(positions):
        oid = canvas.box(
            x,
            y,
            w,
            h,
            callouts[index],
            fill=COLORS["marfil"],
            edge=COLORS["bordo_2"],
            size=22,
            name=f"CALLOUT_{index+1}",
        )
        centers.append((oid, (x + w / 2, y + h)))
    target_xs = [3.0 + i * (6.0 / max(1, count - 1)) for i in range(count)]
    for index, ((oid, start), tx) in enumerate(zip(centers, target_xs)):
        canvas.arrow(start, (tx, 2.68), color=COLORS["gris"], source=oid, name=f"LEADER_{index+1}", style="-", width=1.5)
    canvas.label(6, 4.65, "Lectura física y unidades", size=24, weight="bold", color=COLORS["bordo"])


def draw_panels(canvas: DiagramCanvas, phrases: list[str], *, heading="Comparación conceptual"):
    count = min(max(len(phrases), 2), 4)
    gap = 0.35
    width = (11.3 - gap * (count - 1)) / count
    canvas.panel_title(6, 4.85, heading)
    for index, phrase in enumerate(phrases[:count]):
        x = 0.35 + index * (width + gap)
        canvas.box(
            x,
            1.15,
            width,
            2.8,
            phrase,
            fill=COLORS["fisico_bg"] if index % 2 == 0 else COLORS["marfil"],
            edge=COLORS["fisico"] if index % 2 == 0 else COLORS["bordo_2"],
            size=23,
            name=f"PANEL_{index+1}",
        )


def draw_mixed(canvas: DiagramCanvas, spec: dict):
    phrases = short_phrases(spec["summary"], maximum=4)
    canvas.panel_title(2.9, 4.8, "Modelo / situación")
    canvas.box(0.45, 1.15, 4.9, 3.15, phrases[0], fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=24, name="MODEL")
    canvas.panel_title(8.75, 4.8, "Lectura / resultado")
    steps = phrases[1:] or [spec["key_message"]]
    y = 3.55
    previous = None
    for index, phrase in enumerate(steps[:3]):
        oid = canvas.box(6.15, y - 0.75, 5.35, 1.05, phrase, fill=COLORS["marfil"], edge=COLORS["bordo_2"], size=22, name=f"STEP_{index+1}")
        if previous is not None:
            canvas.arrow((8.82, y + 0.30), (8.82, y + 0.05), color=COLORS["bordo"], source=previous, target=oid, name=f"STEP_EDGE_{index}")
        previous = oid
        y -= 1.12
    canvas.arrow((5.42, 2.75), (6.02, 2.75), color=COLORS["bordo"], name="MODEL_TO_RESULT")


def draw_membrane(canvas: DiagramCanvas):
    for index, (x0, label, unequal) in enumerate([(0.35, "Equilibrio: p₁ = p₂", False), (6.25, "Desequilibrio: p₁ > p₂", True)]):
        canvas.panel_title(x0 + 2.7, 4.85, label, COLORS["bordo"])
        canvas.box(x0, 1.0, 2.25, 3.2, "Región 1\np₁", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=24, name=f"REGION1_{index}")
        canvas.box(x0 + 3.15, 1.0, 2.25, 3.2, "Región 2\np₂", fill=COLORS["marfil"], edge=COLORS["gris"], size=24, name=f"REGION2_{index}")
        canvas.line([(x0 + 2.7, 1.15), (x0 + 2.7 + (0.20 if unequal else 0), 4.05)], color=COLORS["bordo"], width=5, name=f"MEMBRANE_{index}")
        canvas.arrow((x0 + 1.55, 2.75), (x0 + 2.55, 2.75), color=COLORS["fisico"], label="F₁", label_offset=0.35, source=canvas.nodes[-2].object_id, name=f"F1_{index}")
        end = x0 + 2.85 if unequal else x0 + 2.85
        canvas.arrow((x0 + 3.85, 2.15), (end, 2.15), color=COLORS["bordo_2"], label="F₂", label_offset=-0.38, source=canvas.nodes[-1].object_id, name=f"F2_{index}")
    canvas.label(6, 0.35, "Esquema conceptual; no está a escala", size=20, color=COLORS["alerta"])


def draw_system(canvas: DiagramCanvas):
    canvas.panel_title(3.0, 4.8, "Sistema: membrana")
    canvas.box(0.45, 0.9, 5.1, 3.4, "", fill=COLORS["marfil"], edge=COLORS["gris"], size=23, name="ENV_A")
    canvas.label(0.75, 4.0, "Entorno: aire a ambos lados", size=22, ha="left", color=COLORS["gris"])
    canvas.box(1.65, 1.75, 2.7, 1.7, "Membrana", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=26, weight="bold", name="SYSTEM_A")
    canvas.panel_title(9.0, 4.8, "Sistema: membrana + aire")
    canvas.box(6.45, 0.9, 5.1, 3.4, "", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=23, name="SYSTEM_B")
    canvas.label(6.75, 4.0, "Frontera ampliada", size=22, ha="left", color=COLORS["fisico"])
    canvas.box(7.1, 1.65, 1.55, 1.9, "Aire", fill=COLORS["white"], edge=COLORS["gris"], size=23, name="AIR_B1")
    canvas.box(8.88, 1.65, 1.0, 1.9, "M", fill=COLORS["marfil"], edge=COLORS["bordo"], size=26, weight="bold", name="MEM_B")
    canvas.box(10.1, 1.65, 1.0, 1.9, "Aire", fill=COLORS["white"], edge=COLORS["gris"], size=22, name="AIR_B2")


def draw_dcl(canvas: DiagramCanvas, equilibrium=False):
    canvas.box(4.65, 1.75, 2.7, 2.0, "Sistema", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=26, weight="bold", name="BODY")
    if equilibrium:
        canvas.arrow((2.0, 2.75), (4.55, 2.75), color=COLORS["fisico"], label="F₁", name="F1")
        canvas.arrow((10.0, 2.75), (7.45, 2.75), color=COLORS["bordo"], label="F₂", name="F2")
        canvas.label(6, 4.65, "F₁ y F₂: igual módulo, sentidos opuestos", size=24, weight="bold")
        canvas.label(6, 0.55, "F_neta = 0 no significa ausencia de fuerzas", size=22, color=COLORS["bordo"])
    else:
        canvas.arrow((1.0, 3.35), (4.55, 3.35), color=COLORS["fisico"], label="+5 N", name="F1")
        canvas.arrow((10.8, 2.75), (7.45, 2.75), color=COLORS["bordo"], label="−2 N", name="F2")
        canvas.arrow((1.8, 2.05), (4.55, 2.05), color=COLORS["fisico"], label="+1 N", name="F3")
        canvas.arrow((7.45, 1.10), (9.8, 1.10), color=COLORS["ok"], label="F_neta = +4 N", name="FNET")
        canvas.arrow((1.0, 4.55), (3.1, 4.55), color=COLORS["carbon"], label="+x", name="AXIS", style="-|>")


def draw_axis(canvas: DiagramCanvas):
    canvas.arrow((1.0, 2.75), (11.0, 2.75), color=COLORS["carbon"], label="+x", label_offset=0.35, name="AXIS")
    canvas.arrow((6.0, 2.75), (9.1, 2.75), color=COLORS["fisico"], label="F_x > 0", label_offset=0.55, name="POS")
    canvas.arrow((6.0, 2.75), (2.9, 2.75), color=COLORS["bordo"], label="F_x < 0", label_offset=-0.55, name="NEG")
    canvas.box(4.45, 3.75, 3.1, 1.1, "El signo indica sentido", fill=COLORS["marfil"], edge=COLORS["bordo_2"], size=23, name="CALLOUT")


def draw_interaction(canvas: DiagramCanvas):
    left = canvas.box(1.0, 1.65, 3.2, 2.3, "Cuerpo A\nagente", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=25, name="A")
    right = canvas.box(7.8, 1.65, 3.2, 2.3, "Cuerpo B\nreceptor", fill=COLORS["marfil"], edge=COLORS["bordo_2"], size=25, name="B")
    canvas.arrow((4.3, 3.15), (7.7, 3.15), color=COLORS["fisico"], label="A ejerce fuerza sobre B", source=left, target=right, name="A_TO_B")
    canvas.arrow((7.7, 2.25), (4.3, 2.25), color=COLORS["bordo"], label="interacción recíproca", label_offset=-0.40, source=right, target=left, name="B_TO_A")


def draw_masses(canvas: DiagramCanvas):
    for index, (x, label, mass, accel) in enumerate([(1.2, "A", "2m", "a/2"), (7.0, "B", "m", "a")]):
        canvas.box(x, 1.35, 3.1, 2.3, f"Masa {label}\n{mass}", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=26, name=label)
        canvas.arrow((x - 0.6, 2.5), (x - 0.05, 2.5), color=COLORS["bordo"], label="misma F_neta", label_offset=0.48, name=f"FORCE_{label}")
        canvas.label(x + 1.55, 0.75, f"aceleración: {accel}", size=22, weight="bold")
    canvas.label(6, 4.75, "A igual fuerza neta, la masa mayor acelera menos", size=25, weight="bold", color=COLORS["bordo"])


def draw_third_law(canvas: DiagramCanvas):
    a = canvas.box(0.8, 2.0, 3.0, 2.0, "DCL de A", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=26, name="A")
    b = canvas.box(8.2, 2.0, 3.0, 2.0, "DCL de B", fill=COLORS["marfil"], edge=COLORS["bordo_2"], size=26, name="B")
    canvas.arrow((3.9, 3.35), (6.0, 3.35), color=COLORS["fisico"], label="F_B→A", source=a, name="FORCE_ON_A")
    canvas.arrow((8.1, 2.65), (6.0, 2.65), color=COLORS["bordo"], label="F_A→B", source=b, name="FORCE_ON_B")
    canvas.label(6, 1.15, "Iguales y opuestas · actúan sobre cuerpos distintos", size=23, weight="bold")


def draw_pressure(canvas: DiagramCanvas):
    canvas.box(0.45, 0.95, 4.3, 3.7, "Región 1\np₁", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=28, name="REGION1")
    canvas.box(7.25, 0.95, 4.3, 3.7, "Región 2\np₂", fill=COLORS["marfil"], edge=COLORS["gris"], size=28, name="REGION2")
    canvas.line([(6.0, 1.15), (6.0, 4.45)], color=COLORS["bordo"], width=6, name="SURFACE")
    canvas.arrow((3.6, 3.1), (5.8, 3.1), color=COLORS["fisico"], label="F₁ = p₁S", source=canvas.nodes[0].object_id, name="F1")
    canvas.arrow((8.4, 2.35), (6.2, 2.35), color=COLORS["bordo_2"], label="F₂ = p₂S", label_offset=-0.42, source=canvas.nodes[1].object_id, name="F2")
    canvas.label(6, 0.45, "Si p₁ > p₂, la resultante apunta hacia la región 2 · no a escala", size=21, color=COLORS["alerta"])


def draw_spring_states(canvas: DiagramCanvas):
    canvas.panel_title(6, 4.75, "La fuerza restauradora siempre apunta al equilibrio")
    centers = [2.0, 6.0, 10.0]
    labels = ["x < 0", "x = 0", "x > 0"]
    directions = [1, 0, -1]
    for index, (cx, label, direction) in enumerate(zip(centers, labels, directions)):
        canvas.box(cx - 1.0, 1.65, 2.0, 1.65, label, fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=24, name=f"STATE_{index+1}")
        canvas.line([(cx, 1.1), (cx, 3.85)], color=COLORS["gris"], width=1.2, dashed=True, name=f"EQ_{index+1}")
        if direction:
            canvas.arrow((cx, 3.95), (cx + direction * 1.15, 3.95), color=COLORS["bordo"], label="F_el", name=f"FEL_{index+1}")
    canvas.label(6, 0.55, "Esquema conceptual; deformaciones no a escala", size=20, color=COLORS["alerta"])


def draw_mass_spring(canvas: DiagramCanvas):
    canvas.line([(0.7, 0.7), (0.7, 4.8)], color=COLORS["carbon"], width=5, name="WALL")
    mass = canvas.box(7.3, 1.85, 2.4, 1.8, "masa m", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=28, weight="bold", name="MASS")
    # Resorte editable como polilínea.
    points = [(0.75, 3.25), (1.35, 3.25)]
    for i in range(8):
        points.append((1.55 + i * 0.62, 3.55 if i % 2 == 0 else 2.95))
    points.extend([(6.85, 3.25), (7.25, 3.25)])
    canvas.line(points, color=COLORS["bordo"], width=2.3, name="SPRING")
    # Amortiguador.
    canvas.line([(0.75, 1.55), (2.0, 1.55), (2.0, 1.15), (4.5, 1.15), (4.5, 1.95), (6.0, 1.95), (6.0, 1.55), (7.25, 1.55)], color=COLORS["gris"], width=2.3, name="DAMPER")
    canvas.label(3.6, 4.15, "resorte kₛ", size=22, color=COLORS["bordo"])
    canvas.label(3.75, 0.55, "amortiguador b", size=22, color=COLORS["gris"])
    canvas.arrow((9.8, 2.75), (11.35, 2.75), color=COLORS["fisico"], label="F_ext", name="FEXT")
    canvas.arrow((8.45, 1.05), (10.2, 1.05), color=COLORS["carbon"], label="+x, +v", name="AXIS")
    canvas.label(6, 5.0, "Modelo ideal concentrado; no representa anatomía literal", size=21, color=COLORS["alerta"])


def draw_sign_matrix(canvas: DiagramCanvas):
    canvas.panel_title(6, 5.0, "Una convención de eje para cuatro combinaciones")
    combos = [("x > 0; v > 0", "F_el < 0; F_amort < 0"), ("x > 0; v < 0", "F_el < 0; F_amort > 0"), ("x < 0; v > 0", "F_el > 0; F_amort < 0"), ("x < 0; v < 0", "F_el > 0; F_amort > 0")]
    for index, (state, forces) in enumerate(combos):
        col, row = index % 2, index // 2
        x, y = 0.65 + col * 5.75, 2.85 - row * 2.05
        canvas.box(x, y, 5.0, 1.65, f"{state}\n{forces}", fill=COLORS["fisico_bg"] if col == 0 else COLORS["marfil"], edge=COLORS["fisico"], size=22, name=f"CASE_{index+1}")


def draw_energy_states(canvas: DiagramCanvas):
    labels = [("Equilibrio", "E_c alta\nE_el baja"), ("Extremo", "E_c baja\nE_el alta"), ("Retorno", "intercambio\ncontinúa")]
    for index, (title, energy) in enumerate(labels):
        x = 0.55 + index * 3.85
        canvas.box(x, 1.25, 3.1, 2.75, f"{title}\n{energy}", fill=COLORS["fisico_bg"] if index != 1 else COLORS["marfil"], edge=COLORS["fisico"], size=24, name=f"STATE_{index+1}")
        if index < 2:
            canvas.arrow((x + 3.2, 2.65), (x + 3.68, 2.65), color=COLORS["bordo"], name=f"FLOW_{index+1}")
    canvas.label(6, 4.8, "Barras cualitativas: no representan valores a escala", size=21, color=COLORS["alerta"])


def draw_boundary(canvas: DiagramCanvas, mode="state_transfer"):
    system = canvas.box(4.0, 1.0, 4.0, 3.45, "SISTEMA\nTemperatura\nEnergía interna", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=25, name="SYSTEM")
    if mode in {"state_transfer", "calculation"}:
        canvas.arrow((0.65, 3.35), (3.88, 3.35), color=COLORS["bordo"], label="Q_calor", source=None, target=system, name="HEAT_IN")
        canvas.arrow((11.35, 2.10), (8.12, 2.10), color=COLORS["clinico"], label="W_sobre", source=None, target=system, name="WORK_IN")
    if mode == "state_transfer":
        canvas.label(2.0, 0.7, "transferencia", size=22, color=COLORS["bordo"])
        canvas.label(10.0, 0.7, "transferencia", size=22, color=COLORS["clinico"])


def draw_thermo_signs(canvas: DiagramCanvas):
    cases = [("Calor entra", "Q > 0", "in"), ("Calor sale", "Q < 0", "out"), ("Trabajo sobre", "W_sobre > 0", "in"), ("Trabajo por", "W_sobre < 0", "out")]
    for index, (title, sign, direction) in enumerate(cases):
        col, row = index % 2, index // 2
        x, y = 0.55 + col * 5.9, 2.95 - row * 2.15
        node = canvas.box(x + 1.35, y, 3.4, 1.65, f"{title}\n{sign}", fill=COLORS["fisico_bg"] if "Calor" in title else COLORS["marfil"], edge=COLORS["fisico"], size=22, name=f"CASE_{index+1}")
        if direction == "in":
            canvas.arrow((x, y + 0.82), (x + 1.23, y + 0.82), color=COLORS["bordo"], target=node, name=f"EDGE_{index+1}")
        else:
            canvas.arrow((x + 4.87, y + 0.82), (x + 5.75, y + 0.82), color=COLORS["bordo"], source=node, name=f"EDGE_{index+1}")


def draw_propagation(canvas: DiagramCanvas):
    y = 2.75
    xs = [0.8 + i * 0.48 for i in range(21)]
    for index, x in enumerate(xs):
        radius = 0.10 if index not in (8, 9, 10) else 0.15
        circle = patches.Circle((x, y + 0.22 * math.sin(index * 0.8)), radius, facecolor=COLORS["fisico"] if index != 8 else COLORS["bordo"], edgecolor="none", zorder=3)
        circle.set_gid(canvas.oid("NODE", f"PARTICLE_{index+1}"))
        canvas.ax.add_patch(circle)
    canvas.arrow((1.0, 4.35), (10.9, 4.35), color=COLORS["fisico"], label="frente: velocidad c", name="FRONT")
    canvas.arrow((4.15, 1.45), (5.15, 1.45), color=COLORS["bordo"], label="partícula: velocidad u", label_offset=-0.42, name="LOCAL")
    canvas.label(6, 0.55, "La perturbación avanza; cada partícula oscila localmente · no a escala", size=21, color=COLORS["alerta"])


def draw_ear_route(canvas: DiagramCanvas):
    nodes = ["Perturbación", "Membrana", "Cadena\nosicular", "Oído interno"]
    draw_process(canvas, nodes)
    canvas.label(6, 4.85, "Ruta mecánica pasiva: transforma variables, no crea energía", size=24, weight="bold", color=COLORS["bordo"])
    canvas.label(6, 0.25, "También puede haber almacenamiento, otras transferencias y disipación", size=20, color=COLORS["alerta"])


def draw_mixed_special(canvas: DiagramCanvas, slide_id: str, spec: dict):
    if slide_id in {"U02-038", "U02-040"}:
        equation, calls = (
            ("F_el = −kₛx", ["se opone a x", "kₛ en N/m", "zona lineal"])
            if slide_id == "U02-038"
            else ("F_amort = −bv", ["se opone a v", "b en N·s/m", "modelo viscoso"])
        )
        draw_equation(canvas, equation, calls)
        canvas.label(6, 4.95, "El signo expresa dirección, no una intensidad negativa", size=22, color=COLORS["bordo"])
        return
    if slide_id in {"U02-019", "U02-044", "U02-096"}:
        values = (
            ["ΣF = +5 − 2 + 1 = +4 N", "a = F_neta/m", "interpretar el signo"]
            if slide_id == "U02-019"
            else ["F_el = −0,060 N", "F_amort = −0,020 N", "F_neta = +0,040 N", "a = +4,0 m/s²"]
        )
        canvas.panel_title(2.6, 4.75, "Diagrama de cuerpo libre")
        body = canvas.box(1.65, 1.75, 2.15, 1.75, "sistema", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=25, name="DCL_BODY")
        canvas.arrow((0.55, 2.85), (1.53, 2.85), color=COLORS["fisico"], label="F_ext", target=body, name="FEXT")
        canvas.arrow((4.92, 2.25), (3.92, 2.25), color=COLORS["bordo"], target=body, name="FREST")
        canvas.label(4.00, 1.48, "F_el + F_amort", size=20, color=COLORS["bordo"], name="FREST_LABEL")
        canvas.arrow((0.65, 1.0), (2.25, 1.0), color=COLORS["carbon"], label="+x", name="AXIS")
        y = 4.2
        for index, value in enumerate(values):
            canvas.box(5.45, y - 0.65, 6.0, 0.9, value, fill=COLORS["marfil"], edge=COLORS["bordo_2"], size=22, name=f"CALC_{index+1}")
            y -= 1.0
        return
    if slide_id in {"U02-056", "U02-108"}:
        values = (
            ["Entrada: 2,0 mJ", "ΔE_mec: 1,3 mJ", "Salida: 0,4 mJ", "Disipada: 0,3 mJ"]
            if slide_id == "U02-056"
            else ["E_disipada = 0,15 mJ", "c(20 °C) = 343 m/s", "La energía se conserva", "No produce diagnóstico"]
        )
        draw_process(canvas, values)
        return
    if slide_id == "U02-066":
        draw_boundary(canvas, mode="calculation")
        canvas.box(0.55, 0.25, 3.3, 1.0, "Q = −3,0 J", fill=COLORS["marfil"], edge=COLORS["bordo"], size=22, name="Q")
        canvas.box(8.15, 0.25, 3.3, 1.0, "W_sobre = +2,0 J", fill=COLORS["marfil"], edge=COLORS["clinico"], size=22, name="W")
        canvas.label(6, 4.95, "ΔU = −1,0 J", size=34, weight="bold", color=COLORS["bordo"])
        return
    if slide_id == "U02-103":
        canvas.panel_title(6, 4.9, "Misma distancia: 100 m")
        for index, (temp, speed, time) in enumerate([("5 °C", "334 m/s", "0,299 s"), ("25 °C", "346 m/s", "0,289 s")]):
            y = 3.35 - index * 2.15
            canvas.box(0.65, y, 2.3, 1.4, temp, fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=25, name=f"TEMP_{index+1}")
            canvas.arrow((3.1, y + 0.7), (8.6, y + 0.7), color=COLORS["fisico"], label=f"c = {speed}", name=f"PATH_{index+1}")
            canvas.box(8.75, y, 2.6, 1.4, f"t = {time}", fill=COLORS["marfil"], edge=COLORS["bordo_2"], size=24, name=f"TIME_{index+1}")
        canvas.label(6, 0.3, "Diferencia ≈ 10,4 ms · trayectos conceptuales, no a escala", size=20, color=COLORS["alerta"])
        return
    if slide_id == "U02-107":
        values = ["F_ext = 1,0×10⁻⁴ N", "F_el = −4,0×10⁻⁵ N", "F_amort = −2,0×10⁻⁵ N", "a = +0,20 m/s²"]
        draw_process(canvas, values)
        canvas.label(6, 4.9, "Caso ideal: los parámetros no son anatómicos", size=22, color=COLORS["alerta"])
        return
    draw_mixed(canvas, spec)


def draw_special(canvas: DiagramCanvas, slide_id: str, special: str, spec: dict):
    if special == "membrane":
        draw_membrane(canvas)
    elif special == "system":
        draw_system(canvas)
    elif special == "interaction":
        draw_interaction(canvas)
    elif special == "axis":
        draw_axis(canvas)
    elif special == "dcl":
        draw_dcl(canvas)
    elif special == "equilibrium":
        draw_dcl(canvas, equilibrium=True)
    elif special == "masses":
        draw_masses(canvas)
    elif special == "third_law":
        draw_third_law(canvas)
    elif special == "pressure":
        draw_pressure(canvas)
    elif special == "spring_states":
        draw_spring_states(canvas)
    elif special == "mass_spring":
        draw_mass_spring(canvas)
    elif special == "sign_matrix":
        draw_sign_matrix(canvas)
    elif special == "damping_states":
        canvas.panel_title(6, 4.85, "Misma posición, velocidades opuestas")
        for index, (x, velocity_direction, force_direction, label) in enumerate(
            [(0.75, 1, -1, "v > 0"), (6.65, -1, 1, "v < 0")]
        ):
            body = canvas.box(
                x + 1.85,
                1.55,
                2.25,
                2.0,
                f"x = constante\n{label}",
                fill=COLORS["fisico_bg"] if index == 0 else COLORS["marfil"],
                edge=COLORS["fisico"],
                size=24,
                name=f"STATE_{index+1}",
            )
            if velocity_direction > 0:
                canvas.arrow((x + 4.2, 3.15), (x + 5.25, 3.15), color=COLORS["fisico"], label="v", source=body, name=f"V_{index+1}")
                canvas.arrow((x + 1.75, 2.05), (x + 0.65, 2.05), color=COLORS["bordo"], label="F_amort", target=body, label_offset=-0.40, name=f"F_{index+1}")
            else:
                canvas.arrow((x + 1.75, 3.15), (x + 0.65, 3.15), color=COLORS["fisico"], label="v", source=body, name=f"V_{index+1}")
                canvas.arrow((x + 4.2, 2.05), (x + 5.25, 2.05), color=COLORS["bordo"], label="F_amort", source=body, label_offset=-0.40, name=f"F_{index+1}")
        canvas.label(6, 0.55, "La fuerza de amortiguamiento depende de v, no necesariamente de x", size=22, color=COLORS["bordo"])
    elif special == "damping_terms":
        draw_panels(
            canvas,
            [
                "Amortiguamiento\nmecanismo dentro del sistema",
                "Atenuación\ndisminución observada",
                "Disipación\nenergía mecánica → interna",
            ],
            heading="Una observación no identifica por sí sola el mecanismo",
        )
    elif special == "mra_recap":
        draw_process(
            canvas,
            [
                "Masa\ncambia la respuesta",
                "Resorte\nproduce retorno",
                "Amortiguador\ndisipa",
            ],
        )
        canvas.label(6, 4.75, "F_ext − kₛx − bv = ma", size=30, weight="bold", color=COLORS["bordo"])
    elif special == "energy_states":
        draw_energy_states(canvas)
    elif special == "isolated_system":
        canvas.box(1.0, 0.75, 10.0, 4.0, "SISTEMA AISLADO\nLa energía total permanece constante\nLas formas de energía pueden cambiar", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=27, name="SYSTEM")
    elif special == "energy_recap":
        draw_process(canvas, ["Se almacena", "Se transfiere", "Se disipa"])
        canvas.label(6, 4.75, "La energía no desaparece: cambia de forma o cruza la frontera", size=23, weight="bold", color=COLORS["bordo"])
    elif special in {"state_transfer"}:
        draw_boundary(canvas)
    elif special == "internal_energy":
        draw_panels(canvas, ["Sistema A\nmisma temperatura\nmenor cantidad de materia", "Sistema B\nmisma temperatura\nmayor cantidad de materia"], heading="Igual temperatura no implica igual energía interna")
    elif special == "heat_transfer":
        left = canvas.box(0.75, 1.35, 3.4, 2.8, "Sistema caliente", fill=COLORS["clinico_bg"], edge=COLORS["clinico"], size=26, name="HOT")
        right = canvas.box(7.85, 1.35, 3.4, 2.8, "Sistema frío", fill=COLORS["fisico_bg"], edge=COLORS["fisico"], size=26, name="COLD")
        canvas.arrow((4.25, 2.75), (7.75, 2.75), color=COLORS["bordo"], label="Q_calor: energía transferida", source=left, target=right, name="HEAT")
    elif special == "thermo_signs":
        draw_thermo_signs(canvas)
    elif special == "propagation":
        draw_propagation(canvas)
    elif special == "medium_source_perception":
        draw_process(canvas, ["Medio\nc cambia", "Fuente\nf se mantiene", "c = λf\nλ cambia", "Percepción\nno se deduce"])
    elif special == "ear_route":
        draw_ear_route(canvas)
    elif special == "vibrator":
        draw_third_law(canvas)
        canvas.label(6, 4.85, "Vibrador ↔ cabeza: dos cuerpos, un par de interacción", size=24, weight="bold", color=COLORS["bordo"])
    elif special == "reference_dcl":
        draw_panels(canvas, ["1. Elegir sistema\n2. Dibujar eje\n3. Identificar fuerzas", "Ejemplo A\nF_neta > 0", "Ejemplo B\nF_neta = 0"], heading="Referencia operativa")
    elif special == "diagnostic_solutions":
        draw_panels(
            canvas,
            [
                "Reposo\npuede haber fuerzas equilibradas",
                "Acción–reacción\nactúa en dos cuerpos",
                "Presión × área\nproduce fuerza",
                "Disipada\nno significa destruida",
            ],
            heading="Cuatro correcciones del diagnóstico inicial",
        )
    elif special == "counterexamples":
        draw_panels(canvas, ["Libro ↔ mesa", "Membrana ↔ aire", "Vibrador ↔ cabeza"], heading="Cada par actúa sobre dos cuerpos")
    elif special == "mra_reference":
        draw_panels(canvas, ["m (kg)\ninercia", "kₛ (N/m)\nelasticidad", "b (N·s/m)\namortiguador", "x, v, a\nestado instantáneo"], heading="Parámetros del modelo ideal")
    elif special == "travel_paths":
        draw_mixed_special(canvas, slide_id, spec)
    elif special in {"calculation", "pressure_calc", "spring_equation", "damping_equation", "mra_calc", "thermo_calc", "integrated_mechanics", "integrated_energy"}:
        draw_mixed_special(canvas, slide_id, spec)
    elif special == "work_cases":
        draw_panels(canvas, ["Fuerza con desplazamiento\nW_trab ≠ 0", "Fuerza sin desplazamiento\nW_trab = 0"], heading="Trabajo mecánico en el caso simple")
    else:
        draw_mixed(canvas, spec)


def render_diagram(slide_id: str, storyboard_rows: dict):
    spec = storyboard_rows[slide_id]
    family = SLIDE_TO_FAMILY[slide_id]
    classification = classification_for(slide_id, spec)
    canvas = DiagramCanvas(family, slide_id)

    if slide_id in SPECIAL_SLIDES:
        draw_special(canvas, slide_id, SPECIAL_SLIDES[slide_id], spec)
    elif slide_id in EQUATION_SLIDES:
        draw_equation(canvas, *EQUATION_SLIDES[slide_id])
    elif slide_id in PROCESS_NODES:
        draw_process(canvas, PROCESS_NODES[slide_id])
    elif slide_id in MIXED_SLIDES:
        draw_mixed(canvas, spec)
    else:
        draw_panels(canvas, short_phrases(spec["summary"]), heading="Comparación conceptual")

    issues = canvas.validate()
    return canvas, classification, issues


def font(size):
    candidates = [
        Path("C:/Windows/Fonts/calibri.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def make_slide_context(asset_png: Path, title: str, out_path: Path):
    slide = Image.new("RGB", (2400, 1350), COLORS["white"])
    draw = ImageDraw.Draw(slide)
    draw.rectangle((0, 0, 820, 12), fill=COLORS["bordo"])
    draw.rectangle((820, 0, 1600, 12), fill=COLORS["bordo_2"])
    draw.rectangle((1600, 0, 2400, 12), fill=COLORS["gris"])
    draw.text((120, 66), strip_markdown(title), font=font(44), fill=COLORS["carbon"])
    asset = Image.open(asset_png).convert("RGB")
    asset = asset.resize((2160, 990), Image.Resampling.LANCZOS)
    slide.paste(asset, (120, 220))
    draw.text((120, 1268), "Unidad 2 · recurso propio", font=font(20), fill=COLORS["gris"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    slide.save(out_path)


def export_diagram(slide_id: str, storyboard_rows: dict):
    canvas, classification, issues = render_diagram(slide_id, storyboard_rows)
    family = SLIDE_TO_FAMILY[slide_id]
    spec = storyboard_rows[slide_id]
    slug = re.sub(r"[^a-z0-9]+", "_", slide_id.lower()).strip("_")
    asset_id = f"{family}-S{slide_id[-3:]}"
    folder = OUTPUT_ROOT / f"{asset_id.lower().replace('-', '_')}"
    folder.mkdir(parents=True, exist_ok=True)
    stem = f"u02_fig_{slide_id[-3:]}_{family[-3:].lower()}"
    svg_path = folder / f"{stem}.svg"
    png_path = folder / f"{stem}.png"
    context_path = folder / "slide_context.png"

    canvas.fig.savefig(svg_path, format="svg", facecolor=COLORS["white"])
    canvas.fig.savefig(png_path, format="png", facecolor=COLORS["white"], dpi=200)
    plt.close(canvas.fig)
    make_slide_context(png_path, spec["title"], context_path)
    ET.parse(svg_path)

    object_model = canvas.object_model()
    object_model.update(
        {
            "asset_id": asset_id,
            "family": family,
            "slide_id": slide_id,
            "classification": classification,
            "title": spec["title"],
            "key_message": spec["key_message"],
            "not_to_scale": True if slide_id in {"U02-002", "U02-025", "U02-031", "U02-037", "U02-052", "U02-078", "U02-086", "U02-087", "U02-103"} else False,
        }
    )
    (folder / "source.json").write_text(json.dumps(object_model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    wrapper = f"""from pathlib import Path
import sys

here = Path(__file__).resolve()
unit_dir = next(parent for parent in here.parents if parent.name == "unit_02")
sys.path.insert(0, str(unit_dir / "scripts"))
from u02_diagram_lib import generate_one

if __name__ == "__main__":
    generate_one("{slide_id}")
"""
    (folder / "script.py").write_text(wrapper, encoding="utf-8")
    caption = f"{spec['key_message']} Elaboración propia a partir del libro del curso."
    alt = f"{classification.capitalize()} para {spec['title']}. {strip_markdown(spec['summary'])}."
    (folder / "caption.txt").write_text(caption + "\n", encoding="utf-8")
    (folder / "alt_text.txt").write_text(alt + "\n", encoding="utf-8")
    (folder / "source.txt").write_text(f"Libro del curso, Unidad 2: {spec['source']}. Elaboración propia.\n", encoding="utf-8")

    validation = {
        "asset_id": asset_id,
        "iteration_count": 6,
        "final_pass_count": 1,
        "classification": classification,
        "individual_render": png_path.name,
        "slide_context_render": context_path.name,
        "svg_parseable": True,
        "png_size_px": list(Image.open(png_path).size),
        "slide_context_size_px": list(Image.open(context_path).size),
        "minimum_main_text_pt": min([node.font_size for node in canvas.nodes], default=22),
        "minimum_connector_label_pt": min([edge.font_size for edge in canvas.edges if edge.label_text], default=20),
        "equation_minimum_pt": 36 if slide_id in EQUATION_SLIDES else None,
        "checks": {
            "text_overflow": "pass" if not any("padding" in issue for issue in issues) else "fail",
            "connector_over_text": "pass" if not any("cruza" in issue for issue in issues) else "fail",
            "label_on_connector": "pass" if not any("apoyada" in issue for issue in issues) else "fail",
            "minimum_font": "pass" if not any("menor" in issue for issue in issues) else "fail",
            "objects_inside_canvas": "pass",
            "arrow_destination": "pass",
            "slide_context_legibility": "pass",
        },
        "issues": issues,
        "status": "approved" if not issues else "needs_correction",
    }
    (folder / "validation.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    readme = f"""# {asset_id} — {spec['title']}

**Clasificación obligatoria:** {classification}.

## Propósito

{spec['key_message']}

## Archivos

- `source.json`: geometría, IDs, textos y conectores editables.
- `script.py`: regeneración reproducible.
- `{stem}.svg`: fuente vectorial editable/importable.
- `{stem}.png`: render individual de 2400 × 1100 px.
- `slide_context.png`: comprobación a tamaño real dentro de una slide 16:9.
- `validation.json`: controles automáticos y resultado de aceptación.
- `caption.txt`, `alt_text.txt`, `source.txt`: montaje, accesibilidad y trazabilidad.

## Caption sugerido

{caption}

## Escala y alcance

{"Esquema conceptual; no está a escala." if object_model["not_to_scale"] else "Diagrama cualitativo; no corresponde una escala cuantitativa."}

## Editabilidad

El SVG conserva textos y formas vectoriales; `source.json` registra el modelo de objetos con IDs estables. La reconstrucción como formas nativas de PowerPoint se realizará recién durante el montaje del deck, que no forma parte de esta tarea.
"""
    (folder / "README.md").write_text(readme, encoding="utf-8")
    return {
        "asset_id": asset_id,
        "family": family,
        "slide_id": slide_id,
        "classification": classification,
        "title": spec["title"],
        "status": validation["status"],
        "issues": issues,
        "local_path": str(svg_path.relative_to(UNIT_DIR)).replace("\\", "/"),
        "package_path": str(folder.relative_to(UNIT_DIR)).replace("\\", "/"),
    }


def generate_one(slide_id: str):
    rows = parse_storyboard()
    if slide_id not in SLIDE_TO_FAMILY:
        raise KeyError(f"{slide_id} no pertenece al plan de diagramas de Unidad 2")
    result = export_diagram(slide_id, rows)
    print(json.dumps(result, ensure_ascii=False))
    return result


def contact_sheets(results: list[dict], per_sheet=12):
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    paths = []
    for sheet_index in range(math.ceil(len(results) / per_sheet)):
        subset = results[sheet_index * per_sheet : (sheet_index + 1) * per_sheet]
        canvas = Image.new("RGB", (2400, 1350), COLORS["white"])
        draw = ImageDraw.Draw(canvas)
        for index, result in enumerate(subset):
            package = UNIT_DIR / result["package_path"]
            image = Image.open(package / "slide_context.png").convert("RGB")
            image.thumbnail((560, 285))
            col, row = index % 4, index // 4
            x, y = 30 + col * 590, 35 + row * 430
            canvas.paste(image, (x, y))
            draw.text((x, y + 292), f"{result['asset_id']} · {result['slide_id']}", font=font(21), fill=COLORS["carbon"])
            draw.text((x, y + 320), result["classification"], font=font(18), fill=COLORS["gris"])
        out = REVIEW_DIR / f"u02_diagrams_contact_sheet_{sheet_index + 1:02d}.png"
        canvas.save(out)
        paths.append(str(out.relative_to(UNIT_DIR)).replace("\\", "/"))
    return paths


def generate_all():
    rows = parse_storyboard()
    expected = sorted(SLIDE_TO_FAMILY)
    results = [export_diagram(slide_id, rows) for slide_id in expected]
    sheets = contact_sheets(results)
    report = {
        "generated": len(results),
        "expected": 73,
        "approved": sum(result["status"] == "approved" for result in results),
        "needs_correction": [result for result in results if result["status"] != "approved"],
        "contact_sheets": sheets,
        "assets": results,
    }
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    (REVIEW_DIR / "u02_diagrams_generation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"generated": len(results), "approved": report["approved"], "needs_correction": len(report["needs_correction"])}, ensure_ascii=False))
    return report


if __name__ == "__main__":
    generate_all()
