# Unidad 10 — Necesidades iniciales de gráficos cuantitativos

## Alcance

Plan previo a `chart-generation`. Los gráficos deben derivarse de señales sintéticas reproducibles o datos externos verificados. Las figuras existentes del libro son base conceptual, no assets finales: deben regenerarse con tipografía, paleta, ejes y densidad del template.

## Inventario

| chart_id | slides | pregunta que responde | ejes/unidades | datos o modelo | fuente base | controles de interpretación | estado |
|---|---|---|---|---|---|---|---|
| U10-CH-001 | U10-012 | ¿Cómo pueden dos realizaciones diferir y compartir propiedades? | x: tiempo s; y: presión mPa | Dos realizaciones con semilla fija y RMS comparable. | LaTeX 10.5; script U10 existente. | Rotular “sintético”; no inferir distribución solo por apariencia. | planificado |
| U10-CH-002 | U10-015 | ¿Cómo cambian muestras mientras estadísticas permanecen? | x: tiempo s; y: presión mPa | Señal estacionaria sintética; dos ventanas iguales. | LaTeX 10.5.1. | Mostrar media/RMS por ventana; mismo tamaño de ventana. | planificado |
| U10-CH-003 | U10-016 | ¿Por qué la clasificación depende de escala temporal? | x: tiempo s/min; y: amplitud o nivel relativo | Registro largo con detalle ampliado. | LaTeX 10.5.1; elaboración propia. | Mismo registro; señalar zoom y ventanas; no mezclar ejes sin rótulo. | prototipar temprano |
| U10-CH-004 | U10-017 | ¿Cómo se distinguen continuo, fluctuante, intermitente e impulsivo? | x: tiempo s; y: `p(t)` mPa | Cuatro realizaciones sintéticas, 1 s, 1000 Hz. | Figura 10.1; `generate_unit10_figures.py`. | Mismos ejes; amplitudes no son exposición medida. | reconstrucción prioritaria |
| U10-CH-005 | U10-024 | ¿Qué diferencia conserva el histograma cuando RMS coincide? | x temporal: ms; y: mPa; histograma: intervalo mPa/frecuencia relativa | Gaussiana normalizada y señal de dos niveles; semilla fija. | Figura 10.2; script U10. | Dividir en dos etapas si baja legibilidad; mostrar métricas compartidas. | reconstrucción prioritaria |
| U10-CH-006 | U10-027 | ¿Qué aporta tiempo y qué aporta frecuencia? | panel tiempo: s/mPa; panel frecuencia: Hz/escala definida | Una misma realización sintética. | U5 + LaTeX 10.8; elaboración propia. | Declarar método espectral, ventana y escala; no llamar respuesta en frecuencia. | planificado |
| U10-CH-007 | U10-031 | ¿Qué significa densidad blanca constante por Hz? | x: frecuencia Hz; y: `S_pp` Pa²/Hz | `S_pp=S_0` en banda finita. | LaTeX ec. 10.6. | Marcar límites de banda; no extender a infinito. | planificado |
| U10-CH-008 | U10-032 | ¿Qué ocurre al integrar blanco por octavas? | x: bandas de octava Hz; y: contenido relativo adimensional | Integración analítica del modelo blanco. | Figura 10.3; script U10. | Explicar que crece el ancho en Hz; normalización visible. | planificado |
| U10-CH-009 | U10-033 | ¿Qué significa densidad rosa proporcional a `1/f`? | x: frecuencia Hz log; y: `S_pp` Pa²/Hz log | `S_pp=K/f` en banda finita. | LaTeX ec. 10.7. | No confundir −3 dB/oct con nivel total por octava. | planificado |
| U10-CH-010 | U10-034/035 | ¿Cómo se conectan densidades y contenido por octava? | dos paneles coordinados como CH-007–009 | Modelos blanco/rosa de 125 a 8000 Hz. | Figura 10.3; script U10. | Dos etapas o dos slides; etiquetas directas; máximo tres series. | reconstrucción prioritaria |
| U10-CH-011 | U10-047/048 | ¿Cómo se ubican máximo, pico y equivalente sobre una misma señal? | x: tiempo s; y: presión o nivel con descriptor explícito | Señal sintética con componente continua variable e impulsos. | LaTeX 10.9; elaboración propia. | No presentar `L_peak` y `L_max` como puntos de la misma operación sin cadena de detector. | prototipar temprano |
| U10-CH-012 | U10-051/090 | ¿Cómo se interpreta un percentil de excedencia? | x: porcentaje de tiempo excedido; y: nivel dB con ponderación declarada | Distribución acumulada sintética. | LaTeX 10.9. | Rotular `L_10,T`/`L_90,T`; no llamarlos automáticamente fondo. | complementario |
| U10-CH-013 | U10-054 | ¿Qué cambia al reducir SNR manteniendo señal y realización de ruido? | x: tiempo ms; y: presión mPa | Señal 240/430 Hz + ruido; SNR +12, 0, −6 dB. | Figura 10.5; script U10. | Misma escala/ejes; no predecir inteligibilidad. | reconstrucción prioritaria |
| U10-CH-014 | U10-078 | ¿Cómo se distinguen las fuentes del caso por evolución temporal? | x: tiempo; y: nivel relativo o `p(t)` con unidad | Tránsito, climatización y portazos sintéticos coordinados. | Pregunta integradora I1; elaboración propia. | No simular medición real; etiquetar categorías y ventanas. | serie coordinada con DG-050–053 |

## Familias que deben compartir geometría y datos

- CH-002 y CH-003: mismo registro; cambia la escala de observación.
- CH-007, CH-008, CH-009 y CH-010: mismos límites de banda y normalización.
- CH-011 debe alimentar la explicación de U10-047 y el error de U10-048.
- CH-014 debe usar el mismo caso y colores semánticos que DG-050–053.

## Controles comunes de aceptación

- ejes, unidades, escalas y banda visibles;
- método/semilla/parámetros documentados;
- texto de gráfico equivalente a 16–20 pt en slide;
- máximo habitual de tres series;
- ninguna curva presentada como medición si es sintética;
- ningún valor normativo sin fuente completa;
- alternativa estática para cualquier animación;
- verificación dimensional y numérica automatizada.

## Orden de producción posterior

1. Prototipos críticos: CH-003, CH-004, CH-005, CH-010, CH-011 y CH-013.
2. Gráficos conceptuales simples: CH-002, CH-006–009 y CH-012.
3. Serie integradora: CH-014 después de fijar DG-050–053.
4. CH-001 solo si se conserva la slide complementaria U10-012.
