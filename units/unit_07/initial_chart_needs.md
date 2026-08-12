# Necesidades iniciales de gráficos — Unidad 7

## Criterio

Los gráficos deberán generarse de forma reproducible, idealmente en SVG editable y PNG de revisión. “Cuantitativo” significa que los ejes y valores provienen de una ecuación, datos o norma citada; “conceptual” debe rotularse como esquema y no aparentar precisión empírica.

| chart_id | Slides | Título de trabajo | Clase | Datos/modelo | Ejes y unidades | Mensaje | Fuente | Prioridad | Estado |
|---|---|---|---|---|---|---|---|---|---|
| U07-CH-001 | U07-014 | Curva psicométrica de detección | cuantitativo sintético | Función logística parametrizada, sin afirmar datos poblacionales | nivel del estímulo (dB SPL o relativo) vs proporción de respuestas (0–1 o %) | El umbral depende de un criterio sobre una transición gradual | TEX 7.3–7.4; modelo didáctico declarado | alta | por generar |
| U07-CH-002A | U07-015 | Umbral auditivo según frecuencia | cuantitativo condicionado | Datos del libro o fuente académica explícita | frecuencia (Hz, log) vs nivel umbral (dB SPL) | La sensibilidad cambia con frecuencia | TEX 7.4; PDF fig. correspondiente | media | verificar datos |
| U07-CH-002B | U07-016 | Umbral y molestia como límites condicionados | conceptual | Bandas esquemáticas, sin fronteras universales | frecuencia (Hz) vs nivel (dB SPL), rotulado “esquema” | El área utilizable depende de tarea y población | TEX 7.4; SA | baja | propuesto |
| U07-CH-003 | U07-026 | Transferencia campo–tímpano | conceptual | Curva cualitativa de ganancia dependiente de frecuencia | frecuencia (Hz) vs diferencia de nivel (dB) | No existe una ganancia única para todas las frecuencias | TEX 7.4.2; REF `carlini2024` | media | fuente/datos por definir |
| U07-CH-004 | U07-029–030, U07-123 | Familia de curvas isofónicas | cuantitativo normativo o conceptual | ISO 226:2023 si se autoriza; en caso contrario, esquema reconstruido y marcado | frecuencia (Hz, log) vs nivel de presión sonora (dB SPL); curva en fon | Igual sonoridad exige niveles diferentes según frecuencia y nivel | ISO 226:2023; TEX 7.5 | crítica | decisión abierta OD-U07-02/03 |
| U07-CH-005 | U07-036 | Espectros con y sin fundamental | cuantitativo sintético | Suma de armónicos reproducible | frecuencia (Hz) vs amplitud relativa (dB o lineal) | Puede mantenerse periodicidad/pitch aunque falte la línea fundamental | TEX 7.6.1; REF `oxenham2018` | media | por generar |
| U07-CH-006 | U07-050 | Relación fones–sones | cuantitativo por ecuación | `N_son = 2^((L_N-40)/10)` en rango pedagógico declarado | nivel de sonoridad (fon) vs sonoridad (son) | +10 fon duplica aproximadamente los sones | TEX 7.8; ec. 7.2 | alta | por generar |
| U07-CH-007 | U07-060–061 | Patrón de enmascaramiento | cuantitativo o conceptual condicionado | Datos del libro si son legibles/trazables; si no, función sintética declarada | frecuencia objetivo (Hz, log) vs umbral enmascarado (dB SPL o elevación dB) | El efecto depende de separación frecuencial y puede ser asimétrico | TEX 7.9.1; PDF fig. 7.5 | alta | verificar datos |
| U07-CH-008 | U07-064, U07-125–127 | Filtro auditivo y rectángulo equivalente | cuantitativo conceptual | Respuesta de filtro normalizada y rectángulo de igual área | frecuencia relativa/Hz vs respuesta normalizada | ERB resume el ancho efectivo por equivalencia de área | TEX 7.9.1; REF `oxenham2018` | media | por generar tras OD-U07-04 |
| U07-CH-009 | U07-083–084, U07-129 | Decaimiento reverberante y `T_60` | cuantitativo sintético | Decaimiento exponencial/log-lineal con tramo de ajuste declarado | tiempo (s) vs nivel relativo (dB) | `T_60` describe un decaimiento de 60 dB, no “tiempo hasta silencio” | TEX 7.10.2; puente U9 | alta | por generar |
| U07-CH-010 | U07-082 | Igual SNR, distintas condiciones | conceptual comparativo | Dos espectros/envolventes sintéticos con SNR nominal común | frecuencia/tiempo vs nivel relativo | Igual SNR no fija inteligibilidad | TEX 7.10; SA | media | opcional; puede resolverse como mixed |

## Controles técnicos

- Definir ejes, unidades, escala y fuente dentro de la figura o caption futuro.
- Usar leyenda solo cuando haya más de una serie no identificable directamente.
- Declarar “datos normativos”, “datos del libro”, “modelo sintético” o “esquema conceptual”.
- No digitalizar curvas del PDF si la licencia, resolución o trazabilidad son insuficientes.
- Validar consistencia dimensional y puntos de ejemplo mediante pruebas del script.
- Renderizar cada gráfico en el tamaño real del layout antes de aprobar tipografía y etiquetas.
