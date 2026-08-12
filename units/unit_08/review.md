# Revisión integral — Unidad 08

## Dictamen

- Versión inicial auditada: `output/unidad_08_salud_auditiva_v01.pptx`.
- Versión corregida: `output/unidad_08_salud_auditiva_v02.pptx`.
- Render final auditado: 114/114 PNG en `output/unidad_08_salud_auditiva_v02/` y hoja de contacto `output/unidad_08_salud_auditiva_v02_contact_sheet.png`.
- Fuentes contrastadas: programa oficial, capítulo 8 en LaTeX, capítulo 8 en PDF, brief, storyboard, textos, notas y manifiesto de assets.
- Resultado final: **aprobada para esta revisión; 0 problemas críticos y 0 problemas mayores abiertos**.

La v01 tenía dos fallas críticas de contenido y ocho grupos de problemas mayores. La v02 corrige la contaminación de contenido heredado de otra unidad, sustituye los fallbacks genéricos, materializa mapas, procesos, tablas, gráficos y ejercicios que en v01 aparecían vacíos o incompletos, y conserva la secuencia pedagógica de 114 diapositivas. La revisión final se realizó sobre el PowerPoint abierto por el motor de render y sobre todas las imágenes resultantes, no sólo sobre texto u OOXML.

## Cobertura del programa

| Tema obligatorio | Estado final | Evidencia principal |
|---|---|---|
| Curvas pos-exposición y TTS | Cubierto | Slides 17–27 y ficha de trazabilidad 111. La curva didáctica se limita explícitamente y no se presenta como pronóstico. |
| Pérdida auditiva inducida por ruido | Cubierto | Slides 28–31; se exige historia de exposición y evidencia convergente. |
| Tinnitus o acúfenos | Cubierto | Slides 14, 32 y 61–64; se separa percepción referida de fuente física externa. |
| Presbiacusia | Cubierto | Slides 33–34; se presenta como heterogénea y multifactorial. |
| Riesgo porcentual por ruido ocupacional en función de edad | Cubierto | Slides 35–36 y 112; tabla NIOSH 1997 con definición de exceso de riesgo, exposición, edad e incertidumbre. |
| Audiometría y diferencia aérea–ósea | Cubierto | Slides 45–54, 104 y 109; escalas, unidades y condiciones compatibles visibles. |
| Logoaudiometría | Cubierto | Slides 55–60; porcentaje, nivel, material, escala y límite. |
| Timpanometría | Cubierto | Slides 65–72; barrido, inmitancia, ejes, morfologías y límites. |
| Acufenometría | Cubierto | Slides 61–64; correspondencia perceptual y dB SL sin reificar una fuente interna. |
| OEA, PEAT y ECoG | Cubierto | Slides 73–83 y 105; entrada, sensor, magnitud, generadores y alcance comparados. |
| Audífonos e implantes cocleares | Cubierto | Slides 84–94, 99, 106 y 110; entrada, procesamiento, salida, acoplamiento y límites. |

## Hallazgos y correcciones

| review_id | slide_id | dimensión | severidad inicial | problema | corrección verificada en v02 | estado |
|---|---|---|---|---|---|---|
| U08-R001 | 51 | contenido | critical | La diferencia aérea–ósea incluía una interpretación sobre fones y sones. | Se restituyeron `G_AO(f)`, dB HL, misma frecuencia y condiciones comparables; se explicitó el límite diagnóstico. | resolved |
| U08-R002 | 13, 58, 71, 76, 79, 91 | contenido/naturalidad | critical | Un fallback repetía una corrección sobre 0 dB SPL en seis temas no relacionados. | Cada slide contiene ahora afirmación problemática y corrección específicas. | resolved |
| U08-R003 | 38 | diagramas | major | Nodos vacíos y etapas fusionadas. | Cinco nodos semánticos, conectores anclados detrás de las cajas y cierre independiente. | resolved |
| U08-R004 | 2, 4, 7, 12, 16, 27, 30, 35, 41, 44, 46, 49, 57, 69, 81 | diseño/pedagogía | major | Visuales ausentes, scaffolding proyectado o slides casi vacías. | Se materializaron mapas, tablas, procesos, gráficos conceptuales, comparaciones y recapitulaciones. | resolved |
| U08-R005 | 16, 27, 44 | diseño/diagramas | major | Recapitulaciones comprimidas en cajas estrechas. | Ideas distribuidas en bloques equilibrados con tipografía de aula. | resolved |
| U08-R006 | 10, 38, 46, 56, 66, 74, 77, 80, 85, 86, 90 | diagramas | major | Conectores demasiado próximos al texto y jerarquía irregular. | Conectores creados antes de los nodos, corredores vacíos, puntas fuera de las áreas tipográficas y cuerpo de 22–24 pt. | resolved |
| U08-R007 | 107–109 | contenido/pedagogía | major | Ejercicios sin datos suficientes. | Se incorporaron tablas, datos, ecuaciones y consignas resolubles basadas en los ejercicios del capítulo. | resolved |
| U08-R008 | 110 | contenido | major | Ganancias distintas de las del ejercicio NA3. | Tabla y barras corregidas a 500/1000/2000 Hz y 10/15/21 dB; conclusión limitada. | resolved |
| U08-R009 | 35, 112 | cobertura/contenido | major | El requisito de riesgo porcentual sólo figuraba como brecha. | Se incorporó una tabla NIOSH 1997 por edad y exposición, con IC 95 % y advertencia contra la predicción individual. | resolved |
| U08-R010 | deck completo | naturalidad | major | Tarjetas genéricas, frases de producción y slides repetitivas. | Se eliminaron textos internos visibles, se variaron siluetas según función y se conservaron sólo repeticiones con función pedagógica. | resolved |
| U08-R011 | deck completo | diseño | major | Grandes vacíos sin función y cajas angostas con lectura incómoda. | Se reequilibró el área útil y se validaron todas las slides renderizadas. | resolved |
| U08-R012 | deck completo | producción | minor | El alt text de gráficos no quedaba serializado en el PPTX exportado. | 5/5 imágenes de contenido tienen `descr` no vacío; las 114 notas incluyen además una sección `[Alt text]`. | resolved |
| U08-R013 | deck completo | producción | minor | No hay videos o GIF embebidos ni enlaces multimedia activos. | Se mantienen alternativas estáticas; no se incorporan recursos externos sin aprobación. | accepted-open |
| U08-R014 | deck completo | pedagogía/producción | suggestion | 114 slides constituyen una ruta extensa para una sola exposición. | Se preservan cuatro encuentros y respaldo a demanda; conviene ocultar 103–114 cuando no se utilicen. | accepted-open |

## Revisión por dimensión

### Contenido

- Se verificaron definiciones, terminología, escalas dB SPL/dB HL/dB SL, ecuaciones, unidades y ejemplos contra el capítulo y el programa.
- Se corrigieron la ecuación aplicada de diferencia aérea–ósea y el ejercicio de ganancia.
- Los porcentajes NIOSH se presentan como exceso de riesgo poblacional y conservan definición, exposición, comparador e incertidumbre.
- Ninguna forma de audiograma, timpanograma u otra prueba se equipara automáticamente con una etiología.

### Pedagogía

- La secuencia progresa de clase de dato a exposición, estudios, dispositivos e integración.
- Hay preguntas, ejercicios, comparaciones y recapitulaciones en los cuatro encuentros.
- Los ejemplos numéricos separan datos, operación, resultado e interpretación.
- Las advertencias de error frecuente son ahora específicas y no plantillas intercambiables.

### Diseño, diagramas y naturalidad

- Revisión visual completa de 114/114 slides y a tamaño completo de las slides afectadas.
- No se observaron flechas sobre texto, etiquetas sobre conectores, puntas dentro de fórmulas, textos fuera de cajas, auto-shrink excesivo, ecuaciones ilegibles ni colisiones.
- Los procesos 38, 46 y 85 se rediseñaron en el tamaño real de la slide.
- Se preservó la identidad académica UCASAL y se evitó introducir stock decorativo, portadas publicitarias o iconos genéricos.

### Producción

- 114 slides, 114 notas, 2 masters, 27 layouts y relación 16:9.
- Archivo final: 659.403 bytes; sin macros, sin fuentes embebidas y sin dependencias tipográficas exóticas.
- El contenido se mantiene editable mediante texto, formas, conectores, tablas y ecuaciones; 5 gráficos se insertan como imagen con fuente reproducible en el repositorio.
- Numeración 1–114 y notas presentes en todas las slides.
- No se detectaron relaciones externas activas; las URLs de fuente permanecen como texto trazable en notas.

## Verificaciones finales

| control | resultado |
|---|---|
| Render final | 114/114 PNG |
| Revisión de hoja de contacto | aprobada |
| Revisión a tamaño completo de slides afectadas | aprobada |
| `slides_test.py` | `Test passed. No overflow detected.` |
| Apertura y parseo OOXML | aprobados |
| Alt text de imágenes | 5/5 |
| Problemas critical abiertos | 0 |
| Problemas major abiertos | 0 |

## Pendientes no bloqueantes

- Decisión docente sobre preferencia terminológica PAIR/HIR/NIHL y PEAT/PEATC.
- Selección y aprobación de multimedia externa si se desea reemplazar alternativas estáticas.
- El respaldo 103–114 puede ocultarse para una clase más breve; no forma parte de una quinta sesión obligatoria.
