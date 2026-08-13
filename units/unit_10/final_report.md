# Informe final — Unidad 10: Ruidos

**Fecha de cierre:** 12 de agosto de 2026  
**Versión final:** `output/unidad_10_ruidos_final.pptx`  
**Estado:** terminada según la definición de `AGENTS.md`  
**SHA-256:** `74D0E838F7D8930E4C3BC98D87441E517EF76BAA671DDBC088182C1D116AD88D`

## Dictamen de cierre

La Unidad 10 cumple la definición de terminado. Están presentes el brief, storyboard, texto visible, notas, manifiesto, scripts, gráficos, diagramas, PowerPoint, PDF de revisión, render completo, revisión integral y revisión de consistencia.

La cobertura del programa está completa. No quedan problemas críticos ni mayores abiertos: los diez grupos de problemas mayores detectados en v01 fueron corregidos y verificados en v02. La versión final es una copia binaria de v02, por lo que conserva exactamente el deck que pasó la revisión y no sobrescribe ninguna versión anterior.

## Inventario obligatorio

| Entregable | Evidencia | Estado |
|---|---|---|
| Brief | `brief.md` | Completo |
| Storyboard | `storyboard.md`, 93 slides planificadas | Completo |
| Texto visible | `slide_text.md` | Completo |
| Notas del orador | `speaker_notes.md`; 93/93 notas dentro del PPTX | Completo |
| Manifiesto de assets | `asset_manifest.csv`, 89 registros | Completo |
| Scripts | 11 scripts de producción en `scripts/` y 15 scripts reproducibles en los paquetes de gráficos | Completo |
| Gráficos | 15 paquetes U10-CH, con PNG, SVG, datos, parámetros, fuente, alt text y validación | Completo |
| Diagramas | 57 paquetes U10-DG, con PNG, SVG, fuente editable, alt text y validación | Completo |
| PowerPoint | `output/unidad_10_ruidos_final.pptx` | Completo |
| PDF de revisión | `output/unidad_10_ruidos_v02_preview.pdf`, 93 páginas | Completo |
| Render de revisión | `output/unidad_10_ruidos_v02/`, 93 PNG | Completo |
| Revisión integral | `review.md` | 0 críticos; 0 mayores abiertos |
| Revisión de consistencia | `consistency_report.md` | Aprobada con ajustes editoriales abiertos |

## Magnitud y organización de la presentación

- **Cantidad de slides:** 93.
- **Bloques:** 10, de B00 a B09.
- **Ruta central:** 74 slides.
- **Slides complementarias:** 10.
- **Respaldo:** 7 slides.
- **Fuente bloqueada:** 2 slides, conservadas como límites explícitos y no como contenido inventado.
- **Duración estimada:** 285 minutos para la ruta central y complementaria.
- **Distribución recomendada:** tres encuentros de 90–100 minutos; el respaldo se usa de manera no lineal.

| Bloque | Slides | Función | Duración estimada |
|---|---:|---|---:|
| B00 · Apertura | 5 | Caso, objetivos, prerrequisitos y mapa de clase | 12 min |
| B01 · Señal y contexto | 8 | Diferencia entre fenómeno, señal, función y ruido | 25 min |
| B02 · Tiempo y estadística | 12 | Aleatoriedad, estacionariedad, media, RMS, varianza y distribución | 40 min |
| B03 · Frecuencia y colores | 11 | PSD, banda, ruido blanco y ruido rosa | 38 min |
| B04 · Señales de prueba | 8 | Espectro de habla, NBN y especificación de banda | 25 min |
| B05 · Descriptores y SNR | 12 | Máximo, pico, equivalente, excedencia y relación señal-ruido | 40 min |
| B06 · Enmascaramiento | 8 | Fondo, enmascarador, oído, audiometría y acufenometría | 32 min |
| B07 · Exposición y control | 11 | Medición, límites de inferencia y control en fuente, trayecto y receptor | 43 min |
| B08 · Integración | 9 | Resolución por capas y síntesis del curso | 30 min |
| B09 · Respaldo | 9 | Glosario, ejercicios, fuentes y contenidos condicionados | 20–35 min si se usa |

## Temas cubiertos

- Diferencia contextual entre sonido y ruido.
- Señales determinísticas, procesos aleatorios y realizaciones.
- Estacionariedad dependiente del intervalo de observación.
- Clasificación temporal: continuo, fluctuante, intermitente e impulsivo.
- Media, RMS, varianza y distribución de amplitudes.
- Densidad espectral de potencia e integración por banda.
- Ruido blanco, rosa, con espectro de habla y de banda estrecha.
- Frecuencia central, límites, ancho de banda y pendientes de filtros.
- Nivel máximo, pico, nivel equivalente y niveles de excedencia.
- Suma energética, SNR y límites perceptuales de su interpretación.
- Ruido de fondo, señal enmascarante y protección auditiva.
- Enmascaramiento aplicado a audiometría y acufenometría, sin receta clínica universal.
- Exposición, resultado funcional y salud como planos relacionados pero distintos.
- Control en la fuente, el trayecto y el receptor.
- Documentación de condiciones, autoridad normativa y límites de inferencia.

## Recursos multimedia

- **Audio embebido:** 0.
- **Video embebido:** 0.
- **Hipervínculos externos en el PowerPoint:** 0.
- La slide U10-035 conserva una alternativa visual completa para comparar ruido blanco y rosa. Los cuatro registros de audio del manifiesto permanecen propuestos o condicionados; no se incorporaron porque no hay archivo local, licencia y nivel de reproducción aprobados.

La ausencia de audio o video no deja un vacío curricular: todas las explicaciones y actividades son funcionales con los recursos estáticos y editables disponibles.

## Gráficos propios

Se incluyen 15 gráficos reproducibles. Cada paquete contiene figura PNG y SVG, datos, parámetros, script, caption, alt text, fuente y validación. Cubren realizaciones, ventanas de estacionariedad, escala temporal, patrones temporales, distribución, PSD, ruido blanco y rosa, descriptores temporales, excedencia, SNR y comparación de casos.

Los 15 paquetes tienen estado de validación `approved`. Los gráficos usan ejes, unidades, escalas y paleta coherentes con el curso.

## Diagramas propios

Se validaron 57 instancias diagramáticas en el contexto de la slide final. Los paquetes conservan SVG, PNG, descripción, fuente, alt text y un PowerPoint editable independiente cuando corresponde.

Resultado de validación:

- 0 flechas sobre texto;
- 0 etiquetas montadas sobre conectores;
- 0 cajas desbordadas;
- 0 fuentes principales inferiores a 22 pt;
- ecuaciones centrales de 28 pt o más;
- 0 problemas críticos o mayores.

El deck final conserva texto, formas, conectores, retículas y ecuaciones diagramáticas editables. No contiene slides aplanadas como una única imagen.

## Fuentes principales

1. Programa oficial 2025 de Física Acústica, especialmente la formulación de la Unidad 10.
2. Capítulo LaTeX `context/libro_latex/chapters/10-ruido-caracterizacion.tex`.
3. Libro PDF *Física Acústica para Fonoaudiología*, pp. PDF 261–290.
4. `course_map.md`, `course_dependency_map.md`, glosario, guía de notación y decisiones visuales del curso.
5. Bibliografía y documentos técnicos registrados por el capítulo y el manifiesto, incluidos WHO, NIOSH/CDC, ISO, SRT Argentina y ASHA, usados con su alcance declarado.

La trazabilidad está registrada en `source_map.md`, `source_analysis.md`, `asset_manifest.csv` y los 93 bloques `[Sources]` de las notas. No se incorporaron cifras normativas, protocolos clínicos ni recursos externos sin fuente suficiente.

## Decisiones pedagógicas

- Organizar la unidad como cierre integrador: caso concreto → señal y contexto → tiempo → estadística → frecuencia → tipos → medición → enmascaramiento → exposición y control.
- Presentar intuición y pregunta física antes de cada formalización matemática.
- Separar descripción física, medición, interpretación perceptual, inferencia clínica y decisión normativa.
- Tratar “ruido vocal” como término del programa y preferir “ruido con espectro de habla” en la explicación técnica.
- Repetir el marco fuente → señal → contexto → receptor → control cuando cumple una función de integración.
- Mantener el enmascaramiento en un nivel conceptual y funcional hasta contar con un protocolo institucional validado.
- Usar ruta central, complementarias y respaldo para adaptar profundidad sin eliminar contenido obligatorio.
- Mostrar límites documentales y normativos en lugar de completar de memoria datos o procedimientos.

## Verificación de producción

| Control | Resultado final |
|---|---|
| Cobertura del programa | Completa |
| Problemas críticos abiertos | 0 |
| Problemas mayores abiertos | 0 |
| Problemas mayores de v01 | 10 grupos corregidos en v02 |
| `slides_test.py` | Pass; sin overflow |
| Validador estructural U10 | Pass; 0 críticos, 0 mayores |
| Integridad del archivo ZIP/PPTX | Pass |
| Formato | 16:9 |
| Slides / notas | 93 / 93 |
| Masters / layouts | 2 / 27; 23 layouts usados |
| Bloques `[Sources]` en notas | 93 / 93 |
| Numeración | 93 / 93 |
| Imágenes con alt text | Completo |
| Placeholders vacíos | 0 |
| Slides aplanadas | 0 |
| Enlaces externos | 0; no hay enlaces rotos |
| Audio / video embebido | 0; no hay medios rotos |
| Fuentes tipográficas | Calibri Light, Calibri y Cambria Math |
| Paleta | Bordó, carbón, gris, teal y ocre del sistema del curso |
| Tamaño del archivo | 1.439.017 bytes |
| Render / PDF | 93 PNG / 93 páginas |
| Identidad v02–final | SHA-256 idéntico |

## Limitaciones conocidas y aceptación

Las siguientes limitaciones no son críticas ni mayores y se aceptan para el cierre:

- cierta repetición de retículas de cajas en slides conceptuales;
- captions y créditos deliberadamente pequeños por funcionar como metadatos;
- algunos subíndices visibles conservan una construcción tipográfica menos refinada que la guía;
- algunos gráficos conservan punto decimal o notación científica anglosajona;
- varias notas incluyen campos o consignas genéricas que podrían depurarse;
- no se incorporaron los audios comparativos todavía no aprobados;
- las slides U10-088, U10-091 y U10-092 no inventan, respectivamente, un ejemplo no verificado, un protocolo institucional ni valores normativos universales.

Permanecen como decisiones globales del curso —no como defectos exclusivos de U10— el umbral entre OMML, texto matemático y SVG, el color definitivo de títulos y el criterio para tabla nativa frente a retícula de formas editables.

## Recomendaciones para dictar la clase

1. Dividir la ruta principal en tres encuentros y no intentar recorrer las 93 slides linealmente en una sola clase.
2. Usar U10-001–025 en el primer encuentro, U10-026–056 en el segundo y U10-057–084 en el tercero.
3. Detenerse en las recapitulaciones U10-013, U10-025, U10-044, U10-056, U10-064, U10-075 y U10-084 para comprobar comprensión.
4. Pedir siempre que el estudiante declare señal, banda, nivel, intervalo, ponderación y propósito antes de aceptar una clasificación o un número.
5. En U10-035 usar la alternativa visual salvo que los audios hayan sido incorporados y nivelados por la cátedra.
6. Reforzar que blanco no significa potencia igual por octava, que aleatorio no significa inmedible y que enmascarar no equivale a proteger.
7. Usar U10-085–093 solo ante dudas, para autocorrección o cuando se disponga de una fuente institucional aprobada.
8. No presentar las slides condicionadas como protocolo o norma vigente; conservar explícitos edición, jurisdicción, transductor y procedimiento.

## Conclusión

La Unidad 10 queda cerrada como versión final trazable, editable y apta para clase. La presentación satisface el alcance obligatorio, conserva las decisiones pedagógicas justificadas y no contiene problemas críticos ni mayores abiertos.
