# Unidad 3 — Necesidades iniciales de diagramas estructurales

## Criterio

Las slides enumeradas aquí son candidatas explícitas para `diagram-generation`. Se construirán con formas, textos, ecuaciones y conectores editables de PowerPoint, respetando corredores de flechas, márgenes interiores y tamaños mínimos establecidos en `AGENTS.md`. Los gráficos cuantitativos incrustados provendrán de `initial_chart_needs.md`; no se redibujarán a mano.

## Paquetes de diagramas

| diagram_id | slides | función | estructura estimada | complejidad | requisito de diseño |
|---|---|---|---|---|---|
| U03-DG01 | U03-002, U03-015, U03-079 | Cadena fuente–medio–receptor | 3–5 nodos, 2–4 conectores, flechas locales y de propagación | media | Dos códigos de flecha inequívocos; texto breve por nodo. |
| U03-DG02 | U03-006, U03-016, U03-047, U03-059, U03-069, U03-078, U03-081 | Mapa progresivo de la unidad | 9 nodos breves, 8 conectores, estados de avance | alta | Diseñar una familia reutilizable; el mapa final puede ocupar slide completa. |
| U03-DG03 | U03-008, U03-020–021 | Estados de una oscilación | 3–5 estados, eje, signos, flechas y callouts | media | Mantener equilibrio y escala visual constante. |
| U03-DG04 | U03-009–010, U03-014 | Movimiento local y frente | 4–5 instantáneas, partículas y dos tipos de flecha | alta | Reservar corredores; evitar que el frente atraviese etiquetas. |
| U03-DG05 | U03-011–012 | Medio e interacción; longitudinal/transversal | Dos paneles y 3–4 callouts por panel | media | La sinusoide transversal no debe sugerir movimiento vertical del aire. |
| U03-DG06 | U03-018–019 | Modelo masa–resorte y ecuación restauradora | Sistema físico, eje, 4 callouts y ecuación anotada | alta | Usar `k_s`; distinguir posición, fuerza y aceleración. |
| U03-DG07 | U03-026, U03-065, U03-084 | Correspondencia ciclo–fase–sinusoide | Círculo, señal y 4–5 conectores | alta | Mantener convención angular idéntica en las tres slides. |
| U03-DG08 | U03-027 | Matriz de parámetros del MAS | Cuatro celdas y una señal común | baja | No repetir definiciones completas; pregunta, símbolo y unidad. |
| U03-DG09 | U03-029 | Ecuación temporal anotada | Ecuación central y 5 callouts | media | Ecuación ≥28 pt; conectores sin cruzar símbolos. |
| U03-DG10 | U03-031–032 | Estados cualitativos de `x`, `v` y `a` | Cuatro estados, dos variables por versión | alta | Reutilizar geometría y cambiar la tarea; no encoger texto. |
| U03-DG11 | U03-036 | Trayectoria real frente a gráfico | Dos paneles y 3 conectores explicativos | media | Ejes y referentes explícitos. |
| U03-DG12 | U03-037–038 | Niveles de evidencia y checklist | 3 niveles o 4 preguntas conectadas a una señal | media | Separar escala, unidad y calibración. |
| U03-DG13 | U03-040 | Definición y expresión de tono puro | Ecuación, señal y banda de hipótesis | media | Declarar variable genérica `s`; evitar unidad ficticia. |
| U03-DG14 | U03-042, U03-047 | Cadena de transducción | 4 nodos, 3 conectores y variables/unidades | alta | Conectores rotulados como transformación; no igualar amplitudes. |
| U03-DG15 | U03-043–044 | Cono, partículas, compresión y rarefacción | 2–3 estados, partículas y flechas | alta | Separar desplazamiento local y propagación; slide completa para U03-044. |
| U03-DG16 | U03-046 | Cadena de calibración audiométrica | 4 nodos y 3 conectores, callout de calibración | media | No sugerir interpretación clínica ni certificar equipos. |
| U03-DG17 | U03-049 | Tabla conceptual de `ξ(x,t)` | Cuadrícula 3×3 y dos cortes destacados | media | Evitar densidad numérica; función de orientación. |
| U03-DG18 | U03-053 | Comparación `T`–`λ` | Dos gráficos generados, tabla 2×2 y conectores de fase | alta | Conservar datos de U03-CH07 y ejes legibles. |
| U03-DG19 | U03-055–056 | Onda viajera y derivación conceptual de `c=λf` | Ecuación anotada, dos snapshots y 4–6 callouts | alta | Puede requerir dos zonas; no superar cuatro ideas visibles. |
| U03-DG20 | U03-062, U03-069 | Comparación `u`–`c` y control verbal | Dos referentes, flechas y matriz 2×2 | media | Mismo color para `u` en todas las slides y otro para `c`. |
| U03-DG21 | U03-071 | Suma instantánea | Ecuación y tres instantes de dos contribuciones | alta | Separar valor instantáneo de amplitud. |
| U03-DG22 | U03-076 | Cancelación activa y zona de reducción | 5 nodos, 5 conectores y región espacial | alta | Declarar límites fuera del flujo; no cruzar la zona con texto. |
| U03-DG23 | U03-077 | Aplicaciones de superposición | Dos mini cadenas de hasta 3 nodos | media | No introducir resonancia, filtrado ni anatomía detallada. |
| U03-DG24 | U03-080–081, U03-095 | Caso integrador y síntesis | Cadena física, dos gráficos y flujo de resolución | muy alta | Diseñar a tamaño final; dividir U03-095 si el contenido no entra a 22 pt. |
| U03-DG25 | U03-085–092 | Ecuaciones de respaldo anotadas | 3–6 callouts por ecuación; comparaciones laterales | media–alta | Mantener símbolos de `notation_guide.md`; no usar shrink-to-fit. |

## Prioridad de producción

1. **Crítica:** U03-DG02, U03-DG04, U03-DG14, U03-DG15, U03-DG18, U03-DG19, U03-DG20 y U03-DG24.
2. **Alta:** U03-DG03, U03-DG06, U03-DG07, U03-DG09, U03-DG10, U03-DG21 y U03-DG22.
3. **Media o respaldo:** paquetes restantes.

## Controles posteriores obligatorios

- Generar en el tamaño real del layout indicado en `storyboard.md`.
- Renderizar cada diagrama dentro de la slide, no solo como objeto aislado.
- Comprobar clipping, desbordes, tamaño tipográfico, líneas sobre texto y puntas de flecha.
- Mantener al menos 0,18 pulgadas de margen interior y 10–20 % de aire dentro de cada caja.
- Reutilizar geometría solo cuando cambie la tarea cognitiva de manera explícita.
- Dividir U03-DG19 o U03-DG24 si la legibilidad exige bajar de los mínimos de `AGENTS.md`.

