---
name: slide-writing
description: Redacta el contenido visible, títulos, captions, ecuaciones, consignas y notas del orador de una unidad de Física Acústica a partir de un storyboard aprobado. Usar después de planificar la unidad y antes o durante la producción del PowerPoint; no usar para definir el mapa curricular ni para sustituir una revisión del deck.
---

# Slide Writing

## Objetivo

Convertir el storyboard aprobado en texto de presentación claro, riguroso y oralmente enseñable.

La redacción debe funcionar en dos niveles:

1. contenido visible que el estudiante pueda leer y seguir;
2. notas del orador que permitan desarrollar la explicación.

## Entradas

Leer:

- storyboard aprobado;
- brief;
- capítulo LaTeX;
- PDF;
- programa;
- guía de estilo;
- assets aprobados;
- figuras propias;
- presentación anterior cuando exista continuidad.

## Estructura por slide

```text
slide_id
title
subtitle
visible_content
equations
visual_instruction
caption
source_note
speaker_notes
transition
accessibility_text
```

## Títulos

Los títulos deben describir la idea y permitir reconstruir la narrativa.

Ejemplos preferidos:

- “La presión relaciona fuerza y superficie”
- “La frecuencia indica cuántos ciclos ocurren por segundo”
- “El oído medio adapta impedancias”
- “La ponderación A aproxima la sensibilidad auditiva”

Evitar títulos vagos o publicitarios.

## Contenido visible

Usar:

- definiciones;
- frases breves;
- listas estructuradas;
- secuencias;
- tablas;
- ejemplos;
- ecuaciones;
- preguntas;
- etiquetas sobre visuales.

No prohibir automáticamente los párrafos. Un párrafo breve puede ser más claro que bullets fragmentados.


### Texto destinado a diagramas

Cuando el storyboard solicite cajas, flechas o callouts:

- escribir un título de nodo breve;
- limitar el cuerpo a dos o tres líneas cortas;
- evitar más de 20 palabras dentro de un nodo pequeño;
- separar ejemplos o aclaraciones en otra caja o en notas;
- no redactar frases largas para colocarlas sobre un conector;
- marcar explícitamente qué texto pertenece a nodo, etiqueta, caption o nota;
- indicar el tamaño mínimo esperado;
- si la idea no puede expresarse con legibilidad, proponer dividir el diagrama o la slide.

La redacción nunca debe obligar a reducir la tipografía por debajo de los pisos definidos en la guía de estilo.

## Explicación para primer año

Para un concepto nuevo:

1. nombrarlo;
2. dar una intuición;
3. definirlo;
4. mostrar una representación;
5. relacionarlo con algo conocido;
6. aplicar;
7. advertir una confusión si corresponde.

## Ecuaciones

- presentar contexto;
- definir variables;
- dar unidades;
- explicar relación;
- señalar proporcionalidades;
- resolver ejemplo;
- separar cálculo de interpretación.

## Ejemplos

- valores plausibles;
- unidades;
- pasos;
- interpretación;
- conexión con acústica o audición.

## Aplicaciones disciplinares

Usar conexiones reales con audiometría, logoaudiometría, audífonos, implantes, voz, inteligibilidad, anatomía, evaluación, cabinas, ruido y percepción.

## Preguntas y ejercicios

Incluir:

- predicción;
- reconocimiento;
- interpretación;
- cálculo;
- comparación;
- aplicación;
- explicación conceptual.

Las notas deben incluir la respuesta esperada.

## Notas del orador

Agregar:

- explicación extendida;
- transición;
- pregunta;
- demostración;
- énfasis;
- error frecuente;
- explicación del visual;
- solución;
- indicaciones multimedia.

No duplicar literalmente la slide.

## Tono

Usar español claro, académico y natural.

Evitar estilo enciclopédico sin guía, marketing, metáforas exageradas, frases típicas de IA y afirmaciones no verificadas.

## Archivos de salida

- `slide_text.md`;
- `speaker_notes.md`;
- `source_map.md`.

## Revisión

Comprobar cobertura, claridad, consistencia, correspondencia título-contenido, legibilidad, exactitud, continuidad, notas y fuentes.

## No hacer

- no cambiar la arquitectura sin registrarlo;
- no añadir cifras no verificadas;
- no convertir todas las slides en listas;
- no ocultar explicaciones esenciales en notas;
- no repetir definiciones sin justificación.
