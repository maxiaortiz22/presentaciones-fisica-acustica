# Unidad 5 — Revisión de gráficos propios

Fecha de revisión: 2026-07-31
Alcance: implementación de las familias aprobadas en `chart_plan.md`; no se construyó la presentación.

## Resultado

- Familias aprobadas y generadas: **13 de 19**.
- Clasificación obligatoria: las 19 familias son **gráficos cuantitativos**; las 13 aprobadas se produjeron con `chart-generation`.
- Problemas críticos: **0**.
- Problemas mayores: **0**.
- Salidas por familia aprobada: wrapper reproducible, datos CSV, SVG, PNG 2560×1440, README con caption/texto alternativo/fuente y `validation.json`.

## Inventario aprobado

| ID | Tema | Escala principal | Fuente/modelo | Estado |
|---|---|---|---|---|
| CH-001 | Igual RMS, distinta forma | tiempo lineal | señal sintética; U4/brief U5 | aprobado |
| CH-002 | Tiempo, magnitud y fase | tiempo y frecuencia lineales | señal sintética; libro fig. 5.1 | aprobado |
| CH-003 | Misma magnitud, fase distinta | ejes comparables | síntesis controlada; libro/EP | aprobado |
| CH-005 | Síntesis de Fourier | tiempo lineal | serie del libro; alternativa estática 2×2 | aprobado |
| CH-006 | Muestreo y aliasing | tiempo lineal | muestras analíticas | aprobado |
| CH-007 | Bins y resolución | frecuencia lineal | `T_obs=N/f_s`, `Δf=f_s/N` | aprobado |
| CH-008 | Fuga espectral | tiempo y frecuencia lineales | tono y DFT controlados | aprobado |
| CH-011 | Componentes espectrales | frecuencia lineal | casos sintéticos del capítulo | aprobado |
| CH-013 | Regiones de frecuencia | frecuencia logarítmica | programa/libro; fronteras aproximadas | aprobado |
| CH-015 | Bin frente a banda | frecuencia logarítmica | suma energética didáctica | aprobado |
| CH-016 | Respuestas de filtros | frecuencia logarítmica; ganancia en dB | modelos Butterworth documentados | aprobado |
| CH-018 | Nivel equivalente | tiempo lineal; nivel en dB | ejemplo 70/80 dB del libro | aprobado |
| CH-019 | Caso por bandas | frecuencia logarítmica; nivel en dB | datos hipotéticos no normativos | aprobado |

## Validaciones realizadas

1. Ejecución completa de `scripts/u05_generate_charts.py --all` sin edición manual.
2. Verificación de existencia, apertura y dimensiones de las salidas; todos los PNG son 2560×1440 y todos los SVG parsean correctamente.
3. Verificación de CSV no vacío y correspondencia entre datos, ejes, unidades y escala declarada.
4. Controles numéricos específicos registrados en cada `validation.json`: RMS común, igualdad de magnitudes, coincidencia de muestras, relaciones de bins, integración energética y `L_eq≈77,4 dB`.
5. Revisión visual individual y en montaje: títulos, leyendas, contraste, márgenes, ejes y pies de fuente legibles.

## Decisiones y límites

- CH-005 reemplaza la animación opcional por una alternativa estática de cuatro estados, apta para impresión y revisión.
- CH-013 declara que las fronteras son aproximadas y que la figura no representa una escala perceptual.
- CH-019 declara que los datos son hipotéticos y no sirven para evaluar conformidad clínica, laboral o normativa.
- No se fabricaron registros vocales, tablas normativas ni valores de ponderación.

## Recursos no generados

| ID | Estado | Motivo y acción requerida |
|---|---|---|
| CH-004 | `blocked_asset` | incorporar U05-MED-003 con metadatos de captura |
| CH-009 | `pending_source` | cerrar definición SciPy y normalización común de ventanas |
| CH-010 | `blocked_asset` | incorporar U05-MED-003 y parámetros STFT trazables |
| CH-012 | `blocked_asset` | incorporar U05-MED-003 y documentar método de envolvente |
| CH-014 | `pending_standard_check` | verificar IEC 61260-1 con copia autorizada |
| CH-017 | `pending_standard_check` | verificar IEC 61672-1 con copia autorizada |

## Conclusión

Los 13 gráficos generados quedan **aprobados como assets v01**, sin problemas críticos ni mayores. Los seis restantes mantienen bloqueos trazables y no deben considerarse omitidos ni reemplazados por aproximaciones.
