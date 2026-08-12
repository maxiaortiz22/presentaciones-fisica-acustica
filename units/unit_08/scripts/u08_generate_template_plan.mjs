import fs from 'node:fs/promises';
import path from 'node:path';

const [slideTextPath, inspectPath, outDir] = process.argv.slice(2);
if (!slideTextPath || !inspectPath || !outDir) {
  throw new Error('Uso: node u08_generate_template_plan.mjs <slide_text.md> <template-inspect.ndjson> <outDir>');
}

const layoutToSource = {
  FA_00_PORTADA: 1, FA_02_OBJETIVOS: 2, FA_02B_CONOCIMIENTOS_PREVIOS: 3,
  FA_03_MAPA_CLASE: 4, FA_01_DIVISOR: 5, FA_04_TITULO_CONTENIDO: 6,
  FA_05_TEXTO_VISUAL_60_40: 7, FA_06_VISUAL_TEXTO_40_60: 8,
  FA_07_GRAFICO_EXPLICACION: 9, FA_06B_DOS_COLUMNAS: 10, FA_08_DEFINICION: 11,
  FA_09_ECUACION_INTERPRETACION: 12, FA_10_EJEMPLO_RESUELTO: 13,
  FA_11_COMPARACION: 14, FA_12_PROCESO: 15, FA_13_APLICACION_CLINICA: 16,
  FA_14_PREGUNTA_EJERCICIO: 17, FA_14B_MINI_EJERCICIO: 18,
  FA_15_ERROR_FRECUENTE: 19, FA_16_RECAP_PARCIAL: 20, FA_17_RECAP_FINAL: 21,
  FA_18_TABLA_DATOS: 22, FA_19_MEDIA_AUDIO_VIDEO: 23, FA_20_BIBLIO_RECURSOS: 24,
  FA_21_CIERRE_PUENTE: 25, FA_22_VISUAL_COMPLETO: 26, FA_23_APENDICE: 27,
};

const text = await fs.readFile(slideTextPath, 'utf8');
const sections = [...text.matchAll(/^## (U08-\d{3})[^\n]*\n([\s\S]*?)(?=^## U08-\d{3}[^\n]*\n|(?![\s\S]))/gm)];
if (sections.length !== 114) throw new Error(`Se esperaban 114 slides y se encontraron ${sections.length}.`);

const idsBySlide = new Map();
for (const line of (await fs.readFile(inspectPath, 'utf8')).split(/\r?\n/)) {
  if (!line.trim()) continue;
  const record = JSON.parse(line);
  if (!Number.isInteger(record.slide) || !record.id || record.kind === 'slide') continue;
  if (!idsBySlide.has(record.slide)) idsBySlide.set(record.slide, new Set());
  idsBySlide.get(record.slide).add(record.id);
}

const outputSlides = sections.map((m, index) => {
  const id = m[1];
  const body = m[2];
  const layout = body.match(/- \*\*Layout:\*\* `([^`]+)`/)?.[1];
  const sourceSlide = layoutToSource[layout];
  if (!sourceSlide) throw new Error(`Layout no mapeado en ${id}: ${layout}`);
  const inherited = [...(idsBySlide.get(sourceSlide) ?? [])];
  return {
    outputSlide: index + 1,
    slideId: id,
    sourceSlide,
    sourceLayout: layout,
    reuseMode: 'duplicate-slide',
    narrativeRole: 'academic content slide',
    editTargets: [
      { action: 'delete', shapeIds: inherited, reason: 'Retirar contenido demostrativo local y conservar master/layout.' },
      { action: 'add', newPrimitiveAllowed: true, mustNotOverlapInherited: true,
        zone: { left: 40, top: 24, width: 1200, height: 652 },
        reason: 'Agregar contenido editable de Unidad 8 dentro de la zona segura del layout aprobado.' },
    ],
  };
});

await fs.mkdir(outDir, { recursive: true });
await fs.writeFile(path.join(outDir, 'template-frame-map.json'), `${JSON.stringify({
  sourceTemplate: 'fisica_acustica_template_v01.pptx',
  slideSize: { width: 1280, height: 720 },
  outputSlides,
}, null, 2)}\n`, 'utf8');
await fs.writeFile(path.join(outDir, 'template-audit.txt'), [
  'TEMPLATE AUDIT — Unidad 08',
  'Plantilla aprobada: fisica_acustica_template_v01.pptx.',
  'Formato: 16:9, 1280×720 px equivalentes.',
  'Estructura observada: 2 masters y 27 layouts; se inspeccionaron las 27 slides demostrativas.',
  `Slides planificadas: ${outputSlides.length}.`,
  'Estrategia: duplicar la slide demostrativa del layout, conservar master/layout y reemplazar solo contenido local.',
].join('\n'), 'utf8');
console.log(JSON.stringify({ slides: outputSlides.length, layouts: [...new Set(outputSlides.map((x) => x.sourceLayout))] }, null, 2));
