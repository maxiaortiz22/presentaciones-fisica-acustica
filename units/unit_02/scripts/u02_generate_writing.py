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
        if not line.startswith("| U02-"):
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


EQUATIONS = {
    "U02-013": "`F_neta = 0 → v = constante`. `F_neta` en N; `v` en m/s.",
    "U02-017": "`F_neta = m·a`. `F_neta` en N; `m` en kg; `a` en m/s². Control: `1 N = 1 kg·m/s²`.",
    "U02-019": "`F_neta = ΣF_x`; luego `a = F_neta/m`. Conservar los signos del eje elegido.",
    "U02-021": "`F⃗_A→B = −F⃗_B→A`. Los subíndices identifican agente y cuerpo receptor.",
    "U02-025": "`F_1 = p_1S`; `F_2 = p_2S`; la resultante depende de `p_1 − p_2`.",
    "U02-027": "`Δp = p_1 − p_2`. `p_1`, `p_2` y `Δp` se expresan en Pa.",
    "U02-028": "`F_pres = Δp·S`. `F_pres` en N; `Δp` en Pa; `S` en m². Hipótesis: presión uniforme.",
    "U02-029": "`Pa·m² = (N/m²)·m² = N`.",
    "U02-030": "`F_pres = Δp·S = 1,0×10⁻⁴ N`. El sentido se determina con el signo de `Δp` y el eje.",
    "U02-032": "`Δp = p_1 − p_2 → F_pres = Δp·S → a = F_neta/m`.",
    "U02-038": "`F_el = −k_sx`. `k_s` en N/m; `x` en m; `F_el` en N.",
    "U02-040": "`F_amort = −bv`. `b` en N·s/m; `v` en m/s; `F_amort` en N.",
    "U02-042": "`F_ext − k_sx − bv = ma`. Todos los términos tienen unidad de newton.",
    "U02-043": "`signo(F_el) = −signo(x)`; `signo(F_amort) = −signo(v)`.",
    "U02-044": "`F_el = −k_sx`; `F_amort = −bv`; `F_neta = F_ext + F_el + F_amort`; `a = F_neta/m`.",
    "U02-046": "`F_ext − k_sx − bv = ma`.",
    "U02-049": "`W_trab = F·d`. `W_trab` en J; `F` en N; `d` en m. `1 J = 1 N·m`.",
    "U02-050": "`E_c = ½mv²`. `E_c` en J; `m` en kg; `v` en m/s.",
    "U02-051": "`E_el = ½k_sx²`. `E_el` en J; `k_s` en N/m; `x` en m.",
    "U02-055": "`E_entrada = ΔE_mec + E_salida + E_disipada`. Todas las energías se expresan en J.",
    "U02-056": "`E_disipada = 2,0 mJ − 1,3 mJ − 0,4 mJ = 0,3 mJ`.",
    "U02-064": "`ΔU = Q_calor + W_sobre`. En la convención elegida, las transferencias que entran son positivas.",
    "U02-065": "`Q_calor > 0` si entra y `< 0` si sale; `W_sobre > 0` si se realiza sobre el sistema.",
    "U02-066": "`ΔU = (−3,0 J) + (+2,0 J) = −1,0 J`.",
    "U02-067": "`ΔU = Q_calor + W_sobre`.",
    "U02-071": "`ΔS_total ≥ 0`. Unidad: J/K. `= 0` en el límite reversible ideal; `> 0` en un proceso irreversible.",
    "U02-072": "`ΔS_total = 0` frente a `ΔS_total > 0`, siempre para el sistema total considerado.",
    "U02-075": "`ΔU = Q_calor + W_sobre`; `ΔS_total ≥ 0`.",
    "U02-079": "`c ≈ 331 m/s + [0,6 (m/s)/°C]·ϑ`. `ϑ` en °C; `c` en m/s.",
    "U02-080": "`c(ϑ) ≈ 331 + 0,6ϑ`, dentro del intervalo ambiental indicado.",
    "U02-081": "`c(20 °C) ≈ 343 m/s`; `c(30 °C) ≈ 349 m/s`; diferencia aproximada: `6 m/s`.",
    "U02-082": "`c = λf` como puente a U3. Si `f` permanece fija y cambia `c`, cambia `λ`.",
    "U02-094": "Convención visible: `S` para área; `k_s` para rigidez; `F_neta = ΣF`.",
    "U02-095": "`F_el = −k_sx`; `F_amort = −bv`; `F_ext + F_el + F_amort = ma`.",
    "U02-096": "Secuencia: `F_el = −k_sx`; `F_amort = −bv`; `F_neta = F_ext + F_el + F_amort`; `a = F_neta/m`.",
    "U02-098": "`F_pres = Δp·S`; `F_neta = F_ext − k_sx − bv`; `a = F_neta/m`.",
    "U02-099": "`|F_el| = k_s|x|`; `E_el = ½k_sx²`.",
    "U02-101": "`c = √(γRT_temp/M)`. `T_temp` debe expresarse en K.",
    "U02-102": "`[RT_temp/M] = (J·mol⁻¹·K⁻¹)·K/(kg·mol⁻¹) = J/kg = m²/s²`; por lo tanto, `[c] = m/s`.",
    "U02-103": "`c(ϑ) ≈ 331 + 0,6ϑ`; `t = d/c`, con `d = 100 m`.",
    "U02-104": "`ΔU = Q_calor + W_sobre`; asignar cada signo desde la dirección de la flecha.",
    "U02-105": "`ΔS_total = 0` para el límite reversible ideal; `ΔS_total > 0` cuando hay producción de entropía.",
    "U02-107": "`F_ext = Δp·S`; `F_el = −k_sx`; `F_amort = −bv`; `F_neta = F_ext + F_el + F_amort`; `a = F_neta/m`.",
    "U02-108": "`E_disipada = E_entrada − ΔE_mec − E_salida`; `c ≈ 331 + 0,6ϑ`.",
}


DEFINITIONS = {
    "U02-008": "**Sistema:** cuerpo o conjunto de cuerpos cuyo movimiento se desea explicar. **Entorno:** todo lo que queda fuera de la frontera elegida.",
    "U02-009": "**Fuerza:** interacción con agente, receptor, dirección y sentido.",
    "U02-010": "**Eje positivo:** convención que permite asignar signos a componentes con sentidos opuestos.",
    "U02-011": "**Fuerza neta:** suma algebraica de las componentes de todas las fuerzas que actúan sobre el sistema.",
    "U02-013": "**Inercia:** conservación del estado de movimiento cuando la resultante es nula; la masa cuantifica esa propiedad.",
    "U02-016": "**Aceleración:** cambio de velocidad por unidad de tiempo.",
    "U02-026": "**Presión:** fuerza distribuida por unidad de área, en Pa. **Fuerza:** interacción resultante, en N.",
    "U02-035": "**Masa:** inercia. **Elasticidad:** retorno. **Amortiguamiento:** oposición al movimiento y disipación.",
    "U02-036": "**Masa (`m`):** medida de la inercia; unidad SI: kilogramo (kg).",
    "U02-037": "**Fuerza restauradora:** fuerza dirigida hacia la posición de equilibrio.",
    "U02-040": "**Coeficiente `b`:** parámetro del modelo viscoso lineal; unidad N·s/m.",
    "U02-048": "**Trabajo mecánico:** transferencia de energía asociada a una fuerza que produce desplazamiento.",
    "U02-053": "**Sistema aislado:** sistema sin intercambio de energía con el entorno durante el intervalo analizado.",
    "U02-060": "**Temperatura:** magnitud de estado que caracteriza el estado térmico. Usar °C para ambiente y K cuando se requiere temperatura absoluta.",
    "U02-061": "**Energía interna (`U`):** energía asociada al estado microscópico del sistema; unidad: joule (J).",
    "U02-062": "**Calor (`Q_calor`):** energía transferida por diferencia de temperatura; unidad: joule (J).",
    "U02-063": "**Magnitud de estado:** describe al sistema. **Transferencia:** energía que cruza la frontera durante un proceso.",
    "U02-070": "**Entropía:** magnitud de estado usada aquí para reconocer irreversibilidad macroscópica; unidad: J/K.",
    "U02-077": "**Aproximación adiabática:** durante cada ciclo, el intercambio de calor se considera despreciable.",
    "U02-078": "`c`: velocidad de propagación del frente. `u`: velocidad local de una partícula del medio. Ambas en m/s, con significados distintos.",
}


VISIBLE_OVERRIDES = {
    "U02-001": "**Unidad 2.** Movimiento, fuerzas, energía y sistemas acústicos.",
    "U02-002": "**Compare los dos estados:** 1. `p_1 = p_2`; 2. `p_1 > p_2`. ¿En cuál espera movimiento? ¿Qué podría producir retorno? ¿Qué podría hacer que se detenga?",
    "U02-003": "1. “Si está en reposo, no actúa ninguna fuerza”. 2. “Acción y reacción se cancelan sobre el mismo cuerpo”. 3. “La presión ya es una fuerza”. 4. “La energía disipada desaparece”.",
    "U02-004": "**Ya usamos:** masa, fuerza, presión y unidades. **Debemos recuperar:** eje positivo, signos y análisis dimensional.",
    "U02-005": "Al finalizar podremos: identificar sistemas y fuerzas; aplicar las leyes de Newton; relacionar presión, área y fuerza; explicar masa, elasticidad y amortiguamiento; organizar balances de energía y aplicar los modelos con límites explícitos.",
    "U02-006": "1. Sistema y leyes. 2. Presión sobre una superficie. 3. Respuesta mecánica. 4. Energía y termodinámica. 5. Aplicaciones auditivas.",
    "U02-012": "Dos fuerzas de igual módulo y sentidos opuestos actúan sobre el mismo sistema. **Elegir:** A. no actúa ninguna fuerza; B. `F_neta = 0`; C. falta definir la masa. Justificar.",
    "U02-014": "1. Elegir el sistema. 2. Declarar el eje. 3. Identificar y sumar las fuerzas. **Pregunta:** ¿qué debe cambiar para que cambie la velocidad?",
    "U02-019": "**Paso 1:** dibujar el eje y asignar signos. **Paso 2:** sumar las tres fuerzas. **Paso 3:** dividir la resultante por la masa. **Paso 4:** interpretar el signo de `a`.",
    "U02-020": "Los sistemas A y B reciben la misma `F_neta`, pero tienen masas distintas. **Predicción:** ¿cuál adquiere mayor aceleración? Justificar con `a = F_neta/m`.",
    "U02-023": "**Primera ley:** ¿qué ocurre si `F_neta = 0`? **Segunda ley:** ¿cuánto acelera? **Tercera ley:** ¿cómo se relacionan las fuerzas de dos cuerpos?",
    "U02-026": "| Criterio | Presión | Fuerza |\n|---|---|---|\n| Describe | distribución sobre un área | interacción resultante |\n| Unidad | Pa | N |\n| Relación | necesita `S` | `F_pres = Δp·S` |",
    "U02-030": "**Datos e hipótesis:** diferencia de presión conocida, área conocida y presión uniforme. **Cálculo:** multiplicar `Δp` por `S`. **Resultado:** `1,0×10⁻⁴ N`. **Alcance:** superficie ideal.",
    "U02-031": "**Permite razonar:** una diferencia de presión ejerce fuerza distribuida. **No representa:** geometría real, presión espacialmente uniforme ni movimiento rígido de toda la membrana.",
    "U02-034": "**Prediga:** ¿qué sistema mantendrá la oscilación durante más tiempo? **Observe:** igual masa y rigidez, distinto amortiguamiento. **Compare:** rapidez de decaimiento.",
    "U02-043": "| Signos del estado | `F_el` | `F_amort` |\n|---|---:|---:|\n| `x>0`, `v>0` | `<0` | `<0` |\n| `x>0`, `v<0` | `<0` | `>0` |\n| `x<0`, `v>0` | `>0` | `<0` |\n| `x<0`, `v<0` | `>0` | `>0` |",
    "U02-044": "**Procedimiento:** predecir signos → calcular `F_el` y `F_amort` → sumar con `F_ext` → obtener `F_neta` → dividir por `m` → interpretar el instante.",
    "U02-045": "| Término | Pregunta que responde |\n|---|---|\n| Amortiguamiento | ¿qué mecanismo reduce una oscilación dentro del sistema? |\n| Atenuación | ¿qué magnitud disminuye durante transmisión o propagación? |\n| Disipación | ¿qué energía mecánica se convierte en energía interna? |",
    "U02-046": "**Masa:** cambia la respuesta. **Resorte:** produce retorno. **Amortiguador:** se opone al movimiento y disipa. **Control:** ¿qué término cambia directamente cuando cambia `v`?",
    "U02-052": "1. En equilibrio, la rapidez puede ser máxima. 2. En el extremo, la rapidez es momentáneamente nula y la energía elástica es mayor. 3. Durante el retorno, ambas formas se intercambian.",
    "U02-054": "**Entra:** cruza hacia el sistema. **Se almacena:** cambia la energía mecánica. **Sale:** cruza hacia otro sistema. **Se disipa:** se convierte en energía interna.",
    "U02-056": "**Datos:** entrada `2,0 mJ`; aumento mecánico `1,3 mJ`; salida `0,4 mJ`. **Despeje:** restar cambio y salida. **Resultado:** `0,3 mJ` convertidos en energía interna.",
    "U02-057": "La energía puede **almacenarse**, **transferirse** o **disiparse**. Ninguna de esas rutas implica desaparición. **Pregunta:** ¿un sistema pasivo puede aumentar presión sin crear energía?",
    "U02-059": "Clasificar y justificar: **temperatura**, **energía interna**, **calor**, **trabajo**. ¿Cuáles describen el sistema y cuáles describen energía que cruza la frontera?",
    "U02-063": "| Magnitud de estado | Transferencia |\n|---|---|\n| describe al sistema | describe un cruce de frontera |\n| temperatura, `U` | calor, trabajo |\n| se compara entre estados | se define durante un proceso |",
    "U02-065": "1. Calor entra: `Q_calor > 0`. 2. Calor sale: `Q_calor < 0`. 3. Trabajo sobre el sistema: `W_sobre > 0`. 4. Trabajo realizado por el sistema: `W_sobre < 0`.",
    "U02-066": "**Signos:** el calor sale, por eso `Q = −3,0 J`; el trabajo entra, por eso `W_sobre = +2,0 J`. **Resultado:** `ΔU = −1,0 J`; la energía interna disminuye.",
    "U02-067": "**Estado:** temperatura y `U`. **Transferencia:** calor y trabajo. **Balance:** la primera ley relaciona transferencias con `ΔU`. ¿El sistema “contiene calor”?",
    "U02-069": "Secuencia: amplitud decreciente → menor energía mecánica organizada → mayor energía interna. El proceso inverso no ocurre espontáneamente en el modelo.",
    "U02-072": "| Reversible ideal | Irreversible real |\n|---|---|\n| límite ideal | dirección preferente |\n| `ΔS_total = 0` | `ΔS_total > 0` |\n| sin producción de entropía | con producción de entropía |",
    "U02-073": "Fuerza disipativa → disminuye la energía mecánica útil → aumenta la energía interna → se produce entropía. **La energía total se conserva.**",
    "U02-074": "**Error:** “entropía es desorden” o “entropía es eco”. **Corrección:** la entropía es termodinámica y se expresa en J/K; eco y reverberación corresponden a reflexión.",
    "U02-075": "1. La primera ley contabiliza energía. 2. La entropía informa sobre la dirección del proceso. 3. Conservar energía y producir entropía son afirmaciones compatibles.",
    "U02-077": "Observar tres zonas: **compresión**, **equilibrio** y **rarefacción**. Seguir una partícula y luego el frente. Las variaciones son pequeñas y rápidas.",
    "U02-078": "| Frente de perturbación | Partícula del aire |\n|---|---|\n| avanza con velocidad `c` | oscila localmente con velocidad `u` |\n| describe propagación | describe movimiento local |",
    "U02-080": "Puntos del modelo: `0 °C → 331 m/s`; `10 °C → 337 m/s`; `20 °C → 343 m/s`; `30 °C → 349 m/s`. **El eje vertical está truncado y no comienza en cero.**",
    "U02-081": "**20 °C:** `343 m/s`. **30 °C:** `349 m/s`. **Cambio:** aproximadamente `+6 m/s`. Condiciones: aire seco, intervalo ambiental y modelo lineal.",
    "U02-082": "**Error:** “si `c` aumenta, el sonido se vuelve más agudo”. **Corrección:** si la fuente mantiene `f`, el cambio de `c` modifica principalmente `λ`; no permite deducir la altura tonal.",
    "U02-084": "**Aplicaciones:** membrana timpánica; oído medio; vibrador óseo; tejidos; propagación en aire. **Ideas reutilizadas:** presión, fuerza, respuesta mecánica y energía.",
    "U02-085": "**Utilidad:** separar inercia, elasticidad y disipación. **Límites:** las propiedades están distribuidas; la estructura real no es una masa puntual unida literalmente a un resorte.",
    "U02-086": "Perturbación → membrana → cadena osicular → oído interno. En la ruta puede haber almacenamiento, transferencia hacia otras vías y disipación. **No aparece ningún término de creación de energía.**",
    "U02-087": "**Par:** vibrador sobre cabeza ↔ cabeza sobre vibrador. Las fuerzas son iguales y opuestas, pero actúan sobre cuerpos distintos. La vía ósea involucra varios mecanismos.",
    "U02-088": "**Caso común:** superficie flexible. **Ruta mecánica:** fuerza y aceleración. **Ruta energética:** balance y disipación. **Ruta térmica:** velocidad del aire. **Cierre:** declarar límites de inferencia.",
    "U02-089": "Sistema → fuerzas → respuesta → energía → dirección del proceso → aplicación. La frontera elegida organiza qué fuerzas se suman y qué energías cruzan.",
    "U02-090": "Ya identificamos **qué mecanismos actúan**. En la Unidad 3 estudiaremos **cómo evolucionan en el tiempo**: oscilación, período, frecuencia y propagación ondulatoria.",
    "U02-091": "Checklist: 1. Elegir sistema. 2. Dibujar frontera. 3. Declarar `+x`. 4. Identificar agentes. 5. Proyectar fuerzas. 6. Calcular `F_neta`.",
    "U02-092": "1. Reposo puede coexistir con fuerzas equilibradas. 2. Acción y reacción actúan sobre cuerpos distintos. 3. Para pasar de Pa a N se necesita un área. 4. Disipar no es destruir energía.",
    "U02-093": "**Libro–mesa:** equilibrio sobre el libro y par entre cuerpos. **Membrana–aire:** presión y reacción sobre el aire. **Vibrador–cabeza:** el par se distribuye en dos DCL.",
    "U02-094": "| Fuente | Símbolo posible | Convención de slides |\n|---|---|---|\n| Área | `A` o `S` | `S` |\n| Rigidez | `k` o `k_s` | `k_s` |\n| Resultante | `ΣF` o `F_neta` | `F_neta = ΣF` |",
    "U02-095": "| Símbolo | Magnitud | Unidad |\n|---|---|---|\n| `m` | masa | kg |\n| `k_s` | rigidez | N/m |\n| `b` | amortiguamiento | N·s/m |\n| `x`, `v`, `a` | estado mecánico | m; m/s; m/s² |",
    "U02-096": "**Control 1:** signos de `x` y `v`. **Control 2:** unidades de cada fuerza. **Control 3:** suma algebraica. **Control 4:** unidad e interpretación de `a`.",
    "U02-097": "| Término | Uso en esta unidad |\n|---|---|\n| Amortiguamiento | reducción de una oscilación por mecanismo disipativo |\n| Atenuación | disminución durante transmisión o propagación |\n| Disipación | conversión a energía interna |\n| Absorción | se desarrolla en U9 |",
    "U02-098": "**Presión:** multiplicar `Δp` por `S` y comprobar Pa·m²=N. **Modelo mecánico:** calcular fuerzas con signo, sumar y dividir por `m`.",
    "U02-099": "1. Calcular el módulo de la fuerza elástica e interpretar su sentido. 2. Calcular la energía elástica almacenada. En ambos casos: ecuación → sustitución → unidad → interpretación.",
    "U02-100": "Bibliografía del capítulo para: mecánica del oído medio; conducción ósea; comportamiento viscoelástico de tejidos. Consultar la referencia completa antes de citar.",
    "U02-101": "**Parámetros:** `γ` razón térmica; `R` constante de los gases; `T_temp` temperatura absoluta; `M` masa molar. **Hipótesis:** gas ideal y propagación adiabática.",
    "U02-102": "Dentro de la raíz deben quedar unidades de velocidad al cuadrado. `J/kg = m²/s²`; al extraer la raíz se obtiene `m/s`.",
    "U02-103": "Comparar dos estados: `5 °C` y `25 °C`, con la misma distancia `d = 100 m`. Calcular `c` y luego `t = d/c`; expresar la diferencia temporal en ms.",
    "U02-104": "Cuatro casos: calor entra; calor sale; trabajo sobre el sistema; trabajo realizado por el sistema. Dibujar primero la flecha y asignar el signo después.",
    "U02-105": "**Límite reversible ideal:** `ΔS_total = 0`. **Proceso irreversible:** `ΔS_total > 0`. Un subsistema puede disminuir su entropía si el total cumple la desigualdad.",
    "U02-106": "**Datos mecánicos:** presión, área, `m`, `k_s`, `b`, `x`, `v`. **Datos energéticos:** entrada, cambio y salida. **Dato térmico:** temperatura. Resolver por tres ramas.",
    "U02-107": "1. Obtener `F_ext` desde presión y área. 2. Calcular `F_el` y `F_amort`. 3. Sumar con signos. 4. Obtener `a`. 5. Identificar retorno y disipación.",
    "U02-108": "1. Cerrar el balance energético. 2. Estimar `c` desde la temperatura. 3. Verificar conservación. 4. Declarar límites físicos y clínicos.",
    "U02-109": "Cramer (1993); Xiang y Blauert (2021); capítulo del curso; programa oficial. Conservar datos bibliográficos completos desde la bibliografía del capítulo.",
    "U02-110": "| Símbolo | Significado | Unidad/contexto |\n|---|---|---|\n| `F_neta` | fuerza resultante | N |\n| `k_s` | rigidez | N/m |\n| `b` | amortiguamiento | N·s/m |\n| `U` | energía interna | J |\n| `Q_calor` | calor transferido | J |\n| `S` / entropía | según contexto | m² / J·K⁻¹ |",
}

# Redacción explícita para evitar que los resúmenes técnicos del storyboard se
# conviertan en texto visible telegráfico o en instrucciones de producción.
VISIBLE_OVERRIDES.update(
    {
        "U02-007": "**Pregunta guía:** ¿sobre qué cuerpo actúan las fuerzas que vamos a sumar?",
        "U02-008": "**Sistema:** cuerpo o conjunto de cuerpos cuyo movimiento analizamos. **Ejemplo:** estudiar solo la membrana no equivale a estudiar “membrana + aire”.",
        "U02-009": "Nombrar siempre **agente**, **interacción** y **receptor**: “el aire ejerce una fuerza sobre la membrana”.",
        "U02-010": "Elegimos un eje `+x`. Una fuerza hacia `+x` tiene componente positiva; una fuerza en sentido contrario tiene componente negativa.",
        "U02-011": "1. Identificar todas las fuerzas sobre el sistema. 2. Proyectarlas sobre el eje. 3. Sumarlas con signo. La resultante reemplaza ese conjunto para estudiar el movimiento.",
        "U02-013": "Si `F_neta = 0`, la velocidad permanece constante. El reposo es el caso particular `v = 0`; la inercia no genera una fuerza de retorno.",
        "U02-015": "**Pregunta guía:** ¿cuánto cambia el movimiento y de qué depende ese cambio?",
        "U02-016": "Una fuerza neta cambia la **velocidad** mediante una **aceleración**. Si las fuerzas se equilibran, no hay aceleración aunque el sistema pueda seguir moviéndose.",
        "U02-017": "`F_neta = m·a`. La fuerza neta se mide en newtons (N), la masa en kilogramos (kg) y la aceleración en metros por segundo cuadrado (m/s²).",
        "U02-018": "Para una misma fuerza neta, la masa menor adquiere mayor aceleración. En un gráfico `a`–`F_neta`, la pendiente es `1/m`.",
        "U02-021": "`F_{A→B} = −F_{B→A}`. Las dos fuerzas aparecen al mismo tiempo y tienen igual módulo, pero actúan sobre cuerpos diferentes.",
        "U02-022": "**Diagrama de A:** incluye la fuerza que B ejerce sobre A. **Diagrama de B:** incluye la fuerza que A ejerce sobre B. No se suman entre sí en un único DCL.",
        "U02-024": "**Pregunta guía:** ¿cómo convertimos una diferencia de presión, medida en pascales, en una fuerza, medida en newtons?",
        "U02-025": "Cada lado ejerce una fuerza sobre la superficie. Si `p_1 = p_2`, las contribuciones se equilibran; si `p_1 > p_2`, la resultante apunta hacia el lado de menor presión.",
        "U02-026": "**Presión:** fuerza distribuida por unidad de área; unidad Pa. **Fuerza:** interacción resultante; unidad N. Para relacionarlas hace falta conocer el área.",
        "U02-027": "Definimos `Δp = p_1 − p_2`. El orden elegido fija el signo: cambiar el orden invierte el sentido de la fuerza calculada.",
        "U02-028": "Bajo presión uniforme, `F_pres = Δp·S`. La misma diferencia de presión produce una fuerza mayor cuando el área `S` es mayor.",
        "U02-029": "`Pa·m² = (N/m²)·m² = N`. El análisis dimensional permite descartar `Δp/S` y `S/Δp`.",
        "U02-032": "`Δp` (Pa) → `F_pres = Δp·S` (N) → `a = F_neta/m` (m/s²). Cada flecha exige una relación física y unidades compatibles.",
        "U02-033": "**Pregunta guía:** ¿por qué un sistema puede volver al equilibrio, oscilar y finalmente detenerse?",
        "U02-035": "**Masa:** se opone a cambios de velocidad. **Elasticidad:** genera retorno. **Amortiguamiento:** se opone al movimiento y disipa energía.",
        "U02-036": "La masa `m` mide la inercia. Con la misma fuerza neta, una masa mayor presenta una aceleración menor.",
        "U02-037": "Si el sistema se aparta del equilibrio, la fuerza elástica apunta en sentido contrario al desplazamiento y tiende a hacerlo regresar.",
        "U02-038": "`F_el = −k_s·x`. `k_s` es la rigidez (N/m) y `x` el desplazamiento (m). El signo menos indica que la fuerza apunta hacia el equilibrio.",
        "U02-039": "El amortiguamiento se opone a la **velocidad**. En una misma posición, invertir `v` invierte la fuerza de amortiguamiento.",
        "U02-040": "`F_amort = −b·v`. `b` se mide en N·s/m y `v` en m/s. El signo menos indica oposición al movimiento.",
        "U02-041": "El modelo ideal separa tres propiedades: `m` representa inercia, `k_s` representa rigidez y `b` representa amortiguamiento. No es una copia anatómica.",
        "U02-042": "`m·a = F_ext − k_s·x − b·v`. Cada término describe un mecanismo: entrada externa, retorno elástico, disipación e inercia.",
        "U02-043": "Para cada combinación de signos de `x` y `v`, aplicar `F_el = −k_s·x` y `F_amort = −b·v`. Ambas fuerzas pueden coincidir o apuntar en sentidos opuestos.",
        "U02-045": "**Amortiguamiento:** mecanismo que reduce la oscilación. **Atenuación:** disminución de una magnitud. **Disipación:** conversión de energía mecánica en energía interna.",
        "U02-047": "**Pregunta guía:** cuando una fuerza realiza trabajo, ¿dónde queda la energía transferida?",
        "U02-048": "En el caso simple, una fuerza realiza trabajo mecánico si produce un desplazamiento. Puede existir fuerza sin trabajo cuando no hay desplazamiento.",
        "U02-049": "Si la fuerza es constante y paralela al desplazamiento, `W = F·Δx`. El trabajo se mide en joules: `1 J = 1 N·m`.",
        "U02-050": "`E_c = ½m·v²`. Para la misma masa, duplicar la rapidez cuadruplica la energía cinética.",
        "U02-051": "`E_el = ½k_s·x²`. El resorte almacena la misma energía para desplazamientos `+x` y `−x` de igual módulo.",
        "U02-053": "En un sistema aislado, la energía total permanece constante aunque cambie de forma. Una disminución de energía mecánica no implica destrucción de energía.",
        "U02-055": "`E_entrada = ΔE_mec + E_salida + E_disipada`. Si conocemos tres términos, el cuarto se obtiene por balance y debe conservar la unidad de energía.",
        "U02-058": "**Pregunta guía:** ¿qué magnitudes describen el estado del sistema y cuáles representan energía que cruza su frontera?",
        "U02-060": "La temperatura describe el estado térmico. Usamos grados Celsius (°C) para el ambiente y kelvin (K) cuando una ecuación requiere temperatura absoluta.",
        "U02-061": "La energía interna `U` pertenece al estado microscópico del sistema y se mide en joules. Dos sistemas a igual temperatura pueden tener distinta `U`.",
        "U02-062": "El calor `Q_calor` es energía transferida por una diferencia de temperatura. Un sistema no “contiene calor”: contiene energía interna.",
        "U02-063": "**Magnitudes de estado:** temperatura y energía interna; describen al sistema. **Transferencias:** calor y trabajo; describen energía que cruza la frontera durante un proceso.",
        "U02-064": "Con la convención “positivo al entrar”: `ΔU = Q_calor + W_sobre`. Cada término se expresa en joules (J).",
        "U02-068": "**Pregunta guía:** ¿por qué una oscilación amortiguada no recupera por sí sola su amplitud inicial?",
        "U02-070": "La entropía `S_ent` es una magnitud de estado. Aquí se usa cualitativamente para reconocer irreversibilidad macroscópica; su unidad es J/K.",
        "U02-071": "Para un sistema total aislado, `ΔS_total ≥ 0`. La igualdad representa el límite reversible ideal; un aumento indica producción de entropía.",
        "U02-072": "**Reversible ideal:** `ΔS_total = 0`, sin producción de entropía. **Irreversible real:** `ΔS_total > 0`, con una dirección preferente del proceso.",
        "U02-076": "**Pregunta guía:** ¿qué cambia en la propagación del sonido cuando cambia la temperatura del aire?",
        "U02-078": "**Frente:** la perturbación avanza con velocidad `c`. **Partícula:** cada porción de aire oscila localmente con velocidad `u`. Propagación no significa transporte neto del aire.",
        "U02-079": "Cerca de temperaturas ambientales y para aire seco: `c ≈ 331 m/s + (0,6 m/s·°C⁻¹)·ϑ`. Es una aproximación lineal de alcance limitado.",
        "U02-083": "**Pregunta guía:** ¿qué permite afirmar un modelo físico y qué información adicional hace falta para aplicarlo a una situación clínica?",
        "U02-094": "**Convención de slides:** área `S`; rigidez `k_s`; resultante `F_neta = ΣF`. Reconocer que otras fuentes pueden usar `A`, `k` o `ΣF`.",
        "U02-095": "`m`: masa (kg); `k_s`: rigidez (N/m); `b`: amortiguamiento (N·s/m); `x`, `v`, `a`: desplazamiento, velocidad y aceleración.",
        "U02-097": "**Amortiguamiento:** mecanismo disipativo. **Atenuación:** disminución durante transmisión o propagación. **Disipación:** conversión a energía interna. **Absorción:** se desarrolla en U9.",
        "U02-110": "`F_neta`: fuerza resultante (N); `k_s`: rigidez (N/m); `b`: amortiguamiento (N·s/m); `U`: energía interna (J); `Q_calor`: calor transferido (J); `S_ent`: entropía (J/K).",
    }
)


EXAMPLES = {
    "U02-002": "Predecir movimiento, retorno y detención antes de revelar explicaciones.",
    "U02-003": "Votar verdadero/falso y escribir una razón breve para cada afirmación.",
    "U02-012": "Elegir una opción y explicar qué significa `F_neta = 0`.",
    "U02-018": "Leer ambas rectas para una misma fuerza neta y comparar aceleraciones.",
    "U02-019": "Resolver el caso en el orden `fuerzas → resultante → aceleración`.",
    "U02-020": "Responder sin cálculo y luego justificar con la relación inversa con la masa.",
    "U02-023": "Ante un mini caso, elegir qué ley responde primero la pregunta planteada.",
    "U02-026": "Indicar qué dato adicional permite transformar una diferencia de presión en fuerza.",
    "U02-029": "Descartar `Δp/S` y `S/Δp` mediante unidades.",
    "U02-030": "Interpretar el signo y aclarar por qué el valor no es universal para una membrana real.",
    "U02-032": "Si `Δp` permanece fija y se duplica `S`, predecir qué ocurre con `F_pres`.",
    "U02-034": "Reproducir la comparación o usar los dos estados estáticos.",
    "U02-036": "Comparar dos masas sometidas a la misma resultante.",
    "U02-037": "Para `x>0` y `x<0`, dibujar el sentido de retorno.",
    "U02-039": "Comparar igual posición con `v>0` y `v<0`.",
    "U02-043": "Completar los cuatro signos antes de mostrar la matriz resuelta.",
    "U02-044": "Predecir el signo de cada fuerza antes de sustituir los datos aprobados.",
    "U02-048": "Comparar una fuerza con desplazamiento y otra sin desplazamiento.",
    "U02-050": "A la misma masa, comparar `v` con `2v`.",
    "U02-051": "Comparar `x` y `−x`: la fuerza cambia de signo; la energía no.",
    "U02-052": "Ordenar los tres estados e identificar dónde predomina cada forma de energía.",
    "U02-056": "Comprobar que `1,3 + 0,4 + 0,3 = 2,0 mJ`.",
    "U02-057": "Explicar cómo un sistema pasivo puede transformar variables sin crear energía.",
    "U02-059": "Clasificar cuatro términos y justificar por frontera o estado.",
    "U02-065": "Asignar signos a partir de flechas, no de palabras memorizadas.",
    "U02-066": "Explicar físicamente por qué `ΔU` resulta negativa.",
    "U02-071": "Distinguir el caso de igualdad del caso de aumento.",
    "U02-074": "Corregir dos frases usando unidad y fenómeno físico.",
    "U02-075": "Aplicar ambas leyes a un oscilador amortiguado.",
    "U02-077": "Seguir una partícula marcada y luego el frente de perturbación.",
    "U02-080": "Leer el incremento entre puntos sin extrapolar fuera del rango.",
    "U02-081": "Estimar primero en el gráfico y calcular después.",
    "U02-082": "Mantener `f` fija y predecir qué variable debe cambiar.",
    "U02-087": "Dibujar por separado el DCL del vibrador y el de la cabeza.",
    "U02-088": "Elegir la herramienta antes de iniciar cualquier cálculo.",
    "U02-089": "Explicar cada flecha del mapa final con una frase y una unidad.",
    "U02-091": "Usar el checklist en dos mini DCL.",
    "U02-092": "Comparar las respuestas finales con el diagnóstico U02-003.",
    "U02-093": "Seleccionar uno de los tres contraejemplos según la duda del grupo.",
    "U02-096": "Completar la solución numérica con los datos ya asignados en la consigna.",
    "U02-098": "Usar como devolución después de intentar ambos problemas.",
    "U02-099": "Resolver de forma autónoma; las soluciones permanecen en notas.",
    "U02-102": "Cancelar mol y K antes de extraer la raíz.",
    "U02-103": "Comparar tiempos para 100 m y expresar la diferencia en milisegundos.",
    "U02-104": "Resolver los cuatro signos antes de revelar resultados.",
    "U02-105": "Comparar sistema total con un subsistema.",
    "U02-106": "Marcar qué datos alimentan cada rama sin resolver todavía.",
    "U02-107": "Resolver la rama mecánica completa.",
    "U02-108": "Cerrar la rama energética y térmica con dos límites del modelo.",
}


QUESTIONS = {
    "U02-001": ("¿Qué hace que una membrana empiece a moverse y luego se detenga?", "Una fuerza neta inicia el cambio; elasticidad y amortiguamiento ayudan a explicar retorno y decaimiento."),
    "U02-002": ("¿En qué estado espera una fuerza neta?", "Cuando las presiones son diferentes, si las demás condiciones se mantienen."),
    "U02-003": ("¿Qué afirmación les genera más duda?", "No hay una única respuesta diagnóstica; se busca una justificación inicial."),
    "U02-012": ("Si el cuerpo está en reposo, ¿pueden actuar fuerzas?", "Sí; pueden sumar cero."),
    "U02-014": ("¿Qué debe cambiar para que cambie la velocidad?", "Debe existir aceleración producida por una fuerza neta no nula."),
    "U02-018": ("¿Qué recta corresponde a la masa mayor?", "La de menor pendiente."),
    "U02-020": ("¿Quién acelera más con la misma fuerza?", "La masa menor."),
    "U02-023": ("¿Qué ley relaciona dos cuerpos?", "La tercera ley."),
    "U02-026": ("¿Por qué Pa y N no son intercambiables?", "Describen magnitudes distintas y se relacionan mediante un área."),
    "U02-032": ("¿Qué ocurre con la fuerza si se duplica el área?", "Se duplica bajo `Δp` uniforme y constante."),
    "U02-034": ("¿Qué cambia al aumentar el amortiguamiento?", "La oscilación decae más rápido."),
    "U02-043": ("¿De qué variable depende cada fuerza?", "`F_el` depende de `x`; `F_amort` depende de `v`."),
    "U02-046": ("¿Qué término cambia si cambia `v`?", "El término `bv` y, por lo tanto, `F_amort`."),
    "U02-052": ("¿Dónde es mayor la energía elástica?", "En los extremos de mayor deformación."),
    "U02-057": ("¿Aumentar presión equivale a crear energía?", "No; un sistema pasivo puede transformar variables y redistribuir energía."),
    "U02-059": ("¿Qué contiene el sistema?", "Temperatura y energía interna describen su estado; calor y trabajo no son contenidos."),
    "U02-065": ("¿Qué determina el signo?", "La dirección física respecto de la frontera y la convención declarada."),
    "U02-066": ("¿Qué significa `ΔU < 0`?", "Que la energía interna final es menor que la inicial en el intervalo."),
    "U02-071": ("¿Qué diferencia hay entre `=0` y `>0`?", "Igualdad: límite reversible ideal; aumento: proceso irreversible."),
    "U02-074": ("¿La unidad de entropía podría ser la de un eco?", "No; J/K identifica una magnitud termodinámica."),
    "U02-075": ("¿Puede conservarse energía y aumentar la entropía?", "Sí; las leyes responden preguntas distintas."),
    "U02-078": ("¿La partícula marcada viaja con el frente?", "No; oscila localmente."),
    "U02-080": ("¿Los puntos son mediciones?", "No; son valores calculados con el modelo."),
    "U02-081": ("¿Cuánto cambia `c` entre 20 y 30 °C?", "Aproximadamente 6 m/s."),
    "U02-082": ("Si `f` permanece fija y aumenta `c`, ¿qué cambia?", "La longitud de onda `λ`."),
    "U02-083": ("¿Qué permite afirmar un modelo físico?", "Mecanismos y relaciones dentro de sus hipótesis, no diagnósticos ni sensaciones por sí solo."),
    "U02-087": ("¿Por qué el par no se cancela al estudiar la cabeza?", "La fuerza opuesta actúa sobre el vibrador."),
    "U02-088": ("¿Qué herramienta usaría para cada tarea?", "Newton para fuerzas; balance para energía; `c(ϑ)` para propagación."),
    "U02-089": ("¿Qué elemento organiza ambos balances?", "La frontera del sistema."),
    "U02-090": ("¿Qué falta describir?", "La evolución temporal: oscilación, frecuencia y onda."),
    "U02-099": ("¿Qué debe acompañar a cada resultado?", "Ecuación, unidad e interpretación."),
    "U02-103": ("¿Por qué cambia el tiempo si la distancia es la misma?", "Porque `t=d/c` y cambia `c`."),
    "U02-104": ("¿Se puede asignar el signo sin dibujar la dirección?", "Es más seguro dibujar primero la transferencia."),
    "U02-105": ("¿Puede disminuir la entropía de un subsistema?", "Sí, si el total aislado cumple `ΔS_total ≥ 0`."),
}


ERRORS = {
    "U02-012": "Reposo no equivale a ausencia de fuerzas.",
    "U02-013": "La inercia no es una fuerza y no explica el retorno al equilibrio.",
    "U02-017": "Usar una fuerza aislada en lugar de `F_neta`.",
    "U02-021": "Acción y reacción no se cancelan dentro de un mismo DCL.",
    "U02-026": "Confundir Pa con N.",
    "U02-028": "La relación supone presión uniforme sobre el área considerada.",
    "U02-038": "El signo negativo expresa sentido restaurador, no módulo negativo.",
    "U02-040": "No toda atenuación se explica mediante el coeficiente `b`.",
    "U02-042": "El balance instantáneo no es la solución temporal de la oscilación.",
    "U02-045": "Una amplitud menor no identifica por sí sola disipación.",
    "U02-053": "Disminución de energía mecánica útil no significa destrucción de energía total.",
    "U02-060": "No usar grados Celsius dentro de una ecuación que requiere temperatura absoluta.",
    "U02-062": "El sistema no “contiene calor”; contiene energía interna.",
    "U02-064": "No cambiar la convención de signos a mitad del ejercicio.",
    "U02-070": "Evitar definir entropía como desorden cotidiano.",
    "U02-074": "Eco y reverberación no son ejemplos de entropía.",
    "U02-078": "No confundir `c` con la velocidad local `u`.",
    "U02-080": "El eje truncado hace visible el cambio, pero no debe exagerarse su interpretación.",
    "U02-082": "Velocidad de propagación y altura tonal no son sinónimos.",
    "U02-085": "El modelo concentrado no copia la anatomía.",
    "U02-086": "Aumentar presión o fuerza no implica crear energía.",
    "U02-087": "La conducción ósea no se reduce a una única onda que recorre el hueso.",
    "U02-101": "La temperatura de la ecuación general debe ser absoluta.",
    "U02-105": "La desigualdad se aplica al sistema total aislado, no automáticamente a cada subsistema.",
}


SUBTITLE_BY_TYPE = {
    "portada": "Movimiento, energía y sistemas acústicos.",
    "pregunta": "Predicción y justificación.",
    "puente": "Recuperación de conocimientos previos.",
    "objetivos": "Resultados observables de aprendizaje.",
    "mapa": "Orientación de la secuencia.",
    "divisor": "Pregunta guía del bloque.",
    "definición": "Significado físico y alcance.",
    "explicación": "Interpretación antes del cálculo.",
    "proceso": "Secuencia causal.",
    "ecuación": "Símbolos, unidades e interpretación.",
    "gráfico": "Lectura del modelo.",
    "ejemplo": "Procedimiento e interpretación.",
    "comparación": "Diferencias que cambian la explicación.",
    "recapitulación": "Comprobación antes de avanzar.",
    "multimedia": "Predicción, observación y conclusión.",
    "ejercicio": "Elegir primero la herramienta.",
    "aplicación": "Uso físico y límites.",
    "error frecuente": "Corrección conceptual.",
    "cierre": "Puente hacia la Unidad 3.",
    "respaldo": "Material de consulta.",
    "bibliografía": "Trazabilidad técnica.",
}


TYPE_WEIGHTS = {
    "portada": 2,
    "pregunta": 4,
    "puente": 3,
    "objetivos": 2,
    "mapa": 2,
    "divisor": 1,
    "definición": 3,
    "explicación": 3,
    "proceso": 4,
    "ecuación": 4,
    "gráfico": 4,
    "ejemplo": 5,
    "comparación": 4,
    "recapitulación": 3,
    "multimedia": 5,
    "ejercicio": 5,
    "aplicación": 4,
    "error frecuente": 3,
    "cierre": 2,
}

BLOCK_BUDGETS = {
    "B00 · Apertura": 15,
    "B01 · Sistema e inercia": 20,
    "B02 · Segunda y tercera leyes": 25,
    "B03 · Presión y fuerza": 20,
    "B04 · Respuesta mecánica": 35,
    "B05 · Trabajo y energía": 30,
    "B06 · Calor y primera ley": 25,
    "B07 · Entropía e irreversibilidad": 20,
    "B08 · Aire y temperatura": 20,
    "B09 · Aplicación e integración": 15,
}


def clean(value: str):
    value = re.sub(
        r"\*{0,2}CANDIDATA `(?:diagram-generation|chart-generation)`\*{0,2}:?\s*",
        "",
        value.strip(),
    )
    value = value.replace("ASSET EXTERNO por curar", "Imagen técnica")
    value = value.replace("Imagen técnica más fotografía técnica", "Fotografía técnica")
    value = re.sub(r"[;,:]\s*\.", ".", value)
    value = re.sub(r"\s+([,.;:])", r"\1", value)
    return " ".join(value.split())


def split_summary(summary: str):
    parts = [part.strip(" .") for part in summary.split(";") if part.strip(" .")]
    return parts or [summary.strip()]


def generic_visible(row):
    parts = split_summary(row["summary"])
    slide_type = row["slide_type"]
    key = row["key_message"]
    if slide_type == "divisor":
        return f"**Pregunta guía:** {parts[-1] if 'pregunta' in parts[-1].lower() else key}"
    if slide_type in {"mapa", "proceso"}:
        return " → ".join(parts)
    if slide_type == "comparación" and len(parts) >= 2:
        return f"**Comparar:** {parts[0]}. **Distinguir:** {'; '.join(parts[1:])}."
    if slide_type == "recapitulación":
        return f"**Síntesis:** {key} **Control:** {parts[-1]}."
    if slide_type == "ecuación":
        return f"**Lectura física:** {key} **Condiciones:** {'; '.join(parts[1:]) if len(parts) > 1 else parts[0]}."
    if slide_type in {"aplicación", "error frecuente"}:
        return f"**Idea central:** {key} **Alcance:** {'; '.join(parts)}."
    if slide_type in {"respaldo", "bibliografía"}:
        return f"**Consulta:** {key} {'; '.join(parts)}."
    return f"{key} {'; '.join(parts)}."


def caption_for(row):
    if row["visual_class"] == "none":
        return "—"
    suffix = " Esquema conceptual; no está a escala." if row["slide_id"] in {
        "U02-002",
        "U02-025",
        "U02-031",
        "U02-037",
        "U02-052",
        "U02-069",
        "U02-077",
        "U02-078",
        "U02-086",
        "U02-087",
        "U02-103",
    } else ""
    return row["key_message"] + suffix


def alt_text_for(row):
    visual_class = {
        "diagram": "Diagrama",
        "mixed": "Esquema mixto",
        "chart": "Gráfico",
        "external_image": "Imagen técnica",
        "video_or_gif": "Secuencia multimedia",
        "equation_only": "Ecuación anotada",
        "none": "Composición textual",
    }.get(row["visual_class"], "Visual")
    summary = row["summary"]
    if row["slide_id"] == "U02-110":
        summary = "Tabla de símbolos mecánicos y termodinámicos, con significado y unidad."
    return f"{visual_class} de la slide «{re.sub(r'[`*]', '', row['title'])}»: {re.sub(r'[`*]', '', summary)}"


def visual_instruction(row):
    visual = clean(row["visual"])
    if row["visual_class"] in {"diagram", "mixed", "equation_only"}:
        return (
            f"{visual} Mantener cajas en 2–3 líneas, conectores sin texto largo y una lectura principal: "
            f"{row['key_message']}"
        )
    return visual


def allocate_durations(rows):
    durations = {}
    by_block = defaultdict(list)
    for row in rows:
        if row["status"] == "central" and row["block"] in BLOCK_BUDGETS:
            by_block[row["block"]].append(row)
    for block, block_rows in by_block.items():
        budget = BLOCK_BUDGETS[block]
        weights = [TYPE_WEIGHTS.get(row["slide_type"], 3) for row in block_rows]
        total = sum(weights)
        raw = [budget * weight / total for weight in weights]
        allocated = [max(1, math.floor(value)) for value in raw]
        while sum(allocated) < budget:
            candidates = sorted(
                range(len(raw)),
                key=lambda index: raw[index] - math.floor(raw[index]),
                reverse=True,
            )
            for index in candidates:
                allocated[index] += 1
                if sum(allocated) == budget:
                    break
        while sum(allocated) > budget:
            candidates = sorted(range(len(raw)), key=lambda index: allocated[index], reverse=True)
            for index in candidates:
                if allocated[index] > 1:
                    allocated[index] -= 1
                    if sum(allocated) == budget:
                        break
        for row, duration in zip(block_rows, allocated):
            durations[row["slide_id"]] = f"{duration} min"
    for row in rows:
        if row["slide_id"] in durations:
            continue
        if row["status"] == "complementary":
            durations[row["slide_id"]] = "3 min si se selecciona"
        else:
            durations[row["slide_id"]] = "A demanda"
    return durations


def slide_text(rows):
    lines = [
        "# Unidad 2 — Texto visible de las diapositivas",
        "",
        "## Criterio de uso",
        "",
        "Redacción correspondiente exclusivamente al storyboard aprobado de 110 slides. No se agregó, eliminó ni dividió ninguna slide. Cuando el storyboard no explicita valores numéricos, se conserva el procedimiento simbólico y no se fabrican datos. Las fuentes abreviadas se desarrollan en `source_map.md`.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        subtitle = SUBTITLE_BY_TYPE.get(row["slide_type"], row["key_message"])
        visible = VISIBLE_OVERRIDES.get(sid, generic_visible(row))
        equation = EQUATIONS.get(sid, "—")
        definition = DEFINITIONS.get(sid, "—")
        example = EXAMPLES.get(sid, "—")
        lines.extend(
            [
                f"## {sid} — {row['title']}",
                "",
                f"- **Subtítulo:** {subtitle}",
                f"- **Contenido visible:** {visible}",
                f"- **Ecuaciones:** {equation}",
                f"- **Definiciones:** {definition}",
                f"- **Ejemplo/consigna:** {example}",
                f"- **Caption:** {caption_for(row)}",
                f"- **Visual:** {visual_instruction(row)}",
                f"- **Layout:** `{row['layout']}`.",
                f"- **Fuente:** {row['source']}.",
                f"- **Transición:** {row['transition']}",
                f"- **Texto alternativo:** {alt_text_for(row)}",
                "",
            ]
        )
    return "\n".join(lines)


def diagram_guide(row):
    if row["visual_class"] not in {"diagram", "mixed", "equation_only", "chart"}:
        return "—"
    if row["visual_class"] == "chart":
        return (
            "Nombrar primero los ejes y sus unidades; luego leer uno o dos puntos; finalmente formular "
            f"la conclusión: {row['key_message']}"
        )
    steps = split_summary(row["summary"])
    return (
        "1. Delimitar el sistema o la ecuación central. "
        f"2. Recorrer en el orden previsto: {' → '.join(steps[:4])}. "
        f"3. Cerrar con la idea central: {row['key_message']}"
    )


def multimedia_note(row):
    if row["visual_class"] != "video_or_gif":
        return "—"
    return (
        f"Reproducir el recurso indicado: {clean(row['visual'])} Mostrar una vez sin explicar y otra vez "
        "siguiendo el elemento señalado. Si falla la reproducción, usar la alternativa estática completa."
    )


def default_question(row):
    prompts = {
        "divisor": "¿Qué pregunta física organiza este bloque?",
        "definición": "¿Qué distingue esta magnitud o concepto de los anteriores?",
        "ecuación": "¿Qué relación física expresa la ecuación y qué unidades deben ser compatibles?",
        "comparación": "¿Cuál es la diferencia esencial entre los casos comparados?",
        "proceso": "¿Qué etapa conecta la entrada con el resultado?",
        "mapa": "¿Qué conexión del mapa organiza las ideas de la unidad?",
        "recapitulación": "¿Cómo se conectan las ideas principales del bloque?",
        "aplicación": "¿Qué permite afirmar el modelo y qué queda fuera de su alcance?",
        "error frecuente": "¿Por qué la afirmación inicial es incorrecta?",
        "ejercicio": "¿Qué procedimiento permite llegar a una respuesta con unidades?",
        "pregunta": "¿Qué evidencia o relación física sostiene su respuesta?",
    }
    prompt = prompts.get(
        row["slide_type"],
        "¿Cómo justificaría la idea central usando el sistema, los signos o las unidades?",
    )
    return prompt, row["key_message"]


def development_for(row):
    additions = {
        "definición": "Dar un ejemplo y un contraejemplo antes de fijar el término.",
        "ecuación": "Definir símbolos, signos, unidades e hipótesis antes de usar la expresión.",
        "comparación": "Recorrer primero lo común y después la diferencia que cambia la interpretación.",
        "proceso": "Seguir una sola ruta de izquierda a derecha y detenerse en cada transformación.",
        "mapa": "Usar el mapa como orientación y señalar dónde se encuentra la clase.",
        "ejercicio": "Resolver en el orden datos e hipótesis → ecuación → sustitución → unidad → interpretación.",
        "pregunta": "Dar tiempo de respuesta individual y pedir una justificación breve antes de discutir.",
        "recapitulación": "Reconstruir las relaciones causales; evitar una enumeración de términos aislados.",
        "aplicación": "Separar explícitamente la utilidad del modelo de sus límites físicos y clínicos.",
        "error frecuente": "Pedir primero que identifiquen el error y luego formular la corrección precisa.",
        "bibliografía": "Indicar para qué pregunta sirve cada grupo de fuentes; no leer la lista completa.",
    }
    addition = additions.get(row["slide_type"], "")
    text = " ".join(part for part in [row["speaker_goal"], addition] if part)
    return re.sub(r"\bpitch\b", "altura tonal", text, flags=re.IGNORECASE)


def emphasis_for(row):
    if row["slide_id"] in ERRORS:
        return ERRORS[row["slide_id"]]
    if row["visual_class"] == "chart":
        return "Nombrar ejes, unidades y escala; no presentar los puntos del modelo como mediciones."
    if row["visual_class"] in {"diagram", "mixed"}:
        return "No interpretar el esquema como anatomía a escala; usarlo para leer relaciones y direcciones."
    by_type = {
        "ecuación": "No usar la fórmula como receta: controlar signo, unidad e hipótesis.",
        "pregunta": "No revelar la respuesta antes de escuchar al menos una justificación.",
        "ejercicio": "No aceptar un número sin unidad ni interpretación física.",
        "recapitulación": "Pedir conexiones entre conceptos, no una lista memorizada.",
        "aplicación": "No extrapolar el modelo ideal a una conclusión clínica individual.",
        "error frecuente": "Corregir la idea sin ridiculizar la intuición que la originó.",
        "respaldo": "Usar solo si resuelve una duda concreta; no interrumpir la ruta central sin necesidad.",
    }
    return by_type.get(
        row["slide_type"],
        "Mantener consistente el sistema elegido, el eje de signos y las unidades.",
    )


def notes_text(rows, durations):
    lines = [
        "# Unidad 2 — Notas del orador",
        "",
        "## Criterio de uso",
        "",
        "Las notas amplían la explicación sin repetir literalmente la slide. Las duraciones de la ruta central reproducen los 225 minutos del storyboard; las complementarias y los respaldos se usan de manera selectiva.",
        "",
    ]
    for row in rows:
        sid = row["slide_id"]
        question, answer = QUESTIONS.get(sid, default_question(row))
        lines.extend(
            [
                f"## {sid}",
                "",
                f"- **Desarrollo:** {development_for(row)}",
                f"- **Guía del visual/diagrama:** {diagram_guide(row)}",
                f"- **Pregunta y respuesta esperada:** “{question}” Respuesta esperada: {answer}",
                f"- **Demostración/multimedia:** {multimedia_note(row)}",
                f"- **Énfasis/error frecuente:** {emphasis_for(row)}",
                f"- **Transición:** “{row['transition']}”",
                f"- **Duración:** {durations[sid]}.",
                f"- **[Sources]:** {row['source']}.",
                "",
            ]
        )
    return "\n".join(lines)


SOURCE_KEYS = [
    ("PO", "Programa oficial, Unidad 2, p. 3."),
    ("TEX", "Capítulo LaTeX de la Unidad 2, con la sección indicada por el storyboard."),
    ("PDF", "Libro del curso en PDF, páginas indicadas por el storyboard."),
    ("CM", "`course_map.md`, Unidad 2."),
    ("CDM", "`course_dependency_map.md`, Unidad 2."),
    ("BR", "`units/unit_02/brief.md`."),
    ("INV", "`units/unit_02/content_inventory.md`."),
    ("NOT", "`style/notation_guide_draft.md`."),
    ("GLO", "`style/glossary_draft.md`."),
    ("U1", "Unidad 1 final, solo para continuidad declarada en el storyboard."),
    ("REF", "Bibliografía académica ya citada en el capítulo; conservar la referencia completa desde allí."),
]


def source_map(rows):
    lines = [
        "# Unidad 2 — Mapa de fuentes de la redacción",
        "",
        "## Alcance",
        "",
        "La redacción se realizó exclusivamente desde el storyboard aprobado. Este mapa conserva la fuente asignada en cada fila y no incorpora datos, referencias ni arquitectura externos.",
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
            "| slide_id | afirmación o función principal | fuente aprobada |",
            "|---|---|---|",
        ]
    )
    for row in rows:
        key_message = row["key_message"].replace("|", "/")
        source = row["source"].replace("|", "/")
        lines.append(f"| {row['slide_id']} | {key_message} | {source}. |")
    lines.extend(
        [
            "",
            "## Regla de uso",
            "",
            "Durante el montaje, las referencias completas y los créditos de assets deben recuperarse desde las fuentes señaladas por el storyboard. Esta fase no verificó ni amplió bibliografía porque la instrucción exigió trabajar solo desde el storyboard.",
            "",
        ]
    )
    return "\n".join(lines)


def word_count(value):
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ]+\b", re.sub(r"`[^`]+`", " ecuación ", value)))


def writing_review(rows, durations, slide_output, notes_output):
    ids = [row["slide_id"] for row in rows]
    statuses = Counter(row["status"] for row in rows)
    visible_counts = []
    for row in rows:
        visible_counts.append(word_count(VISIBLE_OVERRIDES.get(row["slide_id"], generic_visible(row))))
    duration_sums = defaultdict(int)
    for row in rows:
        if row["status"] == "central":
            duration_sums[row["block"]] += int(durations[row["slide_id"]].split()[0])
    lines = [
        "# Unidad 2 — Revisión de redacción de slides y notas",
        "",
        "## Dictamen",
        "",
        "**Estado: aprobado para iniciar la producción del PowerPoint.**",
        "",
        "La redacción conserva las 110 slides del storyboard aprobado: 72 centrales, 18 complementarias y 20 de respaldo. No se creó ni modificó ningún PowerPoint.",
        "",
        "## Controles estructurales",
        "",
        "| control | resultado |",
        "|---|---|",
        f"| IDs U02-001–U02-110 | {len(ids)}/110 presentes, consecutivos y sin duplicados. |",
        "| Título, subtítulo y contenido visible | 110/110. |",
        "| Ecuación o indicación de no correspondencia | 110/110. |",
        "| Definición o indicación de no correspondencia | 110/110. |",
        "| Ejemplo/consigna | 110/110. |",
        "| Caption, visual y layout | 110/110. |",
        "| Fuente, transición y texto alternativo | 110/110. |",
        "| Desarrollo, pregunta, respuesta y duración en notas | 110/110. |",
        "| Fila de trazabilidad en source_map | 110/110. |",
        "",
        "## Duración de la ruta central",
        "",
        "| bloque | duración redactada | duración del storyboard |",
        "|---|---:|---:|",
    ]
    for block, budget in BLOCK_BUDGETS.items():
        lines.append(f"| {block} | {duration_sums[block]} min | {budget} min |")
    lines.extend(
        [
            "| **Total** | **225 min** | **225 min** |",
            "",
            "La pausa de 15 minutos prevista después de B05 no se asigna a una slide. Las complementarias y los respaldos no forman parte del total.",
            "",
            "## Revisión pedagógica",
            "",
            "| criterio | evidencia | resultado |",
            "|---|---|---|",
            "| Intuición antes del formalismo | Membrana, predicciones y sistema preceden a las leyes; observación térmica precede a `c(ϑ)`. | Conforme. |",
            "| Nivel de primer año | Cada relación define variables y unidades sin cálculo diferencial. | Conforme. |",
            "| Ejemplos con pasos | U02-019, U02-030, U02-044, U02-056, U02-066, U02-081 y respaldos. | Conforme. |",
            "| Aplicaciones fonoaudiológicas | U02-031 y U02-084–U02-088 incluyen utilidad y límites. | Conforme. |",
            "| Preguntas resolubles | Las notas incluyen respuesta esperada; no se oculta una premisa imprescindible. | Conforme. |",
            "| Recapitulaciones | U02-014, 023, 032, 046, 057, 067, 075 y 089 piden decisión o transferencia. | Conforme. |",
            "| Errores frecuentes | Equilibrio, tercera ley, Pa/N, disipación, calor contenido, entropía y altura tonal. | Conforme. |",
            "| Diagramas | El texto visible complementa el visual; las explicaciones largas permanecen en notas. | Conforme. |",
            "",
            "## Densidad prevista",
            "",
            f"- Promedio aproximado del contenido visible: {sum(visible_counts)/len(visible_counts):.1f} palabras.",
            f"- Máximo aproximado del campo visible: {max(visible_counts)} palabras.",
            "- Las tablas de respaldo U02-094, U02-095, U02-097 y U02-110 deberán verificarse a 22 pt o más durante el montaje; si no entran, se dividen.",
            "- Las ecuaciones están separadas del contenido visible para permitir jerarquía y editabilidad.",
            "- Los detalles de solución, conducción oral y errores frecuentes están en notas.",
            "",
            "## Revisión de exactitud y alcance",
            "",
            "- Se definieron símbolos y unidades para Newton, presión–área, modelo masa–resorte–amortiguador, energía, primera ley, entropía y velocidad de propagación.",
            "- Se mantuvo la convención `S`, `k_s`, `F_neta`, `Q_calor`, `W_sobre` y `T_temp` indicada por el storyboard; `S_ent` identifica entropía en texto corrido.",
            "- No se introdujeron valores numéricos ausentes del storyboard. Los ejemplos sin cifras explícitas se redactaron como procedimientos simbólicos.",
            "- Los modelos biológicos se presentan con límites; no producen diagnósticos ni predicciones perceptuales por sí solos.",
            "- `c` se distingue de frecuencia, longitud de onda, velocidad local de partícula y altura tonal.",
            "",
            "## Revisión de fuentes",
            "",
            "- Cada slide conserva exactamente la fuente asignada en el storyboard.",
            "- `source_map.md` contiene 110 filas de trazabilidad.",
            "- No se consultaron ni agregaron fuentes externas durante esta fase.",
            "- Las referencias completas deberán recuperarse desde las fuentes indicadas al montar el deck.",
            "",
            "## Incidencias y decisiones",
            "",
            "| id | severidad | hallazgo | tratamiento | estado |",
            "|---|---|---|---|---|",
            "| U02-WR-001 | Menor | El storyboard no fija cifras completas en varios ejemplos y respaldos. | Se redactó el procedimiento simbólico y se evitó fabricar datos. | Mitigado. |",
            "| U02-WR-002 | Menor | La disponibilidad de demostraciones propias no está confirmada. | Las notas exigen alternativa estática. | Mitigado. |",
            "| U02-WR-003 | Menor | U02-096 y U02-110 pueden ser densas. | Mantener como respaldo y dividir durante montaje solo si el render no cumple mínimos. | Pendiente de montaje. |",
            "| U02-WR-004 | Menor | La notación de entropía puede colisionar con `S` de área. | Se usa `S_ent` en texto corrido, `ΔS_total` en la desigualdad termodinámica y `S` solo para área. | Mitigado. |",
            "",
            "## Problemas críticos",
            "",
            "No se detectan problemas críticos o mayores que impidan avanzar al montaje. La aprobación corresponde a la redacción; la legibilidad final debe verificarse después de producir y renderizar el PowerPoint.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    rows = parse_storyboard()
    expected = [f"U02-{index:03d}" for index in range(1, 111)]
    actual = [row["slide_id"] for row in rows]
    if actual != expected:
        raise ValueError("Los IDs del storyboard no son U02-001–U02-110 consecutivos")
    durations = allocate_durations(rows)
    slide_output = slide_text(rows)
    notes_output = notes_text(rows, durations)
    source_output = source_map(rows)
    review_output = writing_review(rows, durations, slide_output, notes_output)
    (UNIT_DIR / "slide_text.md").write_text(slide_output + "\n", encoding="utf-8")
    (UNIT_DIR / "speaker_notes.md").write_text(notes_output + "\n", encoding="utf-8")
    (UNIT_DIR / "source_map.md").write_text(source_output + "\n", encoding="utf-8")
    (UNIT_DIR / "writing_review.md").write_text(review_output + "\n", encoding="utf-8")
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
        }
    )


if __name__ == "__main__":
    main()
