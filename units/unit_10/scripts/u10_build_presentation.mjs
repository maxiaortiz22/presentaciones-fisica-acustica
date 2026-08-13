import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [rootArg, starterArg, outArg, qaDirArg, workspaceArg] = process.argv.slice(2);
if (!rootArg || !starterArg || !outArg || !workspaceArg) {
  throw new Error('Uso: node u10_build_presentation.mjs <repoRoot> <starter.pptx> <out.pptx> <qaDir> <workspace>');
}

const ROOT = path.resolve(rootArg);
const UNIT = path.join(ROOT, 'units', 'unit_10');
const starterPptxPath = path.resolve(starterArg);
const OUT = path.resolve(outArg);
const QA = path.resolve(qaDirArg || path.join(path.dirname(OUT), 'qa'));
const WORKSPACE = path.resolve(workspaceArg);

const req = createRequire(path.join(WORKSPACE, 'package.json'));
const artifactEntry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(artifactEntry).href);
const runtimeReq = createRequire(artifactEntry);
const JSZip = runtimeReq('jszip');

const C = {
  berry: '#4D1434', berry2: '#903163', carbon: '#3D3D3D', gray: '#969FA7',
  lightGray: '#D9DCE0', ivory: '#F7F6F2', white: '#FFFFFF', teal: '#2F7E83',
  tealLight: '#E7F1F1', ochre: '#9F541A', ochreLight: '#F8EDE2',
  green: '#2F6F55', greenLight: '#E6F0EB', red: '#A33A3A', redLight: '#F7E8E6',
  alert: '#9A641E', accentLight: '#F3E8EE',
};

const BLOCKED_SLIDES = new Set(['U10-088', 'U10-091', 'U10-092']);
const BLOCKED_ASSETS = new Set(['U10-DG-058', 'U10-DG-059', 'U10-DG-060', 'U10-CH-016']);
const LOCAL_VISUAL_REPLACEMENTS = {
  'U10-088': 'Si los intervalos duran distinto, cada contribución debe ponderarse por su duración antes de volver a decibeles.',
  'U10-091': 'Una técnica completa exige indicaciones, niveles, incrementos, criterio de meseta, detención y control de sobreenmascaramiento definidos por un protocolo validado.',
  'U10-092': 'Primero deben coincidir norma, edición, jurisdicción, población, descriptor, ponderación, intervalo y regla aplicable.',
};

const clean = (value = '') => String(value)
  .replace(/`/g, '').replace(/\*+/g, '').replace(/\$/g, '')
  .replace(/\\(?:mathrm|text|operatorname)\{([^{}]+)\}/g, '$1')
  .replace(/\\left|\\right|\\bigl|\\bigr|\\displaystyle/g, '')
  .replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1)/($2)')
  .replace(/\\sqrt\{([^{}]+)\}/g, '√($1)')
  .replace(/\\rho/g, 'ρ').replace(/\\lambda/g, 'λ').replace(/\\pi/g, 'π')
  .replace(/\\theta/g, 'θ').replace(/\\psi/g, 'ψ').replace(/\\gamma/g, 'γ')
  .replace(/\\Delta/g, 'Δ').replace(/\\alpha/g, 'α').replace(/\\tau/g, 'τ')
  .replace(/\\times/g, '×').replace(/\\cdot/g, '·').replace(/\\approx/g, '≈')
  .replace(/\\propto/g, '∝').replace(/\\leq?/g, '≤').replace(/\\geq?/g, '≥')
  .replace(/\\Rightarrow/g, '⇒').replace(/\\rightarrow|\\to/g, '→')
  .replace(/\\log_\{10\}/g, 'log₁₀').replace(/\\sum_i/g, 'Σᵢ')
  .replace(/_\{([^{}]+)\}/g, '_$1').replace(/\^\{([^{}]+)\}/g, '^($1)')
  .replace(/_([A-Za-z0-9]+)/g, (_, token) => ({ p: 'ₚ', p1: 'ₚ₁', p2: 'ₚ₂', W: 'W', E: 'ₑ', eq: 'ₑq', atm: 'ₐₜₘ', ef: 'ₑf', dir: 'dir', s: 'ₛ', s1: 'ₛ₁', s2: 'ₛ₂', a: 'ₐ', i: 'ᵢ', 1: '₁', 2: '₂', 60: '₆₀', viento: ' viento' }[token] || `_${token}`))
  .replace(/\\[,;!]|\\quad|\\qquad/g, ' ').replace(/\\([{}])/g, '$1')
  .replace(/\\([A-Za-z]+)/g, '$1').replace(/[{}]/g, '').replace(/\s+/g, ' ').trim();

function parseSlideText(md) {
  const re = /^## (U10-\d{3})\s*$/gm;
  const matches = [...md.matchAll(re)];
  return matches.map((m, i) => {
    const block = md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length);
    const field = (name) => block.match(new RegExp(`^\\*\\*${name}:\\*\\*\\s*(.*)$`, 'mi'))?.[1]?.trim() || '';
    const section = (name) => block.match(new RegExp(`^### ${name}\\s*$\\n([\\s\\S]*?)(?=^### |(?![\\s\\S]))`, 'mi'))?.[1]?.trim() || '';
    const items = (text) => text.split(/\r?\n/)
      .map((line) => line.trim().replace(/^[-*]\s+/, '').replace(/^\d+[.)]\s+/, ''))
      .map(clean).filter((line) => line && line !== '—');
    const layout = clean(section('Layout')).split(/\s*·\s*/)[0];
    return {
      id: m[1], title: clean(section('Título')), subtitle: clean(section('Subtítulo')) === '—' ? '' : clean(section('Subtítulo')),
      route: clean(field('Estado del storyboard')), layout,
      content: items(section('Contenido visible')), equations: items(section('Ecuaciones')),
      definition: clean(section('Definiciones')), example: clean(section('Ejemplo')),
      visual: clean(section('Visual')), caption: clean(section('Caption sugerido')),
      source: clean(section('Fuente')), alt: clean(section('Texto alternativo')),
      transition: clean(section('Transición')),
    };
  });
}

function parseNotes(md) {
  const re = /^## (U10-\d{3}) · .+$/gm;
  const matches = [...md.matchAll(re)];
  return new Map(matches.map((m, i) => [m[1], md.slice(m.index + m[0].length, matches[i + 1]?.index ?? md.length).trim()]));
}

function parseCsv(text) {
  const rows = []; let row = []; let cell = ''; let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) { if (ch === '"' && text[i + 1] === '"') { cell += '"'; i += 1; } else if (ch === '"') quoted = false; else cell += ch; }
    else if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(cell); cell = ''; }
    else if (ch === '\n') { row.push(cell.replace(/\r$/, '')); rows.push(row); row = []; cell = ''; }
    else cell += ch;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const headers = rows.shift().map((h) => h.replace(/^\uFEFF/, ''));
  return rows.filter((r) => r.some(Boolean)).map((r) => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ''])));
}

function addShape(slide, { geometry = 'rect', name, x, y, w, h, fill = 'none', lineFill = 'none', lineWidth = 0, radius = 0 }) {
  return slide.shapes.add({ geometry, name, position: { left: x, top: y, width: w, height: h }, fill,
    line: { style: 'solid', fill: lineFill, width: lineWidth }, ...(radius ? { borderRadius: radius } : {}) });
}

function addText(slide, text, { x, y, w, h, size = 24, color = C.carbon, bold = false, align = 'left', valign = 'top', font = 'Calibri', name = 'text', fill = 'none', lineFill = 'none', lineWidth = 0, radius = 0, italic = false, insets = { top: 5, right: 7, bottom: 5, left: 7 } } = {}) {
  const shape = addShape(slide, { geometry: 'textbox', name, x, y, w, h, fill, lineFill, lineWidth, radius });
  shape.text = clean(text);
  shape.text.style = { fontSize: size, color, bold, italic, alignment: align, verticalAlignment: valign,
    typeface: font, autoFit: 'none', wrap: 'square', insets, lineSpacing: 1.05 };
  return shape;
}

function addTopRail(slide, d) {
  addShape(slide, { name: 'top-rail-1', x: 65, y: 27, w: 384, h: 5, fill: C.berry });
  addShape(slide, { name: 'top-rail-2', x: 459, y: 27, w: 384, h: 5, fill: C.berry2 });
  addShape(slide, { name: 'top-rail-3', x: 853, y: 27, w: 363, h: 5, fill: C.gray });
  const n = Number(d.id.slice(-3));
  const session = n <= 33 ? 'ENCUENTRO 1' : n <= 56 ? 'ENCUENTRO 2' : n <= 77 ? 'ENCUENTRO 3' : n <= 84 ? 'INTEGRACIÓN' : 'RESPALDO';
  const route = d.route === 'complementary' ? 'AMPLIACIÓN' : ['backup', 'blocked-source'].includes(d.route) ? 'A DEMANDA' : 'RUTA CENTRAL';
  addText(slide, `UNIDAD 10 · ${session} · ${route}`, { x: 50, y: 2, w: 560, h: 23, size: 13, color: C.berry2, bold: true, name: 'eyebrow', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
}

function addTitle(slide, d, dark = false) {
  const long = d.title.length > 54;
  const veryLong = d.title.length > 72;
  const subtitle = d.id === 'U10-092' ? 'Material de respaldo · criterios para aplicar un límite' : d.subtitle;
  addText(slide, d.title, { x: 76, y: long ? 42 : 48, w: 1126, h: long ? 88 : 60, size: veryLong ? 31 : long ? 34 : 36,
    color: dark ? C.white : C.berry, font: 'Calibri Light', name: 'slide-title', insets: { top: 0, right: 3, bottom: 0, left: 3 } });
  if (!long && subtitle) addText(slide, subtitle, { x: 79, y: 108, w: 1120, h: 28, size: 20,
    color: dark ? '#E7D7DF' : '#5E6267', name: 'slide-subtitle', insets: { top: 0, right: 3, bottom: 0, left: 3 } });
}

function addPage(slide, page, dark = false) {
  // Los layouts conservan el placeholder dinámico, pero no se visualiza en el
  // render de las slides importadas; se mantiene un número editable en el pie.
  addText(slide, String(page), { x: 1176, y: 680, w: 42, h: 17, size: 11, color: dark ? '#DFC9D4' : C.gray,
    align: 'right', name: 'slide-number', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
}

function addCaption(slide, d, assetId, dark = false) {
  if (!assetId) return;
  const base = d.caption || 'Recurso visual de producción propia.';
  const safe = base.length > 135 ? `${base.slice(0, 132).replace(/[\s,;:.]+$/, '')}…` : base;
  const text = safe;
  addText(slide, text, { x: 75, y: 625, w: 1125, h: 27, size: 13, color: dark ? '#E7D7DF' : '#5E6267', italic: true, align: 'center', name: 'caption', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
}

function addFooter(slide, d) {
  addText(slide, `Física Acústica · Unidad 10`, { x: 72, y: 682, w: 420, h: 16, size: 10, color: C.gray, name: 'unit-footer', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
}

async function clearSlide(slide) {
  slide.shapes.deleteAll();
  for (const image of [...slide.images.items]) slide.images.deleteById(image.id);
  for (const collection of [slide.tables, slide.charts]) if (collection?.items) for (const item of [...collection.items]) {
    if (typeof item.delete === 'function') item.delete(); else if (typeof collection.deleteById === 'function') collection.deleteById(item.id);
  }
}

function styleForNode(style) {
  if (style === 'physical') return { fill: C.tealLight, line: C.teal, text: C.teal };
  if (style === 'clinical') return { fill: C.ochreLight, line: C.ochre, text: C.ochre };
  if (style === 'accent') return { fill: C.accentLight, line: C.berry, text: C.berry };
  if (style === 'equation') return { fill: C.white, line: C.berry, text: C.berry };
  return { fill: C.ivory, line: C.gray, text: C.carbon };
}

async function addDiagram(slide, d, asset, { dark = false } = {}) {
  const modelPath = path.join(ROOT, asset.local_path, 'diagram_source.json');
  const model = JSON.parse(await fs.readFile(modelPath, 'utf8'));
  const sx = 0.92, sy = 0.82, ox = 88, oy = 153;
  const p = (n) => ({ x: ox + (n.x - 80) * sx, y: oy + (n.y - 125) * sy, w: n.w * sx, h: n.h * sy });
  const anchors = new Map();
  for (const n of model.nodes) {
    const q = p(n);
    anchors.set(n.id, addShape(slide, { geometry: 'rect', name: `${asset.asset_id}-${n.id}-anchor`, x: q.x, y: q.y, w: q.w, h: q.h, fill: 'none', lineFill: 'none' }));
  }
  for (const e of model.edges) {
    const connector = slide.shapes.connect(anchors.get(e.from), anchors.get(e.to), { kind: 'elbow', fromSide: e.fromSide, toSide: e.toSide,
      line: { style: 'solid', fill: dark ? C.white : C.carbon, width: 2 }, tail: { type: 'arrow', width: 'med', length: 'med' } });
    connector.name = `${asset.asset_id}-${e.id}`;
  }
  let first = true;
  for (const n of model.nodes) {
    const q = p(n); const s = styleForNode(n.style);
    addShape(slide, { geometry: 'roundRect', name: first ? `${asset.asset_id}-visual-alt` : `${asset.asset_id}-${n.id}-box`,
      x: q.x, y: q.y, w: q.w, h: q.h, fill: s.fill, lineFill: s.line, lineWidth: 1.5, radius: 7 });
    first = false;
    addText(slide, n.title, { x: q.x + 18, y: q.y + 13, w: q.w - 36, h: q.h - 26,
      // artifact-tool serializa la tipografía aproximadamente al 79,8 % del
      // valor solicitado. Esta compensación mantiene 22 pt reales como mínimo
      // y 28 pt reales para las ecuaciones centrales en el PPTX exportado.
      size: Math.max(n.role === 'equation' ? 36 : 28, n.font * 1.1), color: s.text, bold: n.role !== 'equation',
      align: 'center', valign: 'middle', font: n.role === 'equation' ? 'Cambria Math' : 'Calibri', name: `${asset.asset_id}-${n.id}-text`,
      insets: { top: 3, right: 5, bottom: 3, left: 5 } });
  }
  addCaption(slide, d, asset.asset_id, dark);
  return { type: 'diagram', asset: asset.asset_id, alt: d.alt || model.alt };
}

async function addCoverDiagram(slide, d, asset) {
  const modelPath = path.join(ROOT, asset.local_path, 'diagram_source.json');
  const model = JSON.parse(await fs.readFile(modelPath, 'utf8'));
  const nodes = model.nodes.slice(0, 4);
  nodes.forEach((n, index) => {
    const x = 82 + index * 287;
    const s = styleForNode(n.style);
    addShape(slide, { geometry: 'roundRect', name: index === 0 ? `${asset.asset_id}-visual-alt` : `${asset.asset_id}-${n.id}-box`,
      x, y: 590, w: 260, h: 62, fill: s.fill, lineFill: s.line, lineWidth: 1.5, radius: 7 });
    addText(slide, n.title, { x: x + 16, y: 600, w: 228, h: 42, size: 30, color: s.text, bold: true,
      align: 'center', valign: 'middle', name: `${asset.asset_id}-${n.id}-text`, insets: { top: 2, right: 4, bottom: 2, left: 4 } });
  });
  return { type: 'diagram', asset: asset.asset_id, alt: d.alt || model.alt };
}

async function addChart(slide, d, asset) {
  const svgPath = path.join(ROOT, asset.local_path, 'figure.svg');
  const bytes = await fs.readFile(svgPath);
  const image = slide.images.add({ blob: bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), contentType: 'image/svg+xml',
    alt: d.alt || asset.description || asset.title, fit: 'contain', position: { left: 62, top: 155, width: 740, height: 445 } });
  image.name = `${asset.asset_id}-chart`;
  addShape(slide, { geometry: 'roundRect', name: 'chart-reading-box', x: 835, y: 190, w: 360, h: 290, fill: C.ivory, lineFill: C.lightGray, lineWidth: 1, radius: 6 });
  addText(slide, 'Qué observar', { x: 865, y: 220, w: 300, h: 40, size: 25, color: C.berry, bold: true, name: 'chart-reading-title' });
  const points = d.content.slice(0, 3).join('\n\n');
  addText(slide, points, { x: 865, y: 278, w: 300, h: 170, size: 22, color: C.carbon, name: 'chart-reading-body' });
  addCaption(slide, d, asset.asset_id);
  return { type: 'chart', asset: asset.asset_id, alt: d.alt || asset.description };
}

async function addComposite078(slide, d, diagramAsset, chartAsset) {
  const chartPath = path.join(ROOT, chartAsset.local_path, 'figure.svg');
  const chartBytes = await fs.readFile(chartPath);
  const chart = slide.images.add({ blob: chartBytes.buffer.slice(chartBytes.byteOffset, chartBytes.byteOffset + chartBytes.byteLength),
    contentType: 'image/svg+xml', alt: 'Lectura temporal y frecuencial cuantitativa del caso.', fit: 'contain',
    position: { left: 45, top: 158, width: 755, height: 430 } });
  chart.name = `${chartAsset.asset_id}-chart`;
  const summaries = [
    ['Tránsito · ventana larga · Lₑq,T', 'physical'],
    ['Climatización · ventana estable · Lₑq,T', 'accent'],
    ['Portazos · ventana de evento · Lₚₑₐₖ / Lₘₐₓ', 'clinical'],
  ];
  summaries.forEach(([label, kind], index) => {
    const style = styleForNode(kind);
    addText(slide, label, { x: 835, y: 190 + index * 128, w: 365, h: 96, size: 28,
      color: style.text, bold: true, align: 'center', valign: 'middle', fill: style.fill,
      lineFill: style.line, lineWidth: 1.3, radius: 6, name: `case-temporal-${index}`,
      insets: { top: 8, right: 12, bottom: 8, left: 12 } });
  });
  addText(slide, 'Caso simulado: ventanas temporales, trazas y elección del descriptor; niveles relativos, no mediciones.', { x: 75, y: 625, w: 1125, h: 27,
    size: 13, color: '#5E6267', italic: true, align: 'center', name: 'caption', insets: { top: 0, right: 2, bottom: 0, left: 2 } });
  return { type: 'chart', asset: chartAsset.asset_id, alt: d.alt };
}

function addBlocked(slide, d) {
  addShape(slide, { geometry: 'roundRect', name: `${d.id}-blocked-alt`, x: 150, y: 185, w: 980, h: 345, fill: C.ivory, lineFill: C.gray, lineWidth: 2, radius: 8 });
  addText(slide, 'Material no habilitado para proyección', { x: 210, y: 225, w: 860, h: 55, size: 34, color: C.berry, bold: true, align: 'center', name: 'blocked-heading' });
  addText(slide, d.content.join('\n\n'), { x: 250, y: 315, w: 780, h: 135, size: 25, color: C.carbon, align: 'center', valign: 'middle', name: 'blocked-message' });
  addText(slide, 'Fuente o convención pendiente', { x: 430, y: 470, w: 420, h: 38, size: 22, color: C.red, bold: true, align: 'center', name: 'blocked-label' });
}

function addConditional(slide, d) {
  addShape(slide, { geometry: 'roundRect', name: `${d.id}-conditional-alt`, x: 110, y: 180, w: 1060, h: 360, fill: C.ivory, lineFill: C.alert, lineWidth: 1.5, radius: 7 });
  const headings = {
    'U10-088': 'Principio cualitativo',
    'U10-091': 'Límite de alcance clínico',
    'U10-092': 'Antes de comparar un límite',
  };
  addText(slide, headings[d.id] || 'Condición de uso',
    { x: 170, y: 220, w: 940, h: 54, size: 32, color: C.berry, bold: true, align: 'center', name: 'conditional-title' });
  addText(slide, LOCAL_VISUAL_REPLACEMENTS[d.id], { x: 210, y: 315, w: 860, h: 120, size: 25, color: C.carbon, align: 'center', valign: 'middle', name: 'conditional-message' });
  const footers = {
    'U10-088': 'No se muestra una fórmula ni un ejemplo sin fuente verificada.',
    'U10-091': 'No sustituye el entrenamiento ni el protocolo institucional.',
    'U10-092': 'No fusionar normas o jurisdicciones en una curva única.',
  };
  addText(slide, footers[d.id] || '', { x: 250, y: 465, w: 780, h: 40, size: 21, color: C.alert, bold: true, align: 'center', name: 'conditional-foot' });
}

function audienceItems(d, max = 5) {
  const reject = /^(ecuación|símbolos|pregunta guía|reconstrucción|tarjetas|secuencia de cálculo|dos columnas|matriz|estructura del gráfico|placeholder)/i;
  const items = d.content.filter((x) => x && !reject.test(x));
  if (d.definition && !/^No se introduce/i.test(d.definition)) items.push(d.definition);
  if (d.example && !/^No corresponde/i.test(d.example)) items.push(d.example);
  return [...new Set(items)].slice(0, max);
}

function panel(slide, title, body, { x, y, w, h, kind = 'neutral', titleSize = 25, bodySize = 22, name = 'panel' }) {
  const s = styleForNode(kind === 'physical' ? 'physical' : kind === 'clinical' ? 'clinical' : kind === 'accent' ? 'accent' : 'neutral');
  addShape(slide, { geometry: 'roundRect', name: `${name}-box`, x, y, w, h, fill: s.fill, lineFill: s.line, lineWidth: 1.3, radius: 6 });
  addText(slide, title, { x: x + 22, y: y + 18, w: w - 44, h: 42, size: titleSize, color: s.text, bold: true, name: `${name}-title` });
  addText(slide, body, { x: x + 22, y: y + 72, w: w - 44, h: h - 92, size: bodySize, color: C.carbon, name: `${name}-body` });
}

function addGeneric(slide, d) {
  const items = audienceItems(d, 6);
  const equation = d.equations.find((x) => !/^No corresponde/i.test(x) && !/bloqueado|pendiente/i.test(x));
  if (d.layout === 'FA_09_ECUACION_INTERPRETACION' && equation) {
    addShape(slide, { geometry: 'roundRect', name: `${d.id}-equation-alt`, x: 90, y: 180, w: 710, h: 190, fill: C.ivory, lineFill: C.berry2, lineWidth: 1.5, radius: 6 });
    addText(slide, equation, { x: 125, y: 225, w: 640, h: 100, size: 36, color: C.berry, font: 'Cambria Math', align: 'center', valign: 'middle', name: 'equation-main' });
    panel(slide, 'Interpretación física', items[0] || d.definition, { x: 850, y: 180, w: 350, h: 190, kind: 'physical', name: 'equation-meaning' });
    panel(slide, 'Condiciones y unidades', d.equations.slice(1).join('\n\n') || items.slice(1, 3).join('\n\n'), { x: 90, y: 410, w: 1110, h: 175, kind: 'clinical', name: 'equation-conditions' });
    return;
  }
  if (d.layout === 'FA_10_EJEMPLO_RESUELTO' || d.layout === 'FA_14B_MINI_EJERCICIO') {
    const steps = [...d.equations.filter((x) => !/^No corresponde/i.test(x)), ...items].slice(0, 4);
    const w = 250, gap = 25;
    const anchors = steps.map((_, i) => addShape(slide, { geometry: 'rect', name: `step-anchor-${i}`, x: 78 + i * (w + gap), y: 220, w, h: 230, fill: 'none', lineFill: 'none' }));
    for (let i = 0; i < anchors.length - 1; i += 1) slide.shapes.connect(anchors[i], anchors[i + 1], { kind: 'straight', fromSide: 'right', toSide: 'left', line: { style: 'solid', fill: C.berry2, width: 2 }, tail: { type: 'arrow' } });
    steps.forEach((text, i) => panel(slide, `${i + 1}`, text, { x: 78 + i * (w + gap), y: 220, w, h: 230, kind: ['physical', 'accent', 'neutral', 'clinical'][i % 4], name: `step-${i}`, bodySize: 22 }));
    return;
  }
  if (d.layout === 'FA_11_COMPARACION') {
    const half = Math.max(1, Math.ceil(items.length / 2));
    panel(slide, 'Primera lectura', items.slice(0, half).join('\n\n'), { x: 75, y: 170, w: 535, h: 390, kind: 'physical', name: 'compare-a', bodySize: 23 });
    panel(slide, 'Segunda lectura', items.slice(half).join('\n\n') || d.definition, { x: 670, y: 170, w: 535, h: 390, kind: 'clinical', name: 'compare-b', bodySize: 23 });
    return;
  }
  if (d.layout === 'FA_15_ERROR_FRECUENTE') {
    panel(slide, 'Es frecuente pensar…', d.title, { x: 90, y: 175, w: 1100, h: 150, kind: 'accent', name: 'error', bodySize: 28 });
    panel(slide, 'En realidad…', items[0] || d.definition, { x: 90, y: 360, w: 1100, h: 205, kind: 'physical', name: 'correction', bodySize: 26 });
    return;
  }
  if (d.layout === 'FA_18_TABLA_DATOS' || d.layout === 'FA_20_BIBLIO_RECURSOS') {
    const rows = items.length ? items : [d.source];
    rows.slice(0, 6).forEach((text, i) => {
      addShape(slide, { name: `row-${i}-bg`, x: 100, y: 165 + i * 70, w: 1080, h: 55, fill: i % 2 ? C.ivory : C.white, lineFill: C.lightGray, lineWidth: 0.8 });
      addText(slide, text, { x: 125, y: 176 + i * 70, w: 1030, h: 36, size: 21, color: C.carbon, name: `row-${i}` });
    });
    return;
  }
  if (d.layout === 'FA_19_MEDIA_AUDIO_VIDEO') {
    addShape(slide, { geometry: 'roundRect', name: `${d.id}-media-alt`, x: 80, y: 170, w: 740, h: 405, fill: C.ivory, lineFill: C.lightGray, lineWidth: 1.5, radius: 6 });
    addText(slide, 'Alternativa estática', { x: 130, y: 220, w: 640, h: 45, size: 28, color: C.berry, bold: true, align: 'center', name: 'media-static-title' });
    addText(slide, items.join('\n\n'), { x: 150, y: 300, w: 600, h: 170, size: 24, color: C.carbon, align: 'center', valign: 'middle', name: 'media-static-body' });
    panel(slide, 'Recurso identificado', 'Audio breve de habla seca y reverberada. No está embebido en v01; la slide funciona sin reproducción.', { x: 860, y: 205, w: 330, h: 300, kind: 'clinical', name: 'media-note', bodySize: 22 });
    return;
  }
  const shown = items.length ? items : [d.definition || d.example || 'Contenido desarrollado en las notas del orador.'];
  addText(slide, shown[0], { x: 95, y: 170, w: 1090, h: 90, size: 29, color: C.berry, bold: true, name: `${d.id}-claim-alt`, valign: 'middle' });
  shown.slice(1, 5).forEach((text, i) => {
    addShape(slide, { geometry: 'ellipse', name: `bullet-${i}`, x: 110, y: 300 + i * 68, w: 10, h: 10, fill: C.berry2 });
    addText(slide, text, { x: 145, y: 285 + i * 68, w: 1010, h: 50, size: 23, color: C.carbon, name: `body-${i}` });
  });
}

// Las composiciones especiales de otras unidades no se reutilizan: el
// contenido U10 sigue sus assets y layouts aprobados.
const CUSTOM_SLIDES = new Set();

function customBase(slide, d) {
  addShape(slide, { geometry: 'roundRect', name: `${d.id}-claim-alt`, x: 72, y: 155, w: 1136, h: 450, fill: C.white, lineFill: 'none', radius: 4 });
}

function threeCards(slide, cards, { y = 185, h = 340 } = {}) {
  cards.forEach((card, i) => panel(slide, card[0], card[1], {
    x: 80 + i * 386, y, w: 350, h,
    kind: ['physical', 'accent', 'clinical'][i % 3], name: `custom-card-${i}`,
    titleSize: 25, bodySize: 22,
  }));
}

function twoCards(slide, left, right, { y = 180, h = 365 } = {}) {
  panel(slide, left[0], left[1], { x: 80, y, w: 535, h, kind: 'physical', name: 'custom-left', bodySize: 23 });
  panel(slide, right[0], right[1], { x: 665, y, w: 535, h, kind: 'clinical', name: 'custom-right', bodySize: 23 });
}

function addCustomSlide(slide, d) {
  if (!CUSTOM_SLIDES.has(d.id)) return false;
  customBase(slide, d);
  switch (d.id) {
    case 'U10-008':
      threeCards(slide, [
        ['Fuente', 'Potencia emitida, espectro y directividad. Describe el origen, no el nivel que llegará.'],
        ['Trayecto', 'Distancia, atmósfera, superficies y obstáculos modifican la propagación.'],
        ['Receptor', 'El nivel se define en un punto, una dirección, una banda y un instante.'],
      ]);
      addText(slide, 'Emitir y recibir son magnitudes distintas: entre ambas siempre hay un trayecto.', { x: 125, y: 548, w: 1030, h: 40, size: 24, color: C.berry, bold: true, align: 'center', name: 'custom-conclusion' });
      break;
    case 'U10-025':
      threeCards(slide, [
        ['Aire más cálido', 'La rapidez del sonido es mayor.'],
        ['Gradiente vertical', 'La rapidez cambia con la altura; el medio deja de ser uniforme.'],
        ['Trayectoria', 'El rayo se curva hacia la región donde la rapidez es menor.'],
      ]);
      addText(slide, 'No es una fuerza lateral: es refracción continua por cambio espacial de rapidez.', { x: 150, y: 548, w: 980, h: 40, size: 24, color: C.berry, bold: true, align: 'center', name: 'gradient-key' });
      break;
    case 'U10-027':
      twoCards(slide,
        ['A favor del viento', 'La rapidez efectiva aumenta con la altura si el viento se intensifica; la trayectoria puede curvarse hacia el suelo.'],
        ['Contra el viento', 'La rapidez efectiva cambia en sentido opuesto; puede aparecer una zona de sombra cerca del suelo.']);
      addText(slide, 'Importa el gradiente de viento y la dirección de propagación, no solo “cuánto viento hay”.', { x: 110, y: 565, w: 1060, h: 34, size: 22, color: C.berry, bold: true, align: 'center', name: 'wind-key' });
      break;
    case 'U10-030':
      twoCards(slide,
        ['Divergencia geométrica', 'Redistribuye la energía en una superficie cada vez mayor. En campo libre: −6 dB por duplicar la distancia.'],
        ['Absorción atmosférica', 'Convierte parte de la energía acústica en calor. Depende de frecuencia, temperatura, humedad, presión y distancia.']);
      addText(slide, 'Ambos efectos pueden acumularse, pero describen mecanismos físicos diferentes.', { x: 130, y: 560, w: 1020, h: 36, size: 23, color: C.berry, bold: true, align: 'center', name: 'loss-key' });
      break;
    case 'U10-037':
      addText(slide, 'Balance energético en una interfaz', { x: 120, y: 180, w: 1040, h: 44, size: 28, color: C.berry, bold: true, align: 'center', name: 'balance-heading' });
      threeCards(slide, [
        ['Dato 1', 'Reflexión\nRₑ = 0,55'],
        ['Dato 2', 'Absorción\nα = 0,30'],
        ['Fracción transmitida', 'τₑ = 1 − Rₑ − α = 0,15'],
      ], { y: 245, h: 235 });
      addText(slide, 'Comprobación: 0,55 + 0,30 + 0,15 = 1,00.', { x: 240, y: 515, w: 800, h: 44, size: 26, color: C.green, bold: true, align: 'center', name: 'balance-check' });
      break;
    case 'U10-038':
      twoCards(slide,
        ['Qué permanece', 'El mecanismo sigue siendo reflexión: la onda regresa al medio de incidencia.'],
        ['Qué cambia', 'Cambia la dirección. En una superficie plana, el ángulo reflejado es igual al incidente, medidos desde la normal.']);
      addText(slide, 'Incidencia → superficie → reflexión', { x: 260, y: 555, w: 760, h: 40, size: 28, color: C.berry, bold: true, align: 'center', name: 'reflection-sequence' });
      break;
    case 'U10-039':
      threeCards(slide, [
        ['Reflexión', 'Fenómeno físico: parte de la energía vuelve al medio de origen.'],
        ['Eco', 'Reflexión distinguible temporalmente del sonido directo.'],
        ['Reverberación', 'Conjunto denso de reflexiones que prolonga el decaimiento sonoro.'],
      ]);
      break;
    case 'U10-041':
      twoCards(slide,
        ['Relación geométrica', 'Al atravesar una interfaz cambia la dirección transmitida cuando cambia la rapidez de fase. Los ángulos se miden desde la normal.'],
        ['Lectura segura', 'Mayor diferencia de rapidez implica mayor cambio angular. El esquema es cualitativo: no calcula conversión modal ni reemplaza una fuente normativa.']);
      addText(slide, 'Refracción = cambio de dirección por cambio de rapidez de propagación.', { x: 150, y: 558, w: 980, h: 38, size: 24, color: C.berry, bold: true, align: 'center', name: 'snell-key' });
      break;
    case 'U10-044':
      threeCards(slide, [
        ['125 Hz', 'λ ≈ 2,74 m\nLa barrera es pequeña respecto de λ: la difracción es importante.'],
        ['500 Hz', 'λ ≈ 0,686 m\nLa barrera y λ son comparables: comportamiento intermedio.'],
        ['4000 Hz', 'λ ≈ 0,0858 m\nLa barrera es grande respecto de λ: la sombra es más marcada.'],
      ]);
      addText(slide, 'Misma geometría, distinta relación tamaño/longitud de onda.', { x: 190, y: 548, w: 900, h: 40, size: 24, color: C.berry, bold: true, align: 'center', name: 'barrier-key' });
      break;
    case 'U10-050':
      addText(slide, 'Aₑq = Σᵢ αᵢ Sᵢ', { x: 260, y: 180, w: 760, h: 80, size: 40, color: C.berry, font: 'Cambria Math', bold: true, align: 'center', valign: 'middle', name: 'aeq-formula' });
      threeCards(slide, [
        ['Sᵢ', 'Área de la superficie i\nUnidad: m²'],
        ['αᵢ', 'Coeficiente de absorción de esa superficie\nSin unidad'],
        ['Aₑq', 'Área equivalente de absorción\nUnidad: m² sabin'],
      ], { y: 300, h: 225 });
      addText(slide, 'La suma pondera cada superficie por su capacidad de absorber.', { x: 190, y: 553, w: 900, h: 34, size: 23, color: C.berry, bold: true, align: 'center', name: 'aeq-key' });
      break;
    case 'U10-051':
      addText(slide, 'T₆₀ = 0,161 · V / Aₑq', { x: 210, y: 175, w: 860, h: 86, size: 42, color: C.berry, font: 'Cambria Math', bold: true, align: 'center', valign: 'middle', name: 'sabine-formula' });
      twoCards(slide,
        ['Volumen V', 'Más volumen implica más energía almacenada y, si Aₑq no cambia, un decaimiento más lento.\nUnidad: m³'],
        ['Absorción Aₑq', 'Más absorción equivalente acelera el decaimiento y reduce T₆₀.\nUnidad: m² sabin'],
        { y: 295, h: 250 });
      addText(slide, 'T₆₀ se expresa en segundos y describe reverberación, no aislamiento.', { x: 150, y: 560, w: 980, h: 36, size: 23, color: C.berry, bold: true, align: 'center', name: 'sabine-key' });
      break;
    case 'U10-052':
      addText(slide, 'V = 8 · 6 · 3 = 144 m³', { x: 95, y: 178, w: 510, h: 54, size: 29, color: C.berry, font: 'Cambria Math', bold: true, name: 'example-volume' });
      addText(slide, 'Sₜₒₜ = 2(8·6 + 8·3 + 6·3) = 180 m²', { x: 95, y: 245, w: 535, h: 70, size: 25, color: C.carbon, font: 'Cambria Math', name: 'example-area' });
      addText(slide, 'Con ᾱ = 0,25:', { x: 95, y: 330, w: 430, h: 45, size: 25, color: C.carbon, bold: true, name: 'example-alpha' });
      addText(slide, 'Aₑq = ᾱ · Sₜₒₜ = 45 m² sabin', { x: 95, y: 385, w: 535, h: 55, size: 27, color: C.berry, font: 'Cambria Math', name: 'example-aeq' });
      panel(slide, 'Resultado', 'T₆₀ = 0,161 · 144 / 45 ≈ 0,52 s', { x: 690, y: 190, w: 450, h: 255, kind: 'physical', name: 'example-result', titleSize: 28, bodySize: 26 });
      addText(slide, 'Interpretación: el resultado estima el decaimiento reverberante bajo los supuestos de Sabine.', { x: 105, y: 505, w: 1070, h: 65, size: 23, color: C.carbon, align: 'center', valign: 'middle', name: 'example-interpretation' });
      break;
    case 'U10-054':
      twoCards(slide,
        ['Acondicionamiento', 'Modifica el campo sonoro dentro del recinto: absorción, reflexiones y T₆₀.'],
        ['Aislamiento', 'Reduce la transmisión entre recintos o desde el exterior. Depende de cerramientos y vías laterales.']);
      addText(slide, 'Un T₆₀ corto no demuestra por sí solo que el ruido exterior esté suficientemente atenuado.', { x: 125, y: 555, w: 1030, h: 48, size: 24, color: C.red, bold: true, align: 'center', name: 'conditioning-error' });
      break;
    case 'U10-055':
      twoCards(slide,
        ['Habla seca', 'Decaimiento rápido. Las sílabas sucesivas se superponen menos.'],
        ['Habla reverberada', 'La energía persiste; aumenta el enmascaramiento temporal entre segmentos.']);
      addText(slide, 'Actividad: escuchar una frase en ambas condiciones y señalar qué consonantes pierden claridad.', { x: 135, y: 555, w: 1010, h: 44, size: 23, color: C.berry, bold: true, align: 'center', name: 'media-activity' });
      break;
    case 'U10-059':
      addText(slide, 'R = 10 log₁₀(1 / τₑ)', { x: 260, y: 175, w: 760, h: 82, size: 42, color: C.berry, font: 'Cambria Math', bold: true, align: 'center', valign: 'middle', name: 'reduction-formula' });
      threeCards(slide, [
        ['τₑ = 0,1', 'R = 10 dB'],
        ['τₑ = 0,01', 'R = 20 dB'],
        ['τₑ = 0,001', 'R = 30 dB'],
      ], { y: 300, h: 190 });
      addText(slide, 'Cada reducción de τₑ por un factor 10 suma 10 dB de reducción sonora.', { x: 150, y: 535, w: 980, h: 45, size: 24, color: C.berry, bold: true, align: 'center', name: 'log-key' });
      break;
    case 'U10-063':
      addText(slide, 'ΔR ≈ 20 log₁₀(mₛ₂ / mₛ₁)', { x: 180, y: 170, w: 920, h: 82, size: 39, color: C.berry, font: 'Cambria Math', bold: true, align: 'center', valign: 'middle', name: 'mass-law-formula' });
      twoCards(slide,
        ['Lectura relativa', 'Si la masa superficial se duplica, la reducción ideal aumenta aproximadamente 6 dB.'],
        ['Límite del modelo', 'La tendencia ideal no incluye resonancias, coincidencia, uniones, aberturas ni transmisión lateral.'],
        { y: 290, h: 250 });
      addText(slide, 'Usar la ley para comparar tendencias; no para certificar un cerramiento real.', { x: 155, y: 558, w: 970, h: 36, size: 23, color: C.berry, bold: true, align: 'center', name: 'mass-law-key' });
      break;
    case 'U10-065':
      threeCards(slide, [
        ['Bajas frecuencias', 'La rigidez y las resonancias dominan: la recta ideal no describe bien el sistema.'],
        ['Región de masa', 'La tendencia ideal crece cerca de 6 dB por octava al aumentar la frecuencia.'],
        ['Altas frecuencias', 'Coincidencia, estructura y vías laterales pueden reducir el desempeño esperado.'],
      ]);
      addText(slide, 'Curva conceptual: las regiones dependen del elemento y de sus condiciones de montaje.', { x: 130, y: 548, w: 1020, h: 42, size: 23, color: C.berry, bold: true, align: 'center', name: 'mass-regions-key' });
      break;
    case 'U10-066':
      threeCards(slide, [
        ['Pared', 'Buen desempeño del paño opaco.'],
        ['Puerta y sellos', 'Una abertura o junta débil puede dominar el resultado global.'],
        ['Sistema completo', 'El aislamiento se evalúa con todas las vías: directa, laterales y fugas.'],
      ]);
      addText(slide, 'El conjunto no aísla mejor que su vía dominante de transmisión.', { x: 190, y: 548, w: 900, h: 40, size: 24, color: C.berry, bold: true, align: 'center', name: 'weak-link-key' });
      break;
    case 'U10-070': {
      const nodes = [
        ['Envolvente', 105, 190], ['Puerta y sellos', 105, 430], ['Visor', 465, 175],
        ['Ventilación', 825, 190], ['Pasacables', 825, 430], ['Apoyos y juntas', 465, 455],
      ];
      const coreAnchor = addShape(slide, { geometry: 'rect', name: 'booth-core-anchor', x: 505, y: 300, w: 270, h: 90, fill: 'none', lineFill: 'none' });
      const nodeAnchors = nodes.map(([, x, y], i) => addShape(slide, { geometry: 'rect', name: `booth-node-anchor-${i}`, x, y, w: 310, h: 70, fill: 'none', lineFill: 'none' }));
      nodeAnchors.forEach((node) => slide.shapes.connect(coreAnchor, node, { kind: 'straight', line: { style: 'solid', fill: C.gray, width: 1.5 } }));
      addText(slide, 'CABINA', { x: 505, y: 300, w: 270, h: 90, size: 34, color: C.white, fill: C.berry, bold: true, align: 'center', valign: 'middle', name: 'booth-core' });
      nodes.forEach(([t, x, y], i) => addText(slide, t, { x, y, w: 310, h: 70, size: 22, color: i % 2 ? C.ochre : C.teal, fill: i % 2 ? C.ochreLight : C.tealLight, lineFill: i % 2 ? C.ochre : C.teal, lineWidth: 1.2, bold: true, align: 'center', valign: 'middle', name: `booth-node-${i}` }));
      addText(slide, 'La aptitud depende del sistema y de la verificación acústica, no de una sola pared.', { x: 135, y: 555, w: 1010, h: 40, size: 23, color: C.berry, bold: true, align: 'center', name: 'booth-key' });
      break;
    }
    case 'U10-073':
      twoCards(slide,
        ['Nivel global dB(A)', 'Resume la energía con ponderación A en un único número.\n\nÚtil para una visión general; oculta la distribución espectral.'],
        ['Niveles por bandas', 'Muestran dónde se concentra el ruido y permiten comparar cada banda con el criterio aplicable.\n\nSon necesarios para diagnosticar y decidir.']);
      addText(slide, 'Un mismo dB(A) puede corresponder a espectros muy distintos.', { x: 195, y: 555, w: 890, h: 40, size: 24, color: C.berry, bold: true, align: 'center', name: 'bands-key' });
      break;
    case 'U10-076':
      threeCards(slide, [
        ['Cierre', 'Revisar sellos de puerta y visor; buscar luz visible, holguras y discontinuidades.'],
        ['Servicios', 'Observar ventilación, pasacables y equipos que puedan generar o transmitir ruido.'],
        ['Estructura', 'Identificar juntas, apoyos rígidos y posibles vías laterales hacia el recinto.'],
      ]);
      addText(slide, 'La inspección orienta hipótesis; la aptitud se confirma mediante medición según el protocolo aplicable.', { x: 115, y: 548, w: 1050, h: 52, size: 23, color: C.berry, bold: true, align: 'center', name: 'inspection-key' });
      break;
    case 'U10-086': {
      const rows = [
        ['Rₑ', 'coeficiente energético de reflexión', 'sin unidad'], ['α', 'coeficiente de absorción', 'sin unidad'],
        ['τₑ', 'coeficiente energético de transmisión', 'sin unidad'], ['Aₑq', 'área equivalente de absorción', 'm² sabin'],
        ['T₆₀', 'tiempo de reverberación', 's'], ['R (dB)', 'índice de reducción sonora', 'dB'],
      ];
      addText(slide, 'Símbolo', { x: 100, y: 165, w: 190, h: 40, size: 22, color: C.white, fill: C.berry, bold: true, align: 'center', name: 'notation-h1' });
      addText(slide, 'Significado', { x: 290, y: 165, w: 650, h: 40, size: 22, color: C.white, fill: C.berry, bold: true, align: 'center', name: 'notation-h2' });
      addText(slide, 'Unidad', { x: 940, y: 165, w: 240, h: 40, size: 22, color: C.white, fill: C.berry, bold: true, align: 'center', name: 'notation-h3' });
      rows.forEach((r, i) => {
        const y = 215 + i * 58; const fill = i % 2 ? C.ivory : C.white;
        addText(slide, r[0], { x: 100, y, w: 190, h: 48, size: 22, color: C.berry, fill, lineFill: C.lightGray, lineWidth: 0.7, bold: true, align: 'center', valign: 'middle', name: `notation-s-${i}` });
        addText(slide, r[1], { x: 290, y, w: 650, h: 48, size: 21, color: C.carbon, fill, lineFill: C.lightGray, lineWidth: 0.7, valign: 'middle', name: `notation-m-${i}` });
        addText(slide, r[2], { x: 940, y, w: 240, h: 48, size: 21, color: C.carbon, fill, lineFill: C.lightGray, lineWidth: 0.7, align: 'center', valign: 'middle', name: `notation-u-${i}` });
      });
      break;
    }
    case 'U10-087':
      twoCards(slide,
        ['Distancia', 'Dato: 76 dB SPL a 2 m. Estimar a 10 m.\n\nΔL = −20 log₁₀(10/2) = −13,98 dB\n\nResultado: ≈ 62 dB SPL.'],
        ['Directividad', 'Dato: Q = 8.\n\nDI = 10 log₁₀(8) = 9,03 dB\n\nInterpretación: ganancia direccional ideal respecto de una fuente omnidireccional.'],
        { y: 175, h: 400 });
      break;
    case 'U10-088':
      threeCards(slide, [
        ['Frecuencia', 'La atenuación atmosférica suele crecer hacia frecuencias altas.'],
        ['Estado del aire', 'Temperatura, humedad y presión modifican la absorción molecular.'],
        ['Distancia', 'El efecto se acumula a lo largo del trayecto y se suma a la divergencia.'],
      ]);
      addText(slide, 'No hay una curva universal: para calcular se deben declarar condiciones y fuente de datos.', { x: 120, y: 548, w: 1040, h: 44, size: 23, color: C.berry, bold: true, align: 'center', name: 'atm-key' });
      break;
    case 'U10-089':
      twoCards(slide,
        ['Ondas longitudinales', 'El movimiento de las partículas es paralelo a la propagación; pueden propagarse en fluidos y sólidos.'],
        ['Ondas transversales', 'El movimiento es perpendicular a la propagación; requieren un medio con rigidez al corte, como un sólido.']);
      addText(slide, 'En una interfaz sólida pueden coexistir modos; la partición depende de material, geometría y ángulo.', { x: 120, y: 550, w: 1040, h: 48, size: 23, color: C.berry, bold: true, align: 'center', name: 'mode-key' });
      break;
    case 'U10-090':
      twoCards(slide,
        ['Balance en interfaz', 'Rₑ = 0,55; α = 0,30; τₑ = 1 − Rₑ − α = 0,15. Comprobación: Rₑ + α + τₑ = 1.'],
        ['Sabine', 'Sala 5 × 4 × 3 m; Sₜₒₜ = 94 m²; ᾱ = 0,20. Aₑq = 18,8 m² sabin. T₆₀ = 0,161 · 60 / 18,8 ≈ 0,514 s.'],
        { y: 175, h: 405 });
      break;
    case 'U10-092':
      threeCards(slide, [
        ['Norma y edición', 'Identificar documento completo, versión, adopción local y vigencia.'],
        ['Condición de medida', 'Declarar bandas, ponderación, posición, vía y transductor.'],
        ['Criterio audiométrico', 'Relacionar ruido residual con nivel mínimo de ensayo, calibración e incertidumbre.'],
      ]);
      addText(slide, 'Sin esos metadatos, un valor aislado no permite afirmar que la cabina sea apta.', { x: 145, y: 548, w: 990, h: 43, size: 24, color: C.red, bold: true, align: 'center', name: 'norm-key' });
      break;
    case 'U10-093': {
      const cols = [
        ['Campo libre', 'Directo dominante', 'Distancia y directividad', 'No implica aptitud clínica'],
        ['Sala', 'Directo + reflexiones', 'T₆₀ y distribución espacial', 'Describe acondicionamiento'],
        ['Cabina', 'Sistema controlado', 'Ruido residual + aislamiento', 'Requiere protocolo completo'],
      ];
      cols.forEach((c, i) => panel(slide, c[0], `Campo: ${c[1]}\n\nDescriptor: ${c[2]}\n\nLectura: ${c[3]}`, { x: 80 + i * 386, y: 180, w: 350, h: 365, kind: ['physical', 'accent', 'clinical'][i], name: `field-${i}`, bodySize: 21 }));
      break;
    }
    case 'U10-094': {
      const claims = [
        'α = 0,90 significa “bloquea 90 %”.', 'El viento siempre suma el mismo número de dB.',
        'T₆₀ corto demuestra buen aislamiento.', 'A un nivel direccional se le agrega DI otra vez.',
        'Más temperatura eleva la frecuencia recibida.', 'Duplicar distancia siempre resta 6 dB.',
        'Difracción y transmisión son sinónimos.', 'Un dB(A) global prueba aptitud audiométrica.',
        'Una pared pesada elimina todas las fugas.', 'Más absorción interior evita ingreso exterior.',
        'Viento uniforme curva la trayectoria.', 'Igual Aₑq produce el mismo campo en toda sala.',
      ];
      claims.forEach((t, i) => {
        const col = i < 6 ? 0 : 1; const row = i % 6;
        addText(slide, `${i + 1}. ${t}`, { x: 85 + col * 575, y: 158 + row * 70, w: 545, h: 58, size: 18, color: C.carbon, fill: row % 2 ? C.ivory : C.white, lineFill: C.lightGray, lineWidth: 0.7, valign: 'middle', name: `claim-${i}` });
      });
      break;
    }
    case 'U10-095':
      threeCards(slide, [
        ['Fuente', 'Caracterizar tránsito y equipos: nivel, espectro, horario y directividad.\n\nMedir antes de atribuir.'],
        ['Trayecto', 'Separar fachada, aberturas, estructura y ventilación.\n\nEstimar solo con geometría y datos suficientes.'],
        ['Receptor', 'Medir ruido residual por bandas en puestos de prueba y contrastar con el protocolo aplicable.'],
      ]);
      addText(slide, 'Decisión orientativa: identificar la vía dominante antes de elegir una intervención.', { x: 135, y: 548, w: 1010, h: 44, size: 23, color: C.berry, bold: true, align: 'center', name: 'case-key' });
      break;
    case 'U10-096': {
      const refs = [
        'Programa oficial de Física Acústica (UCASAL, 2025), Unidad 10.',
        'Física Acústica para Fonoaudiología, cap. 9, pp. 235–259.',
        'Fuente editable del curso: context/libro_latex/chapters/unidad-9.tex.',
        'Guía de notación y decisiones del proyecto: style/ y units/unit_10/.',
        'ISO 8253-1 e ISO 8253-2: verificar edición, adopción y texto completo antes de aplicar límites.',
        'ISO 1996-2: consultar la edición vigente para condiciones de medición ambiental.',
      ];
      refs.forEach((t, i) => addText(slide, t, { x: 100, y: 165 + i * 67, w: 1080, h: 52, size: 20, color: C.carbon, fill: i % 2 ? C.ivory : C.white, lineFill: C.lightGray, lineWidth: 0.7, valign: 'middle', name: `source-${i}` }));
      break;
    }
    default:
      return false;
  }
  return true;
}

function pipeTable(content) {
  const rows = content.filter((line) => /^\|.*\|$/.test(line) && !/^\|\s*[-:]+/.test(line))
    .map((line) => line.slice(1, -1).split('|').map((cell) => clean(cell.trim())));
  const extras = content.filter((line) => !/^\|.*\|$/.test(line));
  return { rows, extras };
}

function addEditableTable(slide, d, widths, bodySize = 19) {
  const { rows, extras } = pipeTable(d.content);
  if (rows.length < 2) return false;
  const x = 75, y = 165, totalW = 1130;
  const normalized = widths.map((v) => v * totalW / widths.reduce((a, b) => a + b, 0));
  const availableH = extras.length ? 380 : 430;
  const rowH = Math.min(78, availableH / rows.length);
  rows.forEach((row, r) => {
    let cx = x;
    row.forEach((cell, c) => {
      const w = normalized[c] || normalized.at(-1);
      const header = r === 0;
      addShape(slide, { geometry: 'rect', name: r === 0 && c === 0 ? `${d.id}-claim-alt` : `${d.id}-cell-${r}-${c}`,
        x: cx, y: y + r * rowH, w, h: rowH, fill: header ? C.berry : r % 2 ? C.white : C.ivory,
        lineFill: C.lightGray, lineWidth: 0.8 });
      addText(slide, cell, { x: cx + 8, y: y + r * rowH + 5, w: w - 16, h: rowH - 10,
        size: header ? Math.max(25, bodySize) : bodySize, color: header ? C.white : C.carbon, bold: header,
        valign: 'middle', name: `${d.id}-cell-text-${r}-${c}`, insets: { top: 2, right: 3, bottom: 2, left: 3 } });
      cx += w;
    });
  });
  if (extras.length) addText(slide, extras.join(' '), { x: 95, y: y + rows.length * rowH + 24, w: 1090, h: 52,
    size: 21, color: C.berry, bold: true, align: 'center', name: `${d.id}-table-note` });
  return true;
}

async function addUnit10Special(slide, d) {
  if (d.id === 'U10-035') {
    const asset = assetsById.get('U10-CH-010');
    const svgPath = path.join(ROOT, asset.local_path, 'figure.svg');
    const bytes = await fs.readFile(svgPath);
    const image = slide.images.add({ blob: bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), contentType: 'image/svg+xml',
      alt: 'Comparación estática del ruido blanco y rosa por hertz y por octava.', fit: 'contain',
      position: { left: 60, top: 155, width: 760, height: 430 } });
    image.name = `${asset.asset_id}-chart`;
    panel(slide, 'Audio opcional', 'Dos clips propios de 10 s, con cadena y nivel documentados. Si no están disponibles, la comparación visual permite completar la actividad.',
      { x: 855, y: 205, w: 345, h: 285, kind: 'clinical', name: 'audio-optional', bodySize: 21 });
    addText(slide, 'No elevar el volumen para “notar mejor” la diferencia.', { x: 850, y: 515, w: 355, h: 42,
      size: 20, color: C.alert, bold: true, align: 'center', name: 'audio-safety' });
    addCaption(slide, d, asset.asset_id);
    return { type: 'chart', asset: asset.asset_id, alt: d.alt };
  }
  if (d.id === 'U10-042') {
    addEditableTable(slide, d, [170, 260, 260, 440], 25);
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-068') {
    addEditableTable(slide, d, [230, 360, 540], 25);
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-085') {
    addEditableTable(slide, d, [210, 600, 320], 25);
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-090') {
    addEditableTable(slide, d, [260, 870], 25);
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-074') {
    addText(slide, 'Uso exploratorio posible', { x: 95, y: 165, w: 1090, h: 44, size: 29,
      color: C.berry, bold: true, name: 'app-use-heading' });
    const uses = [
      'Comparar momentos o lugares con el mismo dispositivo y procedimiento.',
      'Detectar cambios grandes que justifiquen una medición formal.',
      'Registrar observaciones preliminares.',
    ];
    uses.forEach((item, index) => {
      addShape(slide, { geometry: 'ellipse', name: `app-bullet-${index}`, x: 112, y: 242 + index * 72, w: 12, h: 12, fill: C.berry2 });
      addText(slide, item, { x: 150, y: 224 + index * 72, w: 1010, h: 54, size: 28,
        color: C.carbon, valign: 'middle', name: `app-use-${index}` });
    });
    addText(slide, 'No certifica sin calibración, respuesta frecuencial conocida, posición, intervalo, ponderaciones, rango e incertidumbre.',
      { x: 95, y: 470, w: 1090, h: 92, size: 27, color: C.alert, bold: true, align: 'center', valign: 'middle',
        fill: C.ochreLight, lineFill: C.ochre, lineWidth: 1.2, radius: 6, name: `${d.id}-claim-alt`,
        insets: { top: 8, right: 16, bottom: 8, left: 16 } });
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-082') {
    addShape(slide, { geometry: 'roundRect', name: `${d.id}-claim-alt`, x: 75, y: 150, w: 1130, h: 54, fill: C.accentLight, lineFill: C.berry2, lineWidth: 1, radius: 5 });
    addText(slide, d.content[0], { x: 95, y: 160, w: 1090, h: 34, size: 21, color: C.berry, bold: true, align: 'center', name: 'errors-instruction' });
    const claims = d.content.slice(1, 13);
    claims.forEach((claim, i) => {
      const col = i < 6 ? 0 : 1; const row = i % 6; const x = col ? 660 : 80;
      addShape(slide, { geometry: 'ellipse', name: `error-n-${i}`, x, y: 233 + row * 57, w: 32, h: 32, fill: i % 2 ? C.tealLight : C.accentLight, lineFill: i % 2 ? C.teal : C.berry2, lineWidth: 1 });
      addText(slide, String(i + 1), { x, y: 238 + row * 57, w: 32, h: 22, size: 16, color: C.carbon, bold: true, align: 'center', name: `error-num-${i}`, insets: { top: 0, right: 0, bottom: 0, left: 0 } });
      addText(slide, claim, { x: x + 45, y: 226 + row * 57, w: 490, h: 44, size: 25, color: C.carbon, valign: 'middle', name: `error-claim-${i}` });
    });
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-089') {
    addShape(slide, { geometry: 'roundRect', name: `${d.id}-claim-alt`, x: 75, y: 145, w: 1130, h: 52, fill: C.accentLight, lineFill: C.berry2, lineWidth: 1, radius: 5 });
    addText(slide, 'Cinco resultados: mostrar procedimiento, unidades y límite de interpretación', { x: 95, y: 156, w: 1090, h: 30, size: 21, color: C.berry, bold: true, align: 'center', name: 'solutions-heading' });
    const results = [
      '0, 2, 2, 4 mPa → p̄=2 mPa; pᵣₘₛ≈2,45 mPa; σₚ²=2 mPa².',
      '9,0×10⁻¹⁰ Pa²/Hz · 2000 Hz → pᵣₘₛ≈1,34 mPa → 36,5 dB SPL.',
      '900–1100 Hz → B=200 Hz; faltan f꜀, forma, pendientes, nivel y calibración.',
      '68−73=−5 dB: el ruido es 5 dB mayor en condiciones comparables.',
      '74, 78, 82 dB(A) → Lₐeq,30 min≈79,2 dB(A).',
    ];
    results.forEach((result, i) => {
      const col = i < 3 ? 0 : 1; const row = col ? i - 3 : i; const x = col ? 660 : 80;
      const y = 220 + row * 116;
      const style = styleForNode(['physical', 'accent', 'neutral', 'clinical', 'physical'][i]);
      addShape(slide, { geometry: 'roundRect', name: `solution-${i}-box`, x, y, w: 540, h: 102, fill: style.fill, lineFill: style.line, lineWidth: 1.2, radius: 5 });
      addText(slide, String(i + 1), { x: x + 14, y: y + 33, w: 38, h: 30, size: 27, color: style.text, bold: true, align: 'center', name: `solution-${i}-number` });
      addText(slide, result, { x: x + 58, y: y + 8, w: 466, h: 86, size: 28, color: C.carbon, valign: 'middle', name: `solution-${i}-body`,
        insets: { top: 3, right: 5, bottom: 3, left: 5 } });
    });
    return { type: 'custom', alt: d.alt };
  }
  if (d.id === 'U10-093') {
    const groups = [
      ['Fuentes primarias', 'Programa oficial 2025 · Libro del curso, capítulo 10 (LaTeX y PDF).'],
      ['Apoyo transversal', 'Guías de estilo, notación y glosario · Unidades 4, 5, 7, 8 y 9.'],
      ['Fuentes externas', 'Normas de medición y audiometría · Guías sanitarias y clínicas · Normativa jurisdiccional.'],
    ];
    groups.forEach(([heading, body], index) => {
      const y = 160 + index * 132;
      addText(slide, heading, { x: 90, y, w: 285, h: 92, size: 27, color: C.white, bold: true,
        align: 'center', valign: 'middle', fill: C.berry, name: index === 0 ? `${d.id}-claim-alt` : `source-heading-${index}` });
      addText(slide, body, { x: 375, y, w: 815, h: 92, size: 25, color: C.carbon, valign: 'middle',
        fill: index % 2 ? C.ivory : C.white, lineFill: C.lightGray, lineWidth: 0.8, name: `source-body-${index}`,
        insets: { top: 8, right: 14, bottom: 8, left: 14 } });
    });
    addText(slide, 'Consultar source_map.md; no usar QR ni URL sin verificación final.', { x: 120, y: 560, w: 1040, h: 42,
      size: 25, color: C.alert, bold: true, align: 'center', name: 'source-warning' });
    return { type: 'custom', alt: d.alt };
  }
  return null;
}

function addNotes(slide, d, note, inserted) {
  const sourceLines = [`- Fuentes de contenido: ${d.source || 'Programa oficial y libro del curso.'}`];
  if (inserted?.asset) sourceLines.push(`- Asset propio aprobado: ${inserted.asset}.`);
  const media = d.id === 'U10-035' ? '\n\n[Media]\nU10-AS-001 y U10-AS-002 identificados; no embebidos porque continúan propuestos y sin archivo local aprobado. Usar U10-CH-010 como alternativa estática.' : '';
  const full = `${note || ''}${media}\n\n[Alt text]\n${inserted?.alt || d.alt || 'Contenido textual editable de la diapositiva.'}\n\n[Sources]\n${sourceLines.join('\n')}`.trim();
  slide.speakerNotes.clear();
  slide.speakerNotes.textFrame.setText(full);
  slide.speakerNotes.setVisible(true);
}

const slidesData = parseSlideText(await fs.readFile(path.join(UNIT, 'slide_text.md'), 'utf8'));
const notes = parseNotes(await fs.readFile(path.join(UNIT, 'speaker_notes.md'), 'utf8'));
const manifest = parseCsv(await fs.readFile(path.join(UNIT, 'asset_manifest.csv'), 'utf8'));
if (slidesData.length !== 93 || notes.size !== 93) throw new Error(`Conteos incompatibles: slides=${slidesData.length}, notas=${notes.size}.`);

const approved = manifest
  .filter((a) => a.status.startsWith('approved') && ['diagram', 'equation', 'chart'].includes(a.type) && a.local_path && !BLOCKED_ASSETS.has(a.asset_id))
  .map((a) => ({ ...a, type: a.type === 'equation' ? 'diagram' : a.type }));
const assetsById = new Map(approved.map((a) => [a.asset_id, a]));
const assetsBySlide = new Map();
for (const asset of approved) {
  for (const sid of asset.slide_id.split('/').map((x) => x.trim()).filter(Boolean)) {
    if (!assetsBySlide.has(sid)) assetsBySlide.set(sid, []);
    assetsBySlide.get(sid).push(asset);
  }
}
function assetFor(d) {
  const ids = [...d.visual.matchAll(/U10-(?:DG|CH)-\d{3}/g)].map((m) => m[0]).filter((id) => !BLOCKED_ASSETS.has(id));
  const available = [...ids.map((id) => assetsById.get(id)).filter(Boolean), ...(assetsBySlide.get(d.id) || [])]
    .filter((asset, index, all) => all.findIndex((x) => x.asset_id === asset.asset_id) === index);
  if (d.layout === 'FA_07_GRAFICO_EXPLICACION') return available.find((a) => a.type === 'chart') || available[0];
  return available.find((a) => a.type === 'diagram') || available.find((a) => a.type === 'chart');
}

await fs.mkdir(path.dirname(OUT), { recursive: true });
await fs.mkdir(QA, { recursive: true });
const deck = await PresentationFile.importPptx(await FileBlob.load(starterPptxPath));
if (deck.slides.items.length !== 93) throw new Error(`El starter debe tener 93 slides; tiene ${deck.slides.items.length}.`);

const buildLog = [];
for (let i = 0; i < deck.slides.items.length; i += 1) {
  const slide = deck.slides.items[i]; const d = slidesData[i];
  await clearSlide(slide);
  const dark = ['FA_00_PORTADA', 'FA_01_DIVISOR', 'FA_17_RECAP_FINAL', 'FA_21_CIERRE_PUENTE'].includes(d.layout);
  slide.background.fill = dark ? C.berry : C.white;
  let inserted;
  if (d.layout === 'FA_00_PORTADA') {
    addText(slide, 'UNIDAD 10 · FÍSICA ACÚSTICA', { x: 64, y: 42, w: 560, h: 28, size: 18, color: C.white, bold: true, name: 'cover-eyebrow' });
    addText(slide, d.title, { x: 78, y: 130, w: 690, h: 210, size: 50, color: C.white, font: 'Calibri Light', name: 'cover-title', insets: { top: 0, right: 0, bottom: 0, left: 0 } });
    addText(slide, 'Tiempo · frecuencia · nivel · función', { x: 82, y: 385, w: 720, h: 60, size: 28, color: '#EADDE4', name: 'cover-subtitle' });
    addText(slide, 'Un ruido se comprende por su señal, su contexto y su función.', { x: 82, y: 500, w: 820, h: 50, size: 23, color: '#EADDE4', name: 'cover-claim' });
    inserted = await addCoverDiagram(slide, d, assetsById.get('U10-DG-001'));
  } else if (d.layout === 'FA_01_DIVISOR' || d.layout === 'FA_21_CIERRE_PUENTE') {
    addText(slide, `UNIDAD 10 · ${d.route === 'central' ? 'RUTA CENTRAL' : d.route.toUpperCase()}`, { x: 55, y: 24, w: 600, h: 24, size: 16, color: '#E1C8D4', bold: true, name: 'dark-eyebrow' });
    addText(slide, d.title, { x: 85, y: 215, w: 1110, h: 130, size: 48, color: C.white, font: 'Calibri Light', align: 'center', valign: 'middle', name: 'divider-title' });
    const claim = d.content[0] || d.subtitle;
    addText(slide, claim, { x: 175, y: 375, w: 930, h: 80, size: 26, color: '#E6D5DD', align: 'center', name: 'divider-subtitle' });
  } else if (d.layout === 'FA_17_RECAP_FINAL') {
    addTitle(slide, d, true);
    inserted = await addDiagram(slide, d, assetsById.get('U10-DG-055'), { dark: true });
  } else {
    addTopRail(slide, d); addTitle(slide, d, false);
    const unit10Special = await addUnit10Special(slide, d);
    if (unit10Special) inserted = unit10Special;
    else if (addCustomSlide(slide, d)) inserted = { type: 'custom', alt: d.alt };
    else if (LOCAL_VISUAL_REPLACEMENTS[d.id]) addConditional(slide, d);
    else if (BLOCKED_SLIDES.has(d.id)) addBlocked(slide, d);
    else {
      if (d.id === 'U10-078') {
        inserted = await addComposite078(slide, d, assetsById.get('U10-DG-051'), assetsById.get('U10-CH-014'));
      } else {
        const asset = assetFor(d);
        if (asset?.type === 'diagram') inserted = await addDiagram(slide, d, asset);
        else if (asset?.type === 'chart') inserted = await addChart(slide, d, asset);
        else addGeneric(slide, d);
      }
    }
  }
  addPage(slide, i + 1, dark);
  addNotes(slide, d, notes.get(d.id), inserted);
  buildLog.push({ slide: i + 1, id: d.id, layout: d.layout, route: d.route, asset: inserted?.asset || null,
    assetType: inserted?.type || null, blocked: BLOCKED_SLIDES.has(d.id) && !CUSTOM_SLIDES.has(d.id) });
}

const pptx = await PresentationFile.exportPptx(deck);
await pptx.save(OUT);

const xmlAttr = (value) => String(value).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const zip = await JSZip.loadAsync(await fs.readFile(OUT));
for (let i = 0; i < slidesData.length; i += 1) {
  const d = slidesData[i]; const log = buildLog[i]; const slidePath = `ppt/slides/slide${i + 1}.xml`; const part = zip.file(slidePath);
  if (!part) continue;
  let xml = await part.async('string');
  const targetNames = log.assetType === 'composite'
    ? log.asset.split(/,\s*/).map((asset) => asset.includes('-CH-') ? `${asset}-chart` : `${asset}-visual-alt`)
    : [log.assetType === 'chart' ? `${log.asset}-chart` : log.assetType === 'diagram' ? `${log.asset}-visual-alt` : LOCAL_VISUAL_REPLACEMENTS[d.id] ? `${d.id}-conditional-alt` : BLOCKED_SLIDES.has(d.id) ? `${d.id}-blocked-alt` : `${d.id}-claim-alt`];
  for (const targetName of targetNames.filter(Boolean)) {
    const escaped = targetName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    xml = xml.replace(new RegExp(`<p:cNvPr\\b([^>]*\\bname="${escaped}"[^>]*)>`), (match, attrs) => {
      const selfClosing = /\/\s*>$/.test(match);
      const cleaned = attrs.replace(/\sdescr="[^"]*"/g, '').replace(/\s*\/$/, '');
      return `<p:cNvPr${cleaned} descr="${xmlAttr(d.alt)}"${selfClosing ? ' /' : ''}>`;
    });
  }
  zip.file(slidePath, xml);
}
await fs.writeFile(OUT, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE', compressionOptions: { level: 6 } }));

const inspect = await deck.inspect({ kind: 'deck,slide,textbox,shape,image,chart,table,notes,layout', include: 'id,slide,name,title,text,textPreview,textChars,bbox,bboxUnit,isPlaceholder,alt', maxChars: 2_000_000 });
await fs.writeFile(path.join(QA, 'final-inspect.ndjson'), inspect.ndjson, 'utf8');
await fs.writeFile(path.join(QA, 'build-log.json'), `${JSON.stringify({ output: OUT, slides: buildLog, approvedAssetCount: approved.length }, null, 2)}\n`, 'utf8');
console.log(JSON.stringify({ output: OUT, slides: buildLog.length, assetsInserted: buildLog.filter((x) => x.asset).length,
  diagrams: buildLog.filter((x) => x.assetType === 'diagram').length, charts: buildLog.filter((x) => x.assetType === 'chart').length,
  blocked: buildLog.filter((x) => x.blocked).length }, null, 2));

