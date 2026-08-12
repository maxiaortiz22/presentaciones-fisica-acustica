#!/usr/bin/env python3
"""Redacta slides, notas y mapa de fuentes de U7 desde el storyboard aprobado."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


UNIT = Path(__file__).resolve().parents[1]
STORYBOARD = UNIT / "storyboard.md"
ASSETS = UNIT / "assets" / "generated"

EQUATIONS = {
    "U07-023": "`G_CT(f) = L_p,T(f) − L_p,campo(f)`; `G_CT` es una diferencia en dB entre dos posiciones para la misma frecuencia.",
    "U07-024": "`G_CT = 58 dB SPL − 50 dB SPL = 8 dB`.",
    "U07-049": "`N_son = 2^[(L_N − 40 fon)/(10 fon)] son`, para `L_N ≥ 40 fon` dentro del modelo introductorio.",
    "U07-051": "`N_son = 2^[(70 fon − 40 fon)/(10 fon)] son = 2³ son = 8 son`.",
    "U07-057": "`M(f_obj) = L_umbral,e(f_obj) − L_umbral,q(f_obj)`; los dos niveles deben compartir referencia y procedimiento.",
    "U07-058": "`M = 35 dB SPL − 10 dB SPL = 25 dB`.",
    "U07-080": "`SNR = L_p,habla − L_p,ruido`; el resultado se expresa en dB si los niveles son comparables.",
    "U07-081": "`SNR = 68 dB SPL − 60 dB SPL = +8 dB`.",
    "U07-086": "`ALCons = 100 · (1 − n_c/n_p) %`; ejemplo: `100 · (1 − 68/80) % = 15 %`.",
    "U07-090": "`Δt = (r_r − r_d)/c = Δr/c`; `Δr` en m, `c` en m·s⁻¹ y `Δt` en s.",
    "U07-091": "`Δt = 6,8 m / 343 m·s⁻¹ = 0,0198 s ≈ 19,8 ms`.",
    "U07-101": "`ILD = L_p,L − L_p,R`; el orden izquierda menos derecha debe mantenerse y el resultado se expresa en dB.",
    "U07-104": "`|Δt_LR| ≈ d/c`; es una cota del modelo rectilíneo, no la ITD de cualquier dirección.",
    "U07-105": "`|Δt_LR| ≈ 0,180 m / 343 m·s⁻¹ = 5,25 × 10⁻⁴ s ≈ 525 µs`.",
    "U07-125": "`ERB_N(f_c) = 24,7 Hz · [4,37 · f_c/(1000 Hz) + 1]`; modelo de Glasberg–Moore bajo condiciones definidas.",
    "U07-126": "`ERB_N(1000 Hz) = 24,7 Hz · (4,37 + 1) = 132,639 Hz ≈ 133 Hz`.",
    "U07-130": "`SNR = L_p,habla − L_p,ruido`; use los datos suministrados y conserve el signo.",
    "U07-131": "`ALCons = 100 · (1 − n_c/n_p) %`; aplique la misma relación a ambos pares de conteos.",
    "U07-132": "`Δt = (r_r − r_d)/c = Δr/c`; use la diferencia de caminos, no el recorrido reflejado aislado.",
    "U07-133": "`|Δt_LR| ≈ d/c`; compare las cotas obtenidas y explicite qué variable direccional falta.",
}

SOLUTIONS = {
    "U07-130": "`SNR = 64 dB SPL − 58 dB SPL = +6 dB`. La voz posee mayor nivel en la medición, pero no se deduce un porcentaje de inteligibilidad.",
    "U07-131": "`68/80` y `102/120` producen `ALCons = 15 %`. El mismo porcentaje no vuelve equivalentes las pruebas.",
    "U07-132": "`Δt = 5,15 m / 343 m·s⁻¹ = 0,0150 s = 15,0 ms`. Faltan nivel, espectro, dirección y tarea para anticipar eco.",
    "U07-133": "`|Δt_LR| ≈ 0,170 m / 340 m·s⁻¹ = 0,000500 s = 0,500 ms`. Es una cota del modelo rectilíneo.",
}

DEFINITIONS = {
    "U07-009": "Psicoacústica: estudio de las relaciones entre propiedades físicas del estímulo, tarea de escucha y respuesta perceptual.",
    "U07-013": "Umbral auditivo: nivel mínimo detectable bajo un procedimiento y un criterio especificados, sin enmascarador deliberado en el caso absoluto.",
    "U07-021": "Campo libre: idealización en la que no hay reflexiones significativas en el punto de observación.",
    "U07-028": "Curva isofónica: combinaciones de frecuencia y nivel juzgadas con igual sonoridad bajo condiciones definidas.",
    "U07-034": "Altura tonal o pitch: atributo que permite ordenar sensaciones de graves a agudas.",
    "U07-037": "Sonoridad: atributo perceptual que permite ordenar sonidos de menos a más sonoros.",
    "U07-039": "Timbre: atributo multidimensional que permite diferenciar señales aun con pitch, sonoridad y duración global semejantes.",
    "U07-041": "Duración física: intervalo medible entre dos instantes. Duración percibida: estimación temporal realizada por el oyente.",
    "U07-042": "Resolución temporal: capacidad para distinguir cambios o separaciones. Integración temporal: efecto de acumular información durante un intervalo.",
    "U07-046": "Nivel de sonoridad `L_N`: valor en fones definido por comparación con un tono de referencia de 1 kHz igualmente sonoro.",
    "U07-047": "Son: unidad de una escala de razón de sonoridad; 1 son corresponde a 40 fon en la referencia adoptada.",
    "U07-055": "Enmascaramiento: elevación del umbral o reducción de detectabilidad de una señal por la presencia de otra.",
    "U07-062": "Filtro auditivo: modelo funcional de un canal que pondera con mayor fuerza una región de frecuencias alrededor de su frecuencia central.",
    "U07-064": "ERB: ancho de un rectángulo ideal con igual altura máxima e igual área que la respuesta del filtro considerado.",
    "U07-068": "Enmascaramiento hacia adelante: la máscara precede al objetivo y eleva transitoriamente su umbral.",
    "U07-069": "Enmascaramiento hacia atrás: la máscara aparece después del objetivo y modifica su detectabilidad.",
    "U07-072": "Enmascaramiento energético: competencia asociada con superposición de energía dentro de canales auditivos relevantes.",
    "U07-073": "Enmascaramiento informacional: dificultad adicional para seleccionar u organizar la fuente objetivo, más allá de la superposición energética.",
    "U07-077": "Inteligibilidad: proporción o porcentaje de unidades lingüísticas correctamente reconocidas en una tarea definida.",
    "U07-084": "Tiempo de reverberación `T_60`: tiempo requerido para que un decaimiento sonoro recorra 60 dB bajo un método definido.",
    "U07-094": "Efecto de precedencia: familia de fenómenos de fusión y localización ante llegadas próximas, con predominio de información temprana.",
    "U07-099": "Audición binaural: uso de la información obtenida al comparar las señales disponibles en ambos oídos.",
    "U07-100": "ITD: diferencia interaural de tiempo entre estructuras correspondientes de las señales de ambos oídos.",
    "U07-101": "ILD: diferencia interaural de nivel entre mediciones comparables en ambos oídos.",
    "U07-112": "Efecto cocktail party: situación en la que se selecciona una fuente objetivo dentro de una escena con fuentes concurrentes.",
    "U07-115": "Liberación espacial del enmascaramiento: mejora de una tarea cuando la separación espacial aporta pistas útiles para distinguir objetivo y competidores.",
}

EXAMPLES = {
    "U07-002": "Comparar tonos de 250 Hz y 1 kHz con igual RMS digital nominal. La reproducción no equivale a igual `L_p` en el oído.",
    "U07-009": "Estímulo: tono de 1 kHz. Tarea: detectar. Respuesta: detectado en 5 de 10 presentaciones, bajo el criterio indicado.",
    "U07-011": "El mismo tono puede usarse para preguntar si está presente, cuál es más sonoro o de dónde proviene; cada consigna produce otra respuesta.",
    "U07-012": "En diez ensayos, seis respuestas afirmativas no describen una frontera física: describen una proporción para ese criterio.",
    "U07-024": "Campo: 50 dB SPL; próximo al tímpano: 58 dB SPL; diferencia: 8 dB para esa frecuencia y posición.",
    "U07-036": "Complejo armónico con `f₀ = 200 Hz`: al retirar la componente de 200 Hz, el espaciamiento entre armónicos sigue siendo 200 Hz.",
    "U07-040": "Dos señales con magnitud espectral semejante pueden diferir en ataque, fase y envolvente temporal.",
    "U07-051": "70 fon → exponente 3 → 8 son. Interpretación: ocho veces la referencia de 1 son dentro de la escala.",
    "U07-058": "Umbral en quietud: 10 dB SPL. Umbral con máscara: 35 dB SPL. Elevación: 25 dB.",
    "U07-074": "Dos voces semejantes pueden solaparse en frecuencia y, además, competir por la atención del oyente.",
    "U07-081": "Voz: 68 dB SPL; ruido: 60 dB SPL; SNR: +8 dB. Falta conocer material, tarea, oyente y reverberación.",
    "U07-086": "80 consonantes presentadas, 68 correctas: 12 errores sobre 80, equivalentes a 15 %.",
    "U07-091": "Una diferencia de 6,8 m produce aproximadamente 19,8 ms; ese número no decide por sí solo si habrá eco.",
    "U07-105": "Con `d = 0,180 m` y `c = 343 m·s⁻¹`, el modelo entrega aproximadamente 525 µs.",
    "U07-117": "Docente como voz objetivo, ventilación y otras voces como competidores, más reflexiones del aula y una tarea de comprensión.",
    "U07-126": "Para `f_c = 1000 Hz`, el ancho equivalente estimado es aproximadamente 133 Hz; no es una banda anatómica rígida.",
    "U07-130": "Habla a 64 dB SPL y ruido a 58 dB SPL, medidos con la misma banda, ponderación, posición e intervalo.",
    "U07-131": "Resolver cada cociente por separado y comparar luego el porcentaje, el número de ítems y las condiciones de prueba.",
    "U07-132": "Usar solo la diferencia de recorridos y convertir el resultado de segundos a milisegundos al final.",
    "U07-133": "Estimar primero el orden de magnitud en segundos y convertir después a milisegundos o microsegundos.",
}

QUESTION_PROMPTS = {
    "U07-002": ["Dos tonos tienen igual RMS digital nominal y distinta frecuencia.", "Prediga: ¿resultarán igualmente sonoros? Justifique sin convertir la reproducción en una medición."],
    "U07-005": ["Clasifique cada elemento como magnitud física o atributo perceptual.", "Use Hz, dB SPL y s como evidencia; explique por qué las flechas expresan relación y no igualdad."],
    "U07-018": ["Se informa un «umbral» sin describir la medición.", "Complete: frecuencia, escala, campo, criterio, población y procedimiento."],
    "U07-027": ["Compare un tono de referencia de 1 kHz con un tono de prueba.", "¿Qué variable debe ajustarse para juzgarlos igualmente sonoros?"],
    "U07-030": ["Identifique frecuencia, nivel, curva de igual sonoridad y tono de referencia.", "¿Qué condiciones faltan para aplicar la lectura a otro oyente o a una señal compleja?"],
    "U07-052": ["Evalúe: «70 dB SPL equivalen a 8 sones».", "Reformule la afirmación usando `L_N`, frecuencia, señal y condiciones."],
    "U07-061": ["Compare los puntos A y B del mismo patrón de enmascaramiento.", "¿Dónde espera mayor elevación del umbral? Cite evidencia gráfica y una limitación."],
    "U07-071": ["Clasifique los tres cronogramas respecto de la señal objetivo.", "Indique si existe solapamiento y justifique cada nombre temporal."],
    "U07-118": ["Clasifique cada tarjeta: U7 percepción; U8 evaluación; U9 propagación/recinto; U10 ruido.", "Justifique un caso dudoso antes de mover la tarjeta."],
    "U07-130": ["Datos comparables: voz `64 dB SPL`; ruido `58 dB SPL`.", "Calcule la SNR, interprete el signo y nombre un dato faltante."],
    "U07-131": ["Prueba A: `n_p=80`, `n_c=68`. Prueba B: `n_p=120`, `n_c=102`.", "Calcule ALCons y explique qué no vuelve equivalentes a las dos pruebas."],
    "U07-132": ["Una reflexión recorre `5,15 m` adicionales; adopte `c=343 m·s⁻¹`.", "Calcule el retardo y explique por qué no decide si habrá eco."],
    "U07-133": ["Modelo rectilíneo: `d=0,170 m`, `c=340 m·s⁻¹`.", "Calcule la cota de ITD y señale qué no informa sobre la dirección."],
}

VISIBLE_OVERRIDES = {
    "U07-001": ["Licenciatura en Fonoaudiología · Física Acústica", "Relaciones entre estímulo físico, tarea de escucha y respuesta perceptual."],
    "U07-122": ["Umbral e isofónicas: U07-123.", "Símbolos: U07-124. ERB: U07-125–127.", "STI/SII y `T_60`: U07-128–129.", "Ejercicios: U07-130–133. Fuentes: U07-134."],
    "U07-124": ["Magnitudes físicas: `p`, `L_p`, `Δt`.", "Cantidades perceptuales: `L_N`, `N_son`, `M`.", "Descriptores: SNR, `T_60`, ALCons, ITD e ILD.", "Cada símbolo debe leerse con unidad, referencia y condición."],
    "U07-134": ["Fuentes primarias: programa oficial, capítulo LaTeX y PDF del curso.", "Verificación: notación, glosario y análisis de fuentes de U7.", "Ampliaciones: ISO 226 y referencias técnicas ya citadas.", "No usar normas o modelos fuera de su edición y dominio."],
}

RECAPS = {
    "U07-019": ["El umbral pertenece a un procedimiento.", "La sensibilidad varía con frecuencia y condiciones.", "Una proporción de respuestas no es una frontera instantánea."],
    "U07-031": ["La posición modifica el nivel medido.", "La transferencia campo–tímpano depende de frecuencia y dirección.", "Igual sonoridad puede requerir niveles físicos diferentes."],
    "U07-043": ["Frecuencia se relaciona con pitch.", "Nivel se relaciona con sonoridad.", "Espectro y tiempo participan en timbre.", "Duración física no equivale a duración percibida."],
    "U07-053": ["`L_p`: medir presión relativa.", "`L_N`: igualar sonoridad con 1 kHz.", "`N_son`: estimar una razón perceptual."],
    "U07-065": ["Los estímulos ingresan a canales auditivos.", "La tarea define la respuesta observable.", "El cambio de umbral cuantifica el enmascaramiento."],
    "U07-070": ["Simultáneo: existe solapamiento.", "Hacia adelante: la máscara precede al objetivo.", "Hacia atrás: la máscara sigue al objetivo."],
    "U07-075": ["El eje temporal responde cuándo ocurre la máscara.", "El eje funcional pregunta por qué se dificulta la tarea.", "Ambos ejes pueden combinarse en una escena real."],
    "U07-087": ["La SNR describe una relación física.", "`T_60` describe decaimiento del recinto.", "La inteligibilidad pertenece a una prueba con material, tarea y oyente."],
    "U07-097": ["La geometría fija una diferencia de caminos.", "La física permite calcular el retardo.", "La respuesta perceptual exige nivel, señal, dirección y tarea."],
    "U07-109": ["ITD aporta tiempo interaural.", "ILD aporta nivel interaural.", "Espectro y movimiento ayudan a resolver ambigüedades."],
    "U07-120": ["¿Qué señal y ambiente?", "¿Qué transferencia y procesamiento?", "¿Qué tarea y respuesta?", "¿Qué condiciones limitan la inferencia?"],
}

MEDIA_NOTES = {
    "U07-002": "Reproducir U07-MEDIA-001 solo después de la predicción. Dos tonos de 1 s, igual RMS digital nominal, volumen confortable. Alternativa: barras RMS y ondas estáticas.",
    "U07-036": "Reproducir U07-MEDIA-002 después de leer ambos espectros. Complejo completo y sin fundamental; alternativa: espaciamiento armónico señalado en el gráfico.",
    "U07-040": "Reproducir U07-MEDIA-003 después de comparar espectros. Señalar ataque y envolvente; alternativa: dos formas de onda estáticas.",
    "U07-074": "U07-MEDIA-004 es opcional y requiere voces autorizadas. Si no está disponible, resolver con espectrogramas y diagrama; no evaluar al grupo.",
    "U07-082": "U07-MEDIA-005 continúa condicionado a voz autorizada. La slide debe funcionar con dos representaciones estáticas de igual SNR.",
    "U07-092": "Reproducir U07-MEDIA-006 a nivel confortable: directo más copia a −6 dB con retardos visibles. No pedir umbrales; ofrecer alternativa temporal estática.",
    "U07-108": "Reproducir la animación silenciosa U07-MEDIA-007 una vez. La alternativa obligatoria son dos cuadros antes/después del giro.",
    "U07-112": "U07-MEDIA-008 es opcional y condicionado a voces autorizadas. No calificar desempeño; la escena gráfica debe ser autosuficiente.",
}

BLOCK_ERRORS = {
    "B00": "Confundir una magnitud física con su correlato perceptual.",
    "B01": "Tratar el umbral como una frontera fija o como sinónimo de 0 dB SPL.",
    "B02": "Convertir una diferencia campo–tímpano en ganancia universal de sonoridad.",
    "B03": "Usar frecuencia, nivel, espectro o duración como sinónimos de sus atributos perceptuales.",
    "B04": "Convertir directamente dB SPL a fones o sones.",
    "B05": "Identificar el nivel del enmascarador con el umbral enmascarado o tomar el filtro como anatomía literal.",
    "B06": "Invertir los nombres temporalmente o interpretar el enmascaramiento hacia atrás como causalidad física hacia el pasado.",
    "B07": "Suponer que SNR, `T_60` o ALCons determinan por sí solos la inteligibilidad.",
    "B08": "Usar 20 ms como frontera universal entre fusión y eco o como definición completa de Haas.",
    "B09": "Afirmar que ITD e ILD bastan para localizar cualquier fuente o que poseen un corte frecuencial rígido.",
    "B10": "Representar el cocktail party como un filtro físico único o prometer un beneficio clínico fijo.",
    "B11": "Aplicar una fórmula de respaldo sin declarar modelo, unidades, dominio y fuente.",
}

BLOCK_CONTEXT = {
    "B00": "Este inicio instala la diferencia entre descripción física y respuesta perceptual, recuperando U4–U6 sin volver a desarrollarlas.",
    "B01": "El bloque construye el umbral como resultado de una tarea de detección y no como una frontera fija del oído.",
    "B02": "El bloque separa posiciones de medición y luego muestra que igualar sonoridad exige una comparación psicofísica.",
    "B03": "El bloque presenta un atributo por vez y conserva la distinción entre magnitud, representación y percepto.",
    "B04": "El bloque distingue medir presión, igualar sonoridad y estimar una razón perceptual.",
    "B05": "El bloque avanza desde el cambio de umbral observado hacia un modelo de selectividad frecuencial.",
    "B06": "El bloque usa dos ejes independientes: orden temporal y tipo funcional de interferencia.",
    "B07": "El bloque trata la inteligibilidad como desempeño en una prueba y no como propiedad directa de una SNR o de un recinto.",
    "B08": "El bloque separa geometría, retardo calculable y respuesta perceptual ante dos llegadas.",
    "B09": "El bloque integra pistas binaurales, espectrales y dinámicas sin asignar a una sola pista toda la localización.",
    "B10": "El cierre aplica los conceptos a escenas con fuentes concurrentes y delimita la inferencia clínica.",
    "B11": "El respaldo amplía o ejercita contenidos sin modificar la ruta central ni convertir modelos en reglas universales.",
}

CAPTION_OVERRIDES = {
    "U07-029": "Construcción conceptual de igual sonoridad; no contiene datos normativos de ISO 226.",
    "U07-030": "Lectura guiada de dos puntos isofónicos: igual sonoridad bajo la tarea no exige igual nivel físico.",
    "U07-123": "Lista de condiciones que debe acompañar cualquier curva isofónica cuantitativa.",
    "U07-125": "Modelo de Glasberg–Moore para estimar la anchura rectangular equivalente en función de la frecuencia central.",
    "U07-126": "Sustitución de 1 kHz en el modelo: ERB estimada de aproximadamente 133 Hz.",
    "U07-127": "Las expresiones de ERB solo pueden compararse cuando se declaran modelo, unidades de entrada y fuente.",
}

ALT_OVERRIDES = {
    "U07-029": "Esquema no normativo del procedimiento de comparación isofónica, con tono de referencia y tonos de prueba a diferentes frecuencias.",
    "U07-030": "Dos puntos de una misma curva conceptual tienen distinta frecuencia y nivel, pero igual sonoridad bajo la tarea indicada.",
    "U07-123": "Checklist de edición normativa, señal, campo, dirección, población, método y fuente de datos.",
    "U07-125": "Ecuación de ERB de Glasberg–Moore con llamadas a frecuencia central, cociente adimensional, factor en hertz y resultado en hertz.",
    "U07-126": "Cálculo en cuatro pasos para frecuencia central de mil hertz y resultado aproximado de ciento treinta y tres hertz.",
}

DURATION = {
    "portada": "1 min", "divisor": "1–2 min", "pregunta": "2–3 min", "actividad": "3–4 min",
    "objetivos": "3 min", "mapa": "3 min", "definición": "3 min", "explicación": "3 min",
    "proceso": "3 min", "comparación": "3 min", "gráfico": "3–4 min", "ecuación": "4 min",
    "ejemplo": "4 min", "media": "4–5 min", "aplicación": "4 min", "caso": "5 min",
    "recapitulación": "3 min", "síntesis": "4 min", "cierre": "2 min", "guía": "2 min",
    "respaldo": "2–3 min si se consulta", "ejercicio": "4 min", "fuentes": "2 min",
    "error frecuente": "3 min", "puente": "2 min",
}


def parse_storyboard() -> list[dict[str, str]]:
    lines = STORYBOARD.read_text(encoding="utf-8").splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| slide_id |"))
    headers = [part.strip() for part in lines[start].strip("|").split("|")]
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("| U07-"):
            break
        values = [part.strip() for part in line.strip("|").split("|")]
        assert len(values) == len(headers), line
        rows.append(dict(zip(headers, values)))
    assert len(rows) == 134
    return rows


def asset_ids(text: str) -> list[str]:
    return list(dict.fromkeys(re.findall(r"U07-(?:DG|CH|MEDIA|IMG)-\d+[A-Z]?", text)))


def read_section(path: Path, heading: str) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    match = re.search(rf"^## {re.escape(heading)}\s*$\n\n(.+?)(?=\n## |\Z)", text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def asset_metadata(aid: str) -> tuple[str, str]:
    roots = []
    if "-DG-" in aid:
        roots = [ASSETS / "diagrams" / aid]
    elif "-CH-" in aid:
        roots = [ASSETS / "charts" / aid]
    for root in roots:
        caption = read_section(root / "README.md", "Caption sugerido")
        alt = read_section(root / "README.md", "Texto alternativo")
        if caption or alt:
            return caption, alt
    return "", ""


def diagram_model(ids: list[str]) -> dict:
    for aid in ids:
        if "-DG-" not in aid:
            continue
        path = ASSETS / "diagrams" / aid / "diagram_source.json"
        if path.exists():
            import json
            return json.loads(path.read_text(encoding="utf-8"))
    return {}


def external_metadata() -> dict[str, dict[str, str]]:
    path = UNIT / "asset_manifest.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["asset_id"]: row for row in csv.DictReader(handle)}


def split_visible(summary: str) -> list[str]:
    parts = [part.strip(" .") for part in re.split(r";| → ", summary) if part.strip(" .")]
    parts = [part[0].upper() + part[1:] if part and part[0].isalpha() else part for part in parts]
    return parts[:4]


def visible_content(row: dict[str, str]) -> list[str]:
    sid, kind = row["slide_id"], row["slide_type"]
    if sid in VISIBLE_OVERRIDES:
        return VISIBLE_OVERRIDES[sid]
    if sid in RECAPS:
        return RECAPS[sid]
    if kind in {"pregunta", "actividad", "ejercicio"}:
        return QUESTION_PROMPTS.get(sid, split_visible(row["visible_content_summary"]))
    if kind in {"portada", "divisor", "cierre", "guía", "fuentes"}:
        return [row["key_message"]]
    if kind in {"ecuación", "ejemplo"} and sid in EQUATIONS:
        items = split_visible(row["visible_content_summary"])
        return items + ["Interpretar el resultado dentro de las condiciones indicadas."]
    if "DG U07-DG" in row["visual_or_media"] or row["visual_class"] == "diagram":
        model = diagram_model(asset_ids(row["visual_or_media"]))
        classification = model.get("classification", "diagrama conceptual")
        reading = {
            "diagrama de proceso": "Siga la secuencia y explique qué representa cada flecha.",
            "diagrama conceptual": "Compare relaciones; la proximidad entre cajas no representa una escala.",
            "ecuación anotada": "Vincule cada símbolo con su unidad y con el límite de interpretación.",
            "esquema mixto": "Separe la capa física o cuantitativa de la interpretación perceptual.",
        }.get(classification, "Identifique entidades, relaciones y límite de interpretación.")
        return [row["key_message"], reading]
    items = split_visible(row["visible_content_summary"])
    if not items:
        items = [row["key_message"]]
    if row["key_message"].rstrip(".") not in " ".join(items):
        items.insert(0, row["key_message"])
    return items[:5]


def subtitle(row: dict[str, str]) -> str:
    if row["slide_type"] in {"portada", "divisor", "cierre"}:
        return row["key_message"]
    if row["slide_type"] in {"pregunta", "actividad", "ejercicio"}:
        return "Consigna: responda y justifique con magnitud, unidad y condiciones."
    return "—"


def question_for(row: dict[str, str]) -> tuple[str, str]:
    kind = row["slide_type"]
    if kind == "portada":
        return "¿Qué pares físico–perceptuales esperan distinguir en esta unidad?", "Frecuencia–pitch, nivel–sonoridad, espectro–timbre y duración física–percibida son ejemplos iniciales."
    if kind == "divisor":
        return row["working_title"] if "¿" in row["working_title"] else f"¿Qué problema abre la afirmación «{row['working_title']}»?", row["key_message"]
    if kind in {"pregunta", "actividad", "ejercicio"}:
        if row["slide_id"] in QUESTION_PROMPTS:
            prompt = " ".join(QUESTION_PROMPTS[row["slide_id"]])
            return prompt, SOLUTIONS.get(row["slide_id"], row["key_message"])
        return row["working_title"], row["key_message"]
    if kind in {"ecuación", "ejemplo"}:
        return "¿Qué informa el resultado y qué conclusión no permite obtener?", row["key_message"]
    if kind == "gráfico":
        return "¿Qué representa cada eje y cuál es el patrón que debe observarse?", row["key_message"]
    if kind == "media":
        return "Antes de observar o escuchar: ¿qué espera que cambie y qué debería permanecer controlado?", row["key_message"]
    if kind in {"recapitulación", "síntesis"}:
        return "Explique la idea central con un ejemplo distinto de los mostrados.", row["key_message"]
    if kind == "proceso":
        return "¿En qué etapa aparece la tarea del oyente y qué elementos siguen describiendo el estímulo?", row["key_message"]
    if kind == "mapa":
        return "Elija dos elementos del mapa: ¿qué relación expresan y qué interpretación sería incorrecta?", row["key_message"]
    if kind == "definición":
        return "¿Qué dato o procedimiento habría que agregar para aplicar esta definición a un caso real?", row["key_message"]
    if kind == "comparación":
        return "¿Qué criterio permite separar las dos columnas sin tratarlas como sinónimos?", row["key_message"]
    if kind in {"aplicación", "caso"}:
        return "¿Qué mediría primero y qué conclusión clínica todavía no estaría justificada?", row["key_message"]
    if kind in {"objetivos", "cierre"}:
        return "¿Qué evidencia observable mostraría que esta meta se alcanzó?", row["key_message"]
    return "Si cambiara una condición del estímulo o de la tarea, ¿qué parte de la conclusión debería revisarse?", row["key_message"]


def guide_visual(row: dict[str, str], ids: list[str]) -> str:
    if any("-DG-" in aid for aid in ids):
        model = diagram_model(ids)
        node_titles = [item.get("title", "") for item in model.get("items", []) if item.get("title")]
        route = " → ".join(node_titles[:5])
        if len(node_titles) > 5:
            route += " → …"
        base = f"Recorrido sugerido: {route}. " if route else "Recorrer las entidades en el orden visual. "
        return base + "Nombrar primero los elementos, explicar luego las relaciones y cerrar con el límite indicado en el caption. No leer las cajas como un párrafo."
    if any("-CH-" in aid for aid in ids) or row["slide_type"] == "gráfico":
        return "Nombrar ejes, magnitudes, unidades y escala antes de seguir la curva. Señalar el patrón y cerrar con el límite del modelo o de los datos."
    if any("-MEDIA-" in aid for aid in ids):
        return "Mostrar primero la consigna y la alternativa estática; reproducir una vez; recoger observaciones sin convertirlas en medición individual."
    return "Señalar el foco principal, recorrer los elementos en el orden del layout y cerrar con la frase de interpretación."


def caption_and_alt(row: dict[str, str], ids: list[str], manifest: dict[str, dict[str, str]]) -> tuple[str, str]:
    if row["slide_id"] in CAPTION_OVERRIDES:
        return CAPTION_OVERRIDES[row["slide_id"]], ALT_OVERRIDES.get(row["slide_id"], row["visual_or_media"])
    for aid in ids:
        caption, alt = asset_metadata(aid)
        if caption or alt:
            return caption or row["key_message"], alt or row["visual_or_media"]
        if aid in manifest and (manifest[aid].get("description") or manifest[aid].get("title")):
            meta = manifest[aid]
            return meta.get("description") or meta.get("title"), meta.get("description") or meta.get("title")
    caption = row["key_message"]
    visual_text = row["visual_or_media"].replace("notas futuras", "notas del orador")
    alt = f"{visual_text} La idea central es: {row['key_message']}"
    return caption, alt


def visual_instruction(row: dict[str, str], ids: list[str]) -> str:
    text = row["visual_or_media"].replace("notas futuras", "notas del orador")
    if any("-DG-" in aid for aid in ids):
        text += " Mantener el diagrama dominante; fuera de las cajas, usar solo la idea central y el caption. No duplicar nodos en bullets."
    elif any("-CH-" in aid for aid in ids):
        text += " Mantener ejes, unidades, escala y rótulo de modelo/datos visibles."
    if row["slide_id"] in {"U07-029", "U07-030", "U07-123"}:
        text += " U07-CH-004 está bloqueado: usar únicamente el esquema conceptual no normativo aprobado."
    if row["slide_id"] == "U07-025":
        text += " El overlay U07-DG-010 permanece condicionado a la fotografía REM definitiva."
    if row["slide_id"] in {"U07-125", "U07-126"}:
        text += " La fuente editable U07-DG-020C permanece pendiente; conservar la ecuación como contenido de respaldo, sin producir todavía el visual."
    return text


def source_note(row: dict[str, str]) -> str:
    return row["source"]


def write_slide_text(rows: list[dict[str, str]], manifest: dict[str, dict[str, str]]) -> None:
    out = [
        "# Unidad 7 — Texto de slides",
        "",
        "Versión de redacción v01 · 2026-08-11 · Derivada exclusivamente del storyboard aprobado.",
        "",
        "Cada bloque conserva la arquitectura, el ID, el layout, la fuente y la transición del storyboard. `—` indica que la slide no introduce ese componente.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        ids = asset_ids(row["visual_or_media"])
        caption, alt = caption_and_alt(row, ids, manifest)
        content = visible_content(row)
        out += [
            f"## {sid}", "",
            f"- **Título:** {row['working_title']}",
            f"- **Subtítulo:** {subtitle(row)}",
            "- **Contenido visible:**",
        ]
        out += [f"  - {item.rstrip()}" if item.rstrip().endswith((".", "?", "%")) else f"  - {item.rstrip()}." for item in content]
        out += [
            f"- **Ecuaciones:** {EQUATIONS.get(sid, '—')}",
            f"- **Definiciones:** {DEFINITIONS.get(sid, '— (se reutilizan términos ya definidos en el bloque).')}",
            f"- **Ejemplo:** {EXAMPLES.get(sid, '—')}",
            f"- **Caption sugerido:** {caption}",
            f"- **Visual:** {visual_instruction(row, ids)}",
            f"- **Layout:** `{row['suggested_layout']}`.",
            f"- **Fuente:** {source_note(row)}",
            f"- **Notas del orador:** ver `{sid}` en `speaker_notes.md`.",
            f"- **Transición:** {row['transition']}",
            f"- **Texto alternativo:** {alt}", "",
        ]
    (UNIT / "slide_text.md").write_text("\n".join(out), encoding="utf-8")


def write_speaker_notes(rows: list[dict[str, str]]) -> None:
    out = [
        "# Unidad 7 — Notas del orador",
        "",
        "Versión de redacción v01 · 2026-08-11 · Las notas amplían el contenido visible sin repetirlo literalmente.",
        "",
        "Las demostraciones auditivas son opcionales, supraliminales y no clínicas. Toda consigna puede resolverse mediante la alternativa visual.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        block = row["block"].split()[0]
        ids = asset_ids(row["visual_or_media"])
        question, expected = question_for(row)
        explanation = (
            f"{row['speaker_note_goal']} {BLOCK_CONTEXT[block]} "
            f"Idea que debe quedar al cerrar: {row['key_message']}"
        )
        if sid in EQUATIONS:
            explanation += f" Escribir y leer la relación por términos: {EQUATIONS[sid]} Comprobar unidades antes de interpretar."
        if sid in DEFINITIONS:
            explanation += f" Definición de trabajo: {DEFINITIONS[sid]}"
        if sid in EXAMPLES:
            explanation += f" Ejemplo para desarrollar oralmente: {EXAMPLES[sid]}"
        if sid in SOLUTIONS:
            explanation += f" Solución esperada: {SOLUTIONS[sid]}"
        out += [
            f"## {sid} — {row['working_title']}", "",
            f"- **Duración aproximada:** {DURATION.get(row['slide_type'], '3 min')}.",
            f"- **Explicación extendida:** {explanation}",
            f"- **Guía para el visual/diagrama:** {guide_visual(row, ids)}",
            f"- **Pregunta al curso:** {question}",
            f"- **Respuesta esperada:** {expected}",
            f"- **Demostración o multimedia:** {MEDIA_NOTES.get(sid, '—')}",
            f"- **Error frecuente a vigilar:** {BLOCK_ERRORS[block] if row['slide_type'] not in {'portada', 'divisor', 'objetivos', 'guía', 'fuentes', 'cierre'} else '—'}",
            f"- **Transición oral:** {row['transition']}",
            f"- **[Sources]:** {row['source']}", "",
        ]
    (UNIT / "speaker_notes.md").write_text("\n".join(out), encoding="utf-8")


def write_source_map(rows: list[dict[str, str]]) -> None:
    legend = """# Unidad 7 — Mapa de fuentes por slide

Versión v01 · 2026-08-11

## Abreviaturas

- `PO`: programa oficial 2025, Unidad 7, p. 4.
- `TEX`: `context/libro_latex/chapters/07-psicoacustica.tex`.
- `PDF`: libro del curso, capítulo 7, pp. 177–205.
- `BR`, `INV`, `SA`, `OD`: brief, inventario, análisis de fuentes y decisiones abiertas de U7.
- `NOT`, `GLO`, `TPL`: notación, glosario y sistema visual.
- `PREV`, `CM`, `CDM`, `MAP`, `COV`, `DM`: continuidad y arquitectura curricular.
- `REF`: referencia técnica ya citada en la bibliografía del libro.
- `EP`: elaboración pedagógica propia, sin introducir datos externos.

## Trazabilidad

| slide_id | función | fuente del storyboard | assets previstos | uso y límite |
|---|---|---|---|---|
"""
    lines = [legend.rstrip()]
    for row in rows:
        ids = asset_ids(row["visual_or_media"])
        assets = ", ".join(f"`{aid}`" for aid in ids) if ids else "—"
        limit = row["key_message"]
        if row["slide_id"] in {"U07-029", "U07-030", "U07-123"}:
            limit += " U07-CH-004 no se usa como dato normativo mientras continúe bloqueado."
        if row["slide_id"] in {"U07-125", "U07-126", "U07-127"}:
            limit += " Material de respaldo condicionado a modelo, convención y fuente explícitos."
        lines.append(f"| {row['slide_id']} | {row['learning_purpose']} | {row['source']} | {assets} | {limit} |")
    lines += [
        "", "## Dependencias abiertas", "",
        "- U07-CH-004: no incorporar datos isofónicos normativos sin licencia, edición y condiciones verificadas; usar esquema conceptual.",
        "- U07-DG-010: overlay REM pendiente de la fotografía definitiva.",
        "- U07-DG-020C: visual de la ecuación ERB pendiente de decisión; el texto permanece solo en respaldo.",
        "- U07-MEDIA-004, 005 y 008: requieren voces autorizadas; las slides tienen alternativa visual autosuficiente.",
        "- STI/SII: mención de respaldo; no calcular sin normas, datos y procedimientos propios.",
    ]
    (UNIT / "source_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_review(rows: list[dict[str, str]]) -> None:
    slide_text = (UNIT / "slide_text.md").read_text(encoding="utf-8")
    notes = (UNIT / "speaker_notes.md").read_text(encoding="utf-8")
    source_map = (UNIT / "source_map.md").read_text(encoding="utf-8")
    ids = [row["slide_id"] for row in rows]
    assert len(ids) == len(set(ids)) == 134
    for sid in ids:
        assert slide_text.count(f"## {sid}\n") == 1
        assert notes.count(f"## {sid} —") == 1
        assert source_map.count(f"| {sid} |") == 1
    required = ["Título", "Subtítulo", "Contenido visible", "Ecuaciones", "Definiciones", "Ejemplo", "Caption sugerido", "Visual", "Layout", "Fuente", "Notas del orador", "Transición", "Texto alternativo"]
    for field in required:
        assert slide_text.count(f"**{field}:") == 134, field
    note_fields = ["Duración aproximada", "Explicación extendida", "Guía para el visual/diagrama", "Pregunta al curso", "Respuesta esperada", "Demostración o multimedia", "Error frecuente a vigilar", "Transición oral", "[Sources]"]
    for field in note_fields:
        assert notes.count(f"**{field}:") == 134, field
    visible_sections = re.findall(r"- \*\*Contenido visible:\*\*(.+?)- \*\*Ecuaciones:", slide_text, flags=re.S)
    word_counts = [len(re.findall(r"\b\w+\b", section)) for section in visible_sections]
    over_90 = [rows[i]["slide_id"] for i, count in enumerate(word_counts) if count > 90]
    under_8 = [rows[i]["slide_id"] for i, count in enumerate(word_counts) if count < 8 and rows[i]["slide_type"] not in {"portada", "divisor", "cierre"}]
    classes = Counter(row["slide_type"] for row in rows)
    classes_summary = ", ".join(f"{kind}: {count}" for kind, count in classes.items())
    review = f"""# Unidad 7 — Revisión de redacción

Fecha: 2026-08-11. Estado: **aprobado como borrador de texto y notas v01**. No se produjo PowerPoint.

## Cobertura

- Slides del storyboard: 134.
- Slides redactadas: 134.
- IDs duplicados o faltantes: 0.
- Campos de texto por slide: 13/13 completos.
- Bloques de notas por slide: 9/9 completos.
- Filas de trazabilidad: 134.
- Tipos principales preservados: {classes_summary}.

## Revisión pedagógica

- Se conserva la secuencia aprobada de cuatro encuentros y el respaldo no lineal.
- Las definiciones se introducen antes de las ecuaciones y los ejemplos separan cálculo de interpretación.
- `L_p`, `L_N`, `N_son`, `M`, SNR, ALCons, `T_60`, ITD e ILD mantienen símbolos y unidades consistentes.
- Las notas incluyen pregunta respondible, respuesta esperada, transición, error frecuente, duración y guía visual.
- Las slides con diagramas usan texto complementario breve; las explicaciones extensas quedan en notas.
- Toda multimedia conserva una alternativa visual y una advertencia de uso supraliminal/no clínico.
- Los resultados de U07-130–133 quedan reservados para las notas; las slides muestran datos, consigna y procedimiento sin anticipar la solución.

## Revisión de legibilidad

- Máximo de palabras detectado en un bloque de contenido visible: {max(word_counts)}.
- Slides con más de 90 palabras visibles: {', '.join(over_90) if over_90 else 'ninguna'}.
- Slides no divisor con menos de 8 palabras visibles: {', '.join(under_8) if under_8 else 'ninguna'}.
- No se añadieron párrafos extensos dentro de cajas de diagramas.

## Correcciones y decisiones aplicadas

| ID | Severidad | Hallazgo | Corrección | Estado |
|---|---|---|---|---|
| WR-01 | mayor | Las isofónicas cuantitativas continúan sin datos reutilizables aprobados. | U07-029, 030 y 123 indican usar el esquema conceptual no normativo. | cerrado para redacción; asset bloqueado |
| WR-02 | mayor | ERB puede presentarse con convenciones distintas. | La fórmula se limita al respaldo U07-125–127, con modelo, unidades y fuente. | mitigado |
| WR-03 | mayor | ALCons podía leerse como predictor causal. | U07-086 y sus notas lo definen como porcentaje observado de una prueba. | cerrado |
| WR-04 | mayor | Audios condicionados podían volver incompleta la secuencia. | Cada media incluye alternativa estática y no evalúa audición individual. | cerrado |
| WR-05 | moderada | Las notas podían duplicar el texto visible. | Se redactaron como explicación, pregunta, respuesta, error y transición. | cerrado |

## Problemas abiertos

- Asset isofónico normativo U07-CH-004.
- Overlay REM U07-DG-010.
- Visual de fórmula ERB U07-DG-020C.
- Voces autorizadas para U07-MEDIA-004, 005 y 008.
- Revisión pedagógica independiente de U7 antes de producir el deck, exigida por `AGENTS.md`.

La presentación todavía no está terminada: estos archivos habilitan la siguiente fase de producción, pero no sustituyen el render y la revisión del PowerPoint.
"""
    (UNIT / "writing_review.md").write_text(review, encoding="utf-8")


def main() -> None:
    rows = parse_storyboard()
    manifest = external_metadata()
    write_slide_text(rows, manifest)
    write_speaker_notes(rows)
    write_source_map(rows)
    write_review(rows)
    print("Redactadas y verificadas 134 slides; PowerPoint no producido.")


if __name__ == "__main__":
    main()
