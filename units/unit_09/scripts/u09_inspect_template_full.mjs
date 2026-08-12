import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [pptxPath, outPath, workspace] = process.argv.slice(2);
if (!pptxPath || !outPath || !workspace) throw new Error('Uso: node u09_inspect_template_full.mjs <template.pptx> <out.ndjson> <workspace>');
const req = createRequire(path.join(path.resolve(workspace), 'package.json'));
const entry = req.resolve('@oai/artifact-tool');
const { FileBlob, PresentationFile } = await import(pathToFileURL(entry).href);
const deck = await PresentationFile.importPptx(await FileBlob.load(path.resolve(pptxPath)));
const snapshot = await deck.inspect({
  kind: 'slide,textbox,shape,image,table,chart,notes,layout',
  include: 'id,slide,name,title,text,textPreview,textChars,textLines,bbox,bboxUnit,isPlaceholder,placeholder',
  maxChars: 2_000_000,
});
await fs.writeFile(path.resolve(outPath), snapshot.ndjson, 'utf8');
console.log(JSON.stringify({ slides: deck.slides.items.length, chars: snapshot.ndjson.length }, null, 2));
