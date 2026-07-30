# Unidad 2 — Plan de recursos visuales

## Decisión general

La Unidad 2 se apoyará principalmente en **diagramas editables, ecuaciones nativas, gráficos propios y tablas nativas**. Las imágenes externas se limitan a estructuras anatómicas y dispositivos reales que agregan autenticidad. La multimedia se reserva para procesos temporales: oscilación amortiguada y propagación local.

No se propone ninguna imagen generada con IA. No existe una necesidad pedagógica que no pueda resolverse con geometría controlada, producción propia o fuentes técnicas verificables.

## Clasificación y tipos de apoyo

La columna `visual_class` usa las clases obligatorias:

- `chart`;
- `diagram`;
- `mixed`;
- `external_image`;
- `video_or_gif`;
- `equation_only`.

`none` indica deliberadamente que no se planifica un visual independiente. Una tabla nativa o una jerarquía tipográfica pueden aparecer en esas slides sin convertirse en asset.

La columna `apoyo` utiliza:

- **FOT:** fotografía real;
- **ILT:** ilustración técnica propia;
- **ANA:** imagen anatómica;
- **GRA:** gráfico cuantitativo propio;
- **DIA:** diagrama editable;
- **TAB:** tabla nativa;
- **ANI:** animación interna de PowerPoint;
- **GIF/VID:** archivo temporal;
- **AUD:** audio;
- **CAP:** captura de instrumento;
- **ECU:** ecuación nativa o anotada;
- **NING:** ninguna imagen.

## Registro slide por slide

| slide_id | visual_class | apoyo | recurso | decisión pedagógica | alternativa |
|---|---|---|---|---|---|
| U02-001 | none | NING | — | Portada tipográfica con motivo lineal mínimo; una imagen competiría con el título. | Línea técnica de superficie flexible construida en PowerPoint. |
| U02-002 | diagram | DIA + ANI | U02-DG001; U02-MEDIA001 opcional | Dos estados de membrana permiten predecir antes de formalizar; revelar fuerzas por clic. | Demostración breve propia o diagrama final estático. |
| U02-003 | none | NING | — | Las cuatro afirmaciones diagnósticas deben ser el único foco. | Marcas tipográficas A–D sin iconografía. |
| U02-004 | none | TAB | Tabla nativa | Dos columnas de prerrequisitos; no necesita imagen. | Lista jerarquizada. |
| U02-005 | none | NING | — | Cinco objetivos agrupados con indicadores tipográficos. | Mapa simple si la lista resulta administrativa. |
| U02-006 | diagram | DIA + ANI | U02-DG001 | Mapa de cinco etapas que se revela progresivamente. | Tabla de recorrido. |
| U02-007 | none | NING | — | Divisor de bloque, pregunta y fondo bordó. | Motivo lineal de frontera de sistema. |
| U02-008 | diagram | DIA | U02-DG002 | Dos fronteras posibles sobre la misma escena muestran que el sistema se elige. | Tabla sistema/entorno. |
| U02-009 | diagram | DIA | U02-DG002 | Un cuerpo, un agente externo y una flecha anclada representan interacción. | Ilustración técnica simple sin caja. |
| U02-010 | diagram | DIA | U02-DG002 | Eje positivo y dos direcciones convierten orientación en signo. | Recta numérica nativa. |
| U02-011 | diagram | DIA + ANI | U02-DG002 | Suma de flechas por etapas hasta obtener la resultante. | Tabla de fuerzas con signo. |
| U02-012 | diagram | DIA | U02-DG002 | Cuerpo con fuerzas equilibradas para confrontar reposo/ausencia de fuerza. | Consigna tipográfica sin visual. |
| U02-013 | equation_only | ECU + DIA | U02-DG002 | Ecuación anotada y mini trayectoria de velocidad constante. | Ecuación nativa sola. |
| U02-014 | none | NING | — | Recap verbal con tres comprobaciones; no agregar otro diagrama. | Mini versión de U02-DG002 si el grupo necesita apoyo. |
| U02-015 | none | NING | — | Divisor. | Flecha tipográfica fuerza neta → cambio de movimiento. |
| U02-016 | diagram | DIA | U02-DG003 | Cadena causal fuerza neta → aceleración → cambio de velocidad. | Tres frases alineadas. |
| U02-017 | equation_only | ECU | U02-DG003 | `F_neta = ma` con callouts de símbolos y unidades. | Ecuación nativa sin callouts en respaldo. |
| U02-018 | chart | GRA | U02-CH001 | Dos rectas permiten leer masa como inversa de la pendiente. | Comparación tabular para un valor de fuerza. |
| U02-019 | mixed | DIA + ECU | U02-DG003 | Diagrama de cuerpo libre junto a suma con signos y resultado. | Separar en diagrama y cálculo si se satura. |
| U02-020 | diagram | DIA | U02-DG003 | Dos masas reciben la misma fuerza; la geometría hace comparable la respuesta. | Pregunta verbal con razón `a_1/a_2`. |
| U02-021 | equation_only | ECU + DIA | U02-DG004 | Par de ecuaciones y dos cuerpos identificados. | Ecuación nativa más rótulos A/B. |
| U02-022 | diagram | DIA | U02-DG004 | Dos diagramas coordinados impiden cancelar acción y reacción. | Tabla fuerza–cuerpo receptor. |
| U02-023 | none | TAB | Tabla nativa | Tres leyes comparadas por pregunta, condición y evidencia. | Tres afirmaciones sin tabla. |
| U02-024 | none | NING | — | Divisor con pregunta sobre presión y superficie. | Silueta mínima de membrana. |
| U02-025 | diagram | DIA + ANI | U02-DG005 | Presiones de cada lado y fuerzas opuestas se revelan antes de `Δp`. | Estado final estático. |
| U02-026 | none | TAB | Tabla nativa | Comparación Pa/N por significado y unidad; una imagen no agrega información. | Dos bloques tipográficos. |
| U02-027 | equation_only | ECU + DIA | U02-DG005 | `Δp` anotada con dirección y signo sobre el esquema espacial. | Ecuación nativa con convención escrita. |
| U02-028 | equation_only | ECU + DIA | U02-DG005 | `F_pres = Δp·S` vinculada con superficie y normal. | Ecuación nativa sola. |
| U02-029 | equation_only | ECU | U02-DG005 | Cadena dimensional Pa·m² → N. | Tabla de unidades. |
| U02-030 | mixed | ILT + ECU | U02-DG005 | Superficie ideal pequeña junto a cálculo y alcance. | Cálculo nativo sin ilustración. |
| U02-031 | diagram | ILT + DIA | U02-DG005 | Superficie distribuida con callout “modelo, no anatomía literal”. | U02-IMG001 si hace falta estructura real. |
| U02-032 | diagram | DIA | U02-DG005 | Cadena `Δp → F_pres → F_neta → a` para recap. | Cuatro frases con unidades. |
| U02-033 | none | NING | — | Divisor; no anticipar el modelo completo. | Tres palabras: masa, elasticidad, amortiguamiento. |
| U02-034 | video_or_gif | GIF/VID | U02-MEDIA002; U02-MEDIA005 opcional | Comparar oscilaciones con menor/mayor amortiguamiento antes de la ecuación. | Secuencia estática de cuatro instantes. |
| U02-035 | diagram | DIA + ANI | U02-DG006 | Mapa de tres propiedades y tres efectos. | Tabla 3×2. |
| U02-036 | diagram | DIA | U02-DG006; apoyo U02-CH001 | Misma fuerza sobre dos masas para recuperar inercia. | Reutilizar un recorte del gráfico U02-CH001. |
| U02-037 | diagram | ILT + DIA | U02-DG006 | Masa desplazada, resorte y flecha restauradora. | Fotograma de demostración propia. |
| U02-038 | mixed | GRA + ECU | U02-CH002; U02-DG006 | Mini gráfico `F_el(x)` y ecuación anotada explican signo y pendiente. | Solo ecuación y dos estados de signo. |
| U02-039 | diagram | DIA | U02-DG006 | Comparación con/sin amortiguador manteniendo masa y resorte. | Secuencia estática de U02-MEDIA002. |
| U02-040 | mixed | GRA + ECU | U02-CH003; U02-DG006 | Mini gráfico `F_amort(v)` y ecuación anotada. | Solo ecuación y dos estados de velocidad. |
| U02-041 | diagram | DIA + ANI | U02-DG006 | Construcción masa → resorte → amortiguador → fuerza externa. | Modelo final estático. |
| U02-042 | equation_only | ECU + DIA | U02-DG006 | Balance completo con callout de un mecanismo por término. | Dos slides si cuatro callouts no caben. |
| U02-043 | diagram | DIA | U02-DG006 | Cuatro estados de signo con modelos pequeños y respuesta oculta. | Dividir en dos slides durante producción. |
| U02-044 | mixed | DIA + ECU + ANI | U02-DG006 | Modelo y cálculo por pasos; la predicción de signos precede al número. | Diagrama y cálculo en slides separadas. |
| U02-045 | mixed | TAB + DIA | U02-DG006 | Tabla nativa de amortiguamiento, atenuación y disipación con un esquema causal breve. | Tabla sola. |
| U02-046 | diagram | DIA | U02-DG006 | Mini modelo rotulado por función, no nueva derivación. | Tres afirmaciones sin diagrama. |
| U02-047 | none | NING | — | Divisor de energía. | Flecha simple fuerza–desplazamiento. |
| U02-048 | diagram | ILT + DIA | U02-DG007 | Fuerza paralela y desplazamiento muestran transferencia de energía. | Ecuación verbal. |
| U02-049 | equation_only | ECU + DIA | U02-DG007 | `W_trab = Fd` con condiciones geométricas anotadas. | Ecuación nativa sola. |
| U02-050 | equation_only | ECU | U02-DG007 | `E_c = ½mv²`, símbolos, unidades y callout “rapidez al cuadrado”. | Ecuación nativa sin visual adicional. |
| U02-051 | equation_only | ECU + ILT | U02-DG007 | Resorte deformado y `E_el = ½k_sx²`. | Ecuación nativa sola. |
| U02-052 | diagram | DIA + ANI | U02-DG007 | Dos depósitos cualitativos intercambian energía sin proporciones falsas. | Dos estados estáticos. |
| U02-053 | diagram | DIA | U02-DG007 | Frontera de sistema aislado y formas internas. | Definición tipográfica. |
| U02-054 | diagram | DIA + ANI | U02-DG007 | Entrada, almacenamiento, salida y disipación como rutas de igual grosor. | Tabla de destinos. |
| U02-055 | equation_only | ECU + DIA | U02-DG007 | Ecuación de balance vinculada a las rutas. | Ecuación nativa sola. |
| U02-056 | mixed | DIA + ECU | U02-DG007 | Ruta de energía y despeje de `E_disipada`. | Cálculo nativo con verificación de suma. |
| U02-057 | mixed | DIA + TAB | U02-DG007 | Recap “forma ≠ total” y corrección del término pérdida. | Tres afirmaciones. |
| U02-058 | none | NING | — | Divisor termodinámico. | Frontera vacía como motivo técnico. |
| U02-059 | diagram | DIA | U02-DG008 | Clasificación de cuatro tarjetas dentro o cruzando una frontera. | Tabla estado/transferencia. |
| U02-060 | none | TAB | Escala nativa °C–K | Escala lineal y equivalencia de unidades; sin termómetro decorativo. | Definición tipográfica. |
| U02-061 | diagram | DIA | U02-DG008 | Dos sistemas a igual temperatura y distinta cantidad de materia. | Comparación textual sin valores. |
| U02-062 | diagram | DIA | U02-DG008 | Dos sistemas y flecha de calor por diferencia de temperatura. | Definición sin imagen. |
| U02-063 | diagram | DIA | U02-DG008 | Frontera central con `T_temp`, `U`, calor y trabajo ubicados por función. | Tabla de dos columnas. |
| U02-064 | equation_only | ECU + DIA | U02-DG008 | Primera ley y orientación de signos sobre una frontera. | Ecuación nativa con convención escrita. |
| U02-065 | diagram | DIA + ANI | U02-DG008 | Cuatro casos de entrada/salida revelados uno por vez. | Tabla de signos. |
| U02-066 | mixed | DIA + ECU | U02-DG008 | Frontera, flechas y cálculo de `ΔU`. | Cálculo nativo solo. |
| U02-067 | none | TAB | Tabla nativa | Recap estado/transferencia/balance. | Tres afirmaciones. |
| U02-068 | none | NING | — | Divisor sobre dirección de procesos. | Flecha temporal simple. |
| U02-069 | video_or_gif | GIF/VID | U02-MEDIA003 | Oscilación amortiguada más destino energético cualitativo. | Tres fotogramas y flecha de energía. |
| U02-070 | none | NING | — | Definición de entropía sin metáfora visual. | Unidad destacada tipográficamente. |
| U02-071 | equation_only | ECU + DIA | U02-DG009 | `ΔS_total ≥ 0` con ramas reversible/irreversible. | Ecuación y dos frases. |
| U02-072 | none | TAB | Tabla nativa | Comparación reversible ideal/irreversible real; evitar dibujos de “orden”. | Dos columnas tipográficas. |
| U02-073 | diagram | DIA + ANI | U02-DG009 | Cadena fuerza disipativa → energía interna → producción de entropía. | Diagrama final estático. |
| U02-074 | none | NING | — | El error frecuente y su corrección son el foco. | Tabla error/evidencia. |
| U02-075 | none | TAB | Tabla nativa | Compatibilidad entre primera y segunda ley en tres afirmaciones. | Mini diagrama U02-DG009. |
| U02-076 | none | NING | — | Divisor sobre estado del aire. | Motivo de partículas muy tenue, solo si no parece decorativo. |
| U02-077 | video_or_gif | GIF/VID | U02-MEDIA004 | Compresión/rarefacción con partícula marcada. | Secuencia estática de tres estados. |
| U02-078 | diagram | DIA | U02-DG010; respaldo U02-MEDIA004 | Comparación frente móvil/partícula local en dos instantes. | Fotogramas del GIF. |
| U02-079 | equation_only | ECU + DIA | U02-DG010 | Aproximación lineal anotada con unidades y condiciones. | Ecuación nativa sola. |
| U02-080 | chart | GRA | U02-CH004 | Gráfico principal `c(ϑ)` con eje truncado declarado. | Tabla de cuatro puntos. |
| U02-081 | mixed | GRA + ECU | U02-CH004 | Marcadores a 20 y 30 °C junto al cálculo. | Tabla + cálculo. |
| U02-082 | mixed | DIA + ECU | U02-DG010 | Separar medio, fuente y percepción; `c = λf` solo como puente. | Tabla de inferencia válida/no válida. |
| U02-083 | none | NING | — | Divisor sobre límites de modelo. | Callout tipográfico “modelo ≠ diagnóstico”. |
| U02-084 | diagram | DIA | U02-DG011 | Cinco aplicaciones conectadas con cuatro conceptos. | Tabla aplicación/concepto. |
| U02-085 | external_image | ANA | U02-IMG001 | Corte anatómico público para mostrar estructura distribuida; acompañar con límite del modelo. | Diagrama propio de membrana multicapa. |
| U02-086 | mixed | ANA + DIA | U02-IMG002; U02-DG011 | Anatomía NIDCD a un lado y ruta energética propia al otro; no superponer cifras. | Solo diagrama propio de ruta pasiva. |
| U02-087 | mixed | FOT + DIA | U02-IMG004 preferida; U02-IMG003 condicionada; U02-DG011 | Dispositivo real y par de fuerzas sobre vibrador/cabeza. | Diagrama técnico propio si no hay foto autorizada. |
| U02-088 | diagram | DIA | U02-DG012 | Árbol que elige ecuación según dato y pregunta. | Tabla tarea/modelo. |
| U02-089 | diagram | DIA + ANI | U02-DG012 | Cadena final explicada flecha por flecha. | Estado final estático. |
| U02-090 | none | NING | — | Cierre tipográfico hacia oscilaciones. | Silueta mínima masa–resorte. |
| U02-091 | diagram | DIA | U02-DG013 | Dos mini diagramas de sistema, eje y signos. | Checklist textual. |
| U02-092 | mixed | DIA + TAB | U02-DG013 | Soluciones diagnósticas con mini esquemas solo donde aportan. | Tabla afirmación/justificación. |
| U02-093 | diagram | DIA | U02-DG004 | Tres contraejemplos de tercera ley y equilibrio. | Elegir un único caso si la densidad supera el mínimo. |
| U02-094 | none | TAB | Tabla nativa | Convenciones del libro, guía y slides. | Dividir en dos tablas si excede ocho filas. |
| U02-095 | mixed | TAB + DIA | U02-DG014 | Tabla de parámetros junto a mini modelo. | Tabla sola. |
| U02-096 | mixed | DIA + ECU | U02-DG014 | Diagrama de fuerzas y cálculo completo. | Dividir modelo y cálculo. |
| U02-097 | none | TAB | Tabla nativa | Cuatro términos comparados; no usar iconografía. | Dos tablas de dos términos. |
| U02-098 | equation_only | ECU | Ecuaciones nativas | Soluciones compactas con control dimensional. | Dividir en dos slides. |
| U02-099 | none | NING | — | Consignas de práctica; no revelar solución visualmente. | Esquema mínimo del sistema si falta contexto. |
| U02-100 | none | TAB | Referencias nativas | Bibliografía y afirmación sostenida por cada fuente. | Lista legible. |
| U02-101 | equation_only | ECU + DIA | U02-DG010 | Ecuación general anotada con parámetros e hipótesis. | Tabla de parámetros. |
| U02-102 | equation_only | ECU + DIA | U02-DG010 | Cadena de unidades y cancelaciones. | Ecuación nativa por etapas. |
| U02-103 | mixed | GRA + DIA + ECU | U02-CH004; U02-CH005; U02-DG010 | Comparar `c` y `t` para dos temperaturas y un trayecto fijo. | Tabla de resultados si U02-CH005 exagera visualmente la diferencia. |
| U02-104 | diagram | DIA | U02-DG015 | Cuatro fronteras con calor/trabajo entrando o saliendo. | Tabla de signos. |
| U02-105 | equation_only | ECU + DIA | U02-DG009 | Desigualdad con dos ramas y alcance de sistema total. | Ecuación y dos casos textuales. |
| U02-106 | diagram | DIA | U02-DG015 | Plan de resolución de tres ramas sin resultados. | Tabla datos/tarea. |
| U02-107 | mixed | DIA + ECU | U02-DG015 | Modelo de superficie y suma completa de fuerzas. | Diagrama y cálculo separados. |
| U02-108 | mixed | DIA + ECU | U02-DG015 | Ruta de energía, cálculo térmico y callout de límites. | Dos slides si no cumple 22 pt. |
| U02-109 | none | TAB | Referencias nativas | Fuentes técnicas de propagación y termodinámica. | Lista legible. |
| U02-110 | none | TAB | Tabla nativa | Símbolos y glosario divididos en mecánica/termodinámica. | Dos slides de respaldo. |

## Recursos externos seleccionados

| asset_id | URL | autor u organización | título | licencia conocida | acceso | slides | propósito | alternativa | estado |
|---|---|---|---|---|---|---|---|---|---|
| U02-IMG001 | https://commons.wikimedia.org/wiki/File:Tympanic_membrane_cross-section.svg | Inductiveload / Wikimedia Commons | Tympanic membrane cross-section | Dominio público | 2026-07-29 | U02-085 | Mostrar capas y estructura real frente al modelo concentrado. | Diagrama multicapa propio. | descargado |
| U02-IMG002 | https://www.nidcd.nih.gov/es/multimedia/partes-del-oido | NIH/NIDCD | Partes del oído | Dominio público; crédito solicitado | 2026-07-29 | U02-086 | Ubicar membrana y cadena osicular. | Diagrama propio simplificado. | descargado |
| U02-IMG003 | https://radioear.us/products/bone-transducers | RadioEar | B71/B81 bone transducer headset | No se publicó licencia de reutilización | 2026-07-29 | U02-087 | Mostrar el dispositivo real. | Foto propia U02-IMG004 o diagrama U02-DG011. | no descargar sin permiso |
| U02-MEDIA005 | https://phet.colorado.edu/es_PE/simulations/masses-and-springs-basics | PhET, University of Colorado Boulder | Masas y Resortes: Fundamentos | CC BY 4.0 solo después de verificar que la versión es anterior a 2026-03-29 | 2026-07-29 | U02-034 | Comparar amortiguamiento de forma interactiva. | Video propio U02-MEDIA002. | shortlist |

## Recursos descartados

- Fotos genéricas de personas con auriculares: no representan los mecanismos de la unidad.
- Imágenes de stock de resortes o termómetros: sustituyen un diagrama verificable por decoración.
- “Entropía como habitación desordenada”: metáfora físicamente insuficiente.
- Sankey de energía: sugeriría proporciones inexistentes.
- Capturas de páginas del PDF o ecuaciones rasterizadas: reducen editabilidad y legibilidad.
- Capturas de audiogramas o instrumentos: introducen medición clínica fuera del objetivo.
- Audio: no permite observar fuerzas, balances ni irreversibilidad y puede adelantar relaciones perceptuales.
- Imágenes generadas por IA: no existe una necesidad que justifique el riesgo anatómico o físico.

## Descargas realizadas

Solo se descargaron dos originales claramente reutilizables:

1. `units/unit_02/assets/external/u02_img_001_tympanic_membrane_cross_section.svg`;
2. `units/unit_02/assets/external/u02_img_002_parts_of_ear_nidcd_es.jpg`.

No se descargó la imagen de RadioEar ni la simulación PhET. Las adaptaciones, recortes y versiones de inserción deberán guardarse sin reemplazar los originales.

