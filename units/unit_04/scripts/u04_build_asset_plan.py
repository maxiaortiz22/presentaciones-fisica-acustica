from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORYBOARD = ROOT / "storyboard.md"
OUTPUT = ROOT / "asset_plan.md"


def ids(start, end):
    return {f"U04-{n:03d}" for n in range(start, end + 1)}


diagram_families = {
    "U04-DG-001": ids(2, 2),
    "U04-DG-002": {"U04-006", "U04-014", "U04-107"},
    "U04-DG-003": ids(8, 10),
    "U04-DG-004": ids(12, 13),
    "U04-DG-005": ids(16, 19),
    "U04-DG-006": ids(20, 22),
    "U04-DG-007": ids(24, 28),
    "U04-DG-008": ids(29, 33) | {"U04-113"},
    "U04-DG-009": {"U04-035", "U04-037", "U04-038"},
    "U04-DG-010": ids(40, 42),
    "U04-DG-011": ids(45, 50),
    "U04-DG-012": ids(52, 55) | ids(111, 112),
    "U04-DG-013": ids(60, 68) | {"U04-114"},
    "U04-DG-014": ids(70, 80) | {"U04-115"},
    "U04-DG-015": ids(82, 89) | ids(116, 117),
    "U04-DG-016": ids(91, 97) | {"U04-118"},
    "U04-DG-017": ids(98, 102),
    "U04-DG-018": ids(104, 107) | {"U04-124"},
    "U04-DG-019": {"U04-106"},
    "U04-DG-020": {"U04-123"},
    "U04-DG-021": {"U04-004", "U04-011", "U04-058"},
    "U04-DG-022": {"U04-039", "U04-110", "U04-120"},
}

chart_families = {
    "U04-CH-001": ids(25, 26),
    "U04-CH-002": {"U04-036"},
    "U04-CH-003": ids(44, 50),
    "U04-CH-004": {"U04-048"},
    "U04-CH-005": ids(53, 56),
    "U04-CH-006": {"U04-057", "U04-109"},
    "U04-CH-007": {"U04-064"},
    "U04-CH-008": {"U04-070", "U04-072", "U04-073", "U04-074", "U04-075", "U04-122"},
    "U04-CH-009": ids(76, 80),
    "U04-CH-010": {"U04-084", "U04-086", "U04-117"},
    "U04-CH-011": ids(95, 97),
    "U04-CH-012": {"U04-102"},
    "U04-CH-013": {"U04-113"},
    "U04-CH-014": {"U04-121"},
    "U04-CH-015": {"U04-122"},
}

external = {
    "U04-012": "U04-EXT-001 (referencia/crop opcional)",
    "U04-013": "U04-MED-001",
    "U04-042": "U04-EXT-003 (opcional)",
    "U04-088": "U04-EXT-004",
    "U04-102": "U04-DATA-001",
    "U04-104": "U04-EXT-003",
}

overrides = {
    "U04-011": ("diagram", "ilustración técnica propia comparativa; evitar mosaico fotográfico heterogéneo"),
    "U04-012": ("mixed", "diagrama funcional editable con referencia anatómica externa opcional"),
    "U04-013": ("video_or_gif", "GIF corto solo si no confunde propagación con arcos transversales; estática propia obligatoria"),
    "U04-042": ("mixed", "cadena editable más captura real opcional de instrumento"),
    "U04-088": ("mixed", "diagramas de campo más fotografía técnica de cámara anecoica"),
    "U04-102": ("mixed", "gráfico propio derivado de datos CC BY 4.0; no captura de fabricante"),
    "U04-104": ("mixed", "cadena editable con fotografía recortada del sonómetro"),
}

support = {
    "chart": "gráfico propio",
    "diagram": "diagrama editable",
    "mixed": "combinación de gráfico/diagrama/tabla",
    "external_image": "imagen externa técnica",
    "video_or_gif": "animación, GIF o video",
    "equation_only": "ecuación anotada editable",
    "none": "ninguna imagen; tipografía, tabla o consigna",
}


def refs(slide_id):
    result = []
    for family, members in diagram_families.items():
        if slide_id in members:
            result.append(family)
    for family, members in chart_families.items():
        if slide_id in members:
            result.append(family)
    if slide_id in external:
        result.append(external[slide_id])
    return "; ".join(result) or "—"


rows = []
for line in STORYBOARD.read_text(encoding="utf-8").splitlines():
    if line.startswith("| U04-"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)

header = """# Unidad 4 — Plan maestro de assets visuales

## Criterio de selección

La clasificación de esta matriz es la decisión final de planificación visual. `chart` se reserva para ejes/datos; `diagram`, para relaciones espaciales o conceptuales; `equation_only`, para fórmulas anotadas; `mixed`, para una combinación inseparable; `external_image`, para evidencia fotográfica o técnica; y `video_or_gif`, para un cambio temporal observable. `none` no es una clase de asset: indica que la slide funciona mejor sin imagen.

Se reduce deliberadamente el uso externo. La slide U04-011 cambia de un mosaico fotográfico a una ilustración técnica propia, porque cinco fotografías con estilos y escalas distintos dificultarían comparar mecanismos. U04-102 cambia de captura de fabricante a gráfico propio derivado de datos académicos abiertos.

## Recursos descargados en esta etapa

| asset_id | uso propuesto | licencia | decisión |
|---|---|---|---|
| U04-EXT-001 | Referencia anatómica opcional para U04-012 | Dominio público, NIDCD/NIH | descargado; usar solo recorte pertinente o como referencia |
| U04-MED-000 | Animación de altavoz réflex | CC0 | descargado y rechazado: representa un sistema de bocina plegada, no el cono de la slide |
| U04-EXT-003 | Sonómetro real para U04-042/U04-104 | dominio público | descargado; aprobado como captura de instrumento |
| U04-EXT-004 | Cámara anecoica para U04-088 | información pública NIST; crédito solicitado | descargado; aprobado con crédito |
| U04-MED-001 | Animación de altavoz y onda | CC0 | descargado; preseleccionado con revisión conceptual pendiente |

## Matriz por slide

| slide_id | bloque | clasificación final | apoyo recomendado | plan/asset | decisión de implementación |
|---|---|---|---|---|---|
"""

out = [header]
for cells in rows:
    slide_id, block, _, title = cells[:4]
    original_class = cells[8]
    final_class, note = overrides.get(slide_id, (original_class, "seguir la familia indicada; sin asset externo"))
    if final_class == "none":
        note = "mantener sin imagen; usar únicamente jerarquía tipográfica, consigna o tabla editable"
    out.append(
        f"| {slide_id} | {block} | {final_class} | {support[final_class]} | {refs(slide_id)} | {note}. |"
    )

out.append("""

## Decisiones globales

- No se propone generación de imágenes por IA: todos los fenómenos pueden resolverse mejor con gráficos, formas editables o fuentes técnicas abiertas.
- Fotografías reales quedan limitadas a instrumento y entorno de medición; no se usarán como fondo ni decoración.
- Toda tabla será nativa de PowerPoint, no una captura.
- Las ecuaciones anotadas serán editables; SVG se reserva como respaldo cuando la ecuación nativa no sea viable.
- Cada GIF/video tendrá frame estático y la clase podrá dictarse sin conexión.
- Los detalles de producción están en `chart_plan.md`, `diagram_plan.md` y `media_plan.md`.
""")

OUTPUT.write_text("\n".join(out), encoding="utf-8")
