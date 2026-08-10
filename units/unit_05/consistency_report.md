# Informe de consistencia — Unidad 05

**Unidad:** Análisis frecuencial de señales acústicas
**Presentación revisada:** `output/unidad_05_analisis_frecuencial_v02.pptx`
**Fecha:** 2026-08-03
**Skill aplicada:** `consistency-guard`

## Dictamen

La Unidad 5 conserva parte de la infraestructura del curso —16:9, dos masters, 27 layouts disponibles, franja superior, logo y pie institucional, familias tipográficas, notas completas y trazabilidad—, pero **no es todavía una referencia visual consistente para las unidades posteriores**.

La divergencia principal está en el sistema visible. Mientras el template y U1–U4 usan bordó, carbón, gris, teal físico y ocre clínico, U5 aplica de forma dominante azul oscuro, azul saturado, verde y violeta (`#172333`, `#2474A6`, `#2D7867`, `#65539A` y fondos asociados). También reemplaza el número automático inferior por el ID de slide en el encabezado, repite tarjetas redondeadas como gramática principal y pierde el texto alternativo de sus 26 imágenes al exportar.

No deben homogeneizarse la mayor cantidad de gráficos, los bloques más cortos, las once recapitulaciones ni la profundidad específica del análisis frecuencial: esas diferencias tienen una razón pedagógica. Sí deben corregirse las desviaciones que cambian la identidad, la notación o la accesibilidad.

## Línea de base

Se compararon:

1. `AGENTS.md`.
2. `course_map.md`, `course_dependency_map.md` y `course_consistency_report.md`.
3. `style/presentation_style_guide.md`, `slide_master_spec.md`, `layout_catalog.md` y `component_catalog.md`.
4. `style/glossary.md`, `notation_guide.md` y `decision_log.md`.
5. `output/fisica_acustica_template_v01.pptx` y su render.
6. Las versiones finales y los renders completos de U1, U2, U3 y U4.
7. Storyboard, texto visible, notas, manifiesto, revisiones previas, PPTX v02 y render de las 150 slides de U5.

## Evidencia estructural

| Artefacto | Slides | Masters | Layouts disponibles | Layouts usados | Notas | Notas con `[Sources]` | Imágenes con alt text | Enlaces | Peso |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Template v01 | 27 | 2 | 27 | 27 | 27 | 2 | 2/2 | 0 | 0,55 MB |
| Unidad 1 final | 94 | 2 | 27 | 25 | 94 | 94 | 16/16 | 2 | 0,85 MB |
| Unidad 2 final | 110 | 2 | 27 | 25 | 110 | 110 | 78/78 | 2 | 1,62 MB |
| Unidad 3 final | 96 | 2 | 27 | 21 | 96 | 96 | 80/80 | 0 | 9,64 MB |
| Unidad 4 v02 | 125 | 2 | 27 | 26 | 125 | 125 | 99/99 | 3 | 2,50 MB |
| Unidad 5 v02 | 150 | 2 | 27 | 26 | 150 | 150 | **0/26** | 3 | 1,89 MB |

La estructura de U5 sigue siendo editable y reutiliza el template real. El problema no es la cantidad de layouts disponibles, sino la aplicación manual de estilos y la repetición de una misma silueta dentro de ellos.

## Criterio de clasificación

| Clasificación | Uso en este informe |
|---|---|
| **intencional** | Diferencia necesaria por el contenido o la progresión pedagógica; debe conservarse. |
| **aceptable** | Variante compatible con el sistema; no necesita corrección. |
| **inconsistente** | Contradice una convención ya aprobada o introduce ambigüedad, pérdida de identidad o problemas de producción. |
| **requiere decisión** | No conviene resolver localmente sin fijar una regla transversal o una prioridad docente. |

## Matriz de diferencias

### Terminología, símbolos, unidades y definiciones

| ID | Dimensión | Línea de base y diferencia observada | Clasificación | Acción recomendada |
|---|---|---|---|---|
| U05-CG-001 | Terminología | La separación `espectro`/`respuesta en frecuencia`, fundamental/armónico/parcial/sobretono y filtro/ponderación coincide con el libro, el mapa y el glosario. | **aceptable** | Conservar; se registró como convención transversal en D-060. |
| U05-CG-002 | Terminología digital | U5 introduce DFT, FFT, bin, ventana, fuga y resolución, términos que no estaban desarrollados en el glosario global. | **intencional** | Se añadieron definiciones sin reducirlas a sinónimos de “espectro”. |
| U05-CG-003 | Vocabulario y profundidad | La unidad usa más vocabulario técnico que U1–U4, pero lo distribuye en bloques y recaps. | **intencional** | Conservar la progresión; no trasladar todo el vocabulario digital a unidades anteriores. |
| U05-CG-004 | Símbolos conceptuales | `x(t)`, `X(f)`, `f_0`, `f_s`, `N`, `T_obs`, `Δf`, `H(f)`, `f_L`, `f_H`, `f_c`, `B` y `S_x(f)` siguen la guía. | **aceptable** | Mantener los símbolos y mejorar solo su composición tipográfica. |
| U05-CG-005 | Serie de Fourier | En U05-023 el render integra de `0` a `T_0`, pero define `t_0` como inicio elegido; el storyboard y `slide_text.md` indican `t_0` a `t_0+T_0`. | **inconsistente** | Corregir la ecuación renderizada y revisar ambos coeficientes. Es una diferencia entre fuente y PPTX, no una variante admisible. |
| U05-CG-006 | Ventana | U05-042 muestra `xw(t)` en el proceso y en la ecuación, aunque la fuente y la guía usan `x_w(t)`. | **inconsistente** | Restaurar el subíndice visible en todas las apariciones. |
| U05-CG-007 | Descriptores de nivel | U05-121 muestra `Leq` y exponentes con `^`; la convención es `L_eq,T` y notación matemática tipográfica. U05-110/111 presentan de modo equivalente `L_A`, `L_Z` y `A(f)`. | **inconsistente** | Usar subíndices reales, incluir `T` cuando corresponda y componer potencias como ecuación. |
| U05-CG-008 | Retardo | U5 usa `τ` para retardo. Es localmente comprensible, pero colisionará con transmisión en U9. | **inconsistente** | Adoptar `τ_d` en U5 y reservar `τ_E` para transmisión, según D-061 y la guía actualizada. |
| U05-CG-009 | Unidades | Hz, s, Pa, µPa y dB se usan con significado físico; los ejemplos visibles emplean coma decimal. | **aceptable** | Conservar. No cambiar unidades por simetría con otros decks. |
| U05-CG-010 | Definiciones | La unidad distingue señal, representación, sistema y medición con más precisión que las unidades previas. | **aceptable** | Reutilizar las distinciones en U6–U10; no simplificarlas hasta perder el objeto físico. |

### Profundidad, fórmulas, ejemplos, recapitulaciones y aplicaciones

| ID | Dimensión | Línea de base y diferencia observada | Clasificación | Acción recomendada |
|---|---|---|---|---|
| U05-CG-011 | Extensión total | U5 tiene 150 slides frente a 94, 110, 96 y 125 en U1–U4. El contenido incluye Fourier, análisis digital, filtros y medición. | **intencional** | No recortar por igualdad numérica. |
| U05-CG-012 | Ruta central | 104 slides están marcadas como centrales, frente a 69–91 en las unidades anteriores. La diferencia afecta el tiempo real de clase. | **requiere decisión** | Definir con criterio docente qué DFT/ventanas/tiempo–frecuencia queda en ruta central y qué pasa a profundización o respaldo. |
| U05-CG-013 | Tratamiento de fórmulas | U5 suele ofrecer ecuación, significado, uso y ejemplo, continuidad válida del contrato de U1–U4. | **aceptable** | Conservar esta mediación pedagógica. |
| U05-CG-014 | Estilo de fórmulas | Las barras violeta y las dos tarjetas azul/verde dominan 15 slides de ecuación y muchas definiciones; no pertenecen al componente matemático del template. | **inconsistente** | Mantener ecuación + interpretación, pero aplicar los tokens y la composición plana del curso. |
| U05-CG-015 | Tecnología matemática | Como U1–U4, U5 mezcla texto Cambria Math y ecuaciones editables sin una política OMML aplicada de forma uniforme. | **requiere decisión** | Resolver el umbral transversal OMML/texto/SVG; no convertir todo por uniformidad. |
| U05-CG-016 | Ejemplos | Ocho ejemplos resueltos conservan datos → relación → resultado → interpretación y añaden condiciones de medición. | **intencional** | Conservar la ampliación, especialmente en bandas y niveles. |
| U05-CG-017 | Cierre de ejemplos | U05-092 y el caso U05-126/127/149 no entregan el mismo nivel de cierre operativo que los ejemplos modelo de U1–U4. | **inconsistente** | Completar datos, procedimiento y solución o reclasificar como preguntas abiertas. |
| U05-CG-018 | Frecuencia de recaps | U5 tiene 11 recapitulaciones, más que U1–U4. `AGENTS.md` exige bloques más cortos en U4–U7. | **intencional** | Conservar la frecuencia; no fusionar recaps para reducir slides. |
| U05-CG-019 | Forma de recaps | U05-040 y U05-116 usan cuatro tarjetas alternadas; el catálogo define una recap plana de tres ideas y una comprobación. | **inconsistente** | Mantener el contenido y la pregunta, pero recuperar jerarquía plana y reducir apariencia de dashboard. |
| U05-CG-020 | Aplicaciones | Nueve aplicaciones conectan voz, audífono, ultrasonido, sonometría y ambiente audiométrico con cautelas explícitas. | **aceptable** | Conservar; no agregar iconos clínicos decorativos. |
| U05-CG-021 | Semántica clínica | Las aplicaciones usan paneles azules/verdes; el sistema reserva ocre para transferencia perceptual/clínica. | **inconsistente** | Recuperar ocre clínico de forma selectiva, sin colorear toda slide de aplicación. |

### Gráficos y diagramas

| ID | Dimensión | Línea de base y diferencia observada | Clasificación | Acción recomendada |
|---|---|---|---|---|
| U05-CG-022 | Gráficos | Los gráficos cuantitativos suelen declarar ejes, unidades, escala y condiciones; la grilla es sobria y las series son distinguibles. | **aceptable** | Conservar el estilo analítico y las advertencias sobre normalización. |
| U05-CG-023 | Progresión visual | La reutilización de una figura para añadir una variable o una decisión cumple una función de revelado progresivo. | **aceptable** | No exigir una imagen nueva cuando cambia realmente la lectura pedagógica. |
| U05-CG-024 | Diagramas | Los procesos señal → sistema → salida y las cadenas de medición son editables, planos y con conectores legibles. | **aceptable** | Conservar la estructura geométrica. |
| U05-CG-025 | Semántica de diagramas | Azul identifica señal/lectura, verde salida/uso y violeta ecuación sin que esos roles existan en la guía; el verde aprobado significa estado correcto y el teal representa física. | **inconsistente** | Mapear nodos a bordó, carbón, gris, teal y ocre; no promover la nueva paleta. |
| U05-CG-026 | Jerarquía de nodos | Títulos y contenido suelen ser legibles, pero la repetición de cajas grandes deja más “interfaz” que diagrama académico. | **inconsistente** | Mantener cajas solo cuando modelan entidades; usar texto, ejes o anotaciones directas cuando no hay estructura relacional. |

### Notas, pies, créditos y producción

| ID | Dimensión | Línea de base y diferencia observada | Clasificación | Acción recomendada |
|---|---|---|---|---|
| U05-CG-027 | Notas | Las 150 slides tienen notas con explicación, pregunta, transición y fuentes serializadas. | **aceptable** | Conservar el nivel de trazabilidad. |
| U05-CG-028 | Versión de notas | `speaker_notes.md` todavía declara `v01`, mientras el deck revisado es v02. | **inconsistente** | Actualizar encabezado y fecha al cerrar la próxima revisión. |
| U05-CG-029 | Pies y captions | El pie UCASAL y el caption interpretativo inferior mantienen la arquitectura del curso. | **aceptable** | Conservar captions que indiquen qué mirar o qué límite recordar. |
| U05-CG-030 | Fuentes visibles | Casi todas las slides muestran códigos internos como `TEX`, `NOT`, `EP` o `GLO`. U1–U4 dejan el detalle técnico en `[Sources]` y muestran crédito legible solo cuando aporta. | **inconsistente** | Llevar códigos internos a notas; si una fuente debe verse, escribir autor/obra u organización de forma comprensible. |
| U05-CG-031 | Créditos | El manifiesto contiene 45 registros con creador, organización, licencia, propósito y crédito; las fuentes externas aprobadas son rastreables. | **aceptable** | Conservar. Los campos vacíos corresponden principalmente a recursos propios/propuestos y están documentados. |
| U05-CG-032 | Numeración | U1–U4 usan número automático inferior; U5 lo reemplaza por `UNIDAD 5 · 058` en el encabezado y pierde la sección pedagógica habitual. | **inconsistente** | Restaurar número automático inferior conforme a D-019/D-046 y usar el encabezado para unidad/sección. El ID puede permanecer en notas o metadata. |
| U05-CG-033 | Masters y layouts | U5 conserva 2 masters, 27 layouts y usa 26, igual que U4. | **aceptable** | No reconstruir el deck ni crear un master nuevo. |
| U05-CG-034 | Variedad nominal | La unidad usa divisores, gráficos, ecuaciones, ejemplos, procesos, aplicaciones, preguntas y apéndices. | **aceptable** | Conservar la variedad funcional. |
| U05-CG-035 | Variedad percibida | Muchas funciones terminan en la misma silueta de dos o cuatro tarjetas redondeadas; el render se percibe más repetitivo que U1–U4. | **inconsistente** | Variar la composición según evidencia: gráfico dominante, ecuación anotada, texto + visual, proceso o comparación plana. |
| U05-CG-036 | Paleta | Los colores dominantes del PPTX son `#172333`, `#2474A6`, `#536276`, `#2D7867`, `#65539A`, `#DDEFF5`, `#E3F2ED` y `#EFECF7`; no son los tokens aprobados. | **inconsistente** | Volver a `#4D1434`, `#903163`, `#3D3D3D`, `#969FA7`, `#2F7E83` y `#9F541A`, con sus fondos claros. |
| U05-CG-037 | Tipografía | El tema conserva Calibri Light, Calibri y Cambria Math, como template y U1–U4. | **aceptable** | No cambiar familias. |
| U05-CG-038 | Jerarquía tipográfica | El azul oscuro de títulos y la escala habitual de 33 pt/18,75 pt se apartan del título de 36 pt y cuerpo de 22–24 pt; el cuerpo queda por debajo del mínimo de 20 pt en muchas cajas. | **inconsistente** | Recuperar escala del template; editar o dividir antes de reducir. |
| U05-CG-039 | Accesibilidad | El PPTX contiene 26 imágenes y ninguna conserva atributo de descripción alternativa, frente a cobertura completa en U1–U4. | **inconsistente** | Reinyectar alt text después de la exportación y verificarlo en el PPTX final. |
| U05-CG-040 | Peso y enlaces | 1,89 MB y tres enlaces externos para 150 slides son valores razonables; no hay evidencia de compresión destructiva. | **aceptable** | No aumentar el peso por uniformidad; priorizar nitidez y accesibilidad. |

## Diferencias que no deben homogeneizarse

1. **Cantidad total de slides.** Fourier, análisis digital, filtros y medición justifican una unidad más extensa; debe ajustarse la ruta, no imponer el número de U1–U3.
2. **Once recapitulaciones y once divisores.** Responden a la carga cognitiva y al requisito específico para U4–U7.
3. **Mayor presencia de gráficos.** El análisis frecuencial necesita comparar representaciones y parámetros, no reemplazarlos por texto para parecerse a otras unidades.
4. **Vocabulario digital propio.** DFT, FFT, bins, ventanas y fuga pertenecen a U5 y preparan U6–U10; no corresponde anticiparlos formalmente en U1–U4.
5. **Aplicaciones de señal y sistema.** La comparación voz/audífono y los casos de sonometría son específicos y deben conservar sus límites, aunque se corrija la apariencia.

## Prioridad de cambios locales

### Imprescindibles para consistencia

1. Restaurar la paleta y jerarquía tipográfica del curso sin cambiar el contenido pedagógico.
2. Corregir U05-023, U05-042, U05-110/111 y U05-121 para que la notación visible coincida con las fuentes y la guía.
3. Restaurar la numeración automática inferior y la función del encabezado.
4. Reinyectar texto alternativo en las 26 imágenes y verificar el `.pptx` exportado.
5. Actualizar `speaker_notes.md` a v02 y retirar del área visible los códigos internos de procedencia.

### Recomendados

1. Reducir la repetición de tarjetas en ecuaciones, recaps, definiciones y comparaciones.
2. Recuperar teal físico y ocre clínico con semántica estable.
3. Completar o reclasificar U05-092 y el caso U05-126/127/149.
4. Revisar todas las cajas con cuerpo de 18,75 pt o menor contra el mínimo de aula.

## Decisiones transversales abiertas

| Decisión | Alcance | Recomendación provisional |
|---|---|---|
| Color habitual de títulos | U1–U10 y guía visual | Resolver carbón de la guía frente a bordó consolidado en U1–U4. El azul `#172333` de U5 no es candidato mientras tanto. |
| Profundidad central de DFT/ventanas | U5 y continuidad con U10 | Mantener intuición y lectura básica en la ruta central; mover formalismo computacional secundario a complementarias/respaldo según tiempo docente. |
| Umbral OMML/texto/SVG | U2–U10 | Usar ecuación nativa o texto matemático editable para relaciones centrales; reservar SVG para composiciones estables cuyo mantenimiento esté garantizado. |

## Documentación global actualizada

- `style/glossary.md`: DFT, FFT, bin de frecuencia, ventana temporal, fuga espectral, resolución frecuencial, banda de frecuencia/octava, ponderaciones A/C/Z, respuesta temporal y calibrador acústico.
- `style/notation_guide.md`: `w(t)`, `x_w(t)`, `k`, `f_k`, `φ_H(f)`, `τ_d`, `G(f)`, `L_B` y `A(f)`.
- `style/decision_log.md`: D-060, D-061 y D-062; además se registraron las decisiones abiertas sobre color de títulos y profundidad central.

No se modificaron el PowerPoint, el storyboard, el texto visible ni las notas durante esta revisión de consistencia.

## Resultado

**Consistencia no aprobada todavía como referencia global.**

La unidad es reconocible como parte del curso por su estructura institucional y su enfoque académico, pero necesita una corrección visual y de producción localizada antes de servir de modelo para U6–U10. Las diferencias pedagógicas justificadas quedan expresamente preservadas.

---

## Segunda pasada de consistencia — versión final

La segunda pasada se realizó sobre el PowerPoint final y su render completo.

| dimensión | diferencia final | clasificación | resolución |
|---|---|---|---|
| Paleta | Carbón, bordó, teal, ocre y grises del curso | aceptable | Corregida globalmente sin cambiar layouts. |
| Tipografía | Calibri, Calibri Light y Cambria Math | aceptable | Coincide con el template y fuentes disponibles. |
| Cuerpo central | 20 pt mínimo en formas de la ruta CENTRAL | aceptable | Corregido; ampliación/respaldo pueden conservar 18,75 pt. |
| Ruta y numeración | `U5 · CENTRAL/AMPLIACIÓN/RESPALDO · nnn` en encabezado | intencional | Sustituye el número inferior para hacer utilizable un banco de 150 slides; no crea precedente global. |
| Notación U05-023 | `t₀`, `T₀` e intervalo declarado | aceptable | Corregida. |
| Notación U05-042 | “señal ventaneada = x(t)·w(t)” | aceptable | Corregida; no usa `xw` como símbolo ambiguo. |
| Ponderación U05-110/111 | Nivel y corrección diferenciados | aceptable | Corregida y limitada al caso tonal. |
| Nivel equivalente | Intuición y ejemplo antes de integral | intencional | Diferencia pedagógica justificada; integral en respaldo. |
| Profundidad Fourier/DFT | Formalismo fuera de la ruta central | intencional | Conserva el material del libro sin sobrecargar primer año. |
| Gráficos y diagramas | Mayor densidad que U1–U4 | intencional | Exigencia propia del análisis frecuencial. |
| Recapitulaciones | Más frecuentes que en U1–U3 | intencional | Requisito específico para U4–U7. |
| Códigos breves de fuente | `TEX`, `PO`, `NOT`, `GLO` en pies | aceptable | Mantienen trazabilidad interna y están definidos en storyboard. |
| Texto alternativo OOXML | 0/27 imágenes | inconsistente | Queda como observación menor por limitación de serialización; requiere decisión si hay exigencia formal de accesibilidad. |

### Decisiones transversales cerradas

- El título visible usa carbón; el bordó queda como acento y etiqueta de ruta.
- La profundidad central de DFT/ventanas se limita a intuición y lectura; el formalismo queda en material no central.
- Las ecuaciones centrales permanecen editables como texto matemático; OMML es una mejora futura, no requisito de cierre.
- La numeración de U5 prioriza ID estable y ruta visible por su función de banco docente.

### Verificación

- 77 slides centrales, 55 de ampliación y 18 de respaldo.
- 150/150 slides con ID y ruta visibles.
- 150 notas con fuentes.
- 2 masters y 27 layouts heredados.
- 3 enlaces oficiales verificados.
- 0 problemas críticos y 0 mayores de consistencia abiertos.

## Resultado actualizado

**Consistencia aprobada con una observación menor de accesibilidad.** La Unidad 5 puede usarse en el curso sin homogeneizar sus diferencias pedagógicas justificadas. El alt text OOXML queda como único punto que requiere decisión si la institución exige validación formal de accesibilidad.
