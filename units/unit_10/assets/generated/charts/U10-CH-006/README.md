# U10-CH-006 — Tiempo y densidad espectral

- **Clasificación obligatoria:** gráfico cuantitativo.
- **Estado:** aprobado tras validación numérica y render a tamaño final.
- **Datos/modelo:** Modelo analítico o señal sintética propia, basado en el capítulo 10 del libro del curso; parámetros y semillas en parameters.json. No representa una medición ni un límite normativo.
- **Escalas:** declaradas en los ejes y en `parameters.json`.
- **Reproducción:** `python u10_plot_006_tiempo_y_psd.py`.

## Caption sugerido

La traza temporal y la PSD describen la misma realización de ruido limitado en banda.

## Texto alternativo

A la izquierda aparece una realización temporal; a la derecha, su densidad espectral estimada por Welch, con la banda útil resaltada.

## Fuente de datos

Modelo analítico o señal sintética propia, basado en el capítulo 10 del libro del curso; parámetros y semillas en parameters.json. No representa una medición ni un límite normativo.

## Archivos

- `u10_plot_006_tiempo_y_psd.py`
- `data.csv`
- `parameters.json`
- `figure.svg`
- `figure.png`
- `slide_context.png`
- `validation.json`

## Validación

PNG de 2665×1213 px; render de contexto 3200×1800 px; ejes ≥20 pt, ticks/leyenda ≥18 pt y anotaciones clave ≥22 pt. Problemas críticos: 0; problemas mayores: 0.
