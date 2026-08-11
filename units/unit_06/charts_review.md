# Unidad 6 — Revisión de gráficos propios

Fecha de revisión: 2026-08-10  
Estado: **aprobado para integración futura en la presentación**  
Alcance: seis gráficos cuantitativos aprobados en `chart_plan.md`. No se construyó la presentación.

## Inventario revisado

| Recurso | Tema | Escala | Datos/modelo | Estado |
|---|---|---|---|---|
| U06-CH-001 | Tonotopía coclear normalizada | ejes lineales, posición y respuesta normalizadas | familia paramétrica conceptual documentada | aprobado |
| U06-CH-002A | Respuesta coclear a nivel débil | ejes lineales compartidos con CH-002B | modelo paramétrico conceptual | aprobado |
| U06-CH-002B | Efecto del nivel sobre la extensión de la respuesta | ejes lineales compartidos | mismo modelo y frecuencia característica que CH-002A | aprobado |
| U06-CH-003 | Compresión coclear | entrada y respuesta en dB relativos, ejes lineales | función didáctica monotónica; no es una curva fisiológica universal | aprobado |
| U06-CH-004 | Código espacial poblacional | posición y respuestas relativas, ejes lineales | derivación determinista de CH-001 | aprobado |
| U06-CH-006 | Nivel y extensión del patrón periférico | posición y respuesta normalizadas, ejes lineales | reutilización documentada del modelo de CH-002B | aprobado |

## Verificaciones realizadas

- Clasificación comprobada: los seis recursos son **gráficos cuantitativos** y se implementaron con `chart-generation`.
- Cada carpeta contiene script reproducible, datos CSV, parámetros, SVG, PNG de 2560 × 1440, README, caption, texto alternativo, fuente y registro de validación.
- Se verificaron ejes, unidades o normalización, tipo de escala y orientación base→ápex cuando corresponde.
- Los modelos conceptuales se identifican como tales y no se presentan como mediciones humanas ni como datos experimentales.
- CH-001 mantiene las curvas dentro de [0, 1] y el orden espacial altas→medias→bajas.
- CH-002A/002B comparten escala y frecuencia característica; la condición de mayor nivel ensancha la respuesta.
- CH-003 es monotónico y su región compresiva conserva pendiente positiva menor que la referencia proporcional.
- CH-004 alinea la firma mecánica y el patrón poblacional sin representar una fibra aislada por frecuencia.
- CH-006 conserva la misma frecuencia de entrada, amplía el patrón a mayor nivel y explicita que respuesta periférica no equivale a sonoridad.
- Se inspeccionaron los renders completos y el montaje comparativo; no se detectaron clipping, desbordes ni texto ilegible.

## Resultado

Problemas críticos: **0**  
Problemas mayores: **0**  
Recursos aprobados: **6 de 6 implementados**

## Recursos no producidos

- U06-CH-005 y U06-CH-009 continúan `blocked_source`; no se fabricaron eventos, límites fisiológicos ni datos clínicos.
- U06-CH-007 y U06-CH-008 continúan `optional_model`; no forman parte del conjunto aprobado solicitado.

El resumen automático consolidado está en `assets/generated/asset_validation_summary.json`.
