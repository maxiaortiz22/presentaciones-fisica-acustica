# Unidad 4 — Necesidades iniciales de diagramas

## Alcance

Todas las familias de esta lista son candidatas explícitas para `diagram-generation`. Se producirán con formas, texto, ecuaciones y conectores editables de PowerPoint, diseñados en su tamaño final. Las familias reúnen slides que pueden compartir geometría sin repetir idéntico contenido.

| diagram_id | slides | familia | estructura prevista | layout/zona | complejidad | prioridad |
|---|---|---|---|---|---|---|
| U04-DG-001 | U04-002 | Situación inicial de medición | Fuente, medio, punto y receptor; cinco callouts externos. | FA_22, visual completo. | media | alta |
| U04-DG-002 | U04-006, 014, 107 | Mapa de la unidad | Tres líneas de hasta cuatro nodos; estados activo/completado; versión final integrada. | FA_03/FA_16/FA_17. | alta | alta |
| U04-DG-003 | U04-008–010 | Físico, perceptual y cadena | Comparación de dos dominios y cadena fuente–medio–campo–receptor. | FA_11/FA_12. | media | alta |
| U04-DG-004 | U04-012–013 | Generación vocal/electroacústica | Dos procesos de cuatro etapas; conectores causales y límites. | FA_13/FA_19. | media | media |
| U04-DG-005 | U04-016–019 | Propagación longitudinal | Partículas/regiones en 4–5 estados; flechas de movimiento, fuerza y avance semánticamente distintas. | FA_22/FA_12. | alta | alta |
| U04-DG-006 | U04-020–022 | Rapidez y cambio de medio | Ecuación `c`, ramas de tendencia, interfaz y `λ=c/f`. | FA_09/FA_15/FA_16. | media | alta |
| U04-DG-007 | U04-024–028 | Campo, presión y movimiento | Dos puntos/tiempos, equilibrio de presión y contraste `u/c`. | FA_08/FA_11. | media | alta |
| U04-DG-008 | U04-029–033, 113 | Impedancia y reflexión | Relación `p/u`, condiciones, interfaz con tres ondas y coeficientes. | FA_08/FA_09/FA_22/FA_23. | alta | alta |
| U04-DG-009 | U04-035, 037–038 | Intensidad | Producto y signos; ventana temporal; relaciones RMS condicionadas. | FA_09. | alta | alta |
| U04-DG-010 | U04-040–042 | Intensidad, potencia, energía y medición | Cadena `I→S→W_ac→Δt→E_ac` y proceso de sensor. | FA_06B/FA_09/FA_13. | alta | alta |
| U04-DG-011 | U04-045–050 | Descriptores temporales | Señal común con callouts y matriz descriptor–pregunta. | FA_11/FA_08/FA_16. | media | media |
| U04-DG-012 | U04-052–055, 111–112 | RMS | Proceso de tres nodos, ecuaciones anotadas y ventana común. | FA_12/FA_09/FA_23. | alta | alta |
| U04-DG-013 | U04-060–068, 114 | Niveles y referencias | Tríada magnitud–referencia–convención; ecuaciones `L_p/L_I/L_W`; derivación 10/20. | FA_08/FA_09/FA_11/FA_23. | alta | alta |
| U04-DG-014 | U04-070–080, 115 | Lógica de suma | Flujo señal→RMS→nivel; fase; rutas coherente/no correlacionada; árbol final. | FA_07/FA_09/FA_16/FA_23. | alta | alta |
| U04-DG-015 | U04-082–089, 116–117 | Frentes, geometrías y campos | Plano/cilindro/esfera; normales; recintos libre/reverberante/difuso; árbol de selección. | FA_08/FA_07/FA_11/FA_16. | alta | alta |
| U04-DG-016 | U04-091–097, 118 | Ley de distancia | Esferas, dos posiciones, ecuaciones y prueba de validez. | FA_22/FA_09/FA_15/FA_23. | alta | alta |
| U04-DG-017 | U04-098–102 | Directividad | Patrón ideal/real, comparación a igual potencia, ecuaciones `Q` y `DI`. | FA_08/FA_07/FA_09/FA_13. | alta | alta |
| U04-DG-018 | U04-104–107, 124 | Cadena de interpretación y caso | Seis nodos, condiciones, plano del caso y mapa final. | FA_13/FA_14/FA_17/FA_23. | alta | alta |
| U04-DG-019 | U04-106 | Errores integradores | Dos columnas, siete errores y correcciones breves. | FA_15. | media | media |
| U04-DG-020 | U04-123 | Distancia más directividad | Fuente direccional, dos puntos y cálculo por capas. | FA_23. | media | baja |

## Especificación geométrica inicial

- Texto principal: 24 pt preferido, nunca menos de 22 pt; etiquetas breves de conectores, 20 pt mínimo; ecuaciones centrales, 28 pt mínimo.
- Margen interior mínimo de 0,18 pulgadas y 10–20 % de aire dentro de cada caja.
- Conectores anclados a bordes, con corredores vacíos; ninguna flecha puede tocar texto.
- Usar conectores en codo cuando una trayectoria recta atraviese contenido.
- Los callouts se ubican fuera del objeto y sus líderes terminan antes del carácter o símbolo señalado.
- Si una familia no entra con estos mínimos, dividirla por estados o por slide; no aplicar reducción automática de texto.

## Reutilización sin redundancia

- U04-DG-002 cambia de mapa prospectivo a progreso y finalmente a síntesis; no es una repetición idéntica.
- U04-DG-010 parte de relaciones físicas y termina en límites de una medición.
- U04-DG-014 conserva la misma semántica cromática, pero cada aparición añade una decisión: señal, fase, condición o nivel.
- U04-DG-015 comparte geometría, pero separa frente ideal, ley cuantitativa y entorno reflectante.
- U04-DG-018 reutiliza el caso sin mostrar la solución hasta respaldo.

## Ciclo de aceptación obligatorio

1. Generar en el tamaño real de la zona de slide.
2. Renderizar a tamaño final.
3. Revisar desbordes, clipping, colisiones, conectores, etiquetas y tamaño tipográfico.
4. Corregir geometría o redacción.
5. Volver a renderizar y repetir hasta no tener problemas críticos o mayores.

La finalización correcta del script no constituye aprobación visual.
