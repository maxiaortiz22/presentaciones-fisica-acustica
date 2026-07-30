# Guía transversal de notación

**Propósito:** evitar cambios de símbolos, unidades y criterios de nivel entre unidades. La guía conserva la notación del libro cuando es consistente y usa calificadores solo donde existe ambigüedad.

## Reglas generales

1. Escribir las variables en cursiva matemática y las unidades en redonda.
2. Separar valor y unidad con un espacio: `20 Hz`, `0,5 s`, `94 dB SPL`.
3. Usar coma decimal en el texto en español y punto decimal solo dentro de código o archivos de datos.
4. No pluralizar ni puntuar símbolos de unidad: `5 kg`, no `5 kgs`.
5. Respetar mayúsculas: `Pa`, `N`, `J`, `W`, `Hz`; pero `m`, `s`, `kg`.
6. Usar prefijos SI sin espacio respecto de la unidad: `kHz`, `ms`, `µPa`.
7. Expresar productos de unidades con punto centrado y exponentes: `kg·m⁻³`, `W·m⁻²`.
8. Definir cada símbolo al aparecer por primera vez en una unidad y repetir la definición si reaparece después de un intervalo largo.
9. Toda ecuación debe ir acompañada por significado físico, condiciones de validez y unidades.
10. No mezclar valores instantáneos, pico, pico a pico, promedio y RMS sin subíndice.
11. No escribir un número en dB sin especificar magnitud, referencia y ponderación cuando sean relevantes.
12. Mantener las ecuaciones editables en los entregables posteriores.

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
| potencia mecánica | `P` | W | 2 | Para potencia acústica se conserva `W_\mathrm{ac}` según uso del libro, pero `P_\mathrm{ac}` es aceptable si se acuerda globalmente. |
| calor transferido | `Q_\mathrm{calor}` | J | 2 | Evita colisión con factor de directividad `Q_\mathrm{dir}`. |
| entropía | `S_\mathrm{ent}` | J·K⁻¹ | 2 | El calificador evita colisión con área `S`. |
| constante elástica | `k_\mathrm{s}` | N·m⁻¹ | 2 | Evita colisión con número de onda. |
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
| período | `T` | s | `T=1/f`. |
| frecuencia | `f` | Hz | `1 Hz = 1 s⁻¹`. |
| frecuencia angular | `ω` | rad·s⁻¹ | `ω=2πf`; el radián es adimensional, pero se conserva para claridad. |
| fase inicial | `φ_0` | rad | Si se usan grados, indicarlo explícitamente y no mezclarlos en una ecuación. |
| longitud de onda | `λ` | m | `λ=c/f` para el medio y modo definidos. |
| número de onda | `k_\mathrm{onda}` | rad·m⁻¹ | `k_\mathrm{onda}=2π/λ`; usar calificador si aparece `k_s`. |
| velocidad de propagación | `c` | m·s⁻¹ | Para sonido en aire puede escribirse `c_\mathrm{aire}`. |
| velocidad de partícula | `u(t)` | m·s⁻¹ | No usar `v` si puede confundirse con propagación. |
| velocidad de un cuerpo | `v(t)` | m·s⁻¹ | Reservar para movimiento macroscópico. |

Forma preferida de una oscilación:

```text
x(t) = A_x cos(ωt + φ₀)
```

Forma preferida de una onda armónica unidimensional:

```text
p(x,t) = p̂ cos(ωt − k_onda x + φ₀)
```

El signo del término espacial depende de la convención de dirección. Una vez elegida, no debe cambiar dentro de una misma explicación.

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
| intensidad sonora | `I` | W·m⁻² | Promedio temporal del flujo de potencia por área. |
| intensidad de referencia | `I_\mathrm{ref}` | W·m⁻² | Declarar cuando se use nivel de intensidad. |
| potencia acústica | `W_\mathrm{ac}` | W | El símbolo y la unidad coinciden tipográficamente si se escribe `W`; mantener subíndice. |
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
| nivel de audición | nivel en dB HL | cero audiométrico normativo | `dB HL`, frecuencia y transductor |
| nivel de sensación | nivel en dB SL | umbral individual | `dB SL re umbral ...` |
| nivel de sonoridad | `L_N` si se necesita | comparación psicofísica | unidad: fon, no dB |
| sonoridad | `N` | escala de razones perceptuales | unidad: son |

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
| frecuencia fundamental | `f_0` | Hz | No usar `F0` salvo texto de software; conservar `f_0` en ecuaciones. |
| frecuencia de muestreo | `f_s` | Hz | `f_s=1/T_s`. |
| período de muestreo | `T_s` | s | No confundir con período de la señal. |
| número de muestras | `N` | 1 | Entero; no confundir con sonoridad si comparten contexto. |
| duración observada | `T_\mathrm{obs}` | s | Determina resolución nominal. |
| separación entre bins | `Δf` | Hz | En DFT simple, `Δf=f_s/N=1/T_obs`. |
| respuesta en frecuencia | `H(f)` | razón o unidad definida | Sistema: `H(f)=Y(f)/X(f)` cuando procede. |
| frecuencia de corte inferior/superior | `f_L`, `f_H` | Hz | Declarar criterio de corte. |
| frecuencia central | `f_c` | Hz | Para banda geométrica: `f_c=√(f_L f_H)`. |
| ancho de banda | `B` o `Δf_B` | Hz | No confundir con separación de bins `Δf`. |
| densidad espectral de potencia | `S_x(f)` | unidad de `x²`/Hz | Para presión: Pa²/Hz. |
| relación señal-ruido | `SNR` | dB o razón | Si está en dB: `10 log₁₀(P_s/P_n)` bajo condiciones compatibles. |

Para gráficos espectrales, indicar:

- señal y variable analizada;
- frecuencia de muestreo y duración, si afectan la interpretación;
- ventana;
- escala de amplitud (lineal, potencia o dB);
- referencia del eje vertical;
- rango de frecuencias.

## Audición y psicoacústica

| Concepto | Símbolo/abreviatura | Unidad | Convención |
|---|---:|---:|---|
| umbral auditivo | `L_\mathrm{umbral}(f)` | dB SPL o dB HL | Declarar procedimiento y escala. |
| nivel de sonoridad | `L_N` | fon | Relativo a tono de referencia según procedimiento. |
| sonoridad | `N_\mathrm{son}` | son | Calificar si aparece `N` de número de muestras. |
| tiempo de reverberación | `T_60` | s | Si se estima desde 20 o 30 dB, indicar `T_20`/`T_30` y extrapolación. |
| pérdida de consonantes | `ALCons` | % | Usar solo dentro del modelo y condiciones que lo sustentan. |
| diferencia interaural de tiempo | `ITD` | µs o ms | Desarrollar sigla en español. |
| diferencia interaural de nivel | `ILD` | dB | Puede variar con frecuencia y posición. |
| ancho de banda rectangular equivalente | `ERB` | Hz | Definir el modelo empleado. |

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
| coeficiente de reflexión energético | `R_E` | 1 | `0≤R_E≤1`; no confundir con coeficiente de presión. |
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
| `W` | trabajo, potencia acústica, watt | `W_trab`, `W_ac`; unidad `W` en redonda. |
| `p_0` | presión estática o presión de referencia | `p_0` para estática; `p_ref` para referencia de nivel. |
| `R` | reflexión, resistencia, aislamiento | `R_E` para reflexión energética; `R` solo para índice de reducción con rótulo. |
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

- Elegir definitivamente `P_ac` o `W_ac` para potencia acústica.
- Confirmar notación aceptada en Audiología para PEAT/PEATC y escalas de nivel.
- Elegir la norma que fijará descriptores de sonómetro, exposición y cabina.
- Decidir cuánta notación de DFT/FFT será obligatoria frente a opcional.
- Confirmar si se usará nomenclatura latina `scala media/vestibuli/tympani` o equivalentes españoles en texto visible.
