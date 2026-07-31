import fs from 'node:fs/promises';
import path from 'node:path';

const [slideTextPath, inspectPath, outDir] = process.argv.slice(2);
if (!slideTextPath || !inspectPath || !outDir) {
  throw new Error('Uso: node u04_generate_template_plan.mjs <slide_text.md> <template-inspect.ndjson> <outDir>');
}

const layoutToSource = {
  FA_00_PORTADA: 1,
  FA_02_OBJETIVOS: 2,
  FA_02B_CONOCIMIENTOS_PREVIOS: 3,
  FA_03_MAPA_CLASE: 4,
  FA_01_DIVISOR: 5,
  FA_04_TITULO_CONTENIDO: 6,
  FA_05_TEXTO_VISUAL_60_40: 7,
  FA_06_VISUAL_TEXTO_40_60: 8,
  FA_07_GRAFICO_EXPLICACION: 9,
  FA_06B_DOS_COLUMNAS: 10,
  FA_08_DEFINICION: 11,
  FA_09_ECUACION_INTERPRETACION: 12,
  FA_10_EJEMPLO_RESUELTO: 13,
  FA_11_COMPARACION: 14,
  FA_12_PROCESO: 15,
  FA_13_APLICACION_CLINICA: 16,
  FA_14_PREGUNTA_EJERCICIO: 17,
  FA_14B_MINI_EJERCICIO: 18,
  FA_15_ERROR_FRECUENTE: 19,
  FA_16_RECAP_PARCIAL: 20,
  FA_17_RECAP_FINAL: 21,
  FA_18_TABLA_DATOS: 22,
  FA_19_MEDIA_AUDIO_VIDEO: 23,
  FA_20_BIBLIO_RECURSOS: 24,
  FA_21_CIERRE_PUENTE: 25,
  FA_22_VISUAL_COMPLETO: 26,
  FA_23_APENDICE: 27,
};

const text = await fs.readFile(slideTextPath, 'utf8');
const slideSections = [...text.matchAll(/^## (U04-\d{3})[^\n]*\n([\s\S]*?)(?=^## U04-\d{3}|(?![\s\S]))/gm)];
if (slideSections.length !== 125) throw new Error(`Se esperaban 125 slides y se encontraron ${slideSections.length}.`);

const idsBySlide = new Map();
for (const line of (await fs.readFile(inspectPath, 'utf8')).split(/\r?\n/)) {
  if (!line.trim()) continue;
  const record = JSON.parse(line);
  if (!Number.isInteger(record.slide) || !record.id || record.kind === 'slide') continue;
  if (!idsBySlide.has(record.slide)) idsBySlide.set(record.slide, new Set());
  idsBySlide.get(record.slide).add(record.id);
}

const outputSlides = slideSections.map((match, index) => {
  const slideId = match[1];
  const body = match[2];
  const layoutMatch = body.match(/\*\*Layout:\*\*\s*`([^`]+)`/);
  if (!layoutMatch) throw new Error(`No se encontró layout para ${slideId}.`);
  const layout = layoutMatch[1];
  const sourceSlide = layoutToSource[layout];
  if (!sourceSlide) throw new Error(`Layout no mapeado: ${layout}`);
  const inheritedIds = [...(idsBySlide.get(sourceSlide) ?? [`source-slide-${sourceSlide}-local-content`])];
  return {
    outputSlide: index + 1,
    slideId,
    sourceSlide,
    sourceLayout: layout,
    reuseMode: 'duplicate-slide',
    narrativeRole: 'academic content slide',
    editTargets: [
      {
        action: 'delete',
        shapeIds: inheritedIds,
        reason: 'Retirar el contenido demostrativo local del template; se conserva el master y el layout aprobado.',
      },
      {
        action: 'add',
        newPrimitiveAllowed: true,
        mustNotOverlapInherited: true,
        zone: { left: 40, top: 24, width: 1200, height: 652 },
        reason: 'Agregar el contenido específico de Unidad 4 dentro de la zona segura del layout sin cubrir elementos del master.',
      },
    ],
  };
});

await fs.mkdir(outDir, { recursive: true });
await fs.writeFile(path.join(outDir, 'template-frame-map.json'), `${JSON.stringify({
  sourceTemplate: 'fisica_acustica_template_v01.pptx',
  slideSize: { width: 1280, height: 720 },
  outputSlides,
}, null, 2)}\n`, 'utf8');

const usedSources = [...new Set(outputSlides.map((x) => x.sourceSlide))].sort((a, b) => a - b);
const audit = [
  'TEMPLATE AUDIT — Unidad 04',
  '',
  'Template aprobado: fisica_acustica_template_v01.pptx',
  'Formato: 16:9, 1280 × 720 px equivalentes.',
  'Fuente tipográfica: Calibri / Calibri Light; ecuaciones en Cambria Math.',
  'Masters detectados: 2. Layouts inspeccionados: 27.',
  `Slides de salida planificadas: ${outputSlides.length}.`,
  `Layouts fuente utilizados: ${usedSources.join(', ')}.`,
  '',
  'Decisión de adaptación:',
  '- duplicar la slide demostrativa correspondiente a cada layout;',
  '- conservar master, fondo, reglas, pie, numeración y layout;',
  '- retirar únicamente objetos demostrativos locales;',
  '- componer el contenido de Unidad 4 con objetos editables y assets aprobados dentro de la zona segura.',
  '',
  'Riesgo conocido: los placeholders del template son demostrativos y algunos tienen geometría nula; por eso el contenido se agrega como objetos editables dentro de los límites del layout.',
  '',
].join('\n');
await fs.writeFile(path.join(outDir, 'template-audit.txt'), audit, 'utf8');

const deviation = [
  'DEVIATION LOG — preparación',
  '',
  'No se cambia el sistema visual global.',
  'Desviación técnica documentada: los placeholders vacíos del template no son utilizables por su geometría; se conservan master/layout y se reemplaza el contenido local demostrativo por objetos editables nuevos.',
  'U04-102: se excluye U04-CH-012 por estado pending_approval; se usa U04-DG-017 aprobado como alternativa estática.',
  'Recursos multimedia shortlisted/proposed: no se incrustan; la alternativa estática aprobada queda identificada.',
  '',
].join('\n');
await fs.writeFile(path.join(outDir, 'deviation-log.txt'), deviation, 'utf8');

console.log(JSON.stringify({ slides: outputSlides.length, usedSources, outDir }, null, 2));
