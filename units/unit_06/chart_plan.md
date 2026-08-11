
# Unidad 6 — Plan de gráficos propios

## Contrato común

Todos los recursos se clasifican como **gráfico cuantitativo** antes de producirse y se derivan a `chart-generation`. Se diseñan en el tamaño físico final del layout, con SVG principal y PNG 2560×1440 de respaldo. Ejes ≥20 pt, ticks/leyenda ≥18 pt, anotaciones ≥22 pt. Cuando el recurso es conceptual se imprime **“esquema conceptual; respuesta normalizada”** y el script conserva todos los parámetros.

Cada familia tendrá, cuando comience la producción:

```text
units/unit_06/assets/generated/charts/U06-CH-*/
├── u06_plot_*.py
├── data.csv o parameters.json
├── figure.svg
├── figure.png
├── README.md
└── validation.md
```

## Familias planificadas

| chart_id | slides | clasificación | pregunta que responde | variables | unidades | escala | datos o modelo | anotaciones previstas | salida y script | validaciones | fuente | estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U06-CH-001 | U06-064, 066–067, 071 | gráfico cuantitativo | ¿Cómo cambia el lugar de máxima respuesta con la frecuencia y por qué no es una “celda” aislada? | posición coclear `s/L`; respuesta relativa; tres condiciones de frecuencia | `s/L` adimensional; respuesta normalizada | x lineal 0–1, orientación base→ápex; y lineal 0–1 | Familia paramétrica de envolventes asimétricas, con máximos didácticos y solapamiento; no datos anatómicos | “altas / medias / bajas”, base, ápex, máximo y ancho; variante de actividad sin etiquetas | SVG/PNG + CSV de curvas; `u06_plot_001_tonotopia_normalizada.py` | máximos en orden correcto; curvas dentro de [0,1]; orientación idéntica en todas las slides; ningún valor se presenta como mapeo humano real | TEX 6.7.2, fig. 6.6a; Fettiplace 2017; Caprara y Peng 2022 | approved |
| U06-CH-002A | U06-068, 071 | gráfico cuantitativo | ¿Qué caracteriza la respuesta coclear a una señal débil? | `s/L`; respuesta relativa; región característica | adimensional / normalizada | mismos ejes que CH-001/002B | Curva conceptual estrecha derivada de un modelo paramétrico documentado | pico, región más selectiva y rótulo “nivel débil; conceptual” | SVG/PNG + parameters.json; `u06_plot_002_nivel_y_extension.py --condition weak` | misma frecuencia característica que CH-002B; escala compartida; no normalizar por separado si se compara altura | TEX 6.7.3, fig. 6.6b; referencias del capítulo | approved |
| U06-CH-002B | U06-069, 071 | gráfico cuantitativo | ¿Qué cambia al aumentar el nivel manteniendo la frecuencia? | `s/L`; respuesta relativa; dos niveles | adimensional / normalizada | x/y compartidos con CH-002A | Dos curvas conceptuales del mismo modelo; mayor entrada produce respuesta más amplia y relación compresiva | “misma frecuencia”, “cambia el nivel”, máximo/región excitada; etiquetas directas, no leyenda distante | SVG/PNG + parameters.json; `u06_plot_002_nivel_y_extension.py --condition compare` | frecuencia del máximo aproximadamente constante; ancho mayor a nivel alto; ninguna curva sale del canvas; parámetros declarados como didácticos | TEX 6.7.3; Fettiplace 2017 | approved |
| U06-CH-003 | U06-070 | gráfico cuantitativo | ¿Por qué el proceso activo no puede representarse como una ganancia constante? | nivel de entrada relativo; respuesta coclear relativa; referencia pasiva | dB relativos o unidades normalizadas, no dB SPL | ambos ejes lineales en dB relativos y rango común | Función suave compresiva con parámetros pedagógicos + recta de proporcionalidad como contraste | región de alta sensibilidad, región compresiva, “no es una recta”; callout DG opcional fuera del eje | SVG/PNG + parameters.json; `u06_plot_003_compresion_coclear.py` | monotonicidad; pendiente local positiva y menor en región compresiva; evitar coeficientes fisiológicos universales; declaración conceptual visible | TEX 6.7.3; Fettiplace 2017 | approved |
| U06-CH-004 | U06-095 | gráfico cuantitativo | ¿Cómo se transforma una firma mecánica espacial en actividad de una población aferente? | `s/L`; respuesta mecánica relativa; actividad poblacional relativa | adimensional / normalizada | x común base→ápex; dos paneles con y propia claramente rotulada | Derivado determinista de CH-001 mediante muestreo de posiciones; población esquemática, no neuronas individuales reales | conectores de DG-058 entre máximos; “extensión y solapamiento” | SVG/PNG + CSV; `u06_plot_004_codigo_espacial.py` | máximos alineados entre paneles; no mostrar una fibra por frecuencia; misma paleta/posición que CH-001 | TEX 6.7.2 y 6.9.1; Fettiplace 2017 | approved |
| U06-CH-005 | U06-096 | gráfico cuantitativo | ¿Qué significa sincronización temporal sin exigir un impulso en cada ciclo? | fase/ciclos del estímulo; eventos neurales simulados; histograma de fase opcional | ciclos o fase en grados; no ms hasta validar rango | tiempo normalizado lineal; fase circular solo en respaldo | Seno didáctico + eventos probabilísticos con semilla fija y omisiones; sin límite frecuencial numérico | fases preferidas, ciclos sin evento, rótulo “probabilístico” | SVG/PNG + CSV de eventos; `u06_plot_005_sincronizacion_temporal.py` | semilla reproducible; nunca más de un significado por panel; eventos no idénticos a la onda; cifras/rangos bloqueados hasta fuente | TEX 6.9.1; fuente fisiológica externa pendiente; OD-U06-13 | blocked_source |
| U06-CH-006 | U06-098 | gráfico cuantitativo | ¿Cómo puede el nivel ampliar el patrón periférico sin equivaler linealmente a sonoridad? | posición/población; respuesta relativa; dos niveles | normalizada; niveles de entrada solo como “menor/mayor” o condiciones del caso | x lineal base→ápex; y común | Reutiliza CH-002B y agrega muestreo poblacional simple; sin tasas absolutas | región reclutada, compresión y advertencia “respuesta periférica ≠ sonoridad” | SVG/PNG + CSV; `u06_plot_006_codigo_nivel.py` | misma frecuencia de entrada; patrón alto más amplio; no usar saturación como única regla; contraste accesible sin color | TEX 6.7.3 y 6.9.2; Fettiplace 2017 | approved |
| U06-CH-007 | U06-011–012, respaldo opcional | gráfico cuantitativo | ¿Cómo varía la presión ideal con la posición de medida en un tubo aproximadamente cerrado? | posición `x/L`; presión relativa; frecuencia relativa `f/f₁` | adimensional / normalizada | x 0–1; y lineal; una o dos frecuencias como máximo | Solución ideal de onda estacionaria en tubo de cuarto de onda; condiciones de contorno explícitas | entrada, fondo timpánico ideal, nodos/antinodos y “no representa el CAE real” | SVG/PNG + parameters.json; `u06_plot_007_presion_posicion_cae_ideal.py` | condiciones matemáticas verificadas; extremos coherentes; no superponerlo a la fotografía como medición real; control dimensional | TEX 6.4.2–6.4.3; U3/U4 | optional_model |
| U06-CH-008 | U06-014–017, U06-109 | gráfico cuantitativo | ¿Cómo se ve la primera resonancia de un modelo amortiguado de cuarto de onda? | frecuencia `f`; respuesta relativa; `f₁=c/(4ℓ)` | Hz para ejemplo declarado; respuesta dB relativa | x lineal 0–8 kHz o normalizada `f/f₁`; y dB relativa | Resonador amortiguado didáctico con `ℓ=27 mm`, `c` declarado y amortiguamiento arbitrario documentado | `f₁`, zona de resonancia y tres límites del modelo | SVG/PNG + parameters.json; `u06_plot_008_resonancia_cae_ideal.py` | reproduce `f₁≈3,18 kHz`; no usar amplitud como ganancia real del CAE; amortiguamiento rotulado como parámetro didáctico | TEX 6.4.3–6.4.4; ejercicio G1 | optional_model |
| U06-CH-009 | U06-115 | gráfico cuantitativo | ¿Cómo dependen latencia o respuesta del reflejo de las condiciones de estímulo? | solo las variables respaldadas por la fuente elegida | ms y/o dB SPL con estímulo, frecuencia, duración y método explícitos | definida por dataset; sin eje truncado engañoso | Datos publicados o guía técnica por seleccionar; no digitalizar una figura sin permiso | condiciones, rango y variabilidad; nunca “valor normal universal” | SVG/PNG + data.csv; `u06_plot_009_reflejo_condiciones.py` | fuente/licencia, transcripción doble, unidades, tamaño muestral y condiciones verificados; no producir con datos del capítulo porque no los aporta | PO; TEX 6.5.4; OD-U06-10; EXT-PEND | blocked_source |

## Orden de prototipado

1. CH-001 y CH-002A/B: fijan orientación, paleta y geometría base–ápex.
2. CH-003: valida el lenguaje visual de compresión.
3. CH-004 y CH-006: heredan las geometrías ya aprobadas.
4. CH-005, CH-007 y CH-008 solo después de confirmar que agregan comprensión respecto de sus diagramas estáticos.
5. CH-009 permanece bloqueado hasta contar con datos y licencia trazables.

## Gate de aceptación

Un gráfico pasa a `approved` únicamente si el script termina sin edición manual, los datos/modelos coinciden con la fuente, ejes y normalizaciones están declarados, no hay clipping ni superposiciones, se lee a tamaño completo de slide y fue renderizado dentro del layout real. Los seis gráficos en estado `approved` fueron generados, renderizados individualmente y revisados a tamaño 16:9. Los estados bloqueados u opcionales se preservan.


## Registro de implementación

- Generador maestro: `units/unit_06/scripts/u06_generate_charts.py`.
- Familias aprobadas: U06-CH-001, U06-CH-002A, U06-CH-002B, U06-CH-003, U06-CH-004 y U06-CH-006.
- Salidas por familia: wrapper reproducible, `data.csv`, `parameters.json`, SVG, PNG 2560×1440, README y `validation.json`.
- Revisión consolidada: `units/unit_06/charts_review.md`.

