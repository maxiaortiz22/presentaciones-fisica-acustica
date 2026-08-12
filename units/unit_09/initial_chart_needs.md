# Unidad 9 — Necesidades iniciales de gráficos cuantitativos

## Criterio

Los gráficos de este inventario deberán producirse en una fase posterior mediante `chart-generation`, preferentemente con Python, NumPy y Matplotlib, con fuente o modelo explícito, ejes, unidades, caption, alt text y archivos reproducibles. En este storyboard un `chart` puede ser:

- **cuantitativo por ecuación:** valores calculados desde una relación del capítulo;
- **cuantitativo por datos externos:** requiere fuente primaria completa;
- **conceptual con ejes:** explica estructura o lectura, pero no representa mediciones reales.

No se usarán curvas sin rango, condiciones o procedencia. Los gráficos U09-CH-010 y U09-CH-011 permanecen bloqueados hasta resolver sus fuentes.

## Inventario

| chart_id | slides | clase | pregunta que responde | ejes/variables | datos o modelo | fuente | decisiones de diseño | estado |
|---|---|---|---|---|---|---|---|---|
| U09-CH-001 | U09-014 | cuantitativo por ecuación | ¿Cómo cambia `L_p` al variar la razón `r₂/r₁`? | x: `r₂/r₁` adimensional; y: `ΔL_p` en dB | `ΔL_p = −20 log10(r₂/r₁)`; marcar 0,5, 1, 2, 4 | LaTeX ec. 9.1; PDF p. 237 | Mostrar zona de validez como banda de condiciones, no como rango numérico; eje x logarítmico si mejora la simetría. | listo para especificar |
| U09-CH-002 | U09-018 | cuantitativo sintético | ¿Cómo puede cambiar el patrón polar con la frecuencia? | ángulo 0–360°; radio en dB relativos | Tres funciones sintéticas documentadas, misma potencia relativa y escala | U4 directividad; LaTeX 9.2; parámetros propios, no datos de producto | Rotular “ejemplo sintético”; misma orientación y escala; comprobar lectura del cero radial. | complementario; listo para prototipo |
| U09-CH-003 | U09-023 | cuantitativo por ecuación | ¿Cuánto cambia `c` en el intervalo térmico didáctico? | x: temperatura `θ` en °C; y: `c` en m·s⁻¹ | `c ≈ 331 + 0,6 θ`; intervalo que se defina en la slide | LaTeX ec. 9.3; PDF pp. 238–239 | Marcar 5 °C, 20 °C y 25 °C; no extrapolar fuera del intervalo declarado. | listo para especificar |
| U09-CH-004 | U09-039 | conceptual con ejes | ¿Cómo se distinguen llegada directa, reflexión aislada y cola reverberante? | x: tiempo; y: amplitud o nivel relativo | Señales sintéticas normalizadas; sin umbral perceptual universal | LaTeX 9.7.1/9.7.3; U7; parámetros propios | Tres paneles o capas; rotular mecanismo físico y organización temporal; evitar sugerir un corte universal eco/reverberación. | listo para prototipo |
| U09-CH-005 | U09-043 | cuantitativo por ecuación | ¿Qué longitud de onda corresponde a cada frecuencia? | x: frecuencia en Hz, preferentemente log; y: `λ` en m | `λ=c/f`, con `c` declarada; marcadores 125, 500 y 4000 Hz | LaTeX 9.7.5 y ejercicios; PDF pp. 244, 252, 256 | Añadir bandas de escala de obstáculos solo si se definen sin convertirlas en atenuación. | listo para especificar |
| U09-CH-006 | U09-049, U09-055 | conceptual cuantificado | ¿Cómo se lee `T_60` en un decaimiento? | x: tiempo en s; y: nivel relativo en dB | Curva sintética exponencial/logarítmica con caída visible; parámetros didácticos | LaTeX 9.7.3; PDF pp. 242–243 | Mostrar −60 dB y, si se usa extrapolación, señalarla como tal; no simular ruido de medición salvo propósito explícito. | listo para prototipo |
| U09-CH-007 | U09-059 | cuantitativo por ecuación | ¿Cómo se relacionan `τ_E` y `R`? | x: `τ_E` adimensional en escala log; y: `R` en dB | `R = 10 log10(1/τ_E)` | LaTeX ec. 9.9; PDF pp. 244–245 | Destacar 1 %, 0,1 % y 0,01 %; no rotular como desempeño de una pared real. | listo para especificar |
| U09-CH-008 | U09-065 | conceptual con regiones | ¿Dónde es válida la tendencia de ley de masas y dónde aparecen límites? | x: frecuencia en Hz log; y: `R` relativo en dB | Curva didáctica inspirada en figura del capítulo; regiones cualitativas, sin valores absolutos | LaTeX 9.8; PDF pp. 245–246; `ley-masas-pared-simple.tex` | Resaltar pendiente de masa; rigidez, resonancia y coincidencia sin frecuencia crítica numérica. | complementario; validar convención |
| U09-CH-009 | U09-073 | conceptual con ejes | ¿Por qué un valor global en dB(A) no sustituye niveles por bandas? | Panel A: único descriptor; panel B: bandas de frecuencia y nivel relativo | Espectro sintético sin límites normativos | LaTeX 9.8.1; PDF pp. 247–249; U5 | Evitar una falsa equivalencia matemática entre paneles; declarar que faltan criterio, vía y transductor. | listo para prototipo |
| U09-CH-010 | U09-088 | cuantitativo por datos externos | ¿Cómo varía la absorción atmosférica con frecuencia y estado del aire? | x: frecuencia; y: atenuación por distancia; curvas por condiciones | Datos tabulados o ecuación normativa/académica con temperatura, humedad y presión explícitas | Fuente primaria completa por seleccionar | No generar hasta conocer rango, unidades, condiciones y permiso de reproducción; incluir incertidumbre o alcance. | bloqueado por fuente |
| U09-CH-011 | U09-092 | cuantitativo normativo | ¿Qué niveles máximos son aplicables a una prueba audiométrica definida? | x: bandas; y: nivel máximo y descriptor normativo | Tabla normativa seleccionada por vía, transductor y menor nivel de prueba | Norma, edición y adopción pendientes: ISO 8253-1/2 o ANSI/ASA S3.1 según decisión docente | No combinar escenarios; conservar identificación completa y notas de aplicación; no usar cifras secundarias. | bloqueado por fuente y decisión institucional |

## Controles comunes de aceptación

1. Ejes, unidades, escala y condiciones visibles.
2. Fuente de datos o ecuación registrada en script y caption.
3. Diferenciación visual entre medición, cálculo por modelo y ejemplo sintético.
4. Tamaño de texto de aula y contraste coherentes con `presentation_style_guide.md`.
5. Ningún eje truncado o suavizado sin declaración.
6. Exportación SVG cuando la editabilidad importe y PNG de alta resolución como fallback.
7. Verificación dimensional de U09-CH-001, 003, 005 y 007.
8. U09-CH-010 y U09-CH-011 no pueden pasar a producción mientras conserven estado bloqueado.

## Priorización de producción posterior

- **Primera tanda central:** U09-CH-001, 003, 004, 005, 006 y 007.
- **Segunda tanda central/conceptual:** U09-CH-009.
- **Complementarios:** U09-CH-002 y 008.
- **Bloqueados:** U09-CH-010 y 011.
