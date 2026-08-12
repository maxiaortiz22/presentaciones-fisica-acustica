# Unidad 8 — Plan de gráficos propios

Versión de planificación · 2026-08-11

## Contrato común

Todos los recursos de este archivo se clasifican como `chart` antes de producirse y se derivan a `chart-generation`. Se diseñarán en el tamaño físico del layout previsto, con SVG como salida principal editable, PNG 2560×1440 de respaldo, script reproducible, datos o parámetros, README, caption, texto alternativo y `validation.json`.

- Etiquetas de ejes: 20 pt o más; ticks y leyendas: 18 pt o más; anotaciones: 22 pt o más.
- Fondo blanco o transparente; ejes en `FA_CARBON_900`; rejilla en `FA_GRIS_200`; curva principal en bordó o teal según semántica.
- Coma decimal en el visual; punto decimal solo en código y datos.
- Toda figura conceptual llevará dentro del canvas: **“esquema didáctico; no representa datos normativos ni un caso clínico”**.
- No se suavizarán puntos primarios ni se omitirán intervalos de confianza disponibles.
- Las variantes reutilizadas en varias slides conservarán la misma escala y solo cambiarán las anotaciones.

Estructura prevista:

```text
units/unit_08/assets/generated/charts/U08-CH-###/
├── u08_plot_###_nombre.py
├── data.csv o parameters.json
├── u08_fig_###_nombre.svg
├── u08_fig_###_nombre.png
├── README.md
└── validation.json
```

## Plan por gráfico

### U08-CH-001 — Serie temporal conceptual de TTS

- **Slides:** U08-022.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿qué información adicional aparece cuando se repite el umbral en varios tiempos postexposición?
- **Variables:** tiempo desde el fin de la exposición `Δt`; cambio de umbral `ΔL_T(f,Δt)` para una frecuencia declarada.
- **Unidades:** horas o minutos, elegidos de forma explícita; dB.
- **Escala:** lineal en ambos ejes; rango cualitativo sin marcas que parezcan normativas.
- **Datos/modelo:** cuatro o cinco puntos sintéticos monotónicos con variabilidad visual; no representan personas ni promedio poblacional.
- **Anotaciones:** “misma frecuencia y procedimiento”, “cada punto es una nueva medición”, “no predice recuperación individual”.
- **Salida:** SVG + PNG; variante sin números para el divisor U08-017 si hiciera falta.
- **Script:** `u08_plot_001_tts_timeline.py`; parámetros en JSON.
- **Validaciones:** eje temporal parte del fin de exposición; signo compatible con la ecuación; rótulo conceptual visible; ninguna lectura clínica posible.
- **Estado:** producido y aprobado el 2026-08-12; ver `assets/generated/charts/U08-CH-001/`.

### U08-CH-002 — Curvas cuantitativas pos-exposición

- **Slides:** U08-023, U08-111.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿cómo varía la recuperación medida cuando cambian frecuencia de prueba, exposición y persona/población?
- **Variables:** `Δt`; `ΔL_T(f,Δt)`; condición de exposición; frecuencia de prueba.
- **Unidades:** tiempo según estudio; dB; nivel y duración de exposición en caption.
- **Escala:** temporal lineal o logarítmica solo si la fuente lo justifica; eje vertical lineal.
- **Datos/modelo:** datos humanos primarios de una sola fuente o conjunto compatible. Candidatos: Klein y Mills (1981), DOI `10.1121/1.386955`, para una exposición estrechamente definida; Qian et al. (2026), DOI `10.1016/j.heares.2026.109578`, solo si se obtiene el texto/datos y se valida su pertinencia. La revisión de Ryan et al. (2016), DOI `10.1007/s10162-016-0564-7`, sirve para contexto, no como tabla de datos.
- **Anotaciones:** exposición, `n`, frecuencia, tiempos, variabilidad y aviso “no extrapolar a otras exposiciones”.
- **Salida:** SVG + PNG; ficha de metadatos para U08-111.
- **Script:** `u08_plot_002_recovery_curves.py`; `data.csv` transcrito de tabla o suplemento, nunca digitalizado sin control.
- **Validaciones:** cotejo doble con fuente; metadatos completos; intervalos/variabilidad; no combinar animales con humanos; no presentar una curva universal.
- **Estado:** **bloqueado**: fuente primaria y transcripción autorizada pendientes; se creó solo el registro documental, sin figura inventada.

### U08-CH-003 — Audiograma con escotadura compatible

- **Slides:** U08-030.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿cómo describir una forma audiométrica sin convertirla en causa?
- **Variables:** frecuencia `f`; nivel de audición `L_HL` por vía aérea en un caso ficticio.
- **Unidades:** Hz; dB HL.
- **Escala:** frecuencia logarítmica convencional; eje vertical lineal e invertido.
- **Datos/modelo:** umbrales ficticios múltiplos del paso audiométrico, con descenso y recuperación en altas frecuencias; sin paciente ni prevalencia.
- **Anotaciones:** región de la escotadura, “patrón compatible”, “la historia de exposición no está contenida en la curva”.
- **Salida:** SVG + PNG.
- **Script:** `u08_plot_003_notch_audiogram.py`; datos en CSV.
- **Validaciones:** símbolos y lateralidad según decisión docente; eje invertido; valores ficticios visibles; cero rótulos etiológicos.
- **Estado:** **bloqueado**: simbología audiométrica pendiente (OD-U08-19); se creó solo el registro documental, sin figura inventada.

### U08-CH-004 — Riesgo excedente por edad, nivel y duración de exposición

- **Slides:** U08-035, U08-036, U08-112.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿cómo cambia el riesgo excedente estimado al variar edad, nivel diario y duración ocupacional?
- **Variables:** edad; nivel diario promedio ponderado A; grupo de duración de exposición; exceso de riesgo de deterioro auditivo material.
- **Unidades:** años; dBA; años de exposición; porcentaje con IC 95 %.
- **Escala:** edad categórica 30/40/50/60; eje porcentual desde 0, sin truncamiento; máximo tres series de 80/85/90 dBA por panel.
- **Datos/modelo:** NIOSH, *Criteria for a Recommended Standard: Occupational Noise Exposure* (1998), tabla 3-3, modelo NIOSH 1997 para deterioro material definido sobre 1–2–3–4 kHz. Dos paneles: 5–10 años y más de 10 años.
- **Anotaciones:** nombre exacto del evento, intervalo de confianza, “estimación poblacional; no probabilidad individual” y contexto ocupacional estadounidense.
- **Salida:** SVG + PNG; tabla de respaldo para U08-112.
- **Script:** `u08_plot_004_excess_risk.py`; `data.csv` con valores e IC transcritos de tabla 3-3.
- **Validaciones:** doble cotejo con PDF NIOSH 98-126; porcentajes e IC completos; no mezclar con prevalencia; eje desde cero; leyenda directa; advertencia de modelo histórico.
- **Estado:** **bloqueado**: métrica/contexto NIOSH pendientes de aprobación docente; se creó solo el registro documental, sin figura inventada.

### U08-CH-005A — Construcción de ejes del audiograma

- **Slides:** U08-048.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿qué debe leerse antes de interpretar un punto del audiograma?
- **Variables:** frecuencia; nivel de audición.
- **Unidades:** Hz; dB HL.
- **Escala:** frecuencia logarítmica discreta; eje vertical lineal invertido.
- **Datos/modelo:** rejilla vacía, sin datos.
- **Anotaciones:** aumento de frecuencia hacia la derecha; aumento de nivel requerido hacia abajo; referencia HL.
- **Salida:** SVG + PNG en cuatro estados de revelado.
- **Script:** `u08_plot_005a_audiogram_axes.py`.
- **Validaciones:** ticks convencionales; orden y orientación explícitos; tipografía de aula; sin sugerir “peor” antes de definir la tarea.
- **Estado:** producido y aprobado el 2026-08-12; ver `assets/generated/charts/U08-CH-005A/`.

### U08-CH-005 — Audiograma conceptual por vías

- **Slides:** U08-049–050.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿qué patrón muestran los umbrales y qué agrega comparar vía aérea y ósea?
- **Variables:** `f`, `L_VA(f)`, `L_VO(f)`.
- **Unidades:** Hz; dB HL.
- **Escala:** frecuencia logarítmica; eje vertical lineal invertido.
- **Datos/modelo:** reconstrucción reproducible de las figuras TikZ 8.2–8.3 con valores ficticios, no captura del PDF.
- **Anotaciones:** símbolos de vía/lateralidad; tramo descriptivo; prohibición de inferencia etiológica.
- **Salida:** SVG + PNG; estados vía aérea sola y vías comparadas.
- **Script:** `u08_plot_005_audiogram_routes.py`; CSV.
- **Validaciones:** simbología aprobada; coincidencia de frecuencias; eje invertido; contraste no dependiente solo del color; no rotular enfermedad.
- **Estado:** **bloqueado**: simbología y rótulo del bloque pendientes (OD-U08-10/19); se creó solo el registro documental, sin figura inventada.

### U08-CH-006 — Curva de desempeño verbal

- **Slides:** U08-057–058.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿cómo cambia el porcentaje de respuestas correctas al variar el nivel de presentación bajo una tarea definida?
- **Variables:** nivel de presentación; porcentaje de palabras/ítems correctos.
- **Unidades:** dB HL o dB SL, una sola escala por versión; %.
- **Escala:** lineal; eje porcentual 0–100 %.
- **Datos/modelo:** puntos sintéticos declarados; no “curva normal”. Si se adopta una fuente, conservar material, idioma, lista, modo y criterio.
- **Anotaciones:** material, consigna, punto máximo observado y “no equivale a umbral tonal”.
- **Salida:** SVG + PNG; variante de actividad con un punto oculto.
- **Script:** `u08_plot_006_speech_performance.py`; parámetros/CSV.
- **Validaciones:** escala de nivel resuelta antes de producir; porcentaje dentro de 0–100; puntos visibles; no suavizar como función universal.
- **Estado:** **bloqueado**: escala dB HL o dB SL pendiente (OD-U08-15); se creó solo el registro documental, sin figura inventada.

### U08-CH-007 — Familia conceptual de timpanogramas

- **Slides:** U08-069–070.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿qué rasgos geométricos distinguen morfologías sin asignarles una etiología única?
- **Variables:** presión relativa del conducto; magnitud de inmitancia seleccionada.
- **Unidades:** daPa; mmho/mL/unidad elegida, sin alternarlas dentro de una misma versión.
- **Escala:** lineal; mismos límites para todas las curvas comparadas.
- **Datos/modelo:** funciones sintéticas parametrizadas que reconstruyen las morfologías del capítulo.
- **Anotaciones:** posición del pico, altura/anchura o ausencia de pico; rótulo conceptual.
- **Salida:** SVG + PNG; versión individual y familia de tres.
- **Script:** `u08_plot_007_tympanogram_family.py`; JSON de parámetros.
- **Validaciones:** eje y unidad definidos; misma escala; curvas no asociadas a una única patología; fuente técnica del montaje separada del modelo.
- **Estado:** **bloqueado**: unidad/profundidad timpanométrica pendiente (OD-U08-18/20); se creó solo el registro documental, sin figura inventada.

### U08-CH-008 — Forma de onda PEAT

- **Slides:** U08-078.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿cómo se representan amplitud y latencia en una respuesta promediada?
- **Variables:** tiempo; diferencia de potencial.
- **Unidades:** ms; µV.
- **Escala:** lineal; polaridad indicada.
- **Datos/modelo:** traza sintética suave construida como suma de componentes, sin latencias normativas; una traza pública solo se usaría como referencia visual, no como datos de “normalidad”.
- **Anotaciones:** componentes I–V como rótulos generales, ventana temporal, promedio y dependencia del protocolo.
- **Salida:** SVG + PNG.
- **Script:** `u08_plot_008_peat_waveform.py`; parámetros en JSON.
- **Validaciones:** amplitud y latencia no se presentan como universales; señal y ruido distinguibles; µV y ms correctos; polaridad explícita.
- **Estado:** producido y aprobado el 2026-08-12; ver `assets/generated/charts/U08-CH-008/`.

### U08-CH-009 — Entrada–salida de audífono

- **Slides:** U08-089.
- **Clasificación:** `gráfico cuantitativo` dentro de una composición futura de tipo `esquema mixto`.
- **Pregunta:** ¿por qué la salida no tiene que crecer uno a uno con la entrada?
- **Variables:** nivel de entrada y salida para una frecuencia/condición fija.
- **Unidades:** dB SPL en ambos ejes.
- **Escala:** lineal, mismos intervalos; diagonal 1:1 como referencia tenue.
- **Datos/modelo:** dos funciones sintéticas: ganancia lineal y compresión suave, sin representar producto ni ajuste real.
- **Anotaciones:** región lineal, compresión, condiciones fijas y “no predice beneficio”.
- **Salida:** SVG + PNG.
- **Script:** `u08_plot_009_hearing_aid_io.py`; parámetros JSON.
- **Validaciones:** monotonía; pendiente de compresión entre 0 y 1; ejes compatibles; no usar nombres comerciales ni prescripción.
- **Estado:** producido y aprobado el 2026-08-12; ver `assets/generated/charts/U08-CH-009/`.

### U08-CH-010 — OEA y piso de ruido

- **Slides:** U08-075.
- **Clasificación:** `gráfico cuantitativo`.
- **Pregunta:** ¿cómo se distingue una señal registrada del ruido bajo un protocolo?
- **Variables:** frecuencia; nivel registrado de emisión y ruido.
- **Unidades:** Hz/kHz; dB SPL.
- **Escala:** frecuencia lineal o logarítmica según protocolo didáctico; nivel lineal.
- **Datos/modelo:** dos trazas sintéticas, con algunos puntos por encima y otros próximos al ruido; no usar umbral “pasa/deriva”.
- **Anotaciones:** SNR local, repetibilidad/sonda y “criterio depende del protocolo”.
- **Salida:** SVG + PNG.
- **Script:** `u08_plot_010_oae_snr.py`; CSV sintético.
- **Validaciones:** `SNR=L_señal−L_ruido` calculado en script; cero corte clínico; rótulo conceptual; no extrapolar a audición global.
- **Estado:** producido y aprobado el 2026-08-12; ver `assets/generated/charts/U08-CH-010/`.

### U08-CH-011 — Ganancia por frecuencia del ejercicio

- **Slides:** U08-110.
- **Clasificación:** `gráfico cuantitativo` de respaldo.
- **Pregunta:** ¿cómo cambia `G(f)` cuando entrada y salida se comparan frecuencia por frecuencia?
- **Variables:** frecuencia; `L_entrada(f)`, `L_salida(f)` y `G(f)`.
- **Unidades:** Hz; dB SPL para niveles; dB para ganancia.
- **Escala:** frecuencia logarítmica discreta; ganancia lineal desde cero.
- **Datos/modelo:** datos ficticios del ejercicio, con cálculo reproducible.
- **Anotaciones:** máximo de ganancia y límite “no equivale a sonoridad ni comprensión”.
- **Salida:** tabla CSV + SVG/PNG.
- **Script:** `u08_plot_011_gain_exercise.py`.
- **Validaciones:** resta por frecuencia exacta; unidades; barras desde cero; correspondencia con solución futura.
- **Estado:** producido y aprobado el 2026-08-12; ver `assets/generated/charts/U08-CH-011/`.

## Gates antes de aprobación

1. El script termina sin advertencias y regenera todos los archivos desde cero.
2. Datos y parámetros coinciden con la fuente o con el rótulo de modelo sintético.
3. No hay textos cortados, objetos fuera del canvas ni colisiones.
4. Ejes, unidades, escala, referencia logarítmica y orientación son explícitos.
5. El gráfico se renderiza dentro del layout real y se entiende a vista de slide completa.
6. El SVG y PNG coinciden visualmente; el PNG mantiene resolución suficiente.
7. U08-CH-002 y U08-CH-004 no se producen como cuantitativos hasta cerrar sus condiciones documentales.

## Implementación y revisión — 2026-08-12

- **Producidos y aprobados:** U08-CH-001, U08-CH-005A, U08-CH-008, U08-CH-009, U08-CH-010, U08-CH-011.
- **Bloqueados sin figura:** U08-CH-002, U08-CH-003, U08-CH-004, U08-CH-005, U08-CH-006, U08-CH-007.
- Todos los producidos se clasificaron como **gráfico cuantitativo**, se exportaron en SVG y PNG 2560×1440 y conservan script, datos o parámetros, README, caption, texto alternativo y fuente de datos declarada.
- Los modelos sintéticos llevan el rótulo visible “esquema didáctico; no representa datos normativos ni un caso clínico”.
- La revisión completa está en `charts_review.md`.
