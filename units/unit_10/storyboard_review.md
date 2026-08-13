# Unidad 10 — Revisión del storyboard

## Dictamen

**Aprobado con condiciones para pasar a curación de recursos, prototipado de gráficos y diagramas.** El storyboard cubre el alcance obligatorio, sostiene una progresión apropiada para primer año y no adelanta la redacción completa de slides. No está aprobado todavía para producir el PowerPoint.

Condiciones antes de redactar slides:

1. Mantener U10-091 y U10-092 como `blocked-source` hasta contar con, respectivamente, un protocolo clínico institucional y una fuente normativa aplicable.
2. Verificar el ejemplo de intervalos de distinta duración de U10-088 antes de desarrollarlo.
3. Prototipar a tamaño final los diagramas y gráficos de alta densidad indicados en los inventarios iniciales.
4. Confirmar, al preparar cada encuentro, qué slides `complementary` se usarán en el flujo y cuáles quedarán disponibles para adaptación docente.

## Auditoría estructural

La tabla fue validada de forma automática:

- 93 filas de slides, desde U10-001 hasta U10-093, sin identificadores repetidos;
- 15 columnas en las 93 filas;
- 74 slides `central`, 10 `complementary`, 7 `backup` y 2 `blocked-source`;
- todas las filas tienen fuente, prerrequisito, transición y estado;
- todas las clases visuales pertenecen al vocabulario permitido;
- 60 necesidades de diagramas y 14 necesidades de gráficos poseen identificadores trazables;
- no se redactó contenido final visible ni notas completas del orador.

## Cobertura del programa y de las fuentes principales

| Alcance obligatorio | Cobertura en storyboard | Evaluación |
|---|---|---|
| Diferencia entre ruido y sonido | U10-002, U10-007–010 y U10-013 | Cubierto sin presentar el ruido como una propiedad física única. |
| Clasificación y tipos de ruido | U10-011–018, U10-031–044 | Cubierto en los ejes predictibilidad, evolución temporal y distribución espectral. |
| Ruido aleatorio | U10-011–012, U10-015–025 | Cubierto con realizaciones, estacionariedad y estadística accesible. |
| Ruido blanco | U10-031–032, U10-034–036 | Cubierto mediante PSD constante, bandas y percepción cautelosa. |
| Ruido rosa | U10-033–036; derivación en U10-087 | Cubierto; formalismo extendido reservado al respaldo. |
| Ruido con espectro de habla | U10-038, U10-042–044 | Cubierto como señal conformada y comparada con las otras familias. |
| Ruido de banda estrecha | U10-039–044 | Cubierto mediante filtro, frecuencia central, ancho de banda y aplicación. |
| Enmascaramiento | U10-052, U10-057–064 | Cubierto como fenómeno y arquitectura de prueba. El protocolo clínico completo queda explícitamente bloqueado. |
| Medición, exposición y control del ruido | U10-045–056 y U10-065–075 | Ampliación justificada por el capítulo y necesaria para caracterizar y aplicar. |

La comparación de fuentes queda respetada: el programa define el mínimo; el LaTeX organiza el desarrollo; el PDF se usa para verificar figuras, tablas y paginación. No se toma la versión PDF antigua como autorización para importar material descartado sin decisión pedagógica.

## Revisión de la secuencia pedagógica

La progresión parte de una situación de consulta y avanza por capas:

1. **Función y contexto:** evita que “ruido” quede fijado como sinónimo de sonido fuerte o desagradable.
2. **Tiempo y estadística:** crea la necesidad de media, RMS, varianza y distribución antes de presentar las ecuaciones.
3. **Frecuencia:** presenta densidad y banda como respuestas a una limitación de los descriptores temporales.
4. **Señales especificadas:** blanco, rosa, habla y NBN aparecen después de contar con el criterio espectral para distinguirlos.
5. **Medición:** máximo, pico, equivalente, percentiles, fondo y SNR se organizan por pregunta, no como catálogo.
6. **Enmascaramiento:** se recupera percepción auditiva y se explicita la frontera entre fenómeno y protocolo.
7. **Exposición y control:** separa medición, inferencia sanitaria, documento normativo y mecanismo de intervención.
8. **Integración:** el caso inicial se resuelve con las mismas capas y cierra con límites de interpretación.

La secuencia es gradual y no introduce simultáneamente más de una nueva relación matemática central. Las excepciones de mayor densidad incluyen ejemplos o recapitulación inmediata.

## Preguntas guía y transiciones

Cada bloque posee una pregunta guía operacional. Las transiciones cumplen una función causal: cada bloque nace de una insuficiencia del anterior —por ejemplo, una muestra no resume una señal, un RMS no describe el reparto espectral y una medición no determina por sí sola una intervención—. No se detectan saltos temáticos sin puente.

El enlace con la Unidad 9 está controlado: se reutilizan el caso de la clínica y la organización fuente–trayecto–receptor, pero no se vuelve a enseñar propagación, aislamiento ni acústica de recintos. El enlace con las Unidades 5, 7 y 8 también se trata como recuperación, no como repetición completa.

## Carga cognitiva por bloque

| Bloque | Carga | Razón | Mitigación prevista |
|---|---|---|---|
| B00 · Apertura | Baja | Orientación, objetivos y activación. | Caso único y mapa visible. |
| B01 · Señal y contexto | Media | Requiere separar término cotidiano, representación y función. | Casos contrastados y recapitulación U10-013. |
| B02 · Tiempo y estadística | Muy alta | Estacionariedad, categorías temporales y tres descriptores matemáticos. | Ventanas, cálculo breve, gráfico comparativo y recapitulación U10-025. |
| B03 · Frecuencia y colores | Muy alta | Densidad espectral, ancho de banda y escalas lineal/logarítmica. | Construcción por área, comparación blanco/rosa y recapitulación U10-036. |
| B04 · Señales de prueba | Alta | Filtros, espectro de habla y NBN pueden confundirse. | Árbol de elección, audio opcional y recapitulación U10-044. |
| B05 · Descriptores y SNR | Muy alta | Varios detectores y operaciones logarítmicas cercanas. | Una misma señal de referencia, ejemplos separados y selector final U10-056. |
| B06 · Enmascaramiento | Alta | Cruza física, percepción y práctica audiométrica. | Cuatro elementos fijos y límite de protocolo en U10-064. |
| B07 · Exposición y control | Alta | Riesgo de mezclar magnitud, efecto, norma y acción. | Tres planos, lectura documental y cadena de control. |
| B08 · Integración | Alta | Coordina todos los descriptores y límites. | Caso estable desarrollado en tres capas y matriz de respuesta. |
| B09 · Respaldo | Variable | Incluye derivaciones, soluciones y material condicionado. | Acceso no lineal; no forma parte del flujo base. |

## Repetición pedagógica frente a redundancia

La repetición está justificada cuando cambia la operación cognitiva:

- RMS pasa de significado estadístico a variable que sustenta nivel y energía de banda.
- Banda pasa de ventana de integración a parámetro de una señal NBN.
- SNR pasa de definición física a criterio de análisis de una tarea comunicativa.
- Fuente–trayecto–receptor pasa de modelo de propagación aprendido en U9 a organizador de control.
- Enmascaramiento pasa de fenómeno perceptual visto en U7 a uso funcional en una prueba.

Se evita repetir definiciones completas, derivaciones o desarrollos ya dados. Las recapitulaciones no agregan un nuevo catálogo: reorganizan relaciones, límites o decisiones.

## Frecuencia de comprobaciones y recapitulaciones

La unidad incluye preguntas o actividades en U10-010, 018, 023, 030, 041, 050, 053, 060–061, 072, 081 y 082. Las recapitulaciones parciales U10-013, 025, 036, 044, 056, 064 y 075 cierran cada tramo de alta carga; U10-083 integra el conjunto.

La densidad de comprobaciones es adecuada para tres encuentros. En una versión abreviada no conviene retirar simultáneamente la actividad y la recapitulación de un mismo bloque.

## Revisión visual y de template

- Se usan layouts del template inspeccionado para portada, objetivos, mapa, divisores, definiciones, comparaciones, procesos, ecuaciones, ejemplos, actividades, aplicaciones, recapitulaciones, apéndice y cierre.
- La alternancia `diagram` / `chart` / `equation_only` / `mixed` reduce el efecto de slides clonadas.
- Los gráficos cuantitativos están separados de los diagramas conceptuales y tienen inventario propio.
- Las ecuaciones anotadas se consideran diagramas editables cuando contienen callouts, conectores o secuencias.
- La única imagen externa centralmente útil es la situación de medición; posee alternativa diagramática si la licencia o calidad no resultan adecuadas.
- El audio comparativo es complementario y tiene una representación visual equivalente; la comprensión no depende de reproducción multimedia.

Riesgo visual principal: 51 slides tienen `visual_class=diagram` y 8 son `mixed`. Esto no implica 59 composiciones independientes: varias forman familias reutilizables —mapa de clase, caso integrador, selector de descriptores y recapitulaciones—. La producción deberá reutilizar geometrías consistentes sin repetir mecánicamente el layout.

## Trazabilidad de ideas importantes

Cada fila cita programa, sección LaTeX/PDF, mapas del curso o decisión didáctica. Las ampliaciones propias se identifican como ejemplo, ejercicio o síntesis. Durante `slide-writing`, las notas deberán contener bloques `[Sources]` con las referencias concretas; la bibliografía final U10-093 no sustituye la trazabilidad por slide.

## Slides centrales, complementarias y de respaldo

- **Centrales (74):** constituyen la ruta pedagógica U10-001–084 salvo las diez marcadas `complementary`.
- **Complementarias (10):** profundizan pseudoaleatoriedad, percepción del color, audio comparativo, respuesta temporal, percentiles/exposición, tinnitus, inferencia sanitaria, documentación y medición exploratoria. Pueden entrar según tiempo y perfil del grupo sin romper la secuencia.
- **Respaldo (7):** glosario, derivaciones, combinación temporal, soluciones, tabla de descriptores y fuentes.
- **Bloqueadas (2):** protocolo clínico completo y valores normativos. Conservan el lugar curricular sin autorizar contenido no verificado.

## Duración y viabilidad

La ruta central más complementos previstos suma aproximadamente 285 minutos, distribuibles en tres encuentros de 90–100 minutos. El respaldo puede añadir 20–35 minutos si se utiliza. La cifra no impone un máximo: expresa la profundidad real del capítulo, el nivel de entrada y el tiempo de interacción.

No es viable comprimir toda la unidad en una única clase sin redefinir objetivos. Si hubiera que reducir duración, la decisión correcta es seleccionar slides `complementary` y parte de la actividad integradora, no eliminar ejemplos, recapitulaciones o definiciones necesarias.

## Riesgos abiertos

| Riesgo | Severidad | Control previsto | Estado |
|---|---|---|---|
| Protocolo clínico de masking incompleto en fuentes base | Crítica | Mantener U10-091 y U10-DG-060 bloqueados | abierto |
| Valores normativos sin jurisdicción/edición confirmada | Crítica | Mantener U10-092 bloqueada | abierto |
| Densidad de ecuaciones en B02, B03 y B05 | Alta | Ejemplo tras ecuación, recapitulaciones y derivaciones en respaldo | controlado en storyboard |
| Confusión entre blanco/rosa/NBN/habla | Alta | Criterio común, comparación coordinada y actividad U10-043 | controlado en storyboard |
| Enmascaramiento confundido con protección | Alta | Contraste explícito U10-062 y cierre U10-064 | controlado en storyboard |
| Uso causal de exposición o SNR | Alta | Slides de límite U10-055, U10-066–068 | controlado en storyboard |
| Diagramas excesivamente densos | Alta | Prototipado temprano, render a tamaño final y posible división | pendiente de producción |
| Dependencia de multimedia | Media | Audio complementario con alternativa visual | controlado en storyboard |
| Ejemplo U10-088 sin verificación final | Media | Verificar fórmula, datos y fuente antes de redactar | abierto |

## Próxima puerta de calidad

El siguiente paso autorizado por este storyboard es desarrollar y validar recursos visuales iniciales —en especial U10-CH-002 a U10-CH-010 y U10-DG-005, 011, 017, 023, 038, 045 y 050–055—. Después corresponde `slide-writing`. La producción del PowerPoint debe esperar a que existan texto visible, notas y assets aprobados.
