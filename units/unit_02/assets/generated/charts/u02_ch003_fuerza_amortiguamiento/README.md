# U02-CH003 — Fuerza de amortiguamiento frente a velocidad

**Clasificación obligatoria:** gráfico cuantitativo.

## Pregunta pedagógica

¿Cómo depende la fuerza de amortiguamiento de la velocidad?

## Datos y modelo

Valores calculados con F_amort = −b v, b = 2,0 N·s/m; modelo viscoso lineal, no ley universal de tejidos.

## Escala

Ambos ejes lineales y simétricos; v en m/s y F_amort en N.

## Archivos

- `script.py`: regeneración reproducible desde la raíz del repositorio.
- `data.csv`: valores exactos usados por el gráfico.
- `u02_fig_003_fuerza_amortiguamiento.svg`: salida vectorial principal.
- `u02_fig_003_fuerza_amortiguamiento.png`: respaldo de 2400 × 1100 px.
- `caption.txt`, `alt_text.txt` y `source.txt`: textos de montaje y accesibilidad.
- `metadata.json`: parámetros y verificaciones.

## Caption sugerido

El modelo viscoso lineal produce una fuerza proporcional y opuesta a la velocidad.

## Validación

- Pendiente negativa igual a −b.
- El producto b·v conserva unidad de newton.
- La figura declara el alcance del modelo.
