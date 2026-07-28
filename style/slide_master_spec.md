# Especificación del slide master

## Alcance

Este documento especifica la arquitectura del futuro template. No crea todavía el archivo `.pptx`.

La implementación debe preservar la jerarquía:

`tema → master → layout → slide`

Los cambios repetidos pertenecen al master o al layout. Las excepciones pertenecen a una slide concreta. No se deben simular masters mediante overlays repetidos.

## Tema

- Nombre interno: `FA_UCASAL_V1`.
- Tamaño: 13,333 × 7,5 in.
- Relación: 16:9.
- Fuentes de tema:
  - major Latin: Calibri Light;
  - minor Latin: Calibri;
  - ecuaciones: Cambria Math.
- Paleta: tokens definidos en `presentation_style_guide.md`.
- No incluir gradientes, glows, bevels ni sombras por defecto en el tema.

## Masters

### `FA_MASTER_CLARO`

Uso: todas las slides de contenido, objetivos, mapas, ejercicios, tablas, gráficos, aplicaciones y bibliografía.

Elementos heredados:

1. fondo blanco;
2. regla superior segmentada;
3. pie institucional;
4. placeholder de unidad/sección;
5. placeholder de número de slide.

No contiene:

- placeholder de fecha;
- placeholder de footer vacío;
- caja de título genérica;
- ornamentos;
- fondo cuadriculado.

### `FA_MASTER_BORDO`

Uso: portada, divisor de sección, recapitulación final y cierre/puente.

Elementos heredados:

1. fondo `FA_BORDO_900`;
2. regla superior en blanco, `FA_BORDO_600` aclarado y gris claro;
3. wordmark UCASAL en su versión autorizada para fondo oscuro;
4. número de slide opcional en blanco al 70 %.

No se usa para contenido denso.

## Sistema de coordenadas

Todas las posiciones se expresan en pulgadas desde la esquina superior izquierda.

| Zona/token | x | y | ancho | alto |
|---|---:|---:|---:|---:|
| Slide | 0,00 | 0,00 | 13,333 | 7,50 |
| Margen seguro | 0,67 | 0,45 | 11,99 | 6,53 |
| Regla superior | 0,67 | 0,27 | 11,99 | 0,06 |
| Eyebrow | 0,67 | 0,47 | 4,20 | 0,20 |
| Título 1 línea | 0,67 | 0,72 | 11,99 | 0,55 |
| Título 2 líneas | 0,67 | 0,61 | 11,99 | 0,87 |
| Contenido normal | 0,67 | 1,45 | 11,99 | 5,40 |
| Contenido con título 2 líneas | 0,67 | 1,62 | 11,99 | 5,23 |
| Regla del pie | 0,67 | 7,00 | 11,99 | 0,01 |
| Pie | 0,67 | 7,08 | 11,99 | 0,22 |

Las posiciones pueden variar ±0,03 in por ajuste óptico. Cualquier cambio mayor debe registrarse.

## Regla superior

Geometría en `FA_MASTER_CLARO`:

| Segmento | x | y | ancho | alto | Color |
|---|---:|---:|---:|---:|---|
| 1 | 0,67 | 0,27 | 4,00 | 0,06 | `FA_BORDO_900` |
| 2 | 4,77 | 0,27 | 4,00 | 0,06 | `FA_BORDO_600` |
| 3 | 8,87 | 0,27 | 3,79 | 0,06 | `FA_GRIS_500` |

- Separación: 0,10 in.
- Sin borde.
- No se anima.
- Se oculta en `FA_00_PORTADA`, `FA_01_DIVISOR`, `FA_17_RECAP_FINAL`, `FA_21_CIERRE_PUENTE` y `FA_22_VISUAL_COMPLETO` cuando el layout requiera otra composición.

## Encabezado

### Eyebrow

- Contenido: `UNIDAD NN · SECCIÓN`.
- Calibri Bold, 11–12 pt.
- Mayúsculas.
- Tracking visual amplio, sin sobrepasar 28 caracteres.
- Color `FA_BORDO_600`.
- Se omite si el título o el divisor ya ofrece suficiente orientación.

### Título

- Calibri Light, 36 pt.
- Color `FA_CARBON_900`.
- Alineación izquierda.
- Una línea por defecto.
- Dos líneas solo en el placeholder específico.
- No usar auto-fit que reduzca por debajo de 35 pt.
- Si no entra: abreviar, dividir la slide o usar el layout de dos líneas.

## Pie institucional

### En master claro

| Elemento | x | y | ancho | alto | Estilo |
|---|---:|---:|---:|---:|---|
| Wordmark/monograma | 0,67 | 7,08 | 1,10 | 0,22 | Activo oficial, proporción bloqueada |
| Unidad/sección | 1,95 | 7,10 | 5,40 | 0,18 | Calibri 10 pt, `FA_GRIS_500` |
| Indicador opcional de fuente | 7,55 | 7,10 | 3,80 | 0,18 | Calibri 9 pt, `FA_GRIS_500` |
| Número | 11,78 | 7,08 | 0,88 | 0,20 | Calibri 11 pt, `FA_BORDO_600`, derecha |

Reglas:

- El número es un placeholder dinámico `sldNum`.
- El total de slides no se incluye por defecto.
- El indicador de fuente visible se usa solo cuando la atribución debe estar en pantalla.
- No dejar placeholders vacíos.
- El logo completo se sustituye por monograma si el wordmark no resulta legible a 1,10 in.

### En master bordó

- Wordmark autorizado en blanco o versión institucional correspondiente.
- Unidad/sección y número en blanco al 75 %.
- Sin regla inferior.

## Grilla de contenido

### Dos columnas iguales

- izquierda: x 0,67; ancho 5,80;
- separación: 0,39;
- derecha: x 6,86; ancho 5,80.

### Dos columnas 60/40

- izquierda: x 0,67; ancho 7,10;
- separación: 0,40;
- derecha: x 8,17; ancho 4,49.

### Dos columnas 40/60

- izquierda: x 0,67; ancho 4,49;
- separación: 0,40;
- derecha: x 5,56; ancho 7,10.

### Tres columnas

- ancho de columna: 3,80;
- separaciones: 0,30;
- x: 0,67 / 4,77 / 8,87.

### División horizontal

- bloque superior: y 1,45; alto 2,48;
- separación: 0,34;
- bloque inferior: y 4,27; alto 2,58.

## Contrato de placeholders

Cada placeholder debe tener:

- nombre semántico;
- tipo correcto;
- posición definida;
- estilo de texto asociado;
- instrucciones de uso en el layout;
- texto de ayuda eliminado antes de exportar;
- orden de lectura lógico.

Nombres permitidos:

- `ph_title`;
- `ph_subtitle`;
- `ph_eyebrow`;
- `ph_body`;
- `ph_visual`;
- `ph_chart`;
- `ph_table`;
- `ph_equation`;
- `ph_caption`;
- `ph_source`;
- `ph_prompt`;
- `ph_answer`;
- `ph_step_01`, `ph_step_02`, etc.;
- `ph_unit`;
- `ph_slide_number`.

No usar nombres genéricos como `TextBox 27` en el template final.

## Inventario de layouts

La geometría detallada se basa en los tokens anteriores. El comportamiento pedagógico se documenta en `layout_catalog.md`.

| Layout | Master | Placeholders principales | Comportamiento |
|---|---|---|---|
| `FA_00_PORTADA` | Bordó | unidad, título, subtítulo, visual opcional, docente | Mínima; sin número visible por defecto. |
| `FA_01_DIVISOR` | Bordó | número de sección, título, frase puente | No admite cuerpo ni listas. |
| `FA_02_OBJETIVOS` | Claro | título, 3–5 objetivos, visual/índice opcional | Objetivos observables; cuerpo amplio. |
| `FA_03_MAPA_CLASE` | Claro | título, 3–6 etapas, estado actual | Secuencia horizontal o vertical simple. |
| `FA_04_TITULO_CONTENIDO` | Claro | título, body | Una columna; texto explicativo. |
| `FA_05_TEXTO_VISUAL_60_40` | Claro | título, body 60, visual 40, caption | Texto dominante con evidencia visual. |
| `FA_06_VISUAL_TEXTO_40_60` | Claro | título, visual 40, body 60, caption | Visual introduce; explicación desarrolla. |
| `FA_07_GRAFICO_EXPLICACION` | Claro | título, chart 60, takeaway 40, source | Gráfico con lectura explícita. |
| `FA_08_DEFINICION` | Claro | término, definición, ejemplo breve, símbolo opcional | Una definición completa, no glosario múltiple. |
| `FA_09_ECUACION_INTERPRETACION` | Claro | título, equation, símbolos/unidades, significado | Ecuación central con explicación. |
| `FA_10_EJEMPLO_RESUELTO` | Claro | título, datos, pasos 1–3, resultado, chequeo | Secuencia editable, sin miniatura de pizarra. |
| `FA_11_COMPARACION` | Claro | título, encabezados A/B, contenido A/B, síntesis | Dos columnas equilibradas. |
| `FA_12_PROCESO` | Claro | título, 3–5 etapas, conectores, resultado | Flujo causal o temporal. |
| `FA_13_APLICACION_CLINICA` | Claro | título, concepto físico, situación clínica, vínculo | Usa ocre solo como semántica. |
| `FA_14_PREGUNTA_EJERCICIO` | Claro | pregunta, datos/figura, tiempo o consigna, respuesta en notas | No muestra solución salvo versión docente. |
| `FA_15_ERROR_FRECUENTE` | Claro | afirmación errónea, corrección, evidencia | Un error por slide. |
| `FA_16_RECAP_PARCIAL` | Claro | título, 3 ideas, pregunta de control | Fondo marfil opcional. |
| `FA_17_RECAP_FINAL` | Bordó | título, 4–6 aprendizajes, mapa reducido | Cierra la unidad, no repite el índice. |
| `FA_18_TABLA_DATOS` | Claro | título, tabla, lectura clave, fuente | Tabla nativa; tamaño limitado. |
| `FA_19_MEDIA_AUDIO_VIDEO` | Claro | título, media, consigna de observación, duración, fuente | Incluye alternativa si falla la reproducción. |
| `FA_20_BIBLIO_RECURSOS` | Claro | título, referencias, recursos, QR/enlace opcional | Referencias legibles, no inventario minúsculo. |
| `FA_21_CIERRE_PUENTE` | Bordó | síntesis, próxima pregunta/unidad, contacto opcional | Reemplaza “Muchas gracias” genérico. |
| `FA_22_VISUAL_COMPLETO` | Claro con gráficos ocultos | título corto opcional, visual, caption, número | Para anatomía, gráfico o diagrama dominante. |
| `FA_23_APENDICE` | Claro | rótulo de apéndice, título, contenido flexible | Identificado como material complementario. |

## Reglas específicas por tipo

### Portada

- Puede usar fondo blanco o bordó; la versión seleccionada debe mantener el wordmark oficial.
- Título máximo: 3 líneas.
- Subtítulo máximo: 2 líneas.
- Un visual opcional, no más.
- Sin slogan.
- Nombre del docente y correo en 16–18 pt.

### Divisor

- Número de sección en 16–20 pt.
- Título en 42–46 pt.
- Frase puente en 20–22 pt, máximo 18 palabras.
- No usar fotografía de stock.

### Contenido

- El título se mantiene en la misma coordenada.
- El contenido nunca invade el pie.
- Las imágenes no se colocan detrás del texto.
- Los componentes se insertan dentro de placeholders previstos.

### Full visual

- Oculta regla y wordmark del master.
- Mantiene número discreto.
- El visual debe incluir espacio real para caption o título.
- No se utiliza para una imagen decorativa.

## Estilos de párrafo del tema

### `FA_Title`

- Calibri Light 36 pt;
- color carbón;
- 0 pt antes / 4 pt después;
- sin bullet;
- una o dos líneas según placeholder.

### `FA_Subtitle`

- Calibri 24 pt;
- carbón 85 %;
- 0 pt antes / 8 pt después.

### `FA_Body`

- Calibri 23 pt;
- carbón;
- interlineado 1,08;
- 6 pt después.

### `FA_Bullet_1`

- Calibri 22 pt;
- bullet cuadrado pequeño en bordó;
- sangría izquierda 0,25 in;
- sangría francesa 0,12 in;
- 6–8 pt después.

### `FA_Bullet_2`

- Calibri 20 pt;
- bullet circular gris;
- sangría izquierda 0,50 in;
- uso excepcional.

### `FA_Caption`

- Calibri 15 pt;
- gris oscuro;
- interlineado simple.

### `FA_Source`

- Calibri 9–10 pt;
- gris medio;
- sin bullet.

## Comportamiento de ajuste

- Auto-fit de título: desactivado.
- Auto-fit de cuerpo: desactivado.
- Si el contenido no entra:
  1. editar;
  2. cambiar de layout;
  3. dividir la slide.
- No reducir fuente automáticamente.
- Las imágenes usan crop “fill” o “fit” según placeholder; nunca se estiran.
- Los títulos no deben quedar viudos respecto del contenido.

## Capas y orden de lectura

Orden recomendado:

1. fondo;
2. conectores;
3. nodos/visuales;
4. anotaciones;
5. texto principal;
6. captions/fuentes;
7. pie y número.

En el panel de selección, los nombres de objetos deben reflejar este orden.

## Accesibilidad del master

- El título es el primer objeto en el orden de lectura.
- El pie y número son los últimos.
- Los elementos decorativos del master se marcan como decorativos.
- El logo tiene texto alternativo institucional.
- Los placeholders de visual exigen texto alternativo antes de aprobar.

## Control de calidad del futuro template

Antes de declarar listo el `.pptx`:

- todos los layouts se renderizan con contenido de prueba;
- no hay placeholders vacíos;
- no hay fecha por defecto;
- el número funciona en todos los layouts;
- el logo no se deforma;
- títulos de una y dos líneas funcionan sin auto-fit;
- la tipografía se resuelve en el equipo docente;
- tablas y ecuaciones siguen editables;
- los masters oscuro y claro no duplican objetos en una misma slide;
- el layout de visual completo no deja furniture oculto superpuesto;
- el archivo pasa prueba de desbordes y revisión visual individual.
