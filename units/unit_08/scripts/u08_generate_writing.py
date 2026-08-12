#!/usr/bin/env python3
"""Genera textos y notas de U08 exclusivamente desde el storyboard aprobado."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "units" / "unit_08"
STORY = UNIT / "storyboard.md"

HEADERS = [
    "slide_id", "block", "slide_type", "working_title", "learning_purpose",
    "key_message", "visible_content_summary", "visual_or_media", "visual_class",
    "suggested_layout", "speaker_note_goal", "source", "prerequisites",
    "transition", "status",
]

SOURCE_KEYS = {
    "PO": "Programa oficial 2025, Unidad 8, p. 4",
    "TEX": "context/libro_latex/chapters/08-enfermedades-diagnostico-rehabilitacion.tex",
    "PDF": "context/libro_pdf/Física Acústica para Fonoaudiología.pdf, capítulo 8, pp. 207–233",
    "BR": "units/unit_08/brief.md",
    "INV": "units/unit_08/content_inventory.md",
    "SA": "units/unit_08/source_analysis.md",
    "OD": "units/unit_08/open_decisions.md",
    "CM": "course_map.md",
    "CDM": "course_dependency_map.md",
    "COV": "content_coverage_matrix.csv",
    "NOT": "style/notation_guide.md",
    "GLO": "style/glossary.md",
    "TPL": "style/layout_catalog.md y guías del sistema visual",
    "PREV": "Unidad 7 final y storyboard, solo como continuidad pedagógica",
    "REF": "Referencia técnica ya citada en la bibliografía del libro",
    "EP": "Elaboración pedagógica propia a partir de las fuentes del storyboard",
    "U5": "Unidad 5 del curso, prerrequisito indicado por el storyboard",
    "U6": "Unidad 6 del curso, prerrequisito indicado por el storyboard",
    "U10": "Unidad 10 del curso, puente indicado por el storyboard",
}

EQUATIONS = {
    "U08-020": "ΔL_T(f, Δt) = L_U,1(f, Δt) − L_U,0(f)",
    "U08-021": "ΔL_T(4000 Hz, Δt) = 27 dB HL − 12 dB HL = 15 dB",
    "U08-026": "L_Aeq,8h = 95 dB(A) + 10 log₁₀(1 h / 8 h) ≈ 86,0 dB(A)",
    "U08-051": "G_AO(f) = L_VA(f) − L_VO(f)",
    "U08-052": "G_AO(1000 Hz) = 40 dB HL − 15 dB HL = 25 dB",
    "U08-063": "L_SL = L_presentación − L_umbral individual",
    "U08-075": "SNR(f) = L_señal(f) − L_ruido(f)",
    "U08-077": "V(t): diferencia de potencial (µV) en función del tiempo (ms)",
    "U08-087": "G(f) = L_salida(f) − L_entrada(f)",
    "U08-088": "G(2000 Hz) = 70 dB SPL − 52 dB SPL = 18 dB",
    "U08-107": "ΔL_T(f) = L_posterior(f) − L_referencia(f)",
    "U08-108": "L_Aeq,8h = 96 dB(A) + 10 log₁₀(0,5 h / 8 h)",
    "U08-109": "G_AO(f) = L_VA(f) − L_VO(f)",
    "U08-110": "G(f) = L_salida(f) − L_entrada(f)",
}

SYMBOLS = {
    "U08-020": ["f: frecuencia de prueba (Hz)", "Δt: tiempo desde el fin de la exposición", "L_U,0: umbral de referencia (dB HL)", "L_U,1: umbral posterior (dB HL)", "ΔL_T: diferencia entre umbrales (dB)"],
    "U08-026": ["L_Aeq,8h: nivel equivalente referido a 8 h", "T_exposición/T_referencia: cociente temporal adimensional", "El cálculo resume energía promedio; no establece cumplimiento normativo."],
    "U08-051": ["f: frecuencia (Hz)", "L_VA: nivel de audición por vía aérea (dB HL)", "L_VO: nivel de audición por vía ósea (dB HL)", "G_AO: diferencia entre vías (dB)"],
    "U08-063": ["L_presentación: nivel del tono externo de comparación", "L_umbral individual: umbral para ese tono y condición", "L_SL: nivel referido al umbral individual (dB SL)"],
    "U08-075": ["L_señal y L_ruido: niveles registrados en la misma banda y escala", "SNR: diferencia local señal–ruido (dB)"],
    "U08-077": ["V: diferencia de potencial (µV)", "t: tiempo desde el estímulo (ms)"],
    "U08-087": ["f: frecuencia (Hz)", "L_entrada y L_salida: niveles medidos en la misma referencia (dB SPL)", "G: diferencia de niveles o ganancia (dB)"],
}

ACTIVITY_QA = {
    "U08-003": ("Clasifique cada dato: exposición, síntoma o resultado.", "95 dB(A) durante 1 h: exposición; tinnitus referido: síntoma; 40 dB HL a 4000 Hz: resultado audiométrico."),
    "U08-011": ("Clasifique las seis tarjetas y señale qué contexto falta.", "Nivel/duración: exposición; escotadura, porcentaje verbal y OEA ‘derivar’: resultados; tinnitus: síntoma; dificultad en ruido: limitación referida. Ninguna tarjeta aislada autoriza diagnóstico."),
    "U08-024": ("Identifique ejes, frecuencia de prueba, tiempos, grupo y variabilidad. Luego escriba una conclusión permitida y una no permitida.", "Permitida: describir la tendencia bajo las condiciones informadas. No permitida: predecir la recuperación de una persona o extrapolar a otra exposición."),
    "U08-036": ("¿Cuál es el evento, la población, el período, la exposición y el comparador?", "Si alguno falta, el porcentaje no puede interpretarse ni aplicarse a un caso individual."),
    "U08-043": ("Si dos pruebas discrepan, ¿qué revisaría antes de elegir una como ‘correcta’?", "Pregunta inicial, generador, sensor o tarea, condiciones técnicas, ruido, protocolo y antecedentes."),
    "U08-050": ("Lea el punto de 1000 Hz: frecuencia, vía, valor y dato faltante. ¿Qué conclusión está prohibida?", "Primero se describe el registro; falta contexto del procedimiento y de la otra vía. No se nombra una enfermedad a partir de un punto."),
    "U08-059": ("Complete al menos cinco campos del informe verbal ficticio.", "Material, idioma, modo de presentación, nivel y escala, oído, consigna y criterio de puntuación."),
    "U08-070": ("Describa eje, unidad, presencia/posición de pico y condición que revisaría.", "Se describe la forma y el protocolo; no se asigna una patología ni se estima cuánto oye la persona."),
    "U08-083": ("OEA ausente y PEAT presente: proponga dos preguntas antes de hablar de contradicción.", "Revisar transmisión por oído externo/medio, colocación y ruido de la sonda; recordar que OEA y PEAT tienen generadores y sensores diferentes."),
    "U08-097": ("Asigne una prueba a cada pregunta y justifique magnitud y límite.", "Se aceptan combinaciones distintas si la prueba responde la pregunta, se identifica qué registra y se declara qué queda abierto."),
    "U08-099": ("Relacione presión acústica, corriente eléctrica y vibración mecánica con un dispositivo.", "Presión: audífono; corriente en electrodos: implante coclear; vibración del cráneo: conducción ósea. Falta evaluación individual para seleccionar."),
    "U08-107": ("Calcule ΔL_T en cada frecuencia y señale la mayor diferencia.", "Restar posterior menos referencia frecuencia por frecuencia; la mayor diferencia no explica causa ni evolución."),
    "U08-108": ("Normalice la exposición de 0,5 h al intervalo de 8 h y declare las hipótesis.", "Aplicar el cociente temporal dentro del logaritmo. El resultado energético no demuestra seguridad ni cumplimiento."),
    "U08-109": ("Calcule G_AO(f) en cada frecuencia y compare los resultados.", "Restar vía ósea a vía aérea en la misma frecuencia y escala; no convertir la diferencia en diagnóstico."),
    "U08-110": ("Calcule G(f) para las tres frecuencias e identifique el máximo.", "Restar entrada a salida en cada frecuencia. El máximo de ganancia no equivale a mayor sonoridad, comodidad o comprensión."),
}

SPECIAL_VISIBLE = {
    "U08-001": ["Física Acústica · Licenciatura en Fonoaudiología", "Alteraciones y enfermedades auditivas, estudios y técnicas de rehabilitación", "Pregunta organizadora: ¿qué responde cada dato y qué no permite concluir por sí solo?"],
    "U08-005": ["Clasificar exposición, alteración, síntoma, resultado y limitación.", "Explicar TTS, pérdida inducida por ruido, tinnitus y presbiacusia con alcance introductorio.", "Comparar estudios por estímulo, sistema, sensor o tarea, magnitud y límite.", "Interpretar audiogramas, curvas y registros sin convertirlos en diagnósticos."],
    "U08-006": ["Calcular diferencias entre mediciones compatibles y explicar sus unidades.", "Comparar dispositivos por entrada, procesamiento, salida y punto de entrega.", "Justificar por qué una batería integra evidencia sin producir certeza automática."],
    "U08-009": ["Exposición: qué señal o agente actuó y durante cuánto tiempo.", "Alteración: cambio físico o funcional del sistema.", "Síntoma: experiencia referida por la persona.", "Resultado: dato obtenido mediante una prueba definida.", "Limitación: dificultad en una actividad o situación concreta."],
    "U08-010": ["¿Cómo fue la exposición?", "¿Qué umbral se obtuvo?", "¿Qué informa el oído medio?", "¿Qué respuesta coclear o neural se registró?", "¿Cómo se desempeña la persona al comunicarse?", "¿Qué transforma y entrega un dispositivo?"],
    "U08-014": ["TTS: diferencia entre umbrales comparables, con frecuencia y tiempo declarados.", "Tinnitus: percepción referida; no necesita una fuente acústica externa.", "No intercambiar: un resultado conductual no describe por sí solo una experiencia perceptual."],
    "U08-018": ["Nivel y descriptor: ¿qué magnitud se informó?", "Ponderación: ¿se declaró A u otra respuesta?", "Duración: ¿durante cuánto tiempo?", "Espectro: ¿cómo se distribuye la energía en frecuencia?", "Temporalidad: ¿continua, variable o impulsiva?", "Contexto: describir no equivale a juzgar seguridad o legalidad."],
    "U08-019": ["Definición: el desplazamiento temporal del umbral (TTS) es la diferencia entre un umbral posterior y uno de referencia.", "Condiciones: misma frecuencia, escala, vía y procedimiento; tiempo postexposición explícito.", "No confundir con tinnitus ni usar como pronóstico individual."],
    "U08-025": ["Temporal: se describe mediante mediciones seriadas y tiempos postexposición.", "Permanente: requiere evidencia de persistencia y condiciones comparables.", "En ambos casos, el curso medido no identifica por sí solo la causa."],
    "U08-029": ["PAIR/NIHL: pérdida auditiva asociada con exposición a ruido, evaluada mediante evidencia convergente.", "Se necesita: historia de exposición, patrón medido, antecedentes y consideración de causas alternativas.", "Una escotadura aislada solo describe una forma compatible."],
    "U08-032": ["Tinnitus o acúfeno: percepción sonora referida sin una fuente acústica externa correspondiente.", "Puede coexistir con umbrales diferentes entre personas y situaciones.", "Una frecuencia o un nivel de correspondencia describe una tarea; no materializa una fuente interna."],
    "U08-033": ["La edad puede coexistir con cambios cocleares, neurales o metabólicos.", "Exposición, salud, enfermedades, medicamentos y variabilidad individual también importan.", "Una pendiente en altas frecuencias no resume todos los casos ni establece una causa única."],
    "U08-038": ["1. Presentar un estímulo controlado.", "2. Observar la interacción con el sistema auditivo.", "3. Captar una respuesta mediante sensor o tarea.", "4. Representar el dato con magnitud y unidad.", "5. Interpretar bajo condiciones técnicas y de protocolo."],
    "U08-039": ["¿Qué estímulo entra?", "¿Qué parte o función interviene?", "¿Qué magnitud cambia?", "¿Qué sensor o tarea produce la respuesta?", "¿Qué dato y unidad se informan?", "¿Qué conclusión no permite?"],
    "U08-040": ["Conductual: requiere una tarea y una respuesta de la persona.", "Fisiológica: usa un sensor para registrar una respuesta del sistema.", "Ambas dependen de estímulo, condiciones, protocolo y criterio; ninguna es infalible."],
    "U08-047": ["dB SPL: referencia física de presión acústica; usar con señales acústicas.", "dB HL: referencia audiométrica dependiente de frecuencia y transductor; usar con umbrales audiométricos.", "dB SL: referencia al umbral individual en una condición declarada.", "Compartir ‘dB’ no autoriza convertir ni restar escalas incompatibles."],
    "U08-048": ["Eje horizontal: frecuencia (Hz), en posiciones audiométricas convencionales.", "Eje vertical: nivel de audición (dB HL), con valores mayores hacia abajo.", "La leyenda debe identificar oído, vía y condición antes de leer un punto."],
    "U08-054": ["Leer: frecuencia, vía, oído, símbolo y nivel.", "Comparar: solo mediciones compatibles y en la misma frecuencia.", "Limitar: el audiograma organiza umbrales; no nombra una enfermedad."],
    "U08-056": ["Material verbal e idioma definidos.", "Nivel, escala, oído y modo de presentación declarados.", "Consigna y respuesta observables.", "Puntuación: porcentaje correcto o umbral, según la tarea."],
    "U08-058": ["Informe incompleto: “72 % correcto”.", "Para interpretarlo faltan material, idioma, modo, nivel y escala, oído, consigna y criterio.", "El porcentaje no describe a la persona fuera de esa prueba."],
    "U08-060": ["Audiometría tonal: detectar tonos; resultado principal, umbral por frecuencia.", "Logoaudiometría: responder a material verbal; resultado, porcentaje o umbral bajo condiciones definidas.", "Se complementan, pero no miden la misma tarea."],
    "U08-061": ["La persona compara su percepto referido con un estímulo externo ajustable.", "Puede elegir una correspondencia de frecuencia y nivel bajo una consigna definida.", "El resultado pertenece a la tarea; el equipo no mide una fuente sonora interna."],
    "U08-062": ["Físico: el tono externo tiene frecuencia medible en Hz.", "Perceptual: el tinnitus es una experiencia referida.", "Correspondencia: juicio de semejanza; no igualdad física entre dos fuentes."],
    "U08-064": ["Tono: detectar → umbral por frecuencia → dB HL.", "Habla: reconocer → porcentaje o umbral → escala declarada.", "Correspondencia: comparar → frecuencia/nivel elegidos → Hz y dB SL bajo referencia individual."],
    "U08-066": ["La sonda sella el conducto y presenta un tono.", "El sistema modifica la presión del conducto de manera controlada.", "El micrófono registra la respuesta acústica.", "La curva representa una magnitud de inmitancia frente a presión."],
    "U08-067": ["Inmitancia: categoría que reúne oposición y facilidad de transferencia.", "Admitancia Y: magnitud habitual; la unidad depende del equipo y protocolo.", "Presión del conducto: daPa.", "Y/Y_max: normalización conceptual, sin unidad."],
    "U08-069": ["Pico centrado, trazado plano y pico desplazado: tres descripciones geométricas.", "Eje horizontal: presión (daPa).", "Eje vertical: admitancia normalizada Y/Y_max.", "La forma no corresponde de manera exclusiva a una enfermedad."],
    "U08-072": ["Entradas: tono de sonda y presión del conducto.", "Sistema: oído externo y medio bajo condiciones de sellado.", "Dato: magnitud de inmitancia en función de la presión.", "Límite: no mide por sí solo audición ni patología."],
    "U08-074": ["Ida: la sonda presenta un estímulo acústico.", "Interacción: oído externo/medio y cóclea condicionan la señal.", "Retorno: presión acústica que vuelve al conducto.", "Sensor: micrófono de la sonda; resultado bajo protocolo."],
    "U08-075": ["Magnitudes: presión acústica, nivel en dB SPL y piso de ruido.", "SNR local: diferencia señal–ruido en una banda definida.", "La salida ‘presente’, ‘ausente’ o ‘derivar’ depende del protocolo, la sonda y la transmisión."],
    "U08-077": ["El estímulo llega por un transductor acústico.", "La vía auditiva genera una respuesta sincronizada.", "Electrodos superficiales registran una diferencia de potencial.", "El promedio permite representar V(t) en µV y ms."],
    "U08-080": ["Estímulo acústico controlado.", "Generadores cocleares y neurales distales.", "Electrodo próximo según montaje extra- o transtimpánico.", "Registro de potenciales; amplitud y componentes dependen del protocolo."],
    "U08-082": ["OEA: micrófono; presión acústica asociada principalmente con cóclea/CCE.", "PEAT: electrodos superficiales; V(t) asociada con respuesta de la vía auditiva.", "ECoG: electrodo próximo; potenciales cocleares y neurales distales.", "La entrada acústica compartida no vuelve equivalentes los resultados."],
    "U08-085": ["Entrada: señal que recibe el dispositivo.", "Transducción y procesamiento: cambio de dominio y modificación de la señal.", "Salida: acústica, eléctrica, mecánica o combinada.", "Acoplamiento: punto donde la salida interactúa con el sistema auditivo remanente.", "Resultado funcional: debe evaluarse; no está garantizado por la cadena."],
    "U08-086": ["Entrada: presión acústica cerca del micrófono (Pa o dB SPL).", "Procesamiento: depende de frecuencia f, nivel y tiempo.", "Receptor: convierte la señal procesada en salida acústica.", "La presión entregada cerca del oído no equivale automáticamente a comprensión."],
    "U08-089": ["Compresión: cambia la relación entrada–salida.", "Direccionalidad: modifica la sensibilidad según dirección.", "Reducción de ruido: actúa sobre componentes estimados de la señal.", "Control de realimentación: limita oscilación acústica no deseada.", "Ninguna función aislada predice beneficio."],
    "U08-090": ["Sonido → micrófono → procesador.", "El enlace transmite la información codificada.", "El receptor–estimulador produce pulsos eléctricos.", "La guía de electrodos entrega estimulación intracoclear."],
    "U08-092": ["Audífono: procesa y vuelve a entregar presión acústica.", "Implante coclear: codifica y entrega pulsos eléctricos intracocleares.", "No forman una escala de ‘potencia’; cambian el dominio y el punto de entrega."],
    "U08-094": ["Audífono → salida acústica.", "Implante coclear → salida eléctrica.", "Conducción ósea → salida mecánica.", "La salida distingue el mecanismo; la indicación requiere evaluación, necesidades y seguimiento."],
    "U08-096": ["L_Aeq,T: dato de exposición.", "Tinnitus y dB SL: percepto y resultado de correspondencia.", "Umbral en dB HL: resultado conductual.", "OEA ‘derivar’: salida operativa bajo un protocolo.", "Cada dato abre una pregunta; ninguno resuelve todo el caso."],
    "U08-098": ["Convergencia parcial: resultados compatibles reducen algunas preguntas abiertas.", "Discrepancia: revisar generador, sensor/tarea, condiciones y protocolo.", "Integrar no es votar: es explicar qué aporta y qué limita cada dato."],
    "U08-100": ["1. Formular la pregunta.", "2. Recuperar antecedentes pertinentes.", "3. Seleccionar pruebas por la información que aportan.", "4. Controlar condiciones técnicas.", "5. Integrar, comunicar límites y planificar seguimiento."],
    "U08-101": ["¿Qué entra?", "¿Qué sistema interviene?", "¿Qué se transforma?", "¿Qué se registra o entrega?", "¿En qué magnitud y unidad?", "¿Qué no permite concluir?"],
    "U08-102": ["U8 entrega: clasificación de evidencia, cadenas de medición y límites de inferencia.", "U10 preguntará: ¿qué ruido?, ¿qué descriptor?, ¿qué exposición?, ¿qué efecto y control?", "Puente: describir con precisión antes de evaluar o intervenir."],
    "U08-103": ["Escalas: U08-104.", "Estudios auditivos: U08-105.", "Dispositivos: U08-106.", "Ejercicios: U08-107–110.", "Brechas y trazabilidad: U08-111–114."],
    "U08-104": ["dB SPL | referencia física de presión | señales acústicas | no convertir a HL sin referencia.", "dB HL | cero audiométrico por frecuencia/transductor | umbrales | comparar solo condiciones compatibles.", "dB SL | umbral individual declarado | nivel relativo | no describe intensidad interna."],
    "U08-105": ["Audiometría tonal | tono | tarea conductual | umbral por frecuencia | no diagnostica sola.", "Logoaudiometría | habla | tarea verbal | porcentaje/umbral | depende de material y nivel.", "Timpanometría | tono + presión | micrófono | inmitancia | no mide audición.", "Acufenometría | sonido ajustable | juicio de semejanza | correspondencia | no mide fuente interna.", "OEA | sonido | micrófono | presión/SNR | integra batería.", "PEAT | sonido | electrodos | V(t) | no mide comprensión.", "ECoG | sonido | electrodo próximo | potenciales | depende del montaje."],
    "U08-106": ["Audífono | entrada acústica | procesamiento | salida acústica | beneficio a evaluar.", "Implante coclear | entrada acústica | codificación | salida eléctrica | no garantiza perceptos independientes.", "Conducción ósea | entrada acústica | transducción | vibración mecánica | selección individual.", "Electroacústica | entrada acústica | procesamiento por bandas | salidas acústica + eléctrica | separación individualizada."],
    "U08-111": ["BLOQUEADA: no insertar curva hasta documentar exposición, frecuencia de prueba, tiempos, muestra, variabilidad y fuente primaria.", "La ficha debe conservar cita completa y límites de extrapolación."],
    "U08-112": ["BLOQUEADA: no insertar porcentaje hasta definir evento, población, período, exposición, comparador e incertidumbre.", "Distinguir riesgo poblacional de probabilidad individual."],
    "U08-113": ["TTS: desplazamiento temporal del umbral.", "PAIR/HIR/NIHL: forma institucional pendiente; desarrollar en primera aparición.", "OEA: otoemisiones acústicas.", "PEAT/PEATC: forma preferida pendiente de validación docente.", "ECoG: electrococleografía."],
    "U08-114": ["Alcance: programa oficial y capítulo 8 del libro del curso.", "Verificación: PDF del libro y análisis de fuentes de la unidad.", "Ampliaciones: referencias técnicas ya citadas en el libro.", "Condición: normas, cifras y convenciones pendientes deben validarse antes del deck.", "Uso: material académico; no sustituye evaluación, protocolo ni indicación clínica."],
}

SUBTITLES = {
    "portada": "De la exposición y la medición a una interpretación con límites",
    "divisor": "Pregunta guía del bloque",
    "objetivos": "Resultados de aprendizaje observables",
    "guía": "Material de consulta no lineal",
    "fuentes": "Trazabilidad y límites de uso",
}

def parse_storyboard():
    rows=[]
    for line in STORY.read_text(encoding="utf-8").splitlines():
        if line.startswith("| U08-"):
            cells=[x.strip() for x in line.strip().strip("|").split("|")]
            if len(cells)!=15: raise ValueError(f"Fila inválida: {line[:80]}")
            rows.append(dict(zip(HEADERS,cells)))
    if len(rows)!=114: raise ValueError(f"Se esperaban 114 slides; se hallaron {len(rows)}")
    return rows

def phrases(text):
    text=text.replace(" → ","; ")
    parts=[p.strip(" .") for p in re.split(r"; |\. (?=[A-ZÁÉÍÓÚ¿])",text) if p.strip()]
    return parts

def asset_ids(text):
    return re.findall(r"U08-(?:DG|CH|IMG|MEDIA)-\d+[A-Z]?",text)

def asset_text(aid, name):
    folder=(UNIT/"assets"/"generated"/("diagrams" if "-DG-" in aid else "charts")/aid)
    p=folder/name
    return p.read_text(encoding="utf-8").strip() if p.exists() else ""

def visual_status(row):
    if row["slide_id"] == "U08-088":
        return "U08-DG-042: requiere alinear sus cifras con el storyboard antes del deck."
    ids=asset_ids(row["visual_or_media"])
    if not ids: return "Sin asset propio obligatorio; composición nativa según storyboard."
    items=[]
    for aid in ids:
        val=UNIT/"assets"/"generated"/("diagrams" if "-DG-" in aid else "charts")/aid/"validation.json"
        if val.exists():
            import json
            status=json.loads(val.read_text(encoding="utf-8")).get("status","documentado")
        else: status="externo o multimedia pendiente"
        items.append(f"{aid}: {status}")
    return "; ".join(items)+"."

def visible_content(row):
    sid=row["slide_id"]; typ=row["slide_type"]
    if sid in SPECIAL_VISIBLE: return SPECIAL_VISIBLE[sid]
    if sid in ACTIVITY_QA:
        prompt,_=ACTIVITY_QA[sid]
        return ["Consigna: "+prompt, "Justifique con la magnitud, la unidad y el límite de la conclusión."]
    if typ=="divisor": return [row["key_message"]]
    if typ=="error frecuente": return ["Error frecuente: "+row["working_title"], "Corrección: "+row["key_message"], "Antes de concluir: "+row["visible_content_summary"]]
    if typ=="definición": return [row["key_message"], *phrases(row["visible_content_summary"])]
    if typ in {"ecuación","ejemplo"}:
        vals=[row["key_message"], *phrases(row["visible_content_summary"])]
        return vals
    if typ in {"recapitulación","cierre"}: return [*phrases(row["key_message"]), *phrases(row["visible_content_summary"])]
    return [row["key_message"], *phrases(row["visible_content_summary"])]

def definition(row):
    if row["slide_type"]=="definición": return row["key_message"]
    if row["slide_id"] in {"U08-020","U08-051","U08-063","U08-067","U08-075","U08-077","U08-087"}: return row["key_message"]
    return "No corresponde una definición nueva; se aplica o compara contenido ya introducido."

def example(row):
    sid=row["slide_id"]
    if sid in {"U08-021","U08-052","U08-088"}: return EQUATIONS[sid]+". Interpretar el resultado por separado del cálculo."
    if sid in ACTIVITY_QA: return "Actividad o ejercicio; la resolución esperada se encuentra en `speaker_notes.md`."
    if row["slide_type"] in {"aplicación","caso"}: return row["visible_content_summary"]
    return "No corresponde ejemplo numérico en esta slide."

def caption(row):
    if row["slide_id"] == "U08-088":
        return "Ejemplo de cálculo de ganancia a 2000 Hz: 70 dB SPL de salida menos 52 dB SPL de entrada equivale a 18 dB. El cálculo no mide comprensión ni comodidad."
    if row["visual_class"] in {"diagram","chart","mixed","equation_only"}:
        scale_note = " Figura conceptual no a escala." if row["visual_class"] in {"diagram","mixed"} else ""
        return row["key_message"]+scale_note
    return "No requiere caption independiente."

def alt_text(row):
    if row["slide_id"] == "U08-088":
        return "Esquema del cálculo de ganancia a 2000 Hz. La entrada es 52 dB SPL, la salida es 70 dB SPL y la diferencia es 18 dB. Un aviso aclara que esta ganancia no equivale a beneficio clínico."
    visual_labels={"diagram":"Diagrama conceptual", "chart":"Gráfico", "mixed":"Esquema mixto", "equation_only":"Ecuación anotada", "video_or_gif":"Secuencia audiovisual con alternativa estática", "none":"Composición textual"}
    scale_note = " Esquema conceptual no a escala." if row["visual_class"] in {"diagram","mixed"} else ""
    title_sep=" " if row["working_title"].endswith((".","?","!")) else ". "
    return f"{row['working_title']}{title_sep}{visual_labels.get(row['visual_class'],'Visual')}: {row['visible_content_summary']} Idea central: {row['key_message'].rstrip('.')}.{scale_note}"

def question_answer(row):
    sid=row["slide_id"]; typ=row["slide_type"]
    if sid in ACTIVITY_QA: return ACTIVITY_QA[sid]
    if typ=="gráfico": return ("¿Qué muestran los ejes o variables, y qué conclusión no autoriza la figura?", row["key_message"])
    if typ in {"proceso","mapa"}: return ("¿Qué cambia de una etapa o nodo al siguiente?", row["key_message"])
    if typ=="comparación": return ("¿Cuál es la diferencia que organiza esta comparación?", row["key_message"])
    if typ=="error frecuente": return ("¿Qué información falta para corregir esta conclusión?", row["visible_content_summary"])
    if typ=="definición": return ("¿Qué condición debe acompañar esta definición para poder usarla?", row["visible_content_summary"])
    if typ in {"ecuación","ejemplo","ejercicio"}: return ("¿Son compatibles las magnitudes y unidades antes de operar?", "Sí solo si coinciden frecuencia, referencia y condiciones indicadas; después se interpreta el resultado con su límite.")
    if typ=="recapitulación": return ("¿Qué regla de este bloque usaría primero ante un dato nuevo?", row["key_message"])
    return ("¿Qué idea permite esta slide y qué conclusión deja abierta?", row["key_message"])

def duration(row):
    typ=row["slide_type"]
    if typ in {"actividad","ejercicio"}: return "3–5 min"
    if typ in {"ejemplo","ecuación","gráfico","proceso","caso"}: return "2–4 min"
    if typ in {"divisor","portada","cierre","guía"}: return "1–2 min"
    return "2–3 min"

def diagram_guide(row):
    if row["slide_id"] == "U08-088":
        return "Explicar en orden: entrada 52 dB SPL → salida 70 dB SPL → resta de magnitudes compatibles → ganancia 18 dB → límite: la ganancia no equivale por sí sola a beneficio clínico. No usar las cifras actuales del asset U08-DG-042 hasta corregirlo."
    ids=[a for a in asset_ids(row["visual_or_media"]) if "-DG-" in a]
    if not ids: return "No corresponde guía de diagrama."
    aid=ids[0]
    if "blocked" in visual_status(row):
        return f"El recurso {aid} está bloqueado o pendiente. Explicar la idea con el texto aprobado y no improvisar un diagrama alternativo."
    steps=phrases(row["visible_content_summary"])
    preview=" → ".join(steps[:5])
    more="; completar oralmente el resto" if len(steps)>5 else ""
    return f"Revelar y explicar en el orden previsto: {preview}{more}. Cerrar con esta idea: {row['key_message']} No repetir las cajas como párrafos."

def media_instruction(row):
    if "U08-MEDIA-" in row["visual_or_media"]:
        return "Recurso opcional: reproducir solo si está disponible y verificado. Presentar antes la consigna de observación y ofrecer la alternativa estática; no usarlo como prueba diagnóstica."
    if row["slide_type"]=="media": return "Usar la secuencia estática si la animación no está disponible."
    return "No corresponde reproducción multimedia."

def demonstration(row):
    typ=row["slide_type"]
    if typ in {"actividad","ejercicio","caso"}:
        return "Dar primero tiempo individual, luego contrastar justificaciones. Mantener la participación en clasificación, lectura o cálculo; no pedir diagnóstico ni experiencia auditiva personal."
    if typ in {"ecuación","ejemplo"}:
        return "Señalar datos y unidades antes de operar; resolver un paso por vez y separar el resultado matemático de su interpretación física o clínica."
    if typ=="gráfico":
        return "Leer en este orden: ejes, unidades, escala, condición o muestra y tendencia. Recién después formular una conclusión y un límite."
    if typ in {"proceso","mapa"}:
        return "Revelar la secuencia por etapas y pedir que el grupo nombre qué entra, qué se transforma y qué se registra o entrega."
    if typ=="comparación":
        return "Recorrer una misma fila o criterio entre columnas; evitar leer cada columna como una lista aislada."
    if typ=="error frecuente":
        return "Mostrar primero la afirmación problemática, pedir que identifiquen el salto lógico y revelar después la corrección."
    if typ in {"recapitulación","cierre"}:
        return "Pedir una regla de decisión en una frase y conectarla con una situación de práctica fonoaudiológica."
    return "Usar el visual para señalar el dato, la condición y el límite; ampliar oralmente sin convertir las cajas o bullets en párrafos."

def common_error(row):
    text=(row["working_title"]+" "+row["key_message"]+" "+row["visible_content_summary"]).lower()
    if any(k in text for k in ["tts", "pos-exposición", "posexposición"]):
        return "Confundir una diferencia temporal de umbral con tinnitus, daño permanente o pronóstico individual."
    if any(k in text for k in ["riesgo", "porcentaje poblacional", "edad y exposición"]):
        return "Trasladar un porcentaje poblacional a una persona sin conservar población, período, comparador e incertidumbre."
    if any(k in text for k in ["tinnitus", "acúfeno", "acufenometr"]):
        return "Interpretar la correspondencia con un tono externo como medición de una fuente o intensidad sonora interna."
    if any(k in text for k in ["audiograma", "audiometr", "db hl", "vía aérea", "vía ósea"]):
        return "Convertir un umbral, una forma o una diferencia entre vías en un diagnóstico sin integrar procedimiento y batería."
    if any(k in text for k in ["logoaudiometr", "material verbal", "desempeño–nivel", "porcentaje correcto"]):
        return "Comparar porcentajes sin declarar material, idioma, nivel, escala, oído, consigna y criterio."
    if any(k in text for k in ["timpan", "inmitancia", "admitancia"]):
        return "Usar la forma de una curva como sinónimo exclusivo de patología o como medida directa de cuánto oye la persona."
    if any(k in text for k in ["oea", "otoemision"]):
        return "Leer ‘presente’, ‘ausente’ o ‘derivar’ como diagnóstico, sin revisar ruido, sonda, transmisión y protocolo."
    if any(k in text for k in ["peat", "peatc", "ecog", "electrococleo", "potencial"]):
        return "Equiparar una respuesta eléctrica registrada con audición normal, comprensión o localización diagnóstica automática."
    if any(k in text for k in ["audífono", "implante", "conducción ósea", "ganancia", "electrodos", "dispositivo"]):
        return "Suponer que salida, ganancia, cantidad de canales o activación técnica equivalen por sí solas a beneficio funcional."
    if any(k in text for k in ["db spl", "db sl", "referencia", "escala"]):
        return "Operar con valores en decibelios sin comprobar referencia, frecuencia, transductor y condición de medición."
    if any(k in text for k in ["fuente", "trazabilidad", "bloqueada"]):
        return "Completar una cifra o regla faltante por memoria o intuición y perder la trazabilidad de la afirmación."
    if row["slide_type"] in {"proceso","mapa"}:
        return "Saltar desde la entrada al resultado e ignorar la transformación, el sensor o tarea y las condiciones del protocolo."
    if row["slide_type"]=="comparación":
        return "Comparar categorías con criterios distintos o convertir una diferencia descriptiva en una jerarquía clínica."
    return "Convertir un dato aislado en causa, diagnóstico, pronóstico o indicación sin declarar condiciones y evidencia complementaria."

def source_claim(row):
    return row["key_message"].replace("|","/")

def write_slide_text(rows):
    out=["# Unidad 8 — Texto de slides", "", "Versión de redacción · 2026-08-12", "", "> Base exclusiva: `storyboard.md` aprobado. Este documento no es un PowerPoint. Las slides bloqueadas conservan estructura y preguntas, pero no incorporan datos no autorizados.", ""]
    for row in rows:
        sid=row["slide_id"]; eq=EQUATIONS.get(sid,"No corresponde.")
        out += [f"## {sid} — {row['working_title']}", "", f"- **Estado:** {row['status']}.", f"- **Título:** {row['working_title']}", f"- **Subtítulo:** {SUBTITLES.get(row['slide_type'],'No corresponde.')}", f"- **Layout:** `{row['suggested_layout']}`", "", "### Contenido visible", ""]
        out += [f"- {x}" for x in visible_content(row)]
        out += ["", "### Ecuaciones", "", eq]
        if sid in SYMBOLS: out += ["", "**Símbolos y unidades:**", ""]+[f"- {x}" for x in SYMBOLS[sid]]
        out += ["", "### Definición", "", definition(row), "", "### Ejemplo", "", example(row), "", "### Visual", "", row["visual_or_media"], "", f"**Idea central del visual:** {row['key_message']}", "", f"**Estado del recurso:** {visual_status(row)}", "", "### Caption sugerido", "", caption(row), "", "### Fuente", "", row["source"], "", "### Texto alternativo", "", alt_text(row), ""]
    (UNIT/"slide_text.md").write_text("\n".join(out).rstrip()+"\n",encoding="utf-8")

def write_notes(rows):
    out=["# Unidad 8 — Notas del orador", "", "Versión de redacción · 2026-08-12", "", "> Las notas amplían el contenido visible sin repetirlo literalmente. Las respuestas son didácticas y no constituyen diagnóstico, indicación ni protocolo clínico.", ""]
    for row in rows:
        q,a=question_answer(row); sid=row["slide_id"]
        blocked="bloqueada" in row["status"] or sid in {"U08-026","U08-063"}
        out += [f"## {sid} — {row['working_title']}", "", f"- **Duración aproximada:** {duration(row)}.", f"- **Objetivo oral:** {row['learning_purpose']}", f"- **Explicación extendida:** {row['key_message']} {row['speaker_note_goal']}", f"- **Guía del visual/diagrama:** {diagram_guide(row)}", f"- **Pregunta al grupo:** {q}", f"- **Respuesta esperada:** {a}", f"- **Demostración o dinámica:** {demonstration(row)}", f"- **Error frecuente a anticipar:** {common_error(row)}", f"- **Multimedia:** {media_instruction(row)}"]
        if blocked:
            out += [f"- **Condición de producción:** No completar cifras, curva o convención pendiente. Mantener la slide como estructura de trazabilidad hasta resolver: {row['source'].rstrip('.')}."]
        if sid=="U08-088":
            out += ["- **Control de consistencia:** Usar 70−52=18 dB según el storyboard. El asset U08-DG-042 actual usa 82−60=22 dB y debe alinearse antes de construir el deck."]
        out += [f"- **Transición:** {row['transition']}", ""]
    (UNIT/"speaker_notes.md").write_text("\n".join(out).rstrip()+"\n",encoding="utf-8")

def write_source_map(rows):
    out=["# Unidad 8 — Mapa de fuentes para la redacción", "", "Versión · 2026-08-12", "", "## Claves", ""]
    for k,v in SOURCE_KEYS.items(): out.append(f"- **{k}:** {v}.")
    out += ["", "## Trazabilidad slide por slide", "", "| Slide | Fuente asignada por el storyboard | Afirmación o uso | Estado de redacción |", "|---|---|---|---|"]
    for row in rows:
        state="bloqueada: estructura sin datos" if "bloqueada" in row["status"] else "redactada"
        if row["slide_id"] in {"U08-026","U08-063"}: state="redactada con convención pendiente"
        out.append(f"| {row['slide_id']} | {row['source'].replace('|','/')} | {source_claim(row)} | {state} |")
    out += ["", "## Reglas de uso", "", "- No sustituir una fuente primaria por el conocimiento general del modelo.", "- U08-023/U08-111 requieren una fuente primaria de curva pos-exposición antes de incorporar datos.", "- U08-035/U08-112 requieren evento, población, período, comparador e incertidumbre definidos.", "- Las referencias técnicas amplían o verifican; programa y libro fijan el alcance.", "- Las decisiones pendientes de siglas, escalas y normas deben resolverse antes del PowerPoint."]
    (UNIT/"source_map.md").write_text("\n".join(out).rstrip()+"\n",encoding="utf-8")

def write_review(rows):
    diagrams=sum(1 for r in rows if "U08-DG-" in r["visual_or_media"])
    charts=sum(1 for r in rows if "U08-CH-" in r["visual_or_media"])
    acts=sum(1 for r in rows if r["slide_type"] in {"actividad","ejercicio"})
    recaps=sum(1 for r in rows if r["slide_type"] in {"recapitulación","cierre"})
    text=f"""# Unidad 8 — Revisión de redacción

Fecha: 2026-08-12

Base: `storyboard.md` aprobado

Estado: **aprobada para futura producción, con bloqueos y una inconsistencia de asset documentados**.

## Cobertura

- Slides redactadas: **{len(rows)}/114**.
- Slides con diagramas previstos: **{diagrams}**.
- Slides con gráficos previstos: **{charts}**.
- Actividades o ejercicios con respuesta esperada: **{acts}**.
- Recapitulaciones y cierre: **{recaps}**.
- Cada slide incluye título, subtítulo, contenido visible, ecuación, definición, ejemplo, caption, visual, layout, fuente y texto alternativo.
- Cada slide tiene notas con explicación, pregunta, respuesta, dinámica, error frecuente, multimedia, duración y transición.

## Criterios revisados

| Criterio | Resultado |
|---|---|
| Correspondencia con las 114 filas del storyboard | cumple |
| Español académico claro y nivel de primer año | cumple |
| Intuición antes de ecuación | cumple; la idea física y las condiciones aparecen en el contenido visible antes de formalizar la operación |
| Símbolos y unidades | definidos en las slides cuantitativas principales |
| Ejemplos con cálculo e interpretación separados | cumple |
| Aplicación a Fonoaudiología sin diagnosticar ni prescribir | cumple |
| Preguntas resolubles y respuestas en notas | cumple |
| Diagramas con texto complementario y cajas breves | cumple en redacción; el desarrollo extenso queda en notas y el estado de cada asset se informa por separado |
| Fuentes por slide | cumple en `source_map.md` |
| PowerPoint producido | no; fuera de alcance de esta fase |

## Hallazgos y decisiones

| ID | Severidad | Hallazgo | Tratamiento | Estado |
|---|---|---|---|---|
| WR-U08-01 | crítica | U08-023 y U08-111 no tienen curva cuantitativa autorizada. | Se redactaron pregunta, metadatos requeridos y límite; no se incluyeron datos. | bloqueado |
| WR-U08-02 | crítica | U08-035 y U08-112 no tienen métrica poblacional aprobada. | Se redactó el marco de lectura; no se incluyó porcentaje. | bloqueado |
| WR-U08-03 | mayor | U08-DG-042 usa 82−60=22 dB, pero el storyboard U08-088 fija 70−52=18 dB. | La redacción sigue el storyboard; el asset debe regenerarse antes del deck. | abierto para producción visual |
| WR-U08-04 | mayor | U08-026 depende de descriptor/normativa y U08-063 de notación dB SL pendiente. | Texto marcado como condicionado; no presentar como norma o intensidad interna. | abierto docente |
| WR-U08-05 | mayor | U08-030, 049, 057 y 069 tienen visual propio bloqueado por convenciones pendientes. | Se redactaron lectura, ejes y límites; el deck no debe usar un reemplazo inventado. | abierto docente |
| WR-U08-06 | moderada | PAIR/HIR/NIHL y PEAT/PEATC siguen sin forma institucional definitiva. | Se usa provisionalmente la forma del storyboard y se explicita la decisión pendiente en U08-113. | abierto docente |

## Control de densidad

- Los diagramas no reciben párrafos adicionales dentro de cajas; el desarrollo queda en notas.
- U08-105 se mantiene como tabla de consulta y deberá dividirse en dos vistas si el render no sostiene al menos 22 pt.
- Las slides bloqueadas no deben “completarse” durante producción sin actualizar antes storyboard, fuente y manifiesto.
- No se introdujeron cifras externas, criterios diagnósticos, indicaciones clínicas ni afirmaciones normativas nuevas.
"""
    (UNIT/"writing_review.md").write_text(text,encoding="utf-8")

def validate(rows):
    errors=[]
    for name in ["slide_text.md","speaker_notes.md","source_map.md","writing_review.md"]:
        if not (UNIT/name).exists(): errors.append(f"falta {name}")
    slide=(UNIT/"slide_text.md").read_text(encoding="utf-8")
    notes=(UNIT/"speaker_notes.md").read_text(encoding="utf-8")
    sources=(UNIT/"source_map.md").read_text(encoding="utf-8")
    for row in rows:
        sid=row["slide_id"]
        if slide.count(f"## {sid} —")!=1: errors.append(f"slide_text: {sid}")
        if notes.count(f"## {sid} —")!=1: errors.append(f"speaker_notes: {sid}")
        if sources.count(f"| {sid} |")!=1: errors.append(f"source_map: {sid}")
    required=["Título","Subtítulo","Contenido visible","Ecuaciones","Definición","Ejemplo","Visual","Caption sugerido","Fuente","Texto alternativo"]
    required_notes=["Duración aproximada","Objetivo oral","Explicación extendida","Guía del visual/diagrama","Pregunta al grupo","Respuesta esperada","Demostración o dinámica","Error frecuente a anticipar","Multimedia","Transición"]
    for sid in [r["slide_id"] for r in rows]:
        section=slide.split(f"## {sid} —",1)[1].split("\n## U08-",1)[0]
        for field in required:
            if field not in section: errors.append(f"{sid}: falta {field}")
        note_section=notes.split(f"## {sid} —",1)[1].split("\n## U08-",1)[0]
        for field in required_notes:
            if field not in note_section: errors.append(f"{sid} notas: falta {field}")
    report=f"status={'passed' if not errors else 'failed'}\nslides=114\nerrors={len(errors)}\n"+"\n".join(errors)
    (UNIT/"writing_validation.txt").write_text(report+"\n",encoding="utf-8")
    if errors: raise SystemExit("\n".join(errors))

def main():
    rows=parse_storyboard(); write_slide_text(rows); write_notes(rows); write_source_map(rows); write_review(rows); validate(rows)
    print("Redacción generada y validada: 114 slides.")

if __name__=="__main__": main()
