# Unidad 10 — Necesidades iniciales de assets y multimedia

## Alcance

Inventario previo a `asset-curation`. No se descargaron, generaron ni aprobaron recursos. La prioridad es usar gráficos y diagramas propios; una imagen externa solo se justifica cuando muestra un montaje, instrumento o contexto real que un esquema no puede representar con igual claridad.

## Principios

- No usar imágenes de stock de personas tapándose los oídos.
- No presentar espuma acústica como símbolo universal de aislamiento.
- Todo audio debe declarar origen, procesamiento, duración, nivelado y cadena de reproducción.
- La experiencia auditiva debe tener alternativa visual completa.
- No reproducir señales clínicas ni normativas sin especificación de equipo/procedimiento.
- No usar logos, interfaces o productos sin necesidad pedagógica y fuente oficial.

## Inventario inicial

| asset_id | slides | tipo | propósito pedagógico | especificación mínima | fuente objetivo | licencia/trazabilidad | prioridad | estado |
|---|---|---|---|---|---|---|---|---|
| U10-AS-001 | U10-035 | audio | Comparar ruido blanco con representación espectral. | 6–10 s; banda finita declarada; WAV; RMS/criterio de nivelado registrado; fade in/out. | Generación propia reproducible. | Script, semilla, parámetros y fecha. | alta | pendiente de `asset-curation` y seguridad |
| U10-AS-002 | U10-035 | audio | Comparar ruido rosa con el blanco. | Mismo formato, duración y criterio de nivelado que AS-001; banda idéntica. | Generación propia reproducible. | Script, filtro, parámetros y fecha. | alta | pendiente de `asset-curation` y seguridad |
| U10-AS-003 | U10-040/043/060 | audio opcional | Escuchar cómo una banda estrecha limita el contenido. | 4–6 s; `f_L`, `f_c`, `f_H`, pendientes y nivel relativo declarados; no rotular como señal clínica calibrada. | Generación propia o documentación técnica autorizada. | Script o URL/autor/licencia. | media | condicionado a criterio docente |
| U10-AS-004 | U10-038/039/043 | audio opcional | Ilustrar ruido con espectro de habla sin afirmar curva universal. | Espectro objetivo identificado; lengua/corpus o norma/equipo declarado; 6–10 s. | Norma, fabricante técnico o elaboración propia con objetivo documentado. | Fuente completa y permiso de uso. | alta | bloqueado por selección de fuente |
| U10-AS-005 | U10-074 | fotografía técnica | Contrastar observación exploratoria y medición trazable. | Teléfono y sonómetro/micrófono en posición de medición; sin publicidad; encuadre horizontal. | Universidad, organismo técnico o fotografía propia. | Autor, fecha, contexto y licencia. | media | pendiente de búsqueda |
| U10-AS-006 | U10-002/055/077 | fotografía de contexto opcional | Situar consultorio, avenida o aula sin sustituir el mapa conceptual. | Debe mostrar fuente/trayecto/receptor identificables; sin pacientes reconocibles. | Fotografía propia o institución. | Consentimientos y licencia si corresponde. | baja | usar solo si supera al diagrama |
| U10-AS-007 | U10-060 | fotografía técnica opcional | Mostrar transductores audiométricos reales después del diagrama funcional. | Equipo identificado; sin sugerir configuración universal; recorte sobre fondo simple. | Fabricante técnico o laboratorio universitario. | URL, modelo, licencia y fecha. | baja | respaldo, no necesaria para el núcleo |
| U10-AS-008 | U10-068/092 | documentos normativos | Mostrar portadas/metadatos de fuentes, no tablas de memoria. | Edición y organismo legibles; máximo 2–3 miniaturas. | ISO/IEC/NIOSH/Argentina según decisión. | Uso permitido, enlace y fecha. | media | bloqueado por decisión normativa |

## Recursos multimedia previstos

| media_set | componentes | consigna de aula | alternativa si falla | control de seguridad |
|---|---|---|---|---|
| U10-MD-001 · Blanco/rosa | AS-001 y AS-002 | “Escuche diferencias y luego compruebe qué muestra el espectro; no juzgue sonoridad absoluta”. | U10-CH-010 con densidad y barras por octava. | Nivel del sistema fijado antes; duración breve; sin auriculares compartidos a nivel no controlado. |
| U10-MD-002 · Banda estrecha | AS-003 | “Identifique qué región frecuencial permanece”. | Respuesta pasabanda U10-DG-024. | Clip breve; nivelado y banda declarados. |
| U10-MD-003 · Espectro de habla | AS-004 | “Observe qué información de la voz conserva el contorno espectral y qué no”. | Esquema cualitativo U10-DG-022/023. | No presentarlo como estímulo clínico calibrado. |

## Assets que no se necesitan

- Ilustraciones decorativas de ondas, orejas, colores o ciudades.
- Capturas de ecuaciones.
- Infografías comerciales de protectores auditivos.
- Imágenes generadas por IA de equipos, cabinas o pruebas reales.
- GIFs de forma de onda si un gráfico reproducible ofrece mayor precisión.

## Dependencias y bloqueos

1. AS-004 requiere decidir una especificación concreta de ruido con espectro de habla.
2. AS-008 requiere norma, edición, jurisdicción y permiso de reproducción.
3. Todos los audios requieren validar nivel, duración y alternativa visual antes de incorporarse.
4. Las fotografías con personas o contexto clínico requieren consentimiento/licencia y no deben aportar información identificable.

## Criterios de aceptación posterior

- propósito pedagógico explícito;
- identificador y manifiesto coincidentes;
- fuente y licencia trazables;
- calidad suficiente para media slide o visual dominante;
- recorte sin deformación;
- texto alternativo preparado;
- audio reproducible y seguro;
- ninguna afirmación normativa o clínica implícita no respaldada.
