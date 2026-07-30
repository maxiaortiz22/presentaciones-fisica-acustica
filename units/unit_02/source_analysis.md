# Unidad 2 — Análisis de fuentes

## Jerarquía aplicada

1. Programa oficial: define el alcance mínimo obligatorio.
2. Libro en LaTeX: fuente estructural y editable.
3. Libro en PDF: verificación de edición, paginación, ecuaciones y figuras.
4. Mapas curriculares y matriz de cobertura.
5. Guías locales de presentación, notación y glosario.
6. Bibliografía técnica citada en el capítulo.
7. Decisiones consolidadas en la Unidad 1 para continuidad.

No se añadieron fuentes externas nuevas ni se inició curación de assets en esta etapa.

## Disponibilidad y limitaciones

| Fuente solicitada | Estado | Observación |
|---|---|---|
| `AGENTS.md` | Disponible | Leído antes de editar. |
| Programa oficial | Disponible | `context/programa/Programa de Física Acústica.pdf`, 6 páginas; U2 en p. 3. |
| `course_map.md` | Disponible | Define U2 como base mecánica y energética de carga alta. |
| `course_dependency_map.md` | Disponible | Explicita prerrequisitos, errores y conexiones. |
| `content_coverage_matrix.csv` | Disponible | Cuatro temas obligatorios y tres ampliaciones registradas. |
| Libro LaTeX | Disponible | Capítulo 2 de 1181 líneas, 14 ecuaciones numeradas y 4 figuras TikZ. |
| Libro PDF | Disponible | Edición 2026, 296 páginas; U2 ocupa pp. 37–60. |
| `presentation_style_guide.md` | Disponible | Guía visual vigente. |
| `notation_guide.md` | No existe | Se consultó `style/notation_guide_draft.md`. |
| `glossary.md` | No existe | Se consultó `style/glossary_draft.md`. |
| Presentación previa de U2 | No localizada | No hay `.pptx` ni otro deck de U2 en el repositorio. |
| Guía de ejercicios independiente | No localizada | Se utilizará el banco del capítulo como fuente interna. |
| Unidad 1 terminada | Disponible | Se revisaron `final_report.md` y `review.md` para continuidad. |

## Alcance obligatorio: programa frente al libro

| Tema del programa | Cobertura LaTeX | Páginas PDF | Estado | Observación |
|---|---|---:|---|---|
| Leyes de Newton | 2.4.1–2.4.4 | 38–40 | Completa | Incluye sistema, fuerza neta, inercia, segunda ley y pares de interacción. |
| Calor | 2.7.1–2.7.2 | 44–45 | Completa | Lo distingue de temperatura y energía interna y lo incorpora a la primera ley. |
| Entropía | 2.7.3 | 45 | Completa en el nivel previsto | Tratamiento cualitativo, unidad e irreversibilidad; evita reducirla a “desorden”. |
| Conservación de la energía | 2.6.1–2.6.3 y 2.7.2 | 43–45 | Completa | Integra formas mecánicas, transferencia, disipación y primera ley. |

No se detectaron temas obligatorios ausentes. El libro desarrolla con más profundidad y mejor secuencia que el listado del programa.

## Diferencias de alcance entre programa y libro

| Ampliación del libro | Ubicación | Valor pedagógico | Clasificación propuesta |
|---|---|---|---|
| Sistema, interacción y fuerza neta | 2.4.1 | Condición para interpretar correctamente las leyes. | Central estructural. |
| Diferencia de presión y fuerza sobre área | 2.4.3 | Conecta U1, tímpano y segunda ley. | Central/importante. |
| Masa, elasticidad y amortiguamiento | 2.5 | Prepara oscilaciones, ondas y sistemas auditivos. | Central estructural. |
| Trabajo y formas de energía mecánica | 2.6.1 | Da contenido físico a la conservación. | Central/importante. |
| Energía interna y primera ley | 2.7.1–2.7.2 | Permite definir calor y conservación sin ambigüedad. | Central estructural. |
| Compresión adiabática y velocidad del sonido | 2.7.4 | Conecta termodinámica con acústica y U9. | Complementario o central breve. |
| Aplicaciones fonoaudiológicas | 2.8 | Da transferencia disciplinar con límites explícitos. | Central seleccionada. |
| Banco amplio de ejercicios | 2.11–2.12 | Permite diagnóstico, práctica y respaldo. | Seleccionable/respaldo. |

La ampliación no contradice al programa. El principal riesgo es que mecánica y termodinámica compitan por tiempo y que el bloque acústico de velocidad del sonido desplace el núcleo obligatorio.

## Correspondencia LaTeX–PDF

### Verificación estructural

| Sección LaTeX | Contenido | PDF |
|---|---|---:|
| 2.1 | Propósito y resultados de aprendizaje | 37–38 |
| 2.2 | Conocimientos previos | 38 |
| 2.3 | Membrana y diferencia de presión | 38 |
| 2.4 | Leyes de Newton | 38–40 |
| 2.5 | Masa, elasticidad y amortiguamiento | 41–43 |
| 2.6 | Trabajo, energía y disipación | 43–44 |
| 2.7 | Temperatura, calor y entropía | 44–47 |
| 2.8 | Relación con Fonoaudiología | 46–48 |
| 2.9 | Errores frecuentes | 48–49 |
| 2.10 | Síntesis | 49 |
| 2.11 | Ejercicios de autoevaluación | 50–54 |
| 2.12 | Soluciones | 54–59 |
| 2.13 | Glosario y conclusión | 59–60 |

El índice del PDF y los encabezados del capítulo coinciden con el LaTeX actual. No se observaron omisiones ni reordenamientos entre ambas versiones.

### Verificación visual

Se renderizaron e inspeccionaron las pp. 37, 40, 41, 47, 48, 50, 54 y 59:

- p. 37 confirma título, propósito y resultados;
- p. 40 confirma la figura 2.1, el ejemplo presión–fuerza y la tercera ley;
- p. 41 confirma la figura 2.2 y el inicio del modelo unidimensional;
- p. 47 confirma el gráfico `c(ϑ)` y las aplicaciones;
- p. 48 confirma el balance de energía de la vía auditiva y el inicio de errores frecuentes;
- p. 50 confirma la organización del banco de autoevaluación;
- p. 54 confirma la pregunta integradora y el comienzo de soluciones;
- p. 59 confirma glosario, unidades y continuidad conceptual.

Las páginas están correctamente compuestas para lectura de libro. Sin embargo, sus párrafos, captions y figuras no deben copiarse como capturas: la escala de aula exige dividir contenido y reconstruir los visuales.

## Ecuaciones del capítulo

El PDF conserva las ecuaciones 2.1–2.14:

1. `F_neta = ma`;
2. `F_pres = Δp·A`;
3. tercera ley vectorial;
4. `F_el = -kx`;
5. `F_amort = -bv`;
6. balance instantáneo masa–resorte–amortiguador;
7. trabajo mecánico;
8. energía cinética;
9. energía potencial elástica;
10. balance didáctico de energía;
11. primera ley de la termodinámica;
12. desigualdad de entropía;
13. velocidad del sonido en gas ideal;
14. aproximación lineal con temperatura ambiental.

No se detectaron inconsistencias dimensionales en el capítulo. Sí existen colisiones con la guía transversal de notación, registradas en `open_decisions.md`.

## Contenido que puede pasar casi directamente a una secuencia de slides

“Casi directamente” significa conservar la idea y la trazabilidad, no copiar el diseño de página ni el párrafo.

| Contenido | Por qué es transferible | Adaptación mínima |
|---|---|---|
| Situación de la membrana | Presenta un problema concreto y preguntas físicas claras. | Convertir en una escena visual con predicción. |
| Definición de sistema y fuerza neta | Es breve, precisa y necesaria. | Añadir frontera y diagrama. |
| Primera ley | Formula condición y corrige retorno al equilibrio. | Separar equilibrio de elasticidad. |
| Segunda ley | Ecuación, símbolos y advertencia están completos. | Una slide de significado y otra de ejemplo. |
| Presión → fuerza | Incluye hipótesis, unidades, figura y cálculo. | Adoptar notación transversal y construir por capas. |
| Tercera ley | Declara cuerpos distintos y alcance. | Usar dos diagramas coordinados. |
| Tres propiedades mecánicas | Masa, elasticidad y amortiguamiento están bien diferenciados. | Una propiedad por etapa. |
| Balance de energía | El esquema entrada–almacenamiento–salida–disipación es pedagógico. | Visual editable y un ejemplo. |
| Temperatura, calor y energía interna | Las definiciones son claras y no equivalentes. | Comparación visual “estado/transferencia”. |
| Primera ley termodinámica | Convención de signos explícita. | Clasificar casos antes de calcular. |
| Errores frecuentes | Están alineados con dificultades de primer año. | Distribuir cerca de cada bloque. |
| Preguntas y ejercicios | Cubren interpretación, cálculo y aplicación. | Seleccionar; mantener soluciones en respaldo. |

## Contenido que necesita mayor explicación

| Contenido | Riesgo si se copia | Recurso necesario |
|---|---|---|
| Sistema e interacción | Puede parecer vocabulario accesorio. | Frontera, entorno y dos elecciones de sistema. |
| Primera ley | Puede interpretarse como “fuerza que conserva el movimiento”. | Casos de equilibrio y contraejemplos. |
| Tercera ley | Se mezcla con fuerzas equilibradas sobre un cuerpo. | Dos diagramas de cuerpo libre y pares rotulados. |
| Signos de fuerzas | El signo puede verse como una regla algebraica arbitraria. | Eje positivo y predicción antes de sustituir. |
| Masa–resorte–amortiguador | Introduce tres propiedades y tres parámetros a la vez. | Construcción progresiva y animación por etapas. |
| Ecuación completa del modelo | Puede sugerir que ya se resolvió el movimiento. | Distinguir balance instantáneo de evolución temporal. |
| Trabajo y energía | Puede confundirse joule con newton o watt. | Diagrama dimensional y casos con/sin desplazamiento. |
| Conservación y disipación | “Pérdida” parece contradecir conservación. | Ruta de energía y frontera de sistema. |
| Calor, trabajo y energía interna | El lenguaje cotidiano introduce errores. | Matriz estado/transferencia y signos. |
| Entropía | “Desorden” no permite razonar ni calcular. | Irreversibilidad, límite reversible y ejemplos acotados. |
| Proceso adiabático | Puede interpretarse como “temperatura constante”. | Comparación breve entre intercambio despreciable y temperatura local variable. |
| `c = √(γRT/M)` | Introduce cuatro parámetros nuevos y raíz sin necesidad central. | Respaldo o explicación conceptual; no derivar. |
| `c ≈ 331 + 0,6ϑ` | Puede parecer universal y causar inferencias perceptuales. | Rango, hipótesis, eje truncado y contraejemplo de pitch. |
| Aplicaciones auditivas | Riesgo de literalidad anatómica o conclusión clínica. | Rótulos de “modelo”, límites y diferimiento a U6. |

## Necesidades de explicación y recursos

### Más ejemplos

- cuerpo en reposo con fuerzas no nulas y suma cero;
- cuerpo con velocidad constante y fuerza neta nula;
- dos masas bajo la misma fuerza neta;
- misma `Δp` sobre dos áreas;
- pares de tercera ley frente a fuerzas equilibradas;
- signos de `F_el` y `F_amort` en cuatro estados de `x` y `v`;
- trabajo nulo cuando no hay desplazamiento;
- balance compatible e incompatible de energía;
- primera ley con calor y trabajo entrantes/salientes;
- cambio de `c` sin cambio de frecuencia de fuente.

### Gráficos y diagramas

- diagrama de cuerpo libre;
- gráfico `a` frente a `F_neta`;
- gráfico `F_el` frente a `x`;
- gráfico `F_amort` frente a `v`;
- ruta de energía;
- gráfico `c` frente a `ϑ`;
- cuadro de conceptos térmicos;
- límites del modelo auditivo.

### Imágenes

Se justifican imágenes técnicas para membrana timpánica, cadena osicular y vibrador óseo. No se justifican fotografías de stock de “energía”, “calor” o “movimiento”.

### Animaciones

Son especialmente útiles para fuerza neta, tercera ley, armado del modelo mecánico, rutas de energía y compresión/rarefacción. La comprensión no debe depender exclusivamente de la animación.

### Demostraciones

Las demostraciones con superficie flexible, carrito y masa–resorte tienen alto valor. Deben incluir predicción, observación y explicación, además de una alternativa visual si el equipamiento no está disponible.

## Coherencia con los mapas curriculares

`course_map.md` y `course_dependency_map.md` coinciden en que U2:

- tiene carga alta;
- depende de magnitudes, unidades y análisis dimensional de U1;
- prepara U3, U4, U6 y U9;
- debe permanecer en modelos unidimensionales y balances;
- necesita diagramas de sistema y rutas de energía;
- tiene como dificultad central la competencia entre mecánica y termodinámica.

El punto de control “dibuja fuerzas y explica un balance de energía” se adopta como evidencia mínima.

## Inconsistencias documentales detectadas

1. `style/notation_guide.md` no existe; solo está `style/notation_guide_draft.md`.
2. `style/glossary.md` no existe; solo está `style/glossary_draft.md`.
3. `content_coverage_matrix.csv` usa referencias de sección desactualizadas para U2: ubica leyes de Newton en 2.2 y ampliaciones en 2.3–2.8, mientras el capítulo actual las desarrolla en 2.4–2.7.
4. La matriz marca trabajo/energía, masa–resorte–amortiguador y velocidad del sonido como `out_of_scope`. El libro y los mapas muestran que los dos primeros son andamiaje estructural y que el tercero es una ampliación preparatoria. La clasificación global debe revisarse en una tarea posterior de arquitectura.
5. El capítulo usa `A` para área, pero la Unidad 1 final adoptó `S`.
6. El capítulo usa `k`, `Q`, `S` y `T` sin calificadores; la guía draft propone resolver colisiones futuras.
7. `course_map.md` usa `E_k` y `E_p`, mientras el capítulo usa `E_c` y `E_el`.
8. No se localizó una guía de ejercicios independiente, aunque el programa menciona una; el capítulo contiene un banco suficiente para esta etapa.

Estas inconsistencias no impiden el brief, pero deben resolverse antes de redactar ecuaciones y títulos visibles.

## Fuentes técnicas citadas por el capítulo

| Clave | Fuente | Uso en U2 |
|---|---|---|
| `cramer1993` | Cramer, *The Variation of the Specific Heat Ratio and the Speed of Sound in Air...*, JASA, 1993 | Dependencia de velocidad con estado del aire. |
| `xiangBlauert2021` | Xiang y Blauert, *Acoustics for Engineers*, 3.ª ed., 2021 | Aproximación adiabática y velocidad del sonido. |
| `ugarteburu2022` | Ugarteburu et al., *Mammalian Middle Ear Mechanics: A Review*, 2022 | Mecánica pasiva del oído medio. |
| `stenfeltGoode2005` | Stenfelt y Goode, *Bone-Conducted Sound: Physiological and Clinical Aspects*, 2005 | Conducción ósea multimecanismo. |
| `fung1981` | Fung, *Biomechanics: Mechanical Properties of Living Tissues*, 1981 | Comportamiento viscoelástico de tejidos. |

Las referencias están registradas en `context/libro_latex/bibliography/references.bib`. En esta etapa se acepta su uso como bibliografía ya incorporada al libro; cualquier asset o dato nuevo requerirá verificación y registro posterior.

## Conclusión del análisis

Programa, LaTeX y PDF son compatibles. El programa fija un núcleo breve y el libro aporta una secuencia pedagógica sólida, ejemplos, visuales y ejercicios. La principal tarea de diseño no será completar vacíos de contenido, sino:

- graduar la profundidad;
- separar mecánica y termodinámica mediante un puente energético;
- reconstruir figuras para aula;
- resolver la notación transversal;
- seleccionar ejercicios sin convertir el deck en una guía completa;
- preservar los límites de los modelos auditivos.

