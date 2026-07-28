# Catálogo de componentes

## Principio

Los componentes expresan funciones pedagógicas repetibles. No son una biblioteca de tarjetas decorativas.

Reglas comunes:

- máximo habitual de un componente destacado por slide;
- dos componentes solo si tienen funciones distintas y no compiten;
- forma rectangular, radio de 0–4 pt;
- borde de 1–1,5 pt;
- sin glow, bevel ni sombra por defecto;
- texto editable;
- rótulo breve y consistente;
- color semántico estable entre unidades;
- el componente debe caber dentro de la grilla del layout;
- no crear variantes nuevas sin registrarlas en `decision_log.md`.

## Tokens compartidos

| Elemento | Especificación |
|---|---|
| Padding horizontal | 0,18–0,24 in |
| Padding vertical | 0,12–0,18 in |
| Rótulo | Calibri Bold 16–18 pt |
| Texto | Calibri 20–22 pt |
| Caption interno | Calibri 14–16 pt |
| Borde | 1–1,5 pt |
| Fondo | blanco o tinte semántico de baja saturación |
| Radio | 0–4 pt |
| Icono | opcional; máximo uno y solo si informa |

## `FA_C01_DEFINICION`

**Función:** fijar el significado de un término, magnitud o propiedad.

**Anatomía:**

1. rótulo `DEFINICIÓN`;
2. término;
3. definición completa;
4. símbolo y unidad opcionales.

**Estilo:**

- borde izquierdo de 0,06 in en `FA_BORDO_900`;
- fondo blanco;
- término en 24–28 pt semibold;
- definición en 20–22 pt.

**Límite:** 55 palabras.

**Usar cuando:** la precisión verbal es central.

**No usar:** para listas de varias definiciones ni para una frase que solo repite el título.

**Editabilidad:** texto y borde nativos.

## `FA_C02_EJEMPLO`

**Función:** concretar una idea abstracta.

**Anatomía:**

1. rótulo `EJEMPLO`;
2. situación o dato;
3. aplicación/resultado;
4. imagen o mini esquema opcional.

**Estilo:**

- borde superior corto en `FA_FISICO_700`;
- fondo `FA_FISICO_100` al 60–80 %;
- sin icono de lamparita.

**Límite:** 45 palabras más una ecuación breve.

**Usar cuando:** el ejemplo puede resolverse o interpretarse en menos de un minuto.

**No usar:** para derivaciones completas; usar `FA_10_EJEMPLO_RESUELTO`.

## `FA_C03_OBSERVACION`

**Función:** señalar una condición, límite o detalle que cambia la interpretación.

**Anatomía:**

1. rótulo `OBSERVACIÓN`;
2. afirmación;
3. condición o consecuencia opcional.

**Estilo:**

- borde gris;
- pequeña barra bordó;
- fondo blanco;
- no usar amarillo brillante.

**Límite:** 35 palabras.

**Usar cuando:** el contenido no es una advertencia de seguridad ni un error conceptual.

**No usar:** para cada nota secundaria.

## `FA_C04_ERROR_FRECUENTE`

**Función:** corregir una concepción frecuente.

**Anatomía:**

1. rótulo `ERROR FRECUENTE`;
2. formulación del error entre comillas o en estilo diferenciado;
3. corrección;
4. evidencia breve.

**Estilo:**

- línea izquierda `FA_ERROR_700`;
- fondo blanco;
- corrección destacada con carbón o verde apagado;
- no usar una X gigante.

**Límite:** 60 palabras.

**Usar cuando:** el error fue observado o es previsible por la estructura conceptual.

**No usar:** para errores tipográficos o detalles administrativos.

**Accesibilidad:** el rótulo verbal evita depender del rojo.

## `FA_C05_CONEXION_CLINICA`

**Función:** vincular un concepto físico con Fonoaudiología, Audiología o voz.

**Anatomía:**

1. rótulo `CONEXIÓN CON FONOAUDIOLOGÍA`;
2. concepto físico;
3. situación profesional;
4. interpretación que habilita.

**Estilo:**

- borde `FA_CLINICO_700`;
- fondo `FA_CLINICO_100`;
- icono opcional solo si es específico: audiómetro, micrófono, oído anatómico o señal.

**Límite:** 65 palabras.

**Usar cuando:** la relación es concreta y verificable.

**No usar:** para afirmar de forma genérica que “esto es importante en clínica”.

## `FA_C06_FORMULA`

**Función:** presentar una relación matemática como objeto de lectura.

**Anatomía:**

1. ecuación nativa;
2. nombre opcional;
3. definición de símbolos;
4. unidad o control dimensional.

**Estilo:**

- fondo blanco;
- borde inferior fino bordó o sin borde;
- ecuación de 30–40 pt;
- Cambria Math.

**Límite:** una ecuación principal y, como máximo, una forma equivalente.

**Usar cuando:** la relación se introduce, interpreta o aplica.

**No usar:** para una fórmula aislada sin contexto.

**Editabilidad:** OMML obligatorio.

## `FA_C07_PREGUNTA_CURSO`

**Función:** activar predicción, recuperación o comprobación.

**Anatomía:**

1. rótulo `PREGUNTA`;
2. consigna;
3. datos/figura opcional;
4. pista opcional.

**Estilo:**

- barra superior en `FA_BORDO_600`;
- fondo marfil;
- pregunta en 24–28 pt;
- sin signo de interrogación decorativo gigante.

**Límite:** 45 palabras.

**Usar cuando:** la respuesta puede discutirse o resolverse con lo ya enseñado.

**No usar:** para preguntas retóricas que no se retoman.

**Notas:** la respuesta esperada y el tiempo sugerido se registran en notas del orador.

## `FA_C08_MEDIA`

**Función:** orientar la reproducción de audio, video o GIF.

**Anatomía:**

1. tipo de recurso;
2. consigna de observación/escucha;
3. duración;
4. control o enlace;
5. fuente;
6. alternativa.

**Estilo:**

- borde `FA_FISICO_700`;
- fondo blanco;
- icono funcional de reproducción o audio, no decorativo.

**Límite:** 50 palabras.

**Usar cuando:** el medio añade evidencia que una imagen estática no aporta.

**No usar:** como enlace sin contexto.

**Accesibilidad:** incluir transcripción, descripción o captura alternativa según el recurso.

## `FA_C09_FUENTE_CREDITO`

**Función:** atribuir una imagen, dato, norma o recurso.

**Anatomía:**

- autor/organización;
- título o descripción;
- año;
- URL o referencia corta;
- licencia cuando corresponda.

**Estilo:**

- Calibri 9–10 pt;
- `FA_GRIS_500`;
- alineación izquierda;
- sin caja salvo que el fondo afecte el contraste.

**Ubicación:** cerca del recurso y dentro del área segura.

**Usar siempre:** con assets externos y cuando la fuente sea relevante para interpretar.

**No usar:** como bibliografía completa en cada slide; las fuentes extensas van en notas `[Sources]`.

## `FA_C10_MINI_RECAP`

**Función:** sintetizar un bloque antes de avanzar.

**Anatomía:**

1. rótulo `HASTA ACÁ`;
2. tres afirmaciones;
3. una pregunta de control opcional.

**Estilo:**

- fondo marfil;
- tres líneas o columnas, sin tarjetas separadas;
- rótulo bordó.

**Límite:** 55 palabras.

**Usar cuando:** termina un bloque de 5–10 slides o antes de un salto de abstracción.

**No usar:** como repetición de títulos.

## `FA_C11_DATO_CLAVE`

**Función:** destacar un valor, rango o constante que se usará inmediatamente.

**Anatomía:**

1. valor;
2. unidad;
3. condición;
4. fuente opcional.

**Estilo:**

- valor en 30–36 pt;
- unidad en 22–24 pt;
- condición en 16–18 pt;
- borde fino, sin “tarjeta KPI”.

**Ejemplo:** `c ≈ 343 m/s` con condición `aire, 20 °C`.

**Límite:** un dato principal por componente.

**No usar:** para llenar espacio ni para cifras sin condición.

## `FA_C12_PASO`

**Función:** identificar un paso dentro de un proceso o ejemplo resuelto.

**Anatomía:**

- número de paso;
- verbo;
- contenido breve;
- resultado intermedio opcional.

**Estilo:**

- número en bordó;
- texto sin caja completa;
- conector simple entre pasos.

**Límite:** 20–35 palabras por paso.

**Usar:** dentro de `FA_10_EJEMPLO_RESUELTO` o `FA_12_PROCESO`.

**No usar:** como navegación permanente.

## Combinaciones autorizadas

| Combinación | Condición |
|---|---|
| Definición + fórmula | La fórmula forma parte de la definición y no compite visualmente. |
| Ejemplo + dato clave | El dato se usa inmediatamente en el ejemplo. |
| Conexión clínica + fuente | La aplicación incluye un recurso externo. |
| Pregunta + media | El audio/video es necesario para responder. |
| Error frecuente + fórmula | La fórmula demuestra la corrección. |
| Mini recap + pregunta | La pregunta comprueba las tres ideas sintetizadas. |

## Combinaciones a evitar

- definición + observación + ejemplo como tres tarjetas;
- error frecuente + check/X gigantes;
- conexión clínica + fotografía de stock;
- dato clave + varias métricas tipo dashboard;
- mini recap + seis cajas;
- media + QR + enlace + botón + iconos redundantes.

## Prueba de componente

Antes de aprobar:

- ¿se entiende su función por el rótulo?
- ¿el color conserva el mismo significado que en otras unidades?
- ¿podría resolverse con texto plano sin perder claridad?
- ¿es editable?
- ¿tiene texto alternativo si incluye un visual?
- ¿respeta márgenes y tamaños mínimos?
- ¿se usa porque enseña o porque “viste” la slide?

