from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "units" / "unit_06"
STORYBOARD = UNIT / "storyboard.md"


BLOCK_TITLES = {
    "B00": "Apertura y orientación",
    "B01": "Oído externo y CAE",
    "B02": "Tímpano, presión y movimiento",
    "B03": "Oído medio y reflejo",
    "B04": "Conducción ósea",
    "B05": "Arquitectura coclear",
    "B06": "Onda viajera y tonotopía",
    "B07": "Órgano de Corti, CCI y CCE",
    "B08": "Transducción mecanoeléctrica",
    "B09": "Codificación periférica e integración",
    "B10": "Respaldo",
}

BLOCK_QUESTIONS = {
    "U06-008": "¿Cómo modifica y conduce el oído externo la presión hasta el tímpano?",
    "U06-018": "¿Cómo se convierte una diferencia de presión en fuerza y qué falta para predecir movimiento?",
    "U06-028": "¿Cómo mejora el oído medio la transferencia hacia la cóclea sin crear energía?",
    "U06-040": "¿Por qué la conducción ósea no es una ruta única que evita el oído externo y medio?",
    "U06-049": "¿Qué aporta la vista longitudinal y qué aporta el corte transversal de la cóclea?",
    "U06-061": "¿Cómo dependen de la frecuencia y del nivel el lugar y la extensión de la respuesta coclear?",
    "U06-072": "¿Qué movimiento relativo estimula las células ciliadas?",
    "U06-082": "¿Cómo pasa una deflexión mecánica a una respuesta celular y neural?",
    "U06-094": "¿Qué información de frecuencia y nivel conserva la salida periférica?",
}

EQUATIONS = {
    "U06-004": "`p` o `Δp`: Pa · `F`: N · `x`: m · `V`: V o mV.",
    "U06-014": "`λ ≈ 4ℓ` para el primer modo del tubo ideal abierto–aproximadamente cerrado.",
    "U06-015": "`f_res ≈ c/(4ℓ)`.",
    "U06-016": "`f_res ≈ (343 m·s⁻¹)/[4(0,027 m)] ≈ 3176 Hz ≈ 3,18 kHz`.",
    "U06-020": "`Δp = p_CAE − p_caja` (convención de signo declarada).",
    "U06-021": "Provisional: `F ≈ Δp·S`; control dimensional: `Pa·m² = N`.",
    "U06-022": "`S = 50 mm² = 5,0×10⁻⁵ m²`; `F ≈ (0,20 Pa)(5,0×10⁻⁵ m²) = 1,0×10⁻⁵ N`.",
    "U06-032": "Provisional: `R_S = S_TM/S_E`; razón adimensional.",
    "U06-034": "Provisional: `M_p ≈ R_S·R_L`; `M_p`, `R_S` y `R_L` son adimensionales.",
    "U06-036": "Provisional: `M_p ≈ 20×1,2 = 24`; `G_p = 20 log₁₀(24) ≈ 27,6 dB`.",
    "U06-037": "Razón: `20 log₁₀(p₂/p₁)`; nivel absoluto: `L_p = 20 log₁₀(p_rms/p_ref)` con `p_ref = 20 µPa` en aire.",
    "U06-084": "Relación cualitativa: `V_endolinfa − V_ref > 0`; toda diferencia de potencial exige indicar referencia.",
    "U06-085": "[BLOQUEADA] No fijar ecuación ni valor hasta validar célula, compartimentos y referencia de medida.",
    "U06-102": "Condiciones del caso: `f = 2,0 kHz`; `L_p = 40 dB SPL` y `70 dB SPL`.",
    "U06-109": "`f_res ≈ c/(4ℓ)`; con `c = 343 m·s⁻¹` y `ℓ = 27 mm`, `f_res ≈ 3,18 kHz`.",
    "U06-110": "Provisional: `F ≈ Δp·S`; `0,20 Pa × 5,0×10⁻⁵ m² = 1,0×10⁻⁵ N`.",
    "U06-111": "[PROVISIONAL] `R_S = S_TM/S_E`; `M_p ≈ R_S·R_L`; la notación final depende de OD-U06-07/08.",
}

DEFINITIONS = {
    "U06-003": "Impedancia: relación entre variables de esfuerzo y flujo que condiciona transferencia y reflexión.",
    "U06-009": "Respuesta direccional: cambio dependiente de frecuencia producido por la dirección de llegada y la geometría del pabellón/cabeza.",
    "U06-011": "CAE: conducto auditivo externo; su presión local depende de posición, frecuencia, geometría y terminaciones.",
    "U06-014": "Modelo de cuarto de onda: tubo ideal abierto en un extremo y aproximadamente cerrado en el otro.",
    "U06-015": "`f_res`: primera frecuencia de resonancia (Hz); `c`: rapidez del sonido (m·s⁻¹); `ℓ`: longitud efectiva (m).",
    "U06-020": "`Δp`: diferencia de presión entre las dos caras del tímpano, medida en pascales.",
    "U06-021": "`F`: fuerza resultante (N); `Δp`: diferencia de presión (Pa); `S`: área efectiva (m²), símbolo provisional.",
    "U06-024": "Respuesta mecánica: relación, dependiente de frecuencia, entre una entrada de fuerza y un movimiento de salida.",
    "U06-025": "Presión acústica: variación alternante; presión estática: condición lenta que fija la posición de equilibrio.",
    "U06-030": "Adaptación de impedancias: transformación mecánica que mejora la transferencia entre cargas diferentes.",
    "U06-032": "Razón de áreas: cociente entre superficies efectivas; no tiene unidad.",
    "U06-038": "Reflejo acústico: respuesta refleja que contrae el músculo estapedio y modifica la rigidez/transferencia después de una latencia.",
    "U06-041": "Vía aérea y conducción ósea nombran condiciones de entrada; ambas pueden converger en la misma partición coclear.",
    "U06-052": "Provisional: rampa vestibular, conducto coclear (rampa media) y rampa timpánica.",
    "U06-053": "Perilinfa: fluido de las rampas vestibular y timpánica. Endolinfa: fluido del conducto coclear o rampa media.",
    "U06-056": "Órgano de Corti: organización sensorial y de sostén ubicada sobre la membrana basilar.",
    "U06-057": "[BLOQUEADA] Definición anatómica pendiente de fuente y revisión del túnel de Corti.",
    "U06-065": "Lugar característico: región de máxima respuesta para una condición. Tonotopía: organización ordenada de frecuencias a lo largo de la cóclea.",
    "U06-070": "Compresión coclear: la respuesta aumenta menos que proporcionalmente en parte del rango de entrada.",
    "U06-076": "CCI: célula ciliada interna, vía aferente principal. CCE: célula ciliada externa, realimentación mecánica activa.",
    "U06-083": "Endococlear: gradiente del compartimento; reposo: estado basal celular; receptor: cambio graduado; acción: impulso de la fibra.",
    "U06-084": "Potencial endococlear: diferencia de potencial positiva de la endolinfa respecto de una referencia declarada.",
    "U06-085": "[BLOQUEADA] Copy final pendiente de fuente fisiológica autorizada.",
    "U06-086": "Potencial receptor: respuesta graduada de la célula. Potencial de acción: señal regenerativa de la fibra aferente.",
    "U06-087": "*Tip link*: enlace mecánico entre estereocilios vecinos; no es un canal iónico.",
    "U06-095": "Código espacial: información representada por la distribución de actividad a lo largo de una población.",
    "U06-096": "[BLOQUEADA] Sincronización temporal pendiente de fuente específica para límites y condiciones.",
    "U06-097": "Frecuencia: magnitud física en hertz. Altura tonal o *pitch*: atributo perceptual.",
    "U06-099": "Nivel de presión sonora: relación física en dB SPL. Sonoridad: atributo perceptual; no es una magnitud en dB SPL.",
}

EXAMPLES = {
    "U06-009": "Una fuente que cambia de dirección puede alterar de modo diferente componentes graves, medias y agudas.",
    "U06-012": "Dos posiciones de sonda pueden registrar presiones diferentes aunque el estímulo externo sea el mismo.",
    "U06-016": "CAE ideal con `ℓ = 27 mm` y `c = 343 m·s⁻¹`.",
    "U06-022": "Modelo elemental con `Δp = 0,20 Pa` y `S = 50 mm²`.",
    "U06-025": "Una señal sonora hace oscilar el tímpano; un cambio de presión ambiental modifica lentamente su equilibrio.",
    "U06-036": "Razón de áreas 20 y razón de palanca 1,2: razón ideal de presión 24.",
    "U06-047": "Un vibrador apoyado en el cráneo puede activar simultáneamente radiación al CAE, inercias y deformación.",
    "U06-059": "Menor movilidad de una frontera puede cambiar la transferencia, pero no localiza por sí sola una causa clínica.",
    "U06-066": "Entre dos tonos, el más agudo alcanza su máximo en una región relativamente más basal.",
    "U06-080": "Una otoemisión debe recorrer cóclea → oído medio → CAE antes de llegar al micrófono.",
    "U06-102": "Mismo tono de 2 kHz presentado a 40 y 70 dB SPL, con igual duración y condiciones.",
    "U06-109": "Cálculo completo del modelo de CAE con 27 mm.",
    "U06-110": "Conversión de 50 mm² a 5,0×10⁻⁵ m² antes de multiplicar.",
    "U06-111": "Cálculo paramétrico; no cerrar valores ni símbolos hasta resolver la notación.",
}

RECAP_VISIBLE = {
    "U06-017": "La dirección modifica el espectro. La presión varía con la posición en el CAE. El cuarto de onda es un modelo limitado. ¿Qué magnitud actúa finalmente sobre el tímpano?",
    "U06-027": "`Δp` produce fuerza distribuida. La fuerza no determina por sí sola el desplazamiento. Masa, rigidez, amortiguamiento y frecuencia condicionan el movimiento. ¿Cómo se transfiere hacia el fluido?",
    "U06-039": "El oído medio mejora la transferencia. Mayor presión no significa creación de energía. El reflejo modifica la transferencia después de una latencia. ¿Qué ocurre si la entrada es una vibración del cráneo?",
    "U06-048": "La conducción ósea reúne mecanismos simultáneos. Algunos involucran CAE y huesecillos. Todos pueden contribuir al movimiento coclear. La vía ósea no es un bypass único.",
    "U06-060": "Ventanas: fronteras móviles complementarias. Rampas y fluidos: organización longitudinal. Membranas: permiten movimiento relativo. ¿Dónde alcanzará su máximo cada frecuencia?",
    "U06-071": "La frecuencia desplaza el lugar de máxima respuesta. El nivel modifica amplitud y extensión. La respuesta activa es compresiva. Ninguna de estas relaciones equivale todavía a pitch o sonoridad.",
    "U06-081": "Movimiento relativo y transducción son comunes. Las CCI sostienen la aferencia principal. Las CCE realimentan la mecánica. ¿En qué etapa aparece una señal eléctrica?",
    "U06-093": "Mecánica → potencial receptor graduado → liberación química → potenciales de acción en la fibra. Ubique cada señal antes de explicar qué información conserva.",
    "U06-104": "Externo: dirección, posición y presión. Medio: fuerza, transferencia y pérdidas. Cóclea: ventanas, onda viajera y tonotopía. Células/fibra: transducción y codificación. Errores a evitar: energía creada; físico = perceptual.",
}

VISIBLE_SPECIAL = {
    "U06-001": "Licenciatura en Fonoaudiología · Física Acústica · Unidad 6. Del aire a la actividad del nervio auditivo.",
    "U06-002": "Ordená: presión en el aire · tímpano · huesecillos · cóclea · células ciliadas · nervio auditivo. Justificá dos enlaces.",
    "U06-003": "Mecánica: fuerza y movimiento. Ondas: oscilación y propagación. Acústica: presión e impedancia. Señales: espectro y respuesta del sistema.",
    "U06-004": "Emparejá cada magnitud con su unidad: presión · fuerza · desplazamiento · potencial eléctrico · actividad neural.",
    "U06-005": "Ordenar la cadena. Relacionar oído externo y transferencia. Calcular presión–fuerza. Comparar vía aérea y conducción ósea.",
    "U06-006": "Identificar la arquitectura coclear. Explicar frecuencia y nivel. Diferenciar CCI/CCE y transducción. Delimitar percepción y diagnóstico.",
    "U06-007": "Entrada externa → oído medio y vía ósea → mecánica coclear → transducción y codificación.",
    "U06-013": "Modelos ideales: frentes simples y condiciones declaradas. CAE real: curvatura, sección variable, terminaciones, pérdidas y dependencia de frecuencia/posición. No existe una conversión geométrica universal.",
    "U06-014": "Hipótesis: tubo recto, entrada abierta y extremo timpánico aproximadamente cerrado. Primera condición: `λ ≈ 4ℓ`. Omite curvatura, sección variable, pérdidas e impedancia timpánica.",
    "U06-015": "`f_res ≈ c/(4ℓ)`. Si `c` se mantiene, una mayor longitud efectiva produce una menor primera frecuencia de resonancia. El signo `≈` recuerda que se trata de un modelo.",
    "U06-016": "1. `27 mm = 0,027 m`. 2. Sustituir `c` y `ℓ`. 3. Cancelar metros. 4. Informar `3,18 kHz`. 5. Declarar los límites del modelo.",
    "U06-021": "La diferencia de presión actúa sobre un área efectiva y permite estimar una fuerza. El resultado queda en newtons; todavía no describe el desplazamiento del tímpano.",
    "U06-022": "1. Convertir `50 mm²` a `5,0×10⁻⁵ m²`. 2. Multiplicar por `0,20 Pa`. 3. Obtener `1,0×10⁻⁵ N`. 4. Preguntar qué falta para predecir movimiento.",
    "U06-023": "1. Variación en Pa junto al tímpano. 2. Resultado en N sobre una superficie. 3. Movimiento en m de una membrana. Asigná magnitud, símbolo y unidad.",
    "U06-032": "[PROVISIONAL] `R_S = S_TM/S_E`. Las dos áreas se expresan en la misma unidad, por lo que el cociente es adimensional. No representa dimensiones anatómicas universales.",
    "U06-034": "[PROVISIONAL] La razón de áreas y la razón de palanca se combinan en una razón ideal de presiones. El símbolo `M_p` evita confundir esta transformación con el coeficiente de reflexión `R_p` de U4.",
    "U06-036": "1. `M_p ≈ 20×1,2 = 24`. 2. `G_p = 20 log₁₀(24) ≈ 27,6 dB`. Interpretación: razón ideal de amplitudes; no dB SPL, no ganancia de energía, no respuesta universal.",
    "U06-037": "Razón del modelo: compara `p₂` con `p₁`. Nivel de presión sonora: compara `p_rms` con `20 µPa` en aire. Ambos pueden expresarse en dB, pero responden preguntas distintas.",
    "U06-042": "Afirmación: «La vía ósea evita por completo el CAE, el tímpano y los huesecillos». Decidí si es verdadera o falsa y justificá con dos mecanismos.",
    "U06-058": "Clasificá: base–ápex · helicotrema · rampas · membrana de Reissner · ventana oval. ¿Se reconoce en la vista longitudinal, en el corte o en ambas?",
    "U06-066": "Dos tonos, un eje base–ápex. Señalá dónde esperás el máximo del tono más agudo y justificá sin inventar distancias.",
    "U06-079": "Clasificá y justificá: aferencia principal · liberación de glutamato · realimentación mecánica · otoemisiones acústicas.",
    "U06-092": "Ordená: deflexión · corriente iónica · potencial receptor · neurotransmisor · respuesta de la fibra. Justificá dos conexiones causales.",
    "U06-102": "Seleccioná y justificá: (a) cambia el lugar característico; (b) cambia la extensión; (c) cambia la amplitud; (d) cambia la frecuencia física; (e) puede inferirse una razón universal de sonoridad.",
    "U06-105": "Ahora podemos explicar la cadena periférica y sus transformaciones. Todavía no podemos deducir percepción completa ni diagnóstico desde una respuesta aislada. Próximas preguntas: ¿cómo emerge la experiencia?, ¿cómo se mide clínicamente?",
    "U06-106": "Consultar según la duda: terminología · notación · cálculos · conducción ósea · electroquímica · reflejo · fuentes anatómicas.",
    "U06-107": "[PROVISIONAL] Conducto auditivo externo (CAE); conducto coclear / rampa media / *scala media*; ventana oval / vestibular; otoemisión acústica (OEA).",
    "U06-108": "[PROVISIONAL] Fuente: `A`, `A_TM`, `A_E`, `R_p`. Curso propuesto: `S`, `S_TM`, `S_E`, `M_p`. Reservar `R_p` para reflexión de presión.",
    "U06-109": "Datos: `c = 343 m·s⁻¹`, `ℓ = 27 mm = 0,027 m`. Sustitución y resultado: `f_res ≈ 3,18 kHz`. Interpretación: cálculo del modelo, no resonancia universal del CAE.",
    "U06-110": "Datos: `Δp = 0,20 Pa`, `S = 50 mm² = 5,0×10⁻⁵ m²`. Resultado: `F ≈ 1,0×10⁻⁵ N`. Falta la respuesta mecánica para obtener desplazamiento.",
    "U06-111": "[PROVISIONAL] Calcular razón de áreas, razón de palanca y razón de presiones; convertir la razón a dB; cerrar con balance de energía, pérdidas y límites del modelo.",
    "U06-112": "G1: variar longitud del CAE y explicar el efecto. G2: variar `Δp` con área fija y comprobar proporcionalidad. G3: variar áreas/palanca y separar razón, dB y dB SPL.",
    "U06-113": "Radiación al CAE · inercia osicular · inercia de fluidos · deformación capsular · tejidos/cavidades. Su importancia depende de frecuencia, punto y acoplamiento.",
    "U06-114": "K⁺: entrada apical y despolarización. Ca²⁺: acoplamiento basal con liberación. Repolarización: cierre del ciclo celular. Glutamato: comunicación con la fibra.",
    "U06-115": "[BLOQUEADA] Completar únicamente con fuente que informe estímulo, frecuencia, duración, nivel, método, población, umbral y latencia.",
    "U06-116": "[BLOQUEADA] Incorporar imagen anatómica validada, límites del túnel, pilares interno/externo, relación con órgano de Corti y cita completa.",
    "U06-117": "Programa oficial · capítulo LaTeX/PDF · bibliografía del capítulo · glosario y notación · manifiesto de assets · decisiones abiertas.",
}

ERRORS = {
    "U06-011": "Confundir desplazamiento local de partículas con avance del patrón de presión.",
    "U06-013": "Presentar «esférica → cilíndrica» como transformación exacta del CAE real.",
    "U06-016": "Tomar 3,18 kHz como constante anatómica universal.",
    "U06-021": "Interpretar fuerza calculada como desplazamiento timpánico.",
    "U06-025": "Afirmar que la trompa iguala la presión acústica ciclo a ciclo.",
    "U06-030": "Decir que adaptar impedancias elimina toda reflexión.",
    "U06-035": "Confundir aumento de presión con creación de energía.",
    "U06-037": "Rotular una razón del modelo como dB SPL.",
    "U06-038": "Describir el reflejo como instantáneo o absolutamente protector.",
    "U06-042": "Describir la vía ósea como un bypass único.",
    "U06-050": "Imaginar circulación neta permanente desde la ventana oval a la redonda.",
    "U06-057": "Completar anatomía desde memoria mientras la fuente está bloqueada.",
    "U06-062": "Confundir oscilación local con transporte neto del fluido.",
    "U06-065": "Convertir el lugar característico en una celda de ancho fijo.",
    "U06-067": "Afirmar que la cóclea ejecuta literalmente una FFT.",
    "U06-070": "Representar el proceso activo como ganancia constante.",
    "U06-076": "Afirmar que solo un tipo celular transduce.",
    "U06-080": "Tomar una OEA ausente como localización única en CCE.",
    "U06-085": "Confundir potencial endococlear, de reposo y receptor.",
    "U06-086": "Ubicar el potencial de acción dentro de la célula ciliada.",
    "U06-087": "Llamar canal iónico al *tip link*.",
    "U06-088": "Representar la apertura de canales como interruptor mecánico todo-o-nada.",
    "U06-096": "Suponer un impulso por ciclo o fijar un límite frecuencial universal.",
    "U06-097": "Usar frecuencia y altura tonal como sinónimos.",
    "U06-099": "Usar dB SPL y sonoridad como sinónimos.",
    "U06-100": "Convertir una medición aislada en diagnóstico o localización única.",
}

QUESTION_SPECIAL = {
    "U06-003": "¿Qué concepto previo usaríamos para explicar la reflexión en una interfaz?",
    "U06-004": "¿Por qué no alcanza con decir que todas son «señales»?",
    "U06-015": "Si aumenta `ℓ`, ¿qué ocurre con `f_res`?",
    "U06-016": "¿Qué dos propiedades del CAE real omite el cálculo?",
    "U06-021": "¿Qué magnitud falta para describir el movimiento?",
    "U06-024": "¿Puede una misma fuerza producir movimientos distintos a frecuencias diferentes?",
    "U06-030": "¿Qué destinos puede tener la energía en una interfaz desadaptada?",
    "U06-035": "¿Qué variable disminuye si aumenta la fuerza de salida en un transformador ideal?",
    "U06-038": "¿Por qué el reflejo no modifica el inicio de un impulso muy breve?",
    "U06-043": "¿Qué condición puede cambiar la importancia relativa de los mecanismos?",
    "U06-050": "¿Qué función mecánica cumple la ventana redonda?",
    "U06-053": "¿Dónde se encuentra la endolinfa?",
    "U06-064": "¿Qué curva alcanza su máximo más cerca de la base?",
    "U06-070": "¿Por qué una recta de ganancia constante no describe esta respuesta?",
    "U06-076": "¿Cuál es la vía aferente principal y cuál realimenta la mecánica?",
    "U06-084": "¿Puede informarse un voltaje sin nombrar la referencia?",
    "U06-086": "¿En qué estructura aparecen los potenciales de acción?",
    "U06-088": "¿Qué cambia primero con la deflexión excitatoria?",
    "U06-091": "¿Dónde cambia la señal de celular a neural?",
    "U06-095": "¿Un máximo espacial representa una sola fibra?",
    "U06-098": "¿Qué se mantiene y qué cambia entre ambos niveles?",
    "U06-100": "¿Qué factores previos condicionan una OEA registrada en el CAE?",
    "U06-103": "¿Qué afirmación del caso pertenece a percepción y no puede cerrarse aquí?",
}

EXPECTED_SPECIAL = {
    "U06-002": "Presión en el aire → tímpano → huesecillos → cóclea → células ciliadas → actividad del nervio auditivo.",
    "U06-004": "Presión: Pa; fuerza: N; desplazamiento: m; potencial eléctrico: V o mV; actividad neural: patrón de descargas, no una única unidad física universal.",
    "U06-010": "No. La geometría produce modificaciones dependientes de frecuencia y dirección.",
    "U06-015": "`f_res` disminuye porque es inversamente proporcional a `ℓ`.",
    "U06-016": "Por ejemplo: curvatura, sección variable, pérdidas e impedancia del tímpano.",
    "U06-021": "Se necesita la respuesta mecánica: masa, rigidez, amortiguamiento, frecuencia y apoyos.",
    "U06-023": "Variación junto al tímpano: presión, Pa. Resultado sobre una superficie: fuerza, N. Movimiento de la membrana: desplazamiento, m.",
    "U06-030": "Puede transferirse, reflejarse y disiparse una parte.",
    "U06-035": "Disminuye el desplazamiento o la velocidad de salida, además de existir pérdidas reales.",
    "U06-038": "La contracción muscular ocurre después de una latencia.",
    "U06-042": "Falsa. La radiación hacia el CAE y la inercia osicular son dos ejemplos de participación del oído externo o medio.",
    "U06-050": "Aporta una frontera móvil complementaria para permitir desplazamientos oscilatorios del fluido.",
    "U06-053": "En el conducto coclear o rampa media.",
    "U06-058": "Base–ápex, helicotrema y ventanas se reconocen principalmente en la vista longitudinal; rampas y membrana de Reissner, en el corte. La orientación general debe coordinarse entre ambas.",
    "U06-064": "La frecuencia alta; las bajas alcanzan máximos más apicales.",
    "U06-066": "En una región relativamente más basal; el storyboard no autoriza asignar una distancia exacta.",
    "U06-076": "CCI: aferencia principal. CCE: realimentación mecánica activa.",
    "U06-079": "Aferencia y glutamato: rama CCI. Realimentación y OEA: rama CCE, con participación de la cadena de salida para registrar la OEA.",
    "U06-084": "No; una diferencia de potencial siempre se define entre dos puntos o referencias.",
    "U06-086": "En las fibras aferentes, después de la transmisión sináptica.",
    "U06-088": "Aumenta la probabilidad de apertura de canales de transducción.",
    "U06-092": "Deflexión → cambio de apertura/corriente iónica → potencial receptor → liberación de neurotransmisor → respuesta de la fibra.",
    "U06-095": "No; representa una población distribuida con extensión y solapamiento.",
    "U06-098": "Se mantiene la frecuencia; cambian amplitud, extensión y patrón poblacional.",
    "U06-102": "Cambian amplitud y extensión; la región característica general se mantiene porque la frecuencia no cambia. No cambia la frecuencia física ni puede inferirse una razón universal de sonoridad.",
    "U06-103": "No puede cerrarse una razón universal de sonoridad ni un diagnóstico.",
}

DURATION = {
    "portada": 2,
    "divisor": 2,
    "objetivos": 3,
    "mapa": 4,
    "puente": 4,
    "definición": 5,
    "ecuación": 6,
    "ejemplo": 7,
    "ejercicio resuelto": 7,
    "pregunta": 5,
    "pregunta integradora": 7,
    "proceso": 6,
    "explicación": 6,
    "comparación": 6,
    "gráfico": 6,
    "aplicación": 6,
    "error frecuente": 5,
    "recapitulación": 5,
    "recapitulación final": 8,
    "resolución": 8,
    "cierre": 4,
    "mapa conceptual": 6,
    "guía de respaldo": 2,
    "glosario visual": 5,
    "referencia": 5,
    "referencia anatómica": 5,
    "ampliación": 7,
    "banco de ejercicios": 10,
    "objetivos": 3,
}


def parse_storyboard() -> list[dict[str, str]]:
    keys = [
        "slide_id", "block", "slide_type", "title", "purpose", "key_message",
        "visible_summary", "visual", "visual_class", "layout", "speaker_goal",
        "source", "prerequisites", "transition", "status",
    ]
    rows: list[dict[str, str]] = []
    for line in STORYBOARD.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| U06-"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != len(keys):
            raise ValueError(f"Fila inválida: {cells[0]} tiene {len(cells)} campos")
        rows.append(dict(zip(keys, cells)))
    if len(rows) != 117:
        raise ValueError(f"Se esperaban 117 slides y se encontraron {len(rows)}")
    return rows


def block_code(row: dict[str, str]) -> str:
    return row["block"].split()[0]


def clean_meta(text: str) -> str:
    text = text.replace("; sin cálculo", ".")
    text = text.replace("; sin nuevo visual", ".")
    text = text.replace("; sin valores", ".")
    text = text.replace("; sin dB HL", ".")
    text = text.replace("; sin diagnóstico", ".")
    text = text.replace("; no diagnóstico", ".")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def writing_state(status: str) -> str:
    if "bloqueada_fuente" in status:
        return "bloqueada: conservar placeholder; falta fuente autorizada"
    if "pendiente_notacion" in status:
        return "provisional: no cerrar símbolos hasta resolver OD-U06-07/08/09"
    if "pendiente_terminologia" in status:
        return "provisional: validar terminología antes de producción"
    if "pendiente_validacion_docente" in status:
        return "provisional: requiere validación docente"
    if "pendiente_asset" in status:
        return "texto redactado; visual externo pendiente"
    if "pendiente_media" in status:
        return "texto redactado; usar alternativa estática hasta aprobar multimedia"
    return "redactada"


def subtitle(row: dict[str, str]) -> str:
    if row["slide_type"] == "portada":
        return "Del aire a la actividad del nervio auditivo"
    if row["slide_id"] in BLOCK_QUESTIONS:
        return BLOCK_QUESTIONS[row["slide_id"]]
    return row["key_message"]


def visible_content(row: dict[str, str]) -> str:
    sid = row["slide_id"]
    if sid in VISIBLE_SPECIAL:
        return VISIBLE_SPECIAL[sid]
    if sid in RECAP_VISIBLE:
        return RECAP_VISIBLE[sid]
    if "bloqueada_fuente" in row["status"]:
        return f"[BLOQUEADA] {clean_meta(row['visible_summary'])} No completar sin la fuente indicada."
    if row["slide_type"] == "divisor":
        return BLOCK_QUESTIONS.get(sid, row["key_message"])
    if row["slide_type"] in {"pregunta", "pregunta integradora"}:
        return f"{clean_meta(row['visible_summary'])} Justificá la respuesta con una relación física o funcional."
    if row["slide_type"] == "error frecuente":
        return f"Afirmación a revisar: {row['title']}. Corrección: {row['key_message']}"
    if row["slide_type"] in {"ecuación", "ejemplo", "ejercicio resuelto"}:
        return clean_meta(row["visible_summary"])
    if "DG" in row["visual"]:
        return f"Idea central: {row['key_message']} Clave de lectura: {clean_meta(row['visible_summary'])}"
    return clean_meta(row["visible_summary"])


def equation(row: dict[str, str]) -> str:
    return EQUATIONS.get(row["slide_id"], "—")


def definition(row: dict[str, str]) -> str:
    return DEFINITIONS.get(row["slide_id"], "—")


def example(row: dict[str, str]) -> str:
    return EXAMPLES.get(row["slide_id"], "—")


def caption(row: dict[str, str]) -> str:
    if "bloqueada_fuente" in row["status"]:
        return "Recurso no aprobado: falta fuente específica; no usar en producción."
    if row["visual_class"] == "chart":
        return f"Lectura conceptual: {row['key_message']} Las curvas no son datos clínicos."
    if "DG" in row["visual"] or row["visual_class"] == "diagram":
        return f"Esquema conceptual, no a escala. {row['key_message']}"
    if "MEDIA" in row["visual"]:
        return f"Secuencia estática disponible. {row['key_message']}"
    return row["key_message"]


def visual_text(row: dict[str, str]) -> str:
    text = row["visual"].replace("DG candidate", "Diagrama").replace("DG candidates", "Diagramas")
    if "pendiente_media" in row["status"]:
        text += " Usar la alternativa estática DG indicada hasta aprobar el recurso multimedia."
    if "pendiente_asset" in row["status"]:
        text += " Mantener el espacio reservado; no sustituir con stock genérico."
    if "bloqueada_fuente" in row["status"]:
        text += " No producir el visual final."
    return text


def alt_text(row: dict[str, str]) -> str:
    sid = row["slide_id"]
    if "bloqueada_fuente" in row["status"]:
        return f"Placeholder de {row['title'].lower()}; el recurso definitivo está bloqueado por falta de fuente."
    if row["visual_class"] == "chart":
        return f"Gráfico que muestra {row['key_message'].lower()} Ejes, escala y normalización se describen en el propio recurso."
    if "DG" in row["visual"] or row["visual_class"] == "diagram":
        return f"Diagrama sobre «{row['title']}»; organiza {clean_meta(row['visible_summary']).lower()}"
    if "MEDIA" in row["visual"]:
        return f"Secuencia de estados de {row['title'].lower()}, acompañada por una alternativa estática equivalente."
    if row["slide_type"] == "portada":
        return "Motivo técnico del oído periférico que vincula presión en el aire con actividad del nervio auditivo."
    return f"Composición visual sobre {row['title'].lower()}; destaca que {row['key_message'].lower()}"


def notes_question(row: dict[str, str]) -> tuple[str | None, str | None]:
    sid = row["slide_id"]
    q = QUESTION_SPECIAL.get(sid)
    if q is None and row["slide_type"] in {"pregunta", "pregunta integradora"}:
        q = row["title"]
    if q is None and row["slide_type"] in {"recapitulación", "recapitulación final", "error frecuente", "aplicación"}:
        q = f"¿Qué permite afirmar esta slide y qué no permite concluir?"
    if q is None:
        return None, None
    expected = EXPECTED_SPECIAL.get(sid, row["key_message"])
    return q, expected


def diagram_guide(row: dict[str, str]) -> str | None:
    if "DG" not in row["visual"] and row["visual_class"] != "diagram":
        return None
    if row["slide_type"] in {"pregunta", "pregunta integradora"}:
        return "Presentar primero el diagrama sin solución; dar tiempo de observación; pedir una justificación; recién después revelar conexiones o rótulos."
    if row["slide_type"] == "ecuación":
        return "Leer primero la relación central; señalar cada símbolo desde sus callouts; comprobar unidades; cerrar con la interpretación y el límite del modelo."
    if row["slide_type"] in {"proceso", "resolución"}:
        return "Nombrar la entrada; seguir una flecha por vez; identificar qué magnitud o dominio cambia; detenerse en la salida y en el límite inferencial."
    if row["slide_type"] == "comparación":
        return "Leer ambas columnas con el mismo criterio; comparar una fila por vez; usar el puente central solo después de describir las diferencias."
    return "Nombrar la idea central fuera del diagrama; recorrer nodos y conectores en el orden propuesto; terminar con la relación funcional, sin repetir todo el texto de las cajas."


def media_note(row: dict[str, str]) -> str | None:
    if "MEDIA" not in row["visual"]:
        return None
    return "Reproducir el recurso solo si está aprobado. Antes de iniciar, indicar qué observar; después, congelar o mostrar la alternativa estática y pedir que describan el cambio."


def duration(row: dict[str, str]) -> int:
    base = DURATION.get(row["slide_type"], 5)
    if "complementaria" in row["status"]:
        return max(3, base - 1)
    return base


def escape_table(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def asset_ids(text: str) -> str:
    ids = re.findall(r"U06-(?:DG|CH|IMG|MEDIA)-\d+[A-Z]?", text)
    return ", ".join(dict.fromkeys(ids)) or "—"


def write_slide_text(rows: list[dict[str, str]]) -> None:
    out = [
        "# Unidad 6 — Texto visible de las slides",
        "",
        "Versión: borrador completo condicionado · 2026-08-10  ",
        "Base exclusiva de arquitectura y secuencia: `storyboard.md`. Las fuentes se usaron para verificar exactitud, no para agregar slides. Los estados condicionales se preservan y este documento no autoriza todavía la producción del PowerPoint.",
        "",
    ]
    current = None
    for row in rows:
        code = block_code(row)
        if code != current:
            current = code
            out.extend([f"## {code} · {BLOCK_TITLES[code]}", ""])
        sid = row["slide_id"]
        out.extend([
            f"### {sid} — {row['title']}",
            "",
            f"- **Estado de escritura:** {writing_state(row['status'])}.",
            f"- **Subtítulo:** {subtitle(row)}",
            f"- **Contenido visible:** {visible_content(row)}",
            f"- **Ecuaciones:** {equation(row)}",
            f"- **Definiciones:** {definition(row)}",
            f"- **Ejemplo:** {example(row)}",
            f"- **Caption:** {caption(row)}",
            f"- **Visual:** {visual_text(row)}",
            f"- **Layout:** `{row['layout']}`.",
            f"- **Fuente:** {row['source']}",
            f"- **Texto alternativo:** {alt_text(row)}",
            "",
        ])
    (UNIT / "slide_text.md").write_text("\n".join(out), encoding="utf-8")


def write_speaker_notes(rows: list[dict[str, str]]) -> None:
    out = [
        "# Unidad 6 — Notas del orador",
        "",
        "Versión: borrador completo condicionado · 2026-08-10  ",
        "Las duraciones son aproximadas. Las slides complementarias y de respaldo se usan a demanda. No proyectar slides bloqueadas como contenido final.",
        "",
    ]
    current = None
    for row in rows:
        code = block_code(row)
        if code != current:
            current = code
            out.extend([f"## {code} · {BLOCK_TITLES[code]}", ""])
        sid = row["slide_id"]
        suffix = ""
        if "complementaria" in row["status"]:
            suffix = " · complementaria"
        elif "respaldo" in row["status"]:
            suffix = " · respaldo"
        if "bloqueada" in row["status"]:
            suffix += " · bloqueada"
        out.append(f"### {sid} · {duration(row)} min{suffix}")
        out.append("")
        if "bloqueada_fuente" in row["status"]:
            out.append(f"**Pausa por fuente:** {row['speaker_goal']} No completar la explicación sustantiva ni proyectar como slide final hasta resolver la fuente indicada. Puede mencionarse al docente como vacío trazado, no al estudiantado como conocimiento cerrado.")
        else:
            out.append(f"**Explicación:** {row['speaker_goal']} Desarrollar la idea con esta conclusión: {row['key_message']}")
        guide = diagram_guide(row)
        if guide:
            out.append(f"**Guía del diagrama:** {guide}")
        if row["visual_class"] == "chart":
            out.append("**Guía del gráfico:** leer primero ejes, unidades/normalización y escala; después localizar máximos, comparar condiciones y cerrar con lo que la curva no representa.")
        media = media_note(row)
        if media:
            out.append(f"**Multimedia/demostración:** {media}")
        q, expected = notes_question(row)
        if q:
            out.append(f"**Pregunta al curso:** {q}")
            out.append(f"**Respuesta esperada:** {expected}")
        if sid in ERRORS:
            out.append(f"**Error frecuente:** {ERRORS[sid]}")
        if sid in {"U06-014", "U06-015", "U06-016", "U06-109"}:
            out.append("**Demostración opcional:** usar un tubo o una tira de longitud visible solo como analogía geométrica del cuarto de onda; no presentarlo como reproducción anatómica del CAE.")
        if sid in {"U06-031", "U06-033", "U06-034", "U06-036", "U06-111"}:
            out.append("**Demostración opcional:** comparar dos brazos de palanca y preguntar qué se gana en fuerza y qué se cede en desplazamiento. No usar la demostración para fijar razones anatómicas.")
        out.append(f"**Transición:** {row['transition']}")
        out.append("")
    (UNIT / "speaker_notes.md").write_text("\n".join(out), encoding="utf-8")


def write_source_map(rows: list[dict[str, str]]) -> None:
    out = [
        "# Unidad 6 — Mapa de fuentes para redacción",
        "",
        "Fecha: 2026-08-10  ",
        "Este archivo copia la trazabilidad del storyboard aprobado. No convierte referencias pendientes en fuentes aprobadas.",
        "",
        "## Abreviaturas",
        "",
        "- `PO`: programa oficial 2025, Unidad 6, p. 4.",
        "- `TEX`: `context/libro_latex/chapters/06-percepcion-auditiva.tex`.",
        "- `PDF`: `context/libro_pdf/Física Acústica para Fonoaudiología.pdf`, capítulo 6, pp. 151–175.",
        "- `BR`, `SA`, `OD`: brief, análisis de fuentes y decisiones abiertas de la Unidad 6.",
        "- `CM`, `CDM`: mapa y dependencias globales del curso.",
        "- `NOT`/`NG`, `GLO`: guía de notación y glosario.",
        "- `REF`: bibliografía académica ya citada en el capítulo.",
        "- `EXT-PEND`: fuente externa aún no curada; no habilita copy final.",
        "- `EP`: elaboración pedagógica propia derivada de las fuentes anteriores.",
        "",
        "## Trazabilidad slide por slide",
        "",
        "| Slide | Bloque | Uso/estado | Fuente del storyboard | Recursos | Estado de escritura |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        out.append(
            f"| {row['slide_id']} | {block_code(row)} | {escape_table(row['status'])} | "
            f"{escape_table(row['source'])} | {asset_ids(row['visual'])} | {escape_table(writing_state(row['status']))} |"
        )
    out.extend([
        "",
        "## Bloqueos que afectan fuentes o copy final",
        "",
        "- U06-057 y U06-116: túnel de Corti; falta fuente anatómica específica y revisión.",
        "- U06-085: potencial de reposo; falta fuente fisiológica con referencia de medida.",
        "- U06-096: sincronización temporal; falta fuente para condiciones y límites.",
        "- U06-115: umbral/latencia del reflejo; faltan datos trazables por estímulo y método.",
        "- U06-013: la formulación esférica–cilíndrica conserva validación docente pendiente.",
        "- U06-021, 032, 034, 036, 108 y 111: notación provisional `S`, `R_S`, `R_L`, `M_p` y `G_p`.",
        "- U06-052 y 107: nomenclatura de rampas/scala pendiente de decisión docente.",
        "",
        "## Regla de uso",
        "",
        "Una fila con `EXT-PEND`, `bloqueada_fuente`, `pendiente_notacion`, `pendiente_terminologia` o `pendiente_validacion_docente` no puede considerarse final aunque el texto de apoyo exista como placeholder o borrador provisional.",
    ])
    (UNIT / "source_map.md").write_text("\n".join(out), encoding="utf-8")


def write_review(rows: list[dict[str, str]]) -> None:
    statuses = Counter(row["status"] for row in rows)
    conditional = [row for row in rows if any(x in row["status"] for x in ("pendiente", "bloqueada"))]
    source_blocked = [row["slide_id"] for row in rows if "bloqueada_fuente" in row["status"]]
    out = [
        "# Unidad 6 — Revisión de redacción",
        "",
        "Fecha: 2026-08-10  ",
        "Estado: **borrador completo condicionado; no habilita todavía la producción del PowerPoint**.",
        "",
        "## Resultado cuantitativo",
        "",
        f"- Slides del storyboard: **{len(rows)}**.",
        f"- Entradas en `slide_text.md`: **{len(rows)}**.",
        f"- Entradas en `speaker_notes.md`: **{len(rows)}**.",
        f"- Slides con algún estado condicional heredado: **{len(conditional)}**.",
        f"- Slides bloqueadas específicamente por fuente: **{len(source_blocked)}** ({', '.join(source_blocked)}).",
        "",
        "## Lista de comprobación",
        "",
        "| Criterio | Resultado | Observación |",
        "|---|---|---|",
        "| Orden y cantidad del storyboard | Cumple | Se preservan U06-001–117 sin fusiones ni nuevas slides. |",
        "| Título, subtítulo, contenido, ecuaciones, definiciones y ejemplo | Cumple | Todos los campos existen; se usa `—` cuando no corresponde. |",
        "| Caption, visual, layout, fuente y texto alternativo | Cumple | Cada slide conserva la instrucción y trazabilidad del storyboard. |",
        "| Notas, transición y duración | Cumple | Las 117 entradas incluyen explicación, transición y tiempo; preguntas/respuestas y errores se agregan cuando corresponde. |",
        "| Intuición antes del formalismo | Cumple | Los modelos y ecuaciones aparecen después de la preparación fenomenológica. |",
        "| Símbolos y unidades | Cumple de forma provisional | `S` y `M_p` se marcan como propuestas, no decisiones cerradas. |",
        "| Aplicación a Fonoaudiología | Cumple | Medición en CAE, vía ósea, OEA, potenciales y pruebas conservan límites no diagnósticos. |",
        "| Diagramas legibles | Cumple en redacción | La idea central queda fuera de las cajas; el texto interno se mantiene breve y la explicación extensa pasa a notas. |",
        "| Fuentes externas pendientes | Controlado | No se completaron valores ni anatomía desde memoria. |",
        "| PowerPoint | No realizado | Se respetó la exclusión solicitada. |",
        "",
        "## Problemas y decisiones abiertas",
        "",
        "| Severidad | Problema | Slides | Tratamiento aplicado | Estado |",
        "|---|---|---|---|---|",
        "| Alta | Fuente anatómica del túnel de Corti ausente | U06-057, 116 | Placeholder explícito; sin definición ni visual final | abierto |",
        "| Alta | Fuente fisiológica del potencial de reposo ausente | U06-085 | Placeholder sin cifra ni ecuación final | abierto |",
        "| Alta | Fuente de sincronización temporal y datos del reflejo insuficiente | U06-096, 115 | Sin límite universal ni valores | abierto |",
        "| Alta | Notación `A/S`, razón de presión y colisión con `R_p` | U06-021, 032, 034, 036, 108, 111 | Borrador con `S`, `R_S`, `R_L`, `M_p`; rotulado provisional | abierto |",
        "| Alta | Storyboard review anterior no habilitaba slide-writing | conjunto | Se mantuvieron todos sus bloqueos; el presente archivo no declara aprobación final | abierto |",
        "| Media | Tratamiento «esférica → cilíndrica» pendiente de validación docente | U06-013 | Se redactó como comparación entre idealización y CAE real | abierto |",
        "| Media | Terminología rampa media/conducto coclear/scala media | U06-052, 107 | Primera aparición doble marcada provisional | abierto |",
        "| Media | Assets externos o multimedia pendientes | U06-012, 019, 047, 056, 062, 073, 074, 101 | Se conserva espacio y alternativa estática cuando existe | abierto |",
        "| Media | El rótulo G1 de U06-109 usa 27 mm, mientras el ejercicio G1 del capítulo usa 25 mm | U06-109 | Se respetó el dato de 27 mm fijado por el storyboard; requiere decidir si se renombra como ejemplo o se alinea al ejercicio | abierto |",
        "",
        "## Revisión pedagógica independiente",
        "",
        "La redacción mantiene bloques cortos, nueve recapitulaciones, preguntas resolubles y límites físico/perceptuales. Antes del PowerPoint debe realizarse la revisión independiente requerida para U6, con foco en anatomía coclear, potenciales, notación y duración real por encuentro.",
        "",
        "## Criterio de pase",
        "",
        "El texto puede usarse como borrador de trabajo y para revisión docente. No debe pasar a producción final hasta cerrar los problemas de severidad alta o excluir de forma explícita las slides afectadas.",
    ]
    (UNIT / "writing_review.md").write_text("\n".join(out), encoding="utf-8")


def validate_outputs(rows: list[dict[str, str]]) -> None:
    slide_text = (UNIT / "slide_text.md").read_text(encoding="utf-8")
    notes = (UNIT / "speaker_notes.md").read_text(encoding="utf-8")
    source_map = (UNIT / "source_map.md").read_text(encoding="utf-8")
    for row in rows:
        sid = row["slide_id"]
        if slide_text.count(f"### {sid} ") != 1:
            raise ValueError(f"slide_text: ID ausente o duplicado {sid}")
        if notes.count(f"### {sid} ") != 1:
            raise ValueError(f"speaker_notes: ID ausente o duplicado {sid}")
        if source_map.count(f"| {sid} |") != 1:
            raise ValueError(f"source_map: ID ausente o duplicado {sid}")
    required = [
        "**Subtítulo:**", "**Contenido visible:**", "**Ecuaciones:**",
        "**Definiciones:**", "**Ejemplo:**", "**Caption:**", "**Visual:**",
        "**Layout:**", "**Fuente:**", "**Texto alternativo:**",
    ]
    for field in required:
        if slide_text.count(field) != len(rows):
            raise ValueError(f"Campo {field} aparece {slide_text.count(field)} veces")
    if notes.count("**Transición:**") != len(rows):
        raise ValueError("No todas las notas tienen transición")


def main() -> None:
    rows = parse_storyboard()
    write_slide_text(rows)
    write_speaker_notes(rows)
    write_source_map(rows)
    write_review(rows)
    validate_outputs(rows)
    print({
        "slides": len(rows),
        "slide_text": "ok",
        "speaker_notes": "ok",
        "source_map": "ok",
        "writing_review": "ok",
        "conditional": sum(1 for r in rows if "pendiente" in r["status"] or "bloqueada" in r["status"]),
    })


if __name__ == "__main__":
    main()
