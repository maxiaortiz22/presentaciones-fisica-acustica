# Unidad 5 — Plan de diagramas y ecuaciones anotadas

## Contrato común

## Clasificación e implementación v01

La clasificación se realizó antes de generar cada recurso y determina el uso de la skill `diagram-generation`:

| Clasificación obligatoria | Familias |
|---|---|
| diagrama conceptual | DG-001, DG-006, DG-010, DG-014 |
| diagrama de proceso | DG-002, DG-004, DG-012, DG-013, DG-015 |
| ecuación anotada | DG-003, DG-009 |
| esquema mixto | DG-005, DG-007, DG-008 |

Se aprobaron y generaron DG-001 a DG-010 y DG-012 a DG-015. DG-011 permanece `pending_standard_check` porque depende de la verificación de IEC 61672-1 y de CH-017. La tabla de familias conserva el estado de aprobación previo; esta sección y `diagram_validation_report.md` son el registro vigente.

Todo diagrama se construirá en el tamaño real de su layout. Por defecto tendrá versión editable con formas nativas de PowerPoint y respaldo SVG/PNG. Texto principal ≥22 pt, títulos de nodo 24–28 pt, etiquetas de conector ≥20 pt, ecuaciones centrales ≥28 pt, margen interior ≥0,18 in y 10–20 % de aire. Los conectores irán anclados y detrás de los nodos; ninguna línea, punta o etiqueta podrá tocar texto.

## Familias planificadas

| diagram_id | slides | propósito pedagógico | tipo | nodos o cajas y texto estimado | conectores y etiquetas | ecuaciones/fórmulas | layout previsto | restricciones geométricas | validaciones obligatorias | editable en PowerPoint | estado |
|---|---|---|---|---|---|---|---|---|---|---|---|
| U05-DG-001 | U05-001, 006, 129 | Orientar la unidad y mostrar progreso acumulativo | mapa narrativo | 4 tramos, hasta 12 hitos; 2–5 palabras por hito | flechas horizontales por tramo; etiquetas de etapa | ninguna | FA_03_MAPA_CLASE / FA_21_CIERRE_PUENTE | agrupar 12 hitos en 4 tramos; revelar progresivamente; sin miniaturas | orden de lectura, cero cruces, texto ≥22 pt, geometría idéntica entre versiones | sí; master con estados | proposed |
| U05-DG-002 | U05-003, 004, 007 | Instalar la rutina “objeto–ejes–unidades–condiciones” | marco de lectura/checklist | 5 cajas; 2–6 palabras por caja; variante de puente con U3/U4 | flujo corto numerado; sin frases largas sobre flechas | símbolos mínimos `t`, `f`, unidad | FA_02B / FA_12_PROCESO / FA_14 | conectores en corredor central; cinco cajas máximo | cada recap conserva posición; campos legibles; no confundir objeto con eje | sí | proposed |
| U05-DG-003 | U05-010, 015, 018, 022–029, 133–135 | Graduar periodicidad, serie y transformada | ecuaciones anotadas y comparación | ecuación central + hasta 4 callouts; cajas de 3–8 palabras | líderes cortos sin cruces; flechas solo en ejemplos por pasos | `x(t+T)=x(t)`, `f_0=1/T_0`, serie, transformada, forma polar | FA_09 / FA_10 / FA_23 | ecuación ≥34 pt; máximo 4 callouts; dividir coeficientes y transformada | símbolos/unidades definidos, líderes a 0,05–0,10 in, control dimensional y de convención | sí; OMML preferido | proposed |
| U05-DG-004 | U05-030–031, 033–040, 133–136 | Hacer visible la cadena digital y las relaciones de muestreo | proceso + ecuaciones | captura, muestras, segmento, ventana, DFT y bins; 3–6 palabras por nodo | conectores de proceso; etiquetas `f_s`, `N`, `T_obs` en zonas libres | `T_obs=N/f_s`, `Δf=f_s/N`; DFT a respaldo | FA_12 / FA_09 / FA_23 | seis nodos máximo; dividir captura y análisis si baja de 24 pt | direcciones correctas, unidades, cero superposición, DFT ≠ FFT explícito | sí | proposed |
| U05-DG-005 | U05-041–042, 047, 049–051, 137–140 | Explicar recorte, espectrograma y bin frente a banda | proceso/comparación | señal larga, segmento, ventanas, rejilla tiempo–frecuencia, bin y banda; 2–7 palabras | flechas de selección y agrupamiento; etiquetas fuera de gráficos | ventana multiplicativa; suma por banda en respaldo | FA_12 / FA_11 / FA_16 | gráficos ocupan ≥55 %; callouts no invaden ejes; bin/banda alineados | cada flecha representa operación; parámetros visibles; no mezclar dB incompatibles | sí; charts como SVG enlazados | proposed |
| U05-DG-006 | U05-052–062 | Separar espectro de señal y respuesta del sistema | diagrama de bloques | entrada `X`, sistema `H`, salida `Y`, condiciones; 2–8 palabras por caja | `atraviesa`, `modifica`, `se observa`; conectores rectos anclados | `Y=HX`, `H=Y/X`, `G=20log10\lvert H\rvert` | FA_12 / FA_09 / FA_13 | tres nodos centrales; ejemplos laterales no cruzan la cadena | unidades compatibles, condición `X≠0`, flechas al destino, magnitud/fase diferenciadas | sí | proposed |
| U05-DG-007 | U05-063–073, 141 | Ordenar fundamental, armónico, parcial, sobretono y formante | taxonomía + fuente–filtro | hasta 6 términos; 3–8 palabras por definición; fuente y tracto como 2 cajas | relaciones “es un caso de”, “por encima de”; fuente→filtro→salida | `f_n=n f_0` y relación de envolvente conceptual | FA_11 / FA_08 / FA_12 | evitar árbol con más de 2 niveles; gráficos separados de definiciones | cada término tiene contraejemplo; no igualar formante y armónico; conectores semánticos | sí | proposed |
| U05-DG-008 | U05-077, 079–083 | Mostrar rangos y límites condicionados | escalas anotadas + comparación | eje de frecuencia y eje de nivel; 4 condiciones por rango; 3–7 palabras | líderes a regiones/límites; no flechas causales | `R_D=L_sup−L_inf` | FA_09 / FA_11 / FA_15 | límites como bandas, no líneas absolutas; dos escalas no superpuestas | condición/población/descriptor visibles; sin cifra universal de dolor | sí | proposed |
| U05-DG-009 | U05-086–094, 142–143 | Construir octavas y tercios desde razón, centro y límites | eje logarítmico + ecuación anotada | eje con centros/límites; 3 cajas de cálculo; 3–8 palabras | líderes verticales a `f_L`, `f_c`, `f_H`; pasos numerados | `f_H/f_L=2^(1/b)`, `f_c=√(f_Lf_H)`, límites y `B` | FA_09 / FA_10 / FA_11 / FA_23 | eje ocupa ≥60 %; máximo 3 fórmulas centrales; derivación a respaldo | valores coinciden con CH-014; líderes sin tocar ticks; armónico/octava separados | sí | proposed |
| U05-DG-010 | U05-095–105, 144 | Relacionar tipos de filtro, parámetros y usos | taxonomía + cadena de sistema | 4 tipos; entrada/filtro/salida; 2–6 palabras por caja | ramas hacia cuatro respuestas; etiquetas `pasa`, `atenúa` | `f_c`, `f_L`, `f_H`, `B`; pendiente solo a respaldo | FA_11 / FA_12 / FA_13 | máximo 4 ramas; curvas de CH-016 no se reducen por debajo de 3,4 in | criterio de corte visible; ideal/real distinguibles; cero cruces | sí; curves SVG + formas | proposed |
| U05-DG-011 | U05-106–116, 145 | Explicar ponderación como procesamiento previo al descriptor | cadena con tres ramas + ecuación | señal, A/C/Z, integración y resultado; 2–7 palabras | bifurcación a tres filtros y convergencia; etiquetas fuera de líneas | `L_A(f)=L_Z(f)+A(f)` para tono; expresiones normativas a respaldo | FA_12 / FA_09 / FA_15 | máximo 3 ramas; no superponer curvas y cadena; ecuación tonal separada | signos y unidades; A no igual a audición/dB HL; curvas coinciden con CH-017 | sí | pending_standard_check |
| U05-DG-012 | U05-117–124, 146–148 | Integrar cadena de sonómetro y descriptores temporales | proceso de medición + timeline | micrófono, preamplificación, ponderación, detector/integración, indicador, informe; 2–6 palabras | proceso izquierda→derecha; etiquetas de configuración en cajas aparte | `L_Xeq,T`, máximo y pico; integral solo respaldo | FA_12 / FA_10 / FA_13 / FA_23 | agrupar en transducción/procesamiento/informe; dividir si seis nodos no entran | etapa/configuración correctas; max ≠ peak; calibración no omitida; cero colisiones | sí | proposed |
| U05-DG-013 | U05-125–131 | Transferir la elección de herramienta a casos profesionales | árbol de decisión + caso en dos zonas | pregunta inicial, señal/sistema/medición, evidencia y límite; 3–8 palabras | ramas con preguntas sí/no de 1–4 palabras | relaciones ya aprendidas, sin fórmula nueva | FA_13 / FA_14 / FA_17 | máximo cinco hojas; caso y solución mantienen geometría | rutas resolubles; respuestas no visibles antes del revelado; límites de inferencia presentes | sí | proposed |
| U05-DG-014 | U05-017, 029, 040, 051, 062, 083, 094, 105, 116, 124 | Recuperar la rutina de lectura con información acumulativa | recap master | 5 campos estables; 2–6 palabras; un campo nuevo resaltado | sin conectores largos; progreso por posición y rótulo | ecuación mínima solo si es objeto del bloque | FA_16_RECAP_PARCIAL | misma grilla en 10 variantes; no copiar definiciones completas | comparación de versiones; texto ≥22 pt; el color no es única señal de progreso | sí; master reutilizable | proposed |
| U05-DG-015 | U05-149–150 | Conservar solución integradora y navegación de respaldo | proceso + índice | 4 pasos de solución; glosario con retornos; 3–8 palabras | flechas verticales entre pasos; índice sin conectores | solo ecuaciones ya introducidas | FA_23_APENDICE | máximo 4 pasos por columna; glosario como tabla nativa | solución coincide con actividad; hipervínculos/retornos funcionan; sin reducción tipográfica | sí | proposed |

## Orden de prototipado

Prototipar primero DG-003, DG-004, DG-006, DG-009, DG-011 y DG-012. Cubren los riesgos mayores: callouts sobre ecuaciones, cadena digital larga, señal–sistema, eje logarítmico, bifurcación A/C/Z y cadena sonométrica.

## Gates de aceptación

Cada familia requiere: editable PowerPoint, SVG/PNG de respaldo, preview renderizado en el layout real, lista de objetos/IDs, texto alternativo, caption, fuente conceptual, informe de iteraciones y cero problemas críticos o mayores. Después de cinco iteraciones con un problema persistente, se divide la slide; no se reduce la tipografía.

## Estado

**Implementación v01 completada para 14 de 15 familias.** Cada familia aprobada incluye fuente editable, PPTX editable, SVG, PNG 2560×1440, README, texto alternativo, caption e informe de validación. No se construyó ni modificó la presentación de la unidad.
