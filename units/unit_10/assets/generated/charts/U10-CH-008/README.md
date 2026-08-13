# U10-CH-008 — Ruido blanco integrado por octavas

- **Clasificación obligatoria:** gráfico cuantitativo.
- **Estado:** aprobado tras validación numérica y render a tamaño final.
- **Datos/modelo:** Modelo analítico o señal sintética propia, basado en el capítulo 10 del libro del curso; parámetros y semillas en parameters.json. No representa una medición ni un límite normativo.
- **Escalas:** declaradas en los ejes y en `parameters.json`.
- **Reproducción:** `python u10_plot_008_blanco_por_octavas.py`.

## Caption sugerido

Con densidad constante por hertz, el contenido por octava se duplica porque cada banda abarca el doble de hertz.

## Texto alternativo

Barras en centros de octava desde 125 hasta 8000 Hz aumentan por factor dos; cada barra indica su ancho de banda.

## Fuente de datos

Modelo analítico o señal sintética propia, basado en el capítulo 10 del libro del curso; parámetros y semillas en parameters.json. No representa una medición ni un límite normativo.

## Archivos

- `u10_plot_008_blanco_por_octavas.py`
- `data.csv`
- `parameters.json`
- `figure.svg`
- `figure.png`
- `slide_context.png`
- `validation.json`

## Validación

PNG de 2665×1213 px; render de contexto 3200×1800 px; ejes ≥20 pt, ticks/leyenda ≥18 pt y anotaciones clave ≥22 pt. Problemas críticos: 0; problemas mayores: 0.
