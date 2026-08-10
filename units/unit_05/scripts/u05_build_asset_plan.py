from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STORYBOARD = ROOT / "storyboard.md"
OUTPUT = ROOT / "asset_plan.md"


def ids(start: int, end: int) -> set[str]:
    return {f"U05-{n:03d}" for n in range(start, end + 1)}


diagram_families = {
    "U05-DG-001": {"U05-001", "U05-006", "U05-129"},
    "U05-DG-002": {"U05-003", "U05-004", "U05-007"},
    "U05-DG-003": {"U05-010", "U05-015", "U05-018"} | ids(22, 29) | ids(133, 135),
    "U05-DG-004": {"U05-030", "U05-031"} | ids(33, 40) | ids(133, 136),
    "U05-DG-005": {"U05-041", "U05-042", "U05-047"} | ids(49, 51) | ids(137, 140),
    "U05-DG-006": ids(52, 62),
    "U05-DG-007": ids(63, 73) | {"U05-141"},
    "U05-DG-008": {"U05-077"} | ids(79, 83),
    "U05-DG-009": ids(86, 94) | {"U05-142", "U05-143"},
    "U05-DG-010": ids(95, 105) | {"U05-144"},
    "U05-DG-011": ids(106, 116) | {"U05-145"},
    "U05-DG-012": ids(117, 124) | ids(146, 148),
    "U05-DG-013": ids(125, 131),
    "U05-DG-014": {
        "U05-017", "U05-029", "U05-040", "U05-051", "U05-062",
        "U05-083", "U05-094", "U05-105", "U05-116", "U05-124",
    },
    "U05-DG-015": {"U05-149", "U05-150"},
}


chart_families = {
    "U05-CH-001": {"U05-002"},
    "U05-CH-002": ids(9, 12),
    "U05-CH-003": ids(13, 14),
    "U05-CH-004": {"U05-016"},
    "U05-CH-005": {"U05-019", "U05-020", "U05-021", "U05-025"},
    "U05-CH-006": {"U05-032", "U05-136"},
    "U05-CH-007": ids(35, 39),
    "U05-CH-008": ids(41, 44),
    "U05-CH-009": {"U05-045", "U05-138"},
    "U05-CH-010": ids(46, 48),
    "U05-CH-011": {"U05-063"} | ids(66, 69),
    "U05-CH-012": ids(71, 73) | {"U05-141"},
    "U05-CH-013": ids(74, 79),
    "U05-CH-014": ids(84, 94) | {"U05-142"},
    "U05-CH-015": {"U05-085", "U05-091", "U05-092"},
    "U05-CH-016": ids(95, 103) | {"U05-144"},
    "U05-CH-017": ids(108, 116) | {"U05-145"},
    "U05-CH-018": {"U05-121", "U05-147"},
    "U05-CH-019": {"U05-123"},
}


external = {
    "U05-078": "U05-EXT-001",
    "U05-081": "U05-EXT-002",
    "U05-118": "U05-EXT-003",
}


media = {
    "U05-020": "U05-MED-001; U05-MED-002",
    "U05-048": "U05-MED-003; U05-MED-004",
    "U05-102": "U05-MED-005",
}


support = {
    "chart": "gráfico propio con ejes",
    "diagram": "diagrama editable",
    "mixed": "gráfico/diagrama/tabla combinados",
    "external_image": "fotografía real o captura técnica",
    "video_or_gif": "animación o audio propio con respaldo estático",
    "equation_only": "ecuación anotada editable",
    "none": "ninguna imagen; tipografía, tabla o consigna",
}


def references(slide_id: str) -> str:
    result: list[str] = []
    for family, members in diagram_families.items():
        if slide_id in members:
            result.append(family)
    for family, members in chart_families.items():
        if slide_id in members:
            result.append(family)
    if slide_id in external:
        result.append(external[slide_id])
    if slide_id in media:
        result.append(media[slide_id])
    return "; ".join(result) or "—"


def implementation(slide_id: str, visual_class: str) -> str:
    if visual_class == "none":
        return "Mantener sin imagen; usar jerarquía tipográfica, tabla nativa o consigna."
    if visual_class == "chart":
        return "Generar con script y datos/modelo declarados; SVG principal y PNG de respaldo."
    if visual_class == "diagram":
        return "Construir con formas y conectores editables; exportar SVG/PNG solo como respaldo."
    if visual_class == "equation_only":
        return "Usar ecuación nativa o SVG editable con callouts externos y control dimensional."
    if visual_class == "mixed":
        return "Combinar solo elementos inseparables; tabla nativa y capas editables."
    if visual_class == "external_image":
        return "Usar evidencia real con crédito, recorte no destructivo y alternativa propia."
    if visual_class == "video_or_gif":
        return "Reproducir manualmente; sin streaming; conservar audio/animación y frame estático."
    raise ValueError(f"Clase no reconocida: {visual_class}")


rows = []
for line in STORYBOARD.read_text(encoding="utf-8").splitlines():
    if line.startswith("| U05-"):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)


header = """# Unidad 5 — Plan maestro de recursos visuales

## Criterio de clasificación

La matriz conserva las clases obligatorias del storyboard: `chart`, `diagram`, `mixed`, `external_image`, `video_or_gif` y `equation_only`. `none` se registra únicamente para las slides que deliberadamente no requieren asset: no es una clase de recurso, sino una decisión de no añadir imagen.

- `chart`: ejes, curvas, espectros, señales o datos; se deriva a `chart-generation`.
- `diagram`: relaciones, procesos, cajas, flechas o esquemas; se deriva a `diagram-generation`.
- `mixed`: combinación inseparable de chart, diagrama, tabla o evidencia real.
- `external_image`: fotografía real, ilustración técnica o captura de instrumento; se deriva a `asset-curation`.
- `video_or_gif`: cambio temporal o audio sincronizado; se deriva a `asset-curation` y, si es propio, al script generador correspondiente.
- `equation_only`: ecuación anotada y editable; se deriva a `diagram-generation`.

No se propone imagen anatómica ni generación por IA para U5. La anatomía pertenece a U6 y los fenómenos de esta unidad pueden mostrarse con datos, señales, diagramas o registros reales.

## Recursos externos aprobados o descargados

| asset_id | slides | recurso | licencia | decisión |
|---|---|---|---|---|
| U05-EXT-001 | U05-078 | Fotografía real de examen ecográfico, Joseph Caballero/U.S. Navy | Dominio público, PDM 1.0 | descargada; usar como aplicación contextual, no para explicar anatomía |
| U05-EXT-003 | U05-118 | Sonómetro Brüel & Kjær Type 2232, Harke/Wikimedia Commons | Dominio público, PD-self | reutilizado desde U4; aprobado como captura de instrumento |

U05-EXT-002 será una fotografía propia de un montaje de medición vocal o instrumental. No se seleccionó una fotografía externa genérica porque el sensor y las condiciones deben corresponder al caso explicado.

## Evaluación de imágenes reales

| asset_id | relevancia y exactitud | legibilidad/recorte | licencia y resolución | decisión y alternativa |
|---|---|---|---|---|
| U05-EXT-001 | Alta para mostrar una aplicación real; no explica el principio físico por sí sola | Recortar sin sobrescribir el original hacia transductor, cable y consola; minimizar rostro y exposición corporal para evitar distracción | Dominio público; 2100×1396 | Aprobada con recorte sensible; alternativa CH-013 + DG-008 |
| U05-EXT-002 | Alta si el montaje coincide con los datos del caso; exactitud pendiente de producción | Encuadre horizontal 16:9 con sensor, fuente y distancia visibles | Producción propia; ≥2000 px | Propuesta; alternativa DG-008 sin fotografía |
| U05-EXT-003 | Alta para reconocer un instrumento; es un modelo histórico limitado a A/Fast/Slow | Recorte vertical natural; no ampliar la pantalla como evidencia | Dominio público; 1643×3650 | Aprobada solo para reconocimiento; alternativa DG-012 |

## Matriz por slide

| slide_id | bloque | clasificación final | apoyo recomendado | recurso concreto | plan/asset | decisión de implementación |
|---|---|---|---|---|---|---|
"""


out = [header]
for cells in rows:
    slide_id, block = cells[0], cells[1]
    concrete_visual = cells[7]
    visual_class = cells[8]
    out.append(
        f"| {slide_id} | {block} | {visual_class} | {support[visual_class]} | "
        f"{concrete_visual} | {references(slide_id)} | {implementation(slide_id, visual_class)} |"
    )


out.append(
    """

## Decisiones globales

- Prioridad: gráficos y diagramas propios; las fotografías se limitan a ecografía, montaje instrumental y sonómetro.
- Las tablas serán nativas de PowerPoint, no capturas.
- Las ecuaciones se mantendrán editables; no se usarán capturas del PDF.
- Las figuras del libro se reconstruirán a 16:9 con sus scripts o con formas nativas.
- Toda multimedia tendrá reproducción manual, alternativa sin conexión y captura estática.
- No se usarán videos de terceros: una animación propia es más precisa para síntesis de Fourier y espectrograma.
- No se usarán imágenes generadas por IA: no existe una necesidad pedagógica que justifique su riesgo de error.
- Los recursos externos se conservarán sin sobrescribir el original; los recortes serán derivados identificables.

## Estado

**Planificado.** Esta matriz no inserta recursos en PowerPoint ni aprueba todavía gráficos o diagramas no renderizados.
"""
)


OUTPUT.write_text("\n".join(out), encoding="utf-8")
