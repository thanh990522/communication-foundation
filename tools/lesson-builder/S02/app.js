/* =========================================================
   S02 · Routines, Habits & Real Schedules — lesson activities
   (DATA is injected by build.py from content.py)
   ========================================================= */
const DATA = /*DATA_JSON*/;
const pbtn = (id,cls) => `<button class="play sm${cls?' '+cls:''}" data-a="${id}">${PLAY_SVG}</button>`;
const norm = s => String(s).toLowerCase().replace(/[\s\-–.,!?'’]+/g,'').trim();
function hl(i){ document.querySelectorAll('#script .ln').forEach((l,k)=>l.classList.toggle('now',k===i)); }


/* ---------- cover cloud */
function buildCloud(id){
  const el=document.getElementById(id); if(!el) return;
  const words=[['⏰','7:00'],['☕','coffee'],['🚌','commute'],['💼','work'],['⏸','break'],['🌙','shift'],['📅','weekdays'],['🎉','weekends']];
  const pos=[[20,10,-6],[230,0,5],[110,120,8],[300,140,-6],[10,250,4],[200,270,-8],[60,380,-4],[260,390,6]];
  el.innerHTML=words.map((w,i)=>`<div class="wtag" style="left:${pos[i][0]}px;top:${pos[i][1]}px;transform:rotate(${pos[i][2]}deg);background:${i%3===0?'var(--yellow)':i%3===1?'var(--blue)':'var(--navy)'};color:${i%3===0?'var(--navy)':i%3===1?'#fff':'var(--yellow)'}"><span>${w[0]}</span>${w[1]}</div>`).join('');
}

/* ---------- warm-up: spell today's words */
function buildWarm(){
  document.getElementById('warm').innerHTML=DATA.WARM.map((w,i)=>`<div class="wu" id="wu${i}"><span class="n">${i+1}</span>${pbtn('W_'+i)}<input id="wui${i}" autocomplete="off" spellcheck="false" aria-label="Word ${i+1}"><span class="ans"></span></div>`).join('');
}
function warmCheck(show){
  let sc=0; DATA.WARM.forEach((w,i)=>{ const el=document.getElementById('wui'+i), ok=norm(el.value)===norm(w);
    el.classList.toggle('ok',ok); el.classList.toggle('no',!ok&&el.value!==''); if(ok) sc++;
    if(show) document.querySelector('#wu'+i+' .ans').textContent=w; });
  document.getElementById('warmScore').textContent=sc+' / '+DATA.WARM.length;
}

/* ---------- vocabulary */
function buildVocab(){
  document.getElementById('vocab').innerHTML=DATA.VOCAB.map(([w,vi,col,ex],i)=>`<div class="vc"><div class="vh"><b>${esc(w)}</b><small>${esc(vi)}</small>${pbtn('V_'+i)}</div><div class="col">${esc(col)}</div><div class="ex">${esc(ex)}</div></div>`).join('');
}
/* ---------- frequency */
function buildFreq(){
  document.getElementById('freq').innerHTML=DATA.FREQ.map(([a,pc,ex],i)=>`<div class="fq"><div class="fbar"><i style="width:${Math.max(pc,4)}%"></i><span>${pc}%</span></div><div class="fw"><b>${esc(a)}</b>${pbtn('F_'+i)}</div><div class="fx">${esc(ex)}</div></div>`).join('');
}
/* ---------- collocation check */
function buildColl(){
  document.getElementById('coll').innerHTML=DATA.COLL.map(([s,opts,ans],i)=>`<div class="cq" id="cq${i}"><span class="n">${i+1}</span><div class="cs">${esc(s).replace('___','<span class="gap">___</span>')}</div><div class="co">${opts.map(o=>`<button class="opt" data-ci="${i}" data-o="${esc(o)}">${esc(o)}</button>`).join('')}</div>${pbtn('CO_'+i,'y')}</div>`).join('');
  document.querySelectorAll('[data-ci]').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.ci, box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1;
    const ans=DATA.COLL[i][2];
    box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); });
    if(b.dataset.o!==ans) b.classList.add('no');
    document.querySelector('#cq'+i+' .gap').textContent=ans;
  });
}
/* ---------- pronunciation */
function buildPron(){
  document.getElementById('sgroups').innerHTML=DATA.S_GROUPS.map(([snd,words],g)=>`<div class="sg"><div class="sgh"><b class="ipa">${esc(snd)}</b>${pbtn('PSG_'+g,'y')}</div><div class="sgw">${words.map((w,j)=>`<button class="lb2" data-a="PS_${g}_${j}">${esc(w).replace(/(e?s)(\b| up)/,'<u>$1</u>$2')}</button>`).join('')}</div></div>`).join('');
  document.getElementById('stress').innerHTML=DATA.STRESS.map((t,i)=>`<div class="stl">${pbtn('ST_'+i)}<span>${esc(t).replace(/\b([A-Z]{2,}(?: [A-Z]{2,})?)\b/g,'<b>$1</b>')}</span></div>`).join('');
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
    if(b.dataset.o!==ans) b.classList.add('no'); document.querySelector('#ld'+i+' .gap').textContent=ans;
  });
}
function listenCheck(){ DATA.LISTEN.times.forEach(([s,ans],i)=>{ const el=document.getElementById('lt'+i), ok=ans.map(norm).includes(norm(el.value)); el.classList.toggle('ok',ok); el.classList.toggle('no',!ok&&el.value!==''); document.getElementById('lta'+i).textContent=ans[0]; }); }
/* ---------- frames */
function buildFrames(){
  document.getElementById('frames').innerHTML=DATA.FRAMES.map(([f,exs],i)=>`<div class="frm"><div class="fh"><span class="n">${i+1}</span><b>${esc(f).replace(/___/g,'<span class="gap">___</span>')}</b></div>${exs.map((e,j)=>`<div class="fe">${pbtn(`FR_${i}_${j}`,'y')}<span>${esc(e)}</span></div>`).join('')}</div>`).join('');
  document.getElementById('linkers').innerHTML=DATA.LINKERS.map(l=>`<span class="lk">${esc(l)}</span>`).join('<span class="arr">→</span>');
}
/* ---------- questions & answers */
function buildQA(){
  document.getElementById('qa').innerHTML=DATA.QA.map(([q,as],i)=>`<div class="qap"><div class="qrow q"><span class="who">Q</span><span>${esc(q)}</span>${pbtn(`QA_${i}_q`)}</div>${as.map((a,j)=>`<div class="qrow a"><span class="who">${as.length>1?String.fromCharCode(97+j):'A'}</span><span>${esc(a)}</span>${pbtn(`QA_${i}_a${j}`,'y')}</div>`).join('')}</div>`).join('');
}
/* ---------- model dialogue */
function buildDialogue(){
  const sc=document.getElementById('script');
  sc.innerHTML=DATA.DIALOGUE.map(([w,t],i)=>`<div class="ln" data-ln="${i}"><span class="who ${w==='L'?'R':'S'}">${w}</span><span class="tx">${esc(t)}</span>${dl('DLG_'+i)}</div>`).join('');
  sc.querySelectorAll('.ln').forEach(l=>l.addEventListener('click',ev=>{ if(ev.target.closest('a')) return; const i=+l.dataset.ln; playQueue(['DLG_'+i],k=>hl(k<0?-1:i)); }));
  document.getElementById('dlgDl').innerHTML=dl('DLG_ALL','Full dialogue (MP3)');
  document.getElementById('dq').innerHTML=DATA.DLG_Q.map(([q,opts,ans],i)=>`<div class="lq"><span class="n">${i+1}</span><span class="qt">${esc(q)}</span><div class="co">${opts.map(o=>`<button class="opt" data-dq="${i}" data-o="${esc(o)}">${esc(o)}</button>`).join('')}</div></div>`).join('');
  document.querySelectorAll('[data-dq]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.dq, box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1; const ans=DATA.DLG_Q[i][2]; box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); }); if(b.dataset.o!==ans) b.classList.add('no'); });
}
function playDialogue(btn){ playQueue(DATA.DIALOGUE.map((_,i)=>'DLG_'+i),i=>{ hl(i); if(i>=0){ const el=document.querySelector('#script .ln[data-ln="'+i+'"]'); el&&el.scrollIntoView({block:'nearest'}); } },450,btn); }
/* ---------- interview */
function buildInterview(){
  document.getElementById('iv').innerHTML=`<tr><th>Ask your partner</th><th>Notes</th><th>Report</th></tr>`+DATA.INTERVIEW.map(([q,r],i)=>`<tr><td><b>${esc(q)}</b></td><td><input class="ivn" aria-label="Notes ${i+1}"></td><td class="rpt">${esc(r).replace(/___/g,'<span class="gap">___</span>')}</td></tr>`).join('');
}
/* ---------- free practice */
let sitCur=0;
function buildSit(){
  document.getElementById('sit').innerHTML=DATA.SITUATIONS.map((x,i)=>`<div class="sit2${i===sitCur?' on':''}" data-sit="${i}"><h4><span>${x.e}</span>${i+1}. ${esc(x.t)}</h4><div class="rl"><b>A</b><span>${esc(x.a)} — ${esc(x.goal)}</span></div><div class="rl b"><b>B</b><span>${esc(x.b)} — use your own routine or this card:</span></div><div class="card2">${x.card.map(c=>`<div>• ${esc(c)}</div>`).join('')}</div></div>`).join('');
  document.querySelectorAll('[data-sit]').forEach(c=>c.onclick=()=>{ sitCur=+c.dataset.sit; buildSit(); });
  const x=DATA.SITUATIONS[sitCur];
  const fill=t=>esc(t).replace(/\{([^}]+)\}/g,(m,k)=>`<span class="slot">${k}</span>`);
  document.getElementById('fpd').innerHTML=`<div class="hd">${x.e} ${esc(x.t)} · A = ${esc(x.a)} · B = ${esc(x.b)}</div>`+DATA.FP_LINES.map(([w,t])=>`<div class="ln2 ${w.toLowerCase()}"><span class="who">${w}</span><span>${fill(t)}</span></div>`).join('');
}
/* ---------- fluency */
function buildTalk(){
  document.getElementById('talk').innerHTML=DATA.TALK.map(([k,t],i)=>`<div class="tk2"><span class="tkk">${esc(k)}</span><span>${esc(t).replace(/___/g,'<span class="gap">___</span>')}</span></div>`).join('');
}
let tkRun=null;
function talkTimer(){
  const el=document.getElementById('tkTime'), bar=document.getElementById('tkBar'); let t=90; clearInterval(tkRun);
  const draw=()=>{ el.textContent=Math.floor(t/60)+':'+String(t%60).padStart(2,'0'); bar.style.width=(t/90*100)+'%'; }; draw();
  tkRun=setInterval(()=>{ t--; draw(); if(t<=0){ clearInterval(tkRun); el.textContent="Time's up!"; beep(); } },1000);
}
/* ---------- game: sentence scramble */
let scI=0, scPicked=[], scScore=0;
function shuffle(a){ a=a.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }
function scWords(s){ return s.replace(/[.?]$/,'').split(' '); }
function scLoad(){
  const s=DATA.SCRAMBLE[scI], words=scWords(s); let mixed=shuffle(words); let guard=0;
  while(mixed.join(' ')===words.join(' ')&&guard++<10) mixed=shuffle(words);
  scPicked=[];
  document.getElementById('scN').textContent=`${scI+1} / ${DATA.SCRAMBLE.length}`;
  document.getElementById('scOut').innerHTML=''; document.getElementById('scMsg').textContent='';
  document.getElementById('scPool').innerHTML=mixed.map((w,k)=>`<button class="chipw" data-k="${k}">${esc(w)}</button>`).join('');
  document.querySelectorAll('#scPool .chipw').forEach(b=>b.onclick=()=>{ if(b.disabled) return; b.disabled=true; scPicked.push(b.textContent); scDraw(); });
}
function scDraw(){ document.getElementById('scOut').innerHTML=scPicked.map((w,k)=>`<button class="chipw on" data-u="${k}">${esc(w)}</button>`).join('');
  document.querySelectorAll('#scOut .chipw').forEach(b=>b.onclick=()=>{ const w=scPicked.splice(+b.dataset.u,1)[0]; const src=[...document.querySelectorAll('#scPool .chipw')].find(x=>x.disabled&&x.textContent===w); if(src) src.disabled=false; scDraw(); }); }
function scCheck(){
  const s=DATA.SCRAMBLE[scI], ok=scPicked.join(' ')===scWords(s).join(' ');
  const m=document.getElementById('scMsg');
  m.innerHTML=ok?`✅ ${esc(s)}`:`❌ ${esc(s)}`; m.className='scmsg '+(ok?'good':'bad');
  if(ok) scScore++; document.getElementById('scScore').textContent='Score: '+scScore;
  play('SC_'+scI);
}

/* =========================================================
   INIT
   ========================================================= */
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud'); buildWarm(); buildVocab(); buildFreq(); buildColl(); buildPron(); buildListen(); buildFrames(); buildQA(); buildDialogue(); buildInterview(); buildSit(); buildTalk(); scLoad();
  // download links beside fixed play buttons
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL') return; if(b.closest('#coll,#sgroups,#qa,#frames,#freq')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
  const $=id=>document.getElementById(id);
  $('warmCheck').onclick=()=>warmCheck(false); $('warmShow').onclick=()=>warmCheck(true);
  $('fAll').onclick=e=>play('F_ALL',e.currentTarget);
  $('lCheck').onclick=listenCheck;
  $('lScript').onclick=e=>{ const p=$('lscr'), show=p.hidden; p.hidden=!show; e.currentTarget.textContent=show?'🙈 Hide script':'📜 Show script'; };
  $('lscr').innerHTML=`<div class="sh">📜 Script <span style="font-size:13px;color:var(--muted)">Source: ${esc(DATA.LISTEN.source)}</span></div>`+DATA.LISTEN.script.map(([w,t])=>`<div class="sl ${w}"><b>${w==='J'?'John':'Sarah'}</b><span>${esc(t)}</span></div>`).join('');
  $('dlgPlay').onclick=e=>playDialogue(e.currentTarget);
  $('dlgStop').onclick=stopAll;
  $('dlgScript').onclick=e=>{ const sc=$('script'); sc.classList.toggle('blur'); e.currentTarget.textContent=sc.classList.contains('blur')?'👁 Show script':'🙈 Hide script'; };
  $('tkStart').onclick=talkTimer; $('tkModel').onclick=e=>play('TALK',e.currentTarget);
  $('scCheck').onclick=scCheck; $('scNext').onclick=()=>{ scI=(scI+1)%DATA.SCRAMBLE.length; scLoad(); }; $('scReset').onclick=()=>{ scPicked=[]; scLoad(); };
  window.addEventListener('resize',fit); document.addEventListener('fullscreenchange',fit); fit();
  const h=parseInt((location.hash||'').slice(1)); go(isNaN(h)?0:h-1);
});
