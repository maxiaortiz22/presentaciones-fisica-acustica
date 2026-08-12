# Unidad 7 — Plan de audio, animaciones y multimedia

Versión de planificación · 2026-08-11

## Criterio general

Los recursos temporales se clasifican como `video_or_gif`, aunque el soporte principal sea audio. Son opcionales, supraliminales y no constituyen pruebas auditivas. Cada recurso tendrá archivo local, control manual, respaldo estático y una alternativa que permita alcanzar el objetivo sin oír ni conectarse a internet.

Formatos preferidos:

- audio: WAV PCM 48 kHz/24 bit como maestro y M4A/AAC solo para distribución si fuera necesario;
- animación: MP4 H.264 1920×1080, 25/30 fps; GIF solo como respaldo silencioso breve;
- nivel digital: picos ≤−3 dBFS y RMS documentado; no traducir dBFS a dB SPL sin calibración;
- reproducción: una vez, después de una predicción; nunca loop continuo ni autoplay.

## Recursos propuestos

### U07-MEDIA-001 — Dos tonos con igual RMS digital

- **Slides:** U07-002.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio sintético propio + barras/ondas estáticas.
- **Propósito:** activar la pregunta “mismo nivel físico, ¿misma sonoridad?” sin convertir la clase en medición.
- **Fragmento recomendado:** dos tonos de 1,0 s separados por 0,5 s; repetir la pareja una vez. Duración total 5–6 s.
- **Momento:** después de la predicción y antes de revelar la diferencia magnitud–percepto.
- **Audio:** sí; tonos a 250 Hz y 1 kHz, con igual RMS digital y fades de 30 ms.
- **Advertencia:** el sistema no garantiza igual `L_p` en el oído; el visual dice “igual RMS digital nominal”. No ajustar a umbral ni pedir cuál “se oye”.
- **Alternativa sin conexión:** WAV local; la presentación funciona también sin reproducirlo.
- **Captura estática:** dos ondas normalizadas + barras RMS iguales + pregunta.
- **Script:** `u07_media_001_tonos_rms.py`.
- **Validaciones:** sin clipping/DC; RMS ±0,01 dB; fades; duración/frecuencia verificadas; nivel de reproducción confortable; texto alternativo.
- **Estado:** listo para producción propia.

### U07-MEDIA-002 — Fundamental ausente

- **Slides:** U07-036.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio sintético propio sincronizado con U07-CH-005.
- **Propósito:** mostrar que quitar la componente `f_0` no obliga a perder el pitch asociado a la periodicidad.
- **Fragmento recomendado:** complejo completo 1,5 s → pausa 0,5 s → complejo sin fundamental 1,5 s; repetir. Total 8–9 s.
- **Momento:** tras leer ambos espectros y antes de discutir la interpretación.
- **Audio:** sí; `f_0=200 Hz`, armónicos 1–8; segundo estímulo conserva 2–8; nivel global equiparado con criterio documentado.
- **Alternativa sin conexión:** WAV local y ejercicio visual con espaciamiento armónico.
- **Captura estática:** dos espectros y una llave que señala `Δf=f_0`.
- **Script:** compartido con `u07_plot_005_fundamental_ausente.py`.
- **Validaciones:** FFT confirma componentes; no aparece energía intencional en 200 Hz en la segunda señal más allá de fuga; ventana/fades; sin afirmar respuesta universal.
- **Estado:** listo para producción propia.

### U07-MEDIA-003 — Igual magnitud espectral, distinta estructura temporal

- **Slides:** U07-040.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio sintético + animación de forma de onda/espectro.
- **Propósito:** mostrar que una magnitud espectral no agota el timbre ni la organización temporal.
- **Fragmento recomendado:** señal A 1,5 s → pausa → señal B 1,5 s; una repetición. Total 8–10 s.
- **Momento:** después de identificar qué partes del timbre son espectrales y temporales.
- **Audio:** sí; mismas magnitudes de componentes y dos configuraciones de fase/estructura temporal, con RMS común.
- **Alternativa sin conexión:** MP4/WAV locales; si no se reproduce, dos formas de onda y espectros idénticos dentro de tolerancia.
- **Captura estática:** panel A/B con magnitud espectral y envolvente/forma temporal.
- **Script:** `u07_media_003_fase_tiempo.py`.
- **Validaciones:** espectros de magnitud coinciden dentro de tolerancia; las formas temporales difieren; sin lenguaje de instrumento real; subtítulos/descripcion.
- **Estado:** listo como estímulo sintético; prueba perceptual previa recomendada.

### U07-MEDIA-004 — Voz objetivo y voz competidora

- **Slides:** U07-074.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio de producción propia; complemento de U07-DG-023.
- **Propósito:** distinguir solapamiento energético de incertidumbre/selección entre fuentes.
- **Fragmento recomendado:** objetivo solo 3 s → competidora sola 3 s → mezcla 5 s. Total 12–14 s.
- **Momento:** después de definir ambos mecanismos; no como diagnóstico inicial.
- **Audio:** sí; dos voces adultas con frases neutras diferentes, nivel RMS y posiciones virtuales documentados.
- **Alternativa sin conexión:** WAV local; espectrogramas y diagrama de fuentes.
- **Captura estática:** dos espectrogramas + mezcla + etiquetas “objetivo/competidora”.
- **Fuente:** grabación UCASAL con consentimiento escrito o narración docente autorizada; no usar corpus sin licencia.
- **Validaciones:** consentimiento; sin datos personales; guion lingüísticamente neutro; SNR documentada; sin clipping; alternativa no auditiva.
- **Estado:** condicionado a grabación propia.

### U07-MEDIA-005 — Misma SNR, distinta estructura y reverberación

- **Slides:** U07-082–085.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio propio + visual sincronizado U07-CH-010.
- **Propósito:** demostrar que una SNR global no determina una inteligibilidad única.
- **Fragmento recomendado:** condición A 4 s → pausa/rotulado → condición B 4 s; repetir solo si se solicita. Total 11–13 s.
- **Momento:** después del cálculo de SNR U07-081 y antes de introducir `T_60`.
- **Audio:** sí; misma frase autorizada, igual SNR RMS objetivo (+8 dB como ejemplo), distinta modulación de ruido y/o respuesta impulsiva sintética.
- **Alternativa sin conexión:** WAV local y dos espectrogramas/envolventes con la misma métrica.
- **Captura estática:** U07-CH-010 con SNR verificada y colas señaladas.
- **Script:** pipeline `u07_media_005_igual_snr.py` + `u07_plot_010_igual_snr.py`.
- **Validaciones:** SNR ±0,1 dB con misma ventana/banda; no etiquetar porcentaje de inteligibilidad; respuesta impulsiva declarada sintética; nivel confortable.
- **Estado:** condicionado a voz autorizada.

### U07-MEDIA-006 — Directo más copia retardada

- **Slides:** U07-092.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio sintético y animación de líneas temporales.
- **Propósito:** hacer observable que retardo y nivel relativo cambian fusión, coloración o separación, sin fijar una frontera universal.
- **Fragmento recomendado:** cuatro condiciones de 1,2 s con retardos 2, 10, 20 y 50 ms, separadas por 0,6 s; total 8–10 s.
- **Momento:** después del cálculo de U07-091; pedir predicción antes de reproducir.
- **Audio:** sí; ráfaga o sílaba propia con copia a −6 dB; parámetros visibles.
- **Alternativa sin conexión:** WAV/MP4 locales; cuatro líneas temporales estáticas.
- **Captura estática:** directo y copia con `Δt`/nivel relativo para cada condición.
- **Script:** `u07_media_006_directo_reflexion.py`.
- **Validaciones:** retardos por conteo de muestras; nivel relativo ±0,1 dB; sin clipping; no llamar “eco” automáticamente a 20 ms; control de volumen.
- **Estado:** listo para producción propia.

### U07-MEDIA-007 — Giro de cabeza y pistas dinámicas

- **Slides:** U07-108.
- **Clasificación:** `video_or_gif`.
- **Tipo:** animación técnica propia sin audio.
- **Propósito:** mostrar cómo un giro pequeño cambia conjuntamente ITD, ILD y filtrado espectral y ayuda a desambiguar posiciones.
- **Fragmento recomendado:** 8–12 s; posición inicial → giro 20° esquemático → actualización de indicadores → retorno; una sola reproducción.
- **Momento:** después del cono de confusión U07-107.
- **Audio:** no; la sonificación binaural añadiría dependencia de auriculares/HRTF individual.
- **Alternativa sin conexión:** MP4 y GIF locales.
- **Captura estática:** dos estados de U07-DG-038, antes/después, con flechas de cambio.
- **Script:** animación derivada del mismo JSON geométrico del diagrama.
- **Validaciones:** no presentar magnitudes numéricas universales; L/R y dirección correctos; sin mareo/destellos; etiquetas ≥22 pt; dos cuadros autosuficientes.
- **Estado:** listo para animación propia.

### U07-MEDIA-008 — Escena cocktail party

- **Slides:** U07-112.
- **Clasificación:** `video_or_gif`.
- **Tipo:** audio multifuente propio; opcional.
- **Propósito:** experimentar la tarea de seguir una voz entre fuentes concurrentes y anticipar las pistas de segregación.
- **Fragmento recomendado:** mezcla de 8–10 s; luego 3 s con objetivo resaltado visualmente, sin cambiar el audio. Total 12–15 s.
- **Momento:** tras ver la mezcla física U07-111 y antes de enumerar pistas U07-114.
- **Audio:** sí; 3 voces autorizadas o una voz transformada de manera declarada, distribuidas espacialmente de forma moderada.
- **Alternativa sin conexión:** WAV local; U07-DG-039 con formas de onda/espectrogramas.
- **Captura estática:** escena de tres fuentes → señales L/R → objeto atendido.
- **Fuente:** producción UCASAL con consentimientos; si no se consigue, no sustituir por material de streaming.
- **Validaciones:** guion neutro; ausencia de datos personales; normalización y SNR registradas; no calificar desempeño del grupo; alternativa visual completa.
- **Estado:** opcional y condicionado a producción propia.

## Decisiones sobre video externo y GIF

No se preseleccionó ningún video externo: las ocho necesidades pueden resolverse con producción propia reproducible y respaldo estático. Esto evita dependencia de streaming, problemas de fragmento/licencia y modelos visuales que no coincidan con el capítulo. Los GIF se usarán solo como copia silenciosa de MEDIA-007 o como fallback; para audio y sincronización se prefiere MP4/WAV.

## Gate de seguridad y accesibilidad

1. Iniciar el sistema de reproducción con volumen bajo y ajustar con material no experimental.
2. No pedir umbrales, equiparaciones individuales ni respuestas diagnósticas.
3. Ofrecer participación sin auriculares y sin obligación de escuchar.
4. Mantener picos digitales ≤−3 dBFS; registrar normalización y fades.
5. Toda consigna debe poder resolverse con la captura estática.
6. Archivos locales probados en el equipo de aula; una falla de reproducción no interrumpe la secuencia.

En esta fase no se generó, descargó ni insertó multimedia.
