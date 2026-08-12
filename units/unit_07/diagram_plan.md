# Unidad 7 — Plan de diagramas y ecuaciones anotadas

Versión implementada v01 · 2026-08-11

## Resultado de implementación

Se produjeron **55 recursos aprobados**: 11 diagramas conceptuales, 20 diagramas de proceso, 13 ecuaciones anotadas y 11 esquemas mixtos. Cada carpeta conserva fuente editable JSON, PPTX editable, SVG, PNG 2560×1440, preview, README con caption/alt/fuente y validación.

- **Aprobados:** U07-DG-001–009, 009B, 011–021 (excepto 020C), 022A–022C y 023–043, incluidas todas las variantes `B` previstas.
- **Bloqueado:** U07-DG-010, hasta seleccionar la fotografía REM y construir el overlay definitivo.
- **Bloqueado:** U07-DG-020C, hasta decidir la inclusión y alcance de la fórmula ERB de Glasberg–Moore.
- **Alias:** U07-DG-022 remite a las variantes aprobadas 022A, 022B y 022C; no constituye un archivo adicional.

El inventario por recurso está en `diagram_assets_review.md` y el cierre de QA en `diagram_validation_report.md`.

## Contrato de implementación

Antes de producirse, cada recurso se clasifica como **diagrama conceptual**, **diagrama de proceso**, **ecuación anotada** o **esquema mixto**. Se implementaron con formas, textos y conectores nativos de PowerPoint. El SVG/PNG es respaldo y preview, nunca sustituto predeterminado del editable.

- Canvas: área real del layout 16:9, con márgenes seguros del master.
- Texto de nodo: 24 pt preferido, 22 pt mínimo; conectores 20 pt mínimo; ecuaciones 28–40 pt.
- Cajas: margen interior ≥0,18 in, 10–20 % de aire y máximo tres líneas de cuerpo.
- Conectores: anclados a bordes, corredor previo, etiqueta independiente y ≥0,10 in respecto de texto ajeno.
- Callouts: máximo cuatro alrededor de una ecuación; líderes cortos que terminen a 0,05–0,10 in del símbolo.
- Si el contenido no entra: reducir texto, redistribuir o dividir; nunca auto-shrink por debajo del mínimo.

## Plan por familia

| diagram_id | slides | propósito y tipo | nodos/cajas y texto estimado | conectores y etiquetas | ecuación/fórmula | layout | restricción geométrica | editable PPT | estado |
|---|---|---|---|---|---|---|---|---|---|
| U07-DG-001 | 003 | Proceso puente U6→U7 | 4 nodos, 2–5 palabras: campo, oído periférico, tarea, respuesta | 3 flechas; etiquetas “transfiere”, “condiciona”, “se registra” fuera de línea | ninguna | FA_12 | cadena horizontal; no reabrir anatomía | sí | listo |
| U07-DG-002 | 005 | Matriz de clasificación físico/perceptual | 8 rótulos, 1–3 palabras, en 4 pares | sin flechas; revelado par a par | símbolos/unidades breves | FA_14B | dos columnas estables; unidad como evidencia | sí | listo |
| U07-DG-003 | 007 | Mapa de cuatro encuentros | 4 macroetapas, 2–4 palabras | 3 conectores con etapa actual destacada | ninguna | FA_03 | una sola línea o 2×2; evitar “tarjetas” decorativas | sí | listo |
| U07-DG-004 | 009, 019 | Marco estímulo–tarea–respuesta | 3 nodos + banda “condiciones”, 2–6 palabras | 2 flechas; “presentar” y “registrar” | ninguna | FA_08/16 | banda inferior no debe parecer cuarto paso | sí | listo |
| U07-DG-005 | 010 | Proceso de observación psicofísica | 3 etapas y 3 tareas alternativas, 2–5 palabras | bifurcación desde estímulo; etiquetas breves | ninguna | FA_12 | usar codos; cero cruces entre tareas | sí | listo |
| U07-DG-006 | 018 | Callouts de condiciones | dato central + 6 condiciones, 1–4 palabras | 6 líderes sin punta sobre el dato | ninguna | FA_14B | distribuir en dos columnas; no radial si cruza | sí | listo |
| U07-DG-007 | 021 | Geometría de campo libre | fuente, onda, punto y dirección, 1–4 palabras | flecha de propagación y líder al punto | `L_p,campo` como rótulo | FA_05 | corredor horizontal; sin oyente en el panel | sí | listo |
| U07-DG-008 | 022, 031 | Transferencia campo→tímpano | campo, cabeza/pabellón, CAE, tímpano; 1–4 palabras | 3 conectores; “dirección”, “geometría”, “frecuencia” como callouts | ninguna | FA_22 | reconstruir `campo-cae-timpano.tex`; no copiar miniatura | sí | listo |
| U07-DG-009/009B | 023–024 | Ecuación anotada y ejemplo `G_CT` | ecuación central + 3 callouts; variante datos/pasos | líderes a términos; flujo datos→resta→límite | `G_CT(f)=L_p,T(f)-L_p,campo(f)` | FA_09/10 | unidades fuera del operador; máximo 4 callouts | sí; ecuación editable/SVG | listo |
| U07-DG-010 | 025 | Callouts sobre foto REM | 4 rótulos: sonda, micrófono referencia, posición, señal | líderes externos sin cubrir oreja/sonda | ninguna | FA_13 | recorte 40 %; callouts fuera de la foto si es posible | sí overlay | shortlist foto |
| U07-DG-011 | 028–031, 123 | Proceso de construcción isofónica | referencia, prueba, juicio, punto, repetición; 2–6 palabras | 5 flechas; “ajustar”, “igual sonoridad”, “repetir” | `f_ref=1 kHz` | FA_12 | dos niveles; curva inferior claramente esquemática | sí | listo; alternativa a ISO |
| U07-DG-012/012B | 033, 043 | Mapa físico–perceptual | 4 pares y enlaces secundarios, 1–4 palabras | flechas `relaciona`, nunca signo igual | símbolos de U7 | FA_03/16 | enlaces secundarios solo tras revelar pares | sí | listo |
| U07-DG-013 | 045, 053 | Comparación de tres cantidades | 3 columnas: `L_p`, `L_N`, `N_son`; 3 filas breves | sin flechas; relación por encabezados | símbolos y unidades | FA_11 | columnas iguales; no comprimir definiciones | sí | listo |
| U07-DG-014 | 048 | Construcción de referencia fon/son | 4 etapas, 2–5 palabras | 3 flechas; “igualar” y “adoptar referencia” | 40 fon ↔ 1 son | FA_12 | evitar sugerir conversión directa desde `L_p` general | sí | listo |
| U07-DG-015/015B | 049, 051 | Ecuación anotada y cálculo fones–sones | ecuación + 4 callouts; variante 4 pasos | líderes a base, exponente, referencia y unidad | `N_son=2^((L_N-40 fon)/(10 fon)) son` | FA_09/10 | ecuación ≥32 pt; dominio `L_N≥40 fon` visible | sí; ecuación editable/SVG | listo |
| U07-DG-016 | 056 | Mapa de niveles de enmascaramiento | 3 cajas, 2–5 palabras | flechas desde condición a nivel; no conectar nivel de máscara como umbral | símbolos completos | FA_03 | subíndices legibles; 3 ramas sin cruces | sí | listo |
| U07-DG-017/017B | 057–058 | Ecuación `M` y ejemplo | ecuación + 3 callouts; variante datos/resta/interpretación | líderes cortos; flujo lateral para ejemplo | `M(f_obj)=L_umbral,e-L_umbral,q` | FA_09/10 | no cruzar subíndices; unidad dB fuera de resta | sí; ecuación editable/SVG | listo |
| U07-DG-018 | 059 | Línea temporal simultánea | 2 pistas y 2 bloques, 1–2 palabras | eje `t`; llaves de solapamiento | ninguna | FA_12 | pistas alineadas; duraciones declaradas esquemáticas | sí | listo |
| U07-DG-019 | 063 | Banco de filtros | espectro entrada + 5 canales, 1–3 palabras | entrada→banco→salidas, con codos | ninguna | FA_22 | si cinco salidas no caben a 22 pt, usar 3 representativas | sí | prototipo |
| U07-DG-020/020B/020C | 064–065, 125–127 | ERB: área, cadena y fórmula | curva/rectángulo + 3 nodos; variante ecuación | líderes a altura, área, ancho; cadena estímulo→canal→decisión | fórmula Glasberg–Moore solo en 020C | FA_09/16/23 | gráfico y callouts en capas; fórmula separada si queda densa | sí; gráfico SVG separado | espera OD-U07-04 para 020C |
| U07-DG-021 | 067–071 | Comparación temporal triple | 3 filas, objetivo y máscara, 1–2 palabras | ejes `t`, llaves `Δt`, sin flechas causales | ninguna | FA_11/14 | misma escala visual; nombres alineados a izquierda | sí | listo |
| U07-DG-022A–C | 072–075, 113 | Mecanismos energético/informacional | 2 rutas de 3 nodos + matriz final, 2–5 palabras | flechas funcionales; etiquetas “competencia”/“selección” | ninguna | FA_08/16 | revelar rutas por separado; no más de 5 nodos simultáneos | sí | prototipo |
| U07-DG-023 | 074 | Escena de dos voces | objetivo, competidora, canales, atención, respuesta | dos entradas convergen; rutas visualmente distintas | ninguna | FA_13 | no usar color como única diferencia; audio opcional | sí | listo |
| U07-DG-024 | 078 | Condiciones de inteligibilidad | 3 grupos con 3 ítems: estímulo, procedimiento, oyente | convergen a resultado; etiquetas ausentes para reducir carga | porcentaje como salida | FA_03 | 3 columnas; máximo 6 palabras por ítem | sí | listo |
| U07-DG-025/025B | 080–081 | SNR anotada y ejemplo | ecuación + 4 callouts; variante datos/signo/límite | líderes a `s`, `n`, resta, dB | `SNR=L_p,s-L_p,n` | FA_09/10 | condiciones comunes en banda inferior, no en callouts | sí; ecuación editable/SVG | listo |
| U07-DG-026/026B | 083, 085 | Habla, colas y ruido | 3 sílabas + 3 respuestas/colas; variante causal | flechas temporales y causalidad en capas separadas | ninguna | FA_12/05 | no cruzar línea temporal con flechas causales | sí | prototipo |
| U07-DG-027 | 084 | `T_60` anotado | curva CH-009 + 3 callouts | líderes a inicio, −60 dB y intervalo | definición `ΔL=−60 dB` | FA_07 | gráfica sigue siendo capa SVG; callouts editables | sí overlay | listo con CH-009 |
| U07-DG-028/028B | 086–087, 131 | ALCons, ejemplo y síntesis | ecuación + `n_p`, `n_c`, resultado; variante cadena | líderes a conteos y porcentaje | `ALCons=100(1-n_c/n_p)%` | FA_10/16 | separar porcentaje observado de predicción acústica | sí; ecuación editable/SVG | listo |
| U07-DG-029 | 089, 132 | Geometría directo/reflejado | fuente, superficie, oyente, 2 caminos; 1–4 palabras | directa y reflejada con estilos distintos; líderes `r_d`, `r_r` | ninguna | FA_22/14 | reservar corredor para reflexión; punta en oyente, no texto | sí | listo |
| U07-DG-030/030B | 090–091, 132 | Retardo anotado y ejemplo | ecuación + 3 callouts; variante 4 pasos | líderes a diferencia de recorrido y `c` | `Δt=(r_r-r_d)/c` | FA_09/10 | control dimensional visible; 20 ms no frontera | sí; ecuación editable/SVG | listo |
| U07-DG-031 | 093 | Mapa de factores de precedencia | 4 grupos, 2–4 palabras | convergen a respuesta perceptual | ninguna | FA_03 | 2×2; sin red completa | sí | listo |
| U07-DG-032 | 095 | Familia del efecto de precedencia | 2 llegadas→3 tareas/respuestas, 2–6 palabras | bifurcación con etiquetas “fusión”, “localización”, “discriminación” | ninguna | FA_22 | prototipo obligatorio; dividir si etiquetas <20 pt | sí | prototipo crítico |
| U07-DG-033/033B | 096–097 | Comparación Haas/precedencia y síntesis | 2 columnas + cadena final, 2–6 palabras | sin cruce; una flecha de formulación corregida | `Δt` solo como variable | FA_11/16 | evitar tachado decorativo; ejemplo y límite separados | sí | listo |
| U07-DG-034 | 099–102 | Pistas binaurales | cabeza, 2 oídos, fuente y 2 recorridos | flechas de llegada; rótulos ITD/ILD externos | diferencias de tiempo/nivel | FA_08/11 | rutas curvas fuera de la cabeza; L/R inequívocos | sí | listo |
| U07-DG-035 | 103, 133 | Geometría ITD máxima | 2 oídos, separación efectiva `d`, llegada extrema | líneas paralelas y cota `d`; sin ángulo | ninguna | FA_22 | declarar modelo sin difracción; no dibujar anatomía exacta | sí | listo |
| U07-DG-036/036B | 104–105, 133 | ITD anotada y cálculo | ecuación + 3 callouts; variante sustitución | líderes a valor absoluto, `d`, `c` | `abs(Δt_LR)≈d/c` | FA_09/10 | representar barras matemáticas en producción; 525 μs visible | sí; ecuación editable/SVG | listo |
| U07-DG-037 | 107 | Cono de confusión | cabeza + superficie cónica + 2 posiciones | líneas de superficie sin flechas; líderes a posiciones | ITD/ILD semejantes como rótulo | FA_22 | perspectiva simple; no ocultar cabeza ni rótulos | sí; SVG si 3D nativo no basta | prototipo crítico |
| U07-DG-038 | 108–109 | Movimiento e integración de pistas | 2 estados de cabeza + tabla de 4 pistas | flecha de giro; cambios etiquetados fuera del arco | ninguna | FA_19/16 | dos cuadros estáticos deben funcionar sin GIF | sí | listo |
| U07-DG-039 | 111 | Mezcla física→objetos perceptuales | 3 fuentes, L/R, mezcla, 2–3 objetos | convergencia a oídos y bifurcación perceptual | suma cualitativa | FA_12 | máximo 3 fuentes; dos niveles de lectura, sin cables cruzados | sí | prototipo crítico |
| U07-DG-040 | 113–114 | Segregación y agrupamiento | 2 dificultades + 5 pistas, 2–4 palabras | pistas convergen a agrupamiento; no red completa | ninguna | FA_03/05 | revelar 3+2 pistas; dividir si excede densidad | sí | prototipo |
| U07-DG-041 | 117 | Caso sistémico de aula | docente, 2 competidores, recinto, oyente, tarea | rutas físicas sólidas; relaciones perceptuales discontinuas | SNR/`T_60` solo como rótulos | FA_13 | no hacer “todo en uno”; usar capas y máximo 7 elementos | sí | prototipo crítico |
| U07-DG-042 | 119–120 | Síntesis acumulativa | 6 nodos: señal, ambiente, transferencia, procesamiento, tarea, respuesta | 5 conectores; ejemplos aparecen por clic | ninguna | FA_22/17 | construcción progresiva; versión final legible a vista completa | sí | prototipo crítico |
| U07-DG-043 | 121 | Puente U7→U8/U9/U10 | U7 central + 3 destinos, 2–6 palabras | 3 flechas con preguntas futuras | ninguna | FA_21 | U7 a izquierda/centro; destinos sin jerarquía clínica falsa | sí | listo |

## Validaciones obligatorias por recurso

Cada familia debe conservar `diagram_source.json`, lista de objetos/IDs, SVG/PNG de respaldo, preview en el layout, texto alternativo y `validation.json`. Gates:

1. cero desbordes, clipping, solapamientos y objetos fuera del canvas;
2. cero conectores, líderes o puntas sobre texto;
3. etiquetas separadas de líneas y destinos correctos;
4. tamaños mínimos respetados sin auto-shrink;
5. ecuaciones, signos, subíndices y unidades verificados contra LaTeX/guía;
6. lectura completa en miniatura de slide y a tamaño de proyección;
7. iteración `generar → renderizar → inspeccionar → corregir` hasta cero problemas críticos/mayores.

U07-DG-032, 037, 039, 041 y 042 se prototiparon y revisaron a tamaño completo. Los 55 recursos aprobados completaron el ciclo `generar → renderizar → inspeccionar → corregir → volver a renderizar` y cerraron con **0 problemas críticos y 0 problemas mayores**. No se insertaron en una presentación: esta entrega termina en assets autónomos y editables.
