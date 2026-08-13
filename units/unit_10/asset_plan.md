# Unidad 10 — Plan integral de recursos visuales y externos

Versión de planificación · 2026-08-12

## Decisión general

El recurso dominante será propio: 16 gráficos cuantitativos planificados, 60 diagramas/ecuaciones identificados, tablas nativas y cuatro audios sintéticos opcionales. Solo se preselecciona una captura externa para U10-074; no se justifica usar imagen anatómica, video externo, GIF decorativo ni imagen generada con IA.

La clasificación se realiza antes de producir: `chart`, `diagram`, `mixed`, `external_image`, `video_or_gif` o `equation_only`. `none` no es una clase de asset: registra que una slide se resuelve con tipografía, tabla nativa o espacio de actividad y no requiere imagen.

## Enrutamiento por skill

| clase | responsable | resultado previsto |
|---|---|---|
| `chart` | `chart-generation` | script, modelo/datos, SVG, PNG, README y validaciones |
| `diagram` | `diagram-generation` | formas, tablas o esquemas editables; SVG/PNG de respaldo |
| `equation_only` | `diagram-generation` | OMML/texto matemático y callouts editables |
| `mixed` | ambas skills según capas | gráfico y diagrama separados; nunca slide aplanada |
| `external_image` | `asset-curation` | original autorizado, recorte derivado, crédito y alt text |
| `video_or_gif` | `asset-curation` + producción propia | audio/MP4/GIF local y fallback estático |

## Decisión por modalidad

| modalidad solicitada | decisión para U10 |
|---|---|
| Fotografía real | Solo opcional para contextualizar el caso U10-002/077; se descarta en la ruta base porque el diagrama mantiene mejor las relaciones. |
| Ilustración técnica | Sí, reconstruida como diagrama editable para medición, filtros, masking, cabina y control. |
| Imagen anatómica | No: el alcance requiere función entre oídos, no anatomía; una imagen anatómica agregaría carga y repetiría U6. |
| Gráfico propio | Sí: U10-CH-001–016; CH-016 permanece bloqueado por fuente normativa. |
| Diagrama editable | Sí: U10-DG-001–060; DG-060 permanece bloqueado por protocolo clínico. |
| Tabla | Sí, siempre nativa: U10-025, 027, 042, 044, 068, 071, 081, 085, 090 y 093. |
| Animación | No como archivo independiente. Se admite revelado progresivo nativo en actividades y caso integrador. |
| GIF | No aporta frente al revelado editable o al gráfico estático. |
| Video | No se selecciona video externo. |
| Audio | Sí, propio y opcional: blanco, rosa, NBN y ruido conformado al habla condicionado. |
| Captura de instrumento | Una captura pública de la app NIOSH puede usarse en U10-074 para discutir condiciones y trazabilidad; no como publicidad ni prueba de certificación. |
| Ecuación anotada | Sí: media, RMS, varianza, PSD, NBN, `L_eq,T`, SNR y derivaciones de respaldo. |
| Ninguna imagen | U10-042, 068, 082, 084, 085, 090 y 093; divisores usan solo un motivo nativo mínimo. |

## Cobertura slide por slide

| slide_id | clasificación final | modalidad / recurso |
|---|---|---|
| U10-001 | `diagram` | Diagrama editable U10-DG-001. |
| U10-002 | `diagram` | U10-DG-002; foto U10-AS-006 descartada salvo disponibilidad institucional superior. |
| U10-003 | `diagram` | U10-DG-003. |
| U10-004 | `diagram` | U10-DG-004. |
| U10-005 | `diagram` | U10-DG-005. |
| U10-006 | `diagram` | Motivo nativo de divisor; no crear asset separado. |
| U10-007 | `diagram` | U10-DG-006. |
| U10-008 | `diagram` | U10-DG-007. |
| U10-009 | `diagram` | U10-DG-008. |
| U10-010 | `diagram` | U10-DG-009 con estado de solución. |
| U10-011 | `mixed` | U10-CH-015 + rótulos editables. |
| U10-012 | `chart` | U10-CH-001. |
| U10-013 | `diagram` | U10-DG-010. |
| U10-014 | `diagram` | Motivo nativo de divisor. |
| U10-015 | `chart` | U10-CH-002. |
| U10-016 | `chart` | U10-CH-003. |
| U10-017 | `chart` | U10-CH-004. |
| U10-018 | `diagram` | U10-DG-011. |
| U10-019 | `diagram` | U10-DG-012. |
| U10-020 | `equation_only` | U10-DG-013. |
| U10-021 | `equation_only` | U10-DG-014. |
| U10-022 | `equation_only` | U10-DG-015. |
| U10-023 | `mixed` | U10-DG-016: ecuación + proceso editable. |
| U10-024 | `chart` | U10-CH-005. |
| U10-025 | `diagram` | Matriz editable U10-DG-017. |
| U10-026 | `diagram` | Corrección propuesta respecto del storyboard: divisor con motivo espectral mínimo, no `chart`. |
| U10-027 | `mixed` | U10-CH-006 + flecha/etiqueta editable. |
| U10-028 | `diagram` | U10-DG-018. |
| U10-029 | `equation_only` | U10-DG-019. |
| U10-030 | `mixed` | U10-DG-020. |
| U10-031 | `chart` | U10-CH-007. |
| U10-032 | `chart` | U10-CH-008. |
| U10-033 | `chart` | U10-CH-009. |
| U10-034 | `chart` | U10-CH-010. |
| U10-035 | `video_or_gif` | Audio propio U10-AS-001/002 + fallback U10-CH-010. |
| U10-036 | `diagram` | U10-DG-021. |
| U10-037 | `diagram` | Motivo nativo de divisor. |
| U10-038 | `diagram` | U10-DG-022; U10-AS-004 condicionado. |
| U10-039 | `diagram` | U10-DG-023. |
| U10-040 | `diagram` | U10-DG-024; audio U10-AS-003 opcional. |
| U10-041 | `mixed` | U10-DG-025: eje conceptual + ecuación anotada. |
| U10-042 | `none` | Tabla nativa; no imagen. |
| U10-043 | `diagram` | U10-DG-026; audio opcional solo después de resolver la actividad. |
| U10-044 | `diagram` | Tabla visual editable U10-DG-027. |
| U10-045 | `diagram` | Corrección propuesta respecto del storyboard: divisor con motivo de cadena de medición, no `chart`. |
| U10-046 | `diagram` | U10-DG-028. |
| U10-047 | `chart` | U10-CH-011. |
| U10-048 | `diagram` | U10-DG-029 coordinado con CH-011. |
| U10-049 | `equation_only` | U10-DG-030. |
| U10-050 | `mixed` | U10-DG-031. |
| U10-051 | `chart` | U10-CH-012. |
| U10-052 | `diagram` | U10-DG-032. |
| U10-053 | `equation_only` | U10-DG-033. |
| U10-054 | `chart` | U10-CH-013. |
| U10-055 | `mixed` | U10-DG-034. |
| U10-056 | `diagram` | U10-DG-035. |
| U10-057 | `diagram` | Motivo nativo de divisor. |
| U10-058 | `diagram` | U10-DG-036. |
| U10-059 | `diagram` | U10-DG-037. |
| U10-060 | `diagram` | U10-DG-038; fotografía de transductor U10-AS-007 no necesaria. |
| U10-061 | `diagram` | Segundo estado de U10-DG-038. |
| U10-062 | `diagram` | U10-DG-039. |
| U10-063 | `diagram` | U10-DG-040, con revisión clínica. |
| U10-064 | `diagram` | U10-DG-041. |
| U10-065 | `diagram` | Motivo nativo de divisor. |
| U10-066 | `diagram` | U10-DG-042. |
| U10-067 | `diagram` | U10-DG-043. |
| U10-068 | `none` | Tabla nativa; documentos U10-AS-008 solo como referencia, no miniaturas por defecto. |
| U10-069 | `diagram` | U10-DG-044. |
| U10-070 | `diagram` | U10-DG-045. |
| U10-071 | `diagram` | Tabla comparativa U10-DG-046. |
| U10-072 | `diagram` | Actividad editable U10-DG-047. |
| U10-073 | `diagram` | U10-DG-048. |
| U10-074 | `external_image` | Captura pública U10-AS-005 + callouts; alternativa diagramática propia. |
| U10-075 | `diagram` | U10-DG-049. |
| U10-076 | `diagram` | Motivo nativo de divisor. |
| U10-077 | `diagram` | U10-DG-050. |
| U10-078 | `mixed` | U10-DG-051 + U10-CH-014. |
| U10-079 | `diagram` | U10-DG-052. |
| U10-080 | `diagram` | U10-DG-053. |
| U10-081 | `diagram` | Matriz editable U10-DG-054. |
| U10-082 | `none` | Tipografía y revelado de afirmaciones; no imagen. |
| U10-083 | `diagram` | U10-DG-055. |
| U10-084 | `none` | Cierre tipográfico. |
| U10-085 | `none` | Tabla/glosario nativo. |
| U10-086 | `equation_only` | U10-DG-056. |
| U10-087 | `equation_only` | U10-DG-057. |
| U10-088 | `equation_only` | U10-DG-058, condicionado a verificación. |
| U10-089 | `mixed` | Serie de soluciones U10-DG-059. |
| U10-090 | `none` | Tabla nativa de referencia. |
| U10-091 | `diagram` | U10-DG-060 bloqueado por protocolo. |
| U10-092 | `chart` | U10-CH-016 bloqueado; documentos U10-DOC-001–005 como fuentes, no collage. |
| U10-093 | `none` | Bibliografía nativa y enlaces; no miniaturas. |

## Curación de recursos externos

Fecha de acceso de todos los enlaces: **2026-08-12**.

| asset_id | slide | URL | autor / organización | título | licencia conocida | propósito | alternativa | decisión |
|---|---|---|---|---|---|---|---|---|
| U10-AS-005 | U10-074 | https://stacks.cdc.gov/view/cdc/181719 | Chucri A. Kardous / NIOSH–CDC | NIOSH sound level meter app | Public Domain | Mostrar una interfaz real y anotar micrófono, calibración, ponderación, detector, intervalo y trazabilidad. | Diagrama propio de teléfono + cadena de medición, sin marca. | `shortlisted`; no descargado. |
| U10-DOC-001 | U10-068/092/093 | https://www.who.int/publications/i/item/9789289053563 | World Health Organization | Environmental noise guidelines for the European Region | CC BY-NC-SA 3.0 IGO | Ejemplo de guía sanitaria; registrar alcance y población. | Citar metadatos en tabla nativa. | `shortlisted`; no usar valores hasta decisión docente. |
| U10-DOC-002 | U10-068/092/093 | https://www.iso.org/standard/81317.html | ISO/TC 43/SC 1 | ISO 9612:2025 — Determination of occupational noise exposure | © ISO; reproducción requiere permiso | Ejemplo de norma de metodología de exposición ocupacional. | Citar número, edición y alcance sin reproducir portada/tablas. | `proposed`; referencia, no asset reutilizable. |
| U10-DOC-003 | U10-068/092/093 | https://www.argentina.gob.ar/srt/prevencion/publicaciones/protocolos/medicion-del-nivel-de-ruido-en-el-ambiente-laboral | Superintendencia de Riesgos del Trabajo, Argentina | Protocolo para medición del nivel de ruido en el ambiente laboral | Reutilización gráfica no confirmada | Contextualizar jurisdicción argentina y distinguir protocolo de guía sanitaria. | Enlace y metadatos en tabla nativa. | `shortlisted`; validar vigencia/aplicabilidad antes de cifras. |
| U10-DOC-004 | U10-068/092/093 | https://www.cdc.gov/niosh/docs/98-126/ | NIOSH–CDC | Criteria for a Recommended Standard: Occupational Noise Exposure | Obra del gobierno federal de EE. UU.; verificar excepciones del documento | Ejemplo de criterio técnico/recomendación ocupacional. | Citar ficha bibliográfica, no reproducir tablas. | `proposed`; requiere comparación institucional. |
| U10-DOC-005 | U10-060/091/093 | https://www.iso.org/standard/74049.html | ISO/TC 43 | ISO 8253-3:2022 — Speech audiometry | © ISO; reproducción requiere permiso | Identificar una fuente relevante para habla, ruido competitivo y masking; no basta para completar el protocolo local. | Citar número/alcance y solicitar protocolo institucional. | `proposed`; U10-091 sigue bloqueada. |

## Evaluación del único asset visual externo preseleccionado

**U10-AS-005 — captura NIOSH SLM:** relevancia alta; exactitud y confiabilidad altas; resolución suficiente para media slide; idioma inglés aceptable si se usan callouts en español; licencia clara; recorte 40–50 % de la slide. La imagen no debe sostener la frase absoluta “una app no certifica”: la fuente oficial indica que las capacidades dependen del dispositivo, micrófono externo calibrado y condiciones de uso. Antes de `slide-writing`, conviene reformular U10-074 como **“La interfaz no reemplaza la configuración ni la trazabilidad”**.

## Recursos descartados o postergados

- U10-AS-006: no buscar foto genérica de clínica/avenida; DG-002 y DG-050 son superiores.
- U10-AS-007: no usar foto de transductores salvo que la cátedra quiera identificar un montaje real; el diagrama funcional evita asociar la técnica con un modelo comercial.
- U10-AS-008: reemplazado por registros U10-DOC-001–005; no hacer collage de portadas.
- No usar capturas de sonómetros comerciales, videos de fabricantes, imágenes anatómicas, stock de personas tapándose los oídos ni IA generativa.

## Descargas

No se descargó ningún archivo. U10-AS-005 es claramente reutilizable por su condición de dominio público, pero se conserva como `shortlisted` hasta aprobar la reformulación de U10-074 y el recorte exacto. Los documentos se enlazan como fuentes; los materiales ISO no deben descargarse ni reproducirse sin permiso.
