# Unidad 2 — Necesidades iniciales de diagramas

## Alcance

El storyboard contiene **72 slides candidatas para `diagram-generation`**:

- 48 centrales;
- 11 complementarias;
- 13 de respaldo.

No implican 72 ilustraciones independientes. Se organizan en 15 familias con una gramática visual común y variantes pedagógicas. Cada variante debe diseñarse en el tamaño real de la slide y permanecer editable en PowerPoint.

Se considera candidata toda slide que requiera cajas, conectores, flechas de fuerza o flujo, fronteras de sistema, callouts sobre símbolos o ecuaciones anotadas. Los gráficos con ejes se especifican aparte en `initial_chart_needs.md`.

## Familias de diagramas

| diagram_id | slides candidatas | clase y función | elementos estructurales | construcción o revelado | fuente | prioridad | estado |
|---|---|---|---|---|---|---|---|
| U02-DG-001 | U02-002, U02-006 | Diagrama conceptual de apertura y mapa de transferencia | Membrana entre dos regiones; nodos sistema → leyes → respuesta → energía → aplicación | Abrir con la membrana sin formalismo; recuperar el mismo fenómeno en el mapa con etiquetas de bloque | TEX 2.3; PDF pp. 38, 40; BR | alta | candidata |
| U02-DG-002 | U02-008–013 | Sistema, interacción, eje, signos y fuerza neta | Frontera de sistema; agente externo; flechas ancladas; eje positivo; suma vectorial unidimensional; caso equilibrado | Una decisión por slide: frontera → interacción → signo → resultante → equilibrio → primera ley | TEX 2.4.1–2.4.2; PDF pp. 38–39 | alta | candidata |
| U02-DG-003 | U02-016, U02-017, U02-019, U02-020 | Segunda ley y proporcionalidades | Cadena fuerza neta → aceleración; ecuación anotada; diagrama de cuerpo libre; dos masas comparables | Separar lectura causal, ecuación, ejemplo con signos y comparación de masas | TEX 2.4.2; PDF p. 39; ejercicios C2/NA2 | alta | candidata |
| U02-DG-004 | U02-021, U02-022, U02-093 | Tercera ley y contraejemplos | Dos cuerpos separados; par de flechas iguales y opuestas; dos diagramas de cuerpo libre; equilibrio como comparación | Mostrar interacción en conjunto y luego distribuir cada fuerza en el diagrama del cuerpo correspondiente | TEX 2.4.2 y errores; PDF pp. 39, 48–49 | alta | candidata |
| U02-DG-005 | U02-025, U02-027–032 | Presión, superficie y fuerza | Dos presiones opuestas; normal de superficie; `Δp`; área `S`; ecuación anotada; cadena `Δp → F_pres → F_neta → a` | Revelar fuerzas de cada lado antes de sustituirlas por `Δp`; cerrar con recap causal | TEX 2.3–2.4.3 y figura 2.1; PDF pp. 38–40 | alta | candidata |
| U02-DG-006 | U02-035–046 | Modelo masa–resorte–amortiguador | Masa, resorte, amortiguador, equilibrio, `x`, `v`, fuerzas restauradora y disipativa; balance instantáneo | Construcción por capas: inercia → elasticidad → amortiguamiento → modelo completo → signos → ejemplo → recap | TEX 2.5 y figura 2.2; PDF pp. 41–43 | crítica | candidata |
| U02-DG-007 | U02-048–057 | Trabajo, formas y balance de energía | Fuerza y desplazamiento; ecuaciones anotadas; depósitos cualitativos; frontera; rutas de entrada, almacenamiento, salida y disipación | Introducir una forma por vez; después conectar rutas; usar recap para cambiar de “forma” a “balance” | TEX 2.6 y figura 2.4; PDF pp. 43–44, 48 | crítica | candidata |
| U02-DG-008 | U02-059, U02-062–066 | Estado, transferencias y primera ley | Frontera de sistema; tarjetas temperatura, `U`, calor y trabajo; flechas de entrada/salida; convención de signos; ecuación anotada | Clasificar antes de formalizar; mantener orientación de flechas estable; ejemplo después de declarar convención | PO; TEX 2.7.1–2.7.2; PDF pp. 44–45 | crítica | candidata |
| U02-DG-009 | U02-071, U02-073, U02-105 | Entropía, irreversibilidad y puente mecánico-térmico | Desigualdad anotada; proceso reversible/real; ruta energía mecánica organizada → energía interna → aumento de entropía total | Evitar metáfora de desorden; mostrar dirección y condición del sistema total aislado | PO; TEX 2.7.3; PDF pp. 45–46 | alta | candidata |
| U02-DG-010 | U02-078, U02-079, U02-082, U02-101–103 | Propagación, temperatura y límites | Partícula local y frente de perturbación; ecuaciones de `c`; árbol de variables; control dimensional; trayectos a distancia fija | Separar movimiento local de propagación; tendencia lineal antes de ecuación general; límites al final | TEX 2.7.4; PDF pp. 46–47, 52, 57 | media | candidata |
| U02-DG-011 | U02-084, U02-086, U02-087 | Mapa de aplicaciones, oído medio y vibrador óseo | Cinco aplicaciones conectadas a cuatro ideas; ruta de energía pasiva; dos cuerpos en contacto | Empezar por selección de modelo; evitar un bloque anatómico; tercera ley reaparece en contacto | TEX 2.8; PDF pp. 46–48; REF stenfeltGoode2005 | alta | candidata |
| U02-DG-012 | U02-088, U02-089 | Integración y cierre | Árbol “qué se conoce → qué relación corresponde”; cadena presión → fuerza → movimiento → energía → disipación → unidades futuras | U02-088 sirve como actividad; U02-089 como síntesis, no como duplicado del mapa inicial | TEX I1; PDF pp. 53–54, 58–59; CM/CDM | alta | candidata |
| U02-DG-013 | U02-091, U02-092 | Referencia de signos y devolución diagnóstica | Eje, frontera, flechas y cuatro mini contraejemplos | Mantenerlos como respaldo; no mostrar soluciones antes de discutir | BR; TEX ejercicios D1–D4; PDF pp. 50, 53 | media | candidata |
| U02-DG-014 | U02-095, U02-096 | Referencia y solución del modelo mecánico | Mini modelo con etiquetas y unidades; diagrama de fuerzas junto al cálculo completo | Diseñar para consulta; dividir U02-096 durante producción si compromete 22 pt | TEX 2.5.3; PDF pp. 41–42 | media | candidata |
| U02-DG-015 | U02-104, U02-106–108 | Respaldos termodinámicos e integradores | Fronteras y flechas de signo; mapa de datos; modelo de superficie; ruta de energía; callouts de límite | Conservar plan, mecánica, energía y límites en slides separadas | TEX NG4 e I1; PDF pp. 51, 56, 58–59 | media | candidata |

## Especificación por familia

### U02-DG-001 — Apertura

- U02-002: dos regiones de aire, una superficie flexible y dos flechas normales; no mostrar todavía `Δp·S`.
- U02-006: cinco nodos de curso conectados; cada nodo incluye una sola pregunta, no una lista de contenidos.
- Repetición intencional: la membrana reaparece para convertir una observación en un mapa de modelos.

### U02-DG-002 — Sistema y fuerza neta

- La frontera del sistema debe ser visible antes de dibujar fuerzas.
- Cada flecha debe comenzar o terminar en el cuerpo correspondiente, sin atravesar texto.
- El eje positivo se mantiene en la misma orientación dentro de la secuencia.
- U02-012 y U02-013 deben compartir geometría, pero cambiar la pregunta: equilibrio instantáneo frente a velocidad constante.

### U02-DG-003 y U02-DG-004 — Leyes de Newton

- La segunda ley debe rotular `F_neta = ΣF`, no una fuerza aislada.
- En la tercera ley, nunca ubicar el par completo dentro de un solo diagrama de cuerpo libre.
- Los dos cuerpos deben tener nombres o identificadores distintos además del color.
- Los casos complementarios deben variar la masa o el sistema, no repetir el mismo ejemplo con otros números.

### U02-DG-005 — Presión y fuerza

- Conservar la semántica espacial izquierda/derecha de la figura del libro.
- Adaptar el símbolo visible de área a `S`, con nota de trazabilidad respecto de `A` en el capítulo.
- U02-029 debe mostrar cancelación dimensional sin reducir la ecuación por debajo de 28 pt.
- U02-031 debe rotular la membrana real como superficie distribuida, no como una masa puntual.

### U02-DG-006 — Masa–resorte–amortiguador

- Diseñar primero el modelo completo en el tamaño final y derivar versiones parciales.
- Reservar corredores independientes para `F_ext`, `F_el` y `F_amort`.
- No superponer los rótulos `x`, `v` y las fuerzas sobre el resorte o amortiguador.
- U02-043 requiere cuatro estados de signo; si no caben a 22 pt, dividir durante producción.
- U02-044 debe revelar el procedimiento y no convertir el cálculo en una captura de texto.
- U02-045 compara mecanismos; no debe sugerir que amortiguamiento, atenuación y disipación son magnitudes equivalentes.

### U02-DG-007 — Energía

- Usar anchos de flecha uniformes: no existe información cuantitativa para un Sankey.
- Diferenciar “energía en el sistema” de “energía que cruza la frontera”.
- U02-054 introduce las rutas; U02-055 formaliza el balance; U02-057 recapitula el cambio de forma. Esta repetición es pedagógica.
- Las ecuaciones de energía deben conservar símbolos, unidades y condiciones visibles.

### U02-DG-008 y U02-DG-009 — Termodinámica

- Orientación estable: flechas hacia el sistema son positivas bajo `ΔU = Q_calor + W_sobre`.
- Temperatura y energía interna se ubican dentro de la frontera; calor y trabajo se rotulan en el cruce de la frontera.
- La entropía no se representará como “desorden” mediante objetos desparramados.
- U02-073 debe mostrar una ruta de conversión y una condición de irreversibilidad, no una pérdida de energía.

### U02-DG-010 — Propagación

- La partícula marcada oscila localmente; la perturbación recorre el espacio.
- U02-079 se coordina con U02-CH-004: el diagrama explica la ecuación y el gráfico aporta lectura cuantitativa.
- En U02-101 y U02-102, cada parámetro de la ecuación general debe tener callout y unidad.
- U02-103 combina gráfico y dos trayectos; reservar una zona independiente para cada clase visual.

### U02-DG-011 y U02-DG-012 — Aplicación e integración

- Las aplicaciones se conectan a conceptos físicos, no a conclusiones clínicas.
- La ruta del oído medio debe indicar “sistema pasivo” y evitar cifras de ganancia sin fuente.
- El vibrador óseo exige dos cuerpos y dos fuerzas de contacto.
- El cierre recupera la cadena causal, pero agrega límites y unidades futuras: no repite literalmente U02-006.

## Reglas geométricas obligatorias para producción

- Texto principal de diagramas: 24 pt preferido, 22 pt mínimo.
- Etiquetas breves de conectores: 20 pt mínimo.
- Ecuaciones centrales: 28 pt mínimo.
- Margen interior: al menos 0,18 pulgadas.
- Espacio libre dentro de cada caja: entre 10 % y 20 %.
- Separación mínima entre línea y texto no relacionado: 0,10 pulgadas.
- Conectores anclados a los bordes; usar codos cuando una recta atraviese contenido.
- Ninguna punta, línea o líder puede tocar o cubrir texto.
- No usar “shrink text to fit”.
- Dividir la slide si el contenido no cumple los mínimos.

## Ciclo de aceptación

Cada diagrama deberá:

1. generarse en el tamaño real de uso;
2. renderizarse a 16:9;
3. revisarse por desborde, clipping, colisiones, anclajes, dirección de flechas y tamaño tipográfico;
4. corregirse en geometría o redacción;
5. volver a renderizarse;
6. repetirse hasta no presentar problemas críticos o mayores.

La ejecución correcta de un script no constituye aprobación visual.

## Priorización

La primera tanda de producción debería cubrir U02-DG-002, U02-DG-004, U02-DG-005, U02-DG-006, U02-DG-007 y U02-DG-008. Esas familias concentran los mayores riesgos conceptuales. Los diagramas de respaldo se derivarán después de aprobar las versiones centrales, sin reducir tamaño tipográfico.

