# Necesidades iniciales de gráficos — Unidad 6

Estos gráficos deben producirse con scripts reproducibles (preferentemente Python/NumPy/Matplotlib), exportarse en SVG cuando convenga la editabilidad y registrar supuestos, fuente de datos y versión. Los gráficos conceptuales deben declararse como tales: no se les asignarán valores anatómicos, fisiológicos ni clínicos inventados.

| chart_id | Slides | Clase | Variables / ejes | Mensaje pedagógico | Fuente y tratamiento de datos | Estado / cautela |
|---|---|---|---|---|---|---|
| U06-CH-001 | 064, 066, 067, 071 | Curvas de envolvente tonotópica | x: posición normalizada `s/L` (base→ápex); y: respuesta normalizada | Frecuencias altas y bajas maximizan en regiones distintas; hay ancho y solapamiento. | Reconstrucción conceptual de TEX fig. 6.6a / PDF 162; contrastar con `fettiplace2017` y `capraraPeng2022`. | Planificado. No rotular distancias ni frecuencias exactas como datos anatómicos. |
| U06-CH-002A | 068, 071 | Envolvente a nivel débil | x: `s/L`; y: respuesta normalizada | A nivel débil, el proceso activo produce mayor sensibilidad/selectividad. | Reconstrucción conceptual de TEX 6.7.3, fig. 6.6b / PDF 161–162. | Planificado; declarar normalización y condición cualitativa. |
| U06-CH-002B | 069, 071 | Comparación débil/intensa | x: `s/L`; y: respuesta normalizada o misma escala relativa | A igual frecuencia, mayor nivel aumenta respuesta y extensión; la relación es compresiva. | Misma familia que CH-002A; curvas generadas con parámetros didácticos, no ajuste de datos. | Planificado; mantener frecuencia constante y documentar parámetros. |
| U06-CH-003 | 070 | Curva entrada–respuesta | x: nivel de entrada relativo (dB); y: respuesta relativa (dB o normalizada) | El proceso activo coclear no es ganancia fija: la pendiente efectiva cambia con nivel. | Esquema conceptual basado en TEX 6.7.3 y referencias del capítulo. | Planificado; no presentar pendiente/ganancia numérica como medición humana universal. |
| U06-CH-004 | 095 | Código espacial de frecuencia | x: posición base→ápex; y: actividad relativa de población | La salida neural conserva una firma espacial derivada de la mecánica. | Derivado visualmente de CH-001 + TEX 6.9.1; población esquemática. | Planificado; no representar una neurona por frecuencia. |
| U06-CH-005 | 096 | Sincronización temporal conceptual | x: tiempo (ms o ciclos normalizados); y: estímulo + eventos | Los eventos pueden sincronizarse probabilísticamente con la fase, no uno por ciclo. | TEX 6.9.1; requiere fuente fisiológica adicional para límites/rangos. | Bloqueado para cifras. Puede diseñarse estructura sin rótulos numéricos. |
| U06-CH-006 | 098 | Nivel y patrón de salida | x: posición o población; y: respuesta relativa; dos niveles | Mayor nivel puede ampliar el patrón y modificar la descarga sin equivaler linealmente a sonoridad. | TEX 6.7.3/6.9.2; combinación conceptual de mecánica y salida. | Planificado; evitar tasas absolutas y saturación universal. |
| U06-CH-007 | 011–012 (opcional) | Presión en función de posición en CAE | x: posición axial (normalizada o cm si se define geometría); y: nivel/presión relativa | La posición de medida afecta la respuesta registrada en un conducto. | Solo producir con modelo documentado o fuente externa técnica; alternativa DG-007. | Opcional; no necesario para ruta central si falta fuente. |
| U06-CH-008 | 014–017, 109 (opcional) | Respuesta ideal de cuarto de onda | x: frecuencia (Hz); y: respuesta relativa | El modelo posee una frecuencia fundamental y resonancias; la anatomía real modifica la curva. | Modelo analítico ideal con `L` y `c` declarados; no usar como respuesta real de oído. | Opcional/complementario; separar claramente idealización y medición. |
| U06-CH-009 | 115 | Reflejo acústico | Según fuente: tiempo (ms) o nivel (dB SPL) frente a respuesta | Mostrar dependencia de condición, no una latencia/umbral único. | Fuente externa por seleccionar y validar; el capítulo no aporta cifras. | Bloqueado por fuente. |

## Requisitos de QA

- Ejes y unidades legibles; si el eje es normalizado, declararlo en la propia figura.
- Una leyenda solo cuando haya más de una curva y el color no sea la única codificación.
- Mantener la misma orientación base→ápex en toda la unidad.
- Incluir caption “esquema conceptual” cuando no haya datos empíricos.
- Guardar script, parámetros y fuente en `units/unit_06/scripts/` cuando comience producción.
- Probar el gráfico dentro del layout real, no solo como archivo aislado.
