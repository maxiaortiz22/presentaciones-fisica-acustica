"""Genera la redacción y las notas de U10 desde el storyboard aprobado.

No altera la arquitectura ni construye el PowerPoint. Los textos visibles son
específicos para cada slide; visual, layout, fuente, transición y estado se
leen directamente de storyboard.md.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

UNIT=Path(__file__).resolve().parents[1]
STORYBOARD=UNIT/"storyboard.md"


def t(s:str)->str:
    return s.strip()


VISIBLE={
"U10-001":t("""
**Unidad 10 · Física Acústica**

**El ruido y su caracterización**

Tiempo · frecuencia · nivel · función
"""),
"U10-002":t("""
En un mismo consultorio coinciden:

- tránsito que ingresa desde la avenida;
- climatización continua;
- portazos del pasillo;
- conversación y evaluaciones auditivas.

**Pregunta inicial:** ¿qué describiríamos, qué mediríamos y qué todavía no podríamos concluir?
"""),
"U10-003":t("""
Al finalizar podremos:

- **distinguir** señal física, contexto y función;
- **describir** evolución temporal, estadística y espectro;
- **calcular** RMS, contenido de banda, nivel equivalente y SNR;
- **interpretar** resultados con sus condiciones y límites;
- **proponer** controles en fuente, trayecto y receptor.
"""),
"U10-004":t("""
**Ya disponible**

- presión acústica, media y RMS;
- niveles en dB y referencia;
- espectro, bandas y filtros.

**Conviene reactivar**

- SNR y enmascaramiento;
- ponderaciones y detectores;
- fuente–trayecto–receptor.

**Mini diagnóstico:** ¿RMS y promedio significan lo mismo?
"""),
"U10-005":t("""
1. Señal y contexto  
2. Tiempo  
3. Estadística  
4. Frecuencia y “colores”  
5. Señales de prueba  
6. Descriptores y SNR  
7. Enmascaramiento  
8. Exposición y control  
9. Integración

Habrá recapitulaciones antes de cambiar de representación.
"""),
"U10-006":t("""
**Pregunta guía**

¿Cuándo una misma señal funciona como ruido?

Separaremos tres planos: **fenómeno físico**, **registro** y **valoración según la tarea**.
"""),
"U10-007":t("""
- Una fuente produce una perturbación mecánica en el medio.
- La presión acústica instantánea se representa como `p(t)` y se expresa en pascales (`Pa`).
- El micrófono transforma esa variación en una señal registrable.
- El registro conserva información seleccionada por el sistema de medición; no “captura todo el sonido”.
"""),
"U10-008":t("""
La señal física puede permanecer igual y cambiar su función:

- **objetivo:** queremos escuchar una conversación;
- **objeto de medición:** queremos caracterizarla;
- **interferencia o enmascarante:** compite con otra señal o se agrega deliberadamente.

Lo que cambia es la **tarea**; no necesariamente cambian presión, espectro o duración.
"""),
"U10-009":t("""
**Uso contextual**  
Señal no deseada respecto de una tarea o receptor.

**Uso físico o de señales**  
Señal aleatoria descrita por propiedades estadísticas y espectrales.

**Uso operativo**  
Señal empleada para medir, probar o controlar otra respuesta.

Ruido no significa automáticamente “sonido fuerte” ni “sonido molesto”.
"""),
"U10-010":t("""
Clasifique y justifique según la tarea:

1. Conversación vecina durante una audiometría.
2. Ruido del equipo mientras se mide el ambiente.
3. Señal NBN presentada en una prueba.
4. Tránsito durante una conversación clínica.

**Consigna:** indique qué es señal objetivo, ruido de fondo u operación de prueba. Puede haber más de una respuesta si cambia la tarea.
"""),
"U10-011":t("""
**Determinística**

- Un modelo y sus parámetros permiten predecir cada muestra.
- Ejemplo: una sinusoide ideal de amplitud y frecuencia conocidas.

**Aleatoria**

- No se predice cada muestra; se describen propiedades del conjunto.
- Ejemplo: una realización de ruido limitado en banda.

Ambas señales del gráfico tienen `p_rms = 1 mPa`.
"""),
"U10-012":t("""
**Realización:** registro concreto de un proceso durante un intervalo.

- A y B difieren muestra a muestra.
- Ambas fueron normalizadas a media `0 mPa` y RMS `1 mPa`.
- Una semilla fija permite repetir una secuencia pseudoaleatoria de ensayo.

Repetible no significa determinística en el sentido del modelo físico estudiado.
"""),
"U10-013":t("""
- **Señal:** posee presión, duración y espectro.
- **Función:** depende de la tarea y del contexto.
- **Predictibilidad:** indica si cada muestra puede anticiparse mediante un modelo.

**Comprobación:** llamar “ruido” a una señal, ¿informa por sí solo su nivel o su espectro?
"""),
"U10-014":t("""
**Pregunta guía**

¿Qué cambia muestra a muestra y qué permanece describible?

La respuesta requiere declarar una **ventana de observación**, una **estadística** y un **patrón temporal**.
"""),
"U10-015":t("""
Una señal puede variar en cada instante y ser aproximadamente estacionaria durante una ventana.

**Criterio práctico:** dentro del intervalo declarado, propiedades como media, varianza o espectro permanecen aproximadamente estables.

Estacionario **no** significa que `p(t)` sea constante.
"""),
"U10-016":t("""
El gráfico muestra **el mismo registro** en dos escalas:

- en una ventana breve, las propiedades pueden parecer estables;
- durante minutos, una envolvente lenta revela cambios;
- la conclusión depende de la ventana y del criterio elegido.

Los niveles son relativos: no representan una medición SPL.
"""),
"U10-017":t("""
Antes de nombrar cada panel, lea los ejes: `t` en segundos y `p(t)` en milipascales.

- continuo aproximadamente estable;
- continuo fluctuante;
- intermitente;
- impulsivo.

Son realizaciones sintéticas: la forma temporal no informa por sí sola exposición ni efecto.
"""),
"U10-018":t("""
Asigne una o más categorías y justifique:

- máquina que funciona toda la hora y cambia lentamente de nivel;
- golpes breves separados por silencios;
- ventilación encendida durante toda la consulta;
- portazos ocasionales en el pasillo.

**Regla:** continuo, fluctuante, intermitente e impulsivo describen rasgos; no siempre son opciones excluyentes.
"""),
"U10-019":t("""
Una muestra responde: **¿qué valor hubo en ese instante?**

Una ventana permite preguntar:

- ¿cuál fue el valor medio?;
- ¿qué tamaño cuadrático tuvo la señal?;
- ¿cuánto se dispersó?;
- ¿con qué frecuencia aparecieron distintos valores?

Cada descriptor conserva información diferente y descarta otra.
"""),
"U10-020":t("""
`p̄ = (1/N) Σᵢ₌₁ᴺ pᵢ`

- `pᵢ`: muestra `i` de presión acústica, en `Pa`;
- `N`: cantidad de muestras, sin unidad;
- `p̄`: media de presión, en `Pa`.

La media conserva el signo: valores positivos y negativos pueden compensarse.
"""),
"U10-021":t("""
`p_rms = √[(1/N) Σᵢ₌₁ᴺ pᵢ²]`

1. Cuadrar evita la cancelación entre signos.
2. Promediar resume el intervalo.
3. Extraer la raíz devuelve la unidad `Pa`.

El RMS cuantifica el **tamaño cuadrático** de la señal; no es una media con signo.
"""),
"U10-022":t("""
`σ_p² = (1/N) Σᵢ₌₁ᴺ (pᵢ − p̄)²`

- `pᵢ − p̄`: desviación de cada muestra respecto de la media;
- `σ_p²`: varianza de la presión, en `Pa²`.

Identidad útil: `p_rms² = σ_p² + p̄²`.

Si `p̄ = 0 Pa`, coinciden `p_rms²` y `σ_p²`; los conceptos siguen siendo distintos.
"""),
"U10-023":t("""
Datos: `−2, −1, 0, 1, 2 mPa`

1. `p̄ = (−2−1+0+1+2)/5 = 0 mPa`
2. Promedio de cuadrados: `(4+1+0+1+4)/5 = 2 mPa²`
3. `p_rms = √2 mPa ≈ 1,41 mPa`
4. `σ_p² = 2 mPa²`

**Interpretación:** media cero no significa ausencia de variación acústica.
"""),
"U10-024":t("""
Ambos registros tienen:

- `p̄ = 0 mPa`;
- `p_rms = 1 mPa`;
- `σ_p² = 1 mPa²`.

Sin embargo, A recorre valores continuos y B solo adopta `−1 mPa` y `+1 mPa`.

El histograma conserva información que el RMS no muestra.
"""),
"U10-025":t("""
| Descriptor | Pregunta | Unidad | No informa por sí solo |
|---|---|---|---|
| Media `p̄` | ¿Hay compensación con signo? | `Pa` | tamaño cuadrático |
| RMS `p_rms` | ¿Qué tamaño cuadrático tiene? | `Pa` | distribución |
| Varianza `σ_p²` | ¿Cuánto se dispersa respecto de `p̄`? | `Pa²` | forma temporal |
| Distribución | ¿Qué valores aparecen y con qué frecuencia? | `1` | orden temporal |
"""),
"U10-026":t("""
**Pregunta guía**

¿Cómo se reparte el contenido entre frecuencias y bandas?

Usaremos tres ideas: **frecuencia**, **densidad espectral** y **ancho de banda**.
"""),
"U10-027":t("""
Dos representaciones de una misma realización:

- el dominio temporal muestra cómo cambia `p(t)`;
- la densidad espectral muestra cómo se distribuye el valor cuadrático entre frecuencias;
- ninguna representación reemplaza a la otra.

La curva de la derecha es una PSD estimada por Welch; no es la respuesta en frecuencia de un sistema.
"""),
"U10-028":t("""
Una densidad expresa contenido cuadrático **por unidad de ancho de banda**.

- altura: `S_pp` en `Pa²/Hz`;
- base: `Δf` en `Hz`;
- área: contenido cuadrático en `Pa²`.

Para densidad aproximadamente constante: `p_B,rms² ≈ S_pp · Δf`.

El esquema es conceptual y no está a escala.
"""),
"U10-029":t("""
`p_B,rms² = ∫_(f_L)^(f_H) S_pp(f) df`

- `S_pp(f)`: PSD unilateral de presión, en `Pa²/Hz`;
- `f_L`, `f_H`: límites inferior y superior, en `Hz`;
- `p_B,rms²`: presión cuadrática media contenida en la banda, en `Pa²`.

La integral se lee como una suma de franjas de frecuencia.
"""),
"U10-030":t("""
Señal sintética con densidad constante:

1. `S_pp = 4,0 × 10⁻⁸ Pa²/Hz`
2. `Δf = 100 Hz`
3. `p_B,rms² = S_pp Δf = 4,0 × 10⁻⁶ Pa²`
4. `p_B,rms = 2,0 × 10⁻³ Pa = 2,0 mPa`
5. Con `p_ref = 20 µPa`: `L_p = 40 dB SPL`

No es un límite de exposición.
"""),
"U10-031":t("""
En una banda finita declarada:

`S_pp(f) = S₀`

- la densidad es constante **por hertz**;
- intervalos de igual ancho `Δf` contienen igual presión cuadrática media;
- el modelo ideal no se extiende físicamente de `0 Hz` a frecuencia infinita.
"""),
"U10-032":t("""
Las bandas de octava sucesivas duplican su ancho en hertz.

Con PSD blanca constante:

- banda centrada en `125 Hz`: contenido relativo `×1`;
- `250 Hz`: `×2`;
- `500 Hz`: `×4`;
- cada octava siguiente vuelve a duplicar el contenido.

El blanco es constante por hertz, **no** por octava.
"""),
"U10-033":t("""
En una banda finita, el ruido rosa ideal se modela como:

`S_pp(f) = K/f`

- la densidad disminuye cuando aumenta `f`;
- una octava superior es más ancha en hertz;
- ambos efectos se compensan: el contenido integrado es aproximadamente constante por octava.

La pendiente de la PSD es `−1` en escala log–log.
"""),
"U10-034":t("""
**Ruido blanco**

- PSD constante por `Hz`;
- contenido creciente por octava.

**Ruido rosa**

- PSD proporcional a `1/f`;
- contenido constante por octava.

Para comparar, mantenga la misma banda y lea primero qué magnitud representa cada eje.
"""),
"U10-035":t("""
**Consigna de escucha · 10 s por clip**

1. Mantener el mismo dispositivo y volumen de reproducción.
2. Escuchar un fragmento de ruido blanco y uno rosa, normalizados con el criterio documentado.
3. Describir diferencias sin afirmar “igual sonoridad”.

**Alternativa sin audio:** usar la comparación estática U10-CH-010.

No elevar el volumen para “notar mejor” la diferencia.
"""),
"U10-036":t("""
Para describir un “color” de ruido hay que declarar:

- la magnitud representada: `S_pp(f)`;
- la unidad: `Pa²/Hz`;
- la regla espectral: constante o proporcional a `1/f`;
- la banda de validez;
- el agrupamiento usado para comparar.

**Control:** ¿se comparan intervalos iguales en `Hz` u octavas?
"""),
"U10-037":t("""
**Pregunta guía**

¿Qué convierte un ruido de banda ancha en una señal especificada?

`Entrada de banda ancha → filtro → salida`

El nombre de la salida no reemplaza su espectro, banda, nivel ni procedimiento.
"""),
"U10-038":t("""
En el programa aparece “ruido vocal”. Usaremos la denominación técnica:

**ruido con forma espectral de habla**

- señal aleatoria filtrada según un espectro objetivo;
- deben declararse banda, nivel, equipo y calibración;
- conserva un contorno espectral; **no contiene habla inteligible**;
- no existe una curva universal deducible del nombre.
"""),
"U10-039":t("""
Una misma entrada de banda ancha puede atravesar filtros diferentes:

- un filtro con respuesta objetivo produce ruido con forma espectral de habla;
- un filtro pasabanda produce ruido de banda estrecha;
- la salida depende de la respuesta `H(f)` del filtro.

El esquema muestra forma espectral cualitativa; no representa calibración ni tolerancias normativas.
"""),
"U10-040":t("""
**NBN:** ruido de banda estrecha (*narrow-band noise*).

Para especificarlo se declaran:

- límite inferior `f_L` y superior `f_H`, en `Hz`;
- frecuencia central `f_c`, con su definición;
- ancho `B`, pendientes y forma del filtro;
- nivel, transductor, calibración y procedimiento.

NBN no significa automáticamente “tercio de octava”.
"""),
"U10-041":t("""
Datos: `f_L = 900 Hz`; `f_H = 1100 Hz`.

1. `B = f_H − f_L`
2. `B = 1100 Hz − 900 Hz = 200 Hz`

Todavía faltan: `f_c`, forma y pendientes del filtro, nivel, calibración, transductor y procedimiento.

**Interpretación:** calcular el ancho es necesario; no alcanza para definir una señal de prueba.
"""),
"U10-042":t("""
| Señal | Regla espectral | Agrupamiento útil | Parámetros que deben declararse |
|---|---|---|---|
| Blanco | `S_pp = S₀` | intervalos iguales en `Hz` | banda y nivel |
| Rosa | `S_pp ∝ 1/f` | octavas | banda y nivel |
| Forma de habla | contorno objetivo | bandas del espectro objetivo | curva, equipo y calibración |
| NBN | contenido concentrado | banda declarada | `f_L`, `f_c`, `f_H`, pendientes y nivel |
"""),
"U10-043":t("""
Para cada tarea, elija una familia de señal y anote qué falta especificar:

1. Comparar contenido por intervalos iguales de `Hz`.
2. Comparar contenido por octavas sucesivas.
3. Crear una interferencia con contorno semejante al habla.
4. Concentrar energía alrededor de una frecuencia de prueba.

**Respuesta completa = tipo + función + banda + nivel + equipo/procedimiento.**
"""),
"U10-044":t("""
Una etiqueta como “blanco”, “rosa”, “habla” o “NBN” debe acompañarse por:

1. **espectro o regla de conformación**;
2. **banda y límites**;
3. **nivel y referencia**;
4. **equipo, calibración y procedimiento**.

**Comprobación:** ¿qué dato falta si solo se informa “se usó NBN”?
"""),
"U10-045":t("""
**Pregunta guía**

¿Qué pregunta responde cada número de una medición?

Distinguiremos **nivel variable**, **máximo**, **pico**, **equivalente**, **excedencia** y **SNR**.
"""),
"U10-046":t("""
Antes de leer el número, registre:

1. señal y micrófono;
2. ponderación frecuencial (`A`, `C` o `Z`);
3. detector o respuesta temporal;
4. intervalo de observación `T`;
5. posición, rango, calibración y condición de funcionamiento.

Un valor en dB sin configuración está incompleto.
"""),
"U10-047":t("""
Sobre el mismo evento sintético:

- `p_peak`: mayor valor absoluto de la presión instantánea;
- `L_max,F`: mayor indicación del detector Fast (`τ = 125 ms` en este ejemplo);
- `L_eq,2 s`: nivel constante con igual promedio cuadrático durante `2 s`.

Las tres magnitudes responden operaciones diferentes y no comparten un único eje.
"""),
"U10-048":t("""
**Es frecuente pensar:** “Impulse”, máximo y pico nombran el mismo extremo.

**Corrección**

- `L_max` es la mayor indicación de un detector con respuesta temporal declarada;
- `L_peak` se obtiene con un detector de pico de presión;
- la ponderación temporal *Impulse* no convierte una lectura en `L_peak`.

Siempre informe detector, ponderación e intervalo.
"""),
"U10-049":t("""
`L_eq,T` representa el nivel constante que conserva el mismo promedio cuadrático que la señal variable durante `T`.

- `T`: intervalo de integración, en `s`, `min` u `h`;
- la ponderación frecuencial debe indicarse: por ejemplo, `L_Aeq,T`;
- no es un promedio aritmético de números en dB;
- no informa por sí solo máximo ni pico.
"""),
"U10-050":t("""
Cuatro intervalos iguales de `15 min`: `88`, `92`, `86` y `90 dB(A)`.

`L_Aeq,1 h = 10 log₁₀[(10^(88/10)+10^(92/10)+10^(86/10)+10^(90/10))/4]`

`L_Aeq,1 h ≈ 89,6 dB(A)`

1. Convertir a cantidades lineales.
2. Promediarlas porque las duraciones son iguales.
3. Volver a decibeles.
"""),
"U10-051":t("""
`L_N,T` es el nivel excedido durante `N %` del intervalo `T`.

- `L_10,T`: nivel excedido durante `10 %` de `T`;
- `L_90,T`: nivel excedido durante `90 %` de `T`;
- la curva de excedencia es monótona;
- el significado ambiental de un percentil depende del procedimiento.

`L_90,T` no equivale automáticamente a “ruido de fondo”.
"""),
"U10-052":t("""
**Ruido de fondo**

- está presente en el entorno o la medición;
- interfiere respecto de una tarea definida.

**Enmascarante**

- se introduce deliberadamente;
- busca modificar la detectabilidad de otra señal.

Una misma familia espectral puede cumplir cualquiera de las dos funciones según el uso.
"""),
"U10-053":t("""
Para niveles comparables:

`SNR = L_señal − L_ruido`

Ejemplo: `L_señal = 65 dB SPL`; `L_ruido = 58 dB SPL`.

`SNR = 65 dB − 58 dB = +7 dB`

La resta requiere misma posición, banda, referencia, ponderación e intervalo. El signo no predice por sí solo comprensión o molestia.
"""),
"U10-054":t("""
En los tres paneles se mantienen:

- la señal objetivo;
- la realización temporal del ruido;
- los ejes y el intervalo.

Solo cambia el RMS del ruido para obtener `SNR = +12 dB`, `0 dB` y `−6 dB`.

Menor SNR significa mayor contribución relativa del ruido; no equivale a una respuesta perceptual universal.
"""),
"U10-055":t("""
En una conversación de aula o consultorio, la SNR es una parte del problema.

También importan:

- espectro y evolución temporal del ruido;
- reverberación y distancia;
- contenido lingüístico y tarea;
- audición, atención y experiencia del oyente.

**Aplicación:** mejorar la SNR física puede ayudar; no garantiza por sí sola inteligibilidad.
"""),
"U10-056":t("""
Antes de interpretar, pregunte:

- ¿nivel en cada instante? → `L(t)`;
- ¿mayor indicación del detector? → `L_max`;
- ¿pico de presión? → `L_peak`;
- ¿promedio cuadrático durante `T`? → `L_eq,T`;
- ¿porcentaje de excedencia? → `L_N,T`;
- ¿contraste entre señal y ruido comparables? → `SNR`.
"""),
"U10-057":t("""
**Pregunta guía**

¿Qué señal se presenta, a qué oído y con qué finalidad?

La revisión será **conceptual**: señal de prueba, ruta cruzada, enmascarante y respuesta. No se desarrollará un protocolo clínico completo.
"""),
"U10-058":t("""
Enmascarar significa **reducir la detectabilidad** de una señal por la presencia de otra.

- intervienen una señal objetivo y un enmascarador;
- el efecto depende de frecuencia, nivel y relación temporal;
- puede elevar el umbral de detección;
- no significa que el oído esté protegido de exposición.
"""),
"U10-059":t("""
Antes de analizar una situación controlada, identifique:

1. **señal de prueba:** ¿qué se quiere detectar?;
2. **enmascarante:** ¿qué señal compite?;
3. **canal o receptor:** ¿dónde se presentan?;
4. **criterio de respuesta:** ¿qué conducta o medida indica detección?

Sin estas cuatro identificaciones, “hubo enmascaramiento” queda incompleto.
"""),
"U10-060":t("""
- La señal de prueba se dirige al **oído evaluado**.
- Parte de la señal puede alcanzar el **oído no evaluado** por una ruta cruzada.
- El enmascarante se presenta deliberadamente al oído no evaluado.
- Su función es reducir la detectabilidad de esa llegada cruzada.

**Límite:** el esquema no fija indicaciones, niveles, incrementos, transductores ni criterio de finalización.
"""),
"U10-061":t("""
Rotule en el esquema:

1. oído evaluado;
2. oído no evaluado;
3. señal de prueba;
4. posible ruta cruzada;
5. enmascarante.

Después responda: ¿qué información faltaría para convertir este esquema en un protocolo clínico?
"""),
"U10-062":t("""
| | Enmascaramiento en prueba | Protección auditiva |
|---|---|---|
| Propósito | modificar detectabilidad | reducir exposición que llega al oído |
| Acción | agregar señal controlada | interponer o usar un protector adecuado |
| Resultado | controlar una respuesta de prueba | reducir una métrica de exposición |
| Verificación | protocolo clínico | medición y criterio aplicable |

Enmascarar no es proteger.
"""),
"U10-063":t("""
En una acufenometría pueden compararse características perceptuales mediante tonos o ruidos.

La evaluación puede registrar, según el procedimiento:

- semejanza perceptual;
- frecuencia o banda asociada;
- nivel de comparación;
- respuesta de la persona evaluada.

**Límite clínico:** comparar no prescribe un tipo de ruido, un nivel terapéutico ni un plan individual.
"""),
"U10-064":t("""
- La función del enmascarante debe estar explícita.
- La arquitectura de la prueba identifica señal, ruta, oído y respuesta.
- El tipo espectral del ruido no determina por sí solo la técnica.

**Requiere protocolo vigente:** indicaciones, niveles iniciales, incrementos, meseta, límites y finalización.
"""),
"U10-065":t("""
**Pregunta guía**

¿Qué puede medirse, qué puede inferirse y dónde conviene actuar?

Separaremos **exposición física**, **resultado funcional**, **salud/diagnóstico** y **control**.
"""),
"U10-066":t("""
| Plano | Pregunta | Evidencia necesaria | Límite |
|---|---|---|---|
| Exposición | ¿qué nivel y duración hubo? | medición calibrada y condiciones | no diagnostica |
| Función | ¿cómo rindió la persona en una tarea? | prueba y contexto | no identifica causa por sí sola |
| Salud/diagnóstico | ¿existe una alteración clínica? | evaluación profesional integrada | no se deduce de un único nivel |

Una medición **informa**; no determina automáticamente los otros planos.
"""),
"U10-067":t("""
Para una conclusión individual se integran:

- medición y condiciones de exposición;
- historia temporal y laboral/ambiental;
- evidencia funcional;
- evaluación clínica;
- variables mediadoras y fuentes alternativas.

Los riesgos poblacionales orientan prevención; una relación causal individual requiere más evidencia.
"""),
"U10-068":t("""
| Documento | Pregunta principal | Metadatos imprescindibles |
|---|---|---|
| Norma de medición | ¿cómo medir y reportar? | número, edición, instrumento y procedimiento |
| Guía sanitaria | ¿qué efectos o recomendaciones considera? | población, alcance y fecha |
| Criterio legal | ¿qué obligación rige? | jurisdicción, vigencia y descriptor |

No trasladar un número entre documentos con propósitos distintos.
"""),
"U10-069":t("""
Un único valor global en `dB(A)` no describe si una cabina es apta para todas las pruebas.

También deben declararse:

- niveles por bandas;
- tipo de prueba, vía y transductor;
- frecuencias y menor nivel de prueba;
- posición, intervalo, calibración y ruido propio;
- documento técnico y criterio aplicable.

La ponderación A puede ocultar información espectral relevante.
"""),
"U10-070":t("""
1. **Fuente:** reducir la generación mediante mantenimiento, sustitución u operación.
2. **Trayecto:** modificar transmisión, aberturas, encapsulado o reflexiones.
3. **Receptor:** organizar posición, tiempo, tarea o protección cuando corresponda.
4. **Verificación:** comparar la misma métrica antes y después, bajo condiciones declaradas.

Primero se identifica el eslabón; después se elige el mecanismo.
"""),
"U10-071":t("""
| Término | Qué cambia | Cómo se verifica |
|---|---|---|
| Reducción de ruido | resultado general | misma métrica antes/después |
| Absorción | reflexiones en una superficie/recinto | `α`, `A_eq`, reverberación |
| Aislamiento | transmisión entre espacios | índice y condiciones de ensayo |
| Cancelación activa | presión en una región y banda | respuesta espacial/frecuencial |
| Protección | exposición que llega al receptor | atenuación efectiva y uso |

El resultado no identifica por sí solo el mecanismo.
"""),
"U10-072":t("""
Para cada acción indique **dónde actúa**, **qué mecanismo usa** y **qué mediría**:

- mantenimiento de un ventilador;
- sellado de una abertura;
- absorción en el recinto;
- limitar el tiempo de permanencia;
- protección auditiva seleccionada por criterio aplicable.

Puede proponer combinaciones, pero la comparación antes/después debe conservar la misma métrica y configuración.
"""),
"U10-073":t("""
La Fonoaudiología formula preguntas físicas vinculadas con una tarea:

- **evaluación auditiva:** ¿el ruido residual limita la prueba?;
- **voz y habla:** ¿qué SNR y reverberación acompañan la comunicación?;
- **ambiente clínico:** ¿qué fuentes y rutas dominan?;
- **prevención:** ¿qué exposición y documento deben considerarse?

Reconocer el límite de la inferencia también es parte de la práctica profesional.
"""),
"U10-074":t("""
**Uso exploratorio posible**

- comparar momentos o lugares con el mismo dispositivo y procedimiento;
- detectar cambios grandes que justifiquen una medición formal;
- registrar observaciones preliminares.

**No permite certificar** sin calibración, respuesta frecuencial conocida, posición, intervalo, ponderaciones, rango e incertidumbre.

Una app no es automáticamente equivalente a un sonómetro trazable.
"""),
"U10-075":t("""
1. Definir el **propósito**.
2. Configurar y documentar la **medición**.
3. Obtener el **dato** con unidad y referencia.
4. Formular una **interpretación acotada**.
5. Elegir una **acción** vinculada con el mecanismo.
6. **Verificar** con la misma métrica.

Medir, interpretar y controlar son decisiones encadenadas.
"""),
"U10-076":t("""
**Pregunta integradora**

¿Cómo se caracteriza un problema real sin saltar pasos?

Volvemos al consultorio y añadimos, por capas: **tiempo**, **estadística**, **espectro**, **nivel**, **función**, **control** y **autoridad técnica**.
"""),
"U10-077":t("""
En el consultorio coinciden:

- tránsito desde la avenida;
- climatización continua;
- portazos del pasillo;
- conversación como señal de interés;
- evaluación auditiva con requisitos propios;
- profesionales, pacientes y equipos como receptores diferentes.

**Primera decisión:** separar fuentes y tareas antes de elegir descriptores.
"""),
"U10-078":t("""
**Tránsito:** envolvente lenta; ventana de decenas de segundos; continuo fluctuante.

**Climatización:** continuo aproximadamente estable; ventana compatible con su ciclo.

**Portazos:** eventos breves; impulsivos e intermitentes; ventana centrada en cada evento.

Para cada fuente: registrar forma temporal, elegir ventana y recién después calcular media, RMS, varianza o distribución.
"""),
"U10-079":t("""
**Tránsito:** medir por bandas y resumir intervalos con `L_eq,T` compatible.

**Climatización:** describir espectro y `L_Aeq,T` con configuración declarada.

**Portazos:** distinguir `L_max` de `L_peak`.

**Conversación:** medir señal y ruido en condiciones comparables para calcular SNR.

No mostrar valores sin instrumento, posición, ponderación e intervalo.
"""),
"U10-080":t("""
- El ruido de fondo está presente según la tarea.
- Un enmascarante audiométrico se introduce deliberadamente y exige protocolo.
- Los controles pueden actuar en fuente, trayecto o receptor.
- La aptitud de la sala y la exposición requieren documentos aplicables.
- Las decisiones clínicas corresponden a profesionales y protocolos vigentes.

Caracterizar no equivale a autorizar una práctica.
"""),
"U10-081":t("""
Diseñe un plan en seis pasos:

1. **Evidencia:** qué señal o fenómeno observar.
2. **Configuración:** dónde, cuándo y con qué instrumento.
3. **Descriptor:** magnitud, unidad, ponderación e intervalo.
4. **Interpretación:** qué puede afirmarse y qué no.
5. **Acción:** fuente, trayecto o receptor; mecanismo esperado.
6. **Verificación/autoridad:** misma métrica y norma o protocolo necesario.
"""),
"U10-082":t("""
Decida: **correcta, incorrecta o incompleta**, y justifique cuatro en clase.

1. Aleatorio significa imposible de medir.
2. Estacionario significa constante.
3. Blanco conserva igual contenido por octava.
4. Rosa conserva igual densidad por hertz.
5. Igual `L_eq,T` implica iguales picos.
6. *Impulse* mide `L_peak`.
7. Todo NBN ocupa un tercio de octava.
8. `L_90,T` siempre es ruido de fondo.
9. La SNR predice sola inteligibilidad.
10. Enmascarar protege el oído.
11. Un valor `dB(A)` certifica una cabina.
12. Absorber y aislar son equivalentes.
"""),
"U10-083":t("""
- “Ruido” exige declarar **señal, tarea y receptor**.
- La evolución temporal requiere **ventana** y clasificación no excluyente.
- Media, RMS, varianza y distribución conservan información distinta.
- PSD y ancho de banda explican blanco, rosa, forma de habla y NBN.
- Máximo, pico, equivalente, percentiles y SNR responden preguntas diferentes.
- Medición, efecto, control y decisión clínica o normativa deben mantenerse separados.

**Evidencia mínima:** justificar qué medir, cómo interpretarlo y qué límite reconocer.
"""),
"U10-084":t("""
**Medir bien también es saber qué no puede concluirse.**

Pregunta de salida:

> Antes de medir un problema de ruido, ¿qué pregunta formularía ahora que no habría formulado al comenzar el curso?

La caracterización continúa en la práctica profesional mediante mediciones trazables, documentos vigentes y trabajo interdisciplinario.
"""),
"U10-085":t("""
| Término | Definición mínima | Unidad / condición |
|---|---|---|
| Aleatorio | muestras descritas probabilísticamente | proceso/realización |
| Estacionario | propiedades estables en una ventana | intervalo declarado |
| PSD `S_pp` | presión cuadrática por ancho de banda | `Pa²/Hz` |
| RMS | raíz del promedio de cuadrados | `Pa` |
| NBN | ruido concentrado en banda declarada | `f_L`, `f_c`, `f_H` |
| Fondo | interferencia presente según tarea | contexto |
| `L_eq,T` | promedio cuadrático expresado como nivel | `dB`, referencia y `T` |
"""),
"U10-086":t("""
Partimos de la varianza:

`σ_p² = (1/N) Σ(pᵢ − p̄)²`

Al expandir y usar `(1/N)Σpᵢ = p̄`:

`σ_p² = (1/N)Σpᵢ² − p̄²`

Como `(1/N)Σpᵢ² = p_rms²`:

`p_rms² = σ_p² + p̄²`

Todos los términos se expresan en `Pa²`.
"""),
"U10-087":t("""
Para ruido rosa ideal `S_pp(ν)=K/ν`, en una octava de `f` a `2f`:

`∫_f^(2f) (K/ν) dν = K[ln ν]_f^(2f)`

`= K(ln 2f − ln f) = K ln 2`

El resultado no depende de `f`: cada octava contiene el mismo valor cuadrático medio dentro de la banda del modelo.
"""),
"U10-088":t("""
**Recurso condicionado · no redactar el ejemplo todavía**

Para intervalos de distinta duración, el promedio debe ponderar cada cantidad lineal por su duración.

Pendiente antes de producción:

- verificar la fórmula general con una fuente seleccionada;
- elegir un ejemplo coherente con la notación del curso;
- comprobar unidades y resultado;
- registrar la ampliación respecto del storyboard/libro.
"""),
"U10-089":t("""
**Soluciones seleccionadas · presentar por revelado o dividir en 089a–c**

- Media/RMS/varianza: `0, 2, 2, 4 mPa` → `p̄=2 mPa`, `p_rms≈2,45 mPa`, `σ_p²=2 mPa²`.
- PSD: `9,0×10⁻¹⁰ Pa²/Hz` entre `500–2500 Hz` → `p_rms²=1,8×10⁻⁶ Pa²`, `p_rms≈1,34 mPa`, `L_p≈36,5 dB SPL`.
- NBN: `900–1100 Hz` → `B=200 Hz`; faltan centro, pendientes, nivel, calibración y procedimiento.
- SNR: `68−73=−5 dB`; el ruido supera a la señal en nivel bajo condiciones comparables.
- Tres intervalos iguales: `74, 78, 82 dB(A)` → `L_Aeq,30 min≈79,2 dB(A)`.
"""),
"U10-090":t("""
| Descriptor | Debe acompañarse por |
|---|---|
| `L(t)` | ponderación frecuencial y temporal; instante/registro |
| `L_max` | detector, ponderación e intervalo de búsqueda |
| `L_peak` | detector de pico, rango, referencia y procedimiento |
| `L_eq,T` | ponderación frecuencial e intervalo `T` |
| `L_N,T` | `N`, `T`, ponderación y muestreo |
| Exposición/dosis | nivel, duración, norma, jurisdicción y regla aplicable |
"""),
"U10-091":t("""
**SLIDE BLOQUEADA POR FUENTE**

No completar hasta que la cátedra seleccione y valide un protocolo clínico institucional.

Campos pendientes: indicaciones, oído de prueba/no prueba, nivel inicial, incrementos, meseta, sobreenmascaramiento, criterio de detención y límites.

No usar este placeholder en clase como contenido clínico.
"""),
"U10-092":t("""
**SLIDE BLOQUEADA POR FUENTE**

No incorporar límites de exposición o ruido admisible hasta definir:

- documento y edición;
- jurisdicción y vigencia;
- población y propósito;
- descriptor, ponderación e intervalo;
- regla de intercambio o procedimiento.

No fusionar ISO, OMS, NIOSH y legislación argentina en una curva única.
"""),
"U10-093":t("""
**Fuentes primarias del curso**

- Programa oficial 2025.
- Libro del curso: capítulo 10, LaTeX y PDF.

**Apoyo transversal**

- guías de estilo, notación y glosario;
- unidades 4, 5, 7, 8 y 9 para prerrequisitos.

**Fuentes externas citadas en el capítulo**

- normas de medición y audiometría;
- guías sanitarias y clínicas;
- normativa jurisdiccional.

Consultar `source_map.md`; no usar QR ni URL sin verificación final.
"""),
}

EQUATIONS={
"U10-020":"`p̄ = (1/N) Σᵢ₌₁ᴺ pᵢ`",
"U10-021":"`p_rms = √[(1/N) Σᵢ₌₁ᴺ pᵢ²]`",
"U10-022":"`σ_p² = (1/N) Σᵢ₌₁ᴺ (pᵢ − p̄)²`; `p_rms² = σ_p² + p̄²`",
"U10-023":"Sustituciones visibles en cuatro pasos; unidades `mPa`, `mPa²`.",
"U10-028":"`p_B,rms² ≈ S_pp · Δf` para densidad aproximadamente constante.",
"U10-029":"`p_B,rms² = ∫_(f_L)^(f_H) S_pp(f) df`",
"U10-030":"`L_p = 20 log₁₀(p_B,rms/p_ref)`, con `p_ref = 20 µPa`.",
"U10-031":"`S_pp(f)=S₀` dentro de una banda finita.",
"U10-033":"`S_pp(f)=K/f` dentro de una banda finita.",
"U10-041":"`B=f_H−f_L=1100 Hz−900 Hz=200 Hz`.",
"U10-047":"`L_peak`, `L_max,F` y `L_eq,T` se mantienen como magnitudes separadas.",
"U10-049":"Definición conceptual de `L_eq,T`; forma integral reservada para notas si se necesita.",
"U10-050":"`L_Aeq = 10 log₁₀[(1/M)Σⱼ10^(Lⱼ/10)]` para `M` intervalos de igual duración.",
"U10-051":"`L_N,T`: nivel excedido durante `N %` del intervalo `T`.",
"U10-053":"`SNR=L_señal−L_ruido=+7 dB` bajo condiciones comparables.",
"U10-086":"`p_rms² = σ_p² + p̄²`, con todos los términos en `Pa²`.",
"U10-087":"`∫_f^(2f) (K/ν)dν = K ln 2`.",
"U10-089":"Cinco resultados seleccionados; dividir o revelar para mantener 22 pt.",
}

DEFINITIONS={
"U10-007":"`p(t)`: presión acústica instantánea en función del tiempo, expresada en `Pa`.",
"U10-009":"Ruido: término contextual, físico/de señales u operativo; el uso debe declararse.",
"U10-011":"Determinístico: predecible desde un modelo y sus parámetros. Aleatorio: cada muestra se caracteriza probabilísticamente.",
"U10-012":"Realización: registro concreto de un proceso durante un intervalo.",
"U10-015":"Estacionario, en sentido práctico: propiedades elegidas aproximadamente estables dentro de una ventana declarada.",
"U10-020":"Media: suma de las muestras dividida por su cantidad; conserva el signo.",
"U10-021":"RMS: raíz cuadrada del promedio de los cuadrados.",
"U10-022":"Varianza: promedio del cuadrado de las desviaciones respecto de la media.",
"U10-029":"PSD unilateral de presión: valor cuadrático medio por unidad de ancho de banda para frecuencias no negativas.",
"U10-031":"Ruido blanco ideal: modelo con PSD constante por hertz dentro de una banda declarada.",
"U10-033":"Ruido rosa ideal: modelo con PSD proporcional a `1/f` e igual contenido cuadrático por octava dentro de una banda.",
"U10-038":"Ruido con forma espectral de habla: señal aleatoria filtrada según un espectro objetivo declarado.",
"U10-040":"NBN: ruido de banda estrecha definido por límites, centro, ancho, forma, nivel y generación.",
"U10-049":"Nivel equivalente: nivel constante con el mismo promedio cuadrático que la señal variable durante `T`.",
"U10-051":"Percentil de excedencia `L_N,T`: nivel excedido durante `N %` de `T`.",
"U10-052":"Ruido de fondo: interferencia presente según la tarea. Enmascarante: señal agregada deliberadamente para reducir detectabilidad.",
"U10-053":"SNR: diferencia de niveles compatibles entre señal y ruido, expresada en `dB`.",
"U10-058":"Enmascaramiento: reducción de detectabilidad de una señal por otra.",
"U10-066":"Exposición, función y salud son planos relacionados que requieren evidencias distintas.",
"U10-070":"Control en fuente–trayecto–receptor: organización inicial de intervenciones y verificación.",
"U10-071":"Reducción: resultado; absorción, aislamiento y cancelación: mecanismos; protección: intervención sobre el receptor.",
}

EXAMPLES={
"U10-002":"Caso del consultorio junto a una avenida, sin resolver todavía.",
"U10-008":"Una conversación es objetivo al escucharla, objeto al medirla e interferencia respecto de otra tarea.",
"U10-010":"Cuatro casos de clasificación contextual.",
"U10-016":"Una misma señal observada durante 5 s y 2 min.",
"U10-018":"Máquina fluctuante y golpes impulsivos/intermitentes.",
"U10-023":"Cinco muestras simétricas en `mPa`.",
"U10-024":"Dos distribuciones con iguales media, RMS y varianza.",
"U10-030":"Banda rectangular sintética de `100 Hz`.",
"U10-032":"Octavas exactas centradas entre `125 Hz` y `8000 Hz`.",
"U10-035":"Dos clips propios pendientes de selección/documentación; alternativa visual completa disponible.",
"U10-041":"NBN entre `900 Hz` y `1100 Hz`.",
"U10-043":"Cuatro tareas de selección de señal sin prescribir niveles clínicos.",
"U10-047":"Evento sintético con componente impulsiva y detector Fast.",
"U10-050":"Cuatro intervalos iguales de `15 min`.",
"U10-053":"Señal `65 dB SPL`, ruido `58 dB SPL`, SNR `+7 dB`.",
"U10-054":"Tres mezclas sintéticas coordinadas.",
"U10-055":"Conversación con ventilación continua y portazos.",
"U10-063":"Acufenometría como comparación perceptual, no como prescripción terapéutica.",
"U10-069":"Evaluación de ruido residual en una cabina sin declarar cumplimiento.",
"U10-072":"Cinco acciones ubicadas en fuente, trayecto o receptor.",
"U10-074":"Uso exploratorio de una aplicación telefónica no calibrada.",
"U10-077":"Caso integrador del consultorio junto a la avenida.",
"U10-081":"Plan de caracterización y control en seis pasos.",
"U10-089":"Resultados seleccionados de los ejercicios G/A del capítulo.",
}

QA={
"U10-004":("Antes de medir, ¿qué tres decisiones debemos explicitar?","Qué fenómeno interesa, con qué descriptor se lo representará y para qué decisión se usará."),
"U10-010":("¿El ruido está definido por la fuente o por la tarea?","Por la relación entre señal, contexto y tarea; una misma fuente puede cambiar de función."),
"U10-013":("¿Qué comparten y qué no comparten dos realizaciones?","Comparten el proceso o modelo estadístico; no comparten necesariamente las muestras instantáneas."),
"U10-018":("¿Qué rasgo temporal distingue a la máquina fluctuante de los golpes?","La primera cambia de forma relativamente continua; los golpes concentran energía en eventos breves."),
"U10-025":("¿Qué descriptor falta si dos señales tienen igual RMS pero una posee picos mucho mayores?","Un descriptor de extremos, como el pico o el factor de cresta, y la forma temporal."),
"U10-035":("¿Qué diferencia perceptual esperarían entre ruido blanco y rosa al igualar el nivel global?","El blanco suele percibirse más brillante; el rosa distribuye de modo más equilibrado el contenido por octavas."),
"U10-036":("¿Qué debe acompañar siempre al nombre de un color de ruido?","La definición espectral, la banda efectiva, el nivel y el método de generación."),
"U10-041":("¿Cuál es el ancho de una banda entre 900 Hz y 1100 Hz?","200 Hz."),
"U10-043":("¿Qué se prioriza al elegir una señal: su nombre o su función?","Su función en la tarea, junto con banda, nivel y protocolo."),
"U10-044":("¿Qué eje permite distinguir variación continua de eventos breves?","El eje temporal; luego se complementa con frecuencia, nivel y función."),
"U10-047":("¿Puede Lmax,F reemplazar al nivel de pico?","No. Responden a detectores y constantes temporales diferentes."),
"U10-051":("¿Qué significa que un nivel sea L10?","Que fue excedido durante el 10 % del intervalo declarado."),
"U10-053":("¿Cuál es la SNR para 65 dB de señal y 58 dB de ruido?","+7 dB, si ambos niveles son comparables."),
"U10-054":("¿Qué mezcla facilita más la detección de la señal?","La de mayor SNR; la respuesta debe justificarse comparando niveles compatibles."),
"U10-056":("¿Qué descriptor usarían para energía promedio durante una consulta?","Leq,T, declarando el intervalo T; podrían sumarse percentiles o picos según la pregunta."),
"U10-060":("¿Qué función cumple el enmascarante en este esquema conceptual?","Reducir la detectabilidad de una posible respuesta cruzada en el oído no evaluado; la slide no define el protocolo clínico."),
"U10-061":("¿Cuándo conviene un enmascarante de banda estrecha?","Cuando el protocolo requiere concentrar la energía alrededor de una región frecuencial definida."),
"U10-062":("¿La presencia de enmascaramiento permite inferir automáticamente un diagnóstico?","No. Es un fenómeno perceptual que debe interpretarse dentro de una tarea y un protocolo."),
"U10-066":("¿Exposición, desempeño funcional y diagnóstico son equivalentes?","No. Son planos relacionados, pero requieren medidas y evidencias distintas."),
"U10-069":("¿Una lectura global en dBA basta para certificar una cabina?","No. Hace falta el procedimiento y el criterio normativo aplicable, además del control instrumental."),
"U10-072":("¿Dónde suele ser más eficaz intervenir primero?","En la fuente, si es viable; luego en el trayecto y finalmente sobre el receptor."),
"U10-074":("¿Para qué sirve una aplicación no calibrada?","Para exploración y comparación orientativa, no para certificar cumplimiento ni diagnóstico."),
"U10-078":("¿Qué información aporta el tiempo que no aporta por sí solo el espectro?","La ocurrencia, duración, repetición y carácter impulsivo o intermitente de los eventos."),
"U10-079":("¿Qué preguntarían antes de elegir un descriptor?","Qué decisión se necesita tomar y qué propiedad del fenómeno es relevante."),
"U10-080":("¿Qué tres separaciones conceptuales debemos conservar?","Fuente versus función, promedio versus pico y exposición versus diagnóstico."),
"U10-081":("¿Cuál es el primer paso del plan?","Formular la pregunta y reconocer la tarea antes de elegir instrumentos o descriptores."),
"U10-082":("¿Por qué “igual L_eq,T implica iguales picos” es incorrecto?","Porque L_eq,T conserva el promedio cuadrático durante T, pero no la forma temporal ni los extremos."),
"U10-084":("¿Qué idea de la unidad usarían mañana en una observación clínica?","Respuesta abierta, pero debe vincular una pregunta concreta con un descriptor y una limitación."),
"U10-086":("¿Por qué RMS y desvío estándar coinciden cuando la media es cero?","Porque p_rms² = σ_p² + p̄²; si p̄ = 0, sus cuadrados son iguales."),
"U10-087":("¿Por qué cada octava de ruido rosa contiene el mismo valor cuadrático?","Porque integrar K/f entre f y 2f da K ln 2, independiente de f."),
}

ERRORS={
"U10-009":"Definir ruido como sinónimo de sonido fuerte o desagradable.",
"U10-011":"Confundir aleatorio con desordenado o carente de estructura.",
"U10-015":"Tomar estacionariedad como constancia muestra por muestra.",
"U10-017":"Tratar las categorías temporales como casilleros universales y excluyentes.",
"U10-020":"Concluir que media cercana a cero implica ausencia de sonido.",
"U10-021":"Confundir RMS con promedio aritmético.",
"U10-022":"Usar varianza y RMS como sinónimos cuando la media no es nula.",
"U10-029":"Leer la altura de la PSD como si fuera el contenido total de una banda.",
"U10-031":"Suponer ruido blanco ideal de ancho de banda infinito en un sistema real.",
"U10-033":"Creer que el ruido rosa tiene menor contenido en cada octava sucesiva.",
"U10-035":"Confundir una diferencia de timbre con una comparación controlada de sonoridad.",
"U10-038":"Presentar una única curva de habla como universal para toda tarea o idioma.",
"U10-040":"Nombrar NBN sin informar banda, forma espectral y nivel.",
"U10-048":"Usar pico, máximo y equivalente como nombres intercambiables.",
"U10-049":"Promediar niveles en dB de manera aritmética.",
"U10-050":"Calcular el promedio aritmético de los cuatro valores en dB(A).",
"U10-051":"Interpretar L90 como sinónimo universal de ruido de fondo.",
"U10-053":"Inferir inteligibilidad solo a partir de una SNR global.",
"U10-058":"Confundir enmascaramiento con protección auditiva.",
"U10-060":"Aplicar una regla clínica sin explicitar el protocolo validado.",
"U10-066":"Convertir una medida de exposición en un diagnóstico individual.",
"U10-069":"Usar una lectura orientativa para declarar cumplimiento normativo.",
"U10-071":"Confundir absorción, aislamiento, cancelación y protección personal.",
"U10-074":"Presentar el teléfono como sustituto de un sonómetro calibrado.",
"U10-082":"Responder solo “verdadero” o “falso” sin nombrar la magnitud, condición o evidencia que corrige la afirmación.",
"U10-088":"Completar el ejemplo con valores o fórmulas antes de verificar la fuente.",
"U10-091":"Improvisar reglas de enmascaramiento clínico.",
"U10-092":"Mostrar límites de exposición sin jurisdicción, versión y fuente vigentes.",
}

DEMO={
"U10-035":"Reproducir audio solo si los clips propios están documentados y el nivel es seguro; si no, usar U10-CH-010 como alternativa estática.",
"U10-054":"Revelar las tres mezclas de menor a mayor SNR y pedir una predicción antes de mostrar la etiqueta.",
"U10-074":"Mostrar la lectura del teléfono como exploración; contrastarla verbalmente con una medición calibrada.",
}

SUBTITLES={
"U10-001":"Unidad 10",
"U10-006":"De la intuición a una clasificación operativa",
"U10-026":"Del registro temporal a la distribución por frecuencia",
"U10-045":"Descriptores distintos para preguntas distintas",
"U10-057":"Fenómeno perceptual, uso clínico y límites",
"U10-067":"Medir, interpretar e intervenir sin mezclar planos",
"U10-076":"Integración del caso y transferencia",
"U10-084":"Una pregunta para llevarse de la unidad",
}

CAPTION_OVERRIDES={
"U10-050":"Ejemplo de nivel equivalente para cuatro intervalos iguales: conversión lineal, promedio energético y retorno a decibeles.",
}

ALT_OVERRIDES={
"U10-050":"Seis etapas: cuatro intervalos de 15 minutos a 88, 92, 86 y 90 dB(A), seguidos por el promedio lineal energético y el resultado L_Aeq,1 h de aproximadamente 89,6 dB(A).",
}

BLOCKED={"U10-088","U10-091","U10-092"}


def parse_storyboard()->list[dict[str,str]]:
    rows=[]
    for raw in STORYBOARD.read_text(encoding="utf-8").splitlines():
        if not raw.startswith("| U10-"):
            continue
        cells=[c.strip() for c in raw.strip().strip("|").split("|")]
        if len(cells)!=15:
            raise ValueError(f"Fila con {len(cells)} columnas: {raw}")
        keys=("slide_id","block","slide_type","working_title","learning_purpose",
              "key_message","visible_content_summary","visual_or_media","visual_class",
              "suggested_layout","speaker_note_goal","source","prerequisites",
              "transition","status")
        rows.append(dict(zip(keys,cells)))
    return rows


def clean_md(value:str)->str:
    return value.replace("<br>"," ").replace("`","").strip()


def sentence(value:str)->str:
    value=clean_md(value)
    return value if not value or value.endswith((".","?","!",":")) else value+"."


def asset_ids(row:dict[str,str])->list[str]:
    ids=re.findall(r"U10-(?:CH|DG)-\d{3}",row["visual_or_media"])
    if row["slide_id"]=="U10-011" and "U10-CH-015" not in ids:
        ids.append("U10-CH-015")
    return list(dict.fromkeys(ids))


def asset_exists(asset_id:str)->bool:
    group="charts" if "-CH-" in asset_id else "diagrams"
    folder=UNIT/"assets"/"generated"/group/asset_id
    return folder.exists() and any(folder.glob("*.svg")) and any(folder.glob("*.png"))


def asset_text(asset_id:str,filename:str)->str:
    group="charts" if "-CH-" in asset_id else "diagrams"
    path=UNIT/"assets"/"generated"/group/asset_id/filename
    return path.read_text(encoding="utf-8").strip() if path.exists() else ""


def duration(row:dict[str,str])->str:
    if row["slide_id"] in BLOCKED:
        return "0 min mientras permanezca bloqueada"
    kind=row["slide_type"].lower()
    if "actividad" in kind or "ejercicio" in kind:
        return "4–6 min"
    if "portada" in kind or "divisor" in kind:
        return "0,5–1 min"
    if "recap" in kind or "cierre" in kind:
        return "2–3 min"
    if "ecuaci" in kind or row["slide_id"] in EQUATIONS:
        return "3–4 min"
    return "2–3 min"


def visual_caption_alt(row:dict[str,str])->tuple[str,str,str]:
    ids=asset_ids(row)
    captions=[asset_text(i,"caption.txt") for i in ids]
    alts=[asset_text(i,"alt_text.txt") for i in ids]
    captions=[c for c in captions if c]
    alts=[a for a in alts if a]
    caption=CAPTION_OVERRIDES.get(row["slide_id"]," ".join(captions) or clean_md(row["key_message"]))
    alt=ALT_OVERRIDES.get(row["slide_id"]," ".join(alts) or f"Recurso visual previsto: {clean_md(row['visual_or_media'])}")
    available=[i for i in ids if asset_exists(i)]
    planned=[i for i in ids if not asset_exists(i)]
    parts=[]
    if available:
        parts.append("disponible: "+", ".join(available))
    if planned:
        parts.append("planificado/no generado: "+", ".join(planned))
    asset_line="; ".join(parts) if parts else "Sin asset propio asignado; seguir la instrucción del storyboard."
    return caption,alt,asset_line


def layout_text(row:dict[str,str])->str:
    base=clean_md(row["suggested_layout"])
    if "diagrama" in row["visual_class"].lower() or "esquema" in row["visual_class"].lower():
        return (f"{base}. Reservar el área principal al esquema; texto de apoyo fuera de las cajas. "
                "Mantener nodos breves, fuente ≥22 pt y corredores limpios para conectores.")
    return base


def note_visual_guide(row:dict[str,str],alt:str)->str:
    cls=row["visual_class"].lower()
    ids=asset_ids(row)
    if "diagrama" in cls or "esquema" in cls or "flujo" in cls or any("-DG-" in i for i in ids):
        return ("1. Enunciar la idea central antes de recorrer el esquema. 2. Leer los nodos en el orden marcado. "
                "3. Explicar las relaciones sin repetir literalmente cada caja. 4. Cerrar volviendo a la pregunta de la slide. "
                f"Referencia descriptiva: {alt}")
    if "gráfico" in cls or any("-CH-" in i for i in ids):
        return ("Identificar primero ejes, unidades y escala; luego señalar el patrón relevante y, por último, "
                f"vincularlo con la pregunta física. Referencia descriptiva: {alt}")
    return f"Usar el recurso como apoyo y no como decoración. Referencia descriptiva: {alt}"


def speaker_notes(row:dict[str,str],alt:str)->str:
    sid=row["slide_id"]
    q,a=QA.get(sid,("—","—"))
    equation_note=("Definir cada símbolo y su unidad antes de operar; leer la igualdad como una relación física, no como una receta."
                   if sid in EQUATIONS else "")
    blocked_note=("No presentar esta slide en clase ni completar sus campos hasta resolver la fuente indicada."
                  if sid in BLOCKED else "")
    activity_note=("Dar primero un tiempo breve de respuesta individual; pedir luego una justificación con magnitud, condición y evidencia antes de la puesta en común."
                   if "actividad" in row["slide_type"].lower() or "ejercicio" in row["slide_type"].lower() else "")
    explanation=" ".join(filter(None,[sentence(row["learning_purpose"]),
                                        "Partir de esta idea: "+sentence(row["key_message"]),
                                        sentence(row["speaker_note_goal"]),
                                        equation_note,activity_note,blocked_note]))
    demo=("No mostrar ni reproducir este recurso mientras continúe bloqueado por fuente."
          if sid in BLOCKED else DEMO.get(sid,"Recorrer el visual en el orden indicado; no requiere reproducción multimedia."))
    error=ERRORS.get(sid,"No convertir la clasificación o el descriptor presentado en una conclusión más amplia que la evidencia.")
    return t(f"""
**Duración aproximada:** {duration(row)}

**Explicación extendida:** {explanation}

**Guía del visual:** {note_visual_guide(row,alt)}

**Pregunta a los alumnos:** {q}

**Respuesta esperada:** {a}

**Demostración o multimedia:** {demo}

**Error frecuente:** {error}

**Transición oral:** {clean_md(row['transition'])}
""")


def source_details(row:dict[str,str])->str:
    source=clean_md(row["source"]).rstrip(".")
    if row["slide_id"] in BLOCKED:
        return f"{source}. Estado: bloqueada; no completar sin la referencia requerida."
    return source+"."


def slide_entry(row:dict[str,str])->str:
    sid=row["slide_id"]
    caption,alt,assets=visual_caption_alt(row)
    eq=EQUATIONS.get(sid,"—")
    definition=DEFINITIONS.get(sid,"—")
    example=EXAMPLES.get(sid,"—")
    subtitle=SUBTITLES.get(sid,"—")
    notes=speaker_notes(row,alt)
    return t(f"""
## {sid}

**Estado del storyboard:** {row['status']}  
**Tipo:** {row['slide_type']}  
**Bloque:** {row['block']}

### Título

{row['working_title']}

### Subtítulo

{subtitle}

### Contenido visible

{VISIBLE[sid]}

### Ecuaciones

{eq}

### Definiciones

{definition}

### Ejemplo

{example}

### Caption sugerido

{caption}

### Visual

- **Idea central:** {row['key_message']}
- **Recurso previsto:** {row['visual_or_media']}
- **Asset propio:** {assets}
- **Clase visual:** {row['visual_class']}

### Layout

{layout_text(row)}

### Fuente

{source_details(row)}

### Notas del orador

Ver desarrollo completo en `speaker_notes.md`, sección **{sid}**.

### Transición

{row['transition']}

### Texto alternativo

{alt}
""")


def note_entry(row:dict[str,str])->str:
    _,alt,_=visual_caption_alt(row)
    return f"## {row['slide_id']} · {row['working_title']}\n\n{speaker_notes(row,alt)}"


def source_map_entry(row:dict[str,str])->str:
    ids=asset_ids(row)
    assets=", ".join(ids) if ids else "—"
    limitation=("BLOQUEADA: requiere verificación de fuente antes de redactar o presentar."
                if row["slide_id"] in BLOCKED else "Uso según el alcance y la advertencia del storyboard.")
    return t(f"""
## {row['slide_id']} · {row['working_title']}

- **Fuente indicada por el storyboard:** {source_details(row)}
- **Ubicación primaria local:** `context/libro_latex/chapters/10-ruido-caracterizacion.tex`, `context/libro_pdf/Física Acústica para Fonoaudiología.pdf` o `context/programa/Programa de Física Acústica.pdf`, según corresponda.
- **Assets propios vinculados:** {assets}
- **Trazabilidad:** `storyboard.md` → {row['slide_id']}; captions y textos alternativos se leen de la carpeta del asset cuando existe.
- **Limitación:** {limitation}
""")


def visible_word_count(text:str)->int:
    return len(re.findall(r"\b[\wÀ-ÿσΔ]+\b",text))


def review_document(rows:list[dict[str,str]])->str:
    states=Counter(r["status"] for r in rows)
    dense=[(r["slide_id"],visible_word_count(VISIBLE[r["slide_id"]])) for r in rows
           if visible_word_count(VISIBLE[r["slide_id"]])>90]
    dense_text="\n".join(f"- {sid}: {count} palabras; revisar mediante revelado o división al producir el deck." for sid,count in dense) or "- Ninguna slide supera 90 palabras visibles."
    return t(f"""
# Revisión de redacción · Unidad 10

## Resultado

Se redactaron {len(rows)} slides, una por cada fila del storyboard aprobado, sin modificar su secuencia ni producir un PowerPoint. Cada entrada contiene título, subtítulo, contenido visible, ecuaciones, definiciones, ejemplo, caption, visual, layout, fuente, referencia a notas, transición y texto alternativo.

## Control de alcance

- Fuente arquitectónica exclusiva: `storyboard.md` aprobado.
- Estados conservados: {dict(states)}.
- Slides con bloqueo explícito: U10-088, U10-091 y U10-092.
- U10-088 no incorpora datos ni fórmulas del ejemplo pendiente.
- U10-091 no prescribe un protocolo clínico de enmascaramiento.
- U10-092 no muestra valores ni curvas normativas sin jurisdicción y versión verificadas.

## Criterios de escritura comprobados

- Intuición antes del formalismo y definición de símbolos/unidades en las slides cuantitativas.
- Ejemplos resueltos o guiados solo cuando el storyboard los autoriza.
- Aplicaciones a consulta, audiometría, logoaudiometría, acufenometría, voz y ambientes de evaluación sin convertir ejemplos en prescripciones.
- Preguntas con respuesta esperada en actividades, recapitulaciones y puntos de comprobación.
- Notas diferenciadas del texto visible, con duración, error frecuente, demostración y transición.
- Diagramas con idea central explícita y explicación fuera de las cajas; no se agregó prosa extensa a nodos o conectores.
- Tono académico, sin lenguaje publicitario ni conclusiones diagnósticas no sustentadas.

## Densidad visible

{dense_text}

## Problemas y decisiones

| Problema | Severidad | Decisión/corrección | Estado |
|---|---:|---|---|
| Clips comparativos de U10-035 pendientes de selección y documentación | Mayor | Mantener instrucción condicional y usar U10-CH-010 como alternativa estática | Abierto para curación |
| Ejemplo externo de U10-088 sin fuente aprobada | Mayor | Redacción bloqueada; no inventar valores | Bloqueado |
| Protocolo clínico de U10-091 no verificado | Crítico si se publicara | No redactar reglas; conservar marcador de fuente | Bloqueado |
| Límites normativos de U10-092 sin jurisdicción/versión | Crítico si se publicara | No incluir cifras ni curvas | Bloqueado |
| Solucionario U10-089 denso para una sola vista | Mayor | Dividir en dos vistas o usar revelado progresivo sin bajar de 22 pt | Pendiente de maquetación |
| Metadata original de U10-DG-031 dice “tres intervalos” aunque el esquema muestra cuatro | Menor | Caption y texto alternativo corregidos en esta fase; actualizar metadata del asset en la fase visual | Abierto fuera de alcance |

## Aprobación de esta fase

La redacción queda **aprobada con bloqueos documentados** para pasar a revisión editorial y futura maquetación. Las tres slides bloqueadas no están aprobadas para exposición hasta resolver sus fuentes. No se evaluó aún la legibilidad dentro de una presentación renderizada porque esa fase no fue solicitada.
""")


def main()->None:
    rows=parse_storyboard()
    ids=[r["slide_id"] for r in rows]
    expected=[f"U10-{i:03d}" for i in range(1,94)]
    if ids!=expected:
        raise ValueError("La secuencia del storyboard no coincide con U10-001…U10-093")
    missing=set(ids)-set(VISIBLE)
    extra=set(VISIBLE)-set(ids)
    if missing or extra:
        raise ValueError(f"Desajuste de redacción. Faltan={sorted(missing)}; sobran={sorted(extra)}")

    slide_header=t("""
# Texto de slides · Unidad 10 · Ruidos

Documento de redacción derivado exclusivamente del storyboard aprobado. No es una presentación ni autoriza a publicar las slides marcadas como bloqueadas. Los guiones largos indican que el campo no corresponde o no debe mostrarse en esa slide.
""")
    notes_header=t("""
# Notas del orador · Unidad 10 · Ruidos

Notas ampliadas coordinadas con `slide_text.md`. Las duraciones son orientativas. Las preguntas y demostraciones se incluyen cuando aportan a la progresión; no deben forzarse en cada slide.
""")
    sources_header=t("""
# Mapa de fuentes · Unidad 10 · Ruidos

Este mapa conserva la fuente declarada por cada fila del storyboard. No reemplaza la comprobación bibliográfica, clínica o normativa previa a la publicación.
""")

    (UNIT/"slide_text.md").write_text(slide_header+"\n\n"+"\n\n---\n\n".join(slide_entry(r) for r in rows)+"\n",encoding="utf-8")
    (UNIT/"speaker_notes.md").write_text(notes_header+"\n\n"+"\n\n---\n\n".join(note_entry(r) for r in rows)+"\n",encoding="utf-8")
    (UNIT/"source_map.md").write_text(sources_header+"\n\n"+"\n\n---\n\n".join(source_map_entry(r) for r in rows)+"\n",encoding="utf-8")
    (UNIT/"writing_review.md").write_text(review_document(rows)+"\n",encoding="utf-8")

    print(f"OK: {len(rows)} slides redactadas")
    print(f"Bloqueadas: {', '.join(sorted(BLOCKED))}")
    print(f"Estados: {dict(Counter(r['status'] for r in rows))}")


if __name__=="__main__":
    main()
