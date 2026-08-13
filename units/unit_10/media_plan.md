# Unidad 10 — Plan de audio y multimedia

Versión de planificación · 2026-08-12

## Criterio general

Los recursos temporales se clasifican como `video_or_gif`, aunque su contenido sea audio. Serán opcionales, locales, reproducidos manualmente una sola vez y siempre posteriores a una predicción del grupo. La información esencial estará en un gráfico o diagrama estático.

Formato maestro: WAV PCM 48 kHz/24 bit, mono, duración breve, pico ≤−6 dBFS, fades de 50–100 ms y metadatos de generación. La comparación se realizará con un criterio de nivelado documentado —por ejemplo, mismo RMS digital dentro de una banda finita— sin llamarlo igualdad de sonoridad ni nivel SPL calibrado.

No se usarán auriculares compartidos ni autoplay. El volumen del sistema se ajustará antes de clase con una señal segura; cada slide advertirá “demostración no calibrada”.

## U10-MD-001 — Blanco y rosa

- **Slides:** U10-035; apoyo a U10-034.
- **Assets:** U10-AS-001 y U10-AS-002.
- **Clasificación:** `video_or_gif` con fallback `chart` U10-CH-010.
- **Propósito:** relacionar la experiencia auditiva con PSD y contenido por octava sin reducir la definición al sonido percibido.
- **Fragmento recomendado:** blanco 6 s → pausa 1 s → rosa 6 s → pausa 1 s → comparación opcional de 2 s; total 14–16 s.
- **Momento:** después de que el grupo prediga cuál tendrá mayor contenido en octavas altas y después de leer CH-010.
- **Audio:** sí; mono; misma banda 125–8000 Hz, misma duración y mismo RMS digital. Semillas fijas distintas o filtrado de una misma realización, decisión documentada.
- **Alternativa sin conexión:** U10-CH-010 completo y descripción verbal; la slide sigue siendo autosuficiente.
- **Captura estática:** dos PSD y barras por octava coordinadas, con rótulos blanco/rosa.
- **Script:** `u10_audio_001_blanco_rosa.py`; guardar WAV, `parameters.json`, espectros de verificación y README.
- **Validaciones:** cero clipping; RMS coincidente ±0,05 dB; banda y filtro verificados; ausencia de DC; no convertir dBFS a dB SPL; escucha técnica a nivel moderado.
- **Estado:** listo para producir con material propio.

## U10-MD-002 — Ruido de banda estrecha

- **Slides:** complemento U10-040 y U10-043; no reproducir durante U10-060 para evitar apariencia de estímulo clínico.
- **Asset:** U10-AS-003.
- **Clasificación:** `video_or_gif` derivado de `diagram` U10-DG-024/025.
- **Propósito:** hacer audible que el contenido se concentra en una región declarada, no enseñar un sonido “típico” universal de NBN.
- **Fragmento recomendado:** banda ancha 3 s → pausa 0,5 s → NBN 1 kHz, 900–1100 Hz, 5 s; total 8,5–9 s.
- **Momento:** después de definir `f_L`, `f_c`, `f_H` y antes de la actividad de elección de señal.
- **Audio:** sí; mono; nivelado por RMS digital; pendientes y método de filtrado documentados; no rotular como estímulo audiométrico calibrado.
- **Alternativa sin conexión:** respuesta pasabanda U10-DG-024 y fórmula U10-DG-025.
- **Captura estática:** PSD de entrada y salida con límites 900/1100 Hz y centro declarado.
- **Script:** `u10_audio_002_nbn.py`.
- **Validaciones:** frecuencia de muestreo y filtros sin aliasing; atenuación fuera de banda medida; centro/ancho coherentes; cero clipping; texto de cautela visible.
- **Estado:** listo para producir si la cátedra conserva el audio opcional.

## U10-MD-003 — Ruido conformado al habla

- **Slides:** complemento de U10-038/043.
- **Asset:** U10-AS-004.
- **Clasificación:** `video_or_gif` con fallback `diagram` U10-DG-022.
- **Propósito:** distinguir “envolvente espectral semejante al habla” de una grabación de habla y mostrar que el nombre no define una curva universal.
- **Fragmento recomendado:** ruido base 4 s → pausa 0,5 s → ruido conformado 6 s; total 10–11 s.
- **Momento:** después de identificar la fuente exacta de la envolvente objetivo y antes de compararlo con NBN.
- **Audio:** sí, pero solo si se selecciona una especificación concreta de equipo, norma o corpus; no usar voz humana ni corpus sin licencia.
- **Alternativa sin conexión:** flujo filtro–envolvente–salida U10-DG-022 con espectro cualitativo claramente rotulado.
- **Captura estática:** espectro objetivo y respuesta del filtro; título con la especificación utilizada.
- **Script:** `u10_audio_003_speech_shaped.py`, bloqueado hasta recibir `target_spectrum.csv` con fuente.
- **Validaciones:** desviación frente a curva objetivo dentro de tolerancia definida; banda, nivelado y fuente registrados; no afirmar validez clínica general.
- **Estado:** `blocked-source`.

## U10-MD-004 — Revelado del caso integrador

- **Slides:** U10-077–080.
- **Clasificación:** estados editables de `diagram`; no se exportará video/GIF por defecto.
- **Propósito:** reducir carga mostrando escena base, capa temporal, capa espectral y capa de decisión sin mover los elementos.
- **Fragmento recomendado si se exportara:** 12–16 s, cuatro estados de 3–4 s; avance manual preferido.
- **Momento:** al inicio de cada una de las cuatro slides del caso.
- **Audio:** no; narración docente en vivo.
- **Alternativa sin conexión:** las cuatro slides estáticas DG-050–053.
- **Captura estática:** DG-053 con leyenda completa.
- **Producción:** duplicación de objetos PowerPoint con revelado progresivo; MP4 solo si una versión autónoma se necesita fuera del aula.
- **Validaciones:** geometría e IDs idénticos; cero saltos; cada capa puede interpretarse sola; sin valores simulados presentados como medición.
- **Estado:** planificado como animación nativa, no como asset temporal.

## Recursos temporales descartados

- Videos externos de ruido ocupacional o audiometría: mezclan contexto, normativa y procedimiento y son difíciles de fragmentar/licenciar.
- GIFs de ondas o partículas: añaden movimiento sin una variable mensurable.
- Grabaciones reales de tránsito/consultorio: no permiten controlar banda, nivel, consentimiento ni reproducibilidad; CH-014 y DG-050 son suficientes.
- Simuladores de tinnitus o pérdida auditiva: pueden inducir interpretaciones clínicas incorrectas y no son necesarios para los objetivos.

## Gate de aceptación

1. Archivo local reproducible y checksum registrado.
2. Script, parámetros, semilla, banda y criterio de nivelado archivados.
3. Revisión espectral y temporal automatizada.
4. Escucha técnica a volumen moderado, sin clicks, DC ni clipping.
5. Fallback estático, caption y texto alternativo completos.
6. Ensayo sin conexión y control manual en PowerPoint.

No se generó ni descargó multimedia en esta fase.
