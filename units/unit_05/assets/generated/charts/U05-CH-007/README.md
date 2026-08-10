# U05-CH-007

- **Clasificación:** gráfico cuantitativo
- **Pregunta:** ¿Cómo determinan f_s, N y T_obs la rejilla de bins?
- **Modelo/datos:** Libro del curso, ecuaciones T_obs=N/f_s y delta f=f_s/N; datos sintéticos.
- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.
- **Reproducción:** `python u05_plot_007_bins_resolucion.py`

## Caption sugerido

A frecuencia de muestreo constante, cuadruplicar la duración reduce la separación entre bins de 4 Hz a 1 Hz y permite distinguir componentes próximas.

## Texto alternativo

Dos espectros DFT alineados comparan registros de 0,25 y 1 segundo. El corto tiene bins separados 4 hertz y no separa con claridad tonos de 1000 y 1002 hertz; el largo presenta bins de 1 hertz y dos máximos.

## Fuente de datos

Libro del curso, ecuaciones T_obs=N/f_s y delta f=f_s/N; datos sintéticos.

## Archivos

- `u05_fig_007_bins_resolucion.svg`
- `u05_fig_007_bins_resolucion.png`
- `data.csv`
- `validation.json`

## Validación numérica

```json
{
  "relations_verified": true
}
```
