import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

const [rootArg, starterArg, outArg, qaDirArg] = process.argv.slice(2);
const workspace = process.env.U08_ARTIFACT_WORKSPACE;
if (!rootArg || !starterArg || !outArg || !workspace) {
  throw new Error('Uso: U08_ARTIFACT_WORKSPACE=<workspace> node u08_build_presentation.mjs <repoRoot> <starter.pptx> <out.pptx> [qaDir]');
}
const req = createRequire(path.join(workspace, 'package.json'));
const entry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(entry).href);
const runtimeReq = createRequire(entry);
const JSZip = runtimeReq('jszip');

const ROOT = path.resolve(rootArg);
const UNIT = path.join(ROOT, 'units/unit_08');
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
const EXCLUDED_ASSETS = new Set([
  'U08-DG-021', 'U08-DG-038', 'U08-DG-047', 'U08-DG-048',
  'U08-DG-049', 'U08-DG-051', 'U08-DG-042',
  'U08-CH-011',
]);
const REVERSE_BRANCHES = new Set();
const REMOVE_EDGES = new Set();
const COMPLEMENTARY = new Set([
  'U08-015', 'U08-016', 'U08-017', 'U08-026', 'U08-036', 'U08-040',
  'U08-042', 'U08-061', 'U08-062', 'U08-063', 'U08-064', 'U08-071',
  'U08-074', 'U08-092', 'U08-105', 'U08-108', 'U08-115', 'U08-116',
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
  const re = /^## (U08-\d{3})[^\n]*$/gm;
  const matches = [...md.matchAll(re)];
  return matches.map((m, i) => {
    const block = md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length);
    const fields = {}; const rawFields = {};
    const fieldMatches = [...block.matchAll(/^- \*\*([^*]+):\*\*\s*(.*)$/gm)];
    fieldMatches.forEach((fm, index) => {
      const value = fm[2].trim();
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
    const section = (name, next) => {
      const rx = new RegExp(`### ${name}\\s*\\n([\\s\\S]*?)(?=\\n### (?:${next})\\s*\\n|$)`, 'i');
      return block.match(rx)?.[1]?.trim() || '';
    };
    const content = section('Contenido visible', 'Ecuaciones').split(/\r?\n/)
      .filter((line) => /^-\s+/.test(line)).map((line) => line.replace(/^-\s+/, '')).join('\n');
    const equations = section('Ecuaciones', 'Definición').replace(/\*\*Símbolos y unidades:\*\*[\s\S]*/i, '').trim();
    const stateRaw = pick('estado');
    return {
      id: m[1], title: pick('título'), state: /respaldo/i.test(stateRaw) ? 'respaldo' : /complementaria/i.test(stateRaw) ? 'ampliación' : 'ruta central',
      subtitle: pick('subtítulo'), content: clean(content), equations: clean(equations),
      definitions: clean(section('Definición', 'Ejemplo')), example: clean(section('Ejemplo', 'Visual')), caption: clean(section('Caption sugerido', 'Fuente')),
      visual: clean(section('Visual', 'Caption sugerido')), layout: String(rawFields.layout || '').replace(/[`\.\s]/g, ''), source: clean(section('Fuente', 'Texto alternativo')),
      alt: clean(section('Texto alternativo', '(?!)')), raw: block,
    };
  });
}

function parseNotes(md) {
  const re = /^## (U08-\d{3})[^\n]*$/gm;
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
  /^no corresponde una definici[oó]n nueva/i,
  /speaker_notes\.md/i,
  /^caso breve con/i,
  /^tres columnas breves/i,
  /^bater[ií]a necesaria$/i,
  /^cinco categor[ií]as, un ejemplo/i,
  /^tres afirmaciones y una pregunta/i,
  /^seis preguntas, un ejemplo/i,
  /^audiograma conceptual con/i,
  /^nivel de presentaci[oó]n frente/i,
  /^cm, sp y ap desarrollados/i,
  /^antes de concluir:/i,
  /^actividad o ejercicio/i,
];

function audienceIdeas(text, max = 6) {
  const parts = splitIdeas(text, Math.max(max * 2, 8))
    .map((part) => part.replace(/^[-–•]\s*/, '').trim())
    .filter((part) => part && !/^\d+[.)]?$/.test(part) && !INTERNAL_COPY.some((pattern) => pattern.test(part)));
  if (parts.length > max) return [...parts.slice(0, max - 1), parts.slice(max - 1).join(' ')];
  return parts;
}

function audienceText(text, fallback = '') {
  const ideas = audienceIdeas(text, 6);
  return ideas.length ? ideas.join('\n\n') : fallback;
}

const COMPARE_LABELS = {
  'U08-014': ['TTS: medición', 'Tinnitus: percepción'],
  'U08-025': ['Temporal', 'Permanente'],
  'U08-031': ['Trauma acústico', 'Ototoxicidad'],
  'U08-040': ['Prueba conductual', 'Prueba fisiológica'],
  'U08-060': ['Audiometría tonal', 'Logoaudiometría'],
  'U08-062': ['Señal externa', 'Correspondencia perceptual'],
  'U08-092': ['Audífono', 'Implante coclear'],
  'U08-093': ['Conducción ósea', 'Estimulación electroacústica'],
};

const EQUATION_USE = {
  'U08-020': 'Un valor positivo indica que en la segunda medición se necesitó un nivel de audición mayor. No identifica por sí solo mecanismo, permanencia ni significación clínica.',
  'U08-051': 'LVA y LVO deben estar expresados en dB HL, a la misma frecuencia y bajo condiciones comparables. La diferencia se informa en dB y no nombra una enfermedad.',
  'U08-063': 'dB SL es una diferencia respecto de un umbral individual declarado; no mide una fuente sonora interna ni cuantifica impacto funcional.',
  'U08-087': 'Entrada y salida sólo pueden restarse si comparten referencia y condición de medida. La ganancia no equivale a beneficio comunicativo.',
};

const ERROR_CORRECTIONS = {
  'U08-013': 'La forma de un audiograma o timpanograma es un resultado. Para atribuir una causa hacen falta historia, condiciones de medición y evidencia complementaria.',
  'U08-058': 'El porcentaje debe acompañarse de material, idioma, modo y nivel de presentación, escala, oído, consigna y criterio de puntuación.',
  'U08-071': 'Un timpanograma plano describe la respuesta de inmitancia durante el barrido. No informa por sí solo cuánto oye la persona ni identifica una patología.',
  'U08-076': 'Una OEA presente aporta información sobre una respuesta coclear bajo el protocolo. No demuestra audición normal ni evalúa por sí sola vía neural, percepción o lenguaje.',
  'U08-079': 'El PEAT registra una respuesta bioeléctrica sincronizada; la comprensión del habla requiere una tarea conductual y otras condiciones de evaluación.',
  'U08-091': 'La cantidad de electrodos no coincide necesariamente con canales funcionales ni con perceptos independientes: intervienen interacción eléctrica, programación y sistema neural.',
};

const QUESTION_GUIDES = {
  'U08-003': ['Clasifique el dato', 'Nombre magnitud y unidad', 'Declare qué queda abierto'],
  'U08-011': ['Separe seis datos', 'Justifique la categoría', 'Evite inferir una causa'],
  'U08-024': ['Lea ejes y tiempos', 'Describa la tendencia', 'No prediga recuperación'],
  'U08-036': ['Defina población y caso', 'Identifique exposición y período', 'No individualice el porcentaje'],
  'U08-050': ['Lea frecuencia, vía y valor', 'Compare la misma frecuencia', 'No nombre una enfermedad'],
  'U08-059': ['Liste metadatos faltantes', 'Declare escala y oído', 'Limite el porcentaje a la prueba'],
  'U08-070': ['Describa eje y unidad', 'Ubique pico o trazado', 'No asigne patología'],
  'U08-083': ['Compare magnitudes', 'Revise sensores y condiciones', 'Proponga una pregunta nueva'],
  'U08-097': ['Una pregunta por prueba', 'Magnitud y unidad esperadas', 'Límite de cada resultado'],
  'U08-099': ['Identifique la salida física', 'Nombre su magnitud', 'No indique sólo por la cadena'],
};

function slideRefMatches(ref, id) {
  const target = Number(id.slice(-3));
  for (const token of String(ref || '').split(/[;,]/).map((x) => x.trim())) {
    const exact = token.match(/^U08-(\d{3})$/); if (exact && Number(exact[1]) === target) return true;
    const range = token.match(/^U08-(\d{3})[–-](?:U08-)?(\d{3})$/);
    if (range && target >= Number(range[1]) && target <= Number(range[2])) return true;
  }
  return false;
}

function hasMeaningfulText(value) {
  const normalized = clean(value);
  return Boolean(normalized && !/^—/.test(normalized) && !/^No corresponde\b/i.test(normalized));
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
  const forceCompact = ['U08-075', 'U08-111'].includes(d.id);
  const titleY = d.id === 'U08-111' ? 63 : 43;
  addText(slide, d.title, { x: 52, y: titleY, w: 1172, h: long ? 88 : 72, size: d.id === 'U08-111' ? 32 : forceCompact ? 34 : veryLong ? 31 : long ? 34 : 40,
    color, bold: false, font: 'Calibri Light', name: 'slide-title', insets: { top: 0, right: 3, bottom: 0, left: 3 } });
  // Un título de dos líneas ya cumple la función orientadora; no se agrega un
  // subtítulo redundante en el mismo corredor vertical.
  if (!long && hasMeaningfulText(d.subtitle)) addText(slide, d.subtitle, { x: 55, y: 108, w: 1150, h: 31,
    size: 23, color: dark ? '#E4D8DF' : '#5E6267', name: 'slide-subtitle', insets: { top: 0, right: 3, bottom: 0, left: 3 } });
}

function addTopRail(slide, d) {
  const route = teachingRoute(d);
  addShape(slide, { geometry: 'rect', name: 'top-rail-1', x: 65, y: 27, w: 384, h: 5, fill: C.berry, lineFill: C.berry, lineWidth: 0 });
  addShape(slide, { geometry: 'rect', name: 'top-rail-2', x: 459, y: 27, w: 384, h: 5, fill: C.berry2, lineFill: C.berry2, lineWidth: 0 });
  addShape(slide, { geometry: 'rect', name: 'top-rail-3', x: 853, y: 27, w: 363, h: 5, fill: C.gray, lineFill: C.gray, lineWidth: 0 });
  addText(slide, `UNIDAD 8 · ${route.session} · ${route.route}`, { x: 50, y: 2, w: 520, h: 24, size: 14,
    color: C.berry2, bold: true, name: 'eyebrow', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
}

function addPageNumber(slide, page, dark = false) {
  addText(slide, String(page), { x: 1180, y: 676, w: 38, h: 18, size: 13,
    color: dark ? '#E1C8D4' : C.gray, align: 'right', name: 'slide-number', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
}

function addCaption(slide, d, asset) {
  if (!asset) return;
  let caption = d.caption && d.caption !== '—' ? d.caption : '';
  caption = caption.replace(/^(?:Esquema|Figura|Lectura) conceptual,?\s*(?:no a escala\.)?\s*/i, '');
  if (caption.length > 120) caption = `${caption.slice(0, 117).replace(/[\s,;:.]+$/, '')}…`;
  const credit = `Producción propia UCASAL · ${asset.asset_id}`;
  const visible = caption ? `${caption}  ·  ${credit}` : credit;
  addText(slide, visible, { x: 70, y: 630, w: 1140, h: 26, size: 14,
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
  addShape(slide, { geometry: 'rect', name: 'scala-vestibuli', x: x + 4, y: 160, w: w - 8, h: 104, fill: C.tealLight, lineFill: 'none' });
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
  if (d.id === 'U08-013') { addCaeComparison(slide); return true; }
  if (d.id === 'U08-033') { addLeverVisual(slide); return true; }
  if (d.id === 'U08-051') { addCochleaLongitudinal(slide); return true; }
  if (d.id === 'U08-052') { addCochleaCrossSection(slide, 1); return true; }
  if (d.id === 'U08-053') { addCochleaCrossSection(slide, 2); return true; }
  if (d.id === 'U08-054') { addCochleaCrossSection(slide, 3); return true; }
  if (['U08-055','U08-056','U08-073'].includes(d.id)) { addCochleaCrossSection(slide, 4); return true; }
  if (d.id === 'U08-057') { addTunnelVisual(slide); return true; }
  if (d.id === 'U08-074') { addMovementStates(slide); return true; }
  if (d.id === 'U08-075') { addBundleStates(slide); return true; }
  if (d.id === 'U08-079') { addGeneric(slide, { ...d, visual: '', layout: 'FA_14_PREGUNTA_EJERCICIO' }); return true; }
  if (d.id === 'U08-083') { addDomainsMap(slide); return true; }
  if (d.id === 'U08-084') { addEndocochlearMap(slide); return true; }
  if (d.id === 'U08-101') { addMeasurementChain(slide); return true; }
  if (d.id === 'U08-111') { addResolvedG3(slide); return true; }
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

function addFlow(slide, items, { y = 225, h = 205, x = 55, width = 1170, gap = 18, name = 'flow' } = {}) {
  const n = items.length;
  const w = (width - gap * (n - 1)) / n;
  const anchors = items.map((_, i) => addShape(slide, {
    geometry: 'roundRect', name: `${name}-anchor-${i + 1}`, x: x + i * (w + gap), y, w, h,
    fill: 'none', lineFill: 'none', lineWidth: 0, radius: 12,
  }));
  for (let i = 0; i < anchors.length - 1; i += 1) {
    slide.shapes.connect(anchors[i], anchors[i + 1], {
      kind: 'straight', fromSide: 'right', toSide: 'left',
      line: { style: 'solid', fill: C.berry2, width: 2.5 },
      tail: { type: 'arrow', width: 'med', length: 'med' },
    });
  }
  items.forEach((item, i) => {
    const [title, body, kind = (i === n - 1 ? 'clinical' : i % 2 ? 'neutral' : 'physical')] = item;
    addPanel(slide, title, body, {
      x: x + i * (w + gap), y, w, h, kind,
      titleSize: n >= 5 ? 23 : 26, bodySize: n >= 5 ? 22 : 24, name: `${name}-${i + 1}`,
    });
  });
}

function addGridTable(slide, rows, widths, { x = 55, y = 165, w = 1170, rowH = 58, name = 'table', bodySize = 21 } = {}) {
  const totalWeight = widths.reduce((a, b) => a + b, 0);
  let yy = y;
  rows.forEach((row, r) => {
    let xx = x;
    row.forEach((value, c) => {
      const cw = w * widths[c] / totalWeight;
      const header = r === 0;
      addShape(slide, { geometry: 'rect', name: `${name}-${r}-${c}-box`, x: xx, y: yy, w: cw, h: rowH,
        fill: header ? C.berry : (r % 2 ? C.ivory : C.white), lineFill: header ? C.berry : C.lightGray, lineWidth: 1.2 });
      addText(slide, value, { x: xx + 8, y: yy + 6, w: cw - 16, h: rowH - 12, size: header ? bodySize + 1 : bodySize,
        color: header ? C.white : C.carbon, bold: header || c === 0, valign: 'middle', name: `${name}-${r}-${c}-text`,
        insets: { top: 0, right: 0, bottom: 0, left: 0 } });
      xx += cw;
    });
    yy += rowH;
  });
}

function addQuestionSlide(slide, d) {
  const prompt = audienceIdeas(d.content, 4).map((x) => x.replace(/^Consigna:\s*/i, '')).join('\n\n');
  const guide = QUESTION_GUIDES[d.id] || ['Identifique el dato', 'Declare magnitud y unidad', 'Justifique el límite'];
  addPanel(slide, 'Consigna', prompt, {
    x: 65, y: 165, w: 690, h: 370, kind: 'accent', titleSize: 30,
    bodySize: prompt.length > 230 ? 25 : 28, name: `${d.id}-question`,
  });
  guide.forEach((text, i) => addPanel(slide, `${i + 1}`, text, {
    x: 800, y: 165 + i * 128, w: 410, h: 104, kind: i === 2 ? 'clinical' : i === 1 ? 'neutral' : 'physical',
    titleSize: 23, bodySize: 23, name: `${d.id}-guide-${i + 1}`,
  }));
}

function addExerciseSlide(slide, d) {
  const configs = {
    'U08-107': {
      rows: [['f (Hz)', '500', '1000', '4000'], ['Lᵤ,₀ (dB HL)', '10', '15', '20'], ['Lᵤ,₁ (dB HL)', '16', '28', '31']],
      equation: 'ΔLₜ(f) = Lᵤ,₁(f) − Lᵤ,₀(f)',
      prompt: 'Calcule ΔLₜ en cada frecuencia, identifique la mayor diferencia y explique qué no permite concluir.',
    },
    'U08-108': {
      rows: [['Dato', 'Valor'], ['Exposición', '96 dB(A) durante 0,5 h'], ['Intervalo de referencia', '8 h'], ['Resto del intervalo', 'contribución despreciable']],
      equation: 'L_Aeq,8h = 96 dB(A) + 10 log₁₀(0,5 h / 8 h)',
      prompt: 'Normalice a 8 h, redondee a una cifra decimal y declare las hipótesis del cálculo.',
    },
    'U08-109': {
      rows: [['f (Hz)', '500', '1000', '4000'], ['LVA (dB HL)', '25', '40', '55'], ['LVO (dB HL)', '10', '15', '30']],
      equation: 'G_AO(f) = LVA(f) − LVO(f)',
      prompt: 'Calcule la diferencia en cada frecuencia e identifique si existe una única diferencia máxima.',
    },
  };
  const cfg = configs[d.id];
  if (!cfg) return false;
  addGridTable(slide, cfg.rows, Array(cfg.rows[0].length).fill(1), {
    x: 60, y: 170, w: 650, rowH: cfg.rows.length === 4 ? 72 : 82, name: `${d.id}-data`, bodySize: 22,
  });
  addPanel(slide, 'Consigna', cfg.prompt, { x: 760, y: 170, w: 455, h: 245, kind: 'accent', titleSize: 28, bodySize: 25, name: `${d.id}-prompt` });
  addEquation(slide, cfg.equation, { x: 110, y: 475, w: 1060, h: 95 });
  return true;
}

function addMapSlide(slide, d) {
  const maps = {
    'U08-004': [
      ['U4', 'Niveles y referencias'], ['U5', 'Señal, sistema y L_Aeq,T'], ['U6', 'Vías y transducción'], ['U7', 'Umbral y tarea perceptual'],
    ],
    'U08-007': [
      ['Encuentro 1', 'Datos, exposición y alteraciones'], ['Encuentro 2', 'Pruebas conductuales y oído medio'],
      ['Encuentro 3', 'OEA, PEAT, ECoG y dispositivos'], ['Encuentro 4', 'Integración, práctica y transferencia'],
    ],
    'U08-039': [
      ['1', 'Estímulo'], ['2', 'Sistema o función'], ['3', 'Sensor o tarea'], ['4', 'Magnitud y unidad'], ['5', 'Resultado'], ['6', 'Límite'],
    ],
    'U08-103': [
      ['Escalas', 'U08-104'], ['Estudios', 'U08-105'], ['Dispositivos', 'U08-106'], ['Ejercicios', 'U08-107–110'], ['Fuentes', 'U08-111–114'],
    ],
  };
  const items = maps[d.id];
  if (!items) return false;
  if (items.length <= 5) addFlow(slide, items, { y: 225, h: 210, gap: 20, name: `${d.id}-map` });
  else {
    const w = 350; const gap = 35;
    items.forEach(([title, body], i) => addPanel(slide, title, body, {
      x: 70 + (i % 3) * (w + gap), y: 175 + Math.floor(i / 3) * 210, w, h: 170,
      kind: i % 3 === 2 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 26, bodySize: 24, name: `${d.id}-map-${i + 1}`,
    }));
  }
  return true;
}

function addEquation(slide, eq, { x = 135, y = 182, w = 1010, h = 105 } = {}) {
  if (!hasMeaningfulText(eq)) return;
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
  const folder = path.resolve(ROOT, asset.local_path.replace(/[\\/]/g, path.sep));
  const model = JSON.parse(await fs.readFile(path.join(folder, 'diagram_source.json'), 'utf8'));
  // El export PPTX editable de algunos conectores no conserva de manera
  // uniforme la primera flecha ni todas las ramas. Se inserta el PNG final de
  // 2560×1440, validado junto con el SVG, y se recortan solo título y footer
  // del asset. Título, rail, footer, numeración y notas siguen editables.
  const pngPath = path.join(workspace, 'diagram_crops', `${asset.asset_id}.png`);
  await fs.access(pngPath);
  const fileBytes = await fs.readFile(pngPath);
  const bytes = fileBytes.buffer.slice(fileBytes.byteOffset, fileBytes.byteOffset + fileBytes.byteLength);
  const image = slide.images.add({ blob: bytes, contentType: 'image/png', alt: d.alt || model.alt || asset.description,
    fit: 'contain', position: { left: 55, top: 135, width: 1170, height: 475 } });
  image.name = `${d.id}-${asset.asset_id}-validated-png`;
  image.alt = d.alt || model.alt || asset.description;
  addText(slide, d.title, { x: 64, y: 44, w: 1150, h: 48, size: d.title.length > 70 ? 32 : 40,
    color: C.carbon, font: 'Calibri Light', name: 'diagram-title', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  // Los avisos repetitivos y los códigos de producción quedan en notas y
  // manifiesto. El área proyectada se reserva para el diagrama y su lectura.
  return model;
}

async function addChart(slide, d, asset) {
  const folder = path.resolve(ROOT, asset.local_path.replace(/[\\/]/g, path.sep));
  const files = await fs.readdir(folder);
  const visualName = files.find((name) => /\.svg$/i.test(name)) || files.find((name) => /\.png$/i.test(name) && !/preview/i.test(name));
  if (!visualName) throw new Error(`No se encontró visual validado para ${asset.asset_id}`);
  const assetPath = path.join(folder, visualName);
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
  const steps = audienceIdeas(d.content, 6).map((s) => s.replace(/^\d+[.)]\s*/, ''));
  const items = (steps.length ? steps : ['Entrada controlada', 'Respuesta registrada']).map((step, i) => [String(i + 1), step]);
  addFlow(slide, items, { y: 220, h: 210, gap: items.length >= 5 ? 14 : 24, name: `${d.id}-process` });
  if (d.equations && d.equations !== '—') addEquation(slide, d.equations, { x: 220, y: 455, w: 840, h: 90 });
}

const WORKED_EXAMPLES = {
  'U08-024': {
    steps: [
      ['Datos comparables', 'Campo: 50 dB SPL\nTímpano: 58 dB SPL'],
      ['Sustitución', 'G꜀ₜ = 58 dB SPL − 50 dB SPL'],
      ['Resultado', 'G꜀ₜ = 8 dB'],
    ],
    interpretation: 'Es una diferencia entre dos posiciones para la misma frecuencia; no es una ganancia fija de sonoridad.',
  },
  'U08-051': {
    steps: [
      ['Dato', 'Lₙ = 70 fon'],
      ['Sustitución', 'Nₛₒₙ = 2^[(70 − 40)/10] son'],
      ['Resultado', 'Nₛₒₙ = 2³ son = 8 sones'],
    ],
    interpretation: 'Ocho sones expresan ocho veces la referencia de 1 son dentro del modelo; no son 8 dB SPL.',
  },
  'U08-058': {
    steps: [
      ['Datos comparables', 'Quietud: 10 dB SPL\nCon enmascarador: 35 dB SPL'],
      ['Sustitución', 'M = 35 dB SPL − 10 dB SPL'],
      ['Resultado', 'M = 25 dB'],
    ],
    interpretation: 'El umbral se elevó 25 dB bajo esas condiciones; no informa por sí solo el nivel del enmascarador.',
  },
  'U08-081': {
    steps: [
      ['Datos comparables', 'Voz: 68 dB SPL\nRuido: 60 dB SPL'],
      ['Sustitución', 'SNR = 68 dB SPL − 60 dB SPL'],
      ['Resultado', 'SNR = +8 dB'],
    ],
    interpretation: 'El signo positivo indica mayor nivel de voz. La SNR sola no predice inteligibilidad: faltan tarea, oyente y reverberación.',
  },
  'U08-091': {
    steps: [
      ['Datos', 'Δd = 6,8 m\nc = 343 m·s⁻¹'],
      ['Sustitución', 'Δt = 6,8 m / 343 m·s⁻¹'],
      ['Resultado', 'Δt = 0,0198 s ≈ 19,8 ms'],
    ],
    interpretation: 'Es el retardo físico del ejemplo; no fija una frontera universal entre fusión y eco.',
  },
  'U08-105': {
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
  if (d.id === 'U08-030') { addIsoCurveActivity(slide); return true; }
  if (d.id === 'U08-074') {
    addLine(slide, 315, 290, 455, 290, { color: C.berry2, width: 3, arrow: true, name: 'voices-a' });
    addLine(slide, 825, 290, 965, 290, { color: C.berry2, width: 3, arrow: true, name: 'voices-b' });
    addPanel(slide, 'Escena física', 'Voz objetivo + voz competidora\n\nSolapamiento espectrotemporal', { x: 70, y: 190, w: 245, h: 230, kind: 'physical', titleSize: 27, bodySize: 24, name: 'voices-scene' });
    addPanel(slide, 'Entrada auditiva', 'La mezcla contiene energía y rasgos de ambas fuentes.', { x: 455, y: 190, w: 370, h: 230, kind: 'accent', titleSize: 27, bodySize: 25, name: 'voices-input' });
    addPanel(slide, 'Tarea y respuesta', 'Atender a la voz objetivo\n\nRegistrar qué se reconoce', { x: 965, y: 190, w: 245, h: 230, kind: 'clinical', titleSize: 27, bodySize: 24, name: 'voices-response' });
    addPanel(slide, 'Dos mecanismos que pueden coexistir', 'Energético: se reducen pistas periféricas.  ·  Informacional: cuesta seleccionar u organizar la fuente relevante.', { x: 180, y: 465, w: 920, h: 125, kind: 'neutral', titleSize: 25, bodySize: 24, name: 'voices-mechanisms' });
    return true;
  }
  if (d.id === 'U08-085') {
    addLine(slide, 330, 245, 480, 300, { color: C.teal, width: 3, arrow: true, name: 'noise-signal' });
    addLine(slide, 330, 420, 480, 330, { color: C.ochre, width: 3, arrow: true, name: 'reverb-signal' });
    addLine(slide, 800, 315, 945, 315, { color: C.berry2, width: 3, arrow: true, name: 'signal-task' });
    addPanel(slide, 'Ruido', 'Compite con la señal en frecuencia y tiempo.', { x: 70, y: 170, w: 260, h: 155, kind: 'physical', titleSize: 28, bodySize: 24, name: 'causal-noise' });
    addPanel(slide, 'Reverberación', 'Redistribuye energía y superpone segmentos.', { x: 70, y: 365, w: 260, h: 155, kind: 'clinical', titleSize: 28, bodySize: 24, name: 'causal-reverb' });
    addPanel(slide, 'Mezcla en el oído', 'Menor contraste entre pistas del habla; los efectos pueden interactuar.', { x: 480, y: 220, w: 320, h: 210, kind: 'accent', titleSize: 28, bodySize: 25, name: 'causal-mixture' });
    addPanel(slide, 'Tarea de reconocimiento', 'Respuesta: proporción de elementos identificados correctamente.', { x: 945, y: 220, w: 270, h: 210, kind: 'neutral', titleSize: 27, bodySize: 24, name: 'causal-response' });
    return true;
  }
  if (d.id === 'U08-103') {
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
  if (d.id === 'U08-107') {
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
  if (d.id === 'U08-117') {
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

function addSimplePlot(slide, { x, y, w, h, xLabel, yLabel, series, xTicks = [], yTicks = [], note = '', name = 'plot' }) {
  addShape(slide, { geometry: 'rect', name: `${name}-frame`, x, y, w, h, fill: C.white, lineFill: C.lightGray, lineWidth: 1.5 });
  const left = x + 78; const right = x + w - 25; const top = y + 28; const bottom = y + h - 62;
  addLine(slide, left, bottom, right, bottom, { color: C.carbon, width: 2, arrow: false, name: `${name}-x` });
  addLine(slide, left, bottom, left, top, { color: C.carbon, width: 2, arrow: false, name: `${name}-y` });
  yTicks.forEach(([t, label]) => {
    const yy = bottom - t * (bottom - top);
    addLine(slide, left, yy, right, yy, { color: C.lightGray, width: 1, name: `${name}-grid-y` });
    addText(slide, label, { x: x + 4, y: yy - 12, w: 65, h: 24, size: 18, color: C.carbon, align: 'right', name: `${name}-ytick`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  });
  xTicks.forEach(([t, label]) => {
    const xx = left + t * (right - left);
    addLine(slide, xx, bottom, xx, top, { color: '#EEF0F2', width: 1, name: `${name}-grid-x` });
    addText(slide, label, { x: xx - 35, y: bottom + 8, w: 70, h: 24, size: 18, color: C.carbon, align: 'center', name: `${name}-xtick`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  });
  series.forEach((s, si) => {
    const color = s.color || (si ? C.teal : C.berry2);
    const pts = s.points.map(([px, py]) => [left + px * (right - left), bottom - py * (bottom - top)]);
    for (let i = 0; i < pts.length - 1; i += 1) addLine(slide, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], { color, width: 3.5, name: `${name}-${si}-line` });
    pts.forEach(([px, py], i) => addShape(slide, { geometry: 'ellipse', name: `${name}-${si}-point-${i}`, x: px - 6, y: py - 6, w: 12, h: 12, fill: color, lineFill: C.white, lineWidth: 1 }));
    if (s.label) addText(slide, s.label, { x: right - 245, y: top + si * 34, w: 230, h: 28, size: 20, color, bold: true, align: 'right', name: `${name}-${si}-label`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  });
  addText(slide, xLabel, { x: left + 80, y: y + h - 32, w: right - left - 160, h: 26, size: 20, color: C.carbon, bold: true, align: 'center', name: `${name}-xlabel`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  addText(slide, yLabel, { x: x + 10, y: y + 6, w: Math.min(260, w - 20), h: 24, size: 18, color: C.carbon, bold: true, align: 'left', name: `${name}-ylabel`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
  if (note) addText(slide, note, { x: left + 30, y: bottom - 36, w: right - left - 60, h: 28, size: 18, color: '#5E6267', italic: true, align: 'center', name: `${name}-note`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
}

function addConceptualGraph(slide, d) {
  if (d.id === 'U08-023') {
    const fields = ['Exposición: nivel, espectro y duración', 'Frecuencia y procedimiento de prueba', 'Tiempos pos-exposición', 'Muestra y variabilidad', 'Fuente primaria y límites'];
    fields.forEach((text, i) => addPanel(slide, `${i + 1}`, text, {
      x: 65 + (i % 3) * 385, y: 165 + Math.floor(i / 3) * 210, w: 350, h: 165,
      kind: i === 4 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 24, bodySize: 23, name: `u08-023-${i + 1}`,
    }));
    addText(slide, 'Sin estos campos, una curva temporal no puede interpretarse ni extrapolarse.', { x: 220, y: 560, w: 840, h: 50, size: 25, color: C.berry, bold: true, align: 'center', name: 'u08-023-limit' });
    return true;
  }
  if (d.id === 'U08-030') {
    addSimplePlot(slide, {
      x: 55, y: 150, w: 840, h: 445, xLabel: 'Frecuencia f (Hz)', yLabel: 'dB HL',
      xTicks: [[0,'250'],[0.17,'500'],[0.34,'1000'],[0.51,'2000'],[0.68,'4000'],[0.85,'6000'],[1,'8000']],
      yTicks: [[0,'70'],[0.25,'50'],[0.5,'30'],[0.75,'10'],[1,'−10']],
      series: [{ label: 'patrón ficticio', color: C.berry2, points: [[0,0.78],[0.17,0.76],[0.34,0.72],[0.51,0.62],[0.68,0.30],[0.85,0.56],[1,0.68]] }],
      note: 'Escotadura conceptual: describe una forma; no establece etiología.', name: 'u08-030-notch',
    });
    addPanel(slide, 'Lectura permitida', 'Hay mayor nivel de audición registrado alrededor de 4000 Hz en este ejemplo ficticio.', { x: 930, y: 170, w: 285, h: 170, kind: 'physical', titleSize: 25, bodySize: 22, name: 'u08-030-allowed' });
    addPanel(slide, 'Conclusión prohibida', 'La forma aislada no demuestra origen laboral ni excluye otras causas.', { x: 930, y: 380, w: 285, h: 170, kind: 'clinical', titleSize: 25, bodySize: 22, name: 'u08-030-forbidden' });
    return true;
  }
  if (d.id === 'U08-035') {
    addText(slide, 'Exceso de riesgo estimado por edad · más de 10 años de exposición', { x: 85, y: 145, w: 1110, h: 42, size: 29, color: C.carbon, bold: true, align: 'center', name: 'u08-035-heading' });
    addGridTable(slide, [
      ['Exposición diaria', '30 años', '40 años', '50 años', '60 años'],
      ['80 dBA', '0,3 %', '0,6 %', '1,0 %', '1,3 %'],
      ['85 dBA', '2,3 %', '4,3 %', '6,7 %', '7,9 %'],
      ['90 dBA', '10,3 %', '17,5 %', '24,1 %', '24,7 %'],
    ], [1.45,1,1,1,1], { x: 90, y: 210, w: 1100, rowH: 72, name: 'u08-035-risk', bodySize: 22 });
    addPanel(slide, 'Cómo leerlo', 'Modelo NIOSH 1997, definición 1–2–3–4 kHz. “Exceso” compara población expuesta y no expuesta. Los IC 95 % son amplios; no es un pronóstico individual.', { x: 130, y: 505, w: 1020, h: 130, kind: 'clinical', titleSize: 24, bodySize: 21, name: 'u08-035-reading' });
    return true;
  }
  if (d.id === 'U08-057') {
    addSimplePlot(slide, {
      x: 55, y: 150, w: 820, h: 445, xLabel: 'Nivel de presentación (escala por declarar)', yLabel: 'Respuestas correctas (%)',
      xTicks: [[0,'bajo'],[0.25,''],[0.5,'medio'],[0.75,''],[1,'alto']], yTicks: [[0,'0'],[0.25,'25'],[0.5,'50'],[0.75,'75'],[1,'100']],
      series: [{ label: 'curva conceptual', color: C.teal, points: [[0.05,0.02],[0.22,0.12],[0.38,0.42],[0.55,0.72],[0.72,0.88],[0.9,0.82]] }],
      note: 'La forma depende de material, idioma, modo, oído y protocolo.', name: 'u08-057-performance',
    });
    addPanel(slide, 'Antes de interpretar', 'Declare la escala horizontal: dB HL, dB SL o dB SPL no son intercambiables.', { x: 915, y: 180, w: 300, h: 170, kind: 'physical', titleSize: 25, bodySize: 22, name: 'u08-057-scale' });
    addPanel(slide, 'Límite', 'La curva no localiza una lesión ni describe por sí sola el desempeño cotidiano.', { x: 915, y: 390, w: 300, h: 170, kind: 'clinical', titleSize: 25, bodySize: 22, name: 'u08-057-limit' });
    return true;
  }
  if (d.id === 'U08-069') {
    const configs = [
      ['Pico centrado', [[0,0.12],[0.2,0.18],[0.4,0.55],[0.5,0.92],[0.6,0.55],[0.8,0.18],[1,0.12]]],
      ['Trazado plano', [[0,0.2],[0.2,0.19],[0.4,0.2],[0.6,0.19],[0.8,0.2],[1,0.2]]],
      ['Pico desplazado', [[0,0.15],[0.15,0.55],[0.28,0.90],[0.45,0.5],[0.65,0.2],[0.85,0.15],[1,0.14]]],
    ];
    configs.forEach(([label, pts], i) => addSimplePlot(slide, {
      x: 40 + i * 420, y: 175, w: 380, h: 360, xLabel: 'Presión (daPa)', yLabel: 'Y / Ymáx',
      xTicks: [[0,'−'],[0.5,'0'],[1,'+']], yTicks: [[0,'0'],[1,'1']],
      series: [{ label, color: i === 1 ? C.gray : i === 2 ? C.ochre : C.teal, points: pts }], note: 'descripción geométrica', name: `u08-069-${i + 1}`,
    }));
    addText(slide, 'Estas morfologías son esquemas descriptivos: ninguna equivale por sí sola a una enfermedad.', { x: 160, y: 565, w: 960, h: 38, size: 25, color: C.berry, bold: true, align: 'center', name: 'u08-069-limit' });
    return true;
  }
  return false;
}

function addStructuredTableSlide(slide, d) {
  if (d.id === 'U08-012') {
    addGridTable(slide, [
      ['Componente', 'Dónde mirar', 'Qué no permite concluir'],
      ['Conductivo', 'Transmisión por oído externo y medio', 'No se infiere de un dato aislado'],
      ['Sensorioneural', 'Cóclea y/o vía neural', 'No identifica por sí solo etiología'],
      ['Mixto', 'Combinación de componentes', 'Requiere integrar una batería'],
    ], [1,1.7,1.7], { x: 70, y: 170, w: 1140, rowH: 93, name: 'u08-012-table', bodySize: 22 });
    return true;
  }
  if (d.id === 'U08-047' || d.id === 'U08-104') {
    addGridTable(slide, [
      ['Escala', 'Referencia', 'Uso típico', 'Operación válida / límite'],
      ['dB SPL', 'Presión acústica física', 'Señales y salidas acústicas', 'No convertir a HL sin referencia'],
      ['dB HL', 'Cero audiométrico por frecuencia y transductor', 'Umbrales audiométricos', 'Comparar condiciones compatibles'],
      ['dB SL', 'Umbral individual declarado', 'Nivel relativo de presentación', 'No describe una fuente interna'],
    ], [0.7,1.6,1.4,1.6], { x: 55, y: 165, w: 1170, rowH: 98, name: `${d.id}-scales`, bodySize: 21 });
    return true;
  }
  if (d.id === 'U08-105') {
    const left = [
      ['Audiometría', 'tono → tarea → umbral en dB HL'], ['Logoaudiometría', 'habla → tarea verbal → % o umbral'],
      ['Timpanometría', 'tono + presión → micrófono → inmitancia'], ['Acufenometría', 'sonido ajustable → correspondencia'],
    ];
    const right = [
      ['OEA', 'sonido → micrófono → presión / SNR'], ['PEAT', 'sonido → electrodos → V(t)'],
      ['ECoG', 'sonido → electrodo próximo → potenciales'],
    ];
    addPanel(slide, 'Conductuales y mecanoacústicas', left.map(([a,b]) => `${a}: ${b}`).join('\n\n'), { x: 60, y: 165, w: 560, h: 430, kind: 'physical', titleSize: 28, bodySize: 22, name: 'u08-105-left' });
    addPanel(slide, 'Fisiológicas', right.map(([a,b]) => `${a}: ${b}`).join('\n\n'), { x: 660, y: 165, w: 560, h: 430, kind: 'clinical', titleSize: 28, bodySize: 22, name: 'u08-105-right' });
    return true;
  }
  if (d.id === 'U08-106') {
    addGridTable(slide, [
      ['Dispositivo', 'Entrada', 'Procesamiento', 'Salida física', 'Límite'],
      ['Audífono', 'acústica', 'dependiente de frecuencia y nivel', 'acústica', 'beneficio a evaluar'],
      ['Implante coclear', 'acústica', 'codificación', 'eléctrica', 'no garantiza perceptos independientes'],
      ['Conducción ósea', 'acústica', 'transducción', 'mecánica', 'selección individual'],
      ['Electroacústica', 'acústica', 'separación por bandas', 'acústica + eléctrica', 'ajuste individualizado'],
    ], [1,0.75,1.5,1,1.6], { x: 45, y: 160, w: 1190, rowH: 84, name: 'u08-106-devices', bodySize: 20 });
    return true;
  }
  return false;
}

function addErrorSlide(slide, d) {
  const problem = {
    'U08-013': '“Si el patrón es compatible, ya conocemos la causa”.',
    'U08-058': '“72 % correcto” se presenta sin material, nivel, escala, oído ni criterio.',
    'U08-071': '“Un trazado plano indica cuánto oye la persona”.',
    'U08-076': '“OEA presente significa audición normal”.',
    'U08-079': '“Si aparece un PEAT, la persona comprende el habla”.',
    'U08-091': '“Cada electrodo produce un canal y un percepto independiente”.',
  }[d.id] || audienceText(d.content, d.title);
  addPanel(slide, 'Afirmación problemática', problem, { x: 65, y: 175, w: 500, h: 320, kind: 'neutral', titleSize: 29, bodySize: 27, name: `${d.id}-problem` });
  addPanel(slide, 'Corrección', ERROR_CORRECTIONS[d.id], { x: 610, y: 175, w: 600, h: 320, kind: 'clinical', titleSize: 29, bodySize: 25, name: `${d.id}-correction` });
  addText(slide, 'Regla de control: describir primero el dato y sus condiciones; recién después integrar hipótesis.', { x: 150, y: 535, w: 980, h: 45, size: 25, color: C.berry, bold: true, align: 'center', name: `${d.id}-rule` });
}

function addApplicationSlide(slide, d) {
  if (d.id === 'U08-002') {
    addPanel(slide, 'Después del trabajo', 'Necesita aumentar el nivel del televisor.', { x: 65, y: 170, w: 340, h: 210, kind: 'physical', titleSize: 27, bodySize: 25, name: 'u08-002-a' });
    addPanel(slide, 'En conversación', 'Le cuesta seguir el habla cuando hay ruido.', { x: 470, y: 170, w: 340, h: 210, kind: 'neutral', titleSize: 27, bodySize: 25, name: 'u08-002-b' });
    addPanel(slide, 'Sin fuente externa', 'Refiere un sonido o zumbido.', { x: 875, y: 170, w: 340, h: 210, kind: 'clinical', titleSize: 27, bodySize: 25, name: 'u08-002-c' });
    addPanel(slide, 'Pregunta de apertura', '¿Qué mediría primero y qué pregunta concreta respondería esa medición?', { x: 250, y: 435, w: 780, h: 135, kind: 'accent', titleSize: 27, bodySize: 25, name: 'u08-002-question' });
    return true;
  }
  if (d.id === 'U08-015') {
    addFlow(slide, [['Historia', 'Antecedentes y exposición'], ['Conducta', 'Umbrales y tareas'], ['Fisiología', 'Respuestas acústicas o eléctricas'], ['Integración', 'Coincidencias, límites y nuevas preguntas']], { y: 215, h: 230, name: 'u08-015-battery' });
    return true;
  }
  if (d.id === 'U08-096') {
    const items = [['Exposición', 'L_Aeq,T'], ['Percepción', 'tinnitus / dB SL'], ['Conducta', 'umbral en dB HL'], ['Fisiología', 'OEA: “derivar”']];
    items.forEach(([a,b],i) => addPanel(slide, a, b, { x: 65 + i * 295, y: 190, w: 255, h: 220, kind: i === 3 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 27, bodySize: 24, name: `u08-096-${i}` }));
    addPanel(slide, 'Integración', 'Cada dato responde una pregunta distinta; ninguno resuelve el caso por sí solo.', { x: 215, y: 465, w: 850, h: 115, kind: 'accent', titleSize: 27, bodySize: 24, name: 'u08-096-limit' });
    return true;
  }
  if (d.id === 'U08-100') {
    addFlow(slide, [['1', 'Formular la pregunta'], ['2', 'Recuperar antecedentes'], ['3', 'Seleccionar pruebas'], ['4', 'Controlar condiciones'], ['5', 'Integrar, comunicar y seguir']], { y: 215, h: 220, name: 'u08-100-professional' });
    return true;
  }
  return false;
}

function addTextVisualSlide(slide, d) {
  if (d.id === 'U08-038') {
    addFlow(slide, [
      ['Presentación', 'Estímulo controlado'],
      ['Interacción', 'Sistema auditivo'],
      ['Registro', 'Sensor o tarea'],
      ['Representación', 'Magnitud y unidad'],
      ['Interpretación', 'Condiciones y protocolo'],
    ], { y: 215, h: 225, gap: 14, name: 'u08-038-process' });
    addText(slide, 'Cada etapa condiciona qué pregunta puede responder el dato final.', { x: 190, y: 500, w: 900, h: 45, size: 28, color: C.berry, bold: true, align: 'center', name: 'u08-038-limit' });
    return true;
  }
  if (d.id === 'U08-046') {
    addText(slide, 'Vía aérea', { x: 55, y: 220, w: 145, h: 42, size: 27, color: C.teal, bold: true, align: 'right', name: 'u08-046-air-label' });
    addFlow(slide, [
      ['Entrada', 'Auricular'],
      ['Trayecto', 'Oído externo y medio'],
      ['Respuesta', 'Cóclea + tarea conductual'],
    ], { x: 220, y: 165, width: 990, h: 155, gap: 22, name: 'u08-046-air' });
    addText(slide, 'Vía ósea', { x: 55, y: 445, w: 145, h: 42, size: 27, color: C.ochre, bold: true, align: 'right', name: 'u08-046-bone-label' });
    addFlow(slide, [
      ['Entrada', 'Vibrador óseo'],
      ['Trayecto', 'Cráneo y mecanismos múltiples'],
      ['Respuesta', 'Cóclea + tarea conductual'],
    ], { x: 220, y: 390, width: 990, h: 155, gap: 22, name: 'u08-046-bone' });
    addText(slide, 'Cambiar el transductor modifica el trayecto predominante; ninguna vía aísla una sola estructura.', { x: 165, y: 585, w: 950, h: 42, size: 25, color: C.berry, bold: true, align: 'center', name: 'u08-046-limit' });
    return true;
  }
  if (d.id === 'U08-085') {
    addFlow(slide, [
      ['Entrada', 'Señal que recibe'],
      ['Procesamiento', 'Transduce y modifica'],
      ['Salida', 'Acústica, eléctrica o mecánica'],
      ['Acoplamiento', 'Punto de entrega'],
      ['Evaluación', 'Resultado funcional'],
    ], { y: 205, h: 235, gap: 14, name: 'u08-085-device-chain' });
    addPanel(slide, 'Límite de la comparación', 'Una cadena técnica describe cómo actúa el dispositivo; no garantiza beneficio comunicativo ni reemplaza la evaluación clínica.', { x: 175, y: 485, w: 930, h: 125, kind: 'clinical', titleSize: 25, bodySize: 23, name: 'u08-085-limit' });
    return true;
  }
  const cards = {
    'U08-018': [['Nivel', 'Magnitud y descriptor'], ['Ponderación', 'A u otra respuesta'], ['Duración', 'Intervalo de medida'], ['Espectro', 'Distribución en frecuencia'], ['Temporalidad', 'Continuo, variable o impulsivo']],
    'U08-033': [['Edad', 'Cambios asociados'], ['Sistema neural', 'Cóclea y vía: mecanismos heterogéneos'], ['Exposición', 'Historia acústica'], ['Salud y fármacos', 'Factores concurrentes'], ['Variabilidad', 'No existe una pendiente única']],
    'U08-042': [['Calibración', 'Referencia del equipo'], ['Ambiente', 'Ruido y condiciones'], ['Colocación', 'Transductor o sensor'], ['Consigna', 'Comprensión y respuesta']],
    'U08-053': [['Ambiente', 'Ruido de fondo'], ['Transductor', 'Tipo y colocación'], ['Consigna', 'Tarea comprendida'], ['Enmascaramiento', 'Cruce entre oídos']],
    'U08-081': [['CM', 'Microfónico coclear: sigue el estímulo'], ['SP', 'Potencial de sumación: componente sostenido'], ['AP', 'Potencial de acción compuesto: respuesta neural distal']],
    'U08-098': [['Convergencia', 'Resultados compatibles reducen preguntas'], ['Discrepancia', 'Revisar generador, sensor y tarea'], ['Condiciones', 'Calibración, ruido y protocolo'], ['Integración', 'Explicar qué aporta y limita cada dato']],
  }[d.id];
  if (!cards) return false;
  if (cards.length === 3) addFlow(slide, cards, { y: 220, h: 245, gap: 35, name: `${d.id}-cards` });
  else cards.forEach(([title, body], i) => addPanel(slide, title, body, {
    x: 55 + i * 240, y: 205, w: 215, h: 270, kind: i === cards.length - 1 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 25, bodySize: 23, name: `${d.id}-card-${i + 1}`,
  }));
  return true;
}

function addVisualCompleteSlide(slide, d) {
  if (d.id === 'U08-009') {
    const cards = [['Exposición', 'Qué actuó y durante cuánto'], ['Alteración', 'Cambio físico o funcional'], ['Síntoma', 'Experiencia referida'], ['Resultado', 'Dato de una prueba'], ['Limitación', 'Dificultad en una actividad']];
    cards.forEach(([title, body], i) => addPanel(slide, title, body, { x: 45 + i * 246, y: 205, w: 220, h: 270, kind: i === 4 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 25, bodySize: 23, name: `u08-009-${i}` }));
    return true;
  }
  if (d.id === 'U08-041') {
    const rows = [
      ['Oído externo y medio', 'Audiometría aérea · timpanometría · OEA'], ['Cóclea', 'Audiometría tonal · OEA · ECoG'],
      ['Nervio y tronco', 'PEAT · ECoG'], ['Respuesta integrada', 'Audiometría · logoaudiometría · acufenometría'],
    ];
    rows.forEach(([a,b],i) => addPanel(slide, a, b, { x: 75 + (i % 2) * 590, y: 165 + Math.floor(i/2) * 215, w: 540, h: 175, kind: i % 3 === 2 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 27, bodySize: 24, name: `u08-041-${i}` }));
    addText(slide, 'Una prueba puede depender de más de una parte del sistema; ninguna fila equivale a diagnóstico.', { x: 165, y: 565, w: 950, h: 40, size: 24, color: C.berry, bold: true, align: 'center', name: 'u08-041-limit' });
    return true;
  }
  if (d.id === 'U08-049') {
    addSimplePlot(slide, { x: 55, y: 150, w: 860, h: 445, xLabel: 'Frecuencia f (Hz)', yLabel: 'Nivel de audición (dB HL)',
      xTicks: [[0,'250'],[0.2,'500'],[0.4,'1000'],[0.6,'2000'],[0.8,'4000'],[1,'8000']], yTicks: [[0,'70'],[0.25,'50'],[0.5,'30'],[0.75,'10'],[1,'−10']],
      series: [
        { label: 'Vía aérea', color: C.berry2, points: [[0,0.55],[0.2,0.5],[0.4,0.37],[0.6,0.28],[0.8,0.18],[1,0.16]] },
        { label: 'Vía ósea', color: C.teal, points: [[0,0.73],[0.2,0.75],[0.4,0.68],[0.6,0.62],[0.8,0.5],[1,0.47]] },
      ], note: 'Datos didácticos ficticios; no representan una patología.', name: 'u08-049-audiogram' });
    addPanel(slide, 'Orden de lectura', '1. Frecuencia\n2. Oído y vía\n3. Valor en dB HL\n4. Diferencia entre vías\n5. Límite de interpretación', { x: 950, y: 185, w: 265, h: 330, kind: 'physical', titleSize: 26, bodySize: 23, name: 'u08-049-guide' });
    return true;
  }
  if (d.id === 'U08-069') return addConceptualGraph(slide, d);
  return false;
}

function addRecapSlide(slide, d) {
  const recap = {
    'U08-016': ['Clasifique el dato', 'Nombre magnitud y unidad', 'Separe medición de causa', 'Integre antes de diagnosticar'],
    'U08-027': ['TTS exige comparación', 'La curva exige condiciones', 'L_Aeq,T describe energía promedio', 'El signo no predice evolución'],
    'U08-044': ['Estímulo', 'Sistema o función', 'Sensor o tarea', 'Magnitud y unidad', 'Resultado', 'Límite'],
    'U08-054': ['Leer frecuencia, oído y vía', 'Comparar condiciones compatibles', 'Informar la diferencia en dB', 'No nombrar una enfermedad'],
    'U08-064': ['Tono: umbral por frecuencia', 'Habla: umbral o porcentaje', 'Acúfeno: correspondencia', 'Cada tarea tiene su límite'],
    'U08-072': ['Entrada: tono y presión', 'Sistema: oído externo/medio', 'Dato: inmitancia frente a presión', 'No mide por sí solo audición'],
    'U08-094': ['Audífono: salida acústica', 'Implante: salida eléctrica', 'Conducción ósea: salida mecánica', 'La indicación exige evaluación'],
  }[d.id];
  if (!recap) return false;
  const n = recap.length; const gap = n > 4 ? 16 : 26; const w = (1160 - gap * (n - 1)) / n;
  recap.forEach((text,i) => addPanel(slide, String(i + 1).padStart(2,'0'), text, { x: 60 + i * (w + gap), y: 220, w, h: 250, kind: i === n - 1 ? 'clinical' : i % 2 ? 'neutral' : 'physical', titleSize: 24, bodySize: n > 4 ? 21 : 23, name: `${d.id}-recap-${i}` }));
  return true;
}

function addGainExercise(slide) {
  addGridTable(slide, [
    ['f (Hz)', '500', '1000', '2000'], ['Lentrada (dB SPL)', '54', '54', '54'], ['Lsalida (dB SPL)', '64', '69', '75'], ['G(f) (dB)', '10', '15', '21'],
  ], [1.4,1,1,1], { x: 60, y: 165, w: 610, rowH: 72, name: 'u08-110-table', bodySize: 22 });
  const bars = [10,15,21];
  addShape(slide, { geometry: 'rect', name: 'u08-110-chart-frame', x: 720, y: 165, w: 490, h: 330, fill: C.white, lineFill: C.lightGray, lineWidth: 1.5 });
  bars.forEach((v,i) => {
    const bh = v * 9; const xx = 790 + i * 135;
    addShape(slide, { geometry: 'rect', name: `u08-110-bar-${i}`, x: xx, y: 450 - bh, w: 72, h: bh, fill: i === 2 ? C.berry2 : C.teal, lineFill: 'none', lineWidth: 0 });
    addText(slide, `${v} dB`, { x: xx - 10, y: 415 - bh, w: 92, h: 30, size: 22, color: C.carbon, bold: true, align: 'center', name: `u08-110-value-${i}` });
    addText(slide, `${[500,1000,2000][i]} Hz`, { x: xx - 15, y: 460, w: 102, h: 28, size: 20, color: C.carbon, align: 'center', name: `u08-110-label-${i}` });
  });
  addPanel(slide, 'Conclusión limitada', 'La mayor ganancia es 21 dB a 2000 Hz. Esto no determina sonoridad, comodidad ni comprensión del habla.', { x: 180, y: 510, w: 920, h: 120, kind: 'clinical', titleSize: 24, bodySize: 22, name: 'u08-110-limit' });
}

function addAppendixSlide(slide, d) {
  if (d.id === 'U08-104') return addStructuredTableSlide(slide, d);
  if (d.id === 'U08-111') {
    const fields = ['Exposición y descriptor', 'Frecuencia de prueba', 'Tiempos pos-exposición', 'Muestra y variabilidad', 'Cita primaria completa', 'Límites de extrapolación'];
    fields.forEach((text,i) => addPanel(slide, String(i+1), text, { x: 65 + (i%3)*390, y: 165 + Math.floor(i/3)*205, w: 350, h: 165, kind: i >= 4 ? 'clinical' : i%2 ? 'neutral' : 'physical', titleSize: 24, bodySize: 23, name: `u08-111-${i}` }));
    addText(slide, 'No usar una curva pos-exposición si alguno de estos campos está ausente.', { x: 250, y: 565, w: 780, h: 38, size: 24, color: C.berry, bold: true, align: 'center', name: 'u08-111-rule' });
    return true;
  }
  if (d.id === 'U08-112') {
    addGridTable(slide, [
      ['Campo', 'Debe declarar'], ['Evento', 'Deterioro auditivo material según criterio explícito'], ['Población', 'Grupo expuesto y comparador no expuesto'], ['Exposición', 'Nivel diario y duración'], ['Resultado', 'Exceso de riesgo, no probabilidad individual'],
    ], [1,2.8], { x: 70, y: 160, w: 760, rowH: 82, name: 'u08-112-table', bodySize: 22 });
    addPanel(slide, 'Incertidumbre visible', 'A 85 dBA y >10 años, NIOSH estima 2,3 % a los 30 años (IC 95 %: 0,7–5,3) y 7,9 % a los 60 (2,3–16,6).', { x: 875, y: 165, w: 335, h: 235, kind: 'physical', titleSize: 26, bodySize: 21, name: 'u08-112-example' });
    addPanel(slide, 'Límite', 'El intervalo, la definición y el grupo comparador son parte del dato. El exceso poblacional no predice el resultado de una persona.', { x: 875, y: 420, w: 335, h: 190, kind: 'clinical', titleSize: 26, bodySize: 21, name: 'u08-112-limit' });
    return true;
  }
  if (d.id === 'U08-113') {
    addGridTable(slide, [
      ['Término', 'Desarrollo', 'Magnitud asociada'], ['TTS', 'desplazamiento temporal del umbral', 'diferencia de umbrales (dB)'], ['PAIR / NIHL', 'pérdida auditiva inducida por ruido', 'historia + patrón + evidencia'], ['OEA', 'otoemisiones acústicas', 'presión / dB SPL / SNR'], ['PEAT', 'potencial evocado auditivo de tronco', 'µV frente a ms'], ['ECoG', 'electrococleografía', 'potenciales y latencias'],
    ], [0.8,2,1.5], { x: 55, y: 150, w: 1170, rowH: 72, name: 'u08-113-terms', bodySize: 21 });
    return true;
  }
  return false;
}

function addLayoutSpecific(slide, d) {
  if (addMapSlide(slide, d)) return true;
  if (addApplicationSlide(slide, d)) return true;
  if (addTextVisualSlide(slide, d)) return true;
  if (addVisualCompleteSlide(slide, d)) return true;
  if (addStructuredTableSlide(slide, d)) return true;
  if (addConceptualGraph(slide, d)) return true;
  if (addRecapSlide(slide, d)) return true;
  if (addExerciseSlide(slide, d)) return true;
  if (d.id === 'U08-110') { addGainExercise(slide); return true; }
  if (d.layout.includes('APENDICE') && addAppendixSlide(slide, d)) return true;
  return false;
}

function addGeneric(slide, d) {
  if (addLayoutSpecific(slide, d)) return;
  const ideas = audienceIdeas(d.content, 6);
  const visibleContent = audienceText(d.content, 'Aplique la relación y explicite unidades, referencias y condiciones.');
  const isQuestion = /PREGUNTA|EJERCICIO/.test(d.layout);
  const isError = d.layout.includes('ERROR'); const isRecap = d.layout.includes('RECAP');
  const isCompare = d.layout.includes('COMPARACION'); const isEquation = d.layout.includes('ECUACION') || hasMeaningfulText(d.equations);
  if (isQuestion) {
    addQuestionSlide(slide, d);
  } else if (isError) {
    addErrorSlide(slide, d);
  } else if (isCompare) {
    const mid = Math.ceil(Math.max(2, ideas.length) / 2);
    const labels = COMPARE_LABELS[d.id] || ['Situación A', 'Situación B'];
    addPanel(slide, labels[0], ideas.slice(0, mid).join('\n\n') || visibleContent, { x: 65, y: 160, w: 545, h: 395, kind: 'physical', bodySize: 26, name: 'compare-a' });
    addPanel(slide, labels[1], ideas.slice(mid).join('\n\n') || audienceText(d.definitions || d.example, 'Compare el segundo caso con la misma magnitud, unidad y referencia.'), { x: 670, y: 160, w: 545, h: 395, kind: 'clinical', bodySize: 26, name: 'compare-b' });
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
      const sideBody = hasDefinition ? audienceText(d.definitions, 'Defina la magnitud, la unidad y la condición de medida.') : audienceText(d.example, 'Aplique el criterio a un ejemplo breve y explicite el límite de la conclusión.');
      addPanel(slide, sideTitle, sideBody, { x: 830, y: 170, w: 375, h: 350, kind: /clín|fono|audit|voz/i.test(`${d.title} ${d.content}`) ? 'clinical' : 'physical', bodySize: 25, name: 'side-panel' });
    }
  }
}

function addStudyComparison082(slide) {
  addPanel(slide, 'OEA', 'Sensor: micrófono\n\nMagnitud: presión acústica\n\nGenerador predominante: cóclea / CCE', {
    x: 65, y: 175, w: 350, h: 365, kind: 'physical', titleSize: 30, bodySize: 25, name: 'u08-082-oea',
  });
  addPanel(slide, 'PEAT', 'Sensor: electrodos superficiales\n\nMagnitud: V(t), en µV y ms\n\nGenerador: respuesta sincronizada de la vía auditiva', {
    x: 465, y: 175, w: 350, h: 365, kind: 'accent', titleSize: 30, bodySize: 25, name: 'u08-082-peat',
  });
  addPanel(slide, 'ECoG', 'Sensor: electrodo próximo\n\nMagnitud: potencial eléctrico\n\nGeneradores: cóclea y porción neural distal', {
    x: 865, y: 175, w: 350, h: 365, kind: 'clinical', titleSize: 30, bodySize: 25, name: 'u08-082-ecog',
  });
  addText(slide, 'Comparten una entrada acústica; no registran la misma magnitud ni permiten la misma inferencia.', {
    x: 145, y: 575, w: 990, h: 42, size: 25, color: C.berry, bold: true, align: 'center', name: 'u08-082-limit',
  });
}

function addExposureComparison031(slide) {
  addPanel(slide, 'Trauma acústico', 'Episodio acústico abrupto.\n\nRegistrar: nivel o pico con su referencia, duración, distancia, protección y síntomas temporales.', {
    x: 80, y: 180, w: 540, h: 390, kind: 'physical', titleSize: 30, bodySize: 26, name: 'u08-031-trauma',
  });
  addPanel(slide, 'Ototoxicidad', 'Exposición farmacológica o química.\n\nRegistrar: agente, dosis, duración, vía, función renal y posibles coexposiciones.', {
    x: 660, y: 180, w: 540, h: 390, kind: 'clinical', titleSize: 30, bodySize: 26, name: 'u08-031-ototoxicity',
  });
}

function addBatteryReview043(slide) {
  addBulletList(slide, [
    'Verifique qué magnitud registra cada prueba y con qué unidad.',
    'Revise estímulo, transductor, calibración y condiciones de medición.',
    'Considere repetibilidad, estado del paciente y coherencia con la historia.',
    'Explique qué hipótesis apoya cada resultado y cuál deja abierta.',
  ], { x: 70, y: 165, w: 730, h: 410, size: 28, name: 'u08-043-review-list' });
  addPanel(slide, 'Idea central', 'Una batería integra evidencia convergente. La discrepancia exige revisar condiciones y supuestos; no autoriza a descartar automáticamente una prueba.', {
    x: 835, y: 180, w: 380, h: 350, kind: 'physical', titleSize: 29, bodySize: 25, name: 'u08-043-central',
  });
}

function addResolvedSourceSlide(slide, d) {
  if (d.id === 'U08-057') {
    addPanel(slide, 'Pilar interno', 'Límite medial', { x: 80, y: 215, w: 285, h: 205, kind: 'physical', bodySize: 30, name: 'tunnel-inner' });
    addPanel(slide, 'Túnel de Corti', 'Espacio triangular lleno de fluido', { x: 410, y: 185, w: 460, h: 265, kind: 'accent', bodySize: 30, name: 'tunnel-space' });
    addPanel(slide, 'Pilar externo', 'Límite lateral', { x: 915, y: 215, w: 285, h: 205, kind: 'clinical', bodySize: 30, name: 'tunnel-outer' });
    addPanel(slide, 'Membrana basilar', 'La zona arcuata completa el límite inferior', { x: 250, y: 485, w: 780, h: 100, kind: 'neutral', titleSize: 28, bodySize: 25, name: 'tunnel-base' });
    return true;
  }
  if (d.id === 'U08-085') {
    addPanel(slide, 'Potencial de reposo', 'Condición eléctrica basal de la membrana, medida respecto de una referencia extracelular declarada.', { x: 80, y: 175, w: 520, h: 330, kind: 'neutral', titleSize: 31, bodySize: 29, name: 'resting' });
    addPanel(slide, 'Potencial receptor', 'Cambio graduado respecto del estado basal cuando la deflexión modifica la corriente iónica.', { x: 680, y: 175, w: 520, h: 330, kind: 'accent', titleSize: 31, bodySize: 29, name: 'receptor' });
    addText(slide, 'La referencia de medida importa; aquí no se fija un valor universal.', { x: 190, y: 535, w: 900, h: 42, size: 29, color: C.berry, bold: true, align: 'center', name: 'resting-caution' });
    return true;
  }
  if (d.id === 'U08-096') {
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
  if (d.id === 'U08-115') {
    addPanel(slide, 'Umbral', 'Depende del estímulo, el método y la persona; no es una constante universal.', { x: 75, y: 160, w: 530, h: 185, kind: 'physical', titleSize: 29, bodySize: 26, name: 'reflex-threshold' });
    addPanel(slide, 'Latencia', 'Disminuye al aumentar el nivel por encima del umbral, pero la respuesta muscular no es instantánea.', { x: 675, y: 160, w: 530, h: 185, kind: 'accent', titleSize: 29, bodySize: 26, name: 'reflex-latency' });
    addPanel(slide, 'Impulsos breves', 'El comienzo del impulso puede preceder a la contracción: no hay protección inicial garantizada.', { x: 75, y: 380, w: 530, h: 185, kind: 'clinical', titleSize: 29, bodySize: 26, name: 'reflex-impulse' });
    addPanel(slide, 'Interpretación', 'Una medición del reflejo informa sobre varias partes del sistema; no identifica por sí sola una etiología.', { x: 675, y: 380, w: 530, h: 185, kind: 'neutral', titleSize: 29, bodySize: 26, name: 'reflex-interpretation' });
    return true;
  }
  if (d.id === 'U08-116') {
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
  const explicit = [...d.visual.matchAll(/U08-(?:CH|DG)-\d{3}[A-Z]?/g)].map((m) => m[0]);
  for (const id of explicit) if (byId.has(id)) return byId.get(id);
  return undefined;
}

function addNotes(slide, d, note, asset) {
  const lines = [`- Fuentes de contenido: ${d.source || 'Programa oficial y libro del curso.'}`];
  if (asset) lines.push(`- Asset propio aprobado: ${asset.asset_id}.`);
  if (['U08-035', 'U08-112'].includes(d.id)) {
    lines.push('- NIOSH. Criteria for a Recommended Standard: Occupational Noise Exposure, DHHS (NIOSH) Publication 98-126 (1998): https://www.cdc.gov/niosh/docs/98-126/');
    lines.push('- Datos de la tabla 3-3: modelo NIOSH 1997 para la definición 1–2–3–4 kHz; exceso de riesgo por edad, nivel diario y duración de exposición, con IC 95 %.');
    lines.push('- NIOSH HHE 2019-0106-3378: definición de deterioro auditivo material y estimaciones de 8 % a 85 dBA y 25 % a 90 dBA para una vida laboral de 40 años: https://www.cdc.gov/niosh/hhe/reports/pdfs/2019-0106-3378.pdf');
  }
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
// Diagram assets were validated as stand-alone 16:9 figures, but their
// internal labels become clipped or collide when projected into the content
// aperture of this approved template.  Keep the six approved quantitative
// charts as vector artwork and render diagram-led slides with the editable
// native compositions below.  This avoids inserting a preliminary/cropped
// diagram version that fails the required in-context validation.
const approved = manifest.filter((a) => a.status === 'approved' && a.type === 'chart'
  && a.local_path && !EXCLUDED_ASSETS.has(a.asset_id));
const byId = new Map(approved.map((a) => [a.asset_id, a]));
if (slidesData.length !== 114 || notes.size !== 114) throw new Error(`Conteos incompatibles: slides=${slidesData.length}, notas=${notes.size}.`);

const deck = await PresentationFile.importPptx(await FileBlob.load(STARTER));
const slides = [...deck.slides.items];
if (slides.length !== 114) throw new Error(`El starter debe tener 114 slides; tiene ${slides.length}.`);
const log = [];
for (let i = 0; i < slides.length; i += 1) {
  const slide = slides[i]; const d = slidesData[i]; await clearSlide(slide);
  const dark = ['FA_00_PORTADA', 'FA_01_DIVISOR', 'FA_21_CIERRE_PUENTE'].includes(d.layout);
  slide.background.fill = dark ? C.berry : C.white;
  if (d.layout === 'FA_00_PORTADA') {
    addText(slide, 'UNIDAD 8 · FÍSICA ACÚSTICA', { x: 64, y: 42, w: 560, h: 28, size: 18, color: C.white, bold: true, name: 'cover-eyebrow' });
    addText(slide, d.title, { x: 78, y: 125, w: 650, h: 245, size: 50, color: C.white, font: 'Calibri Light', name: 'cover-title', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
    addText(slide, d.subtitle, { x: 82, y: 390, w: 640, h: 70, size: 29, color: '#EADDE4', name: 'cover-subtitle' });
    const chain = ['exposición', 'estudio', 'dato', 'intervención'];
    const boxes = chain.map((_, k) => addShape(slide, { geometry: 'roundRect', name: `cover-step-${k + 1}-anchor`, x: 780 + (k % 2) * 205, y: 185 + Math.floor(k / 2) * 170, w: 170, h: 110, fill: 'none', lineFill: 'none', lineWidth: 0, radius: 10 }));
    slide.shapes.connect(boxes[0], boxes[1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: '#E0B9CB', width: 2 }, tail: { type: 'arrow' } });
    slide.shapes.connect(boxes[1], boxes[2], { kind: 'elbow', fromSide: 'bottom', toSide: 'top', line: { style: 'solid', fill: '#E0B9CB', width: 2 }, tail: { type: 'arrow' } });
    slide.shapes.connect(boxes[2], boxes[3], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: '#E0B9CB', width: 2 }, tail: { type: 'arrow' } });
    chain.forEach((t, k) => { addShape(slide, { geometry: 'roundRect', name: `cover-step-${k + 1}`, x: 780 + (k % 2) * 205, y: 185 + Math.floor(k / 2) * 170, w: 170, h: 110, fill: k < 2 ? '#6A2447' : '#77384F', lineFill: '#CFA7BA', lineWidth: 1.5, radius: 10 }); addText(slide, t, { x: 795 + (k % 2) * 205, y: 215 + Math.floor(k / 2) * 170, w: 140, h: 50, size: 26, color: C.white, bold: true, align: 'center', valign: 'middle', name: `cover-step-${k + 1}-text` }); });
    addText(slide, '4 encuentros · ruta central + ampliaciones + respaldo', { x: 82, y: 520, w: 650, h: 35, size: 22, color: '#EADDE4', name: 'cover-route' });
  } else if (d.layout === 'FA_01_DIVISOR' || d.layout === 'FA_21_CIERRE_PUENTE') {
    const route = teachingRoute(d);
    addText(slide, `UNIDAD 8 · ${route.session} · ${route.route}`, { x: 55, y: 24, w: 520, h: 24, size: 16, color: '#E1C8D4', bold: true, name: 'dark-eyebrow' });
    addText(slide, d.title, { x: 80, y: 225, w: 1120, h: 115, size: 54, color: C.white, font: 'Calibri Light', align: 'center', valign: 'middle', name: 'divider-title' });
    if (hasMeaningfulText(d.subtitle)) addText(slide, d.subtitle, { x: 165, y: 370, w: 950, h: 65, size: 28, color: '#E6D5DD', align: 'center', name: 'divider-subtitle' });
  } else {
    const asset = BLOCKED.has(d.id) ? undefined : assetForSlide(d, approved, byId);
    const custom = false;
    if (['diagram', 'equation_only'].includes(asset?.type)) { await addDiagram(slide, d, asset); addCaption(slide, d, asset); }
    else {
      addTitle(slide, d);
      if (BLOCKED.has(d.id)) addBlocked(slide, d);
      else if (asset?.type === 'chart') await addChart(slide, d, asset);
      else if (d.id === 'U08-031') addExposureComparison031(slide);
      else if (d.id === 'U08-043') addBatteryReview043(slide);
      else if (d.id === 'U08-082') addStudyComparison082(slide);
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

// artifact-tool conserva `alt` en el modelo y en inspect, pero algunas
// versiones del exportador no lo serializan en cNvPr. Reafirmarlo en el PPTX
// garantiza que PowerPoint y lectores de pantalla reciban la descripción.
const xmlAttr = (value) => String(value).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const zip = await JSZip.loadAsync(await fs.readFile(OUT));
for (let i = 0; i < slidesData.length; i += 1) {
  const d = slidesData[i];
  const asset = BLOCKED.has(d.id) ? undefined : assetForSlide(d, approved, byId);
  if (asset?.type !== 'chart') continue;
  const slidePath = `ppt/slides/slide${i + 1}.xml`;
  const part = zip.file(slidePath);
  if (!part) continue;
  const name = `${d.id}-${asset.asset_id}`;
  const alt = d.alt || asset.description || asset.title;
  let xml = await part.async('string');
  const escapedName = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  xml = xml.replace(new RegExp(`<p:cNvPr\\b([^>]*\\bname="${escapedName}"[^>]*)/?>`), (match, attrs) => {
    const cleaned = attrs.replace(/\sdescr="[^"]*"/g, '').replace(/\s*\/$/, '');
    return `<p:cNvPr${cleaned} descr="${xmlAttr(alt)}" />`;
  });
  zip.file(slidePath, xml);
}
await fs.writeFile(OUT, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE', compressionOptions: { level: 6 } }));
const inspect = await deck.inspect({ kind: 'deck,slide,textbox,shape,image,chart,table,notes,layout', include: 'id,slide,name,title,text,textPreview,textChars,bbox,bboxUnit,isPlaceholder,alt', maxChars: 2_000_000 });
await fs.writeFile(path.join(QA, 'final-inspect.ndjson'), inspect.ndjson, 'utf8');
await fs.writeFile(path.join(QA, 'build-log.json'), `${JSON.stringify({ output: OUT, slides: log, approvedAssetCount: approved.length }, null, 2)}\n`, 'utf8');
console.log(JSON.stringify({ output: OUT, slides: log.length, assetsInserted: log.filter((x) => x.asset).length, blocked: log.filter((x) => x.blocked).length }, null, 2));
