// Compile every LaTeX expression in a GitHub-flavoured Markdown file with MathJax (base, ams, boldsymbol only:
// what GitHub's renderer supports), fail loudly on any TeX error, and write a typeset HTML page and PDF.
// Usage: node render.js <in.md> <out.html> <out.pdf>
const fs = require('fs');
const path = require('path');
const { mathjax } = require('mathjax-full/js/mathjax.js');
const { TeX } = require('mathjax-full/js/input/tex.js');
const { SVG } = require('mathjax-full/js/output/svg.js');
const { liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor.js');
const { RegisterHTMLHandler } = require('mathjax-full/js/handlers/html.js');
require('mathjax-full/js/input/tex/base/BaseConfiguration.js');
require('mathjax-full/js/input/tex/ams/AmsConfiguration.js');
require('mathjax-full/js/input/tex/boldsymbol/BoldsymbolConfiguration.js');
const { marked } = require('marked');

const [, , inMd, outHtml, outPdf] = process.argv;
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const errors = [];
const tex = new TeX({ packages: ['base', 'ams', 'boldsymbol'],
                      formatError: (jax, err) => { throw err; } });
const svg = new SVG({ fontCache: 'local' });
const doc = mathjax.document('', { InputJax: tex, OutputJax: svg });

function typeset(src, display, where) {
  try {
    const node = doc.convert(src, { display });
    const html = adaptor.outerHTML(node);
    if (/data-mjx-error|merror/.test(html)) throw new Error('merror in output');
    return html;
  } catch (e) {
    errors.push(`${where}: ${e.message} :: ${src.slice(0, 120).replace(/\n/g, ' ')}`);
    return `<code style="color:red">${src}</code>`;
  }
}

let md = fs.readFileSync(inMd, 'utf8');
const store = [];
const ph = (html) => { store.push(html); return `MJXPH${store.length - 1}X`; };
let nDisplay = 0, nInline = 0;
// display maths: ```math fences
md = md.replace(/```math\n([\s\S]*?)```/g, (m, body) => {
  nDisplay++;
  return '\n<div class="eq">' + ph(typeset(body.trim(), true, `display #${nDisplay}`)) + '</div>\n';
});
// inline maths, outside code spans and fenced code: split on code first
const parts = md.split(/(```[\s\S]*?```|`[^`\n]*`)/);
for (let i = 0; i < parts.length; i += 2) {
  parts[i] = parts[i].replace(/(?<![\\$\w])\$(?=\S)([^$\n]+?)(?<=\S)\$(?![\w$])/g, (m, body) => {
    nInline++;
    return ph(typeset(body, false, `inline #${nInline}`));
  });
}
md = parts.join('');
let html = marked.parse(md, { gfm: true });
html = html.replace(/MJXPH(\d+)X/g, (m, i) => store[+i]);

const title = (fs.readFileSync(inMd, 'utf8').match(/^# (.*)$/m) || [, 'Document'])[1];
const page = `<!doctype html><html><head><meta charset="utf-8"><title>${title}</title><style>
  body { font: 10.5pt/1.5 "DejaVu Serif", Georgia, serif; color: #111; max-width: 46em; margin: 2em auto; padding: 0 1em; }
  h1 { font-size: 20pt; } h2 { font-size: 15pt; margin-top: 1.6em; border-bottom: 1px solid #ccc; } h3 { font-size: 12pt; }
  code { font: 9pt "DejaVu Sans Mono", monospace; background: #f3f3f3; padding: 0 .2em; }
  table { border-collapse: collapse; margin: .8em 0; font-size: 9.5pt; } td, th { border: 1px solid #bbb; padding: .25em .5em; vertical-align: top; }
  .eq { margin: .9em 0; overflow-x: visible; text-align: center; } .eq mjx-container { max-width: 100%; }
  mjx-container[display="true"] svg { max-width: 100%; height: auto; }
  hr { border: 0; border-top: 1px solid #ddd; }
  @page { size: A4; margin: 16mm 14mm; }
</style></head><body>${html}</body></html>`;
fs.writeFileSync(outHtml, page);
console.log(`display maths: ${nDisplay}, inline maths: ${nInline}, TeX errors: ${errors.length}`);
errors.forEach((e) => console.log('  ERROR ' + e));

(async () => {
  const { chromium } = require('playwright-core');
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  const pg = await browser.newPage();
  await pg.goto('file://' + path.resolve(outHtml));
  await pg.pdf({ path: outPdf, format: 'A4', printBackground: true,
                 margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  await browser.close();
  console.log('pdf written: ' + outPdf);
  process.exit(errors.length ? 1 : 0);
})();
