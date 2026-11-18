/* =========================================================
   S09 · Everyday Services & Polite Requests — lesson activities
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

/* ---------- warm-up: who do you call? */
function whoCallInit(){
  const $=id=>document.getElementById(id); let sel=-1, n=0; const N=DATA.PROBLEMS.length;
  const sc=()=>$('wpScore').textContent=`✓ ${n} / ${N}`;
  document.querySelectorAll('[data-wp]').forEach(b=>b.onclick=()=>{ if(b.classList.contains('done')) return; document.querySelectorAll('.wpr.sel').forEach(x=>x.classList.remove('sel')); b.classList.add('sel'); sel=+b.dataset.wp; });
  document.querySelectorAll('[data-wb]').forEach(bin=>bin.onclick=()=>{ if(sel<0) return; const b=document.querySelector(`[data-wp="${sel}"]`), [em,t,s]=DATA.PROBLEMS[sel];
    if(bin.dataset.wb===s){ b.classList.remove('sel'); b.classList.add('done'); $('wbl'+s).insertAdjacentHTML('beforeend',`<span class="wbi">${em} ${esc(t)}</span>`); n++; sc(); sel=-1; }
    else { bin.classList.add('shake'); setTimeout(()=>bin.classList.remove('shake'),450); } });
  $('wpReset').onclick=()=>{ sel=-1; n=0; sc(); document.querySelectorAll('.wpr').forEach(b=>b.classList.remove('sel','done')); document.querySelectorAll('.wbl').forEach(l=>l.innerHTML=''); };
}
/* ---------- shape of a call (step reveal) */
function callShapeInit(){
  const $=id=>document.getElementById(id), st=[...document.querySelectorAll('.cst2')]; let k=0;
  const draw=()=>{ st.forEach((s,i)=>{ s.classList.toggle('on',i<k); s.classList.toggle('now',i===k-1); }); $('csNext').textContent=k>=st.length?'✓ Done':'Next step →'; };
  $('csNext').onclick=()=>{ if(k<st.length){ k++; draw(); } };
  $('csAll').onclick=()=>{ k=st.length; draw(); }; $('csReset').onclick=()=>{ k=0; draw(); }; draw();
}
/* ---------- there seems to be (click to soften) */
function thereInit(){
  document.querySelectorAll('[data-th]').forEach(c=>c.addEventListener('click',e=>{ if(e.target.closest('button')) return; c.classList.add('on'); }));
  document.getElementById('thAll').onclick=()=>document.querySelectorAll('[data-th]').forEach(c=>c.classList.add('on'));
  document.getElementById('thReset').onclick=()=>document.querySelectorAll('[data-th]').forEach(c=>c.classList.remove('on'));
}
/* ---------- politeness meter */
function meterInit(){
  const $=id=>document.getElementById(id); let n=0, done=0; const N=DATA.POLITE.length;
  const draw=()=>{ $('pmScore').textContent=`✓ ${n} / ${N}`; $('pmFill').style.height=(done?n/done*100:0)+'%'; };
  document.querySelectorAll('[data-pm]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.pm, row=$('pm'+i); if(row.dataset.done) return; row.dataset.done=1; done++;
    const a=DATA.POLITE[i][1]; row.querySelectorAll('.opt').forEach(o=>{ if(+o.dataset.o===a) o.classList.add('ok'); }); if(+b.dataset.o!==a) b.classList.add('no'); else n++; draw(); });
  $('pmReset').onclick=()=>{ n=0; done=0; document.querySelectorAll('.pmr').forEach(r=>{ delete r.dataset.done; r.querySelectorAll('.opt').forEach(o=>o.classList.remove('ok','no')); }); draw(); }; draw();
}
/* ---------- find the stress */
function stressInit(){
  const $=id=>document.getElementById(id);
  document.querySelectorAll('.swd').forEach(b=>b.onclick=()=>{ if(b.closest('.swr').dataset.done) return; b.classList.toggle('mk'); });
  $('swCheck').onclick=()=>{ let ok=0, tot=0; document.querySelectorAll('.swr').forEach(r=>{ r.dataset.done=1; r.querySelectorAll('.swd').forEach(b=>{ const st=b.dataset.st==='1', mk=b.classList.contains('mk');
      if(st){ tot++; b.textContent=b.textContent.toUpperCase(); b.classList.add(mk?'hit':'miss'); if(mk) ok++; } else if(mk) b.classList.add('extra'); }); });
    $('swScore').textContent=`🎯 ${ok} / ${tot} strong words`; };
  $('swReset').onclick=()=>{ document.querySelectorAll('.swr').forEach(r=>{ delete r.dataset.done; r.querySelectorAll('.swd').forEach(b=>{ b.classList.remove('mk','hit','miss','extra'); if(b.dataset.st==='1') b.textContent=b.textContent.toLowerCase(); }); }); $('swScore').textContent='🎯 ?'; };
}
/* ---------- 2-minute service call */
function serviceCallInit(){
  const $=id=>document.getElementById(id); let cur=-1;
  $('scNew').onclick=()=>{ let i; do{ i=Math.floor(Math.random()*DATA.CALLS.length); }while(i===cur&&DATA.CALLS.length>1); cur=i; const [em,prob,want,opts,note]=DATA.CALLS[i];
    const c=$('scCaller'); c.innerHTML=`<div class="rce">${em}</div><div class="rct">Caller</div><div class="rcx">⚠️ ${esc(prob)}<br>🙏 ${esc(want)}</div><div class="rcn">Call ${i+1} / ${DATA.CALLS.length}</div>`; c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop');
    $('scAgent').innerHTML=`<div class="scl">Options you can offer:</div>${opts.map((o,k)=>`<div class="sco"><b>${k+1}</b>${esc(o)}</div>`).join('')}<div class="scn">💳 ${esc(note)}</div><div class="scl">Finally: confirm the details!</div>`;
    $('scAgent').classList.remove('hid'); $('scHide').textContent='🙈 Hide'; document.querySelectorAll('.stg input').forEach(x=>x.checked=false); };
  $('scHide').onclick=e=>{ const a=$('scAgent'); a.classList.toggle('hid'); e.currentTarget.textContent=a.classList.contains('hid')?'👁 Show':'🙈 Hide'; };
}
/* ---------- 45-second voice message recorder */
function voiceInit(){
  const $=id=>document.getElementById(id), T=45; let rec=null, chunks=[], tm=null, left=T, stream=null;
  const IDEAS=['📦 Your parcel is a week late.','📺 Your new TV does not work.','💳 There is an extra charge on your bill.','🌐 Your internet is very slow.','🛋 The driver brought the wrong sofa.','❄️ Your fridge is not cold. Book a repair.'];
  $('vmIdea').onclick=()=>{ $('vmIdeaTx').textContent=IDEAS[Math.floor(Math.random()*IDEAS.length)]; };
  const draw=()=>{ $('vmTime').textContent='0:'+String(left).padStart(2,'0'); $('vmBar').style.width=(left/T*100)+'%'; };
  const stop=()=>{ clearInterval(tm); if(rec&&rec.state!=='inactive') rec.stop(); $('vmRec').disabled=false; $('vmStop').disabled=true; };
  $('vmRec').onclick=async()=>{
    if(!navigator.mediaDevices||!window.MediaRecorder){ $('vmSt').textContent='⚠️ This browser cannot record. Try Chrome, or use your phone voice recorder.'; return; }
    try{ stream=await navigator.mediaDevices.getUserMedia({audio:true}); }catch(err){ $('vmSt').textContent='⚠️ Please allow the microphone, then try again.'; return; }
    chunks=[]; rec=new MediaRecorder(stream); rec.ondataavailable=e=>chunks.push(e.data);
    rec.onstop=()=>{ stream.getTracks().forEach(t=>t.stop()); const url=URL.createObjectURL(new Blob(chunks,{type:rec.mimeType||'audio/webm'}));
      $('vmAudio').src=url; $('vmAudio').hidden=false; $('vmDl').href=url; $('vmDl').hidden=false; $('vmSt').textContent=`✅ Done! You spoke for ${T-left} seconds. Listen: is it clear and polite?`; };
    rec.start(); left=T; draw(); $('vmRec').disabled=true; $('vmStop').disabled=false; $('vmSt').textContent='🔴 Recording… speak now!'; $('vmAudio').hidden=true; $('vmDl').hidden=true;
    tm=setInterval(()=>{ left--; draw(); if(left<=0){ stop(); beep(); } },1000); };
  $('vmStop').onclick=stop; draw();
}
/* ---------- game: quick replies */
function quickInit(){
  const $=id=>document.getElementById(id), N=DATA.REPLIES.length; let r=-1, score=0, streak=0, done=true, order=shuffle([...Array(N).keys()]), tm=null, t=10;
  const upd=()=>{ $('qrN').textContent=`Call ${Math.max(r+1,0)} / ${N}`; $('qrScore').textContent=`Score: ${score} · 🔥 ${streak}`; $('qrT').textContent='⏱ '+t; };
  const finish=k=>{ clearInterval(tm); done=true; const [q,opts,a]=DATA.REPLIES[order[r]];
    $('qrO').querySelectorAll('.opt').forEach(o=>{ if(+o.dataset.o===a) o.classList.add('ok'); else if(+o.dataset.o===k) o.classList.add('no'); });
    if(k===a){ score++; streak++; } else streak=0; if(k===-1) $('qrT').textContent="⏱ Time's up!"; else upd();
    $('qrScore').textContent=`Score: ${score} · 🔥 ${streak}`; $('qrGo').textContent=r>=N-1?'🏆 See score':'Next call →'; };
  $('qrGo').onclick=()=>{ if(!done) return; if(r>=N-1){ $('qrQ').innerHTML=`<b>🏆 Finished!</b><span>Score: ${score} / ${N}</span>`; $('qrO').innerHTML=''; r=-1; score=0; streak=0; order=shuffle(order); $('qrGo').textContent='Next call →'; return; }
    r++; done=false; t=10; const [q,opts]=DATA.REPLIES[order[r]];
    $('qrQ').innerHTML=`<b>📞 “${esc(q)}”</b><span><button class="play sm" data-a="QR_${order[r]}">${PLAY_SVG}</button> Choose the best reply — then say it!</span>`;
    $('qrO').innerHTML=shuffle(opts.map((o,k)=>[o,k])).map(([o,k])=>`<button class="opt" data-o="${k}">${esc(o)}</button>`).join('');
    $('qrO').querySelectorAll('.opt').forEach(o=>o.onclick=()=>{ if(!done) finish(+o.dataset.o); }); upd();
    clearInterval(tm); tm=setInterval(()=>{ t--; $('qrT').textContent='⏱ '+t; if(t<=0) finish(-1); },1000); };
  $('qrAgain').onclick=()=>{ if(r>=0) play('QR_'+order[r],$('qrAgain')); };
  upd();
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=120;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['🚚','delivery'],['🔧','repair'],['⚠️','issue'],['☎️','customer service'],['📦','replacement'],['💳','charge'],['🟢','available'],['✅','confirm']]);
  buildCloud('cloud2',[['🎟','attend'],['🛒','visit'],['🏨','stay'],['🏠','return'],['😊','enjoy'],['😫','exhausted'],['⭐','memorable'],['🎉','event']]);
  whoCallInit(); callShapeInit(); thereInit(); meterInit(); stressInit(); buildListen(); buildDialogue(); setupCard(); serviceCallInit(); voiceInit(); quickInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL'||id==='EL2') return; if(b.closest('.fgrid,.csflow,.gfbox,.thgrid,.swbox2,.sgrid,.qrq')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
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
