# Unidad 2 — Revisión del storyboard

## Dictamen

**Aprobado para pasar a planificación de recursos visuales y multimedia.**

El storyboard cubre el alcance obligatorio del programa, mantiene una progresión gradual y separa una ruta central de materiales complementarios y de respaldo. No redacta todavía el contenido completo de las slides ni inicia la producción del PowerPoint.

No se detectaron omisiones críticas del programa ni contradicciones conceptuales con el capítulo. Persisten decisiones de notación y logística que deben resolverse antes de `slide-writing`, pero no invalidan la arquitectura pedagógica.

## Evidencia revisada

- `AGENTS.md`.
- Programa oficial, Unidad 2, p. 3.
- `context/libro_latex/chapters/02-mecanica-clasica-termodinamica.tex`.
- Libro del curso en PDF, pp. 37–60.
- `course_map.md`.
- `course_dependency_map.md`.
- `content_coverage_matrix.csv`.
- `units/unit_02/brief.md`.
- `units/unit_02/content_inventory.md`.
- `units/unit_02/source_analysis.md`.
- `units/unit_02/open_decisions.md`.
- `style/presentation_style_guide.md`.
- `style/notation_guide_draft.md` y `style/glossary_draft.md`, porque las versiones definitivas no existen.
- `style/layout_catalog.md`, `style/slide_master_spec.md` y `style/component_catalog.md`.
- `output/fisica_acustica_template_v01.pptx`.
- Unidad 1 final y su render, usados como referencia de continuidad visual y ritmo, no como fuente de contenido.

## Auditoría estructural

| control | resultado | estado |
|---|---|---|
| IDs | U02-001 a U02-110, consecutivos y sin duplicados | conforme |
| Columnas obligatorias | 15 campos en las 110 filas | conforme |
| Campos vacíos | no hay rutas, fuentes, transiciones, layouts ni estados vacíos | conforme |
| Estados | 72 `central`, 18 `complementary`, 20 `backup` | conforme |
| Visual classes | solo se usan `chart`, `diagram`, `mixed`, `external_image`, `video_or_gif`, `equation_only` y `none` | conforme |
| Layouts | todos pertenecen a los layouts reales del template | conforme |
| Diagramas candidatos | 72 slides marcadas explícitamente para `diagram-generation` | conforme |
| Gráficos candidatos | necesidades cuantitativas registradas aparte | conforme |
| Redacción completa | no se produjo copy final ni notas completas | conforme |
| PowerPoint | no se creó ni modificó un `.pptx` | conforme |

## Cobertura del programa

| alcance obligatorio | desarrollo central | refuerzo o respaldo | evaluación |
|---|---|---|---|
| Leyes de Newton | U02-007–024 | U02-091–099 | Cubiertas las tres leyes, con sistema, fuerza neta, inercia, aceleración y pares de interacción. |
| Calor | U02-058–067 | U02-104 | Cubierto como transferencia por diferencia de temperatura y diferenciado de temperatura y energía interna. |
| Entropía | U02-068–075 | U02-105 | Cubierta como magnitud de estado, unidad e indicador de irreversibilidad; sin formalismo fuera de alcance. |
| Conservación de la energía | U02-047–057 y U02-064–067 | U02-098–108 | Cubierta mediante formas, frontera, balance, primera ley, disipación y aplicaciones pasivas. |

El trabajo, las formas de energía, el modelo masa–resorte–amortiguador y la velocidad del sonido con temperatura aparecen como ampliaciones estructurales trazables al capítulo. La ecuación general del gas ideal queda en respaldo, coherente con el alcance declarado.

## Mapeo de objetivos

| objetivo del brief | evidencia principal en el storyboard | comprobación prevista |
|---|---|---|
| Identificar sistema y representar fuerzas | U02-008–013 | pregunta U02-012, recap U02-014 y respaldo U02-091 |
| Aplicar las leyes de Newton | U02-013–024 | ejemplos U02-019, preguntas U02-020/U02-023 |
| Relacionar presión, área y fuerza | U02-025–032 | ejemplo U02-030 y recap U02-032 |
| Explicar masa, elasticidad y amortiguamiento | U02-033–046 | predicción U02-043, ejemplo U02-044 y recap U02-046 |
| Calcular e interpretar trabajo y energía | U02-047–057 | ejercicio U02-052, ejemplo U02-056 y recap U02-057 |
| Diferenciar temperatura, calor, `U` y entropía | U02-058–075 | clasificación U02-059, signos U02-065 y recap U02-075 |
| Aplicar modelos a situaciones fonoaudiológicas con límites | U02-083–088 | aplicaciones U02-085–087 y caso U02-088 |
| Explicar el efecto de temperatura sobre `c` sin inferir pitch | U02-076–082 | gráfico U02-080, ejemplo U02-081 y error U02-082 |

Los ocho objetivos se conservan. La slide de objetivos agrupa su formulación para legibilidad, pero las notas deberán expresar los resultados observables completos.

## Revisión de progresión y carga cognitiva

| bloque | carga estimada | decisión de secuencia | recap o alivio |
|---|---|---|---|
| B00 · Apertura | media | fenómeno concreto, diagnóstico, prerrequisitos, objetivos y mapa | U02-006 orienta sin formalizar |
| B01 · Sistema e inercia | media–alta | frontera antes de fuerzas; fuerza neta antes de primera ley | U02-014 |
| B02 · Segunda y tercera leyes | alta | segunda y tercera leyes separadas; ejemplos con signos y cuerpos distintos | U02-023 y divisor posterior |
| B03 · Presión y fuerza | media–alta | presiones de cada lado antes de `Δp`; unidades antes del ejemplo | U02-032 |
| B04 · Respuesta mecánica | muy alta | masa, elasticidad y amortiguamiento se introducen por capas | U02-046; cuatro complementarias permiten regular carga |
| B05 · Trabajo y energía | alta | una forma por vez antes del balance | U02-057; pausa de 15 min |
| B06 · Calor y primera ley | alta | clasificación estado/transferencia antes de signos | U02-067 |
| B07 · Entropía | muy alta | fenómeno irreversible antes de definición y desigualdad | U02-075 |
| B08 · Aire y temperatura | alta | hipótesis y tendencia antes del gráfico y la inferencia perceptual | U02-082 funciona como corrección-síntesis |
| B09 · Aplicación e integración | alta | selección de modelo antes del cálculo integrador | U02-089 y cierre U02-090 |

Las recapitulaciones aparecen después de cada tramo de carga alta y no acumulan símbolos nuevos. El storyboard evita presentar simultáneamente las tres leyes, los tres componentes mecánicos o las cuatro magnitudes térmicas sin preparación.

## Preguntas, ejemplos, aplicaciones y cierre

- Portada, objetivos, puente y mapa: U02-001–006.
- Preguntas o ejercicios formativos: U02-002, 003, 012, 019–020, 023, 026, 043, 052, 059, 065–066, 074–075, 081–082 y 088.
- Ejemplos numéricos centrales o seleccionables: U02-019, 030, 044, 049, 056, 066 y 081.
- Aplicaciones fonoaudiológicas: U02-031, 084–087.
- Recapitulaciones: U02-014, 023, 032, 046, 057, 067, 075 y 089.
- Cierre y puente a U3: U02-090.
- Soluciones y profundización: U02-091–110.

La evidencia de dependencia curricular —“dibuja fuerzas y explica un balance de energía”— se trabaja de manera explícita y reaparece en el caso integrador.

## Repetición pedagógica frente a redundancia

La repetición está justificada cuando cambia la función de la idea:

- la frontera pasa de delimitar fuerzas a delimitar transferencias;
- la fuerza neta pasa de suma cualitativa a cálculo de aceleración y luego a término de un modelo;
- la masa pasa de inercia en Newton a propiedad del modelo mecánico;
- la conservación pasa de balance a compatibilidad con irreversibilidad y luego a sistema pasivo auditivo;
- la distinción físico/perceptual se recupera para corregir la inferencia `c` → pitch.

No se detectaron slides consecutivas con el mismo propósito, mensaje y evidencia. Durante `slide-writing` deberá evitarse copiar literalmente definiciones en las recapitulaciones: estas deben pedir una explicación, una decisión o una transferencia.

## Revisión visual y de layouts

### Distribución visual

| visual_class | cantidad |
|---|---:|
| chart | 2 |
| diagram | 38 |
| mixed | 19 |
| external_image | 1 |
| video_or_gif | 3 |
| equation_only | 18 |
| none | 29 |

La elevada cantidad de diagramas y ecuaciones anotadas responde a la naturaleza causal del contenido, pero constituye el principal riesgo de producción. `initial_diagram_needs.md` los agrupa en 15 familias para evitar 72 diseños inconexos.

### Adecuación al template

El storyboard usa 24 de los 27 layouts reales. La variedad es funcional:

- divisores para cambios de pregunta;
- layouts de definición y ecuación para formalismo;
- proceso y comparación para relaciones;
- ejemplo resuelto y mini ejercicio para práctica;
- recap parcial/final para consolidación;
- aplicación clínica para transferencia responsable;
- apéndice para soluciones y referencias.

No se utilizan layouts inventados. La Unidad 1 se tomó como referencia para densidad, jerarquía y secuencia, pero no se replicaron slides concretas.

### Clasificación explícita de recursos

- Gráficos cuantitativos: U02-018, 038, 040, 080–081 y 103, inventariados en `initial_chart_needs.md`.
- Diagramas conceptuales y ecuaciones anotadas: candidatos identificados en el storyboard y agrupados en `initial_diagram_needs.md`.
- Imágenes externas: U02-085 y apoyo posible en U02-086–087, inventariadas en `initial_asset_needs.md`.
- Multimedia: U02-034, 069 y 077; además, puede realizarse una demostración breve antes o durante U02-002. Cada recurso tiene alternativa estática.

## Trazabilidad de fuentes

Cada fila contiene una fuente. Las ideas obligatorias citan el programa; el desarrollo conceptual y los ejemplos remiten a sección LaTeX y páginas PDF; las decisiones de secuencia remiten al brief y a los mapas del curso; las aplicaciones ampliadas usan referencias ya citadas en el capítulo.

Las ampliaciones didácticas no se presentan como citas del libro. Los valores numéricos existentes se conservan con sus hipótesis, y cualquier parámetro nuevo para gráficos se rotulará como dato didáctico.

## Registro de hallazgos

| id | hallazgo | severidad | acción | estado |
|---|---|---|---|---|
| U02-SR-001 | La duración disponible no está confirmada; la ruta central ocupa 225 min más pausa. | media | Mantener la ruta de 72 slides y dividir en dos encuentros si se incorporan complementarias. | abierto antes de calendarizar |
| U02-SR-002 | `notation_guide.md` y `glossary.md` definitivos no existen. | media | Usar provisionalmente los borradores y resolver `S/A`, `k_s/k`, `S_ent`, temperatura y energías antes de `slide-writing`. | abierto |
| U02-SR-003 | Setenta y dos slides requieren diagramas o ecuaciones anotadas. | media | Producir por familias, validar primero las versiones centrales y derivar respaldos después. | mitigado en el inventario |
| U02-SR-004 | U02-043 podría necesitar más de una slide para mostrar cuatro estados de signo a 22 pt. | baja | Probar geometría real; dividir sin penalizar el conteo si no entra. | pendiente de prototipo |
| U02-SR-005 | U02-096, U02-098 y U02-110 pueden exceder la densidad mínima en respaldo. | baja | Dividir durante producción si la verificación renderizada lo exige. | pendiente |
| U02-SR-006 | Las imágenes técnicas aún no tienen URL ni licencia. | esperada en esta fase | Curar y registrar antes de usarlas. | pendiente de `asset-curation` |
| U02-SR-007 | Los valores didácticos de U02-CH-001 a U02-CH-003 todavía no están fijados. | baja | Elegir parámetros simples, verificar unidades y rotularlos como modelos. | pendiente de `chart-generation` |

No hay hallazgos críticos ni mayores.

## Puertas para la siguiente fase

Antes de redactar slides:

1. confirmar si la unidad se dicta en uno o dos encuentros;
2. cerrar las convenciones de notación transversal;
3. decidir si U02-CH-005 será gráfico o tabla;
4. confirmar disponibilidad de las demostraciones propias;
5. prototipar U02-DG-006 y U02-DG-008, las familias de mayor carga;
6. curar imágenes externas con licencia y trazabilidad.

El storyboard está listo como especificación pedagógica. La próxima fase autorizable es producción/curación de recursos; no corresponde todavía generar texto final ni PowerPoint.
