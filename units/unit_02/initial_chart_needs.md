# Unidad 2 — Necesidades iniciales de gráficos cuantitativos

## Criterio

Los gráficos de esta unidad deben responder una pregunta física concreta y derivarse de ecuaciones o valores trazables. En la fase de producción se generarán de forma reproducible con Python, NumPy y Matplotlib, preferentemente en SVG editable y PNG de alta resolución.

No se usarán curvas decorativas, datos anatómicos inventados ni ejes truncados sin advertencia visible.

## Inventario

| chart_id | slides previstas | pregunta que responde | variables y unidades | modelo o datos | representación propuesta | fuente | salida prevista | decisiones antes de producir | prioridad | estado |
|---|---|---|---|---|---|---|---|---|---|---|
| U02-CH-001 | U02-018 y apoyo a U02-036 | ¿Cómo cambia la aceleración al aumentar la fuerza neta y qué papel cumple la masa? | eje x: `F_neta` en N; eje y: `a` en m/s²; dos valores de `m` en kg | `a = F_neta/m`; datos sintéticos exactos calculados | dos rectas desde el origen con masas claramente rotuladas; igual rango para comparación | TEX 2.4.1–2.4.2; PDF pp. 38–39; elaboración didáctica | SVG + PNG; variante con aparición progresiva de la segunda masa | elegir masas simples que no sugieran anatomía; fijar rango y cantidad de marcas | alta | pendiente de `chart-generation` |
| U02-CH-002 | U02-038 | ¿Qué expresa el signo de la fuerza elástica y qué representa la pendiente? | eje x: `x` en m o mm; eje y: `F_el` en N | `F_el = -k_s x`; modelo lineal ideal | recta de pendiente negativa con origen, zonas `x>0` y `x<0`, flechas de retorno | TEX 2.5.2; PDF p. 41 | SVG + PNG | decidir unidad de desplazamiento y un `k_s` didáctico; declarar zona lineal ideal | media | pendiente de `chart-generation` |
| U02-CH-003 | U02-040 | ¿Cómo cambia la fuerza de amortiguamiento cuando cambia la velocidad? | eje x: `v` en m/s; eje y: `F_amort` en N | `F_amort = -b v`; modelo viscoso lineal | recta de pendiente negativa con comparación cualitativa de dos valores de `b` solo si ayuda | TEX 2.5.2; PDF pp. 41–42 | SVG + PNG | decidir si una o dos pendientes; evitar adelantar coeficientes de tejidos reales | media | pendiente de `chart-generation` |
| U02-CH-004 | U02-080, U02-081 y apoyo a U02-103 | ¿Cuánto cambia la velocidad de propagación del sonido con la temperatura dentro del rango ambiental? | eje x: `ϑ` en °C; eje y: `c` en m/s | `c ≈ 331 m/s + [0,6 (m/s)/°C]·ϑ`; puntos de control: 0, 10, 20 y 30 °C | recta y marcadores; eje vertical aproximadamente 325–355 m/s con advertencia explícita de truncamiento | TEX 2.7.4 y figura 2.3; PDF pp. 46–47 | SVG + PNG; variante con revelado de recta y puntos | confirmar glifo de temperatura; decidir rango exacto; incluir “aire seco, rango ambiental” | alta | pendiente de `chart-generation` |
| U02-CH-005 | U02-103 | ¿Cómo repercute el cambio de `c` en el tiempo de propagación sobre una distancia fija? | eje x: `ϑ` en °C; eje y: `t` en s o ms; `d = 100 m` | `c(ϑ)` anterior y `t=d/c`; valores de NA5 para 5 °C y 25 °C | dos puntos o curva estrecha con diferencia de tiempo anotada; alternativa: tabla si la diferencia no se lee bien | TEX ejercicio NA5 y solución; PDF pp. 52, 57 | SVG + PNG o tabla nativa, según legibilidad | comprobar magnitud de la diferencia; no exagerarla mediante un eje engañoso | baja; respaldo | pendiente de decisión |

## Gráficos descartados por ahora

| propuesta descartada | motivo |
|---|---|
| Sankey cuantitativo de energía auditiva | El capítulo no aporta proporciones de flujo; un ancho de banda sugeriría datos inexistentes. |
| Curvas temporales del oscilador amortiguado | Exigirían fijar condiciones iniciales y resolver una evolución que excede el objetivo de U2; una animación cualitativa es suficiente. |
| Curva “entropía frente al tiempo” | Sin proceso y datos definidos sería una ilustración arbitraria, no un gráfico cuantitativo. |
| Datos clínicos de membrana, oído medio o conducción ósea | No son necesarios para el objetivo y requerirían bibliografía y condiciones experimentales específicas. |

## Especificaciones comunes

- Ejes con magnitud, símbolo y unidad.
- Escala declarada y, si se trunca, advertencia visible.
- Leyenda solo cuando existan dos o más series que no puedan rotularse directamente.
- Paleta consistente con el sistema visual y diferenciación adicional mediante trazo, marcador o rótulo.
- Tamaño tipográfico verificado en el espacio real de la slide.
- Script reproducible guardado posteriormente bajo `units/unit_02/scripts/`.
- Fuente de datos o ecuación incorporada al caption o a las notas.
- Parámetros didácticos identificados como tales y nunca presentados como valores anatómicos.
- Control dimensional y verificación manual de, al menos, dos puntos por gráfico.

## Carga de producción

Se prevén cuatro gráficos necesarios y un gráfico de respaldo sujeto a prueba de legibilidad. U02-CH-004 es el único que reproduce directamente una figura cuantitativa del capítulo; los demás son elaboraciones didácticas basadas en sus ecuaciones.

