# Unidad 10 — Revisión integral y corrección v02

Fecha: 2026-08-12  
Deck revisado: `output/unidad_10_ruidos_v01.pptx`  
Deck corregido: `output/unidad_10_ruidos_v02.pptx`  
Alcance: 93 diapositivas, 93 renders, notas, masters, layouts, recursos y fuentes.

## Dictamen

- **Críticos abiertos:** 0.
- **Mayores abiertos:** 0.
- Se corrigieron 10 grupos de problemas mayores y se ejecutaron nuevas construcciones y renders hasta cerrar la inspección.
- La cobertura obligatoria del programa está completa y la secuencia corresponde al capítulo 10 del libro.
- Quedan 2 problemas menores y 2 sugerencias abiertos; ninguno compromete exactitud, legibilidad del contenido principal ni uso en clase.

## Método y evidencia

Se compararon el programa oficial, el capítulo 10 en LaTeX y las páginas correspondientes del PDF del libro. Se inspeccionó el PowerPoint como paquete y mediante `artifact-tool`, y se revisaron visualmente los 93 renders de v01 y v02 en hojas de contacto ampliadas. Las slides densas o corregidas se examinaron además a tamaño completo.

La segunda pasada incluyó `slides_test.py`, validación OOXML, validación contextual de diagramas, PDF de 93 páginas y revisión final específica de las slides 42, 49, 68, 74, 78, 82, 85, 87, 89, 90 y 93.

## Cobertura y correspondencia

| Requisito del programa | Evidencia en el deck | Resultado |
|---|---|---|
| Concepto, tipos y clasificación de ruido | U10-006–U10-019 y U10-037–U10-044 | cubierto |
| Diferencia entre sonido y ruido | U10-006–U10-010, con función, contexto, receptor y tarea | cubierto |
| Ruido aleatorio | U10-011–U10-25: realización, estacionariedad, media, RMS, varianza y distribución | cubierto |
| Ruido blanco y rosa | U10-026–U10-036; PSD, integración por banda y octavas | cubierto |
| Ruido vocal o con espectro de habla | U10-037–U10-038 y U10-044 | cubierto |
| Ruido de banda estrecha (NBN) | U10-039–U10-044; límites, centro, ancho y pendientes | cubierto |
| Enmascaramiento | U10-052–U10-064; señal, ruido, SNR, oído y respuesta | cubierto |

Las ampliaciones sobre descriptores temporales, exposición, control y aplicaciones fonoaudiológicas siguen el libro y están separadas de los bloques centrales. No se incorporaron límites normativos, fórmulas para intervalos desiguales ni protocolos clínicos sin fuente verificada.

## Revisión por dimensión

### Contenido

- Terminología coherente: realización/proceso, estacionario/constante, fondo/enmascarante, pico/máximo/Impulse y exposición/resultado funcional.
- Fórmulas revisadas: media, RMS, varianza, potencia en banda a partir de PSD, SNR, nivel equivalente, identidad RMS–varianza–media e integral de PSD rosa por octava.
- Unidades verificadas: Pa, mPa, Pa², Pa²/Hz, Hz, dB SPL, dB(A), porcentajes e intervalo T.
- Los ejemplos numéricos de U10-030, U10-050 y U10-089 coinciden con los datos y resultados del libro; se conservan sus límites de interpretación.

### Pedagogía

- La secuencia avanza de función y contexto a tiempo, estadística, frecuencia, nivel, enmascaramiento, control e integración.
- Los prerrequisitos se recuperan en U10-004 y los encuentros se separan con preguntas guía y recapitulaciones.
- Hay ejemplos concretos, aplicaciones a audiología y ambiente clínico, preguntas de comprobación y ejercicios con solución.
- Se redujo la carga cognitiva de U10-074, U10-082 y U10-089; el procedimiento extendido de los ejercicios queda en notas.

### Diseño

- Jerarquía, contraste, márgenes y alineación son consistentes con el sistema visual del curso.
- Las tablas de U10-042, U10-068, U10-085 y U10-090 se reconstruyeron con tipografía de aula.
- No hay clipping, desbordes, imágenes deformadas ni slides aplanadas.
- Existe variedad suficiente entre portadas de bloque, preguntas, diagramas, gráficos, tablas, ecuaciones y actividades.

### Diagramas y esquemas

- Se eliminó el descarte silencioso de terceras líneas en el generador; ahora todo texto debe redistribuirse o fallar el preflight.
- Se revisaron 57 instancias en contexto final: 0 flechas sobre texto, 0 etiquetas montadas sobre conectores, 0 cajas desbordadas y 0 fuentes principales por debajo de 22 pt.
- Las ecuaciones centrales conservan 28 pt o más.
- En U10-078 se sustituyó el diagrama completo reducido por un gráfico ampliado y tres cajas nativas editables; también se corrigió el eje compartido del gráfico.

### Producción

- 16:9, 2 masters, 27 layouts, 93 notas y numeración completa.
- Texto, formas, conectores, tablas y ecuaciones diagramáticas editables; gráficos en SVG con scripts y datos reproducibles.
- Todas las imágenes insertadas tienen texto alternativo; no hay imágenes de slide completa.
- No hay hipervínculos externos, audio ni video embebidos; por lo tanto, no hay enlaces o medios rotos.
- El archivo pesa 1.439.017 bytes y usa fuentes de sistema; no requiere fuentes incrustadas.

### Naturalidad

- No se encontraron frases promocionales, grandilocuentes o típicas de IA, portadas exageradas, iconos irrelevantes ni fotografías decorativas.
- Los títulos son académicos e informativos.
- Persiste cierta repetición de grillas de cajas en slides conceptuales; se registra como problema menor, no como defecto mayor, porque la secuencia alterna con gráficos, procesos, ecuaciones, preguntas y tablas.

## Registro de problemas

| review_id | slide_id | category | severity | finding | evidence | recommended_fix | status | owner |
|---|---|---|---|---|---|---|---|---|
| U10-RV02-001 | U10-003, 010, 020, 022, 023, 028, 029, 038, 043, 049, 053, 062, 064, 067, 070, 071, 086, 087 | diagramas / contenido | major | El generador recortaba silenciosamente etiquetas de más de dos líneas; algunas perdían unidades, condiciones o significado. | Comparación de JSON fuente, SVG y render v01. | Redistribuir todo el texto en dos líneas y hacer fallar el preflight si no entra. | fixed-v02 | Codex |
| U10-RV02-002 | U10-049 | contenido / diagrama | major | El esquema de nivel equivalente perdía la condición temporal `T`. | Render v01 y fuente U10-DG-030. | Restituir `T` en título, ecuación y callouts. | fixed-v02 | Codex |
| U10-RV02-003 | U10-087 | fórmula / diagrama | major | El salto de línea separaba `ln 2` del resultado y volvía ambigua la igualdad. | Render v01 a tamaño completo. | Mostrar `∫[f→2f] K/ν dν = K·ln 2` como una igualdad continua de dos líneas. | fixed-v02 | Codex |
| U10-RV02-004 | U10-078 | diseño / diagrama | major | El diagrama validado aisladamente quedaba demasiado pequeño dentro de la composición final. | Render v01 a tamaño completo. | Ampliar el gráfico y reemplazar el diagrama reducido por tres cajas nativas editables. | fixed-v02 | Codex |
| U10-RV02-005 | U10-078 | gráfico / diseño | major | Tras la primera corrección, tres rótulos de eje vertical y una advertencia se superponían al gráfico. | Segunda inspección del render v02. | Usar un único eje vertical compartido y mover la advertencia al caption de la slide. | fixed-v02 | Codex |
| U10-RV02-006 | U10-042, 068, 085, 090 | diseño / legibilidad | major | Las tablas se serializaban cerca de 14 pt, insuficiente para aula. | Inspección OOXML y renders v01. | Aumentar fuente, encabezados y altura de filas. | fixed-v02 | Codex |
| U10-RV02-007 | U10-074 | diseño / pedagogía | major | Texto principal pequeño en una slide con amplio espacio sin usar. | Render v01. | Crear layout específico con bullets grandes y advertencia jerarquizada. | fixed-v02 | Codex |
| U10-RV02-008 | U10-082 | pedagogía / legibilidad | major | Las doce afirmaciones quedaban demasiado pequeñas para lectura cómoda. | Render v01. | Aumentar la tipografía y conservar dos columnas con numeración clara. | fixed-v02 | Codex |
| U10-RV02-009 | U10-089 | pedagogía / legibilidad | major | Cinco ejercicios y resultados se comprimían alrededor de 15 pt. | Render v01 y criterio del storyboard. | Sintetizar resultados visibles, ampliar tarjetas y llevar procedimiento a notas. | fixed-v02 | Codex |
| U10-RV02-010 | U10-093 | producción / legibilidad | major | La bibliografía se presentaba en filas genéricas con fuente pequeña. | Render v01. | Reagrupar en fuentes primarias, apoyo transversal y fuentes externas con tipografía mayor. | fixed-v02 | Codex |
| U10-RV02-011 | varias | naturalidad / diseño | minor | Se repite la grilla de cajas en varias slides conceptuales. | Revisión de las 93 slides. | En una futura revisión global, variar 3–4 layouts sin cambiar el sistema visual. | open | Docente |
| U10-RV02-012 | varias | diseño | minor | Captions y créditos usan una escala pequeña respecto del texto docente. | Renders finales. | Mantenerlos como metadatos; evaluar 1–2 pt extra si deben leerse desde el fondo del aula. | open-accepted | Docente |
| U10-RV02-013 | U10-035 | producción / multimedia | suggestion | Los audios comparativos previstos no tienen archivo local aprobado. | Manifiesto U10-AS-001/U10-AS-002 y notas. | Incorporar audio solo después de verificar archivo, licencia y nivel de reproducción; la alternativa estática ya es funcional. | open | Docente |
| U10-RV02-014 | U10-088, 091, 092 | contenido / fuentes | suggestion | No se muestran fórmula de intervalos desiguales, protocolo clínico completo ni límite normativo sin fuente verificada. | Slides y registros de recursos bloqueados. | Completar únicamente cuando se definan fuente, edición, jurisdicción y protocolo institucional. | open-accepted | Docente |

## Verificación final

| Control | Resultado |
|---|---|
| `slides_test.py` | pass; sin overflow |
| Validación estructural | 0 críticos, 0 mayores |
| Diagramas en contexto | 57 slides / 57 instancias; 0 críticos, 0 mayores |
| Render final | 93/93 PNG revisados |
| PDF de revisión | 93/93 páginas |
| Masters / layouts | 2 / 27 preservados |
| Notas | 93/93 |
| Alt text en imágenes | completo |
| Hipervínculos externos | 0 |
| Audio / video embebido | 0 |
| Slides aplanadas | 0 |
| SHA-256 v02 | `74D0E838F7D8930E4C3BC98D87441E517EF76BAA671DDBC088182C1D116AD88D` |

La unidad puede usarse como **v02 corregida**: no quedan problemas críticos ni mayores abiertos. Los problemas menores y sugerencias anteriores quedan registrados para una futura revisión global o para cuando existan fuentes y medios aprobados.
