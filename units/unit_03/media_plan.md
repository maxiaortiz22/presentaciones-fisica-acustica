# Unidad 3 — Plan de video, GIF, animación y audio

## Decisión general

La multimedia se reserva para procesos temporales que pierden claridad en una imagen única: avance de un pulso, movimiento local frente a propagación, transitorios de un tono y cancelación localizada. Ninguna idea obligatoria depende de conexión a internet ni de reproducción de audio.

No se descargaron recursos. La producción propia es la opción preferida porque permite controlar referentes, velocidad y exactitud.

## Plan de archivos y recursos temporales

| media_id | slides | tipo | fuente y licencia | fragmento recomendado | duración | momento de reproducción | audio | alternativa sin conexión | captura estática de respaldo | estado |
|---|---|---|---|---|---|---|---|---|---|---|
| U03-MEDIA001 | U03-013–014 | Video propio de demostración | Producción docente UCASAL | Pulso único que atraviesa el resorte con una espira marcada visible desde antes del impulso hasta después del paso | 8–12 s | Después de la predicción y antes de nombrar frente/partícula; repetir una vez en cámara lenta | No; el sonido ambiente no aporta | MP4 H.264 1080p local | Cuatro PNG: antes, llegada, paso y después | proposed |
| U03-MEDIA002 | U03-013 | Simulación interactiva | PhET, University of Colorado Boulder; CC BY-NC 4.0 para aula no comercial, atribución y logo obligatorios | Modo pulso, extremo sin reflexión durante la observación, velocidad lenta, regla y una marca visual | 20–30 s de interacción | Solo si no existe resorte propio o para comprobar amplitud/longitud; no como video pasivo | No; desactivar audio y sonificación | No descargar en esta etapa; si falla la conexión, usar U03-MEDIA001 o fotogramas | Captura de configuración y cuatro estados propios, sin ocultar logo si se usa PhET | shortlisted |
| U03-MEDIA003 | U03-061–062 | Animación propia | Elaboración propia a partir del modelo del capítulo | Onda sinusoidal con una partícula marcada y una cresta marcada; pausa en dos extremos y dos cruces | 6–8 s, reproducción única | Después de preguntar “¿qué velocidad representa cada marcador?” | No | MP4 y GIF locales generados por script | Seis PNG numerados y diagrama U03-DG020 | proposed |
| U03-MEDIA004 | U03-061 | GIF externo opcional | KyleThayer, Wikimedia Commons; CC0 1.0 | Tramo de 3–5 s donde la fuente comienza a oscilar y aparece el patrón de propagación | Original: 10 s; usar reproducción única, no loop continuo | Solo después de verificar que no sugiere transporte material ni otra variable no explicada | No contiene audio | No depender del GIF; usar U03-MEDIA003 | Fotograma seleccionado y anotado fuera del archivo original | shortlisted; requiere revisión cuadro a cuadro |
| U03-MEDIA005 | U03-040–041 | Audio sintético | Elaboración propia mediante script | Tono de 500 Hz, 1,0 s, con 50 ms de ataque y caída; versión adicional sin fades solo para comparar el modelo gráfico, no para reproducir a alto nivel | 1 s por archivo; máximo dos reproducciones | Después de leer U03-CH005 y antes de cerrar la diferencia ideal/real | Sí, necesario para este recurso; nivel cómodo y no calibrado | WAV local incrustable y plan de omitirlo | U03-CH005 con envolvente y señal | proposed |
| U03-MEDIA006 | U03-064–068; U03-072–075 | Audio sintético opcional | Elaboración propia mediante script | Dos tonos de 500 Hz por separado y suma mono con `Δφ=0`, `π/2`, `π`; misma ganancia de entrada y limitador desactivado | 1,0 s por caso, con fades de 30 ms | Después de la predicción gráfica; nunca para “demostrar” que la fase absoluta aislada es perceptible | Sí | WAV locales; si el sistema altera canales o fase, omitir | U03-CH010 y U03-CH012 | proposed; baja prioridad |
| U03-MEDIA007 | U03-076 | GIF o MP4 conceptual propio | Elaboración propia a partir de TEX 3.8.5 | Frente primario, señal secundaria y una zona puntual que disminuye; repetir con el punto de observación desplazado | 6–8 s | Después del diagrama estático y antes de discutir límites | No; el audio podría sugerir cancelación universal | MP4/GIF local; diagrama U03-DG022 es suficiente | Tres estados: antes, coincidencia y punto desplazado | proposed |

## Especificaciones de producción

### U03-MEDIA001 — resorte

- Cámara fija lateral y fondo neutro.
- Resorte ocupando al menos 70 % del ancho.
- Una espira marcada con cinta de alto contraste.
- Movimiento transversal declarado como modelo de propagación, no como representación literal del sonido en aire.
- No estimar `c`, `T` o `λ` si no hay escala y tiempo calibrados.
- Exportar original, MP4 1080p y cuatro PNG; no borrar el original.

### U03-MEDIA003 — partícula y frente

- Lienzo 1920 × 1080 px.
- Mismo dataset o convención de U03-CH007.
- Partícula marcada en bordó; fase o cresta en teal; forma o etiqueta adicional para accesibilidad.
- La partícula invierte sentido; la fase continúa en la dirección de `c`.
- Velocidad visual reducida sin alterar la relación de fase.
- Exportar MP4, GIF optimizado, seis PNG y parámetros JSON.

### U03-MEDIA005 y U03-MEDIA006 — audio

- Frecuencia de muestreo 48 kHz, PCM 24 o 16 bit.
- Pico digital máximo recomendado: -12 dBFS antes de sumar.
- Fades cosenoidales para evitar clics.
- No declarar SPL ni calibración.
- Reproducir a nivel cómodo y por duración breve.
- Para `Δφ=π`, comprobar cancelación numérica de la suma antes del fade común.
- Conservar WAV fuente; MP3 solo como copia de distribución si fuera necesario.

### U03-MEDIA007 — cancelación

- Rotular “esquema conceptual; no a escala”.
- La zona de reducción debe ser localizada, no abarcar toda la escena.
- Mostrar una segunda posición donde la suma ya no es nula.
- No usar ondas de color como única codificación; añadir rótulos “primaria” y “secundaria”.

## Animaciones internas de PowerPoint

No generan un archivo multimedia separado.

| animation_id | slides | secuencia | duración sugerida | disparo | estado final |
|---|---|---|---|---|---|
| U03-ANI001 | U03-002 | Fuente → aire vecino → regiones sucesivas → receptor | 4 pasos de 0,4 s | Por clic durante predicciones | Cadena completa |
| U03-ANI002 | U03-006 y recaps | Activar una etapa del mapa por bloque | 0,2–0,3 s por etapa | Por clic | Mapa completo o progreso actual |
| U03-ANI003 | U03-009 | Instantes de propagación con partícula marcada | 5 pasos de 0,35 s | Por clic o avance automático controlado | Último instante más traza tenue |
| U03-ANI004 | U03-020 | Cinco estados de un ciclo | 0,35 s por estado | Por clic | Ciclo completo |
| U03-ANI005 | U03-042 | Revelar `V`, cono, aire y presión | 4 pasos de 0,4 s | Por clic | Cadena completa con variables |
| U03-ANI006 | U03-044 | Cono hacia afuera → compresión; cono hacia adentro → rarefacción | 2 pasos de 0,6 s | Por clic | Dos estados en paralelo |
| U03-ANI007 | U03-056 | Snapshot inicial → avance durante `T` → corchete `λ` → ecuación | 4 pasos de 0,4 s | Por clic | Relación `c=λf` completa |
| U03-ANI008 | U03-081 | Recorrer conexiones del mapa final | 8 pasos de 0,25 s | Por clic | Mapa final completo |

Las animaciones internas deben dejar una composición final autosuficiente para PDF o impresión.

## Créditos previstos

- PhET:
  - “Simulación realizada por PhET Interactive Simulations, Universidad de Colorado Boulder, bajo licencia CC BY-NC 4.0 (https://phet.colorado.edu).”
- Wikimedia Commons:
  - “KyleThayer, *Sound wave animation no labels*, CC0, vía Wikimedia Commons.”
- Producción propia:
  - “Elaboración propia a partir del capítulo 3 del libro del curso.”

## Decisiones pendientes

1. Confirmar disponibilidad de resorte largo y espacio de filmación.
2. Confirmar sistema de reproducción y política de volumen para los audios.
3. Revisar U03-MEDIA004 cuadro a cuadro antes de aprobarla.
4. Definir si U03-MEDIA006 aporta algo al grupo; no es necesaria para el aprendizaje central.
5. No descargar PhET hasta decidir si se necesita acceso sin conexión y verificar la versión concreta.

