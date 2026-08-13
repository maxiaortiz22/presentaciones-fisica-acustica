# Unidad 10 — Brief pedagógico

## Identificación

- **Unidad:** 10.
- **Título oficial del programa:** Ruidos.
- **Título de trabajo solicitado y del capítulo:** El ruido y su caracterización.
- **Etapa:** estudio de fuentes y brief pedagógico; anterior al storyboard.
- **Público:** estudiantes de primer año de la Licenciatura en Fonoaudiología.
- **Carga conceptual global:** alta, con dos núcleos de carga muy alta.
- **Pregunta organizadora:** ¿qué necesitamos describir de una señal para decidir si interfiere, expone, enmascara o requiere control?
- **Evidencia mínima:** clasificar un ruido temporal y espectralmente, elegir descriptores compatibles con la pregunta y justificar una estrategia de control sin confundir medición, percepción, salud y procedimiento clínico.

La unidad funciona como cierre integrador del curso. Recupera magnitudes y niveles, análisis frecuencial, percepción, audiometría, exposición y propagación para estudiar señales variables en contexto. El riesgo pedagógico principal es presentar una lista de “tipos de ruido” sin conectar **forma temporal, estadística, espectro, función y condiciones de medición**. El segundo riesgo es extender el capítulo hasta convertirlo en un curso independiente de estadística, higiene ocupacional o enmascaramiento clínico.

## Fuentes y limitaciones de esta etapa

Se consultaron el programa oficial 2025; `course_map.md`; `course_dependency_map.md`; `content_coverage_matrix.csv`; el capítulo LaTeX `context/libro_latex/chapters/10-ruido-caracterizacion.tex`; sus figuras, diagramas y script reproducible; el libro PDF, pp. PDF 261–290; y las tres guías de `style/` solicitadas.

LaTeX y PDF son sustantivamente concordantes. El programa es más breve que el capítulo. La brecha principal es la “revisión de la técnica de enmascaramiento”: el libro explica su función y sus límites, pero no desarrolla un protocolo clínico completo. No se incorporaron fuentes externas nuevas ni valores normativos en esta etapa.

## Función dentro del curso

La Unidad 10:

1. recupera de U4 media, RMS, niveles y suma energética;
2. aplica de U5 tiempo, espectro, bandas, filtros, ponderaciones, sonómetro y nivel equivalente;
3. recupera de U7 enmascaramiento, SNR e inteligibilidad;
4. conserva de U8 la separación entre exposición, síntoma, función y resultado de prueba;
5. integra de U9 propagación, acondicionamiento, aislamiento, cabinas y control del trayecto;
6. cierra el curso con decisiones sobre caracterización, medición, aplicación y límites de inferencia.

No prepara una unidad posterior del plan, porque es la última. Sí prepara la integración profesional futura: leer mediciones, documentar condiciones, conversar con equipos de Audiología e Higiene y Seguridad y reconocer cuándo se necesita una norma o un protocolo específico.

## Alcance obligatorio del programa

El programa oficial 2025, p. 5, exige:

- tipos de ruido y su clasificación;
- diferencia entre ruido y sonido;
- ruido aleatorio;
- ruido blanco;
- ruido rosa;
- ruido vocal;
- ruido de banda estrecha (NBN);
- revisión de la técnica de enmascaramiento.

Todo este alcance debe quedar en la ruta central. Se adoptará **ruido con espectro de habla** o **ruido con forma espectral vocal** como denominación técnica preferida, aclarando una vez que corresponde al “ruido vocal” del programa.

## Profundidad prevista y límites

La ruta central debería permitir:

- separar sonido físico, señal medida y valoración contextual como ruido;
- distinguir señal determinística, proceso aleatorio y realización;
- interpretar estacionariedad según intervalo de observación;
- clasificar ruido continuo, fluctuante, intermitente e impulsivo sin tratarlos como categorías excluyentes;
- diferenciar media, RMS, varianza y distribución;
- conectar densidad espectral, ancho de banda y valor cuadrático integrado;
- explicar blanco por hertz y rosa por octava;
- especificar ruido con espectro de habla y NBN mediante banda, nivel, equipo y procedimiento;
- diferenciar nivel instantáneo, máximo, pico y equivalente;
- calcular SNR bajo condiciones comparables y limitar su interpretación perceptual;
- explicar la función del enmascarante y distinguirlo del ruido de fondo y de la protección auditiva;
- organizar controles en fuente, trayecto y receptor.

No corresponde en la ruta central:

- desarrollar probabilidad formal, inferencia estadística o teoremas de procesos aleatorios;
- derivar PSD desde autocorrelación ni formalizar Fourier estocástica;
- presentar ruido blanco o rosa como señales ideales de ancho infinito;
- convertir una SNR física en predicción automática de inteligibilidad, molestia o riesgo;
- fijar límites de exposición, dosis, atenuación de protectores o ruido admisible sin norma, edición y jurisdicción;
- enseñar una receta de enmascaramiento audiométrico sin protocolo clínico vigente;
- recomendar niveles o sonidos terapéuticos para tinnitus;
- certificar una cabina o una medición con una aplicación telefónica.

## Objetivos de aprendizaje propuestos

Al finalizar la unidad, el estudiante podrá:

1. **Diferenciar** fenómeno sonoro, señal medida y valoración contextual como ruido mediante ejemplos de comunicación, medición y prueba.
2. **Clasificar** señales como determinísticas o aleatorias y reconocer estacionariedad y categorías temporales a partir de registros representativos.
3. **Calcular e interpretar** media, RMS y varianza, explicando qué información agrega una distribución de amplitudes.
4. **Relacionar** densidad espectral, ancho de banda y contenido cuadrático para comparar ruido blanco, rosa, con espectro de habla y NBN.
5. **Seleccionar e interpretar** descriptores temporales y de nivel —máximo, pico, equivalente y, si se incluye, percentiles— declarando ponderación e intervalo.
6. **Calcular y contextualizar** una SNR sin convertirla por sí sola en una conclusión perceptual o clínica.
7. **Explicar** el papel de una señal enmascarante en audiometría y distinguir enmascaramiento, ruido de fondo y protección auditiva.
8. **Proponer** medidas de control en fuente, trayecto y receptor y reconocer qué decisiones exigen medición calibrada, norma o protocolo.

## Conocimientos previos

### Deben recordarse

- magnitud, símbolo, unidad, referencia y consistencia dimensional;
- presión acústica `p(t)`, media y `p_rms`;
- niveles logarítmicos y diferencia entre magnitud lineal y dB;
- tiempo, frecuencia, espectro, banda, filtro, `f_L`, `f_c`, `f_H` y ancho de banda;
- ponderaciones A, C y Z, respuesta temporal del sonómetro y `L_eq,T`;
- señal, sistema y respuesta en frecuencia;
- enmascaramiento, señal objetivo, enmascarador y SNR;
- dB SPL, dB HL y dB SL como escalas no intercambiables;
- exposición, TTS, pérdida auditiva inducida por ruido y tinnitus sin inferencia diagnóstica automática;
- absorción, aislamiento, reverberación, transmisión y cabina audiométrica.

### No se debe asumir dominado

- diferencia entre proceso aleatorio y una realización;
- estacionariedad dependiente de la ventana;
- distinción entre media, RMS y varianza;
- unidades de una densidad espectral;
- integración de una densidad sobre una banda;
- diferencia blanco/rosa cuando se agrupa por octavas;
- diferencia entre `L_max`, `L_peak` y `L_eq,T`;
- promedio energético de niveles;
- alcance real de una SNR;
- función del oído no evaluado en el enmascaramiento audiométrico;
- jerarquía de control y diferencia entre resultado y mecanismo.

## Conceptos difíciles y errores previsibles

| Nudo | Dificultad | Tratamiento recomendado |
|---|---|---|
| Sonido frente a ruido | Se busca una diferencia física absoluta. | Una misma señal en tres tareas: conversación, medición y enmascaramiento. |
| Aleatoriedad | “Impredecible” se interpreta como “inmedible”. | Separar muestra instantánea de propiedades estadísticas. |
| Estacionariedad | Se confunde con valor constante. | Comparar ventanas breves y largas de una misma señal. |
| Media, RMS y varianza | Las fórmulas parecen redundantes. | Muestras sencillas y dos señales con igual RMS pero distinta distribución. |
| PSD y banda | Se confunden `Pa²/Hz`, `Pa²` y nivel en dB. | Rectángulo área = densidad × ancho antes de usar la integral. |
| Blanco frente a rosa | Se memoriza el color sin el criterio de agrupamiento. | Comparar bandas de igual ancho en Hz y octavas sucesivas. |
| Descriptores de nivel | Se intercambian máximo, pico, equivalente e Impulse. | Tabla pregunta–detector–intervalo–ponderación. |
| Promedio de dB | Se aplica media aritmética. | Contraste numérico entre promedio aritmético y energético. |
| SNR | Se convierte en inteligibilidad universal. | Misma SNR con variables perceptuales declaradas como faltantes. |
| Enmascaramiento | Se confunde con proteger el oído. | Diagrama de señal de prueba, ruta cruzada, oído no evaluado y enmascarante. |
| Control | Absorción, aislamiento y reducción se usan como sinónimos. | Fuente–trayecto–receptor y mecanismo–métrica antes/después. |
| Normativa | Un número en dB(A) se toma como criterio universal. | Exigir descriptor, intervalo, población, norma, edición y jurisdicción. |

## Aplicaciones prioritarias

1. Evaluación auditiva: ruido ambiente, señales de prueba y enmascaramiento introductorio.
2. Comunicación en aula o consultorio: SNR, reverberación y ruido de fondo.
3. Voz y habla: ruido con espectro de habla y límites de inferir inteligibilidad.
4. Cabinas audiométricas: necesidad de bandas, vía, transductor y procedimiento.
5. Salud ocupacional y comunitaria: descriptor de exposición y lectura crítica de documentos.
6. Acufenometría: comparación con tonos o ruidos, sin prescripción terapéutica.
7. Control de ruido: selección inicial de acciones en fuente, trayecto o receptor.

## Bloques pedagógicos preliminares y carga cognitiva

Esta tabla agrupa núcleos; **no es un storyboard ni fija slides individuales**.

| Bloque preliminar | Pregunta guía | Contenido dominante | Carga | Medida de alivio |
|---|---|---|---|---|
| 1. Puente y contexto | ¿Cuándo una señal funciona como ruido? | Sonido, señal, tarea, receptor y contexto. | Media | Caso de consultorio junto a avenida. |
| 2. Variación temporal | ¿Qué puede predecirse y qué debe describirse? | Determinístico, aleatorio, realización, estacionariedad y clasificación temporal. | Alta | Registros coordinados y actividad de clasificación. |
| 3. Estadística mínima | ¿Qué conserva cada descriptor? | Media, RMS, varianza, distribución e histograma. | Muy alta | Ejemplo con pocas muestras, visual igual RMS/diferente distribución y recapitulación. |
| 4. Espectro y tipos obligatorios | ¿Qué significa “igual por Hz” o “igual por octava”? | PSD, banda, blanco, rosa, espectro de habla y NBN. | Muy alta | Área bajo curva, comparación por bandas y audios normalizados con alternativa visual. |
| 5. Medición y SNR | ¿Qué pregunta responde cada número? | `L(t)`, máximo, pico, equivalente, percentiles, SNR y fondo. | Alta | Matriz de descriptores, cálculo breve y caso aplicado. |
| 6. Enmascaramiento aplicado | ¿Qué señal se presenta, a qué oído y con qué finalidad? | Fenómeno de U7, función audiométrica, ruta cruzada y límites del protocolo. | Alta | Diagrama funcional y contraste con protección. |
| 7. Exposición y control | ¿Qué puede medirse, inferirse y modificarse? | Exposición, comunicación, documentos, fuente–trayecto–receptor y términos de control. | Alta | Separar tres planos de inferencia y clasificar intervenciones. |
| 8. Integración y cierre | ¿Cómo se caracteriza un problema real sin saltar pasos? | Caso integrador, errores, recapitulación y transferencia profesional. | Media–alta | Plan de caracterización con decisiones justificadas. |

Los bloques 3 y 4 no deberían impartirse seguidos sin una recapitulación. El bloque 6 requiere una advertencia explícita de que el diagrama no es una receta clínica.

## Extensión probable

Sin imponer un máximo y antes de conocer la duración de los encuentros:

- **ruta central:** aproximadamente 50–64 slides;
- **material complementario integrado:** 10–16 slides;
- **respaldo y soluciones:** 10–18 slides;
- **deck completo probable:** 65–90 slides, según práctica, audios y profundidad normativa.

Una clase única obligaría a omitir práctica o a comprimir conceptos incompatibles con el nivel de ingreso. La previsión razonable es de dos encuentros largos o tres encuentros con práctica distribuida. Esta estimación deberá revisarse al decidir tiempos y recién entonces pasar al storyboard.

## Distribución preliminar por prioridad

### Parte central

- alcance completo del programa;
- clasificación temporal y estacionariedad;
- media/RMS/varianza como soporte para ruido aleatorio;
- PSD y contenido de banda suficientes para blanco/rosa;
- especificación de ruido con espectro de habla y NBN;
- descriptores máximo, pico y equivalente;
- SNR, ruido de fondo y enmascarante;
- enmascaramiento audiométrico funcional, sin protocolo;
- control fuente–trayecto–receptor;
- errores frecuentes y un caso integrador.

### Material complementario

- distribución e histograma con mayor detalle;
- derivación de contenido constante por octava;
- percentiles `L_n,T`;
- promedio energético de varios intervalos;
- exposición, dosis y lectura de tipos de documento;
- cancelación activa, acufenometría y protección auditiva con límites explícitos;
- ejercicios adicionales y demostraciones de audio.

### Slides de respaldo

- derivaciones y soluciones completas;
- casos numéricos adicionales;
- metadatos de normas y documentos;
- tablas normativas solo después de obtener fuente autorizada y decidir aplicabilidad;
- detalles de calibración, transductores y procedimientos;
- protocolo clínico de enmascaramiento, únicamente si la cátedra define una fuente específica.

## Condición de entrada al storyboard

Antes de crear `storyboard.md` deben resolverse: duración y número de encuentros; profundidad estadística; peso central de métricas de exposición; alcance clínico del enmascaramiento; notación visible; selección de ejercicios; estrategia de audios y seguridad; reconstrucción de visuales; fuentes normativas aplicables; y actualización o no de los localizadores desfasados de la matriz de cobertura.
