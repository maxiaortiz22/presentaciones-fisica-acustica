# Unidad 10 — Revisión de gráficos cuantitativos

Fecha: 2026-08-12

## Resultado

Se generaron y revisaron **15 gráficos cuantitativos**. Todos poseen script reproducible, datos o parámetros, SVG, PNG de alta resolución, render 16:9, caption, texto alternativo y fuente del modelo. No se generó U10-CH-016 porque continúa bloqueado por falta de una fuente normativa definida.

## Gates aplicados

- ejes, magnitudes, unidades y escala declarados;
- ejes ≥20 pt, ticks/leyenda ≥18 pt y anotaciones clave ≥22 pt;
- modelos analíticos o señales sintéticas identificadas;
- validaciones de normalización, Parseval, integración, pendiente, percentiles, detectores y SNR;
- PNG individual ≥2400 px de ancho y render de contexto 3200×1800;
- inspección de las dos hojas de contacto;
- cero problemas críticos y cero mayores al cierre.

## Revisión por recurso

| ID | Control cuantitativo principal | Revisión visual | Estado |
|---|---|---|---|
| U10-CH-001 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-002 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-003 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-004 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-005 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-006 | Parseval: error relativo 0.0035 | render individual y 16:9 legibles | aprobado |
| U10-CH-007 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-008 | integración por octavas verificada | render individual y 16:9 legibles | aprobado |
| U10-CH-009 | pendiente log–log -1 | render individual y 16:9 legibles | aprobado |
| U10-CH-010 | integración por octavas verificada | render individual y 16:9 legibles | aprobado |
| U10-CH-011 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-012 | curva monótona; percentiles verificados | render individual y 16:9 legibles | aprobado |
| U10-CH-013 | error máximo de SNR 8.88e-16 dB | render individual y 16:9 legibles | aprobado |
| U10-CH-014 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |
| U10-CH-015 | aserciones y parámetros en validation.json | render individual y 16:9 legibles | aprobado |

## Correcciones del ciclo visual

- CH-003: el aviso de nivel relativo se trasladó dentro del panel superior para liberar el eje.
- CH-005: el rango del histograma se amplió para contener todas las muestras y conservar suma relativa ≈1.
- CH-013 y CH-014: los avisos de señal/caso sintético se reubicaron dentro del último panel, sin tocar la etiqueta del eje.

## Problemas abiertos

- U10-CH-016 permanece bloqueado. No se fabricaron límites de exposición ni se fusionaron normas de distintas jurisdicciones.
