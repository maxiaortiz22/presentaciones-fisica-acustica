# Guía transversal de notación

**Propósito:** evitar cambios de símbolos, unidades y criterios de nivel entre unidades. La guía conserva la notación del libro cuando es consistente y usa calificadores solo donde existe ambigüedad.

## Reglas generales

1. Escribir las variables en cursiva matemática y las unidades en redonda.
2. Separar valor y unidad con un espacio: `20 Hz`, `0,5 s`, `94 dB SPL`.
3. Usar coma decimal en el texto en español y en los rótulos y ticks de gráficos destinados al aula; reservar el punto decimal para código o archivos de datos.
4. No pluralizar ni puntuar símbolos de unidad: `5 kg`, no `5 kgs`.
5. Respetar mayúsculas: `Pa`, `N`, `J`, `W`, `Hz`; pero `m`, `s`, `kg`.
6. Usar prefijos SI sin espacio respecto de la unidad: `kHz`, `ms`, `µPa`.
7. Expresar productos de unidades con punto centrado y exponentes: `kg·m⁻³`, `W·m⁻²`.
8. Definir cada símbolo al aparecer por primera vez en una unidad y repetir la definición si reaparece después de un intervalo largo.
9. Toda ecuación debe ir acompañada por significado físico, condiciones de validez y unidades.
10. No mezclar valores instantáneos, pico, pico a pico, promedio y RMS sin subíndice.
11. No escribir un número en dB sin especificar magnitud, referencia y ponderación cuando sean relevantes.
12. Mantener las ecuaciones editables en los entregables posteriores.
13. En el material visible, representar subíndices y valor absoluto con tipografía matemática: `L_N`, `N_\mathrm{son}`, `T_60`, `f_\mathrm{obj}` y `\lvert\Delta t_\mathrm{LR}\rvert`. Los guiones bajos pueden aparecer en Markdown o código, pero no deben convertirse en paréntesis como `L(N)`, `T(60)` o `f(obj)`, ni en funciones de programación como `abs(...)`.

## Magnitudes básicas y mecánicas

| Magnitud | Símbolo preferido | Unidad SI | Primera unidad | Convención |
|---|---:|---:|---:|---|
| tiempo | `t` | s | 1 | Variable temporal. |
| intervalo de tiempo | `Δt` | s | 1 | No usar `T` salvo que sea período o tiempo de observación definido. |
| distancia/posición | `x`, `r` | m | 1 | `x` para eje/desplazamiento; `r` para distancia radial a una fuente. |
| desplazamiento | `x(t)` | m | 1 | Si es amplitud de desplazamiento, usar `x_0` o `\hat{x}`. |
| masa | `m` | kg | 1 | No usar `M` salvo variable distinta definida. |
| aceleración | `a` | m·s⁻² | 2 | Aceleración gravitatoria: `g`. |
| fuerza | `F` | N | 1 | Resultante formal: `ΣF`. Se admite `F_\mathrm{neta}` como rótulo didáctico después de definirlo; no alternar ambas formas sin explicación. |
| fuerza debida a presión | `F_\mathrm{pres}` | N | 2 | Para presión uniforme sobre un área: `F_pres=Δp·S`; declarar eje y signo. |
| fuerza elástica | `F_\mathrm{el}` | N | 2 | En el modelo lineal unidimensional: `F_el=−k_s x`. |
| fuerza de amortiguamiento | `F_\mathrm{amort}` | N | 2 | En el modelo viscoso lineal: `F_amort=−bv`. |
| área | `S` | m² | 1 | Se prefiere `S` para evitar colisión con amplitud `A`. Si se conserva `A` de una fuente, aclarar localmente. |
| volumen geométrico | `V` | m³ | 1 | No usar “volumen” para sonoridad. |
| densidad | `ρ` | kg·m⁻³ | 1 | Densidad de equilibrio del medio: `ρ_0`. |
| presión estática | `p_0` | Pa | 1 | No confundir con presión acústica de referencia. |
| temperatura | `T_\mathrm{temp}` o `θ` | K o °C | 2 | En fórmulas termodinámicas usar K; evitar colisión con período `T`. |
| trabajo | `W_\mathrm{trab}` | J | 2 | Calificar si comparte contexto con potencia acústica o watt. En la primera ley puede usarse `W_\mathrm{sobre}` para el trabajo sobre el sistema. |
| energía | `E` | J | 2 | Añadir subíndice: `E_k`, `E_p`, `E_\mathrm{ac}`. |
| potencia mecánica | `P` | W | 2 | Para potencia acústica se usa `W_\mathrm{ac}` como convención transversal; `P_\mathrm{ac}` queda reservado para citas o fuentes externas que deban conservarse. |
| calor transferido | `Q_\mathrm{calor}` | J | 2 | Evita colisión con factor de directividad `Q_\mathrm{dir}`. |
| entropía | `S_\mathrm{ent}` | J·K⁻¹ | 2 | El calificador evita colisión con área `S`. |
| constante elástica | `k_\mathrm{s}` | N·m⁻¹ | 2 | Evita colisión con número de onda. |
| módulo volumétrico adiabático | `K_\mathrm{s}` | Pa | 4 | La mayúscula es significativa: no confundir con la constante elástica `k_s` de un resorte. |
| coeficiente de amortiguamiento | `b` | N·s·m⁻¹ | 2 | Declarar el modelo al que pertenece. |

### Convención de balance energético adoptada en la Unidad 2

- En mecánica, usar `W_\mathrm{trab}` para nombrar el trabajo como transferencia producida por una fuerza y un desplazamiento.
- En la primera ley, usar `W_\mathrm{sobre}` cuando el signo indica explícitamente trabajo realizado **sobre** el sistema:

```text
ΔU = Q_calor + W_sobre
```

- Con esta convención, `Q_calor>0` y `W_sobre>0` representan energía que entra al sistema.
- Si se usa trabajo realizado **por** el sistema, invertir el signo y explicitar el cambio de convención.
- En texto visible final, representar los calificadores como subíndices tipográficos. El guion bajo se reserva para Markdown, código, nombres de objetos o una limitación técnica documentada.

## Oscilaciones y ondas

| Magnitud | Símbolo preferido | Unidad | Convención |
|---|---:|---:|---|
| amplitud de una variable `x` | `A_x` o `\hat{x}` | unidad de `x` | Usar `A` sola solo si no hay área ni otra amplitud en el contexto. |
| amplitud resultante | `A_R` | unidad de las señales sumadas | Usar solo cuando las contribuciones representan la misma magnitud; no sumar amplitudes sin considerar fase. |
| período | `T` | s | `T=1/f`. |
| frecuencia | `f` | Hz | `1 Hz = 1 s⁻¹`. |
| frecuencia angular | `ω` | rad·s⁻¹ | `ω=2πf`; el radián es adimensional, pero se conserva para claridad. |
| fase inicial | `φ_0` | rad | Si se usan grados, indicarlo explícitamente y no mezclarlos en una ecuación. |
| longitud de onda | `λ` | m | `λ=c/f` para el medio y modo definidos. |
| número de onda | `k_\mathrm{onda}` | rad·m⁻¹ | `k_\mathrm{onda}=2π/λ`; usar calificador si aparece `k_s`. |
| rapidez de propagación | `c` | m·s⁻¹ | Para sonido en aire puede escribirse `c_\mathrm{aire}`. “Velocidad de propagación” es aceptable como término acústico convencional si no genera ambigüedad vectorial. |
| velocidad de partícula | `u(t)` | m·s⁻¹ | No usar `v` si puede confundirse con propagación. |
| velocidad de un cuerpo | `v(t)` | m·s⁻¹ | Reservar para movimiento macroscópico. |
| perturbación genérica | `ξ(x,t)` | declarar según la variable | Se admite en U3 para enseñar dependencia espacial y temporal antes de elegir una magnitud acústica específica. |

Forma preferida de una oscilación:

```text
x(t) = A_x cos(ωt + φ₀)
```

Forma preferida de una onda armónica unidimensional:

```text
p(x,t) = p̂ cos(ωt − k_onda x + φ₀)
```

El signo del término espacial depende de la convención de dirección. Una vez elegida, no debe cambiar dentro de una misma explicación.

En U3 se admite la forma genérica:

```text
ξ(x,t) = A_ξ cos(ωt − k_onda x + φ₀)
```

si `ξ` y `A_ξ` se definen con su unidad. Desde U4, cuando la magnitud ya está identificada, se prefiere `p(x,t)`, `u(x,t)` u otra variable física específica. En una cadena de transducción de U3 puede usarse `p_ac(t)` como rótulo transitorio para distinguir presión acústica de presión estática; al formalizar valores pico, RMS y niveles se vuelve a `p(t)`, `p̂` y `p_rms`.

## Magnitudes acústicas lineales

| Magnitud | Símbolo preferido | Unidad | Observación |
|---|---:|---:|---|
| presión acústica instantánea | `p(t)` o `p(x,t)` | Pa | Variación respecto de `p_0`. |
| presión pico | `\hat{p}` o `p_\mathrm{pico}` | Pa | Para senoide, `p_\mathrm{rms}=\hat{p}/√2`. |
| presión pico a pico | `p_\mathrm{pp}` | Pa | Para senoide simétrica, `p_pp=2\hat{p}`. |
| presión eficaz | `p_\mathrm{rms}` | Pa | Definir ventana/promedio en señales no estacionarias. |
| presión de referencia | `p_\mathrm{ref}` | Pa | En aire, habitualmente 20 µPa; bajo agua suele emplearse 1 µPa. Declarar siempre. |
| velocidad de partícula | `u(t)` | m·s⁻¹ | Valor instantáneo; usar `u_rms` si corresponde. |
| impedancia acústica específica | `Z` | Pa·s·m⁻¹ | En general compleja; en onda plana progresiva ideal `Z≈ρc`. |
| impedancia característica del medio | `Z_0` | Pa·s·m⁻¹ | En una onda plana progresiva ideal de un medio homogéneo y sin pérdidas, `Z_0=ρ_0c`. No sustituye a `Z` en un campo general. |
| intensidad acústica instantánea | `i(t)` | W·m⁻² | `i(t)=p(t)u(t)` para componentes colineales y convención de signo declarada; puede ser negativa. |
| intensidad sonora | `I` | W·m⁻² | Promedio temporal del flujo de potencia por área. |
| intensidad de referencia | `I_\mathrm{ref}` | W·m⁻² | Declarar cuando se use nivel de intensidad. |
| potencia acústica | `W_\mathrm{ac}` | W | Convención transversal del curso. El símbolo y la unidad coinciden tipográficamente si se escribe `W`; mantener subíndice. |
| potencia de referencia | `W_\mathrm{ref}` | W | Declarar según el contexto. |
| energía acústica | `E_\mathrm{ac}` | J | No confundir con exposición sonora. |
| factor de directividad | `Q_\mathrm{dir}` | 1 | Adimensional; evita colisión con calor. |
| índice de directividad | `DI` | dB | `DI=10 log₁₀(Q_dir)`. |

## Promedios y descriptores temporales

- Promedio de una variable en el intervalo `T_\mathrm{obs}`:

```text
⟨x⟩ = (1/T_obs) ∫ x(t) dt
```

- Valor eficaz:

```text
x_rms = √[(1/T_obs) ∫ x²(t) dt]
```

- No usar “promedio” para referirse informalmente a RMS.
- En una senoide simétrica, el promedio temporal de `p(t)` es cero, pero `p_rms` no.
- Para señales variables, declarar duración, constante temporal o ventana de integración.

## Niveles logarítmicos

Convención general:

```text
L_X = 10 log₁₀(X/X_ref)
```

para magnitudes proporcionales a potencia, y:

```text
L_x = 20 log₁₀(x/x_ref)
```

solo cuando `x²` es proporcional a la magnitud de potencia bajo las mismas condiciones de impedancia.

| Descriptor | Símbolo | Expresión o referencia | Escritura recomendada |
|---|---:|---|---|
| nivel de presión sonora | `L_p` | `20 log₁₀(p_rms/p_ref)` | `85 dB SPL` o `L_p = 85 dB re 20 µPa` |
| nivel de intensidad sonora | `L_I` | `10 log₁₀(I/I_ref)` | declarar `I_ref` |
| nivel de potencia sonora | `L_W` | `10 log₁₀(W_ac/W_ref)` | no confundir con potencia en W |
| nivel continuo equivalente | `L_eq,T` | energía cuadrática media en `T` | incluir intervalo |
| equivalente ponderado A | `L_Aeq,T` | ponderación A e intervalo `T` | preferido frente a “Leq dBA” aislado |
| nivel máximo A, Fast | `L_AFmax` | ponderación A, respuesta temporal F | no equivale a pico |
| nivel pico C | `L_Cpeak` | ponderación C, detector de pico | declarar configuración |
| corrección A para un tono | `A(f)` | dB | Bajo condiciones verificadas, `L_A(f)=L_Z(f)+A(f)`; no aplicar una corrección única a banda ancha. |
| nivel de audición | nivel en dB HL | cero audiométrico normativo | `dB HL`, frecuencia y transductor |
| nivel de sensación | nivel en dB SL | umbral individual | `dB SL re umbral ...` |
| nivel de sonoridad | `L_N` si se necesita | comparación psicofísica | unidad: fon, no dB |
| sonoridad | `N_\mathrm{son}` | escala de razones perceptuales | unidad: son; evita colisión con el número de muestras `N` de U5 |

Reglas:

- No sumar aritméticamente niveles en dB. Convertir a magnitudes lineales compatibles, sumar y volver a nivel.
- Para fuentes no correlacionadas, sumar intensidades o valores cuadrados medios.
- Para fuentes coherentes, considerar amplitud y fase antes de promediar.
- No convertir dB SPL a dB HL sin datos de referencia y transductor.
- No comparar mediciones en aire y agua solo por su valor numérico en dB.
- La forma `dBA` puede aparecer en material original, pero en expresiones técnicas se prefiere `dB(A)` o un descriptor como `L_Aeq,T`.

## Señales y análisis frecuencial

| Magnitud o entidad | Símbolo preferido | Unidad | Convención |
|---|---:|---:|---|
| señal temporal | `x(t)` | según variable | Para presión: `p(t)`. |
| transformada de Fourier | `X(f)` | depende de convención | Declarar convención si se calculan amplitudes absolutas. |
| ventana temporal | `w(t)` | 1 | Declarar tipo y parámetros cuando afecten la lectura. |
| señal ventaneada | `x_w(t)` | unidad de `x` | `x_w(t)=x(t)w(t)`; el subíndice debe verse tipográficamente. |
| frecuencia fundamental | `f_0` | Hz | No usar `F0` salvo texto de software; conservar `f_0` en ecuaciones. |
| frecuencia de muestreo | `f_s` | Hz | `f_s=1/T_s`. |
| período de muestreo | `T_s` | s | No confundir con período de la señal. |
| número de muestras | `N` | 1 | Entero; no confundir con sonoridad si comparten contexto. |
| duración observada | `T_\mathrm{obs}` | s | Determina resolución nominal. |
| separación entre bins | `Δf` | Hz | En DFT simple, `Δf=f_s/N=1/T_obs`. |
| índice de bin | `k` | 1 | Entero; no confundir con `k_s` ni `k_onda`. |
| frecuencia del bin `k` | `f_k` | Hz | En la convención básica, `f_k=k f_s/N=kΔf`. |
| respuesta en frecuencia | `H(f)` | razón o unidad definida | Sistema: `H(f)=Y(f)/X(f)` cuando procede. |
| fase de la respuesta | `φ_H(f)` | rad | Declarar convención de signo y fase; usar grados solo si se indica. |
| retardo de sistema | `τ_d` | s | Para retardo puro, `φ_H(f)=−2πfτ_d`; evita colisión con transmisión en U9. |
| ganancia de amplitud | `G(f)` | dB | `G(f)=20 log₁₀\lvert H(f)\rvert` solo para razones de amplitudes compatibles. |
| frecuencia de corte inferior/superior | `f_L`, `f_H` | Hz | Declarar criterio de corte. |
| frecuencia central | `f_c` | Hz | Para banda geométrica: `f_c=√(f_L f_H)`. |
| ancho de banda | `B` o `Δf_B` | Hz | No confundir con separación de bins `Δf`. |
| nivel integrado en banda | `L_B` | dB | Declarar magnitud integrada `q_B`, límites de banda y referencia. |
| densidad espectral de potencia | `S_x(f)` | unidad de `x²`/Hz | Para presión: Pa²/Hz. |
| relación señal-ruido | `SNR` | dB o razón | Si está en dB: `10 log₁₀(P_s/P_n)` bajo condiciones compatibles. |

Para gráficos espectrales, indicar:

- señal y variable analizada;
- frecuencia de muestreo y duración, si afectan la interpretación;
- ventana;
- escala de amplitud (lineal, potencia o dB);
- referencia del eje vertical;
- rango de frecuencias.

## Oído medio y transducción coclear

| Magnitud | Símbolo | Unidad | Convención |
|---|---:|---:|---|
| diferencia de presión | `Δp` | Pa | Declarar el orden de la resta y las dos regiones comparadas. |
| área efectiva de la membrana timpánica | `S_TM` | m² | Usar `S` para área efectiva en este bloque; no confundir con entropía ni densidad espectral. |
| área efectiva del estribo | `S_E` | m² | Declarar que se trata de un área efectiva del modelo. |
| razón de áreas | `R_S=S_TM/S_E` | 1 | Razón adimensional; no llamarla ganancia energética. |
| razón de palanca osicular | `R_L` | 1 | Razón adimensional; declarar la geometría o convención adoptada. |
| razón ideal de presiones | `M_p≈R_S·R_L` | 1 | Reservar `R_p` para el coeficiente de reflexión de presión definido en U4/U9. |
| expresión en decibelios de la razón ideal de presiones | `G_p=20 log₁₀(M_p)` | dB | No es dB SPL ni ganancia de energía; identificar siempre las dos presiones comparadas. |
| longitud efectiva del conducto | `ℓ` | m | En el modelo de cuarto de onda, escribir `f_res≈c/(4ℓ)` y declarar sus límites. |
| diferencia de potencial | `ΔV` | V o mV | Especificar los dos puntos o compartimentos entre los que se mide. |
| potencial respecto de una referencia | `V_ref` | V o mV | Nombrar la referencia física; evitar valores de potencial aislados y la forma ambigua `V(ref)`. |

## Audición y psicoacústica

| Concepto | Símbolo/abreviatura | Unidad | Convención |
|---|---:|---:|---|
| umbral auditivo | `L_\mathrm{umbral}(f)` | dB SPL o dB HL | Declarar procedimiento y escala. |
| nivel umbral en quietud | `L_{\mathrm{umbral,q}}(f_\mathrm{obj})` | dB con referencia declarada | La coma `q` identifica quietud; mantener frecuencia objetivo, procedimiento y referencia. |
| nivel umbral enmascarado | `L_{\mathrm{umbral,e}}(f_\mathrm{obj})` | dB con la misma referencia | La coma `e` identifica presencia del enmascarador; debe compararse con el umbral en quietud bajo el mismo procedimiento. |
| cantidad de enmascaramiento | `M(f_\mathrm{obj})` | dB | `M=L_{\mathrm{umbral,e}}-L_{\mathrm{umbral,q}}`; no es el nivel del enmascarador. |
| diferencia campo–tímpano | `G_\mathrm{CT}(f)` | dB | `G_\mathrm{CT}=L_{p,\mathrm{T}}-L_{p,\mathrm{campo}}` para la misma frecuencia, campo, posición y procedimiento; no es ganancia de sonoridad. |
| nivel de sonoridad | `L_N` | fon | Relativo a tono de referencia según procedimiento. |
| sonoridad | `N_\mathrm{son}` | son | Calificar si aparece `N` de número de muestras. |
| tiempo de reverberación | `T_60` | s | Si se estima desde 20 o 30 dB, indicar `T_20`/`T_30` y extrapolación. |
| relación señal-ruido | `SNR` | dB o razón | Para niveles comparables, `SNR=L_{p,\mathrm{s}}-L_{p,\mathrm{n}}`; declarar posición, banda, ponderación, referencia e intervalo. |
| pérdida de consonantes | `ALCons` | % | `ALCons=100(1-n_\mathrm{c}/n_\mathrm{p})\,%`, con `n_p` presentadas y `n_c` correctas; describe la prueba observada, no una predicción universal. |
| diferencia interaural de tiempo | `ITD` o `\Delta t_\mathrm{LR}` | µs o ms | Desarrollar sigla en español y declarar el orden izquierda–derecha; para una cota usar `\lvert\Delta t_\mathrm{LR}\rvert`. |
| diferencia interaural de nivel | `ILD` | dB | `ILD=L_{p,\mathrm{L}}-L_{p,\mathrm{R}}` con niveles comparables; puede variar con frecuencia y posición. |
| ancho de banda rectangular equivalente | `ERB` o `\mathrm{ERB}_N(f_c)` | Hz | Definir modelo y frecuencia central; el subíndice `N` se conserva cuando identifica la aproximación para audición normal del modelo utilizado. |

## Audiología y rehabilitación

| Término | Escritura | Regla |
|---|---|---|
| nivel de presión sonora | dB SPL | Referencia física declarada. |
| nivel de audición | dB HL | Referencia audiométrica específica por frecuencia/transductor. |
| nivel de sensación | dB SL | Referido al umbral individual en la condición indicada. |
| desplazamiento temporal del umbral | TTS | Desarrollar en primera aparición; indicar tiempo postexposición. |
| hipoacusia inducida por ruido | HIR o NIHL | Elegir una sigla institucional y mantenerla. |
| otoemisiones acústicas | OEA | Se admiten DPOAE/TEOAE solo después de desarrollar. |
| potenciales evocados auditivos de tronco | PEAT/PEATC | Validar forma preferida por la cátedra; si se usa ABR, desarrollar. |
| células ciliadas internas/externas | CCI/CCE | Desarrollar por unidad. |

## Propagación y recintos

| Magnitud | Símbolo | Unidad | Convención |
|---|---:|---:|---|
| coeficiente de reflexión de presión | `R_p` | 1 | Razón de amplitudes de presión; puede incluir signo o fase. Definir incidencia y medios. |
| coeficiente de reflexión de intensidad | `R_I` | 1 | Razón entre intensidades medias reflejada e incidente; `0≤R_I≤1` en el caso pasivo ideal. |
| coeficiente de reflexión energético genérico | `R_E` | 1 | Usar solo cuando la fuente o un balance energético requiera esa denominación; no sustituir automáticamente a `R_I`. |
| coeficiente de absorción | `α` | 1 | Dependiente de frecuencia y condiciones de montaje. |
| coeficiente de transmisión energético | `τ` | 1 | En balance ideal sin otras pérdidas: `R_E+α+τ=1`, según definiciones. |
| área de absorción equivalente | `A_\mathrm{eq}` | m² sabin | Evita colisión con amplitud. |
| volumen del recinto | `V` | m³ | Aquí “volumen” sí es magnitud geométrica. |
| tiempo de reverberación | `T_60` | s | No usar `RT60` dentro de ecuaciones; puede aparecer como etiqueta desarrollada. |
| índice de reducción sonora | `R` | dB | No confundir con coeficiente de reflexión; calificar en texto. |

Si se usa la fórmula de Sabine:

```text
T_60 = 0,161 V/A_eq
```

debe indicarse que la constante corresponde a unidades SI y a condiciones aproximadas del modelo.

## Estadística del ruido

| Magnitud | Símbolo | Unidad | Convención |
|---|---:|---:|---|
| media | `μ_x` o `\bar{x}` | unidad de `x` | Distinguir media poblacional y muestral si se formaliza. |
| varianza | `σ_x²` | unidad de `x²` | No es RMS; para media cero, RMS² coincide con varianza. |
| desviación estándar | `σ_x` | unidad de `x` | Indicar intervalo de análisis. |
| autocorrelación | `R_xx(τ)` | unidad de `x²` | `τ` es retardo, no coeficiente de transmisión. |
| densidad espectral de potencia | `S_x(f)` | unidad de `x²`/Hz | Relacionada con autocorrelación bajo condiciones de estacionariedad. |
| nivel de exposición sonora | `L_AE` o descriptor normativo elegido | dB | No fijar símbolo definitivo sin norma adoptada. |

## Colisiones de símbolos y resolución

| Símbolo en fuentes | Usos posibles | Regla transversal propuesta |
|---|---|---|
| `A` | amplitud, área, absorción equivalente | `A_x` para amplitud; `S` para área; `A_eq` para absorción equivalente. |
| `Q` | calor, factor de directividad | `Q_calor` y `Q_dir`. |
| `k` | constante elástica, número de onda | `k_s` y `k_onda`. |
| `T` | período, temperatura, duración | `T` para período; `T_temp`/`θ` para temperatura; `T_obs` para observación. |
| `S` | área, entropía, densidad espectral | `S` para área solo si no hay espectro; `S_ent`; `S_x(f)` para PSD. |
| `W` | trabajo, potencia acústica, watt | `W_trab`, `W_ac`; unidad `W` en redonda. `P_ac` solo al conservar notación externa explícita. |
| `p_0` | presión estática o presión de referencia | `p_0` para estática; `p_ref` para referencia de nivel. |
| `R` | reflexión, resistencia, aislamiento | `R_p` para presión reflejada, `R_I` para razón de intensidades y `R_E` solo para fracción energética genérica definida; `R` solo para índice de reducción con rótulo. |
| `N` | número de muestras, sonoridad | `N` para muestras; `N_son` en psicoacústica si coinciden. |
| `τ` | retardo, coeficiente de transmisión | `τ_d` para retardo si aparece junto a transmisión; `τ_E` para transmisión. |

## Estándar para gráficos y tablas

- Eje horizontal: nombre de magnitud, símbolo y unidad; ejemplo: `Frecuencia, f (Hz)`.
- Eje vertical: descriptor completo y referencia; ejemplo: `Nivel de presión sonora, L_p (dB re 20 µPa)`.
- Usar escala logarítmica solo si se identifica visualmente y tiene sentido físico.
- No truncar ejes de modo que altere la interpretación sin advertencia.
- En curvas normativas, indicar norma, edición y condiciones.
- En curvas conceptuales, rotular **esquema conceptual; no usar para lectura normativa**.
- Mantener colores y estilos iguales para las mismas entidades a través de unidades una vez aprobado el sistema visual.
- Toda figura con datos externos debe registrar fuente; toda figura simulada debe registrar ecuación, parámetros y script.

## Comprobación mínima por ecuación

Antes de aprobar una ecuación para material docente:

- [ ] todos los símbolos están definidos;
- [ ] las unidades son coherentes;
- [ ] se explican las hipótesis;
- [ ] se distingue igualdad exacta de aproximación;
- [ ] se aclara si el valor es instantáneo, medio, RMS o nivel;
- [ ] la referencia logarítmica está declarada;
- [ ] el ejemplo numérico conserva cifras significativas razonables;
- [ ] el resultado incluye unidad e interpretación física;
- [ ] no colisiona con un símbolo usado en la misma unidad.

## Pendientes de validación docente

- Confirmar notación aceptada en Audiología para PEAT/PEATC y escalas de nivel.
- Elegir la norma que fijará descriptores de sonómetro, exposición y cabina.
- Decidir cuánta notación de DFT/FFT será obligatoria frente a opcional.
- Confirmar si se usará nomenclatura latina `scala media/vestibuli/tympani` o equivalentes españoles en texto visible.
