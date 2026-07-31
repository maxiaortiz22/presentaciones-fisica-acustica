# Unidad 3 — Necesidades iniciales de assets y multimedia

## Criterio

La unidad puede resolverse principalmente con diagramas y gráficos propios. Los assets externos solo se justifican cuando muestran un dispositivo, una demostración o un movimiento difícil de reconstruir con formas editables. Toda pieza externa deberá incorporarse luego a `asset_manifest.csv` con autor, URL, licencia, fecha de acceso, propósito y estado.

No se inició todavía búsqueda ni descarga. Los campos “fuente candidata” son criterios de curación, no atribuciones.

## Inventario inicial

| asset_id | slides | tipo | necesidad pedagógica | especificación inicial | fuente candidata | alternativa propia o estática | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U03-AS01 | U03-013–014 | video o GIF de demostración | Seguir una espira marcada mientras un pulso avanza. | Resorte largo, fondo neutro, cámara fija, marca de color, 6–10 s, reproducción lenta. | Producción docente propia o recurso universitario con licencia abierta. | Secuencia propia de cuatro a seis fotogramas vectoriales. | alta | pendiente de producir o curar |
| U03-AS02 | U03-061–062 | animación | Comparar trayectoria local de una partícula y avance de una cresta o frente. | Dos marcadores cromáticos, controles de pausa, escala cualitativa declarada. | Preferir animación propia reproducible; recurso externo solo con licencia clara. | Seis snapshots generados desde el mismo modelo del gráfico espacio–tiempo. | alta | pendiente de producir |
| U03-AS03 | U03-043–044 | ilustración técnica opcional | Dar contexto físico al cono y al aire vecino. | Corte lateral simple de parlante, sin etiquetas comerciales ni detalle irrelevante. | Fabricante técnico, universidad o Wikimedia Commons con licencia compatible. | Diagrama propio editable; opción preferida si la imagen no mejora la explicación. | media | curación opcional |
| U03-AS04 | U03-046 | fotografía técnica opcional | Mostrar una cadena real de calibración audiométrica. | Audiómetro o generador, transductor y acoplador; encuadre que permita señalar funciones. | Fabricante con permiso, organismo técnico o fotografía propia del laboratorio. | Diagrama funcional propio de cuatro nodos. | media | pendiente de disponibilidad |
| U03-AS05 | U03-040–041 | audio generado | Contrastar tono sostenido idealizado con señal de entrada y salida suaves. | Dos archivos breves a nivel seguro y normalizado; 500 Hz; fade in/out declarado. | Producción propia mediante script reproducible. | Gráfico temporal de la señal y descripción verbal. | media | pendiente de generar |
| U03-AS06 | U03-064–068 | audio generado | Escuchar dos tonos de igual frecuencia con diferente fase solo como demostración física controlada. | Señales mono y suma reproducible; advertir que fase absoluta aislada no es atributo perceptual simple. | Producción propia mediante script reproducible. | Gráficos sincronizados; demostración omitible si el sistema de reproducción no conserva condiciones. | baja | pendiente de decisión docente |
| U03-AS07 | U03-072–076 | simulación o audio | Mostrar suma, refuerzo y cancelación ideal en una región. | Control de `A₁`, `A₂` y `Δφ`; salida gráfica obligatoria y audio opcional. | Simulación propia o recurso universitario abierto. | Gráficos estáticos generados para `0`, `π/2` y `π`. | media | pendiente de producir |
| U03-AS08 | U03-079 | imagen técnica opcional | Contextualizar producción y recepción sin convertir la slide en anatomía. | Una imagen de pliegues vocales o cadena auditiva solo si permite señalar fuente, medio y receptor. | Atlas universitario, organismo de salud o publicación abierta. | Dos mini diagramas funcionales propios; opción preferida para mantener el alcance. | baja | curación opcional |

## Decisiones de uso

- Los audios deben tener nivel de reproducción seguro, duración breve y alternativa visual.
- Las animaciones deben permitir pausa y observación cuadro a cuadro.
- No se necesita una fotografía decorativa de “ondas de sonido”.
- Una captura de osciloscopio o software no reemplaza ejes, unidades ni calibración.
- Si U03-AS03, U03-AS04 o U03-AS08 no tienen licencia clara, se reemplazan por diagramas propios.
- U03-AS06 solo se conserva si el docente desea discutir los límites perceptuales de la fase; no es necesaria para la ruta central.

