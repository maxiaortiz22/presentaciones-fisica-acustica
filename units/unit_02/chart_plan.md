# Unidad 2 — Plan de gráficos cuantitativos

## Estado de implementación

**Implementado y validado el 2026-07-29.** U02-CH001–U02-CH004 se clasifican como **gráficos cuantitativos** y cuentan con script reproducible, `data.csv`, SVG, PNG de 2400 × 1100 px, README, caption, texto alternativo, fuente y metadatos. U02-CH005 permanece reemplazado por una tabla y dos trayectos; su cálculo de control se conserva en U02-CH004.

Salida: `units/unit_02/assets/generated/charts/`.

## Especificación común

- Diseño en el tamaño físico final del layout 16:9.
- Salida principal: SVG con texto editable cuando sea viable.
- Salida de respaldo/revisión: PNG de 2400 × 1350 px o recorte equivalente al área real.
- Tipografía: Calibri; ecuaciones en Cambria Math si se incorporan fuera del gráfico.
- Ejes: `FA_CARBON_900`; rejilla `FA_GRIS_200`; curva principal teal o bordó.
- Etiquetas de ejes: 20 pt o más; ticks y rótulos: 18 pt o más; anotaciones: 22 pt o más.
- Sin título duplicado dentro del asset.
- Datos de modelo claramente identificados; no se presentan como mediciones.
- Cada paquete futuro deberá incluir `script.py`, `data.csv`, SVG, PNG, `README.md`, caption, alt text y fuente.

## Plan detallado

| chart_id | slides | pregunta que responde | variables y unidades | escala | datos o modelo | anotaciones | formato | script necesario | validaciones | estado |
|---|---|---|---|---|---|---|---|---|---|---|
| U02-CH001 | U02-018; apoyo a U02-036 | ¿Cómo cambia `a` cuando aumenta `F_neta` y qué cambia al duplicar la masa? | x: `F_neta` (N); y: `a` (m/s²); series `m = 1,0 kg` y `m = 2,0 kg` | Lineal; x 0–4 N; y 0–4,5 m/s²; ticks enteros | `a = F_neta/m`; `F_neta = 0, 1, 2, 3, 4 N`; datos exactos calculados | Marcar `F_neta = 2 N`: `a = 2,0 m/s²` y `1,0 m/s²`; rotular directamente cada recta; pendiente `1/m` | SVG + PNG + CSV | `units/unit_02/scripts/u02_plot_001_aceleracion_fuerza.py` | Ambas rectas pasan por origen; valores coinciden con `F/m`; ejes/unidades visibles; máximo dos series; no interpretar masa como peso | implemented_validated |
| U02-CH002 | U02-038 | ¿Por qué `F_el` apunta hacia el equilibrio y qué representa la pendiente? | x: `x` (mm); y: `F_el` (N); parámetro `k_s = 20 N/m` | Lineal simétrica; x -20–20 mm; y -0,45–0,45 N | `F_el = -k_s x`; script convierte mm a m; modelo lineal ideal | Origen “equilibrio”; puntos `x=+20 mm → F=-0,40 N` y `x=-20 mm → F=+0,40 N`; flechas de retorno | SVG + PNG + CSV; versión recortada para mini gráfico | `units/unit_02/scripts/u02_plot_002_fuerza_elastica.py` | Signo y conversión mm→m; pendiente negativa; unidades de `k_s`; ejes cruzan origen; rótulo “modelo lineal ideal” | implemented_validated |
| U02-CH003 | U02-040 | ¿Cómo depende la fuerza de amortiguamiento de la velocidad? | x: `v` (m/s); y: `F_amort` (N); `b = 2,0 N·s/m` | Lineal simétrica; x -0,20–0,20 m/s; y -0,45–0,45 N | `F_amort = -bv`; puntos cada 0,05 m/s | Origen; `v=+0,20 m/s → F=-0,40 N`; rótulo “se opone a `v`”; zona completa declarada como modelo viscoso lineal | SVG + PNG + CSV; versión recortada | `units/unit_02/scripts/u02_plot_003_fuerza_amortiguamiento.py` | Signo, unidad de `b`, producto `bv` en N; pendiente `-b`; no presentar como ley universal de tejidos | implemented_validated |
| U02-CH004 | U02-080;U02-081;U02-103 | ¿Cuánto aumenta `c` en el rango ambiental y qué no permite concluir el gráfico? | x: `ϑ` (°C); y: `c` (m/s) | Lineal; x 0–30 °C; y 325–355 m/s; eje vertical truncado declarado | `c = 331 m/s + [0,6 (m/s)/°C]·ϑ`; puntos 0, 10, 20, 30 °C → 331, 337, 343, 349 m/s | Rótulo “modelo para aire seco y rango ambiental”; destacar 20 y 30 °C; aviso “el eje vertical no comienza en 0” | SVG + PNG + CSV; variante con puntos revelables | `units/unit_02/scripts/u02_plot_004_velocidad_temperatura.py` | Verificar cuatro puntos; pendiente 0,6; unidades del coeficiente; no suavizado; rango truncado visible; no inferir frecuencia o pitch | implemented_validated |
| U02-CH005 | U02-103 | ¿Cuánto cambia el tiempo en 100 m entre 5 °C y 25 °C? | `ϑ` (°C), `c` (m/s), `t` (s), `d=100 m` | Evaluada con eje completo 0–0,31 s y eje estrecho | `c(5)=334 m/s`, `c(25)=346 m/s`; `t(5)=0,299401 s`, `t(25)=0,289017 s`; diferencia ≈ 0,010384 s = 10,4 ms | Comparación numérica y advertencia de escala | Tabla nativa + dos trayectos; no generar gráfico final | cálculo incorporado a `u02_plot_004_velocidad_temperatura.py` para verificación; sin script separado | El eje completo oculta la diferencia y el eje truncado la exagera; una tabla comunica mejor el resultado | replaced |

## Datos previstos

### U02-CH001

| `F_neta` (N) | `a`, `m=1,0 kg` (m/s²) | `a`, `m=2,0 kg` (m/s²) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1,0 | 0,5 |
| 2 | 2,0 | 1,0 |
| 3 | 3,0 | 1,5 |
| 4 | 4,0 | 2,0 |

### U02-CH004

| `ϑ` (°C) | `c` (m/s) |
|---:|---:|
| 0 | 331 |
| 10 | 337 |
| 20 | 343 |
| 30 | 349 |

Los CSV futuros conservarán punto decimal para compatibilidad con Python; el render visible usará coma decimal en español.

## Arquitectura de scripts prevista

| archivo | función | entradas | salidas | dependencias |
|---|---|---|---|---|
| `units/unit_02/scripts/u02_chart_style.py` | Tokens visuales, tamaños, metadatos y helpers de exportación. | Configuración de figura y rutas. | Estilo común y validaciones de canvas. | Matplotlib, pathlib. |
| `units/unit_02/scripts/u02_plot_001_aceleracion_fuerza.py` | Generar U02-CH001. | Masas y vector de fuerzas. | SVG, PNG, CSV, README y textos. | NumPy, Matplotlib. |
| `units/unit_02/scripts/u02_plot_002_fuerza_elastica.py` | Generar U02-CH002. | `k_s`, rango de `x`. | SVG, PNG, CSV, README y textos. | NumPy, Matplotlib. |
| `units/unit_02/scripts/u02_plot_003_fuerza_amortiguamiento.py` | Generar U02-CH003. | `b`, rango de `v`. | SVG, PNG, CSV, README y textos. | NumPy, Matplotlib. |
| `units/unit_02/scripts/u02_plot_004_velocidad_temperatura.py` | Generar U02-CH004 y verificar U02-CH005. | Intercepto, pendiente, temperaturas y distancia. | SVG, PNG, CSV, README; tabla de tiempos de control. | NumPy, Matplotlib. |
| `units/unit_02/scripts/u02_generate_all_charts.py` | Regeneración integral y hoja de contacto. | Sin argumentos obligatorios. | Cuatro paquetes, reporte JSON y contacto PNG. | Scripts anteriores. |

La arquitectura se implementó. `u02_generate_all_charts.py` regenera los cuatro paquetes y la hoja de contacto; los cuatro wrappers individuales fueron ejecutados nuevamente sin errores.

## Anotaciones, caption y texto alternativo

| chart_id | caption propuesto | texto alternativo mínimo |
|---|---|---|
| U02-CH001 | “Modelo exacto `a=F_neta/m`: con la misma fuerza neta, la masa de 2,0 kg acelera la mitad que la de 1,0 kg.” | Gráfico lineal de aceleración frente a fuerza neta para 1 y 2 kg; ambas rectas parten del origen y la de menor masa tiene mayor pendiente. |
| U02-CH002 | “En el modelo lineal, la fuerza elástica cambia de signo con el desplazamiento y apunta al equilibrio.” | Recta descendente de fuerza elástica frente a desplazamiento, con origen en equilibrio y fuerzas opuestas al signo de x. |
| U02-CH003 | “El modelo viscoso lineal produce una fuerza proporcional y opuesta a la velocidad.” | Recta descendente de fuerza de amortiguamiento frente a velocidad, que cruza el origen. |
| U02-CH004 | “Aproximación para aire seco en rango ambiental; el eje vertical 325–355 m/s no comienza en cero.” | Recta de velocidad del sonido frente a temperatura desde 331 m/s a 0 °C hasta 349 m/s a 30 °C. |

## Validación obligatoria

1. Ejecutar cada script desde la raíz sin edición manual.
2. Verificar que existan SVG, PNG, CSV y metadatos.
3. Comparar puntos seleccionados con cálculo independiente.
4. Confirmar unidades, signo, rango y condiciones del modelo.
5. Simular la inserción en el layout real y renderizar a 16:9.
6. Revisar textos cortados, leyendas, anotaciones y márgenes.
7. Comprobar legibilidad a 25 % de zoom.
8. Asegurar que color no sea la única codificación.
9. Corregir y renderizar otra vez hasta cero problemas críticos o mayores.
