import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

const [rootArg, starterArg, outArg, qaDirArg] = process.argv.slice(2);
const workspace = process.env.U07_ARTIFACT_WORKSPACE;
if (!rootArg || !starterArg || !outArg || !workspace) {
  throw new Error('Uso: U07_ARTIFACT_WORKSPACE=<workspace> node u07_build_presentation.mjs <repoRoot> <starter.pptx> <out.pptx> [qaDir]');
}
const req = createRequire(path.join(workspace, 'package.json'));
const entry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(entry).href);

const ROOT = path.resolve(rootArg);
const UNIT = path.join(ROOT, 'units/unit_07');
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
const REVERSE_BRANCHES = new Set();
const REMOVE_EDGES = new Set();
const COMPLEMENTARY = new Set([
  'U07-015', 'U07-016', 'U07-017', 'U07-026', 'U07-036', 'U07-040',
  'U07-042', 'U07-061', 'U07-062', 'U07-063', 'U07-064', 'U07-071',
  'U07-074', 'U07-092', 'U07-105', 'U07-108', 'U07-115', 'U07-116',
]);

const subscript = (token) => ({
  S: 'ₛ', TM: 'ₜₘ', E: 'ₑ', L: 'ₗ', p: 'ₚ', res: 'ᵣₑₛ', rms: 'ᵣₘₛ',
  ref: 'ᵣₑ𝒻',
  N: 'ₙ', son: 'ₛₒₙ', CT: '꜀ₜ', LR: 'ₗᵣ', obj: 'ₒᵦⱼ',
  60: '₆₀', c: '꜀', q: 'q', e: 'e',
  0: '₀', 1: '₁', 2: '₂', 3: '₃',
}[token] || `_${token}`);

await fs.mkdir(path.dirname(OUT), { recursive: true });
await fs.mkdir(QA, { recursive: true });

const clean = (s = '') => String(s)
  .replace(/`/g, '').replace(/\*+/g, '').replace(/\$/g, '')
  .replace(/\[(?:BLOQUEADA|PROVISIONAL)\]\s*/gi, '')
  .replace(/\b(?:Provisional|Bloqueada):\s*/gi, '')
  .replace(/\bIdea central:\s*/gi, '')
  .replace(/\bphones\b/gi, 'fones').replace(/\bphon\b/gi, 'fon')
  .replace(/\bsones\b/gi, 'sones').replace(/\bsone\b/gi, 'son')
  .replace(/\bmáscara\b/gi, (m) => m[0] === 'M' ? 'Señal enmascarante' : 'señal enmascarante')
  .replace(/\babs\s*\(([^()]+(?:\([^()]*\))?[^()]*)\)/gi, '|$1|')
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
  const re = /^## (U07-\d{3})\s*$/gm;
  const matches = [...md.matchAll(re)];
  return matches.map((m, i) => {
    const block = md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length);
    const fields = {}; const rawFields = {};
    const fieldMatches = [...block.matchAll(/^- \*\*([^*]+):\*\*\s*(.*)$/gm)];
    fieldMatches.forEach((fm, index) => {
      const start = fm.index + fm[0].length;
      const end = fieldMatches[index + 1]?.index ?? block.length;
      const continuation = block.slice(start, end).split(/\r?\n/)
        .map((line) => line.replace(/^\s*[-*]\s+/, '').trim()).filter(Boolean);
      const value = [fm[2].trim(), ...continuation].filter(Boolean).join(' ');
      const key = fm[1].trim().toLowerCase(); rawFields[key] = value; fields[key] = clean(value);
    });
    const pick = (...keys) => {
      for (const key of keys) {
        if (fields[key] !== undefined) return fields[key];
        const fuzzy = Object.entries(fields).find(([k]) => k.startsWith(key));
        if (fuzzy) return fuzzy[1];
      }
      return '';
    };
    return {
      id: m[1], title: pick('título'), state: Number(m[1].slice(-3)) >= 122 ? 'respaldo' : COMPLEMENTARY.has(m[1]) ? 'ampliación' : 'ruta central',
      subtitle: pick('subtítulo'), content: pick('contenido visible'), equations: pick('ecuaciones', 'ecuación'),
      definitions: pick('definiciones', 'definición'), example: pick('ejemplo'), caption: pick('caption'),
      visual: pick('visual'), layout: String(rawFields.layout || '').replace(/[`\.\s]/g, ''), source: pick('fuente'),
      alt: pick('texto alternativo'), raw: block,
    };
  });
}

function parseNotes(md) {
  const re = /^## (U07-\d{3})[^\n]*$/gm;
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

const INTERNAL_COPY = [
  /^compare relaciones/i,
  /^la proximidad entre cajas/i,
  /^definici[oó]n completa\.?$/i,
  /^condiciones\.?$/i,
  /^dos columnas:/i,
  /^tabla de /i,
  /^ecuaci[oó]n[,;:]/i,
  /^error, definici[oó]n f[ií]sica/i,
  /^(datos|resta|resultado|exponente|potencia|signo|sustituci[oó]n|segundos|microsegundos|valores expl[ií]citos)\.?$/i,
  /^conversi[oó]n a /i,
  /^qu[eé] no permite concluir/i,
  /^interpretaci[oó]n( condicionada| y l[ií]mite)?\.?$/i,
  /^divisi[oó]n\.?$/i,
  /^l[ií]mite interpretativo\.?$/i,
  /^interpretar el resultado dentro de las condiciones indicadas/i,
];

function audienceIdeas(text, max = 6) {
  const parts = splitIdeas(text, Math.max(max * 2, 8))
    .map((part) => part.replace(/^[-–•]\s*/, '').trim())
    .filter((part) => part && !INTERNAL_COPY.some((pattern) => pattern.test(part)));
  if (parts.length > max) return [...parts.slice(0, max - 1), parts.slice(max - 1).join(' ')];
  return parts;
}

function audienceText(text, fallback = '') {
  const ideas = audienceIdeas(text, 6);
  return ideas.length ? ideas.join('\n\n') : fallback;
}

const COMPARE_LABELS = {
  'U07-013': ['Modelo ideal', 'Conducto auditivo real'],
  'U07-035': ['Frecuencia', 'Pitch'],
  'U07-038': ['Nivel físico', 'Sonoridad percibida'],
  'U07-041': ['Duración física', 'Duración percibida'],
  'U07-053': ['Magnitud física', 'Atributo perceptual'],
  'U07-082': ['Escena A', 'Escena B'],
  'U07-096': ['Simplificación', 'Formulación correcta'],
  'U07-102': ['ITD', 'ILD'],
  'U07-113': ['Enmascaramiento energético', 'Enmascaramiento informacional'],
  'U07-115': ['Fuentes coincidentes', 'Fuentes separadas'],
  'U07-128': ['STI', 'SII'],
};

const EQUATION_USE = {
  'U07-023': 'La diferencia expresa, en dB, cuánto cambia el nivel medido entre el tímpano y el campo libre a una misma frecuencia. No es una ganancia de sonoridad.',
  'U07-024': 'El resultado de 8 dB vale solo para la frecuencia, las posiciones y el procedimiento indicados.',
  'U07-049': 'Modelo válido por encima de 40 phon: cada aumento de 10 phon duplica la sonoridad en sones; 40 phon corresponden a 1 sone.',
  'U07-051': 'Dentro del modelo, 70 phon corresponden a 8 sones. No implica que 70 phon equivalgan siempre a 70 dB SPL.',
  'U07-057': 'Un valor positivo indica que el enmascarador elevó el umbral. Ambos umbrales deben compararse con el mismo método y referencia.',
  'U07-058': 'Una diferencia de 25 dB representa la elevación del umbral bajo las condiciones declaradas.',
  'U07-080': 'Una SNR positiva indica que el nivel de habla supera al ruido cuando banda, posición e intervalo de medida son comparables.',
  'U07-081': '+8 dB describe una relación de niveles; no predice por sí sola la inteligibilidad.',
  'U07-086': 'Un 15 % significa 12 consonantes no reconocidas de 80 en esa prueba; no identifica por sí solo la causa.',
  'U07-090': 'La diferencia de recorrido dividida por c da el retardo físico. La percepción también depende de nivel, dirección y contenido.',
  'U07-091': '19,8 ms es el retardo físico del ejemplo, no un límite universal entre fusión y eco.',
  'U07-104': 'd/c brinda una estimación de orden de magnitud; no incorpora difracción ni dirección de llegada.',
  'U07-105': '525 μs es una estimación para la separación indicada, no una constante anatómica universal.',
  'U07-101': 'La sombra de la cabeza puede producir diferencias de nivel dependientes de frecuencia y dirección. Mantenga siempre el orden izquierda menos derecha.',
  'U07-125': 'La ERB es un modelo empírico expresado en hertz; no representa una banda anatómica rígida.',
  'U07-126': 'A 1 kHz, el modelo estima una ERB cercana a 133 Hz.',
  'U07-132': 'La diferencia entre el recorrido reflejado y el directo determina el retardo físico; no debe usarse el recorrido reflejado aislado.',
};

function slideRefMatches(ref, id) {
  const target = Number(id.slice(-3));
  for (const token of String(ref || '').split(/[;,]/).map((x) => x.trim())) {
    const exact = token.match(/^U07-(\d{3})$/); if (exact && Number(exact[1]) === target) return true;
    const range = token.match(/^U07-(\d{3})[–-](?:U07-)?(\d{3})$/);
    if (range && target >= Number(range[1]) && target <= Number(range[2])) return true;
  }
  return false;
}

function hasMeaningfulText(value) {
  const normalized = clean(value);
  return Boolean(normalized && !/^—/.test(normalized));
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
  const forceCompact = ['U07-075', 'U07-111'].includes(d.id);
  const titleY = d.id === 'U07-111' ? 63 : 43;
  addText(slide, d.title, { x: 52, y: titleY, w: 1172, h: long ? 88 : 72, size: d.id === 'U07-111' ? 32 : forceCompact ? 34 : veryLong ? 31 : long ? 34 : 40,
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
  addText(slide, `UNIDAD 7 · ${route.session} · ${route.route}`, { x: 50, y: 2, w: 520, h: 24, size: 14,
    color: C.berry2, bold: true, name: 'eyebrow', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
}

function addPageNumber(slide, page, dark = false) {
  addText(slide, String(page), { x: 1180, y: 676, w: 38, h: 18, size: 13,
    color: dark ? '#E1C8D4' : C.gray, align: 'right', name: 'slide-number', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
}

function addCaption(slide, d, asset) {
  // Los recursos propios se documentan en notas/manifiesto. En pantalla queda
  // únicamente un caption funcional cuando el gráfico exige una clave de lectura.
  if (asset?.type !== 'chart') return;
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
  if (d.id === 'U07-013') { addCaeComparison(slide); return true; }
  if (d.id === 'U07-033') { addLeverVisual(slide); return true; }
  if (d.id === 'U07-051') { addCochleaLongitudinal(slide); return true; }
  if (d.id === 'U07-052') { addCochleaCrossSection(slide, 1); return true; }
  if (d.id === 'U07-053') { addCochleaCrossSection(slide, 2); return true; }
  if (d.id === 'U07-054') { addCochleaCrossSection(slide, 3); return true; }
  if (['U07-055','U07-056','U07-073'].includes(d.id)) { addCochleaCrossSection(slide, 4); return true; }
  if (d.id === 'U07-057') { addTunnelVisual(slide); return true; }
  if (d.id === 'U07-074') { addMovementStates(slide); return true; }
  if (d.id === 'U07-075') { addBundleStates(slide); return true; }
  if (d.id === 'U07-079') { addGeneric(slide, { ...d, visual: '', layout: 'FA_14_PREGUNTA_EJERCICIO' }); return true; }
  if (d.id === 'U07-083') { addDomainsMap(slide); return true; }
  if (d.id === 'U07-084') { addEndocochlearMap(slide); return true; }
  if (d.id === 'U07-101') { addMeasurementChain(slide); return true; }
  if (d.id === 'U07-111') { addResolvedG3(slide); return true; }
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
  const equationSize = eq.length > 90 ? 30 : eq.length > 65 ? 34 : 42;
  addText(slide, eq, { x: x + 24, y: y + 12, w: w - 48, h: h - 24, size: equationSize,
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
  const assetPath = path.resolve(ROOT, asset.local_path.replace(/[\\/]/g, path.sep));
  const folder = path.dirname(assetPath);
  const model = JSON.parse(await fs.readFile(path.join(folder, 'diagram_source.json'), 'utf8'));
  // El export PPTX editable de algunos conectores no conserva de manera
  // uniforme la primera flecha ni todas las ramas. Se inserta el PNG final de
  // 2560×1440, validado junto con el SVG, y se recortan solo título y footer
  // del asset. Título, rail, footer, numeración y notas siguen editables.
  const suffix = asset.asset_id.replace('U07-DG-', '').toLowerCase();
  const pngPath = path.join(folder, `u07_dg_${suffix}_master.png`);
  const fileBytes = await fs.readFile(pngPath);
  const bytes = fileBytes.buffer.slice(fileBytes.byteOffset, fileBytes.byteOffset + fileBytes.byteLength);
  const image = slide.images.add({ blob: bytes, contentType: 'image/png', alt: d.alt || model.alt || asset.description,
    fit: 'cover', position: { left: 0, top: 100, width: 1280, height: 520 } });
  image.name = `${d.id}-${asset.asset_id}-validated-png`;
  image.alt = d.alt || model.alt || asset.description;
  addText(slide, model.title || d.title, { x: 64, y: 44, w: 1150, h: 48, size: 40,
    color: C.carbon, font: 'Calibri Light', name: 'diagram-title', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  // Los avisos repetitivos y los códigos de producción quedan en notas y
  // manifiesto. El área proyectada se reserva para el diagrama y su lectura.
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
  const steps = audienceIdeas(d.content, 6);
  const n = Math.max(2, steps.length); const gap = n >= 5 ? 16 : 26; const w = Math.min(245, (1160 - gap * (n - 1)) / n);
  const total = n * w + (n - 1) * gap; const x0 = (1280 - total) / 2; const boxes = [];
  steps.forEach((step, i) => { const kind = i === n - 1 ? 'clinical' : i % 2 ? 'neutral' : 'physical'; const st = STYLE[kind];
    const box = addShape(slide, { geometry: 'roundRect', name: `process-${i + 1}`, x: x0 + i * (w + gap), y: 235, w, h: 160, fill: st.fill, lineFill: st.line, lineWidth: 2, radius: 12 });
    boxes.push(box); addText(slide, step, { x: x0 + i * (w + gap) + 14, y: 253, w: w - 28, h: 125, size: n >= 5 ? 23 : 26, color: st.body, bold: true, align: 'center', valign: 'middle', name: `process-${i + 1}-text`, insets: { top: 0, right: 0, bottom: 0, left: 0 } }); });
  for (let i = 0; i < boxes.length - 1; i += 1) slide.shapes.connect(boxes[i], boxes[i + 1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: C.berry2, width: 2.5 }, tail: { type: 'arrow', width: 'med', length: 'med' } });
  if (d.equations && d.equations !== '—') addEquation(slide, d.equations, { x: 220, y: 455, w: 840, h: 90 });
}

const WORKED_EXAMPLES = {
  'U07-024': {
    steps: [
      ['Datos comparables', 'Campo: 50 dB SPL\nTímpano: 58 dB SPL'],
      ['Sustitución', 'G꜀ₜ = 58 dB SPL − 50 dB SPL'],
      ['Resultado', 'G꜀ₜ = 8 dB'],
    ],
    interpretation: 'Es una diferencia entre dos posiciones para la misma frecuencia; no es una ganancia fija de sonoridad.',
  },
  'U07-051': {
    steps: [
      ['Dato', 'Lₙ = 70 fon'],
      ['Sustitución', 'Nₛₒₙ = 2^[(70 − 40)/10] son'],
      ['Resultado', 'Nₛₒₙ = 2³ son = 8 sones'],
    ],
    interpretation: 'Ocho sones expresan ocho veces la referencia de 1 son dentro del modelo; no son 8 dB SPL.',
  },
  'U07-058': {
    steps: [
      ['Datos comparables', 'Quietud: 10 dB SPL\nCon enmascarador: 35 dB SPL'],
      ['Sustitución', 'M = 35 dB SPL − 10 dB SPL'],
      ['Resultado', 'M = 25 dB'],
    ],
    interpretation: 'El umbral se elevó 25 dB bajo esas condiciones; no informa por sí solo el nivel del enmascarador.',
  },
  'U07-081': {
    steps: [
      ['Datos comparables', 'Voz: 68 dB SPL\nRuido: 60 dB SPL'],
      ['Sustitución', 'SNR = 68 dB SPL − 60 dB SPL'],
      ['Resultado', 'SNR = +8 dB'],
    ],
    interpretation: 'El signo positivo indica mayor nivel de voz. La SNR sola no predice inteligibilidad: faltan tarea, oyente y reverberación.',
  },
  'U07-091': {
    steps: [
      ['Datos', 'Δd = 6,8 m\nc = 343 m·s⁻¹'],
      ['Sustitución', 'Δt = 6,8 m / 343 m·s⁻¹'],
      ['Resultado', 'Δt = 0,0198 s ≈ 19,8 ms'],
    ],
    interpretation: 'Es el retardo físico del ejemplo; no fija una frontera universal entre fusión y eco.',
  },
  'U07-105': {
    steps: [
      ['Datos', 'd = 0,180 m\nc = 343 m·s⁻¹'],
      ['Sustitución', '|Δtₗᵣ| ≈ 0,180 m / 343 m·s⁻¹'],
      ['Resultado', '5,25 × 10⁻⁴ s ≈ 525 µs'],
    ],
    interpretation: 'Es una cota del modelo rectilíneo; no incorpora dirección de llegada ni difracción alrededor de la cabeza.',
  },
};

function addWorkedExample(slide, d) {
  const model = WORKED_EXAMPLES[d.id];
  if (!model) return false;
  const xs = [70, 455, 840];
  addLine(slide, 400, 300, 455, 300, { color: C.berry2, width: 3, arrow: true, name: `${d.id}-step-1` });
  addLine(slide, 785, 300, 840, 300, { color: C.berry2, width: 3, arrow: true, name: `${d.id}-step-2` });
  model.steps.forEach(([title, body], i) => addPanel(slide, `${i + 1} · ${title}`, body, {
    x: xs[i], y: 190, w: 330, h: 220, kind: i === 2 ? 'clinical' : i === 1 ? 'accent' : 'physical',
    titleSize: 26, bodySize: body.length > 54 ? 24 : 27, name: `${d.id}-worked-${i + 1}`,
  }));
  addPanel(slide, 'Interpretación y límite', model.interpretation, {
    x: 150, y: 450, w: 980, h: 135, kind: 'neutral', titleSize: 26, bodySize: 24, name: `${d.id}-worked-limit`,
  });
  return true;
}

function addIsoCurveActivity(slide) {
  addLine(slide, 155, 540, 155, 195, { color: C.carbon, width: 3, arrow: true, name: 'iso-axis-y' });
  addLine(slide, 155, 540, 775, 540, { color: C.carbon, width: 3, arrow: true, name: 'iso-axis-x' });
  const pts = [[205,470],[285,395],[380,340],[485,315],[590,350],[700,430]];
  for (let i = 0; i < pts.length - 1; i += 1) addLine(slide, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], { color: C.berry2, width: 4, name: `iso-curve-${i}` });
  pts.forEach(([x,y], i) => addShape(slide, { geometry: 'ellipse', name: `iso-point-${i}`, x: x - 7, y: y - 7, w: 14, h: 14, fill: C.berry2, lineFill: C.white, lineWidth: 1 }));
  addText(slide, 'Nivel de presión sonora Lₚ (dB SPL)', { x: 15, y: 290, w: 240, h: 40, size: 22, color: C.carbon, bold: true, align: 'center', name: 'iso-y-label' });
  addText(slide, 'Frecuencia f (Hz, eje logarítmico)', { x: 325, y: 548, w: 360, h: 32, size: 22, color: C.carbon, bold: true, align: 'center', name: 'iso-x-label' });
  addText(slide, 'misma sonoridad', { x: 500, y: 282, w: 230, h: 34, size: 23, color: C.berry, bold: true, name: 'iso-curve-label' });
  addText(slide, 'Esquema cualitativo · no reproduce valores de ISO 226', { x: 190, y: 600, w: 560, h: 28, size: 18, color: '#5E6267', italic: true, align: 'center', name: 'iso-disclaimer' });
  addPanel(slide, 'Lectura guiada', '1. Nombre los ejes y sus unidades.\n\n2. Elija dos puntos de la misma curva.\n\n3. Compare sus Lₚ.\n\n4. Explique por qué igual sonoridad no exige igual nivel físico.\n\n5. Limite la conclusión a tarea y condiciones.', {
    x: 830, y: 175, w: 380, h: 410, kind: 'physical', titleSize: 29, bodySize: 23, name: 'iso-reading-guide',
  });
}

function addCorrectedDiagram(slide, d) {
  if (d.id === 'U07-030') { addIsoCurveActivity(slide); return true; }
  if (d.id === 'U07-074') {
    addLine(slide, 315, 290, 455, 290, { color: C.berry2, width: 3, arrow: true, name: 'voices-a' });
    addLine(slide, 825, 290, 965, 290, { color: C.berry2, width: 3, arrow: true, name: 'voices-b' });
    addPanel(slide, 'Escena física', 'Voz objetivo + voz competidora\n\nSolapamiento espectrotemporal', { x: 70, y: 190, w: 245, h: 230, kind: 'physical', titleSize: 27, bodySize: 24, name: 'voices-scene' });
    addPanel(slide, 'Entrada auditiva', 'La mezcla contiene energía y rasgos de ambas fuentes.', { x: 455, y: 190, w: 370, h: 230, kind: 'accent', titleSize: 27, bodySize: 25, name: 'voices-input' });
    addPanel(slide, 'Tarea y respuesta', 'Atender a la voz objetivo\n\nRegistrar qué se reconoce', { x: 965, y: 190, w: 245, h: 230, kind: 'clinical', titleSize: 27, bodySize: 24, name: 'voices-response' });
    addPanel(slide, 'Dos mecanismos que pueden coexistir', 'Energético: se reducen pistas periféricas.  ·  Informacional: cuesta seleccionar u organizar la fuente relevante.', { x: 180, y: 465, w: 920, h: 125, kind: 'neutral', titleSize: 25, bodySize: 24, name: 'voices-mechanisms' });
    return true;
  }
  if (d.id === 'U07-085') {
    addLine(slide, 330, 245, 480, 300, { color: C.teal, width: 3, arrow: true, name: 'noise-signal' });
    addLine(slide, 330, 420, 480, 330, { color: C.ochre, width: 3, arrow: true, name: 'reverb-signal' });
    addLine(slide, 800, 315, 945, 315, { color: C.berry2, width: 3, arrow: true, name: 'signal-task' });
    addPanel(slide, 'Ruido', 'Compite con la señal en frecuencia y tiempo.', { x: 70, y: 170, w: 260, h: 155, kind: 'physical', titleSize: 28, bodySize: 24, name: 'causal-noise' });
    addPanel(slide, 'Reverberación', 'Redistribuye energía y superpone segmentos.', { x: 70, y: 365, w: 260, h: 155, kind: 'clinical', titleSize: 28, bodySize: 24, name: 'causal-reverb' });
    addPanel(slide, 'Mezcla en el oído', 'Menor contraste entre pistas del habla; los efectos pueden interactuar.', { x: 480, y: 220, w: 320, h: 210, kind: 'accent', titleSize: 28, bodySize: 25, name: 'causal-mixture' });
    addPanel(slide, 'Tarea de reconocimiento', 'Respuesta: proporción de elementos identificados correctamente.', { x: 945, y: 220, w: 270, h: 210, kind: 'neutral', titleSize: 27, bodySize: 24, name: 'causal-response' });
    return true;
  }
  if (d.id === 'U07-103') {
    addLine(slide, 139, 345, 460, 345, { color: C.teal, width: 4, arrow: true, name: 'itd-short-path' });
    addLine(slide, 139, 370, 778, 370, { color: C.ochre, width: 4, arrow: true, name: 'itd-long-path' });
    addShape(slide, { geometry: 'ellipse', name: 'itd-head', x: 485, y: 205, w: 310, h: 310, fill: C.ivory, lineFill: C.berry, lineWidth: 3 });
    addShape(slide, { geometry: 'ellipse', name: 'itd-ear-left', x: 460, y: 325, w: 42, h: 72, fill: C.tealLight, lineFill: C.teal, lineWidth: 2 });
    addShape(slide, { geometry: 'ellipse', name: 'itd-ear-right', x: 778, y: 325, w: 42, h: 72, fill: C.ochreLight, lineFill: C.ochre, lineWidth: 2 });
    addShape(slide, { geometry: 'ellipse', name: 'itd-source', x: 85, y: 325, w: 54, h: 54, fill: C.berry2, lineFill: C.berry2, lineWidth: 1 });
    addText(slide, 'rL', { x: 285, y: 305, w: 70, h: 30, size: 24, color: C.teal, bold: true, align: 'center', name: 'itd-rL' });
    addText(slide, 'rR', { x: 435, y: 382, w: 70, h: 30, size: 24, color: C.ochre, bold: true, align: 'center', name: 'itd-rR' });
    addText(slide, 'd: separación efectiva', { x: 500, y: 525, w: 280, h: 32, size: 24, color: C.carbon, bold: true, align: 'center', name: 'itd-d' });
    addPanel(slide, 'Del recorrido al retardo', 'Δd = |rR − rL|\n\n|Δtₗᵣ| = Δd / c\n\nCota: |Δtₗᵣ| ≲ d / c', { x: 885, y: 230, w: 330, h: 270, kind: 'physical', titleSize: 26, bodySize: 23, name: 'itd-model' });
    return true;
  }
  if (d.id === 'U07-107') {
    addLine(slide, 640, 375, 255, 185, { color: C.gray, width: 3, name: 'cone-ray-a' });
    addLine(slide, 640, 375, 260, 555, { color: C.gray, width: 3, name: 'cone-ray-b' });
    addShape(slide, { geometry: 'ellipse', name: 'cone-head', x: 500, y: 235, w: 280, h: 280, fill: C.ivory, lineFill: C.berry, lineWidth: 3 });
    addShape(slide, { geometry: 'ellipse', name: 'cone-ear-left', x: 475, y: 330, w: 42, h: 70, fill: C.tealLight, lineFill: C.teal, lineWidth: 2 });
    addShape(slide, { geometry: 'ellipse', name: 'cone-ear-right', x: 763, y: 330, w: 42, h: 70, fill: C.tealLight, lineFill: C.teal, lineWidth: 2 });
    addShape(slide, { geometry: 'ellipse', name: 'cone-source-a', x: 220, y: 155, w: 54, h: 54, fill: C.berry2, lineFill: C.berry2, lineWidth: 1 });
    addShape(slide, { geometry: 'ellipse', name: 'cone-source-b', x: 225, y: 525, w: 54, h: 54, fill: C.berry2, lineFill: C.berry2, lineWidth: 1 });
    addText(slide, 'A', { x: 229, y: 165, w: 35, h: 30, size: 24, color: C.white, bold: true, align: 'center', name: 'cone-a' });
    addText(slide, 'B', { x: 234, y: 535, w: 35, h: 30, size: 24, color: C.white, bold: true, align: 'center', name: 'cone-b' });
    addPanel(slide, 'Ambigüedad binaural', 'A y B pueden producir ITD e ILD semejantes en una geometría idealizada.', { x: 865, y: 185, w: 345, h: 175, kind: 'accent', titleSize: 27, bodySize: 25, name: 'cone-ambiguity' });
    addPanel(slide, 'Cómo se reduce', 'Pistas espectrales del pabellón y movimiento de la cabeza aportan información adicional.', { x: 865, y: 400, w: 345, h: 175, kind: 'clinical', titleSize: 27, bodySize: 25, name: 'cone-resolution' });
    addText(slide, 'Corte 2D conceptual de una superficie de ambigüedad; no representa anatomía ni escala.', { x: 300, y: 610, w: 680, h: 28, size: 18, color: '#5E6267', italic: true, align: 'center', name: 'cone-disclaimer' });
    return true;
  }
  if (d.id === 'U07-117') {
    addLine(slide, 330, 275, 465, 315, { color: C.teal, width: 3, arrow: true, name: 'class-source' });
    addLine(slide, 330, 455, 465, 345, { color: C.ochre, width: 3, arrow: true, name: 'class-room' });
    addLine(slide, 815, 330, 955, 330, { color: C.berry2, width: 3, arrow: true, name: 'class-task' });
    addPanel(slide, 'Fuentes', 'Docente = objetivo\nOtras voces + ventilación = competidores', { x: 65, y: 185, w: 265, h: 180, kind: 'physical', titleSize: 28, bodySize: 24, name: 'class-sources' });
    addPanel(slide, 'Aula', 'Reflexiones y distancia modifican la mezcla física.', { x: 65, y: 405, w: 265, h: 155, kind: 'clinical', titleSize: 28, bodySize: 24, name: 'class-room' });
    addPanel(slide, 'Mezcla en los oídos', 'Habla objetivo + competidores + reverberación\n\nAquí convergen las rutas físicas.', { x: 465, y: 220, w: 350, h: 230, kind: 'accent', titleSize: 28, bodySize: 25, name: 'class-mixture' });
    addPanel(slide, 'Tarea y respuesta', 'Seguir instrucciones\n\nRegistrar comprensión, sin inferir diagnóstico.', { x: 955, y: 220, w: 260, h: 230, kind: 'neutral', titleSize: 27, bodySize: 24, name: 'class-response' });
    return true;
  }
  return false;
}

function addGeneric(slide, d) {
  const ideas = audienceIdeas(d.content, 6);
  const visibleContent = audienceText(d.content, 'Aplique la relación y explicite unidades, referencias y condiciones.');
  const isQuestion = /PREGUNTA|EJERCICIO/.test(d.layout);
  const isError = d.layout.includes('ERROR'); const isRecap = d.layout.includes('RECAP');
  const isCompare = d.layout.includes('COMPARACION'); const isEquation = d.layout.includes('ECUACION') || (d.equations && d.equations !== '—');
  if (isQuestion) {
    addPanel(slide, 'Consigna', visibleContent, { x: 72, y: 165, w: 755, h: 365, kind: 'accent', titleSize: 30, bodySize: visibleContent.length > 260 ? 25 : 29, name: 'question' });
    addPanel(slide, 'Para responder', d.example && d.example !== '—' ? audienceText(d.example, d.example) : 'Nombrá el objeto, identificá las magnitudes y justificá la relación causal.', { x: 865, y: 165, w: 345, h: 365, kind: 'physical', titleSize: 27, bodySize: 25, name: 'answer-guide' });
  } else if (isError) {
    addPanel(slide, 'Error frecuente', visibleContent, { x: 68, y: 165, w: 730, h: 390, kind: 'neutral', bodySize: 27, name: 'error' });
    const correction = hasMeaningfulText(d.definitions) ? audienceText(d.definitions, d.definitions)
      : hasMeaningfulText(d.example) ? audienceText(d.example, d.example)
        : '0 dB SPL es un nivel físico de referencia. El umbral auditivo depende de la frecuencia, la tarea, el procedimiento y la persona.';
    addPanel(slide, 'Corrección', correction, { x: 835, y: 165, w: 380, h: 390, kind: 'clinical', bodySize: 25, name: 'correction' });
  } else if (isCompare) {
    const mid = Math.ceil(Math.max(2, ideas.length) / 2);
    const labels = COMPARE_LABELS[d.id] || ['Situación A', 'Situación B'];
    addPanel(slide, labels[0], ideas.slice(0, mid).join('\n\n') || visibleContent, { x: 65, y: 160, w: 545, h: 395, kind: 'physical', bodySize: 26, name: 'compare-a' });
    addPanel(slide, labels[1], ideas.slice(mid).join('\n\n') || d.definitions || d.example, { x: 670, y: 160, w: 545, h: 395, kind: 'clinical', bodySize: 26, name: 'compare-b' });
  } else if (isRecap) {
    const chunks = ideas.length ? ideas : audienceIdeas(d.definitions || d.example, 5); const n = Math.max(1, chunks.length);
    const gap = n <= 4 ? 34 : 16; const w = Math.min(260, (1160 - gap * (n - 1)) / n); const total = n * w + (n - 1) * gap; let x = (1280 - total) / 2;
    chunks.forEach((t, i) => { addPanel(slide, String(i + 1).padStart(2, '0'), t, { x, y: 210, w, h: 285, kind: i % 3 === 2 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 25, bodySize: 24, name: `recap-${i + 1}` }); x += w + gap; });
  } else if (isEquation) {
    addEquation(slide, d.equations);
    const hasMeaning = hasMeaningfulText(d.definitions); const hasUse = hasMeaningfulText(d.example);
    if (!hasMeaning && !hasUse) addPanel(slide, 'Interpretación', EQUATION_USE[d.id] || visibleContent, { x: 170, y: 325, w: 940, h: 250, kind: 'physical', bodySize: 27, name: 'equation-interpretation' });
    else {
      addPanel(slide, 'Significado físico', hasMeaning ? audienceText(d.definitions, 'Las variables y unidades se definen en la ecuación y en el ejemplo.') : visibleContent, { x: 88, y: 325, w: 520, h: 250, kind: 'physical', bodySize: 25, name: 'equation-meaning' });
      addPanel(slide, 'Ejemplo o uso', EQUATION_USE[d.id] || (hasUse ? audienceText(d.example, d.example) : visibleContent), { x: 670, y: 325, w: 520, h: 250, kind: 'clinical', bodySize: 25, name: 'equation-use' });
    }
  } else if (d.layout.includes('PROCESO')) addProcess(slide, d);
  else if (d.layout.includes('MEDIA')) {
    addPanel(slide, 'Qué observar', visibleContent, { x: 75, y: 165, w: 750, h: 380, kind: 'physical', titleSize: 30, bodySize: 28, name: 'media-static' });
    addPanel(slide, 'Condición de escucha', hasMeaningfulText(d.example) ? audienceText(d.example, d.example) : 'Formule una predicción antes de escuchar y describa solo el cambio perceptual relevante. La escucha es cualitativa y no reemplaza una medición calibrada.', { x: 865, y: 165, w: 340, h: 380, kind: 'neutral', titleSize: 27, bodySize: 24, name: 'media-id' });
  } else {
    const bodySize = visibleContent.length > 330 ? 25 : visibleContent.length > 235 ? 27 : 29;
    const hasDefinition = hasMeaningfulText(d.definitions);
    const hasExample = hasMeaningfulText(d.example);
    addBulletList(slide, ideas.length ? ideas : [visibleContent], { x: 70, y: 160, w: hasDefinition || hasExample ? 710 : 1135, h: 405, size: bodySize, name: 'main-ideas' });
    if (hasDefinition || hasExample) {
      const sideTitle = hasDefinition ? 'Definición' : 'Ejemplo';
      const sideBody = hasDefinition ? d.definitions : audienceText(d.example, d.example);
      addPanel(slide, sideTitle, sideBody, { x: 830, y: 170, w: 375, h: 350, kind: /clín|fono|audit|voz/i.test(`${d.title} ${d.content}`) ? 'clinical' : 'physical', bodySize: 25, name: 'side-panel' });
    }
  }
}

function addResolvedSourceSlide(slide, d) {
  if (d.id === 'U07-057') {
    addPanel(slide, 'Pilar interno', 'Límite medial', { x: 80, y: 215, w: 285, h: 205, kind: 'physical', bodySize: 30, name: 'tunnel-inner' });
    addPanel(slide, 'Túnel de Corti', 'Espacio triangular lleno de fluido', { x: 410, y: 185, w: 460, h: 265, kind: 'accent', bodySize: 30, name: 'tunnel-space' });
    addPanel(slide, 'Pilar externo', 'Límite lateral', { x: 915, y: 215, w: 285, h: 205, kind: 'clinical', bodySize: 30, name: 'tunnel-outer' });
    addPanel(slide, 'Membrana basilar', 'La zona arcuata completa el límite inferior', { x: 250, y: 485, w: 780, h: 100, kind: 'neutral', titleSize: 28, bodySize: 25, name: 'tunnel-base' });
    return true;
  }
  if (d.id === 'U07-085') {
    addPanel(slide, 'Potencial de reposo', 'Condición eléctrica basal de la membrana, medida respecto de una referencia extracelular declarada.', { x: 80, y: 175, w: 520, h: 330, kind: 'neutral', titleSize: 31, bodySize: 29, name: 'resting' });
    addPanel(slide, 'Potencial receptor', 'Cambio graduado respecto del estado basal cuando la deflexión modifica la corriente iónica.', { x: 680, y: 175, w: 520, h: 330, kind: 'accent', titleSize: 31, bodySize: 29, name: 'receptor' });
    addText(slide, 'La referencia de medida importa; aquí no se fija un valor universal.', { x: 190, y: 535, w: 900, h: 42, size: 29, color: C.berry, bold: true, align: 'center', name: 'resting-caution' });
    return true;
  }
  if (d.id === 'U07-096') {
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
  if (d.id === 'U07-115') {
    addPanel(slide, 'Umbral', 'Depende del estímulo, el método y la persona; no es una constante universal.', { x: 75, y: 160, w: 530, h: 185, kind: 'physical', titleSize: 29, bodySize: 26, name: 'reflex-threshold' });
    addPanel(slide, 'Latencia', 'Disminuye al aumentar el nivel por encima del umbral, pero la respuesta muscular no es instantánea.', { x: 675, y: 160, w: 530, h: 185, kind: 'accent', titleSize: 29, bodySize: 26, name: 'reflex-latency' });
    addPanel(slide, 'Impulsos breves', 'El comienzo del impulso puede preceder a la contracción: no hay protección inicial garantizada.', { x: 75, y: 380, w: 530, h: 185, kind: 'clinical', titleSize: 29, bodySize: 26, name: 'reflex-impulse' });
    addPanel(slide, 'Interpretación', 'Una medición del reflejo informa sobre varias partes del sistema; no identifica por sí sola una etiología.', { x: 675, y: 380, w: 530, h: 185, kind: 'neutral', titleSize: 29, bodySize: 26, name: 'reflex-interpretation' });
    return true;
  }
  if (d.id === 'U07-116') {
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
  const explicit = [...d.visual.matchAll(/U07-(?:CH|DG)-\d{3}[A-Z]?/g)].map((m) => m[0]);
  for (const id of explicit) if (byId.has(id)) return byId.get(id);
  return undefined;
}

function addNotes(slide, d, note, asset) {
  const lines = [`- Fuentes de contenido: ${d.source || 'Programa oficial y libro del curso.'}`];
  if (asset) lines.push(`- Asset propio aprobado: ${asset.asset_id}.`);
  const normalizedNote = String(note || '')
    .replace(/^\s*- \*\*\[Sources\]:\*\*.*$/gm, '')
    .replace(/^\s*\[Sources\][\s\S]*$/gm, '')
    .replace(/\n{3,}/g, '\n\n').trim();
  const full = `${normalizedNote}\n\n[Alt text]\n${d.alt || 'Contenido textual editable de la diapositiva.'}\n\n[Sources]\n${lines.join('\n')}`.trim();
  slide.speakerNotes.clear(); slide.speakerNotes.textFrame.setText(full); slide.speakerNotes.setVisible(true);
}

const slidesData = parseSlideText(await fs.readFile(path.join(UNIT, 'slide_text.md'), 'utf8'));
const notes = parseNotes(await fs.readFile(path.join(UNIT, 'speaker_notes.md'), 'utf8'));
const manifest = parseCsv(await fs.readFile(path.join(UNIT, 'asset_manifest.csv'), 'utf8'));
const approved = manifest.filter((a) => a.status === 'approved' && ['chart', 'diagram'].includes(a.type) && a.local_path);
const byId = new Map(approved.map((a) => [a.asset_id, a]));
if (slidesData.length !== 134 || notes.size !== 134) throw new Error(`Conteos incompatibles: slides=${slidesData.length}, notas=${notes.size}.`);

const deck = await PresentationFile.importPptx(await FileBlob.load(STARTER));
const slides = [...deck.slides.items];
if (slides.length !== 134) throw new Error(`El starter debe tener 134 slides; tiene ${slides.length}.`);
const log = [];
for (let i = 0; i < slides.length; i += 1) {
  const slide = slides[i]; const d = slidesData[i]; await clearSlide(slide);
  const dark = ['FA_00_PORTADA', 'FA_01_DIVISOR', 'FA_21_CIERRE_PUENTE'].includes(d.layout);
  slide.background.fill = dark ? C.berry : C.white;
  if (d.layout === 'FA_00_PORTADA') {
    addText(slide, 'UNIDAD 7 · FÍSICA ACÚSTICA', { x: 64, y: 42, w: 560, h: 28, size: 18, color: C.white, bold: true, name: 'cover-eyebrow' });
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
    addText(slide, `UNIDAD 7 · ${route.session} · ${route.route}`, { x: 55, y: 24, w: 520, h: 24, size: 16, color: '#E1C8D4', bold: true, name: 'dark-eyebrow' });
    addText(slide, d.title, { x: 80, y: 225, w: 1120, h: 115, size: 54, color: C.white, font: 'Calibri Light', align: 'center', valign: 'middle', name: 'divider-title' });
    addText(slide, d.subtitle, { x: 165, y: 370, w: 950, h: 65, size: 28, color: '#E6D5DD', align: 'center', name: 'divider-subtitle' });
  } else {
    const asset = BLOCKED.has(d.id) ? undefined : assetForSlide(d, approved, byId);
    const customIds = new Set(['U07-024', 'U07-030', 'U07-051', 'U07-058', 'U07-074', 'U07-081', 'U07-085', 'U07-091', 'U07-103', 'U07-105', 'U07-107', 'U07-117']);
    const custom = customIds.has(d.id);
    if (asset?.type === 'diagram' && !custom) await addDiagram(slide, d, asset);
    else {
      addTitle(slide, d);
      if (BLOCKED.has(d.id)) addBlocked(slide, d);
      else if (addWorkedExample(slide, d)) { /* ejemplo de tres pasos visible */ }
      else if (addCorrectedDiagram(slide, d)) { /* diagrama causal/geometría editable */ }
      else if (asset?.type === 'chart') await addChart(slide, d, asset);
      else addGeneric(slide, d);
      addCaption(slide, d, asset);
    }
    addTopRail(slide, d);
    addPageNumber(slide, i + 1, false);
    addNotes(slide, d, notes.get(d.id), custom ? undefined : asset);
    log.push({ slide: i + 1, id: d.id, layout: d.layout, asset: asset?.asset_id || null, custom, blocked: BLOCKED.has(d.id) });
    continue;
  }
  addPageNumber(slide, i + 1, dark);
  addNotes(slide, d, notes.get(d.id), undefined);
  log.push({ slide: i + 1, id: d.id, layout: d.layout, asset: null, blocked: false });
}

const pptx = await PresentationFile.exportPptx(deck); await pptx.save(OUT);
const altScript = path.join(UNIT, 'scripts', 'u07_add_alt_text.ps1');
const altResult = spawnSync('powershell.exe', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', altScript,
  '-PptxPath', OUT, '-SlideTextPath', path.join(UNIT, 'slide_text.md')], { encoding: 'utf8' });
if (altResult.status !== 0) throw new Error(`No se pudo aplicar texto alternativo: ${altResult.stderr || altResult.stdout}`);
const inspect = await deck.inspect({ kind: 'deck,slide,textbox,shape,image,chart,table,notes,layout', include: 'id,slide,name,title,text,textPreview,textChars,bbox,bboxUnit,isPlaceholder,alt', maxChars: 2_000_000 });
await fs.writeFile(path.join(QA, 'final-inspect.ndjson'), inspect.ndjson, 'utf8');
await fs.writeFile(path.join(QA, 'build-log.json'), `${JSON.stringify({ output: OUT, slides: log, approvedAssetCount: approved.length }, null, 2)}\n`, 'utf8');
console.log(JSON.stringify({ output: OUT, slides: log.length, assetsInserted: log.filter((x) => x.asset).length, blocked: log.filter((x) => x.blocked).length }, null, 2));
