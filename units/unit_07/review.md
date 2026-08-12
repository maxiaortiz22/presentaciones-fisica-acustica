# Revisión integral de cierre — Unidad 7

**Deck revisado:** `output/unidad_07_psicoacustica_final.pptx`  
**Fecha:** 11 de agosto de 2026  
**Alcance:** 134/134 diapositivas, PowerPoint, notas, estructura, assets, PDF y render completo.  
**Resultado:** aprobado para cierre docente; **0 problemas críticos abiertos y 0 problemas mayores bloqueantes**.

## Fuentes contrastadas

1. Programa oficial: `context/programa/Programa de Física Acústica.pdf`.
2. Libro editable: `context/libro_latex/chapters/07-psicoacustica.tex`.
3. Libro en PDF: `context/libro_pdf/Física Acústica para Fonoaudiología.pdf`, capítulo 7, pp. 177–204.
4. ISO 226:2023, edición 3, para alcance y condiciones de las curvas normales de igual sonoridad: <https://www.iso.org/standard/83117.html>.
5. Brief, storyboard, redacción, notas, manifiesto, revisión pedagógica independiente e informe de consistencia de `units/unit_07/`.

No se reprodujeron tablas ni valores normativos de ISO 226. La cobertura se resuelve con definición, condiciones de aplicación y un trazado cualitativo rotulado como no normativo.

## Cobertura del programa

| Tema obligatorio | Slides principales | Estado final |
|---|---:|---|
| Umbral absoluto, criterio, audibilidad y sensibilidad | 8–19, 123 | Cubierto |
| Campo libre, CAE, tímpano y diferencia campo–tímpano | 20–26 | Cubierto |
| Curvas isofónicas y condiciones de lectura | 27–31, 123 | Cubierto conceptualmente; sin datos normativos reproducidos |
| Altura tonal, sonoridad, timbre y duración subjetiva | 32–53 | Cubierto |
| Nivel de sonoridad, fones y sones | 44–53 | Cubierto con modelo, ejemplo y límites |
| Enmascaramiento frecuencial, temporal, energético e informacional | 54–75 | Cubierto |
| Voz, ruido, reverberación, SNR, inteligibilidad y ALCons | 76–87, 117, 128–131 | Cubierto |
| Reflexiones, precedencia/Haas y retardo | 88–97, 132 | Cubierto |
| Localización, audición binaural, ITD, ILD y cono de confusión | 98–109, 133 | Cubierto |
| Fuentes concurrentes y efecto *cocktail party* | 110–120 | Cubierto |

## Problemas de cierre y estado

| ID | Slides | Severidad | Problema | Acción de cierre | Estado |
|---|---:|---|---|---|---|
| IP07-01 / CG07-01 | 27–30 | major | La actividad pedía leer una curva ausente. | La slide 30 muestra un trazado cualitativo con ejes, unidades, dos puntos y guía de lectura; el carácter no normativo es visible. | closed |
| IP07-02 / CG07-29 | 15–17, 26, 36, 40, 42, 61–64, 71, 74, 92, 105, 108, 115–116 | major | Las complementarias aparecían como ruta central. | Las 18 slides muestran `AMPLIACIÓN`; las 13 de respaldo muestran `A DEMANDA`. | closed |
| IP07-03 / CG07-36 | 2, 92; notas | major | No existían las demostraciones esenciales y algunas notas remitían a archivos inexistentes. | Se produjeron y probaron `U07-MEDIA-001` y `U07-MEDIA-006`; las demás notas declaran la alternativa visual y no ordenan reproducir archivos ausentes. | closed |
| IP07-04 / CG07-17 | 24, 51, 58, 81, 91, 105 | major | Los ejemplos ocultaban sustitución y razonamiento en las notas. | Cada ejemplo muestra datos comparables → sustitución → resultado → interpretación y límite. | closed |
| IP07-05 / CG07-22 | 74, 85, 103, 107, 117 | major | Diagramas con causalidad o geometría ambiguas. | Se redibujaron con formas y conectores nativos: causas antes que respuesta, dos recorridos para ITD, ambigüedad espacial y mezcla en los oídos como nodo integrador. | closed |
| CG07-07/08 | 54–75, 44–53 | major | Terminología alternante `máscara`/enmascarador y *phon/sone*. | Texto visible y fuentes de redacción usan señal enmascarante/enmascarador, fon y son. | closed |
| CG07-11/12/13 | fórmulas | major | Subíndices convertidos en paréntesis y `abs(...)` visible. | El parser ya no genera esas formas; se usan subíndices Unicode, nombres desarrollados y valor absoluto matemático. | closed |
| CG07-26 | notas | major | Dos bloques de fuentes por slide. | El empaquetado deja un único `[Sources]` por cada una de las 134 notas. | closed |
| CG07-30/31 | diagramas | major | Pies y créditos internos repetidos en pantalla. | Se retiraron del área proyectada; trazabilidad y autoría permanecen en notas/manifiesto. | closed |

## Problemas abiertos aceptados

| ID | Severidad | Estado | Justificación |
|---|---|---|---|
| R07-F01 | major | open — accepted | No se reproducen datos numéricos de ISO 226 por tratarse de una norma comercial. La actividad final es cualitativa, está rotulada y no simula una lectura normativa. Para una edición cuantitativa futura se requiere una fuente/licencia autorizada. |
| R07-F02 | minor | open — accepted | Parte de los diagramas heredados se inserta como PNG validado; sus maestros `.pptx`, SVG, scripts y descripciones siguen organizados. Los cinco diagramas corregidos en esta fase sí son nativos y editables. |
| R07-F03 | minor | open — accepted | Seis medios opcionales siguen en estado `proposed`. Ninguna nota exige su reproducción y todas las slides conservan una alternativa estática completa. |
| R07-F04 | minor | open — accepted | Algunas notas mantienen una cadencia formularia repetida. No afecta exactitud, navegación ni legibilidad; se recomienda una edición oral posterior con el docente. |
| R07-F05 | suggestion | open — accepted | No hay hipervínculos ni audio incrustado en el PPTX. Los dos WAV aprobados se entregan como archivos locales y las notas registran sus rutas. |

## Revisión específica de diagramas

- Se revisó el render completo y, a tamaño ampliado, 24, 30, 51, 58, 74, 81, 85, 91, 103, 105, 107 y 117.
- El primer render final detectó solapamientos internos en 85, 103 y 117; se corrigieron y se repitió el ciclo completo.
- No quedan flechas sobre texto o fórmulas, etiquetas apoyadas en conectores, líneas atravesando cajas, texto fuera de caja ni auto-shrink.
- Los conectores de los diagramas nuevos se crean detrás de los nodos y terminan en bordes o blancos gráficos.
- Las ecuaciones centrales y etiquetas de conectores conservan tamaños de aula.

## Revisión de producción

- Formato: 16:9.
- Slides: 134.
- Notas: 134/134; un bloque `[Sources]` por slide.
- Slide masters: 2; layouts: 27.
- Imágenes: 44; texto alternativo: 44/44.
- Rótulos: 18 `AMPLIACIÓN`; 13 `A DEMANDA`.
- Relaciones externas: 0; no hay enlaces rotos.
- Multimedia incrustada: 0; dos WAV locales aprobados y registrados.
- Render: 134/134 PNG en `output/rendered_final/`.
- PDF de revisión: 134 páginas.
- `slides_test.py`: aprobado; sin contenido fuera del canvas.
- Búsqueda XML visible: 0 apariciones de `L(N)`, `N(son)`, `T(60)`, `G(CT)`, `abs(`, *phon*, *sone*, `máscara`, `Figura conceptual` o créditos internos `TEX/PDF`.
- Archivo final: 4.271.742 bytes.
- SHA-256: `7EA7F9B51B474328AE79041593C895776738A006CAED4106FDA3E16DC97CA1D2`.

## Dictamen

La Unidad 7 cumple la definición de terminado. La cobertura es completa dentro del alcance autorizado; no existen problemas críticos ni mayores bloqueantes; las limitaciones aceptadas están registradas y no impiden dictar la clase. La extensión se mantiene porque responde a cuatro encuentros y a una ruta explícita de ampliaciones y respaldo.
