# Unidad 10 — Necesidades iniciales de diagramas

## Criterio de producción

Todos los recursos de este inventario son **candidatos explícitos para `diagram-generation`**. Se producirán, de manera predeterminada, con formas, texto y conectores editables de PowerPoint. Los identificadores son provisionales pero estables para enlazar storyboard, scripts y revisión.

Antes de aprobar cada diagrama se deberá: diseñar en el tamaño real del layout, medir el texto, mantener al menos 0,18 in de margen interior y 10–20 % de aire en las cajas, usar texto principal de 22 pt o más (24 pt preferido), etiquetas breves de 20 pt o más y ecuaciones centrales de 28 pt o más. Los conectores deberán quedar anclados, con corredores libres, sin tocar texto. Cada pieza deberá renderizarse y corregirse hasta eliminar clipping, desbordes y colisiones.

## Inventario

| diagram_id | slide_id | función pedagógica | estructura prevista | fuente principal | complejidad / riesgo | estado |
|---|---|---|---|---|---|---|
| U10-DG-001 | U10-001 | Anticipar la idea de caracterizar ruido | Señal irregular que se transforma en cuatro descriptores: tiempo, frecuencia, nivel y efecto | Diseño didáctico; brief U10 | Media; evitar una portada sobrecargada | pendiente |
| U10-DG-002 | U10-002 | Abrir con un problema auténtico | Escena de conversación con fuente útil, interferente, receptor y contexto | Libro §10.3 y §10.8; programa | Alta; muchas relaciones en poco espacio | prototipar temprano |
| U10-DG-003 | U10-003 | Hacer observables los objetivos | Ruta de acciones: distinguir, describir, medir, interpretar y proponer | Programa; brief U10 | Baja | pendiente |
| U10-DG-004 | U10-004 | Reactivar prerrequisitos | Red de presión sonora, RMS, decibel, espectro y percepción | Course dependency map; U4, U5 y U7 | Media; no convertir en mini-resumen | pendiente |
| U10-DG-005 | U10-005 | Mostrar la arquitectura de la clase | Mapa de nueve bloques con trayecto central y ramal de respaldo | Storyboard U10 | Alta; debe seguir siendo legible | prototipar temprano |
| U10-DG-006 | U10-007 | Separar fenómeno, medición e interpretación | Cadena fuente → señal → medición → receptor → efecto | Libro §10.3–10.4 | Media | pendiente |
| U10-DG-007 | U10-008 | Mostrar dependencia del contexto | Una misma forma de onda en tres escenas con distinta función | Libro §10.3 | Media | pendiente |
| U10-DG-008 | U10-009 | Ordenar usos del ruido | Matriz señal de prueba / ambiente / enmascarador / interferencia | Libro §10.3, §10.11–10.13 | Media | pendiente |
| U10-DG-009 | U10-010 | Practicar la clasificación contextual | Cuatro casos con tarjetas arrastrables o revelado progresivo | Elaboración didáctica desde §10.3 | Media; interacción opcional | pendiente |
| U10-DG-010 | U10-013 | Recapitular el primer bloque | Triángulo señal–contexto–receptor con pregunta de control | Síntesis U10-006–012 | Baja | pendiente |
| U10-DG-011 | U10-018 | Clasificar sin memorizar listas | Árbol de decisión determinista / aleatorio y continuo / impulsivo | Libro §10.4–10.5 | Alta; categorías no siempre excluyentes | revisar taxonomía |
| U10-DG-012 | U10-019 | Justificar los descriptores estadísticos | Ruido aleatorio → observación finita → magnitudes resumen | Libro §10.5–10.6 | Media | pendiente |
| U10-DG-013 | U10-020 | Explicar el valor medio | Señal alrededor de cero, suma de áreas positivas y negativas | Libro §10.6.1 | Media | pendiente |
| U10-DG-014 | U10-021 | Dar sentido físico al RMS | Señal → cuadrado → promedio → raíz, con unidad preservada | Libro §10.6.2; guía de notación | Media; cuidar que no parezca algoritmo vacío | pendiente |
| U10-DG-015 | U10-022 | Relacionar varianza y dispersión | Dos señales con igual media y distinta dispersión | Libro §10.6.3 | Baja | pendiente |
| U10-DG-016 | U10-023 | Resolver una caracterización breve | Flujo datos → media → RMS → interpretación | Libro §10.6; ejemplo didáctico | Media | pendiente |
| U10-DG-017 | U10-025 | Integrar descriptores temporales | Matriz descriptor / pregunta / unidad / limitación | Libro §10.6 | Alta; densidad textual | prototipar temprano |
| U10-DG-018 | U10-028 | Construir la noción densidad × ancho de banda | Rectángulo espectral con altura de densidad y base Δf | Libro §10.7.1 | Media | pendiente |
| U10-DG-019 | U10-029 | Leer la ecuación de densidad espectral | Ecuación anotada con símbolos, unidades y relación con banda | Libro §10.7.1; notation guide | Media | pendiente |
| U10-DG-020 | U10-030 | Guiar un cálculo de potencia en banda | Secuencia datos → ancho de banda → producto → interpretación | Libro §10.7.1; ejemplo propio | Media | pendiente |
| U10-DG-021 | U10-036 | Recapitular espectro y color | Mapa color → pendiente → energía por banda → percepción esperable | Libro §10.7 | Media | pendiente |
| U10-DG-022 | U10-038 | Explicar ruido conformado al habla | Espectro base → filtro → envolvente objetivo | Libro §10.7.4 | Media | pendiente |
| U10-DG-023 | U10-039 | Diferenciar banda ancha y filtrado | Banco de filtros que deriva blanco en pasa-altos, pasa-bajos y pasabanda | Libro §10.7.5–10.7.7 | Alta; conectores y etiquetas | prototipar temprano |
| U10-DG-024 | U10-040 | Definir ruido de banda estrecha | Espectro amplio → filtro centrado en fc → banda Δf | Libro §10.7.7 | Media | pendiente |
| U10-DG-025 | U10-041 | Interpretar parámetros de NBN | Ecuación/diagrama anotado de límites, centro y ancho | Libro §10.7.7; notation guide | Media | pendiente |
| U10-DG-026 | U10-043 | Elegir una señal de prueba | Árbol problema → objetivo → espectro necesario → señal | Libro §10.7 y §10.11 | Media | pendiente |
| U10-DG-027 | U10-044 | Recapitular familias de señal | Tabla visual familia / forma espectral / uso / cautela | Libro §10.7 | Media | pendiente |
| U10-DG-028 | U10-046 | Ubicar las etapas de medición | Fuente → micrófono → ponderación → integración → indicador | Libro §10.8–10.10 | Media | pendiente |
| U10-DG-029 | U10-048 | Distinguir máximo y pico | Dos detectores sobre el mismo evento temporal | Libro §10.8 | Media | pendiente |
| U10-DG-030 | U10-049 | Explicar el nivel equivalente | Evento variable → energía acumulada → nivel constante equivalente | Libro §10.8; glossary | Media | pendiente |
| U10-DG-031 | U10-050 | Resolver un ejemplo de Leq | Línea temporal segmentada con aporte energético y resultado | Libro §10.8; ejemplo propio | Media | pendiente |
| U10-DG-032 | U10-052 | Separar fondo, señal y enmascarador | Tres capas acústicas alrededor del receptor | Libro §10.8, §10.11 | Media | pendiente |
| U10-DG-033 | U10-053 | Definir relación señal/ruido | Ecuación anotada y regla visual de signo positivo/negativo | Libro §10.8; notation guide | Media | pendiente |
| U10-DG-034 | U10-055 | Aplicar SNR a comunicación | Fuente vocal, ruido, distancia y oyente con palancas de mejora | Libro §10.8, §10.13 | Alta; no sugerir causalidad única | pendiente |
| U10-DG-035 | U10-056 | Recapitular descriptores de nivel | Selector: pregunta → indicador apropiado | Libro §10.8–10.10 | Media | pendiente |
| U10-DG-036 | U10-058 | Tender el puente hacia enmascaramiento | Ruido externo → representación interna → detectabilidad del tono | Libro §10.11; U6–U7 | Media | pendiente |
| U10-DG-037 | U10-059 | Identificar los elementos del fenómeno | Señal, enmascarador, receptor y criterio de detección | Libro §10.11 | Media | pendiente |
| U10-DG-038 | U10-060, U10-061 | Explicar geometría espectral básica | Audiograma/esquema con señal y bandas enmascaradoras en dos configuraciones | Libro §10.11 | Alta; debe diferenciar esquema de protocolo clínico | prototipar temprano |
| U10-DG-039 | U10-062 | Distinguir enmascaramiento y protección | Bifurcación propósito perceptual vs control de exposición | Libro §10.11–10.12 | Media | pendiente |
| U10-DG-040 | U10-063 | Tratar tinnitus con prudencia | Ruido como apoyo terapéutico dentro de un encuadre clínico, con límites | Libro §10.11 | Media; evitar recomendación clínica prescriptiva | pendiente |
| U10-DG-041 | U10-064 | Recapitular enmascaramiento | Mapa qué cambia / qué no cambia / qué falta para protocolo | Libro §10.11; open_decisions | Media | pendiente |
| U10-DG-042 | U10-066 | Separar tres planos de análisis | Fuente/ambiente, exposición y efecto en salud | Libro §10.12–10.14 | Media | pendiente |
| U10-DG-043 | U10-067 | Frenar inferencias causales simples | Medición → exposición → riesgo, con variables mediadoras | Libro §10.12 y §10.14 | Media | pendiente |
| U10-DG-044 | U10-069 | Interpretar ruido de fondo en cabina | Cabina, transductor, oído y límite de detección | Libro §10.10 y §10.13 | Alta; la magnitud normativa queda fuera | pendiente |
| U10-DG-045 | U10-070 | Jerarquizar controles | Fuente → trayectoria → receptor, con barreras y prioridad | Libro §10.13 | Alta; geometría de conectores | prototipar temprano |
| U10-DG-046 | U10-071 | Diferenciar conceptos próximos | Cuadro absorción / aislamiento / silenciador / protección personal | Libro §10.13 | Alta; evitar definiciones telegráficas | pendiente |
| U10-DG-047 | U10-072 | Decidir dónde intervenir | Caso con puntos de intervención seleccionables | Libro §10.13; elaboración didáctica | Media | pendiente |
| U10-DG-048 | U10-073 | Conectar con Fonoaudiología | Red de voz, audición, ambiente clínico y prevención | Libro §10.11–10.14; programa | Media | pendiente |
| U10-DG-049 | U10-075 | Recapitular exposición y control | Cadena medir → interpretar → controlar → verificar | Libro §10.12–10.14 | Media | pendiente |
| U10-DG-050 | U10-077 | Presentar el caso integrador | Plano simple del aula/consultorio con fuentes y receptores | Síntesis de la unidad | Alta; base de cuatro slides | prototipar temprano |
| U10-DG-051 | U10-078 | Analizar el caso en el tiempo | Caso + señal temporal + selección de descriptores | Síntesis §10.5–10.6 | Alta | pendiente |
| U10-DG-052 | U10-079 | Analizar el caso en frecuencia | Caso + espectro + elección de familia de ruido | Síntesis §10.7 | Alta | pendiente |
| U10-DG-053 | U10-080 | Analizar el caso desde control y normas | Caso + jerarquía de control + marcador de información normativa faltante | Síntesis §10.10, §10.13; open_decisions | Alta; separar criterio físico de valor normativo | pendiente |
| U10-DG-054 | U10-081 | Organizar una respuesta grupal | Matriz evidencia → descriptor → interpretación → acción | Síntesis U10 | Alta; densidad textual | pendiente |
| U10-DG-055 | U10-083 | Cerrar la arquitectura conceptual | Mapa final completo con nueve nodos y relaciones | Síntesis U10 | Muy alta; debe simplificar, no acumular | prototipar temprano |
| U10-DG-056 | U10-086 | Mostrar la identidad nivel–densidad–banda | Ecuación anotada y bloque dimensional | Libro §10.7.1 | Media | pendiente |
| U10-DG-057 | U10-087 | Derivar energía del ruido rosa por octava | Bandas logarítmicas con áreas equivalentes | Libro §10.7.3 | Alta; mantenerlo como respaldo | pendiente |
| U10-DG-058 | U10-088 | Demostrar que igual Leq no implica igual exposición temporal | Dos cronogramas con igual energía y distinta estructura | Libro §10.8, §10.12 | Alta; verificar ejemplo numérico | pendiente |
| U10-DG-059 | U10-089 | Ofrecer solución comentada | Diagrama de decisión con respuestas de ejercicios clave | Elaboración didáctica; U10-010, 023, 030, 041, 050, 053, 072, 081 | Muy alta; puede requerir dos slides | prototipar temprano |
| U10-DG-060 | U10-091 | Reservar la arquitectura de un protocolo clínico completo | Flujo de indicación, oído de prueba/no prueba, nivel inicial, incrementos, meseta, sobreenmascaramiento y criterio de detención | Fuente clínica institucional pendiente | Muy alta; no debe diseñarse ni completarse de memoria | bloqueado por fuente |

## Prioridades de prototipado

1. **Arquitectura global:** U10-DG-005 y U10-DG-055 deben compartir vocabulario y geometría para que el cierre permita reconocer el mapa inicial enriquecido.
2. **Clasificación:** U10-DG-011 y U10-DG-017 requieren una revisión conceptual previa para no presentar categorías contextuales como si fueran mutuamente excluyentes.
3. **Filtros y enmascaramiento:** U10-DG-023 y U10-DG-038 necesitan corredores claros para conectores y una leyenda inequívoca.
4. **Caso integrador:** U10-DG-050 a U10-DG-054 deben partir de una misma escena base, con capas activables, para reducir carga extrínseca.
5. **Respaldo:** U10-DG-056 a U10-DG-059 se producirán después de aprobar el cuerpo central.

## Decisiones pendientes que afectan diagramas

- Confirmar si el protocolo clínico de enmascaramiento tendrá una fuente autorizada. Hasta entonces, U10-DG-038 solo representará el fenómeno físico y U10-091 seguirá bloqueada.
- U10-DG-060 existe solo como identificador de trazabilidad: su producción está prohibida hasta recibir y validar esa fuente clínica.
- Confirmar la norma y jurisdicción para valores de exposición y ruido de fondo. U10-DG-053 deberá mostrar el lugar del criterio normativo, pero no inventar umbrales.
- Resolver si U10-DG-059 cabe en una única slide de respaldo o debe dividirse al redactar soluciones.
