---
name: course-architecture
description: Analiza el programa y el libro de Física Acústica para construir o actualizar el mapa global de las diez unidades, sus objetivos, dependencias, alcance, profundidad y continuidad pedagógica. Usar al iniciar el proyecto, al modificar el programa o al revisar la coherencia curricular completa; no usar para redactar directamente una presentación individual.
---

# Course Architecture

## Objetivo

Transformar el programa oficial y la estructura del libro en una arquitectura docente explícita para las diez unidades.

Esta skill responde:

- qué debe aprenderse en cada unidad;
- qué conceptos son prerrequisitos;
- qué temas deben retomarse posteriormente;
- qué profundidad corresponde a estudiantes de primer año;
- dónde existen sobrecargas o vacíos;
- cómo se distribuyen teoría, ejercicios y aplicaciones.

## Entradas

Buscar y leer, según disponibilidad:

- programa oficial;
- índice general del libro;
- capítulos en LaTeX;
- PDF del libro;
- guías de ejercicios;
- evaluaciones;
- decisiones previas en `style/`, `units/` o documentos de planificación.

No asumir que el índice del libro coincide exactamente con el programa.

## Flujo de trabajo

### 1. Extraer el alcance obligatorio

Crear una lista exhaustiva de temas por unidad a partir del programa.

Para cada tema registrar:

- unidad;
- formulación original;
- presencia en el libro;
- profundidad aparente;
- relaciones con otras unidades.

### 2. Identificar resultados de aprendizaje

Escribir de 4 a 8 resultados observables por unidad.

Usar verbos como:

- reconocer;
- definir;
- representar;
- interpretar;
- calcular;
- comparar;
- explicar;
- relacionar;
- aplicar.

Evitar objetivos vagos como “comprender todo” o “conocer el tema”.

### 3. Construir dependencias

Identificar:

- conocimientos previos necesarios;
- conceptos que se introducen parcialmente;
- conceptos que se formalizan después;
- conocimientos que deben repasarse;
- dependencias matemáticas;
- dependencias entre física, acústica, audición y clínica.

### 4. Evaluar la carga conceptual

Clasificar cada unidad como baja, media, alta o muy alta carga conceptual.

Para cargas altas:

- proponer bloques;
- prever recapitulaciones;
- indicar puntos apropiados para ejercicios;
- recomendar si conviene dividir la clase o aportar material complementario.

### 5. Diseñar continuidad

Definir transiciones entre unidades:

- qué se recupera de la anterior;
- qué pregunta abre la siguiente;
- qué notación debe conservarse;
- qué gráficos o analogías pueden reutilizarse.

La repetición debe ser intencional y progresiva, no una copia literal.

### 6. Detectar vacíos y desbalances

Comparar programa y libro.

Marcar:

- tema obligatorio ausente;
- tema del libro fuera del programa;
- concepto presentado sin prerrequisito;
- exceso de profundidad;
- falta de aplicación;
- falta de ejemplos;
- terminología inconsistente.

No corregir silenciosamente. Registrar la decisión propuesta.

## Salidas

### `course_map.md`

Debe incluir:

1. propósito general del curso;
2. perfil de estudiante;
3. tabla de las diez unidades;
4. resultados de aprendizaje;
5. prerrequisitos;
6. conexiones con unidades anteriores y posteriores;
7. carga conceptual;
8. aplicaciones a Fonoaudiología;
9. recursos especiales esperados;
10. alertas de contenido.

### `course_dependency_map.md`

Puede expresarse como tabla, Mermaid, lista jerárquica o combinación de formatos.

### `content_coverage_matrix.csv`

Columnas mínimas:

```text
topic_id,program_topic,unit,book_section,status,depth,prerequisites,notes
```

Estados permitidos:

- `covered`;
- `partial`;
- `missing`;
- `external_expansion`;
- `out_of_scope`.

## Criterios de calidad

El mapa es aceptable cuando:

- todos los temas del programa están representados;
- ninguna unidad se define solo como un listado de capítulos;
- las dependencias son explícitas;
- el nivel de primer año está contemplado;
- las aplicaciones disciplinares aparecen donde son útiles;
- las unidades 4, 5, 6 y 7 tienen una estrategia de reducción de carga cognitiva;
- el mapa permite generar storyboards sin volver a decidir la arquitectura global.

## No hacer

- no crear slides finales;
- no fijar una cantidad rígida de diapositivas;
- no eliminar temas complejos para simplificar;
- no confundir orden del libro con orden pedagógico;
- no introducir una reforma curricular sin señalarla;
- no rellenar huecos con datos no verificados.
