import fs from "node:fs/promises";
import path from "node:path";

import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const PT_TO_PX = 96 / 72;
const fontPx = (points) => points * PT_TO_PX;

async function readBytes(filePath) {
  return new Uint8Array(await fs.readFile(filePath));
}

function findShape(slide, name) {
  const shape = [...slide.shapes.items].find((item) => item.name === name);
  if (!shape) throw new Error(`No se encontró la forma ${name}`);
  return shape;
}

function setText(shape, text, { fontPt, color = "#3D3D3D", bold = false, align = "left", valign = "top", insets = 0 }) {
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
}

async function replaceOnlyImage(slide, assetPath) {
  const images = [...slide.images.items];
  if (images.length !== 1) {
    throw new Error(`Se esperaba una imagen en la diapositiva; se encontraron ${images.length}`);
  }
  const image = images[0];
  const oldFrame = image.resolveFrame();
  const oldCrop = image.crop;
  const oldFit = image.fit;
  const oldAlt = image.alt;
  const oldGeometry = image.geometry;
  const oldBorderRadius = image.borderRadius;
  const oldRotation = image.rotation;
  const oldFlipHorizontal = image.flipHorizontal;
  const oldFlipVertical = image.flipVertical;
  const oldLockAspectRatio = image.lockAspectRatio;

  await image.replace({
    blob: await readBytes(assetPath),
    contentType: assetPath.toLowerCase().endsWith(".png") ? "image/png" : "image/svg+xml",
    alt: oldAlt ?? "Recurso vectorial corregido.",
    fit: oldFit ?? "contain",
  });
  image.frame = oldFrame;
  image.crop = oldCrop;
  image.geometry = oldGeometry;
  image.borderRadius = oldBorderRadius;
  image.rotation = oldRotation;
  image.flipHorizontal = oldFlipHorizontal;
  image.flipVertical = oldFlipVertical;
  image.lockAspectRatio = oldLockAspectRatio;
}

function bringCaptionsAndSourcesForward(presentation) {
  for (const slide of presentation.slides.items) {
    for (const shape of slide.shapes.items) {
      const name = shape.name ?? "";
      if (name.endsWith("_caption") || name.endsWith("_source") || name.endsWith("_bibliography_source")) {
        shape.bringToFront();
      }
    }
  }
}

async function main() {
  const [sourcePptx, outputPptx, previewDir, unitDir] = process.argv.slice(2);
  if (!sourcePptx || !outputPptx || !previewDir || !unitDir) {
    throw new Error(
      "Uso: node u02_review_repair_v02.mjs <v01.pptx> <v02.pptx> <preview-dir> <unit-dir>",
    );
  }

  const presentation = await PresentationFile.importPptx(await FileBlob.load(sourcePptx));
  await fs.mkdir(previewDir, { recursive: true });

  const chartRoot = path.join(unitDir, "assets", "generated", "charts");
  const diagramRoot = path.join(unitDir, "assets", "generated", "diagrams");
  const imageReplacements = new Map([
    [18, path.join(chartRoot, "u02_ch001_aceleracion_fuerza", "u02_fig_001_aceleracion_fuerza.png")],
    [36, path.join(chartRoot, "u02_ch001_aceleracion_fuerza", "u02_fig_001_aceleracion_fuerza.png")],
    [38, path.join(chartRoot, "u02_ch002_fuerza_elastica", "u02_fig_002_fuerza_elastica.png")],
    [40, path.join(chartRoot, "u02_ch003_fuerza_amortiguamiento", "u02_fig_003_fuerza_amortiguamiento.png")],
    [80, path.join(chartRoot, "u02_ch004_velocidad_temperatura", "u02_fig_004_velocidad_temperatura.png")],
    [81, path.join(chartRoot, "u02_ch004_velocidad_temperatura", "u02_fig_004_velocidad_temperatura.png")],
    [103, path.join(chartRoot, "u02_ch004_velocidad_temperatura", "u02_fig_004_velocidad_temperatura.png")],
    [19, path.join(diagramRoot, "u02_dg003_s019", "u02_fig_019_003.png")],
    [44, path.join(diagramRoot, "u02_dg006_s044", "u02_fig_044_006.png")],
    [96, path.join(diagramRoot, "u02_dg014_s096", "u02_fig_096_014.png")],
  ]);

  for (const [slideNumber, assetPath] of imageReplacements.entries()) {
    await replaceOnlyImage(presentation.slides.getItem(slideNumber - 1), assetPath);
  }

  const slide30 = presentation.slides.getItem(29);
  setText(findShape(slide30, "U02-030_equation"), "F_pres = 1,0×10⁻⁴ N", {
    fontPt: 24,
    color: "#4D1434",
    align: "center",
    valign: "middle",
  });

  const slide103 = presentation.slides.getItem(102);
  setText(
    findShape(slide103, "U02-103_equation"),
    "c = 331 m/s +\n[0,6 (m/s)/°C]·ϑ;  t = d/c",
    {
      fontPt: 17,
      color: "#4D1434",
      align: "center",
      valign: "middle",
    },
  );

  const slide100 = presentation.slides.getItem(99);
  setText(
    findShape(slide100, "U02-100_bibliography"),
    [
      "Ugarteburu, M. et al. (2022). Mammalian Middle Ear Mechanics: A Review. Frontiers in Bioengineering and Biotechnology, 10, 983510. doi:10.3389/fbioe.2022.983510",
      "",
      "Stenfelt, S. y Goode, R. L. (2005). Bone-Conducted Sound: Physiological and Clinical Aspects. Otology & Neurotology, 26(6), 1245–1261. doi:10.1097/01.mao.0000187236.10842.d5",
      "",
      "Fung, Y. C. (1981). Biomechanics: Mechanical Properties of Living Tissues. Springer. doi:10.1007/978-1-4757-1752-5",
    ].join("\n"),
    { fontPt: 18, insets: { top: 8, right: 8, bottom: 8, left: 8 } },
  );
  setText(
    findShape(slide100, "U02-100_bibliography_source"),
    "Referencias verificadas contra la bibliografía del capítulo 2.",
    { fontPt: 13, color: "#667079", valign: "middle" },
  );

  const slide109 = presentation.slides.getItem(108);
  setText(
    findShape(slide109, "U02-109_bibliography"),
    [
      "Cramer, O. (1993). The Variation of the Specific Heat Ratio and the Speed of Sound in Air with Temperature, Pressure, Humidity, and CO₂ Concentration. The Journal of the Acoustical Society of America, 93(5), 2510–2516. doi:10.1121/1.405827",
      "",
      "Xiang, N. y Blauert, J. (2021). Acoustics for Engineers: Troy Lectures (3.ª ed.). Springer. doi:10.1007/978-3-662-63342-7",
      "",
      "Fuentes primarias del curso: programa oficial y capítulo 2 del libro.",
    ].join("\n"),
    { fontPt: 18, insets: { top: 8, right: 8, bottom: 8, left: 8 } },
  );
  setText(
    findShape(slide109, "U02-109_bibliography_source"),
    "Referencias verificadas contra la bibliografía del capítulo 2.",
    { fontPt: 13, color: "#667079", valign: "middle" },
  );

  bringCaptionsAndSourcesForward(presentation);
  for (const slideNumber of [19, 44, 96]) {
    setText(
      findShape(
        presentation.slides.getItem(slideNumber - 1),
        `U02-${String(slideNumber).padStart(3, "0")}_source`,
      ),
      "Elaboración propia; recurso vectorial validado.",
      { fontPt: 9.4, color: "#969FA7", valign: "middle" },
    );
  }
  for (const slideNumber of [36, 80]) {
    setText(
      findShape(
        presentation.slides.getItem(slideNumber - 1),
        `U02-${String(slideNumber).padStart(3, "0")}_source`,
      ),
      "Elaboración propia a partir del modelo del curso; escala lineal.",
      { fontPt: 9.4, color: "#969FA7", valign: "middle" },
    );
  }

  const changedSlides = [...new Set([...imageReplacements.keys(), 30, 100, 109])].sort((a, b) => a - b);
  for (const slideNumber of changedSlides) {
    const slide = presentation.slides.getItem(slideNumber - 1);
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    await fs.writeFile(
      path.join(previewDir, `slide-${String(slideNumber).padStart(3, "0")}.png`),
      new Uint8Array(await png.arrayBuffer()),
    );
  }

  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(outputPptx);
  await fs.writeFile(
    path.join(previewDir, "repair-report.json"),
    `${JSON.stringify({ sourcePptx, outputPptx, changedSlides }, null, 2)}\n`,
    "utf8",
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
