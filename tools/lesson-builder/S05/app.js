/* =========================================================
   S05 · Directions & Getting Around Town — lesson activities
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
/* ---------- warm-up: reveal tiles */
function rvInit(){
  document.querySelectorAll('[data-rv]').forEach(t=>t.addEventListener('click',e=>{ if(e.target.closest('button,a')) return; t.classList.toggle('on'); }));
  document.querySelectorAll('[data-rvall]').forEach(b=>b.onclick=()=>document.querySelectorAll('[data-rv]').forEach(t=>t.classList.add('on')));
  document.querySelectorAll('[data-rvreset]').forEach(b=>b.onclick=()=>document.querySelectorAll('[data-rv]').forEach(t=>t.classList.remove('on')));
}
/* ---------- order the steps */
function orderInit(){
  const $=id=>document.getElementById(id); let set=0, mix=[], pick=[], checked=false;
  const mixFor=k=>{ const n=DATA.ORDER[k].steps.length; let m; do{ m=shuffle([...Array(n).keys()]); }while(m.every((v,i)=>v===i)); return m; };
  const draw=()=>{
    const O=DATA.ORDER[set];
    $('ocards').innerHTML=mix.map(j=>{ const p=pick.indexOf(j); return `<div class="oc${p>=0?' on':''}" data-j="${j}"><span class="on1">${p>=0?p+1:''}</span><span class="ot">${esc(O.steps[j]).replace(/^(First|Then|After that|Finally)/,'<b class="lkw">$1</b>').replace(/\buntil\b/,'<b class="lkw">until</b>')}</span>${pbtn(`OS_${set}_${j}`)}</div>`; }).join('');
    $('ocards').querySelectorAll('.oc').forEach(c=>c.addEventListener('click',e=>{ if(e.target.closest('button')||checked) return; const j=+c.dataset.j, p=pick.indexOf(j); if(p>=0) pick.splice(p,1); else pick.push(j); draw(); }));
    $('oScore').textContent=`${pick.length} / ${O.steps.length}`;
  };
  const load=k=>{ set=k; mix=mixFor(k); pick=[]; checked=false; draw(); document.querySelectorAll('[data-ot]').forEach(b=>b.classList.toggle('ghost',+b.dataset.ot!==k)); };
  document.querySelectorAll('[data-ot]').forEach(b=>b.onclick=()=>load(+b.dataset.ot));
  $('oCheck').onclick=()=>{ checked=true; let n=0; $('ocards').querySelectorAll('.oc').forEach(c=>{ const j=+c.dataset.j, good=pick.indexOf(j)===j; if(good) n++; c.classList.toggle('ok',good); c.classList.toggle('no',!good); }); $('oScore').textContent=`✓ ${n} / ${DATA.ORDER[set].steps.length}`; };
  $('oShow').onclick=()=>{ pick=DATA.ORDER[set].steps.map((_,i)=>i); mix=pick.slice(); checked=true; draw(); $('ocards').querySelectorAll('.oc').forEach(c=>c.classList.add('ok')); $('oScore').textContent=`✓ ${pick.length} / ${pick.length}`; };
  $('oReset').onclick=()=>load(set);
  load(0);
}
/* ---------- town map helpers */
const SVGNS='http://www.w3.org/2000/svg';
function placeName(id){ return DATA.PLACES[id]; }
function markPlace(svg,id,cls){ const g=svg.querySelector(`.pl[data-place="${id}"]`); if(g) g.classList.add(cls); }
function clearPlaces(svg){ svg.querySelectorAll('.pl').forEach(g=>g.classList.remove('ok','no','hint')); }
/* ---------- follow the route */
function routeInit(){
  const $=id=>document.getElementById(id), svg=$('map2'), mk=svg.querySelector('.mk'), trail=svg.querySelector('.trail');
  let r=0, k=0, pos=DATA.START.slice(), anim=null, solved=false;
  const R=()=>DATA.ROUTES[r];
  const ptsUpTo=n=>{ let a=[DATA.START.slice()]; R().steps.slice(0,n).forEach(s=>s[1].forEach(p=>a.push(p))); return a; };
  const setPos=p=>{ pos=p.slice(); mk.setAttribute('transform',`translate(${p[0]} ${p[1]})`); };
  const setTrail=a=>trail.setAttribute('d','M'+a.map(p=>p.join(' ')).join(' L'));
  const moveAlong=(targets,done)=>{ cancelAnimationFrame(anim); const seq=targets.slice(); let from=pos.slice(), to=seq.shift(), t0=null;
    if(!to){ done&&done(); return; }
    const step=ts=>{ if(t0===null) t0=ts; const d=Math.hypot(to[0]-from[0],to[1]-from[1])||1, dur=d/0.32, f=Math.min(1,(ts-t0)/dur);
      setPos([from[0]+(to[0]-from[0])*f, from[1]+(to[1]-from[1])*f]);
      if(f>=1){ from=to.slice(); to=seq.shift(); t0=null; if(!to){ done&&done(); return; } }
      anim=requestAnimationFrame(step); };
    anim=requestAnimationFrame(step); };
  const drawSteps=()=>{ const S=R().steps;
    $('rtSteps').innerHTML=S.map(([t],j)=>`<div class="rst${j<k?' on':''}${j===k-1?' now':''}"><span class="n">${j+1}</span><span class="t">${j<k?esc(t).replace(/^(First|Then|After that|Finally)/,'<b class="lkw">$1</b>').replace(/\buntil\b/,'<b class="lkw">until</b>'):'· · ·'}</span>${j<k?pbtn(`RS_${r}_${j}`):''}</div>`).join('');
    $('rtNext').textContent=k>=S.length?'Done ✓':'Next step →';
    if(k>=S.length&&!solved) $('rtQ').innerHTML='📍 <b>Where are you?</b> Click the place on the map.';
    else if(!solved) $('rtQ').textContent='Read each step aloud. The marker moves on the map.';
  };
  const load=n=>{ cancelAnimationFrame(anim); r=n; k=0; solved=false; clearPlaces(svg); setPos(DATA.START); setTrail([DATA.START]); svg.classList.remove('ask'); drawSteps();
    document.querySelectorAll('[data-rt]').forEach(b=>b.classList.toggle('ghost',+b.dataset.rt!==n)); };
  $('rtNext').onclick=()=>{ const S=R().steps; if(k>=S.length) return; k++; setTrail(ptsUpTo(k)); moveAlong(S[k-1][1].slice()); drawSteps(); if(k>=S.length) svg.classList.add('ask'); };
  $('rtBack').onclick=()=>{ if(k<=0) return; k--; cancelAnimationFrame(anim); const a=ptsUpTo(k); setTrail(a); setPos(a[a.length-1]); solved=false; clearPlaces(svg); svg.classList.toggle('ask',k>=R().steps.length); drawSteps(); };
  $('rtReset').onclick=()=>load(r);
  document.querySelectorAll('[data-rt]').forEach(b=>b.onclick=()=>load(+b.dataset.rt));
  svg.querySelectorAll('.pl.click').forEach(g=>g.addEventListener('click',()=>{
    if(k<R().steps.length||solved) return; const id=g.dataset.place;
    if(id===R().to){ solved=true; clearPlaces(svg); markPlace(svg,id,'ok'); $('rtQ').innerHTML=`✅ <b>Yes!</b> You are at the <b>${esc(placeName(id))}</b>.`; }
    else { g.classList.add('no'); setTimeout(()=>g.classList.remove('no'),900); $('rtQ').innerHTML=`❌ Not the ${esc(placeName(id))}. Read the last step again!`; }
  }));
  load(0);
}
/* ---------- word stress: tap the stressed syllable */
function stressInit(){
  let n=0; const sc=()=>document.getElementById('stScore').textContent=`✓ ${n} / ${DATA.STRESS.length}`;
  document.querySelectorAll('[data-st]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.st, box=document.getElementById('st'+i); if(box.dataset.done) return; box.dataset.done=1;
    const ans=DATA.STRESS[i][2]; box.querySelectorAll('.syl').forEach(x=>{ if(+x.dataset.k===ans) x.classList.add('ok'); }); if(+b.dataset.k!==ans) b.classList.add('no'); else n++; box.classList.add('shown'); sc(); });
  document.getElementById('stReset').onclick=()=>{ n=0; sc(); document.querySelectorAll('.stw').forEach(w=>{ delete w.dataset.done; w.classList.remove('shown'); w.querySelectorAll('.syl').forEach(x=>x.classList.remove('ok','no')); }); };
}
/* ---------- secret destination: random start */
function secretInit(){ const el=document.getElementById('sdStart'); document.getElementById('sdDraw').onclick=()=>{ let s; do{ s=DATA.STARTS[Math.floor(Math.random()*DATA.STARTS.length)]; }while(s===el.textContent&&DATA.STARTS.length>1); el.textContent=s; el.classList.remove('pop'); void el.offsetWidth; el.classList.add('pop'); }; }
/* ---------- my route: checklist */
function planInit(){
  const $=id=>document.getElementById(id), v=id=>($(id).value||'').trim()!=='';
  const upd=()=>{ const steps=[0,1,2,3,4].filter(i=>v('pl'+i)).length, lm=v('plL0')&&v('plL1'), lk=v('pl0')&&v('pl1')&&v('pl4');
    const set=(id,ok,t)=>{ $(id).textContent=(ok?'✅ ':'⬜ ')+t; $(id).classList.toggle('ok',ok); };
    set('pcSteps',steps>=4,`At least 4 steps (${steps})`); set('pcLm',lm,'2 landmarks'); set('pcLink',lk,'first · then · finally'); };
  document.querySelectorAll('.plan input').forEach(i=>i.addEventListener('input',upd)); upd();
}
/* ---------- game: listen & find */
function findInit(){
  const $=id=>document.getElementById(id), svg=$('map4'), N=DATA.GAME.length; let r=-1, score=0, done=true, order=[];
  const upd=()=>{ $('lfN').textContent=`Round ${Math.max(r+1,0)} / ${N}`; $('lfScore').textContent='Score: '+score; };
  const reset=()=>{ r=-1; score=0; done=true; order=shuffle([...Array(N).keys()]); clearPlaces(svg); svg.classList.remove('ask'); $('lfTx').hidden=true; upd();
    $('lfQ').innerHTML='<b>🎯 Ready?</b><span>Start at the station ★. Listen, follow on the map, then click the place.</span>'; $('lfGo').textContent='▶ Listen · next round'; };
  $('lfGo').onclick=()=>{ if(r>=N-1&&done){ $('lfQ').innerHTML=`<b>🏆 Finished!</b><span>Score: ${score} / ${N}</span>`; return; }
    if(!done){ play('GM_'+order[r],$('lfGo')); return; }
    r++; done=false; clearPlaces(svg); svg.classList.add('ask'); $('lfTx').hidden=true; $('lfTx').textContent=DATA.GAME[order[r]][0]; upd();
    $('lfQ').innerHTML='<b>🎧 Listen…</b><span>Follow the directions from the station ★. Click the place.</span>'; play('GM_'+order[r],$('lfGo')); };
  $('lfAgain').onclick=()=>{ if(r>=0) play('GM_'+order[r],$('lfAgain')); };
  $('lfShow').onclick=()=>{ if(r>=0) $('lfTx').hidden=!$('lfTx').hidden; };
  $('lfReset').onclick=reset;
  svg.querySelectorAll('.pl.click').forEach(g=>g.addEventListener('click',()=>{ if(done||r<0) return; done=true; svg.classList.remove('ask');
    const id=g.dataset.place, ans=DATA.GAME[order[r]][1]; markPlace(svg,ans,'ok'); if(id!==ans) g.classList.add('no'); else score++; upd();
    $('lfQ').innerHTML=id===ans?`<b>✅ Correct!</b><span>It's the ${esc(placeName(ans))}.</span>`:`<b>❌ Not quite</b><span>It's the ${esc(placeName(ans))}, not the ${esc(placeName(id))}.</span>`;
    $('lfTx').hidden=false; $('lfGo').textContent=r>=N-1?'🏆 See score':'▶ Listen · next round'; }));
  reset();
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=60;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['🗺','map'],['🏛','landmark'],['↰','turn left'],['🚦','intersection'],['🚶','walk'],['📍','across from'],['🏁','get to'],['⏱','10 min']]);
  buildCloud('cloud2',[['🛒','shopping'],['🥛','dairy'],['🍚','a packet of rice'],['🥕','fresh'],['📝','list'],['❓','any?'],['🧺','aisle'],['✅','enough']]);
  rvInit(); const mqReset=setupMC('mq',DATA.MAPQ,'mqScore','MQ'); orderInit(); routeInit(); stressInit(); buildListen(); buildDialogue(); setupCard(); secretInit(); planInit(); findInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL') return; if(b.closest('.mapq,.wq,.fgrid,.rvgrid,.btgrid,.ocards,.rtsteps,.lkbox,.stbox,.sgrid')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
  const $=id=>document.getElementById(id);
  document.querySelectorAll('[data-flipall]').forEach(b=>b.onclick=()=>flipAll(b,true));
  document.querySelectorAll('[data-flipreset]').forEach(b=>b.onclick=()=>flipAll(b,false));
  document.querySelectorAll('[data-rep]').forEach(b=>b.onclick=()=>repeatQueue(b));
  $('mqReset').onclick=mqReset;
  $('lCheck').onclick=listenCheck;
  $('lScript').onclick=e=>{ const p=$('lscr'), show=p.hidden; p.hidden=!show; e.currentTarget.textContent=show?'🙈 Hide script':'📜 Show script'; };
  $('lscr').innerHTML=`<div class="sh">📜 Script <span style="font-size:13px;color:var(--muted)">Source: ${esc(DATA.LISTEN.source)}</span></div>`+DATA.LISTEN.script.map(([w,t])=>`<div class="sl ${w}"><b>${DATA.LISTEN.names[w]}</b><span>${esc(t)}</span></div>`).join('');
  $('dlgPlay').onclick=e=>playDialogue(e.currentTarget);
  $('dlgStop').onclick=stopAll;
  $('dlgScript').onclick=e=>{ const sc=$('script'); sc.classList.toggle('blur'); e.currentTarget.textContent=sc.classList.contains('blur')?'👁 Show script':'🙈 Hide script'; };
  $('tkStart').onclick=talkTimer;
  window.addEventListener('resize',fit); document.addEventListener('fullscreenchange',fit); fit();
  const h=parseInt((location.hash||'').slice(1)); go(isNaN(h)?0:h-1);
});
