# Unidad 10 — Plan de gráficos cuantitativos

Versión de planificación · 2026-08-12

## Contrato de producción

Todos los recursos de este archivo se clasifican como `chart` o, cuando comparten slide con una explicación espacial, como capa `chart` de un visual `mixed`. Serán gráficos propios reproducibles con Python, NumPy, SciPy y Matplotlib. Las figuras del libro funcionan como fuente conceptual: no se copiarán como captura.

Cada script deberá guardar `data.csv` o `parameters.json`, `figure.svg`, `figure.png` y `README.md` en `units/unit_10/assets/generated/charts/<chart_id>/`. El SVG será el formato de inserción preferido; el PNG de respaldo tendrá como mínimo 2400 px de ancho y fondo compatible con el template.

Diseño a tamaño final: ejes ≥20 pt, ticks/leyenda ≥18 pt, anotaciones ≥22 pt. Se usará coma decimal en la salida docente, ejes con magnitud y unidad, y rótulo “señal sintética” cuando corresponda. Ningún gráfico contendrá valores normativos inventados.

## Especificación por gráfico

| chart_id | slides / clase | pregunta y mensaje | variables y unidades | escala | datos o modelo | anotaciones | salida y script | validaciones específicas | estado |
|---|---|---|---|---|---|---|---|---|---|
| U10-CH-001 | U10-012 · `chart` | ¿Cómo pueden dos realizaciones diferir y compartir propiedades? Dos trazas no idénticas pueden tener media y RMS comparables. | `t` (s); `p(t)` (mPa); media y `p_rms` (mPa). | x e y lineales; mismos límites. | Dos realizaciones gaussianas de 2 s, `f_s=2 kHz`, semillas fijas; normalización a media 0 y RMS 1 mPa. | Media y RMS por traza; “realización A/B”; “sintético”. | SVG + PNG; `u10_plot_001_realizaciones.py`. | Aserciones de media <10⁻¹² mPa y RMS 1±10⁻¹² mPa; mismo muestreo/ejes; sin insinuar distribución por apariencia. | aprobado · 2026-08-12 |
| U10-CH-002 | U10-015 · `chart` | ¿Cómo cambia la muestra mientras una estadística permanece? Estacionario no significa constante. | `t` (s); `p(t)` (mPa); media/RMS por ventana. | Lineal; dos ventanas iguales sobre una traza. | Señal estacionaria sintética de 8 s; `f_s=2 kHz`; semilla fija. | Ventanas A/B; valores redondeados; definición “aprox. estable”. | SVG + PNG; `u10_plot_002_ventanas_estacionarias.py`. | Mismo largo de ventana; diferencia de RMS dentro de tolerancia documentada; no rotular “idénticas”. | aprobado · 2026-08-12 |
| U10-CH-003 | U10-016 · `chart` | ¿Por qué una señal puede parecer estable en segundos y variar en minutos? La conclusión depende de la ventana. | Tiempo corto (s) y largo (min); nivel relativo (dB) o presión (mPa), no mezclarlos. | Vista general + zoom coordinado; ejes rotulados por separado. | Envolvente lenta sobre ruido estacionario; señal única, no dos datasets. | Corchete de zoom; ventanas corta/larga; “mismo registro”. | SVG + PNG; `u10_plot_003_escala_temporal.py`. | Verificar correspondencia exacta del zoom; declarar nivel relativo si no hay referencia SPL; evitar doble eje ambiguo. | aprobado · 2026-08-12 |
| U10-CH-004 | U10-017 · `chart` | ¿Cómo se reconocen continuo estable, fluctuante, intermitente e impulsivo? La forma temporal describe un rasgo, no categorías excluyentes. | `t` (s); `p(t)` (mPa). | Cuatro paneles lineales, mismos límites. | Reconstrucción del modelo de figura 10.1; reutilizar parámetros del script LaTeX U10 tras adaptar tipografía y canvas. | Etiquetas directas; ventanas/impulsos señalados; “sintético”. | SVG + PNG; `u10_plot_004_patrones_temporales.py`. | Reproducir semilla y parámetros; controlar que el impulso no se recorte; no usar amplitud como proxy de exposición. | aprobado · 2026-08-12 |
| U10-CH-005 | U10-024 · `chart` | ¿Qué conserva el histograma cuando media, RMS y varianza coinciden? La distribución contiene información adicional. | Tiempo (ms), `p(t)` (mPa); intervalos de presión (mPa), frecuencia relativa (adimensional). | 2×2 coordinado; lineal. | Gaussiana normalizada y secuencia ±1 mPa, 5000 muestras; semilla fija; base del script del libro. | Métricas compartidas; “A continua/B dos niveles”. | SVG + PNG; `u10_plot_005_mismo_rms_distinta_distribucion.py`. | Aserciones exactas de media, RMS y varianza; suma de frecuencias ≈1; dividir en dos slides si ticks <18 pt. | aprobado · 2026-08-12 |
| U10-CH-006 | U10-027 · `mixed` | ¿Qué aporta el dominio temporal y qué aporta el frecuencial? Son representaciones complementarias de la misma realización. | `t` (s), `p(t)` (mPa); `f` (Hz), PSD `S_pp` (Pa²/Hz). | Tiempo lineal; frecuencia log o lineal declarada; PSD logarítmica solo si mejora lectura. | Ruido banda finita con semilla fija; Welch con ventana, solapamiento y `nperseg` documentados. | Flecha “misma señal”; banda útil; método Welch en caption. | SVG + PNG; `u10_plot_006_tiempo_y_psd.py`. | Parseval aproximado entre potencia temporal e integral de PSD; unidades one-sided correctas; sin llamar “respuesta en frecuencia”. | aprobado · 2026-08-12 |
| U10-CH-007 | U10-031 · `chart` | ¿Qué significa PSD blanca constante por hertz? Igual densidad en cada intervalo de 1 Hz dentro de una banda finita. | `f` (Hz); `S_pp(f)` (Pa²/Hz). | x lineal 0–8 kHz; y lineal o log declarada. | Modelo analítico `S_pp=S_0` entre 125 y 8000 Hz; fuera de banda 0 o no mostrado. | Altura `S_0`; límites de banda; rectángulo Δf. | SVG + PNG; `u10_plot_007_psd_blanca.py`. | Integral analítica = `S_0 Δf`; no extender el modelo a infinito; unidades visibles. | aprobado · 2026-08-12 |
| U10-CH-008 | U10-032 · `chart` | ¿Qué ocurre al integrar ruido blanco por octavas? El contenido aumenta porque el ancho en Hz se duplica. | Banda central (Hz); contenido relativo por octava (adimensional o Pa² si se fija `S_0`). | x log por centros 125–8000 Hz; barras. | Integración analítica del modelo CH-007 en bandas de octava exactas. | Ancho de banda en Hz; razón 2:1 entre barras sucesivas. | SVG + PNG; `u10_plot_008_blanco_por_octavas.py`. | Centros y bordes coherentes; normalización explícita; comprobar duplicación numérica. | aprobado · 2026-08-12 |
| U10-CH-009 | U10-033 · `chart` | ¿Qué significa PSD rosa proporcional a `1/f`? La densidad cae con la frecuencia. | `f` (Hz); `S_pp(f)` (Pa²/Hz). | Ambos ejes log; banda 125–8000 Hz. | Modelo analítico `K/f` en banda finita. | Pendiente −1 en log–log; referencia `K`; límites. | SVG + PNG; `u10_plot_009_psd_rosa.py`. | Ajuste lineal log–log con pendiente −1±10⁻¹²; no equiparar pendiente de PSD con nivel total. | aprobado · 2026-08-12 |
| U10-CH-010 | U10-034/035 · `chart` y fallback multimedia | ¿Cómo se conectan PSD y contenido por octava en blanco y rosa? Rosa conserva contenido por octava; blanco no. | `f` (Hz), PSD normalizada; centros de octava, contenido relativo. | Dos paneles coordinados, x log. | CH-007–009 con misma banda y normalización. | Etiquetas directas blanco/rosa; barras por octava; sin leyenda distante. | SVG + PNG; `u10_plot_010_blanco_rosa_comparacion.py`. | Reutilizar exactamente modelos anteriores; comprobar áreas; producir versión estática autosuficiente para U10-035. | aprobado · 2026-08-12 |
| U10-CH-011 | U10-047/048 · `mixed` | ¿Dónde aparecen máximo, pico y equivalente sobre un mismo evento? Cada detector responde otra pregunta. | `t` (s); panel de `p(t)` (Pa o mPa) y panel de nivel (dB con referencia/ponderación declarada). | Lineal; dos paneles alineados. | Señal sintética variable con impulso; detector exponencial Fast/Slow solo si se especifican constantes; pico en presión. | `p_peak`, `L_max`, `L_eq,T`; intervalo `T`; cadena de detector. | SVG + PNG; `u10_plot_011_pico_maximo_equivalente.py`. | No ubicar tres magnitudes incompatibles sobre un solo eje; verificar detector, referencia y ponderación; control de clipping del impulso. | aprobado · 2026-08-12 |
| U10-CH-012 | U10-051/090 · `chart` | ¿Cómo se interpreta un percentil de excedencia? `L_N,T` es el nivel excedido N % del intervalo. | Tiempo excedido (%) o percentil `N`; nivel `L_A` (dB, ref. 20 µPa) para dataset sintético. | Curva monótona; x 0–100 %. | Distribución sintética de niveles con semilla fija; ordenamiento descendente. | Líneas en `L_10,T` y `L_90,T`; definición junto al eje. | SVG + PNG; `u10_plot_012_percentiles_excedencia.py`. | Monotonía; cálculo independiente por `numpy.percentile`; no llamar automáticamente “fondo” a `L_90`. | aprobado · 2026-08-12 |
| U10-CH-013 | U10-054 · `chart` | ¿Qué cambia al variar SNR con señal y ruido fijos? La detectabilidad visual cambia, no se predice inteligibilidad. | `t` (ms); `p(t)` (mPa); SNR (dB). | Tres paneles, mismos ejes. | Señal 240/430 Hz + misma realización de ruido; SNR +12, 0 y −6 dB; base figura 10.5. | SNR directo; “misma señal/mismo ruido”; “sintético”. | SVG + PNG; `u10_plot_013_snr_coordinado.py`. | Calcular SNR desde RMS y verificar ±0,05 dB; no renormalizar cada mezcla después; cero clipping. | aprobado · 2026-08-12 |
| U10-CH-014 | U10-078 · capa `chart` de `mixed` | ¿Cómo se distinguen temporalmente tránsito, climatización y portazos? Cada fuente exige otra ventana y descriptor. | `t` (s o min, explícito); nivel relativo (dB) o `p(t)` (mPa). | Tres minipaneles coordinados. | Señales sintéticas: envolvente lenta, continuo estable e impulsos; parámetros documentados. | Categoría, ventana sugerida y descriptor; “caso simulado”. | SVG + PNG; `u10_plot_014_caso_fuentes.py`. | Misma semántica cromática que DG-050–053; no presentar como medición real; escalas compatibles o advertidas. | aprobado · 2026-08-12 |
| U10-CH-015 | U10-011 · capa `chart` de `mixed` | ¿Por qué una sinusoide y una realización aleatoria se describen de manera distinta? Una se predice muestra a muestra; la otra por propiedades. | `t` (s); amplitud normalizada (adimensional) o `p(t)` (mPa), una sola opción. | Dos paneles lineales con los mismos límites. | Sinusoide de frecuencia/amplitud conocidas y ruido gaussiano banda limitada; semilla fija. | “modelo conocido” / “realización”; pregunta de predicción al instante siguiente. | SVG + PNG; `u10_plot_015_determinista_aleatorio.py`. | Igual RMS si se usa como contraste; no afirmar que aleatorio carece de estructura; ejes y unidades comunes. | aprobado · 2026-08-12 |
| U10-CH-016 | U10-092 · `chart` bloqueado | ¿Cómo varía un límite o criterio de exposición con tiempo/fuente? Solo podrá responderse para un documento, jurisdicción y descriptor definidos. | A definir por la fuente validada; no fijar ejes ni unidades todavía. | A definir. | Norma oficial seleccionada; no combinar ISO, OMS, NIOSH y legislación argentina en una curva única. | Edición, jurisdicción, población, descriptor y fecha de vigencia visibles. | SVG + PNG; `u10_plot_016_criterio_normativo.py` solo después de aprobación. | Verificación punto por punto contra la fuente; revisión normativa independiente; cero interpolación no autorizada. | `blocked-source` |

## Familias y reutilización

- **Tiempo:** CH-001–005 y CH-015 comparten semilla/estilo y una utilidad común para cálculo de media, RMS y varianza.
- **Espectro:** CH-006–010 comparten banda 125–8000 Hz, definiciones de PSD y normalización; no duplicar datos manualmente.
- **Descriptores:** CH-011–013 comparten convención de nivel, referencia y rotulación de detector/intervalo.
- **Caso:** CH-014 usa la escena y colores de DG-050–055.

## Validaciones globales

1. Tests de unidades, normalización, Parseval, SNR y percentiles ejecutados por script.
2. SVG inspeccionado para texto cortado y viewBox correcto; PNG ≥2400 px.
3. Render de prueba en el layout real de la slide; cero solapamientos y fuentes mínimas cumplidas.
4. Caption, alt text, fuente/modelo, semilla y parámetros guardados en README.
5. Revisión visual independiente de CH-005, CH-010, CH-011 y CH-013 antes de aprobar.

No se generaron gráficos en esta fase.


## Clasificación obligatoria y resultado de producción

Registro cerrado el 2026-08-12. La clasificación se fijó antes de ejecutar cada generador.

| ID | Clasificación obligatoria | Resultado | Carpeta |
|---|---|---|---|
| U10-CH-001 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-001/` |
| U10-CH-002 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-002/` |
| U10-CH-003 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-003/` |
| U10-CH-004 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-004/` |
| U10-CH-005 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-005/` |
| U10-CH-006 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-006/` |
| U10-CH-007 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-007/` |
| U10-CH-008 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-008/` |
| U10-CH-009 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-009/` |
| U10-CH-010 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-010/` |
| U10-CH-011 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-011/` |
| U10-CH-012 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-012/` |
| U10-CH-013 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-013/` |
| U10-CH-014 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-014/` |
| U10-CH-015 | gráfico cuantitativo | aprobado | `assets/generated/charts/U10-CH-015/` |
| U10-CH-016 | gráfico cuantitativo | bloqueado por fuente normativa | no generado |
