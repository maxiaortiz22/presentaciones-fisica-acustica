# Unidad 6 — Revisión de assets de diagramas

Fecha de revisión: 2026-08-10  
Estado: **aprobado para integración futura**

## Alcance producido

Se implementaron 53 recursos editables a partir de las filas aprobadas de `diagram_plan.md`. El conjunto cubre:

- orientación de la cadena auditiva periférica y recuperación de prerrequisitos;
- oído externo y modelos ondulatorios;
- oído medio, transferencia mecánica, conducción aérea y ósea;
- cóclea, compartimentos, ondas y organización tonotópica;
- células ciliadas, transducción, potenciales y sinapsis;
- códigos periféricos, ventanas de observación y actividades integradoras.

## Entregables por recurso

Cada carpeta `assets/generated/diagrams/U06-DG-*` contiene:

- fuente editable `.pptx` de una diapositiva, con textos, cajas y conectores editables;
- `diagram_source.json` como fuente estructurada; el script generador reproducible se conserva en `scripts/u06_generate_diagrams.mjs`;
- SVG y PNG estático de alta resolución;
- `README.md` con caption sugerido, texto alternativo, fuente y uso previsto;
- `validation.json` con clasificación, tamaños, padding, iteraciones y controles geométricos;
- inspección estructural `.pptx.inspect.ndjson` y descripción de layout.

## Revisión visual y pedagógica

- Se aplicó el sistema visual académico de la unidad: fondo claro, azul oscuro estructural, celeste y amarillo como acentos controlados, sin degradados ni decoración 3D.
- La jerarquía distingue título del recurso, nodos, cuerpo, ecuaciones y etiquetas de conectores.
- Las rutas causales, comparaciones y bucles usan corredores libres; la dirección no depende solo del color.
- Las ecuaciones anotadas conservan símbolos, relaciones y unidades visibles, sin simular precisión ausente.
- Los esquemas anatómicos o fisiológicos se presentan como conceptuales y no a escala.
- Los estados estáticos de U06-DG-038 y U06-DG-042 funcionan como alternativa a animaciones.
- Los SVG y PNG permiten integración visual; los PPTX individuales preservan la editabilidad para la futura construcción del deck.
- Los textos alternativos describen la relación pedagógica, no solo la apariencia.

## Trazabilidad

- Los 53 IDs fueron incorporados a `asset_manifest.csv` con ruta local, estado y fuente.
- `diagram_plan.md` registra los maestros y variantes efectivamente aprobados.
- Las fuentes son el programa y el capítulo del curso indicados en cada README; no se agregaron cifras clínicas ni datasets externos sin respaldo.
- El generador maestro es `scripts/u06_generate_diagrams.mjs` y el control consolidado es `scripts/u06_validate_generated_assets.py`.

## Problemas abiertos

No quedan problemas críticos ni mayores en los 53 recursos producidos. Permanecen fuera de alcance las filas que el plan marca como `pending_*`, `blocked_*` o `detail_pending`; requieren las decisiones o fuentes allí registradas.

La presentación de la Unidad 6 no fue creada ni modificada en esta tarea.
