# Unidad 4 — Plan de gráficos cuantitativos

## Clasificación previa a producción

De acuerdo con la taxonomía obligatoria, `U04-CH-001` a `U04-CH-015` se clasifican como **gráfico cuantitativo**: todos representan variables, modelos o datos mediante ejes y escalas. Las variantes con callouts o revelado siguen siendo gráficos cuantitativos; sus anotaciones no cambian la clase del recurso. Se implementan con `chart-generation`.

## Contrato común

Todos los gráficos se diseñarán en el tamaño físico del layout, con fondo transparente o blanco, tipografía Calibri, rótulos en español y coma decimal en la salida. Los scripts usarán punto decimal internamente. Salvo indicación contraria, se exportarán SVG editable y PNG de respaldo a 200–300 ppp, junto con script, datos y README.

Mínimos: anotaciones 22 pt, ejes 20 pt, ticks/leyendas 18 pt. La paleta mantiene `p` en teal, `u` en bordó, intensidad/resultado en ocre y referencias en gris. Color nunca será el único código.

| chart_id | slides | clase | pregunta y mensaje | variables, unidades y escala | datos/modelo y anotaciones | salida y script | validaciones específicas |
|---|---|---|---|---|---|---|---|
| U04-CH-001 | 025–026 | chart | ¿Cómo se separan presión total y acústica? La variación acústica es pequeña alrededor de `p_0`. | `t` en ms; `p_total` en Pa y `p` en Pa. Dos paneles alineados, escala lineal; no usar un eje quebrado ambiguo. | Modelo sinusoidal ilustrativo: `p_0=101325 Pa`, amplitud `0,20 Pa`, 500 Hz. Anotar equilibrio, sobrepresión y rarefacción; declarar “valores ilustrativos”. | `u04_plot_001_presion_total_acustica.py`; SVG multipanel y variante simple. | Confirmar que no parece presión total negativa; escalas y unidades visibles; mismo cero temporal. |
| U04-CH-002 | 036 | chart | ¿Cómo se relacionan `p(t)`, `u(t)` e `i(t)`? En onda progresiva ideal, `p` y `u` están en fase y el producto es no negativo. | `t/T` adimensional, 0–2; amplitud normalizada `(1)` en tres ejes coordinados. | `p=sin(2πt/T)`, `u=sin(2πt/T)`, `i=sin²(2πt/T)`; anotar intervalos con signos dobles negativos. | `u04_plot_002_presion_velocidad_intensidad.py`; SVG 3 paneles. | Verificar fase, frecuencia doble visual de `i`, normalización explícita y ausencia de leyenda redundante. |
| U04-CH-003 | 044–050 | chart/mixed | ¿Qué mide cada descriptor? Los marcadores responden preguntas diferentes sobre una misma señal. | `t` en ms, 0–40; `p(t)` en Pa. Escala lineal fija para todas las variantes. | Señal sintética asimétrica con componente continua; marcar `t_1`, `p_max`, `p_min`, `p_pp` y media. Revelado progresivo sin mover ejes. | `u04_plot_003_descriptores_temporales.py`; familia de 6 SVG. | Recalcular todos los descriptores; comprobar que `p_pp≠2p_pico` en el ejemplo; idénticos límites entre slides. |
| U04-CH-004 | 048 | chart | ¿Por qué media cero no significa señal nula? Dos señales con igual media pueden tener RMS diferente. | `t` en ms, 0–20; `p` en Pa, −0,20 a 0,20. | Seno de 100 Hz y línea `p=0`; anotar media `0 Pa`, RMS `0,141 Pa` vs `0 Pa`. | `u04_plot_004_media_cero.py`; SVG comparativo. | Media numérica cercana a cero; RMS verificado; no confundir áreas por recorte de período. |
| U04-CH-005 | 053–056 | chart | ¿Cómo se construye RMS? Cuadrar elimina signo, promediar resume y la raíz recupera la unidad. | `t/T`, 0–2; `p` en Pa, `p²` en Pa²; escalas lineales. | Sinusoide pico `0,20 Pa`; `p_rms=0,1414 Pa`; cuatro paneles con áreas/rectas de media. | `u04_plot_005_construccion_rms.py`; SVG completo y 4 pasos. | Control analítico `p_rms=pico/√2`; unidades diferentes en el panel cuadrático; no llamar promedio a RMS. |
| U04-CH-006 | 057, 109 | chart | ¿Pueden dos señales distintas tener igual RMS? Igual tamaño eficaz no implica igual forma ni contenido frecuencial. | `t` en ms, 0–20; `p` en Pa; escala idéntica. | Seno de 200 Hz y suma 100+300+500 Hz, ambas normalizadas a `0,20 Pa RMS`; espectro solo en U04-109 como silueta anticipatoria. | `u04_plot_006_igual_rms_forma_distinta.py`; 2 SVG. | RMS relativo <0,1 % de diferencia; declarar señal sintética; evitar desarrollar Fourier. |
| U04-CH-007 | 064 | chart | ¿Cómo comprime el nivel el rango de presión? Cada década de presión agrega 20 dB. | Eje de `p_rms` logarítmico, 20 µPa–20 Pa; eje `L_p` lineal, 0–120 dB SPL. | `L_p=20log10(p/p_ref)`, `p_ref=20 µPa`; anclas 0, 20, 40, 60, 80, 100 y 120 dB. | `u04_plot_007_presion_nivel.py`; SVG horizontal y vertical. | Conversión exacta de anclas; referencia visible; no añadir umbrales perceptuales universales. |
| U04-CH-008 | 070, 072–075, 122 | chart/mixed | ¿Cómo cambia la suma coherente con la fase? El término de fase determina la resultante. | `t/T`, 0–2; `p` en Pa o normalizado `(1)` según variante, siempre declarado. | Senos iguales para `φ=0`, `π/2`, `π`; curvas fuente y suma, con valores pico/RMS anotados. | `u04_plot_008_suma_coherente.py`; familia de 5 SVG y frames para animación. | Verificar `+6,02 dB`, cancelación ideal y caso `π/2`; misma escala entre casos. |
| U04-CH-009 | 076–080 | chart/mixed | ¿Qué cambia cuando las señales no están correlacionadas? Se suman cuadrados RMS, no niveles aritméticamente. | Tiempo en ms para zoom y ventana total 1 s; `p` en Pa; panel de nivel en dB SPL. | Dos ruidos gaussianos independientes con semilla fija y `0,20 Pa RMS`; suma, correlación muestral y `+3,01 dB` esperado. | `u04_plot_009_suma_no_correlacionada.py`; SVG y CSV de métricas. | Semilla registrada; correlación absoluta <0,02; RMS y nivel dentro de tolerancia; ventana declarada. |
| U04-CH-010 | 084, 086, 117 | chart/mixed | ¿Cómo decrece la intensidad según la geometría? El crecimiento del área fija `r⁰`, `r⁻¹` o `r⁻²`. | `r/r_0` adimensional, 1–8; `I/I_0` adimensional. Escala log–log para pendientes y variante lineal para duplicaciones. | Modelos ideales plano, cilíndrico y esférico; anotar `r`, `2r`, `4r`, `−3,01` y `−6,02 dB`. | `u04_plot_010_geometrias_decaimiento.py`; 2 SVG. | Pendientes verificadas; normalización visible; no presentar como datos experimentales. |
| U04-CH-011 | 095–097 | chart/mixed | ¿Cómo cambia el nivel con distancia en campo esférico? Cada duplicación resta 6,02 dB. | `r/r_0`, 1–8, eje log base 2; `ΔL_p` en dB, 0 a −18,1. | `ΔL_p=20log10(r_0/r)`; puntos 1, 2, 4 y 8; destacar caso 1→4 m. | `u04_plot_011_nivel_distancia.py`; SVG. | Signo y anclas exactos; eje log señalado; condiciones del modelo en caption. |
| U04-CH-012 | 102 | chart | ¿Cómo cambia la directividad real con frecuencia? Un único patrón no describe toda la fuente. | Ángulo en grados, nivel relativo en dB; polar, normalizado a 0 dB en eje. Frecuencias seleccionadas y separables. | Datos CC BY 4.0 del dataset Aalto/Zenodo DOI 10.5281/zenodo.10255555; seleccionar un altavoz y 250 Hz, 1 kHz, 4 kHz después de validar disponibilidad. | `u04_plot_012_patron_polar_datos_abiertos.py`; datos derivados CSV, SVG polar y README de atribución. | No descargar 400+ MB sin aprobación; verificar licencia, orientación, normalización y metadatos; máximo 3 curvas. |
| U04-CH-013 | 113 | chart | ¿Cómo depende la reflexión del cociente de impedancias? El signo de `R_p` y la fracción `R_I` informan cosas distintas. | `η=Z_2/Z_1` adimensional, 0,1–10 log; `R_p` −1–1; `R_I` 0–1. | `R_p=(η−1)/(η+1)`, `R_I=R_p²`; anotar `η=1` y extremos. | `u04_plot_013_reflexion_impedancias.py`; SVG de respaldo. | Simetría energética bajo `η↔1/η`; unidades adimensionales; no confundir signo con energía negativa. |
| U04-CH-014 | 121 | chart | ¿Cuánto agrega una segunda fuente según la diferencia de niveles? La contribución cae al crecer `ΔL`. | Diferencia `ΔL` en dB, 0–20; incremento total en dB, 0–3,01. | `Δ=10log10(1+10^(−ΔL/10))`; anotar 0, 3, 6, 10 y 20 dB. | `u04_plot_014_incremento_suma_niveles.py`; SVG. | Valores exactos y eje no truncado de forma engañosa; condición no correlacionada visible. |
| U04-CH-015 | 122 | chart | ¿Qué aspecto tiene la suma en cuadratura? La resultante no es máximo ni cancelación. | Igual que CH-008. | Derivación directa de CH-008 para `φ=π/2`; anotar amplitud resultante y nivel. | Reutiliza `u04_plot_008_suma_coherente.py`; SVG de respaldo. | Coherencia con el caso de la slide 072 y con la solución algebraica. |

## Secuencia de producción

1. Prototipos prioritarios: CH-002, CH-003, CH-005 y CH-007.
2. Familias de suma: CH-008 y CH-009.
3. Geometría/distancia: CH-010 y CH-011.
4. Directividad con datos externos: CH-012, solo después de aprobar la descarga/procesamiento.
5. Gráficos de respaldo: CH-013–015.

Cada figura pasará por `generar → simular inserción → renderizar → inspeccionar → corregir → renderizar`. No se aprobará por ejecución exitosa del script únicamente.

## Estado de producción — 2026-07-31

| recursos | estado | resultado |
|---|---|---|
| U04-CH-001–011 | aprobado | Scripts reproducibles, datos, README, SVG y PNG generados. |
| U04-CH-012 | pendiente de aprobación | No se descargaron 326–466 MB del dataset Zenodo; no se fabricaron datos sustitutos. |
| U04-CH-013–015 | aprobado | Scripts reproducibles, datos, README, SVG y PNG generados. |

Se aprobaron **14 familias y 32 variantes estáticas**. La revisión completa está en `charts_review.md`; el resumen verificable está en `visual_validation_summary.json`.
