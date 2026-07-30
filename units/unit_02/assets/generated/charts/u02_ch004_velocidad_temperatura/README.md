# U02-CH004 — Velocidad del sonido frente a temperatura

**Clasificación obligatoria:** gráfico cuantitativo.

## Pregunta pedagógica

¿Cuánto aumenta c en el rango ambiental y qué no permite concluir el gráfico?

## Datos y modelo

Valores calculados con c ≈ 331 m/s + [0,6 (m/s)/°C]·ϑ, modelo del libro; no son mediciones.

## Escala

Eje horizontal lineal de 0 a 30 °C. Eje vertical lineal truncado de 325 a 355 m/s, declarado en la figura.

## Archivos

- `script.py`: regeneración reproducible desde la raíz del repositorio.
- `data.csv`: valores exactos usados por el gráfico.
- `u02_fig_004_velocidad_temperatura.svg`: salida vectorial principal.
- `u02_fig_004_velocidad_temperatura.png`: respaldo de 2400 × 1100 px.
- `caption.txt`, `alt_text.txt` y `source.txt`: textos de montaje y accesibilidad.
- `metadata.json`: parámetros y verificaciones.

## Caption sugerido

Aproximación para aire seco en rango ambiental; el eje vertical 325–355 m/s no comienza en cero.

## Validación

- Se verifican 331, 337, 343 y 349 m/s.
- Pendiente exacta del modelo: 0,6 (m/s)/°C.
- No se infiere frecuencia, longitud de onda ni altura tonal sin datos adicionales.
