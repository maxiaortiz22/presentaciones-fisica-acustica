# Unidad 5 — Decisiones abiertas

## Propósito

Este registro reúne decisiones que afectan alcance, notación, secuencia, recursos o tiempo. No constituye un storyboard. Las decisiones de prioridad alta deben resolverse antes de aprobar la secuencia slide por slide.

## Decisiones pendientes

| ID | Prioridad | Decisión | Evidencia/tensión | Recomendación preliminar | Impacto si queda abierta | Estado |
|---|---|---|---|---|---|---|
| OD-U05-01 | Alta | Definir cuántos encuentros y cuánto tiempo se asignan a U5. | Parte central estimada en 82–104 slides; carga muy alta y recapitulaciones obligatorias. | Planificar tres o cuatro encuentros de 75–100 min; si hay menos tiempo, acordar una ruta de corte explícita. | Determina profundidad de Fourier digital, espectrograma y sonometría. | Pendiente de planificación docente. |
| OD-U05-02 | Alta | Fijar profundidad central de muestreo, DFT y FFT. | No figuran literalmente en el programa, pero el libro, `course_map.md` y las aplicaciones reales los incorporan. | Mantener una ruta mínima central: registro finito, `f_s`, `N`, `T_obs`, `Δf` y FFT como algoritmo; dejar normalización y detalle computacional como complemento/respaldo. | Puede dejar el análisis desconectado de software real o sobrecargar el núcleo. | Pendiente de validación docente. |
| OD-U05-03 | Alta | Decidir si ventanas, fuga y espectrograma integran la ruta central. | Son `out_of_scope` literal, pero el espectrograma es muy relevante para voz y habla. | Incluir al menos un ejemplo visual central de compromiso tiempo–frecuencia; mover detalles de ventanas y fuga a complemento si el tiempo es limitado. | Afecta aplicaciones de voz y comprensión de espectros reales. | Pendiente. |
| OD-U05-04 | Alta | Acordar nivel matemático visible de la serie de Fourier. | El programa exige serie; el capítulo incluye ecuación infinita y coeficientes integrales. | Mostrar la síntesis progresiva y la estructura de la serie en el núcleo; no exigir cálculo de `a_n`/`b_n`. | Puede convertirse en memorización formal o quedar demasiado superficial. | Pendiente de validación pedagógica. |
| OD-U05-05 | Alta | Acordar nivel matemático visible de la transformada. | La integral compleja introduce `j`, unidades y convención. | Presentar primero significado, magnitud y fase; mostrar la integral como formalización de referencia, sin evaluación operativa. | Puede crear una barrera matemática o incumplir el alcance si se omite toda formalización. | Pendiente. |
| OD-U05-06 | Alta | Seleccionar datos para rangos dinámicos vocal e instrumental. | El programa los exige; el libro evita cifras por falta de condiciones universales. | Buscar en etapa de assets/fuentes ejemplos con tarea, distancia, descriptor, ponderación, instrumento y población declarados; no usar tablas genéricas. | El tema puede quedar abstracto o apoyarse en cifras engañosas. | Pendiente de fuentes verificadas. |
| OD-U05-07 | Alta | Resolver el tratamiento de “rango dinámico del oído: umbral de dolor”. | El programa usa “umbral de dolor”; el libro propone límites definidos y rechaza una cifra universal. | Explicitar la formulación del programa, usar “límite superior definido” y comparar dolor/incomodidad solo con fuente y condiciones. Confirmar con docente y Audiología. | Riesgo de enseñar un umbral universal o de parecer que se omitió el programa. | Pendiente de validación docente. |
| OD-U05-08 | Media | Elegir cómo relacionar armónicos y octavas. | El programa los yuxtapone; el capítulo los desarrolla por separado. | Crear una comparación explícita: armónicos son múltiplos enteros de `f_0`; octava es razón `2:1`; algunos pares armónicos quedan separados por octavas. | Puede consolidarse la idea errónea de que toda sucesión armónica avanza por octavas. | Pendiente para storyboard. |
| OD-U05-09 | Alta | Definir notación para transformada de presión. | Guía: `x(t)`/`X(f)` genéricos y `p(t)` para presión; `course_map.md` incluye `P(f)`. | Usar `x(t)`/`X(f)` al explicar la herramienta y `p(t)`/`P(f)` solo después de declarar la convención en un ejemplo acústico. | Afecta ecuaciones, gráficos y continuidad entre U4–U5. | Pendiente de validación de notación. |
| OD-U05-10 | Alta | Definir qué representa el eje vertical de cada visual espectral. | El capítulo advierte que puede ser amplitud, magnitud, potencia, densidad o nivel; los recursos actuales no comparten una única convención. | Crear una ficha de metadatos por gráfico: variable, unidad, escala, referencia, ventana, normalización y rango. | Se puede enseñar “FFT = intensidad” o comparar gráficos incompatibles. | Recomendación obligatoria; pendiente de especificación por recurso. |
| OD-U05-11 | Media | Decidir centralidad de la fase espectral. | El programa no la nombra; el capítulo la usa para completar Fourier y respuesta. | Mantener la idea y un ejemplo central; reservar cálculo de fase y retardo para complemento. | Sin fase, la representación queda incompleta; con exceso de formalismo, se desvía el foco. | Pendiente según tiempo. |
| OD-U05-12 | Alta | Generar o no una figura propia de ponderaciones A/C/Z. | El capítulo contiene un `TODO`; el programa exige A y el libro amplía C/Z. | Generar curvas nominales desde expresiones verificadas en la etapa de gráficos; citar edición y rotular que no son límites de aceptación. | La ponderación A quedaría verbal o podría mostrarse con una curva no trazable. | Pendiente para `chart-generation`. |
| OD-U05-13 | Alta | Adoptar nomenclatura `dBA`/`dB(A)` y descriptores. | Programa: `dBA`; guía/libro: `dB(A)` o `L_A...`. | Presentar `dBA` como escritura del programa y adoptar `dB(A)`, `L_Aeq,T`, `L_AFmax`, etc., en uso técnico. | Inconsistencia con fuentes y pérdida de información temporal. | Recomendación lista; falta validar con docente. |
| OD-U05-14 | Media | Profundidad central de C, Z, `L_eq`, máximo y pico. | Son ampliaciones fuera del listado literal, pero evitan absolutizar A y preparan U10. | Introducción central breve; cálculo de `L_eq` y detalle temporal como módulo ampliable. | Puede desplazar contenido obligatorio o dejar al estudiante sin contexto metrológico. | Pendiente según tiempo. |
| OD-U05-15 | Media | Incluir un caso real o sintético de voz. | El libro contiene aplicación verbal y figura sintética, pero no un registro vocal trazable. | Priorizar un registro propio/autorizado con parámetros reproducibles; si no existe, usar señal sintética y declarar el límite. | Afecta relevancia profesional, permisos y reproducibilidad. | Pendiente de recurso. |
| OD-U05-16 | Media | Profundidad de formantes y modelo fuente–filtro. | No aparece literalmente en el programa; es relevante para Fonoaudiología y puede invadir U7/voz clínica. | Incluir una introducción que separe líneas armónicas y envolvente; no introducir medidas diagnósticas. | Puede confundir formante con armónico o anticipar clínica sin base. | Recomendación preliminar. |
| OD-U05-17 | Alta | Seleccionar ejercicios del banco para el hilo principal. | Hay 6 conceptuales, 5 lecturas, 5 guiados, 5 autónomos, 5 aplicaciones, 1 integrador y 4 distractores. | Elegir una predicción, una lectura y una aplicación por bloque; mover soluciones y variantes a respaldo. | El deck puede crecer sin control o quedar sin práctica suficiente. | Pendiente para storyboard. |
| OD-U05-18 | Media | Confirmar disponibilidad de software, audio y equipos de medición. | Fourier, filtros y sonometría se benefician de demostraciones, pero requieren control de nivel y alternativa visual. | Inventariar generador/análisis espectral, parlantes, micrófono, calibrador y sonómetro; diseñar demostraciones que no dependan del equipo. | Afecta assets, tiempo, seguridad y reproducibilidad. | Pendiente de recursos docentes. |
| OD-U05-19 | Media | Reutilizar o reconstruir las ocho figuras del libro. | Son propias y correctas, pero diseñadas para página vertical y lectura cercana. | Reconstruir a tamaño de slide, por etapas y con SVG/objetos editables; conservar scripts y trazabilidad. | Copiarlas directamente produciría ilegibilidad y baja editabilidad. | Decisión recomendada; pendiente de producción. |
| OD-U05-20 | Alta | Corregir referencias de sección U05 en `content_coverage_matrix.csv`. | Las filas apuntan a numeración anterior; por ejemplo, componentes figuran como 5.11 y sonómetro como 5.17. | Realizar una tarea posterior con `course-architecture` para actualizar solo `book_section`, preservando estado y decisiones. | La trazabilidad del storyboard y revisiones futuras será defectuosa. | Pendiente; fuera de los cuatro archivos solicitados. |
| OD-U05-21 | Media | Definir fuente y edición para curvas/límites normativos. | El capítulo cita IEC 61260, IEC 61672, ISO 8253 y ANSI/ASA; la vigencia y jurisdicción importan. | Verificar edición aplicable antes de mostrar curvas, tolerancias o límites; distinguir material conceptual de normativo. | Riesgo de presentar requisitos desactualizados o universales. | Pendiente para fuentes/assets. |
| OD-U05-22 | Media | Decidir tratamiento de frecuencia de muestreo máxima/aliasing. | El capítulo introduce `f_s` pero no desarrolla Nyquist/aliasing en U5; una lectura digital puede necesitar al menos una cautela. | Añadir solo un límite conceptual si el bloque digital es central; reservar demostración y fórmulas avanzadas para complemento. | Puede quedar un vacío técnico o abrir un bloque fuera de alcance. | Pendiente según decisión OD-U05-02. |
| OD-U05-23 | Media | Definir criterio de frecuencia de corte visible. | El libro menciona `−3 dB` como modelo común, no universal. | Etiquetar explícitamente el criterio en cada filtro; no usar `f_c` sin definición. | Refuerza la idea de corte abrupto o universal. | Recomendación obligatoria. |
| OD-U05-24 | Media | Diferenciar sonómetro real, aplicación móvil y demostración. | La aplicación profesional del capítulo rechaza equivalencia automática. | Si se muestra una app, usarla solo para observar tendencias y contrastarla con instrumento/configuración/calibración. | Puede legitimar mediciones no trazables en contexto clínico. | Pendiente de diseño de demostración. |

## Decisiones ya adoptadas para esta etapa

| ID | Decisión | Justificación |
|---|---|---|
| DA-U05-01 | No crear storyboard ni PowerPoint. | Solicitud explícita del usuario y flujo obligatorio del repositorio. |
| DA-U05-02 | No redactar contenido visible ni notas de slides. | La etapa termina en brief, inventario, análisis y decisiones. |
| DA-U05-03 | Tratar U5 como carga conceptual muy alta. | Coincidencia entre `AGENTS.md`, `course_map.md`, `course_dependency_map.md` y cantidad de objetos/representaciones. |
| DA-U05-04 | Usar bloques cortos y recapitulaciones frecuentes. | Requisito específico para U5; la mini tabla “objeto–ejes–unidad–condiciones” será el patrón de cierre. |
| DA-U05-05 | Distinguir espectro de señal y respuesta de sistema como eje central. | Es objetivo del programa, evidencia mínima del mapa y nudo crítico de dependencias. |
| DA-U05-06 | Mantener Fourier como representación matemática, no mecanismo físico. | Advertencia explícita del capítulo y error frecuente crítico. |
| DA-U05-07 | No fijar fronteras auditivas ni umbral de dolor como valores universales. | El capítulo y la matriz exigen condiciones de frecuencia, nivel, estímulo y oyente. |
| DA-U05-08 | Usar `sonómetro` como término preferido y explicar la formulación del programa. | Coherencia con glosario y uso técnico. |
| DA-U05-09 | No incorporar fuentes externas nuevas en esta etapa. | Las fuentes locales bastan para el análisis; datos, imágenes y curvas externas se resolverán en assets/gráficos. |
| DA-U05-10 | No modificar `course_map.md`, `course_dependency_map.md` ni la matriz en esta tarea. | El pedido limita la salida a cuatro archivos de U5; la corrección de trazabilidad queda registrada. |

## Orden recomendado de resolución antes del storyboard

1. confirmar número y duración de encuentros;
2. acordar la ruta mínima/ampliada de DFT, ventanas y espectrograma;
3. validar el tratamiento matemático de serie y transformada;
4. resolver notación `X(f)`/`P(f)` y metadatos obligatorios de gráficos;
5. acordar el tratamiento de rangos dinámicos y umbral de dolor;
6. seleccionar o producir datos/recursos de voz y rangos;
7. confirmar figura y fuentes para A/C/Z;
8. decidir profundidad de `L_eq`, máximo, pico y verificación instrumental;
9. confirmar equipos y alternativas de demostración;
10. seleccionar ejercicios por bloque;
11. planificar reconstrucción de las ocho figuras;
12. programar la corrección de referencias U05 en la matriz de cobertura.
