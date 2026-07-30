# U02-CH002 — Fuerza elástica frente a desplazamiento

**Clasificación obligatoria:** gráfico cuantitativo.

## Pregunta pedagógica

¿Por qué la fuerza elástica apunta hacia el equilibrio y qué representa la pendiente?

## Datos y modelo

Valores calculados con F_el = −k_s x, k_s = 20 N/m; modelo lineal ideal, no mediciones de tejido.

## Escala

Ambos ejes lineales y simétricos; x en milímetros y F_el en newtons.

## Archivos

- `script.py`: regeneración reproducible desde la raíz del repositorio.
- `data.csv`: valores exactos usados por el gráfico.
- `u02_fig_002_fuerza_elastica.svg`: salida vectorial principal.
- `u02_fig_002_fuerza_elastica.png`: respaldo de 2400 × 1100 px.
- `caption.txt`, `alt_text.txt` y `source.txt`: textos de montaje y accesibilidad.
- `metadata.json`: parámetros y verificaciones.

## Caption sugerido

En el modelo lineal, la fuerza elástica cambia de signo con el desplazamiento y apunta al equilibrio.

## Validación

- Conversión explícita de milímetros a metros en el cálculo.
- Pendiente negativa igual a −20 N/m.
- Fuerza y desplazamiento tienen signos opuestos.
