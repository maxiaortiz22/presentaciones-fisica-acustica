# Unidad 5 — Revisión del storyboard pedagógico

## Dictamen

**Aprobado con decisiones abiertas para pasar a especificación de recursos, gráficos y diagramas.** El storyboard cubre el programa oficial, conserva la progresión del brief y distingue una ruta central de módulos complementarios y respaldo. No autoriza todavía la redacción completa de slides ni la producción del PowerPoint.

La extensión propuesta —150 slides totales, 104 centrales, 28 complementarias y 18 de respaldo— es coherente con la carga conceptual muy alta, pero exige una implementación modular. La ruta central se estima en 438 minutos y se distribuye en cinco encuentros; el tercer encuentro requiere ajuste o división adicional.

## Fuentes revisadas

- `AGENTS.md`.
- Programa oficial 2025, Unidad 5, pp. 3–4.
- `context/libro_latex/chapters/05-analisis-frecuencial.tex` y figuras asociadas.
- Libro PDF, capítulo 5, pp. 119–149.
- `units/unit_05/brief.md`, `content_inventory.md`, `source_analysis.md` y `open_decisions.md`.
- `course_map.md`, `course_dependency_map.md` y `content_coverage_matrix.csv`.
- Guías de estilo, notación y glosario.
- `style/layout_catalog.md`, `style/component_catalog.md`, template v01 y mosaico del template.
- Presentación final, storyboard y revisión de la Unidad 4 como precedente de continuidad.

## Verificación estructural

| control | resultado | estado |
|---|---:|---|
| Filas de storyboard | 150 | conforme |
| IDs únicos | 150 | conforme |
| Secuencia U05-001–U05-150 | Sin faltantes ni duplicados | conforme |
| Columnas por fila | 15 en todas las filas | conforme |
| Slides centrales | 104 | conforme |
| Slides complementarias | 28 | conforme |
| Slides de respaldo | 18 | conforme |
| `visual_class` permitidas | 37 `chart`, 48 `diagram`, 36 `mixed`, 13 `equation_only`, 3 `external_image`, 3 `video_or_gif`, 10 `none` | conforme |
| Layouts utilizados | 26 nombres: 23 del catálogo y 3 variantes aceptadas en `template_review.md`/template | conforme |
| Candidatas explícitas a `diagram-generation` | 91 | conforme; agrupadas en 15 familias |
| Candidatas explícitas a `chart-generation` | 34 menciones de slide | conforme; agrupadas en 19 familias |
| Alternativa estática en multimedia | Prevista en los tres casos | conforme |
| Redacción completa de slides | No realizada | conforme con alcance |

## Cobertura del programa oficial

| alcance obligatorio | slides principales | tratamiento | resultado |
|---|---|---|---|
| Representación de señales complejas | U05-008–017 | Tiempo, magnitud, fase y categorías temporales | cubierto |
| Serie de Fourier | U05-018–024, U05-133–134 | Intuición, estructura, ejemplo; coeficientes a respaldo | cubierto y graduado |
| Transformada de Fourier | U05-025–029, U05-135 | Significado, magnitud/fase e integral de referencia | cubierto y graduado |
| Gráficos de espectro | U05-009–017, U05-029, U05-046–051 | Lectura de ejes, ordenada, condiciones y tiempo–frecuencia | cubierto |
| Gráficos de respuesta en frecuencia | U05-052–062 | Entrada–sistema–salida, `H(f)` y ganancia | cubierto |
| Infrasonido, audible y ultrasonido | U05-074–079 | Fronteras aproximadas, condiciones y aplicación | cubierto con cautela |
| Rango dinámico vocal e instrumental | U05-080–081 | Definición y comparación condicionada | cubierto; datos reales pendientes |
| Rango dinámico auditivo y umbral de dolor | U05-079–083 | Formulación del programa y límites no universales | cubierto; validación docente pendiente |
| Fundamental, armónicos, parciales y sobretonos | U05-063–070 | Definiciones, contraejemplos y actividad | cubierto |
| Armónicos y octavas | U05-089–090 | Comparación explícita de múltiplos y razón `2:1` | cubierto |
| División del espectro en bandas | U05-084–094 | Bin/banda, octavas, tercios, centro, límites y ancho | cubierto |
| Filtros | U05-095–105 | Tipos, ideal/real, corte, transición y aplicaciones | cubierto |
| Frecuencia límite y central | U05-086–091, U05-096–100 | Ecuaciones y criterios declarados | cubierto |
| Ancho de banda | U05-091–094, U05-100 | Ancho absoluto y relación con filtro | cubierto |
| Curva de ponderación A / dBA | U05-106–116 | A en contexto A/C/Z; notación técnica y límites | cubierto; curva normativa pendiente |
| Medidor de nivel de presión sonora | U05-117–124 | Sonómetro, cadena, configuración y descriptores | cubierto |

No se detectan omisiones del programa. Las ampliaciones digitales, de voz y de sonometría están rotuladas como soportes, complementos o respaldo y no sustituyen el núcleo obligatorio.

## Trazabilidad de objetivos

| objetivo del brief | evidencia principal | comprobación prevista |
|---|---|---|
| O1. Comparar representaciones | U05-008–017, U05-046–048 | Lectura guiada y recap U05-017/051 |
| O2. Explicar Fourier y distinguir transformada/DFT/FFT | U05-018–040 | Síntesis progresiva, tabla de distinciones y mini ejercicio |
| O3. Relacionar `T_0`, `f_0`, `T_obs` y `Δf` | U05-015, U05-033–039 | Cálculos guiados y comparación de registros |
| O4. Diferenciar señal y sistema | U05-052–062 | Ejemplo de ganancia, aplicación y pregunta de control |
| O5. Identificar componentes y formantes | U05-063–073 | Tres casos, clasificación y caso de voz |
| O6. Interpretar rangos | U05-074–083 | Escalas condicionadas, aplicación y recap |
| O7. Calcular bandas y reconocer filtros | U05-084–105 | Ejemplo de tercio, ejercicio y respuestas de filtros |
| O8. Interpretar ponderación y sonómetro | U05-106–124 | Curvas, ejemplo tonal, error de banda ancha y cadena de medición |

Todos los objetivos tienen presentación, práctica o pregunta de comprobación y recuperación posterior. No hay objetivos declarados sin evidencia observable.

## Revisión de progresión y carga cognitiva

| bloque | carga | juicio | control incorporado |
|---|---|---|---|
| B00 | media | Adecuada para activar y diagnosticar | Objetivos, puente, mapa y rutina de lectura |
| B01 | alta | Gradual; una representación por vez | Comparación y recap antes de Fourier |
| B02 | muy alta | Correcta si la matemática permanece estratificada | Intuición → ecuación → ejemplo → recap; coeficientes a respaldo |
| B03 | muy alta | Necesaria para conectar con análisis real | Ruta mínima central; detalle de DFT/aliasing a complemento/respaldo |
| B04 | muy alta | Densa pero pedagógicamente justificada | Ventana y fuga antes de espectrograma; actividad breve y recap |
| B05 | muy alta | Nudo crítico correctamente aislado | Cadena `X–H–Y`, ejemplo, aplicaciones y recap |
| B06 | alta | Terminología propensa a interferencia | Comparaciones, casos límite y aplicación vocal |
| B07 | alta | Riesgo de memorizar fronteras | Condiciones y límites visibles en cada escala |
| B08 | muy alta | Exige razón, escala logarítmica y álgebra | De octava intuitiva a centro/límites/ancho; ejemplo y ejercicio |
| B09 | muy alta | Conceptos visualmente parecidos | Clasificación gradual, ideal/real y aplicación separada |
| B10 | muy alta | Riesgo metrológico/perceptual | A/C/Z en contexto, ejemplo tonal y error de banda ancha |
| B11 | muy alta | Integra varias decisiones previas | Cadena de medición, ficha de condiciones y descriptores separados |
| B12 | media–alta | Adecuada como transferencia | Casos, árbol de selección, autoevaluación y puente a U6 |
| B13 | variable | No interrumpe el hilo central | Detalle formal, normativo y soluciones a demanda |

### Riesgo de duración

La ruta central suma aproximadamente 438 minutos de exposición/actividad. La propuesta de cinco encuentros es viable con pausas y trabajo activo, pero B06–B08 concentra 116 minutos. Se recomienda una de estas decisiones antes de `slide-writing`:

1. dividir ese tramo en dos encuentros y convertir la unidad en seis clases; o
2. mantener cinco encuentros y trasladar U05-068, U05-070–071, U05-078, U05-081 y U05-093 a trabajo asincrónico/consulta.

La decisión no cambia la cobertura central porque los conceptos obligatorios permanecen en las slides contiguas.

## Repetición pedagógica frente a redundancia

### Repetición funcional aprobada

- La rutina “objeto–ejes–unidades–condiciones” reaparece al cerrar cada bloque, pero agrega una variable nueva.
- La cadena entrada–sistema–salida se recupera en filtros, voz y sonometría con objetos diferentes.
- `f_0` se retoma como relación temporal, índice armónico y dato de interpretación vocal.
- Bin y banda se presentan primero como contraste y luego se integran con octavas.
- Ponderación A reaparece como curva, operación tonal, límite en banda ancha y configuración sonométrica.

### Redundancia que debe evitar `slide-writing`

- Copiar definiciones completas en cada recap.
- Repetir una misma figura con idénticos callouts.
- Volver a explicar toda la serie de Fourier al introducir DFT.
- Usar “¿qué aprendimos?” como título genérico sin una relación nueva.
- Duplicar la misma advertencia en texto visible y notas sin asignarle una acción al estudiante.

## Revisión visual y de template

- La secuencia alterna apertura, comparación, gráfico, ecuación, proceso, ejercicio y recap; no se apoya en un único layout.
- Los layouts sugeridos existen en el sistema vigente: 23 están en `layout_catalog.md` y `FA_02B_CONOCIMIENTOS_PREVIOS`, `FA_06B_DOS_COLUMNAS` y `FA_14B_MINI_EJERCICIO` son variantes documentadas en `template_review.md` y usadas por la Unidad 4.
- Las figuras del libro se reconstruyen para 16:9 y no se insertan como página recortada.
- Los tres recursos multimedia tienen alternativa estática.
- Las imágenes externas se limitan a tres slides y cumplen una función técnica.
- Las 91 candidatas a `diagram-generation` fueron agrupadas para reducir inconsistencia y carga de producción.
- Los 37 gráficos cuantitativos se organizan en 19 familias reproducibles.

## Decisiones pedagógicas adoptadas por el storyboard

1. La unidad se organiza por objeto de lectura, no por sucesión de fórmulas.
2. Fourier se presenta como representación matemática, nunca como mecanismo que crea componentes.
3. DFT/FFT, ventana y espectrograma tienen una ruta central mínima; su formalismo profundo queda fuera del hilo principal.
4. La integral compleja se muestra como referencia, no como procedimiento evaluable.
5. Espectro de señal y respuesta de sistema constituyen el nudo central de B05.
6. Fundamental, máximo espectral, armónico, parcial, sobretono y formante se contrastan con casos límite.
7. El tratamiento de rangos explicita población, condición, descriptor y límite de inferencia.
8. Armónicos y octavas se comparan de manera explícita.
9. `dBA` se reconoce como escritura del programa; la unidad adopta `dB(A)` y descriptores completos en el uso técnico.
10. Sonómetro se usa como término preferido, aclarando la formulación del programa.
11. `L_eq`, máximo y pico se introducen para interpretar resultados y preparar U10, no como curso normativo.
12. Toda aplicación de voz o audición explicita que un gráfico aislado no produce diagnóstico.

## Decisiones abiertas antes de producción

| prioridad | decisión | impacto |
|---|---|---|
| alta | Confirmar cinco o seis encuentros | Define ruta proyectada y lugar de complementarias |
| alta | Validar con el docente profundidad de DFT, ventana y espectrograma | Evita desconexión de software o exceso digital |
| alta | Resolver notación `X(f)`/`P(f)` y metadatos de ordenada | Afecta todos los gráficos espectrales |
| alta | Verificar fuente/edición para A/C/Z y bandas | Condiciona gráficos y cifras normativas |
| alta | Definir datos válidos para rangos vocal e instrumental | Evita tablas genéricas engañosas |
| alta | Validar tratamiento de umbral de dolor/incomodidad | Tensión explícita entre programa y libro |
| media | Seleccionar registro de voz real o sintético | Afecta espectrograma, formantes y permisos |
| media | Confirmar equipo de audio y sonómetro | Afecta demostraciones y contingencias |
| media | Decidir cuáles complementarias serán asincrónicas | Controla duración efectiva |
| media | Corregir referencias U05 de `content_coverage_matrix.csv` con `course-architecture` | Mejora trazabilidad; no bloquea contenido |

## Riesgos pedagógicos y mitigación

| severidad | riesgo | mitigación prevista | estado |
|---|---|---|---|
| alta | Serie, transformada, DFT y FFT como sinónimos | Tabla comparativa, secuencia diferenciada y recap | controlado en storyboard |
| alta | “FFT = intensidad” | Ordenada y normalización obligatorias | pendiente de gráficos |
| alta | Espectro de salida = respuesta del sistema | B05 completo y casos de aplicación | controlado en storyboard |
| alta | Pico mayor = `f_0` | Fundamental ausente y armónico dominante | controlado en storyboard |
| alta | Octava = diferencia fija en Hz | Eje logarítmico y dos ejemplos | controlado en storyboard |
| alta | A = audición individual o dB HL | Comparación explícita y límites | controlado en storyboard |
| alta | Promediar dB para obtener `L_eq` | Ejemplo energético y respaldo integral | controlado en storyboard |
| alta | Fatiga por densidad y extensión | Ruta modular, recap cada 7–10 slides y cinco/seis encuentros | decisión docente pendiente |
| media | Diagramas ilegibles por exceso de nodos | Familias, tamaños mínimos y ciclo render/revisión | pendiente de producción |
| media | Multimedia no disponible | Alternativa estática y demos precomputadas | previsto |
| media | Datos técnicos presentados como universales | Metadatos, fuentes y cautelas visibles | pendiente de curaduría |

## Condiciones para avanzar

Antes de redactar el contenido completo de las slides se recomienda:

1. aprobar la ruta temporal de cinco o seis encuentros;
2. fijar la notación espectral y la ficha de metadatos;
3. seleccionar las familias de gráficos y diagramas de prioridad alta;
4. verificar las fuentes normativas necesarias;
5. resolver voz, audio y disponibilidad de instrumentos;
6. actualizar en `open_decisions.md` qué decisiones quedan adoptadas;
7. producir y renderizar primero las figuras conceptualmente críticas.

## Estado final de esta revisión

**Storyboard pedagógicamente coherente, completo y trazable; aprobado con condiciones para la siguiente fase de diseño de recursos.** Se mantiene explícitamente fuera de alcance la redacción completa de slides y la creación del PowerPoint.
