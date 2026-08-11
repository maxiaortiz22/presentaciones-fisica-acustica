# Necesidades iniciales de diagramas — Unidad 6

Todos los recursos listados son candidatos explícitos para `diagram-generation`. Deben producirse, por defecto, con formas, texto, ecuaciones y conectores editables de PowerPoint. Las variantes `B/C` reutilizan geometría maestra, pero cambian la tarea pedagógica; no son copias estáticas.

## Criterios de producción

- Diseñar en el tamaño real del layout de `storyboard.md`.
- Mantener texto principal ≥22 pt, etiquetas ≥20 pt y ecuaciones centrales ≥28 pt.
- Margen interior mínimo 0,18 in y 10–20 % de aire en cada caja.
- Anclar conectores a bordes y reservar corredores; ninguna línea debe tocar texto.
- Mostrar 4–5 nodos por estado. Si se necesitan más, revelar por capas o dividir.
- Renderizar, revisar clipping, colisiones y puntas de flecha, corregir y volver a renderizar.

## Inventario trazado al storyboard

| diagram_id | Slides | Propósito / contenido | Requisitos estructurales | Fuente base | Estado |
|---|---|---|---|---|---|
| U06-DG-001 | 002, 017, 027, 039, 071 | Cadena periférica acumulativa | Seis zonas; comienza incompleta y agrega capas/transformaciones en cada recap. | PO; TEX 6.2–6.10; PDF 151–165 | planificado |
| U06-DG-002 | 003 | Puente U2–U5 → U6 | Cuatro prerrequisitos alimentan preguntas de la unidad. | CM; CDM; BR | planificado |
| U06-DG-003 | 004, 023 | Magnitud–unidad y variante timpánica | Tarjetas revelables; no codificar solo por color. | GLO; NOT; TEX 6.4.5 | planificado |
| U06-DG-004 | 007 | Mapa de la unidad | Cuatro macroetapas, diez bloques y marcadores de recap. | BR; storyboard | planificado |
| U06-DG-005 | 009–010 | Pabellón, dirección y espectro | Pabellón + dos incidencias; variante ejercicio sin solución. | TEX 6.4.1; REF `carlini2024` | pendiente asset anatómico |
| U06-DG-006 | 011 | Presión según posición en CAE | Conducto curvo, onda incidente/reflejada y tres puntos; sin curva inventada. | TEX 6.4.2; REF `ugarteburu2022` | planificado |
| U06-DG-007 | 013 | Frente ideal frente a CAE real | Dos columnas y límites de idealización esférica/cilíndrica. | PO; TEX 6.4.2–6.4.3 | pendiente validación docente |
| U06-DG-008 | 014 | Resonador de cuarto de onda | Tubo abierto–cerrado aproximado, nodos cualitativos y supuestos. | TEX 6.4.3; PDF 154 | planificado |
| U06-DG-009, U06-DG-009B | 015–016, 109 | `f_res≈c/(4ℓ)` y ejemplo de 27 mm | Ecuación con callouts; variante resuelta con unidades y límites. | TEX 6.4.3–6.4.4 y ejercicio G1; NOT | planificado |
| U06-DG-010 | 020 | Dos presiones → fuerza | `p_CAE`, `p_OM`, `Δp` y fuerza distribuida en cuatro etapas. | TEX 6.4.5 | planificado |
| U06-DG-011, U06-DG-011B | 021–022, 110 | `F≈Δp·S` y ejemplo | Ecuación anotada, área efectiva, unidades; variante numérica/resuelta. | TEX 6.4.5 y ejercicio G2; NOT; OD-U06-07 | pendiente notación |
| U06-DG-012 | 024 | Fuerza → sistema mecánico → movimiento | Masa, rigidez, amortiguamiento y frecuencia como condicionantes. | TEX 6.4.5; CDM | planificado |
| U06-DG-013 | 025 | Presión acústica frente a estática | Dos escalas temporales; comparación, no igualdad ciclo a ciclo. | TEX 6.5.1 | planificado |
| U06-DG-014 | 026 | Trompa auditiva: conexión y funciones | Caja↔nasofaringe; equilibrado, ventilación y drenaje. | TEX 6.5.1; PO | pendiente asset anatómico |
| U06-DG-015 | 029 | Cadena osicular funcional | Martillo–yunque–estribo, ventanas y trompa; rótulos divididos. | TEX 6.5.1; PDF fig. 6.2 | planificado |
| U06-DG-016 | 030 | Desadaptación aire–fluido | Interfaz con reflexión/transferencia; sin coeficientes numéricos. | TEX 6.5.2; U4 | planificado |
| U06-DG-017 | 031 | Dos mecanismos del oído medio | Área, palanca y carga coclear en tres etapas. | TEX 6.5.2 | planificado |
| U06-DG-018 | 032 | Razón de áreas | Superficies efectivas y ecuación provisional `R_S`. | TEX ec. 6.3; NOT | pendiente notación |
| U06-DG-019 | 033 | Acción de palanca | Brazos, fuerzas y desplazamientos en sentidos de intercambio. | TEX 6.5.2; PDF fig. 6.3 | planificado |
| U06-DG-020, U06-DG-020B, U06-DG-020C | 034, 036, 108, 111 | Modelo combinado, ejemplo y cruce de símbolos | Maestro de áreas/palanca; ecuación provisional, tabla de notación y cálculo. | TEX 6.5; NOT; OD-U06-07/08 | pendiente notación |
| U06-DG-021 | 035 | Presión no equivale a energía | Balance cualitativo de magnitudes y pérdidas. | TEX 6.5.2; U2/U4 | planificado |
| U06-DG-022 | 037 | Razón en dB frente a dB SPL | Dos ecuaciones anotadas con referencia explícita. | TEX 6.5.3; NOT | planificado |
| U06-DG-023 | 038–039 | Reflejo acústico y límite temporal | Proceso funcional + línea temporal cualitativa; sin cifras universales. | TEX 6.5.4; PO | planificado sin cifras |
| U06-DG-024 | 041–042, 048 | Vía aérea frente a ósea y recap | Dos rutas convergentes; variante pregunta y cierre. | TEX 6.6; PDF 158–159 | planificado |
| U06-DG-025 | 043 | Cinco contribuciones de conducción ósea | Cinco nodos en dos filas; evitar mapa radial apretado. | TEX 6.6.1–6.6.5 | planificado |
| U06-DG-026, U06-DG-026B | 044, 113 | Radiación al CAE y ampliación de mecanismos | Maestro de pared del CAE; respaldo amplía familia completa y puede dividirse. | TEX 6.6; REF `Stenfelt2011` | planificado |
| U06-DG-027 | 045 | Inercia de huesecillos/fluidos | Dos minimecanismos con referencia al cráneo; flechas relativas. | TEX 6.6.2–6.6.3 | planificado |
| U06-DG-028 | 046 | Cápsula y tejidos | Dos mecanismos restantes; presión diferencial sin jerarquía universal. | TEX 6.6.4–6.6.5 | planificado |
| U06-DG-029 | 047 | Vibrador óseo activa varias rutas | Transductor → cráneo → mecanismos; qué no localiza. | TEX 6.6; CM U6→U8 | pendiente asset |
| U06-DG-030 | 050, 059 | Ventanas e hidromecánica | Movimiento complementario; variante de frontera móvil y límites. | TEX 6.7.1/6.10 | planificado |
| U06-DG-031 | 051, 058 | Vista longitudinal y actividad de vistas | Base–ápex–helicotrema; variante sin rótulos. | TEX 6.7.1 | planificado |
| U06-DG-032, U06-DG-032B | 052, 058, 107 | Corte de rampas y terminología | Tres compartimentos; variante de equivalencias anatómicas. | PO; TEX 6.7.1; GLO | pendiente terminología |
| U06-DG-033 | 053 | Fluidos por compartimento | Patrones además de color; leyenda verbal. | TEX 6.7.1/6.8.3 | planificado |
| U06-DG-034 | 054 | Reissner, basilar y rampa media | Capas anatómicas con órgano de Corti solo como relación. | TEX 6.7.1 | planificado |
| U06-DG-035, U06-DG-035B | 055–056 | Partición y órgano de Corti | Basilar, tectorial y haces; variante definición del órgano. | TEX 6.7.1/6.8.1 | pendiente validación anatómica |
| U06-DG-036, U06-DG-036B | 057, 116 | Túnel de Corti y rotulado | Solo desde fuente anatómica aprobada; líderes fuera de tipografía. | PO; EXT-PEND | bloqueado por fuente |
| U06-DG-037 | 060 | Recap longitudinal + transversal | Dos vistas enlazadas, máximo seis rótulos. | B05 | planificado |
| U06-DG-038 | 062 | Alternativa estática a la animación de onda | Cuatro estados: oscilación local y avance de envolvente. | TEX 6.7.2 | planificado como fallback |
| U06-DG-039 | 063 | Etapas de onda viajera | Base→crecimiento→máximo→decaimiento. | TEX 6.7.2 | planificado |
| U06-DG-040 | 065 | Lugar característico frente a tonotopía | Curva única frente a mapa ordenado. | TEX 6.7.2; GLO | planificado |
| U06-DG-041 | 073 | Órgano de Corti funcional | CCI/CCE, soporte, tectorial/basilar; túnel condicionado. | TEX 6.8.1 | pendiente asset/fuente |
| U06-DG-042 | 074 | Micromecánica estática | Dos estados de movimiento relativo; diferenciar CCI/CCE. | TEX 6.8.1; REF | planificado como fallback |
| U06-DG-043 | 075 | Polaridad del haz | Reposo, deflexión excitatoria y opuesta. | TEX 6.8.3; REF | planificado |
| U06-DG-044 | 076, 079, 081 | Tramo común y ramas CCI/CCE | Maestro acumulativo; comparación, actividad y recap. | TEX 6.8.2–6.8.3 | planificado |
| U06-DG-045 | 077 | Ruta aferente desde CCI | Cuatro etapas y frontera célula/fibra. | TEX 6.8.2 | planificado |
| U06-DG-046 | 078 | Bucle activo de CCE | Realimentación en corredor trasero; no cruzar nodos. | TEX 6.8.2 | planificado |
| U06-DG-047 | 080 | OEA: ida y vuelta | Dos corredores acústicos separados y límite inferencial. | TEX 6.10 | planificado |
| U06-DG-048 | 083 | Mapa de cuatro potenciales | Ubicación, causa y función; cuatro nodos jerárquicos. | PO; TEX 6.8.3; NOT | planificado |
| U06-DG-049 | 084 | Potencial endococlear | Corte, regiones, polaridad relativa y referencia declarada. | TEX 6.8.3; REF | planificado |
| U06-DG-050 | 085 | Potencial de reposo | Célula, interior/exterior y referencia de medida. | PO; EXT-PEND | bloqueado por fuente |
| U06-DG-051 | 086 | Receptor frente a acción | Dos ubicaciones y trazas esquemáticas sin amplitudes absolutas. | TEX 6.8.3; REF | planificado |
| U06-DG-052 | 087 | *Tip links* | Dos estereocilios, enlace y tensión; sin microdetalle molecular. | TEX 6.8.3; REF | planificado |
| U06-DG-053, U06-DG-053B | 088, 114 | Apertura de canales y detalle iónico | Dos estados; respaldo agrega gradientes solo si se validan. | TEX 6.8.3; REF | planificado / detalle por validar |
| U06-DG-054, U06-DG-054B | 089, 114 | Sinapsis de CCI | Ca²⁺, vesículas, glutamato y fibra; variante de respaldo agrega detalle electroquímico validado. | TEX 6.8.2–6.8.3; REF | planificado / detalle por validar |
| U06-DG-055 | 090, 092 | Movimiento → potencial receptor | Cinco nodos; variante de actividad sin flechas. | TEX 6.8.1–6.8.3 | planificado |
| U06-DG-056 | 091–092 | Receptor → señal neural | Cinco nodos con frontera célula/fibra. | TEX 6.8.2–6.8.3 | planificado |
| U06-DG-057 | 093 | Recap de potenciales/transducción | Mapa acumulativo por capas, no definiciones repetidas. | B08 | planificado |
| U06-DG-058, U06-DG-058B | 095, 097 | Firma espacial y frecuencia/*pitch* | Eje base–ápex + población; variante físico/perceptual. | TEX 6.9.1; CM | planificado |
| U06-DG-059, U06-DG-059B | 098–099 | Nivel, respuesta y sonoridad | Dos niveles y población; variante físico/perceptual. | TEX 6.9.2; CM | planificado |
| U06-DG-060 | 100 | Pruebas como ventanas sobre la cadena | Cadena común y tres observaciones, sin cruces. | TEX 6.10; CM U6→U8 | planificado |
| U06-DG-061 | 101 | Montaje eléctrico conceptual | Estímulo, electrodos, referencia, señal y límites. | PO; TEX 6.10; EXT-PEND | pendiente fuente/asset |
| U06-DG-062 | 102 | Caso 2 kHz a dos niveles | Dos entradas sobre una cadena y campos de selección. | TEX 6.7–6.9 | planificado |
| U06-DG-063 | 103 | Resolución acumulativa del caso | Capas 40/70 dB SPL, supuestos y límites visibles. | TEX 6.2–6.10 | planificado |
| U06-DG-064 | 104 | Mapa final de diez ideas | Cuatro zonas, aparición progresiva, máximo cuatro ideas por estado. | PO; BR; CM | planificado |

## Prioridad sugerida

1. Maestros de arquitectura: DG-001, 015, 031–035, 041 y 044.
2. Procesos causales centrales: DG-017, 020, 039, 046–047, 053 y 055–056.
3. Actividades y recapitulaciones: variantes después de aprobar el maestro.
4. Bloqueados: DG-036/036B y DG-050; DG-020* espera notación.
