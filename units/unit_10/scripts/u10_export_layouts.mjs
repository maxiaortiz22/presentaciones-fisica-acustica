import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [pptxArg, outDirArg, workspaceArg] = process.argv.slice(2);
if (!pptxArg || !outDirArg || !workspaceArg) throw new Error('Uso: u10_export_layouts.mjs <pptx> <outDir> <workspace>');
const req = createRequire(path.join(path.resolve(workspaceArg), 'package.json'));
const entry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(entry).href);
const deck = await PresentationFile.importPptx(await FileBlob.load(path.resolve(pptxArg)));
await fs.mkdir(path.resolve(outDirArg), { recursive: true });
for (let i = 0; i < deck.slides.items.length; i += 1) {
  const blob = await deck.slides.items[i].export({ format: 'layout' });
  const bytes = new Uint8Array(await blob.arrayBuffer());
  await fs.writeFile(path.join(path.resolve(outDirArg), `final-slide-${String(i + 1).padStart(2, '0')}.layout.json`), bytes);
}
console.log(JSON.stringify({ slides: deck.slides.items.length, outDir: path.resolve(outDirArg) }));
