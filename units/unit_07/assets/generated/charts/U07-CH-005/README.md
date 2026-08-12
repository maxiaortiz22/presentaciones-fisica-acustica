# U07-CH-005

- **Clasificación obligatoria:** gráfico cuantitativo.
- **Pregunta:** ¿Puede sostenerse el pitch aunque falte la línea en la frecuencia fundamental?
- **Estado:** aprobado como asset v01 tras render individual y simulación a tamaño final 16:9.
- **Escala:** ejes lineales.
- **Fuente de datos/modelo:** Síntesis determinista propia: f₀=200 Hz, armónicos 1–8 y caída 1/n; no son datos humanos.
- **Reproducción:** ejecutar `u07_plot_005_fundamental_ausente.py` en esta carpeta o `units/unit_07/scripts/u07_generate_charts.py U07-CH-005`.

## Caption sugerido

Dos espectros comparten el espaciamiento de 200 Hz; en el segundo falta la componente física de 200 Hz, pero permanecen los armónicos 2–8.

## Texto alternativo

Dos espectros de líneas. El primero contiene armónicos desde doscientos hasta mil seiscientos hertz; el segundo omite la línea de doscientos hertz y conserva las demás.

## Límites

Figura calculada desde una ecuación o síntesis determinista declarada; no contiene datos experimentales.

## Validación

- PNG 2560×1440 y SVG parseable;
- CSV y parámetros reproducibles;
- ejes, unidades y tipo de escala declarados;
- fuentes mínimas: ejes 20 pt, ticks/leyenda 18 pt y anotaciones 22 pt;
- revisión individual y en canvas de slide completo;
- problemas críticos: 0; problemas mayores: 0.
