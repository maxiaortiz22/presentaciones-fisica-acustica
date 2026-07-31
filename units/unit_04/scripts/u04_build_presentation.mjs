import fs from 'node:fs/promises';
import path from 'node:path';
import { FileBlob, PresentationFile } from '@oai/artifact-tool';

const [starterPath, slideTextPath, notesPath, manifestPath, repoRoot, outPath, previewDir] = process.argv.slice(2);
if (![starterPath, slideTextPath, notesPath, manifestPath, repoRoot, outPath].every(Boolean)) {
  throw new Error('Uso: node u04_build_presentation.mjs <starter.pptx> <slide_text.md> <speaker_notes.md> <asset_manifest.csv> <repoRoot> <out.pptx> [previewDir]');
}

const C = {
  berry: '#4D1434', berry2: '#903163', carbon: '#3D3D3D', gray: '#969FA7',
  lightGray: '#D9DCE0', ivory: '#F7F6F2', teal: '#2F7E83', tealLight: '#E7F1F1',
  ochre: '#9F541A', ochreLight: '#F8EDE2', error: '#A33A3A', ok: '#2F6F55',
  white: '#FFFFFF', blue: '#023E7C', black: '#242A2E',
};
const FONT = { title: 'Calibri Light', body: 'Calibri', eq: 'Cambria Math' };
const CHART_CONDITIONS = {
  'U04-CH-001': 'valores ilustrativos · escala lineal',
  'U04-CH-003': 'señal sintética · límites idénticos',
  'U04-CH-006': 'señales sintéticas · misma escala',
  'U04-CH-010': 'modelos ideales · no son datos experimentales',
  'U04-CH-011': 'fuente puntual · campo libre y lejano · misma dirección',
  'U04-CH-014': 'dos fuentes no correlacionadas',
};
const clean = (s = '') => s.replace(/\r/g, '').trim();

function splitSections(markdown) {
  const matches = [...markdown.matchAll(/^## (U04-\d{3})[^\n]*\n([\s\S]*?)(?=^## U04-\d{3}|(?![\s\S]))/gm)];
  return new Map(matches.map((m) => [m[1], m[2]]));
}

function field(section, label) {
  const m = section.match(new RegExp(`\\*\\*${label}:\\*\\*\\s*([^\\n]*)`));
  return clean(m?.[1] ?? '');
}

function block(section, label) {
  const m = section.match(new RegExp(`\\*\\*${label}:\\*\\*\\s*\\n([\\s\\S]*?)(?=\\n\\*\\*[^\\n]+:\\*\\*|$)`));
  return clean(m?.[1] ?? '');
}

function visibleBullets(section) {
  return block(section, 'Contenido visible').split('\n')
    .map((line) => line.replace(/^\s*[-*]\s+/, '').trim())
    .filter((line) => line && !/^No corresponde/i.test(line))
    .map(formatInline);
}

function equations(section) {
  const raw = block(section, 'Ecuaciones');
  if (!raw || /^No corresponde/i.test(raw)) return [];
  return raw.split('\n').map((line) => line.replace(/^\s*[-*]\s+/, '').trim())
    .filter((line) => line && !/^No corresponde/i.test(line)).map(formatInline);
}

function replaceFractions(text) {
  let out = text;
  for (let i = 0; i < 8; i += 1) {
    const next = out.replace(/\\(?:d?frac)\{([^{}]+)\}\{([^{}]+)\}/g, '($1)/($2)');
    if (next === out) break;
    out = next;
  }
  return out;
}

function scriptChars(text, kind) {
  const maps = {
    sub: {0:'₀',1:'₁',2:'₂',3:'₃',4:'₄',5:'₅',6:'₆',7:'₇',8:'₈',9:'₉',a:'ₐ',e:'ₑ',h:'ₕ',i:'ᵢ',j:'ⱼ',k:'ₖ',l:'ₗ',m:'ₘ',n:'ₙ',o:'ₒ',p:'ₚ',r:'ᵣ',s:'ₛ',t:'ₜ',u:'ᵤ',v:'ᵥ',x:'ₓ','+':'₊','-':'₋','=':'₌','(':'₍',')':'₎'},
    sup: {0:'⁰',1:'¹',2:'²',3:'³',4:'⁴',5:'⁵',6:'⁶',7:'⁷',8:'⁸',9:'⁹',n:'ⁿ',i:'ⁱ','+':'⁺','-':'⁻','=':'⁼','(':'⁽',')':'⁾'},
  };
  const map = maps[kind];
  return [...text].map((ch) => map[ch] ?? ch).join('');
}

function formatInline(input) {
  let s = String(input ?? '').replace(/`([^`]+)`/g, '$1').replace(/\$/g, '');
  s = replaceFractions(s);
  s = s.replace(/\\hat\s*\{?([A-Za-z])\}?/g, '$1̂')
    .replace(/\\(?:mathrm|text|operatorname)\{/g, '')
    .replace(/\\(?:mathrm|text|operatorname)\s+/g, '')
    .replace(/\\sqrt\{([^{}]+)\}/g, '√($1)').replace(/\\sqrt\s*([0-9A-Za-z]+)/g, '√$1')
    .replace(/\\left|\\right|\\bigl|\\bigr|\\displaystyle/g, '')
    .replace(/\\rho/g, 'ρ').replace(/\\lambda/g, 'λ').replace(/\\pi/g, 'π')
    .replace(/\\theta/g, 'θ').replace(/\\varphi|\\phi/g, 'φ').replace(/\\gamma/g, 'γ')
    .replace(/\\Delta/g, 'Δ').replace(/\\mu/g, 'µ').replace(/\\omega/g, 'ω')
    .replace(/\\times/g, '×').replace(/\\cdot/g, '·').replace(/\\approx/g, '≈')
    .replace(/\\propto/g, '∝').replace(/\\neq/g, '≠').replace(/\\leq?|\\le/g, '≤')
    .replace(/\\geq?|\\ge/g, '≥').replace(/\\Rightarrow/g, '⇒').replace(/\\rightarrow|\\to/g, '→')
    .replace(/\\infty/g, '∞').replace(/\\sum/g, 'Σ').replace(/\\int/g, '∫')
    .replace(/\\log_\{10\}/g, 'log₁₀').replace(/\\log/g, 'log')
    .replace(/\^\{([^{}]+)\}/g, (_, x) => scriptChars(x, 'sup'))
    .replace(/_\{([^{}]+)\}/g, (_, x) => scriptChars(x, 'sub'))
    .replace(/\^([0-9ni+-])/g, (_, x) => scriptChars(x, 'sup'))
    .replace(/_([0-9A-Za-z+-])/g, (_, x) => scriptChars(x, 'sub'))
    .replace(/\\([{}])/g, '$1')
    .replace(/\\\s+/g, ' ')
    .replace(/\\[,;!]|\\quad|\\qquad/g, ' ')
    .replace(/\\([A-Za-z]+)/g, '$1')
    .replace(/\{([^{}]+)\}/g, '$1').replace(/[{}]/g, '')
    .replace(/\s+/g, ' ').trim();
  return s;
}

// Estos assets agrupaban microvisuales o diagramas reutilizados cuya imagen
// no respondía a la consigna concreta de la slide. En v02 se conserva el
// contenido aprobado como texto y ecuaciones editables, sin un visual engañoso.
const TEXT_ONLY_REVIEW_FIXES = new Set([
  'U04-004', 'U04-011', 'U04-029', 'U04-030', 'U04-032', 'U04-035', 'U04-037',
  'U04-038', 'U04-058', 'U04-062', 'U04-063', 'U04-065', 'U04-066',
  'U04-067', 'U04-071', 'U04-073', 'U04-075', 'U04-076', 'U04-078',
  'U04-079', 'U04-080', 'U04-085', 'U04-092', 'U04-093', 'U04-094',
  'U04-100', 'U04-101', 'U04-102', 'U04-105', 'U04-114', 'U04-115',
  'U04-120', 'U04-124',
]);

function parseCsv(csv) {
  const rows = [];
  let row = [], cell = '', quoted = false;
  for (let i = 0; i < csv.length; i += 1) {
    const ch = csv[i];
    if (quoted) {
      if (ch === '"' && csv[i + 1] === '"') { cell += '"'; i += 1; }
      else if (ch === '"') quoted = false;
      else cell += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ',') { row.push(cell); cell = ''; }
    else if (ch === '\n') { row.push(cell.replace(/\r$/, '')); rows.push(row); row = []; cell = ''; }
    else cell += ch;
  }
  if (cell.length || row.length) { row.push(cell); rows.push(row); }
  const headers = rows.shift();
  return rows.filter((r) => r.some(Boolean)).map((r) => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ''])));
}

function addText(slide, text, pos, style = {}, name = 'text') {
  const shape = slide.shapes.add({
    geometry: 'textbox', name,
    position: pos, fill: 'none', line: { style: 'solid', fill: 'none', width: 0 },
  });
  shape.text = text;
  shape.text.style = {
    fontSize: style.fontSize ?? 28, typeface: style.typeface ?? FONT.body,
    color: style.color ?? C.black, bold: style.bold ?? false,
    alignment: style.alignment ?? 'left', verticalAlignment: style.verticalAlignment ?? 'top',
    autoFit: 'none', wrap: 'square', lineSpacing: style.lineSpacing ?? 1.0,
    insets: style.insets ?? { top: 0, right: 0, bottom: 0, left: 0 },
  };
  return shape;
}

function addRect(slide, pos, fill, line = 'none', radius = 0, name = 'surface') {
  return slide.shapes.add({
    geometry: radius ? 'roundRect' : 'rect', name, position: pos, fill,
    line: { style: 'solid', fill: line, width: line === 'none' ? 0 : 1.5 },
    ...(radius ? { borderRadius: radius } : {}),
  });
}

function addTitle(slide, record, dark = false, top = 72) {
  addText(slide, `UNIDAD 4 · FÍSICA ACÚSTICA`, { left: 64, top: 43, width: 560, height: 24 },
    { fontSize: 16, typeface: FONT.body, bold: true, color: dark ? C.white : C.berry }, `eyebrow-${record.id}`);
  const titleSize = record.title.length > 70 ? 36 : record.title.length > 48 ? 40 : 44;
  addText(slide, record.title, { left: 64, top, width: 1150, height: 82 },
    { fontSize: titleSize, typeface: FONT.title, color: dark ? C.white : C.berry, lineSpacing: 0.95 }, `title-${record.id}`);
}

function addNumber(slide, n, dark = false) {
  addText(slide, String(n), { left: 1176, top: 677, width: 40, height: 22 },
    { fontSize: 14, bold: true, color: dark ? C.white : C.berry, alignment: 'right', verticalAlignment: 'middle' }, `slide-number-${n}`);
}

function addBulletList(slide, bullets, pos, options = {}) {
  const size = options.fontSize ?? (bullets.length <= 4 ? 30 : bullets.length <= 6 ? 26 : 22);
  const shape = slide.shapes.add({ geometry: 'textbox', name: options.name ?? 'bullets', position: pos, fill: 'none', line: { style: 'solid', fill: 'none', width: 0 } });
  shape.text = bullets.map((b) => ({ bulletCharacter: '•', marginLeft: 26, indent: -16, spaceAfter: 10, runs: [{ run: b }] }));
  shape.text.style = { fontSize: size, typeface: FONT.body, color: options.color ?? C.carbon, autoFit: 'none', wrap: 'square', lineSpacing: 1.0, insets: { top: 4, right: 4, bottom: 4, left: 4 } };
  return shape;
}

function addEquationBox(slide, eqs, pos, accent = C.teal) {
  addRect(slide, pos, C.ivory, accent, 10, 'equation-surface');
  const fontSize = eqs.join(' ').length > 75 ? 32 : 39;
  addText(slide, eqs.join('\n'), { left: pos.left + 24, top: pos.top + 18, width: pos.width - 48, height: pos.height - 36 },
    { fontSize, typeface: FONT.eq, color: C.black, alignment: 'center', verticalAlignment: 'middle', lineSpacing: 1.08 }, 'equation');
}

function slideAssetsFor(id, section, assets) {
  const plannedPrimaryOverride = {
    'U04-025': 'U04-CH-001',
    'U04-048': 'U04-CH-004',
    'U04-072': 'U04-CH-008',
    'U04-106': 'U04-DG-019',
    'U04-113': 'U04-CH-013',
  };
  const explicit = [...section.matchAll(/`(U04-(?:CH|DG|EXT)-\d{3})`/g)].map((m) => m[1]);
  const candidates = assets.filter((a) => a.status === 'approved' && ['chart', 'diagram', 'equation_only', 'external_image'].includes(a.type)
    && a.slide_id.split(';').map((x) => x.trim()).includes(id));
  const override = candidates.find((a) => a.asset_id === plannedPrimaryOverride[id]);
  if (override) return [override];
  const ordered = [...candidates].sort((a, b) => {
    const ai = explicit.indexOf(a.asset_id), bi = explicit.indexOf(b.asset_id);
    if (ai >= 0 || bi >= 0) return (ai < 0 ? 99 : ai) - (bi < 0 ? 99 : bi);
    const aExact = a.slide_id.split(';').length === 1 ? 1 : 0, bExact = b.slide_id.split(';').length === 1 ? 1 : 0;
    return bExact - aExact;
  });
  if (!ordered.length) return [];
  const external = ordered.find((a) => a.type === 'external_image');
  if (external) return [external];
  const charts = ordered.filter((a) => a.type === 'chart');
  const diagrams = ordered.filter((a) => ['diagram', 'equation_only'].includes(a.type));
  if (charts.length && /FA_07_GRAFICO|FA_10_EJEMPLO|FA_09_ECUACION/.test(field(section, 'Layout'))) return [charts.at(-1)];
  if (diagrams.length) return [diagrams[0]];
  return [charts.at(-1)];
}

async function addVisual(slide, record, asset, mediaPending) {
  const fullDiagram = ['diagram', 'equation_only', 'chart'].includes(asset.type);
  const assetPath = path.resolve(repoRoot, asset.local_path.replace(/\//g, path.sep));
  const blob = await fs.readFile(assetPath);
  const ext = path.extname(assetPath).toLowerCase();
  const contentType = ext === '.svg' ? 'image/svg+xml' : ext === '.jpg' || ext === '.jpeg' ? 'image/jpeg' : 'image/png';
  const alt = record.alt || asset.description || asset.title;

  if (fullDiagram) {
    if (asset.type === 'chart') {
      slide.images.add({ blob, contentType, alt, fit: 'contain', position: { left: 20, top: 106, width: 1240, height: 530 } });
    } else {
      slide.images.add({ blob, contentType, alt, fit: 'cover', position: { left: 0, top: 100, width: 1280, height: 540 } });
    }
    addRect(slide, { left: 54, top: 40, width: 1172, height: 62 }, C.white, 'none', 0, 'visual-title-backing');
    addText(slide, 'UNIDAD 4 · FÍSICA ACÚSTICA', { left: 64, top: 42, width: 560, height: 18 },
      { fontSize: 14, typeface: FONT.body, bold: true, color: C.berry }, `eyebrow-${record.id}`);
    const titleSize = record.title.length > 78 ? 29 : record.title.length > 55 ? 32 : 36;
    addText(slide, record.title, { left: 64, top: 59, width: 1150, height: 42 },
      { fontSize: titleSize, typeface: FONT.title, color: C.berry, verticalAlignment: 'middle', lineSpacing: 0.95 }, `title-${record.id}`);
    const genericCaption = /esquema conceptual|figura cuantitativa reproducible|recurso técnico usado|distancias, tamaños y formas|no está a escala/i;
    const proposedCaption = record.caption && !/^No corresponde/i.test(record.caption) ? record.caption : '';
    const baseCaption = proposedCaption && !genericCaption.test(proposedCaption) ? proposedCaption : record.keyIdea;
    const caption = formatInline(CHART_CONDITIONS[asset.asset_id] ? `${baseCaption} · ${CHART_CONDITIONS[asset.asset_id]}.` : baseCaption);
    const shortCaption = caption.length > 145 ? `${caption.slice(0, 142).trim()}…` : caption;
    addRect(slide, { left: 64, top: 639, width: 1110, height: 24 }, C.white, 'none', 0, 'caption-backing');
    addText(slide, shortCaption, { left: 70, top: 642, width: 1098, height: 19 }, { fontSize: 13, color: C.carbon }, 'caption');
  } else {
    addTitle(slide, record, false, 70);
    addRect(slide, { left: 64, top: 170, width: 520, height: 430 }, C.ivory, C.lightGray, 8, 'image-surface');
    slide.images.add({ blob, contentType, alt, fit: 'contain', position: { left: 78, top: 184, width: 492, height: 402 } });
    const rightBullets = record.bullets.slice(0, 5);
    addBulletList(slide, rightBullets, { left: 630, top: 185, width: 570, height: 330 }, { fontSize: rightBullets.length > 4 ? 24 : 27 });
    if (record.caption && !/^No corresponde/i.test(record.caption)) addText(slide, formatInline(record.caption), { left: 630, top: 525, width: 570, height: 50 }, { fontSize: 16, color: C.carbon }, 'caption');
    if (asset.credit_text) {
      const credit = addText(slide, asset.credit_text, { left: 630, top: 585, width: 570, height: 24 }, { fontSize: 12, color: C.gray }, 'credit');
      if (asset.source_url) credit.text.get(asset.credit_text).link = { uri: asset.source_url, isExternal: true };
    }
  }
}

function addTextLayout(slide, record, mediaPending) {
  const dark = ['FA_00_PORTADA', 'FA_01_DIVISOR', 'FA_21_CIERRE_PUENTE'].includes(record.layout);
  if (record.layout === 'FA_00_PORTADA') {
    addText(slide, 'UNIDAD 4 · FÍSICA ACÚSTICA', { left: 64, top: 44, width: 650, height: 28 }, { fontSize: 18, bold: true, color: C.white }, 'cover-eyebrow');
    addText(slide, record.title, { left: 84, top: 150, width: 910, height: 175 }, { fontSize: 55, typeface: FONT.title, color: C.white, verticalAlignment: 'middle', lineSpacing: 0.92 }, 'cover-title');
    const subtitle = record.subtitle && !/^No corresponde/i.test(record.subtitle) ? record.subtitle : 'Campo acústico · medición · niveles';
    addText(slide, subtitle, { left: 88, top: 340, width: 770, height: 88 }, { fontSize: 29, color: C.white }, 'cover-subtitle');
    addText(slide, '¿Qué falta saber cuando alguien informa solo “80 dB”?', { left: 88, top: 520, width: 850, height: 42 }, { fontSize: 24, color: C.white }, 'cover-question');
    return;
  }
  if (record.layout === 'FA_01_DIVISOR' || record.layout === 'FA_21_CIERRE_PUENTE') {
    addText(slide, 'UNIDAD 4', { left: 64, top: 46, width: 300, height: 24 }, { fontSize: 16, bold: true, color: C.white }, 'divider-eyebrow');
    addText(slide, record.title, { left: 92, top: 205, width: 1050, height: 160 }, { fontSize: record.title.length > 60 ? 45 : 52, typeface: FONT.title, color: C.white, verticalAlignment: 'middle', lineSpacing: 0.95 }, 'divider-title');
    const line = record.bullets.find((x) => !x.toLowerCase().includes(record.title.toLowerCase().slice(0, 20))) ?? record.keyIdea;
    addText(slide, line, { left: 94, top: 405, width: 980, height: 80 }, { fontSize: 27, color: C.white }, 'divider-subtitle');
    return;
  }

  addTitle(slide, record, false, 78);
  const bullets = record.bullets;
  const eqs = record.equations;
  const layout = record.layout;

  if (layout === 'FA_09_ECUACION_INTERPRETACION' || (eqs.length && layout !== 'FA_10_EJEMPLO_RESUELTO')) {
    addEquationBox(slide, eqs, { left: 110, top: 180, width: 1060, height: eqs.length > 2 ? 190 : 155 }, C.teal);
    addBulletList(slide, bullets.slice(0, 5), { left: 105, top: eqs.length > 2 ? 395 : 360, width: 1070, height: 250 }, { fontSize: bullets.length > 4 ? 23 : 27 });
  } else if (layout === 'FA_11_COMPARACION' || layout === 'FA_06B_DOS_COLUMNAS' || layout === 'FA_02B_CONOCIMIENTOS_PREVIOS') {
    const mid = Math.ceil(bullets.length / 2);
    addRect(slide, { left: 64, top: 175, width: 552, height: 445 }, C.ivory, C.lightGray, 8, 'left-column');
    addRect(slide, { left: 664, top: 175, width: 552, height: 445 }, C.tealLight, C.teal, 8, 'right-column');
    addBulletList(slide, bullets.slice(0, mid), { left: 92, top: 205, width: 500, height: 380 }, { fontSize: bullets.length > 7 ? 22 : 25, name: 'left-bullets' });
    addBulletList(slide, bullets.slice(mid), { left: 692, top: 205, width: 500, height: 380 }, { fontSize: bullets.length > 7 ? 22 : 25, name: 'right-bullets' });
  } else if (layout === 'FA_15_ERROR_FRECUENTE') {
    addRect(slide, { left: 84, top: 180, width: 1112, height: 110 }, '#F8E8E8', C.error, 8, 'error-surface');
    addText(slide, bullets[0] ?? record.keyIdea, { left: 112, top: 205, width: 1055, height: 60 }, { fontSize: 30, bold: true, color: C.error, verticalAlignment: 'middle' }, 'error-statement');
    addRect(slide, { left: 84, top: 330, width: 1112, height: 275 }, C.tealLight, C.teal, 8, 'correction-surface');
    addBulletList(slide, bullets.slice(1), { left: 115, top: 360, width: 1045, height: 215 }, { fontSize: bullets.length > 5 ? 23 : 27 });
  } else if (layout === 'FA_14_PREGUNTA_EJERCICIO' || layout === 'FA_14B_MINI_EJERCICIO') {
    addRect(slide, { left: 88, top: 175, width: 1104, height: 440 }, C.ochreLight, C.ochre, 10, 'question-surface');
    addBulletList(slide, bullets, { left: 130, top: 215, width: 1020, height: 350 }, { fontSize: bullets.length > 6 ? 23 : 28, color: C.black });
  } else if (layout === 'FA_08_DEFINICION') {
    const lead = bullets[0] ?? record.keyIdea;
    addRect(slide, { left: 84, top: 180, width: 1112, height: 155 }, C.tealLight, C.teal, 10, 'definition-surface');
    addText(slide, lead, { left: 120, top: 210, width: 1040, height: 95 }, { fontSize: 32, color: C.black, verticalAlignment: 'middle' }, 'definition');
    addBulletList(slide, bullets.slice(1), { left: 100, top: 375, width: 1080, height: 235 }, { fontSize: bullets.length > 5 ? 23 : 27 });
  } else if (layout === 'FA_10_EJEMPLO_RESUELTO') {
    if (eqs.length) addEquationBox(slide, eqs, { left: 690, top: 205, width: 500, height: 160 }, C.ochre);
    addRect(slide, { left: 70, top: 180, width: 560, height: 430 }, C.ivory, C.lightGray, 8, 'example-surface');
    addBulletList(slide, bullets, { left: 102, top: 215, width: 500, height: 350 }, { fontSize: bullets.length > 6 ? 22 : 25 });
    if (!eqs.length) addText(slide, record.example, { left: 690, top: 215, width: 490, height: 290 }, { fontSize: 26, color: C.black }, 'example-detail');
  } else if (layout === 'FA_18_TABLA_DATOS') {
    addRect(slide, { left: 70, top: 170, width: 1140, height: 450 }, C.ivory, C.lightGray, 4, 'data-surface');
    addBulletList(slide, bullets, { left: 105, top: 205, width: 1070, height: 370 }, { fontSize: bullets.length > 8 ? 21 : 24 });
  } else {
    addBulletList(slide, bullets, { left: 90, top: 175, width: 1100, height: 430 }, { fontSize: bullets.length > 8 ? 21 : bullets.length > 6 ? 23 : 27 });
    if (eqs.length) addEquationBox(slide, eqs, { left: 190, top: 485, width: 900, height: 120 }, C.teal);
  }
}

const slideText = await fs.readFile(slideTextPath, 'utf8');
const notesText = await fs.readFile(notesPath, 'utf8');
const slideSections = splitSections(slideText);
const noteSections = splitSections(notesText);
const assets = parseCsv(await fs.readFile(manifestPath, 'utf8'));
const deck = await PresentationFile.importPptx(await FileBlob.load(starterPath));
const slides = Array.isArray(deck.slides?.items) ? deck.slides.items : Array.from({ length: deck.slides.count }, (_, i) => deck.slides.getItem(i));
if (slides.length !== 125 || slideSections.size !== 125 || noteSections.size !== 125) {
  throw new Error(`Conteos incompatibles: starter=${slides.length}, texto=${slideSections.size}, notas=${noteSections.size}.`);
}

const buildLog = [];
for (let index = 0; index < slides.length; index += 1) {
  const slide = slides[index];
  const id = `U04-${String(index + 1).padStart(3, '0')}`;
  const section = slideSections.get(id);
  const noteSection = noteSections.get(id);
  for (const item of [...(slide.shapes?.items ?? [])]) item.delete();
  for (const collection of [slide.images, slide.tables, slide.charts]) {
    for (const item of [...(collection?.items ?? [])]) {
      if (typeof item.delete === 'function') item.delete();
      else item.position = { left: -5000, top: -5000, width: 1, height: 1 };
    }
  }
  const record = {
    id,
    title: formatInline(field(section, 'Título')),
    subtitle: formatInline(field(section, 'Subtítulo')),
    bullets: visibleBullets(section),
    equations: equations(section),
    caption: field(section, 'Caption sugerido'),
    visual: field(section, 'Visual'),
    layout: (field(section, 'Layout').match(/FA_[A-Z0-9_]+/) ?? ['FA_04_TITULO_CONTENIDO'])[0],
    source: field(section, 'Fuente'),
    transition: field(section, 'Transición'),
    alt: field(section, 'Texto alternativo'),
    example: field(section, 'Ejemplo'),
  };
  const response = field(noteSection, 'Respuesta esperada');
  record.keyIdea = response && !/^No corresponde/i.test(response) ? response : (record.bullets.at(-1) ?? record.title);
  const selected = TEXT_ONLY_REVIEW_FIXES.has(id) ? [] : slideAssetsFor(id, section, assets);
  const mediaRows = assets.filter((a) => ['audio', 'video', 'video_or_gif'].includes(a.type) && ['shortlisted', 'proposed'].includes(a.status)
    && a.slide_id.split(';').map((x) => x.trim()).includes(id));
  if (selected.length) await addVisual(slide, record, selected[0], mediaRows.length > 0);
  else addTextLayout(slide, record, mediaRows.length > 0);
  const dark = ['FA_00_PORTADA', 'FA_01_DIVISOR', 'FA_21_CIERRE_PUENTE'].includes(record.layout);
  addNumber(slide, index + 1, dark);

  const sourceLines = [
    record.source ? `- ${record.source}` : '',
    ...selected.filter((a) => a.source_url).map((a) => `- ${a.source_url}`),
  ].filter(Boolean);
  const note = [
    `U04-${String(index + 1).padStart(3, '0')} · ${record.title}`,
    '',
    clean(noteSection),
    '',
    `[Texto alternativo] ${record.alt}`,
    '',
    '[Sources]',
    ...sourceLines,
    '[/Sources]',
  ].join('\n');
  slide.speakerNotes.textFrame.setText(note);
  slide.speakerNotes.setVisible(true);
  buildLog.push({ slide: index + 1, id, layout: record.layout, asset: selected[0]?.asset_id ?? '', mediaStatus: mediaRows.length ? 'static-fallback' : '' });

  if (previewDir) {
    await fs.mkdir(previewDir, { recursive: true });
    const image = await slide.export({ format: 'png', scale: 0.25 });
    await image.save(path.join(previewDir, `slide-${String(index + 1).padStart(3, '0')}.png`));
  }
}

await fs.mkdir(path.dirname(outPath), { recursive: true });
const pptx = await PresentationFile.exportPptx(deck);
await pptx.save(outPath);
await fs.writeFile(`${outPath}.build-log.json`, `${JSON.stringify(buildLog, null, 2)}\n`, 'utf8');
console.log(JSON.stringify({ outPath, slides: slides.length, assetsInserted: buildLog.filter((x) => x.asset).length, notes: slides.length }, null, 2));
