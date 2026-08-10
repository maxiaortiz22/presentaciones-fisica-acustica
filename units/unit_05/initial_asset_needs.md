# Unidad 5 — Necesidades iniciales de assets y multimedia

## Alcance

Este registro deriva de `storyboard.md` y separa recursos externos o multimedia de los gráficos cuantitativos y diagramas propios. No autoriza todavía descargas, generación final ni incorporación al PowerPoint. La prioridad es que cada recurso cumpla una función observable y tenga alternativa estática.

## Criterios de curaduría

- Preferir registros propios, material del docente y fuentes técnicas institucionales.
- No usar fotografías de stock ni imágenes meramente decorativas.
- Para voz o audio: contar con permiso de uso, anonimizar si corresponde y registrar condiciones de captura.
- Para instrumentos: mostrar el montaje o la función técnica, no una marca como protagonista.
- Para toda fuente externa: URL, autor/organización, licencia, fecha de acceso y uso pedagógico.
- Todo audio debe tener nivel de reproducción seguro, duración breve, consigna previa y alternativa visual.
- Ningún dato clínico o perceptual se presentará como universal a partir de una imagen aislada.

## Inventario inicial

| asset_id | slides previstas | tipo | necesidad | función pedagógica | fuente preferida | requisitos y alternativa | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U05-AS-001 | U05-020 | audio propio | Tres tonos puros y su suma, con pistas separadas y combinada | Oír que una forma compleja puede construirse con componentes simples | Generación propia reproducible | Igualar nivel RMS aproximado; advertir volumen; mostrar formas temporales y espectros si no hay audio | alta | por producir |
| U05-AS-002 | U05-048, U05-071 | audio y registro de voz | Vocal sostenida breve, estable y autorizada | Vincular forma temporal, espectrograma, armónicos y envolvente/formantes | Registro propio del docente o voluntario con consentimiento | Documentar micrófono, `f_s`, duración, ventana; usar registro sintético o figura estática si no hay autorización | alta | por decidir |
| U05-AS-003 | U05-078 | imagen técnica externa | Ejemplo de ultrasonido/ecografía o aplicación técnica equivalente | Mostrar que “ultrasonido” nombra una región y una tecnología, no una experiencia auditiva | Universidad, hospital, organismo o fabricante técnico con licencia clara | Pie de figura con contexto y límites; alternativa: diagrama propio del principio físico | media | por curar |
| U05-AS-004 | U05-081 | imagen técnica o dataset | Montaje de medición de vibración/sonido en un instrumento o fuente compleja | Conectar rango dinámico y espectral con una medición real | Fotografía propia, laboratorio o publicación técnica | La imagen debe permitir señalar sensor, fuente y condición; alternativa: esquema propio con datos sintéticos | media | por curar |
| U05-AS-005 | U05-102 | audio propio | Frase breve sin filtrar y versiones pasa bajos, pasa altos y pasa banda | Experimentar qué información cambia al filtrar | Producción propia desde una grabación autorizada | Normalizar con criterio declarado; evitar diferencias de nivel que revelen la respuesta; espectros estáticos como respaldo | alta | por producir |
| U05-AS-006 | U05-118, U05-117 | fotografía técnica | Sonómetro y calibrador acústico, idealmente en uso | Reconocer los elementos de la cadena de medición y la verificación | Equipo propio del curso o fabricante con permiso | Evitar publicidad; rotular micrófono, calibrador y pantalla; alternativa: diagrama editable de cadena | alta | por curar |
| U05-AS-007 | U05-123 | fotografía o esquema de contexto | Medición ambiental/audiométrica como caso hipotético | Situar el ejercicio de bandas sin convertirlo en protocolo clínico | Fotografía propia o institución académica | Rotular “caso didáctico hipotético”; alternativa: plano esquemático del recinto | baja | opcional |
| U05-AS-008 | U05-127 | audio opcional | Mismo estímulo reproducido bajo tres condiciones controladas o simulado | Discutir qué puede inferirse y qué metadatos faltan | Producción propia | No usar si la comparación no es calibrada; la slide funciona con gráficos y ficha de condiciones | baja | opcional |

## Demostraciones propuestas

| demo_id | slides | preparación | interacción prevista | contingencia |
|---|---|---|---|---|
| U05-DEMO-01 | U05-020 | Generar senoides individuales y suma con parámetros visibles | Predecir cuántos componentes se oirán/verán antes de reproducir | Comparar cuatro paneles estáticos |
| U05-DEMO-02 | U05-043–048 | Script o archivo preparado que cambie longitud, ventana y solapamiento | Preguntar qué cambia por la señal y qué cambia por el análisis | Secuencia de gráficos exportados |
| U05-DEMO-03 | U05-102 | Preparar frase y tres versiones filtradas | Elegir qué filtro se aplicó y justificar con evidencia espectral | Espectros + transcripción de la frase |
| U05-DEMO-04 | U05-107–124 | Sonómetro o simulación con lecturas A/Z y variación temporal | Completar una ficha mínima de medición | Capturas verificadas y diagrama de cadena |

## Datos y metadatos obligatorios

Para cada audio o registro se deberán conservar: procedencia, autorización, frecuencia de muestreo, profundidad de bits si resulta relevante, duración, canal, cadena de captura, edición, normalización, nivel de reproducción previsto y fecha. Para imágenes externas: crédito, enlace, licencia y recorte realizado.

## Decisiones pendientes

1. Confirmar disponibilidad de sonómetro, calibrador y sistema de reproducción en aula.
2. Resolver si la voz será real, sintética o ambas; la elección afecta U05-AS-002 y varios gráficos.
3. Seleccionar una aplicación de ultrasonido vinculada al perfil profesional sin abrir un bloque biomédico ajeno al alcance.
4. Definir si las demostraciones se harán en vivo o con material precomputado.
5. Validar con el docente el nivel seguro y la duración total de las experiencias auditivas.

## Estado

**Inventario inicial.** No se descargaron ni aprobaron assets. La curaduría definitiva corresponde a la fase `asset-curation` y deberá alimentar `asset_manifest.csv`.
