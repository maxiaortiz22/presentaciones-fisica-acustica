# Revisión pedagógica independiente — Unidad 4

**Fecha:** 31 de julio de 2026  
**Deck revisado:** `output/unidad_04_sonido_magnitudes_v02.pptx`  
**Render revisado:** `output/render_v02/slide-1.png` a `slide-125.png` y `output/contact_sheet_v02.png`  
**Rol asumido:** segundo docente que recibe el material por primera vez y no considera correctas por defecto las decisiones del storyboard, del deck ni de la revisión anterior.  
**Estado de esta pasada:** revisión solamente. No se modificó el PowerPoint, el storyboard, las notas ni los archivos fuente.

## Dictamen ejecutivo

La unidad cubre de manera sustantiva el programa oficial y, en términos generales, mantiene la exactitud del capítulo del libro. El problema principal no es de cobertura sino de **enseñabilidad**: el material funciona mejor como banco amplio de recursos que como secuencia lista para dictar de principio a fin.

No recomiendo impartir la ruta actual sin una reestructuración previa. La secuencia central declarada contiene 91 slides y aproximadamente 347 minutos según sus propias notas, antes de considerar pausas, demoras reales, resolución de dudas y actividades más extensas. Esto excede la ruta preferida de tres encuentros de 95–100 minutos. Además, varios recursos finales contradicen el andamiaje descrito en el storyboard: muestran fórmulas antes de introducirlas, repiten el mismo gráfico con títulos que prometen operaciones diferentes o reemplazan un ejercicio por una lista de criterios sin datos sobre los cuales decidir.

Resumen de hallazgos abiertos:

- `critical`: 0;
- `major`: 12;
- `minor`: 3;
- `suggestion`: 2.

No se detectó un error científico global que invalide toda la unidad. Sí hay problemas mayores capaces de producir aprendizaje frágil o una interpretación incorrecta: RMS utilizado antes de construirse, simplificación excesiva de la suma coherente, relaciones matemáticas ilegibles en el render y actividades que no permiten demostrar los objetivos declarados.

## Fuentes leídas y método

Se contrastaron:

- el programa oficial, Unidad 4, p. 3;
- el capítulo 4 del libro en LaTeX y en PDF, pp. 89–117;
- `brief.md`, `source_analysis.md`, `storyboard.md` y `storyboard_review.md`;
- `slide_text.md` y las 125 secciones de `speaker_notes.md`;
- `review.md` anterior;
- el PowerPoint v02 y el render completo de las 125 slides, con inspección ampliada de las secuencias conceptualmente más densas.

La evaluación se concentró en cobertura, progresión, prerrequisitos, intuición antes del formalismo, interpretación de fórmulas y gráficos, calidad de ejemplos y preguntas, carga cognitiva, vocabulario, aplicaciones y oportunidades de recuperación.

## Fortalezas que conviene preservar

1. **Cobertura:** están presentes los núcleos obligatorios del programa: naturaleza física/perceptual, generación, elasticidad e inercia, rapidez, campo, presión y velocidad de partícula, impedancia y reflexión, intensidad/potencia/energía, descriptores temporales, RMS, niveles y referencias, coherencia, suma, geometrías, distancia y directividad.
2. **Exactitud general:** las relaciones principales, unidades y referencias coinciden con el capítulo. Las condiciones de validez aparecen con frecuencia y se distingue correctamente entre magnitudes físicas, niveles y percepción.
3. **Errores frecuentes:** se anticipan confusiones valiosas, como `u=c`, media cero igual a señal nula, suma aritmética de dB, equivalencia entre dB SPL y percepción, y aplicación universal de `−6 dB`.
4. **Visualización cuantitativa:** los gráficos de presión/velocidad/intensidad, RMS, presión–nivel y distancia pueden sostener buenas discusiones si se acompañan con preguntas específicas.
5. **Puente profesional:** la medición puntual con micrófono o sonómetro es una aplicación pertinente y prudente; evita inferencias clínicas no sustentadas.

Estas fortalezas justifican corregir y reorganizar el material existente, no rehacer la unidad desde cero.

## Auditoría de carga y viabilidad

Las duraciones registradas en las notas suman 501 minutos para las 125 slides. La ruta central declarada suma 347 minutos para 91 slides. La diferencia con la planificación preferida de tres encuentros de 95–100 minutos es de 47–62 minutos incluso antes de agregar pausas y contingencias de aula.

| tramo actual | slides | tiempo anotado, incluyendo complementarias del tramo |
|---|---:|---:|
| Apertura, fenómeno y medio | 1–22 | 79 min |
| Campo, impedancia, reflexión y energía | 23–42 | 80 min |
| Descriptores y RMS | 43–58 | 63 min |
| Niveles y referencias | 59–68 | 40 min |
| Coherencia y suma | 69–80 | 49 min |
| Geometrías y campos | 81–89 | 33 min |
| Distancia, directividad e integración | 90–109 | 81 min |
| Respaldo | 110–125 | 76 min |

La segmentación en bloques ayuda a orientarse, pero no resuelve por sí sola la sobrecarga. Muchos bloques contienen micro-slides de 2–5 minutos que fragmentan una misma explicación y generan transiciones constantes. Para estudiantes de primer año, esa fragmentación puede aumentar la carga extrínseca: deben reconstruir la continuidad entre slides muy similares en vez de concentrarse en la relación física.

## Hallazgos priorizados

| id | slides / fuente | severidad | hallazgo independiente | impacto pedagógico | estado |
|---|---|---|---|---|---|
| U04-IPR-001 | deck completo; notas; storyboard | major | La ruta central de 347 min no cabe honestamente en los tres encuentros preferidos de 95–100 min. La planificación anterior subestima la duración real. | Obliga a acelerar justamente los bloques de mayor dificultad o a omitir actividades y recapitulaciones. | abierto |
| U04-IPR-002 | 004, 035–039, 051–055, 111 | major | Los prerrequisitos y el orden no están resueltos. U04-004 anticipa un “checklist RMS” antes de instalar el problema; U04-035–038 ya muestran `p_rms` y `I=p_rms²/Z₀`, aunque RMS se construye recién desde U04-051. La versión discreta accesible queda relegada a U04-111, después de la integral. | Se usa una herramienta matemática antes de que el estudiante comprenda qué representa. La ruta exige aceptar símbolos por autoridad. | abierto |
| U04-IPR-003 | 029–032, 035–038, 062–067, 092–094, 099–101 | major | El revelado progresivo descrito por el storyboard no existe en el render final: el recurso completo muestra desde la primera slide fórmulas y conceptos que supuestamente se introducirán después. Ejemplos: `R_p` ya aparece en U04-029; `I=p_rms²/Z₀` aparece en U04-035; `Q` y `DI` aparecen desde U04-099. | La atención se divide entre el concepto actual y formalismos futuros. Los títulos dejan de organizar la lectura. | abierto |
| U04-IPR-004 | 073–079, especialmente 073, 078 y 079 | major | Hay discrepancia entre título, notas y evidencia visible. U04-073 promete interpretar el término de fase, pero no muestra la expresión. U04-078 promete la fórmula de suma de niveles, pero vuelve a mostrar el mismo registro de ruido. U04-079 anuncia un ejemplo de 70 dB + 70 dB, pero no presenta la sustitución ni el cálculo. | El docente debe completar información esencial de memoria y el estudiante no puede seguir ni revisar el razonamiento. | abierto |
| U04-IPR-005 | 071–080, especialmente 072 | major | El árbol de decisión reduce la rama coherente a “sumar presiones en fase: +6,02 dB”. Coherencia no implica fase cero; el resultado depende de la fase relativa. En la rama no correlacionada, “sumar energías” es demasiado amplio para una secuencia que trabaja presión RMS, intensidad y niveles. | Puede consolidar la regla falsa “coherente = +6 dB” y confundir energía física con magnitudes cuadráticas equivalentes. | abierto |
| U04-IPR-006 | 105 y 124 | major | El “caso integrador” no presenta datos de dos fuentes, distancias ni recinto. Solo pide enumerar qué habría que saber. La “solución” repite criterios generales y no resuelve una situación concreta. | No hay transferencia, selección real de modelo ni evidencia de que el estudiante pueda integrar suma, distancia, campo y directividad. | abierto |
| U04-IPR-007 | 120; relación con 054–056 y 111 | major | La slide titulada “Solución del ejercicio de RMS” no contiene señal, muestras, sustitución, resultado ni interpretación. Repite dos fórmulas y una instrucción. | No funciona como solución ni feedback; deja sin modelar la decisión entre fórmula sinusoidal y cálculo general. | abierto |
| U04-IPR-008 | 098–102 | major | La aplicación de directividad quedó pedagógicamente vacía. U04-102 pide comparar patrones a distintas frecuencias, pero no muestra ningún patrón polar. U04-099–101 repiten el mismo esquema y exhiben `Q` y `DI` desde el comienzo. | El estudiante recibe una advertencia válida, pero no aprende a leer ángulo, lóbulo, normalización ni cambio con frecuencia. | abierto |
| U04-IPR-009 | notas completas | major | Las notas están completas en forma, pero demasiado estandarizadas. Tres preguntas genéricas se repiten en 101 de 125 slides: 48 veces “¿Cuál es la idea física central...?”, 34 veces la pregunta sobre magnitud/unidad/condición y 19 veces “¿Qué criterio...?”. También se repite una guía visual genérica 19 veces. | Las notas no reemplazan la preparación de un segundo docente: faltan preguntas de lectura exacta, respuestas intermedias, decisiones de pizarra y tratamiento específico de errores. | abierto |
| U04-IPR-010 | 085, 092, 108 | major | El render corrompe relaciones matemáticas. En U04-085 y U04-092 el símbolo de proporcionalidad aparece como un glifo inválido. En U04-108 `u≠c` queda partido como “u / eq c”. | Se vuelven ilegibles relaciones centrales de geometría y un objetivo de cierre. Es un problema visual con consecuencia conceptual directa. | abierto |
| U04-IPR-011 | 029–041 | major | Impedancia, reflexión, intensidad instantánea/media, potencia y energía se concentran en una secuencia formal muy densa. Se introducen `Z`, `Z₀`, `R_p`, `i`, `I`, `W_ac`, `E_ac`, integrales y varias hipótesis en aproximadamente una hora. La nota de U04-029 añade que `Z` es “compleja en general”, sin necesidad pedagógica ni prerrequisito de números complejos. | Es probable que estudiantes memoricen fórmulas y condiciones sin construir un modelo físico integrado. | abierto |
| U04-IPR-012 | 033, 042, 050, 058, 068, 080, 089, 107–108 | major | Hay recapitulaciones frecuentes, pero varias son mapas declarativos o matrices ya completadas. Solo algunas exigen producir una respuesta verificable. U04-108 intenta hacerlo, pero incluye el texto matemático corrupto y seis prompts simultáneos. | La presencia de “recap” no garantiza recuperación. Falta evidencia formativa antes de avanzar a bloques dependientes. | abierto |
| U04-IPR-013 | 086; también 064, 084, 095 y 097 | minor | Los gráficos logarítmicos se usan como si la lectura de escala ya estuviera consolidada. U04-086 combina ejes logarítmicos, potencias y rótulos poco familiares sin un puente previo desde duplicaciones de área. | El estudiante puede leer la pendiente como una tendencia visual sin comprender la razón física ni la escala. | abierto |
| U04-IPR-014 | 011–013, 042, 102–105 | minor | Las aplicaciones son pertinentes pero superficiales. Voz y parlante ilustran la fuente; sonómetro ilustra la medición; ninguna aplicación central obliga a elegir una magnitud, estimar un resultado y justificar límites con datos. U04-104 introduce “ponderación” y “respuesta temporal” sin definirlas. | La conexión con Fonoaudiología queda en el nivel de mención y no alcanza a demostrar transferencia profesional. | abierto |
| U04-IPR-015 | 024–032, 043–068, 071–088 | minor | El vocabulario técnico se acumula con pocas reformulaciones en lenguaje cotidiano: campo, impedancia específica, valor eficaz, referencia, no correlacionada, frente, campo difuso y directividad. “Señal compleja” puede confundirse con número complejo; “avance de fase” es innecesariamente avanzado para distinguir `u` y `c`. | Aumenta la carga verbal y dificulta que el estudiante explique con sus palabras. | abierto |
| U04-IPR-016 | 031–032 y 084–086 | suggestion | La reflexión y la propagación cilíndrica tienen tratamiento conceptual, pero sus ejemplos numéricos aparecen solo en respaldo (U04-113 y U04-117). | Un ejemplo corto en la ruta principal permitiría comprobar que se entendió el modelo y no solo la definición. | abierto |
| U04-IPR-017 | deck completo | suggestion | La unidad sobre sonido no incorpora todavía una comparación auditiva controlada. | Un audio breve puede reforzar media frente a RMS o suma coherente frente a no correlacionada, siempre con alternativa estática y sin convertir percepción en prueba de una magnitud física. | abierto |

## Discrepancias con la revisión anterior

La revisión anterior fue útil para corregir colisiones, fuentes, referencias, alt text y varios recursos equivocados. Sin embargo, su criterio de cierre fue principalmente técnico y de legibilidad. Esta segunda lectura no considera suficientes algunas correcciones dadas por resueltas:

- **U04-102:** retirar el patrón polar inexistente eliminó una consigna imposible, pero dejó una aplicación sin evidencia visual. Se reabre como `major` pedagógico.
- **U04-105 y U04-124:** sustituir el visual incorrecto por listas editables eliminó una incoherencia gráfica, pero no creó un caso resoluble ni una solución. Se reabren como `major` pedagógico.
- **U04-120:** retirar el diagrama ajeno y mostrar las fórmulas correctas eliminó el error de contenido, pero no produjo la solución anunciada. Se reabre como `major` pedagógico.
- **Secuencias repetidas:** la revisión anterior las dejó como `minor` por considerarlas revelado progresivo. El render muestra que el contenido futuro ya está visible desde la primera slide y que algunos títulos no coinciden con el recurso. Se escala a `major`.
- **Fidelidad matemática del render:** aunque la revisión anterior declaró resueltos los restos de LaTeX, U04-085, U04-092 y U04-108 conservan relaciones semánticamente dañadas.

## Evaluación por dimensión pedagógica

### Secuencia y prerrequisitos

La macrosecuencia fenómeno → medio → campo → magnitudes → niveles → suma → geometría es razonable. El problema aparece dentro de los bloques y entre B04 y B06. RMS es prerrequisito operativo de `I=p_rms²/Z₀`, pero se formaliza después. La integral aparece antes que la aproximación discreta, pese a que el curso no presupone cálculo integral.

La mejor solución no es agregar más explicaciones a las mismas slides, sino cambiar el orden:

1. construir primero promedio y RMS mediante muestras o áreas cualitativas;
2. introducir después la notación integral como forma compacta o complementaria;
3. volver a intensidad media y a `I=p_rms²/Z₀` una vez que RMS tenga significado;
4. dejar `R_p` algebraico y la impedancia compleja fuera de la ruta esencial salvo que exista tiempo real.

### Intuición, formalismo y fórmulas

Las notas dicen “pregunta física antes de ecuación”, pero el render a menudo exhibe la ecuación futura desde el inicio. En B03–B04 la intuición debería apoyarse en una sola escena persistente: una fuente, dos puntos, una interfaz y una superficie imaginaria. Cada magnitud respondería una pregunta sobre esa escena. Hoy el estudiante cambia de esquema y de conjunto de símbolos demasiado rápido.

Para cada fórmula central debe quedar visible, no solo en notas:

- qué pregunta responde;
- qué magnitud entrega y en qué unidad;
- qué datos necesita;
- bajo qué condiciones vale;
- un caso simple donde no debe usarse.

### Gráficos y diagramas

Los gráficos son potencialmente valiosos, pero necesitan consignas observables. “¿Qué magnitud entrega esta relación?” no ayuda a leer una curva. Conviene preguntar, por ejemplo:

- U04-036: “¿Por qué `i(t)` sigue positiva cuando `p` y `u` son negativas?”;
- U04-044: “Leé `p_max`, `p_min`, `p_pp` y la media en el mismo registro”;
- U04-053–054: “¿Qué cambia en la unidad al cuadrar y al extraer raíz?”;
- U04-064: “Ubicá una multiplicación por 2 y por 10 en presión y compará los saltos de nivel”;
- U04-072–075: “Predecí el resultado antes de mostrar la suma”;
- U04-086: “Primero duplicá el área; recién después ubicá la pendiente en escala logarítmica”;
- U04-095: “Compará 1→2 m y 2→4 m antes de formular la regla”.

Un diagrama no está pedagógicamente resuelto solo porque no tenga colisiones. Si contiene todas las respuestas antes de tiempo o no representa la operación indicada por el título, también falla.

### Ejemplos, práctica y feedback

Hay ejemplos numéricos correctos para presión–intensidad, RMS sinusoidal, dB y distancia. Faltan ejemplos centrales de reflexión y propagación cilíndrica. Sobre todo, falta un problema integrador con datos y una solución que modele decisiones.

El capítulo ofrece un banco de ejercicios más rico que el deck actual: lectura de gráficos, problemas guiados, aplicaciones e integradores. Conviene adaptar un caso del capítulo —por ejemplo el integrador I1— en vez de reemplazarlo por una lista abstracta de datos que “habría que conocer”.

### Recapitulaciones y repetición

La frecuencia de recapitulaciones es adecuada para una unidad densa. Su función debe cambiar de “volver a mostrar el mapa” a “obtener una respuesta”. Una recapitulación útil podría pedir:

- elegir una magnitud y justificarla;
- detectar la condición que falta;
- predecir el signo o el orden de magnitud;
- interpretar un punto de un gráfico;
- explicar por qué dos reglas numéricas parecidas (`+3`, `+6`, `−6`) no son intercambiables.

La repetición visual de 029–032, 035–038, 077–079, 092–094 y 099–101 no produce por sí sola práctica espaciada; en varios casos es repetición pasiva.

### Vocabulario y aplicaciones

Conviene acompañar cada término técnico con una reformulación estable:

- campo acústico: “qué valor hay en cada lugar y momento”;
- velocidad de partícula: “movimiento local del medio”;
- impedancia: “relación entre presión y movimiento bajo condiciones dadas”;
- RMS: “tamaño cuadrático efectivo durante una ventana”;
- no correlacionadas: “sin relación de fase estable durante la observación”;
- directividad: “cómo cambia la radiación con la dirección”.

“Impedancia compleja” debe quedar fuera de la explicación central. “Señal compleja” debe aclararse como “compuesta/no sinusoidal” para evitar la lectura matemática. “Ponderación” y “respuesta temporal” en U04-104 deben definirse en una línea o reservarse para U10.

## Propuesta priorizada de cambios

### Imprescindibles

1. **Definir una ruta realista antes de editar contenido.** Elegir explícitamente entre:
   - una ruta completa de cinco o seis encuentros de 60–80 minutos; o
   - una ruta esencial de tres encuentros, reducida a aproximadamente 65–75 slides y 210–240 minutos de exposición/actividad prevista, con el resto como complementario o respaldo.
2. **Corregir el orden RMS–intensidad.** Retirar `p_rms` de U04-035–037; construir RMS con muestras antes de la integral; ubicar `I=p_rms²/Z₀` después de que RMS haya sido comprendido o convertirlo en reentrada explícita.
3. **Reconstruir los revelados.** En 029–032, 035–038, 062–067, 092–094 y 099–101, cada slide debe mostrar solo la información necesaria para su propósito. No debe aparecer la fórmula que se explicará dos slides después.
4. **Rehacer la secuencia de suma.** Mostrar dos señales de entrada y su suma; formular primero `p_total(t)`; diferenciar luego fase cero, fase intermedia y oposición; reservar `+6,02 dB` para el caso coherente en fase. En no correlacionadas, hablar de suma de cuadrados RMS/intensidades equivalentes antes de convertir a nivel.
5. **Hacer visibles las fórmulas y los pasos que los títulos prometen.** U04-073, U04-078 y U04-079 necesitan respectivamente el término de fase, la suma logarítmica y el ejemplo completo con estimación, sustitución, resultado y condición.
6. **Crear un caso integrador resoluble y su solución.** U04-105 debe incluir datos suficientes y al menos un dato deliberadamente faltante o una condición a decidir. U04-124 debe resolver exactamente ese caso, no repetir una lista de criterios. Adaptar un ejercicio integrador del capítulo es preferible a inventar una situación nueva.
7. **Convertir U04-120 en una solución real.** Incluir una senoide con pico dado y una señal no sinusoidal con muestras dadas; calcular ambos RMS paso a paso y cerrar con la decisión sobre cuándo vale `pico/√2`.
8. **Restituir una práctica real de directividad.** Incorporar dos patrones polares rotulados por frecuencia y condiciones, con una consigna de lectura. Si no se aprueba el recurso, reclasificar U04-102 como advertencia y no presentarla como aplicación resuelta.
9. **Corregir la fidelidad matemática del render.** Reparar `∝` en U04-085 y U04-092 y `u≠c` en U04-108; volver a renderizar y verificar a tamaño de aula.
10. **Reescribir las notas de la ruta central.** Sustituir las preguntas genéricas por preguntas específicas para cada gráfico, ecuación y caso. Incluir respuesta esperada, error probable, una pregunta de seguimiento y qué escribir o señalar en pizarra.
11. **Convertir recapitulaciones en evaluación formativa.** Al menos U04-033, 042, 058, 068, 080 y 089 deben exigir una decisión o explicación breve antes de revelar la respuesta. U04-108 debe reducirse a dos o tres prompts o dividirse.

### Recomendados

1. **Reducir fragmentación sin perder profundidad.** Candidatas a consolidación o reordenamiento:
   - 016–019: mantener el movimiento longitudinal y reunir elasticidad–inercia–propagación en dos pasos bien conectados;
   - 029–032: definición intuitiva, interfaz/casos límite y fórmula opcional;
   - 044–050: combinar instantáneo/pico y pico a pico; usar una sola recapitulación activa;
   - 052–055: proceso gráfico, cálculo discreto y caso sinusoidal; integral después;
   - 091–097: intuición geométrica, relación de nivel, ejemplo y límites, sin repetir tres veces el mismo esquema;
   - 099–102: cuatro recursos realmente distintos: patrón, `Q`, `DI`, aplicación.
2. **Mover formalismo no esencial.** Mantener `R_p`, integrales continuas, correlación parcial e impedancia compleja en complementarias/respaldo salvo necesidad docente explícita.
3. **Agregar un ejemplo breve de reflexión y uno cilíndrico en la ruta principal.** Pueden ser predicciones cualitativas o cálculos de una sola operación.
4. **Enseñar lectura de ejes logarítmicos.** Antes de U04-086, usar una tabla de duplicaciones o una comparación de áreas; no asumir familiaridad con pendientes en log–log.
5. **Profundizar dos aplicaciones en vez de nombrar muchas.** Una de voz/generación y una de medición/calibración deberían incluir variable, unidad, decisión y límite del modelo.
6. **Usar una escena física recurrente.** Un parlante, un micrófono, dos posiciones y una interfaz pueden sostener `p`, `u`, `Z`, `I`, distancia y directividad sin cambiar de contexto en cada slide.
7. **Añadir reformulaciones cotidianas estables** para el vocabulario avanzado y verificar que todo término nuevo aparezca definido antes de ser usado en una consigna.
8. **Separar físicamente rutas en el archivo.** Señalar en el mapa y en notas qué slides son esenciales, complementarias y de respaldo, y preparar saltos de navegación que permitan dictar cada ruta sin improvisar.

### Opcionales

1. Incorporar una comparación auditiva breve y controlada para suma coherente/no correlacionada o para señales con igual media y distinto RMS, siempre con alternativa estática.
2. Preparar una hoja de trabajo de una página con tablas incompletas, gráficos para anotar y el caso integrador; evitar que la slide sea simultáneamente explicación, consigna y solución.
3. Crear una versión docente con pasos de revelado y una versión de lectura autónoma consolidada.
4. Añadir una demostración sencilla con sonómetro o micrófono calibrado para discutir punto, distancia, orientación y ajustes, sin prometer inferencias perceptuales.
5. Usar el apéndice como banco de respuesta adaptativa: cada slide de respaldo debe indicar desde qué slide central se invoca y a cuál se regresa.

## Secuencia recomendada de trabajo posterior

1. decidir duración y número real de encuentros;
2. editar el storyboard y reclasificar la ruta central;
3. corregir el orden de RMS/intensidad y la lógica de suma;
4. diseñar ejercicios y soluciones antes de rediseñar sus slides;
5. corregir los recursos repetidos y los símbolos dañados;
6. reescribir las notas de la ruta central;
7. renderizar todas las slides afectadas;
8. hacer una segunda revisión pedagógica sobre la nueva ruta, incluyendo una simulación cronometrada de al menos un bloque denso.

## Problemas abiertos al terminar la primera pasada

Todos los hallazgos quedaron abiertos en esta instancia porque la primera pasada no autorizaba modificar el deck. No se detectaron problemas `critical`; se identificaron doce problemas `major` que debían tratarse antes de considerar la secuencia lista para uso docente sin preparación adicional.

La cobertura del programa no necesitaba ampliarse. La prioridad indicada fue reducir carga extrínseca, reparar la progresión, transformar recapitulaciones en evidencia y devolver a los ejercicios sus datos, razonamiento y feedback.

## Actualización posterior a las correcciones

La condición de independencia de la primera pasada se preserva: no se reescriben sus hallazgos ni sus prioridades. Después de esa revisión se corrigió el deck y se realizó una segunda verificación sobre el PPTX y el render final.

- nueve hallazgos `major` quedaron resueltos;
- tres quedaron aceptados con condición pedagógica explícita: notas genéricas residuales, densidad del bloque formal y uso activo de algunas recapitulaciones;
- no queda ningún problema `critical` ni `major` sin tratamiento.

La trazabilidad individual y la evidencia de cierre se registran en `review.md`, sección “Cierre final posterior a la revisión pedagógica independiente”, y se resumen en `final_report.md`.
