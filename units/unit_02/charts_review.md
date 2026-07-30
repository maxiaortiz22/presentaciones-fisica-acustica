# Unidad 2 — Revisión de gráficos cuantitativos

## Resultado

**Estado general: aprobado para la fase de redacción y montaje.**

Se implementaron U02-CH001–U02-CH004. U02-CH005 no se generó como gráfico porque el plan ya lo había reemplazado por una tabla y dos trayectos; el cálculo numérico de control permanece en los metadatos de U02-CH004.

## Clasificación

Los cuatro recursos activos se clasificaron antes de generarse como **gráficos cuantitativos**. No se usó `chart-generation` para diagramas de cajas, procesos o ecuaciones anotadas.

## Entorno

- Fecha: 2026-07-29.
- Python: 3.12.7.
- NumPy: 1.26.4.
- Matplotlib: 3.9.2.
- Pillow: 10.4.0.
- pandas y SciPy no fueron necesarios: todos los valores provienen de modelos algebraicos exactos del capítulo.

## Inventario

Cada paquete bajo `assets/generated/charts/` contiene:

- `script.py`;
- `data.csv`;
- SVG editable;
- PNG de 2400 × 1100 px;
- `README.md`;
- `caption.txt`;
- `alt_text.txt`;
- `source.txt`;
- `metadata.json`.

Los cuatro scripts fuente se conservan también en `units/unit_02/scripts/`. `u02_generate_all_charts.py` regenera el lote y la hoja de contacto.

## Verificación técnica

| control | resultado |
|---|---|
| Paquetes | 4/4. |
| Wrappers individuales ejecutables | 4/4 sin error. |
| SVG válido | 4/4. |
| PNG de alta resolución | 4/4 a 2400 × 1100 px. |
| CSV, README, caption, alt text y fuente | 4/4. |
| Ejes y unidades | Presentes en 4/4. |
| Escala declarada | 4/4 lineales; U02-CH004 declara el eje vertical truncado. |
| Datos fabricados | Ninguno; son valores calculados y declarados como modelo. |
| Codificación no dependiente solo del color | Conforme mediante trazo, marcador y rótulos directos. |
| Gráficos 3D | Ninguno. |

## Comprobaciones numéricas independientes

| recurso | comprobación | resultado |
|---|---|---|
| U02-CH001 | Para `F_neta = 2 N`, `a = F/m` | `2,0 m/s²` para 1 kg y `1,0 m/s²` para 2 kg. |
| U02-CH002 | `−(20 N/m)(0,020 m)` | `−0,40 N`; el extremo opuesto vale `+0,40 N`. |
| U02-CH003 | `−(2,0 N·s/m)(0,20 m/s)` | `−0,40 N`. |
| U02-CH004 | `331 + 0,6ϑ` para 0, 10, 20 y 30 °C | `331`, `337`, `343` y `349 m/s`. |
| Control U02-CH005 | `100/334 − 100/346` | `0,010384 s ≈ 10,4 ms`. |

## Revisión visual

Se inspeccionó `assets/generated/_review/u02_charts_contact_sheet.png` y los PNG individuales. En el primer render las etiquetas de los ejes horizontales quedaban demasiado próximas al límite inferior. Se aumentó el margen inferior y se regeneraron los cuatro gráficos.

Resultado final:

- no hay textos cortados;
- no hay leyendas innecesarias;
- las anotaciones no ocultan datos clave;
- las unidades son legibles;
- U02-CH002 y U02-CH003 distinguen el modelo ideal de una ley universal de tejidos;
- U02-CH004 declara que los puntos no son mediciones y que el eje vertical no comienza en cero.

## Problemas abiertos

No quedan problemas críticos ni mayores. La tabla nativa prevista para U02-CH005 se construirá durante el montaje del PowerPoint.

