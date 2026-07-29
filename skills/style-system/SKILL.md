---
name: style-system
description: Define, documenta y aplica el sistema visual académico de las presentaciones de Física Acústica a partir del PowerPoint del docente como referencia principal y del deck de Gemini como referencia secundaria. Usar para crear la guía de estilo, plantilla, layouts, tipografía, color, jerarquía y reglas visuales; no usar para decidir el contenido pedagógico de una unidad.
---

# Style System

## Objetivo

Crear un sistema visual coherente, académico, natural y funcional para las diez presentaciones.

La estética debe sentirse diseñada por un docente con criterio editorial, no por una herramienta automática.

## Referencias

Orden de prioridad:

1. presentación original de la Unidad 1 creada por el docente;
2. identidad institucional disponible;
3. decisiones registradas en `style/`;
4. presentación de Gemini como referencia secundaria;
5. buenas prácticas generales de diseño académico.

La referencia de Gemini puede aportar ideas de jerarquía o composición, pero no debe imponer un estilo genérico de IA.

## Proceso

### 1. Auditar las referencias

Analizar:

- tamaño y relación de aspecto;
- portada;
- tipografías;
- colores;
- posición de títulos;
- pies y numeración;
- densidad de texto;
- uso de imágenes;
- ecuaciones;
- tablas;
- diagramas;
- consistencia entre slides;
- elementos distintivos del docente;
- problemas visuales actuales.

Separar:

- rasgos que deben conservarse;
- rasgos que deben mejorarse;
- rasgos que deben descartarse;
- ideas aprovechables del deck secundario.

### 2. Definir principios

El sistema debe priorizar:

- legibilidad en aula;
- jerarquía clara;
- alineaciones visibles;
- espacios suficientes;
- equilibrio entre texto y visual;
- variedad controlada;
- editabilidad;
- consistencia entre unidades;
- bajo nivel de decoración irrelevante.

### 3. Definir tokens de diseño

Documentar:

- relación 16:9;
- paleta principal y secundaria;
- colores semánticos;
- fondo;
- tipografías disponibles;
- tamaños mínimos;
- pesos tipográficos;
- espaciado;
- márgenes seguros;
- radios, bordes y sombras, si se usan;
- estilos de líneas, flechas y conectores;
- tratamiento de imágenes;
- estilo de ecuaciones;
- estilo de captions;
- pie de página;
- numeración.

No elegir fuentes que requieran una instalación especial salvo aprobación explícita.


### 3A. Pisos tipográficos y cajas

Para slides 16:9 proyectadas en aula, definir en la guía:

- título de slide: 30–36 pt;
- cuerpo principal: 24–28 pt;
- texto de diagramas: 22–24 pt;
- etiquetas de conectores: 20–22 pt;
- ecuaciones centrales: 28–40 pt;
- captions: 18–20 pt;
- créditos: pueden ser menores según la guía.

Reglas:

- no usar auto-shrink como mecanismo de layout;
- si el texto no entra, ampliar, resumir, redistribuir o dividir;
- usar padding interior mínimo de 0,18 in;
- reservar espacio para flechas antes de cerrar la composición;
- definir un layout específico para diagramas de procesos y otro para ecuaciones anotadas.

### 4. Diseñar layouts

Definir al menos:

1. portada de unidad;
2. objetivos;
3. mapa de la clase;
4. título y contenido;
5. explicación con imagen;
6. explicación con gráfico;
7. definición destacada;
8. ecuación y explicación;
9. ejemplo resuelto;
10. comparación;
11. proceso o secuencia;
12. aplicación a Fonoaudiología;
13. pregunta o mini ejercicio;
14. resumen parcial;
15. recapitulación final;
16. bibliografía o recursos;
17. cierre.

No todos los layouts deben usarse en todas las unidades.

### 5. Diseñar componentes

Crear reglas para:

- caja de definición;
- caja de ejemplo;
- observación;
- error frecuente;
- conexión clínica;
- fórmula;
- pregunta al curso;
- llamada a video o audio;
- fuente de imagen;
- mini recapitulación.

Usar pocos componentes y repetirlos con significado consistente.

## Reglas contra el “look IA”

Evitar:

- portadas cinematográficas;
- slogans;
- títulos grandilocuentes;
- gradientes intensos;
- exceso de tarjetas redondeadas;
- iconos decorativos en cada bullet;
- fotografías conceptuales de stock;
- fondos con redes, partículas o neón;
- ilustraciones pseudo-3D sin valor didáctico;
- alternancia arbitraria de estilos;
- composiciones demasiado perfectas pero impersonales;
- textos como “El plano maestro del sonido” cuando no corresponden al tono académico.

Preferir:

- fotografías o diagramas vinculados al contenido;
- títulos descriptivos;
- ejemplos del campo profesional;
- pequeñas variaciones manuales;
- captions y anotaciones;
- composiciones que respondan al tema concreto.

## Salidas

### `style/presentation_style_guide.md`

Debe incluir principios, paleta, tipografías, escala tipográfica, espaciado, grilla, layouts, componentes, imágenes, gráficos, ecuaciones, tablas, notas, créditos y ejemplos.

### `style/slide_master_spec.md`

Especificar masters, layouts, placeholders, pie, numeración, márgenes, nombres de layouts y comportamiento esperado.

### `style/visual_audit.md`

Registrar el análisis de las presentaciones de referencia y las decisiones resultantes.

## Criterios de calidad

La guía debe permitir producir una slide coherente sin adivinar color, tipografía, tamaño, espaciado, layout, estilo visual, ubicación de créditos ni densidad aceptable.

## No hacer

- no redactar todo el contenido de una unidad;
- no reemplazar decisiones pedagógicas por decisiones decorativas;
- no imitar ciegamente el deck de Gemini;
- no convertir cada slide en una plantilla rígida;
- no priorizar estética sobre legibilidad;
- no generar assets finales sin activar la skill correspondiente.
