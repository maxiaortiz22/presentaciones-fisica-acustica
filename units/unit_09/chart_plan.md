# Unidad 9 — Plan de gráficos propios

Versión de planificación · 2026-08-12

## Clasificación obligatoria previa a producción

Los recursos U09-CH-001 a U09-CH-011 se clasifican como **gráfico cuantitativo**. Esta clasificación se conserva aun cuando los datos sean calculados por fórmula o sintéticos y conceptuales; en esos casos la condición se declara dentro del recurso. U09-CH-010 y U09-CH-011 permanecen clasificados, pero no se generan ni se aprueban mientras continúen bloqueados por fuente, permiso o decisión institucional.

## Contrato de producción

Todos los recursos de este archivo se clasifican como `gráfico cuantitativo` antes de generarse, aunque una slide pueda ser `mixed` al combinar el gráfico con ecuación o diagrama. Se producirán mediante `chart-generation` con Python, NumPy y Matplotlib.

Por gráfico se conservarán:

```text
units/unit_09/scripts/u09_plot_NNN_nombre.py
units/unit_09/assets/generated/charts/U09-CH-NNN/
├── data.csv o parameters.json
├── figure.svg
├── figure.png
├── README.md
├── caption.txt
└── alt_text.txt
```

Especificación común:

- fondo blanco o transparente;
- `FA_CARBON_900` para ejes y texto, `FA_GRIS_200` para grilla tenue;
- bordó o teal para la serie principal; segunda/tercera serie con gris u ocre y patrón/etiqueta;
- máximo tres series;
- etiquetas de ejes ≥20 pt equivalentes, ticks/leyenda ≥18 pt y anotaciones ≥22 pt;
- SVG como salida principal y PNG 2400 × 1350 px o mayor como respaldo;
- ningún título duplicado dentro del gráfico;
- prueba en el tamaño físico final del layout, no solo en el canvas aislado.

## Especificaciones

### U09-CH-001 — Cambio ideal de nivel con razón de distancias

- **Slides:** U09-014; apoyo opcional U09-015/016.
- **Pregunta:** ¿cómo cambia `L_p` al variar `r₂/r₁`?
- **Mensaje:** la razón, no la distancia aislada, determina `ΔL_p` en el modelo ideal.
- **Tipo:** curva matemática.
- **Variables/unidades:** `x=r₂/r₁` adimensional; `y=ΔL_p` en dB.
- **Escala/rango:** x logarítmica, 0,25–8; y lineal, aproximadamente +12 a −18 dB.
- **Modelo:** `ΔL_p=−20 log10(r₂/r₁)`.
- **Anotaciones:** marcadores 0,5, 1, 2 y 4; destacar `(2, −6,02 dB)`; banda textual externa “campo libre aproximado, campo lejano, misma dirección”.
- **Tamaño final:** panel de 5,0 × 3,2 in dentro de `FA_09_ECUACION_INTERPRETACION`.
- **Script:** `units/unit_09/scripts/u09_plot_001_distancia.py`.
- **Salidas:** SVG + PNG; `parameters.json` con rango y marcadores.
- **Validaciones:** signo, monotonicidad, `ΔL_p(1)=0`, simetría logarítmica, ausencia de interpretación fuera de hipótesis.
- **Estado:** aprobado · generado y validado el 2026-08-12.

### U09-CH-002 — Patrón polar sintético por frecuencia

- **Slides:** U09-018.
- **Pregunta:** ¿por qué una fuente real no tiene un único patrón direccional?
- **Mensaje:** el patrón puede estrecharse o desarrollar lóbulos al cambiar la frecuencia.
- **Tipo:** tres gráficos polares sintéticos coordinados.
- **Variables/unidades:** ángulo en grados; nivel relativo normalizado en dB.
- **Escala/rango:** misma escala radial en los tres paneles, 0 a −18 dB; 0° orientado hacia la derecha o arriba, definido en README.
- **Modelo:** funciones analíticas sintéticas normalizadas, no mediciones ni ficha de producto; parámetros explícitos en JSON.
- **Anotaciones:** frecuencia baja/media/alta como categorías o valores didácticos; eje de máxima emisión; rótulo “ejemplo sintético”.
- **Tamaño final:** 10,8 × 4,4 in en `FA_07_GRAFICO_EXPLICACION`.
- **Script:** `units/unit_09/scripts/u09_plot_002_patron_polar.py`.
- **Salidas:** SVG + PNG + `parameters.json`.
- **Validaciones:** igual referencia radial, máximo 0 dB, no confundir área dibujada con potencia, legibilidad de grilla polar a 25 %.
- **Estado:** aprobado como ejemplo sintético · generado y validado el 2026-08-12.

### U09-CH-003 — Rapidez del sonido frente a temperatura

- **Slides:** U09-023.
- **Pregunta:** ¿cuánto cambia `c` en el intervalo térmico de clase?
- **Mensaje:** dentro del rango declarado, `c` aumenta linealmente aproximadamente 0,6 m·s⁻¹ por °C.
- **Tipo:** recta calculada.
- **Variables/unidades:** temperatura `θ` en °C; rapidez `c` en m·s⁻¹.
- **Escala/rango:** x lineal −10 a 35 °C; y lineal ajustada al rango 325–355 m·s⁻¹ sin truncamiento engañoso; declarar que el eje se enfoca en el intervalo.
- **Modelo:** `c≈331+0,6θ` del capítulo.
- **Anotaciones:** 5 °C, 20 °C y 25 °C; flecha “cambia `c`, no la frecuencia emitida”.
- **Tamaño final:** 6,8 × 4,2 in.
- **Script:** `units/unit_09/scripts/u09_plot_003_c_temperatura.py`.
- **Salidas:** SVG + PNG + CSV calculado.
- **Validaciones:** unidades, valores 334/343/346 m·s⁻¹, rango de aproximación visible, cero extrapolación silenciosa.
- **Estado:** aprobado · generado y validado el 2026-08-12.

### U09-CH-004 — Llegada directa, reflexión y cola reverberante

- **Slides:** U09-039.
- **Pregunta:** ¿qué diferencia temporal existe entre una reflexión aislada y una cola reverberante?
- **Mensaje:** la reflexión es una llegada física; eco/reverberación dependen de la organización temporal de varias llegadas.
- **Tipo:** señal temporal conceptual con ejes.
- **Variables/unidades:** tiempo relativo en ms o escala normalizada; amplitud/nivel relativo, según prototipo.
- **Escala/rango:** tres paneles con idéntico eje temporal; no usar un umbral universal de eco.
- **Modelo:** impulsos y envolvente sintéticos; parámetros documentados.
- **Anotaciones:** directa, llegada aislada, densidad creciente y cola; rótulo “conceptual, no medición”.
- **Tamaño final:** 7,0 × 4,1 in.
- **Script:** `units/unit_09/scripts/u09_plot_004_llegadas_reverberacion.py`.
- **Salidas:** SVG + PNG + `parameters.json`.
- **Validaciones:** mismos ejes, ninguna línea suavizada sin declarar, etiquetas fuera de las curvas, no fijar frontera perceptual universal.
- **Estado:** aprobado como señal conceptual sintética · generado y validado el 2026-08-12.

### U09-CH-005 — Longitud de onda frente a frecuencia

- **Slides:** U09-043; apoyo U09-044.
- **Pregunta:** ¿qué escalas espaciales corresponden a 125, 500 y 4000 Hz?
- **Mensaje:** para un mismo medio, `λ` disminuye al aumentar `f`.
- **Tipo:** curva hiperbólica.
- **Variables/unidades:** frecuencia en Hz; longitud de onda en m.
- **Escala/rango:** x logarítmica 63–8000 Hz; y logarítmica o lineal con criterio declarado; preferencia log–log si mejora la comparación de escalas.
- **Modelo:** `λ=c/f`, con `c=343 m·s⁻¹` y temperatura de referencia declarada.
- **Anotaciones:** 125 Hz ≈2,74 m; 500 Hz ≈0,686 m; 4000 Hz ≈0,0858 m; líneas a escalas geométricas solo si están rotuladas como ejemplos.
- **Tamaño final:** 7,2 × 4,2 in.
- **Script:** `units/unit_09/scripts/u09_plot_005_lambda_frecuencia.py`.
- **Salidas:** SVG + PNG + CSV.
- **Validaciones:** cálculo, redondeo, unidades, temperatura declarada, ninguna traducción de `λ` a atenuación de barrera.
- **Estado:** aprobado · generado y validado el 2026-08-12.

### U09-CH-006 — Decaimiento y lectura de `T_60`

- **Slides:** U09-049 y fallback estático U09-055.
- **Pregunta:** ¿cómo se identifica `T_60` en un decaimiento?
- **Mensaje:** el descriptor vincula una caída de nivel con un intervalo temporal bajo condiciones definidas.
- **Tipo:** curva de decaimiento sintética.
- **Variables/unidades:** tiempo en s; nivel relativo en dB.
- **Escala/rango:** x 0–1,2 s para el ejemplo; y 0 a −70 dB; eje no truncado respecto del intervalo mostrado.
- **Modelo:** decaimiento exponencial representado en dB; parámetro didáctico `T_60=0,60 s` o el que se sincronice con el ejemplo.
- **Anotaciones:** inicio, −60 dB, `T_60`; si se muestra extrapolación T20/T30, usar línea discontinua y rótulo explícito.
- **Tamaño final:** 7,0 × 4,0 in.
- **Script:** `units/unit_09/scripts/u09_plot_006_decaimiento_t60.py`.
- **Salidas:** SVG + PNG + parámetros; frames opcionales para U09-MEDIA-001.
- **Validaciones:** pendiente, intersección −60 dB, coherencia con audio procesado, ninguna curva presentada como medición real.
- **Estado:** aprobado como decaimiento sintético · generado y validado el 2026-08-12.

### U09-CH-007 — Fracción transmitida e índice de reducción

- **Slides:** U09-059.
- **Pregunta:** ¿cómo se transforma `τ_E` en `R`?
- **Mensaje:** cada década menos de transmisión aumenta 10 dB el índice ideal.
- **Tipo:** curva matemática con eje logarítmico.
- **Variables/unidades:** `τ_E` adimensional; `R` en dB.
- **Escala/rango:** x log 1 a 10⁻⁶; y lineal 0–60 dB.
- **Modelo:** `R=10 log10(1/τ_E)`.
- **Anotaciones:** 1 %, 0,1 % y 0,01 %; etiqueta “elemento ideal, no aislamiento in situ del conjunto”.
- **Tamaño final:** 7,0 × 4,1 in.
- **Script:** `units/unit_09/scripts/u09_plot_007_tau_R.py`.
- **Salidas:** SVG + PNG + CSV.
- **Validaciones:** dominio `0<τ_E≤1`, puntos 0,01→20 dB y 0,001→30 dB, eje decreciente o creciente claramente indicado.
- **Estado:** aprobado · generado y validado el 2026-08-12.

### U09-CH-008 — Regiones de una pared simple

- **Slides:** U09-065.
- **Pregunta:** ¿dónde describe la ley de masas y dónde aparecen otros mecanismos?
- **Mensaje:** la recta ideal es una región, no el desempeño completo de cualquier pared.
- **Tipo:** gráfico conceptual con regiones.
- **Variables/unidades:** frecuencia en Hz, escala log; `R` relativo en dB.
- **Escala/rango:** sin valores absolutos hasta validar convención; ejes rotulados “frecuencia” y “reducción relativa”.
- **Modelo:** reconstrucción didáctica de `ley-masas-pared-simple.tex`; regiones de rigidez, resonancia, masa y coincidencia.
- **Anotaciones:** región de masa destacada y pendiente aproximada; resto como límites cualitativos.
- **Tamaño final:** 7,0 × 4,2 in.
- **Script:** `units/unit_09/scripts/u09_plot_008_regiones_ley_masas.py`.
- **Salidas:** SVG + PNG + `parameters.json`.
- **Validaciones:** no asignar frecuencia crítica ni valor absoluto; pendiente coherente; regiones no confundidas con materiales específicos.
- **Estado:** no generado · condicionado a validación de convención y pendiente de aprobación.

### U09-CH-009 — Descriptor global frente a bandas

- **Slides:** U09-073.
- **Pregunta:** ¿por qué un valor global en dB(A) no reemplaza niveles por bandas para una prueba?
- **Mensaje:** el descriptor global y el espectro responden preguntas distintas.
- **Tipo:** comparación conceptual con ejes.
- **Variables/unidades:** panel A, un valor global ficticio sin criterio de aceptación; panel B, frecuencia central de banda y nivel relativo ficticio.
- **Escala/rango:** bandas de octava 125–8000 Hz; valores normalizados y rotulados “ejemplo sintético”.
- **Modelo/datos:** conjunto sintético diseñado para que dos espectros puedan compartir un global aproximado; no usar límites normativos.
- **Anotaciones:** “no informa vía/transductor/límite por banda” y “permite ver distribución frecuencial”.
- **Tamaño final:** 10,8 × 4,3 in.
- **Script:** `units/unit_09/scripts/u09_plot_009_global_vs_bandas.py`.
- **Salidas:** SVG + PNG + parámetros.
- **Validaciones:** no presentar igualdad metrológica exacta sin cálculo de ponderación; sin línea de aprobación; rótulo sintético visible.
- **Estado:** aprobado · panel global icónico sin cifra normativa; generado y validado el 2026-08-12.

### U09-CH-010 — Absorción atmosférica por frecuencia

- **Slides:** U09-088; nunca necesaria para la ruta central.
- **Pregunta:** ¿cómo depende el coeficiente de absorción de frecuencia y estado del aire?
- **Variables/unidades:** frecuencia en Hz; atenuación en dB por distancia; temperatura °C, humedad relativa % y presión kPa como parámetros.
- **Escala:** a definir según el rango legalmente reproducible de la fuente.
- **Datos/modelo:** método de ISO 9613-1:1993 o fuente académica primaria equivalente; la página oficial confirma dependencia con frecuencia, temperatura, humedad y presión, pero no entrega el contenido completo necesario para reproducir curvas.
- **Fuente de control:** <https://www.iso.org/standard/17426.html>.
- **Anotaciones:** condiciones completas por curva, máximo tres; advertencia contra coeficiente universal.
- **Script:** `units/unit_09/scripts/u09_plot_010_absorcion_atmosferica.py`.
- **Salidas previstas:** SVG + PNG + datos/fórmula documentados.
- **Validaciones:** versión y licencia de fuente, implementación comparada con casos publicados, unidades de distancia, condiciones y rango.
- **Estado:** **bloqueado por acceso a fuente primaria completa y permiso de uso**.

### U09-CH-011 — Niveles máximos admisibles para audiometría

- **Slides:** U09-092.
- **Pregunta:** ¿qué límite por banda corresponde a una prueba audiométrica definida?
- **Variables/unidades:** bandas de octava o tercio; nivel máximo y descriptor exactamente como lo defina la norma; vía, transductor y rango de prueba como facetas.
- **Escala:** categórica por bandas; no mezclar escenarios.
- **Datos:** norma elegida por la cátedra. Las páginas oficiales verificadas son ISO 8253-1:2010, ISO 8253-2:2009 y ASA/ANSI S3.1-1999 (R2023); los resúmenes no bastan para extraer la tabla.
- **Fuentes de control:** <https://www.iso.org/standard/43601.html>, <https://www.iso.org/standard/51997.html>, <https://webstore.ansi.org/standards/asa/asaansis31999r2023>.
- **Anotaciones:** norma, edición, adopción institucional, escenario, bandas, menor nivel de prueba y nota de aplicación.
- **Script:** `units/unit_09/scripts/u09_plot_011_limites_audiometria.py`.
- **Salidas previstas:** gráfico/tabla SVG y tabla nativa editable; CSV con procedencia celda por celda.
- **Validaciones:** doble verificación contra fuente completa; cero transcripción desde capturas o fuentes secundarias; revisión docente/normativa.
- **Estado:** **bloqueado por decisión institucional, acceso a fuente y escenario**.

## Orden de producción recomendado

1. U09-CH-001, 003, 005 y 007: relaciones exactas del capítulo.
2. U09-CH-004 y 006: señales sintéticas coordinadas con diagramas/media.
3. U09-CH-002, 008 y 009: ejemplos conceptuales que requieren revisión de interpretación.
4. U09-CH-010 y 011: solo después de cerrar fuentes y permisos.

## Registro de producción · 2026-08-12

| recursos | clasificación | resultado | archivos y validación |
|---|---|---|---|
| U09-CH-001–007 y U09-CH-009 | gráfico cuantitativo | 8 aprobados | script reproducible, `data.csv`, parámetros, SVG, PNG ≥2400 × 1350, preview 16:9, README, caption, texto alternativo, fuente y `validation.json` |
| U09-CH-008 | gráfico cuantitativo | no generado; condicionado | requiere cerrar la convención de ley de masas antes de dibujar regiones |
| U09-CH-010 | gráfico cuantitativo | bloqueado | requiere fuente primaria completa, permiso y caso de control |
| U09-CH-011 | gráfico cuantitativo | bloqueado | requiere norma completa, adopción institucional y escenario audiométrico |

La revisión estructural y visual terminó con cero problemas críticos y cero mayores. El historial de correcciones y los puntos de control se registran en `charts_review.md` y en `assets/generated/_review/`.

## Gate de aprobación

Ningún gráfico pasa a `approved` hasta ejecutarse, renderizarse dentro del layout real y superar: cero clipping/superposición; unidades y escala visibles; texto mínimo; datos/modelo trazables; coincidencia con puntos de control; caption y alt text; SVG/PNG/archivo de parámetros presentes.
