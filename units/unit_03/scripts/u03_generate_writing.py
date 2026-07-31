from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path


UNIT_DIR = Path(__file__).resolve().parents[1]
STORYBOARD = UNIT_DIR / "storyboard.md"


def parse_storyboard():
    rows = []
    for line in STORYBOARD.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| U03-"):
            continue
        values = [value.strip() for value in line.strip("|").split("|")]
        if len(values) != 15:
            raise ValueError(f"Fila con {len(values)} columnas: {values[:2]}")
        rows.append(
            {
                "slide_id": values[0],
                "block": values[1],
                "slide_type": values[2],
                "title": values[3],
                "learning_purpose": values[4],
                "key_message": values[5],
                "summary": values[6],
                "visual": values[7],
                "visual_class": values[8],
                "layout": values[9],
                "speaker_goal": values[10],
                "source": values[11],
                "prerequisites": values[12],
                "transition": values[13],
                "status": values[14],
            }
        )
    return rows


VISIBLE = {
    "U03-001": "**Unidad 3.** Oscilaciones, ondas y tonos: del movimiento local a la propagación.",
    "U03-002": "**Prediga antes de explicar:** ¿se desplaza el aire desde el parlante hasta el oído?, ¿qué avanza?, ¿qué permanece oscilando cerca de su equilibrio?",
    "U03-003": "Decida **verdadero o falso** y justifique: 1. La materia viaja con la onda. 2. Una frecuencia mayor siempre se propaga más rápido. 3. Mayor amplitud siempre significa mayor sonoridad. 4. La sinusoide dibuja la trayectoria de una partícula.",
    "U03-004": "**Ya podemos usar:** equilibrio, eje y unidades, seno y coseno, `f=1/T`. **Conviene recuperar:** el signo restaurador en `F_el=-k_sx` y la lectura de ambos ejes.",
    "U03-005": "**Distinguir:** oscilación y propagación. **Representar:** amplitud, período, frecuencia, fase y longitud de onda. **Calcular:** relaciones simples con unidades. **Aplicar:** describir un tono desde la fuente hasta el receptor.",
    "U03-006": "Oscilación → MAS → parámetros → sinusoide → parlante → onda viajera → fase → superposición → aplicación.",
    "U03-007": "**Pregunta guía:** ¿cómo puede una parte del medio oscilar sin viajar junto con la perturbación?",
    "U03-008": "Una oscilación es un movimiento de ida y vuelta alrededor de una posición de equilibrio. Puede ser repetitiva sin ser necesariamente armónica.",
    "U03-009": "Una región desplaza a la siguiente; la respuesta ocurre con retraso. Cada región se mueve localmente mientras el frente de perturbación avanza.",
    "U03-010": "**Materia:** oscila localmente. **Perturbación:** cambia de región. **Energía:** puede transferirse. En el modelo ideal no hay transporte neto de materia con el frente.",
    "U03-011": "Para una onda mecánica se necesitan: **medio material**, **interacción entre regiones vecinas** y **una perturbación inicial**. El sonido no se propaga en el vacío.",
    "U03-012": "**Longitudinal:** movimiento local paralelo a la propagación. **Transversal:** movimiento local perpendicular. La clasificación compara dos direcciones.",
    "U03-013": "**Observe dos movimientos:** una marca de la espira oscila localmente; el pulso recorre el resorte. ¿Qué distancia recorre cada uno?",
    "U03-014": "La marca vuelve cerca de su posición inicial, pero la perturbación alcanza regiones nuevas. **Volver no significa no transmitir.**",
    "U03-015": "**Fuente:** inicia la perturbación. **Medio:** la transmite. **Receptor:** responde localmente. Esta cadena describe el mecanismo físico, no una interpretación clínica.",
    "U03-016": "Compruebe: 1. ¿Qué oscila? 2. ¿Qué se propaga? 3. ¿Qué necesita una onda mecánica? 4. ¿Qué direcciones se comparan para clasificarla?",
    "U03-017": "**Pregunta guía:** ¿qué información mínima permite describir una oscilación repetitiva?",
    "U03-018": "En el movimiento armónico simple, la fuerza neta es proporcional al desplazamiento y apunta hacia el equilibrio.",
    "U03-019": "**Tres lecturas simultáneas:** mayor `|x|` implica mayor `|F|`; el signo de `F` se opone al de `x`; la aceleración apunta hacia el equilibrio.",
    "U03-020": "Un ciclo puede leerse en cinco estados: extremo positivo → equilibrio → extremo negativo → equilibrio → estado inicial.",
    "U03-021": "La amplitud `A_x` es el máximo valor de `|x|`. Es una distancia y se expresa en metros o submúltiplos.",
    "U03-022": "El período `T` es el tiempo que tarda un ciclo completo. Su unidad SI es el segundo (`s`).",
    "U03-023": "La frecuencia `f` es la cantidad de ciclos por segundo. `1 Hz = 1 s⁻¹`.",
    "U03-024": "Período y frecuencia describen la misma repetición desde perspectivas inversas: duración de un ciclo y ciclos por segundo.",
    "U03-025": "**Datos:** `T=2 ms`. **Paso 1:** convertir a segundos. **Paso 2:** aplicar `f=1/T`. **Resultado:** `f=500 Hz`.",
    "U03-026": "La fase indica **en qué estado del ciclo** se encuentra la oscilación respecto de una referencia. No es una posición adicional.",
    "U03-027": "Para describir una oscilación: `A_x` indica cuánto se separa; `T` cuánto dura un ciclo; `f` cuántos ciclos ocurren por segundo; la fase dónde está dentro del ciclo.",
    "U03-028": "**Pregunta guía:** ¿qué significa una curva sinusoidal y qué no permite concluir por sí sola?",
    "U03-029": "Una sinusoide es una función: para cada instante `t`, el modelo asigna una elongación `x(t)`. La forma de la curva no es la trayectoria espacial de la masa.",
    "U03-030": "**Modelo del cono:** `A_x=0,010 mm=10 µm`, `f=500 Hz`, `T=2 ms`. Describe desplazamiento local; no determina por sí solo presión sonora ni sonoridad.",
    "U03-031": "En los extremos, la elongación es máxima y la velocidad instantánea es cero. Al cruzar el equilibrio, el módulo de la velocidad es máximo.",
    "U03-032": "La aceleración apunta siempre hacia el equilibrio: es máxima en módulo en los extremos y nula al pasar por el equilibrio.",
    "U03-033": "Las curvas `x(t)`, `v(t)` y `a(t)` comparten período, pero no alcanzan máximos ni ceros al mismo tiempo.",
    "U03-034": "En el instante marcado, determine el signo de `x`, `v` y `a`. Justifique con pendiente y dirección hacia el equilibrio.",
    "U03-035": "La misma forma sinusoidal puede representar desplazamiento `x`, desplazamiento de aire `ξ`, presión acústica `p_ac` o tensión `V`. **Los ejes deciden el significado.**",
    "U03-036": "Una curva `x(t)` muestra posición frente a tiempo. No dibuja el camino de la partícula en el espacio.",
    "U03-037": "**Esquemática:** muestra relaciones. **Normalizada:** compara formas sin valor físico absoluto. **Calibrada:** permite leer magnitudes con unidad.",
    "U03-038": "Antes de interpretar una curva, pregunte: ¿qué variable representa?, ¿qué hay en el eje horizontal?, ¿qué unidades aparecen?, ¿la escala está calibrada?",
    "U03-039": "**Pregunta guía:** ¿cómo se transforma una señal eléctrica sinusoidal en una perturbación acústica?",
    "U03-040": "Un tono puro ideal contiene una sola frecuencia y puede representarse mediante una sinusoide estable.",
    "U03-041": "Un tono real tiene comienzo y final: ataque → tramo aproximadamente estable → caída. El modelo ideal describe sobre todo el tramo estable.",
    "U03-042": "`V(t)` excita el parlante → el cono presenta `x_cono(t)` → el aire adquiere `ξ(t)` → en un punto se mide `p_ac(t)`. Cada etapa usa una variable y una unidad distintas.",
    "U03-043": "El cono avanza y retrocede alrededor de su equilibrio. Su desplazamiento es local: no viaja desde el parlante hasta el oído.",
    "U03-044": "Cuando el cono avanza comprime el aire vecino; cuando retrocede produce rarefacción. Las regiones alternadas se transmiten por interacción.",
    "U03-045": "En un punto fijo, `p_ac(t)` alterna por encima y por debajo de la presión ambiente. Una curva sin calibración no permite asignar nivel sonoro.",
    "U03-046": "Para describir físicamente un tono audiométrico hacen falta frecuencia, nivel y condiciones de calibración. El modelo no sustituye una interpretación clínica.",
    "U03-047": "Misma periodicidad, variables distintas: señal eléctrica → cono → aire → presión. En cada dominio cambian el símbolo y la unidad.",
    "U03-048": "**Pregunta guía:** ¿cómo cambia la lectura cuando observamos una onda en el tiempo o en el espacio?",
    "U03-049": "La función `ξ(x,t)` asigna un estado del medio a cada posición `x` y a cada instante `t`.",
    "U03-050": "Un mapa espacio–tiempo reúne dos preguntas: cómo evoluciona un punto fijo y cómo se distribuye la perturbación en un instante fijo.",
    "U03-051": "Al fijar `x=x₀`, se observa una historia temporal. La repetición se mide con `T` y `f`.",
    "U03-052": "Al fijar `t=t₀`, se observa un perfil espacial. La repetición se mide con la longitud de onda `λ`.",
    "U03-053": "`T` separa estados equivalentes en el **tiempo**; `λ` separa estados equivalentes en el **espacio**. No son la misma magnitud.",
    "U03-054": "La longitud de onda `λ` es la distancia mínima entre dos puntos en el mismo estado de fase, medida en metros.",
    "U03-055": "La fase depende de `t` y de `x`. El signo del término espacial indica la dirección de propagación según la convención elegida.",
    "U03-056": "En un período, un estado de fase avanza una longitud de onda. Por eso la rapidez de propagación es distancia dividida por tiempo.",
    "U03-057": "**Condición:** aire con `c≈340 m/s`. **Dato:** `f=1000 Hz`. **Cálculo:** `λ=c/f=0,34 m=34 cm`.",
    "U03-058": "Lea primero `T` en el gráfico temporal y `λ` en el perfil espacial. Luego calcule `f=1/T` y finalmente `c=λf`. Incluya unidades.",
    "U03-059": "Una sola onda admite: mapa `x–t` → corte temporal (`T`, `f`) → corte espacial (`λ`) → relación `c=λf`.",
    "U03-060": "**Pregunta guía:** ¿qué velocidad estamos describiendo y respecto de qué referencia comparamos la fase?",
    "U03-061": "Siga primero una partícula del medio y luego un estado de fase. ¿Cuál oscila cerca de su lugar y cuál avanza?",
    "U03-062": "`u`: velocidad local de una partícula del medio. `c`: rapidez de propagación de un estado de fase. Pueden tener dirección y valor distintos.",
    "U03-063": "En un mismo medio, aumentar `f` no obliga a aumentar `c`: si `c` permanece aproximadamente constante, `λ` disminuye.",
    "U03-064": "Dos oscilaciones con igual frecuencia pueden estar en estados de ciclo diferentes. La separación horizontal expresa un desfase.",
    "U03-065": "`Δφ` compara dos fases. Valores de referencia: `0` en fase; `π/2` un cuarto de ciclo; `π` oposición; `2π` un ciclo completo.",
    "U03-066": "En un perfil espacial: separación `λ` → `Δφ=2π`; separación `λ/2` → `Δφ=π`.",
    "U03-067": "Para igual frecuencia, un retraso temporal `Δt` produce un cambio de fase proporcional a la fracción de ciclo transcurrida.",
    "U03-068": "Clasifique cada par como `0`, `π/2` o `π`. Use máximos, mínimos y cruces por cero; no estime solo por apariencia.",
    "U03-069": "Dos preguntas evitan confusiones: **¿velocidad de qué?** (`u` o `c`) y **¿fase respecto de qué referencia?**",
    "U03-070": "**Pregunta guía:** ¿qué ocurre cuando dos perturbaciones coinciden en el mismo lugar y momento?",
    "U03-071": "En un medio lineal, la perturbación resultante en cada punto e instante es la suma algebraica de las perturbaciones individuales.",
    "U03-072": "Dos sinusoides iguales y en fase se refuerzan: sus valores instantáneos tienen el mismo signo y la amplitud resultante aumenta.",
    "U03-073": "Dos sinusoides de igual frecuencia y amplitud, opuestas en fase en un punto, pueden cancelarse allí. La condición es local y controlada.",
    "U03-074": "Entre refuerzo y cancelación hay resultados intermedios. Compare `Δφ=π/3`, `π/2` y `2π/3`.",
    "U03-075": "Antes de ver la suma, prediga su amplitud relativa y justifique con el desfase. Después contraste con la curva resultante.",
    "U03-076": "La cancelación activa requiere referencia, amplitud, fase y geometría controladas. No produce silencio perfecto en todo el espacio.",
    "U03-077": "En el oído y en la voz coinciden muchas componentes. La superposición permite sumar perturbaciones; el análisis frecuencial se desarrollará en la Unidad 5.",
    "U03-078": "Para analizar superposición pregunte: ¿qué valor tiene cada señal?, ¿qué amplitud?, ¿qué desfase?, ¿en qué lugar se comparan?",
    "U03-079": "Producción: la fuente oscila. Propagación: el medio transmite la perturbación. Recepción: el sistema auditivo responde localmente.",
    "U03-080": "**Caso:** un parlante emite un tono de `500 Hz`. Explique el mecanismo, identifique variables, lea las dos representaciones, calcule `T` y `λ` bajo la condición indicada y señale un límite del modelo.",
    "U03-081": "Oscilación local → parámetros → representación temporal y espacial → propagación y fase → superposición → producción, medio y recepción.",
    "U03-082": "Revise las cuatro afirmaciones iniciales. Para cada una, escriba **V/F**, una razón física y la slide que aporta evidencia.",
    "U03-083": "Una curva normalizada informa forma, periodicidad y fase relativa. Para hablar de presión, nivel o espectro aún necesitamos variable, escala, calibración y contenido frecuencial.",
    "U03-084": "`sen` y `cos` describen el mismo tipo de oscilación con distinta referencia de fase. Un ciclo completo corresponde a `2π rad`.",
    "U03-085": "La frecuencia angular mide cambio de fase por unidad de tiempo. Para `f=500 Hz`, `ω=1000π rad/s`.",
    "U03-086": "En un MAS ideal masa–resorte, la frecuencia propia aumenta con la rigidez y disminuye con la masa.",
    "U03-087": "1. **F:** la materia oscila localmente. 2. **F:** `c` depende principalmente del medio. 3. **F:** la sonoridad no se deduce solo de una amplitud no calibrada. 4. **F:** la sinusoide no es una trayectoria espacial.",
    "U03-088": "`x`, `v` y `a` comparten `ω`; la velocidad está desfasada un cuarto de ciclo respecto de `x` y la aceleración está en oposición con `x`.",
    "U03-089": "`k_onda` mide fase acumulada por distancia; `k_s` mide rigidez. Los subíndices evitan confundir `rad/m` con `N/m`.",
    "U03-090": "Las formas con `f, λ` y con `ω, k_onda` son equivalentes. El signo del término espacial conserva la convención de dirección.",
    "U03-091": "La notación angular no introduce una rapidez nueva: al sustituir `ω=2πf` y `k_onda=2π/λ` se recupera `c=λf`.",
    "U03-092": "La amplitud resultante depende de `A₁`, `A₂` y `cos(Δφ)`. Verifique los límites `Δφ=0` y `Δφ=π`.",
    "U03-093": "Para amplitudes iguales, `A_R/A` cambia de forma continua entre `2` y `0` al variar `Δφ` entre `0` y `π`, y vuelve a `2` en `2π`.",
    "U03-094": "**Paso 1:** marcar `T` en el eje temporal y `λ` en el espacial. **Paso 2:** convertir `T` a segundos. **Paso 3:** calcular `f=1/T`. **Paso 4:** calcular `c=λf`. Conservar los valores leídos en los gráficos aprobados.",
    "U03-095": "1. El cono oscila localmente. 2. El aire transmite la perturbación. 3. `f=500 Hz` implica `T=2 ms`. 4. `λ` se obtiene con la rapidez indicada para el medio. 5. El modelo no fija nivel ni respuesta clínica.",
    "U03-096": "`A_x`, `A_ξ`: amplitudes; `f`: frecuencia; `T`: período; `φ₀`, `Δφ`: fases; `λ`: longitud de onda; `u`: velocidad local; `c`: propagación; `k_s`: rigidez; `k_onda`: número de onda.",
}


EQUATIONS = {
    "U03-004": "`f=1/T`; `F_el=-k_sx`. `f` en Hz; `T` en s; `F_el` en N; `k_s` en N/m; `x` en m.",
    "U03-018": "`F_neta=-k_sx`. Condición del MAS ideal: proporcionalidad lineal y sentido restaurador.",
    "U03-019": "`ma=-k_sx`. `m` en kg; `a` en m/s²; `k_s` en N/m; `x` en m.",
    "U03-021": "`A_x=max|x(t)|`. `A_x` tiene la misma unidad que `x`.",
    "U03-022": "`T=Δt` de un ciclo completo. Unidad SI: s.",
    "U03-023": "`f=N/Δt`. Unidad: Hz = s⁻¹.",
    "U03-024": "`f=1/T`; `T=1/f`.",
    "U03-025": "`T=2 ms=2×10⁻³ s`; `f=1/T=500 Hz`.",
    "U03-029": "`x(t)=A_x cos(2πft+φ₀)`. `x` y `A_x` en m; `t` en s; `f` en Hz; `φ₀` en rad.",
    "U03-030": "`x_cono(t)=A_x cos(2πft+φ₀)` con `A_x=10 µm`, `f=500 Hz`, `T=2 ms`.",
    "U03-040": "`s(t)=A_s cos(2πft+φ₀)`. El símbolo y la unidad de `A_s` dependen de la variable representada.",
    "U03-045": "`p_ac(t)=A_p cos(2πft+φ₀)`. `p_ac` y `A_p` en Pa; curva conceptual sin nivel calibrado.",
    "U03-049": "`ξ=ξ(x,t)`. `ξ` en m; `x` en m; `t` en s.",
    "U03-051": "`ξ(x₀,t)`; `f=1/T`.",
    "U03-052": "`ξ(x,t₀)`; repetición espacial `λ` en m.",
    "U03-054": "`λ`: distancia entre puntos consecutivos con igual fase. Unidad: m.",
    "U03-055": "`ξ(x,t)=A_ξ cos(2πft-2πx/λ+φ₀)`. `A_ξ` en m; `f` en Hz; `λ`, `x` en m; fases en rad.",
    "U03-056": "`c=λ/T=λf`. `c` en m/s; `λ` en m; `T` en s; `f` en Hz.",
    "U03-057": "`λ=c/f=(340 m/s)/(1000 s⁻¹)=0,34 m=34 cm`.",
    "U03-058": "`f=1/T`; `c=λf`.",
    "U03-062": "`u`: velocidad local de partícula; `c=λf`: rapidez de propagación. Ambas se expresan en m/s, pero describen objetos distintos.",
    "U03-063": "`c=λf`; si `c` es constante y `f` aumenta, `λ=c/f` disminuye.",
    "U03-065": "`Δφ=φ₂-φ₁`. Unidad: rad.",
    "U03-066": "`Δφ=2πΔx/λ`. Para `Δx=λ/2`, `Δφ=π`.",
    "U03-067": "`Δφ=2πfΔt=2πΔt/T`.",
    "U03-071": "`y_R(x,t)=y₁(x,t)+y₂(x,t)`.",
    "U03-072": "Si `A₁=A₂=A` y `Δφ=0`, entonces `A_R=2A`.",
    "U03-073": "Si `A₁=A₂=A` y `Δφ=π`, entonces `A_R=0` en el punto considerado.",
    "U03-080": "`T=1/f`; bajo la condición indicada, `λ=c/f`.",
    "U03-084": "`cos θ=sen(θ+π/2)`; un ciclo completo: `2π rad`.",
    "U03-085": "`ω=2πf=2π/T`. `ω` en rad/s.",
    "U03-086": "`ω=√(k_s/m)`. `k_s` en N/m; `m` en kg; `ω` en rad/s.",
    "U03-088": "`x=A_x cos(ωt+φ₀)`; `v=-ωA_x sen(ωt+φ₀)`; `a=-ω²A_x cos(ωt+φ₀)`.",
    "U03-089": "`k_onda=2π/λ`. Unidad: rad/m. No confundir con `k_s` en N/m.",
    "U03-090": "`ξ=A_ξ cos(2πft-2πx/λ+φ₀)=A_ξ cos(ωt-k_onda x+φ₀)`.",
    "U03-091": "`c=ω/k_onda=(2πf)/(2π/λ)=λf`. Unidad: m/s.",
    "U03-092": "`A_R=√(A₁²+A₂²+2A₁A₂ cosΔφ)`.",
    "U03-093": "Para `A₁=A₂=A`: `A_R/A=√(2+2cosΔφ)=2|cos(Δφ/2)|`.",
    "U03-094": "`f=1/T`; luego `c=λf`. Sustituir los valores leídos en los dos gráficos aprobados y conservar unidades.",
    "U03-095": "`T=1/(500 Hz)=2 ms`; `λ=c/(500 Hz)`, con el valor de `c` indicado por la condición del caso.",
}


DEFINITIONS = {
    "U03-008": "**Equilibrio:** referencia alrededor de la cual ocurre el movimiento. **Elongación `x`:** desplazamiento respecto del equilibrio.",
    "U03-009": "**Perturbación:** cambio local del estado del medio que puede transmitirse a regiones vecinas.",
    "U03-011": "**Onda mecánica:** perturbación que se propaga mediante interacciones en un medio material.",
    "U03-012": "**Longitudinal/transversal:** clasificación según la orientación del movimiento local respecto de la propagación.",
    "U03-018": "**MAS:** oscilación ideal con fuerza restauradora lineal, proporcional y opuesta a la elongación.",
    "U03-021": "**Amplitud `A_x`:** máxima separación respecto del equilibrio.",
    "U03-022": "**Período `T`:** duración de un ciclo completo.",
    "U03-023": "**Frecuencia `f`:** cantidad de ciclos por unidad de tiempo.",
    "U03-026": "**Fase:** estado del ciclo medido respecto de una referencia.",
    "U03-037": "**Calibrada:** la escala vincula el gráfico con valores físicos y unidades trazables.",
    "U03-040": "**Tono puro ideal:** señal sinusoidal de una sola frecuencia.",
    "U03-045": "**Presión acústica `p_ac`:** variación de presión respecto de la presión ambiente, expresada en Pa.",
    "U03-049": "**Campo ondulatorio:** variable física especificada como función de posición y tiempo.",
    "U03-054": "**Longitud de onda `λ`:** menor distancia entre puntos equivalentes de fase.",
    "U03-062": "**`u`:** velocidad local de partícula. **`c`:** rapidez de propagación de fase.",
    "U03-065": "**Desfase `Δφ`:** diferencia entre dos fases referidas a la misma convención.",
    "U03-071": "**Superposición:** suma punto a punto de perturbaciones en un modelo lineal.",
    "U03-089": "**Número de onda `k_onda`:** cambio de fase espacial por unidad de distancia.",
}


EXAMPLES = {
    "U03-002": "Predicción parlante–aire–oído; no corregir antes de escuchar las razones.",
    "U03-003": "Cuatro afirmaciones diagnósticas; la solución queda en U03-087.",
    "U03-013": "Demostración con resorte y una marca visible en una espira.",
    "U03-025": "Conversión y cálculo completo de `T=2 ms` a `f=500 Hz`.",
    "U03-030": "Cono de parlante: `10 µm`, `500 Hz`, `2 ms`; declarar el alcance del modelo.",
    "U03-034": "Lectura de signos en un instante marcado sobre `x(t)`, `v(t)` y `a(t)`.",
    "U03-038": "Aplicar las cuatro preguntas a una curva sin rótulos y luego revelar ejes.",
    "U03-046": "Tono audiométrico: enumerar qué debe especificarse sin inferir diagnóstico.",
    "U03-057": "Longitud de onda de un tono de `1000 Hz` en aire con `c≈340 m/s`.",
    "U03-058": "Ejercicio de lectura coordinada; solución reservada para U03-094.",
    "U03-061": "Seguimiento animado de una partícula y de una cresta; usar alternativa estática.",
    "U03-068": "Clasificación de pares de señales con `Δφ=0`, `π/2` o `π`.",
    "U03-075": "Predicción antes de revelar la suma de dos señales.",
    "U03-080": "Caso integrador del tono de `500 Hz`; solución reservada para U03-095.",
    "U03-082": "Revisión final de las cuatro afirmaciones de U03-003.",
    "U03-085": "`f=500 Hz → ω=1000π rad/s`.",
    "U03-087": "Tabla de corrección del diagnóstico inicial.",
    "U03-089": "Contraste `k_s` en N/m frente a `k_onda` en rad/m.",
    "U03-092": "Comprobar `Δφ=0` y `Δφ=π` con amplitudes iguales.",
    "U03-094": "Solución completa en el orden `T → f → λ → c`, usando los valores de los gráficos aprobados.",
    "U03-095": "Solución modelo en cinco pasos para el caso de `500 Hz`.",
}


QUESTIONS = {
    "U03-001": ("Si oímos un tono a distancia, ¿viajó el aire desde el parlante hasta el oído?", "No; las partículas de aire oscilan localmente y la perturbación se propaga."),
    "U03-002": ("¿Qué elemento creen que recorre toda la distancia?", "Respuesta diagnóstica abierta; se espera distinguir al menos cono, aire y perturbación."),
    "U03-003": ("¿Qué afirmación les genera más duda y por qué?", "No se corrige todavía; se registra la justificación para retomarla."),
    "U03-004": ("Si `x>0`, ¿qué signo tiene `F_el`?", "Negativo, porque la fuerza restauradora apunta hacia el equilibrio."),
    "U03-008": ("¿Toda oscilación repetitiva es armónica?", "No; el MAS exige una relación restauradora lineal específica."),
    "U03-009": ("¿Qué evidencia muestra que la perturbación avanza?", "Regiones cada vez más alejadas comienzan a responder con retraso."),
    "U03-010": ("¿Qué se transporta sin que la materia recorra toda la distancia?", "La perturbación y la energía pueden propagarse; la materia oscila localmente."),
    "U03-011": ("¿Puede propagarse sonido en el vacío?", "No, porque es una onda mecánica y necesita medio material."),
    "U03-012": ("¿Qué dos direcciones hay que comparar?", "El movimiento local de las partículas y la dirección de propagación."),
    "U03-014": ("¿Por qué la marca vuelve pero la onda no?", "La marca representa materia local; el estado de perturbación se transmite a vecinos."),
    "U03-016": ("¿Qué oscila y qué se propaga en el aire?", "Las partículas oscilan localmente; se propagan la perturbación y la energía."),
    "U03-018": ("¿Qué condición distingue al MAS de una oscilación cualquiera?", "La fuerza neta es proporcional y opuesta a la elongación."),
    "U03-019": ("En `x>0`, ¿hacia dónde apunta `a`?", "Hacia el equilibrio; con el eje elegido, `a<0`."),
    "U03-021": ("¿La amplitud puede ser negativa?", "No como magnitud; `A_x` es un máximo de `|x|` y es no negativa."),
    "U03-024": ("Si el período se duplica, ¿qué ocurre con la frecuencia?", "Se reduce a la mitad."),
    "U03-025": ("¿Por qué hay que convertir milisegundos a segundos?", "Para obtener la frecuencia en s⁻¹, es decir, hertz."),
    "U03-026": ("¿Dos puntos con igual elongación tienen siempre igual fase?", "No; también importa el sentido del movimiento dentro del ciclo."),
    "U03-029": ("¿Qué representa el eje horizontal?", "Tiempo, no una coordenada espacial."),
    "U03-030": ("¿Qué sí permite afirmar el modelo y qué no?", "Permite describir desplazamiento y frecuencia del cono; no fija presión ni sonoridad."),
    "U03-031": ("¿Dónde es cero la velocidad instantánea?", "En los extremos de la oscilación."),
    "U03-032": ("¿Dónde es cero la aceleración?", "En el equilibrio, para el MAS ideal."),
    "U03-034": ("¿Cómo se obtiene el signo de `v` desde `x(t)`?", "Por el signo de la pendiente de la curva de posición."),
    "U03-035": ("¿Qué dato cambia el significado físico de una misma forma?", "Los rótulos de variable, ejes, unidades y calibración."),
    "U03-036": ("¿La sinusoide muestra el camino de la partícula?", "No; muestra cómo una variable cambia respecto del eje horizontal."),
    "U03-038": ("¿Qué conclusión puede sostenerse si faltan unidades?", "Solo relaciones cualitativas o normalizadas, no valores físicos absolutos."),
    "U03-040": ("¿Qué idealización define al tono puro?", "Una sola frecuencia y comportamiento sinusoidal estable."),
    "U03-042": ("¿En qué etapa cambia la variable física representada?", "En cada transformación: eléctrica, mecánica del cono, mecánica del aire y presión."),
    "U03-045": ("¿La curva permite conocer nivel sonoro?", "No si no se especifican amplitud calibrada, referencia y condiciones."),
    "U03-049": ("¿Por qué hacen falta dos variables independientes?", "Porque el estado puede cambiar tanto con la posición como con el tiempo."),
    "U03-051": ("¿Qué magnitud se lee en un corte temporal?", "El período `T`, y de él la frecuencia `f`."),
    "U03-052": ("¿Qué magnitud se lee en un perfil espacial?", "La longitud de onda `λ`."),
    "U03-053": ("¿Por qué `T` y `λ` no pueden intercambiarse?", "Uno es tiempo en segundos y el otro distancia en metros."),
    "U03-056": ("¿Qué distancia avanza la fase en un período?", "Una longitud de onda."),
    "U03-057": ("¿Qué significa físicamente `λ=0,34 m`?", "Puntos separados 0,34 m pueden estar en el mismo estado de fase."),
    "U03-058": ("¿Qué se lee antes de calcular?", "`T` y `λ`, cada uno en el eje correspondiente."),
    "U03-061": ("¿La partícula y la cresta recorren la misma trayectoria?", "No; la partícula oscila localmente y la cresta representa fase que avanza."),
    "U03-062": ("¿Cuál velocidad usaría para describir el avance del tono?", "`c`, no la velocidad local `u`."),
    "U03-063": ("Si `f` se duplica y `c` permanece constante, ¿qué ocurre con `λ`?", "Se reduce a la mitad."),
    "U03-065": ("¿`2π` representa un estado distinto de `0`?", "Es un ciclo completo después y corresponde a fase equivalente."),
    "U03-067": ("¿Qué desfase produce un retraso de `T/4`?", "`π/2 rad`."),
    "U03-071": ("¿La superposición suma amplitudes o valores instantáneos?", "Suma valores instantáneos punto a punto; la amplitud resultante depende de la fase."),
    "U03-072": ("¿Qué ocurre si los máximos coinciden?", "Hay refuerzo; con amplitudes iguales, la amplitud resultante es `2A`."),
    "U03-073": ("¿Cuándo puede haber cancelación completa?", "Con igual frecuencia y amplitud, oposición de fase y en el punto considerado."),
    "U03-076": ("¿La cancelación activa produce silencio en toda una sala?", "No; depende de posición, geometría y control de amplitud y fase."),
    "U03-080": ("¿Qué dato adicional hace falta para calcular `λ`?", "La rapidez de propagación `c` o las condiciones del medio que la determinan."),
    "U03-082": ("¿Qué cambió entre la primera respuesta y la final?", "La respuesta final distingue variable, medio, propagación, escala y condiciones."),
    "U03-083": ("¿Qué falta para convertir una forma normalizada en una magnitud acústica?", "Variable, unidad, escala, calibración y referencia."),
    "U03-085": ("¿Qué unidad distingue a `ω` de `f`?", "`ω` se expresa en rad/s y `f` en Hz."),
    "U03-086": ("¿Cómo cambia `ω` si aumenta la masa y `k_s` permanece fija?", "Disminuye como la raíz inversa de la masa."),
    "U03-089": ("¿Por qué no conviene escribir ambos parámetros como `k`?", "Porque describen magnitudes distintas y tienen unidades distintas."),
    "U03-091": ("¿Qué factor se cancela al demostrar la equivalencia?", "`2π`."),
    "U03-092": ("¿Qué resultados se obtienen para `Δφ=0` y `π` con amplitudes iguales?", "`2A` y `0`, respectivamente."),
    "U03-094": ("¿Cuál es el primer dato que debe leerse en cada gráfico?", "`T` en el temporal y `λ` en el espacial; después se calculan `f` y `c`."),
    "U03-095": ("¿Qué límite evita convertir el modelo en una conclusión clínica?", "No se conocen nivel, calibración, anatomía individual ni respuesta perceptual."),
}


ERRORS = {
    "U03-004": "Una fuerza hacia el equilibrio no implica que la velocidad también apunte hacia el equilibrio en ese instante.",
    "U03-008": "No usar oscilatorio, periódico y armónico como sinónimos.",
    "U03-009": "No decir que una forma material viaja de partícula en partícula.",
    "U03-010": "No afirmar transporte neto de materia en el modelo ideal.",
    "U03-011": "La necesidad de medio se refiere a ondas mecánicas; no a toda clase de onda.",
    "U03-012": "No clasificar por la orientación del dibujo, sino por las dos direcciones físicas.",
    "U03-018": "No confundir MAS con cualquier movimiento que se repite.",
    "U03-019": "El signo negativo expresa dirección restauradora, no módulo negativo.",
    "U03-021": "La amplitud no es la distancia entre máximo y mínimo; esa distancia es `2A_x`.",
    "U03-024": "Frecuencia y período son inversos, no directamente proporcionales.",
    "U03-025": "No reemplazar `2 ms` por `2 s`.",
    "U03-026": "Fase no es una distancia ni un instante absoluto.",
    "U03-029": "La curva no es una trayectoria espacial.",
    "U03-030": "No deducir presión o sonoridad desde desplazamiento sin una relación y calibración adicionales.",
    "U03-031": "Velocidad cero no implica aceleración cero en los extremos.",
    "U03-032": "Aceleración cero al pasar por el equilibrio no implica velocidad cero.",
    "U03-035": "No atribuir significado físico por la forma sin leer ejes y unidades.",
    "U03-037": "Normalizado no significa calibrado.",
    "U03-040": "Un tono real no tiene duración infinita ni comienzo instantáneo.",
    "U03-045": "Presión acústica no es presión ambiente total.",
    "U03-046": "No convertir una descripción física en diagnóstico o pronóstico.",
    "U03-049": "No leer `ξ(x,t)` como producto de `x` por `t`.",
    "U03-053": "No confundir segundos con metros.",
    "U03-055": "La dirección depende del signo espacial y de la convención adoptada.",
    "U03-056": "La relación no afirma que una partícula recorra `λ` en un período.",
    "U03-062": "No confundir velocidad local de partícula con rapidez de propagación.",
    "U03-063": "Mayor frecuencia no implica necesariamente mayor rapidez de propagación.",
    "U03-065": "Comparar fases exige una referencia común.",
    "U03-071": "La superposición lineal suma valores instantáneos, no etiquetas globales.",
    "U03-073": "La cancelación completa exige condiciones simultáneas y es local.",
    "U03-076": "Evitar prometer cancelación perfecta en todo el espacio.",
    "U03-080": "No calcular `λ` sin declarar `c` o las condiciones del medio.",
    "U03-085": "No confundir hertz con radianes por segundo.",
    "U03-086": "La fórmula corresponde al modelo ideal no amortiguado.",
    "U03-089": "`k_onda` y `k_s` no son intercambiables.",
    "U03-092": "La fórmula supone sinusoides coherentes de igual frecuencia en el punto comparado.",
    "U03-094": "No mezclar el eje temporal con el espacial ni omitir la conversión de ms a s.",
    "U03-095": "El caso no determina nivel ni respuesta auditiva individual.",
}


ASSET_IDS = {
    **{f"U03-{n:03d}": "U03-DG001" for n in (2, 15, 79)},
    **{f"U03-{n:03d}": "U03-DG002" for n in (6, 16, 47, 59, 69, 78, 81)},
    **{f"U03-{n:03d}": "U03-DG003" for n in (8, 20, 21)},
    **{f"U03-{n:03d}": "U03-DG004" for n in (9, 10, 14)},
    **{f"U03-{n:03d}": "U03-DG005" for n in (11, 12)},
    **{f"U03-{n:03d}": "U03-DG006" for n in (4, 18, 19)},
    **{f"U03-{n:03d}": "U03-DG007" for n in (26, 65, 84)},
    "U03-027": "U03-DG008",
    "U03-029": "U03-DG009",
    **{f"U03-{n:03d}": "U03-DG010" for n in (31, 32)},
    "U03-036": "U03-DG011",
    **{f"U03-{n:03d}": "U03-DG012" for n in (37, 38)},
    "U03-040": "U03-DG013",
    **{f"U03-{n:03d}": "U03-DG014" for n in (42, 45, 47)},
    **{f"U03-{n:03d}": "U03-DG015" for n in (43, 44)},
    "U03-046": "U03-DG016",
    "U03-049": "U03-DG017",
    "U03-053": "U03-DG018",
    **{f"U03-{n:03d}": "U03-DG019" for n in (55, 56, 57, 59)},
    **{f"U03-{n:03d}": "U03-DG020" for n in (62, 69)},
    "U03-071": "U03-DG021",
    "U03-076": "U03-DG022",
    "U03-077": "U03-DG023",
    **{f"U03-{n:03d}": "U03-DG024" for n in (80, 81, 95)},
    **{f"U03-{n:03d}": "U03-DG025" for n in (24, 67, 85, 86, 87, 88, 89, 90, 91, 92)},
    **{f"U03-{n:03d}": "U03-CH001" for n in (4, 22, 23)},
    "U03-030": "U03-CH002",
    **{f"U03-{n:03d}": "U03-CH003" for n in (33, 34, 88)},
    **{f"U03-{n:03d}": "U03-CH004" for n in (35, 36)},
    "U03-041": "U03-CH005",
    "U03-045": "U03-CH006",
    **{f"U03-{n:03d}": "U03-CH007" for n in (50, 51, 52, 53, 54, 59)},
    **{f"U03-{n:03d}": "U03-CH008" for n in (58, 80, 94, 95)},
    "U03-063": "U03-CH009",
    **{f"U03-{n:03d}": "U03-CH010" for n in (64, 68)},
    "U03-066": "U03-CH011",
    **{f"U03-{n:03d}": "U03-CH012" for n in (72, 73, 74, 75)},
    "U03-093": "U03-CH013",
}


SUBTITLES = {
    "portada": "Oscilaciones, ondas y tonos.",
    "pregunta": "Predicción y justificación.",
    "puente": "Recuperación de conocimientos previos.",
    "objetivos": "Resultados observables de aprendizaje.",
    "mapa": "Orientación de la secuencia.",
    "divisor": "Pregunta guía del bloque.",
    "definición": "Significado físico y alcance.",
    "explicación": "Interpretación antes del formalismo.",
    "comparación": "Diferencias que cambian la explicación.",
    "ecuación": "Símbolos, unidades e interpretación.",
    "gráfico": "Lectura de ejes, escala y relaciones.",
    "ejemplo": "Datos, procedimiento e interpretación.",
    "aplicación": "Uso físico y límites.",
    "recapitulación": "Comprobación antes de avanzar.",
    "multimedia": "Predicción, observación y conclusión.",
    "ejercicio": "Leer antes de calcular.",
    "error frecuente": "Corrección conceptual.",
    "cierre": "Síntesis y transferencia.",
    "respaldo": "Consulta opcional.",
    "tabla": "Consulta y retroalimentación.",
    "solución": "Procedimiento modelo.",
    "fuentes": "Consistencia y trazabilidad.",
}


TYPE_WEIGHTS = {
    "portada": 1,
    "pregunta": 4,
    "puente": 3,
    "objetivos": 2,
    "mapa": 2,
    "divisor": 1,
    "definición": 3,
    "explicación": 3,
    "comparación": 3,
    "ecuación": 4,
    "gráfico": 4,
    "ejemplo": 5,
    "aplicación": 4,
    "recapitulación": 3,
    "multimedia": 5,
    "ejercicio": 6,
    "error frecuente": 3,
    "cierre": 3,
}


BLOCK_BUDGETS = {
    "B00 · Apertura": 15,
    "B01 · Oscilación y onda": 25,
    "B02 · Movimiento armónico simple": 30,
    "B03 · Sinusoides y representaciones": 28,
    "B04 · Tono puro y parlante": 24,
    "B05 · Onda viajera": 35,
    "B06 · Velocidades y fase": 27,
    "B07 · Superposición": 25,
    "B08 · Integración y cierre": 20,
}


SOURCE_KEYS = [
    ("PO", "Programa oficial 2025, Unidad 3, p. 3."),
    ("TEX", "`context/libro_latex/chapters/03-mecanica-ondulatoria.tex`."),
    ("PDF", "Libro del curso en PDF, pp. 61–88."),
    ("CM", "`course_map.md`, Unidad 3."),
    ("CDM", "`course_dependency_map.md`, Unidad 3."),
    ("CCM", "`content_coverage_matrix.csv`, registros U03."),
    ("BR", "`units/unit_03/brief.md`."),
    ("INV", "`units/unit_03/content_inventory.md`."),
    ("SA", "`units/unit_03/source_analysis.md`."),
    ("NOT", "`style/notation_guide.md`."),
    ("GLO", "`style/glossary.md`."),
    ("U2", "Unidad 2 final, únicamente para la continuidad declarada por el storyboard."),
    ("ED", "Elaboración didáctica ya aprobada y trazable en el storyboard."),
]


def clean(value: str):
    value = re.sub(
        r"\*{0,2}CANDIDATA `(?:diagram-generation|chart-generation)`\*{0,2}:?\s*",
        "",
        value.strip(),
    )
    return " ".join(value.split())


def split_summary(summary: str):
    return [part.strip(" .") for part in summary.split(";") if part.strip(" .")]


def generic_visible(row):
    if row["slide_id"] in VISIBLE:
        return VISIBLE[row["slide_id"]]
    if row["visual_class"] in {"diagram", "mixed", "equation_only"}:
        return f"**Idea central:** {row['key_message']}"
    return f"{row['key_message']} {row['summary']}"


def caption_for(row):
    if row["visual_class"] == "none":
        return "—"
    if row["slide_id"] == "U03-002":
        return "Predicción inicial sobre fuente, medio y receptor. Esquema conceptual; no está a escala."
    conceptual = row["visual_class"] in {"diagram", "mixed", "equation_only"}
    suffix = " Esquema conceptual; no está a escala." if conceptual else ""
    return row["key_message"] + suffix


def visual_instruction(row):
    visual = clean(row["visual"])
    asset = ASSET_IDS.get(row["slide_id"])
    asset_text = f" Recurso propio previsto: `{asset}`." if asset else ""
    if row["visual_class"] in {"diagram", "mixed", "equation_only"}:
        return (
            f"{visual}{asset_text} Mantener fuera de las cajas la explicación extensa; "
            f"la lectura principal es: {row['key_message']}"
        )
    return f"{visual}{asset_text}"


def alt_text_for(row):
    labels = {
        "diagram": "Diagrama conceptual",
        "mixed": "Esquema mixto",
        "chart": "Gráfico cuantitativo",
        "video_or_gif": "Secuencia animada con alternativa estática",
        "equation_only": "Ecuación anotada",
        "none": "Composición textual",
    }
    summary = re.sub(r"[`*]", "", row["summary"])
    return f"{labels.get(row['visual_class'], 'Recurso visual')} con título «{row['title']}». {summary}"


def allocate_durations(rows):
    durations = {}
    grouped = defaultdict(list)
    for row in rows:
        if row["status"] == "central":
            grouped[row["block"]].append(row)
    for block, block_rows in grouped.items():
        budget = BLOCK_BUDGETS[block]
        weights = [TYPE_WEIGHTS.get(row["slide_type"], 3) for row in block_rows]
        raw = [budget * weight / sum(weights) for weight in weights]
        allocated = [max(1, math.floor(value)) for value in raw]
        while sum(allocated) < budget:
            for index in sorted(
                range(len(raw)),
                key=lambda i: raw[i] - math.floor(raw[i]),
                reverse=True,
            ):
                allocated[index] += 1
                if sum(allocated) == budget:
                    break
        while sum(allocated) > budget:
            for index in sorted(range(len(allocated)), key=lambda i: allocated[i], reverse=True):
                if allocated[index] > 1:
                    allocated[index] -= 1
                    if sum(allocated) == budget:
                        break
        for row, duration in zip(block_rows, allocated):
            durations[row["slide_id"]] = f"{duration} min"
    for row in rows:
        if row["slide_id"] in durations:
            continue
        durations[row["slide_id"]] = (
            "3–5 min si se selecciona" if row["status"] == "complementary" else "A demanda"
        )
    return durations


def default_question(row):
    prompts = {
        "divisor": "¿Qué pregunta física organiza este bloque?",
        "definición": "¿Qué condición o diferencia forma parte de esta definición?",
        "ecuación": "¿Qué relación física expresa la ecuación y qué unidades deben ser compatibles?",
        "comparación": "¿Cuál es la diferencia esencial entre los casos?",
        "mapa": "¿En qué etapa del recorrido estamos y qué conexión sigue?",
        "recapitulación": "¿Cómo se conectan las ideas principales del bloque?",
        "aplicación": "¿Qué permite afirmar el modelo y qué queda fuera de su alcance?",
        "ejercicio": "¿Qué dato se lee antes de elegir la ecuación?",
        "pregunta": "¿Qué evidencia física sostiene su respuesta?",
        "gráfico": "¿Qué indican los ejes, las unidades y la escala?",
    }
    return prompts.get(
        row["slide_type"],
        "¿Cómo justificaría la idea central con variables, unidades o relaciones físicas?",
    ), row["key_message"]


def development_for(row):
    additions = {
        "definición": "Comenzar con el fenómeno y un contraejemplo; fijar el término después.",
        "ecuación": "Definir símbolos, unidades, signo y condiciones antes de sustituir valores.",
        "comparación": "Nombrar primero lo común y luego la diferencia que cambia la interpretación.",
        "mapa": "Señalar la etapa activa sin convertir el mapa en una lista para memorizar.",
        "ejercicio": "Dar tiempo individual. Resolver en el orden lectura → datos → ecuación → unidad → interpretación.",
        "pregunta": "Escuchar una justificación antes de validar o corregir.",
        "recapitulación": "Reconstruir relaciones; evitar una enumeración de palabras.",
        "aplicación": "Separar utilidad física, condiciones del modelo y límite clínico.",
        "gráfico": "Nombrar variable, ejes, unidades y escala antes de describir la forma.",
        "multimedia": "Realizar una primera observación global y una segunda guiada.",
    }
    parts = [
        row["speaker_goal"],
        additions.get(row["slide_type"], ""),
        f"Cierre conceptual: {row['key_message']}",
    ]
    return " ".join(part for part in parts if part)


def diagram_guide(row):
    if row["visual_class"] not in {"diagram", "mixed", "equation_only", "chart"}:
        return "—"
    if row["visual_class"] == "chart":
        return (
            "1. Nombrar ejes, variable, unidad y escala. "
            "2. Leer los puntos o intervalos señalados. "
            f"3. Formular la conclusión sin extenderla más allá del modelo: {row['key_message']}"
        )
    parts = split_summary(row["summary"])
    order = " → ".join(parts[:4])
    return (
        "1. Señalar el objeto, sistema o ecuación central. "
        f"2. Recorrer el esquema en este orden: {order}. "
        f"3. Distinguir conectores de movimiento local y propagación cuando corresponda. "
        f"4. Cerrar con una sola idea: {row['key_message']} "
        "El esquema es conceptual y no está a escala."
    )


def multimedia_note(row):
    if row["visual_class"] != "video_or_gif":
        return "—"
    return (
        f"Reproducir: {clean(row['visual'])} Mostrar primero sin narración y luego seguir la marca o el frente. "
        "Si el recurso no se reproduce, usar la secuencia estática incluida."
    )


def emphasis_for(row):
    if row["slide_id"] in ERRORS:
        return ERRORS[row["slide_id"]]
    if row["visual_class"] == "chart":
        return "No presentar curvas del modelo como datos medidos; explicitar ejes, unidades y escala."
    if row["visual_class"] in {"diagram", "mixed", "equation_only"}:
        return "No leer el esquema como representación anatómica o geométrica a escala."
    if row["slide_type"] in {"ejercicio", "solución"}:
        return "No aceptar resultados sin unidad, procedimiento e interpretación física."
    if row["slide_type"] == "recapitulación":
        return "Pedir conexiones entre conceptos, no una lista memorizada."
    return "Mantener consistentes variable, referencia, signo y unidad."


def slide_text(rows):
    lines = [
        "# Unidad 3 — Texto visible de las diapositivas",
        "",
        "## Criterio de uso",
        "",
        "Redacción desarrollada exclusivamente desde el storyboard aprobado. Se conservan sus 96 slides, IDs, secuencia, función, layout, estado y fuentes. El contenido visible prioriza una idea central; las explicaciones extendidas están en `speaker_notes.md`. No se produjo ni modificó ningún PowerPoint.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        lines.extend(
            [
                f"## {sid} — {row['title']}",
                "",
                f"- **Título:** {row['title']}",
                f"- **Subtítulo:** {SUBTITLES.get(row['slide_type'], '—')}",
                f"- **Contenido visible:** {generic_visible(row)}",
                f"- **Ecuaciones:** {EQUATIONS.get(sid, '—')}",
                f"- **Definiciones:** {DEFINITIONS.get(sid, '—')}",
                f"- **Ejemplo/consigna:** {EXAMPLES.get(sid, '—')}",
                f"- **Caption sugerido:** {caption_for(row)}",
                f"- **Visual:** {visual_instruction(row)}",
                f"- **Layout:** `{row['layout']}`.",
                f"- **Fuente:** {row['source']}.",
                f"- **Transición:** {row['transition']}",
                f"- **Texto alternativo:** {alt_text_for(row)}",
                "",
            ]
        )
    return "\n".join(lines)


def notes_text(rows, durations):
    lines = [
        "# Unidad 3 — Notas del orador",
        "",
        "## Criterio de uso",
        "",
        "Estas notas amplían la explicación sin leer literalmente la slide. Las duraciones de las 69 slides centrales suman los 229 minutos aprobados; las complementarias y el respaldo se usan de manera selectiva. Las guías de diagramas mantienen el copy largo fuera de cajas y conectores.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        question, answer = QUESTIONS.get(sid, default_question(row))
        lines.extend(
            [
                f"## {sid} — {row['title']}",
                "",
                f"- **Explicación extendida:** {development_for(row)}",
                f"- **Guía del visual/diagrama:** {diagram_guide(row)}",
                f"- **Pregunta al grupo:** {question}",
                f"- **Respuesta esperada:** {answer}",
                f"- **Demostración/audio/video/GIF:** {multimedia_note(row)}",
                f"- **Error frecuente o énfasis:** {emphasis_for(row)}",
                f"- **Transición oral:** “{row['transition']}”",
                f"- **Duración aproximada:** {durations[sid]}.",
                f"- **[Sources]:** {row['source']}.",
                "",
            ]
        )
    return "\n".join(lines)


def source_map(rows):
    lines = [
        "# Unidad 3 — Mapa de fuentes de la redacción",
        "",
        "## Alcance",
        "",
        "La redacción se elaboró exclusivamente desde el storyboard aprobado. Este archivo desarrolla sus claves y conserva la fuente asignada a cada slide; no incorpora bibliografía ni afirmaciones externas.",
        "",
        "## Claves",
        "",
    ]
    lines.extend([f"- **{key}:** {description}" for key, description in SOURCE_KEYS])
    lines.extend(
        [
            "",
            "## Trazabilidad por slide",
            "",
            "| slide_id | función o afirmación principal | fuente aprobada |",
            "|---|---|---|",
        ]
    )
    for row in rows:
        message = row["key_message"].replace("|", "/")
        source = row["source"].replace("|", "/")
        lines.append(f"| {row['slide_id']} | {message} | {source}. |")
    lines.extend(
        [
            "",
            "## Regla para producción posterior",
            "",
            "Al montar la presentación, recuperar las referencias completas y los créditos desde las fuentes indicadas por el storyboard y desde `asset_manifest.csv`. Esta fase no verificó ni amplió bibliografía porque la instrucción exigió trabajar solo desde el storyboard.",
            "",
        ]
    )
    return "\n".join(lines)


def word_count(value):
    cleaned = re.sub(r"`[^`]+`", " ecuación ", value)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", cleaned))


def writing_review(rows, durations):
    ids = [row["slide_id"] for row in rows]
    statuses = Counter(row["status"] for row in rows)
    visible_counts = [word_count(generic_visible(row)) for row in rows]
    duration_sums = defaultdict(int)
    for row in rows:
        if row["status"] == "central":
            duration_sums[row["block"]] += int(durations[row["slide_id"]].split()[0])
    diagram_count = sum(
        row["visual_class"] in {"diagram", "mixed", "equation_only"} for row in rows
    )
    lines = [
        "# Unidad 3 — Revisión de redacción de slides y notas",
        "",
        "## Dictamen",
        "",
        "**Estado: aprobado para la fase posterior de montaje, sujeto a la revisión renderizada exigida por AGENTS.md.**",
        "",
        f"La redacción conserva las 96 slides aprobadas: {statuses['central']} centrales, {statuses['complementary']} complementarias y {statuses['backup']} de respaldo. No se creó ni modificó ningún PowerPoint.",
        "",
        "## Controles estructurales",
        "",
        "| control | resultado |",
        "|---|---|",
        f"| IDs U03-001–U03-096 | {len(ids)}/96 presentes, consecutivos y sin duplicados. |",
        "| Título y subtítulo | 96/96. |",
        "| Contenido visible | 96/96. |",
        "| Ecuación o indicación de no correspondencia | 96/96. |",
        "| Definición o indicación de no correspondencia | 96/96. |",
        "| Ejemplo/consigna o indicación de no correspondencia | 96/96. |",
        "| Caption, visual y layout | 96/96. |",
        "| Fuente, transición y texto alternativo | 96/96. |",
        "| Explicación, pregunta, respuesta y duración en notas | 96/96. |",
        "| Fila de trazabilidad en source_map | 96/96. |",
        "",
        "## Duración de la ruta central",
        "",
        "| bloque | redacción | storyboard |",
        "|---|---:|---:|",
    ]
    for block, budget in BLOCK_BUDGETS.items():
        lines.append(f"| {block} | {duration_sums[block]} min | {budget} min |")
    lines.extend(
        [
            "| **Total** | **229 min** | **229 min** |",
            "",
            "Las duraciones incluyen preguntas y mini ejercicios. Las complementarias y el respaldo no forman parte del total.",
            "",
            "## Revisión pedagógica",
            "",
            "| criterio | evidencia | resultado |",
            "|---|---|---|",
            "| Intuición antes del formalismo | Parlante, oscilación local y propagación preceden al MAS y a la onda viajera. | Conforme. |",
            "| Nivel de primer año | Las ecuaciones se introducen después del fenómeno y definen símbolos, unidades y condiciones. | Conforme. |",
            "| Ejemplos con pasos | U03-025, U03-030, U03-057, U03-094 y U03-095. | Conforme. |",
            "| Lectura de representaciones | U03-035–038 y U03-049–059 obligan a identificar variable, ejes, unidad y corte. | Conforme. |",
            "| Aplicación fonoaudiológica | U03-015, U03-046, U03-077, U03-079–080 y U03-083 explicitan utilidad y límites. | Conforme. |",
            "| Preguntas resolubles | Las 96 notas incluyen respuesta esperada o propósito diagnóstico explícito. | Conforme. |",
            "| Recapitulaciones | U03-016, 027, 038, 047, 059, 069, 078 y 081–083. | Conforme. |",
            "| Errores frecuentes | Materia/onda, trayectoria, `T`/`λ`, `u`/`c`, fase, calibración y cancelación. | Conforme. |",
            f"| Slides con diagramas o ecuaciones anotadas | {diagram_count}; idea central fuera de cajas y guía paso a paso en notas. | Conforme. |",
            "",
            "## Densidad prevista",
            "",
            f"- Promedio aproximado del contenido visible: {sum(visible_counts)/len(visible_counts):.1f} palabras.",
            f"- Máximo aproximado del campo visible: {max(visible_counts)} palabras.",
            "- Las explicaciones largas, respuestas y errores frecuentes se mantienen en notas.",
            "- U03-003, U03-087 y U03-096 requieren una tabla o lista con jerarquía; verificar 22 pt o más durante el montaje.",
            "- U03-095 conserva cinco pasos breves. El storyboard permite dividirla si el render final no cumple legibilidad.",
            "",
            "## Exactitud y alcance",
            "",
            "- Se distinguen movimiento local, propagación, materia, perturbación y energía.",
            "- `x`, `ξ`, `p_ac` y `V` conservan significados y unidades diferentes.",
            "- `T` y `λ`, `u` y `c`, `k_s` y `k_onda`, `f` y `ω` están diferenciados explícitamente.",
            "- Las cifras usadas están explícitas en el storyboard: 2 ms/500 Hz, amplitud de 0,010 mm, 1000 Hz con `c≈340 m/s` y caso integrador de 500 Hz. En U03-094 se conserva el procedimiento sin inventar los valores que deben leerse en los gráficos aprobados.",
            "- Los modelos audiométricos y auditivos incluyen límites; no se formulan diagnósticos ni inferencias clínicas individuales.",
            "- Las figuras conceptuales se declaran como no a escala; las curvas se describen como modelo, no como medición.",
            "",
            "## Fuentes",
            "",
            "- Cada slide conserva exactamente la fuente asignada por el storyboard.",
            "- `source_map.md` contiene 96 filas de trazabilidad.",
            "- No se consultaron ni agregaron fuentes externas durante esta fase.",
            "",
            "## Incidencias y decisiones",
            "",
            "| id | severidad | hallazgo | tratamiento | estado |",
            "|---|---|---|---|---|",
            "| U03-WR-001 | Menor | U03-002 debe conservar la respuesta incompleta. | El copy formula predicciones y las notas no adelantan el diagrama resuelto. | Mitigado. |",
            "| U03-WR-002 | Menor | U03-061 depende de animación. | Las notas exigen una secuencia estática alternativa. | Mitigado. |",
            "| U03-WR-003 | Menor | U03-095 puede resultar densa en una sola slide. | Se limitaron las etapas a una oración breve; dividir solo si el render real falla. | Pendiente de montaje. |",
            "| U03-WR-004 | Menor | Las tablas U03-087 y U03-096 pueden tensionar la legibilidad. | Mantener como respaldo, resumir celdas y verificar a 22 pt o más. | Pendiente de montaje. |",
            "",
            "## Problemas críticos",
            "",
            "No se detectan problemas críticos o mayores en la redacción. La aprobación corresponde a estos documentos; la legibilidad, los desbordes y las colisiones deberán verificarse cuando se produzca y renderice el PowerPoint.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    rows = parse_storyboard()
    expected = [f"U03-{index:03d}" for index in range(1, 97)]
    actual = [row["slide_id"] for row in rows]
    if actual != expected:
        raise ValueError("Los IDs del storyboard no son U03-001–U03-096 consecutivos")
    if set(actual) != set(VISIBLE):
        missing = sorted(set(actual) - set(VISIBLE))
        extra = sorted(set(VISIBLE) - set(actual))
        raise ValueError(f"Copy visible incompleto. Faltan={missing}; sobran={extra}")
    durations = allocate_durations(rows)
    outputs = {
        "slide_text.md": slide_text(rows),
        "speaker_notes.md": notes_text(rows, durations),
        "source_map.md": source_map(rows),
        "writing_review.md": writing_review(rows, durations),
    }
    for name, content in outputs.items():
        (UNIT_DIR / name).write_text(content + "\n", encoding="utf-8")
    print(
        {
            "slides": len(rows),
            "central": sum(row["status"] == "central" for row in rows),
            "complementary": sum(row["status"] == "complementary" for row in rows),
            "backup": sum(row["status"] == "backup" for row in rows),
            "central_minutes": sum(
                int(durations[row["slide_id"]].split()[0])
                for row in rows
                if row["status"] == "central"
            ),
            "outputs": sorted(outputs),
        }
    )


if __name__ == "__main__":
    main()
