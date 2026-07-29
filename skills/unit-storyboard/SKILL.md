---
name: unit-storyboard
description: Convierte una unidad de Física Acústica en un storyboard pedagógico completo, diapositiva por diapositiva, usando el programa, el capítulo LaTeX, el PDF, el mapa del curso y la guía visual. Usar antes de redactar o producir cualquier deck de unidad y al reestructurar una presentación existente.
---

# Unit Storyboard

## Objetivo

Diseñar la clase antes de escribir las diapositivas.

El storyboard debe transformar el contenido fuente en una secuencia de aprendizaje, no copiar el índice del capítulo.

## Entradas requeridas

Leer:

- tema de la unidad en el programa;
- capítulo LaTeX;
- capítulo o páginas correspondientes del PDF;
- `course_map.md`;
- guía de estilo;
- presentación anterior, si existe;
- decisiones o feedback docente acumulado.

Si falta una fuente, registrar la limitación en el brief.

## Fase 1. Brief

Crear o actualizar `units/unit_XX/brief.md` con:

- título;
- alcance obligatorio;
- perfil del estudiante;
- objetivos;
- conocimientos previos;
- conceptos difíciles;
- ideas erróneas previsibles;
- aplicaciones profesionales;
- recursos disponibles;
- decisiones abiertas;
- relación con la unidad anterior y siguiente.

## Fase 2. Inventario conceptual

Extraer y clasificar:

- conceptos;
- definiciones;
- leyes;
- magnitudes;
- fórmulas;
- representaciones;
- ejemplos;
- aplicaciones;
- ejercicios;
- recursos visuales existentes;
- términos que requieren glosario.

Distinguir entre imprescindible, importante, complementario y fuera de alcance.

## Fase 3. Secuencia pedagógica

Usar una progresión apropiada al tema:

- concreto → representación → formalización → aplicación;
- fenómeno → mecanismo → modelo → evidencia;
- problema → concepto → herramienta → resolución;
- estructura → función → respuesta → consecuencia.

No forzar el mismo patrón en todas las unidades.

## Fase 4. Bloques

Dividir la unidad en bloques de 5 a 12 slides aproximadamente.

Cada bloque debe tener:

- pregunta guía;
- propósito;
- conceptos;
- visuales;
- ejemplo;
- recapitulación o transición.

Para unidades densas, introducir recapitulaciones más frecuentes.

## Fase 5. Storyboard slide-by-slide

Crear `storyboard.md` con una tabla que incluya:

```text
slide_id
block
slide_type
working_title
learning_purpose
key_message
visible_content_summary
visual_or_media
visual_type
diagram_complexity
speaker_note_goal
source
prerequisites
transition
status
```

Tipos sugeridos:

- portada;
- objetivos;
- puente;
- mapa;
- pregunta;
- definición;
- explicación;
- ecuación;
- gráfico;
- comparación;
- proceso;
- ejemplo;
- ejercicio;
- aplicación;
- error frecuente;
- recapitulación;
- cierre.


## Reglas para diagramas previstos

Cuando una slide requiera un diagrama:

- clasificarlo como gráfico cuantitativo o diagrama estructural;
- derivar diagramas estructurales a `diagram-generation`;
- estimar la cantidad de nodos, conectores y etiquetas;
- evitar más de cuatro nodos con texto extenso en una sola slide;
- indicar si el visual necesita dos etapas o dos slides;
- reservar una slide completa cuando la legibilidad lo requiera;
- no plantear un visual cuya información obligue a usar fuente pequeña.

## Reglas de secuencia

- una slide debe tener un propósito dominante;
- no introducir tres conceptos nuevos simultáneamente;
- preparar vocabulario antes de usarlo;
- presentar símbolos antes de operar con ellos;
- no separar fórmula y significado físico;
- no colocar un ejercicio antes de enseñar las herramientas;
- recuperar ideas anteriores mediante una slide breve cuando sea necesario;
- repetir un concepto solo si cambia el nivel, representación o aplicación;
- añadir transición entre bloques conceptualmente distantes;
- ubicar aplicaciones disciplinares cerca del concepto que iluminan.

## Cantidad de diapositivas

No imponer una cantidad objetivo por estética.

Estimar la extensión según número de conceptos, dificultad, ejemplos, recursos, conocimientos previos, ejercicios y recapitulaciones.

Si el storyboard supera ampliamente el tiempo de clase, proponer parte principal, material complementario, slides de respaldo o división en encuentros.

## Fuentes dentro del storyboard

Cada slide debe indicar su base: programa, sección LaTeX, página del PDF, fuente externa propuesta o elaboración propia.

## Revisión del storyboard

Antes de aprobarlo, comprobar:

- cobertura completa;
- flujo comprensible;
- dificultad gradual;
- equilibrio entre teoría y aplicación;
- presencia de ejemplos;
- presencia de recapitulaciones;
- viabilidad visual;
- ausencia de redundancia sin propósito;
- continuidad con unidades previas;
- cierre coherente.

## Salidas

- `brief.md`;
- `storyboard.md`;
- `storyboard_review.md`;
- lista inicial de assets;
- lista inicial de gráficos propios;
- lista inicial de diagramas estructurales;
- alertas y decisiones abiertas.

## No hacer

- no producir el PowerPoint final;
- no redactar párrafos completos de todas las slides;
- no definir el estilo global;
- no reducir el capítulo a bullets;
- no usar una imagen decorativa como sustituto de una explicación;
- no ocultar vacíos de la fuente.
