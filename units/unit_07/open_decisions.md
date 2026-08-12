# Unidad 7 — Decisiones abiertas

## Propósito

Este registro reúne decisiones que afectan alcance, terminología, notación, secuencia, recursos o tiempo. No constituye un storyboard. Las decisiones de prioridad alta deben resolverse antes de aprobar una secuencia slide por slide.

## Decisiones adoptadas para esta etapa

| ID | Decisión | Justificación |
|---|---|---|
| DA-U07-01 | No crear storyboard ni PowerPoint. | Solicitud explícita y flujo obligatorio del repositorio. |
| DA-U07-02 | No redactar texto visible ni notas del orador. | Esta etapa termina en brief, inventario, análisis y decisiones. |
| DA-U07-03 | Tratar U7 como carga conceptual muy alta. | Coincidencia entre `AGENTS.md`, arquitectura curricular y cantidad de dominios simultáneos. |
| DA-U07-04 | Usar bloques breves y recapitulaciones frecuentes. | Requisito específico para U7. |
| DA-U07-05 | Organizar toda interpretación como estímulo–tarea–respuesta–condiciones. | Es el aporte metodológico central del capítulo y la evidencia mínima del mapa de dependencias. |
| DA-U07-06 | Mantener separadas magnitudes físicas, atributos perceptuales y conclusiones clínicas. | Evita equivalencias universales y prepara U8. |
| DA-U07-07 | Considerar LaTeX y PDF sustantivamente concordantes. | Se leyó el capítulo completo y se renderizaron las pp. 177–205 sin diferencias de contenido detectadas. |
| DA-U07-08 | Corregir “Hass” a Haas y distinguirlo del efecto de precedencia. | Coherencia con libro, glosario y bibliografía. |
| DA-U07-09 | Usar “diferencia interaural de nivel (ILD)” como término principal. | Es más preciso que “diferencia interaural de intensidad” del programa. |
| DA-U07-10 | No presentar valores universales de umbral, sensibilidad, sonoridad, enmascaramiento, inteligibilidad, precedencia o localización. | El capítulo explicita dependencia de procedimiento, señal, ambiente, población y oyente. |
| DA-U07-11 | No explorar didácticamente niveles elevados o límites superiores del campo audible. | Criterio de seguridad explícito del capítulo. |
| DA-U07-12 | No incorporar fuentes externas nuevas en esta etapa. | Las fuentes locales bastan para el análisis; datos normativos y assets se resolverán después. |
| DA-U07-13 | No modificar `course_map.md`, `course_dependency_map.md` ni `content_coverage_matrix.csv`. | El pedido limita la salida a cuatro archivos de U7; cualquier ajuste global queda registrado. |

## Decisiones pendientes

| ID | Prioridad | Decisión | Evidencia/tensión | Recomendación preliminar | Impacto si queda abierta | Estado |
|---|---|---|---|---|---|---|
| OD-U07-01 | Alta | Confirmar cantidad y duración de encuentros. | Ruta central estimada en 76–94 slides y cinco bloques de carga muy alta. | Planificar tres o cuatro encuentros; no comprimir a una clase única sin mover contenido explícitamente. | Determina central/complementario, cantidad de actividades y ritmo. | Pendiente de planificación docente. |
| OD-U07-02 | Alta | Definir tratamiento de curvas isofónicas normalizadas. | Programa exige curvas normalizadas; el libro solo muestra una construcción conceptual y cita ISO 226:2023. | Usar una curva conceptual para enseñar el procedimiento y, si la licencia/datos lo permiten, una figura normativa separada con norma, edición y condiciones. | Riesgo de incumplir el programa o presentar un esquema como dato normativo. | Pendiente de fuente/licencia. |
| OD-U07-03 | Alta | Confirmar edición normativa y fuente de datos de isofónicas. | La bibliografía local registra ISO 226:2023, 3.ª edición; los datos no están incorporados al repositorio. | Verificar la edición aplicable y construir la figura solo desde datos autorizados/trazables. | La curva podría quedar desactualizada, sin condiciones o sin autorización de uso. | Pendiente antes de `chart-generation`. |
| OD-U07-04 | Alta | Delimitar “concepto de ruido” en U7. | Programa lo exige; capítulo usa ruido funcionalmente y U10 es propietario de definición, tipos y estadística. | Incluir definición operativa breve como interferencia/sonido no deseado según tarea y explicitar el puente a U10. | Omisión programática o duplicación extensa de U10. | Pendiente de validación docente. |
| OD-U07-05 | Alta | Delimitar tiempo de reverberación en U7. | Programa lo exige; capítulo describe reverberación, pero no formaliza `T_60`; matriz lo marca parcial y U9 lo desarrolla. | Definir `T_60`, unidad y significado como descriptor, sin Sabine ni cálculo; reservar física y medición para U9. | Cobertura parcial o invasión curricular de U9. | Pendiente de validación docente. |
| OD-U07-06 | Alta | Fijar terminología visible fon/son frente a `phon`/`sone`. | Programa/glosario usan español; LaTeX usa formas inglesas en la ecuación. | Usar **fon** y **son** en texto y ejes; introducir `phon`/`sone` solo como equivalencia bibliográfica. | Inconsistencia entre slides, guía y capítulo. | Recomendación lista; falta validar. |
| OD-U07-07 | Alta | Resolver símbolo de sonoridad `N`. | U5 usa `N` para número de muestras; LaTeX U7 usa `N` para sonoridad; guía recomienda `N_son` si coinciden. | Adoptar `N_son` y registrar equivalencia con el capítulo. | Colisión transversal en unidades consecutivas y errores en fórmulas. | Recomendación lista; falta validar. |
| OD-U07-08 | Alta | Resolver `f_s` en el bloque de enmascaramiento. | LaTeX usa `f_s` para frecuencia objetivo; U5/guía usan `f_s` para frecuencia de muestreo. | Adoptar `f_obj` o `f_\mathrm{obj}`. | Confusión con un símbolo ya formalizado en U5. | Recomendación lista; falta validar. |
| OD-U07-09 | Media | Elegir `ERB_N` frente a `ERB`. | LaTeX usa `ERB_N`; guía transversal registra `ERB`; el subíndice recuerda población/modelo. | Conservar `ERB_N` al usar la ecuación y desarrollar su significado; usar ERB como término general. | Inconsistencia menor en gráficos y ejercicios. | Pendiente de notación. |
| OD-U07-10 | Alta | Definir peso de filtros auditivos, banda crítica y ERB. | No están en el programa; el libro los amplía; la matriz marca U07-X1 `out_of_scope`. | Mantener el modelo de filtros como importante para enmascaramiento; ubicar cálculo de ERB como complementario o respaldo salvo decisión docente. | Puede sobrecargar el núcleo o dejar el enmascaramiento sin mecanismo explicativo. | Pendiente según tiempo. |
| OD-U07-11 | Media | Definir profundidad de duración percibida, resolución e integración temporal. | El programa exige duración subjetiva; el libro añade dos conceptos cercanos. | Mantener la distinción conceptual en el núcleo; reservar curvas/ventanas cuantitativas para complemento. | Riesgo de mezclar tres conceptos o expandir demasiado el bloque. | Recomendación preliminar. |
| OD-U07-12 | Alta | Decidir tratamiento de SNR e inteligibilidad. | El programa vincula voz, sonoridad e inteligibilidad; el libro rechaza una relación universal. | Incluir un cálculo de SNR y dos casos con igual SNR pero condiciones diferentes; nunca asignar porcentaje universal. | Puede enseñarse una predicción falsa o quedar la aplicación demasiado abstracta. | Recomendación preliminar. |
| OD-U07-13 | Alta | Definir tratamiento de ALCons. | Es obligatorio; el libro ofrece porcentaje observado, pero advierte contra fórmulas predictivas no verificadas. | Mantener definición y cálculo observado como central; modelos de sala solo en respaldo con fuente y dominio. | Puede confundirse resultado, causa y predicción. | Recomendación lista; falta validar. |
| OD-U07-14 | Media | Decidir mención de STI y SII. | El capítulo los introduce como métodos distintos; no son exigidos por el programa. | Una slide/nota de respaldo que explique que existen y no son intercambiables; no calcularlos. | Sobrecarga y falsa sensación de dominio normativo. | Pendiente según tiempo. |
| OD-U07-15 | Alta | Definir estrategia para precedencia y Haas. | El programa usa “Hass”; el libro rechaza una regla universal de 20 ms. | Enseñar cálculo de retardo, luego respuestas graduales y finalmente el alcance histórico de Haas; incluir un distractor explícito sobre 20 ms. | Persistencia de una regla incorrecta o pérdida de trazabilidad. | Recomendación lista; falta validar. |
| OD-U07-16 | Media | Elegir profundidad del modelo geométrico de ITD. | El cálculo es útil, pero omite difracción y geometría real. | Mantener un ejemplo de orden de magnitud y acompañarlo con límites; modelos angulares más realistas como complemento. | Puede interpretarse `d/c` como constante anatómica exacta. | Recomendación preliminar. |
| OD-U07-17 | Alta | Definir estrategia de audios/demostraciones. | Pitch, timbre, enmascaramiento, inteligibilidad y precedencia se benefician de audio; el entorno de reproducción no es calibrado. | Inventariar equipo, nivel seguro, duración, formato y alternativa visual antes de incorporar cada demo. | Riesgo de seguridad, accesibilidad, variación entre dispositivos y conclusiones falsas. | Pendiente de recursos docentes. |
| OD-U07-18 | Alta | Seleccionar demostraciones seguras y no clínicas. | El capítulo prohíbe explorar niveles elevados; una demo de umbral puede confundirse con evaluación auditiva. | Usar comparaciones supraliminales y tareas conceptuales; no medir umbrales individuales ni usar auriculares sin control de nivel. | Riesgo de exposición, exclusión o interpretación clínica. | Pendiente de protocolo docente. |
| OD-U07-19 | Media | Definir uso de fundamental ausente. | Es una ampliación muy potente para pitch, pero requiere señal y visual coordinados. | Mantener como ejemplo importante si existe audio reproducible y alternativa espectral; si no, dejarlo complementario. | Puede consumir tiempo o quedar como afirmación sin experiencia. | Pendiente de assets. |
| OD-U07-20 | Alta | Seleccionar fuente y estrategia visual para curvas/gráficos. | Nueve TikZ son conceptuales; `FletcherMunson.png` y `enmascaramiento.png` no tienen trazabilidad verificada. | Priorizar reconstrucciones propias; usar rasters solo tras verificar origen, licencia, ejes y vigencia. | Curvas obsoletas, ilegibles o sin licencia. | Pendiente para `asset-curation`/`chart-generation`. |
| OD-U07-21 | Media | Reconstruir o reutilizar las nueve figuras TikZ. | Son correctas en PDF, pero varias contienen letra pequeña y demasiados elementos. | Reconstruir a tamaño real, editable y por etapas; dividir enmascaramiento, precedencia, espacio y escena concurrente cuando sea necesario. | Copiarlas produciría ilegibilidad o baja editabilidad. | Decisión recomendada; pendiente de producción. |
| OD-U07-22 | Media | Definir imágenes técnicas necesarias. | La mayoría de relaciones se explican mejor con gráficos/diagramas; campo libre y anatomía espacial pueden necesitar apoyo técnico. | Buscar solo montajes, CAE/cabeza y escenas que respondan una pregunta; evitar stock decorativo. | Trabajo de assets sin función o imágenes no trazables. | Pendiente para `asset-curation`. |
| OD-U07-23 | Alta | Seleccionar ejercicios para la ruta central. | El capítulo ofrece 39 grupos de consignas. | Una comprobación por bloque, cálculos de campo–tímpano, fon–son, enmascaramiento, SNR/ALCons y retardo; integradora al cierre; soluciones a respaldo. | Deck sobredimensionado o sin práctica distribuida. | Pendiente para storyboard. |
| OD-U07-24 | Media | Definir aplicaciones de dispositivos. | Audífonos, implantes y micrófonos direccionales son relevantes, pero corresponden en detalle a U8. | Mantener comparación “qué modifica físicamente / qué debe evaluarse perceptualmente”; no prescribir ni diagnosticar. | Invasión curricular y conclusiones clínicas indebidas. | Recomendación preliminar. |
| OD-U07-25 | Alta | Programar revisión pedagógica independiente. | `AGENTS.md` la exige para U7 por su densidad y riesgo de equivalencias conceptuales. | Revisar storyboard antes de redactar y volver a revisar el deck renderizado. | Errores pueden persistir aunque la presentación sea visualmente correcta. | Pendiente de responsable/etapa. |
| OD-U07-26 | Media | Programar revisión de seguridad/accesibilidad auditiva. | Varias actividades potenciales dependen de audio y diferencias auditivas individuales. | Verificar niveles, instrucciones, subtítulos/alternativas visuales y participación no obligatoria en tareas auditivas. | Riesgo de exclusión, exposición o resultados no comparables. | Pendiente de responsable/etapa. |
| OD-U07-27 | Media | Evaluar ajuste futuro de la matriz global. | U07-11 figura cubierto aunque el concepto de ruido es implícito; U07-12 es parcial; U07-X1 marca ERB fuera de alcance. | Revisar estados y notas con `course-architecture` después de fijar alcance, sin modificar la matriz en esta tarea. | Trazabilidad global puede no reflejar la decisión final. | Pendiente; fuera de los cuatro archivos. |
| OD-U07-28 | Baja | Confirmar capitalización del título y forma “Psicoacústica”. | Programa y capítulo difieren solo editorialmente. | Usar el título oficial y una capitalización coherente en portada/metadatos. | Inconsistencia menor de nombres. | Pendiente de estilo docente. |

## Decisiones de frontera curricular recomendadas

| Tema | Núcleo U7 | Puente permitido | Desarrollo reservado |
|---|---|---|---|
| Umbral | Definición psicofísica y condiciones | dB HL como anticipo terminológico | Protocolo de audiometría en U8. |
| Ruido | Interferencia/enmascarador dentro de una tarea | SNR y escena concurrente | Tipos, estadística, exposición y control en U10. |
| Reverberación | Persistencia perceptual y `T_60` como descriptor | Relación con inteligibilidad | Decaimiento, medición y Sabine en U9. |
| Enmascaramiento | Elevación del umbral y mecanismos | Ruidos enmascarantes como anticipo | Técnica audiométrica y tipos de ruido en U10/protocolo específico. |
| Estudios auditivos | Qué dato perceptual se obtiene | Umbral, habla, localización | Baterías, interpretación y diagnóstico en U8. |
| Dispositivos | Qué señal/pista pueden modificar | SNR, respuesta frecuencial, ITD/ILD | Selección, programación y rehabilitación en U8. |

## Orden recomendado de resolución antes del storyboard

1. confirmar cantidad y duración de encuentros;
2. resolver fuente, edición y estrategia para isofónicas normalizadas;
3. fijar la frontera de ruido y `T_60` con U9/U10;
4. adoptar fon/son, `N_son`, `f_obj` y convención de ERB;
5. decidir peso central/complementario de ERB, integración temporal, STI/SII e ITD geométrica;
6. seleccionar ejercicios y aplicaciones obligatorias;
7. definir audios, niveles, equipo, accesibilidad y alternativas visuales;
8. fijar estrategia de reconstrucción de las nueve figuras y búsqueda de imágenes;
9. programar revisión pedagógica y de seguridad/accesibilidad independiente;
10. registrar para una tarea posterior cualquier ajuste necesario en la matriz global.
