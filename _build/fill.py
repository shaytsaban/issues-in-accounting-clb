# Part of the 432348 build kit (2026-11-24). # How much of each slide's height is used, with every reveal shown. Usage: python3 fill.py deck.html
import json, os, re, subprocess, sys, tempfile, html as hh
SRC = sys.argv[1]
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
JS = r'''
(function(){const D=window.__deck,stage=document.getElementById('stage'),out=[];
const st=document.createElement('style');st.textContent='*{transition:none!important;animation:none!important}';document.head.appendChild(st);
D.slides.forEach((s,i)=>{D.show(i);D.setAll(s,true);s.querySelectorAll('.mc').forEach(m=>{m.classList.add('done');m.querySelectorAll('.o')[+m.dataset.a].classList.add('ok');});
 const S=stage.getBoundingClientRect(),k=S.width/1280;let top=1e9,bot=0,left=1e9,right=0;
 s.querySelectorAll('*').forEach(e=>{if(e.closest('.ft,.kick'))return;if(e.children.length&&!e.matches('svg,button,td,th'))return;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none'||+cs.opacity===0)return;
  const r=e.getBoundingClientRect();if(!r.width||!r.height)return;const t=(r.top-S.top)/k,b=(r.bottom-S.top)/k,l=(r.left-S.left)/k,rr=(r.right-S.left)/k;if(t<0||t>720)return;
  if(e.closest('h2'))return;top=Math.min(top,t);bot=Math.max(bot,b);left=Math.min(left,l);right=Math.max(right,rr);});
 const h2=s.querySelector('h2');const ht=h2?(h2.getBoundingClientRect().bottom-S.top)/k:90;
 out.push({i:i+1,id:s.id,kind:s.className.includes('opener')?'opener':'',head:Math.round(ht),bottom:Math.round(bot),fill:Math.round(100*(bot-ht)/(684-ht)),w:Math.round(right-left)});
 s.querySelectorAll('.mc').forEach(m=>{m.classList.remove('done');m.querySelectorAll('.o').forEach(o=>o.classList.remove('ok'));});D.setAll(s,false);});
document.documentElement.setAttribute('data-fill',JSON.stringify(out));})();'''
src = open(SRC, encoding='utf8').read()
d = tempfile.mkdtemp()
p = os.path.join(d, 't.html')
open(p, 'w', encoding='utf8').write(src.replace('</body>', '<script>setTimeout(function(){' + JS + '},1500)</script></body>'))
r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={d}/prof', '--window-size=1280,764', '--virtual-time-budget=60000', '--dump-dom', 'file://' + p], capture_output=True, text=True, timeout=1200)
m = re.search(r'data-fill="([^"]*)"', r.stdout)
rows = json.loads(hh.unescape(m.group(1)))
for x in rows:
    flag = '  <-- low' if x['fill'] < 70 and x['kind'] != 'opener' else ''
    print(f"{x['i']:3} {x['id']:16} head {x['head']:3} bottom {x['bottom']:3} fill {x['fill']:3}% width {x['w']:4}{flag}")
