import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const PX_PER_PT = 96 / 72;
const C = {
  bordo: "#4D1434",
  bordo2: "#903163",
  carbon: "#3D3D3D",
  gris: "#76818A",
  gris2: "#D9DCE0",
  marfil: "#F7F6F2",
  fisico: "#2F7E83",
  fisicoBg: "#E7F1F1",
  clinico: "#9F541A",
  clinicoBg: "#F8EDE2",
  ok: "#2F6F55",
  alerta: "#9A641E",
  blanco: "#FFFFFF",
};

const TARGETS = new Map([
  [1, "U01-CH001"],
  [7, "U01-CH001"],
  [8, "U01-CH001"],
  [9, "U01-CH001"],
  [10, "U01-CH002"],
  [12, "U01-CH001"],
  [14, "U01-CH001"],
  [17, "U01-CH003"],
  [19, "U01-CH004"],
  [21, "U01-CH005"],
  [22, "U01-CH006"],
  [24, "U01-CH011"],
  [25, "U01-CH007"],
  [26, "U01-CH007"],
  [27, "U01-CH007"],
  [28, "U01-CH008"],
  [30, "U01-CH009"],
  [31, "U01-CH009"],
  [32, "U01-CH010"],
  [33, "U01-CH010"],
  [34, "U01-CH010"],
  [35, "U01-CH011"],
  [36, "U01-CH012"],
  [37, "U01-CH012"],
  [38, "U01-CH012"],
  [39, "U01-CH013"],
  [40, "U01-CH013"],
  [41, "U01-CH014"],
  [42, "U01-CH014"],
  [43, "U01-CH014"],
  [44, "U01-CH016"],
  [45, "U01-CH016"],
  [46, "U01-CH015"],
  [47, "U01-CH015"],
  [48, "U01-CH016"],
  [49, "U01-CH016"],
  [50, "U01-CH016"],
  [51, "U01-CH016"],
  [52, "U01-CH017"],
  [53, "U01-CH018"],
  [54, "U01-CH018"],
  [55, "U01-CH018"],
  [56, "U01-CH018"],
  [57, "U01-CH018"],
  [58, "U01-CH019"],
  [59, "U01-CH019"],
  [60, "U01-CH019"],
  [61, "U01-CH019"],
  [62, "U01-CH020"],
  [63, "U01-CH020"],
  [64, "U01-CH020"],
  [65, "U01-CH020"],
  [66, "U01-CH020"],
  [67, "U01-CH020"],
  [69, "U01-CH021"],
  [70, "U01-CH022"],
  [71, "U01-CH022"],
  [72, "U01-CH023"],
  [73, "U01-CH023"],
  [74, "U01-CH023"],
  [75, "U01-CH023"],
  [76, "U01-CH026"],
  [77, "U01-CH023"],
  [78, "U01-CH023"],
  [79, "U01-CH001"],
  [80, "U01-CH023"],
  [81, "U01-CH024"],
  [82, "U01-CH024"],
  [83, "U01-CH024"],
  [84, "U01-CH025"],
  [87, "U01-CH014"],
  [90, "U01-CH018"],
]);

const RASTER_ASSETS = new Map([
  ["U01-CH002", "u01_media_002_propagacion_particulas_diagram_fix.gif"],
  ["U01-CH015", "u01_fig_015_funcion_distancia_diagram_fix.png"],
  ["U01-CH019", "u01_fig_019_circulo_unitario_diagram_fix.png"],
  ["U01-CH020", "u01_fig_020_exponencial_log_diagram_fix.png"],
  ["U01-CH021", "u01_fig_021_escalas_lineal_log_diagram_fix.png"],
  ["U01-CH022", "u01_fig_022_razon_db_diagram_fix.png"],
  ["U01-CH026", "u01_fig_026_espectros_conceptuales_diagram_fix.png"],
]);

function fontPx(pt) {
  return pt * PX_PER_PT;
}

function rect(frame) {
  return {
    left: Number(frame.left),
    top: Number(frame.top),
    width: Number(frame.width),
    height: Number(frame.height),
  };
}

function addText(
  slide,
  name,
  position,
  text,
  { fontPt = 22, color = C.carbon, bold = false, align = "center", valign = "middle", fill = "none", line = "none", insets = 0 } = {},
) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    name,
    position,
    fill,
    line: line === "none" ? { style: "solid", fill: "none", width: 0 } : line,
  });
  shape.text = text;
  shape.text.style = {
    fontSize: fontPx(fontPt),
    typeface: "Calibri",
    color,
    bold,
    alignment: align,
    verticalAlignment: valign,
    autoFit: "none",
    wrap: "square",
    insets:
      typeof insets === "number"
        ? { top: insets, right: insets, bottom: insets, left: insets }
        : insets,
  };
  return shape;
}

function addBox(
  slide,
  name,
  position,
  text,
  {
    fontPt = 22,
    fill = C.blanco,
    stroke = C.gris2,
    color = C.carbon,
    bold = false,
    align = "center",
    padding = 17.3,
    radius = 8,
    lineWidth = 1.5,
  } = {},
) {
  const shape = slide.shapes.add({
    geometry: "roundRect",
    name,
    position,
    fill,
    line: { style: "solid", fill: stroke, width: lineWidth },
    borderRadius: radius,
  });
  shape.text = text;
  shape.text.style = {
    fontSize: fontPx(fontPt),
    typeface: "Calibri",
    color,
    bold,
    alignment: align,
    verticalAlignment: "middle",
    autoFit: "none",
    wrap: "square",
    insets: { top: padding, right: padding, bottom: padding, left: padding },
  };
  return shape;
}

function addLine(slide, name, x1, y1, x2, y2, { color = C.gris, width = 2, head = null, dash = "solid" } = {}) {
  const left = Math.min(x1, x2);
  const top = Math.min(y1, y2);
  return slide.shapes.add({
    geometry: "line",
    name,
    position: {
      left,
      top,
      width: Math.max(0.1, Math.abs(x2 - x1)),
      height: Math.max(0.1, Math.abs(y2 - y1)),
      horizontalFlip: x2 < x1,
      verticalFlip: y2 < y1,
    },
    fill: "none",
    line: { style: dash, fill: color, width },
    ...(head ? { tail: head } : {}),
  });
}

function connect(slide, name, from, to, { fromSide = "right", toSide = "left", label = "", labelFrame = null, color = C.bordo2 } = {}) {
  const connector = slide.shapes.connect(from, to, {
    kind: "straight",
    fromSide,
    toSide,
    line: { style: "solid", fill: color, width: 2.2 },
    tail: { type: "arrow", width: "sm", length: "sm" },
  });
  connector.name = name;
  connector.sendToBack();
  if (label && labelFrame) {
    addText(slide, `${name}_label`, labelFrame, label, {
      fontPt: 20,
      color,
      fill: C.blanco,
      insets: 4,
    });
  }
  return connector;
}

function deleteTargetImage(slide) {
  const images = [...slide.images.items];
  if (images.length !== 1) {
    throw new Error(`Expected one image on slide ${slide.slideNumber}; found ${images.length}`);
  }
  const image = images[0];
  const frame = rect(image.resolveFrame());
  const alt = image.alt ?? "";
  image.delete();
  return { frame, alt };
}

function modeFor(frame) {
  if (frame.width < 420 || frame.height < 235) return "mini";
  if (frame.width < 650 || frame.height < 330) return "compact";
  return "full";
}

function drawMiniMotif(slide, assetId, frame, colors = [C.fisico, C.bordo2, C.clinico]) {
  const cy = frame.top + frame.height / 2;
  const radius = Math.min(frame.height * 0.18, frame.width * 0.06);
  const xs = [0.22, 0.5, 0.78].map((fraction) => frame.left + frame.width * fraction);
  const nodes = xs.map((x, index) =>
    slide.shapes.add({
      geometry: index === 1 ? "roundRect" : "ellipse",
      name: `${assetId}_mini_node_${index + 1}`,
      position: { left: x - radius, top: cy - radius, width: radius * 2, height: radius * 2 },
      fill: index === 0 ? C.fisicoBg : index === 1 ? C.marfil : C.clinicoBg,
      line: { style: "solid", fill: colors[index], width: 2 },
    }),
  );
  connect(slide, `${assetId}_mini_link_1`, nodes[0], nodes[1], { color: C.bordo2 });
  connect(slide, `${assetId}_mini_link_2`, nodes[1], nodes[2], { color: C.clinico });
}

function drawFmr(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") return drawMiniMotif(slide, assetId, frame);
  const gap = mode === "compact" ? 8 : 28;
  const nodeW = (frame.width - 2 * gap) / 3;
  const nodeH = mode === "compact" ? frame.height * 0.56 : frame.height * 0.58;
  const y = frame.top + frame.height * 0.20;
  const specs = [
    ["FUENTE", "origina la perturbación\nvoz · parlante", C.fisicoBg, C.fisico],
    ["MEDIO", "permite la propagación\naire · agua · sólido", C.marfil, C.bordo],
    ["RECEPTOR", "responde a la perturbación\noído · micrófono", C.clinicoBg, C.clinico],
  ];
  const nodes = specs.map(([title, body, fill, stroke], index) => {
    const x = frame.left + index * (nodeW + gap);
    const node = slide.shapes.add({
      geometry: "roundRect",
      name: `${assetId}_node_${index + 1}`,
      position: { left: x, top: y, width: nodeW, height: nodeH },
      fill,
      line: { style: "solid", fill: stroke, width: 2 },
      borderRadius: 8,
    });
    addText(slide, `${assetId}_node_${index + 1}_title`, { left: x + 17.3, top: y + 13, width: nodeW - 34.6, height: 38 }, title, {
      fontPt: mode === "compact" ? 22 : 24,
      color: stroke,
      bold: true,
      insets: 0,
    });
    if (mode === "full") {
      addText(slide, `${assetId}_node_${index + 1}_body`, { left: x + 17.3, top: y + 58, width: nodeW - 34.6, height: nodeH - 72 }, body, {
        fontPt: 22,
        color: C.carbon,
        insets: 0,
      });
    }
    return node;
  });
  const gapCenter1 = frame.left + nodeW + gap / 2;
  const gapCenter2 = frame.left + nodeW * 2 + gap * 1.5;
  connect(slide, `${assetId}_link_1`, nodes[0], nodes[1], {
    label: mode === "full" ? "perturbación" : "",
    labelFrame: { left: gapCenter1 - 95, top: y - 38, width: 190, height: 30 },
  });
  connect(slide, `${assetId}_link_2`, nodes[1], nodes[2], {
    label: mode === "full" ? "se propaga" : "",
    labelFrame: { left: gapCenter2 - 95, top: y - 38, width: 190, height: 30 },
  });
}

function drawMeasurement(slide, frame, assetId) {
  const equationW = frame.width * 0.34;
  const equationX = frame.left + (frame.width - equationW) / 2;
  const equationY = frame.top + frame.height * 0.37;
  addText(slide, `${assetId}_equation`, { left: equationX, top: equationY, width: equationW, height: 78 }, "d = 2 m", {
    fontPt: 40,
    color: C.carbon,
    insets: 0,
  });
  const w = frame.width * 0.22;
  const h = 72;
  const callouts = [
    ["símbolo", frame.left + frame.width * 0.04, frame.top + 8, equationX + equationW * 0.18, equationY + 34],
    ["valor", frame.left + frame.width * 0.76, frame.top + 8, equationX + equationW * 0.60, equationY + 34],
    ["igualdad", frame.left + frame.width * 0.14, frame.top + frame.height - h - 8, equationX + equationW * 0.40, equationY + 50],
    ["unidad", frame.left + frame.width * 0.64, frame.top + frame.height - h - 8, equationX + equationW * 0.82, equationY + 50],
  ];
  for (const [label, x, y, tx, ty] of callouts) {
    addBox(slide, `${assetId}_callout_${label}`, { left: x, top: y, width: w, height: h }, label, {
      fontPt: 22,
      fill: C.marfil,
      stroke: C.gris,
      padding: 17.3,
    });
    const startX = x + w / 2;
    const startY = y < equationY ? y + h : y;
    const endY = y < equationY ? ty - 10 : ty + 10;
    addLine(slide, `${assetId}_leader_${label}`, startX, startY, tx, endY, {
      color: C.bordo2,
      width: 1.8,
    }).sendToBack();
  }
}

function drawSi(slide, frame, assetId) {
  const gap = 8;
  const topW = (frame.width - gap * 2) / 3;
  const topH = 82;
  const yTop = frame.top + 10;
  const bases = [
    ["tiempo\ns", C.fisico],
    ["longitud\nm", C.fisico],
    ["masa\nkg", C.fisico],
  ].map(([text, stroke], index) =>
    addBox(slide, `${assetId}_base_${index + 1}`, { left: frame.left + index * (topW + gap), top: yTop, width: topW, height: topH }, text, {
      fontPt: 22,
      bold: true,
      fill: C.fisicoBg,
      stroke,
      padding: 14,
    }),
  );
  const derived = addBox(
    slide,
    `${assetId}_derived`,
    { left: frame.left + frame.width * 0.10, top: frame.top + frame.height - 146, width: frame.width * 0.80, height: 132 },
    "DERIVADAS\nrapidez · aceleración\nfuerza · presión · densidad",
    { fontPt: 22, fill: C.marfil, stroke: C.bordo2, padding: 17.3 },
  );
  for (const [index, base] of bases.entries()) {
    const connector = slide.shapes.connect(base, derived, {
      kind: "elbow",
      fromSide: "bottom",
      toSide: "top",
      line: { style: "solid", fill: C.gris, width: 1.8 },
      tail: { type: "arrow", width: "sm", length: "sm" },
    });
    connector.name = `${assetId}_dependency_${index + 1}`;
    connector.sendToBack();
  }
}

function drawUnitConstruction(slide, frame, assetId) {
  const rows = [
    ["m / s", "distancia ÷ tiempo", "rapidez"],
    ["kg · m/s² = N", "masa × aceleración", "fuerza"],
    ["N/m² = Pa", "fuerza ÷ área", "presión"],
  ];
  const rowGap = 14;
  const rowH = (frame.height - rowGap * 2) / 3;
  for (const [index, [formula, relation, result]] of rows.entries()) {
    const y = frame.top + index * (rowH + rowGap);
    const formulaBox = addBox(slide, `${assetId}_formula_${index + 1}`, { left: frame.left, top: y, width: frame.width * 0.54, height: rowH }, formula, {
      fontPt: 28,
      fill: C.marfil,
      stroke: C.gris2,
      padding: 17.3,
    });
    const resultBox = addBox(slide, `${assetId}_result_${index + 1}`, { left: frame.left + frame.width * 0.77, top: y + 4, width: frame.width * 0.23, height: rowH - 8 }, result, {
      fontPt: 22,
      fill: C.fisicoBg,
      stroke: C.fisico,
      padding: 17.3,
    });
    connect(slide, `${assetId}_relation_${index + 1}`, formulaBox, resultBox, {
      label: relation,
      labelFrame: { left: frame.left + frame.width * 0.54, top: y + 3, width: frame.width * 0.23, height: 34 },
      color: C.fisico,
    });
  }
}

function drawQuantityTable(slide, frame, assetId) {
  const values = [
    ["Magnitud", "Símbolo", "Relación", "Unidad"],
    ["Distancia", "d", "—", "m"],
    ["Tiempo", "t, Δt", "—", "s"],
    ["Rapidez", "v", "d/Δt", "m/s"],
    ["Aceleración", "a", "Δv/Δt", "m/s²"],
    ["Fuerza", "F", "ma", "N"],
    ["Presión", "p", "F⊥/S", "Pa"],
    ["Densidad", "ρ", "m/V", "kg/m³"],
    ["Frecuencia", "f", "N/Δt", "Hz"],
  ];
  const table = slide.tables.add({
    rows: values.length,
    columns: 4,
    left: frame.left,
    top: frame.top,
    width: frame.width,
    height: frame.height,
    values,
    columnWidths: [frame.width * 0.29, frame.width * 0.17, frame.width * 0.34, frame.width * 0.20],
  });
  table.name = `${assetId}_native_table`;
  table.borders.assign({ style: "solid", fill: C.gris2, width: 1 });
  const all = table.cells.block({ row: 0, column: 0, rowCount: values.length, columnCount: 4 });
  all.assign({
    textStyle: { fontSize: fontPx(22), color: C.carbon, typeface: "Calibri" },
    margins: { top: 3, right: 6, bottom: 3, left: 6 },
    anchor: "middle",
  });
  const header = table.cells.block({ row: 0, column: 0, rowCount: 1, columnCount: 4 });
  header.assign({
    fill: C.bordo,
    textStyle: { color: C.blanco, bold: true, fontSize: fontPx(22), typeface: "Calibri" },
  });
  for (let row = 2; row < values.length; row += 2) {
    table.cells.block({ row, column: 0, rowCount: 1, columnCount: 4 }).fill = C.marfil;
  }
}

function drawKinematics(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "compact") {
    const rows = [
      ["RAPIDEZ", "d/Δt", C.fisico],
      ["VELOCIDAD", "módulo + dirección", C.bordo2],
      ["PROPAGACIÓN", "avanza el frente", C.clinico],
    ];
    const gap = 10;
    const rowH = (frame.height - gap * 2) / 3;
    rows.forEach(([title, body, color], index) =>
      addBox(
        slide,
        `${assetId}_row_${index + 1}`,
        { left: frame.left, top: frame.top + index * (rowH + gap), width: frame.width, height: rowH },
        `${title}  —  ${body}`,
        {
          fontPt: 22,
          fill: index === 1 ? C.marfil : C.blanco,
          stroke: color,
          padding: 14,
        },
      ),
    );
    return;
  }
  const gap = 18;
  const panelW = (frame.width - gap * 2) / 3;
  const labels = [
    ["RAPIDEZ", "d/Δt", C.fisico],
    ["VELOCIDAD", "módulo + dirección", C.bordo2],
    ["PROPAGACIÓN", "avanza el frente", C.clinico],
  ];
  for (const [index, [title, subtitle, color]] of labels.entries()) {
    const x = frame.left + index * (panelW + gap);
    addBox(slide, `${assetId}_panel_${index + 1}`, { left: x, top: frame.top, width: panelW, height: frame.height }, "", {
      fill: C.blanco,
      stroke: C.gris2,
      padding: 17.3,
    });
    addText(slide, `${assetId}_panel_${index + 1}_title`, { left: x + 17.3, top: frame.top + 14, width: panelW - 34.6, height: 42 }, title, {
      fontPt: 22,
      color,
      bold: true,
      insets: 0,
    });
    if (mode !== "mini") {
      addText(slide, `${assetId}_panel_${index + 1}_body`, { left: x + 17.3, top: frame.top + 72, width: panelW - 34.6, height: frame.height - 90 }, subtitle, {
        fontPt: 22,
        color: C.carbon,
        insets: 0,
      });
    }
  }
}

function drawPropagationTime(slide, frame, assetId) {
  const top = frame.top + 12;
  const y = top + 48;
  const source = slide.shapes.add({
    geometry: "ellipse",
    name: `${assetId}_source`,
    position: { left: frame.left + 18, top: y, width: 42, height: 42 },
    fill: C.bordo2,
    line: { style: "solid", fill: C.bordo2, width: 1 },
  });
  const receptor = slide.shapes.add({
    geometry: "rect",
    name: `${assetId}_receiver`,
    position: { left: frame.left + frame.width - 60, top: y, width: 42, height: 42 },
    fill: C.clinico,
    line: { style: "solid", fill: C.clinico, width: 1 },
  });
  connect(slide, `${assetId}_distance`, source, receptor, {
    label: "d = 100 m",
    labelFrame: { left: frame.left + frame.width * 0.38, top: y - 42, width: frame.width * 0.24, height: 34 },
    color: C.fisico,
  });
  addBox(
    slide,
    `${assetId}_calculation`,
    { left: frame.left + frame.width * 0.10, top: frame.top + frame.height * 0.48, width: frame.width * 0.80, height: frame.height * 0.34 },
    "t = d/c = 100 m ÷ 343 m/s = 0,29 s",
    { fontPt: 28, fill: C.marfil, stroke: C.bordo2, padding: 17.3 },
  );
}

function drawMassWeight(slide, frame, assetId) {
  const gap = 24;
  const panelW = (frame.width - gap) / 2;
  const panels = [
    ["MASA", "inercia", "kg", C.fisicoBg, C.fisico],
    ["PESO", "fuerza gravitatoria", "Fg = m·g    N", C.clinicoBg, C.clinico],
  ];
  panels.forEach(([title, body, equation, fill, stroke], index) => {
    const x = frame.left + index * (panelW + gap);
    const panelY = frame.top + frame.height * 0.12;
    const panelH = frame.height * 0.76;
    addBox(slide, `${assetId}_panel_${index + 1}`, { left: x, top: panelY, width: panelW, height: panelH }, "", {
      fill,
      stroke,
      padding: 17.3,
    });
    addText(slide, `${assetId}_panel_${index + 1}_title`, { left: x + 17.3, top: panelY + 18, width: panelW - 34.6, height: 44 }, title, {
      fontPt: 24,
      color: stroke,
      bold: true,
      insets: 0,
    });
    addText(slide, `${assetId}_panel_${index + 1}_body`, { left: x + 17.3, top: panelY + 82, width: panelW - 34.6, height: 54 }, body, {
      fontPt: 22,
      color: C.carbon,
      insets: 0,
    });
    addText(slide, `${assetId}_panel_${index + 1}_equation`, { left: x + 17.3, top: panelY + panelH - 78, width: panelW - 34.6, height: 54 }, equation, {
      fontPt: 28,
      color: C.bordo,
      insets: 0,
    });
  });
}

function drawFpd(slide, frame, assetId, slideNumber) {
  const focus = slideNumber === 32 ? 0 : slideNumber === 33 ? 1 : 2;
  const specs = [
    ["FUERZA", "F = m·a", "fuerza neta → aceleración", C.fisico],
    ["PRESIÓN", "p = F⊥/S", "misma fuerza; cambia el área", C.bordo2],
    ["DENSIDAD", "ρ = m/V", "misma masa; cambia el volumen", C.clinico],
  ];
  const gap = 16;
  const panelW = (frame.width - gap * 2) / 3;
  const visualHeight = Math.max(170, frame.height - 45);
  specs.forEach(([title, equation, body, color], index) => {
    const x = frame.left + index * (panelW + gap);
    const active = index === focus;
    addBox(slide, `${assetId}_panel_${index + 1}`, { left: x, top: frame.top, width: panelW, height: visualHeight }, "", {
      fill: active ? C.marfil : C.blanco,
      stroke: active ? color : C.gris2,
      lineWidth: active ? 2.5 : 1.2,
      padding: 17.3,
    });
    addText(slide, `${assetId}_panel_${index + 1}_title`, { left: x + 12, top: frame.top + 10, width: panelW - 24, height: 36 }, title, {
      fontPt: 22,
      color,
      bold: true,
      insets: 0,
    });
    addText(slide, `${assetId}_panel_${index + 1}_equation`, { left: x + 12, top: frame.top + 58, width: panelW - 24, height: 50 }, equation, {
      fontPt: 26,
      color: C.bordo,
      insets: 0,
    });
    if (frame.height >= 235) {
      addText(slide, `${assetId}_panel_${index + 1}_body`, { left: x + 17.3, top: frame.top + 118, width: panelW - 34.6, height: visualHeight - 132 }, body, {
        fontPt: 22,
        color: C.carbon,
        insets: 0,
      });
    }
  });
}

function drawNetwork(slide, frame, assetId) {
  if (modeFor(frame) === "mini") return drawMiniMotif(slide, assetId, frame);
  const rows = [
    ["d ÷ Δt", "→", "v"],
    ["m × a", "→", "F", "    F ÷ S", "→", "p"],
    ["m ÷ V", "→", "ρ"],
  ];
  const gap = 14;
  const rowH = (frame.height - gap * 2) / 3;
  rows.forEach((tokens, index) => {
    addBox(slide, `${assetId}_relation_row_${index + 1}`, { left: frame.left, top: frame.top + index * (rowH + gap), width: frame.width, height: rowH }, tokens.join("  "), {
      fontPt: 24,
      fill: index % 2 ? C.marfil : C.fisicoBg,
      stroke: index % 2 ? C.bordo2 : C.fisico,
      padding: 17.3,
    });
  });
}

function drawNotation(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") {
    return addText(slide, `${assetId}_mini_equivalence`, frame, "10⁻⁵  ↔  µ", {
      fontPt: 28,
      color: C.blanco,
      bold: true,
      insets: 8,
    });
  }
  if (mode === "compact") {
    const rows = [
      ["DECIMAL", "0,000020 Pa"],
      ["CIENTÍFICA", "2,0 × 10⁻⁵ Pa"],
      ["PREFIJO", "20 µPa"],
    ];
    const gap = 10;
    const rowH = (frame.height - gap * 2) / 3;
    rows.forEach(([label, value], index) =>
      addBox(
        slide,
        `${assetId}_row_${index + 1}`,
        { left: frame.left, top: frame.top + index * (rowH + gap), width: frame.width, height: rowH },
        `${label}  —  ${value}`,
        {
          fontPt: 22,
          fill: index === 1 ? C.marfil : C.blanco,
          stroke: C.gris2,
          color: index === 1 ? C.bordo : C.carbon,
          padding: 14,
        },
      ),
    );
    return;
  }
  const gap = 18;
  const cardW = (frame.width - gap * 2) / 3;
  const cards = [
    ["DECIMAL", "0,000020 Pa"],
    ["CIENTÍFICA", "2,0 × 10⁻⁵ Pa"],
    ["PREFIJO", "20 µPa"],
  ];
  cards.forEach(([title, value], index) => {
    const x = frame.left + index * (cardW + gap);
    addBox(slide, `${assetId}_card_${index + 1}`, { left: x, top: frame.top, width: cardW, height: frame.height }, "", {
      fill: C.marfil,
      stroke: C.gris2,
      padding: 17.3,
    });
    addText(slide, `${assetId}_card_${index + 1}_title`, { left: x + 17.3, top: frame.top + 18, width: cardW - 34.6, height: 42 }, title, {
      fontPt: 22,
      color: C.bordo,
      bold: true,
      insets: 0,
    });
    addText(slide, `${assetId}_card_${index + 1}_value`, { left: x + 17.3, top: frame.top + 78, width: cardW - 34.6, height: frame.height - 96 }, value, {
      fontPt: 28,
      color: C.carbon,
      insets: 0,
    });
  });
}

function drawPrefixes(slide, frame, assetId) {
  const entries = [
    ["kilo", "k", "10³"],
    ["unidad", "—", "10⁰"],
    ["mili", "m", "10⁻³"],
    ["micro", "µ", "10⁻⁶"],
  ];
  const xs = entries.map((_, index) => frame.left + frame.width * (0.10 + index * 0.267));
  const y = frame.top + frame.height * 0.52;
  addLine(slide, `${assetId}_axis`, xs[0], y, xs[3], y, { color: C.gris2, width: 4 });
  entries.forEach(([name, symbol, factor], index) => {
    slide.shapes.add({
      geometry: "ellipse",
      name: `${assetId}_marker_${index + 1}`,
      position: { left: xs[index] - 11, top: y - 11, width: 22, height: 22 },
      fill: index === 1 ? C.bordo2 : C.fisico,
      line: { style: "solid", fill: C.blanco, width: 1 },
    });
    addText(slide, `${assetId}_prefix_${index + 1}`, { left: xs[index] - frame.width * 0.10, top: frame.top + 8, width: frame.width * 0.20, height: 68 }, `${name}\n${symbol}`, {
      fontPt: 22,
      color: C.bordo,
      bold: true,
      insets: 0,
    });
    addText(slide, `${assetId}_factor_${index + 1}`, { left: xs[index] - frame.width * 0.10, top: y + 24, width: frame.width * 0.20, height: 48 }, factor, {
      fontPt: 24,
      color: C.carbon,
      insets: 0,
    });
  });
}

function drawDimensions(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") {
    return addText(slide, `${assetId}_mini_dimensions`, frame, "[M]   [L]   [T]  →  [v]   [a]   [F]   [p]   [ρ]", {
      fontPt: 22,
      color: C.bordo,
      insets: 6,
    });
  }
  const gap = 18;
  const topW = (frame.width - gap * 2) / 3;
  ["[M]", "[L]", "[T]"].forEach((label, index) =>
    addBox(slide, `${assetId}_base_${index + 1}`, { left: frame.left + index * (topW + gap), top: frame.top, width: topW, height: 70 }, label, {
      fontPt: 24,
      fill: C.fisicoBg,
      stroke: C.fisico,
      padding: 14,
    }),
  );
  const formulas = [
    "[v] = L T⁻¹    [a] = L T⁻²",
    "[F] = M L T⁻²    [p] = M L⁻¹ T⁻²",
    "[ρ] = M L⁻³",
  ];
  const startY = frame.top + 92;
  const rowGap = 10;
  const rowH = (frame.height - 92 - rowGap * 2) / 3;
  formulas.forEach((formula, index) =>
    addBox(slide, `${assetId}_derived_${index + 1}`, { left: frame.left, top: startY + index * (rowH + rowGap), width: frame.width, height: rowH }, formula, {
      fontPt: 22,
      fill: index === 1 ? C.marfil : C.blanco,
      stroke: C.bordo2,
      padding: 14,
    }),
  );
}

function drawInverse(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") return drawMiniMotif(slide, assetId, frame);
  const gap = 22;
  const boxW = (frame.width - gap * 2) / 3;
  const boxH = frame.height * 0.38;
  const y = frame.top + frame.height * 0.18;
  const specs = [
    ["entrada\nt (s)", C.fisicoBg, C.fisico],
    ["regla\nd = c·t", C.marfil, C.bordo2],
    ["salida\nd (m)", C.fisicoBg, C.fisico],
  ];
  const nodes = specs.map(([text, fill, stroke], index) =>
    addBox(slide, `${assetId}_node_${index + 1}`, { left: frame.left + index * (boxW + gap), top: y, width: boxW, height: boxH }, text, {
      fontPt: 22,
      fill,
      stroke,
      padding: 17.3,
    }),
  );
  connect(slide, `${assetId}_forward_1`, nodes[0], nodes[1], { color: C.fisico });
  connect(slide, `${assetId}_forward_2`, nodes[1], nodes[2], { color: C.fisico });
  addText(slide, `${assetId}_inverse_label`, { left: frame.left + frame.width * 0.20, top: y + boxH + 26, width: frame.width * 0.60, height: 50 }, "inversa:  t = d/c  recupera la entrada", {
    fontPt: 22,
    color: C.bordo,
    insets: 0,
  });
  addLine(slide, `${assetId}_inverse_arrow`, frame.left + frame.width * 0.78, y + boxH + 14, frame.left + frame.width * 0.22, y + boxH + 14, {
    color: C.bordo2,
    width: 2.2,
    head: { type: "arrow", width: "sm", length: "sm" },
  });
  addText(
    slide,
    `${assetId}_inverse_arrowhead`,
    { left: frame.left + frame.width * 0.22 - 15, top: y + boxH + 2, width: 30, height: 26 },
    "◀",
    { fontPt: 18, bold: true, color: C.bordo2, insets: 0 },
  );
}

function drawInverseReciprocal(slide, frame, assetId) {
  const gap = 24;
  const w = (frame.width - gap) / 2;
  addBox(slide, `${assetId}_inverse`, { left: frame.left, top: frame.top, width: w, height: frame.height }, "FUNCIÓN INVERSA\nf(x)=2x\nf⁻¹(x)=x/2\nf(f⁻¹(x))=x", {
    fontPt: 22,
    fill: C.fisicoBg,
    stroke: C.fisico,
    padding: 17.3,
  });
  addBox(slide, `${assetId}_reciprocal`, { left: frame.left + w + gap, top: frame.top, width: w, height: frame.height }, "RECÍPROCO\nf(x)=2x\n1/f(x)=1/(2x)\nx ≠ 0", {
    fontPt: 22,
    fill: C.clinicoBg,
    stroke: C.clinico,
    padding: 17.3,
  });
}

function drawTriangle(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") {
    const x = frame.left + frame.width * 0.22;
    const y = frame.top + frame.height * 0.75;
    addLine(slide, `${assetId}_mini_vertical`, x, y, x, frame.top + frame.height * 0.24, { color: C.blanco, width: 3 });
    addLine(slide, `${assetId}_mini_base`, x, y, frame.left + frame.width * 0.76, y, { color: C.blanco, width: 3 });
    addLine(slide, `${assetId}_mini_hypotenuse`, x, frame.top + frame.height * 0.24, frame.left + frame.width * 0.76, y, { color: "#7CC5C8", width: 3 });
    return;
  }
  const usableHeight = Math.max(180, frame.height - 70);
  const triLeft = frame.left + frame.width * 0.06;
  const triRight = frame.left + frame.width * 0.58;
  const triTop = frame.top + frame.height * 0.12;
  const triBottom = frame.top + usableHeight * 0.88;
  addLine(slide, `${assetId}_vertical`, triLeft, triBottom, triLeft, triTop, { color: C.fisico, width: 3 });
  addLine(slide, `${assetId}_base`, triLeft, triBottom, triRight, triBottom, { color: C.fisico, width: 3 });
  addLine(slide, `${assetId}_hypotenuse`, triLeft, triTop, triRight, triBottom, { color: C.bordo2, width: 3 });
  addText(slide, `${assetId}_opposite`, { left: triLeft + 16, top: triTop + frame.height * 0.24, width: frame.width * 0.24, height: 44 }, "opuesto = 3", {
    fontPt: 22,
    color: C.bordo,
    align: "left",
    insets: 0,
  });
  addText(slide, `${assetId}_adjacent`, { left: triLeft + frame.width * 0.12, top: triBottom - 48, width: frame.width * 0.28, height: 44 }, "adyacente = 4", {
    fontPt: 22,
    color: C.bordo,
    insets: 0,
  });
  const formulaX = frame.left + frame.width * 0.64;
  const formulaW = frame.width * 0.34;
  ["sin θ = 3/5", "cos θ = 4/5", "tan θ = 3/4"].forEach((formula, index) =>
    addBox(slide, `${assetId}_ratio_${index + 1}`, { left: formulaX, top: frame.top + 8 + index * ((usableHeight - 12) / 3), width: formulaW, height: (usableHeight - 36) / 3 }, formula, {
      fontPt: 22,
      fill: C.marfil,
      stroke: C.gris2,
      padding: 14,
    }),
  );
}

function drawChartMini(slide, assetId, frame, kind) {
  const x0 = frame.left + frame.width * 0.12;
  const y0 = frame.top + frame.height * 0.82;
  const x1 = frame.left + frame.width * 0.88;
  const y1 = frame.top + frame.height * 0.18;
  addLine(slide, `${assetId}_mini_x`, x0, y0, x1, y0, { color: C.blanco, width: 1.8 });
  addLine(slide, `${assetId}_mini_y`, x0, y0, x0, y1, { color: C.blanco, width: 1.8 });
  if (kind === "exp") {
    const points = [
      [0.12, 0.78],
      [0.28, 0.74],
      [0.44, 0.64],
      [0.60, 0.46],
      [0.75, 0.20],
    ];
    for (let index = 0; index < points.length - 1; index += 1) {
      addLine(
        slide,
        `${assetId}_mini_curve_${index}`,
        frame.left + frame.width * points[index][0],
        frame.top + frame.height * points[index][1],
        frame.left + frame.width * points[index + 1][0],
        frame.top + frame.height * points[index + 1][1],
        { color: "#7CC5C8", width: 3 },
      );
    }
  }
}

function drawDbMapping(slide, frame, assetId) {
  const values = [
    ["1", "0 dB"],
    ["10", "10 dB"],
    ["100", "20 dB"],
    ["1000", "30 dB"],
  ];
  const gap = 10;
  const w = (frame.width - gap * 3) / 4;
  values.forEach(([ratio, level], index) => {
    const x = frame.left + index * (w + gap);
    addBox(
      slide,
      `${assetId}_mapping_${index + 1}`,
      { left: x, top: frame.top + frame.height * 0.16, width: w, height: frame.height * 0.68 },
      `${ratio}\n↓\n${level}`,
      {
        fontPt: 22,
        fill: index % 2 ? C.marfil : C.fisicoBg,
        stroke: index % 2 ? C.bordo2 : C.fisico,
        padding: 14,
      },
    );
  });
}

function drawMatrix(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") {
    const gap = 8;
    const w = (frame.width - gap * 3) / 4;
    [C.fisicoBg, C.marfil, C.clinicoBg, "#F1F1F1"].forEach((fill, index) =>
      slide.shapes.add({
        geometry: "roundRect",
        name: `${assetId}_mini_column_${index + 1}`,
        position: { left: frame.left + index * (w + gap), top: frame.top + frame.height * 0.18, width: w, height: frame.height * 0.64 },
        fill,
        line: { style: "solid", fill: [C.fisico, C.bordo, C.clinico, C.gris][index], width: 1.5 },
        borderRadius: 5,
      }),
    );
    return;
  }
  if (mode === "compact") {
    const entries = [
      ["MEDICIÓN FÍSICA", C.fisicoBg, C.fisico],
      ["NIVEL REFERIDO", C.marfil, C.bordo],
      ["ATRIBUTO PERCEPTUAL", C.clinicoBg, C.clinico],
      ["RESPUESTA / CONCLUSIÓN", "#F1F1F1", C.gris],
    ];
    const gap = 10;
    const w = (frame.width - gap) / 2;
    const usableHeight = frame.height - 24;
    const h = (usableHeight - gap) / 2;
    entries.forEach(([title, fill, stroke], index) =>
      addBox(
        slide,
        `${assetId}_cell_${index + 1}`,
        {
          left: frame.left + (index % 2) * (w + gap),
          top: frame.top + Math.floor(index / 2) * (h + gap),
          width: w,
          height: h,
        },
        title,
        {
          fontPt: 22,
          fill,
          stroke,
          color: stroke === C.gris ? C.carbon : stroke,
          bold: true,
          padding: 17.3,
        },
      ),
    );
    return;
  }
  const columns = [
    ["MEDICIÓN\nFÍSICA", mode === "full" ? "frecuencia\namplitud\npresión" : "", C.fisicoBg, C.fisico],
    ["NIVEL\nREFERIDO", mode === "full" ? "dB HL\nrequiere referencia" : "", C.marfil, C.bordo],
    ["ATRIBUTO\nPERCEPTUAL", mode === "full" ? "altura tonal\nsonoridad\ntimbre" : "", C.clinicoBg, C.clinico],
    ["RESPUESTA /\nCONCLUSIÓN", mode === "full" ? "“detectado”\nconducta\nclínica" : "", "#F1F1F1", C.gris],
  ];
  const gap = 10;
  const w = (frame.width - gap * 3) / 4;
  const visualHeight = frame.height - 80;
  columns.forEach(([title, body, fill, stroke], index) => {
    const x = frame.left + index * (w + gap);
    addBox(slide, `${assetId}_column_${index + 1}`, { left: x, top: frame.top, width: w, height: visualHeight }, "", {
      fill,
      stroke,
      padding: 17.3,
    });
    addText(slide, `${assetId}_column_${index + 1}_title`, { left: x + 10, top: frame.top + 12, width: w - 20, height: mode === "full" ? 70 : frame.height - 24 }, title, {
      fontPt: 22,
      color: stroke === C.gris ? C.carbon : stroke,
      bold: true,
      insets: 0,
    });
    if (mode === "full") {
      addText(slide, `${assetId}_column_${index + 1}_body`, { left: x + 17.3, top: frame.top + 92, width: w - 34.6, height: visualHeight - 110 }, body, {
        fontPt: 22,
        color: C.carbon,
        insets: 0,
      });
    }
  });
}

function drawCase(slide, frame, assetId) {
  const mode = modeFor(frame);
  if (mode === "mini") return drawMiniMotif(slide, assetId, frame);
  const gap = 8;
  const w = (frame.width - gap * 2) / 3;
  const topH = frame.height * 0.34;
  const nodes = [
    ["FUENTE", C.fisicoBg, C.fisico],
    ["MEDIO", C.marfil, C.bordo],
    ["RECEPTOR", C.clinicoBg, C.clinico],
  ].map(([text, fill, stroke], index) =>
    addBox(slide, `${assetId}_node_${index + 1}`, { left: frame.left + index * (w + gap), top: frame.top, width: w, height: topH }, text, {
      fontPt: 22,
      bold: true,
      fill,
      stroke,
      padding: 10,
    }),
  );
  connect(slide, `${assetId}_chain_1`, nodes[0], nodes[1], { color: C.bordo2 });
  connect(slide, `${assetId}_chain_2`, nodes[1], nodes[2], { color: C.clinico });
  const results = ["t = 0,020 s", "f = 200 Hz", "LQ = 20 dB"];
  results.forEach((text, index) =>
    addBox(slide, `${assetId}_result_${index + 1}`, { left: frame.left + index * (w + gap), top: frame.top + frame.height * 0.54, width: w, height: frame.height * 0.34 }, text, {
      fontPt: 24,
      fill: index === 2 ? C.marfil : C.fisicoBg,
      stroke: index === 2 ? C.bordo2 : C.fisico,
      padding: 17.3,
    }),
  );
}

function drawCourseDependencies(slide, frame, assetId) {
  if (frame.width < 500) {
    const center = addBox(
      slide,
      `${assetId}_u1`,
      { left: frame.left + frame.width * 0.37, top: frame.top + frame.height * 0.37, width: frame.width * 0.26, height: frame.height * 0.26 },
      "U1",
      { fontPt: 24, bold: true, fill: C.bordo, stroke: C.bordo, color: C.blanco, padding: 14 },
    );
    const positions = [
      [frame.left + 4, frame.top + 6, "U2"],
      [frame.left + frame.width * 0.74 - 4, frame.top + 6, "U3"],
      [frame.left + frame.width * 0.37, frame.top + frame.height * 0.72, "U4"],
    ];
    positions.forEach(([left, top, label], index) => {
      const node = addBox(
        slide,
        `${assetId}_future_${index + 1}`,
        { left, top, width: frame.width * 0.26, height: frame.height * 0.22 },
        label,
        { fontPt: 22, bold: true, fill: C.marfil, stroke: C.fisico, padding: 14 },
      );
      const connector = slide.shapes.connect(center, node, {
        kind: "elbow",
        fromSide: index === 2 ? "bottom" : index === 0 ? "left" : "right",
        toSide: index === 2 ? "top" : "bottom",
        line: { style: "solid", fill: "#7CC5C8", width: 2 },
        tail: { type: "arrow", width: "sm", length: "sm" },
      });
      connector.sendToBack();
    });
    return;
  }
  const centerW = frame.width * 0.30;
  const centerH = frame.height * 0.28;
  const center = addBox(slide, `${assetId}_u1`, { left: frame.left + frame.width * 0.35, top: frame.top + frame.height * 0.36, width: centerW, height: centerH }, "UNIDAD 1", {
    fontPt: 24,
    bold: true,
    fill: C.bordo,
    stroke: C.bordo,
    color: C.blanco,
    padding: 17.3,
  });
  const specs = [
    ["UNIDAD 2\nmecánica", frame.left + 4, frame.top + 4],
    ["UNIDAD 3\nondas", frame.left + frame.width * 0.70 - 4, frame.top + 4],
    ["UNIDAD 4\nmagnitudes", frame.left + frame.width * 0.35, frame.top + frame.height * 0.74],
  ];
  specs.forEach(([text, x, y], index) => {
    const box = addBox(slide, `${assetId}_future_${index + 1}`, { left: x, top: y, width: frame.width * 0.30, height: frame.height * 0.24 }, text, {
      fontPt: 22,
      fill: C.marfil,
      stroke: C.fisico,
      padding: 14,
    });
    const connector = slide.shapes.connect(center, box, {
      kind: "elbow",
      fromSide: index === 2 ? "bottom" : index === 0 ? "left" : "right",
      toSide: index === 2 ? "top" : "bottom",
      line: { style: "solid", fill: C.fisico, width: 2 },
      tail: { type: "arrow", width: "sm", length: "sm" },
    });
    connector.name = `${assetId}_dependency_${index + 1}`;
    connector.sendToBack();
  });
}

async function readBytes(filePath) {
  const bytes = await fs.readFile(filePath);
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

async function replaceRaster(slide, assetId, image, assetDir, slideNumber) {
  if ((assetId === "U01-CH019" && slideNumber === 53) || (assetId === "U01-CH020" && slideNumber === 62)) {
    const frame = rect(image.resolveFrame());
    image.delete();
    if (assetId === "U01-CH019") drawTriangle(slide, frame, "U01-CH018");
    else drawChartMini(slide, assetId, frame, "exp");
    return { mode: "native-mini", frame };
  }
  if (assetId === "U01-CH022" && slideNumber === 70) {
    const frame = rect(image.resolveFrame());
    image.delete();
    drawDbMapping(slide, frame, assetId);
    return { mode: "native-compact-mapping", frame };
  }
  const fileName = RASTER_ASSETS.get(assetId);
  const assetPath = path.join(assetDir, fileName);
  const oldAlt = image.alt ?? `${assetId}, recurso corregido.`;
  const oldFrame = image.resolveFrame();
  const oldCrop = image.crop;
  const oldFit = image.fit;
  const oldGeometry = image.geometry;
  const oldBorderRadius = image.borderRadius;
  const oldFlipHorizontal = image.flipHorizontal;
  const oldFlipVertical = image.flipVertical;
  const oldLockAspectRatio = image.lockAspectRatio;
  await image.replace({
    blob: await readBytes(assetPath),
    contentType: fileName.endsWith(".gif") ? "image/gif" : "image/png",
    alt: oldAlt,
    fit: "contain",
  });
  image.frame = oldFrame;
  image.crop = oldCrop;
  image.geometry = oldGeometry;
  image.borderRadius = oldBorderRadius;
  image.flipHorizontal = oldFlipHorizontal;
  image.flipVertical = oldFlipVertical;
  image.lockAspectRatio = oldLockAspectRatio;
  if (oldFit && oldFit !== "cover") image.fit = oldFit;
  return { mode: "raster-replaced", frame: rect(oldFrame), assetPath };
}

function drawNative(slide, assetId, frame, slideNumber) {
  switch (assetId) {
    case "U01-CH001":
      return drawFmr(slide, frame, assetId);
    case "U01-CH003":
      return drawMeasurement(slide, frame, assetId);
    case "U01-CH004":
      return drawSi(slide, frame, assetId);
    case "U01-CH005":
      return drawUnitConstruction(slide, frame, assetId);
    case "U01-CH006":
      return drawQuantityTable(slide, frame, assetId);
    case "U01-CH007":
      return drawKinematics(slide, frame, assetId);
    case "U01-CH008":
      return drawPropagationTime(slide, frame, assetId);
    case "U01-CH009":
      return drawMassWeight(slide, frame, assetId);
    case "U01-CH010":
      return drawFpd(slide, frame, assetId, slideNumber);
    case "U01-CH011":
      return drawNetwork(slide, frame, assetId);
    case "U01-CH012":
      return drawNotation(slide, frame, assetId);
    case "U01-CH013":
      return drawPrefixes(slide, frame, assetId);
    case "U01-CH014":
      return drawDimensions(slide, frame, assetId);
    case "U01-CH016":
      return drawInverse(slide, frame, assetId);
    case "U01-CH017":
      return drawInverseReciprocal(slide, frame, assetId);
    case "U01-CH018":
      return drawTriangle(slide, frame, assetId);
    case "U01-CH023":
      return drawMatrix(slide, frame, assetId);
    case "U01-CH024":
      return drawCase(slide, frame, assetId);
    case "U01-CH025":
      return drawCourseDependencies(slide, frame, assetId);
    default:
      throw new Error(`No native renderer for ${assetId}`);
  }
}

async function main() {
  const [sourcePptx, outputPptx, previewDir, assetDir] = process.argv.slice(2);
  if (!sourcePptx || !outputPptx || !previewDir || !assetDir) {
    throw new Error(
      "Usage: node u01_repair_diagrams_native.mjs <source.pptx> <output.pptx> <preview-dir> <quantitative-asset-dir>",
    );
  }
  const presentation = await PresentationFile.importPptx(await FileBlob.load(sourcePptx));
  const report = [];
  await fs.mkdir(previewDir, { recursive: true });

  for (const [slideNumber, assetId] of TARGETS.entries()) {
    const slide = presentation.slides.getItem(slideNumber - 1);
    const images = [...slide.images.items];
    if (images.length !== 1) {
      throw new Error(`Expected one image on slide ${slideNumber}; found ${images.length}`);
    }
    const image = images[0];
    const beforeFrame = rect(image.resolveFrame());
    if (RASTER_ASSETS.has(assetId)) {
      const result = await replaceRaster(slide, assetId, image, assetDir, slideNumber);
      report.push({ slide: slideNumber, assetId, ...result });
    } else {
      const { frame } = deleteTargetImage(slide);
      drawNative(slide, assetId, frame, slideNumber);
      report.push({ slide: slideNumber, assetId, mode: `native-${modeFor(frame)}`, frame, originalFrame: beforeFrame });
    }
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    await fs.writeFile(
      path.join(previewDir, `slide-${String(slideNumber).padStart(3, "0")}.png`),
      new Uint8Array(await png.arrayBuffer()),
    );
  }

  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(outputPptx);
  await fs.writeFile(path.join(previewDir, "repair-report.json"), `${JSON.stringify(report, null, 2)}\n`, "utf8");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
