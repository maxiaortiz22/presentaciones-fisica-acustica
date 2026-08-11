import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [templatePath, outDir] = process.argv.slice(2);
const workspace = process.env.U06_ARTIFACT_WORKSPACE;
if (!templatePath || !outDir || !workspace) {
  throw new Error('Uso: U06_ARTIFACT_WORKSPACE=<workspace> node u06_inspect_template.mjs <template.pptx> <outDir>');
}
const req = createRequire(path.join(workspace, 'package.json'));
const entry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(entry).href);

await fs.mkdir(outDir, { recursive: true });
const deck = await PresentationFile.importPptx(await FileBlob.load(templatePath));
const inspect = await deck.inspect({
  kind: 'deck,slide,textbox,shape,image,table,chart,notes,layout',
  include: 'id,slide,name,title,text,textPreview,textChars,bbox,bboxUnit,isPlaceholder,placeholders,alt,chartType,rows,cols',
  maxChars: 2_000_000,
});
await fs.writeFile(path.join(outDir, 'template-inspect.ndjson'), inspect.ndjson, 'utf8');
const manifest = {
  slides: deck.slides.items.length,
  layouts: deck.layouts?.items?.map((x) => ({ id: x.id, name: x.name })) ?? [],
  masters: deck.masters?.items?.map((x) => ({ id: x.id, name: x.name })) ?? [],
};
await fs.writeFile(path.join(outDir, 'template-manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
for (let i = 0; i < deck.slides.items.length; i += 1) {
  const slide = deck.slides.items[i];
  const stem = `slide-${String(i + 1).padStart(2, '0')}`;
  const png = await deck.export({ slide, format: 'png', scale: 1 });
  await fs.writeFile(path.join(outDir, `${stem}.png`), new Uint8Array(await png.arrayBuffer()));
  const layout = await slide.export({ format: 'layout' });
  await fs.writeFile(path.join(outDir, `${stem}.layout.json`), await layout.text(), 'utf8');
}
const montage = await deck.export({ format: 'png', montage: true, scale: 0.5 });
await fs.writeFile(path.join(outDir, 'template-contact-sheet.png'), new Uint8Array(await montage.arrayBuffer()));
console.log(JSON.stringify(manifest, null, 2));
