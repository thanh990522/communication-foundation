/* =========================================================
   S11 · Past Questions & Storytelling — lesson activities
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

const qn=s=>String(s).toLowerCase().replace(/[’`]/g,"'").replace(/[?.!,]/g,'').replace(/\s+/g,' ').trim();
/* ---------- warm-up: guess the story (one clue per click) */
function guessInit(){
  const cards=[...document.querySelectorAll('[data-gs]')];
  const draw=c=>{ const k=+c.dataset.k, n=c.querySelectorAll('.gsi').length; c.querySelectorAll('.gsi').forEach(x=>x.classList.toggle('on',+x.dataset.n<k)); c.classList.toggle('on',k>n); };
  cards.forEach(c=>{ c.addEventListener('click',e=>{ if(e.target.closest('button')) return; const n=c.querySelectorAll('.gsi').length; c.dataset.k=Math.min(+c.dataset.k+1,n+1); draw(c); }); c.dataset.k=1; draw(c); });
  document.getElementById('gsAll').onclick=()=>cards.forEach(c=>{ c.dataset.k=9; draw(c); });
  document.getElementById('gsReset').onclick=()=>cards.forEach(c=>{ c.dataset.k=1; draw(c); });
}
/* ---------- story mountain */
function mountainInit(){
  const set=(i,on)=>{ document.querySelector(`[data-mt="${i}"]`).classList.toggle('on',on); document.getElementById('mtl'+i).classList.toggle('on',on); };
  document.querySelectorAll('[data-mt]').forEach(b=>b.onclick=()=>set(+b.dataset.mt,true));
  document.getElementById('mtAll').onclick=()=>document.querySelectorAll('[data-mt]').forEach(b=>set(+b.dataset.mt,true));
  document.getElementById('mtReset').onclick=()=>document.querySelectorAll('[data-mt]').forEach(b=>set(+b.dataset.mt,false));
}
/* ---------- question maker */
function qmakerInit(){
  const $=id=>document.getElementById(id), rows=[...document.querySelectorAll('.qmr')];
  const sc=()=>$('qmScore').textContent=`✓ ${rows.filter(r=>r.classList.contains('ok')).length} / ${rows.length}`;
  const check=show=>rows.forEach((r,i)=>{ const [a,qs]=DATA.QMAKER[i], x=r.querySelector('.qmin'); if(show) x.value=qs[0][0].toUpperCase()+qs[0].slice(1)+'?';
    if(!x.value.trim()) return; const ok=qs.includes(qn(x.value)); r.classList.toggle('ok',ok); r.classList.toggle('no',!ok); r.querySelector('.qmok').textContent=ok?'✅':'→ '+qs[0][0].toUpperCase()+qs[0].slice(1)+'?'; sc(); });
  $('qmCheck').onclick=()=>check(false); $('qmShow').onclick=()=>check(true);
  $('qmReset').onclick=()=>{ rows.forEach(r=>{ r.classList.remove('ok','no'); r.querySelector('.qmin').value=''; r.querySelector('.qmok').textContent=''; }); sc(); };
}
/* ---------- story dice */
function diceInit(){
  const $=id=>document.getElementById(id), pick=a=>a[Math.floor(Math.random()*a.length)];
  $('dRoll').onclick=()=>{ [['dP',DATA.DICE_PLACE],['dR',DATA.DICE_PROBLEM],['dL',DATA.DICE_LUCK]].forEach(([id,a])=>{ const d=$(id); d.querySelector('b').textContent=pick(a); d.classList.remove('pop'); void d.offsetWidth; d.classList.add('pop'); });
    document.querySelectorAll('.stgs input').forEach(x=>x.checked=false); };
}
/* ---------- real-life: follow-up questions */
function followInit(){
  const $=id=>document.getElementById(id); let last=0;
  document.querySelectorAll('[data-fq]').forEach(b=>b.onclick=()=>{ const ins=[0,1,2].map(i=>$('fq'+i)); const t=ins.find(x=>!x.value.trim())||ins[last%3]; t.value=b.dataset.fq.replace('…?','').replace('…',' ').replace(/\s+/g,' '); t.focus(); last++; });
  $('fqCheck').onclick=()=>{ const v=[0,1,2].map(i=>$('fq'+i).value.trim()).filter(Boolean);
    const good=v.filter(q=>/\?$/.test(q)&&/^(did|was|were|where|what|who|how|when|why)\b/i.test(q));
    $('fqRes').innerHTML=v.length<3?'✍️ Write 3 questions.':good.length===3?'✅ Great! 3 past questions — now ask your partner!':`⚠️ Check: start with <b>Did / Was / Were / Where / What / Who / How</b> and end with <b>?</b> (${good.length}/3 OK)`; };
}
/* ---------- game: story jigsaw */
function jigsawInit(){
  const $=id=>document.getElementById(id); let cur=-1, score=0, line=[], order=[];
  const draw=()=>{ const st=DATA.JIGSAW[cur][1]; $('jgBank').innerHTML=order.filter(k=>!line.includes(k)).map(k=>`<button class="jgs" data-jg="${k}">${esc(st[k])}</button>`).join('');
    $('jgLine').innerHTML=line.map(k=>`<li>${esc(st[k])}</li>`).join(''); $('jgBank').querySelectorAll('[data-jg]').forEach(b=>b.onclick=()=>{ line.push(+b.dataset.jg); $('jgRes').textContent=''; draw(); }); };
  $('jgNew').onclick=()=>{ cur=(cur+1)%DATA.JIGSAW.length; line=[]; order=shuffle([...Array(DATA.JIGSAW[cur][1].length).keys()]); $('jgTitle').textContent=DATA.JIGSAW[cur][0]+' — click the sentences in order'; $('jgRes').textContent=''; draw(); };
  $('jgUndo').onclick=()=>{ if(cur<0) return; line.pop(); draw(); };
  $('jgCheck').onclick=()=>{ if(cur<0) return; const n=DATA.JIGSAW[cur][1].length; if(line.length<n){ $('jgRes').textContent='Put all the sentences in the story first.'; return; }
    const ok=line.every((k,i)=>k===i); if(ok){ score++; $('jgScore').textContent='Score: '+score; }
    $('jgLine').querySelectorAll('li').forEach((li,i)=>li.classList.add(line[i]===i?'ok':'no')); $('jgRes').innerHTML=ok?'✅ Perfect story! Now tell it to your partner.':'❌ Not quite — check the linkers: at first → while → suddenly → fortunately → eventually → in the end.'; };
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=120;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['❓','happen'],['⚡','suddenly'],['🍀','fortunately'],['🚌','miss the bus'],['💡','realise'],['🤔','decide'],['🏁','eventually'],['⏳','while']]);
  buildCloud('cloud2',[['🏆','challenge'],['✅','complete'],['🔎','clarify'],['🗣','explain'],['💡','solution'],['😎','confident'],['🤝','interaction'],['📝','feedback']]);
  guessInit(); mountainInit(); qmakerInit(); buildListen(); buildDialogue(); setupCard(); diceInit(); followInit(); jigsawInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL'||id==='EL2') return; if(b.closest('.fgrid,.gsgrid,.mtlist,.lkbox,.sgrid')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
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
