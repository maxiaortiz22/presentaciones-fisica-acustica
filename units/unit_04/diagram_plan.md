# Unidad 4 — Plan de diagramas editables

## Clasificación previa a producción

| diagram_id | clasificación obligatoria | skill |
|---|---|---|
| U04-DG-001 | diagrama conceptual | `diagram-generation` |
| U04-DG-002 | diagrama conceptual | `diagram-generation` |
| U04-DG-003 | esquema mixto | `diagram-generation` |
| U04-DG-004 | diagrama de proceso | `diagram-generation` |
| U04-DG-005 | diagrama de proceso | `diagram-generation` |
| U04-DG-006 | ecuación anotada | `diagram-generation` |
| U04-DG-007 | esquema mixto | `diagram-generation` |
| U04-DG-008 | esquema mixto | `diagram-generation` |
| U04-DG-009 | ecuación anotada | `diagram-generation` |
| U04-DG-010 | diagrama de proceso | `diagram-generation` |
| U04-DG-011 | esquema mixto | `diagram-generation` |
| U04-DG-012 | esquema mixto | `diagram-generation` |
| U04-DG-013 | ecuación anotada | `diagram-generation` |
| U04-DG-014 | diagrama de proceso | `diagram-generation` |
| U04-DG-015 | diagrama conceptual | `diagram-generation` |
| U04-DG-016 | esquema mixto | `diagram-generation` |
| U04-DG-017 | esquema mixto | `diagram-generation` |
| U04-DG-018 | esquema mixto | `diagram-generation` |
| U04-DG-019 | diagrama conceptual | `diagram-generation` |
| U04-DG-020 | esquema mixto | `diagram-generation` |
| U04-DG-021 | esquema mixto | `diagram-generation` |
| U04-DG-022 | ecuación anotada | `diagram-generation` |

## Contrato común

Todos los recursos de este archivo se clasifican como `diagram`, `equation_only` o `mixed` y se producirán mediante `diagram-generation`. La salida principal será editable en PowerPoint; SVG/PNG será respaldo, no sustituto. Canvas real 13,333 × 7,5 in o la zona exacta del layout. Texto de nodo 24 pt preferido/22 pt mínimo, conectores 20 pt mínimo y ecuaciones 30–40 pt.

Restricciones comunes: margen interno 0,18 in; 10–20 % de aire por caja; máximo tres líneas de cuerpo; corredores de conectores; 0,10 in entre línea y texto no relacionado; puntas ancladas al borde; cero cruces sobre texto. La columna “validación” se suma a estos gates comunes.

| diagram_id | slides/clase | propósito y tipo | nodos/cajas y texto estimado | conectores, etiquetas y ecuaciones | layout y geometría | editable | validación específica |
|---|---|---|---|---|---|---|---|
| U04-DG-001 | 002 · diagram | Situación problema con callouts. | 4 objetos: fuente, medio, punto de medición, receptor; 2–4 palabras por rótulo; 5 preguntas de 4–7 palabras fuera del dibujo. | Flechas solo para propagación; líderes de preguntas sin punta invasiva. | FA_22; franja central 11,8×5,5 in; fuente izquierda, receptor derecha. | Sí, formas nativas. | Ningún callout debe sugerir que el receptor crea el campo. |
| U04-DG-002 | 006, 014, 107 · diagram | Mapa prospectivo, progreso y síntesis. | 11 etapas, máximo 4 nodos por línea; 2–4 palabras por nodo. | Flechas horizontales y saltos de línea en corredores; sin etiquetas largas. | FA_03/16/17; tres bandas de 3,3–3,7 in. | Sí; grupos por encuentro. | Orden de lectura inequívoco y estado activo distinguible sin depender solo del color. |
| U04-DG-003 | 008–010 · diagram | Comparación físico/perceptual y cadena funcional. | Dos columnas de 4 filas; cadena de 4 nodos con título 1–2 palabras y verbo de 3–6 palabras. | Conectores `perturba`, `se propaga en`, `describe`, `responde`; etiquetas en cajas separadas. | FA_11/12; 60/40 o cuatro nodos horizontales. | Sí. | El campo se representa como estado/distribución, no como etapa material. |
| U04-DG-004 | 012–013 · mixed/video | Procesos vocal y electroacústico. | 4 nodos: flujo, pliegues/diafragma, perturbación, campo; 3–6 palabras por nodo. | Flechas causales; etiquetas `excita`, `oscila`, `perturba`; sin anatomía detallada. | FA_13/19; 4 nodos en arco suave o línea. | Sí; GIF externo solo como apoyo. | Separar movimiento local de avance; no atribuir toda la voz a una senoide. |
| U04-DG-005 | 016–019 · diagram | Propagación longitudinal por estados. | 5 regiones/estados; rótulos compresión, equilibrio, rarefacción; 1–3 palabras. | Flechas de partícula teal, fuerza bordó y avance gris, con leyenda textual. | FA_22/12; secuencia de 5 paneles o animación por estados. | Sí. | Direcciones correctas; no dibujar trayectoria transversal ni transporte neto de partículas. |
| U04-DG-006 | 020–022 · equation_only/mixed | Ecuación de rapidez y cambio de medio. | Ecuación central; 2 cajas de tendencia y 2 medios; 5–10 palabras por caja. | Líderes a `K_s` y `ρ`; interfaz con normal; `λ=c/f`. | FA_09/15/16; ecuación 4,5 in y dos ramas laterales. | Sí; Cambria Math. | Callouts a 0,05–0,10 in del símbolo; frecuencia idéntica en ambos medios. |
| U04-DG-007 | 024–028 · diagram/mixed | Campo, presión relativa y `u` frente a `c`. | Mapa con 2 puntos/2 tiempos; eje `p_0`; dos paneles `u`/`c`; 3–8 palabras por rótulo. | Líderes cortos; flechas locales alternantes y flecha de propagación estable. | FA_08/11; usar mitades coordinadas, no superponer tres conceptos. | Sí. | `p<0` queda debajo de `p_0` pero `p_total>0`; unidades `m/s` en ambos paneles. |
| U04-DG-008 | 029–033, 113 · diagram/equation_only | Impedancia, interfaz y reflexión. | 2 medios, interfaz, 3 ondas; ecuación `Z=p/u`, condiciones y `R_p`; 2–6 palabras por caja. | Flechas incidente/reflejada/transmitida con anclaje en interfaz; coeficientes fuera de trayectorias. | FA_08/09/22/23; visual completo para interfaz, ecuación en zona 60/40. | Sí. | Longitud de flecha no codifica amplitud; distinguir `R_p` y `R_I`; cero cruces. |
| U04-DG-009 | 035, 037–038 · equation_only | Intensidad instantánea, media y RMS. | Ecuación central más 3–4 callouts; línea temporal con ventana; caja de condiciones de 8–12 palabras. | Líderes a `p`, `u`, integral y `Z_0`; sin flechas causales. | FA_09; ecuación ≥34 pt, callouts exteriores. | Sí. | Control dimensional visible; signo interpretado como dirección; hipótesis no quedan solo en notas. |
| U04-DG-010 | 040–042 · mixed/diagram | Cadena `I–W_ac–E_ac` y medición. | 5 nodos `I`, superficie, `W_ac`, tiempo, `E_ac`; cadena de sensor de 4 nodos; 2–8 palabras. | `×S`, `×Δt`; flechas de proceso separadas de relaciones matemáticas. | FA_06B/09/13; dos filas o dos slides, nunca 9 nodos simultáneos. | Sí. | Unidades bajo cada magnitud; micrófono no conectado directamente a potencia total. |
| U04-DG-011 | 045–050 · mixed/diagram | Anotación de descriptores y matriz final. | Señal de CH-003 más 4 callouts; matriz 4×3 con 2–6 palabras por celda. | Líderes a puntos/segmentos; `p_pp=p_max−p_min`. | FA_11/08/16; gráfico 60 %, texto 40 %. | Sí, callouts y tabla nativos; gráfico SVG. | Convención de pico explícita; líderes no tocan curva ni rótulos de ejes. |
| U04-DG-012 | 052–055, 111–112 · diagram/equation_only | Proceso y fórmulas RMS. | 3 nodos `cuadrar`, `promediar`, `raíz`; 3 ecuaciones alineadas en respaldo; 3–7 palabras por nodo. | Flechas con etiquetas de función; ventana temporal común. | FA_12/09/23; 3 columnas iguales. | Sí. | Unidad Pa→Pa²→Pa; el factor `1/√2` lleva sello “solo senoide”. |
| U04-DG-013 | 060–068, 114 · diagram/equation_only | Niveles, referencias y derivación 10/20. | Tríada de 3 nodos; ecuaciones `L_p`, `L_I`, `L_W`; comparación SPL/HL/sonoridad. | Tres conectores convergentes; líderes a magnitud/referencia; derivación en 3 pasos. | FA_08/09/11/18/23; máximo 3 ecuaciones por slide. | Sí. | Toda razón adimensional; referencias y medio visibles; no usar dB aislado. |
| U04-DG-014 | 070–080, 115 · mixed/equation_only | Algoritmo y árbol de suma. | Flujo de 4 nodos; bifurcación coherente/no correlacionada; hasta 6 nodos; 3–8 palabras. | Etiquetas `fase estable`, `término cruzado`, `promedia a cero`; ecuaciones por ruta. | FA_07/09/16/23; árbol ocupa ≥75 % de ancho. | Sí; gráficos CH-008/009 como SVG. | Rutas no se cruzan; condiciones aparecen antes de `+6/+3`; correlación parcial solo respaldo. |
| U04-DG-015 | 082–089, 116–117 · diagram/mixed | Frentes plano/cilíndrico/esférico y campos. | Tres geometrías, 2–4 frentes cada una; tres recintos; árbol de 5 nodos. | Normales etiquetadas; flechas radiales; reflexiones con baja densidad. | FA_08/07/11/16/23; tres paneles de igual ancho. | Sí. | Área crece correctamente; tubo circular no se confunde con frente cilíndrico; reverberante ≠ difuso. |
| U04-DG-016 | 091–097, 118 · diagram/equation_only | Esferas, razón y ley de distancia. | Fuente, dos radios y dos superficies; 2 posiciones; derivación de 4 pasos. | Flechas radiales sin atravesar etiquetas; líderes a `r_1/r_2`; ecuaciones anotadas. | FA_22/09/15/23; geometría izquierda 55 %, ecuación derecha 45 %. | Sí. | Áreas `4πr²`; signo de `ΔL`; condiciones campo libre/fuente puntual visibles. |
| U04-DG-017 | 098–102 · diagram/equation_only/mixed | Omnidireccionalidad, `Q_dir` y `DI`. | Patrón circular, patrón direccional, comparación de 2 fuentes; 2 ecuaciones; 3–8 palabras. | Flechas angulares y líderes a lóbulo/eje; `Q_dir=...`, `DI=10log10(Q_dir)`. | FA_08/07/09/13; polar mínimo 4,2×4,2 in. | Sí; patrón de datos puede ser SVG. | Ángulos y frecuencia visibles; igual potencia/distancia en comparación; no interpretar área dibujada como potencia. |
| U04-DG-018 | 104–107, 124 · diagram/mixed | Cadena de interpretación, caso y síntesis. | 6 nodos sensor→reporte; plano de caso con fuente/puntos/recinto; mapa final 7 nodos; 3–8 palabras. | Conectores de proceso y capas de solución; condiciones en callouts. | FA_13/14/17/23; dividir cadena y caso; no más de 7 nodos. | Sí. | Caso inicial y solución mantienen geometría idéntica; no revelar respuestas antes de U04-124. |
| U04-DG-019 | 106 · diagram | Siete errores y correcciones. | Dos columnas, 7 pares; error 3–6 palabras, corrección 6–10. | Sin flechas; emparejamiento por alineación e índice, no solo color. | FA_15; 4 pares izquierda, 3 derecha. | Sí. | Texto ≥22 pt; si no entra, dividir en dos slides en vez de reducir fuente. |
| U04-DG-020 | 123 · mixed | Distancia más directividad. | Fuente direccional, dos puntos y 3 cajas de cálculo; 3–8 palabras. | Flechas radial/angular; etiquetas `ΔL_r` y `DI`; suma final en caja separada. | FA_23; plano 55 %, cálculo 45 %. | Sí. | Declarar misma referencia y modelo; ninguna flecha toca ecuaciones. |
| U04-DG-021 | 004, 011, 058 · mixed/diagram | Microvisuales de prerrequisitos, generación y checklist RMS. | U04-004: 6 ítems en dos columnas; U04-011: 5 mecanismos con rótulos de 2–5 palabras; U04-058: 4 cajas de control de 3–6 palabras. | Sin conectores en U04-004; líderes mínimos en U04-011; flujo corto señal→ventana→RMS→unidad en U04-058. | FA_02B/22/16; mantener cada microvisual dentro de su zona y sin miniaturas fotográficas. | Sí. | Cada slide conserva una función; si los cinco mecanismos quedan menores a 22 pt, dividir U04-011. |
| U04-DG-022 | 039, 110, 120 · equation_only/mixed | Ejemplos resueltos y recordatorio matemático. | 3–4 pasos numerados por ejemplo; máximo 12 palabras por caja; ecuación principal y comprobación de unidades. | Flechas verticales entre pasos; etiquetas `datos`, `relación`, `cálculo`, `interpretación`; líderes solo para unidades. | FA_10/23; columna de cálculo 65 % y verificación 35 %. | Sí. | No saltar pasos, ecuaciones ≥30 pt, coma decimal visible y resultado con unidad/condición. |

## Plan de prototipado

Prioridad de prototipo a tamaño real: DG-005 (movimiento/propagación), DG-013 (ecuación dB), DG-014 (árbol de suma), DG-015 (geometrías) y DG-017 (directividad). Estos cinco prueban los casos geométricos más riesgosos antes de producir las familias restantes.

Cada diagrama deberá conservar IDs de objetos, texto alternativo, caption, fuente conceptual e informe de iteraciones. Después de cinco iteraciones con un problema crítico o mayor, se divide la slide o se cambia el tipo de visual; no se reduce tipografía por debajo del contrato.

## Estado de producción — 2026-07-31

Las **22 familias** están generadas y aprobadas. Cada carpeta `assets/generated/diagrams/U04-DG-*` contiene fuente editable PowerPoint, SVG, PNG 2560×1440, layout estructural, README e informe JSON. El archivo `assets/generated/diagrams/u04_diagram_assets_editables.pptx` reúne una copia editable por familia para control técnico; no es la presentación de la unidad.

El render final usa texto principal de 22–40 pt, etiquetas de conectores de 21 pt, padding de 18 px o más, conectores anclados y flechas orientadas hacia el destino. `diagram_validation_report.md` y `diagram_assets_review.md` registran el ciclo de aceptación.
