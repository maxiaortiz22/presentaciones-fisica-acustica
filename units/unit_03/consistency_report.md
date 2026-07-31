# Informe de consistencia — Unidad 03

**Unidad:** Fundamentos de la mecánica ondulatoria  
**Presentación revisada:** `output/unidad_03_mecanica_ondulatoria_v02.pptx`  
**Fecha de revisión:** 2026-07-30  
**Skill aplicada:** `consistency-guard`

## Dictamen

La Unidad 3 conserva la identidad académica del curso y se integra correctamente entre las bases matemático-mecánicas de las Unidades 1 y 2 y la formalización acústica prevista para las Unidades 4 y 5. La profundidad, la cantidad de recapitulaciones y el uso de una variable ondulatoria genérica son diferencias **intencionales** con fundamento pedagógico.

La comparación detectó inconsistencias editoriales y de notación localizadas, pero no una divergencia conceptual o visual que justifique homogeneizar el deck completo. Se actualizaron el glosario, la guía de notación y el registro de decisiones para resolver tres ambigüedades transversales. Quedan abiertas correcciones de producción en el `.pptx` y tres decisiones técnicas globales.

## Fuentes de comparación

- `AGENTS.md`.
- `course_map.md` y `course_dependency_map.md`.
- `course_consistency_report.md`.
- `style/presentation_style_guide.md`.
- `style/slide_master_spec.md`.
- `style/layout_catalog.md`.
- `style/component_catalog.md`.
- `style/glossary.md`.
- `style/notation_guide.md`.
- `style/decision_log.md`.
- `output/fisica_acustica_template_v01.pptx`.
- Unidad 1 final: `units/unit_01/output/unidad_01_nociones_basicas_final.pptx`, su render y su informe de revisión.
- Unidad 2 final: `units/unit_02/output/unidad_02_mecanica_termodinamica_final.pptx`, su render y sus informes de revisión y consistencia.
- Unidad 3 v02: presentación, render completo de 96 slides, storyboard, texto visible, notas e informe de revisión.

## Criterio de clasificación

| Clasificación | Criterio |
|---|---|
| **intencional** | Diferencia deliberada, con una función curricular o pedagógica identificable. Debe conservarse. |
| **aceptable** | Variante compatible con el sistema; no introduce ambigüedad ni deteriora la experiencia. |
| **inconsistente** | Contradice una convención aprobada o introduce ruido, ambigüedad o pérdida de legibilidad. Debe corregirse. |
| **requiere decisión** | La evidencia no permite imponer una única solución sin una decisión transversal del proyecto o de la cátedra. |

## Evidencia estructural de los archivos

| Propiedad | Template | Unidad 1 | Unidad 2 | Unidad 3 v02 |
|---|---:|---:|---:|---:|
| Relación y tamaño | 16:9; 13,333 × 7,5 in | igual | igual | igual |
| Slides | 27 | 94 | 110 | 96 |
| Masters / layouts disponibles | 2 / 27 | 2 / 27 | 2 / 27 | 2 / 27 |
| Layouts utilizados | 27 | 25 | 25 | 21 |
| Notas presentes | 27 | 94 | 110 | 96 |
| Notas con bloque `[Sources]` | 2 | 94 | 110 | 96 |
| Fuentes declaradas | Calibri, Calibri Light, Cambria Math | iguales | iguales | iguales |
| Recursos gráficos principales | PNG/GIF | PNG/GIF | PNG/SVG | PNG/SVG |
| Tamaño aproximado | 0,57 MB | 0,89 MB | 1,70 MB | 10,11 MB |

La menor cantidad de layouts usados en U3 no implica monotonía: el deck utiliza 21 funciones distintas, entre ellas definición, comparación, ecuación, gráfico, proceso, aplicación clínica, pregunta, error frecuente, ejemplo resuelto, recapitulación y apéndice.

## Matriz de consistencia

| ID | Dimensión | Comparación y evidencia | Clasificación | Acción |
|---|---|---|---|---|
| CG3-001 | Cobertura y mapa del curso | Recupera funciones, trigonometría y radianes de U1; equilibrio, elasticidad, inercia y amortiguamiento de U2; prepara sonido y análisis frecuencial de U4–U5. | **aceptable** | Conservar. |
| CG3-002 | Nivel de profundidad | Mantiene 69 slides centrales y una ruta docente estimada en tres encuentros. La extensión responde a la dificultad de distinguir oscilación, propagación, fase y superposición. | **intencional** | No reducir para igualar el número de slides de U1 o U2. |
| CG3-003 | Contenido avanzado | `ω` y `k_onda` se presentan en el bloque de respaldo y no dominan la ruta central, porque el programa exige la intuición ondulatoria pero no ese formalismo completo. | **intencional** | Mantener como ampliación y puente a U4–U5. |
| CG3-004 | Prerrequisitos | El deck no presupone dominio matemático avanzado: repone lectura de ejes, periodicidad, fase y unidades antes de formalizar. | **aceptable** | Conservar. |
| CG3-005 | Terminología: rapidez y velocidad | U1 distingue rapidez y velocidad; U2 alterna “rapidez/velocidad de propagación”; U3 separa la velocidad local `u` del escalar `c`. La regla global anterior era ambigua. | **inconsistente** | Resuelto en `glossary.md`, `notation_guide.md` y D-054: preferir “rapidez de propagación” al contrastar con velocidades locales; admitir el uso convencional no ambiguo. |
| CG3-006 | Definiciones: perturbación y desfase | U3 usa ambos conceptos como piezas centrales, pero no estaban asentados en el glosario canónico. | **inconsistente** | Resuelto mediante nuevas entradas en `style/glossary.md`. |
| CG3-007 | Secuencia terminológica de `u` y `c` | El glosario indicaba primera aparición en U4, aunque U3 ya introduce cualitativamente ambas magnitudes. | **inconsistente** | Resuelto: primera introducción en U3 y formalización acústica en U4. |
| CG3-008 | Variable ondulatoria `ξ(x,t)` | U3 usa una perturbación genérica para no identificar prematuramente toda onda con desplazamiento o presión. | **intencional** | Regla incorporada a `notation_guide.md` y D-055; desde U4 debe preferirse la magnitud física específica. |
| CG3-009 | Presión transicional `p_ac(t)` y amplitud `A_p` | Aparecen en una cadena de transducción antes de la definición formal de presión acústica de U4. | **aceptable** | Mantener solo como anticipo definido; en U4 migrar a `p(t)`, valor pico y RMS. |
| CG3-010 | Símbolos principales | `A_x`, `A_ξ`, `T`, `f`, `φ₀`, `Δφ`, `λ`, `u`, `c`, `k_s` y `k_onda` siguen la lógica transversal y evitan colisiones. | **aceptable** | Conservar. |
| CG3-011 | Subíndices visibles | En el respaldo todavía aparecen rótulos como `A_R` y `k_onda` con guion bajo visible, en vez de subíndice tipográfico. Repite un pendiente registrado en U2. | **inconsistente** | Corregir en la próxima versión del deck; mantener el guion bajo solo en fuentes editables o código. |
| CG3-012 | Unidades | Las unidades de período, frecuencia, longitud y rapidez son correctas. El uso breve de `m/s` en gráficos convive con `m·s⁻¹` en referencias formales. | **aceptable** | Mantener `m/s` en etiquetas introductorias si mejora la lectura; usar la forma SI canónica en tablas y definiciones. |
| CG3-013 | Separador decimal | Varios gráficos usan punto decimal en ticks (`0.2`, `0.4`), contrario a la convención española ya declarada. | **inconsistente** | Regenerar los gráficos afectados con coma decimal; la regla se explicitó en `notation_guide.md`. |
| CG3-014 | Tratamiento pedagógico de fórmulas | Las fórmulas se introducen después de la intuición, definen símbolos y unidades y suelen continuar con ejemplo e interpretación física. | **aceptable** | Conservar esta gramática. |
| CG3-015 | Formato técnico de ecuaciones | El sistema favorece OMML, pero U1–U3 combinan texto editable y figuras vectoriales; aún no existe un umbral transversal para decidir cuándo una expresión debe ser OMML. | **requiere decisión** | Definir una regla global según complejidad, editabilidad y estabilidad del render. |
| CG3-016 | Estilo de gráficos | Fondo claro, retícula gris tenue, líneas teal/bordó, ejes rotulados y unidades visibles coinciden con la guía y con U2. | **aceptable** | Conservar; corregir solo el separador decimal. |
| CG3-017 | Estilo visual de diagramas | Usa cajas planas, conectores directos, colores semánticos y jerarquía título–contenido. El render final no muestra una ruptura del lenguaje visual. | **aceptable** | Conservar la solución visual. |
| CG3-018 | Tecnología de diagramas | U3 depende de 78 SVG, mientras la regla de proyecto prefiere formas y conectores nativos para diagramas simples. U2 ya dejó esta familia sin resolver. | **requiere decisión** | Definir qué familias deben ser nativas y cuáles pueden permanecer SVG/PNG reproducibles; considerar editabilidad, tiempo y peso. |
| CG3-019 | Estilo de ejemplos | Los ejemplos siguen datos → relación → cálculo → unidad → comprobación física. U3 agrega lectura de `T` y `λ` desde ejes antes de calcular `c`. | **intencional** | Conservar el paso gráfico porque responde al objetivo de lectura ondulatoria. |
| CG3-020 | Recapitulaciones | U3 contiene siete recapitulaciones parciales, más frecuentes que U1, y equivalentes a U2 pese a tener menos slides. | **intencional** | No reducir: segmentan una carga conceptual más abstracta. |
| CG3-021 | Aplicaciones | Parlante, audiometría, oído, voz y cancelación vinculan la física con Fonoaudiología sin reemplazar la explicación central. | **aceptable** | Conservar; el mayor número de aplicaciones responde al primer contacto explícito con ondas. |
| CG3-022 | Notas del orador | Las 96 slides tienen notas y `[Sources]`; U3 sistematiza pregunta, demostración, error, transición y duración con más granularidad que U1. | **intencional** | Adoptar como mejora de producción, sin exigir que todas las unidades copien campos innecesarios. |
| CG3-023 | Pies institucionales | Regla superior, pie UCASAL y zona de seguridad coinciden con template, U1 y U2. | **aceptable** | Conservar. |
| CG3-024 | Captions | En 56 slides se duplica “no está a escala” dentro del mismo pie y se acumulan etiquetas como “Diagrama propio validado”. U1 y U2 son más selectivas. | **inconsistente** | D-056 establece un único caption funcional; eliminar duplicaciones en una futura corrección de U3 y conservar trazabilidad en notas/manifiesto. |
| CG3-025 | Créditos y fuentes | Todos los slides tienen bloque de fuentes; los recursos propios se identifican y no se atribuyen como externos. | **aceptable** | Conservar; evitar trasladar metadatos de producción al área visible. |
| CG3-026 | Texto alternativo | U3 contiene 80 títulos o descripciones alternativas para sus 79 recursos visuales principales, cobertura superior a U1 y comparable con U2. | **aceptable** | Conservar y revisar semánticamente al cambiar cualquier SVG. |
| CG3-027 | Numeración | U3 numera desde la portada, como U2. U1 oculta la numeración inicial; el master admite ambas variantes. | **aceptable** | No homogeneizar retroactivamente; definir la portada numerada como opción de layout. |
| CG3-028 | Layouts | Usa 21 de 27 layouts y concentra los que sirven a ondas. No usa familias irrelevantes para este contenido. | **aceptable** | No introducir layouts solo para igualar U1/U2. |
| CG3-029 | Paleta | Los scripts usan exactamente bordó, magenta, gris, teal y ocre del sistema. La semántica cromática se conserva. | **aceptable** | Conservar. |
| CG3-030 | Tipografía | Calibri Light, Calibri y Cambria Math coinciden con template y unidades previas; la jerarquía principal es estable. | **aceptable** | Conservar. |
| CG3-031 | Tamaño de texto secundario | Elementos secundarios de las slides 13, 25, 87 y 96 están entre 15 y 17,25 pt, por debajo del mínimo general de 20 pt. | **inconsistente** | Reescribir, ampliar o redistribuir en la próxima versión; no resolver con auto-shrink. |
| CG3-032 | Multimedia y enlaces | U3 no incorpora enlaces ni videos aprobados y mantiene alternativas estáticas. Esto difiere de U1/U2, pero evita dependencias no verificadas. | **aceptable** | Mantener hasta disponer de recursos aprobados y registrados. |
| CG3-033 | Vocabulario del manifiesto | Persiste entre unidades una taxonomía variable para “propio”, “derivado”, “validado”, “conceptual” y tipo de recurso. | **requiere decisión** | Aprobar un vocabulario controlado transversal antes de la siguiente auditoría de assets. |
| CG3-034 | Peso y temas internos | El archivo pesa 10,11 MB, más que U1/U2, principalmente por el volumen de SVG. Sigue siendo utilizable, pero evidencia la decisión técnica pendiente sobre diagramas. | **aceptable** | No comprimir a costa de rasterizar; optimizar después de resolver CG3-018. |
| CG3-035 | Cierre y continuidad | La recapitulación final y el puente a sonido y análisis frecuencial siguen la arquitectura del curso y superan el cierre ceremonial. | **intencional** | Conservar. |
| CG3-036 | Naturalidad académica | Los títulos son informativos; las aplicaciones son específicas; las repeticiones de mapas y pares de slides cumplen una función didáctica. No se observan portadas grandilocuentes, iconografía decorativa ni stock conceptual. | **aceptable** | Conservar; la única señal de automatismo relevante es el exceso de captions de producción de CG3-024. |

## Diferencias pedagógicas que deben conservarse

1. **Mayor segmentación conceptual.** U3 separa oscilación, onda, representación temporal, representación espacial, fase, rapidez y superposición antes de integrarlas.
2. **Siete recapitulaciones parciales.** Reducen la carga cognitiva y funcionan como puntos de salida o reinicio entre encuentros.
3. **Variable genérica `ξ(x,t)`.** Evita que el estudiantado confunda la forma sinusoidal con una única magnitud física.
4. **Formalismo avanzado en respaldo.** `ω` y `k_onda` quedan disponibles para profundizar sin volver obligatoria esa carga algebraica en la ruta central.
5. **Lectura gráfica en los ejemplos.** U3 exige identificar magnitudes en ejes antes de operar, una dificultad propia de esta unidad.
6. **Mayor presencia de aplicaciones fonoaudiológicas.** La conexión con voz, audición y transducción da sentido a un contenido abstracto.

## Actualizaciones realizadas en documentos transversales

### `style/glossary.md`

- Se distinguieron velocidad local o vectorial, velocidad de partícula `u` y rapidez de propagación `c`.
- Se incorporaron **perturbación mecánica** y **diferencia de fase o desfase**.
- Se corrigió la primera aparición de velocidad de partícula y rapidez de propagación a U3, con formalización acústica posterior.
- Se ajustó la definición de refracción para referirla a variaciones de rapidez de propagación.

### `style/notation_guide.md`

- Se explicitó la coma decimal también para ticks y etiquetas de gráficos.
- Se incorporó la amplitud resultante `A_R`.
- Se normalizó `c` como rapidez de propagación, admitiendo el uso convencional no ambiguo.
- Se documentó `ξ(x,t)` como perturbación genérica de U3.
- Se acotó el uso transicional de `p_ac(t)` en U3 y la migración a magnitudes acústicas específicas desde U4.

### `style/decision_log.md`

- **D-054:** criterio transversal para “rapidez de propagación” y “velocidad de propagación”.
- **D-055:** uso condicionado de `ξ(x,t)` en U3.
- **D-056:** un único caption funcional por recurso propio; trazabilidad técnica en notas y manifiesto.

## Problemas abiertos

| ID | Clasificación | Problema abierto | Próxima acción |
|---|---|---|---|
| CG3-A01 | **inconsistente** | Guiones bajos visibles en subíndices del bloque de respaldo. | Convertir a subíndices tipográficos en el próximo `.pptx`. |
| CG3-A02 | **inconsistente** | Puntos decimales en algunos ticks de gráficos. | Regenerar las figuras con coma decimal. |
| CG3-A03 | **inconsistente** | Duplicación de captions y del aviso “no está a escala” en 56 slides. | Aplicar D-056 sin eliminar fuentes ni advertencias necesarias. |
| CG3-A04 | **inconsistente** | Texto secundario menor de 20 pt en slides 13, 25, 87 y 96. | Reducir redacción o redistribuir contenido. |
| CG3-A05 | **requiere decisión** | Umbral de uso de OMML frente a texto editable o SVG para ecuaciones. | Aprobar criterio transversal y aplicarlo desde U4. |
| CG3-A06 | **requiere decisión** | Familias de diagramas que deben ser nativas frente a SVG/PNG reproducible. | Resolver junto con editabilidad y peso del archivo. |
| CG3-A07 | **requiere decisión** | Vocabulario controlado para estados y tipos del manifiesto de assets. | Aprobar taxonomía común antes de revisar U4. |

## Conclusión

La Unidad 3 es consistente con la arquitectura, la identidad visual y la progresión pedagógica del curso. Las diferencias de profundidad, recapitulación y formalización son deliberadas y deben conservarse. No corresponde homogeneizarlas con U1 o U2.

La consistencia transversal queda documentada, con cuatro correcciones locales pendientes y tres decisiones globales abiertas. Este informe no modifica la presentación v02 ni sustituye su revisión integral; establece la línea de base para la siguiente versión o para la producción de la Unidad 4.
