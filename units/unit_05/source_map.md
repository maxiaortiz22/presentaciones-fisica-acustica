# Unidad 5 — Mapa de fuentes de la redacción

Versión: v01 · 2026-08-03
Este mapa complementa el campo **Fuente** de cada entrada en `slide_text.md`. La redacción no incorpora temas fuera del storyboard aprobado.

## Claves

| Clave | Fuente |
|---|---|
| PO | Programa oficial 2025, Unidad 5, pp. 3–4 |
| TEX | `context/libro_latex/chapters/05-analisis-frecuencial.tex` |
| PDF | *Física Acústica para Fonoaudiología*, capítulo 5, pp. 119–149 |
| BR | `units/unit_05/brief.md` |
| INV | `units/unit_05/content_inventory.md` |
| OD | `units/unit_05/open_decisions.md` |
| NOT | `style/notation_guide.md` |
| GLO | `style/glossary.md` |
| CM/CDM | `course_map.md` y `course_dependency_map.md` |
| PREV | Unidad 4 y su cierre U04-109 |
| EP | Elaboración pedagógica propia apoyada en las fuentes anteriores |

## Correspondencia por secuencia

| Slides | Núcleo de contenido | Fuente primaria | Apoyo / observación |
|---|---|---|---|
| U05-001–007 | apertura, objetivos, diagnóstico y rutina | PO; BR; CM/CDM | PREV; NOT; GLO; EP |
| U05-008–017 | tiempo, frecuencia, fase y periodicidad | TEX 5.3–5.3.1; PDF 120–122 | NOT; GLO; U05-CH-001/002/003; U05-DG-002/003/014 |
| U05-018–025 | intuición y serie de Fourier | TEX 5.4–5.4.2; PDF 121–124 | figura 5.2; U05-CH-005; U05-DG-003 |
| U05-026–029 | transformada, magnitud y fase | TEX 5.4.3; PDF 123–125 | NOT; U05-DG-003/014 |
| U05-030–040 | muestreo, DFT, FFT, bins y resolución | TEX 5.4.4; PDF 125 | NOT; EP; U05-CH-006/007; U05-DG-004/014 |
| U05-041–051 | ventana, fuga, espectrograma y bin/banda | TEX 5.4.5–5.4.7; PDF 125–127 | PREV; U05-CH-008/015; U05-DG-005/014 |
| U05-052–062 | espectro frente a respuesta de sistema | PO; TEX 5.5–5.5.1; PDF 127–130 | CDM; NOT; GLO; U05-DG-006/014 |
| U05-063–073 | fundamental, componentes y voz | PO; TEX 5.6; PDF 129–131 | Brockmann-Bauser y Drinnan (2011); U05-CH-011; U05-DG-007/014 |
| U05-074–083 | infra/audible/ultra y rangos dinámicos | PO; TEX 5.7; PDF 131–132 | Oxenham (2018); ISO 226:2023; OD; U05-CH-013; U05-DG-008/014 |
| U05-084–094 | bandas, octavas, tercios, centro y ancho | PO; TEX 5.8; PDF 132–133 | IEC 61260-1:2014 pendiente para series nominales; U05-CH-015; U05-DG-009/014 |
| U05-095–105 | filtros y aplicaciones | PO; TEX 5.9–5.9.1; PDF 133–135 | GLO; U05-CH-016; U05-DG-010/014 |
| U05-106–116 | ponderaciones A/C/Z | PO; TEX 5.10; PDF 135–136 | NOT; GLO; IEC 61672-1 pendiente; DG-011/CH-017 bloqueados |
| U05-117–124 | sonómetro y descriptores | PO; TEX 5.11; PDF 136–138 | NOT; ISO 8253/ANSI como contexto; U05-CH-018/019; U05-DG-012/014 |
| U05-125–132 | integración, cierre y recursos | BR; TEX 5.12–5.14; PDF 138–147 | CM/CDM; `references.bib`; U05-DG-001/013 |
| U05-133–150 | formalismo, normas, soluciones y glosario | TEX 5.4–5.17; PDF 123–149 | NOT; GLO; normas citadas; U05-DG-015 |

## Trazabilidad de ejemplos y ecuaciones

| Slides | Relación o ejemplo | Fuente |
|---|---|---|
| U05-002 | igual RMS, distinta forma | PREV U04-109; BR; producción propia U05-CH-001 |
| U05-011–014 | tiempo, magnitud y fase | TEX fig. 5.1 y 5.4.3; U05-CH-002/003 |
| U05-015, 024, 064 | `f_0=1/T_0` | TEX ecs. 5.1–5.2 y ejemplo 5.4.2 |
| U05-021–023, 134 | serie y coeficientes | TEX ecs. 5.3–5.5; fig. 5.2 |
| U05-027–028, 133, 135 | transformada y forma polar | TEX ecs. 5.6–5.7; NOT |
| U05-033, 036–038 | `T_obs=N/f_s`, `Δf=f_s/N` | TEX ecs. 5.8–5.9 |
| U05-042–050, 139 | ventana y suma por banda | TEX 5.4.5–5.4.7, ecs. 5.10–5.11 |
| U05-056–059, 140 | `Y=HX`, `H=Y/X`, ganancia y fase | TEX ecs. 5.12–5.14 |
| U05-065–072 | armónicos, parciales y formantes | TEX 5.6 y fig. 5.5; Brockmann2011 para límites vocales |
| U05-079–080, 142 | `R_D=L_sup−L_inf` | TEX ec. 5.15; caso F5 |
| U05-086–093, 143 | bandas de octava/tercio | TEX ecs. 5.16–5.19; fig. 5.6 |
| U05-097–103, 144 | filtros básicos e ideal/real | TEX 5.9 y fig. 5.7; U05-CH-016 |
| U05-110–112 | corrección A tonal | TEX ec. 5.20 y ejemplo 5.10.1; IEC 61672-1 pendiente |
| U05-120–122, 146–147 | equivalente, máximo y pico | TEX 5.11.1–5.11.2, ec. 5.21 |
| U05-123 | caso audiométrico por bandas | TEX F2; datos hipotéticos U05-CH-019 |
| U05-126–127, 149 | caso integrador I1 | TEX pregunta y solución I1; PDF 142–147 |

## Recursos visuales aprobados y pendientes

### Aprobados

- Gráficos: CH-001, 002, 003, 005, 006, 007, 008, 011, 013, 015, 016, 018 y 019.
- Diagramas: DG-001–010 y DG-012–015.

### Pendientes o bloqueados

| Recurso | Slides afectadas | Tratamiento de redacción |
|---|---|---|
| CH-004, U05-MED-003 | U05-016 | alternativa conceptual de ataque–tramo estable–final |
| CH-009 | U05-045, 138 | comparación cualitativa, sin cifras de lóbulos |
| CH-010, U05-MED-003 | U05-046–048 | figura sintética del libro o esquema estático; sin voz fabricada |
| CH-012, U05-MED-003 | U05-071, 141 | caso sintético y límite no diagnóstico |
| CH-014 / IEC 61260-1 | U05-084, 091–093, 143 | relaciones exactas del libro; sin tabla nominal normativa |
| CH-017, DG-011 / IEC 61672-1 | U05-106–115, 145 | cadena conceptual; sin curva ni tolerancias; cifra tonal marcada provisional |
| Audio propio | U05-020, 102 | alternativa estática obligatoria |
| Imagen técnica | U05-078, 081, 118 | esquema propio hasta completar curaduría y licencia |

## Criterio de citación en las slides

- Las slides de concepto citan sección del libro o programa en el pie.
- Las figuras propias se acreditan como “Producción propia basada en…” y conservan el ID del manifiesto.
- Las normas se citan con número y edición; los contenidos pendientes no se presentan como definitivos.
- Los casos hipotéticos se rotulan como didácticos y no normativos.
- Las aplicaciones de voz declaran que el análisis aislado no establece diagnóstico.
