# Unidad 5 — Necesidades iniciales de gráficos cuantitativos

## Alcance

Familias de gráficos propias requeridas por el storyboard. Cada familia debe producirse de forma reproducible, preferentemente con Python, NumPy, SciPy y Matplotlib, y exportarse en SVG cuando la editabilidad importe. No se deberán copiar capturas del PDF: sus figuras son fuente conceptual y de verificación.

## Reglas comunes

- Ejes, unidades, escala y magnitud de la ordenada siempre explícitos.
- Mantener parámetros visibles: `f_s`, `N`, `T_obs`, ventana, solapamiento y normalización cuando correspondan.
- No denominar “intensidad” a una amplitud o potencia espectral sin definición física.
- Usar escalas coordinadas entre comparaciones y revelar cambios de a uno.
- Diferenciar datos reales, datos sintéticos y curvas normativas.
- Mantener una alternativa estática para toda animación o audio.
- Validar consistencia dimensional y numérica antes de exportar.

## Inventario de familias

| chart_id | slides previstas | gráfico cuantitativo | variables y controles | fuente/base | propósito | salida prevista | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U05-CH-001 | U05-002 | Dos señales temporales de igual RMS y forma distinta | tiempo, amplitud, RMS común | EP; continuidad U04-109 | Diagnóstico inicial: una sola magnitud no describe la señal | SVG 16:9, dos paneles | alta | especificar |
| U05-CH-002 | U05-009–011 | Misma señal en tiempo, magnitud y fase | `t`, `f`, amplitud, fase | TEX/PDF fig. 5.1 | Separar las preguntas respondidas por cada representación | Familia de 3–4 SVG coordinados | alta | reconstruir |
| U05-CH-003 | U05-013–014 | Igual magnitud, fase distinta, forma temporal distinta | magnitud y fase por componente | TEX/PDF; EP | Evitar que “el espectro” se reduzca a magnitud | SVG comparativo; posible animación | alta | producir |
| U05-CH-004 | U05-016 | Señal vocal segmentada en zonas casi estacionarias | tiempo, amplitud, ventanas | TEX/PDF; registro U05-AS-002 o sintético | Distinguir transitorio, periódico y cuasiestacionario | SVG con tres regiones | media | depende de asset |
| U05-CH-005 | U05-019–021, U05-025 | Construcción progresiva de una señal por senoides | frecuencia, amplitud, fase, número de componentes | TEX/PDF fig. 5.2; EP | Crear intuición de serie/transformada de Fourier | 4 SVG con escalas fijas | alta | producir |
| U05-CH-006 | U05-032, U05-136 | Muestreo y aliasing | `f_s`, `f`, muestras por período | TEX/PDF; EP | Mostrar qué se conserva y qué se vuelve ambiguo | SVG + animación opcional | alta | producir |
| U05-CH-007 | U05-035–039 | Bins, duración y resolución | `N`, `f_s`, `T_obs`, `Δf` | TEX/PDF; EP | Conectar rejilla espectral con observación finita | Familia de rejillas y espectros | alta | producir |
| U05-CH-008 | U05-043–044 | Fuga espectral: número entero/no entero de períodos | frecuencia de tono, `T_obs`, ventana | TEX/PDF fig. 5.3 | Explicar que el recorte modifica la lectura | SVG comparativo, mismas escalas | alta | reconstruir |
| U05-CH-009 | U05-045, U05-138 | Ventanas y sus respuestas | rectangular, Hann y otra a decidir; ancho de lóbulo, lóbulos laterales | TEX/PDF; bibliografía técnica por validar | Mostrar compromiso resolución–fuga | SVG + tabla breve | media | fuente pendiente |
| U05-CH-010 | U05-046–048 | Espectrograma sintético y de voz | tiempo, frecuencia, nivel/color, ventana, solapamiento | TEX/PDF; U05-AS-002 | Introducir representación tiempo–frecuencia | SVG/PNG de alta resolución | alta | producir |
| U05-CH-011 | U05-066–069 | Componente fundamental, armónicos y parciales | `f_0`, múltiplos, amplitudes | TEX/PDF fig. 5.5 | Fijar nomenclatura con evidencia visual | 3 SVG coordinados | alta | reconstruir |
| U05-CH-012 | U05-071–073, U05-141 | Espectro vocal: líneas y envolvente/formantes | frecuencia, amplitud/nivel, `f_0`, `F_1…` | TEX/PDF; U05-AS-002 | Separar fuente periódica y resonancias del tracto | SVG con datos declarados | alta | depende de voz |
| U05-CH-013 | U05-074–079 | Regiones frecuenciales y límites condicionados | frecuencia logarítmica; fronteras aproximadas | PO; TEX/PDF; fuentes a validar | Ubicar infra/audible/ultra sin universalizar límites | SVG conceptual con banda de incertidumbre | alta | curar cifras |
| U05-CH-014 | U05-084–094, U05-142 | Octavas y tercios de octava | `f_c`, `f_L`, `f_H`, ancho, razón | PO; TEX/PDF fig. 5.6; norma/bibliografía por validar | Construir escala relativa y agrupamiento por bandas | Familia de ejes logarítmicos y tablas | alta | producir |
| U05-CH-015 | U05-085, U05-091–092 | Espectro fino frente a energía por bandas | frecuencia, magnitud/potencia, límites de banda | TEX/PDF; EP | Diferenciar bin, componente y banda | SVG doble con ordenada declarada | alta | producir |
| U05-CH-016 | U05-097–103, U05-144 | Respuestas de filtros | ganancia, frecuencia, corte, ancho, pendiente | TEX/PDF fig. 5.7 | Comparar pasa bajos, altos, banda y rechazo | 4 SVG y comparación ideal/real | alta | reconstruir |
| U05-CH-017 | U05-108–116, U05-145 | Curvas A, C y Z | frecuencia, corrección en dB | PO; TEX/PDF; IEC 61672-1 a verificar | Explicar qué modifica cada ponderación y sus límites | SVG calculado/documentado | alta | fuente normativa pendiente |
| U05-CH-018 | U05-121, U05-147 | Nivel variable y nivel continuo equivalente | tiempo, nivel/energía, duración | TEX/PDF; EP | Evitar promedio aritmético de dB | Gráfico temporal + áreas equivalentes | alta | producir |
| U05-CH-019 | U05-123 | Resultados hipotéticos por banda | bandas, niveles y límites dados | EP, datos explícitamente hipotéticos | Actividad integradora sin simular protocolo real | Barras por banda | media | diseñar con actividad |

## Agrupación para producción

1. **Familia A — representación y Fourier:** U05-CH-001 a 005.
2. **Familia B — digital y tiempo–frecuencia:** U05-CH-006 a 010.
3. **Familia C — componentes, voz y rangos:** U05-CH-011 a 013.
4. **Familia D — bandas y filtros:** U05-CH-014 a 016.
5. **Familia E — medición:** U05-CH-017 a 019.

La agrupación debe reutilizar paleta, escalas y funciones de generación, pero no duplicar una figura sin una nueva lectura pedagógica.

## Controles de aceptación

- Parámetros y fuentes registrados en el propio script o en un archivo de datos versionado.
- Ejes y unidades legibles a tamaño real de slide.
- Comparaciones con límites idénticos cuando se interpreta un cambio.
- Cifras normativas rastreables a edición y cláusula/tabla pertinentes.
- Exportación sin recortes, solapamientos ni leyendas innecesarias.
- Verificación manual de al menos un caso numérico por familia.

## Estado

**Inventario inicial.** La producción corresponde a `chart-generation`; todavía no se generaron figuras finales.
