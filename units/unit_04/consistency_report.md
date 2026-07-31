# Informe de consistencia — Unidad 4

**Unidad:** Generalidades sobre el sonido, sus propiedades y magnitudes  
**Deck revisado:** `output/unidad_04_sonido_magnitudes_v02.pptx`  
**Render revisado:** `output/render_v02/slide-1.png` a `slide-125.png`  
**Fecha:** 2026-07-31  
**Estado:** revisión transversal completa; el deck no fue modificado en esta tarea.

## Alcance y criterio

La revisión compara la Unidad 4 con:

- `AGENTS.md`;
- `style/presentation_style_guide.md`;
- `style/slide_master_spec.md`;
- `style/layout_catalog.md` y `style/component_catalog.md`;
- `style/glossary.md`, `style/notation_guide.md` y `style/decision_log.md`;
- `style/template_review.md` y `output/fisica_acustica_template_v01.pptx`;
- `course_map.md`, `course_dependency_map.md` y `course_consistency_report.md`;
- las versiones finales de las Unidades 1, 2 y 3, sus renders e informes de revisión y consistencia;
- `storyboard.md`, `slide_text.md`, `speaker_notes.md`, `review.md`, el PowerPoint v02 y las 125 imágenes renderizadas de la Unidad 4.

No se tomó el template como única referencia: las decisiones que ya demostraron funcionar en las tres unidades anteriores tienen más peso que una demo aislada. Tampoco se consideró inconsistente una diferencia solo porque la Unidad 4 sea más extensa o formal; se evaluó si la diferencia tiene una razón pedagógica explícita y si conserva la legibilidad y las convenciones del curso.

Las categorías usadas son:

- **intencional:** diferencia justificada por el contenido o la progresión pedagógica;
- **aceptable:** variante que no rompe comprensión, identidad ni continuidad;
- **inconsistente:** contradice una convención ya adoptada o una práctica consolidada sin beneficio pedagógico;
- **requiere decisión:** la evidencia no permite fijar una única solución local sin afectar unidades futuras.

## Síntesis ejecutiva

La Unidad 4 pertenece visual y técnicamente al mismo curso. Conserva 16:9, dos masters, 27 layouts disponibles, paleta, tipografías, regla superior segmentada, pies, numeración, bloques de notas y texto alternativo. La variedad de layouts es incluso mayor que en las unidades anteriores: usa 26 de los 27 layouts del template.

La mayor profundidad, los once separadores y las siete recapitulaciones son diferencias **intencionales**: U4 es el punto de formalización de las magnitudes acústicas y `AGENTS.md` exige bloques más cortos para las Unidades 4–7. No corresponde reducirla para que tenga el mismo número de slides que U1–U3.

Las inconsistencias principales no están en la identidad general, sino en cuatro focos:

1. alternancia visible entre `Q` y `Q_dir`, pese a la colisión ya resuelta con `Q_calor`;
2. captions de producción repetidos y badges de fallback visibles, contrarios a D-056 y al lenguaje académico del resto del curso;
3. reutilización de figuras amplias en slides consecutivas, que debilita la función específica de cada layout y la variedad real;
4. algunas ecuaciones, ejemplos y recapitulaciones que no cumplen el contrato pedagógico ya consolidado en U1–U3.

Quedan decisiones transversales sobre `R_I/R_E`, el umbral OMML–SVG y la duración real de la ruta central. Ninguna exige homogeneizar por homogeneizar.

## Evidencia estructural

| Artefacto | Slides | Masters | Layouts | Notas | Notas con `[Sources]` | Imágenes con alt/title | Enlaces externos | Tamaño |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Template v01 | 27 | 2 | 27 | 27 | 2 | 2/2 | 0 | 0,57 MB |
| Unidad 1 final | 94 | 2 | 27 | 94 | 94 | 16/16 | 2 | 0,89 MB |
| Unidad 2 final | 110 | 2 | 27 | 110 | 110 | 78/78 | 2 | 1,70 MB |
| Unidad 3 final | 96 | 2 | 27 | 96 | 96 | 80/80 | 0 | 10,11 MB |
| Unidad 4 v02 | 125 | 2 | 27 | 125 | 125 | 99/99 | 3 | 2,62 MB |

La auditoría estructural confirma continuidad de master, layouts, notas, fuentes y accesibilidad. El peso del archivo de U4 es razonable y no muestra el crecimiento observado en U3.

### Uso comparado de layouts

| Unidad | Layouts usados | Ecuación | Separador | Recapitulación | Ejemplo resuelto | Gráfico | Apéndice/respaldo |
|---|---:|---:|---:|---:|---:|---:|---:|
| U1 | 25/27 | 7 | 8 | 3 | 6 | 6 | 9 |
| U2 | 25/27 | 16 | 9 | 7 | 6 | 4 | 16 |
| U3 | 21/27 | 8 | 7 | 7 | 3 | 7 | 12 |
| U4 | 26/27 | 20 | 11 | 7 | 6 | 7 | 15 |

La concentración en ecuaciones no es, por sí sola, una anomalía: 20 de 125 slides representa una proporción cercana a la de U2. El problema aparece cuando una slide rotulada como ecuación reutiliza una figura que contiene varias relaciones y conceptos a la vez.

## Matriz de diferencias

### Terminología, símbolos, unidades y definiciones

| ID | Aspecto | Diferencia observada | Clasificación | Criterio y acción |
|---|---|---|---|---|
| U04-CG-001 | Terminología general | “presión acústica”, “presión sonora”, RMS, intensidad, potencia, campo, directividad y dB se usan con el sentido del glosario. | **aceptable** | “Presión sonora” se reserva principalmente para el nivel `L_p`; no se trata como sinónimo perceptual. |
| U04-CG-002 | Rapidez/velocidad | U4 alterna “rapidez de propagación” con el uso acústico convencional “velocidad de propagación”. | **intencional** | Cumple D-054: `c` se presenta como escalar y se diferencia de `u`. No homogeneizar toda aparición si no hay ambigüedad. |
| U04-CG-003 | Señal | El glosario situaba la primera introducción de “señal” en U5, pero U4 la usa de forma central para descriptores temporales y RMS. | **inconsistente** | Se corrigió el glosario: primera introducción en U4; análisis temporal/frecuencial formal en U5. |
| U04-CG-004 | Señal compleja | U04-057 usa “señal compleja” antes de Fourier. | **aceptable** | Es necesaria para contrastar forma de onda y RMS. Se añadió al glosario la advertencia de no confundir “compleja” con representación mediante números complejos. |
| U04-CG-005 | Sonómetro | U04-104 anticipa el instrumento antes de la unidad de análisis/medición. | **intencional** | La slide explicita qué informa y qué no informa, sin desarrollar aún ponderaciones. Se actualizó el glosario: introducción conceptual en U4 y formalización en U5/U10. |
| U04-CG-006 | `p`, `u`, `c` | U4 abandona correctamente la perturbación genérica `ξ` de U3 y usa magnitudes físicas específicas. | **aceptable** | Cumple D-055 y mejora el puente U3→U4. |
| U04-CG-007 | Potencia acústica | El deck usa `W_ac`, mientras la guía aún mantenía abierta la alternativa `P_ac`. | **aceptable** | U4 es consistente internamente y con el libro. Se adoptó `W_ac` como convención transversal en D-057 y se actualizó el glosario y la guía. |
| U04-CG-008 | `K_s`, `i(t)`, `Z_0` | U4 formaliza símbolos que no estaban documentados con suficiente precisión en la guía global. | **inconsistente** | Era una omisión de la documentación global, no un error local del deck. Se añadieron las distinciones `K_s/k_s`, `i(t)/I` y `Z_0/Z` mediante D-058. |
| U04-CG-009 | Directividad | Storyboard, título de U04-101, texto alternativo y notas usan a veces `Q`, aunque la fórmula visible usa `Q_dir`. | **inconsistente** | Sustituir el símbolo desnudo por `Q_dir` en título, lectura central, alt text y notas; escribir `DI=10 log₁₀(Q_dir)`. El nombre verbal puede ser “factor de directividad”. |
| U04-CG-010 | Mapa del curso | La fila de U4 en `course_map.md` conserva `W` y `Q` sin calificadores. | **requiere decisión** | El mapa debería alinearse con `W_ac` y `Q_dir`, pero debe actualizarse mediante `course-architecture`, no desde esta revisión local. |
| U04-CG-011 | Reflexión | U4 usa `R_p` para amplitud de presión y `R_I` para la razón de intensidades; la guía global usaba solamente `R_E`. | **aceptable** | D-059 fija `R_p` y `R_I` para U4 y reserva `R_E` para una fracción energética genérica definida. Se evita `R` desnudo. |
| U04-CG-012 | Coherencia | La definición central exige frecuencia común y diferencia de fase estable; U04-115 reconoce correlación parcial. | **aceptable** | No se reduce coherencia a “estar en fase”. La formulación binaria central es didáctica y la limitación aparece en respaldo. |
| U04-CG-013 | Unidades y referencias | Pa, m·s⁻¹, W·m⁻², W, J, Pa·s·m⁻¹, 20 µPa, 1 µPa y 10⁻¹² se mantienen coherentes. | **aceptable** | Los valores y dimensiones coinciden con libro, glosario y guía. Mantener productos con punto centrado en texto visible. |
| U04-CG-014 | Niveles | `L_p`, `L_I`, `L_W`, referencias y factores 20/10 se distinguen correctamente. | **aceptable** | La separación entre magnitud lineal y nivel logarítmico es más explícita que en unidades anteriores y debe conservarse. |

### Profundidad, fórmulas, ejemplos, recapitulaciones, aplicaciones y notas

| ID | Aspecto | Diferencia observada | Clasificación | Criterio y acción |
|---|---|---|---|---|
| U04-CG-015 | Profundidad | U4 tiene 125 slides y 91 marcadas como centrales, frente a 69–72 centrales en U1–U3. | **intencional** | La mayor profundidad responde al alcance de U4 y a la exigencia de bloques más cortos. La ruta central de 347 min quedó distribuida en cuatro encuentros de 98, 84, 76 y 89 min; 18 slides son complementarias y 16 de respaldo. |
| U04-CG-016 | Segmentación | Once separadores y siete recapitulaciones superan o igualan las unidades anteriores. | **intencional** | Responde al requisito específico de bloques cortos para U4–U7. Conservar. |
| U04-CG-017 | Fórmulas | Veinte layouts de ecuación, más que en U1 y U3. | **intencional** | U4 formaliza magnitudes, referencias y relaciones. La frecuencia de ecuaciones está justificada; la calidad de tratamiento debe revisarse caso por caso. |
| U04-CG-018 | Contrato de ecuación | Varias slides de ecuación reutilizan una figura amplia con más de una relación, condiciones y contenido futuro. | **inconsistente** | El layout del curso pide una ecuación principal, símbolos, unidades, significado y condiciones. Dividir o recortar el visual cuando compita con esa lectura. |
| U04-CG-019 | Tecnología matemática | Conviven texto editable, ecuaciones renderizadas en SVG y fórmulas que no son OMML. | **requiere decisión** | Es el mismo pendiente detectado en U2/U3. Definir un umbral por complejidad y frecuencia de edición; no convertir todo a OMML si reduce legibilidad o mantenimiento. |
| U04-CG-020 | Ejemplos resueltos | La mayoría conserva la secuencia datos→relación→cálculo→resultado→interpretación, como U1/U2. | **aceptable** | U04-039, 056, 063, 074 y 097 son referencias válidas de estilo. |
| U04-CG-021 | Casos incompletos | U04-079 no explicita suficientemente el cálculo; U04-105/U04-124 carecen de datos plenamente operativos; U04-120 no funciona como solución del caso anunciado. | **inconsistente** | Completar datos, pasos y criterio de cierre o reclasificar las slides como preguntas de discusión. |
| U04-CG-022 | Recapitulaciones | La frecuencia es adecuada, pero varias recaps funcionan como mapas ya completos y no siempre incluyen recuperación activa visible. | **inconsistente** | Mantener las siete recaps, pero asegurar el contrato “tres ideas + una pregunta/decisión” usado en el catálogo y en U2/U3. |
| U04-CG-023 | Aplicaciones | Hay cinco layouts clínicos/aplicados y ejemplos sobre voz, micrófonos, campo y medición. | **aceptable** | La cantidad y pertinencia son coherentes con el curso. No agregar iconografía clínica decorativa. |
| U04-CG-024 | Directividad aplicada | U04-102 pide comparar dos patrones, pero el PPTX no muestra patrones polares interpretables; `review.md` lo da por resuelto. | **inconsistente** | Incorporar un patrón polar mínimo o reformular como advertencia puramente conceptual sin pedir una lectura ausente; actualizar luego el estado del review previo. |
| U04-CG-025 | Notas: cobertura | Las 125 slides tienen notas y bloque `[Sources]`. | **aceptable** | Es una mejora productiva sostenida respecto del mínimo del template. |
| U04-CG-026 | Notas: naturalidad | 101 de 125 notas reutilizan alguna de tres preguntas genéricas y varias explicaciones repiten una plantilla verbal. | **inconsistente** | Sustituir por preguntas ligadas al fenómeno, la magnitud o el error concreto. Mantener la estructura de notas, no la redacción repetida. |

### Gráficos, diagramas, pies, créditos, numeración y sistema visual

| ID | Aspecto | Diferencia observada | Clasificación | Criterio y acción |
|---|---|---|---|---|
| U04-CG-027 | Identidad visual | Formato 16:9, franja superior segmentada, fondos, márgenes y jerarquía coinciden con el template y U1–U3. | **aceptable** | No cambiar el estilo global durante una corrección local. |
| U04-CG-028 | Paleta | Borgoña, azul verdoso, ocre, gris y fondos claros conservan los roles del sistema. | **aceptable** | El uso del color no introduce una semántica incompatible. |
| U04-CG-029 | Tipografía | Calibri Light, Calibri y Cambria Math son las familias visibles principales; Arial aparece solo como referencia de tema/fallback del paquete. | **aceptable** | No hay evidencia renderizada de una cuarta familia visible que rompa identidad. |
| U04-CG-030 | Layouts | U4 usa 26/27 layouts, más variedad nominal que U1–U3. | **aceptable** | La unidad explota el sistema sin crear variantes manuales incompatibles. |
| U04-CG-031 | Variedad real | La misma figura o familia SVG se reutiliza en slides consecutivas —especialmente 72–79 y 92–97— y hace que funciones distintas se perciban como clones. | **inconsistente** | Ajustar encuadre, destacar el elemento pertinente o dividir recursos; no hace falta cambiar de layout si cambia la evidencia visual. |
| U04-CG-032 | Gráficos | Ejes, unidades, coma decimal, grilla liviana y colores se alinean con U2/U3. | **aceptable** | Conservar el estilo cuantitativo y la declaración de hipótesis. |
| U04-CG-033 | Explicación de gráficos | En U04-077–079 el mismo recurso no guía con claridad de la comparación al cálculo, y algunos captions sustituyen la explicación. | **inconsistente** | Añadir una lectura visual específica por slide: qué cambia, qué se mantiene y qué resultado se obtiene. |
| U04-CG-034 | Diagramas | Los SVG embebidos son nítidos y sus fuentes son reproducibles, pero no son editables como formas nativas dentro del PPTX. | **requiere decisión** | Resolver por familia: formas nativas para cajas/conectores que cambian; SVG para gráficos o esquemas matemáticos estables. No rasterizar por uniformidad. |
| U04-CG-035 | Glifos matemáticos | En el render aparecen signos deformados o poco legibles en U04-085, U04-092 y U04-108 (`∝`, subíndices o `u≠c`). | **inconsistente** | Corregir la fuente o reemplazar el fragmento por una ecuación editable/render estable y volver a revisar a tamaño de clase. |
| U04-CG-036 | Captions | La advertencia genérica sobre escala aparece 81 veces y la frase de “figura cuantitativa reproducible” aparece 11 veces. | **inconsistente** | Contradice D-056 y diferencia a U4 de U1/U2. Conservar solo captions que expliquen qué mirar; llevar autoría, validación y escala a notas/manifiesto cuando no sean parte del argumento. |
| U04-CG-037 | Etiquetas de producción | `ALTERNATIVA ESTÁTICA · MEDIA NO INCRUSTADA` queda visible en U04-013, 072–076, 079, 095 y 097. | **inconsistente** | Es lenguaje de producción, no académico. Retirar del área visible; registrar la ausencia de media en notas y manifiesto. |
| U04-CG-038 | Pies y numeración | Pie institucional, unidad y números se mantienen; U4 numera desde la portada como U2/U3. | **aceptable** | La portada sin número visible de U1 es una variante histórica aceptable; no obliga a quitar numeración en U4. |
| U04-CG-039 | Créditos | Los recursos externos tienen créditos y enlaces; las imágenes cuentan con texto alternativo/title. | **aceptable** | Mantener el crédito próximo al recurso cuando la licencia o atribución lo requiera y el detalle completo en notas/manifiesto. |
| U04-CG-040 | Peso del archivo | 2,62 MB para 125 slides, por debajo de U3 y sin pérdida visual evidente. | **aceptable** | No comprimir más por uniformidad; priorizar nitidez y editabilidad. |

## Diferencias que no deben homogeneizarse

1. **Mayor cantidad de slides.** La Unidad 4 cubre más magnitudes, modelos y conexiones; el problema es la ruta temporal, no el número bruto.
2. **Más separadores y recapitulaciones.** Es una respuesta pedagógica explícita para U4–U7.
3. **Mayor proporción de ecuaciones.** Es el punto del curso donde se formalizan presión, velocidad de partícula, intensidad, potencia, energía y niveles.
4. **Uso temprano de sonómetro y aplicaciones de micrófono.** Funciona como anticipación clínica/instrumental si se declara el límite y no se desarrollan normas antes de U5/U10.
5. **Uso de SVG para figuras cuantitativas estables.** No debe reemplazarse por formas nativas solo para igualar U1; la decisión depende de la familia y de la necesidad real de edición.
6. **Tratamiento operativo de impedancia.** El glosario conserva la definición general compleja, pero U4 puede enseñar primero la relación física y reservar el formalismo complejo para respaldo.

## Prioridades de corrección local

### Imprescindibles para consistencia

1. Unificar `Q_dir` en U04-101 y en storyboard, notas y texto alternativo relacionados.
2. Retirar los nueve badges de producción visibles.
3. Sustituir los captions repetidos por pies funcionales conforme a D-056.
4. Corregir los glifos matemáticos defectuosos de U04-085, 092 y 108.

### Recomendadas

1. Diferenciar visualmente las secuencias 72–79 y 92–97 para que cada slide tenga evidencia propia.
2. Revisar las slides de ecuación que muestran varias relaciones sin una jerarquía principal.
3. Completar o reclasificar U04-079, 105, 120 y 124.
4. Convertir parte de las preguntas genéricas de notas en comprobaciones específicas.
5. Añadir recuperación activa visible a las recaps que hoy son mapas resueltos.

## Decisiones abiertas

| Decisión | Alcance | Recomendación provisional |
|---|---|---|
| Duración de la ruta central | U4 y planificación del curso | **Resuelta en U4:** cuatro encuentros explícitos; no se elimina profundidad. |
| OMML/texto/SVG | U2–U5 y template | Usar OMML o texto editable para ecuaciones centrales simples; SVG para composiciones complejas estables con fuente reproducible. |
| Formas nativas frente a SVG | Familias de diagramas | Nativo para cajas/conectores modificables; SVG para gráficos y esquemas matemáticos estables. |
| `W`/`Q` en `course_map.md` | Mapa global | Actualizar a `W_ac` y `Q_dir` mediante `course-architecture`. |

## Documentación global actualizada

- `style/glossary.md`: se documentaron `K_s`, `i(t)`, la introducción de “señal” y “señal compleja/compuesta” en U4, la anticipación del sonómetro y la adopción de `W_ac`.
- `style/notation_guide.md`: se fijaron `W_ac`, `K_s`, `i(t)`, `I` y `Z_0`, y se eliminó el pendiente ya resuelto `P_ac/W_ac`.
- `style/decision_log.md`: se registraron D-057 y D-058; D-042 quedó validada con U1–U4, D-056 ahora registra las retrocorrecciones pendientes de U3/U4 y se reemplazó el pendiente obsoleto de escalabilidad por el pendiente real OMML/texto/SVG.

No se modificaron `course_map.md`, el storyboard ni el deck porque las decisiones que los afectan requieren otra skill o una tarea explícita de corrección.

## Verificación final

- Se inspeccionó el PowerPoint real y no solamente su XML.
- Se revisaron las 125 slides renderizadas y las hojas de contacto del template y U1–U4.
- Se auditó la estructura interna de los cinco PPTX comparados: masters, layouts, notas, fuentes, imágenes, alt text, enlaces y peso.
- Se contrastaron texto visible, notas, storyboard, informes previos y documentación global.
- La clasificación preserva las diferencias con justificación pedagógica y separa los problemas locales de las decisiones transversales.

## Actualización de cierre final

La versión final resolvió las inconsistencias locales que impedían el cierre:

- `Q_dir` quedó unificado en títulos, fórmulas, texto alternativo, storyboard y notas;
- D-059 resolvió la distinción `R_p`/`R_I` y reservó `R_E` para una fracción energética genérica definida;
- la ruta central se documentó como cuatro encuentros y dejó de presentarse como tres;
- las secuencias con visuales repetidos o revelado prematuro se sustituyeron selectivamente por contenido editable específico;
- U04-073, 078, 079, 102, 105, 120 y 124 cumplen ahora su función declarada;
- se corrigieron los glifos de U04-085, 092 y 108;
- se eliminaron captions genéricos, backticks y nueve badges de producción;
- el paquete final conserva 2 masters, 27 layouts, 125 notas, 75 descripciones accesibles, 3 enlaces y numeración 1–125.

Quedan como diferencias **aceptables** y documentadas: SVG embebidos con fuentes editables externas, ausencia de multimedia todavía no aprobada y uso de una tabla angular didáctica en lugar de un patrón polar comercial. La actualización de `W`/`Q` en `course_map.md` sigue reservada a `course-architecture` y no afecta la consistencia visible de la Unidad 4.
