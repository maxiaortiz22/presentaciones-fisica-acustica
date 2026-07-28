---
name: consistency-guard
description: Compara las presentaciones y materiales de distintas unidades de Física Acústica para mantener continuidad conceptual, terminológica, notacional, pedagógica y visual en todo el curso. Usar después de completar una unidad, antes de publicar un conjunto de decks o cuando se detectan diferencias entre presentaciones.
---

# Consistency Guard

## Objetivo

Asegurar que las diez unidades se perciban como partes de un mismo curso.

La consistencia no significa uniformidad absoluta. Cada tema puede requerir layouts, recursos y ritmos diferentes.

## Dimensiones

### 1. Curricular

Controlar:

- continuidad de objetivos;
- prerrequisitos;
- referencias a unidades anteriores;
- preparación de unidades siguientes;
- distribución de profundidad;
- cobertura del programa.

### 2. Terminológica

Mantener:

- nombres de magnitudes;
- traducciones;
- abreviaturas;
- mayúsculas;
- términos anatómicos;
- nombres de estudios;
- nomenclatura de bandas;
- unidades.

### 3. Notacional

Controlar:

- símbolos;
- subíndices;
- letras griegas;
- decimales;
- niveles;
- referencias acústicas;
- signos;
- fase;
- ejes;
- escalas.

### 4. Pedagógica

Comparar:

- nivel de explicación;
- cantidad de pasos;
- frecuencia de recapitulaciones;
- tipo de ejercicios;
- tratamiento de errores;
- aplicaciones;
- notas del orador;
- vocabulario asumido.

### 5. Visual

Controlar:

- master;
- paleta;
- tipografía;
- tamaños;
- pies;
- numeración;
- layouts;
- componentes;
- ecuaciones;
- gráficos;
- captions;
- créditos.

### 6. Fuentes y assets

Verificar:

- mismo formato de atribución;
- manifests completos;
- URLs;
- nombres de archivos;
- reutilización;
- duplicados innecesarios.

## Flujo

### 1. Seleccionar baseline

Usar:

- guía de estilo;
- course map;
- glosario;
- unidad aprobada más reciente;
- decisiones explícitas del docente.

### 2. Comparar

Crear matriz:

```text
dimension,baseline,new_unit,difference,impact,recommendation
```

### 3. Clasificar

- `intended`;
- `acceptable`;
- `inconsistent`;
- `needs_decision`.

### 4. Corregir o documentar

Corregir inconsistencias evidentes. Para decisiones globales, proponer una norma e indicar si corresponde retrocorregir.

### 5. Actualizar documentación

Actualizar:

- glosario;
- style guide;
- notation guide;
- course map;
- decision log;
- `AGENTS.md` solo si la regla es verdaderamente global.

## Salidas

- `course_consistency_report.md`;
- `style/glossary.md`;
- `style/notation_guide.md`;
- `style/decision_log.md`.

## Momentos recomendados

- tras cada unidad;
- antes de evaluaciones;
- después de cambiar plantilla;
- al actualizar el libro;
- antes de publicar todo el curso;
- cuando un concepto reaparece.

## No hacer

- no homogeneizar por la fuerza;
- no convertir todo al mismo layout;
- no cambiar una convención sin revisar usos anteriores;
- no reescribir unidades por diferencias menores;
- no ignorar inconsistencias técnicas;
- no mezclar esta revisión con una reforma curricular.
