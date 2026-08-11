import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [rootArg, starterArg, outArg, qaDirArg] = process.argv.slice(2);
const workspace = process.env.U06_ARTIFACT_WORKSPACE;
if (!rootArg || !starterArg || !outArg || !workspace) {
  throw new Error('Uso: U06_ARTIFACT_WORKSPACE=<workspace> node u06_build_presentation.mjs <repoRoot> <starter.pptx> <out.pptx> [qaDir]');
}
const req = createRequire(path.join(workspace, 'package.json'));
const entry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(entry).href);

const ROOT = path.resolve(rootArg);
const UNIT = path.join(ROOT, 'units/unit_06');
const OUT = path.resolve(outArg);
const QA = path.resolve(qaDirArg || path.join(workspace, 'qa-build'));
const STARTER = path.resolve(starterArg);

const C = {
  berry: '#4D1434', berry2: '#903163', carbon: '#3D3D3D', gray: '#969FA7',
  lightGray: '#D9DCE0', ivory: '#F7F6F2', white: '#FFFFFF',
  teal: '#2F7E83', tealLight: '#E7F1F1', ochre: '#9F541A', ochreLight: '#F8EDE2',
  green: '#2F6F55', greenLight: '#E6F0EB', red: '#A33A3A', redLight: '#F7E8E6',
};
const STYLE = {
  physical: { fill: C.tealLight, line: C.teal, title: C.teal, body: C.carbon },
  accent: { fill: '#F4E9EF', line: C.berry, title: C.berry, body: C.carbon },
  clinical: { fill: C.ochreLight, line: C.ochre, title: C.ochre, body: C.carbon },
  neutral: { fill: C.ivory, line: C.gray, title: C.carbon, body: C.carbon },
  equation: { fill: C.ivory, line: C.berry2, title: C.berry, body: C.carbon },
};
const BLOCKED = new Set();
const REVERSE_BRANCHES = new Set(['U06-DG-002', 'U06-DG-012', 'U06-DG-025']);
const REMOVE_EDGES = new Set(['U06-DG-043']);

const subscript = (token) => ({
  S: 'ₛ', TM: 'ₜₘ', E: 'ₑ', L: 'ₗ', p: 'ₚ', res: 'ᵣₑₛ', rms: 'ᵣₘₛ',
  ref: 'ᵣₑ𝒻',
  0: '₀', 1: '₁', 2: '₂', 3: '₃',
}[token] || `(${token})`);

await fs.mkdir(path.dirname(OUT), { recursive: true });
await fs.mkdir(QA, { recursive: true });

const clean = (s = '') => String(s)
  .replace(/`/g, '').replace(/\*+/g, '').replace(/\$/g, '')
  .replace(/\[(?:BLOQUEADA|PROVISIONAL)\]\s*/gi, '')
  .replace(/\b(?:Provisional|Bloqueada):\s*/gi, '')
  .replace(/\bIdea central:\s*/gi, '')
  .replace(/\bClave de lectura:\s*/gi, 'Observá: ')
  .replace(/\\(?:mathrm|text|operatorname)\{([^{}]+)\}/g, '$1')
  .replace(/\\(?:mathrm|text|operatorname)\s+/g, '')
  .replace(/\\left|\\right|\\bigl|\\bigr|\\displaystyle/g, '')
  .replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1)/($2)')
  .replace(/\\sqrt\{([^{}]+)\}/g, '√($1)')
  .replace(/\\rho/g, 'ρ').replace(/\\lambda/g, 'λ').replace(/\\pi/g, 'π')
  .replace(/\\theta/g, 'θ').replace(/\\phi/g, 'φ').replace(/\\Delta/g, 'Δ')
  .replace(/\\mu/g, 'µ').replace(/\\omega/g, 'ω').replace(/\\alpha/g, 'α')
  .replace(/\\beta/g, 'β').replace(/\\tau/g, 'τ').replace(/\\times/g, '×')
  .replace(/\\cdot/g, '·').replace(/\\approx/g, '≈').replace(/\\propto/g, '∝')
  .replace(/\\neq/g, '≠').replace(/\\leq?/g, '≤').replace(/\\geq?/g, '≥')
  .replace(/\\Rightarrow/g, '⇒').replace(/\\rightarrow|\\to/g, '→')
  .replace(/\\infty/g, '∞').replace(/\\sum/g, 'Σ').replace(/\\int/g, '∫')
  .replace(/_\{([^{}]+)\}/g, '_$1').replace(/\^\{([^{}]+)\}/g, '^($1)')
  .replace(/_(CAE|OM)/g, '($1)')
  .replace(/_([A-Za-z0-9]+)/g, (_, token) => subscript(token))
  .replace(/\\[,;!]|\\quad|\\qquad/g, ' ').replace(/\\([{}])/g, '$1')
  .replace(/\\([A-Za-z]+)/g, '$1').replace(/[{}]/g, '').replace(/\s+/g, ' ').trim();

function parseSlideText(md) {
  const re = /^### (U06-\d{3}) — (.+)$/gm;
  const matches = [...md.matchAll(re)];
  return matches.map((m, i) => {
    const block = md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length);
    const fields = {}; const rawFields = {};
    for (const fm of block.matchAll(/^- \*\*([^*]+):\*\*\s*(.*)$/gm)) {
      const key = fm[1].trim().toLowerCase(); rawFields[key] = fm[2].trim(); fields[key] = clean(fm[2]);
    }
    const pick = (...keys) => {
      for (const key of keys) {
        if (fields[key] !== undefined) return fields[key];
        const fuzzy = Object.entries(fields).find(([k]) => k.startsWith(key));
        if (fuzzy) return fuzzy[1];
      }
      return '';
    };
    return {
      id: m[1], title: clean(m[2]).replace(/^—\s*/, ''), state: pick('estado de escritura'),
      subtitle: pick('subtítulo'), content: pick('contenido visible'), equations: pick('ecuaciones', 'ecuación'),
      definitions: pick('definiciones', 'definición'), example: pick('ejemplo'), caption: pick('caption'),
      visual: pick('visual'), layout: String(rawFields.layout || '').replace(/[`\.\s]/g, ''), source: pick('fuente'),
      alt: pick('texto alternativo'), raw: block,
    };
  });
}

function parseNotes(md) {
  const re = /^### (U06-\d{3})[^\n]*$/gm;
  const matches = [...md.matchAll(re)];
  const map = new Map();
  matches.forEach((m, i) => map.set(m[1], md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length).replace(/^## .*$/gm, '').trim()));
  return map;
}

function parseCsv(csv) {
  const rows = []; let row = []; let cell = ''; let quoted = false;
  for (let i = 0; i < csv.length; i += 1) {
    const ch = csv[i];
    if (quoted) {
      if (ch === '"' && csv[i + 1] === '"') { cell += '"'; i += 1; }
      else if (ch === '"') quoted = false; else cell += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(cell); cell = ''; }
    else if (ch === '\n') { row.push(cell.replace(/\r$/, '')); rows.push(row); row = []; cell = ''; }
    else cell += ch;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const headers = rows.shift();
  return rows.filter((r) => r.some(Boolean)).map((r) => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ''])));
}

function splitIdeas(text, max = 5) {
  const src = clean(text);
  if (!src || src === '—') return [];
  let parts = src.split(/(?<=[.!?])\s+|\s*;\s*/).map((x) => x.trim()).filter(Boolean);
  if (parts.length === 1 && src.includes(' · ')) parts = src.split(' · ').map((x) => x.trim()).filter(Boolean);
  if (parts.length > max) parts = [...parts.slice(0, max - 1), parts.slice(max - 1).join(' ')];
  return parts;
}

function slideRefMatches(ref, id) {
  const target = Number(id.slice(-3));
  for (const token of String(ref || '').split(/[;,]/).map((x) => x.trim())) {
    const exact = token.match(/^U06-(\d{3})$/); if (exact && Number(exact[1]) === target) return true;
    const range = token.match(/^U06-(\d{3})[–-](?:U06-)?(\d{3})$/);
    if (range && target >= Number(range[1]) && target <= Number(range[2])) return true;
  }
  return false;
}

function addShape(slide, { geometry = 'rect', name, x, y, w, h, fill = 'none', lineFill = 'none', lineWidth = 0, radius = 0 }) {
  return slide.shapes.add({ geometry, name, position: { left: x, top: y, width: w, height: h }, fill,
    line: { style: 'solid', fill: lineFill, width: lineWidth }, ...(radius ? { borderRadius: radius } : {}) });
}

function addText(slide, text, { x, y, w, h, size = 28, color = C.carbon, bold = false, align = 'left', valign = 'top', font = 'Calibri', name = 'text', fill = 'none', lineFill = 'none', lineWidth = 0, radius = 0, insets = { top: 4, right: 6, bottom: 4, left: 6 }, italic = false } = {}) {
  const shape = addShape(slide, { geometry: 'textbox', name, x, y, w, h, fill, lineFill, lineWidth, radius });
  shape.text = clean(text);
  shape.text.style = { fontSize: size, color, bold, italic, alignment: align, verticalAlignment: valign,
    typeface: font, autoFit: 'none', wrap: 'square', insets, lineSpacing: 1.02 };
  return shape;
}

function teachingRoute(d) {
  if (/respaldo/i.test(d.state)) return { session: 'RESPALDO', route: 'A DEMANDA' };
  const n = Number(d.id.slice(-3));
  const session = n <= 39 ? 'ENCUENTRO 1' : n <= 71 ? 'ENCUENTRO 2' : n <= 93 ? 'ENCUENTRO 3' : 'ENCUENTRO 4';
  return { session, route: /complementaria|ampliación/i.test(d.state) ? 'AMPLIACIÓN' : 'RUTA CENTRAL' };
}

function addTitle(slide, d, dark = false) {
  const color = dark ? C.white : C.berry;
  const long = d.title.length > 55; const veryLong = d.title.length > 82;
  const forceCompact = ['U06-075', 'U06-111'].includes(d.id);
  const titleY = d.id === 'U06-111' ? 63 : 43;
  addText(slide, d.title, { x: 52, y: titleY, w: 1172, h: long ? 88 : 72, size: d.id === 'U06-111' ? 32 : forceCompact ? 34 : veryLong ? 31 : long ? 34 : 40,
    color, bold: false, font: 'Calibri Light', name: 'slide-title', insets: { top: 0, right: 3, bottom: 0, left: 3 } });
  // Un título de dos líneas ya cumple la función orientadora; no se agrega un
  // subtítulo redundante en el mismo corredor vertical.
  if (!long && d.subtitle && d.subtitle !== '—') addText(slide, d.subtitle, { x: 55, y: 108, w: 1150, h: 31,
    size: 23, color: dark ? '#E4D8DF' : '#5E6267', name: 'slide-subtitle', insets: { top: 0, right: 3, bottom: 0, left: 3 } });
}

function addTopRail(slide, d) {
  const route = teachingRoute(d);
  addShape(slide, { geometry: 'rect', name: 'top-rail-1', x: 65, y: 27, w: 384, h: 5, fill: C.berry, lineFill: C.berry, lineWidth: 0 });
  addShape(slide, { geometry: 'rect', name: 'top-rail-2', x: 459, y: 27, w: 384, h: 5, fill: C.berry2, lineFill: C.berry2, lineWidth: 0 });
  addShape(slide, { geometry: 'rect', name: 'top-rail-3', x: 853, y: 27, w: 363, h: 5, fill: C.gray, lineFill: C.gray, lineWidth: 0 });
  addText(slide, `UNIDAD 6 · ${route.session} · ${route.route}`, { x: 50, y: 2, w: 520, h: 24, size: 14,
    color: C.berry2, bold: true, name: 'eyebrow', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
}

function addCaption(slide, d, asset) {
  // Los recursos propios se documentan en notas/manifiesto. En pantalla queda
  // únicamente un caption funcional cuando el gráfico exige una clave de lectura.
  if (asset?.type !== 'generated_chart') return;
  let caption = d.caption && d.caption !== '—' ? d.caption : '';
  caption = caption.replace(/^(?:Esquema|Figura|Lectura) conceptual,?\s*(?:no a escala\.)?\s*/i, '');
  if (caption.length > 145) caption = `${caption.slice(0, 142).replace(/[\s,;:.]+$/, '')}…`;
  if (caption) addText(slide, caption, { x: 70, y: 630, w: 1140, h: 26, size: 16,
    color: '#5E6267', italic: true, align: 'center', name: 'caption', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
}

let helperSeq = 0;
function addLine(slide, x1, y1, x2, y2, { color = C.carbon, width = 3, arrow = false, name = 'line' } = {}) {
  const a = addShape(slide, { geometry: 'rect', name: `${name}-a-${helperSeq}`, x: x1, y: y1, w: 1, h: 1, fill: 'none', lineFill: 'none' });
  const b = addShape(slide, { geometry: 'rect', name: `${name}-b-${helperSeq}`, x: x2, y: y2, w: 1, h: 1, fill: 'none', lineFill: 'none' });
  helperSeq += 1;
  return slide.shapes.connect(a, b, { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: color, width }, ...(arrow ? { tail: { type: 'arrow', width: 'med', length: 'med' } } : {}) });
}

function addCaeComparison(slide) {
  addText(slide, 'Modelo ideal', { x: 95, y: 165, w: 470, h: 40, size: 30, color: C.teal, bold: true, align: 'center', name: 'cae-ideal-title' });
  addText(slide, 'Conducto auditivo real', { x: 715, y: 165, w: 470, h: 40, size: 30, color: C.ochre, bold: true, align: 'center', name: 'cae-real-title' });
  [0, 1, 2].forEach((i) => addShape(slide, { geometry: 'ellipse', name: `wavefront-${i}`, x: 135 + i * 92, y: 245 - i * 18, w: 160 + i * 36, h: 160 + i * 36, fill: 'none', lineFill: C.teal, lineWidth: 3 }));
  addShape(slide, { geometry: 'rect', name: 'ideal-tube', x: 170, y: 315, w: 350, h: 86, fill: C.tealLight, lineFill: C.teal, lineWidth: 2 });
  addText(slide, 'Geometría regular\ncondiciones de contorno declaradas', { x: 155, y: 440, w: 380, h: 90, size: 25, color: C.carbon, align: 'center', name: 'ideal-caption' });
  const realSegments = [[745,300,150,92],[880,270,155,105],[1015,318,135,80]];
  realSegments.forEach(([x,y,w,h],i) => addShape(slide, { geometry: 'roundRect', name: `real-cae-${i}`, x, y, w, h, fill: i === 1 ? C.ochreLight : C.ivory, lineFill: C.ochre, lineWidth: 2, radius: 20 }));
  addLine(slide, 730, 345, 1158, 355, { color: C.ochre, width: 4, arrow: true, name: 'real-path' });
  addText(slide, 'Curvatura · sección variable · pérdidas\nterminación timpánica y posición de observación', { x: 725, y: 440, w: 470, h: 90, size: 25, color: C.carbon, align: 'center', name: 'real-caption' });
  addText(slide, 'Los modelos explican una parte de la transferencia; no describen una conversión geométrica exacta.', { x: 175, y: 560, w: 930, h: 42, size: 27, color: C.berry, bold: true, align: 'center', name: 'cae-conclusion' });
}

function addLeverVisual(slide) {
  addText(slide, 'Entrada: más desplazamiento', { x: 90, y: 185, w: 420, h: 42, size: 28, color: C.teal, bold: true, align: 'center', name: 'lever-input' });
  addText(slide, 'Salida: más fuerza', { x: 790, y: 185, w: 400, h: 42, size: 28, color: C.ochre, bold: true, align: 'center', name: 'lever-output' });
  addShape(slide, { geometry: 'rect', name: 'lever-beam', x: 165, y: 350, w: 950, h: 22, fill: C.carbon, lineFill: C.carbon, lineWidth: 1 });
  addShape(slide, { geometry: 'triangle', name: 'lever-fulcrum', x: 620, y: 370, w: 90, h: 105, fill: C.berry2, lineFill: C.berry, lineWidth: 2 });
  addLine(slide, 270, 260, 270, 345, { color: C.teal, width: 5, arrow: true, name: 'lever-displacement' });
  addLine(slide, 1010, 260, 1010, 345, { color: C.ochre, width: 5, arrow: true, name: 'lever-force' });
  addText(slide, 'brazo de entrada', { x: 230, y: 405, w: 300, h: 36, size: 24, color: C.carbon, align: 'center', name: 'lever-arm-in' });
  addText(slide, 'brazo de salida', { x: 760, y: 405, w: 300, h: 36, size: 24, color: C.carbon, align: 'center', name: 'lever-arm-out' });
  addText(slide, 'La palanca intercambia fuerza y movimiento; no crea energía.', { x: 235, y: 515, w: 810, h: 50, size: 30, color: C.berry, bold: true, align: 'center', name: 'lever-conclusion' });
}

function addCochleaLongitudinal(slide) {
  addText(slide, 'BASE', { x: 85, y: 200, w: 130, h: 38, size: 28, color: C.berry, bold: true, align: 'center', name: 'cochlea-base' });
  addText(slide, 'ÁPEX', { x: 1070, y: 200, w: 130, h: 38, size: 28, color: C.berry, bold: true, align: 'center', name: 'cochlea-apex' });
  addShape(slide, { geometry: 'ellipse', name: 'oval-window', x: 125, y: 270, w: 52, h: 82, fill: C.ochreLight, lineFill: C.ochre, lineWidth: 3 });
  addShape(slide, { geometry: 'ellipse', name: 'round-window', x: 125, y: 430, w: 52, h: 82, fill: C.tealLight, lineFill: C.teal, lineWidth: 3 });
  addShape(slide, { geometry: 'roundRect', name: 'vestibular-path', x: 180, y: 275, w: 850, h: 78, fill: C.tealLight, lineFill: C.teal, lineWidth: 2, radius: 28 });
  addShape(slide, { geometry: 'roundRect', name: 'tympanic-path', x: 180, y: 430, w: 850, h: 78, fill: C.ivory, lineFill: C.berry2, lineWidth: 2, radius: 28 });
  addShape(slide, { geometry: 'roundRect', name: 'helicotrema', x: 985, y: 330, w: 145, h: 125, fill: C.ochreLight, lineFill: C.ochre, lineWidth: 2, radius: 40 });
  addText(slide, 'rampa vestibular', { x: 320, y: 294, w: 470, h: 40, size: 28, color: C.teal, bold: true, align: 'center', name: 'vestibular-label' });
  addText(slide, 'rampa timpánica', { x: 320, y: 449, w: 470, h: 40, size: 28, color: C.berry, bold: true, align: 'center', name: 'tympanic-label' });
  addText(slide, 'helicotrema', { x: 995, y: 372, w: 125, h: 38, size: 21, color: C.ochre, bold: true, align: 'center', name: 'helicotrema-label' });
  addLine(slide, 205, 315, 960, 315, { color: C.teal, width: 3, arrow: true, name: 'upper-direction' });
  addLine(slide, 960, 470, 205, 470, { color: C.berry2, width: 3, arrow: true, name: 'lower-direction' });
  addText(slide, 'Orientación espacial del modelo desenrollado; el fluido oscila localmente y no circula en una vuelta completa.', { x: 190, y: 555, w: 900, h: 48, size: 26, color: C.carbon, align: 'center', name: 'cochlea-long-note' });
}

function addCochleaCrossSection(slide, stage = 4) {
  const x = 205, w = 870;
  addShape(slide, { geometry: 'roundRect', name: 'cross-frame', x, y: 155, w, h: 430, fill: C.white, lineFill: C.carbon, lineWidth: 2, radius: 18 });
  addShape(slide, { geometry: 'rect', name: 'scala-vestibuli', x: x + 4, y: 160, w: w - 8, h: 122, fill: C.tealLight, lineFill: 'none' });
  addShape(slide, { geometry: 'rect', name: 'scala-media', x: x + 4, y: 285, w: w - 8, h: 135, fill: C.ochreLight, lineFill: 'none' });
  addShape(slide, { geometry: 'rect', name: 'scala-tympani', x: x + 4, y: 423, w: w - 8, h: 157, fill: C.ivory, lineFill: 'none' });
  addText(slide, stage >= 2 ? 'Rampa vestibular · perilinfa' : 'Rampa vestibular', { x: 325, y: 195, w: 630, h: 40, size: 28, color: C.teal, bold: true, align: 'center', name: 'cross-vestibular' });
  if (stage >= 4) addText(slide, 'Conducto coclear\nendolinfa', { x: 225, y: 315, w: 205, h: 66, size: 21, color: C.ochre, bold: true, align: 'center', name: 'cross-media' });
  else addText(slide, stage >= 2 ? 'Conducto coclear o rampa media · endolinfa' : 'Conducto coclear o rampa media', { x: 285, y: 320, w: 710, h: 46, size: 28, color: C.ochre, bold: true, align: 'center', name: 'cross-media' });
  addText(slide, stage >= 2 ? 'Rampa timpánica · perilinfa' : 'Rampa timpánica', { x: 325, y: 505, w: 630, h: 40, size: 28, color: C.berry, bold: true, align: 'center', name: 'cross-tympanic' });
  if (stage >= 3) {
    addLine(slide, x + 65, 280, x + w - 80, 300, { color: C.teal, width: 4, name: 'reissner' });
    addLine(slide, x + 55, 420, x + w - 55, 420, { color: C.berry, width: 5, name: 'basilar' });
    addText(slide, 'membrana de Reissner', { x: 860, y: 250, w: 280, h: 34, size: 21, color: C.teal, name: 'reissner-label' });
    addText(slide, 'membrana basilar', { x: 865, y: 430, w: 250, h: 34, size: 21, color: C.berry, name: 'basilar-label' });
  }
  if (stage >= 4) {
    addShape(slide, { geometry: 'ellipse', name: 'tectorial-membrane', x: 440, y: 337, w: 360, h: 42, fill: '#F4E9EF', lineFill: C.berry2, lineWidth: 2 });
    addShape(slide, { geometry: 'roundRect', name: 'ihc', x: 485, y: 375, w: 54, h: 42, fill: C.ochre, lineFill: C.ochre, lineWidth: 1, radius: 10 });
    [0, 1, 2].forEach((i) => addShape(slide, { geometry: 'roundRect', name: `ohc-${i+1}`, x: 650 + i * 62, y: 375, w: 44, h: 42, fill: C.teal, lineFill: C.teal, lineWidth: 1, radius: 10 }));
    addText(slide, 'CCI', { x: 487, y: 382, w: 50, h: 28, size: 20, color: C.white, bold: true, align: 'center', name: 'ihc-label' });
    addText(slide, 'CCE', { x: 650, y: 382, w: 180, h: 28, size: 20, color: C.white, bold: true, align: 'center', name: 'ohc-label' });
    addText(slide, 'membrana tectorial', { x: 435, y: 305, w: 370, h: 28, size: 20, color: C.berry2, align: 'center', name: 'tectorial-label' });
    addText(slide, 'órgano de Corti', { x: 475, y: 430, w: 350, h: 30, size: 22, color: C.carbon, bold: true, align: 'center', name: 'organ-label' });
  }
}

function addTunnelVisual(slide) {
  addLine(slide, 210, 525, 1070, 525, { color: C.berry, width: 6, name: 'tunnel-basilar' });
  addLine(slide, 400, 515, 560, 245, { color: C.teal, width: 9, name: 'inner-pillar' });
  addLine(slide, 560, 245, 825, 515, { color: C.ochre, width: 9, name: 'outer-pillar' });
  addText(slide, 'pilar interno', { x: 235, y: 335, w: 220, h: 36, size: 25, color: C.teal, bold: true, align: 'center', name: 'inner-pillar-label' });
  addText(slide, 'pilar externo', { x: 875, y: 350, w: 230, h: 36, size: 25, color: C.ochre, bold: true, align: 'center', name: 'outer-pillar-label' });
  addText(slide, 'TÚNEL DE\nCORTI', { x: 485, y: 360, w: 195, h: 72, size: 24, color: C.berry, bold: true, align: 'center', name: 'tunnel-space-title' });
  addText(slide, 'espacio triangular', { x: 470, y: 440, w: 235, h: 32, size: 21, color: C.berry, align: 'center', name: 'tunnel-space-body' });
  addText(slide, 'zona arcuata de la membrana basilar', { x: 365, y: 535, w: 550, h: 34, size: 23, color: C.berry, align: 'center', name: 'tunnel-base-label' });
  addText(slide, 'Referencia anatómica dentro del órgano de Corti; no es una célula ni una vía de propagación.', { x: 210, y: 590, w: 860, h: 40, size: 25, color: C.carbon, align: 'center', name: 'tunnel-note' });
}

function addMovementStates(slide) {
  addText(slide, 'Estado A', { x: 130, y: 170, w: 430, h: 40, size: 30, color: C.teal, bold: true, align: 'center', name: 'state-a-title' });
  addText(slide, 'Estado B', { x: 720, y: 170, w: 430, h: 40, size: 30, color: C.ochre, bold: true, align: 'center', name: 'state-b-title' });
  addLine(slide, 640, 155, 640, 565, { color: C.lightGray, width: 2, name: 'state-divider' });
  [[130,560,290,330,-1],[720,1150,360,295,1]].forEach(([x1,x2,basilarY,tectorialY,dir],i) => {
    addLine(slide, x1, basilarY, x2, basilarY, { color: C.berry, width: 6, name: `state-basilar-${i}` });
    addLine(slide, x1 + 45, tectorialY, x2 - 45, tectorialY, { color: C.teal, width: 6, name: `state-tectorial-${i}` });
    [0,1,2,3].forEach((j) => addShape(slide, { geometry: 'rect', name: `stereo-${i}-${j}`, x: x1 + 145 + j * 35 + dir * j * 5, y: Math.min(basilarY,tectorialY) + 18, w: 8, h: Math.abs(basilarY-tectorialY)-34, fill: C.carbon, lineFill: C.carbon, lineWidth: 1 }));
    addLine(slide, x1 + 220, basilarY + 70 * dir, x1 + 220, basilarY, { color: C.berry2, width: 4, arrow: true, name: `basilar-arrow-${i}` });
    addLine(slide, x1 + 290, tectorialY, x1 + 345, tectorialY, { color: C.teal, width: 4, arrow: true, name: `shear-arrow-${i}` });
  });
  addText(slide, 'El movimiento relativo cambia de sentido y deflecta los haces; las amplitudes están exageradas para leer la dirección.', { x: 160, y: 555, w: 960, h: 50, size: 26, color: C.carbon, align: 'center', name: 'movement-note' });
}

function addBundleStates(slide) {
  const labels = [['Reposo','probabilidad basal',0],['Deflexión excitatoria','apertura aumenta',1],['Dirección opuesta','apertura disminuye',-1]];
  labels.forEach(([title,body,dir],i) => {
    const x = 115 + i * 395;
    addText(slide, title, { x, y: 170, w: 300, h: 42, size: 28, color: i===0?C.carbon:i===1?C.teal:C.ochre, bold: true, align: 'center', name: `bundle-title-${i}` });
    [0,1,2,3,4].forEach((j) => addShape(slide, { geometry: 'rect', name: `bundle-hair-${i}-${j}`, x: x + 90 + j * 30 + dir * j * 7, y: 280 - j * 16, w: 10, h: 190 + j * 16, fill: C.carbon, lineFill: C.carbon, lineWidth: 1 }));
    if (dir !== 0) addLine(slide, x + 130, 245, x + 130 + dir * 95, 245, { color: dir > 0 ? C.teal : C.ochre, width: 5, arrow: true, name: `bundle-arrow-${i}` });
    addText(slide, body, { x, y: 505, w: 300, h: 44, size: 25, color: C.carbon, bold: true, align: 'center', name: `bundle-body-${i}` });
  });
}

function addDomainsMap(slide) {
  const nodes = [
    ['Energía disponible','gradiente electroquímico',C.tealLight,C.teal],
    ['Respuesta celular','potencial receptor graduado', '#F4E9EF', C.berry],
    ['Salida neural','potenciales de acción en la fibra', C.ochreLight, C.ochre],
  ];
  const boxes = nodes.map(([title,body,fill,line],i) => {
    const x = 90 + i * 400;
    const box = addShape(slide, { geometry: 'ellipse', name: `domain-${i}`, x, y: 225, w: 300, h: 210, fill, lineFill: line, lineWidth: 3 });
    addText(slide, title, { x: x+30, y: 260, w: 240, h: 42, size: 27, color: line, bold: true, align: 'center', name: `domain-title-${i}` });
    addText(slide, body, { x: x+35, y: 315, w: 230, h: 75, size: 24, color: C.carbon, align: 'center', name: `domain-body-${i}` });
    return box;
  });
  slide.shapes.connect(boxes[0], boxes[1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: C.berry2, width: 3 }, tail: { type: 'arrow' } });
  slide.shapes.connect(boxes[1], boxes[2], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: C.berry2, width: 3 }, tail: { type: 'arrow' } });
  addText(slide, 'Después ubicaremos potencial endococlear, reposo, receptor y acción dentro de estos tres dominios.', { x: 190, y: 510, w: 900, h: 48, size: 27, color: C.berry, bold: true, align: 'center', name: 'domains-note' });
}

function addEndocochlearMap(slide) {
  addPanel(slide, 'Endolinfa', 'potencial positivo respecto de una referencia extracoclear declarada', { x: 180, y: 175, w: 920, h: 120, kind: 'accent', titleSize: 28, bodySize: 25, name: 'endocochlear-endolymph' });
  addPanel(slide, 'Célula ciliada', 'interior celular', { x: 180, y: 320, w: 920, h: 120, kind: 'clinical', titleSize: 28, bodySize: 25, name: 'endocochlear-cell' });
  addPanel(slide, 'Perilinfa / referencia', 'el electrodo y la referencia de medida deben explicitarse', { x: 180, y: 465, w: 920, h: 120, kind: 'physical', titleSize: 28, bodySize: 25, name: 'endocochlear-reference' });
  addText(slide, 'Importa el gradiente electroquímico; un voltaje aislado no tiene significado sin referencia.', { x: 170, y: 610, w: 940, h: 38, size: 24, color: C.berry, bold: true, align: 'center', name: 'endocochlear-limit' });
}

function addMeasurementChain(slide) {
  const labels = [['Estímulo','entrada acústica'],['Generadores','cóclea y vía neural'],['Electrodos','activo y referencia'],['Registro','diferencia de potencial']];
  const boxes = labels.map(([title,body],i) => addPanel(slide,title,body,{x:65+i*300,y:225,w:255,h:175,kind:i===3?'clinical':i===2?'accent':'physical',titleSize:27,bodySize:24,name:`measurement-${i}`}));
  for(let i=0;i<boxes.length-1;i++) slide.shapes.connect(boxes[i], boxes[i+1], { kind:'straight', fromSide:'right', toSide:'left', line:{style:'solid',fill:C.berry2,width:3}, tail:{type:'arrow'} });
  addText(slide, 'La forma registrada depende del montaje y de la referencia; no es “el potencial del oído”.', { x: 190, y: 485, w: 900, h: 54, size: 29, color: C.berry, bold: true, align: 'center', name: 'measurement-limit' });
}

function addResolvedG3(slide) {
  addEquation(slide, 'Rₛ = 60/3,0 = 20   ·   Mₚ ≈ 20·1,2 = 24   ·   Gₚ = 20 log₁₀(24) ≈ 27,6 dB', { x: 95, y: 165, w: 1090, h: 105 });
  addPanel(slide, 'Datos didácticos', 'Sₜₘ = 60 mm²\nSₑ = 3,0 mm²\nRₗ = 1,2', { x: 90, y: 315, w: 330, h: 225, kind: 'physical', titleSize: 28, bodySize: 27, name: 'g3-data' });
  addPanel(slide, 'Resultado', 'Razón ideal de presiones: 24\nExpresión logarítmica: 27,6 dB', { x: 475, y: 315, w: 330, h: 225, kind: 'accent', titleSize: 28, bodySize: 27, name: 'g3-result' });
  addPanel(slide, 'Límite', 'No es dB SPL ni ganancia de energía. El oído real presenta pérdidas.', { x: 860, y: 315, w: 330, h: 225, kind: 'clinical', titleSize: 28, bodySize: 26, name: 'g3-limit' });
}

function addFinalCustomSlide(slide, d) {
  if (d.id === 'U06-013') { addCaeComparison(slide); return true; }
  if (d.id === 'U06-033') { addLeverVisual(slide); return true; }
  if (d.id === 'U06-051') { addCochleaLongitudinal(slide); return true; }
  if (d.id === 'U06-052') { addCochleaCrossSection(slide, 1); return true; }
  if (d.id === 'U06-053') { addCochleaCrossSection(slide, 2); return true; }
  if (d.id === 'U06-054') { addCochleaCrossSection(slide, 3); return true; }
  if (['U06-055','U06-056','U06-073'].includes(d.id)) { addCochleaCrossSection(slide, 4); return true; }
  if (d.id === 'U06-057') { addTunnelVisual(slide); return true; }
  if (d.id === 'U06-074') { addMovementStates(slide); return true; }
  if (d.id === 'U06-075') { addBundleStates(slide); return true; }
  if (d.id === 'U06-079') { addGeneric(slide, { ...d, visual: '', layout: 'FA_14_PREGUNTA_EJERCICIO' }); return true; }
  if (d.id === 'U06-083') { addDomainsMap(slide); return true; }
  if (d.id === 'U06-084') { addEndocochlearMap(slide); return true; }
  if (d.id === 'U06-101') { addMeasurementChain(slide); return true; }
  if (d.id === 'U06-111') { addResolvedG3(slide); return true; }
  return false;
}

function addBulletList(slide, ideas, { x, y, w, h, size = 28, color = C.carbon, name = 'bullets' } = {}) {
  if (!ideas.length) return;
  const shape = addShape(slide, { geometry: 'textbox', name, x, y, w, h, fill: 'none' });
  shape.text.set(ideas.map((idea) => ({ bulletCharacter: '•', marginLeft: 28, indent: -15, spaceAfter: 11,
    runs: [{ run: clean(idea), textStyle: { fontSize: `${size}px`, typeface: 'Calibri', color } }] })));
  shape.text.style = { fontSize: size, color, typeface: 'Calibri', autoFit: 'none', wrap: 'square',
    insets: { top: 8, right: 8, bottom: 8, left: 8 }, lineSpacing: 1.04 };
  return shape;
}

function addPanel(slide, title, body, { x, y, w, h, kind = 'neutral', titleSize = 28, bodySize = 26, name = 'panel' } = {}) {
  const st = STYLE[kind] ?? STYLE.neutral;
  const box = addShape(slide, { geometry: 'roundRect', name: `${name}-box`, x, y, w, h, fill: st.fill, lineFill: st.line, lineWidth: 2, radius: 12 });
  addText(slide, title, { x: x + 18, y: y + 14, w: w - 36, h: 38, size: titleSize, color: st.title, bold: true, name: `${name}-title`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  addText(slide, body, { x: x + 18, y: y + 56, w: w - 36, h: h - 72, size: bodySize, color: st.body, name: `${name}-body`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  return box;
}

function addEquation(slide, eq, { x = 135, y = 182, w = 1010, h = 105 } = {}) {
  if (!eq || eq === '—') return;
  addShape(slide, { geometry: 'roundRect', name: 'equation-box', x, y, w, h, fill: C.ivory, lineFill: C.berry2, lineWidth: 2, radius: 12 });
  addText(slide, eq, { x: x + 24, y: y + 12, w: w - 48, h: h - 24, size: eq.length > 105 ? 34 : 42,
    color: C.carbon, bold: true, align: 'center', valign: 'middle', font: 'Cambria Math', name: 'equation', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
}

function wrapLines(text, maxChars) {
  const out = [];
  for (const raw of String(text || '').split('\n')) {
    const words = raw.trim().split(/\s+/).filter(Boolean); let line = '';
    for (const word of words) { if (!line) line = word; else if (`${line} ${word}`.length <= maxChars) line += ` ${word}`; else { out.push(line); line = word; } }
    if (line) out.push(line);
  }
  return out;
}

function nodeTextLayout(n) {
  const titleSize = n.role === 'equation' ? 46 : 32; const bodySize = 30;
  const titleCap = Math.max(6, Math.floor((n.w - 40) / (titleSize * 0.54)));
  const bodyCap = Math.max(7, Math.floor((n.w - 40) / (bodySize * 0.50)));
  const titleLines = wrapLines(n.title, titleCap); const bodyLines = wrapLines(n.body, bodyCap).filter(Boolean);
  if (!n.body) { const blockH = titleLines.length * 38; return { titleSize, bodySize, titleLines, bodyLines, titleY: n.y + (n.h - blockH) / 2, titleH: blockH, bodyY: 0, bodyH: 0 }; }
  const titleH = Math.max(42, titleLines.length * 38); const titleY = n.y + 15; const bodyY = titleY + titleH + 5;
  return { titleSize, bodySize, titleLines, bodyLines, titleY, titleH, bodyY, bodyH: n.y + n.h - bodyY - 10 };
}

async function addDiagram(slide, d, asset) {
  const folder = path.dirname(path.resolve(ROOT, asset.local_path.replace(/[\\/]/g, path.sep)));
  const model = JSON.parse(await fs.readFile(path.join(folder, 'diagram_source.json'), 'utf8'));
  if (REVERSE_BRANCHES.has(model.id)) {
    model.edges = (model.edges || []).map((edge) => ({ ...edge, from: edge.to, to: edge.from }));
  }
  if (REMOVE_EDGES.has(model.id)) model.edges = [];
  // Los conectores se anclan primero a cajas transparentes. Las cajas visibles
  // se dibujan después, igual que en el SVG validado, para que ningún tramo de
  // línea pueda quedar por encima del texto o del interior de un nodo.
  const boxes = new Map();
  for (const n of model.nodes) {
    const box = addShape(slide, { geometry: 'roundRect', name: `${asset.asset_id}-${n.id}-anchor`, x: n.x, y: n.y, w: n.w, h: n.h, fill: 'none', lineFill: 'none', lineWidth: 0, radius: 10 });
    boxes.set(n.id, box);
  }
  for (const e of model.edges ?? []) {
    const from = boxes.get(e.from); const to = boxes.get(e.to); if (!from || !to) continue;
    const a = model.nodes.find((n) => n.id === e.from); const b = model.nodes.find((n) => n.id === e.to);
    const dx = (b.x + b.w / 2) - (a.x + a.w / 2); const dy = (b.y + b.h / 2) - (a.y + a.h / 2);
    const horizontal = Math.abs(dx) >= Math.abs(dy);
    const fromSide = horizontal ? (dx >= 0 ? 'right' : 'left') : (dy >= 0 ? 'bottom' : 'top');
    const toSide = horizontal ? (dx >= 0 ? 'left' : 'right') : (dy >= 0 ? 'top' : 'bottom');
    const conn = slide.shapes.connect(from, to, { kind: e.kind || 'elbow', fromSide, toSide,
      line: { style: 'solid', fill: C.carbon, width: 3 }, tail: { type: 'arrow', width: 'med', length: 'med' } });
    conn.name = `${asset.asset_id}-${e.id}`;
  }
  for (const n of model.nodes) {
    const st = STYLE[n.style] ?? STYLE.neutral; const t = nodeTextLayout(n);
    addShape(slide, { geometry: 'roundRect', name: `${asset.asset_id}-${n.id}-box`, x: n.x, y: n.y, w: n.w, h: n.h, fill: st.fill, lineFill: st.line, lineWidth: 2, radius: 10 });
    addText(slide, t.titleLines.join('\n'), { x: n.x + 20, y: t.titleY, w: n.w - 40, h: t.titleH, size: t.titleSize,
      color: st.title, bold: true, align: 'center', valign: n.body ? 'top' : 'middle', font: n.role === 'equation' ? 'Cambria Math' : 'Calibri', name: `${asset.asset_id}-${n.id}-title`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
    if (n.body) addText(slide, t.bodyLines.join('\n'), { x: n.x + 20, y: t.bodyY, w: n.w - 40, h: t.bodyH, size: t.bodySize,
      color: st.body, align: 'center', valign: 'top', font: n.role === 'equation' ? 'Cambria Math' : 'Calibri', name: `${asset.asset_id}-${n.id}-body`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  }
  return model;
}

async function addChart(slide, d, asset) {
  const assetPath = path.resolve(ROOT, asset.local_path.replace(/[\\/]/g, path.sep));
  const bytes = await fs.readFile(assetPath);
  const longTitle = d.title.length > 65;
  // Los gráficos se proyectan a ancho completo. La columna lateral de v01
  // reducía ejes y anotaciones por debajo de un tamaño cómodo para aula.
  const pos = { left: 45, top: longTitle ? 160 : 140, width: 1190, height: longTitle ? 460 : 480 };
  const image = slide.images.add({ blob: bytes, contentType: assetPath.toLowerCase().endsWith('.svg') ? 'image/svg+xml' : 'image/png',
    alt: d.alt || asset.description || asset.title, fit: 'contain', position: pos });
  image.name = `${d.id}-${asset.asset_id}`; image.alt = d.alt || asset.description || asset.title;
}

function addProcess(slide, d) {
  const steps = splitIdeas(d.content, 6);
  const n = Math.max(2, steps.length); const gap = n >= 5 ? 16 : 26; const w = Math.min(245, (1160 - gap * (n - 1)) / n);
  const total = n * w + (n - 1) * gap; const x0 = (1280 - total) / 2; const boxes = [];
  steps.forEach((step, i) => { const kind = i === n - 1 ? 'clinical' : i % 2 ? 'neutral' : 'physical'; const st = STYLE[kind];
    const box = addShape(slide, { geometry: 'roundRect', name: `process-${i + 1}`, x: x0 + i * (w + gap), y: 235, w, h: 160, fill: st.fill, lineFill: st.line, lineWidth: 2, radius: 12 });
    boxes.push(box); addText(slide, step, { x: x0 + i * (w + gap) + 14, y: 253, w: w - 28, h: 125, size: n >= 5 ? 23 : 26, color: st.body, bold: true, align: 'center', valign: 'middle', name: `process-${i + 1}-text`, insets: { top: 0, right: 0, bottom: 0, left: 0 } }); });
  for (let i = 0; i < boxes.length - 1; i += 1) slide.shapes.connect(boxes[i], boxes[i + 1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: C.berry2, width: 2.5 }, tail: { type: 'arrow', width: 'med', length: 'med' } });
  if (d.equations && d.equations !== '—') addEquation(slide, d.equations, { x: 220, y: 455, w: 840, h: 90 });
}

function addGeneric(slide, d) {
  const ideas = splitIdeas(d.content, 6);
  const isQuestion = /PREGUNTA|EJERCICIO/.test(d.layout);
  const isError = d.layout.includes('ERROR'); const isRecap = d.layout.includes('RECAP');
  const isCompare = d.layout.includes('COMPARACION'); const isEquation = d.layout.includes('ECUACION') || (d.equations && d.equations !== '—');
  if (isQuestion) {
    addPanel(slide, 'Consigna', d.content, { x: 72, y: 165, w: 755, h: 365, kind: 'accent', titleSize: 30, bodySize: d.content.length > 260 ? 25 : 29, name: 'question' });
    addPanel(slide, 'Para responder', d.example && d.example !== '—' ? d.example : 'Nombrá el objeto, identificá las magnitudes y justificá la relación causal.', { x: 865, y: 165, w: 345, h: 365, kind: 'physical', titleSize: 27, bodySize: 25, name: 'answer-guide' });
  } else if (isError) {
    addPanel(slide, 'Error frecuente', d.content, { x: 68, y: 165, w: 730, h: 390, kind: 'neutral', bodySize: 27, name: 'error' });
    addPanel(slide, 'Corrección', d.definitions || d.example || 'Volver a la cadena física y a las condiciones del modelo.', { x: 835, y: 165, w: 380, h: 390, kind: 'clinical', bodySize: 25, name: 'correction' });
  } else if (isCompare) {
    const mid = Math.ceil(Math.max(2, ideas.length) / 2);
    const labels = d.id === 'U06-013' ? ['Modelo ideal', 'Conducto auditivo real'] : ['Caso A', 'Caso B'];
    addPanel(slide, labels[0], ideas.slice(0, mid).join('\n\n') || d.content, { x: 65, y: 160, w: 545, h: 395, kind: 'physical', bodySize: 26, name: 'compare-a' });
    addPanel(slide, labels[1], ideas.slice(mid).join('\n\n') || d.definitions || d.example, { x: 670, y: 160, w: 545, h: 395, kind: 'clinical', bodySize: 26, name: 'compare-b' });
  } else if (isRecap) {
    const chunks = ideas.length ? ideas : splitIdeas(d.definitions || d.example, 5); const n = Math.max(1, chunks.length);
    const gap = n <= 4 ? 34 : 16; const w = Math.min(260, (1160 - gap * (n - 1)) / n); const total = n * w + (n - 1) * gap; let x = (1280 - total) / 2;
    chunks.forEach((t, i) => { addPanel(slide, String(i + 1).padStart(2, '0'), t, { x, y: 210, w, h: 285, kind: i % 3 === 2 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 25, bodySize: 24, name: `recap-${i + 1}` }); x += w + gap; });
  } else if (isEquation) {
    addEquation(slide, d.equations);
    const hasMeaning = d.definitions && d.definitions !== '—'; const hasUse = d.example && d.example !== '—';
    if (!hasMeaning && !hasUse) addPanel(slide, 'Interpretación', d.content, { x: 170, y: 325, w: 940, h: 250, kind: 'physical', bodySize: 27, name: 'equation-interpretation' });
    else {
      addPanel(slide, 'Significado físico', hasMeaning ? d.definitions : d.content, { x: 88, y: 325, w: 520, h: 250, kind: 'physical', bodySize: 25, name: 'equation-meaning' });
      addPanel(slide, 'Ejemplo o uso', hasUse ? d.example : d.content, { x: 670, y: 325, w: 520, h: 250, kind: 'clinical', bodySize: 25, name: 'equation-use' });
    }
  } else if (d.layout.includes('PROCESO')) addProcess(slide, d);
  else if (d.layout.includes('MEDIA')) {
    addPanel(slide, 'Alternativa estática', d.content, { x: 75, y: 165, w: 750, h: 380, kind: 'physical', titleSize: 30, bodySize: 28, name: 'media-static' });
    addPanel(slide, 'Recurso identificado', 'La reproducción opcional y sus condiciones están indicadas en las notas del orador.', { x: 865, y: 165, w: 340, h: 380, kind: 'neutral', titleSize: 27, bodySize: 25, name: 'media-id' });
  } else {
    const bodySize = d.content.length > 330 ? 25 : d.content.length > 235 ? 27 : 29;
    const hasDefinition = d.definitions && d.definitions !== '—';
    const hasExample = d.example && d.example !== '—';
    addBulletList(slide, ideas.length ? ideas : [d.content], { x: 70, y: 160, w: hasDefinition || hasExample ? 710 : 1135, h: 405, size: bodySize, name: 'main-ideas' });
    if (hasDefinition || hasExample) {
      const sideTitle = hasDefinition ? 'Definición' : 'Ejemplo';
      const sideBody = hasDefinition ? d.definitions : d.example;
      addPanel(slide, sideTitle, sideBody, { x: 830, y: 170, w: 375, h: 350, kind: /clín|fono|audit|voz/i.test(`${d.title} ${d.content}`) ? 'clinical' : 'physical', bodySize: 25, name: 'side-panel' });
    }
  }
}

function addResolvedSourceSlide(slide, d) {
  if (d.id === 'U06-057') {
    addPanel(slide, 'Pilar interno', 'Límite medial', { x: 80, y: 215, w: 285, h: 205, kind: 'physical', bodySize: 30, name: 'tunnel-inner' });
    addPanel(slide, 'Túnel de Corti', 'Espacio triangular lleno de fluido', { x: 410, y: 185, w: 460, h: 265, kind: 'accent', bodySize: 30, name: 'tunnel-space' });
    addPanel(slide, 'Pilar externo', 'Límite lateral', { x: 915, y: 215, w: 285, h: 205, kind: 'clinical', bodySize: 30, name: 'tunnel-outer' });
    addPanel(slide, 'Membrana basilar', 'La zona arcuata completa el límite inferior', { x: 250, y: 485, w: 780, h: 100, kind: 'neutral', titleSize: 28, bodySize: 25, name: 'tunnel-base' });
    return true;
  }
  if (d.id === 'U06-085') {
    addPanel(slide, 'Potencial de reposo', 'Condición eléctrica basal de la membrana, medida respecto de una referencia extracelular declarada.', { x: 80, y: 175, w: 520, h: 330, kind: 'neutral', titleSize: 31, bodySize: 29, name: 'resting' });
    addPanel(slide, 'Potencial receptor', 'Cambio graduado respecto del estado basal cuando la deflexión modifica la corriente iónica.', { x: 680, y: 175, w: 520, h: 330, kind: 'accent', titleSize: 31, bodySize: 29, name: 'receptor' });
    addText(slide, 'La referencia de medida importa; aquí no se fija un valor universal.', { x: 190, y: 535, w: 900, h: 42, size: 29, color: C.berry, bold: true, align: 'center', name: 'resting-caution' });
    return true;
  }
  if (d.id === 'U06-096') {
    const items = [
      ['Onda', 'La señal presenta ciclos y fases.'],
      ['Descargas', 'Los eventos pueden concentrarse en fases preferidas.'],
      ['Sincronía', 'No implica un impulso por cada ciclo.'],
      ['Dependencia', 'Varía con frecuencia y tipo de información.'],
    ];
    const boxes = items.map((_, i) => addShape(slide, { geometry: 'roundRect', name: `phase-${i + 1}-anchor`, x: 55 + i * 305, y: 210, w: 265, h: 255, fill: 'none', lineFill: 'none', lineWidth: 0, radius: 12 }));
    for (let i = 0; i < boxes.length - 1; i += 1) slide.shapes.connect(boxes[i], boxes[i + 1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: C.berry2, width: 2.5 }, tail: { type: 'arrow', width: 'med', length: 'med' } });
    items.forEach(([title, body], i) => {
      const x = 55 + i * 305;
      addPanel(slide, title, body, { x, y: 210, w: 265, h: 255, kind: i % 2 ? 'neutral' : 'physical', titleSize: 27, bodySize: 26, name: `phase-${i + 1}` });
    });
    return true;
  }
  if (d.id === 'U06-115') {
    addPanel(slide, 'Umbral', 'Depende del estímulo, el método y la persona; no es una constante universal.', { x: 75, y: 160, w: 530, h: 185, kind: 'physical', titleSize: 29, bodySize: 26, name: 'reflex-threshold' });
    addPanel(slide, 'Latencia', 'Disminuye al aumentar el nivel por encima del umbral, pero la respuesta muscular no es instantánea.', { x: 675, y: 160, w: 530, h: 185, kind: 'accent', titleSize: 29, bodySize: 26, name: 'reflex-latency' });
    addPanel(slide, 'Impulsos breves', 'El comienzo del impulso puede preceder a la contracción: no hay protección inicial garantizada.', { x: 75, y: 380, w: 530, h: 185, kind: 'clinical', titleSize: 29, bodySize: 26, name: 'reflex-impulse' });
    addPanel(slide, 'Interpretación', 'Una medición del reflejo informa sobre varias partes del sistema; no identifica por sí sola una etiología.', { x: 675, y: 380, w: 530, h: 185, kind: 'neutral', titleSize: 29, bodySize: 26, name: 'reflex-interpretation' });
    return true;
  }
  if (d.id === 'U06-116') {
    addPanel(slide, '1 · Ubicación', 'Órgano de Corti, sobre la membrana basilar.', { x: 70, y: 175, w: 350, h: 310, kind: 'physical', titleSize: 29, bodySize: 28, name: 'tunnel-check-1' });
    addPanel(slide, '2 · Límites', 'Pilar interno, pilar externo y zona arcuata de la membrana basilar.', { x: 465, y: 175, w: 350, h: 310, kind: 'accent', titleSize: 29, bodySize: 28, name: 'tunnel-check-2' });
    addPanel(slide, '3 · Lectura', 'Espacio triangular; esquema conceptual, no escala anatómica.', { x: 860, y: 175, w: 350, h: 310, kind: 'clinical', titleSize: 29, bodySize: 28, name: 'tunnel-check-3' });
    addText(slide, 'Rotular sin confundir el túnel con una célula, una membrana o el espacio de Nuel.', { x: 150, y: 525, w: 980, h: 42, size: 28, color: C.berry, bold: true, align: 'center', name: 'tunnel-check-warning' });
    return true;
  }
  return false;
}

function addBlocked(slide, d) {
  addShape(slide, { geometry: 'roundRect', name: 'blocked-frame', x: 155, y: 185, w: 970, h: 330, fill: C.ivory, lineFill: C.gray, lineWidth: 2, radius: 12 });
  addText(slide, 'Material de respaldo no habilitado para proyección', { x: 205, y: 230, w: 870, h: 55, size: 34, color: C.berry, bold: true, align: 'center', name: 'blocked-heading' });
  addText(slide, 'La definición y el rotulado requieren una fuente específica autorizada. Esta versión no completa el contenido por inferencia.', { x: 235, y: 325, w: 810, h: 105, size: 28, color: C.carbon, align: 'center', valign: 'middle', name: 'blocked-message' });
  addText(slide, 'No proyectar', { x: 495, y: 455, w: 290, h: 40, size: 24, color: C.red, bold: true, align: 'center', name: 'blocked-label' });
}

async function clearSlide(slide) {
  slide.shapes.deleteAll();
  for (const image of [...slide.images.items]) slide.images.deleteById(image.id);
  for (const collection of [slide.tables, slide.charts]) if (collection?.items) for (const item of [...collection.items]) {
    if (typeof item.delete === 'function') item.delete(); else if (typeof collection.deleteById === 'function') collection.deleteById(item.id);
  }
}

function assetForSlide(d, approved, byId) {
  const explicit = [...d.visual.matchAll(/U06-(?:CH|DG)-\d{3}[A-Z]?/g)].map((m) => m[0]);
  for (const id of explicit) if (byId.has(id)) return byId.get(id);
  return approved.find((a) => slideRefMatches(a.slide_id, d.id));
}

function addNotes(slide, d, note, asset) {
  const lines = [`- Fuentes de contenido: ${d.source || 'Programa oficial y libro del curso.'}`];
  if (asset) lines.push(`- Asset propio aprobado: ${asset.asset_id}.`);
  const full = `${note || ''}\n\n[Alt text]\n${d.alt || 'Contenido textual editable de la diapositiva.'}\n\n[Sources]\n${lines.join('\n')}`.trim();
  slide.speakerNotes.clear(); slide.speakerNotes.textFrame.setText(full); slide.speakerNotes.setVisible(true);
}

const slidesData = parseSlideText(await fs.readFile(path.join(UNIT, 'slide_text.md'), 'utf8'));
const notes = parseNotes(await fs.readFile(path.join(UNIT, 'speaker_notes.md'), 'utf8'));
const manifest = parseCsv(await fs.readFile(path.join(UNIT, 'asset_manifest.csv'), 'utf8'));
const approved = manifest.filter((a) => a.status === 'approved' && ['generated_chart', 'generated_diagram'].includes(a.type));
const byId = new Map(approved.map((a) => [a.asset_id, a]));
if (slidesData.length !== 117 || notes.size !== 117) throw new Error(`Conteos incompatibles: slides=${slidesData.length}, notas=${notes.size}.`);

const deck = await PresentationFile.importPptx(await FileBlob.load(STARTER));
const slides = [...deck.slides.items];
if (slides.length !== 117) throw new Error(`El starter debe tener 117 slides; tiene ${slides.length}.`);
const log = [];
for (let i = 0; i < slides.length; i += 1) {
  const slide = slides[i]; const d = slidesData[i]; await clearSlide(slide);
  const dark = ['FA_00_PORTADA', 'FA_01_DIVISOR', 'FA_21_CIERRE_PUENTE'].includes(d.layout);
  slide.background.fill = dark ? C.berry : C.white;
  if (d.layout === 'FA_00_PORTADA') {
    addText(slide, 'UNIDAD 6 · FÍSICA ACÚSTICA', { x: 64, y: 42, w: 560, h: 28, size: 18, color: C.white, bold: true, name: 'cover-eyebrow' });
    addText(slide, d.title, { x: 78, y: 125, w: 650, h: 245, size: 50, color: C.white, font: 'Calibri Light', name: 'cover-title', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
    addText(slide, d.subtitle, { x: 82, y: 390, w: 640, h: 70, size: 29, color: '#EADDE4', name: 'cover-subtitle' });
    const chain = ['aire', 'tímpano', 'cóclea', 'nervio'];
    const boxes = chain.map((_, k) => addShape(slide, { geometry: 'roundRect', name: `cover-step-${k + 1}-anchor`, x: 780 + (k % 2) * 205, y: 185 + Math.floor(k / 2) * 170, w: 170, h: 110, fill: 'none', lineFill: 'none', lineWidth: 0, radius: 10 }));
    slide.shapes.connect(boxes[0], boxes[1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: '#E0B9CB', width: 2 }, tail: { type: 'arrow' } });
    slide.shapes.connect(boxes[1], boxes[2], { kind: 'elbow', fromSide: 'bottom', toSide: 'top', line: { style: 'solid', fill: '#E0B9CB', width: 2 }, tail: { type: 'arrow' } });
    slide.shapes.connect(boxes[2], boxes[3], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: '#E0B9CB', width: 2 }, tail: { type: 'arrow' } });
    chain.forEach((t, k) => { addShape(slide, { geometry: 'roundRect', name: `cover-step-${k + 1}`, x: 780 + (k % 2) * 205, y: 185 + Math.floor(k / 2) * 170, w: 170, h: 110, fill: k < 2 ? '#6A2447' : '#77384F', lineFill: '#CFA7BA', lineWidth: 1.5, radius: 10 }); addText(slide, t, { x: 795 + (k % 2) * 205, y: 215 + Math.floor(k / 2) * 170, w: 140, h: 50, size: 26, color: C.white, bold: true, align: 'center', valign: 'middle', name: `cover-step-${k + 1}-text` }); });
    addText(slide, '4 encuentros · ruta central + ampliaciones + respaldo', { x: 82, y: 520, w: 650, h: 35, size: 22, color: '#EADDE4', name: 'cover-route' });
  } else if (d.layout === 'FA_01_DIVISOR' || d.layout === 'FA_21_CIERRE_PUENTE') {
    const route = teachingRoute(d);
    addText(slide, `UNIDAD 6 · ${route.session} · ${route.route}`, { x: 55, y: 24, w: 520, h: 24, size: 16, color: '#E1C8D4', bold: true, name: 'dark-eyebrow' });
    addText(slide, d.title, { x: 80, y: 225, w: 1120, h: 115, size: 54, color: C.white, font: 'Calibri Light', align: 'center', valign: 'middle', name: 'divider-title' });
    addText(slide, d.subtitle, { x: 165, y: 370, w: 950, h: 65, size: 28, color: '#E6D5DD', align: 'center', name: 'divider-subtitle' });
    if (d.content && d.content !== '—' && clean(d.content).toLowerCase() !== clean(d.subtitle).toLowerCase()) addText(slide, d.content, { x: 220, y: 470, w: 840, h: 75, size: 25, color: '#D4BDC8', align: 'center', name: 'divider-content' });
  } else {
    addTitle(slide, d);
    const asset = BLOCKED.has(d.id) ? undefined : assetForSlide(d, approved, byId);
    const custom = addFinalCustomSlide(slide, d);
    if (custom) { /* Correcciones pedagógicas y de consistencia para la versión final. */ }
    else if (addResolvedSourceSlide(slide, d)) { /* Corrección de fuentes y contenido en v02. */ }
    else if (BLOCKED.has(d.id)) addBlocked(slide, d);
    else if (asset?.type === 'generated_chart') await addChart(slide, d, asset);
    else if (asset?.type === 'generated_diagram') await addDiagram(slide, d, asset);
    else addGeneric(slide, d);
    addCaption(slide, d, custom ? undefined : asset);
    addTopRail(slide, d);
    addNotes(slide, d, notes.get(d.id), custom ? undefined : asset);
    log.push({ slide: i + 1, id: d.id, layout: d.layout, asset: custom ? null : asset?.asset_id || null, custom, blocked: BLOCKED.has(d.id) });
    continue;
  }
  addNotes(slide, d, notes.get(d.id), undefined);
  log.push({ slide: i + 1, id: d.id, layout: d.layout, asset: null, blocked: false });
}

const pptx = await PresentationFile.exportPptx(deck); await pptx.save(OUT);
const inspect = await deck.inspect({ kind: 'deck,slide,textbox,shape,image,chart,table,notes,layout', include: 'id,slide,name,title,text,textPreview,textChars,bbox,bboxUnit,isPlaceholder,alt', maxChars: 2_000_000 });
await fs.writeFile(path.join(QA, 'final-inspect.ndjson'), inspect.ndjson, 'utf8');
await fs.writeFile(path.join(QA, 'build-log.json'), `${JSON.stringify({ output: OUT, slides: log, approvedAssetCount: approved.length }, null, 2)}\n`, 'utf8');
console.log(JSON.stringify({ output: OUT, slides: log.length, assetsInserted: log.filter((x) => x.asset).length, blocked: log.filter((x) => x.blocked).length }, null, 2));
