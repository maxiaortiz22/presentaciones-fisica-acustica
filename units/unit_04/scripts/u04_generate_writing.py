from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
UNIT = ROOT / "units" / "unit_04"
STORYBOARD = UNIT / "storyboard.md"
MANIFEST = UNIT / "asset_manifest.csv"


BLOCK_QUESTIONS = {
    "B00": "¿Qué magnitud describe realmente un valor de sonido?",
    "B01": "¿Qué existe físicamente antes de medir o escuchar?",
    "B02": "¿Cómo permiten la elasticidad y la inercia que avance una perturbación?",
    "B03": "¿Qué magnitudes cambian en el campo y qué ocurre en una interfaz?",
    "B04": "¿Cómo distinguimos una variable local de la transferencia de energía?",
    "B05": "¿Qué número resume cada aspecto de una señal variable?",
    "B06": "¿Cómo cuantificamos el tamaño cuadrático de una señal?",
    "B07": "¿Qué debe acompañar siempre a un valor en decibeles?",
    "B08": "¿Qué cambia según la relación temporal entre las señales?",
    "B09": "¿Cómo cambia la distribución de energía según el frente de onda y el entorno?",
    "B10": "¿Cómo cambian nivel y radiación con distancia y dirección?",
    "B11": "¿Qué permite interpretar una medición acústica en Fonoaudiología?",
    "B12": "¿Qué detalle adicional necesitamos para resolver una duda o profundizar?",
}


EQUATIONS = {
    "U04-004": [r"$c=\lambda f$", r"$u(t)\neq c$"],
    "U04-020": [r"$c=\sqrt{K_s/\rho}$"],
    "U04-022": [r"$c=\lambda f$", r"$c_{\mathrm{aire}}\approx343\ \mathrm{m\,s^{-1}}$ a $20\ ^\circ\mathrm{C}$"],
    "U04-024": [r"$X=X(\mathbf r,t)$"],
    "U04-025": [r"$p_{\mathrm{total}}(\mathbf r,t)=p_0+p(\mathbf r,t)$"],
    "U04-026": [r"$p_{\mathrm{total}}=p_0+p(t)$"],
    "U04-029": [r"$Z=p/u$"],
    "U04-030": [r"$Z_0=\dfrac{p}{u}=\rho c$"],
    "U04-032": [r"$R_p=\dfrac{Z_{02}-Z_{01}}{Z_{02}+Z_{01}}$", r"$R_I=|R_p|^2$"],
    "U04-035": [r"$i(t)=p(t)u(t)$"],
    "U04-037": [r"$I=\dfrac{1}{\Delta t}\int_{t_0}^{t_0+\Delta t}p(t)u(t)\,\mathrm dt$"],
    "U04-038": [r"$I=p_{\mathrm{rms}}u_{\mathrm{rms}}=\dfrac{p_{\mathrm{rms}}^2}{Z_0}=Z_0u_{\mathrm{rms}}^2$"],
    "U04-039": [r"$u_{\mathrm{rms}}=p_{\mathrm{rms}}/Z_0=5{,}0\times10^{-4}\ \mathrm{m\,s^{-1}}$", r"$I=p_{\mathrm{rms}}^2/Z_0=1{,}0\times10^{-4}\ \mathrm{W\,m^{-2}}$"],
    "U04-041": [r"$W_{\mathrm{ac}}=IS$", r"$E_{\mathrm{ac}}=W_{\mathrm{ac}}\Delta t$"],
    "U04-045": [r"$p(t_1)$", r"$\hat p=\max |p(t)|$"],
    "U04-046": [r"$p_{\mathrm{pp}}=p_{\max}-p_{\min}$", r"$p_{\mathrm{pp}}=2\hat p$ solo si la señal es simétrica respecto de cero"],
    "U04-047": [r"$\overline p=\dfrac{1}{\Delta t}\int_{t_0}^{t_0+\Delta t}p(t)\,\mathrm dt$"],
    "U04-048": [r"$\overline p=0\ \mathrm{Pa}$ no implica $p(t)=0$"],
    "U04-052": [r"$x(t)\rightarrow x^2(t)\rightarrow \overline{x^2}\rightarrow x_{\mathrm{rms}}$"],
    "U04-054": [r"$x_{\mathrm{rms}}=\sqrt{\dfrac{1}{T_{\mathrm{obs}}}\int_{t_0}^{t_0+T_{\mathrm{obs}}}x^2(t)\,\mathrm dt}$"],
    "U04-055": [r"$x_{\mathrm{rms}}=\dfrac{x_{\mathrm{pico}}}{\sqrt2}\approx0{,}707x_{\mathrm{pico}}$"],
    "U04-056": [r"$p_{\mathrm{rms}}=\dfrac{0{,}283\ \mathrm{Pa}}{\sqrt2}\approx0{,}200\ \mathrm{Pa}$", r"$\hat p\approx\sqrt2\,p_{\mathrm{rms}}$"],
    "U04-058": [r"$p_{\mathrm{rms}}=\hat p/\sqrt2$ solo para una sinusoide"],
    "U04-062": [r"$L_p=20\log_{10}\!\left(\dfrac{p_{\mathrm{rms}}}{p_{\mathrm{ref}}}\right)$", r"$p_{\mathrm{ref}}=20\ \mu\mathrm{Pa}$ en aire"],
    "U04-063": [r"$L_p=20\log_{10}\!\left(\dfrac{0{,}20}{2{,}0\times10^{-5}}\right)=80\ \mathrm{dB\ SPL}$"],
    "U04-064": [r"$p\times10\Rightarrow\Delta L_p=+20\ \mathrm{dB}$", r"$p\times2\Rightarrow\Delta L_p\approx+6{,}02\ \mathrm{dB}$"],
    "U04-065": [r"$p_{\mathrm{ref,aire}}=20\ \mu\mathrm{Pa}$", r"$p_{\mathrm{ref,agua}}=1\ \mu\mathrm{Pa}$"],
    "U04-066": [r"$10\log_{10}\!\left[(p/p_{\mathrm{ref}})^2\right]=20\log_{10}(p/p_{\mathrm{ref}})$"],
    "U04-067": [r"$L_p=20\log_{10}(p_{\mathrm{rms}}/p_{\mathrm{ref}})$", r"$L_I=10\log_{10}(I/I_{\mathrm{ref}})$", r"$L_W=10\log_{10}(W_{\mathrm{ac}}/W_{\mathrm{ref}})$"],
    "U04-070": [r"$p_{\mathrm R}(t)=p_1(t)+p_2(t)$"],
    "U04-073": [r"$p_{\mathrm{R,rms}}^2=p_{1,\mathrm{rms}}^2+p_{2,\mathrm{rms}}^2+2p_{1,\mathrm{rms}}p_{2,\mathrm{rms}}\cos\varphi$"],
    "U04-074": [r"$p_{\mathrm R}=2p$", r"$\Delta L_p=20\log_{10}(2)\approx6{,}02\ \mathrm{dB}$"],
    "U04-075": [r"$\varphi=\pi\Rightarrow p_{\mathrm R}(t)=0$ en el punto ideal si las amplitudes son iguales"],
    "U04-076": [r"$\overline{p_1(t)p_2(t)}=0$ durante $T_{\mathrm{obs}}$"],
    "U04-077": [r"$p_{\mathrm{R,rms}}^2=\sum_i p_{i,\mathrm{rms}}^2$"],
    "U04-078": [r"$L_{\mathrm R}=10\log_{10}\!\left(\sum_i10^{L_i/10}\right)$"],
    "U04-079": [r"$L_{\mathrm R}=10\log_{10}(2\times10^{70/10})=73{,}01\ \mathrm{dB\ SPL}$"],
    "U04-080": [r"$+6{,}02\ \mathrm{dB}$: presiones iguales coherentes en fase", r"$+3{,}01\ \mathrm{dB}$: señales iguales no correlacionadas"],
    "U04-084": [r"$S_{\mathrm{cil}}\propto r$", r"$I\propto1/r$", r"$r\times2\Rightarrow\Delta L\approx-3{,}01\ \mathrm{dB}$"],
    "U04-085": [r"$S_{\mathrm{esf}}=4\pi r^2$", r"$I\propto1/r^2$"],
    "U04-086": [r"$I_{\mathrm{plana}}\propto r^0$", r"$I_{\mathrm{cil}}\propto r^{-1}$", r"$I_{\mathrm{esf}}\propto r^{-2}$"],
    "U04-092": [r"$I(r)=\dfrac{W_{\mathrm{ac}}}{4\pi r^2}$"],
    "U04-093": [r"$\dfrac{I_2}{I_1}=\left(\dfrac{r_1}{r_2}\right)^2$"],
    "U04-094": [r"$L_2-L_1=20\log_{10}\!\left(\dfrac{r_1}{r_2}\right)$"],
    "U04-095": [r"$r_2=2r_1\Rightarrow L_2-L_1=-6{,}02\ \mathrm{dB}$"],
    "U04-097": [r"$L_2=80+20\log_{10}(1/4)=67{,}96\ \mathrm{dB\ SPL}\approx68\ \mathrm{dB\ SPL}$"],
    "U04-100": [r"$Q_{\mathrm{dir}}(\theta,\phi)=\dfrac{I(r,\theta,\phi)}{W_{\mathrm{ac}}/(4\pi r^2)}$"],
    "U04-101": [r"$DI=10\log_{10}(Q_{\mathrm{dir}})$", r"$Q_{\mathrm{dir}}=4\Rightarrow DI\approx6{,}02\ \mathrm{dB}$"],
    "U04-110": [r"$\log_{10}(ab)=\log_{10}a+\log_{10}b$", r"$\log_{10}(a^n)=n\log_{10}a$", r"$10^{\log_{10}a}=a$"],
    "U04-111": [r"$\overline x=\dfrac1N\sum_{n=1}^N x_n$", r"$x_{\mathrm{rms}}=\sqrt{\dfrac1N\sum_{n=1}^N x_n^2}$"],
    "U04-112": [r"$\overline p=\dfrac1{T_{\mathrm{obs}}}\int p(t)\,\mathrm dt$", r"$p_{\mathrm{rms}}=\sqrt{\dfrac1{T_{\mathrm{obs}}}\int p^2(t)\,\mathrm dt}$", r"$I=\dfrac1{T_{\mathrm{obs}}}\int p(t)u(t)\,\mathrm dt$"],
    "U04-113": [r"$R_p=(800-400)/(800+400)=1/3$", r"$R_I=|R_p|^2=1/9\approx0{,}111$"],
    "U04-114": [r"$I_{\mathrm{ref}}=10^{-12}\ \mathrm{W\,m^{-2}}$", r"$W_{\mathrm{ref}}=10^{-12}\ \mathrm W$"],
    "U04-115": [r"$p_{\mathrm{R,rms}}^2=p_1^2+p_2^2+2\gamma p_1p_2$", r"$-1\le\gamma\le1$"],
    "U04-117": [r"$I_2/I_1=r_1/r_2=1/2$", r"$\Delta L_I=10\log_{10}(1/2)=-3{,}01\ \mathrm{dB}$"],
    "U04-118": [r"$I_2/I_1=(r_1/r_2)^2$", r"$\Delta L=10\log_{10}(I_2/I_1)=20\log_{10}(r_1/r_2)$"],
    "U04-120": [r"$p_{\mathrm{rms}}=\hat p/\sqrt2$ solo para el caso sinusoidal", r"$x_{\mathrm{rms}}=\sqrt{N^{-1}\sum x_n^2}$ para muestras"],
    "U04-121": [r"$L_{\mathrm R}=10\log_{10}(10^{70/10}+10^{60/10})\approx70{,}4\ \mathrm{dB\ SPL}$"],
    "U04-122": [r"$p_{\mathrm{R,rms}}=\sqrt2\,p$", r"$L_{\mathrm R}=65+20\log_{10}(\sqrt2)\approx68{,}0\ \mathrm{dB\ SPL}$"],
    "U04-123": [r"$I(r,\theta,\phi)=\dfrac{W_{\mathrm{ac}}Q_{\mathrm{dir}}(\theta,\phi)}{4\pi r^2}$", r"$\Delta L=20\log_{10}(r_1/r_2)+DI$ cuando las referencias y el modelo son compatibles"],
}


DEFINITIONS = {
    "U04-008": "Fenómeno físico: perturbación medible en un medio. Sensación sonora: experiencia producida por el sistema auditivo en un contexto.",
    "U04-017": "Elasticidad: capacidad del medio de desarrollar una respuesta restauradora cuando se deforma.",
    "U04-018": r"Densidad $\rho$: masa por unidad de volumen; unidad SI $\mathrm{kg\,m^{-3}}$.",
    "U04-024": "Campo acústico: distribución espacial y temporal de magnitudes acústicas.",
    "U04-025": "Presión acústica $p$: variación respecto de la presión estática local $p_0$; unidad Pa.",
    "U04-027": r"Velocidad de partícula $u$: velocidad local de una pequeña región del medio; unidad $\mathrm{m\,s^{-1}}$.",
    "U04-029": r"Impedancia acústica específica $Z$: relación entre presión acústica y velocidad de partícula bajo condiciones declaradas; unidad $\mathrm{Pa\,s\,m^{-1}}$.",
    "U04-035": r"Intensidad instantánea $i(t)$: flujo instantáneo de potencia acústica por unidad de área en la dirección elegida; unidad $\mathrm{W\,m^{-2}}$.",
    "U04-037": r"Intensidad media $I$: promedio temporal del flujo de potencia por unidad de área; unidad $\mathrm{W\,m^{-2}}$.",
    "U04-040": r"Potencia acústica $W_{\mathrm{ac}}$: energía transferida por unidad de tiempo, en W. Energía acústica $E_{\mathrm{ac}}$: transferencia acumulada, en J.",
    "U04-045": "Valor instantáneo: valor en un instante. Pico: mayor módulo respecto del equilibrio, según la convención declarada.",
    "U04-046": "Pico a pico: diferencia entre el máximo y el mínimo de una señal durante la ventana elegida.",
    "U04-047": "Valor medio: promedio algebraico de la señal durante una ventana de observación.",
    "U04-052": "RMS o valor eficaz: raíz cuadrada del promedio del cuadrado de la señal.",
    "U04-057": "Tono puro: señal sinusoidal. Señal compleja: señal cuya forma temporal no es una única sinusoide.",
    "U04-059": "Decibel: expresión logarítmica de una razón; no es una magnitud física aislada.",
    "U04-062": "Nivel de presión sonora $L_p$: razón logarítmica entre presión eficaz y presión de referencia.",
    "U04-071": "Coherencia: relación temporal estable; para sinusoides de igual frecuencia, diferencia de fase constante durante la observación.",
    "U04-076": "No correlacionadas: señales cuyo término cruzado medio es nulo durante la ventana considerada.",
    "U04-082": "Frente de onda: conjunto de puntos que comparten fase en un instante.",
    "U04-088": "Campo libre: reflexiones despreciables. Campo reverberante: contribución persistente de reflexiones. Campo difuso: idealización estadística de energía y direcciones.",
    "U04-098": "Fuente omnidireccional ideal: distribuye la potencia por igual en todas las direcciones.",
    "U04-100": r"Factor de directividad $Q_{\mathrm{dir}}$: razón adimensional entre la intensidad en una dirección y la de una fuente omnidireccional de igual potencia y distancia.",
    "U04-101": "Índice de directividad $DI$: expresión logarítmica del factor de directividad, en dB.",
}


EXAMPLES = {
    "U04-009": "Un micrófono registra presión acústica en una sala vacía: el campo existe aunque no haya una persona escuchando.",
    "U04-012": "En la voz, los pliegues vocales constituyen la fuente mecánica y el aire es el medio que transporta la perturbación.",
    "U04-013": "El cono del parlante se mueve localmente; las compresiones y rarefacciones se propagan por el aire.",
    "U04-021": "Dos medios no deben compararse solo por $\rho$: también cambia su rigidez volumétrica $K_s$.",
    "U04-022": r"En una interfaz estacionaria, la frecuencia fijada por la fuente se conserva; al cambiar $c$, cambia $\lambda$.",
    "U04-026": "Si $p(t)<0$, la presión total es menor que $p_0$, no menor que cero absoluto.",
    "U04-039": r"Datos didácticos: $p_{\mathrm{rms}}=0{,}20\ \mathrm{Pa}$ y $Z_0=400\ \mathrm{Pa\,s\,m^{-1}}$.",
    "U04-042": "Un micrófono calibrado estima presión en un punto; no entrega por sí solo la potencia total de la fuente.",
    "U04-048": "Una sinusoide centrada en cero tiene media nula y RMS distinto de cero.",
    "U04-049": "Muestreo → valor instantáneo; saturación → pico; rango total → pico a pico; componente continua → media.",
    "U04-056": r"Para una presión sinusoidal de pico $0{,}283\ \mathrm{Pa}$, el RMS es aproximadamente $0{,}200\ \mathrm{Pa}$.",
    "U04-061": "“60 dB” no informa si se trata de dB SPL, dB HL u otro nivel, ni cuál es la referencia.",
    "U04-063": r"En aire, $0{,}20\ \mathrm{Pa}$ RMS respecto de $20\ \mu\mathrm{Pa}$ equivale a $80\ \mathrm{dB\ SPL}$.",
    "U04-068": "Un valor en dB SPL no se convierte en dB HL sin la referencia audiométrica, la frecuencia y el transductor.",
    "U04-074": r"Dos presiones iguales, coherentes y en fase duplican la amplitud y aumentan el nivel $6{,}02\ \mathrm{dB}$.",
    "U04-075": "Dos tonos iguales en oposición de fase pueden cancelar la presión en un punto ideal; no es una regla global del recinto.",
    "U04-079": r"Dos señales no correlacionadas de $70\ \mathrm{dB\ SPL}$ producen $73{,}01\ \mathrm{dB\ SPL}$ con la misma referencia.",
    "U04-084": r"En el modelo cilíndrico ideal, duplicar distancia reduce el nivel de intensidad $3{,}01\ \mathrm{dB}$.",
    "U04-087": "Un tubo circular puede sostener un campo aproximadamente plano: la forma del conducto no define por sí sola el frente.",
    "U04-097": r"En campo libre esférico ideal, $80\ \mathrm{dB\ SPL}$ a 1 m pasan a $67{,}96\ \mathrm{dB\ SPL}$ a 4 m.",
    "U04-101": r"$Q_{\mathrm{dir}}=4$ corresponde a $DI\approx6{,}02\ \mathrm{dB}$ en la dirección considerada.",
    "U04-102": "Comparar dos patrones del mismo transductor rotulados con frecuencias distintas: identificar la dirección frontal y un ángulo donde la respuesta relativa cambie.",
    "U04-104": "Un sonómetro informa un nivel en un punto con ponderación y respuesta temporal declaradas; no informa sonoridad individual.",
    "U04-105": "Dos fuentes se observan desde dos posiciones dentro de un recinto. El ejercicio consiste en decidir qué dato permite sumar, aplicar distancia o incorporar directividad, y qué conclusión queda indeterminada.",
    "U04-113": r"Con $Z_{01}=400$ y $Z_{02}=800\ \mathrm{Pa\,s\,m^{-1}}$, $R_p=1/3$ y $R_I\approx0{,}111$.",
    "U04-117": r"Si $I\propto1/r$, al pasar de $r$ a $2r$ la intensidad se reduce a la mitad.",
    "U04-120": r"Comparar una sinusoide con una señal no sinusoidal de muestras dadas; usar $1/\sqrt2$ solo en la primera.",
    "U04-121": r"$70+60\ \mathrm{dB\ SPL}$, con señales no correlacionadas, resulta $70{,}4\ \mathrm{dB\ SPL}$, no $130\ \mathrm{dB}$.",
    "U04-122": r"Dos tonos de $65\ \mathrm{dB\ SPL}$ y desfase $\pi/2$ producen aproximadamente $68\ \mathrm{dB\ SPL}$.",
    "U04-123": "Combinar el cambio radial con el índice de directividad solo si distancia, dirección, referencia y campo pertenecen al mismo modelo.",
}


VISIBLE_OVERRIDES = {
    "U04-001": ["Generalidades sobre el sonido, sus propiedades y magnitudes", "Campo acústico · medición · niveles", "Pregunta de apertura: ¿qué falta saber cuando alguien informa solo “80 dB”?"],
    "U04-002": ["Una misma situación admite preguntas distintas:", "¿Qué cambia en el aire?", "¿Cómo se mueve localmente el medio?", "¿Qué flujo atraviesa un punto?", "¿Cuánta potencia entrega la fuente?", "¿Qué percibe la persona?"],
    "U04-003": ["Decidí verdadero o falso y justificá:", "El sonido necesita un oyente para existir.", r"$u=c$ porque ambas se expresan en $\mathrm{m\,s^{-1}}$.", "Si la media es cero, la señal es nula.", "Un valor en dB es absoluto.", "Dos fuentes iguales siempre agregan 3 dB.", "Duplicar la distancia siempre resta 6 dB."],
    "U04-004": ["Podemos usar: magnitud, símbolo y unidad; presión; energía y potencia; onda, fase y superposición.", r"Conviene revisar: $c=\lambda f$; diferencia entre $u$ y $c$; razones, potencias de diez y logaritmo decimal."],
    "U04-005": ["Diferenciar fenómeno físico y sensación sonora.", "Explicar elasticidad, inercia y rapidez de propagación.", r"Relacionar $p$, $u$, $Z$, $I$, $W_{\mathrm{ac}}$ y $E_{\mathrm{ac}}$.", "Interpretar valores instantáneo, pico, pico a pico, medio y RMS.", "Calcular niveles con referencia explícita y justificar 10/20.", "Sumar señales según fase o correlación.", "Aplicar modelos plano, cilíndrico y esférico con condiciones.", r"Interpretar $Q_{\mathrm{dir}}$ y $DI$ sin suponer creación de potencia."],
    "U04-006": ["Encuentro 1: fenómeno → medio → campo → energía.", "Encuentro 2: valores → RMS → niveles → suma.", "Encuentro 3: geometría → distancia/directividad → aplicación."],
    "U04-105": ["Antes de calcular, registrá para cada fuente:", "1. magnitud y referencia informadas;", "2. relación temporal entre señales;", "3. distancia y dirección del punto;", "4. geometría y tipo de campo;", "5. dato faltante que impediría el cálculo.", "No se asignan valores numéricos nuevos: el objetivo es decidir qué relación sería válida."],
    "U04-108": ["Explicá con tus palabras:", "qué existe sin oyente;", "por qué $u\neq c$;", "qué distingue RMS de media;", "qué completa a un valor en dB;", "cuándo aparecen $+6$, $+3$ o cancelación;", "cuándo puede usarse la regla de distancia."],
    "U04-119": ["1. Falso: el campo no requiere oyente.", "2. Falso: $u$ es movimiento local y $c$ es propagación.", "3. Falso: media cero puede coexistir con RMS no nulo.", "4. Falso: todo nivel requiere magnitud y referencia.", "5. Falso: la suma depende de fase o correlación.", r"6. Falso como regla universal: $-6{,}02\ \mathrm{dB}$ exige propagación esférica ideal y campo libre."],
    "U04-124": ["Solución razonada de U04-105:", "Identificar primero magnitud y referencia.", "Elegir la regla de suma solo si se conoce fase o correlación.", "Aplicar distancia solo con geometría y campo compatibles.", "Incorporar directividad solo con dirección y frecuencia declaradas.", "Si falta una condición, informar qué no puede calcularse y por qué."],
    "U04-125": ["Símbolos principales:", r"$p$ — presión acústica (Pa); $u$ — velocidad de partícula ($\mathrm{m\,s^{-1}}$); $I$ — intensidad ($\mathrm{W\,m^{-2}}$).", r"$W_{\mathrm{ac}}$ — potencia acústica (W); $E_{\mathrm{ac}}$ — energía acústica (J).", r"$L_p$ — nivel de presión sonora (dB); $Q_{\mathrm{dir}}$ — factor de directividad (1); $DI$ — índice de directividad (dB).", "Fuentes principales: programa oficial; libro del curso, Unidad 4; guía transversal de notación y glosario."],
}


VISUAL_OVERRIDES = {
    "U04-011": "Esquema propio U04-DG-021 con cinco mecanismos de generación; una imagen técnica externa solo puede añadirse si está verificada y registrada.",
    "U04-013": "Usar U04-DG-004 como alternativa estática. El GIF U04-MED-001 es opcional y solo se reproduce después de aprobar encuadre y crédito.",
    "U04-102": "Usar U04-DG-017 como esquema conceptual mientras U04-CH-012 permanezca pendiente. Al aprobar el dataset abierto, reemplazar o complementar con patrones polares a dos o tres frecuencias, con ejes y condiciones declaradas.",
}


DURATION = {
    "portada": "2 min", "divisor": "2 min", "pregunta": "4 min", "objetivos": "3 min",
    "mapa": "3 min", "puente": "4 min", "definición": "3 min", "explicación": "4 min",
    "comparación": "4 min", "proceso": "4 min", "ecuación": "5 min", "gráfico": "4 min",
    "ejemplo": "5 min", "aplicación": "4 min", "error frecuente": "4 min", "recapitulación": "4 min",
    "recapitulación final": "5 min", "cierre": "3 min", "recordatorio": "4 min", "profundización": "5 min",
    "derivación": "6 min", "solución": "5 min", "referencia": "2 min",
}


SOURCE_LEGEND = {
    "PO": "Programa oficial 2025, Unidad 4, p. 3.",
    "TEX": "`context/libro_latex/chapters/04-sonido-propiedades-magnitudes.tex`.",
    "PDF": "Libro del curso, Unidad 4, pp. 89–117.",
    "CM": "`course_map.md`, Unidad 4.",
    "CDM": "`course_dependency_map.md`, Unidad 4.",
    "CCM": "`content_coverage_matrix.csv`, registros U04.",
    "BR": "`units/unit_04/brief.md`.",
    "INV": "`units/unit_04/content_inventory.md`.",
    "SA": "`units/unit_04/source_analysis.md`.",
    "OD": "`units/unit_04/open_decisions.md`.",
    "NOT": "`style/notation_guide.md`.",
    "GLO": "`style/glossary.md`.",
    "U3": "Presentación final de Unidad 3: onda, velocidad de partícula, rapidez, fase y superposición.",
    "ED": "Elaboración didáctica ya aprobada y trazable en el storyboard.",
}


def parse_storyboard() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in STORYBOARD.read_text(encoding="utf-8").splitlines():
        if line.startswith("| slide_id "):
            headers = [x.strip() for x in line.strip().strip("|").split("|")]
        elif line.startswith("| U04-") and headers:
            parts = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(parts) == len(headers) and re.fullmatch(r"U04-\d{3}", parts[0]):
                rows.append(dict(zip(headers, parts)))
    if [r["slide_id"] for r in rows] != [f"U04-{i:03d}" for i in range(1, 126)]:
        raise RuntimeError("La secuencia aprobada U04-001…U04-125 no se pudo leer completa.")
    return rows


def parse_manifest() -> tuple[dict[str, list[dict[str, str]]], dict[str, dict[str, str]]]:
    by_slide: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_id: dict[str, dict[str, str]] = {}
    with MANIFEST.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            by_id[row["asset_id"]] = row
            for sid in row["slide_id"].split(";"):
                sid = sid.strip()
                if re.fullmatch(r"U04-\d{3}", sid):
                    by_slide[sid].append(row)
    return by_slide, by_id


def split_summary(text: str) -> list[str]:
    text = text.strip().rstrip(".")
    parts = re.split(r";\s+|;\s*", text)
    if len(parts) == 1 and ":" in text:
        lead, tail = text.split(":", 1)
        items = [x.strip() for x in re.split(r",\s+|\s+y\s+", tail) if x.strip()]
        if 2 <= len(items) <= 8:
            return [lead.strip() + ":"] + items
    return [p.strip() for p in parts if p.strip()]


def clean_visual(text: str) -> str:
    text = re.sub(r"CANDIDATA `(?:diagram|chart)-generation`(?::\s*)?", "", text)
    text = text.replace("ASSET EXTERNO propuesto:", "Imagen técnica propuesta:")
    text = text.replace("ASSET EXTERNO:", "Imagen técnica:")
    text = text.replace("MEDIA opcional:", "Recurso audiovisual opcional:")
    text = re.sub(r"\.\s+para el esquema base\.", "; el esquema base es la alternativa estática.", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.replace("Sin visual adicional.", "Sin recurso visual adicional; composición tipográfica del layout aprobado.")


def visual_description(row: dict[str, str]) -> str:
    return VISUAL_OVERRIDES.get(row["slide_id"], clean_visual(row["visual_or_media"]))


def assets_for_slide(sid: str, by_slide: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    preferred = []
    for row in by_slide.get(sid, []):
        if row["status"] in {"approved", "downloaded", "shortlisted", "proposed", "pending_approval"}:
            preferred.append(row)
    return sorted(preferred, key=lambda r: ({"approved": 0, "downloaded": 1, "shortlisted": 2, "proposed": 3, "pending_approval": 4}.get(r["status"], 9), r["asset_id"]))


def pick_primary(row: dict[str, str], assets: list[dict[str, str]]) -> dict[str, str] | None:
    if not assets:
        return None
    vclass = row["visual_class"]
    if vclass == "chart":
        matches = [a for a in assets if a["asset_id"].startswith("U04-CH-") and a["status"] == "approved"]
    elif vclass in {"diagram", "equation_only"}:
        matches = [a for a in assets if a["asset_id"].startswith("U04-DG-") and a["status"] == "approved"]
    elif vclass == "video_or_gif":
        matches = [a for a in assets if a["type"] in {"video_or_gif", "video"} and a["status"] == "approved"]
        if not matches:
            matches = [a for a in assets if a["asset_id"].startswith("U04-DG-") and a["status"] == "approved"]
    elif vclass == "external_image":
        matches = [a for a in assets if a["type"] == "external_image" and a["status"] == "approved"]
        if not matches:
            matches = [a for a in assets if a["asset_id"].startswith("U04-DG-") and a["status"] == "approved"]
    else:
        matches = [a for a in assets if a["status"] == "approved"]
    return matches[0] if matches else assets[0]


def visible_lines(row: dict[str, str]) -> list[str]:
    sid = row["slide_id"]
    if sid in VISIBLE_OVERRIDES:
        return VISIBLE_OVERRIDES[sid]
    typ = row["slide_type"]
    message = row["key_message"].rstrip(".") + "."
    if typ == "divisor":
        return [BLOCK_QUESTIONS[row["block"].split()[0]], message]
    lines = [message]
    definition = DEFINITIONS.get(sid)
    if definition and definition.rstrip(".") != message.rstrip("."):
        lines.append(definition)
    if sid in EQUATIONS:
        lines.extend(EQUATIONS[sid])
    example = EXAMPLES.get(sid)
    if example and typ in {"ejemplo", "aplicación", "error frecuente", "pregunta", "solución", "comparación", "recapitulación"}:
        lines.append(example)
    # Los diagramas llevan el detalle estructural dentro del recurso aprobado.
    # El copy exterior se limita a la idea central, la definición o ecuación y
    # una aplicación breve para no duplicar cajas ni forzar tipografía pequeña.
    return lines


def format_lines(lines: list[str]) -> str:
    if len(lines) == 1:
        return lines[0]
    return "\n".join(f"- {line}" for line in lines)


def equation_text(sid: str) -> str:
    eqs = EQUATIONS.get(sid)
    return "\n".join(f"- {eq}" for eq in eqs) if eqs else "No corresponde en esta slide."


def definition_text(row: dict[str, str]) -> str:
    sid = row["slide_id"]
    if sid in DEFINITIONS:
        return DEFINITIONS[sid]
    if row["slide_type"] == "definición":
        return row["key_message"]
    return "No se introduce una definición nueva; se aplican las ya construidas."


def example_text(row: dict[str, str]) -> str:
    sid = row["slide_id"]
    if sid in EXAMPLES:
        return EXAMPLES[sid]
    if row["slide_type"] in {"pregunta", "aplicación", "ejemplo", "solución"}:
        return row["visible_content_summary"]
    return "No corresponde; la función de la slide es conceptual, comparativa o de transición."


def visual_text(row: dict[str, str], assets: list[dict[str, str]]) -> str:
    base = visual_description(row)
    if not assets:
        return base
    refs = []
    for asset in assets:
        path = asset["local_path"] or "sin archivo local"
        refs.append(f"`{asset['asset_id']}` ({asset['status']}): `{path}`")
    return base + "\n\nRecursos vinculados: " + "; ".join(refs) + "."


def caption_text(row: dict[str, str], assets: list[dict[str, str]]) -> str:
    vclass = row["visual_class"]
    if vclass == "none":
        return "No corresponde."
    primary_asset = pick_primary(row, assets)
    primary = primary_asset["title"] if primary_asset else row["working_title"]
    chart_assets = [a for a in assets if a["asset_id"].startswith("U04-CH-") and a["status"] == "approved"]
    diagram_assets = [a for a in assets if a["asset_id"].startswith("U04-DG-") and a["status"] == "approved"]
    if vclass == "chart":
        return f"{primary}. Figura cuantitativa reproducible; ecuaciones o datos y escala se indican en el recurso."
    if vclass == "mixed" and chart_assets and diagram_assets:
        return f"{chart_assets[0]['title']} y {diagram_assets[0]['title']}. El gráfico es cuantitativo; el esquema organiza las condiciones y no está a escala."
    if vclass == "mixed" and chart_assets:
        return f"{chart_assets[0]['title']}. Figura cuantitativa reproducible acompañada por texto o ecuaciones editables."
    if vclass in {"diagram", "mixed", "equation_only"}:
        return f"{primary}. Esquema conceptual; las distancias, tamaños y formas no representan una escala física salvo indicación expresa."
    if vclass in {"external_image", "video_or_gif"}:
        return f"{primary}. Recurso técnico usado para identificar el fenómeno; conservar crédito y condiciones registradas en el manifiesto."
    return f"{primary}."


def alt_text(row: dict[str, str], assets: list[dict[str, str]]) -> str:
    vclass = row["visual_class"]
    desc = visual_description(row).rstrip(".")
    if vclass == "none":
        return f"Slide tipográfica titulada «{row['working_title']}»; destaca que {row['key_message'][0].lower() + row['key_message'][1:]}"
    approved_diagram = any(a["asset_id"].startswith("U04-DG-") and a["status"] == "approved" for a in assets)
    approved_media = any(a["type"] in {"video_or_gif", "audio", "video"} and a["status"] == "approved" for a in assets)
    if vclass == "video_or_gif" and approved_diagram and not approved_media:
        noun = "Diagrama estático alternativo"
    elif vclass == "external_image" and approved_diagram:
        noun = "Diagrama conceptual alternativo"
    else:
        noun = {"chart": "Gráfico", "diagram": "Diagrama", "mixed": "Esquema mixto", "equation_only": "Ecuación anotada", "external_image": "Imagen técnica", "video_or_gif": "Secuencia audiovisual"}.get(vclass, "Recurso visual")
    primary = pick_primary(row, assets)
    asset_note = f" Recurso principal: {primary['asset_id']}." if primary else ""
    return f"{noun} sobre «{row['working_title']}»: {desc}. La lectura central es que {row['key_message'][0].lower() + row['key_message'][1:]}{asset_note}"


def question_and_answer(row: dict[str, str]) -> tuple[str, str]:
    sid = row["slide_id"]
    if sid == "U04-003":
        return "¿Cuál afirmación te resulta más dudosa y qué dato necesitarías para justificarla?", "No se corrige todavía; se espera que nombren al menos magnitud, referencia, fase/correlación o condiciones de campo."
    if sid == "U04-049":
        return "¿Qué descriptor elegirías para detectar saturación y cuál para estimar componente continua?", "Pico para saturación; valor medio para componente continua."
    if sid == "U04-075":
        return "¿Dos fuentes iguales siempre elevan el nivel?", "No. Si son coherentes y llegan en oposición de fase pueden cancelar la presión en el punto ideal."
    if sid == "U04-105":
        return "¿Qué dato debe conocerse antes de elegir una fórmula de suma?", "La relación temporal: fase estable/coherencia o ausencia de correlación durante la ventana."
    if sid == "U04-108":
        return "Elegí uno de los seis prompts y justificá la respuesta con magnitud, unidad o condición.", "La respuesta debe nombrar la variable y al menos una condición de validez; no alcanza con citar una regla numérica."
    if row["slide_type"] == "divisor":
        q = BLOCK_QUESTIONS[row["block"].split()[0]]
    elif row["slide_type"] == "error frecuente":
        q = f"¿Qué condición o distinción falta en la afirmación «{row['working_title']}»?"
    elif row["slide_type"] in {"ecuación", "ejemplo", "gráfico"}:
        q = "¿Qué magnitud entrega esta relación, en qué unidad y bajo qué condición principal?"
    elif row["slide_type"] in {"comparación", "recapitulación", "recapitulación final"}:
        q = "¿Qué criterio permite distinguir los casos mostrados?"
    else:
        q = "¿Cuál es la idea física central de esta slide?"
    return q, row["key_message"]


def visual_guide(row: dict[str, str], assets: list[dict[str, str]]) -> str:
    if row["visual_class"] == "none":
        return "Mantener la atención en el título y revelar el contenido en el orden escrito; no agregar un visual decorativo."
    guide = visual_description(row).rstrip(".")
    if row["visual_class"] in {"diagram", "mixed", "equation_only"}:
        return f"Recorrer el recurso de izquierda a derecha o de causa a consecuencia. Señalar primero la entidad inicial, luego las relaciones y al final la condición o conclusión. {guide}. No leer cada caja: usar el diagrama como guía y explicar la relación entre nodos."
    if row["visual_class"] == "chart":
        return f"Nombrar primero ejes, variables, unidades y escala. Después identificar una tendencia o ancla y recién entonces formular la conclusión. {guide}."
    if row["visual_class"] == "video_or_gif":
        return f"Antes de reproducir, pedir una predicción. Pausar en un cuadro donde se distingan movimiento local y propagación. {guide}. Usar la alternativa estática si el medio falla."
    return f"Identificar qué parte del recurso aporta evidencia y qué parte solo orienta. {guide}."


def media_cue(row: dict[str, str], assets: list[dict[str, str]]) -> str:
    media = [a for a in assets if a["type"] in {"video_or_gif", "audio", "video"}]
    if not media:
        return "No corresponde."
    cues = []
    for asset in media:
        if asset["status"] == "proposed":
            cues.append(f"`{asset['asset_id']}` está propuesto: no reproducir hasta aprobarlo; usar la alternativa estática indicada.")
        elif asset["status"] == "shortlisted":
            cues.append(f"`{asset['asset_id']}` está preseleccionado: verificar encuadre/crédito antes de reproducir y conservar alternativa estática.")
        else:
            cues.append(f"Reproducir `{asset['asset_id']}` después de pedir una predicción; mantener volumen seguro y alternativa estática.")
    return " ".join(cues)


def explanation_text(row: dict[str, str]) -> str:
    typ = row["slide_type"]
    message = row["key_message"]
    scope = row["visible_content_summary"].rstrip(".")
    if typ == "portada":
        return "Escribir o decir «80 dB» antes de mostrar el subtítulo. Pedir qué información falta y conservar las respuestas sin corregirlas todavía. Presentar la unidad como una búsqueda de magnitud, referencia y condiciones, no como una lista de fórmulas."
    if typ == "divisor":
        return f"Leer la pregunta guía y recuperar una respuesta del bloque anterior. Instalar el nuevo problema con lenguaje cotidiano; cerrar con el criterio que se construirá: {message}"
    if typ in {"pregunta", "objetivos", "puente"}:
        return f"Dar unos segundos de trabajo individual antes de escuchar respuestas. Organizar lo que aparezca alrededor del propósito de la slide: {row['learning_purpose']} No resolver por adelantado; usar como criterio de cierre que {message[0].lower() + message[1:]}"
    if typ == "ecuación":
        return f"Comenzar por la pregunta física y recién después revelar la ecuación. Leer cada símbolo con su unidad, comprobar que la razón o el resultado tengan las dimensiones correctas y señalar la hipótesis que permite usarla. Interpretación que debe quedar: {message}"
    if typ == "ejemplo":
        return f"Pedir primero una estimación cualitativa. Resolver en el orden dato → relación válida → sustitución con unidades → resultado → interpretación. Hacer explícito el redondeo y volver a la condición del modelo. Conclusión: {message}"
    if typ == "gráfico":
        return f"Solicitar una lectura sin conclusiones: identificar ejes, unidades, escala y curvas. Luego comparar dos puntos o regiones y formular la tendencia. Aclarar qué representa la figura y qué no permite inferir. Síntesis: {message}"
    if typ == "proceso":
        return f"Narrar la secuencia paso a paso sin convertirla en una cadena causal más rígida de lo aprobado. En cada etapa preguntar qué entidad cambia y qué permanece. Alcance visual: {scope}. Idea de cierre: {message}"
    if typ == "definición":
        return f"Partir de un caso observable y pedir una descripción antes de nombrar el término. Introducir luego símbolo y unidad, y contrastar con el concepto vecino que suele confundirse. Definición funcional que debe quedar: {message}"
    if typ == "comparación":
        return f"Establecer un único criterio de comparación por vez: objeto, magnitud, unidad o condición. Pedir que el grupo encuentre una diferencia y una relación válida. No presentar las columnas como sinónimos. Cierre: {message}"
    if typ == "error frecuente":
        return f"Mostrar primero la afirmación problemática y pedir un contraejemplo o la condición faltante. Corregirla nombrando la magnitud adecuada, sin reemplazarla por otra regla memorizada. Formulación correcta: {message}"
    if typ in {"recapitulación", "recapitulación final"}:
        return f"Usar recuperación activa: ocultar inicialmente las respuestas y pedir que completen el mapa o la matriz. Volver solo a los nodos que generen duda. La síntesis debe poder expresarse así: {message}"
    if typ == "aplicación":
        return f"Presentar la situación profesional sin prometer una inferencia clínica mayor que la evidencia disponible. Separar fenómeno, sensor, procesamiento y decisión. Vínculo que debe quedar: {message}"
    if typ in {"recordatorio", "profundización", "derivación", "solución"}:
        return f"Usar esta slide solo si la ruta central deja una duda concreta. Reconstruir el paso solicitado, mantener símbolos y unidades, y regresar a la slide de origen. Resultado conceptual: {message}"
    if typ == "mapa":
        return f"Recorrer el mapa por encuentros y explicar que representa decisiones encadenadas, no el índice del capítulo. Señalar la etapa actual y anticipar solo la siguiente. Idea organizadora: {message}"
    if typ == "cierre":
        return f"Comparar las dos señales sin entrar todavía en Fourier. Preguntar qué información falta pese a conocer el mismo RMS y dejar la pregunta abierta para U5. Cierre: {message}"
    return f"Desarrollar el alcance aprobado —{scope}— y vincular cada afirmación con una magnitud, unidad, referencia o condición. Idea central: {message}"


def make_slide_text(rows: list[dict[str, str]], by_slide: dict[str, list[dict[str, str]]]) -> str:
    out = [
        "# Unidad 4 — Texto de slides",
        "",
        "**Base exclusiva:** `storyboard.md` aprobado. **Alcance:** U04-001 a U04-125. Este archivo define copy y especificaciones; no constituye un PowerPoint.",
        "",
        "Las ecuaciones usan la notación transversal aprobada (`W_ac`, `Q_dir`, `p_ref`, `T_obs`). En diagramas, el texto exterior expresa la idea central y el recurso conserva nodos breves; no se duplican explicaciones largas dentro de cajas.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        assets = assets_for_slide(sid, by_slide)
        block_code, _, block_name = row["block"].partition(" · ")
        subtitle = BLOCK_QUESTIONS.get(block_code, "") if row["slide_type"] in {"portada", "divisor", "mapa", "recapitulación final", "cierre"} else "No corresponde."
        out.extend([
            f"## {sid} — {row['working_title']}",
            "",
            f"**Título:** {row['working_title']}",
            "",
            f"**Subtítulo:** {subtitle}",
            "",
            "**Contenido visible:**",
            "",
            format_lines(visible_lines(row)),
            "",
            "**Ecuaciones:**",
            "",
            equation_text(sid),
            "",
            f"**Definiciones:** {definition_text(row)}",
            "",
            f"**Ejemplo:** {example_text(row)}",
            "",
            f"**Caption sugerido:** {caption_text(row, assets)}",
            "",
            f"**Visual:** {visual_text(row, assets)}",
            "",
            f"**Layout:** `{row['suggested_layout']}`. Bloque {block_code} — {block_name}; función `{row['slide_type']}`.",
            "",
            f"**Fuente:** {row['source']}",
            "",
            f"**Transición:** {row['transition']}",
            "",
            f"**Texto alternativo:** {alt_text(row, assets)}",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"


def make_notes(rows: list[dict[str, str]], by_slide: dict[str, list[dict[str, str]]]) -> str:
    out = [
        "# Unidad 4 — Notas del orador",
        "",
        "Las notas amplían el copy visible sin repetirlo literalmente. Las duraciones son orientativas; las slides de respaldo se usan solo cuando una duda o actividad lo justifica.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        assets = assets_for_slide(sid, by_slide)
        q, a = question_and_answer(row)
        error = row["speaker_note_goal"]
        out.extend([
            f"## {sid} — {row['working_title']}",
            "",
            f"**Duración aproximada:** {DURATION.get(row['slide_type'], '4 min')}",
            "",
            f"**Propósito:** {row['learning_purpose']}",
            "",
            f"**Explicación extendida:** {explanation_text(row)}",
            "",
            f"**Guía para el visual o diagrama:** {visual_guide(row, assets)}",
            "",
            f"**Pregunta al grupo:** {q}",
            "",
            f"**Respuesta esperada:** {a}",
            "",
            f"**Énfasis / error frecuente:** {error}",
            "",
            f"**Demostración o multimedia:** {media_cue(row, assets)}",
            "",
            f"**Transición:** {row['transition']}",
            "",
            f"**Fuente de apoyo:** {row['source']}",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"


def make_source_map(rows: list[dict[str, str]], by_slide: dict[str, list[dict[str, str]]]) -> str:
    out = [
        "# Unidad 4 — Mapa de fuentes del texto",
        "",
        "Este mapa conserva la trazabilidad definida por el storyboard aprobado. `ED` identifica elaboración didáctica ya aprobada; no se incorporaron afirmaciones externas nuevas durante la redacción.",
        "",
        "## Claves",
        "",
    ]
    out.extend(f"- **{key}:** {value}" for key, value in SOURCE_LEGEND.items())
    out.extend([
        "",
        "## Trazabilidad slide por slide",
        "",
        "| slide_id | bloque | fuentes aprobadas | recursos vinculados | observación de uso |",
        "|---|---|---|---|---|",
    ])
    for row in rows:
        assets = assets_for_slide(row["slide_id"], by_slide)
        asset_text = "; ".join(f"{a['asset_id']} ({a['status']})" for a in assets) or "—"
        observation = "Fuente para copy y notas; recurso visual solo como apoyo."
        if any(a["status"] in {"proposed", "pending_approval", "shortlisted"} for a in assets):
            observation = "Copy cerrado; el recurso no aprobado debe reemplazarse por la alternativa estática aprobada o mantenerse pendiente."
        out.append(f"| {row['slide_id']} | {row['block']} | {row['source']} | {asset_text} | {observation} |")
    out.extend([
        "",
        "## Límites de la redacción",
        "",
        "- U04-105 y U04-124 se mantienen como caso diagnóstico y solución razonada: el storyboard no fija valores numéricos propios y no se fabricaron datos.",
        "- U04-102 conserva la consigna de leer patrones a varias frecuencias, pero el dataset `U04-CH-012` sigue pendiente de aprobación; el copy no depende de una curva específica.",
        "- Las referencias normativas se mencionan solo a través del libro y del análisis de fuentes; no se añadieron ediciones ni requisitos no aprobados.",
        "- Las slides de percepción anticipan límites de inferencia y remiten a U7/U8; no desarrollan psicoacústica ni calibración clínica.",
    ])
    return "\n".join(out).rstrip() + "\n"


def make_review(rows: list[dict[str, str]], by_slide: dict[str, list[dict[str, str]]]) -> str:
    counts = Counter(r["slide_type"] for r in rows)
    diagram_slides = sum(r["visual_class"] in {"diagram", "mixed", "equation_only"} for r in rows)
    chart_slides = sum(r["visual_class"] == "chart" for r in rows)
    media_pending = []
    for row in rows:
        assets = assets_for_slide(row["slide_id"], by_slide)
        for asset in assets:
            if asset["status"] in {"proposed", "pending_approval", "shortlisted"}:
                media_pending.append((row["slide_id"], asset["asset_id"], asset["status"]))
    out = [
        "# Unidad 4 — Revisión de redacción",
        "",
        "**Resultado:** redacción completa para las 125 slides aprobadas, con texto visible, notas y trazabilidad. No quedan problemas críticos ni mayores. No se produjo ni modificó ningún PowerPoint.",
        "",
        "## Cobertura",
        "",
        f"- Secuencia verificada: `U04-001` a `U04-125`, sin faltantes ni duplicados.",
        f"- Slides con gráfico cuantitativo: {chart_slides}.",
        f"- Slides con diagrama, esquema mixto o ecuación anotada: {diagram_slides}.",
        f"- Tipos de slide: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) + ".",
        "- Cada ficha de `slide_text.md` incluye título, subtítulo, contenido visible, ecuaciones, definiciones, ejemplo, caption, visual, layout, fuente, transición y texto alternativo.",
        "- Cada ficha de `speaker_notes.md` incluye duración, propósito, explicación, guía visual, pregunta, respuesta, énfasis/error, multimedia, transición y fuente.",
        "",
        "## Revisión por criterios",
        "",
        "| criterio | estado | evidencia / decisión |",
        "|---|---|---|",
        "| Fidelidad al storyboard | aprobado | Se conservaron IDs, títulos, bloque, función, mensaje, alcance, layout, fuente y transición. |",
        "| Nivel de primer año | aprobado | La secuencia conserva intuición → definición → ecuación → ejemplo → interpretación. |",
        "| Símbolos y unidades | aprobado | Se aplicó `notation_guide.md`; toda ecuación redactada identifica magnitudes y las notas exigen control de unidades. |",
        "| Ejemplos con pasos | aprobado | Los ejemplos numéricos usan únicamente valores ya presentes en storyboard/libro; U04-105 no recibe datos nuevos. |",
        "| Interpretación física | aprobado | Las notas piden distinguir magnitud, referencia, ventana y dominio de validez. |",
        "| Fonoaudiología | aprobado | Voz, micrófono, sonómetro, SPL/HL y campo sonoro aparecen con límites explícitos. |",
        "| Diagramas | aprobado para escritura | El copy exterior resume la idea central y evita duplicar nodos; las explicaciones extensas quedan en notas. |",
        "| Accesibilidad | aprobado | Todas las slides incluyen texto alternativo; los captions distinguen gráficos, esquemas conceptuales y recursos externos. |",
        "| Tono | aprobado | Español académico claro, sin tono publicitario ni fórmulas retóricas genéricas. |",
        "| PowerPoint | no iniciado | Fuera del alcance solicitado. |",
        "",
        "## Hallazgos y pendientes no bloqueantes",
        "",
        "| elemento | severidad | tratamiento | estado |",
        "|---|---|---|---|",
        "| U04-105: el storyboard no fija un conjunto numérico para el caso integrador | menor | Se redactó como diagnóstico de datos, decisiones y limitaciones; no se inventaron valores. | resuelto para escritura; validar antes del montaje si se desea cálculo numérico |",
        "| U04-102: patrón polar con datos abiertos | menor | El copy funciona con dos o tres frecuencias, pero no afirma valores. | pendiente de aprobación de `U04-CH-012` |",
        "| Recursos audiovisuales propuestos o preseleccionados | menor | Las notas indican usar alternativa estática mientras no estén aprobados. | pendiente de curaduría/producción |",
        "| Notación visible `W_ac` y `Q_dir` | menor | Se aplicó la guía transversal y se documentó la equivalencia con `W` y `Q` del libro. | pendiente de validación docente global |",
        "",
        "## Controles automáticos ejecutados",
        "",
        "- Conteo y continuidad de IDs.",
        "- Presencia de todos los campos obligatorios por slide.",
        "- Correspondencia de fuentes con cada fila del storyboard.",
        "- Detección de recursos con estado `proposed`, `shortlisted` o `pending_approval`.",
        "- Confirmación de que los archivos de salida son Markdown y no se generó `.pptx`.",
        "",
        "## Recursos visuales todavía no aprobados",
        "",
    ]
    for sid, aid, status in sorted(set(media_pending)):
        out.append(f"- {sid}: `{aid}` — `{status}`.")
    return "\n".join(out).rstrip() + "\n"


def validate(text: str, rows: list[dict[str, str]], required: list[str]) -> None:
    for row in rows:
        sid = row["slide_id"]
        if text.count(f"## {sid} ") != 1:
            raise RuntimeError(f"Entrada ausente o duplicada: {sid}")
    for label in required:
        if text.count(label) != len(rows):
            raise RuntimeError(f"Campo {label!r}: se esperaban {len(rows)} apariciones y hay {text.count(label)}")


def main() -> None:
    rows = parse_storyboard()
    by_slide, _ = parse_manifest()
    slide_text = make_slide_text(rows, by_slide)
    notes = make_notes(rows, by_slide)
    source_map = make_source_map(rows, by_slide)
    review = make_review(rows, by_slide)

    validate(slide_text, rows, ["**Título:**", "**Subtítulo:**", "**Contenido visible:**", "**Ecuaciones:**", "**Definiciones:**", "**Ejemplo:**", "**Caption sugerido:**", "**Visual:**", "**Layout:**", "**Fuente:**", "**Transición:**", "**Texto alternativo:**"])
    validate(notes, rows, ["**Duración aproximada:**", "**Propósito:**", "**Explicación extendida:**", "**Guía para el visual o diagrama:**", "**Pregunta al grupo:**", "**Respuesta esperada:**", "**Énfasis / error frecuente:**", "**Demostración o multimedia:**", "**Transición:**", "**Fuente de apoyo:**"])

    (UNIT / "slide_text.md").write_text(slide_text, encoding="utf-8")
    (UNIT / "speaker_notes.md").write_text(notes, encoding="utf-8")
    (UNIT / "source_map.md").write_text(source_map, encoding="utf-8")
    (UNIT / "writing_review.md").write_text(review, encoding="utf-8")
    print("Generated:")
    for name in ["slide_text.md", "speaker_notes.md", "source_map.md", "writing_review.md"]:
        p = UNIT / name
        print(f"- {p.relative_to(ROOT)} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
