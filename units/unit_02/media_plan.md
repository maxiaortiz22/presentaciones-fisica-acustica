# Unidad 2 — Plan de multimedia

## Principio de uso

La multimedia se reserva para cambios temporales que una figura única no comunica con la misma claridad. Ninguna explicación dependerá de streaming, reproducción automática o audio. Cada recurso tendrá:

- archivo local o demostración realizable;
- duración y fragmento definidos;
- consigna de observación;
- captura estática;
- alternativa sin conexión;
- estado final comprensible.

No se planifican recursos de audio. Escuchar un tono no ayuda a observar fuerzas, energía o entropía y podría adelantar relaciones perceptuales que la unidad busca tratar con cautela.

## Plan de videos, GIFs y demostraciones

| media_id | slides | recurso | fragmento recomendado | duración | momento de reproducción | audio | alternativa sin conexión | captura estática de respaldo | fuente/licencia | estado |
|---|---|---|---|---:|---|---|---|---|---|---|
| U02-MEDIA001 | U02-002 | Demostración o clip propio de superficie flexible | Equilibrio visible; aplicar una diferencia cualitativa; observar deformación o inicio de movimiento; detener antes de oscilaciones complejas | 8–12 s útiles; archivo total ≤20 s | Después de preguntar qué cambiará y antes de mostrar flechas | No; silenciar ambiente | Demostración física en vivo o MP4 H.264 local | Tres cuadros: equilibrio, diferencia aplicada, respuesta | Producción propia UCASAL | proposed |
| U02-MEDIA002 | U02-034 | Video propio de masa–resorte con dos amortiguamientos | Dos tomas paralelas o consecutivas con la misma masa, desplazamiento inicial y encuadre; comparar reducción de amplitud | 10–15 s; máximo dos repeticiones | Después de pedir que observen “cuánto tarda en disminuir” y antes de nombrar `b` | No | MP4 local; si falla, secuencia de cuatro posiciones por condición | Inicio, primer extremo opuesto, segundo extremo y estado tardío para cada condición | Producción propia UCASAL | proposed; preferido |
| U02-MEDIA003 | U02-069 | Animación propia de oscilación amortiguada y ruta energética | Masa oscila con amplitud decreciente; indicador cualitativo de energía mecánica baja y energía interna aumenta | 8–10 s, un ciclo narrativo; no loop continuo | Después de recuperar amortiguamiento y antes de definir entropía | No | MP4 y GIF locales | Tres estados con barras cualitativas de igual escala y rótulo “no proporcional” | Elaboración propia; modelo conceptual no a escala | proposed |
| U02-MEDIA004 | U02-077; apoyo U02-078 | Animación longitudinal de compresión/rarefacción | Un frente avanza de izquierda a derecha mientras una partícula marcada oscila alrededor de su posición | 8–10 s; máximo dos repeticiones | Primero seguir el frente; segunda reproducción seguir la partícula | No | MP4/GIF local | Tres estados: antes, frente sobre la marca, después | Elaboración propia; adaptar la gramática de U01-CH002 y verificar alcance U2 | proposed |
| U02-MEDIA005 | U02-034 | PhET “Masas y Resortes: Fundamentos” como alternativa interactiva | Configurar una masa y un resorte; comparar damping bajo/alto sin cambiar masa ni desplazamiento inicial | 20–30 s de interacción | Solo si no se dispone de U02-MEDIA002 o para responder una pregunta | No; desactivar cualquier sonificación | Archivo HTML5 histórico local únicamente tras verificar versión anterior a 2026-03-29 | Captura de dos configuraciones con mismos parámetros excepto amortiguamiento | PhET Interactive Simulations, University of Colorado Boulder; versión histórica CC BY 4.0, atribución obligatoria | shortlisted; no descargado |

## Especificaciones de producción

### U02-MEDIA001 — superficie flexible

- Cámara fija y lateral o ligeramente oblicua.
- Fondo neutro y alto contraste con la superficie.
- Montaje estable; no usar presión no controlada como dato cuantitativo.
- No mostrar manómetros si no se calibra la medición.
- El caption debe decir “demostración cualitativa”.
- Exportar MP4 H.264 1080p, 25/30 fps y tres PNG.

### U02-MEDIA002 — masa–resorte

- Misma masa, longitud de resorte, desplazamiento inicial, escala y encuadre.
- Cambiar solo el mecanismo de amortiguamiento visible o la configuración de damping.
- Incluir una referencia fija de equilibrio.
- Evitar rebotes de cámara y manos en el recorrido.
- No estimar `b` a partir del video.
- Exportar MP4 H.264 1080p y ocho fotogramas PNG.

### U02-MEDIA003 — amortiguamiento y energía

- Lienzo 1920 × 1080 px, fondo transparente o blanco.
- Masa y equilibrio coherentes con U02-DG006.
- La amplitud decrece de forma suave; no hace falta resolver la ecuación diferencial del sistema.
- Los indicadores energéticos son cualitativos y deben rotularse “esquema, no proporciones”.
- Salidas: MP4 H.264, GIF optimizado y PNG de tres estados.
- El loop GIF no debe producir un reinicio brusco; preferir reproducción única en PowerPoint.

### U02-MEDIA004 — compresión y rarefacción

- Lienzo 1920 × 1080 px.
- Cadena horizontal de partículas con posiciones de equilibrio discretas.
- Una partícula marcada en bordó; frente o región de compresión en teal.
- La partícula marcada vuelve cerca de su posición inicial.
- No introducir longitud de onda, frecuencia o resonancia como rótulos.
- Salidas: MP4, GIF y PNG de tres estados.

### U02-MEDIA005 — PhET

- Usar una versión histórica HTML5 publicada antes de 2026-03-29.
- Confirmar versión y fecha en el diálogo `About`.
- Conservar visible el logo PhET.
- Atribución exacta:

  > Simulation by PhET Interactive Simulations, University of Colorado Boulder, licensed under CC BY 4.0 (https://phet.colorado.edu).

- Descargar solo después de aprobar su uso y verificar que la versión histórica puede ejecutarse sin conexión.
- No grabar ni recortar una captura que oculte controles relevantes o el logo.

## Animaciones internas de PowerPoint

Las siguientes animaciones no generan un archivo multimedia separado:

| animation_id | slides | secuencia | duración | disparo | estado final |
|---|---|---|---:|---|---|
| U02-ANI001 | U02-002 | presiones → fuerzas → pregunta | 6–8 s | por clic | ambos estados completos |
| U02-ANI002 | U02-006 | cinco etapas | 8–10 s | por clic | mapa completo |
| U02-ANI003 | U02-011 | fuerzas individuales → suma → resultante | 8–12 s | por clic | diagrama completo |
| U02-ANI004 | U02-025–028 | fuerzas → `Δp` → `F_pres` | 10–15 s distribuidos | por clic | cada slide independiente |
| U02-ANI005 | U02-035–042 | masa → resorte → amortiguador → balance | 20–30 s distribuidos | por clic | modelo y ecuación completos |
| U02-ANI006 | U02-052–055 | intercambio → rutas → balance | 12–18 s | por clic | balance completo |
| U02-ANI007 | U02-063–065 | estado → transferencias → cuatro signos | 10–15 s | por clic | cuatro casos completos |
| U02-ANI008 | U02-089 | cadena final de seis nodos | 10–15 s | por clic | mapa final completo |

Solo se permite aparición y énfasis. No se animan títulos, logos ni elementos decorativos.

## Capturas estáticas

| media_id | captura requerida | función |
|---|---|---|
| U02-MEDIA001 | tres estados de la superficie | mantener la pregunta si no hay demostración |
| U02-MEDIA002 | cuatro estados por nivel de amortiguamiento | comparar trayectorias sin video |
| U02-MEDIA003 | inicio, estado intermedio y estado tardío | mostrar amplitud y destino energético |
| U02-MEDIA004 | frente antes, durante y después de la partícula marcada | separar propagación y movimiento local |
| U02-MEDIA005 | dos configuraciones con parámetros visibles | documentar la comparación de PhET |

## Comportamiento sin conexión

1. Ningún recurso se reproduce desde una URL durante la clase.
2. MP4 y GIF aprobados se guardarán junto al deck o se incrustarán.
3. Cada medio tendrá PNG de respaldo en la misma carpeta.
4. Las notas indicarán tiempo de reproducción y qué observar.
5. Si PowerPoint falla, la slide conserva la secuencia estática.
6. PhET no se considerará disponible hasta probar el HTML local en el equipo de aula.

## Accesibilidad y seguridad

- Sin parpadeos ni loops continuos distractores.
- Contraste suficiente para partícula, frente y equilibrio.
- Texto alternativo que describa el cambio temporal.
- La información esencial no depende del color.
- Sin audio necesario; no se requieren advertencias de nivel sonoro.
- Si aparece una persona en una producción propia, obtener autorización o encuadrar solo manos/dispositivo.

