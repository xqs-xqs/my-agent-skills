// 用 Chromium 渲染 out/widgets.jsonl 里的组件，检查总结句、导图节点与 JS 报错。用法: node render_widgets.js [run_id 前缀]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const OUT = path.join(__dirname, 'out'); const PREFIX = process.argv[2] || '';
const tpl = fs.readFileSync(path.join(__dirname, '..', 'SKILL.md'),'utf8');
const engine = tpl.slice(tpl.indexOf('/* ↓↓↓ 引擎部分'), tpl.indexOf('</script>'));
const css = ':root{--font-sans:sans-serif;--color-text-primary:#1f1f1f;--color-background-primary:#fff}';
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:900,height:800}});
  const ws = fs.readFileSync(path.join(OUT, 'widgets.jsonl'),'utf8').trim().split('\n').map(JSON.parse).filter(w=>w.run.startsWith(PREFIX));
  for (const w of ws) {
    const errs=[]; p.removeAllListeners('pageerror'); p.on('pageerror', e=>errs.push(e.message));
    await p.setContent(`<html><head><style>${css}</style></head><body>${w.widget_code}</body></html>`);
    const r = await p.evaluate(()=>({sum:document.getElementById('mmsum')?.textContent||'', h3:[...document.querySelectorAll('#mmwrap h3')].map(e=>e.textContent), rects:document.querySelectorAll('#mm rect').length, paths:document.querySelectorAll('#mm path').length}));
    const codeLines = new Set(w.widget_code.split('\n').map(l=>l.trim()));
    const engineIntact = engine.split('\n').map(l=>l.trim()).filter(l=>l && !l.startsWith('/*')).every(l=>codeLines.has(l));
    console.log(w.run.padEnd(16), errs.length?'JSERR '+errs[0]:'ok', 'engineIntact='+engineIntact, 'rects='+r.rects, 'h3='+r.h3.join('/'), 'sum='+r.sum.slice(0,50));
    await p.screenshot({path: path.join(OUT, w.run + '.png'), fullPage: true});
  }
  await b.close();
})();
