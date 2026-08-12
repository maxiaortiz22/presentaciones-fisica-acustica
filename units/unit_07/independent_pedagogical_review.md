# Revisión pedagógica independiente — Unidad 7

**Unidad:** 7 · Características subjetivas de la percepción auditiva y psicoacústica  
**Fecha:** 2026-08-11  
**Deck revisado:** `output/unidad_07_psicoacustica_v02.pptx`  
**Alcance:** segunda lectura docente, independiente de las decisiones de producción previas  
**Condición de esta pasada:** no se modificó el PowerPoint.

## Dictamen independiente

La unidad presenta una base científicamente cuidadosa, una cobertura amplia del programa y una intención pedagógica explícita. Distingue con rigor magnitudes físicas, atributos perceptuales, tareas y condiciones; evita equivalencias universales indebidas; y conserva límites de interpretación en fones/sones, enmascaramiento, SNR, precedencia e ITD/ILD.

Sin embargo, **no la considero todavía lista para ser recibida y dictada por un segundo docente sin una intervención pedagógica adicional**. No encontré un nuevo error físico crítico en las ecuaciones centrales, pero sí cinco problemas de impacto mayor:

1. la secuencia de curvas isofónicas culmina en una actividad que pide leer una curva que no está visible;
2. las ampliaciones están clasificadas en el storyboard, pero no se distinguen como tales dentro del deck;
3. las experiencias auditivas que sostienen la intuición psicoacústica no existen aún como archivos utilizables;
4. varios cálculos aparecen resueltos, pero los pasos y la interpretación quedan demasiado delegados a las notas;
5. algunos diagramas son limpios en producción, aunque no representan con claridad la causalidad o la geometría que deberían enseñar.

El deck puede transformarse en una unidad sólida sin rehacerlo completo. La prioridad debe ser **hacer ejecutable la ruta**, no agregar más contenido.

## Fuentes leídas y evidencia examinada

- programa oficial: `context/programa/Programa de Física Acústica.pdf`;
- capítulo del libro: `context/libro_latex/chapters/07-psicoacustica.tex`;
- brief: `units/unit_07/brief.md`;
- storyboard completo: `units/unit_07/storyboard.md`;
- deck v02: `units/unit_07/output/unidad_07_psicoacustica_v02.pptx`;
- render completo: 134 slides de `units/unit_07/output/rendered_v02/` y sus montajes;
- notas: `units/unit_07/speaker_notes.md`;
- revisión anterior: `units/unit_07/review.md`;
- manifiesto de recursos: `units/unit_07/asset_manifest.csv`.

La revisión anterior se tomó como evidencia de producción, pero no como garantía pedagógica. En particular, se reabren aquí cuestiones que aquella revisión había considerado cerradas o aceptables.

## Línea de base que sí funciona

- El programa está ampliamente cubierto: umbral, sensibilidad, campo–tímpano, isofónicas, atributos, fones/sones, enmascaramiento, voz e inteligibilidad, reverberación, ALCons, precedencia/Haas, localización, audición binaural, ITD, ILD y fuentes concurrentes.
- El deck corrige adecuadamente la errata del programa “Hass” y usa **Haas**, diferenciándolo del efecto de precedencia según el capítulo.
- Las fórmulas principales son dimensionalmente coherentes y suelen explicitar unidades y límites.
- La secuencia general físico → tarea → respuesta → condiciones es conceptualmente valiosa.
- Hay recapitulaciones frecuentes y preguntas distribuidas a lo largo de los cuatro encuentros.
- Los renders son legibles; los problemas principales de esta revisión no son de clipping o tamaño, sino de construcción del aprendizaje.

## Hallazgos pedagógicos

| ID | Impacto | Slides / evidencia | Problema independiente | Consecuencia en clase | Acción propuesta | Prioridad |
|---|---|---|---|---|---|---|
| IP07-01 | major | 27–30; notas 29–30; programa | La slide 29 explica en tarjetas qué es una isofónica, pero no muestra una familia de curvas. La slide 30 pide “leer la curva”, ubicar ejes, phon, referencia de 1 kHz y comparar niveles; no hay curva visible. Las notas también indican “nombrar ejes” y “seguir la curva”. | La actividad central no puede resolverse con la evidencia proyectada. Se declara cubierto un objetivo —interpretar curvas isofónicas— sin ofrecer el objeto que debe interpretarse. | Incorporar una figura verdaderamente legible: datos normalizados con edición y condiciones verificadas, o un esquema no normativo rotulado como tal. Después, mantener una lectura guiada con dos puntos concretos. Si la figura no está disponible, reescribir la actividad para que no simule una lectura cuantitativa. | **Imprescindible** |
| IP07-02 | major | storyboard 234–236; deck 1–121 | El storyboard distingue 103 slides centrales y 18 complementarias, pero las complementarias intercaladas conservan el encabezado “RUTA CENTRAL”. Ocurre, por ejemplo, en 15–17, 26, 36, 40, 42, 61–64, 71, 74, 92, 105, 108 y 115–116. Solo el respaldo 122–134 está claramente marcado. | Un docente nuevo no puede aplicar la selección “según tiempo y necesidad”. En la práctica, la ruta visible parece contener 121 slides antes del respaldo. | Marcar “AMPLIACIÓN” en cada complementaria, crear secciones de PowerPoint y ofrecer una lista de reproducción por encuentro. Considerar ocultarlas por defecto en la versión de clase y conservar una versión completa para edición. | **Imprescindible** |
| IP07-03 | major | slides 2, 36, 40, 74, 82–84, 92, 108, 112; notas; manifiesto | Las ocho experiencias `U07-MEDIA-001` a `008` figuran como `proposed`, sin ruta local. Las notas indican reproducir algunos archivos que no existen. Hay alternativas estáticas, pero la unidad enseña fenómenos subjetivos casi exclusivamente mediante explicación verbal. | El estudiante puede memorizar distinciones sin experimentar el contraste perceptual que les da sentido. El segundo docente además recibe instrucciones que no puede ejecutar. | Producir y probar al menos dos demostraciones esenciales: una temprana de nivel físico vs. sonoridad/pitch/timbre y otra de enmascaramiento, precedencia o localización. Eliminar de las notas toda instrucción a archivos inexistentes. Mantener alternativa visual y protocolo de escucha segura. | **Imprescindible** |
| IP07-04 | major | 23–24, 49–51, 57–58, 80–81, 86, 90–91, 101, 104–105 | La progresión fórmula → ejemplo es correcta, pero varias slides de resultado repiten paneles genéricos como “Aplique la relación y explicite unidades, referencias y condiciones”. La sustitución, el cálculo y la interpretación completa aparecen sobre todo en las notas. | Para estudiantes de primer año, el procedimiento matemático queda implícito o depende demasiado de la actuación del docente. La slide parece resuelta, pero no modela cómo pensar el cálculo. | Convertir cada ejemplo central en tres pasos visibles: datos comparables → sustitución con unidades → resultado e interpretación. Mantener una sola idea de límite por ejemplo. Priorizar `G(CT)`, sones, elevación de umbral, SNR, retardo e ITD. | **Imprescindible** |
| IP07-05 | major | 74, 85, 103, 107 y 117 | Algunos diagramas son ordenados pero pedagógicamente ambiguos. En 74 la “respuesta del oyente” queda arriba y las fuentes/atención aparecen como ramas descendentes; en 85 el reconocimiento aparece como nodo del que salen ruido y reverberación; en 103 no se ve una cabeza ni dos recorridos que justifiquen `d/c`; en 107 el “cono de confusión” se nombra sin representar geometría o igualdad de ITD/ILD; en 117 el docente ocupa el centro aunque el punto integrador debería ser la mezcla que llega al oyente. | La dirección de lectura puede invertir causa y resultado, o convertir un concepto espacial en una taxonomía de cajas. El diagrama limpio no garantiza comprensión. | Redibujar desde la pregunta causal: fuentes/ambiente → señales en los oídos → procesamiento/tarea → respuesta. En ITD, mostrar dos recorridos y resaltar la diferencia de camino antes de introducir `d/c`. En cono de confusión, mostrar posiciones que comparten ITD/ILD y la pista que desambigua. | **Imprescindible** |
| IP07-06 | major | 54–75 | Entre elevación del umbral, simultaneidad, patrón frecuencial, filtros, ERB, temporalidad y distinción energético/informacional aparecen muchos nombres nuevos en un tramo corto. La estructura es rigurosa, pero el ejemplo concreto llega tarde o queda en apoyo. | El estudiante puede conservar una lista de categorías sin una escena estable que permita compararlas. | Usar una única escena objetivo–enmascarador a lo largo del bloque. Primero predecir y observar; luego nombrar simultáneo/temporal y energético/informacional. Dejar banco de filtros y ERB como explicación del patrón, no como un segundo tema paralelo. | **Recomendado** |
| IP07-07 | major | 76–87 | El bloque integra en 12 slides inteligibilidad, medición de SNR, reverberación, `T_60`, ruido, ALCons y límites causales. El brief ya lo clasificaba como carga muy alta. | Se pasa de una magnitud física a un descriptor de recinto y luego a un resultado lingüístico antes de consolidar la diferencia entre “señal disponible” y “respuesta correcta”. | Dividir el bloque en dos subrutas: a) habla, tarea e inteligibilidad; b) condiciones físicas: SNR y reverberación. Introducir ALCons primero como conteo de errores y solo después como fórmula. Mover el gráfico detallado de `T_60` a ampliación si no se lo trabajará realmente. | **Recomendado** |
| IP07-08 | major | 98–109 | ITD, ILD, dependencia con frecuencia, modelo geométrico, cálculo, pistas espectrales, cono de confusión y movimiento se presentan en doce slides. La slide 103 no aporta todavía la intuición geométrica necesaria. | La fórmula puede convertirse en el centro del bloque aunque el objetivo sea integrar pistas y límites. Vocabulario como “interaural”, “difracción”, “cota”, “pista espectral” y “cono” se acumula rápidamente. | Comenzar con una escena lateral y una predicción antes/después de mover la cabeza. Introducir ITD e ILD como observaciones, después el modelo `d/c`, y cerrar con una comparación explícita de qué explica y qué no explica cada pista. | **Recomendado** |
| IP07-09 | minor | 19, 31, 43, 53, 65, 75, 87, 97, 109, 120 | Hay muchas recapitulaciones, pero varias son listas o reapariciones del marco estímulo–tarea–respuesta. La slide 53 repite casi literalmente la organización de la 45. | La frecuencia de recapitulación es adecuada, pero no siempre produce recuperación activa. La repetición puede sentirse ritual y no diagnóstica. | Conservar cuatro recapitulaciones fuertes y convertir otras en tareas de recuperación: completar una relación, elegir una inferencia inválida, explicar un gráfico o comparar dos escenas. | **Recomendado** |
| IP07-10 | major | notas completas | Las notas están rotuladas como “Versión de redacción v01” mientras el deck es v02. En 29–30 describen una curva y ejes que no aparecen. Además, 50 slides comparten una guía visual genérica; 23 repiten la misma pregunta sobre cambiar condiciones; 18 repiten qué dato falta; las 134 incluyen la fórmula “Idea que debe quedar al cerrar”. | El segundo docente recibe un guion extenso pero poco discriminativo. La repetición hace difícil detectar qué intervención es realmente específica de cada slide. | Actualizar las notas a v02, eliminar referencias a recursos inexistentes y escribir una instrucción docente específica solo cuando agregue valor: qué señalar, qué preguntar, qué error escuchar y cuándo avanzar. | **Recomendado** |
| IP07-11 | minor | 34–43, 54–75, 98–114 | Aparecen términos avanzados con poca mediación lexical: criterio operacional, función psicométrica, correlato, supraliminal, ERB, selectividad, máscara, segregación, cota, interaural y liberación espacial. | Para primer año, la precisión terminológica puede aumentar la carga extrínseca si el término se usa antes de una imagen, escena o paráfrasis cotidiana. | Introducir primero una frase común y luego el término técnico; mantener un glosario mínimo por encuentro, no solo en respaldo. | **Recomendado** |
| IP07-12 | minor | 25, 77–87, 115–118 | Las aplicaciones fonoaudiológicas se concentran tarde. La slide 118 clasifica contenidos por unidades U7–U10, una tarea útil para el diseño curricular pero menos auténtica para el estudiante. | La transferencia profesional puede sentirse añadida al final. Clasificar “a qué unidad pertenece” no demuestra que el estudiante pueda analizar una situación auditiva. | Sustituir o reformular 118 como caso: una estudiante intenta comprender habla en aula; decidir qué medir, qué inferir y qué no diagnosticar. Insertar microaplicaciones cerca de umbral, sonoridad, enmascaramiento e ITD/ILD. | **Recomendado** |
| IP07-13 | minor | 14–16, 26, 36, 50, 60–61, 64, 84 | Los gráficos son legibles, pero la guía oral para 13 de ellos es prácticamente la misma: nombrar ejes, seguir la curva y cerrar con un límite. La slide 84 exige entender decaimiento, pendiente, extrapolación y piso de ruido en una sola lectura. | La lectura gráfica puede volverse una rutina verbal sin enseñar qué evidencia concreta extraer de cada representación. | Escribir para cada gráfico una secuencia visible o en notas: 1) qué se mantiene fijo; 2) qué cambia; 3) qué punto o región mirar; 4) qué conclusión es válida; 5) qué no puede concluirse. | **Recomendado** |
| IP07-14 | minor | 104; títulos y notación de varias slides | El título `abs(Δt(LR)) ≈ d/c` usa notación de programación y pierde la forma matemática presentada en el capítulo. También aparecen formas como `M(f(obj))` o `n(c)/n(p)` en títulos o texto corriente. | La notación deja de ser un apoyo visual y puede parecer un código alternativo no explicado. | Usar `\|Δt_{LR}\|`, `M(f_{obj})`, `n_c/n_p` y la misma notación del libro en títulos, fórmulas y notas. | **Opcional** |
| IP07-15 | suggestion | conjunto del deck | Se alternan divisores, gráficos y diagramas, pero muchas slides de desarrollo recurren a tarjetas similares y a grandes zonas vacías. La fragmentación en 134 slides produce cambios frecuentes de pantalla aun cuando algunas ideas podrían sostenerse más tiempo. | La clase puede adquirir un ritmo de “frase por slide” y perder continuidad explicativa. | Fusionar pares muy próximos cuando no haya ganancia por separación y usar revelado progresivo en ejemplos. Mantener espacios amplios, pero con una intención explícita de discusión o anotación. | **Opcional** |

## Evaluación por encuentro

### Encuentro 1 — umbral, campo e isofónicas

La entrada desde U6 y la construcción de umbral son claras. Las slides 9–19 preparan bien la idea de que detectar depende de una tarea y un criterio. El problema aparece en el cierre del encuentro: las slides 27–30 prometen pasar del procedimiento a la lectura de curvas isofónicas, pero no muestran la familia de curvas que la actividad requiere. Este vacío afecta directamente un contenido obligatorio del programa.

La fórmula campo–tímpano de 23–24 tiene preparación conceptual suficiente en 20–22, aunque el ejemplo debería mostrar visualmente sustitución e interpretación y no descansar en una consigna genérica.

### Encuentro 2 — atributos, sones y enmascaramiento

La separación frecuencia/pitch, nivel/sonoridad, espectro/timbre y tiempo/duración es adecuada. La fundamental ausente es un buen contraejemplo, pero pierde fuerza sin la escucha planificada. El bloque fones/sones está bien ordenado en definición → relación → gráfico → ejemplo → error; conviene conservar esa estructura y mejorar el ejemplo visible.

El bloque de enmascaramiento está sobrecargado por acumulación terminológica. El estudiante necesita una misma escena que se transforme en frecuencia y tiempo. ERB debe aparecer como una herramienta para explicar selectividad, no como una rama matemática nueva dentro del mismo flujo.

### Encuentro 3 — habla, recinto y reflexiones

La distinción detectabilidad/inteligibilidad es relevante y está bien formulada. Sin embargo, SNR, reverberación, `T_60` y ALCons conforman cuatro objetos diferentes: magnitud física, descriptor de decaimiento, proceso perceptual y resultado de una prueba. La secuencia actual los presenta con rapidez y exige que el docente recomponga la jerarquía oralmente.

El bloque de precedencia mejora al separar retardo físico de respuesta perceptual y al evitar una regla universal de 20 ms. Aun así, la escucha directo–copia retardada debe existir o la slide 92 debe presentarse explícitamente como predicción razonada, no como experiencia pendiente.

### Encuentro 4 — localización y fuentes concurrentes

El recorrido reconoce correctamente que ITD e ILD no bastan y que las pistas espectrales y dinámicas reducen ambigüedades. La debilidad está en la mediación visual: el modelo geométrico no muestra la diferencia de caminos y el cono de confusión no se ve como geometría. La escena final de aula es valiosa y debería convertirse en el caso organizador del encuentro, no quedar casi al final.

La actividad de clasificación U7/U8/U9/U10 evalúa conocimiento de la arquitectura del curso más que análisis psicoacústico. Un caso auténtico permitiría recuperar más conceptos y delimitar inferencias clínicas sin adelantar protocolos.

## Carga cognitiva y extensión

- Storyboard: 134 slides, de las cuales 103 son centrales, 18 complementarias y 13 de respaldo.
- Estimación del storyboard: aproximadamente 332 minutos centrales y 391 minutos con complementarias.
- Suma de duraciones de las notas: 294–315 minutos centrales, 59–67 minutos complementarios y 34–41 minutos de respaldo; 387–423 minutos para el conjunto.
- El brief estimaba una ruta central de 76–94 slides; la ruta actual tiene 103.

La extensión total no es por sí sola un error: cuatro encuentros justifican una unidad larga. El riesgo surge de tres factores combinados:

1. las ampliaciones no están señaladas en la proyección;
2. algunos encuentros reúnen demasiados conceptos de distinta naturaleza;
3. el deck agrega pantallas de recapitulación y estructura mientras deja actividades experienciales sin producir.

La revisión recomienda **reducir y señalizar la ruta central antes de sumar slides nuevas**. Las divisiones adicionales necesarias para isofónicas o ITD pueden compensarse fusionando recapitulaciones repetidas y enviando `T_60`, ERB ampliada o variantes matemáticas a ampliación/respaldo.

## Propuesta priorizada de cambios

### Imprescindibles

1. **Resolver la secuencia isofónica 27–30.** Mostrar una curva legible y coherente con la consigna, con ejes, referencia, condiciones y carácter normativo o esquemático inequívoco. Reescribir 30 según la figura real.
2. **Hacer visible la ruta docente.** Etiquetar las 18 complementarias, crear secciones por encuentro y entregar una ruta central ejecutable. No dejar ampliaciones con el encabezado “RUTA CENTRAL”.
3. **Producir un mínimo experiencial.** Entregar y probar al menos dos audios esenciales con alternativa estática; retirar toda referencia a archivos inexistentes.
4. **Rehacer los ejemplos numéricos centrales.** Mostrar datos, sustitución, unidades, cálculo e interpretación en la slide o mediante revelado, no solo en las notas.
5. **Corregir la semántica de los diagramas 74, 85, 103, 107 y 117.** Las flechas y jerarquías deben reflejar causalidad; ITD y cono de confusión necesitan geometría, no solo cajas.

### Recomendados

1. Reorganizar 54–75 alrededor de una única escena de enmascaramiento y separar observación, clasificación y modelo.
2. Dividir 76–87 en “inteligibilidad como resultado” y “condiciones físicas que la afectan”; introducir ALCons desde conteos.
3. Reordenar 98–109 para que la experiencia espacial preceda a la fórmula y para comparar explícitamente alcances de ITD, ILD, espectro y movimiento.
4. Convertir varias recapitulaciones declarativas en recuperación activa; evitar repetir 45 en 53 sin una tarea nueva.
5. Actualizar las notas a v02, hacerlas específicas y reducir frases formularias.
6. Introducir vocabulario técnico mediante paráfrasis y un glosario mínimo por encuentro.
7. Distribuir aplicaciones fonoaudiológicas junto a los conceptos y reemplazar la actividad 118 por un caso auténtico.
8. Escribir una guía de lectura específica para cada gráfico, especialmente 14, 15, 26, 60–61, 64 y 84.

### Opcionales

1. Unificar la notación visible con el capítulo y retirar formas de programación como `abs(...)`.
2. Fusionar slides demasiado fragmentarias cuando no aporten una pausa cognitiva real.
3. Variar algunas composiciones de tarjetas mediante anotación sobre gráficos, pequeños casos o comparación antes/después.
4. Convertir los diagramas raster restantes en formas nativas cuando se intervenga su contenido, sin rehacer los que no cambien.
5. Preparar una hoja docente de una página por encuentro con objetivos, slides obligatorias, ampliaciones, actividad y criterio de cierre.

## Problemas que quedan abiertos

Todos los hallazgos IP07-01 a IP07-15 quedan **open** porque esta pasada fue deliberadamente diagnóstica y no modificó el deck. Los cinco primeros bloquean la aprobación pedagógica independiente. No se declara terminada la Unidad 7 desde esta revisión hasta resolver, como mínimo, IP07-01 a IP07-05 y verificar nuevamente las slides afectadas en render y modo presentación.

## Actualización posterior de cierre — versión final

La primera pasada se preserva arriba como diagnóstico independiente. En la fase de cierre se aplicaron y verificaron las correcciones imprescindibles sin alterar el juicio original:

| Hallazgo | Estado final | Evidencia |
|---|---|---|
| IP07-01 | closed | Slide 30 contiene un trazado isofónico cualitativo con ejes, unidades, dos puntos, consigna resoluble y aviso de que no reproduce ISO 226. |
| IP07-02 | closed | Las 18 slides complementarias están rotuladas `AMPLIACIÓN`; el respaldo está separado como `A DEMANDA`. |
| IP07-03 | closed | Existen y están registrados dos WAV esenciales (`U07-MEDIA-001` y `U07-MEDIA-006`); las notas no ordenan reproducir los seis medios opcionales ausentes. |
| IP07-04 | closed | Los seis ejemplos prioritarios muestran datos → sustitución → resultado → interpretación y límite. |
| IP07-05 | closed | 74, 85, 103, 107 y 117 se redibujaron con formas nativas y dirección causal/geometría explícita. |
| IP07-06 a IP07-08 | open — accepted | La densidad se gestiona mediante cuatro encuentros, 18 ampliaciones y 13 slides de respaldo. Conviene seleccionar la ruta antes de clase. |
| IP07-09 a IP07-13 | open — accepted | Son oportunidades de refinamiento didáctico y de notas, no errores que impidan dictar la unidad. |
| IP07-14 | closed | Se eliminaron del PPTX las formas visibles `abs(...)` y subíndices convertidos en paréntesis. |
| IP07-15 | open — accepted | La extensión y el ritmo se conservan por cobertura y por el carácter denso de U7; no se proyectan las 134 slides en una sola sesión. |

Se renderizaron nuevamente las 134 slides. La inspección ampliada detectó y corrigió solapamientos internos en 85, 103 y 117; el render final no presenta problemas críticos o mayores. Con esta actualización, la revisión pedagógica independiente deja de bloquear el cierre.

## Verificación realizada

- lectura del programa y del capítulo completo en sus secciones conceptuales centrales;
- contraste de objetivos, carga y clasificación central/complementaria del storyboard;
- inspección visual de las 134 slides renderizadas;
- contraste selectivo slide–nota en los bloques de isofónicas, sones, enmascaramiento, habla, precedencia, localización y cierre;
- recuento de duración y repetición de instrucciones en notas;
- contraste del estado de los ocho recursos multimedia con el manifiesto;
- lectura crítica del informe anterior sin asumir su dictamen como válido por defecto.
