/* ---------- audio policy: nothing reads by itself — words & sentences play only when a read button (▶ / 🔊) is clicked */
(function(){
  if(typeof playQueue!=='function') return;
  let okUntil=0;
  const READ='.play,.spk,.ear,[data-letter],.lb';
  const isRead=t=>{ if(!t||!t.closest) return false; if(t.closest(READ)) return true; const b=t.closest('button'); return !!(b&&/[▶🔊🔁🎧]/.test(b.textContent||'')); };
  const allow=()=>{ okUntil=Date.now()+700; };
  document.addEventListener('click',e=>{
    const s=e.target.closest&&e.target.closest('.spk');
    if(s){ e.stopPropagation(); e.preventDefault(); allow(); if(typeof stopAll==='function') stopAll(); play(s.dataset.a,s); return; }
    if(isRead(e.target)) allow();
  },true);
  document.addEventListener('keydown',e=>{ if((e.key==='Enter'||e.key===' ')&&isRead(document.activeElement)) allow(); },true);
  const orig=playQueue;
  playQueue=function(){ if(Date.now()>okUntil) return Promise.resolve(); return orig.apply(this,arguments); };
  /* clickable words/cards that used to speak on click get their own 🔊 button */
  const SKIP='.play,.spk,.ear,.btn,[data-letter],.lb,.dl,a';
  function arm(root){
    (root.querySelectorAll?root:document).querySelectorAll('[data-a]').forEach(el=>{
      if(el.matches(SKIP)||el.querySelector(':scope > .spk')||el.closest('.spk')) return;
      if(typeof AUDIO!=='undefined'&&!AUDIO[el.dataset.a]) return;
      el.insertAdjacentHTML('beforeend',`<span class="spk" role="button" tabindex="0" data-a="${el.dataset.a}" title="Nghe">🔊</span>`);
    });
    (root.querySelectorAll?root:document).querySelectorAll('.ln[data-ln]').forEach(el=>{
      const id='DLG_'+el.dataset.ln; if(el.querySelector('.spk,.play')||(typeof AUDIO!=='undefined'&&!AUDIO[id])) return;
      el.insertAdjacentHTML('beforeend',`<span class="spk" role="button" tabindex="0" data-a="${id}" title="Nghe">🔊</span>`);
    });
  }
  arm(document);
  new MutationObserver(ms=>ms.forEach(m=>m.addedNodes.forEach(n=>{ if(n.nodeType===1) arm(n.parentNode||n); }))).observe(document.body,{childList:true,subtree:true});
})();
