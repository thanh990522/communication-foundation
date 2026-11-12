/* =========================================================
   S02 · Routines, Habits & Real Schedules — lesson activities
   (DATA is injected by build.py from content.py)
   ========================================================= */
const DATA = /*DATA_JSON*/;
const pbtn = (id,cls) => `<button class="play sm${cls?' '+cls:''}" data-a="${id}">${PLAY_SVG}</button>`;
const norm = s => String(s).toLowerCase().replace(/[\s\-–.,!?'’]+/g,'').trim();
function hl(i){ document.querySelectorAll('#script .ln').forEach((l,k)=>l.classList.toggle('now',k===i)); }


/* ---------- cover cloud */
function buildCloud(id,words){
  const el=document.getElementById(id); if(!el) return;
  words=words||[['⏰','7:00'],['☕','coffee'],['🚌','commute'],['💼','work'],['⏸','break'],['🌙','shift'],['📅','weekdays'],['🎉','weekends']];
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

/* ---------- flip cards */
document.addEventListener('click',e=>{
  if(e.target.closest('button,a,input')) return;
  const f=e.target.closest('[data-flip]'); if(f) f.classList.toggle('on');
});
function flipAll(btn,on){ btn.closest('.slide').querySelectorAll('[data-flip]').forEach(f=>f.classList.toggle('on',on)); }
/* ---------- collocation check */
let collN=0;
function collScore(){ document.getElementById('collScore').textContent=`✓ ${collN} / ${DATA.COLL.length}`; }
function buildColl(){
  document.querySelectorAll('[data-ci]').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.ci, box=b.parentElement; if(box.dataset.done) return; box.dataset.done=1;
    const ans=DATA.COLL[i][2];
    box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); });
    if(b.dataset.o!==ans) b.classList.add('no'); else collN++;
    document.querySelector('#cq'+i+' .gap').textContent=ans; collScore(); play('CO_'+i);
  });
}
function collReset(){ collN=0; collScore(); document.querySelectorAll('#coll2 .co, .coll2 .co').forEach(c=>{ delete c.dataset.done; c.querySelectorAll('.opt').forEach(o=>o.classList.remove('ok','no')); }); document.querySelectorAll('.coll2 .gap').forEach(g=>g.textContent='___'); }
/* ---------- sort it: /s/ /z/ /ɪz/ */
let sortSel=null, sortChecked=false;
function sortChip(i){ const [w]=DATA.SORT[i]; return `<span class="sw" draggable="true" data-sw="${i}">${esc(w)}<span class="ear" data-a="SW_${i}">🔊</span></span>`; }
function sortLoad(){
  sortSel=null; sortChecked=false;
  document.getElementById('pool').innerHTML=shuffle(DATA.SORT.map((_,i)=>i)).map(sortChip).join('');
  [0,1,2].forEach(g=>document.getElementById('bz'+g).innerHTML='');
  document.getElementById('sortScore').textContent=`— / ${DATA.SORT.length}`;
}
function sortPut(chip,g){ if(sortChecked) return; chip.classList.remove('sel','ok','no'); document.getElementById('bz'+g).appendChild(chip); sortSel=null; document.querySelectorAll('.bucket').forEach(b=>b.classList.remove('hot')); }
function sortInit(){
  const slide=document.getElementById('pool').closest('.slide');
  slide.addEventListener('click',e=>{
    if(e.target.closest('[data-a]')) return;
    const chip=e.target.closest('.sw');
    if(chip){ if(sortChecked) return;
      if(chip.parentElement.id==='pool'){ document.querySelectorAll('.sw.sel').forEach(c=>c!==chip&&c.classList.remove('sel')); chip.classList.toggle('sel'); sortSel=chip.classList.contains('sel')?chip:null; document.querySelectorAll('.bucket').forEach(b=>b.classList.toggle('hot',!!sortSel)); }
      else { document.getElementById('pool').appendChild(chip); }
      return; }
    const b=e.target.closest('.bucket'); if(b&&sortSel) sortPut(sortSel,+b.dataset.b);
  });
  slide.addEventListener('dragstart',e=>{ const c=e.target.closest&&e.target.closest('.sw'); if(c){ e.dataTransfer.setData('text/plain',c.dataset.sw); } });
  slide.querySelectorAll('.bucket').forEach(b=>{ b.addEventListener('dragover',e=>{ e.preventDefault(); b.classList.add('hot'); }); b.addEventListener('dragleave',()=>b.classList.remove('hot'));
    b.addEventListener('drop',e=>{ e.preventDefault(); const c=slide.querySelector(`.sw[data-sw="${e.dataTransfer.getData('text/plain')}"]`); if(c) sortPut(c,+b.dataset.b); }); });
}
function sortCheck(){
  let ok=0; document.querySelectorAll('#pool .sw').forEach(c=>c.classList.remove('ok','no'));
  [0,1,2].forEach(g=>document.querySelectorAll('#bz'+g+' .sw').forEach(c=>{ const good=DATA.SORT[+c.dataset.sw][1]===g; c.classList.toggle('ok',good); c.classList.toggle('no',!good); if(good) ok++; }));
  document.getElementById('sortScore').textContent=`✓ ${ok} / ${DATA.SORT.length}`;
}
function sortShow(){ document.querySelectorAll('.sw').forEach(c=>{ const g=DATA.SORT[+c.dataset.sw][1]; document.getElementById('bz'+g).appendChild(c); c.classList.remove('sel','no'); c.classList.add('ok'); }); sortChecked=true; document.getElementById('sortScore').textContent=`✓ ${DATA.SORT.length} / ${DATA.SORT.length}`; }
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
/* ---------- game: spin & translate */
let spRot=0, spUsed=[], spCur=-1, spScore=0, spTimer=null, spBusy=false;
function spInit(){
  const $=id=>document.getElementById(id), N=DATA.SPIN.length;
  const upd=()=>{ $('spN').textContent=`${spUsed.length} / ${N}`; $('spScore').textContent='Score: '+spScore; };
  const timer=()=>{ clearInterval(spTimer); let t=20; const bar=$('spBar'); bar.style.width='100%';
    spTimer=setInterval(()=>{ t-=.1; bar.style.width=Math.max(0,t/20*100)+'%'; if(t<=0){ clearInterval(spTimer); beep(); } },100); };
  $('spGo').onclick=()=>{
    if(spBusy) return; stopAll();
    const left=[...Array(N).keys()].filter(i=>!spUsed.includes(i));
    if(!left.length){ $('spCard').innerHTML='<div class="sph">🎉 All done!</div><div class="spvi">Score: '+spScore+' / '+N+'</div>'; return; }
    const i=left[Math.floor(Math.random()*left.length)], seg=360/N;
    const target=360-(i*seg+seg/2), cur=((spRot%360)+360)%360;
    spRot+= 360*5 + ((target-cur+360)%360);
    spBusy=true; ['spAns','spVi','spOk'].forEach(k=>$(k).disabled=true);
    const g=document.getElementById('whRot'); g.style.transform=`rotate(${spRot}deg)`;
    $('spCard').innerHTML='<div class="sph">🎡 …</div>';
    setTimeout(()=>{ spBusy=false; spCur=i; spUsed.push(i); document.getElementById('wseg'+i).classList.add('used'); upd();
      const [d,pr,an,hint]=DATA.SPIN[i];
      $('spCard').innerHTML=`<div class="sph"><span class="spn">${i+1}</span> ${d==='vi'?'🇻🇳 → 🇬🇧 Translate into English':'🇬🇧 → 🇻🇳 Dịch sang tiếng Việt'}</div><div class="spvi">${esc(pr)}</div><div class="sphint">💡 ${esc(hint)}</div><div class="spen" id="spEn" hidden>${esc(an)} <span class="spk" role="button" data-a="SA_${i}">🔊</span></div>`;
      $('spVi').textContent=d==='vi'?'🔊 Tiếng Việt':'🔊 English';
      ['spAns','spVi','spOk'].forEach(k=>$(k).disabled=false); timer(); play('SQ_'+i); },3300);
  };
  $('spVi').onclick=e=>{ if(spCur>=0) play('SQ_'+spCur,e.currentTarget); };
  $('spAns').onclick=e=>{ if(spCur<0) return; clearInterval(spTimer); const el=document.getElementById('spEn'); if(el) el.hidden=false; play('SA_'+spCur,e.currentTarget); };
  $('spOk').onclick=()=>{ if(spCur<0) return; spScore++; spCur=-1; $('spOk').disabled=true; upd(); };
  $('spReset').onclick=()=>{ stopAll(); clearInterval(spTimer); spUsed=[]; spCur=-1; spScore=0; document.querySelectorAll('.whsvg .used').forEach(x=>x.classList.remove('used'));
    $('spCard').innerHTML='<div class="sph">🎡 Spin the wheel!</div><div class="spvi">🇻🇳 → 🇬🇧 or 🇬🇧 → 🇻🇳 — translate with today\'s words &amp; structures.</div>'; $('spBar').style.width='0'; ['spAns','spVi','spOk'].forEach(k=>$(k).disabled=true); upd(); };
  upd();
}
/* ---------- game: sentence scramble (unused) */
let scI=0, scPicked=[], scScore=0;
function shuffle(a){ a=a.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }
function scWords(s){ return s.replace(/[.?]$/,'').split(' '); }
function scLoad(){
  const s=DATA.SCRAMBLE[scI], words=scWords(s); let mixed=shuffle(words); let guard=0;
  while(mixed.join(' ')===words.join(' ')&&guard++<10) mixed=shuffle(words);
  scPicked=[];
  document.getElementById('scN').textContent=`${scI+1} / ${DATA.SCRAMBLE.length}`;
  document.getElementById('scDots').innerHTML=DATA.SCRAMBLE.map((_,k)=>`<i class="${k===scI?'cur':k<scI?'done':''}"></i>`).join('');
  document.getElementById('scOut').innerHTML=''; document.getElementById('scMsg').textContent='';
  document.getElementById('scPool').innerHTML=mixed.map((w,k)=>`<button class="chipw" data-k="${k}">${esc(w)}</button>`).join('');
  document.querySelectorAll('#scPool .chipw').forEach(b=>b.onclick=()=>{ if(b.disabled) return; b.disabled=true; scPicked.push(b.textContent); scDraw(); });
}
function scDraw(){ document.getElementById('scOut').innerHTML=scPicked.map((w,k)=>`<button class="chipw on" data-u="${k}">${esc(w)}</button>`).join('');
  document.querySelectorAll('#scOut .chipw').forEach(b=>b.onclick=()=>{ const w=scPicked.splice(+b.dataset.u,1)[0]; const src=[...document.querySelectorAll('#scPool .chipw')].find(x=>x.disabled&&x.textContent===w); if(src) src.disabled=false; scDraw(); }); }
function scCheck(){
  const s=DATA.SCRAMBLE[scI], ok=scPicked.join(' ')===scWords(s).join(' ');
  const m=document.getElementById('scMsg');
  m.innerHTML=(ok?`✅ ${esc(s)}`:`❌ ${esc(s)}`)+` <span class="spk" role="button" data-a="SC_${scI}">🔊</span>`; m.className='scmsg '+(ok?'good':'bad');
  if(ok) scScore++; document.getElementById('scScore').textContent='Score: '+scScore;
  play('SC_'+scI);
}

/* =========================================================
   INIT
   ========================================================= */
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud'); buildCloud('cloud2',[['☕','coffee'],['📊','usually'],['🚌','commute'],['👄','/ɪz/'],['⏸','break'],['🌙','shift'],['📅','weekdays'],['🎉','weekends']]); buildWarm(); buildColl(); sortInit(); sortLoad(); buildListen(); buildFrames(); buildQA(); buildDialogue(); buildInterview(); buildSit(); buildTalk(); spInit();
  // download links beside fixed play buttons
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL') return; if(b.closest('.coll2,.sgroups2,#qa,#frames,.freq2,.fgrid,.ladder,.chal,.pool,.buckets,.stressbox')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
  const $=id=>document.getElementById(id);
  $('warmCheck').onclick=()=>warmCheck(false); $('warmShow').onclick=()=>warmCheck(true);
  $('fAll').onclick=e=>play('F_ALL',e.currentTarget);
  document.querySelectorAll('[data-flipall]').forEach(b=>b.onclick=()=>flipAll(b,true));
  document.querySelectorAll('[data-flipreset]').forEach(b=>b.onclick=()=>flipAll(b,false));
  document.querySelectorAll('[data-rep]').forEach(b=>b.onclick=()=>repeatQueue(b));
  $('collReset').onclick=collReset;
  $('sortCheck').onclick=sortCheck; $('sortShow').onclick=sortShow; $('sortReset').onclick=sortLoad;
  $('lCheck').onclick=listenCheck;
  $('lScript').onclick=e=>{ const p=$('lscr'), show=p.hidden; p.hidden=!show; e.currentTarget.textContent=show?'🙈 Hide script':'📜 Show script'; };
  $('lscr').innerHTML=`<div class="sh">📜 Script <span style="font-size:13px;color:var(--muted)">Source: ${esc(DATA.LISTEN.source)}</span></div>`+DATA.LISTEN.script.map(([w,t])=>`<div class="sl ${w}"><b>${w==='J'?'John':'Sarah'}</b><span>${esc(t)}</span></div>`).join('');
  $('dlgPlay').onclick=e=>playDialogue(e.currentTarget);
  $('dlgStop').onclick=stopAll;
  $('dlgScript').onclick=e=>{ const sc=$('script'); sc.classList.toggle('blur'); e.currentTarget.textContent=sc.classList.contains('blur')?'👁 Show script':'🙈 Hide script'; };
  $('tkStart').onclick=talkTimer; $('tkModel').onclick=e=>play('TALK',e.currentTarget);
  window.addEventListener('resize',fit); document.addEventListener('fullscreenchange',fit); fit();
  const h=parseInt((location.hash||'').slice(1)); go(isNaN(h)?0:h-1);
});
