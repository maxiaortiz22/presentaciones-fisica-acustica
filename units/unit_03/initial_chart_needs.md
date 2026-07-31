# Unidad 3 — Necesidades iniciales de gráficos cuantitativos

## Criterio

Todos los gráficos se producirán con datos calculados y scripts reproducibles. Deben incluir ejes, unidades, escala explícita y una nota que identifique si la amplitud es física o normalizada. Los gráficos coordinados deben derivarse del mismo dataset para que los cortes temporales y espaciales no se contradigan.

## Inventario inicial

| chart_id | slides | pregunta que responde | datos o modelo | ejes y unidades | salida prevista | prioridad | estado |
|---|---|---|---|---|---|---|---|
| U03-CH01 | U03-022–023 | ¿Cómo se leen período y frecuencia en registros de igual duración? | Sinusoides sintéticas de frecuencias simples. | `t` en s o ms; amplitud normalizada declarada. | SVG y PNG; dos variantes coordinadas. | alta | pendiente |
| U03-CH02 | U03-030 | ¿Qué aspecto tiene el desplazamiento de un cono de 500 Hz y 10 µm? | `x(t)=10 µm cos(2π·500 t)`. | `t` en ms; `x` en µm. | SVG editable y datos CSV. | media | pendiente |
| U03-CH03 | U03-033–034 | ¿Cómo se coordinan posición, velocidad y aceleración? | MAS normalizado con una frecuencia común. | `t/T`; variables normalizadas y rótulos de signo. | SVG de tres paneles y variante de pregunta. | media | pendiente |
| U03-CH04 | U03-035 | ¿Cómo puede la misma forma representar variables distintas? | Cuatro sinusoides de forma semejante con escalas deliberadamente distintas. | `t`; `x`, `ξ`, `p` y `V` con unidades declaradas o esquema cualitativo. | SVG de pequeños múltiples. | media | pendiente |
| U03-CH05 | U03-041 | ¿En qué difiere un tono real de una sinusoide infinita? | Sinusoide con envolvente de ataque y caída. | `t` en s; amplitud normalizada. | SVG y audio U03-AS05. | media | pendiente |
| U03-CH06 | U03-045 | ¿Qué registra un micrófono en una posición fija? | Presión acústica sinusoidal relativa a la presión ambiente. | `t` en ms; `p` en Pa si se fija amplitud o normalizada si no. | SVG; decisión de escala pendiente U3-D06. | alta | pendiente |
| U03-CH07 | U03-050–054, U03-059 | ¿Cómo se relacionan un mapa espacio–tiempo y sus dos cortes? | `ξ(x,t)=A_ξ cos(2πft-2πx/λ)` con parámetros simples y consistentes. | `x` en m; `t` en ms; `ξ` normalizada o en µm. | Mapa 2D, corte temporal, corte espacial y perfiles anotados desde un solo script. | crítica | pendiente |
| U03-CH08 | U03-058, U03-094 | ¿Puede el estudiante leer `T` y `λ` y calcular `c`? | Dataset propio con valores simples y distintos del ejemplo de 1000 Hz. | `t` en ms; `x` en m; amplitud normalizada. | Versiones ejercicio y solución, idénticas salvo anotaciones. | crítica | pendiente |
| U03-CH09 | U03-063 | ¿Qué cambia al variar `f` si el medio mantiene `c`? | Dos sinusoides espaciales con `λ=c/f`. | `x` en m; amplitud normalizada; valores de `f` y `λ`. | SVG comparativo. | alta | pendiente |
| U03-CH10 | U03-064–068 | ¿Cómo se reconoce una diferencia de fase? | Pares de sinusoides con `Δφ=0`, `π/2` y `π`. | `t/T` o `x/λ`; amplitud normalizada. | Familia SVG con código visual estable. | alta | pendiente |
| U03-CH11 | U03-066 | ¿Qué separación espacial corresponde a una diferencia de fase? | Perfil sinusoidal con puntos a `λ/4`, `λ/2` y `λ`. | `x/λ`; amplitud normalizada. | SVG anotado. | alta | pendiente |
| U03-CH12 | U03-072–075 | ¿Cómo cambia la suma con la fase? | `y_R=y₁+y₂` para amplitudes iguales y desfases seleccionados. | `t/T`; amplitud normalizada común. | Familia de gráficos de constructiva, destructiva, parcial y ejercicio. | alta | pendiente |
| U03-CH13 | U03-093 | ¿Cómo varía la amplitud resultante con `Δφ`? | `A_R/A=√(2+2cosΔφ)` para amplitudes iguales. | `Δφ` en rad; `A_R/A` adimensional. | SVG con puntos notables y datos CSV. | baja | pendiente |

## Reglas de producción

1. U03-CH07 y U03-CH08 deben compartir convención de dirección, color y fase.
2. Las curvas de interferencia deben conservar la misma escala vertical; no autoajustar cada panel.
3. Los gráficos de amplitud normalizada deben rotularlo en el eje, no solo en notas.
4. La señal de presión U03-CH06 no usará dB ni RMS: esos conceptos pertenecen a U4.
5. U03-CH03 es complementario y no debe condicionar la comprensión de la ruta central.
6. Cada script deberá registrar parámetros físicos, versión y fuente de datos; en esta unidad los datos son sintéticos y derivados de ecuaciones del capítulo.

