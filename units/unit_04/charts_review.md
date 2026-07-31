# Unidad 4 — Revisión de gráficos cuantitativos

## Resultado

Se aprobaron 14 de las 15 familias planificadas, con 32 variantes SVG/PNG. `U04-CH-012` permanece pendiente porque los archivos útiles del dataset abierto pesan entre 326,6 y 466,3 MB y el plan exige aprobación antes de descargarlos.

## Cobertura y archivos

| recurso | variantes | datos/modelo | estado |
|---|---:|---|---|
| U04-CH-001 | 2 | seno ilustrativo, 500 Hz | aprobado |
| U04-CH-002 | 1 | seno y seno² normalizados | aprobado |
| U04-CH-003 | 6 | señal sintética asimétrica | aprobado |
| U04-CH-004 | 1 | seno de 100 Hz y señal nula | aprobado |
| U04-CH-005 | 5 | seno de 0,20 Pa pico | aprobado |
| U04-CH-006 | 2 | señales sintéticas a 0,20 Pa RMS | aprobado |
| U04-CH-007 | 2 | relación analítica Pa–dB SPL | aprobado |
| U04-CH-008 | 5 | suma coherente para varias fases | aprobado |
| U04-CH-009 | 2 | ruidos gaussianos independientes, semilla 40467 | aprobado |
| U04-CH-010 | 2 | modelos ideales r⁰, r⁻¹ y r⁻² | aprobado |
| U04-CH-011 | 1 | ley de distancia esférica ideal | aprobado |
| U04-CH-012 | 0 | dataset Zenodo 10.5281/zenodo.10255555 | pendiente de aprobación |
| U04-CH-013 | 1 | coeficientes analíticos de reflexión | aprobado |
| U04-CH-014 | 1 | suma de niveles no correlacionados | aprobado |
| U04-CH-015 | 1 | caso coherente φ=π/2 | aprobado |

Cada carpeta aprobada contiene `data.csv`, README con caption, texto alternativo y fuente, y pares SVG/PNG con nombres equivalentes. Los PNG tienen al menos 1800×1200 píxeles y los SVG pasaron parseo XML.

## Verificaciones numéricas

- CH-003: se recalcularon extremos, media y pico a pico; el ejemplo cumple `p_pp ≠ 2·p_pico`.
- CH-005: `p_rms = 0,141421… Pa`, coincidente con `0,20/√2`.
- CH-006: la diferencia relativa de RMS entre ambas señales es menor que 0,1 %.
- CH-007: las anclas 0–120 dB corresponden exactamente a `p_ref·10^(L/20)` con `p_ref=20 µPa`.
- CH-008/015: los aumentos verificados son `+6,0206 dB` en fase y `+3,0103 dB` en cuadratura; la oposición ideal cancela.
- CH-009: RMS A y B son 0,20 Pa; correlación muestral `3,71×10⁻⁵`; incremento `3,01046 dB`.
- CH-010/011: pendientes y anclas de duplicación se derivan de los modelos declarados.
- CH-013: `R_I=R_p²` y la simetría energética bajo `η↔1/η` se conserva.
- CH-014: la curva usa `10log10(1+10^(−ΔL/10))` sin tabla de atajos fabricada.

## Hallazgos y correcciones

| problema | severidad | corrección | estado |
|---|---|---|---|
| Los ticks de presión total se redondeaban todos a 101325 Pa. | mayor | Se fijó formato a una decimal con coma. | cerrado |
| Los rótulos verticales del proceso RMS eran demasiado densos. | mayor | Se acortaron unidades en eje y se trasladaron los verbos al interior de cada panel. | cerrado |
| La primera muestra de ruido producía +3,04 dB. | menor | Se eligió una semilla reproducible con dos secuencias independientes y correlación muestral casi nula. | cerrado |
| Dos glifos de flecha no estaban disponibles en Calibri. | menor | Se reemplazaron por puntuación y redacción equivalentes. | cerrado |
| CH-012 requería una descarga masiva no autorizada. | bloqueo externo | Se conservó el script que detiene la generación y se registró el pendiente; no se sustituyeron los datos. | abierto |

## Aceptación visual

Se inspeccionaron el montaje completo y, a tamaño original, CH-001, CH-005 y CH-009. No se observaron recortes, texto fuera del canvas, leyendas superpuestas, escalas ambiguas ni resolución insuficiente. Las escalas logarítmicas se declaran en los ejes; los modelos ideales y señales sintéticas se identifican como tales.
