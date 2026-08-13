# Informe de consistencia — Unidad 10: Ruidos

**Fecha de revisión:** 12 de agosto de 2026  
**Presentación revisada:** `output/unidad_10_ruidos_v02.pptx`  
**Alcance:** comparación de la presentación editable y del render completo de sus 93 diapositivas con el sistema visual, el mapa del curso, el glosario, la guía de notación, el template y las Unidades 1–9 finalizadas.

## Dictamen

La Unidad 10 pertenece de forma clara al mismo curso y mantiene su identidad académica, visual y pedagógica. La cobertura, la secuencia integradora, la paleta, la tipografía, los layouts, los pies, los créditos, el estilo de gráficos y la gramática de diagramas son coherentes con la línea consolidada en las unidades anteriores.

Las diferencias de ritmo y composición son **intencionales**: la unidad debe integrar estadística, espectro, exposición, percepción, medición y control. Por eso usa más diagramas de clasificación, flujos de decisión y recapitulaciones de encuentro que una unidad conceptual temprana. Esta diferencia no debe homogeneizarse.

Quedan tres inconsistencias locales que no impiden reconocer la unidad como parte del curso, pero conviene corregir en una futura edición localizada:

1. varios símbolos matemáticos visibles conservan guiones bajos o subíndices planos;
2. algunos gráficos generados usan punto decimal y notación científica anglosajona;
3. muchas notas del orador repiten instrucciones genéricas o campos sin acción real.

También permanecen decisiones globales que no corresponde resolver corrigiendo solo U10: umbral OMML/texto matemático/SVG, color definitivo de títulos y criterio técnico para tablas nativas frente a retículas de formas editables.

## Referencias comparadas

- `AGENTS.md`.
- `course_map.md`, `course_dependency_map.md`, `content_coverage_matrix.csv` y `course_consistency_report.md`.
- `style/presentation_style_guide.md`, `style/slide_master_spec.md`, `style/layout_catalog.md` y `style/component_catalog.md`.
- `style/glossary.md`, `style/notation_guide.md` y `style/decision_log.md`.
- `output/fisica_acustica_template_v01.pptx` y `style/template_mosaic.png`.
- Presentaciones finales y renders de las Unidades 1–9.
- Storyboard, texto, notas, manifiesto, revisión, PowerPoint v02 y render completo de la Unidad 10.

## Evidencia estructural

| Indicador | Template / curso | Unidad 10 | Evaluación |
|---|---|---|---|
| Formato | 16:9 | 16:9 | Coincide |
| Masters y layouts disponibles | 2 masters; 27 layouts | 2 masters; 27 layouts | Coincide |
| Variedad de layouts usada | Variedad controlada | 23 layouts en 93 slides | Coherente; evita slides clonadas |
| Extensión | U1–U9: 94–150 slides | 93 slides | Aceptable; alcance completo y cierre integrador |
| Tipografía dominante | Calibri Light, Calibri, Cambria Math | Las mismas tres familias | Coincide |
| Paleta dominante | Bordó, carbón, gris, teal y ocre | Las mismas familias cromáticas | Coincide |
| Notas | Notas por slide y fuentes trazables | 93/93 slides con notas y bloque de fuentes | Cobertura completa; redacción mejorable |
| Numeración visible | Convención automática; precedente local por compatibilidad en U9 | 93/93 slides numeradas mediante objeto local | Aceptable como solución compatible; no cambia la preferencia global |
| Multimedia | Solo cuando cumple una función didáctica | Sin audio ni video embebido | Aceptable; no era necesario para cubrir la unidad |
| Tablas nativas | Preferidas por la guía | Retículas editables construidas con formas | Visualmente coherente; implementación global por decidir |
| Ecuaciones OMML | Umbral no resuelto | Sin OMML; texto matemático editable | Requiere decisión global |

## Matriz de consistencia

Las categorías usadas son exactamente: **intencional**, **aceptable**, **inconsistente** y **requiere decisión**.

| Dimensión | Línea base del curso | Unidad 10 | Clasificación | Impacto y recomendación |
|---|---|---|---|---|
| Cobertura curricular | Tipos de ruido; diferencia sonido/ruido; aleatorio, blanco, rosa, vocal, NBN; repaso de enmascaramiento | Cubre todos los mínimos y añade estadística, PSD, exposición, fondo, SNR y control previstos por el libro y el mapa | aceptable | La ampliación está justificada y distingue lo central de lo complementario. |
| Dependencias | U10 integra U4, U5, U7, U8 y U9 | Recupera magnitudes, espectro, percepción, estudios y propagación antes de aplicarlos | aceptable | La secuencia respeta el mapa de dependencias. |
| Nivel de profundidad | Profundidad alta, con límites clínicos y normativos explícitos | Desarrolla modelos y descriptores sin convertirlos en protocolo clínico completo ni norma universal | intencional | Mantener este límite; evita sobreextender el alcance. |
| Arquitectura de ruta | Las unidades densas pueden separar central, complementaria y respaldo si la clasificación es operativa | 74 slides centrales, 10 complementarias, 7 de respaldo y 2 de fuente bloqueada | aceptable | La clasificación es real y permite adaptar la clase. |
| Relación sonido/ruido | “Ruido” depende del contexto; no hay frontera física absoluta | Abre con la distinción entre fenómeno físico, señal medida y criterio contextual | aceptable | Coherente con el glosario y con la progresión desde U4. |
| “Ruido vocal” | El programa usa el término; el glosario prefiere “ruido con espectro de habla” | Presenta el término del programa y lo corrige académicamente en la misma secuencia | intencional | Conservar el puente terminológico para que el estudiante reconozca ambas expresiones. |
| Ruido aleatorio y estacionariedad | Aleatorio no significa blanco ni estacionario | La unidad separa realización, estadística, espectro y escala temporal | aceptable | Evita uno de los errores conceptuales previstos por el mapa. |
| Fondo, enmascarador y protección | Son roles distintos en física, audiología y prevención | Los diferencia y muestra que una misma señal puede desempeñar papeles diferentes | aceptable | Convención incorporada al glosario y al registro de decisiones. |
| Símbolos de presión y estadística | `p(t)`, media, RMS, varianza y duración declarada | Usa las mismas magnitudes y explica su relación | aceptable | Consistencia conceptual y dimensional correcta. |
| PSD genérica y de presión | `S_x(f)` era la forma genérica; el mapa de U10 ya preveía `S_pp(f)` | Usa `S_pp(f)` para PSD unilateral de presión | aceptable | Se actualizó la guía: es un caso específico, no una notación paralela. |
| Integración en banda | Deben declararse banda, magnitud y referencia | Usa `p_{B,\mathrm{rms}}` y relaciona PSD con presión eficaz de banda | aceptable | Convención añadida a la guía de notación. |
| Descriptores temporales | `L_Aeq,T`, `L_AFmax` y `L_Cpeak` cuando la configuración es conocida | Usa también `L_max,F` y `L_peak` en comparaciones conceptuales sin ponderación frecuencial fijada | aceptable | Se admite solo en contexto conceptual; en informes usar descriptor completo. |
| Niveles de excedencia | Deben expresar porcentaje, intervalo y configuración | Introduce `L_N,T` y advierte que `L_90` no equivale universalmente a fondo | aceptable | Convención incorporada a glosario, notación y decisiones. |
| Subíndices visibles | Los subíndices deben ser tipográficos; el guion bajo queda para Markdown/código | Persisten rótulos como `L_eq,T`, `L_peak`, `S_pp` y variantes planas en varias slides | inconsistente | Corregir de forma localizada con subíndices reales o ecuación editable; no cambiar símbolos. |
| Separador decimal | Coma decimal en material docente en español | Varias tarjetas usan coma, pero algunos gráficos muestran `1.000`, `0.25`, `60.6` o notación `e` | inconsistente | Aplicar un formateador común con coma decimal en los scripts de gráficos; conservar el punto solo en código. |
| Unidades | SI y referencias logarítmicas explícitas | Usa Pa, Pa²/Hz, Hz, s y dB con contexto | aceptable | `Pa²/Hz` se registra como forma legible equivalente a `Pa²·Hz⁻¹`; no alternar en una misma slide. |
| Definiciones | Término, condición y límite de interpretación | Define ruido, realización, estacionariedad, PSD, NBN, SNR, fondo, exposición y control | aceptable | Las definiciones no contradicen libro ni glosario. |
| Tratamiento pedagógico de fórmulas | Intuición → formalismo → símbolos/unidades → ejemplo → límite | La secuencia se aplica a media, RMS, varianza, PSD, integración en banda y niveles | aceptable | Mantener; es coherente con U2–U5 y más guiado por el carácter integrador. |
| Tecnología de ecuaciones | Preferencia por editabilidad; umbral OMML/texto/SVG aún abierto | Las ecuaciones son editables como texto, pero no OMML | requiere decisión | Resolver transversalmente; no corregir U10 de forma aislada. |
| Estilo de gráficos | Fondo claro, ejes y unidades, gris de apoyo, teal/bordó/ocre, leyenda solo si aporta | Repite la gramática cromática y visual consolidada | aceptable | Solo requiere corregir formato numérico en figuras afectadas. |
| Estilo de diagramas | Formas simples, conectores claros, semántica estable y sin decoración gratuita | Predominan clasificaciones, procesos fuente–trayecto–receptor y decisiones de control | intencional | La mayor frecuencia responde a la integración conceptual; no convertirla en norma para otras unidades. |
| Jerarquía interna de diagramas | Título de nodo claramente separado del desarrollo | Los diagramas renderizados mantienen jerarquía, tamaño y corredores de conectores | aceptable | No se detectan colisiones mayores en v02. |
| Estilo de ejemplos | Ejemplo concreto antes de generalización; vínculo con sonido, audición o voz | Incluye clínica, tránsito, HVAC, puertas, exposición, enmascaramiento, acufenometría y cabina | aceptable | La variedad evita ejemplos intercambiables o decorativos. |
| Recapitulaciones | Más frecuentes en contenidos densos o integradores | Usa preguntas de encuentro, síntesis parciales y cierre general | intencional | La frecuencia es menor que en U5–U7 pero adecuada a la carga de U10. |
| Aplicaciones | Deben vincular física con Fonoaudiología, Audiología, voz o práctica | Integra medición, evaluación, exposición, control y límites de inferencia | intencional | La aplicación no se agrega como adorno final: organiza la unidad. |
| Preguntas y errores frecuentes | Preguntas resolubles y anticipación de errores | Trabaja “aleatorio = inmedible”, “blanco = igual por octava” y “enmascaramiento = protección” | aceptable | Coincide con los errores previstos por el mapa del curso. |
| Notas: cobertura y fuentes | Todas las slides deben tener apoyo docente y trazabilidad | 93/93 slides contienen notas y bloque `[Sources]` | aceptable | Cobertura completa y fuentes presentes. |
| Notas: naturalidad | D-076 pide omitir campos sin acción y reemplazar consignas genéricas | Se repiten 87 avisos de ausencia de multimedia y numerosas guías genéricas de exposición | inconsistente | Depurar en una edición de notas: conservar transición, ejemplo, pregunta, demostración y límite específicos. |
| Pies | Logo, carrera y número con ubicación estable | Mantiene el furniture del template en todo el deck | aceptable | Consistente con las unidades finales. |
| Créditos y captions | Crédito legible; códigos internos solo en notas/manifiesto | No muestra identificadores internos y usa captions funcionales | aceptable | Cumple D-056 y D-066. |
| Numeración | Numeración automática preferida; U9 admite objeto local cuando el campo dinámico no renderiza tras importación | Usa objeto local consistente en las 93 slides | aceptable | Mantener por compatibilidad mientras no se resuelva el flujo dinámico; verificar al reordenar. |
| Layouts | Variedad controlada dentro de los layouts reales del template | Usa 23 de 27 layouts | aceptable | Buena variedad sin romper la identidad. |
| Paleta | Bordó, carbón, gris, teal y ocre con roles estables | Coincide con la paleta consolidada en U8–U9 | aceptable | No requiere homogeneización. |
| Color de títulos | La guía escrita indica carbón; varios decks finales consolidan bordó | U10 usa mayoritariamente bordó | requiere decisión | Decisión global ya abierta; no recolorear solo U10. |
| Tipografía | Calibri Light para títulos, Calibri para texto y Cambria Math para matemática | Coincide en todo el deck | aceptable | Consistencia alta; revisar únicamente subíndices y tamaño de metadatos. |
| Tablas | La guía prefiere tablas nativas cuando corresponde | Las comparaciones se construyen como retículas de formas editables | requiere decisión | Son legibles y editables, pero debe definirse si la preferencia “tabla nativa” es obligatoria o funcional. |
| Slides de fuente bloqueada | Las limitaciones de fuente deben hacerse visibles y no inventarse | Dos slides registran explícitamente el bloqueo normativo o documental | intencional | Coherente con U8–U9 y con la jerarquía de fuentes. |
| Naturalidad visual y verbal | Diseño académico, humano y funcional; evitar tarjetas e iconos genéricos | No hay portadas grandilocuentes, iconos irrelevantes ni imágenes decorativas; las tarjetas cumplen funciones de comparación | aceptable | La única marca mecánica relevante está en las notas genéricas, no en la narrativa visible. |

## Diferencias intencionales que se preservan

- Mayor uso de flujos de clasificación y decisión que en U1–U4.
- Integración reiterada de fuente → señal → contexto → receptor → control.
- Recapitulaciones por encuentro para recuperar prerrequisitos distribuidos en cinco unidades anteriores.
- Separación entre ruta central, ampliaciones, respaldo y material con fuente bloqueada.
- Tratamiento conceptual del enmascaramiento, sin convertir la unidad en un protocolo audiológico completo.
- Ausencia de multimedia decorativa: los fenómenos se explican mejor con señales, gráficos y diagramas reproducibles.

## Problemas abiertos de U10

| ID | Diferencia | Clasificación | Acción recomendada | Estado |
|---|---|---|---|---|
| U10-C01 | Guiones bajos o subíndices planos en notación visible | inconsistente | Corregir los objetos de texto afectados con subíndices tipográficos o ecuaciones editables y volver a renderizar esas slides | Abierto |
| U10-C02 | Punto decimal y notación científica anglosajona en algunos gráficos | inconsistente | Incorporar un formateador de coma decimal en los scripts y regenerar solo las figuras afectadas | Abierto |
| U10-C03 | Notas con avisos de “no requiere multimedia” y guías de exposición repetidas | inconsistente | Depurar los campos sin acción y escribir indicaciones específicas cuando agreguen valor docente | Abierto |
| U10-D01 | Umbral entre OMML, texto matemático y SVG/PNG | requiere decisión | Resolver para todo el curso mediante prueba de editabilidad, render y mantenimiento | Abierto global |
| U10-D02 | Títulos carbón según guía escrita frente a bordó consolidado | requiere decisión | Resolver transversalmente y luego actualizar guía/template o decks | Abierto global |
| U10-D03 | Tabla nativa frente a retícula de formas editables | requiere decisión | Definir criterio funcional por accesibilidad, edición y estabilidad de render | Abierto global |

## Documentación global actualizada

- `style/glossary.md`: se añadieron “realización de un proceso aleatorio”, “ruido de fondo” y “nivel de excedencia”; se explicitó la diferencia entre fondo, enmascarador y protección.
- `style/notation_guide.md`: se documentaron `S_pp(f)`, `p_{B,\mathrm{rms}}`, `L_max,F`, `L_peak` y `L_N,T`, y el uso legible de Pa²/Hz.
- `style/decision_log.md`: se registraron D-080 a D-083 para las convenciones anteriores y para la excepción pedagógica de U10.

No se modificaron el mapa del curso, el template ni las unidades anteriores: la comparación no reveló una contradicción que justificara esos cambios.

## Cierre

La consistencia de la Unidad 10 queda **aprobada con ajustes editoriales abiertos**. No existen diferencias que exijan homogeneizar su arquitectura pedagógica. Las tres inconsistencias locales están identificadas y las decisiones globales permanecen explícitamente abiertas para evitar cambios aislados o contradictorios.
