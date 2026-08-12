# Revisión del storyboard — Unidad 9

Fecha: 2026-08-12

Estado: **aprobado como arquitectura pedagógica para avanzar a planificación detallada de recursos; una slide cuantitativa normativa permanece bloqueada por fuente y decisión institucional**.

## Dictamen ejecutivo

El storyboard propone **96 slides**: 75 centrales, 9 complementarias, 11 de respaldo y 1 bloqueada. La ruta central se organiza en tres encuentros y avanza desde un modelo fuente–trayecto–receptor hacia distancia/directividad, atmósfera, superficies, recintos, aislamiento, cabinas e integración.

La cantidad no se fijó a priori. El brief estimaba 52–70 slides centrales; el storyboard llega a 75 porque separa ecuación, interpretación, ejemplo, error frecuente y recapitulación en los nudos de mayor interferencia. Comprimirlos volvería a unir ideas que el análisis identificó como errores previsibles. La ruta central demanda unos **234 minutos dialogados**; con las complementarias, unos **270 minutos**, sin contar pausas extensas ni respaldo.

La cobertura del programa es completa en intención. El requisito “ruido máximo permitido para audiometrías” se cubre conceptualmente en U09-072–075 y tiene una ubicación cuantitativa reservada en U09-092. Esa tabla no puede producirse hasta seleccionar norma, edición, adopción, vía, transductor, bandas, menor nivel de prueba y fuente completa.

## Cobertura del programa

| contenido obligatorio | slides principales | cobertura | observación de revisión |
|---|---|---|---|
| Factores que afectan la propagación | U09-007–011, U09-083 | completa | El modelo organizador evita una lista aislada de factores. |
| Distancia a la fuente | U09-013–016, U09-021, U09-085, U09-087 | completa | Regla, hipótesis, ejemplo, error y derivación en respaldo. |
| Fuentes direccionales | U09-017–021, U09-087 | completa | `Q_dir` y `DI` se tratan a igual potencia/distancia y sin doble conteo. |
| Temperatura ambiente | U09-023–025, U09-033 | completa | Se separan estado uniforme, `c`, `λ` y gradiente. |
| Velocidad y dirección del viento | U09-026–027, U09-033 | completa | Se distingue viento uniforme de gradiente vertical. |
| Presión atmosférica | U09-028–029, U09-033 | completa | La ecuación se usa para negar una corrección aislada por presión. |
| Efectos de superficies sobre el ruido | U09-034–046 | completa | Balance energético, mecanismos y rutas. |
| Reflexión | U09-035–039, U09-046 | completa | Se diferencia mecanismo físico de eco y reverberación. |
| Absorción | U09-035–037, U09-050–056 | completa | Se separan absorción material, atmosférica y acondicionamiento. |
| Refracción en sólidos | U09-040–041, U09-089 | completa con ampliación pendiente | El núcleo es cualitativo; Snell/conversión modal requieren fuente académica antes de producción. |
| Refracción en la atmósfera | U09-025, U09-027, U09-033 | completa | Dos gradientes comparados y principio de curvatura. |
| Difracción y longitud de onda | U09-042–045, U09-046 | completa | Se calcula `λ`, no una atenuación de barrera sin geometría. |
| Aislamiento | U09-057–067 | completa | Se diferencia elemento ideal, conjunto y ruta débil. |
| Insonorización | U09-061, U09-068–077 | completa | Se usa como objetivo general, no como magnitud. |
| Cabinas sonoamortiguadas | U09-068–077, U09-095 | completa | Sistema, componentes, rutas y verificación; sin diseño constructivo. |
| Ley de masas | U09-062–065, U09-087 | completa con convención pendiente | Tendencia relativa central; valor absoluto condicionado. |
| Ruido máximo permitido para audiometrías | U09-072–075, U09-092 | conceptual completa; tabla bloqueada | No se inventan cifras ni se usa un valor global en dB(A). |

## Comparación y trazabilidad de fuentes

- El programa oficial fija todos los temas de la tabla anterior.
- El capítulo 9 en LaTeX aporta las ecuaciones 9.1–9.10, seis figuras U9, ejemplos y ejercicios.
- El PDF, pp. 235–259, es sustantivamente concordante con el LaTeX y sirve como verificación visual y de paginación.
- `course_map.md` y `course_dependency_map.md` justifican la función integradora U2/U3/U4/U5/U7/U8 → U9 → U10.
- `content_coverage_matrix.csv` confirma intención de cobertura, aunque sus localizadores U9 están desactualizados; no se modifican en esta tarea.
- `presentation_style_guide.md`, `notation_guide.md` y `glossary.md` gobiernan layouts, símbolos y términos.
- Las ampliaciones sobre Snell, datos de absorción atmosférica y tabla normativa están identificadas como fuente pendiente; no se atribuyen al libro más detalles de los que contiene.

Cada fila del storyboard registra una fuente principal. En producción posterior, cada slide deberá añadir en notas su bloque `[Sources]` con referencia completa y, cuando corresponda, fuente de datos o asset.

## Revisión de progresión y carga cognitiva

| bloque | carga | dificultad dominante | control incorporado |
|---|---|---|---|
| B00 · Apertura | baja–media | Activar varias unidades previas sin recapitularlas completas. | Caso concreto, objetivos, diagnóstico y mapa. |
| B01 · Modelo organizador | media | Atribuir un valor medido solo a la fuente. | Un único esquema, ocho mecanismos solo nombrados y actividad temprana. |
| B02 · Distancia/directividad | alta | Regla −6 dB, doble conteo de `DI`, `L_W`/`L_p`. | Intuición → ecuación → ejemplo → error → aplicación → recapitulación. |
| B03 · Atmósfera | muy alta | Mezclar rapidez, trayectoria, nivel y variables meteorológicas. | Estado uniforme antes de gradiente; temperatura y viento en pares; matriz U09-033. |
| B04 · Superficies/obstáculos | muy alta | Seis mecanismos y coeficientes con símbolos parecidos. | Balance primero; una interacción por slide; misma geometría para comparar rutas; recapitulación. |
| B05 · Recintos/reverberación | alta | Confundir reflexión, percepción, `T_60` y aislamiento. | Línea temporal → gráfico → `A_eq` → Sabine → ejemplo → límites. |
| B06 · Aislamiento/masa | muy alta | Pasar de fracción a dB y de pared ideal a sistema real. | `τ_E` antes de `R`; rutas antes de ley de masas; cambio relativo antes de valor absoluto. |
| B07 · Cabinas/verificación | muy alta | “Caja con espuma”, valor global y falsa certificación. | Elementos y rutas en slides separadas; proceso metrológico; checklist normativo; caso. |
| B08 · Integración | alta integradora | Sumar fórmulas sin decidir evidencia o límites. | Caso en tres capas y actividad estimar–medir–consultar. |
| B09 · Respaldo | variable | Detalles que pueden interrumpir la ruta. | Acceso no lineal y estados condicionados/bloqueados visibles. |

Los bloques B03, B04, B06 y B07 no deben impartirse seguidos sin la recapitulación prevista. Los tres encuentros propuestos son una decisión pedagógica provisional que responde a OD-U09-01; puede ajustarse sin reordenar conceptos si se conservan las pausas y las slides complementarias siguen siendo retirables.

## Componentes pedagógicos requeridos

| componente | verificación |
|---|---|
| Portada | U09-001. |
| Objetivos observables | U09-003. |
| Puente con conocimientos previos | U09-004 y diagnóstico inicial. |
| Mapa de la clase | U09-005. |
| Pregunta guía por bloque | B00–B09 documentadas; visible en divisores U09-006, 012, 022, 034, 047, 057, 068 y 078. |
| Desarrollo gradual | Fenómeno → mecanismo → modelo → condiciones → aplicación → límite. |
| Ejemplos | U09-015, 024, 052, 064, 075 y caso U09-079–082. |
| Aplicaciones | Campo sonoro, medición exterior, salas, cerramientos y cabina audiométrica. |
| Preguntas/actividades | U09-002, 004, 010, 021, 033, 037, 046, 064, 067, 075, 077 y 082. |
| Recapitulaciones | U09-011, 021, 033, 046, 056, 067, 077 y 083. |
| Cierre | U09-084, con puente a U10. |
| Respaldo | U09-085–096. |
| Transiciones | Las 96 filas incluyen transición explícita. |
| Fuente | Las 96 filas incluyen fuente principal o brecha declarada. |

## Repetición pedagógica y redundancia

| idea repetida | reapariciones | cambio de función | dictamen |
|---|---|---|---|
| Fuente–trayecto–receptor | U09-007, 010–011, 079–083, 095 | Organizador → clasificación → caso integrado → solución orientativa. | Repetición pedagógica necesaria; conservar silueta común. |
| Declarar hipótesis | U09-011, 016, 021, 030, 051–054, 063–067, 074 | Rutina general → límite específico de cada modelo. | Repetición acumulativa. |
| `L_W` no es `L_p` | U09-008, 013–020, 079–081 | Definición → aplicación geométrica → caso profesional. | Transferencia, no redundancia. |
| Absorber no es aislar | U09-035–037, 054, 061, 069, 077 | Destino energético → descriptor de sala → objetivo constructivo → cabina. | Repetición preventiva central. |
| Bandas y condiciones | U09-030, 043, 049–053, 073–075, 081, 092 | Dependencia física → lectura de modelo → criterio de prueba. | Repetición profesionalizante. |
| Ruta débil | U09-045, 060, 066–067, 071, 077 | Obstáculo → cerramiento → cabina. | Transferencia entre escalas. |

Son redundantes y se evitan: derivar de nuevo la ley del cuadrado inverso en la ruta central; copiar el checklist completo en cada recapitulación; explicar bandas como si U5 no existiera; repetir la definición de reverberación de U7; resolver varios ejercicios consecutivos de la misma operación; o dibujar tres veces las mismas rutas de cabina sin cambiar la pregunta.

## Revisión visual, de template y precedente

Se inspeccionaron los **27 layouts reales** de `output/fisica_acustica_template_v01.pptx`, incluidos `FA_02B_CONOCIMIENTOS_PREVIOS` y `FA_14B_MINI_EJERCICIO`, y la hoja de contacto completa del deck final de Unidad 8, de 114 slides. La Unidad 8 se tomó como precedente de ritmo, rutas central/complementaria/respaldo y densidad, no como autoridad de contenido. Esos dos layouts existen en el PPTX, aunque todavía no figuran en `style/layout_catalog.md`; el storyboard usa sus nombres reales y registra la discrepancia sin modificar el catálogo.

El storyboard usa 25 de los 27 layouts disponibles. La distribución de clases visuales es:

| visual_class | cantidad | observación |
|---|---:|---|
| diagram | 56 | Organiza mecanismos, procesos, casos y recapitulaciones. |
| mixed | 26 | Combina ecuación/diagrama, cálculo o imagen con anotaciones. |
| chart | 8 | Gráficos con ejes; dos adicionales aparecen dentro de slides `mixed`. |
| external_image | 1 | Inspección técnica opcional de cabina. |
| video_or_gif | 1 | Demostración seca/reverberada opcional con fallback estático. |
| none | 4 | Tablas o texto de respaldo sin asset específico. |
| equation_only | 0 | Las ecuaciones se acompañan con interpretación, condiciones o gráfico; ninguna queda aislada. |

La gran cantidad de diagramas responde a la naturaleza espacial y causal de U9. No autoriza una estética de “cajas por defecto”: patrones polares, curvas, geometrías, interfaces y cortes deben conservar su forma disciplinar. Los recursos estructurales están identificados como candidatos para `diagram-generation` y listados individualmente en `initial_diagram_needs.md`.

Lecciones aplicadas del precedente U8:

1. no dejar placeholders visuales o tarjetas genéricas donde se prometió una relación física;
2. dibujar conectores detrás de nodos y reservar corredores antes de redactar;
3. dividir diagramas densos —especialmente cabina— en lugar de reducir tipografía;
4. conservar alternativas estáticas para multimedia;
5. mantener respaldo fuera del recorrido lineal;
6. revisar a tamaño completo, no solo mediante hoja de contacto.

## Revisión de notación y fórmulas

| tema | decisión del storyboard | pendiente |
|---|---|---|
| Directividad | Usar `Q_dir` y explicar equivalencia con `Q` del libro. | Validar consistencia con U4 final. |
| Viento | Usar `v_viento` en lugar de `u`. | Confirmar preferencia institucional. |
| Balance energético | Usar `R_E + α + τ_E = 1`. | Verificar en redacción que no se mezcle con `R_p`, `R_I` o `R`. |
| Reverberación | Usar `A_eq` y `T_60`. | Mantener unidades y dependencia por bandas. |
| Reducción sonora | Usar índice `R`; explicar `TL` solo como equivalencia contextual. | Elegir término visible definitivo. |
| Masa superficial | Proponer `m_s` en `kg·m⁻²`. | Validación de consistencia global. |
| Ley de masas | Enseñar tendencia relativa en el núcleo. | Convención y término constante antes de valor absoluto. |

## Hallazgos y acciones abiertas

| id | severidad | hallazgo | acción requerida | estado |
|---|---|---|---|---|
| SR-U09-01 | crítica | No existe en el repositorio una tabla normativa completa y aplicable de ruido máximo para audiometría. | Resolver OD-U09-22–25 y obtener fuente autorizada antes de producir U09-092/U09-CH-011. | abierto; slide bloqueada |
| SR-U09-02 | mayor | Refracción en sólidos es obligatoria, pero el libro la trata de forma mínima. | Mantener U09-040 cualitativa; seleccionar fuente académica antes de completar U09-041/089. | mitigado en secuencia; fuente abierta |
| SR-U09-03 | mayor | La forma absoluta de la ley de masas depende de convención y campo. | Validar símbolo, constante y alcance; conservar solo `ΔR≈6 dB` como cálculo central seguro. | mitigado; decisión abierta |
| SR-U09-04 | mayor | Colisiones `Q`, `u`, `R`, `A`, `RT_60` pueden producir errores entre unidades. | Validar la tabla U09-086 contra U4/U7 y la guía de notación antes de redactar. | abierto para consistencia |
| SR-U09-05 | mayor | U09-018, 041 y 076 requieren parámetros o assets no presentes. | Producir patrón sintético documentado; curar fuente académica y fotos técnicas o usar alternativas propias. | abierto; no bloquea ruta central |
| SR-U09-06 | mayor | Diagramas atmosféricos, de interfaz, cabina e integración pueden superar mínimos tipográficos. | Prototipar las prioridades de `initial_diagram_needs.md` y dividir cualquier recurso que no sostenga 22–24 pt. | abierto para `diagram-generation` |
| SR-U09-07 | moderada | La ruta central de 75 slides no cabe en una clase única. | Mantener tres encuentros y retirar complementarias según diagnóstico; no comprimir recaps. | resuelto en planificación |
| SR-U09-08 | moderada | Audio o demostraciones pueden confundirse con medición o producir exposición innecesaria. | Usar nivel seguro, material breve, alternativa visual y advertencia de no calibración. | mitigado; curaduría pendiente |
| SR-U09-09 | moderada | `content_coverage_matrix.csv` conserva localizadores U9 antiguos. | Corregir mediante `course-architecture` en una tarea posterior, sin alterar la cobertura actual. | fuera de alcance |
| SR-U09-10 | moderada | `open_decisions.md` registra condiciones previas al storyboard y una decisión histórica de no crearlo. | Conservarlo como registro de etapa; actualizarlo en una tarea de arquitectura/decisiones si se desea reflejar este avance. | documentado; no bloqueante |
| SR-U09-11 | moderada | `FA_02B_CONOCIMIENTOS_PREVIOS` y `FA_14B_MINI_EJERCICIO` existen en el template, pero faltan en `style/layout_catalog.md`. | Mantener sus nombres reales en U9 y actualizar el catálogo en una tarea de sistema visual. | documentado; no bloqueante |

## Aprobación y frontera de la fase siguiente

El storyboard puede avanzar a:

- especificación detallada de diagramas y gráficos no bloqueados;
- curaduría de imágenes técnicas y multimedia opcional;
- validación docente de notación, duración y prioridades;
- resolución documental de la norma audiométrica.

No debe avanzar todavía a redacción completa de slides ni a PowerPoint como parte de esta tarea. Antes de redactar U09-041, U09-063 en forma absoluta, U09-088 o U09-092 deben cerrarse sus fuentes y convenciones. Las demás slides pueden continuar a la fase de recursos manteniendo la arquitectura aquí aprobada.
