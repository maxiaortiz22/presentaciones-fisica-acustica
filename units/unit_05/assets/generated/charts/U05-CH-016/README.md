# U05-CH-016

- **Clasificación:** gráfico cuantitativo
- **Pregunta:** ¿Cómo distingue la respuesta a los cuatro tipos de filtro y a un filtro real?
- **Modelo/datos:** Libro del curso, figura 5.7; modelos Butterworth calculados con SciPy 1.13.1.
- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.
- **Reproducción:** `python u05_plot_016_respuestas_filtros.py`

## Caption sugerido

Respuestas ideales y modelos Butterworth analógicos de cuarto orden muestran paso, rechazo y transición de cuatro tipos de filtro.

## Texto alternativo

Cuatro paneles en frecuencia logarítmica comparan pasa bajos, pasa altos, pasa banda y elimina banda. Cada panel distingue el salto ideal de una respuesta real con transición y marca el criterio de menos tres decibeles.

## Fuente de datos

Libro del curso, figura 5.7; modelos Butterworth calculados con SciPy 1.13.1.

## Archivos

- `u05_fig_016_respuestas_filtros.svg`
- `u05_fig_016_respuestas_filtros.png`
- `data.csv`
- `validation.json`

## Validación numérica

```json
{
  "cutoff_criterion_db": -3,
  "scipy_version": "1.13.1",
  "models_stable": true
}
```
