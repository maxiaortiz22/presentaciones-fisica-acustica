# Unidad 6 — Decisiones abiertas

## Propósito

Este registro reúne decisiones que afectan alcance, terminología, notación, secuencia, recursos o tiempo. No constituye un storyboard. Las decisiones de prioridad alta deben resolverse antes de aprobar una secuencia slide por slide.

## Estado de cierre final

Esta tabla reemplaza el estado histórico de las filas originales para la versión final. Las alternativas aceptadas no se consideran problemas críticos ni mayores abiertos.

| Tema | Decisión final | Estado |
|---|---|---|
| Título y frontera de U6 | Se adopta “El mecanismo periférico de la percepción auditiva”; el título oficial del programa queda registrado en brief e informes. | Resuelta. |
| Duración | Se organiza el deck en cuatro encuentros visibles: 1–39, 40–71, 72–93 y 94–105; 106–117 es respaldo. | Resuelta. |
| Frente de onda en CAE | Se enseña como contraste entre modelos ideales y conducto real, no como conversión universal. | Resuelta. |
| Conducción ósea | Vista convergente central y mecanismos detallados como ampliación/respaldo. | Resuelta. |
| Profundidad electroquímica | Mapa intuitivo central; detalle molecular seleccionado como ampliación o respaldo. | Resuelta. |
| Codificación periférica | Puente breve hacia U7/U8; sincronización temporal y mediciones avanzadas son complementarias. | Resuelta. |
| Anatomía y micromecánica | Se incorporan visuales propios acumulativos y editables; la validación por especialista se conserva como recomendación institucional, no como bloqueo. | Resuelta con recomendación. |
| Multimedia | No se incrusta multimedia; las alternativas estáticas son completas y autosuficientes. | Aceptada. |
| Demostraciones | Permanecen opcionales en notas y no son necesarias para comprender el deck. | Aceptada. |
| Ejercicios | Se conservan comprobaciones distribuidas y G1–G3 resueltos en respaldo; G3 incluye datos, cálculo e interpretación. | Resuelta. |
| Aplicaciones | OEA, potencial evocado e inmitancia se tratan funcionalmente, sin protocolo ni inferencia diagnóstica automática. | Resuelta. |
| Revisión independiente | Completada y aplicada a storyboard, notas y versión final. | Resuelta. |
| Sigla de potenciales evocados | No se fija PEAT/PEATC/ABR; se usa el término desarrollado hasta validación institucional. | Aceptada. |
| Color de títulos | Se conserva bordó por consistencia con los decks renderizados; la contradicción con la guía escrita queda como decisión global del curso. | Aceptada localmente. |
| Matriz global de cobertura | Su actualización corresponde a `course-architecture` y no modifica la cobertura comprobada de U6. | Aceptada como tarea global. |

## Decisiones pendientes

| ID | Prioridad | Decisión | Evidencia/tensión | Recomendación preliminar | Impacto si queda abierta | Estado |
|---|---|---|---|---|---|---|
| OD-U06-01 | Media | Confirmar el título visible de la unidad. | Programa: “El mecanismo de la percepción auditiva”; LaTeX/PDF y pedido: “El mecanismo periférico…”. | Usar el título con “periférico” y consignar el oficial en metadatos/fuentes, porque delimita U6 frente a U7. | Puede perderse trazabilidad o invadirse el alcance perceptual. | Pendiente de validación docente. |
| OD-U06-02 | Alta | Confirmar cantidad y duración de encuentros. | Ruta central estimada en 66–82 slides; cuatro bloques de carga muy alta. | Planificar dos encuentros largos o tres breves; no comprimir a uno sin mover contenido de forma explícita. | Determina central/complementario, cantidad de actividades y ritmo de recapitulación. | Pendiente de planificación docente. |
| OD-U06-03 | Alta | Resolver el enunciado “frente de onda esférica a cilíndrica”. | Programa lo exige literalmente; libro rechaza una conversión universal y modela un conducto curvo, variable y finito. | Explicar modelos esférico/cilíndrico como idealizaciones y enseñar transferencia del CAE dependiente de frecuencia/posición. Conservar el enunciado del programa como pregunta crítica. | Riesgo de enseñar una geometría falsa o de parecer que se omitió un tema obligatorio. | Pendiente de validación docente. |
| OD-U06-04 | Alta | Incorporar el túnel de Corti. | Tema obligatorio ausente en capítulo y PDF. | Usar definición anatómica trazable y esquema editable con pilares y membrana basilar. | Omisión programática y anatomía incompleta. | **Resuelta en v02:** U06-057/U06-116; PMC1852340 y PMC4310856. |
| OD-U06-05 | Alta | Explicitar el potencial de reposo. | Programa lo exige; capítulo solo describe potencial endococlear y potencial receptor. | Comparar condición basal y respuesta graduada, declarando compartimentos y referencia. | Confusión electrofisiológica y cobertura parcial del programa. | **Resuelta en v02:** U06-085; Fettiplace 2017. |
| OD-U06-06 | Alta | Elegir nomenclatura de rampas y membrana de Reissner. | Programa: rampa coclear; libro: conducto coclear/rampa media. | Usar “conducto coclear o rampa media”; reservar *scala media* para equivalencia bibliográfica. | Inconsistencia entre fuentes y sobrecarga terminológica. | **Resuelta en v02:** U06-052/U06-107. |
| OD-U06-07 | Alta | Resolver notación de área `A` frente a `S`. | Capítulo usa `A`, `A_TM`, `A_E`; guía transversal prefiere `S`. | Adoptar `S`, `S_TM`, `S_E` y registrar equivalencia con el libro. | Afecta todas las ecuaciones y figuras del oído medio. | **Resuelta en v02:** convención `S`, `S_TM`, `S_E`. |
| OD-U06-08 | Alta | Resolver la colisión de `R_p`. | U4/guía: coeficiente de reflexión de presión; U6: razón de presiones del transformador. | Usar `M_p` para transformación ideal y reservar `R_p` para reflexión. | Puede confundirse reflexión con transformación en unidades consecutivas. | **Resuelta en v02:** `M_p` adoptado. |
| OD-U06-09 | Media | Definir símbolo para razón logarítmica de presión. | Capítulo usa `G_p`; guía usa `G(f)` para ganancia de amplitud de sistema. | Conservar `G_p` como expresión logarítmica de la razón ideal definida en esta unidad. | Inconsistencia entre ejemplo, gráficos y notación transversal. | **Resuelta en v02:** `G_p = 20 log₁₀(M_p)`. |
| OD-U06-10 | Alta | Decidir tratamiento de umbral y latencia del reflejo. | Programa exige tiempos de reacción; libro evita valor universal. | Núcleo y respaldo cualitativos; toda cifra futura debe declarar estímulo, método y población. | Puede enseñarse una cifra universal o quedar el tema demasiado vago. | **Resuelta en v02 para el alcance del curso:** U06-038/U06-115, sin valores universales. |
| OD-U06-11 | Media | Definir profundidad de los cinco mecanismos de conducción ósea. | Concepto multimecanismo es central; el detalle puede saturar. | Una vista central convergente y una actividad; detalle por mecanismo como complemento/respaldo. | O simplificación de “bypass”, o sobrecarga anatómico-mecánica. | Pendiente según tiempo. |
| OD-U06-12 | Alta | Definir profundidad electroquímica de la transducción. | Capítulo incluye *tip links*, K⁺, Ca²⁺, prestina, glutamato y sinapsis de cinta. | Mantener la secuencia causal y función de cada elemento; reservar detalle molecular y valores para complemento. | Puede transformarse en memorización molecular o quedar sin mecanismo. | Pendiente según perfil del grupo. |
| OD-U06-13 | Media | Ubicar la codificación periférica inicial. | No aparece literalmente en el programa, pero prepara U7 y evita identificar mecánica con percepción. | Mantener un bloque breve central de lugar/temporización y tasa/reclutamiento; detalle de sincronización como complemento. | Puede invadir U7 o dejar un salto entre potencial receptor y percepción. | Recomendación preliminar. |
| OD-U06-14 | Alta | Seleccionar fuente y estrategia de anatomía visual. | Siete diagramas propios son funcionales pero esquemáticos; faltan túnel y referencia anatómica detallada. | Combinar diagramas propios editables con una ilustración técnica autorizada; validar orientación, nombres y relaciones espaciales. | Riesgo de anatomía inexacta o visualmente insuficiente. | Pendiente para `asset-curation` y revisión experta. |
| OD-U06-15 | Media | Reconstruir o reutilizar las siete figuras TikZ. | Son correctas para libro, pequeñas para aula y algunas contienen demasiadas relaciones simultáneas. | Reconstruir a tamaño real de slide, por etapas y con objetos editables; conservar fuentes y trazabilidad. | Copiarlas produciría ilegibilidad y baja editabilidad. | Decisión recomendada; pendiente de producción. |
| OD-U06-16 | Media | Decidir uso de animaciones. | Onda viajera, ventanas y transducción se benefician de movimiento; la accesibilidad exige versión estática completa. | Usar revelado por etapas o animación breve solo donde cambie la comprensión; preparar siempre alternativa estática. | Puede dependerse de la animación o multiplicarse trabajo sin beneficio. | Pendiente para storyboard/assets. |
| OD-U06-17 | Media | Confirmar demostraciones y condiciones de seguridad. | Cuarto de onda, palanca y conducción ósea admiten demostración; un diapasón/vibrador no debe usarse como prueba clínica ni a nivel no controlado. | Inventariar equipo, nivel, higiene, duración y alternativa visual antes de incorporar la actividad. | Riesgo de seguridad, interpretación clínica o dependencia de equipo. | Pendiente de recursos docentes. |
| OD-U06-18 | Alta | Seleccionar ejercicios para la ruta central. | El capítulo ofrece 30 grupos de consignas con múltiples subapartados. | Elegir una comprobación por bloque, al menos un cálculo del CAE, uno del oído medio y la pregunta integradora; soluciones completas a respaldo. | El deck puede crecer sin control o quedar sin práctica distribuida. | Pendiente para storyboard. |
| OD-U06-19 | Media | Definir tratamiento de OEA, PEAT e inmitancia. | Son aplicaciones útiles y puente a U8, pero pueden convertirse en protocolo/diagnóstico. | Mantener la pregunta “qué etapa contribuye a la medición y qué no localiza por sí sola”; reservar procedimiento para U8. | Invasión curricular y conclusiones clínicas indebidas. | Recomendación preliminar. |
| OD-U06-20 | Alta | Actualizar referencias U06 en `content_coverage_matrix.csv`. | Varias filas apuntan a numeración anterior del capítulo. | Tarea posterior con `course-architecture`: corregir `book_section` sin alterar estados ni decisiones de cobertura. | Trazabilidad defectuosa en storyboard y revisión. | Pendiente; fuera de los cuatro archivos solicitados. |
| OD-U06-21 | Media | Definir revisión pedagógica y anatómica independiente. | `AGENTS.md` exige revisión independiente para U6; anatomía y electrofisiología aumentan el riesgo de error. | Programar una revisión pedagógica y otra de exactitud anatómico-fisiológica antes del deck final. | Errores pueden sobrevivir aunque la secuencia sea visualmente correcta. | Pendiente de responsable/etapa. |
| OD-U06-22 | Media | Decidir si se usan valores numéricos anatómicos reales. | El libro usa razones y longitudes didácticas, no universales. | En el núcleo, usar datos del modelo explícitamente didácticos; cualquier rango anatómico real debe tener población, método y fuente. | Puede confundirse variabilidad humana con una constante. | Recomendación preliminar. |
| OD-U06-23 | Baja | Elegir términos “reflejo acústico” y “reflejo estapedial”. | Programa usa estapedial; capítulo alterna acústico del estapedio. | Introducir “reflejo acústico (contracción del músculo estapedio)” y mantener una forma principal. | Inconsistencia terminológica menor. | Pendiente de estilo docente. |
| OD-U06-24 | Media | Confirmar la frontera de “oído periférico”. | El capítulo llega a actividad del nervio auditivo y codificación inicial; la vía central queda fuera. | Declarar en apertura qué estructuras y procesos incluye U6 y detenerse antes de núcleos centrales/percepción. | Puede expandirse la unidad sin control o quedar una frontera implícita. | Recomendación lista; falta validar. |

## Decisiones ya adoptadas para esta etapa

| ID | Decisión | Justificación |
|---|---|---|
| DA-U06-01 | No crear storyboard ni PowerPoint. | Solicitud explícita y flujo obligatorio del repositorio. |
| DA-U06-02 | No redactar texto visible ni notas del orador. | Esta etapa termina en brief, inventario, análisis y decisiones. |
| DA-U06-03 | Tratar U6 como carga conceptual muy alta. | Coincidencia entre `AGENTS.md`, mapas curriculares y cantidad de dominios simultáneos. |
| DA-U06-04 | Usar bloques breves y recapitulaciones frecuentes. | Requisito específico para U6 y estrategia de reducción de carga. |
| DA-U06-05 | Organizar la unidad mediante cadena funcional, no lista anatómica. | El capítulo y `course_map.md` priorizan entrada–transformación–salida–límite. |
| DA-U06-06 | No enseñar valores universales de CAE, oído medio o reflejo. | El libro explicita variabilidad, dependencia de frecuencia, estímulo, persona y medición. |
| DA-U06-07 | Presentar conducción ósea como multimecanismo. | Coherencia entre capítulo, glosario y matriz de cobertura. |
| DA-U06-08 | Mantener separadas magnitudes físicas y atributos perceptuales. | U6 prepara U7; frecuencia/pitch y nivel/sonoridad no son equivalencias. |
| DA-U06-09 | Registrar túnel de Corti y potencial de reposo como vacíos, sin completarlos silenciosamente. | Son temas obligatorios y requieren fuentes verificables. |
| DA-U06-10 | No incorporar fuentes externas nuevas en esta etapa. | Las fuentes locales bastan para el análisis; las ampliaciones se resolverán en una etapa de fuentes/assets. |
| DA-U06-11 | No modificar mapas globales ni matriz en esta tarea. | El pedido limita la salida a cuatro archivos de U6; las correcciones quedan registradas. |
| DA-U06-12 | Considerar LaTeX y PDF sustantivamente concordantes. | Se revisó el capítulo completo y se renderizaron las pp. 151–175 sin diferencias de contenido detectadas. |

## Orden recomendado de resolución antes del storyboard

1. confirmar título y frontera de “periférico”;
2. confirmar cantidad y duración de encuentros;
3. acordar la reformulación pedagógica del frente de onda en el CAE;
4. seleccionar y validar fuentes para túnel de Corti y potencial de reposo;
5. fijar nomenclatura anatómica de rampas/membranas;
6. resolver `A/S`, `R_p` y `G_p`;
7. decidir profundidad del reflejo, conducción ósea, electroquímica y codificación periférica;
8. definir estrategia de anatomía visual y reconstrucción de las siete figuras;
9. confirmar demostraciones, seguridad y alternativas visuales;
10. seleccionar ejercicios y aplicaciones por bloque;
11. programar la actualización de referencias U06 en la matriz;
12. programar revisión pedagógica y anatómico-fisiológica independiente.
