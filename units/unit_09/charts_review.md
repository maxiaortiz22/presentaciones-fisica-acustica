# Unidad 9 — Revisión de gráficos propios

Fecha de cierre: 2026-08-12

## Resultado

- **Clasificación:** gráfico cuantitativo para U09-CH-001 a U09-CH-011.
- **Aprobados:** U09-CH-001–007 y U09-CH-009 (8 recursos).
- **No generados:** U09-CH-008, U09-CH-010 y U09-CH-011.
- **Problemas críticos abiertos:** 0.
- **Problemas mayores abiertos:** 0.
- **Presentación de la unidad:** no construida.

Cada gráfico aprobado conserva script reproducible, datos calculados o sintéticos, parámetros, SVG, PNG de alta resolución, preview 16:9, README, caption, texto alternativo, fuente y validación JSON.

## Control por recurso

| ID | modelo o datos | escalas | puntos de control | estado |
|---|---|---|---|---|
| U09-CH-001 | `ΔL_p=−20 log10(r₂/r₁)` | x log; y lineal | `ΔL_p(1)=0`; `ΔL_p(2)=−6,0206 dB` | aprobado |
| U09-CH-002 | patrones analíticos sintéticos normalizados | polar; 0 a −18 dB | máximo 0 dB en los tres paneles; misma referencia radial | aprobado · sintético |
| U09-CH-003 | `c≈331+0,6θ` | lineal; intervalo enfocado | 5 °C→334; 20 °C→343; 25 °C→346 m·s⁻¹ | aprobado |
| U09-CH-004 | suma de llegadas gaussianas sintéticas | mismos ejes temporales | directa, reflexión aislada y cola; sin umbral universal | aprobado · conceptual |
| U09-CH-005 | `λ=343/f` | log–log | 125 Hz→2,744 m; 500 Hz→0,686 m; 4000 Hz→0,08575 m | aprobado |
| U09-CH-006 | decaimiento sintético de −100 dB·s⁻¹ | lineal | `T_60=0,60 s`; `L(T_60)=−60 dB` | aprobado · sintético |
| U09-CH-007 | `R=10 log10(1/τ_E)` | x log decreciente; y lineal | 0,01→20 dB; 0,001→30 dB | aprobado |
| U09-CH-009 | dos espectros sintéticos ajustados a igual suma A‑ponderada relativa | bandas de octava | diferencia del descriptor relativo menor que precisión numérica; sin cifra normativa | aprobado · panel global icónico |

## Hallazgos y correcciones

| problema | severidad | corrección | estado |
|---|---|---|---|
| U09-CH-002 quedó en 1293 px de alto por recorte automático. | mayor | Se eliminó `bbox_inches="tight"`; el canvas conserva el tamaño físico y supera 2400 × 1350 px. | corregido |
| Rótulos largos se recortaban en U09-CH-001, 005 y 007. | mayor | Se acortaron los nombres de eje y se mantuvieron unidades y declaración de escala; no se redujo la fuente. | corregido |
| La nota conceptual invadía el eje en U09-CH-004 y U09-CH-006. | mayor | Se reubicó dentro de una zona libre del panel. | corregido |
| Las etiquetas de 5, 20 y 25 °C competían entre sí en U09-CH-003. | mayor | Se usaron líderes separados y posiciones directas; la frase interpretativa pasó a un área blanca reservada. | corregido |
| Leyenda y advertencia se superponían en U09-CH-009. | mayor | Se separaron entre el panel icónico y el panel por bandas. | corregido |

## Recursos condicionados

- **U09-CH-008:** no generado hasta validar la convención y el alcance de la ley de masas.
- **U09-CH-010:** bloqueado por falta de fuente primaria completa, permiso y casos publicados de control.
- **U09-CH-011:** bloqueado por falta de norma completa, adopción institucional y escenario audiométrico definido.

No se transcribieron valores normativos ni se fabricaron datos experimentales.
