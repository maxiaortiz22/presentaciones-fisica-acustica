# Guía de estilo para las presentaciones de Física Acústica

## Propósito

Esta guía define el sistema visual común para las diez unidades. Debe permitir crear una slide coherente sin adivinar tipografía, color, tamaño, margen, jerarquía, tratamiento de gráficos, ecuaciones, tablas, créditos ni densidad.

La identidad buscada se resume así:

> Una presentación académica clara, sobria y actual, producida por un docente de Física Acústica para estudiantes de primer año de Fonoaudiología.

El sistema conserva la identidad institucional y el tono humano del deck del docente. De Gemini toma únicamente estructuras pedagógicas útiles, reconstruidas como objetos editables y sin señales visuales de generación automática.

## Trabajo de comunicación

Al finalizar cada unidad, el estudiantado debe poder explicar los conceptos físicos con lenguaje y unidades correctos, relacionarlos con fenómenos acústicos y reconocer su relevancia para audición, voz y práctica clínica.

Cada slide debe cumplir una sola función principal:

- introducir;
- explicar;
- comparar;
- demostrar;
- aplicar;
- comprobar;
- resumir;
- conectar con la siguiente idea.

Una slide que intenta cumplir tres funciones debe dividirse.

## Principios rectores

1. **Intuición antes del formalismo.** El diseño debe preparar la ecuación o definición, no exhibirla sin contexto.
2. **Una lectura primaria clara.** En tres segundos debe distinguirse qué mirar primero.
3. **Legibilidad de aula.** El cuerpo visible no depende de acercarse a la pantalla.
4. **Sobriedad institucional.** El bordó y UCASAL identifican; no decoran todo.
5. **Variedad controlada.** Los layouts cambian según la función pedagógica, pero comparten tokens y grilla.
6. **Visuales que enseñan.** Cada imagen, gráfico o diagrama debe responder una pregunta.
7. **Editabilidad.** Texto, ecuaciones, formas, tablas, flechas y gráficos permanecen editables siempre que sea razonable.
8. **Naturalidad docente.** Se permiten anotaciones, captions y énfasis puntuales; se evitan composiciones de plantilla rígida.
9. **Consistencia semántica.** Un color o componente mantiene el mismo significado en todas las unidades.
10. **Profundidad sin saturación.** Una presentación larga se organiza por ritmo y recapitulaciones, no por comprimir contenido.

## Formato y grilla

- Formato: PowerPoint panorámico estándar.
- Tamaño: 13,333 × 7,5 in.
- Relación: 16:9.
- Márgenes seguros:
  - izquierda y derecha: 0,67 in;
  - superior: 0,45 in;
  - inferior de contenido: 0,52 in;
  - área de pie: 0,30 in.
- Grilla base: 12 columnas.
- Separación habitual entre columnas: 0,20–0,30 in.
- Separación entre dos paneles principales: 0,40 in.
- Unidad vertical de espaciado: 0,08 in.

El fondo no muestra la grilla. La grilla existe para alinear.

## Firma visual

### Regla superior segmentada

Se conserva la línea superior de tres segmentos del deck docente como firma discreta:

- segmento 1: bordó primario;
- segmento 2: bordó secundario;
- segmento 3: gris medio;
- altura: 0,06 in;
- sin sombra ni degradado.

No reemplaza al título ni se convierte en una banda alta.

### Banda bordó

La banda completa se reserva para:

- portada;
- divisores de sección;
- recapitulación final;
- cierre/puente de unidad.

No debe aparecer como encabezado pesado en todas las slides.

### Identidad UCASAL

- Usar el wordmark oficial sin deformarlo.
- Portada y cierre: versión completa.
- Slides de contenido: wordmark pequeño o monograma autorizado en el pie.
- No recolorear el logo.
- No usar el azul y rojo del logo como paleta principal de contenido.

## Paleta

### Colores base

| Token | Hex | Uso |
|---|---|---|
| `FA_BORDO_900` | `#4D1434` | Identidad principal, divisores, títulos destacados, reglas. |
| `FA_BORDO_600` | `#903163` | Énfasis secundario, bullets, numeración, subrayado corto. |
| `FA_CARBON_900` | `#3D3D3D` | Texto principal. |
| `FA_GRIS_500` | `#969FA7` | Líneas secundarias, ejes auxiliares, metadatos. |
| `FA_GRIS_200` | `#D9DCE0` | Bordes suaves y separación. |
| `FA_BLANCO` | `#FFFFFF` | Fondo principal. |
| `FA_MARFIL_050` | `#F7F6F2` | Fondo alternativo para recapitulaciones y aplicaciones. |

### Colores semánticos disciplinarios

| Token | Hex | Uso |
|---|---|---|
| `FA_FISICO_700` | `#2F7E83` | Magnitudes físicas, medio, señal o medición objetiva. |
| `FA_FISICO_100` | `#E7F1F1` | Fondo leve para contenidos físicos. |
| `FA_CLINICO_700` | `#9F541A` | Percepción, aplicación clínica o respuesta del receptor. |
| `FA_CLINICO_100` | `#F8EDE2` | Fondo leve para contenidos clínicos/perceptuales. |
| `FA_OK_700` | `#2F6F55` | Respuesta correcta o condición válida. |
| `FA_ALERTA_700` | `#9A641E` | Advertencia o condición de uso. |
| `FA_ERROR_700` | `#A33A3A` | Error conceptual o condición inválida. |

Reglas:

- El bordó identifica el curso; teal y ocre explican relaciones.
- En una slide común usar como máximo un color semántico además del bordó.
- Teal y ocre pueden coexistir solo cuando la comparación físico/perceptual es la idea central.
- Los fondos semánticos nunca superan aproximadamente 12 % de saturación visual.
- No usar turquesa neón, naranja intenso, glow o gradiente.
- Para texto pequeño sobre color usar únicamente combinaciones con contraste AA; carbón sobre fondo claro es la opción predeterminada.

### Colores institucionales del logo

Los valores observados en la referencia son aproximadamente:

- azul UCASAL: `#023E7C`;
- rojo UCASAL: `#D10A11`.

Se reservan al activo institucional hasta verificar la versión oficial del logo.

## Tipografía

### Familias

- Títulos: **Calibri Light**.
- Texto, rótulos y captions: **Calibri**.
- Ecuaciones: **Cambria Math** mediante ecuación nativa de PowerPoint.
- Respaldo: Arial solo cuando un sistema no disponga de Calibri.

No usar Gill Sans MT: figura en el tema de referencia, pero no está instalada y provoca sustituciones. No usar Google Sans: no es una dependencia apropiada para un template distribuible.

### Escala tipográfica

| Nivel | Tamaño habitual | Mínimo | Peso |
|---|---:|---:|---|
| Título de unidad | 50–54 pt | 48 pt | Light o Regular |
| Subtítulo de portada | 26–30 pt | 24 pt | Regular |
| Divisor de sección | 42–46 pt | 40 pt | Light |
| Título de slide | 36 pt | 35 pt en título técnico largo | Light o Regular |
| Subtítulo/pregunta guía | 24–26 pt | 24 pt | Regular |
| Encabezado interno | 24–26 pt | 24 pt | Semibold/Bold |
| Cuerpo | 22–24 pt | 20 pt | Regular |
| Fórmula principal | 34–40 pt | 30 pt | Cambria Math |
| Fórmula secundaria | 26–30 pt | 24 pt | Cambria Math |
| Tabla: encabezado | 20–22 pt | 20 pt | Bold |
| Tabla: celdas | 18–20 pt | 18 pt | Regular |
| Caption | 14–16 pt | 14 pt | Regular |
| Crédito/fuente | 10–11 pt | 9 pt | Regular |
| Pie y numeración | 10–12 pt | 10 pt | Regular |

### Reglas tipográficas

- Alineación a la izquierda por defecto.
- No justificar párrafos.
- Interlineado del cuerpo: 1,05–1,15.
- Espacio posterior entre párrafos: 6–10 pt.
- No usar mayúsculas sostenidas en títulos comunes.
- Las mayúsculas se reservan para el rótulo corto de unidad o sección.
- Negrita para palabras clave; no para párrafos completos.
- Subrayado solo para enlaces; no para crear jerarquía.
- No combinar más de dos pesos en una misma slide.
- Evitar títulos de una línea que se partan por accidente. Si el título necesita dos líneas, usar el layout previsto para dos líneas.

## Densidad

Rangos orientativos:

- slide visual: 15–40 palabras;
- slide mixta: 35–65 palabras;
- slide explicativa: 55–75 palabras;
- máximo excepcional: 90 palabras, solo en definición normativa, instrucciones o bibliografía.

Además:

- máximo habitual de 5 bullets;
- un bullet puede ocupar hasta dos líneas;
- evitar más de 7 líneas continuas en un bloque;
- notas del orador reciben ejemplos, transiciones, derivaciones y aclaraciones extendidas;
- nunca reducir el cuerpo por debajo de 20 pt para “hacer entrar” texto.

## Títulos y redacción visible

Preferir:

- “La presión relaciona fuerza y área”.
- “La partícula oscila; la perturbación se propaga”.
- “Frecuencia y altura tonal están relacionadas, pero no son sinónimos”.
- “¿Qué cambia cuando duplicamos la distancia?”.

Evitar:

- “El plano maestro del sonido”.
- “El gran puente”.
- “Desmitificando el decibel”.
- “La caja de herramientas”.
- “Esta confusión destruye las ecuaciones”.

Los títulos pueden expresar una relación o una pregunta, pero deben sonar naturales en boca del docente.

## Fondos y planos

- Fondo principal: blanco.
- Fondo alternativo: marfil claro.
- Fondo bordó: solo en layouts de transición o cierre.
- No usar texturas, papel cuadriculado, redes, ondas decorativas o partículas.
- Una cuadrícula puede aparecer dentro de:
  - un gráfico cartesiano;
  - una representación de escala;
  - un plano técnico donde la grilla tenga significado.
- Los paneles de contenido son planos, con borde fino o fondo muy leve. No usar sombras por defecto.

## Formas, bordes y conectores

- Radio de esquina: 0–4 pt. La forma dominante es rectangular.
- Borde estándar: 1 pt.
- Borde de énfasis: 1,5 pt.
- Conectores: 1,5–2,25 pt.
- Flechas: cabeza simple, sin 3D.
- Líneas de guía: gris medio, 0,75–1 pt.
- Sombras: ninguna por defecto; sombra suave de 6 % de negro solo para separar una fotografía del fondo cuando sea necesario.
- No usar glow, bevel, reflejo o volumen.
- En diagramas, crear conectores detrás de los nodos y evitar cruces sobre etiquetas.

## Imágenes e ilustraciones

Orden de preferencia:

1. gráfico o diagrama propio;
2. fotografía técnica confiable;
3. ilustración anatómica o científica con fuente;
4. captura o visual de fabricante técnico;
5. imagen generada, solo cuando la visualización sintética sea pedagógicamente superior y esté registrada.

Reglas:

- una imagen debe tener un propósito explícito;
- no usar stock conceptual;
- no repetir la misma imagen salvo fondo o activo institucional;
- no deformar: recortar, no estirar;
- resolución recomendada: al menos 1200 px en su dimensión mayor para media slide y 2000 px para visual dominante;
- integrar caption cuando la lectura no sea autoevidente;
- añadir texto alternativo;
- registrar fuente y licencia;
- no usar memes por defecto; si se usa uno como recurso docente excepcional, debe estar justificado, acreditado y ser comprensible sin contexto cultural específico.

## Diagramas

- Usar formas nativas para diagramas simples.
- Usar SVG editable/importable para diagramas científicos más complejos.
- Mantener de 3 a 7 nodos principales por slide.
- Cada flecha debe tener un significado estable.
- Evitar iconografía genérica si un rótulo o forma simple explica mejor.
- Los diagramas fuente–medio–receptor, físico–perceptual y proceso de medición son patrones permitidos.
- No convertir cada explicación en un diagrama.

## Gráficos

- Preferir SVG o gráfico nativo de PowerPoint.
- Conservar script y datos cuando el gráfico sea generado.
- Fondo blanco o transparente.
- Ejes en `FA_CARBON_900`, rejilla en `FA_GRIS_200`.
- Curva principal en bordó o teal según semántica.
- Segunda curva en gris o ocre.
- Máximo habitual de tres series.
- Leyenda solo si las etiquetas directas no son posibles.
- Ejes con nombre y unidad.
- No truncar ejes sin indicarlo.
- No suavizar datos sin declararlo.
- Tamaño de texto dentro del gráfico: 16–20 pt equivalente en slide.
- Añadir una anotación o frase que explique qué debe observarse.

## Ecuaciones

- Usar ecuaciones nativas de PowerPoint (OMML).
- Fuente: Cambria Math.
- Definir cada símbolo al introducirlo.
- Indicar unidades.
- Explicar el significado físico.
- Mostrar un ejemplo numérico cuando ayude.
- Mantener coherencia con `style/notation_guide.md`.
- Una ecuación principal debe tener espacio propio y no quedar enterrada entre bullets.
- Usar color solo para relacionar términos con partes de un diagrama; no colorear cada símbolo.
- No usar capturas de ecuaciones.
- Si una ecuación proviene de una fuente histórica o facsimilar, acompañarla con una versión editable.

## Tablas

- Construir como tabla nativa.
- Encabezado con bordó o carbón; texto blanco cuando el contraste sea suficiente.
- Filas alternas en blanco y gris muy claro.
- Alineación:
  - texto a la izquierda;
  - símbolos al centro;
  - números al separador decimal cuando sea posible.
- Máximo recomendado:
  - 6 columnas;
  - 8 filas de contenido.
- Dividir tablas mayores.
- No usar bordes en todas las celdas si bandas y alineación bastan.
- Resaltar como máximo una fila, columna o celda por vez.
- Añadir una frase de lectura: “Observe que…”.

## Componentes semánticos

Los componentes autorizados se especifican en `style/component_catalog.md`. Los principales son:

- definición;
- ejemplo;
- observación;
- error frecuente;
- conexión clínica;
- fórmula;
- pregunta al curso;
- llamada a audio/video;
- fuente/crédito;
- mini recapitulación.

No se deben inventar nuevas tarjetas para cada unidad si un componente existente resuelve la función.

## Layouts

El catálogo completo se encuentra en `style/layout_catalog.md`. La selección debe responder a la función pedagógica. Los layouts no son decoraciones intercambiables.

Ritmo recomendado para una unidad larga:

- apertura;
- objetivo y mapa;
- bloques de 4–8 slides explicativas;
- pregunta o ejemplo;
- recapitulación parcial;
- nuevo bloque;
- aplicación;
- recapitulación final;
- puente a la unidad siguiente.

Evitar más de tres slides consecutivas con la misma silueta.

## Pie, numeración y fuentes

- Número de slide: automático, esquina inferior derecha.
- Texto de unidad/sección: breve, esquina inferior izquierda o centro-izquierda.
- Wordmark: pequeño y constante en slides de contenido; completo en portada y cierre.
- Fecha: no aparece por defecto.
- Créditos de imagen: dentro del área de contenido, 9–10 pt, cerca del recurso.
- Fuentes técnicas: en notas del orador mediante bloque `[Sources]`; una cita visible se agrega cuando la atribución es parte de la lectura.
- No dejar placeholders de fecha, número o footer vacíos.

## Accesibilidad

- Contraste equivalente a WCAG AA para texto común.
- No depender solo del color: combinar color con rótulo, patrón o posición.
- Texto alternativo en imágenes, gráficos y diagramas.
- Orden de lectura lógico.
- No incrustar texto esencial dentro de una imagen.
- No usar animaciones indispensables para comprender una slide estática.
- Evitar parpadeo y transiciones decorativas.

## Animaciones y multimedia

- Transición por defecto: ninguna o fundido breve.
- Animación permitida solo para:
  - revelar pasos;
  - mostrar una superposición;
  - comparar estados;
  - sincronizar con un audio.
- No animar títulos, logos o elementos decorativos.
- El componente de audio/video debe indicar:
  - qué observar o escuchar;
  - duración;
  - fuente;
  - alternativa si el medio no reproduce.

## Editabilidad

Debe permanecer editable:

- texto;
- formas y flechas;
- ecuaciones;
- tablas;
- gráficos nativos o SVG;
- captions;
- numeración;
- componentes;
- títulos y pies.

Una slide completa nunca se aplana como imagen.

Si un gráfico se exporta como SVG o PNG:

- conservar script y datos;
- usar SVG cuando se necesite editar etiquetas o colores;
- usar PNG de alta resolución solo cuando la complejidad lo justifique.

## Criterios de revisión visual

Antes de aprobar una slide:

- el título se lee sin esfuerzo;
- el cuerpo no baja de 20 pt;
- hay un foco principal;
- los márgenes son consistentes;
- no hay desbordes ni solapamientos;
- ecuaciones y símbolos están definidos;
- gráficos tienen ejes y unidades;
- imágenes no están deformadas;
- el componente usado conserva su significado;
- el pie y número aparecen correctamente;
- los créditos están presentes;
- la slide funciona a 25 % de zoom en pantalla;
- la slide no parece una tarjeta de dashboard ni una infografía automática.

## Prueba de identidad

Una slide pertenece al sistema si:

1. puede reconocerse como material académico de UCASAL sin que el logo sea dominante;
2. prioriza contenido y explicación por encima de decoración;
3. usa bordó, tipografía y grilla de forma coherente;
4. se puede editar sin reconstruir una imagen;
5. parece preparada por un docente que conoce el tema y su grupo.
