/* =========================================================
   S10 · Past Events: What Happened? — lesson activities
   (DATA is injected by build.py from content.py)
   ========================================================= */
const DATA = /*DATA_JSON*/;
const pbtn = (id,cls) => `<button class="play sm${cls?' '+cls:''}" data-a="${id}">${PLAY_SVG}</button>`;
const norm = s => String(s).toLowerCase().replace(/[\s\-–.,!?'’]+/g,'').trim();
function hl(i){ document.querySelectorAll('#script .ln').forEach((l,k)=>l.classList.toggle('now',k===i)); }


/* ---------- cover cloud */
function buildCloud(id,words){
  const el=document.getElementById(id); if(!el) return;
  words=words||[['🕒','3:30'],['📅','Friday'],['🗓','schedule'],['✅','confirm'],['🔁','reschedule'],['⏰','deadline'],['📞','call'],['🟢','free']];
  const pos=[[20,10,-6],[230,0,5],[110,120,8],[300,140,-6],[10,250,4],[200,270,-8],[60,380,-4],[260,390,6]];
  el.innerHTML=words.map((w,i)=>`<div class="wtag" style="left:${pos[i][0]}px;top:${pos[i][1]}px;transform:rotate(${pos[i][2]}deg);background:${i%3===0?'var(--yellow)':i%3===1?'var(--blue)':'var(--navy)'};color:${i%3===0?'var(--navy)':i%3===1?'#fff':'var(--yellow)'}"><span>${w[0]}</span>${w[1]}</div>`).join('');
}

/* ---------- flip cards */
document.addEventListener('click',e=>{
  if(e.target.closest('button,a,input')) return;
  const f=e.target.closest('[data-flip]'); if(f) f.classList.toggle('on');
});
function flipAll(btn,on){ btn.closest('.slide').querySelectorAll('[data-flip]').forEach(f=>f.classList.toggle('on',on)); }
/* ---------- multiple-choice rows (collocation check · map) */
function setupMC(pre,items,scoreId,aid){
  let n=0; const score=()=>document.getElementById(scoreId).textContent=`✓ ${n} / ${items.length}`;
  document.querySelectorAll(`[data-${pre}]`).forEach(b=>b.onclick=()=>{
    const i=+b.dataset[pre], box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1;
    const ans=items[i][2];
    box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); });
    if(b.dataset.o!==ans) b.classList.add('no'); else n++;
    const g=document.querySelector(`#${pre}q${i} .gap`); if(g) g.textContent=ans; score(); play(`${aid}_${i}`);
  });
  return ()=>{ n=0; score(); document.querySelectorAll(`[id^="${pre}q"] .co`).forEach(c=>{ delete c.dataset.done; c.querySelectorAll('.opt').forEach(o=>o.classList.remove('ok','no')); }); document.querySelectorAll(`[id^="${pre}q"] .gap`).forEach(g=>g.textContent='___'); };
}
/* ---------- listen & repeat (gap for students to repeat) */
function repeatQueue(btn){
  const ids=btn.dataset.rep.split(','), slide=btn.closest('.slide');
  const mark=k=>{ slide.querySelectorAll('.now').forEach(x=>x.classList.remove('now')); if(k>=0){ const el=slide.querySelector(`[data-a="${ids[k]}"]`); el&&el.classList.add('now'); } };
  playQueue(ids,mark,1900,btn).then(()=>mark(-1));
}
/* ---------- listening (real recording) */
function buildListen(){
  const L=DATA.LISTEN;
  document.getElementById('lgist').innerHTML=`<div class="lq"><span class="n">1</span><span class="qt">${esc(L.gist[0])}</span><div class="co">${L.gist[1].map(o=>`<button class="opt" data-lg="${esc(o)}">${esc(o)}</button>`).join('')}</div></div>`;
  document.getElementById('ldetail').innerHTML=L.detail.map(([s,opts,ans],i)=>`<div class="lq" id="ld${i}"><span class="n">${i+2}</span><span class="qt">${esc(s).replace('___','<span class="gap">___</span>')}</span><div class="co">${opts.map(o=>`<button class="opt" data-ld="${i}" data-o="${esc(o)}">${esc(o)}</button>`).join('')}</div></div>`).join('')
    + L.times.map(([s,ans],i)=>`<div class="lq"><span class="n">${i+2+L.detail.length}</span><span class="qt">${esc(s).replace('___',`<input class="tin" id="lt${i}" autocomplete="off" spellcheck="false">`)}</span><span class="tans" id="lta${i}"></span></div>`).join('');
  document.querySelectorAll('[data-lg]').forEach(b=>b.onclick=()=>{ const box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1; box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.lg===L.gist[2]) x.classList.add('ok'); }); if(b.dataset.lg!==L.gist[2]) b.classList.add('no'); });
  document.querySelectorAll('[data-ld]').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.ld, box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1;
    const ans=L.detail[i][2]; box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); });
    if(b.dataset.o!==ans) b.classList.add('no'); { const g=document.querySelector('#ld'+i+' .gap'); if(g) g.textContent=ans; }
  });
}
function listenCheck(){ DATA.LISTEN.times.forEach(([s,ans],i)=>{ const el=document.getElementById('lt'+i), ok=ans.map(norm).includes(norm(el.value)); el.classList.toggle('ok',ok); el.classList.toggle('no',!ok&&el.value!==''); document.getElementById('lta'+i).textContent=ans[0]; }); }
/* ---------- model dialogue */
function buildDialogue(){
  const sc=document.getElementById('script');
  sc.innerHTML=DATA.DIALOGUE.map(([w,t],i)=>`<div class="ln" data-ln="${i}"><span class="who ${w===Object.keys(DATA.DLG_NAMES)[0]?'R':'S'}">${w}</span><span class="tx">${esc(t)}</span>${dl('DLG_'+i)}</div>`).join('');
  sc.querySelectorAll('.ln').forEach(l=>l.addEventListener('click',ev=>{ if(ev.target.closest('a')) return; const i=+l.dataset.ln; playQueue(['DLG_'+i],k=>hl(k<0?-1:i)); }));
  document.getElementById('dlgDl').innerHTML=dl('DLG_ALL','Full dialogue (MP3)');
  document.getElementById('dq').innerHTML=DATA.DLG_Q.map(([q,opts,ans],i)=>`<div class="lq"><span class="n">${i+1}</span><span class="qt">${esc(q)}</span><div class="co">${opts.map(o=>`<button class="opt" data-dq="${i}" data-o="${esc(o)}">${esc(o)}</button>`).join('')}</div></div>`).join('');
  document.querySelectorAll('[data-dq]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.dq, box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1; const ans=DATA.DLG_Q[i][2]; box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); }); if(b.dataset.o!==ans) b.classList.add('no'); });
}
function playDialogue(btn){ playQueue(DATA.DIALOGUE.map((_,i)=>'DLG_'+i),i=>{ hl(i); if(i>=0){ const el=document.querySelector('#script .ln[data-ln="'+i+'"]'); el&&el.scrollIntoView({block:'nearest'}); } },450,btn); }
let tkRun=null;
function talkTimer(){
  const el=document.getElementById('tkTime'), bar=document.getElementById('tkBar'); const T0=window.TK_SECS||90; let t=T0; clearInterval(tkRun);
  const draw=()=>{ el.textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0'); bar.style.width=(t/T0*100)+'%'; }; draw();
  tkRun=setInterval(()=>{ t--; draw(); if(t<=0){ clearInterval(tkRun); el.textContent="Time's up!"; beep(); } },1000);
}
/* ---------- appointment card */
function setupCard(){
  const nm=v=>String(v).toLowerCase().replace(/[\s\-.,'’]+/g,'').replace(/^the/,'');
  const check=show=>DATA.CARD.forEach(([l,a,ok],i)=>{ const el=document.getElementById('cf'+i), good=ok.map(nm).includes(nm(el.value))||nm(el.value)===nm(a);
    el.classList.toggle('ok',good); el.classList.toggle('no',!good&&el.value!==''); document.getElementById('cfa'+i).textContent=show?a:''; });
  document.getElementById('cfCheck').onclick=()=>check(false); document.getElementById('cfShow').onclick=()=>check(true);
}
function shuffle(a){ a=a.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }

/* ---------- click-to-reveal cards (photos, verb time machine) */
function revealInit(sel,allId,resetId){
  document.querySelectorAll(sel).forEach(c=>c.addEventListener('click',e=>{ if(e.target.closest('button')) return; c.classList.add('on'); }));
  document.getElementById(allId).onclick=()=>document.querySelectorAll(sel).forEach(c=>c.classList.add('on'));
  document.getElementById(resetId).onclick=()=>document.querySelectorAll(sel).forEach(c=>c.classList.remove('on'));
}
/* ---------- -ed endings */
function edInit(){
  const $=id=>document.getElementById(id); let n=0; const N=DATA.ED_WORDS.length;
  const sc=()=>$('edScore').textContent=`✓ ${n} / ${N}`;
  document.querySelectorAll('[data-ed]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.ed, row=$('ed'+i); if(row.dataset.done) return; row.dataset.done=1;
    const a=DATA.ED_WORDS[i][1]; row.querySelectorAll('.opt').forEach(o=>{ if(o.dataset.o===a) o.classList.add('ok'); }); if(b.dataset.o!==a) b.classList.add('no'); else n++; sc(); });
  $('edReset').onclick=()=>{ n=0; sc(); document.querySelectorAll('.edw').forEach(r=>{ delete r.dataset.done; r.querySelectorAll('.opt').forEach(o=>o.classList.remove('ok','no')); }); };
}
/* ---------- my weekend story */
function storyInit(){
  const $=id=>document.getElementById(id); let pick=[], al='';
  const LK=['First,','Then','After that,','In the end,'];
  const draw=()=>{ document.querySelectorAll('.sev').forEach(b=>{ const k=pick.indexOf(+b.dataset.sev); b.classList.toggle('sel',k>=0); b.dataset.k=k>=0?k+1:''; });
    document.querySelectorAll('.sal').forEach(b=>b.classList.toggle('ok',b.dataset.al===al)); $('stN').textContent=`${pick.length} / 4`;
    if(!pick.length){ $('stTx').innerHTML='<span class="muted">Your story appears here. Then tell it to your partner!</span>'; return; }
    const ev=pick.map(i=>DATA.STORY_EVENTS[i][1]);
    const lines=['Last weekend was great.'].concat(ev.map((t,k)=>`<b>${LK[k===ev.length-1&&ev.length>1?3:Math.min(k,2)]}</b> I ${esc(t)}.`));
    if(al) lines.push(`<b>Although</b> ${esc(al)}, I really enjoyed the experience.`);
    lines.push('I was exhausted, but it was worth it!');
    $('stTx').innerHTML=lines.map(l=>`<p>${l}</p>`).join(''); };
  document.querySelectorAll('.sev').forEach(b=>b.onclick=()=>{ const i=+b.dataset.sev, k=pick.indexOf(i); if(k>=0) pick.splice(k,1); else if(pick.length<4) pick.push(i); draw(); });
  document.querySelectorAll('.sal').forEach(b=>b.onclick=()=>{ al=al===b.dataset.al?'':b.dataset.al; draw(); });
  $('stReset').onclick=()=>{ pick=[]; al=''; draw(); }; draw();
}
/* ---------- small countdown (two truths) */
function miniTimer(tId,bId,secs){ let t=secs, run=null; const el=document.getElementById(tId), bar=document.getElementById(bId);
  const draw=()=>{ el.textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0'); bar.style.width=(t/secs*100)+'%'; };
  return ()=>{ clearInterval(run); t=secs; draw(); run=setInterval(()=>{ t--; draw(); if(t<=0){ clearInterval(run); el.textContent="Time's up!"; beep(); } },1000); }; }
function truthInit(){
  const $=id=>document.getElementById(id); let cur=0;
  $('ttNew').onclick=()=>{ let i; do{ i=Math.floor(Math.random()*DATA.TRUTH_TOPICS.length); }while(i===cur); cur=i; const c=$('ttTopic'); c.innerHTML=`<span>🎲</span><b>Topic: ${esc(DATA.TRUTH_TOPICS[i])}</b>`; c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); };
  $('ttStart').onclick=miniTimer('ttTime','ttBar',60);
}
/* ---------- six past verbs counter */
function verbsInit(){
  const $=id=>document.getElementById(id); const upd=()=>{ const n=document.querySelectorAll('.tvb.on').length; $('tvN').textContent=`${n} / 6`; $('tvN').classList.toggle('done',n>=6); };
  document.querySelectorAll('[data-tv]').forEach(b=>b.onclick=()=>{ b.classList.toggle('on'); upd(); });
  $('tvReset').onclick=()=>{ document.querySelectorAll('.tvb').forEach(b=>b.classList.remove('on')); upd(); }; upd();
}
/* ---------- yesterday card */
function yesterdayInit(){
  const $=id=>document.getElementById(id);
  $('ycMake').onclick=()=>{ const v=DATA.YESTERDAY.map((y,i)=>$('yc'+i).value.trim());
    if(!v.some(Boolean)){ $('ycTx').innerHTML='<span class="muted">Fill in at least one line.</span>'; return; }
    $('ycTx').innerHTML=DATA.YESTERDAY.map(([em,t],i)=>v[i]?`<p>${em} ${esc(t.replace('___',v[i]))}</p>`:'').join(''); };
}
/* ---------- game: irregular quick-fire */
function quickInit(){
  const $=id=>document.getElementById(id), N=DATA.QUICK.length; let r=-1, score=0, done=true, order=shuffle([...Array(N).keys()]), tm=null, t=6;
  const nm=s=>String(s).toLowerCase().trim();
  const upd=()=>{ $('qfN').textContent=`Round ${Math.max(r+1,0)} / ${N}`; $('qfScore').textContent='Score: '+score; };
  const finish=()=>{ if(done) return; clearInterval(tm); done=true; const [b,ans]=DATA.QUICK[order[r]], ok=ans.includes(nm($('qfIn').value)); if(ok) score++;
    $('qfIn').classList.add(ok?'ok':'no'); $('qfQ').innerHTML=`<b>${esc(b)} → ${esc(ans[0])}</b><span>${ok?'✅ Correct!':'❌ '+(t<=0?"Time's up!":'Not quite.')}</span>`; upd(); $('qfGo').textContent=r>=N-1?'🏆 See score':'Next verb →'; };
  $('qfGo').onclick=()=>{ if(!done) return; if(r>=N-1){ $('qfQ').innerHTML=`<b>🏆 Finished!</b><span>Score: ${score} / ${N}</span>`; r=-1; score=0; order=shuffle(order); $('qfGo').textContent='Next verb →'; return; }
    r++; done=false; t=6; $('qfIn').value=''; $('qfIn').classList.remove('ok','no'); $('qfQ').innerHTML=`<b>${esc(DATA.QUICK[order[r]][0])}</b><span>past form?</span>`; $('qfT').textContent='⏱ 6'; upd(); $('qfIn').focus();
    clearInterval(tm); tm=setInterval(()=>{ t--; $('qfT').textContent='⏱ '+Math.max(t,0); if(t<=0) finish(); },1000); };
  $('qfOk').onclick=finish; $('qfIn').addEventListener('keydown',e=>{ if(e.key==='Enter') finish(); }); upd();
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=90;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['🎉','event'],['🛒','visit'],['🏨','stay'],['🏠','return'],['😄','enjoy'],['😩','exhausted'],['⭐','memorable'],['🎤','attend']]);
  buildCloud('cloud2',[['❓','happen'],['⚡','suddenly'],['🍀','fortunately'],['🚌','miss'],['💡','realise'],['🤔','decide'],['🏁','eventually'],['⏳','while']]);
  revealInit('[data-ph]','phAll','phReset'); revealInit('[data-vt]','vtAll','vtReset'); edInit(); buildListen(); buildDialogue(); setupCard(); storyInit(); truthInit(); verbsInit(); yesterdayInit(); quickInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL'||id==='EL2') return; if(b.closest('.fgrid,.phgrid,.vtgrid,.edgrid,.sgrid')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
  const $=id=>document.getElementById(id);
  document.querySelectorAll('[data-flipall]').forEach(b=>b.onclick=()=>flipAll(b,true));
  document.querySelectorAll('[data-flipreset]').forEach(b=>b.onclick=()=>flipAll(b,false));
  document.querySelectorAll('[data-rep]').forEach(b=>b.onclick=()=>repeatQueue(b));
  $('lCheck').onclick=listenCheck;
  $('dlgPlay').onclick=e=>playDialogue(e.currentTarget);
  $('dlgStop').onclick=stopAll;
  $('dlgScript').onclick=e=>{ const sc=$('script'); sc.classList.toggle('blur'); e.currentTarget.textContent=sc.classList.contains('blur')?'👁 Show script':'🙈 Hide script'; };
  $('tkStart').onclick=talkTimer;
  window.addEventListener('resize',fit); document.addEventListener('fullscreenchange',fit); fit();
  const h=parseInt((location.hash||'').slice(1)); go(isNaN(h)?0:h-1);
});
