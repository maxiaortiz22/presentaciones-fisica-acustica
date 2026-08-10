# U05-CH-005

- **Clasificación:** gráfico cuantitativo
- **Pregunta:** ¿Cómo cambia una señal al sumar componentes de Fourier?
- **Modelo/datos:** Libro del curso, Unidad 5, figura 5.2; serie matemática determinista.
- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.
- **Reproducción:** `python u05_plot_005_sintesis_fourier.py`

## Caption sugerido

Sumas parciales de 1, 3, 5 y 10 términos impares aproximan una onda rectangular sin eliminar la oscilación próxima a la discontinuidad.

## Texto alternativo

Cuatro paneles con la misma escala comparan una onda rectangular ideal con sumas parciales de uno, tres, cinco y diez términos impares de su serie de Fourier.

## Fuente de datos

Libro del curso, Unidad 5, figura 5.2; serie matemática determinista.

## Archivos

- `u05_fig_005_sintesis_fourier.svg`
- `u05_fig_005_sintesis_fourier.png`
- `data.csv`
- `validation.json`

## Validación numérica

```json
{
  "term_counts": [
    1,
    3,
    5,
    10
  ],
  "static_alternative": "panel 2×2"
}
```
