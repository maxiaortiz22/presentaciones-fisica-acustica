# Unidad 5 — Necesidades iniciales de diagramas y ecuaciones anotadas

## Alcance

El storyboard marca 91 slides como candidatas a `diagram-generation`. Para evitar producir 91 composiciones aisladas, este documento las organiza en familias reutilizables. Incluye diagramas conceptuales, procesos, escalas, tablas-mapa y ecuaciones anotadas; excluye los gráficos cuantitativos registrados en `initial_chart_needs.md`.

## Reglas de diseño obligatorias

- Crear con formas, textos, ecuaciones y conectores editables de PowerPoint siempre que sea posible.
- Diseñar en la zona real del layout y renderizar a tamaño final.
- Texto principal de 22 pt o más; 24 pt preferido; etiquetas de conectores de 20 pt o más; ecuaciones centrales de 28 pt o más.
- Margen interior mínimo de 0,18 in y 10–20 % de aire en cada caja.
- Conectores anclados y detrás de los nodos; reservar corredores libres; ninguna línea debe tocar texto.
- Dividir la slide antes de reducir tipografía por debajo de los mínimos.
- Aplicar el ciclo generar → renderizar → revisar colisiones/desbordes → corregir → volver a renderizar.

## Inventario de familias

| diagram_id | slides previstas | clase | estructura | función pedagógica | layout base | complejidad | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U05-DG-001 | U05-001, U05-006, U05-129 | mapa narrativo | Señal → representación → herramienta → medición → decisión | Orientar y cerrar la unidad con el mismo mapa evolucionado | FA_03_MAPA_CLASE / FA_21_CIERRE_PUENTE | alta | alta | especificar |
| U05-DG-002 | U05-003, U05-004, U05-007 | marco de lectura | Pregunta, objeto, eje horizontal, eje vertical y condiciones | Instalar la rutina común que reaparece en recaps | FA_14_PREGUNTA_EJERCICIO / FA_12_PROCESO | media | alta | especificar |
| U05-DG-003 | U05-010, U05-015, U05-018, U05-022–029 | ecuaciones anotadas | `x(t)`, `A`, `f`, `φ`, período, suma/serie/transformada | Estratificar el formalismo de Fourier sin abrir un curso de complejos | FA_09_ECUACION_INTERPRETACION | alta | alta | dividir en subfamilias |
| U05-DG-004 | U05-030–031, U05-033–040, U05-133–136 | proceso digital y ecuaciones | Captura → muestras → ventana → DFT → bins; relaciones `f_s,N,T_obs,Δf` | Hacer visible cómo una señal continua llega al espectro digital | FA_12_PROCESO / FA_09_ECUACION_INTERPRETACION | alta | alta | especificar |
| U05-DG-005 | U05-041–042, U05-047, U05-049–051, U05-137–140 | ventana y espectrograma | Selección/segmentación, rejilla tiempo–frecuencia, bin frente a banda | Explicar decisiones del análisis y metadatos mínimos | FA_12_PROCESO / FA_11_COMPARACION | alta | alta | especificar |
| U05-DG-006 | U05-052–062 | señal–sistema | `X(f)` → `H(f)` → `Y(f)`; respuesta, ganancia y condiciones | Evitar confundir espectro de señal con respuesta de sistema | FA_12_PROCESO / FA_09_ECUACION_INTERPRETACION | alta | alta | especificar |
| U05-DG-007 | U05-063–073, U05-141 | mapa terminológico | Fundamental, armónico, parcial, sobretono, envolvente y formante | Ordenar nombres relacionados sin tratarlos como sinónimos | FA_11_COMPARACION / FA_08_DEFINICION | media | alta | especificar |
| U05-DG-008 | U05-077, U05-079–083 | escalas condicionadas | Frecuencia y nivel con límites, condiciones y advertencias | Representar rangos sin convertir fronteras variables en constantes universales | FA_09_ECUACION_INTERPRETACION / FA_15_ERROR_FRECUENTE | media | alta | especificar |
| U05-DG-009 | U05-086–094, U05-142–143 | escala de bandas y ecuaciones | Razones, centros, límites y ancho sobre eje logarítmico | Construir octavas/tercios y separar bandas de armónicos | FA_09_ECUACION_INTERPRETACION / FA_10_EJEMPLO_RESUELTO | alta | alta | especificar |
| U05-DG-010 | U05-095–105, U05-144 | taxonomía de filtros | Entrada → filtro → salida; cuatro tipos y parámetros | Conectar respuesta frecuencial con función y aplicación | FA_12_PROCESO / FA_11_COMPARACION | alta | alta | especificar |
| U05-DG-011 | U05-106–116, U05-145 | cadena de ponderación | Espectro → corrección por frecuencia → integración → descriptor | Diferenciar A/C/Z, audición y escalas clínicas | FA_12_PROCESO / FA_09_ECUACION_INTERPRETACION | alta | alta | especificar |
| U05-DG-012 | U05-117–124, U05-146–148 | cadena de medición | Micrófono → preamplificación → ponderación → detector/integración → resultado; ficha de metadatos | Integrar instrumento, configuración, `L_eq`, máximo y pico | FA_12_PROCESO / FA_10_EJEMPLO_RESUELTO | muy alta | alta | probable división |
| U05-DG-013 | U05-125–131 | selección e integración | Árbol de decisión y caso señal/sistema/medición | Elegir herramienta y justificar una inferencia profesional | FA_13_APLICACION_CLINICA / FA_17_RECAP_FINAL | alta | alta | especificar |
| U05-DG-014 | U05-017, U05-029, U05-040, U05-051, U05-062, U05-083, U05-094, U05-105, U05-116, U05-124 | recapitulación acumulativa | Rutina U05-DG-002 con un campo nuevo por bloque | Repetición pedagógica con recuperación activa | FA_16_RECAP_PARCIAL | media | alta | crear master de familia |
| U05-DG-015 | U05-149–150 | solución y glosario | Secuencia de resolución + índice de términos y retorno | Mantener detalle consultable sin interrumpir la ruta central | FA_23_APENDICE | media | media | especificar al final |

## Slides que requieren especial atención geométrica

| slide_id | motivo | decisión previa |
|---|---|---|
| U05-006 | Mapa de 12 hitos puede exceder tipografía mínima | Usar revelado progresivo o agrupar en cuatro tramos |
| U05-031 | Cadena digital de seis nodos | Dividir captura/representación si no entra a 24 pt |
| U05-056 | Cadena `X–H–Y` más ecuación y unidades | Reservar slide completa y mantener conectores detrás |
| U05-060 | Fuente–filtro de voz con dos niveles conceptuales | Separar mecanismo y lectura espectral si aparecen cruces |
| U05-091 | Centro, límites y ancho de banda | Priorizar ecuación y eje; mover derivación a respaldo |
| U05-106 | Cadena de ponderación con tres ramas | Máximo tres ramas y convergencia explícita |
| U05-117 | Cadena del sonómetro de seis etapas | Agrupar en transducción, procesamiento e informe |
| U05-126 | Caso integrador con señal y sistema | Dos zonas claras, pasos numerados y sin flechas diagonales |
| U05-129 | Mapa final acumulativo | Reutilizar geometría de U05-006, no rediseñar desde cero |

## Decisiones de reutilización

- U05-DG-001 tendrá versiones inicial, parcial y final con la misma geometría.
- U05-DG-002 será el componente recurrente de lectura; los recaps completarán un campo nuevo, no repetirán texto.
- U05-DG-014 derivará de un único master editable con variantes por bloque.
- Las ecuaciones se dividirán por propósito: definición, interpretación, ejemplo y respaldo; no se acumularán derivaciones en una sola slide.
- Las tablas nativas simples no se convertirán en diagramas de cajas si no hay una relación causal o espacial que lo justifique.

## Estado

**Inventario inicial.** No se produjeron diagramas finales. Las familias prioritarias deben pasar por `diagram-generation` y por su ciclo de render/revisión antes de redactar o montar el deck.
