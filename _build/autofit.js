/* Meeting 4 on (2026-11-24): autofit. Loaded only when LMETA autofit is on, so taught decks rebuild byte-identical. Two fixes from the YVC kit (its commit 18f6a83): no zoom that clips a number in a table, and a refit once every font face has loaded. */
/* ---------- autofit (Shay, 2026-11-24: "large parts of the slides stay empty"): the body of a content slide is scaled up, at most
   1.4 times, until it reaches the footer. It is measured with every reveal shown and every answer explanation open, so nothing
   overflows later. Slides are laid out even while hidden, so all of them are fitted at load, and again once the fonts are in. ---------- */
(function(){
 function fitOne(s){const w=s.querySelector(':scope > .afit');if(!w)return;
  const cs=getComputedStyle(s),cw=s.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);
  const limit=(s.querySelector('.ft')?720-36:716)-8,top=()=>s.getBoundingClientRect().top;
  const k0=(s.getBoundingClientRect().height/720)||1;
  const bottom=()=>(w.getBoundingClientRect().bottom-top())/k0;
  const set=z=>{w.style.zoom=z;w.style.width=(cw/z)+'px';};
  /* YVC lesson 7: a zoom that makes any table cell clip its number (110,000 shown as 10,000) is too much: the width shrinks as the zoom grows */
  const cells=[...w.querySelectorAll('td,th')],clipped=()=>cells.some(c=>c.offsetParent&&c.scrollWidth>c.clientWidth);
  const ok=()=>bottom()<=limit&&!clipped();
  const hid=[...s.querySelectorAll('.st:not(.show)')];hid.forEach(e=>e.classList.add('show'));s.classList.add('afm');set(1);
  /* the 3% step back is taken only when a clipped number set the limit: an overflow under a pixel still cuts a number */
  if(ok()){let lo=1,hi=1.4,byClip=false;for(let i=0;i<10;i++){const m=(lo+hi)/2;set(m);if(ok())lo=m;else{hi=m;byClip=bottom()<=limit;}}set(byClip?Math.max(1,lo*.97):lo);}
  s.classList.remove('afm');hid.forEach(e=>e.classList.remove('show'));}
 const all=()=>document.querySelectorAll('.slide').forEach(fitOne);
 all();addEventListener('load',()=>{all();setTimeout(all,600);});if(document.fonts&&document.fonts.ready)document.fonts.ready.then(all);
 /* YVC lesson 7: the embedded faces load only when first used, so a bold number measured before its face arrived came out 1px too narrow.
    Every face is loaded up front, and the slides are fitted again whenever a face finishes loading. */
 if(document.fonts){Promise.all([...document.fonts].map(f=>f.load().catch(()=>{}))).then(all);document.fonts.addEventListener('loadingdone',all);}
 window.__autofit=all;
})();
