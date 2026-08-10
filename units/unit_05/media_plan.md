# Unidad 5 — Plan de multimedia, audio y animaciones

## Criterio

La multimedia se reserva para cambios temporales que una figura fija no muestra con la misma claridad. Todos los recursos serán de producción propia, se reproducirán manualmente y funcionarán sin conexión. No se usarán videos de terceros ni autoplay continuo.

| media_id | slides | clase | recurso | fragmento recomendado y duración | momento de reproducción | audio | alternativa sin conexión | captura estática de respaldo | fuente/licencia | estado |
|---|---|---|---|---|---|---|---|---|---|---|
| U05-MED-001 | U05-020 | video_or_gif | Audio de tres tonos y suma | 2 s por tono + 3 s suma; pausas de 0,5 s; total 10–11 s | después de que el curso prediga cuántas componentes verá/oirá | sí; nivel moderado, no juicio de sonoridad | WAV PCM 48 kHz/24 bit local, cuatro pistas y versión concatenada | CH-005 con componentes y suma | Producción propia UCASAL; parámetros en README | proposed |
| U05-MED-002 | U05-020–021 | video_or_gif | Animación de síntesis de Fourier | 8–12 s, una pasada; 1→3→5→más componentes | después del audio y antes de la ecuación de serie | no en primera pasada; audio opcional no esencial | MP4 H.264 y GIF local derivados de CH-005 | cuatro frames SVG/PNG con escalas idénticas | Producción propia basada en TEX/PDF fig. 5.2 | proposed |
| U05-MED-003 | U05-048, U05-071 | video_or_gif | Vocal sostenida autorizada | 2–3 s de tramo estable, una reproducción | antes de mostrar el espectrograma y otra vez al leer líneas/envolvente | sí; nivel moderado | WAV PCM local; registro sintético si no hay consentimiento | forma temporal CH-004 y espectro CH-012 | Producción propia; consentimiento y cadena de captura obligatorios | blocked_asset |
| U05-MED-004 | U05-048 | video_or_gif | Espectrograma sincronizado con cursor | 6–8 s; cursor recorre inicio, tramo estable y final | después de identificar ejes y color en la imagen estática | opcional; primera pasada sin audio, segunda con U05-MED-003 | MP4/GIF local; no streaming | espectrograma completo CH-010 con tres zonas | Producción propia desde U05-MED-003 | blocked_asset |
| U05-MED-005 | U05-102 | video_or_gif | Frase original y versiones filtradas | original, pasa bajos, pasa altos y pasa banda: 2 s cada una; total 10–12 s | después de predecir el filtro y antes de revelar respuestas | sí; igualación de nivel documentada | WAV local por versión y concatenado | respuestas CH-016 + espectros antes/después | Producción propia UCASAL | proposed |

## Parámetros y seguridad

- Audio: PCM WAV, 48 kHz, 24 bit; pico digital máximo recomendado `−12 dBFS`; normalización y RMS documentados.
- Verificar el volumen de aula antes de cada demostración; reproducir ejemplos breves y nunca usar el audio como prueba clínica o umbral.
- Animaciones: una reproducción guiada y pausa; sin loops distractores.
- MP4 H.264 como formato principal de video y GIF solo como alternativa de compatibilidad.
- Capturas: PNG 1920×1080 o SVG del estado clave; deben permitir dictar la clase sin reproducir el medio.
- La vocal se anonimizará; no se almacenarán nombres ni metadatos personales en el archivo.

## Recursos descartados

- Videos externos de ecografía: desplazan el foco hacia procedimientos médicos y requieren más contexto del que aporta U5.
- Videos de interfaces de software FFT: quedan rápidamente desactualizados y mezclan herramienta con concepto.
- Apps de sonometría como demostración principal: se puede citar NIOSH para discutir límites, pero la cadena conceptual y el instrumento real son suficientes.

## Estado

**Planificado; no producido.** Todos los recursos tienen alternativa estática y no dependen de conexión.
