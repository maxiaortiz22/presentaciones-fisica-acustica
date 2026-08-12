# Unidad 9 — Informe de validación de diagramas

Fecha de cierre: 2026-08-12

## Alcance y resultado

- **Generados y aprobados:** 67 diagramas.
- **No generados por dependencia abierta:** U09-DG-032, U09-DG-048 y U09-DG-067.
- **Clasificación de los aprobados:** 16 diagramas conceptuales, 12 diagramas de proceso, 16 ecuaciones anotadas y 23 esquemas mixtos.
- **Problemas críticos abiertos:** 0.
- **Problemas mayores abiertos:** 0.

IDs aprobados: U09-DG-001–031, U09-DG-033–047, U09-DG-049–066 y U09-DG-068–070.

## Contrato verificado

| gate | valor comprobado | resultado |
|---|---|---|
| canvas | 1280 × 720, relación 16:9 y render PNG 2560 × 1440 | aprobado |
| texto principal | 22,5 pt efectivos o más | aprobado |
| ecuación central | 30 pt o más | aprobado |
| padding interno | 0,25 in | aprobado |
| separación línea–texto no relacionado | 0,125 in | aprobado |
| overflow y clipping | 0 casos | aprobado |
| conectores sobre texto | 0 casos | aprobado |
| etiquetas apoyadas en conectores | 0 casos; la semántica se trasladó a nodos o cajas independientes | aprobado |
| puntas sobre caracteres | 0 casos; los conectores terminan en el borde de la forma | aprobado |
| objetos fuera del canvas | 0 casos | aprobado |
| editabilidad | formas, textos y conectores nativos en `editable.pptx`; geometría e IDs en `diagram_source.json` | aprobado |

## Iteraciones

1. **Preflight geométrico.** Se comprobaron bounding boxes, capacidad estimada de texto, separación entre nodos y trayectorias de conectores.
2. **Render individual en canvas real.** Se exportó cada recurso a 2560 × 1440 y se inspeccionó su estructura editable mediante el archivo `.inspect.ndjson` generado junto al PPTX.
3. **Inspección visual.** Se revisaron seis hojas de contacto de diagramas y recursos individuales de las familias modificadas; se regeneraron las familias afectadas y se repitió la validación.

## Hallazgos y correcciones

| problema | severidad | corrección | estado |
|---|---|---|---|
| Algunos prototipos mostraban rótulos genéricos como “Paso 4” o “Qué se mide”. | mayor | Se extrajo vocabulario del storyboard y se añadieron etiquetas específicas para mecanismos, rutas, cabinas y el caso integrador. | corregido |
| Las primeras ramas de balance, interfaz y cabina podían sugerir una causalidad falsa entre resultados paralelos. | mayor | Se reemplazaron por ramas independientes desde un nodo común. | corregido |
| Comparaciones como espuma/envolvente e igual absorción/distinta distribución usaban conectores innecesarios. | mayor | Se cambiaron a paneles conceptuales sin flechas causales. | corregido |
| Los decimales con coma se dividían durante el análisis de texto (`6,02`). | mayor | Se protegieron las comas decimales y se fijaron callouts numéricos explícitos. | corregido |
| Algunos rótulos largos excedían la capacidad estimada de una caja. | mayor | Se resumió el texto y se redistribuyó en dos líneas; no se redujo la fuente por debajo del mínimo. | corregido |

## Dependencias no resueltas

- **U09-DG-032:** relación de Snell acústica; requiere fuente académica completa y selección de alcance.
- **U09-DG-048:** ley de masas absoluta; requiere convención técnica y símbolo definitivo.
- **U09-DG-067:** conversión modal ampliada; requiere fuente académica primaria.

Estos tres recursos conservan estado bloqueado y no cuentan como aprobados.
