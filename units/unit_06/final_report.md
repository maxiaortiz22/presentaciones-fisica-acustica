# Unidad 6 — Informe final

**Fecha de cierre:** 2026-08-10  
**Presentación final:** `output/unidad_06_mecanismo_periferico_final.pptx`  
**PDF de revisión:** `output/unidad_06_mecanismo_periferico_final_review.pdf`  
**Render:** `output/render_final/`  
**Dictamen:** unidad terminada; no quedan problemas críticos ni mayores.

## Identificación del artefacto

- 117 slides en formato 16:9.
- 2 masters y 27 layouts preservados de la plantilla del curso.
- PPTX de 745.584 bytes; SHA-256 `8F300D7B0B1C47168C6C52AB6EC0195D05E6B416E3C3E5157E68B8D5CCB739BE`.
- PDF de 117 páginas; SHA-256 `9D3D831F2356B40FA44B0AC43EE6A8A22857EF1EC7ADC6549CB9A5657A26164A`.
- 117 PNG de revisión a 1600 × 900 y mosaico general `output/contact_sheet_final.png`.

## Definición de terminado

| Entregable o control | Estado | Evidencia |
|---|---|---|
| `brief.md` | completo | Objetivos, alcance, decisiones y estado final. |
| `storyboard.md` | completo | 117 filas sincronizadas; bloques, ruta y fuentes. |
| `slide_text.md` | completo | 117 slides con texto visible, visual, layout, fuente y alt text. |
| `speaker_notes.md` | completo | 117 notas con tiempos, desarrollo, pregunta/transición, fuentes y alt text. |
| `asset_manifest.csv` | completo | 78 IDs únicos; 59 recursos propios aprobados y localizados. |
| scripts | completos | Generación, build, alt text, numeración, exportación y validación reproducibles. |
| gráficos propios | completos | 6 familias reproducibles; SVG/PNG y scripts conservados. |
| diagramas propios | completos | 53 familias aprobadas con fuentes editables y validación; composiciones nativas adicionales en el deck. |
| PowerPoint | completo | Archivo final nuevo; v01 y v02 preservados. |
| PDF de revisión | completo | 117 páginas. |
| render | completo | 117/117 slides y contact sheet. |
| `review.md` | aprobado | Sin problemas critical ni major. |
| revisión independiente | cerrada | Los diez hallazgos major fueron resueltos o aceptados con justificación. |
| revisión de consistencia | aprobada | `consistency_report.md` actualizado; sin decisiones bloqueantes. |

## Estructura y duración

- Ruta central: 82 slides, 425 minutos estimados (7 h 05 min).
- Complementarias: 23 slides, 111 minutos estimados.
- Respaldo: 12 slides, 72 minutos estimados.
- Banco completo: 608 minutos estimados (10 h 08 min); no se recomienda proyectarlo linealmente.

Distribución sugerida de la ruta central:

| Encuentro | Rango del banco | Tiempo central estimado |
|---|---|---:|
| 1 | U06-001–039 | 161 min |
| 2 | U06-040–071 | 117 min |
| 3 | U06-072–093 | 89 min |
| 4 | U06-094–117 | 58 min |

## Bloques y temas cubiertos

| Bloque | Tema | Slides |
|---|---|---:|
| B00 | Apertura, prerrequisitos, objetivos y mapa de la unidad | 7 |
| B01 | Oído externo y conducto auditivo externo | 10 |
| B02 | Tímpano, presión, fuerza y movimiento | 10 |
| B03 | Oído medio, transformación mecánica y reflejo acústico | 12 |
| B04 | Conducción ósea y sus mecanismos | 9 |
| B05 | Arquitectura coclear: ventanas, rampas, fluidos, membranas y túnel de Corti | 12 |
| B06 | Onda viajera, lugar característico, frecuencia, nivel y mecánica activa | 11 |
| B07 | Órgano de Corti, micromecánica, CCI, CCE y OEA | 10 |
| B08 | Transducción mecanoeléctrica, gradiente, potencial receptor y sinapsis | 12 |
| B09 | Codificación periférica, sincronización, población neural, pruebas y límites inferenciales | 12 |
| B10 | Respaldo: terminología, símbolos, ejercicios resueltos y auditoría anatómica | 12 |

La cobertura del programa es completa y mantiene correspondencia con el capítulo 6 del libro. Las ampliaciones didácticas se distinguen de la fuente principal y no contradicen su alcance.

## Recursos visuales y multimedia

- 6 gráficos propios únicos y reproducibles; 9 apariciones raster/SVG contabilizadas como imágenes en el PPTX.
- 53 diagramas propios aprobados, con `diagram_source.json`, PPTX editable, SVG/PNG y validación en sus carpetas.
- 64 usos reales de assets aprobados del manifiesto y 17 composiciones nativas finales; no se atribuyen assets reemplazados en las notas.
- Diagramas nativos finales adicionales para CAE ideal/real, palanca, vistas cocleares, micromecánica, dominios eléctricos, montaje de medición y G3.
- 5 recursos de video/GIF permanecen como candidatos opcionales; no hay multimedia incrustada.
- Cada candidato multimedia tiene una alternativa estática autosuficiente, por lo que no constituye un bloqueo.
- 23 slides complementarias y 12 de respaldo permiten ampliar, practicar o consultar sin sobrecargar la ruta central.

## Fuentes principales

1. Programa oficial 2025, Unidad 6.
2. Libro del curso en LaTeX: `context/libro_latex/chapters/06-percepcion-auditiva.tex`.
3. Libro del curso en PDF, capítulo 6, pp. 151–175.
4. Mapas y guías del repositorio: curso, dependencias, glosario, notación, estilo, layouts y decisiones.
5. Referencias técnicas ya registradas en el capítulo y en las notas, entre ellas `fettiplace2017`, `capraraPeng2022`, `ugarteburu2022`, `stenfeltGoode2005`, `Stenfelt2011` y `schilder2015`.

Todas las fuentes efectivamente usadas están registradas. Los assets incorporados son producciones propias aprobadas; los candidatos externos no incorporados permanecen documentados en `asset_manifest.csv`. Seis propuestas sin selección de fuente conservan URL vacía y no forman parte del deck final.

## Decisiones pedagógicas

- La unidad se limita al mecanismo periférico y prepara, sin reemplazar, psicoacústica (U7) y clínica (U8).
- La intuición precede al formalismo: presión → fuerza → movimiento → transferencia → respuesta coclear → señal celular → actividad aferente.
- Las fórmulas se acompañan con significado físico, símbolos, unidades y límites; G3 usa datos didácticos explícitos.
- La anatomía se construye acumulativamente mediante vistas longitudinales y transversales antes de la micromecánica.
- CCI y CCE comparten transducción inicial, pero se separan en aferencia principal y realimentación mecánica.
- Las recapitulaciones son más frecuentes que en unidades livianas por la densidad de U6.
- Las pruebas auditivas se presentan como ventanas sobre una cadena, no como diagnósticos aislados.
- Se preservan diferencias pedagógicas justificadas respecto de unidades anteriores; no se homogeneizó la profundidad.

## Producción y editabilidad

- Textos, cajas, ecuaciones centrales, flechas y diagramas finales permanecen editables en PowerPoint.
- Los gráficos insertados como SVG/imagen no son gráficos nativos de PowerPoint, pero sus scripts y archivos fuente reproducibles están conservados.
- 117 campos dinámicos de numeración fueron insertados; la auditoría OOXML identifica el campo en todas las slides.
- 64 objetos visuales tienen alt text y las 117 notas incluyen una descripción alternativa.
- 117/117 notas contienen fuentes.
- 0 placeholders locales, 0 objetos fuera del lienzo y 0 relaciones externas.
- Las fuentes de contenido son Calibri, Calibri Light y Cambria Math; los nombres adicionales del paquete corresponden a fallbacks del tema/master.

## Verificaciones realizadas

- Revisión visual del mosaico completo de 117 slides.
- Revisión a tamaño completo de las slides de mayor riesgo pedagógico y geométrico.
- Regeneración y preflight de los diagramas afectados hasta 0 critical/major.
- Render final mediante PowerPoint, no solo inspección de texto o XML.
- `u06_validate_pptx.py`: `pass`.
- `slides_test.py`: aprobado, sin overflow.
- PDF: 117/117 páginas.
- Búsqueda de estados históricos y sincronización de `source_map.md`.

## Limitaciones conocidas

- La ruta central sigue siendo extensa; requiere cuatro encuentros o una selección docente explícita.
- No hay audio, video o GIF incrustado. Es una decisión de cierre: la versión estática es completa y robusta en aula.
- No hay hipervínculos externos en el PPTX; las fuentes están en notas y manifiesto. Puede añadirse navegación solo si el docente la considera útil.
- Algunos valores del ejercicio G3 son didácticos y no deben interpretarse como parámetros universales de un oído real.
- Las imágenes externas descargadas o preseleccionadas que no se usan permanecen organizadas en el manifiesto, no en la salida final.

## Recomendaciones para dictar la clase

1. Usar los cuatro encuentros señalizados y no proyectar el banco completo de manera lineal.
2. Comenzar cada encuentro con la pregunta guía del bloque y cerrar con la recapitulación correspondiente.
3. Dibujar o señalar físicamente las transformaciones de dominio: presión, fuerza, movimiento, potencial y actividad neural.
4. En anatomía coclear, recorrer primero la vista longitudinal y luego el corte; evitar presentar todos los rótulos simultáneamente.
5. En CCI/CCE, pedir que el grupo justifique cada consecuencia por la rama causal antes de mostrar la síntesis.
6. En gráficos de frecuencia/nivel, solicitar una lectura verbal de ejes y variables antes de interpretar percepción.
7. Usar complementarias y respaldo a demanda según diagnóstico del grupo, tiempo y preguntas clínicas.
8. Cerrar remarcando el límite: la periferia condiciona la percepción, pero no la agota.
