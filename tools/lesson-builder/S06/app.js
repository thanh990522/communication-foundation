/* =========================================================
   S06 · Food, Shopping Lists & Quantities — lesson activities
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
/* ---------- warm-up: what's in the fridge? */
function fridgeInit(){
  const $=id=>document.getElementById(id), fr=$('fridge'); let t=null;
  $('frLook').onclick=()=>{ clearInterval(t); fr.classList.remove('covered'); let s=20; $('frTime').textContent='0:20';
    t=setInterval(()=>{ s--; $('frTime').textContent='0:'+String(s).padStart(2,'0'); if(s<=0){ clearInterval(t); fr.classList.add('covered'); fr.querySelector('.frcover').innerHTML='🤔<b>What did you see?</b><span>There are some… · There\'s a carton of…</span>'; beep(); } },1000); };
  $('frShow').onclick=()=>{ clearInterval(t); fr.classList.remove('covered'); };
}
/* ---------- containers: build the list */
function containersInit(){
  const $=id=>document.getElementById(id), N=DATA.CONTAINERS.length; let selC=null, done=new Set();
  const draw=()=>{ $('ctOut').innerHTML=[...done].map(i=>`<div class="cto"><span>✓ <b>${esc(DATA.CONTAINERS[i][0])}</b> ${esc(DATA.CONTAINERS[i][1])} ${DATA.CONTAINERS[i][2]}</span><span class="spk" role="button" data-a="CT_${i}">🔊</span></div>`).join('');
    $('ctScore').textContent=`${done.size} / ${N}`;
    document.querySelectorAll('[data-ct]').forEach(b=>{ b.classList.toggle('done',done.has(+b.dataset.ct)); b.classList.toggle('sel',selC===+b.dataset.ct); });
    document.querySelectorAll('[data-fd]').forEach(b=>b.classList.toggle('done',done.has(+b.dataset.fd))); };
  document.querySelectorAll('[data-ct]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.ct; if(done.has(i)) return; selC=selC===i?null:i; draw(); });
  document.querySelectorAll('[data-fd]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.fd; if(done.has(i)||selC===null) return;
    if(i===selC){ done.add(i); selC=null; draw(); } else { b.classList.add('no'); setTimeout(()=>b.classList.remove('no'),600); } });
  $('ctShow').onclick=()=>{ DATA.CONTAINERS.forEach((_,i)=>done.add(i)); selC=null; draw(); };
  $('ctReset').onclick=()=>{ done.clear(); selC=null; draw(); };
  draw();
}
/* ---------- enough or not enough? */
function enoughInit(){
  const $=id=>document.getElementById(id), items=DATA.RECIPE.items; let pick={};
  document.querySelectorAll('[data-en]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.en; pick[i]=b.dataset.v==='1'; document.querySelectorAll(`[data-en="${i}"]`).forEach(x=>x.classList.toggle('sel',x===b)); });
  $('enCheck').onclick=()=>{ let n=0; items.forEach((it,i)=>{ const row=$('rc'+i), good=pick[i]===it[4]; if(good) n++; row.classList.toggle('ok',good); row.classList.toggle('no',!good); });
    $('enScore').textContent=`✓ ${n} / ${items.length}`;
    const need=items.filter(it=>!it[4]).map(it=>(DATA.COUNT.includes(it[0])?'a few ':'a little ')+it[0]);
    $('enOut').innerHTML=need.map(x=>`<div class="cto"><span>🛒 We need <b>${esc(x)}</b>.</span></div>`).join('')+`<div class="cto muted">We have enough ${items.filter(it=>it[4]).map(it=>esc(it[0])).join(', ')}.</div>`; };
  $('enReset').onclick=()=>{ pick={}; document.querySelectorAll('.rcr').forEach(r=>r.classList.remove('ok','no')); document.querySelectorAll('[data-en]').forEach(x=>x.classList.remove('sel')); $('enScore').textContent=`— / ${items.length}`; $('enOut').innerHTML='<span class="muted">Check first!</span>'; };
}
/* ---------- supermarket stock board */
function stockInit(){
  const $=id=>document.getElementById(id), ST=[['ok','✅'],['few','⚠'],['out','❌']]; let li=-1;
  const shuffleStock=()=>document.querySelectorAll('.sti2').forEach(el=>{ const r=Math.random(), k=r<.55?0:r<.78?1:2; el.className='sti2 '+ST[k][0]; el.querySelector('.sst').textContent=ST[k][1]; });
  const newList=()=>{ let i; do{ i=Math.floor(Math.random()*DATA.SHOP_LISTS.length); }while(i===li&&DATA.SHOP_LISTS.length>1); li=i; $('slOut').innerHTML=DATA.SHOP_LISTS[i].map(x=>`<div class="cto">☐ ${esc(x)}</div>`).join(''); };
  $('skShuffle').onclick=shuffleStock; $('slNew').onclick=newList; shuffleStock(); newList();
}
/* ---------- my shopping list: quantifier checker */
function mslistInit(){
  const $=id=>document.getElementById(id);
  const upd=()=>{ let n=0; document.querySelectorAll('.msr').forEach(r=>{ const q=r.querySelector('.msq').value, f=r.querySelector('.msf').value, v=r.querySelector('.msv');
      r.classList.remove('ok','no'); if(!q||!f){ v.textContent=''; return; }
      const good=(DATA.FITS[q]||[]).includes(f); if(good) n++; r.classList.add(good?'ok':'no');
      v.innerHTML=good?`✓ We need ${esc(q)} ${esc(f)}.`:`✗ ${esc(q)} + ${esc(f)}?`; });
    $('msN').textContent=n; $('msBar').style.width=Math.min(100,n/5*100)+'%'; $('msGoal').textContent=n>=5?'🎉 Goal!':'Goal: 5'; };
  document.querySelectorAll('.msr select').forEach(s=>s.addEventListener('change',upd)); upd();
}
/* ---------- game: fill the trolley */
function trolleyInit(){
  const $=id=>document.getElementById(id), N=DATA.ORDERS.length, names=DATA.TROLLEY.map(t=>t[0]); let r=-1, score=0, done=true, cnt=names.map(()=>0), order=[];
  const draw=()=>{ cnt.forEach((c,i)=>{ $('tn'+i).textContent=c; document.querySelector(`[data-ti="${i}"]`).classList.toggle('has',c>0); }); $('tgN').textContent=`Round ${Math.max(r+1,0)} / ${N}`; $('tgScore').textContent='Score: '+score; };
  document.querySelectorAll('[data-tp]').forEach(b=>b.onclick=()=>{ if(done) return; cnt[+b.dataset.tp]=Math.min(20,cnt[+b.dataset.tp]+1); draw(); });
  document.querySelectorAll('[data-tm]').forEach(b=>b.onclick=()=>{ if(done) return; cnt[+b.dataset.tm]=Math.max(0,cnt[+b.dataset.tm]-1); draw(); });
  $('tgGo').onclick=()=>{ if(!done){ play('OR_'+order[r],$('tgGo')); return; } if(r>=N-1){ $('tgQ').innerHTML=`<b>🏆 Finished!</b><span>Score: ${score} / ${N}</span>`; return; }
    r++; done=false; cnt=names.map(()=>0); document.querySelectorAll('.tri').forEach(x=>x.classList.remove('ok','no')); $('tgTx').hidden=true; $('tgTx').textContent='“'+DATA.ORDERS[order[r]][0]+'”'; draw();
    $('tgQ').innerHTML='<b>🎧 Listen…</b><span>Fill the trolley, then click “Check trolley”.</span>'; play('OR_'+order[r],$('tgGo')); };
  $('tgAgain').onclick=()=>{ if(r>=0) play('OR_'+order[r],$('tgAgain')); };
  $('tgCheck').onclick=()=>{ if(done||r<0) return; done=true; const want=DATA.ORDERS[order[r]][1]; let ok=true;
    names.forEach((n,i)=>{ const w=want[n]||0, good=cnt[i]===w; if(!good) ok=false; const el=document.querySelector(`[data-ti="${i}"]`); if(w||cnt[i]){ el.classList.add(good?'ok':'no'); } if(!good) $('tn'+i).textContent=cnt[i]+' → '+w; });
    if(ok) score++; $('tgScore').textContent='Score: '+score; $('tgQ').innerHTML=ok?'<b>✅ Perfect trolley!</b><span>Next order →</span>':'<b>❌ Check the numbers</b><span>Red = wrong number (yours → correct).</span>'; $('tgTx').hidden=false;
    $('tgGo').textContent=r>=N-1?'🏆 See score':'▶ Listen · next order'; };
  order=shuffle([...Array(N).keys()]); draw();
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=60;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['🥛','a carton of milk'],['🍚','a packet of rice'],['🥚','a few eggs'],['🧈','a little butter'],['🛒','aisle 3'],['❌','out of stock'],['🥕','fresh'],['✅','enough']]);
  buildCloud('cloud2',[['🍽','menu'],['🥗','starter'],['🍛','main course'],['🍟','side dish'],['👍','recommend'],['🥜','allergy'],['🧾','bill'],['➗','split']]);
  fridgeInit(); containersInit(); const mqReset=setupMC('mq',DATA.MAPQ,'mqScore','MQ'); enoughInit(); buildListen(); buildDialogue(); setupCard(); stockInit(); mslistInit(); trolleyInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL') return; if(b.closest('.wq,.fgrid,.fridge,.gqgrid,.lkbox,.swbox,.sgrid')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
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
  window.addEventListener('resize',fit); document.addEventListener('fullscreenchange',fit); fit();
  const h=parseInt((location.hash||'').slice(1)); go(isNaN(h)?0:h-1);
});
