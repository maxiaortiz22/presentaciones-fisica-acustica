# Unidad 9 — Plan de audio, animaciones y multimedia

Versión de planificación · 2026-08-12

## Criterio general

Los recursos temporales se clasifican como `video_or_gif`. Serán opcionales, locales y controlados manualmente. Ninguno sustituye una explicación estática, una medición normalizada o una certificación. No habrá autoplay, loop continuo ni dependencia de streaming.

Formatos preferidos:

- audio maestro: WAV PCM 48 kHz/24 bit; pico ≤−3 dBFS; nivel de reproducción confortable y no calibrado;
- animación: MP4 H.264 1920×1080, 25/30 fps; GIF silencioso solo si conserva etiquetas;
- captura estática: PNG 1920×1080 o estado final editable;
- subtítulos/transcripción para todo recurso con habla;
- reproducción una sola vez, después de una predicción del grupo.

## Recursos

### U09-MEDIA-001 — Habla seca y reverberada

- **Slides:** U09-055; apoyo conceptual U09-049.
- **Clasificación:** `video_or_gif` por incluir audio; la slide completa es `video_or_gif` con fallback `chart`.
- **Tipo:** audio propio + animación sincronizada de U09-CH-006.
- **Propósito:** relacionar la experiencia auditiva con una envolvente temporal y el concepto de decaimiento.
- **Fragmento recomendado:** una frase neutra de 2–3 s en versión seca, pausa de 1 s y misma frase procesada; duración total 7–9 s.
- **Momento:** después de que el grupo prediga qué cambia al aumentar la reverberación y antes de la recapitulación U09-056.
- **Audio:** sí; voz docente/UCASAL con consentimiento o grabación propia aprobada. No usar corpus externo mientras no se verifique licencia y tratamiento de voz.
- **Procesamiento:** convolución reproducible con respuesta impulsional sintética o propia; parámetros, tiempo de decaimiento, mezcla directo/reverberado y normalización documentados.
- **Alternativa sin conexión:** WAV local y dos envolventes estáticas; si no hay audio, el gráfico U09-CH-006 conserva el objetivo.
- **Captura estática:** dos mini envolventes con la misma frase/energía de entrada y cola distinta, rótulos “seca” y “reverberada”.
- **Validaciones:** misma locución y ganancia comparables; cero clipping; no convertir dBFS en dB SPL; nivel seguro; transcripción exacta; advertencia “demostración no calibrada”.
- **Estado:** listo para producir con material propio; no se descargó audio externo.

### U09-MEDIA-002 — Gradiente térmico y curvatura

- **Slides:** complemento de U09-025.
- **Clasificación:** `video_or_gif` derivado de `diagram` U09-DG-018.
- **Tipo:** animación propia por estados.
- **Propósito:** hacer visible la diferencia entre aire uniforme, suelo cálido e inversión térmica sin superponer todos los rayos desde el inicio.
- **Fragmento recomendado:** 9–12 s: perfil uniforme 3 s → suelo cálido 3–4 s → inversión 3–4 s → estado comparativo final 2 s.
- **Momento:** después de leer `c(θ)` y antes de explicar viento uniforme.
- **Audio:** no; narración docente en vivo.
- **Alternativa sin conexión:** U09-DG-018 en dos paneles, más un estado uniforme pequeño.
- **Captura estática:** estado final con perfiles `θ(z)`/`c(z)` y dos familias de trayectorias.
- **Producción:** formas editables de PowerPoint, exportación MP4; GIF solo si rótulos permanecen ≥20 pt.
- **Validaciones:** rayos curvan hacia menor rapidez; perfiles y trayectorias sincronizados; movimiento no implica partículas siguiendo el rayo; versión estática autosuficiente.
- **Estado:** listo para producir después de aprobar U09-DG-018.

### U09-MEDIA-003 — Viento uniforme frente a gradiente

- **Slides:** complemento de U09-026–027.
- **Clasificación:** `video_or_gif` derivado de U09-DG-019/020.
- **Tipo:** animación propia comparativa.
- **Propósito:** mostrar que el viento uniforme cambia la rapidez efectiva respecto del suelo, mientras el gradiente introduce curvatura en el modelo.
- **Fragmento recomendado:** 8–10 s: vector uniforme y trayecto recto 3 s → perfil `v_viento(z)` 2 s → trayectorias a favor/en contra 3–5 s.
- **Momento:** después de interpretar `c_ef=c+v_viento cos ψ`, antes de U09-028.
- **Audio:** no.
- **Alternativa sin conexión:** dos slides estáticas U09-026 y U09-027; no se pierde información.
- **Captura estática:** comparación uniforme/gradiente con perfiles y rótulos de dirección.
- **Producción:** animación de PowerPoint o MP4 H.264; no usar partículas decorativas.
- **Validaciones:** mismo viento de referencia, símbolos coherentes, trayecto uniforme sin curvatura, etiquetas fuera de flechas, sentido del viento inequívoco.
- **Estado:** listo para producir tras validar notación `v_viento`.

### U09-MEDIA-004 — Rutas de ingreso a una cabina

- **Slides:** complemento de U09-071; apoyo U09-077.
- **Clasificación:** `video_or_gif` derivado de `diagram` U09-DG-054.
- **Tipo:** revelado progresivo de rutas.
- **Propósito:** reducir carga visual y mostrar que la ruta limitante puede cambiar sin mover la geometría del sistema.
- **Fragmento recomendado:** 10–12 s: envolvente 2 s → juntas/puerta 2 s → ventilación 2 s → flanqueo/vibración 2 s → ruido propio y estado completo 2–4 s.
- **Momento:** después de identificar elementos U09-070 y antes del proceso de verificación U09-072.
- **Audio:** no; no simular “cuánto se oye” cada ruta.
- **Alternativa sin conexión:** U09-DG-054 completo, con revelado manual por duplicación de objetos o puntero docente.
- **Captura estática:** estado final con todas las rutas, rótulos y leyenda.
- **Producción:** estados editables de PowerPoint; MP4 opcional. GIF no recomendado si obliga a reducir etiquetas.
- **Validaciones:** geometría idéntica a U09-DG-053; conectores detrás de componentes; cero cruces; cada ruta tiene inicio/destino; no se asignan atenuaciones.
- **Estado:** listo para producir después de aprobar la familia de cabina.

## Recursos externos descartados o postergados

- No se selecciona un video de fabricante sobre cabinas: suele mezclar publicidad, desempeño comercial y condiciones no verificables.
- No se usa un GIF genérico de ondas o “partículas sonoras”: los gradientes requieren perfiles y símbolos controlados.
- No se descarga una respuesta impulsional o voz de repositorio mientras no se cierre licencia, consentimiento y trazabilidad; la producción propia es más segura.
- Las fotografías externas de cabinas se gestionan en `asset_plan.md` y no se convierten en video.

## Seguridad, accesibilidad y verificación

1. Ningún audio es prueba de umbral, simulador clínico o demostración calibrada.
2. La información esencial está en el estado estático.
3. Control manual y una sola reproducción; volumen ajustado antes de clase.
4. Audio con transcripción; animaciones narrables sin audio.
5. Captura estática, caption, alt text y parámetros archivados junto al recurso.
6. MP4/GIF se revisan cuadro a cuadro para clipping, legibilidad, parpadeo y cambios de unidad.
