# Revisión pedagógica del storyboard — Unidad 6

**Estado:** aprobado condicionalmente para la planificación de recursos visuales. No habilita todavía `slide-writing` ni producción de PowerPoint hasta resolver los bloqueos de prioridad alta indicados abajo.

## Alcance de la revisión

Se revisó `storyboard.md` contra el programa oficial, el capítulo LaTeX, su versión PDF, el brief, el inventario de contenidos, el mapa y las dependencias del curso, las guías de estilo/notación/glosario, el template y la experiencia estructural de la Unidad 5. La revisión evalúa cobertura, progresión, carga cognitiva, repetición, factibilidad visual y trazabilidad; no valida aún el copy final ni los assets.

## Resultado cuantitativo

| Indicador | Resultado |
|---|---:|
| Slides propuestas | 117 |
| Centrales | 82 |
| Complementarias | 23 |
| Respaldo | 12 |
| Bloques de recorrido | 10 + respaldo |
| Recapitulaciones parciales/finales | 9 |
| Preguntas o mini ejercicios explícitos | 10 en la ruta + 3 resueltos y 1 banco en respaldo |
| Duración de la ruta central | 394 min aprox. |

## Lista de comprobación

| Criterio | Evaluación | Evidencia / observación |
|---|---|---|
| Cobertura del programa | Cumple con bloqueos declarados | Todos los términos obligatorios tienen ubicación; túnel de Corti y potencial de reposo permanecen bloqueados por fuente. |
| Progresión gradual | Cumple | Entrada acústica → mecánica → hidromecánica → celular → neural; los formalismos aparecen después de la intuición. |
| Prerrequisitos | Cumple | U06-003/004 recuperan ondas, presión, fuerza, energía, frecuencia, nivel y gráficos de U2–U5. |
| Teoría–ejemplo–aplicación | Cumple | Hay ejemplos numéricos en B01–B03, actividades de transferencia y aplicaciones funcionales en B04, B07 y B09. |
| Una idea principal por slide | Cumple en storyboard | Los nodos densos de anatomía y transducción fueron separados; debe conservarse al redactar. |
| Recapitulaciones frecuentes | Cumple | B01–B09 cierran con recap o integración; cambian la tarea cognitiva, no copian definiciones. |
| Frontera U6/U7/U8 | Cumple | U06-071, 094, 097, 099, 100 y 105 distinguen mecanismo periférico, percepción y aplicación clínica. |
| Factibilidad visual | Cumple condicionalmente | Los diagramas complejos están marcados como candidatos para `diagram-generation`; los assets externos necesitan curaduría. |
| Variedad de layouts | Cumple | Se alternan divisor, visual dominante, comparación, proceso, gráfico, ejercicio, aplicación y recap. |
| Trazabilidad | Cumple | Cada fila registra fuente; las ampliaciones pendientes usan `EXT-PEND` y no se presentan como hechos cerrados. |
| Cierre | Cumple | U06-103–105 resuelven un caso, recapitulan y abren U7/U8. |

## Cobertura del programa

| Tema obligatorio | Slides principales | Estado |
|---|---|---|
| Efecto del pabellón auricular | U06-009–010 | Cubierto; requiere asset anatómico/técnico. |
| Onda en el conducto auditivo externo | U06-011–017 | Cubierto; incluye idealización de cuarto de onda y tensión esférica/cilíndrica. |
| Presión y fuerza sobre el tímpano | U06-019–027 | Cubierto con magnitudes, ecuación y límites. |
| Transmisión por oído medio | U06-029–039 | Cubierto con adaptación, áreas, palanca, energía y reflejo. |
| Conducción ósea | U06-041–048 | Cubierto en ruta central; cinco mecanismos detallados en respaldo. |
| Anatomía coclear, rampas, fluidos y membranas | U06-050–060 | Cubierto; terminología a validar. |
| Órgano y túnel de Corti | U06-056–057, 073, 116 | Órgano cubierto; túnel bloqueado hasta fuente anatómica. |
| Onda viajera y tonotopía | U06-062–071 | Cubierto con gráficos de frecuencia y nivel. |
| CCI, CCE y proceso activo | U06-073–081 | Cubierto, con aplicación a OEA. |
| Potencial endococlear | U06-083–084 | Cubierto sin imponer cifra universal. |
| Potencial de reposo | U06-085 | Ubicado, pero bloqueado hasta fuente fisiológica. |
| Potencial receptor y de acción | U06-086–093 | Cubierto y contrastado por ubicación/función. |
| *Tip links*, transducción y sinapsis | U06-087–093 | Cubierto; detalle electroquímico queda en respaldo. |
| Codificación de frecuencia y nivel | U06-095–103 | Cubierto; sincronización temporal requiere fuente adicional. |

## Auditoría de progresión y carga cognitiva

| Bloques | Carga | Control previsto |
|---|---|---|
| B00–B02 | Media | Diagnóstico, magnitudes una por vez, ejemplo antes de generalización. |
| B03–B04 | Media–alta | Separar adaptación aérea de conducción ósea; explicitar supuestos y energía. |
| B05 | Alta | Separar vista longitudinal y transversal; máximo de rótulos por capa; recap espacial. |
| B06 | Alta | Leer ejes antes de interpretar; mantener frecuencia y nivel como variables distintas. |
| B07 | Alta | Micromecánica antes de transducción; comparación CCI/CCE con funciones observables. |
| B08 | Muy alta | Vocabulario eléctrico previo, mecanismo en dos tramos y actividad de ordenamiento. |
| B09 | Muy alta | Recuperación acumulativa, fronteras físico/perceptual y caso integrado. |

No se recomienda fusionar B05–B09 ni reducir su cantidad de slides mediante pantallas más densas. La reducción legítima consiste en omitir complementarias, no en comprimir conceptos centrales.

## Auditoría visual

- Todo proceso con cajas, flechas, conectores o ecuaciones anotadas está marcado como **DG candidate**.
- Los diagramas maestros se diseñarán a tamaño final, con máximo de 4–5 nodos visibles por estado y revelado progresivo cuando la cadena completa exceda ese límite.
- Los gráficos cuantitativos/conceptuales tienen IDs `U06-CH-*` y requieren ejes, unidades o declaración explícita de normalización.
- Las imágenes externas y recursos multimedia tienen IDs `U06-IMG-*` y `U06-MEDIA-*`; ninguno está aprobado todavía.
- Los layouts se seleccionaron desde el template. Si un visual no cabe con texto principal ≥22 pt o ecuación central ≥28 pt, se divide la slide.
- Las recapitulaciones reutilizan un diagrama por **capas acumulativas**; no deben duplicar una imagen estática sin nueva tarea.

## Repetición pedagógica frente a redundancia

| Repetición útil | Función nueva |
|---|---|
| Cadena periférica en apertura, recaps y cierre | Pasa de orientación incompleta a explicación causal y luego a límite inferencial. |
| Física frente a percepción | Pasa de clasificación diagnóstica a lectura de tonotopía/códigos y puente a U7. |
| Conservación de energía | Pasa de advertencia conceptual a control de ecuación y resultado. |
| “Una prueba observa un tramo” | Pasa del caso OEA a matriz comparativa y caso integrado. |
| CCI/CCE | Pasa de comparación anatómico-funcional a consecuencias en OEA y codificación. |

Es redundante: repetir una definición completa en cada recap; usar la misma figura anatómica sin una capa nueva; repetir la tabla CCI/CCE sin cambiar la pregunta; volver a mostrar toda la cadena en cada divisor; o incluir en centrales todos los detalles de respaldo.

## Hallazgos y acciones

| Severidad | Hallazgo | Acción requerida | Estado |
|---|---|---|---|
| Alta | El programa exige túnel de Corti, ausente del capítulo local. | Seleccionar fuente anatómica autorizada y validar U06-057/073/116. | Abierto; bloquea esas slides. |
| Alta | El potencial de reposo solo aparece de forma indirecta. | Incorporar fuente fisiológica que defina ubicación, referencia y relación con potencial receptor. | Abierto; bloquea U06-085. |
| Alta | Colisión de `A/S` para área y `R_p` con reflexión de U4. | Resolver OD-U06-07/08 y actualizar la guía de notación antes de escribir ecuaciones. | Abierto. |
| Alta | La formulación programa “esférica → cilíndrica” puede interpretarse como transformación exacta. | Validar formulación docente y presentar como idealización/transferencia del CAE. | Abierto; afecta U06-013. |
| Alta | Assets anatómicos y animaciones todavía no están curados. | Buscar fuentes institucionales/licencias y registrar alternativas estáticas. | Abierto. |
| Media | Título oficial y título de capítulo difieren en “periférico”. | Confirmar título de portada y mantener ambos rastreados. | Abierto. |
| Media | Variantes conducto/meato y rampa/escala. | Cerrar terminología en glosario antes de slide-writing. | Abierto. |
| Media | Cifras de reflejo y límites temporales de sincronización no están sustentados localmente. | Mantener en respaldo/bloqueo hasta fuente. | Controlado. |
| Media | El volumen central exige varias clases. | Diseñar cortes de clase al final de B03, B06 y B08. | Recomendado. |
| Media | U6 requiere revisión pedagógica independiente según AGENTS.md. | Ejecutar una segunda revisión después del primer draft de storyboard visual. | Pendiente. |

## Decisión de pase

El storyboard puede avanzar a **curaduría de assets, diseño de diagramas y especificación de gráficos**. No debe avanzar todavía a redacción completa de slides ni PowerPoint. Antes de `slide-writing` deben cerrarse como mínimo: fuente del túnel de Corti, fuente del potencial de reposo, notación de área/cociente de presiones y tratamiento de la idealización del CAE.
