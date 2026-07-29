# Unidad 1 — Decisiones abiertas

## Criterio

Este documento registra decisiones que no deben resolverse silenciosamente. Ninguna impide completar el brief, pero varias deben cerrarse antes del storyboard o de la redacción de slides.

## Decisiones pedagógicas

| ID | Decisión pendiente | Recomendación inicial | Impacto | Momento de resolución |
|---|---|---|---|---|
| U01-D01 | ¿La Unidad 1 se dicta en una única clase de 4 horas o puede continuar en otro encuentro? | Diseñar una parte central viable en una clase de 4 horas y conservar material seleccionable. | Extensión y ritmo. | Antes del storyboard. |
| U01-D02 | ¿Se realizará diagnóstico matemático inicial? | Sí, breve, no calificado y con cuatro consignas. | Ritmo y nivel de explicación. | Antes del storyboard. |
| U01-D03 | ¿Qué herramientas pueden usar los estudiantes? | Permitir calculadora; no depender de una aplicación específica. | Ejercicios de logaritmos y potencias. | Antes de redactar actividades. |
| U01-D04 | ¿La actividad con resorte puede realizarse en aula? | Mantenerla si hay espacio y material; preparar animación alternativa. | Demostración de propagación. | Antes de curar assets. |
| U01-D05 | ¿Cuánta mecánica ondulatoria se anticipa? | Limitarse a perturbación, oscilación local y propagación; derivaciones en U3/U4. | Evita redundancia y sobrecarga. | En storyboard. |
| U01-D06 | ¿Las siete magnitudes fundamentales se enseñan en la parte central? | Presentar el sistema completo, pero concentrar práctica en longitud, masa y tiempo; tabla completa como complemento. | Tiempo y memorización. | En storyboard. |
| U01-D07 | ¿Cifras significativas forman parte del núcleo? | Tratar redondeo razonable en ejemplos; dejar reglas formales como complemento hasta ampliar la fuente. | Coherencia con la matriz. | Antes de slide writing. |
| U01-D08 | ¿Cuántas propiedades de logaritmos se enseñan? | Solo definición, inversión, base 10, factores de diez y razón adimensional. | Evita convertir U1 en curso de álgebra. | En storyboard. |
| U01-D09 | ¿El anticipo de dB es central? | Sí, con una razón de tipo potencia y una única fórmula; reservar `20 log` y SPL para U4. | Preparación de U4. | En storyboard. |
| U01-D10 | ¿Se mencionan dB HL y dB SPL en el cuerpo principal? | Usarlos solo en un caso de clasificación y como advertencia; detalle en respaldo. | Aplicación audiológica y carga. | En storyboard. |
| U01-D11 | ¿La pregunta integradora se resuelve en clase? | Trabajar partes seleccionadas en el cierre y dejar la solución completa en respaldo. | Tiempo de clase. | En storyboard. |

## Decisiones de notación

| ID | Conflicto | Fuentes | Recomendación provisional |
|---|---|---|---|
| U01-N01 | Área `A` frente a `S` | Capítulo: `A`; guía draft: `S` | Adoptar `S` si se confirma transversalmente; si se conserva `A`, evitar usar `A` para amplitud en U1. |
| U01-N02 | Distancia `d` frente a `x`/`r` | Capítulo y course map: `d`; guía draft: `x`, `r` | Mantener `d` en ejemplos introductorios y reservar `x` para posición y `r` para distancia radial. Documentar la excepción. |
| U01-N03 | Peso `F_g` frente a `P` | Capítulo: `F_g`; deck docente: `P` | Usar `F_g` para enfatizar que el peso es una fuerza y evitar colisión con potencia. |
| U01-N04 | Fuerza neta en `F=ma` | Capítulo introduce `F=ma`; U2 usará `ΣF` | Rotular explícitamente “fuerza neta” y anticipar `ΣF` solo si no sobrecarga. |
| U01-N05 | Temperatura `T` frente a período `T` | Guía draft propone calificador | En U1 usar `T_temp` o escribir la palabra temperatura; reservar `T` para período desde U3. |
| U01-N06 | `Q` en la fórmula de dB | En U2 `Q` puede ser calor; U4 `Q` directividad | Conservar `Q/Q₀` solo como magnitud genérica local y aclarar que no fija una notación transversal. |
| U01-N07 | Escritura de unidades compuestas | Libro usa `m/s`; guía draft prefiere `m·s⁻¹` | Elegir una forma principal para slides y aceptar la equivalente al enseñar lectura de unidades. |

La existencia de `notation_guide_draft.md` y no de una guía aprobada impide considerar definitivas estas elecciones.

## Decisiones de alcance y clasificación

| ID | Tema | Situación | Acción propuesta |
|---|---|---|---|
| U01-A01 | Notación científica y análisis dimensional | La matriz los marca `out_of_scope`; el libro y los mapas los consideran necesarios. | Mantenerlos en la parte central como ampliación instrumental. |
| U01-A02 | Físico frente a perceptual | La matriz lo marca `out_of_scope`; es un eje transversal del curso. | Mantenerlo en la parte central y explicitar que amplía el listado literal. |
| U01-A03 | Frecuencia | No aparece en el listado de U1, pero se usa como magnitud derivada. | Introducirla como conteo por tiempo; formalizarla en U3. |
| U01-A04 | Aceleración | No aparece en el listado de U1, pero se necesita para fuerza. | Introducción mínima; leyes y dinámica en U2. |
| U01-A05 | Sonido como perturbación mecánica | El programa lo desarrolla con mayor amplitud en U3/U4. | Usar como marco conceptual, sin ecuación de onda. |
| U01-A06 | Aplicaciones fonoaudiológicas | El programa menciona Audiología; el libro amplía a voz y dispositivos. | Cumplir Audiología y sumar voz/dispositivos como ampliación aplicada. |

## Decisiones sobre ejemplos y datos

| ID | Decisión | Recomendación |
|---|---|---|
| U01-E01 | Valor didáctico de velocidad del sonido | Usar `343 m/s` para aire cercano a `20 °C` cuando importe precisión y `340 m/s` solo en ejercicios redondeados, rotulándolo como aproximación. |
| U01-E02 | Símbolo y valor de aceleración gravitatoria | Usar `g = 9,8 m·s⁻²` como dato del problema; no presentarlo como constante universal exacta. |
| U01-E03 | Ejemplo `20 µPa` | Aclarar que se usa para notación científica; su papel como referencia acústica se formaliza en U4. |
| U01-E04 | Ángulos `640°` y `280°` | Mantener como complemento; usar primero ejemplos `90°`, `180°`, `270°` y `360°`. |
| U01-E05 | Ejemplo de audiometría `35 dB HL` | Mantener para clasificar dato físico/nivel/respuesta, sin conversión a SPL. |
| U01-E06 | Ejemplos del deck docente | No reutilizar formulaciones clínicas hasta corregir precisión y fuente. |

## Decisiones visuales y de assets

| ID | Decisión pendiente | Recomendación |
|---|---|---|
| U01-V01 | ¿Reutilizar los gráficos raster del deck docente? | No. Recrearlos como SVG, gráfico o formas editables con trazabilidad. |
| U01-V02 | ¿Reutilizar la tabla raster de prefijos? | No. Crear tabla nativa y seleccionar prefijos relevantes. |
| U01-V03 | ¿Reutilizar el meme de función inversa? | No por defecto. Solo reconsiderar si se demuestra propósito y licencia. |
| U01-V04 | ¿Usar fotografías? | Solo para situaciones reales de voz, medición o demostración; evitar stock conceptual. |
| U01-V05 | ¿Animar propagación y funciones? | Sí, si la versión estática sigue siendo suficiente y existe alternativa. |
| U01-V06 | ¿Conservar los TikZ del libro? | Conservar su contenido y fuente; adaptar el estilo y editabilidad al sistema visual. |
| U01-V07 | Logo institucional | Usar provisionalmente el activo ya aprobado en el template; reemplazar cuando exista el vector oficial. |

## Decisiones documentales

| ID | Problema | Recomendación |
|---|---|---|
| U01-M01 | Referencias de sección desactualizadas en `content_coverage_matrix.csv` | Actualizar la matriz en una tarea de arquitectura, no dentro de este brief. |
| U01-M02 | `notation_guide.md` no existe | Validar y promover el borrador antes de la redacción final. |
| U01-M03 | `glossary.md` no existe | Validar y promover el borrador o declarar que seguirá siendo provisional. |
| U01-M04 | “Cifras significativas” aparece en la matriz, pero no se desarrolla en el capítulo | Añadir fuente interna o reclasificar el alcance. |
| U01-M05 | Falta una guía de ejercicios independiente mencionada en el programa | Usar el banco del libro; registrar si aparece luego una guía oficial. |

## Decisiones que no bloquean el brief

- número exacto de slides;
- títulos de slides;
- orden slide por slide;
- selección final de layouts;
- assets externos específicos;
- notas del orador;
- animaciones concretas;
- versión final de ejercicios visibles.

Estas decisiones pertenecen al storyboard, curación de assets y redacción posterior.

## Criterios para cerrar decisiones

Una decisión se considera cerrada cuando:

1. existe una elección explícita;
2. se identifica la fuente o razón;
3. la elección es coherente con unidades futuras;
4. se registra el impacto en brief, inventario o guía transversal;
5. no introduce una afirmación clínica o normativa sin respaldo.

