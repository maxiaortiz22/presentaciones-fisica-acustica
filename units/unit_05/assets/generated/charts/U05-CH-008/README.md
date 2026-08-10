# U05-CH-008

- **Clasificación:** gráfico cuantitativo
- **Pregunta:** ¿Por qué un recorte puede distribuir un tono entre varios bins?
- **Modelo/datos:** Libro del curso, Unidad 5, figura 5.3; modelo matemático determinista.
- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.
- **Reproducción:** `python u05_plot_008_fuga_espectral.py`

## Caption sugerido

Con ventana rectangular, un tono que completa un número no entero de períodos distribuye su magnitud entre varios bins.

## Texto alternativo

Cuatro paneles comparan un tono de cien hertz con diez períodos exactos y otro de ciento cinco hertz con diez períodos y medio. El primer espectro se concentra en un bin; el segundo presenta fuga espectral.

## Fuente de datos

Libro del curso, Unidad 5, figura 5.3; modelo matemático determinista.

## Archivos

- `u05_fig_008_fuga_espectral.svg`
- `u05_fig_008_fuga_espectral.png`
- `data.csv`
- `validation.json`

## Validación numérica

```json
{
  "parseval_relative_errors": [
    5.551115123125783e-17,
    0.0009030844756610645
  ]
}
```
