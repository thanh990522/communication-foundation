/* ---------- structure slides: step-by-step reveal (like PowerPoint animations) */
(function(){
  const S=()=>document.querySelector('.slide.active .sgrid');
  function state(g){ const steps=[...g.querySelectorAll('.stp[data-step]:not([data-step="0"])')]; return {steps, shown:steps.filter(s=>s.classList.contains('on')).length}; }
  function draw(g){ const {steps,shown}=state(g); const sl=g.closest('.slide');
    sl.querySelectorAll('.stp[data-step="0"]').forEach(h=>h.classList.toggle('on',shown>=2));
    const d=sl.querySelector('.sdots'); if(d) d.innerHTML=steps.map((_,k)=>`<i class="${k<shown?'on':''}"></i>`).join('');
    const nb=sl.querySelector('[data-snext]'); if(nb) nb.textContent=shown>=steps.length?'Next slide →':'Next step →'; }
  function next(g){ const {steps,shown}=state(g); if(shown>=steps.length) return false;
    const el=steps[shown]; el.classList.add('on'); if(el.dataset.say&&typeof play==='function') play(el.dataset.say); draw(g); return true; }
  function prev(g){ const {steps,shown}=state(g); if(shown<=1) return false; steps[shown-1].classList.remove('on'); if(typeof stopAll==='function') stopAll(); draw(g); return true; }
  window.addEventListener('keydown',e=>{
    if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)) return; const g=S(); if(!g) return; const k=e.key;
    if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='ArrowDown'){ if(next(g)){ e.preventDefault(); e.stopPropagation(); } }
    else if(k==='ArrowLeft'||k==='PageUp'||k==='ArrowUp'){ if(prev(g)){ e.preventDefault(); e.stopPropagation(); } }
  },true);
  window.addEventListener('DOMContentLoaded',()=>{
    document.querySelectorAll('.sgrid').forEach(g=>{ const f=g.querySelector('.stp[data-step="1"]'); if(f) f.classList.add('on'); draw(g);
      const sl=g.closest('.slide');
      sl.querySelector('[data-snext]').onclick=()=>{ if(!next(g)&&typeof go==='function') go(cur+1); };
      sl.querySelector('[data-sprev]').onclick=()=>prev(g); });
  });
})();
