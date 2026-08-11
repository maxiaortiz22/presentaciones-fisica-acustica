# U06-CH-003

- **Clasificación:** gráfico cuantitativo.
- **Pregunta:** ¿Por qué el proceso activo no puede representarse como una ganancia constante?
- **Estado:** aprobado como asset v01 tras generación, render individual y revisión a tamaño 16:9.
- **Escala:** ambos ejes lineales en dB relativos.
- **Fuente de datos/modelo:** Función matemática didáctica inspirada en TEX 6.7.3 y Fettiplace (2017); coeficientes no fisiológicos ni universales.
- **Reproducción:** ejecutar el wrapper local o `units/unit_06/scripts/u06_generate_charts.py U06-CH-003`.

## Caption sugerido

La respuesta activa conceptual es más sensible a entradas débiles y reduce gradualmente su pendiente en la región compresiva.

## Texto alternativo

Gráfico entrada-salida en decibeles relativos. Una recta gris representa proporcionalidad; una curva bordó comienza por encima y se aproxima a la referencia al aumentar la entrada, manteniendo pendiente positiva menor en la región compresiva.

## Límites

Figura conceptual normalizada y no a escala. No contiene mediciones anatómicas, clínicas ni tasas neurales absolutas. Los parámetros se conservan en `parameters.json` y los valores dibujados en `data.csv`.

## Validación

- PNG 2560×1440 y SVG parseable;
- ejes, unidades/normalización y orientación base→ápex declarados;
- fuente mínima: ticks/leyenda 18 pt, ejes 20 pt, anotaciones 22 pt;
- revisión individual y dentro del canvas final 16:9;
- problemas críticos: 0; problemas mayores: 0.
