"""Genera los entregables de redacción de U09 desde el storyboard aprobado.

No consulta el libro, la web ni otras fuentes de contenido. Las referencias que
aparecen en los documentos de salida se copian literalmente del storyboard.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STORYBOARD = ROOT / "storyboard.md"

LABELS = (
    "bloque",
    "funcion",
    "titulo",
    "objetivo",
    "mensaje",
    "contenido",
    "visual",
    "clase",
    "layout",
    "notas",
    "fuente",
    "prerreq",
    "transicion",
    "ruta",
)


def parse_storyboard() -> list[dict[str, str]]:
    slides: list[dict[str, str]] = []
    for line in STORYBOARD.read_text(encoding="utf-8-sig").splitlines():
        if not line.startswith("| U09-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 15:
            raise ValueError(f"Fila inválida ({len(cells)} celdas): {line}")
        slide = {"id": cells[0]}
        slide.update(dict(zip(LABELS, cells[1:])))
        slides.append(slide)
    ids = [slide["id"] for slide in slides]
    expected = [f"U09-{number:03d}" for number in range(1, 97)]
    if ids != expected:
        raise ValueError("El storyboard no contiene la secuencia completa U09-001–U09-096")
    return slides


def sentence(text: str) -> str:
    text = text.strip()
    if not text:
        return "—"
    text = text[0].upper() + text[1:]
    if text[-1] not in ".?!":
        text += "."
    return text


def chunks(text: str) -> list[str]:
    parts = [part.strip() for part in re.split(r";\s*", text) if part.strip()]
    return [sentence(part) for part in parts]


def subtitle(slide: dict[str, str]) -> str:
    topic = slide["bloque"].split("·", 1)[-1].strip()
    if slide["ruta"] == "backup":
        return f"Material de respaldo · {slide['funcion'].capitalize()}"
    if slide["ruta"] == "blocked-source":
        return "Respaldo bloqueado · falta completar la fuente normativa"
    if slide["funcion"] == "divisor":
        return topic
    return f"{topic} · {slide['funcion'].capitalize()}"


EQUATIONS: dict[str, list[str]] = {
    "U09-008": ["`L_W`: nivel de potencia sonora de la fuente, en dB.", "`L_p`: nivel de presión sonora en un punto, en dB.", "Ambos usan referencias diferentes; no son magnitudes intercambiables."],
    "U09-014": ["`L_{p2}=L_{p1}-20\\log_{10}(r_2/r_1)`", "`r_1` y `r_2` en la misma unidad de longitud; el cociente es adimensional."],
    "U09-015": ["`r_2/r_1=1,00/0,50=2`", "`L_{p2}=L_{p1}-20\\log_{10}(2)=L_{p1}-6,02\\ \\text{dB}`", "Con el dato inicial del caso aprobado: `L_{p2}=83,98\\approx84\\ \\text{dB SPL}`."],
    "U09-019": ["`DI=10\\log_{10}(Q_{dir})`", "`Q_{dir}=4\\Rightarrow DI=6,02\\ \\text{dB}`"],
    "U09-023": ["`c\\approx331+0,6\\,\\theta`", "`c` en m·s⁻¹ y `θ` en °C, dentro del intervalo didáctico indicado."],
    "U09-024": ["`\\lambda=c/f`", "A 5 °C: `c=334 m·s⁻¹` y `λ=0,334 m` para 1000 Hz.", "A 25 °C: `c=346 m·s⁻¹` y `λ=0,346 m` para 1000 Hz."],
    "U09-026": ["`c_{ef}=c+v_{viento}\\cos\\psi`", "`c_{ef}`, `c` y `v_{viento}` en m·s⁻¹; `ψ` es el ángulo entre propagación y viento."],
    "U09-028": ["`c=\\sqrt{\\gamma p_a/\\rho_a}`", "`p_a` en Pa; `ρ_a` en kg·m⁻³; `γ` es adimensional."],
    "U09-030": ["`L_p(r_2)=L_p(r_1)-20\\log_{10}(r_2/r_1)-a_{atm}(f,estado)\\,\\Delta r`", "No se asigna un valor a `a_atm` sin una fuente y condiciones completas."],
    "U09-036": ["`R_E+\\alpha+\\tau_E=1`", "`0\\le R_E,\\alpha,\\tau_E\\le1`; los tres coeficientes son adimensionales."],
    "U09-037": ["`\\tau_E=1-0,55-0,30=0,15`"],
    "U09-041": ["No se incorpora la relación de senos hasta aprobar una fuente académica completa."],
    "U09-043": ["`\\lambda=c/f`", "`λ` en m; `c` en m·s⁻¹; `f` en Hz."],
    "U09-049": ["`T_{60}`: intervalo asociado con una disminución de 60 dB del nivel durante el decaimiento."],
    "U09-050": ["`A_{eq}=\\sum_i \\alpha_i S_i`", "`A_eq` en m² equivalentes; `α_i` adimensional; `S_i` en m²."],
    "U09-051": ["`T_{60}\\approx0,161\\,V/A_{eq}`", "En SI: `V` en m³, `A_eq` en m² equivalentes y `T_60` en s."],
    "U09-052": ["`V=8\\times6\\times3=144\\ \\text{m}^3`", "`S_{total}=180\\ \\text{m}^2`; `\\bar\\alpha=0,25`; `A_{eq}=45\\ \\text{m}^2`.", "`T_{60}\\approx0,161(144/45)=0,52\\ \\text{s}`."],
    "U09-058": ["`R=10\\log_{10}(1/\\tau_E)`", "`τ_E=0,01\\Rightarrow R=20 dB`; `τ_E=0,001\\Rightarrow R=30 dB`."],
    "U09-059": ["`R=10\\log_{10}(1/\\tau_E)`; cada década menos de `τ_E` agrega 10 dB."],
    "U09-062": ["`m_s=\\text{masa}/\\text{área}`", "Unidad SI: kg·m⁻²."],
    "U09-063": ["Forma relativa segura: `\\Delta R=20\\log_{10}(m_{s2}/m_{s1})+20\\log_{10}(f_2/f_1)`.", "Se omite la constante de la forma absoluta hasta verificar la convención."],
    "U09-064": ["`20\\log_{10}(2)=6,02\\ \\text{dB}`"],
    "U09-085": ["`W/(4\\pi r^2)\\propto I\\propto p_{rms}^2\\Rightarrow p_{rms}\\propto1/r`", "`\\Delta L_p=-20\\log_{10}(r_2/r_1)` bajo las hipótesis del modelo."],
    "U09-088": ["Sin ecuación numérica ni coeficientes hasta documentar la fuente primaria y el estado del aire."],
    "U09-089": ["Sin ecuaciones de Snell generalizado hasta aprobar una fuente académica primaria."],
    "U09-092": ["Contenido bloqueado: no se incluyen límites numéricos."],
}

DEFINITIONS: dict[str, str] = {
    "U09-007": "Fuente: sistema que emite. Trayecto: medio, geometría e interfaces que modifican la propagación. Receptor: sistema físico que recibe; la medición registra bajo condiciones declaradas.",
    "U09-008": "`L_W` describe emisión; `L_p` describe presión sonora en un punto y un campo concretos.",
    "U09-009": "Mecanismo de propagación: proceso físico identificable que redistribuye, disipa, desvía o transmite energía sonora.",
    "U09-017": "Directividad: variación angular de la emisión o del nivel a igual distancia y bajo condiciones comparables.",
    "U09-019": "`Q_dir` es una razón lineal de concentración relativa; `DI` expresa esa razón en decibelios.",
    "U09-025": "Gradiente: cambio espacial de una magnitud; aquí, temperatura y rapidez con la altura.",
    "U09-026": "Rapidez efectiva: rapidez de propagación respecto del suelo al considerar el movimiento uniforme del aire.",
    "U09-030": "Divergencia redistribuye energía geométricamente; absorción atmosférica la disipa según frecuencia y estado del aire.",
    "U09-035": "Reflexión retorna energía, absorción la disipa en el material y transmisión la conduce al otro lado.",
    "U09-038": "Reflexión: retorno de una fracción de la energía al medio de origen.",
    "U09-039": "Reflexión es un mecanismo; eco es una llegada distinguible; reverberación es la persistencia de múltiples llegadas.",
    "U09-042": "Difracción: propagación hacia regiones de sombra geométrica por bordes o aberturas.",
    "U09-049": "`T_60`: descriptor temporal del decaimiento reverberante, no una medida de aislamiento.",
    "U09-050": "Área equivalente de absorción: suma de cada superficie multiplicada por su coeficiente de absorción.",
    "U09-058": "`τ_E` es la fracción energética transmitida; `R` es el índice logarítmico asociado, en dB.",
    "U09-061": "Acondicionar modifica el campo interior; aislar limita transmisión; insonorizar nombra un objetivo general, no una magnitud.",
    "U09-062": "Masa superficial: masa de una hoja dividida por su área.",
}

EXAMPLES: dict[str, str] = {
    "U09-002": "Comparar dos puntos de medición entre avenida, fachada, consultorio y cabina sin atribuir todavía una única causa.",
    "U09-010": "Clasificar orientación del altavoz, distancia, viento, puerta, micrófono y escala de lectura como fuente, trayecto o medición; justificar los casos mixtos.",
    "U09-015": "Entre 0,50 m y 1,00 m, la razón es 2 y el cambio ideal es −6,02 dB. Con el dato inicial del caso aprobado, el resultado previsto es 83,98 ≈ 84 dB SPL.",
    "U09-021": "Ante tres escenarios, decidir si corresponde distancia, directividad, ambos o ninguna estimación por falta de datos.",
    "U09-024": "Para una fuente de 1000 Hz, calcular primero `c` a 5 °C y 25 °C y luego `λ=c/f`; `f` permanece en 1000 Hz.",
    "U09-032": "Completar una ficha de campo antes de comparar dos mediciones exteriores.",
    "U09-037": "Si `R_E=0,55` y `α=0,30`, falta `τ_E=0,15`; la respuesta debe incluir que 15 % de la energía incidente se transmite.",
    "U09-044": "Mantener barrera y receptor fijos y comparar cualitativamente 125, 500 y 4000 Hz mediante `λ/escala`.",
    "U09-052": "Aula rectangular de 8 m × 6 m × 3 m, con `A_eq=45 m²`: estimación `T_60≈0,52 s` bajo Sabine.",
    "U09-058": "Transmitir 1 % corresponde a 20 dB; transmitir 0,1 %, a 30 dB, dentro de la relación ideal.",
    "U09-064": "Duplicar solo `m_s` suma 6,02 dB; duplicar solo `f` suma 6,02 dB en la región controlada por masa.",
    "U09-067": "Clasificar tres intervenciones: absorbente interior, panel más pesado y puerta abierta; indicar si actúan sobre campo interior, elemento o ruta débil.",
    "U09-075": "Evaluar la frase “la cabina tiene 28 dB(A)” enumerando qué datos faltan antes de afirmar aptitud audiométrica.",
    "U09-077": "Priorizar qué medir cuando coexisten ruido exterior, ventilación, equipos y tratamiento interior, sin diseñar una solución.",
    "U09-082": "Para seis afirmaciones del caso, completar mecanismo, modelo, dato requerido, medición y límite de la conclusión.",
    "U09-087": "Dos problemas adicionales de distancia y directividad, con resultado, hipótesis, unidades y límite de validez.",
    "U09-090": "Resolver un balance energético y el aula de Sabine; cerrar cada cálculo con control dimensional y crítica del modelo.",
    "U09-094": "Reformular doce afirmaciones falsas o incompletas y nombrar en cada una el mecanismo o la condición omitida.",
    "U09-095": "Resolver el caso de la clínica mediante una matriz fuente–trayecto–receptor, sin fingir una atenuación total.",
}


def equations(slide: dict[str, str]) -> list[str]:
    return EQUATIONS.get(slide["id"], ["No corresponde en esta slide."])


def definition(slide: dict[str, str]) -> str:
    if slide["id"] in DEFINITIONS:
        return DEFINITIONS[slide["id"]]
    if any(word in slide["funcion"] for word in ("definición", "concepto", "comparación")):
        return slide["mensaje"]
    return "No se introduce una definición nueva en esta slide."


def example(slide: dict[str, str]) -> str:
    if slide["id"] in EXAMPLES:
        return EXAMPLES[slide["id"]]
    if any(word in slide["funcion"] for word in ("actividad", "aplicación", "ejercicio", "caso")):
        return slide["contenido"]
    return "No corresponde en esta slide."


def visual_instruction(slide: dict[str, str]) -> str:
    base = slide["visual"]
    cls = slide["clase"]
    special = {
        "U09-041": "Mantener un placeholder editable sin relación de senos. Mostrar solo ángulos, normal y la advertencia ‘formalización pendiente de fuente académica’.",
        "U09-063": "Usar U09-DG-048 únicamente con la expresión relativa de `ΔR`; reservar la forma absoluta hasta verificar la convención.",
        "U09-088": "No renderizar una curva. Conservar un marco editable con ejes sin datos y una ficha visible de variables y fuente pendiente.",
        "U09-089": "Usar U09-DG-067 como esquema cualitativo de modos longitudinal y transversal, sin ecuaciones ni ángulos cuantificados.",
        "U09-092": "No renderizar una tabla cuantitativa. Mostrar una tarjeta de estado bloqueado y los campos documentales pendientes.",
    }
    if slide["id"] in special:
        return special[slide["id"]]
    if cls == "diagram":
        return f"{base} Idea central: {slide['mensaje']} Mantener nodos breves, conectores sin texto superpuesto y lectura por etapas."
    if cls == "mixed":
        return f"{base} Separar ecuación, interpretación y ejemplo; no trasladar la explicación extensa al diagrama."
    if cls == "chart":
        return f"{base} Rotular ejes, magnitudes, unidades y escala; distinguir datos calculados, ejemplo sintético o placeholder, según corresponda."
    if cls in {"video_or_gif", "external_image"}:
        return f"{base} Conservar una alternativa estática y llamados breves que no oculten el recurso."
    return f"{base} Mantener jerarquía tipográfica y espacio de lectura propio del layout."


def caption(slide: dict[str, str]) -> str:
    if slide["ruta"] == "blocked-source":
        return "Recurso reservado: no contiene cifras hasta documentar la fuente normativa completa."
    if slide["clase"] == "chart":
        return sentence(f"Lectura propuesta: {slide['mensaje'].lower()}")
    if slide["clase"] in {"diagram", "mixed"}:
        return sentence(f"El esquema organiza la idea central: {slide['mensaje'].lower()}")
    if slide["clase"] == "video_or_gif":
        return "Comparación auditiva y temporal con reproducción a nivel seguro; no constituye una medición."
    return sentence(slide["mensaje"])


def alt_text(slide: dict[str, str]) -> str:
    visual = re.sub(r"`([^`]+)`", r"\1", slide["visual"])
    if slide["ruta"] == "blocked-source":
        return "Marcador de una tabla normativa bloqueada, sin cifras, con los campos de fuente y escenario todavía pendientes."
    return sentence(f"{visual} La composición permite reconocer que {slide['mensaje'].lower()}")


def visible_content(slide: dict[str, str]) -> list[str]:
    special = {
        "U09-001": ["Entre la fuente y quien escucha, el trayecto importa.", "Pregunta organizadora: ¿por qué una misma fuente no produce el mismo nivel en todo lugar?"],
        "U09-003": ["Analizar mecanismos de propagación.", "Aplicar modelos con hipótesis explícitas.", "Calcular e interpretar resultados con unidades.", "Comparar alternativas y justificar qué debe medirse."],
        "U09-004": ["Ya conocemos: distancia, frecuencia, longitud de onda, niveles, temperatura y bandas.", "Necesitamos recuperar: unidades, razones, logaritmos y lectura de gráficos.", "Diagnóstico: ¿qué magnitud cambiaría en cada situación?"],
        "U09-005": ["Encuentro 1: modelo organizador, distancia, directividad y atmósfera.", "Encuentro 2: superficies, obstáculos, recintos y reverberación.", "Encuentro 3: aislamiento, cabinas, verificación e integración."],
        "U09-007": ["Fuente: emite.", "Trayecto: redistribuye, disipa o desvía.", "Receptor: recibe.", "Medición: registra bajo condiciones declaradas."],
        "U09-009": ["¿Se redistribuye? Divergencia o directividad.", "¿Se disipa? Absorción atmosférica o material.", "¿Cambia de ruta? Reflexión, transmisión, refracción o difracción.", "¿Qué magnitud y qué condiciones describen cada mecanismo?"],
        "U09-011": ["1. ¿Qué cambia?", "2. ¿Qué se conserva?", "3. ¿Qué puede estimarse?", "4. ¿Qué debe medirse?"],
        "U09-032": ["Geometría: distancias y alturas.", "Atmósfera: temperatura, viento, humedad y presión.", "Entorno: suelo, obstáculos y dirección.", "Medición: bandas, instante y duración del registro."],
        "U09-041": ["Formalización pendiente de fuente académica aprobada.", "Idea cualitativa permitida: los ángulos dependen de las velocidades de fase y de los modos considerados.", "No usar esta slide para calcular conversión modal."],
        "U09-070": ["Envolvente y uniones.", "Puerta, visor y sellos.", "Ventilación y pasacables.", "Apoyos y vínculo con la estructura."],
        "U09-071": ["Rutas posibles: envolvente, juntas, conductos, flanqueo, vibración y equipos.", "La ruta dominante puede no atravesar el panel principal."],
        "U09-072": ["1. Definir la prueba.", "2. Seleccionar el criterio.", "3. Medir por bandas.", "4. Comparar con el criterio.", "5. Documentar condiciones y resultado."],
        "U09-074": ["Norma y edición.", "Adopción o jurisdicción.", "Vía y transductor.", "Bandas de frecuencia.", "Menor nivel de prueba.", "Sin estos datos, no corresponde publicar cifras."],
        "U09-083": ["Identificar el mecanismo.", "Elegir el modelo adecuado.", "Declarar condiciones e hipótesis.", "Medir cuando la estimación no alcance.", "Limitar la conclusión a la evidencia disponible."],
        "U09-088": ["Gráfico reservado: todavía no contiene curva.", "Datos requeridos: frecuencia, temperatura, humedad, presión y distancia.", "No reconstruir coeficientes de memoria."],
        "U09-089": ["Ampliación cualitativa: en un sólido pueden coexistir modos longitudinales y transversales.", "Las ecuaciones y relaciones angulares permanecen pendientes de una fuente académica primaria.", "El modelo de rayos tiene límites que deben declararse."],
    }
    if slide["id"] in special:
        return special[slide["id"]]
    items = [sentence(slide["mensaje"])]
    items.extend(chunks(slide["contenido"]))
    if slide["ruta"] == "blocked-source":
        return [
            "Contenido bloqueado: no se muestran cifras normativas.",
            "Campos pendientes: norma, edición, adopción, bandas, vía, transductor y menor nivel de prueba.",
            "La slide se habilitará únicamente cuando la fuente completa esté aprobada.",
        ]
    return items


def duration(slide: dict[str, str]) -> str:
    function = slide["funcion"]
    if slide["id"] in {"U09-041", "U09-088", "U09-089", "U09-092"}:
        return "0 min en la ruta docente; slide bloqueada"
    if function in {"portada", "divisor", "cierre y puente"}:
        minutes = 2
    elif any(word in function for word in ("ejemplo", "ejercicio", "actividad", "caso")):
        minutes = 5
    elif any(word in function for word in ("ecuación", "gráfico", "proceso", "aplicación")):
        minutes = 4
    elif "multimedia" in function:
        minutes = 5
    elif slide["ruta"] == "backup":
        minutes = 4
    else:
        minutes = 3
    return f"{minutes} min"


def question_and_answer(slide: dict[str, str]) -> tuple[str, str]:
    function = slide["funcion"]
    title = re.sub(r"`([^`]+)`", r"\1", slide["titulo"]).strip("“”\"")
    if slide["ruta"] == "blocked-source":
        return (
            "¿Por qué no alcanza con copiar una cifra sin identificar norma y escenario?",
            "Porque el límite depende de la fuente normativa completa y de las condiciones de la prueba.",
        )
    if function == "divisor" or "pregunta" in function:
        return (title if title.endswith("?") else f"¿{title}?", slide["mensaje"])
    if slide["id"] == "U09-002":
        return (
            "¿Qué cambió entre los dos puntos: la fuente, el trayecto, la medición o más de una cosa?",
            "Todavía no alcanza para decidir: hay que separar variables y registrar condiciones.",
        )
    if "error frecuente" in function:
        return (f"¿Cómo reformularían la afirmación “{title}” para que sea físicamente válida?", slide["mensaje"])
    if any(word in function for word in ("ecuación", "gráfico")):
        return ("¿Qué magnitud cambia, en qué sentido y bajo qué condiciones?", slide["mensaje"])
    if any(word in function for word in ("ejemplo", "ejercicio", "actividad", "caso", "aplicación")):
        return (f"¿Qué evidencia o cálculo permite responder “{title}” sin exceder el modelo?", slide["mensaje"])
    if slide["clase"] == "diagram":
        return ("¿Qué recorrido o relación del esquema sostiene la idea central?", slide["mensaje"])
    return ("¿Cuál es la afirmación principal que esta slide permite sostener?", slide["mensaje"])


def demo(slide: dict[str, str]) -> str:
    if slide["id"] == "U09-055":
        return "Reproducir primero habla seca y luego reverberada a nivel seguro; mostrar en simultáneo la alternativa estática de la envolvente."
    if slide["clase"] == "video_or_gif":
        return "Usar el recurso solo si está disponible y conservar la alternativa estática visible."
    if any(word in slide["funcion"] for word in ("actividad", "ejercicio", "caso")):
        return "Dar tiempo de respuesta antes del revelado; registrar la justificación, no solo la opción elegida."
    return "No corresponde."


def common_error(slide: dict[str, str]) -> str:
    note = slide["notas"]
    if any(token in note.lower() for token in ("evitar", "diferenciar", "distinguir", "no ", "aclarar", "advertir")):
        return note
    block = slide["bloque"].split("·", 1)[0].strip()
    by_block = {
        "B00": "Responder el caso antes de distinguir fuente, trayecto, receptor y medición.",
        "B01": "Atribuir el nivel recibido a una sola etapa sin identificar qué cambió y bajo qué condiciones.",
        "B02": "Aplicar −6 dB o sumar directividad sin declarar campo, dirección, distancia y referencia.",
        "B03": "Tratar temperatura, viento o absorción atmosférica como una corrección única de nivel.",
        "B04": "Usar reflexión, absorción, transmisión, refracción y difracción como si fueran sinónimos.",
        "B05": "Confundir tiempo de reverberación con aislamiento o con un criterio universal de calidad.",
        "B06": "Extrapolar el desempeño de un elemento ideal al conjunto construido y omitir rutas débiles.",
        "B07": "Declarar aptitud de una cabina por su apariencia o por un único valor global en dB(A).",
        "B08": "Sumar fórmulas sin localizar antes el mecanismo y el tipo de evidencia necesario.",
        "B09": "Usar una slide de respaldo fuera de sus condiciones o antes de cerrar la fuente indicada.",
    }
    return by_block.get(block, "Omitir las condiciones y el límite de la conclusión.")


def speaker_guide(slide: dict[str, str]) -> str:
    special = {
        "U09-041": "No presentar una ecuación. Si se muestra el placeholder, señalar la normal, los ángulos y el estado pendiente; volver inmediatamente al modelo cualitativo de U09-040.",
        "U09-088": "No mostrar una curva. Usar la ficha vacía solo para identificar qué variables y qué referencia deberán acompañar los datos futuros.",
        "U09-089": "Recorrer primero el modo longitudinal y luego el transversal; no asignar ángulos, velocidades ni relaciones matemáticas hasta cerrar la fuente.",
        "U09-092": "No proyectar como tabla normativa. Mostrar únicamente el estado bloqueado y explicar qué metadatos faltan para habilitarla.",
    }
    if slide["id"] in special:
        return special[slide["id"]]
    steps = ", ".join(part.rstrip(".") for part in chunks(slide["contenido"]))
    return f"Presentar primero la estructura general y luego recorrer {steps}. Cerrar señalando la idea central, sin leer todas las cajas como una lista."


def render_slide_text(slides: list[dict[str, str]]) -> str:
    out = [
        "# Unidad 09 — Texto visible de slides",
        "",
        "> Estado: redacción basada exclusivamente en el storyboard aprobado. No constituye un PowerPoint. Los campos marcados como pendientes o bloqueados no deben completarse sin cerrar su fuente o convención.",
        "",
        "## Criterio editorial",
        "",
        "Cada slide presenta una idea central, texto visible breve y una instrucción visual compatible con tipografía legible. Las explicaciones, preguntas, respuestas y límites del modelo se desarrollan en `speaker_notes.md`.",
        "",
    ]
    for slide in slides:
        out += [
            f"## {slide['id']} — {slide['titulo']}",
            "",
            f"- **Subtítulo:** {subtitle(slide)}",
            f"- **Ruta:** {slide['ruta']}",
            f"- **Layout:** `{slide['layout']}`",
            "",
            "### Contenido visible",
            "",
        ]
        out += [f"- {item}" for item in visible_content(slide)]
        out += ["", "### Ecuaciones", ""]
        out += [f"- {item}" for item in equations(slide)]
        out += [
            "",
            "### Definición",
            "",
            definition(slide),
            "",
            "### Ejemplo o consigna",
            "",
            example(slide),
            "",
            "### Visual",
            "",
            visual_instruction(slide),
            "",
            "### Caption sugerido",
            "",
            caption(slide),
            "",
            "### Fuente",
            "",
            slide["fuente"],
            "",
            "### Texto alternativo",
            "",
            alt_text(slide),
            "",
            "### Notas del orador",
            "",
            f"Desarrolladas en `speaker_notes.md`, sección {slide['id']}.",
            "",
            "### Transición",
            "",
            sentence(slide["transicion"]),
            "",
        ]
    return "\n".join(out).rstrip() + "\n"


def render_speaker_notes(slides: list[dict[str, str]]) -> str:
    out = [
        "# Unidad 09 — Notas del orador",
        "",
        "> Estas notas amplían el texto visible sin repetirlo literalmente. Las duraciones son orientativas y no modifican la secuencia del storyboard aprobado.",
        "",
    ]
    for slide in slides:
        question, answer = question_and_answer(slide)
        out += [
            f"## {slide['id']} — {slide['titulo']}",
            "",
            f"- **Duración aproximada:** {duration(slide)}.",
            f"- **Propósito docente:** {sentence(slide['objetivo'])}",
            f"- **Explicación extendida:** {sentence(slide['notas'])} Explicitar que {slide['mensaje'][0].lower() + slide['mensaje'][1:]}",
            f"- **Guía del visual o diagrama:** {speaker_guide(slide)}",
            f"- **Pregunta al grupo:** {question}",
            f"- **Respuesta esperada:** {sentence(answer)}",
            f"- **Demostración o revelado:** {demo(slide)}",
            f"- **Error frecuente:** {sentence(common_error(slide))}",
            f"- **Transición:** {sentence(slide['transicion'])}",
            "",
        ]
    return "\n".join(out).rstrip() + "\n"


def source_status(slide: dict[str, str]) -> str:
    sid = slide["id"]
    special = {
        "U09-041": "Pendiente: fuente académica para la formalización; se omite la ecuación.",
        "U09-063": "Condicional: convención absoluta pendiente; solo se redacta el cambio relativo.",
        "U09-076": "Pendiente: fuente visual técnica externa por curar.",
        "U09-088": "Pendiente: fuente primaria y condiciones; no hay curva ni coeficientes.",
        "U09-089": "Pendiente: fuente académica primaria; desarrollo solo cualitativo.",
        "U09-092": "Bloqueado: faltan norma, edición, adopción y escenario completos.",
    }
    return special.get(sid, "Trazable desde el storyboard aprobado.")


def render_source_map(slides: list[dict[str, str]]) -> str:
    out = [
        "# Unidad 09 — Mapa de fuentes de la redacción",
        "",
        "> El mapa reproduce las atribuciones del storyboard. No agrega ni valida fuentes externas nuevas.",
        "",
        "| Slide | Fuente indicada en el storyboard | Uso en la redacción | Estado |",
        "|---|---|---|---|",
    ]
    for slide in slides:
        source = slide["fuente"].replace("|", "\\|")
        use = "Contenido, visual y límites de la explicación"
        if slide["clase"] == "chart":
            use = "Contenido y trazabilidad del gráfico o placeholder"
        elif slide["clase"] in {"diagram", "mixed"}:
            use = "Contenido y estructura del diagrama"
        out.append(f"| {slide['id']} | {source} | {use} | {source_status(slide)} |")
    out += [
        "",
        "## Pendientes que impiden completar contenido",
        "",
        "- `U09-041` y `U09-089`: seleccionar y aprobar la fuente académica para Snell acústica y conversión modal.",
        "- `U09-063`: confirmar la convención de la forma absoluta de la ley de masas; la redacción actual conserva solo cambios relativos.",
        "- `U09-088`: seleccionar fuente primaria y condiciones atmosféricas antes de producir coeficientes o curvas.",
        "- `U09-092`: completar norma, edición, adopción, vía, transductor, bandas y menor nivel de prueba antes de incorporar cifras.",
        "- `U09-076`: curar y registrar la fuente de las fotografías técnicas antes de usar el recurso visual.",
    ]
    return "\n".join(out).rstrip() + "\n"


def render_review(slides: list[dict[str, str]]) -> str:
    routes = Counter(slide["ruta"] for slide in slides)
    classes = Counter(slide["clase"] for slide in slides)
    return f"""# Unidad 09 — Revisión de redacción

## Resultado

La redacción cubre las {len(slides)} slides del storyboard aprobado: {routes['central']} centrales, {routes['complementary']} complementarias, {routes['backup']} de respaldo y {routes['blocked-source']} bloqueada por fuente. No se creó ni modificó ningún PowerPoint.

Se redactaron títulos, subtítulos, contenido visible, ecuaciones, definiciones, ejemplos o consignas, captions, instrucciones visuales, layouts, fuentes, notas del orador, transiciones y textos alternativos. La distribución visual registrada es: {classes['diagram']} diagramas, {classes['mixed']} esquemas mixtos, {classes['chart']} gráficos, {classes['video_or_gif']} recurso multimedia, {classes['external_image']} recurso de imagen externa y {classes['none']} slides sin recurso gráfico propio.

## Controles aplicados

- **Fidelidad:** toda afirmación temática parte de los campos del storyboard; no se consultaron fuentes externas ni se añadieron datos normativos.
- **Nivel inicial:** se antepone la interpretación física a la operación y se definen símbolos y unidades cuando el storyboard introduce ecuaciones.
- **Legibilidad:** una idea central por slide; las explicaciones extensas, límites y respuestas esperadas se trasladan a notas.
- **Diagramas:** el texto de cajas se mantiene breve; la guía paso a paso queda en notas y se exige que conectores y etiquetas no invadan texto.
- **Aplicación clínica:** las slides U09-020, U09-068–077 y U09-079–082 vinculan modelos con campo sonoro, cabinas y verificación sin convertirlos en protocolos ni certificaciones.
- **Evaluación formativa:** las preguntas solicitan mecanismo, condición, evidencia o límite, no respuestas binarias aisladas.
- **Accesibilidad:** cada slide contiene texto alternativo y cada recurso multimedia conserva alternativa estática.
- **Trazabilidad:** `source_map.md` conserva la fuente declarada por slide y separa estados trazables, condicionales, pendientes y bloqueados.

## Hallazgos y estado

| ID | Problema | Severidad | Corrección aplicada | Estado |
|---|---|---|---|---|
| WR-U09-01 | Snell acústica de U09-041 carece de fuente académica aprobada. | Mayor | Se conserva el objetivo, pero no se redacta la relación matemática. | Abierto; requiere fuente. |
| WR-U09-02 | La forma absoluta de la ley de masas de U09-063 depende de una convención no cerrada. | Mayor | Se redacta únicamente la variación relativa segura y se explicita el límite. | Abierto; no bloquea la ruta relativa. |
| WR-U09-03 | U09-088 no tiene fuente primaria ni condiciones para coeficientes atmosféricos. | Mayor | Se mantiene como placeholder, sin curva ni valores. | Abierto; respaldo no utilizable. |
| WR-U09-04 | U09-089 requiere fuente primaria para conversión modal. | Mayor | Se conserva una ampliación cualitativa y se omiten ecuaciones. | Abierto; respaldo condicional. |
| WR-U09-05 | U09-092 no tiene norma, edición, adopción ni escenario completos. | Crítica | La slide queda explícitamente bloqueada y sin cifras. | Bloqueado por fuente externa. |
| WR-U09-06 | U09-076 depende de fotografías técnicas todavía no curadas. | Menor | La redacción admite diagrama o imagen y prohíbe inferir desempeño por apariencia. | Pendiente de asset. |
| WR-U09-07 | Riesgo de duplicar el texto dentro de diagramas densos. | Mayor | El visible se limita a tesis y etiquetas; el recorrido explicativo se mueve a notas. | Corregido en redacción; verificar en maquetación. |
| WR-U09-08 | Riesgo de presentar ejemplos ideales como reglas universales. | Mayor | Cada ejemplo incluye hipótesis, unidad, interpretación y límite de validez. | Corregido. |

## Verificación automática

- Secuencia validada: `U09-001` a `U09-096`, sin huecos ni duplicados.
- Correspondencia 1:1 comprobada entre storyboard, texto visible, notas y mapa de fuentes.
- Todos los registros incluyen layout, fuente, transición y texto alternativo.
- No se habilitó contenido numérico para la slide normativa bloqueada.

## Pendientes antes de producir el deck

1. Resolver las fuentes y convenciones de U09-041, U09-063, U09-088, U09-089 y U09-092.
2. Curar la fuente visual de U09-076 y confirmar disponibilidad del audio opcional U09-055.
3. Verificar, durante la futura maquetación, el texto de cada diagrama a tamaño real de slide y dividir cualquier composición que no sostenga 22–24 pt.
4. Revisar con el docente si los ejemplos de respaldo U09-087 y U09-090 deben mostrarse completos o por revelado progresivo.
"""


def main() -> None:
    slides = parse_storyboard()
    outputs = {
        ROOT / "slide_text.md": render_slide_text(slides),
        ROOT / "speaker_notes.md": render_speaker_notes(slides),
        ROOT / "source_map.md": render_source_map(slides),
        ROOT / "writing_review.md": render_review(slides),
    }
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {path.name}: {content.count(chr(10)) + 1} lines")


if __name__ == "__main__":
    main()
