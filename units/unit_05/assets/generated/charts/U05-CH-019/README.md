# U05-CH-019

- **Clasificación:** gráfico cuantitativo
- **Pregunta:** ¿Qué bandas incumplen límites dados en un caso hipotético?
- **Modelo/datos:** Actividad didáctica hipotética U05-123; valores creados únicamente para resolver el ejercicio.
- **Escala y tamaño:** canvas 16:9; PNG 2560×1440; SVG con texto editable.
- **Reproducción:** `python u05_plot_019_caso_bandas.py`

## Caption sugerido

Caso didáctico no normativo: niveles por banda se comparan con límites hipotéticos y las excedencias se identifican por color y trama.

## Texto alternativo

Barras por centro de banda entre 125 y 4000 hertz se comparan con una línea escalonada de límites. Las bandas de 500, 1000 y 2000 hertz aparecen tramadas por superar el límite hipotético.

## Fuente de datos

Actividad didáctica hipotética U05-123; valores creados únicamente para resolver el ejercicio.

## Archivos

- `u05_fig_019_caso_bandas.svg`
- `u05_fig_019_caso_bandas.png`
- `data.csv`
- `validation.json`

## Validación numérica

```json
{
  "failing_centers_hz": [
    500,
    1000,
    2000
  ]
}
```
