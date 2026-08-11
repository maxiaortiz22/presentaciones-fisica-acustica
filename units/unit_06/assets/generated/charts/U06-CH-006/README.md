# U06-CH-006

- **Clasificación:** gráfico cuantitativo.
- **Pregunta:** ¿Cómo puede el nivel ampliar el patrón periférico sin equivaler a sonoridad?
- **Estado:** aprobado como asset v01 tras generación, render individual y revisión a tamaño 16:9.
- **Escala:** x e y lineales; respuesta normalizada común.
- **Fuente de datos/modelo:** Derivación determinista de U06-CH-002B; TEX 6.7.3 y 6.9.2; Fettiplace (2017). No son tasas neurales absolutas.
- **Reproducción:** ejecutar el wrapper local o `units/unit_06/scripts/u06_generate_charts.py U06-CH-006`.

## Caption sugerido

En el modelo conceptual, una entrada mayor extiende la región de excitación y activa una población más amplia; esa respuesta periférica no es una medida de sonoridad.

## Texto alternativo

Dos curvas de actividad poblacional sobre el eje base-ápex. La condición mayor es más ancha y algo más alta; ambas mantienen aproximadamente el mismo lugar característico. Una advertencia separa respuesta periférica y sonoridad.

## Límites

Figura conceptual normalizada y no a escala. No contiene mediciones anatómicas, clínicas ni tasas neurales absolutas. Los parámetros se conservan en `parameters.json` y los valores dibujados en `data.csv`.

## Validación

- PNG 2560×1440 y SVG parseable;
- ejes, unidades/normalización y orientación base→ápex declarados;
- fuente mínima: ticks/leyenda 18 pt, ejes 20 pt, anotaciones 22 pt;
- revisión individual y dentro del canvas final 16:9;
- problemas críticos: 0; problemas mayores: 0.
