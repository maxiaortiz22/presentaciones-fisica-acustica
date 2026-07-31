# Unidad 3 — Decisiones abiertas

## Criterio

Este registro separa decisiones que deben tomarse antes del storyboard de aquellas que pueden resolverse durante la producción. Las recomendaciones son propuestas de trabajo, no aprobaciones silenciosas.

## Decisiones pedagógicas

| ID | Decisión | Opciones | Recomendación preliminar | Impacto |
|---|---|---|---|---|
| U03-P01 | Extensión temporal de la unidad | Un encuentro intensivo; dos encuentros; tres bloques breves | Diseñar parte central para dos encuentros de 80–100 min y mantener divisiones que permitan una tercera sesión. | Determina ritmo, recapitulaciones y cantidad de práctica. |
| U03-P02 | Profundidad de posición, velocidad y aceleración | Solo cualitativa; ecuaciones completas; derivación | Interpretación completa y ecuaciones como apoyo; sin derivación obligatoria. | Evita sobrecarga matemática. |
| U03-P03 | Momento de introducir `ω` | Junto con `f`; después de dominar `f` y `T`; solo complementario | Introducir después de `f` y `T`, cuando simplifique fase y MAS. | Afecta la ecuación elegida como primera representación. |
| U03-P04 | Momento de introducir `ξ(x,t)` | Temprano; después de tiempo/espacio; solo respaldo | Construir primero las dos lecturas y presentar luego la ecuación completa. | Reduce carga de función de dos variables. |
| U03-P05 | Profundidad de superposición | Omitir; cualitativa; cualitativa más fórmula | Conservar cualitativamente en el núcleo; fórmula de amplitud en complementario. | Prepara U4/U5 sin desplazar el programa. |
| U03-P06 | Lugar de ondas longitudinales/transversales | Núcleo breve; complementario | Núcleo breve con límites de la analogía. | Da base al sonido en fluidos. |
| U03-P07 | Cantidad de ejercicios en clase | Uno por bloque; banco al final; práctica separada | Un control breve por bloque y dos problemas integradores; resto complementario. | Afecta tiempo y evidencia de aprendizaje. |
| U03-P08 | Uso de la cancelación activa | Núcleo; complementario; respaldo | Complementario, con límites explícitos. | Evita sobregeneralización y deriva temática. |

## Decisiones de alcance y clasificación

| ID | Contenido | Tensión documental | Propuesta |
|---|---|---|---|
| U03-A01 | Frecuencia angular | Matriz `out_of_scope`; libro y mapa la usan | Ampliación formal importante, subordinada a `f` y `T`. |
| U03-A02 | Número de onda | Matriz `out_of_scope`; útil para onda viajera | Material complementario; no exigir en la evidencia mínima. |
| U03-A03 | Superposición/interferencia | Fuera del listado literal; objetivo del mapa | Cualitativo central como preparación; fórmula complementaria. |
| U03-A04 | Velocidad de partícula | No está en programa; error crítico de continuidad | Distinción conceptual central; cálculo opcional. |
| U03-A05 | `c = λf` | `c` no figura en el listado literal | Mantener en el núcleo porque permite definir y calcular `λ`. |
| U03-A06 | Transitorios del tono | No están en programa | Conservar como límite breve del modelo ideal. |
| U03-A07 | Presión acústica | Aparece en la cadena, se formaliza en U4 | Nombrar variable y unidad; no desarrollar RMS ni nivel. |
| U03-A08 | Pitch y sonoridad | Se usan para marcar errores, se formalizan en U7 | Mantener solo como contraste físico–perceptual. |

## Decisiones de notación

| ID | Decisión | Problema | Recomendación preliminar |
|---|---|---|---|
| U03-N01 | Amplitud `A` frente a `A_x`/`x̂` | Programa y libro usan `A`; la guía evita colisión con área | Usar `A_x` para desplazamiento de cuerpo y `ξ̂` para partícula; mencionar que el programa puede escribir `A`. |
| U03-N02 | Rigidez y número de onda | El libro usa `k` para ambos | Adoptar `k_s` y `k_onda` en material visible. |
| U03-N03 | Fase `φ`/`ϕ`/`varphi` | Las fuentes usan glifos próximos | Elegir un único glifo compatible con Cambria Math; conservar `φ₀` y `Δφ` en texto del brief. |
| U03-N04 | Posición espacial y desplazamiento | `x` puede ser coordenada o elongación | Usar `x(t)` para cuerpo en el bloque MAS y `ξ(x,t)` para partícula en el bloque ondulatorio; reintroducir el significado al cambiar de bloque. |
| U03-N05 | Velocidades | `v`, `u` y `c` pueden mezclarse | `v(t)` para cuerpo o cono, `u(x,t)` para partícula, `c` para propagación. |
| U03-N06 | Forma principal de la sinusoide | `A cos(ωt+φ₀)` frente a `A cos(2πft+φ₀)` | Introducir primero `A_x cos(2πft+φ₀)` por conexión directa con el programa y luego la forma con `ω`. |
| U03-N07 | Unidades de frecuencia angular/número de onda | El radián es adimensional, pero aporta significado | Mostrar `rad·s⁻¹` y `rad·m⁻¹` por claridad pedagógica. |
| U03-N08 | Valor de velocidad del sonido | El capítulo usa 340, 343 y 344 m/s | Elegir un valor de trabajo por ejemplo y declarar temperatura/condición o “dato del problema”; no presentar un valor universal. |

La actualización desde `origin/main` incorporó `style/notation_guide.md`. Las recomendaciones `U03-N01` a `U03-N05` quedan respaldadas por esa guía; `U03-N06` a `U03-N08` siguen siendo decisiones didácticas locales compatibles con ella.

## Decisiones sobre ejemplos, actividades y seguridad

| ID | Decisión | Pregunta | Recomendación preliminar |
|---|---|---|---|
| U03-E01 | Ejemplo numérico conductor | ¿Usar 500 Hz, 800 Hz o 1000 Hz? | Usar 1000 Hz para conectar `T = 1 ms` y una longitud de onda simple; reservar otros valores para práctica. |
| U03-E02 | Demostración con resorte | ¿Existe resorte largo y espacio visible? | Confirmar disponibilidad; preparar animación estática equivalente. |
| U03-E03 | Demostración con parlante | ¿Se puede observar el cono sin riesgo ni distorsión? | Usar video técnico o demostración de baja frecuencia, sin asociarla directamente con presión calibrada. |
| U03-E04 | Reproducción de tonos | ¿Qué sistema y nivel se utilizarán? | Reproducir solo a nivel cómodo, por duración breve, sin prometer calibración clínica; incluir alternativa visual. |
| U03-E05 | Tono audiométrico | ¿Cuánto detalle de procedimiento incluir? | Limitar a estímulo calibrado, presentación repetida y respuesta; técnica completa en U8. |
| U03-E06 | Cancelación activa | ¿Se dispone de ejemplo reproducible? | No depender de una demo en vivo; usar simulación conceptual con región de validez. |
| U03-E07 | Analogía del péndulo | ¿Se usa además del resorte? | Solo para mostrar aproximación de pequeña amplitud; evitar dos analogías si compiten. |
| U03-E08 | Datos de desplazamiento del cono | ¿Se usarán valores hipotéticos del libro? | Sí, rotulados como modelo hipotético; no inferir presión ni audibilidad. |

## Decisiones visuales y de assets

| ID | Decisión | Alternativas | Recomendación preliminar |
|---|---|---|---|
| U03-V01 | Reutilización de TikZ | Captura; SVG directo; reconstrucción | Reconstruir o regenerar para tamaño de slide; no capturar la página. |
| U03-V02 | Movimiento local/propagación | Diagrama estático; animación | Diseñar un estado estático autosuficiente y un revelado opcional. |
| U03-V03 | Tiempo/espacio | Una slide densa; dos slides; secuencia | Reservar al menos una slide completa para comparación y otra para ejercicio si la legibilidad lo exige. |
| U03-V04 | `x`, `v`, `a` | Tres paneles; gráfico único | Gráfico único normalizado con cuatro instantes destacados; separar ecuaciones si saturan. |
| U03-V05 | Cadena del parlante | Cuatro nodos en línea; dos etapas | Cuatro nodos breves con conectores editables; dividir si se agregan condiciones. |
| U03-V06 | Superposición | Tres paneles simultáneos; revelado | Estado final con tres casos legibles y revelado por etapas opcional. |
| U03-V07 | Uso de imágenes | Foto dominante; diagrama propio | Priorizar diagramas y gráficos; foto solo con función técnica. |
| U03-V08 | Audio | Integrado; enlace; sin audio | Si se usa, integrar alternativa visual y registrar fuente, duración y nivel de uso. |

## Decisiones documentales

| ID | Decisión | Estado | Acción necesaria |
|---|---|---|---|
| U03-D01 | Guía transversal de notación | Cerrada | `style/notation_guide.md` está disponible y es la referencia vigente. |
| U03-D02 | Glosario transversal | Cerrada | `style/glossary.md` está disponible; respetar sus pendientes explícitos. |
| U03-D03 | Sincronización de ramas | Cerrada | `main`, `origin/main` y la base de `codex/unidad-03-estudio-brief` coinciden en `4b9d8eb`. |
| U03-D04 | No existe deck previo de U3 | Informativa | Usar U1 solo como referencia de identidad global, no de secuencia específica. |
| U03-D05 | No existe guía de ejercicios independiente | Informativa | Usar y seleccionar el banco del capítulo. |
| U03-D06 | Páginas PDF del capítulo | Cerrada | Usar pp. 61–88 como referencia estable para esta edición. |

## Decisiones que no bloquean el brief

Pueden resolverse durante el storyboard:

- cantidad exacta de slides por bloque;
- selección final de layouts;
- número exacto de ejercicios visibles;
- elección de animaciones por clic;
- procedencia final de una fotografía de parlante;
- incorporación de un simulador;
- asignación definitiva de contenido complementario frente a respaldo;
- ubicación exacta de citas y créditos.

## Decisiones que sí deben cerrarse antes del storyboard

1. tiempo de clase disponible y cantidad de encuentros;
2. profundidad obligatoria de `ω`, `k_onda`, `v(t)`, `a(t)` y superposición;
3. valor de trabajo y condiciones declaradas para `c`;
4. disponibilidad de resorte, parlante y reproducción de audio;
5. criterio para mantener superposición en el núcleo o mover su fórmula a complemento.

## Criterios para cerrar decisiones

Una decisión puede considerarse cerrada cuando:

- conserva todo el alcance obligatorio;
- reduce carga sin ocultar conceptos;
- mantiene continuidad con U1, U2, U4 y U5;
- respeta la notación transversal;
- permite enseñar con cuerpo visible de 20 pt o mayor;
- tiene alternativa estática y accesible si depende de animación o audio;
- no convierte una aplicación audiológica en una inferencia diagnóstica;
- puede rastrearse a programa, libro o una ampliación declarada.
