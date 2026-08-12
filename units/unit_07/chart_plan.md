# Unidad 7 — Plan de gráficos propios

Versión implementada v01 · 2026-08-11

## Resultado de implementación

| asset_id | clasificación obligatoria | estado v01 | salida principal |
|---|---|---|---|
| U07-CH-001 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-001/` |
| U07-CH-002A | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-002A/` |
| U07-CH-002B | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-002B/` |
| U07-CH-003 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-003/` |
| U07-CH-004 | gráfico cuantitativo | bloqueado | requiere datos normativos/licencia; alternativa U07-DG-011 |
| U07-CH-005 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-005/` |
| U07-CH-006 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-006/` |
| U07-CH-007 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-007/` |
| U07-CH-008 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-008/` |
| U07-CH-009 | gráfico cuantitativo | aprobado | `assets/generated/charts/U07-CH-009/` |
| U07-CH-010 | gráfico cuantitativo | bloqueado | requiere voz/corpus aprobado y pipeline de audio |

Se produjeron los nueve recursos aprobados con script, datos/parametrización, SVG, PNG 2560×1440, README, caption, texto alternativo, fuente/modelo y validación. El detalle de QA está en `charts_review.md`.

## Contrato común

Todos los recursos de este archivo se clasifican como **gráfico cuantitativo** antes de producirse y se derivan a `chart-generation`. Se diseñan en el tamaño físico del layout previsto, con SVG principal y PNG 2560×1440 de respaldo. Etiquetas de ejes ≥20 pt, ticks/leyenda ≥18 pt y anotaciones ≥22 pt. Los gráficos conceptuales llevan dentro del canvas: **“modelo didáctico; no representa datos normativos/experimentales”**.

Cada familia tendrá:

```text
units/unit_07/assets/generated/charts/U07-CH-###/
├── u07_plot_###_nombre.py
├── data.csv o parameters.json
├── u07_fig_###_nombre.svg
├── u07_fig_###_nombre.png
├── README.md
└── validation.json
```

## Plan por gráfico

### U07-CH-001 — Curva psicométrica didáctica

- **Slides:** U07-008, U07-014.
- **Clasificación:** `chart`.
- **Pregunta:** ¿por qué un criterio selecciona un punto de una transición gradual?
- **Variables:** nivel relativo al punto medio `L-L_50`; proporción de detecciones `P`.
- **Unidades:** dB relativos y porcentaje.
- **Escala/rango:** x lineal, −15 a +15 dB; y lineal, 0–100 %.
- **Datos/modelo:** función logística sintética `P=1/(1+exp(-(L-L_50)/s))`, con `s=3 dB`; no son datos humanos.
- **Anotaciones:** línea de 50 %, punto `L_50`, zonas “poco frecuente”/“frecuente” y rótulo de modelo didáctico.
- **Salida:** SVG + PNG; variante sin ejes para divisor U07-008.
- **Script:** `u07_plot_001_curva_psicometrica.py` con parámetros en JSON.
- **Validaciones:** monotonicidad; `P(L_50)=0,5`; límites 0–1; no rotular `L_50` como umbral universal; alternativa textual.
- **Estado:** listo para producir.

### U07-CH-002A/B — Umbral y campo audible condicionados

- **Slides:** U07-015–017.
- **Clasificación:** `chart` y `mixed` en U07-017.
- **Pregunta:** ¿cómo cambia el umbral con frecuencia y por qué la región de mayor sensibilidad está más abajo?
- **Variables:** frecuencia `f`; nivel de presión sonora de umbral `L_p,umbral(f)`.
- **Unidades:** Hz y dB SPL solo si se autoriza una fuente cuantitativa; en la opción base, ambos ejes se rotulan cualitativos.
- **Escala/rango:** frecuencia logarítmica; nivel lineal.
- **Datos/modelo:** reconstrucción del esquema TikZ `umbral-campo-audible.tex`; sin puntos normativos. No mostrar límite superior cuantitativo.
- **Anotaciones:** región de máxima sensibilidad; umbral; “niveles elevados: no explorar didácticamente”; `0 dB SPL` como referencia, no frontera perceptual.
- **Salida:** SVG/PNG y tres variantes A, B y error frecuente.
- **Script:** `u07_plot_002_umbral_campo.py`, con curvas Bézier o funciones sintéticas parametrizadas y marca explícita de esquema.
- **Validaciones:** eje log identificado; ninguna lectura numérica posible en versión conceptual; no atribuir a ISO 226; coherencia visual entre variantes.
- **Estado:** listo como conceptual; cuantitativo bloqueado junto con U07-CH-004.

### U07-CH-003 — Transferencia campo–tímpano dependiente de frecuencia

- **Slides:** U07-026.
- **Clasificación:** `mixed` (gráfico propio + recordatorio diagramático).
- **Pregunta:** ¿por qué una única cifra de “ganancia del CAE” es insuficiente?
- **Variables:** frecuencia `f`; diferencia `G_CT(f)`.
- **Unidades:** Hz y dB.
- **Escala/rango:** frecuencia logarítmica; eje vertical lineal sin valores si no se adopta una fuente de datos.
- **Datos/modelo:** curva conceptual suave con varias regiones, derivada del argumento del libro; no usar como respuesta en frecuencia individual.
- **Anotaciones:** “depende de frecuencia, dirección, geometría y punto”; enlace con U07-DG-008/009.
- **Salida:** SVG/PNG; preferencia por mini gráfico dentro del layout 40/60.
- **Script:** `u07_plot_003_transferencia_conceptual.py`.
- **Validaciones:** rótulo no normativo; no mostrar picos numéricos ni prometer una resonancia fija; eje y claramente identificado como diferencia.
- **Estado:** listo como conceptual; reemplazable por datos trazables si se aprueban.

### U07-CH-004 — Familia de curvas isofónicas

- **Slides:** U07-029–030, U07-038 y U07-123.
- **Clasificación:** `chart` o `mixed` en U07-038.
- **Pregunta:** ¿qué nivel necesita cada frecuencia para una sonoridad igual a la referencia?
- **Variables:** frecuencia `f`, nivel `L_p`, nivel de sonoridad `L_N`.
- **Unidades:** Hz, dB SPL y fon.
- **Escala/rango:** frecuencia logarítmica 20 Hz–12,5 kHz; nivel lineal, rango según datos autorizados.
- **Datos/modelo:** rama A — datos de ISO 226:2023 con autorización y registro de condiciones; rama B — curva esquemática sin valores, basada en `construccion-isofonica.tex`.
- **Anotaciones:** referencia 1 kHz, dos lecturas guiadas, condiciones ISO visibles y aviso de esquema cuando corresponda.
- **Salida:** SVG/PNG; variantes de explicación, ejercicio y metadatos.
- **Script:** `u07_plot_004_isofonicas.py`; debe rechazar ejecución normativa si falta `data_source.json` con edición/licencia.
- **Validaciones:** edición 2023; campo libre, incidencia frontal, tonos puros, escucha binaural y población 18–25 visibles si se usa ISO; comparación numérica contra tabla fuente; no digitalizar el PDF del libro.
- **Estado:** **bloqueado para datos normativos**; aprobada la alternativa conceptual U07-DG-011.

### U07-CH-005 — Fundamental ausente

- **Slides:** U07-036.
- **Clasificación:** `mixed` (espectros + audio propio).
- **Pregunta:** ¿puede mantenerse la periodicidad/pitch aunque falte la línea en `f_0`?
- **Variables:** frecuencia y amplitud relativa por componente.
- **Unidades:** Hz y dB relativos.
- **Escala/rango:** x lineal 0–2 kHz; y lineal en dB relativos, −40 a 0 dB.
- **Datos/modelo:** `f_0=200 Hz`, armónicos 1–8 con caída declarada; panel B elimina el primer armónico y conserva 2–8.
- **Anotaciones:** línea esperada en `f_0`, espaciamiento armónico y “no aparece una nueva componente física”.
- **Salida:** SVG/PNG + CSV de líneas espectrales; audio U07-MEDIA-002 usa los mismos parámetros.
- **Script:** `u07_plot_005_fundamental_ausente.py`.
- **Validaciones:** FFT y síntesis coinciden; niveles pico/RMS normalizados y declarados; sin clipping; misma duración/ventana; no inferir respuesta individual.
- **Estado:** listo para producir.

### U07-CH-006 — Relación fones–sones

- **Slides:** U07-050 y apoyo de U07-051.
- **Clasificación:** `chart`.
- **Pregunta:** ¿cómo crece la sonoridad en sones cuando aumenta `L_N`?
- **Variables:** `L_N` y `N_son`.
- **Unidades:** fon y son.
- **Escala/rango:** ambos ejes lineales; 40–80 fon y 0–16 son.
- **Datos/modelo:** `N_son=2^((L_N-40 fon)/(10 fon)) son`, solo para `L_N≥40 fon` en el modelo introductorio.
- **Anotaciones:** puntos 40/1, 50/2, 60/4, 70/8, 80/16; “+10 fon → duplica `N_son`”.
- **Salida:** SVG/PNG + `data.csv` calculado.
- **Script:** `u07_plot_006_fones_sones.py`.
- **Validaciones:** exponente adimensional; puntos exactos; unidad singular/plural coherente; no rotular el eje x como dB SPL.
- **Estado:** listo para producir.

### U07-CH-007 — Patrón de enmascaramiento

- **Slides:** U07-060–061.
- **Clasificación:** `chart`.
- **Pregunta:** ¿cómo cambia la elevación del umbral al separar objetivo y enmascarador en frecuencia?
- **Variables:** frecuencia objetivo relativa a `f_m`; elevación `M(f_obj)`.
- **Unidades:** octavas relativas o Hz y dB.
- **Escala/rango:** opción base x en octavas relativas −2 a +2; y 0–30 dB de modelo sintético.
- **Datos/modelo:** función pedagógica asimétrica declarada, con pendientes diferentes a cada lado; no datos experimentales. Si se recuperan datos del libro, reemplazar el CSV y citar condiciones.
- **Anotaciones:** posición del enmascarador, puntos A/B, umbral en quietud y aviso de modelo.
- **Salida:** SVG/PNG; variantes explicación y ejercicio.
- **Script:** `u07_plot_007_patron_enmascaramiento.py`.
- **Validaciones:** `M≥0` en el rango; asimetría no presentada como ley universal; misma referencia de nivel; f_obj/f_m inequívocos.
- **Estado:** listo como modelo sintético; datos empíricos pendientes.

### U07-CH-008 — Filtro y ERB por igualdad de área

- **Slides:** U07-064, U07-125–127.
- **Clasificación:** `mixed` en U07-064 y respaldo; curva cuantitativa conceptual.
- **Pregunta:** ¿qué significa que un rectángulo tenga la misma altura y área que la respuesta del filtro?
- **Variables:** frecuencia relativa a `f_c`; respuesta normalizada `W/W_max`.
- **Unidades:** Hz o frecuencia normalizada; eje vertical adimensional.
- **Escala/rango:** x lineal; y 0–1.
- **Datos/modelo:** respuesta gaussiana normalizada elegida solo para ilustrar área; ancho del rectángulo calculado por integración numérica. La fórmula Glasberg–Moore se reserva para U07-125/126.
- **Anotaciones:** `f_c`, área sombreada, rectángulo equivalente y `ERB`.
- **Salida:** SVG/PNG + CSV de curva/rectángulo.
- **Script:** `u07_plot_008_erb_area.py` y variante `u07_plot_008b_erb_formula.py`.
- **Validaciones:** áreas coinciden con tolerancia <0,5 %; eje vertical normalizado; no llamar a la gaussiana “filtro humano medido”; fórmula con `f_c` y Hz correctos.
- **Estado:** listo para figura de área; fórmula espera cierre OD-U07-04.

### U07-CH-009 — Decaimiento reverberante y `T_60`

- **Slides:** U07-083–084 y U07-129.
- **Clasificación:** `mixed`/`chart`.
- **Pregunta:** ¿qué mide `T_60` y por qué no significa “tiempo hasta silencio”?
- **Variables:** tiempo `t`; nivel relativo del decaimiento `L_rel`.
- **Unidades:** s y dB.
- **Escala/rango:** ambos lineales; ejemplo sintético 0–1,5 s y 0 a −70 dB.
- **Datos/modelo:** decaimiento log-lineal ideal con `T_60=1,2 s`; variante con tramo −5 a −35 dB para explicar extrapolación `T_30` en respaldo.
- **Anotaciones:** inicio, −60 dB, `T_60`, piso de ruido conceptual y tramo de ajuste.
- **Salida:** SVG/PNG y datos sintéticos.
- **Script:** `u07_plot_009_decaimiento_t60.py`.
- **Validaciones:** pendiente `−60/T_60 dB/s`; unidades; no introducir Sabine; variante de extrapolación correctamente multiplicada.
- **Estado:** listo para producir.

### U07-CH-010 — Igual SNR, distinta estructura

- **Slides:** U07-082–085.
- **Clasificación:** `mixed`.
- **Pregunta:** ¿cómo pueden dos señales compartir SNR global y conservar distinta información espectrotemporal?
- **Variables:** tiempo, frecuencia, nivel espectral relativo y SNR calculada.
- **Unidades:** s, Hz, dB relativos y dB para SNR.
- **Escala/rango:** espectrogramas con la misma escala de color y duración; rangos según grabación aprobada.
- **Datos/modelo:** frase propia U07-MEDIA-005; condición A con ruido estacionario, condición B con reverberación/ruido modulado; ambas ajustadas a la misma SNR RMS (+8 dB en el ejemplo) bajo idéntica ventana.
- **Anotaciones:** SNR verificada, transiciones cubiertas y colas temporales; no estimar inteligibilidad.
- **Salida:** SVG/PNG, WAV intermedios y CSV/JSON de métricas.
- **Script:** `u07_plot_010_igual_snr.py`, compartido con el pipeline de audio.
- **Validaciones:** SNR calculada dentro de ±0,1 dB; misma ponderación, banda, posición simulada e intervalo; sin clipping; escalas idénticas; autorización de la voz.
- **Estado:** condicionado a grabación propia aprobada.

## Orden de producción

1. CH-001, CH-005, CH-006 y CH-009: modelos cerrados y alto valor pedagógico.
2. CH-002, CH-003, CH-007 y CH-008: conceptuales con rótulos de alcance.
3. CH-010: después de aprobar el corpus/voz y el plan de audio.
4. CH-004: solo tras resolver licencia/datos; mientras tanto usar U07-DG-011.

## Validación consolidada

Cada script terminó sin errores, regeneró los archivos previstos y produjo un `validation.json` con parámetros, fuente, checks numéricos y resultado visual. Los nueve gráficos aprobados se revisaron individualmente y en el canvas 16:9 real; el cierre registra **0 problemas críticos y 0 problemas mayores**. U07-CH-004 y U07-CH-010 permanecen bloqueados por las dependencias indicadas y no se fabricaron datos sustitutos.
