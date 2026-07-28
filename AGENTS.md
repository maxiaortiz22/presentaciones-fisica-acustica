# AGENTS.md — Presentaciones de Física Acústica

## 1. Propósito del repositorio

Este proyecto produce las presentaciones académicas de la materia **Física Acústica** de la Licenciatura en Fonoaudiología de UCASAL.

El curso está compuesto por diez unidades. Cada unidad debe convertirse en una presentación pedagógica completa, basada principalmente en:

1. el programa oficial de la materia;
2. el capítulo correspondiente del libro escrito por el docente;
3. el archivo fuente en LaTeX;
4. las decisiones pedagógicas y visuales registradas en este repositorio.

El objetivo no es resumir mecánicamente el libro. El objetivo es transformar su contenido en una **secuencia de clase comprensible, explicativa, visual y rigurosa** para estudiantes de primer año.

## 2. Público y nivel

El público está formado por estudiantes de primer año de Fonoaudiología que pueden tener conocimientos limitados de física, matemática, representación gráfica, acústica, procesamiento de señales y anatomía auditiva.

Por lo tanto:

- no asumir conocimientos avanzados;
- introducir la intuición antes del formalismo;
- definir símbolos, unidades y variables;
- mostrar ejemplos simples antes de casos generales;
- explicitar pasos intermedios;
- recuperar conocimientos previos cuando sea necesario;
- repetir conceptos clave cuando la repetición tenga una función pedagógica.

La profundidad es prioritaria. No existe un límite rígido de diapositivas. Una unidad puede superar las 50 diapositivas si el contenido y la progresión didáctica lo justifican.

## 3. Jerarquía de fuentes

Usar las fuentes en este orden:

1. **Programa oficial:** define el alcance mínimo obligatorio.
2. **Libro del curso en LaTeX:** fuente editable y estructural principal.
3. **Libro del curso en PDF:** referencia visual y de verificación.
4. **Bibliografía académica y normas técnicas citadas en el libro.**
5. **Fuentes externas confiables:** para imágenes, videos, ejemplos, datos o ampliaciones.
6. **Conocimiento general del modelo:** solo para conectar, explicar o proponer; nunca para contradecir las fuentes principales sin advertirlo.

Reglas:

- ningún tema del programa puede omitirse sin justificación;
- si programa y libro difieren, registrar la diferencia y priorizar el alcance del programa;
- no inventar citas, normas, fórmulas, valores ni resultados;
- distinguir el contenido del libro de las ampliaciones didácticas;
- registrar las fuentes externas utilizadas.

## 4. Unidades del curso

1. Nociones básicas e introducción a la acústica.
2. Leyes de la mecánica clásica y de la termodinámica.
3. Fundamentos de la mecánica ondulatoria.
4. Generalidades sobre el sonido, sus propiedades y magnitudes.
5. Análisis frecuencial de señales acústicas.
6. El mecanismo de la percepción auditiva.
7. Características subjetivas de la percepción auditiva y psicoacústica.
8. Enfermedades y estudios auditivos; técnicas de rehabilitación.
9. Factores que afectan a la propagación del sonido.
10. Ruidos.

El mapa detallado del curso debe mantenerse mediante la skill `course-architecture`.

## 5. Flujo obligatorio por unidad

No crear una presentación final directamente desde el capítulo.

Trabajar en este orden:

1. analizar programa, capítulo LaTeX y PDF;
2. identificar objetivos, prerrequisitos y dificultades;
3. crear o actualizar el brief;
4. crear el storyboard completo;
5. definir recursos visuales y multimedia;
6. generar gráficos o diagramas propios;
7. redactar contenido visible y notas del orador;
8. producir o editar el PowerPoint;
9. renderizar todas las diapositivas;
10. revisar contenido, legibilidad, consistencia y fuentes;
11. corregir;
12. registrar la versión final y el informe de revisión.

No saltar la fase de storyboard ni la revisión renderizada.

## 6. Skills del proyecto

| Skill | Usar para |
|---|---|
| `course-architecture` | mapa global de las diez unidades, dependencias y alcance |
| `style-system` | sistema visual académico, plantilla, layouts y componentes |
| `unit-storyboard` | planificación pedagógica slide por slide |
| `asset-curation` | búsqueda y registro de imágenes, videos, GIFs y recursos externos |
| `chart-generation` | gráficos, señales, curvas y figuras reproducibles |
| `slide-writing` | títulos, texto visible, captions y notas del orador |
| `deck-review` | revisión integral de un borrador o deck terminado |
| `consistency-guard` | consistencia global entre las diez unidades |

Cuando una tarea combine varias fases, activar las skills siguiendo el flujo obligatorio.

## 7. Estructura esperada

```text
fisica-acustica-slides/
├── AGENTS.md
├── context/
│   ├── programa/
│   ├── libro_pdf/
│   ├── libro_latex/
│   └── referencias_visuales/
├── skills/
├── style/
├── units/
│   ├── unit_01/
│   │   ├── brief.md
│   │   ├── storyboard.md
│   │   ├── slide_text.md
│   │   ├── speaker_notes.md
│   │   ├── assets/
│   │   ├── asset_manifest.csv
│   │   ├── scripts/
│   │   ├── review.md
│   │   └── output/
│   └── ...
├── scripts/
└── output/
```

No guardar temporales, descargas sin clasificar o versiones ambiguas en `output/`.

## 8. Convenciones de nombres

- carpetas: `unit_01`, `unit_02`, etc.;
- presentaciones: `unidad_01_nociones_basicas_v01.pptx`;
- figuras: `u01_fig_001_sistema_si.svg`;
- imágenes: `u01_img_001_aplicacion_audiologia.jpg`;
- videos o GIFs: `u01_media_001_descripcion.ext`;
- scripts: `u01_plot_001_nombre.py`.

Cada recurso debe tener un identificador único que coincida con el manifiesto de assets.

## 9. Principios pedagógicos

Cada unidad debe:

- declarar objetivos observables;
- comenzar con un puente desde conocimientos previos;
- avanzar desde ejemplos concretos hacia abstracciones;
- introducir una idea principal por vez;
- relacionar teoría, matemática y fenómeno físico;
- incluir aplicaciones a Fonoaudiología, Audiología o voz cuando corresponda;
- contener preguntas de comprobación o mini ejercicios;
- incluir resúmenes parciales en unidades densas;
- cerrar con una recapitulación general;
- anticipar errores conceptuales frecuentes;
- usar analogías solo cuando sean físicamente correctas y aclarar sus límites.

Las unidades 4, 5, 6 y 7 requieren bloques más cortos, recapitulaciones frecuentes y una revisión pedagógica independiente.

## 10. Cantidad de texto

Las presentaciones son material de apoyo, no reemplazos del libro.

- usar el texto necesario para comprender;
- evitar párrafos extensos cuando puedan convertirse en secuencias, diagramas o varias slides;
- dividir una slide si contiene más de una idea principal;
- reservar explicaciones extendidas para notas;
- conservar definiciones completas cuando la precisión importe;
- evitar bullets telegráficos que pierdan significado.

Una slide puede ser explicativa, pero debe seguir siendo legible desde el aula.

## 11. Ecuaciones y magnitudes

Para toda ecuación:

- definir símbolos;
- indicar unidades;
- explicar el significado físico;
- mostrar un ejemplo numérico cuando ayude;
- controlar consistencia dimensional;
- diferenciar valores instantáneos, promedio, RMS, lineales y logarítmicos;
- no introducir fórmulas sin contexto;
- mantenerlas editables cuando sea posible.

Usar notación coherente entre unidades y registrarla en la guía correspondiente.

## 12. Sistema visual

La referencia principal es la presentación de Unidad 1 creada por el docente. Conservar su identidad académica y directa, mejorando:

- jerarquía tipográfica;
- alineaciones;
- márgenes;
- consistencia;
- uso de espacios;
- variedad controlada de layouts;
- calidad de diagramas;
- integración de imágenes;
- claridad de ecuaciones;
- slides de recapitulación.

El deck de Gemini es una referencia secundaria de composición, no una plantilla a copiar.

Evitar:

- degradados decorativos;
- exceso de tarjetas flotantes;
- iconografía genérica repetida;
- imágenes de stock sin función;
- títulos publicitarios;
- frases grandilocuentes;
- layouts idénticos en todas las slides;
- fondos complejos;
- adornos que compitan con el contenido.

Priorizar un diseño académico, humano y funcional.

## 13. Recursos visuales y multimedia

Orden de preferencia:

1. gráficos y diagramas propios;
2. fotografías o ilustraciones técnicas confiables;
3. material de organismos, universidades, fabricantes técnicos o publicaciones científicas;
4. videos y GIFs educativos;
5. imágenes generadas por IA solo si no existe un recurso adecuado o si una visualización sintética explica mejor el fenómeno.

Registrar para cada recurso externo:

- identificador;
- URL;
- autor u organización;
- descripción;
- fecha de acceso;
- licencia conocida;
- slide prevista;
- propósito pedagógico;
- estado.

No usar una imagen solo porque es atractiva.

## 14. Gráficos y figuras propias

Preferir Python, NumPy, SciPy y Matplotlib. Exportar SVG cuando la editabilidad importe y PNG de alta resolución cuando sea necesario.

Todo gráfico debe incluir:

- ejes y unidades;
- escala explícita;
- leyenda solo si es necesaria;
- texto legible;
- explicación pedagógica;
- fuente de datos.

No falsear datos con ejes truncados, escalas ambiguas o suavizados no declarados.

## 15. Redacción

Usar español académico claro, natural y rioplatense neutro.

Preferir:

- títulos informativos;
- oraciones completas cuando ayuden;
- términos técnicos definidos;
- transiciones explícitas;
- preguntas que guíen;
- ejemplos vinculados con sonido, audición, voz y práctica clínica.

Evitar tono de marketing, clichés de IA, listas vagas y conclusiones no sustentadas.

## 16. Notas del orador

Las notas pueden incluir:

- explicación extendida;
- transición;
- preguntas;
- ejemplos orales;
- demostraciones;
- errores frecuentes;
- indicación de reproducir audio, GIF o video;
- solución esperada de un ejercicio.

No deben repetir literalmente todo el texto visible.

## 17. PowerPoint y editabilidad

Siempre que sea posible:

- mantener textos, formas, flechas, ecuaciones y gráficos editables;
- usar master slides y layouts consistentes;
- no aplanar una slide completa como imagen;
- recortar imágenes sin deformarlas;
- usar 16:9;
- incluir texto alternativo;
- conservar enlaces y créditos;
- evitar fuentes poco disponibles.

No reemplazar el archivo fuente sin conservar una versión previa identificable.

## 18. Revisión obligatoria

Antes de declarar terminada una unidad:

### Contenido
- todos los temas del programa están cubiertos;
- fórmulas y unidades son correctas;
- no hay contradicciones con el libro;
- ampliaciones externas están verificadas;
- existe progresión pedagógica.

### Visual
- no hay desbordes ni solapamientos;
- texto y ecuaciones son legibles;
- imágenes no están deformadas;
- contraste y alineación son correctos;
- las slides no parecen clones.

### Didáctica
- conceptos difíciles tienen preparación;
- ejemplos acompañan la abstracción;
- existen recapitulaciones;
- preguntas y ejercicios son resolubles.

### Fuentes
- assets externos están registrados;
- citas técnicas son rastreables;
- no se atribuye material incorrectamente.

La revisión debe producir `review.md` con problema, severidad, corrección y estado.

## 19. Definición de terminado

Una unidad está terminada únicamente cuando existen:

- `brief.md`;
- `storyboard.md`;
- `slide_text.md`;
- `speaker_notes.md`;
- `asset_manifest.csv`;
- scripts y figuras, si corresponden;
- presentación `.pptx`;
- render de revisión;
- `review.md` sin problemas críticos;
- verificación de consistencia con unidades anteriores.

## 20. Conducta del agente

Antes de editar:

- inspeccionar archivos relevantes;
- preservar decisiones previas;
- informar contradicciones o faltantes;
- hacer cambios trazables;
- no borrar contenido fuente sin justificación;
- no cambiar el estilo global durante una tarea de contenido;
- no rehacer un deck completo si basta una corrección localizada.

Al finalizar:

- enumerar archivos creados o modificados;
- resumir decisiones importantes;
- indicar verificaciones realizadas;
- señalar problemas abiertos.
