# U05-CH-015

- **Clasificación:** gráfico cuantitativo
- **Pregunta:** ¿Qué se pierde y qué se conserva al agrupar bins en bandas?
- **Modelo/datos:** Libro del curso, ecuaciones de suma por banda; espectro sintético determinista.
- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.
- **Reproducción:** `python u05_plot_015_bin_frente_banda.py`

## Caption sugerido

Los bins conservan detalle fino; las bandas resumen la potencia total mediante suma lineal antes de convertir a decibeles.

## Texto alternativo

El panel superior muestra muchas contribuciones por bin en un eje logarítmico. El inferior agrupa esos valores en cinco bandas teóricas de octava y muestra el nivel total de cada una.

## Fuente de datos

Libro del curso, ecuaciones de suma por banda; espectro sintético determinista.

## Archivos

- `u05_fig_015_bin_frente_banda.svg`
- `u05_fig_015_bin_frente_banda.png`
- `data.csv`
- `validation.json`

## Validación numérica

```json
{
  "linear_sum_before_db": true,
  "band_total_linear": 15.848656247284357
}
```
