# Unidad 5 — Registro de cambios

## v01

- Primera producción completa de 150 slides en 16:9.
- Inclusión de gráficos, diagramas, notas, fuentes y enlaces.
- Render completo y revisión integral inicial.

## v02

- Corrección de todos los problemas críticos y mayores detectados en v01.
- Preservación de 2 masters, 27 layouts, notas y enlaces.
- Segundo render completo y cierre visual preliminar.

## Versión final — 2026-08-03

Archivo de entrega: `output/unidad_05_analisis_frecuencial_final.pptx`
SHA-256: `2D00BF0391C3B7F133BE28F965AE69F9FDFC76B6492905FE65A27962F4AF3AF7`.

### Cambios pedagógicos

- Ruta central reducida de 104 a 77 slides, distribuida en seis encuentros.
- Etiquetas visibles `CENTRAL`, `AMPLIACIÓN` y `RESPALDO` en las 150 slides.
- U05-032 y U05-048 incorporadas a la ruta central.
- U05-101 movida a ampliación y U05-120 incorporada a la ruta central.
- Formalismo integral y computacional secundario relegado a ampliación o respaldo.
- Caso integrador U05-126/127/149 completado con datos y resultados verificables.

### Cambios de contenido y notación

- U05-023: intervalo de integración y definiciones de `t₀` y `T₀` corregidos.
- U05-042: se eliminó la ambigüedad de `xw(t)` y se nombró “señal ventaneada”.
- U05-048: se sustituyó el placeholder por el espectrograma sintético del libro, con guía de lectura y límite clínico.
- U05-092: se incorporó el cálculo completo de límites y ancho de tercio de octava.
- U05-110/111: relación de corrección expresada en lenguaje inequívoco y ejemplo de 63 Hz verificado.
- U05-120/121: intuición energética antes de la formalización integral y cálculo legible de 77,4 dB.
- U05-126/127/149: datos, unidades, ganancia, fase y separación entre fundamental y envolvente.

### Cambios visuales y de consistencia

- Paleta mapeada al sistema del curso: carbón, bordó, teal y ocre.
- Portada corregida para eliminar solapamiento entre título y subtítulo.
- Etiquetas de ruta con contraste específico en divisores oscuros.
- Cuerpo mínimo de 20 pt en la ruta central para formas heredadas a 18,75 pt.
- Masters, layouts, geometría y editabilidad preservados.

### Cambios de producción

- `speaker_notes.md` y `slide_text.md` actualizados a versión final.
- 150/150 notas del PPTX con bloque de fuentes cerrado.
- `asset_manifest.csv` ampliado con `U05-BOOK-001`.
- `storyboard.md` alineado slide por slide con la versión final.
- PDF de revisión final de 150 páginas.
- Render final de 150 PNG y contacto visual completo.
- Tres enlaces externos verificados con respuesta HTTP 200.
- Auditoría estructural: 150 slides, 150 notas, 2 masters, 27 layouts, 1658 formas editables y 27 imágenes.
- `slides_test.py`: sin desbordes.

### Archivos creados

- `output/unidad_05_analisis_frecuencial_final.pptx`
- `units/unit_05/output/unidad_05_analisis_frecuencial_final.pptx`
- `units/unit_05/output/unidad_05_analisis_frecuencial_final_review.pdf`
- `units/unit_05/output/unidad_05_analisis_frecuencial_final/`
- `units/unit_05/final_report.md`
- `units/unit_05/change_log.md`

### Archivos actualizados

- `units/unit_05/brief.md`
- `units/unit_05/storyboard.md`
- `units/unit_05/slide_text.md`
- `units/unit_05/speaker_notes.md`
- `units/unit_05/asset_manifest.csv`
- `units/unit_05/review.md`
- `units/unit_05/independent_pedagogical_review.md`
- `units/unit_05/consistency_report.md`

### Problemas abiertos

- **Minor:** el exportador no persiste alt text en el atributo OOXML `descr` de las 27 imágenes.
- **Minor:** algunas slides no centrales conservan 18,75 pt por ajuste; no deben proyectarse por defecto.
- **Suggestion:** convertir ecuaciones seleccionadas a OMML nativo y preparar demostraciones de audio si el entorno docente lo permite.

No se sobrescribieron `v01` ni `v02`.
