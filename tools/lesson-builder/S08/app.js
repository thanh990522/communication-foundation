/* =========================================================
   S08 · Shopping, Sizes, Returns & Refunds — lesson activities
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

/* ---------- warm-up: speed naming */
function clothesInit(){
  const cards=[...document.querySelectorAll('.clc')], N=cards.length; let run=null;
  const cnt=()=>document.getElementById('clN').textContent=`${cards.filter(c=>c.classList.contains('on')).length} / ${N}`;
  const stop=()=>{ clearTimeout(run); run=null; cards.forEach(c=>c.classList.remove('hot')); document.getElementById('clGo').textContent='⚡ Speed round'; };
  cards.forEach(c=>c.addEventListener('click',e=>{ if(e.target.closest('button')) return; c.classList.add('on'); cnt(); }));
  document.getElementById('clAll').onclick=()=>{ stop(); cards.forEach(c=>c.classList.add('on')); cnt(); };
  document.getElementById('clReset').onclick=()=>{ stop(); cards.forEach(c=>c.classList.remove('on')); cnt(); };
  document.getElementById('clGo').onclick=e=>{ if(run){ stop(); return; }
    cards.forEach(c=>c.classList.remove('on','hot')); cnt(); const order=shuffle([...Array(N).keys()]); let k=0; e.currentTarget.textContent='⏹ Stop';
    const step=()=>{ if(k>0){ const p=cards[order[k-1]]; p.classList.remove('hot'); p.classList.add('on'); cnt(); }
      if(k>=N){ stop(); return; } cards[order[k]].classList.add('hot'); k++; run=setTimeout(step,3000); };
    step(); };
}
/* ---------- fitting room sliders */
function fitInit(){
  const $=id=>document.getElementById(id);
  const sz=()=>{ const i=+$('frSize').value, [s,t,v]=DATA.SIZES[i]; $('frShirt').style.transform=`scale(${[.6,.8,1,1.22,1.42][i]})`;
    $('frSt').textContent=t; $('frSv').textContent=v; $('frSp').dataset.a='FS_'+i; $('frShirt').className='frshirt '+(i===2?'good':'bad'); };
  const pr=()=>{ const i=+$('frPrice').value, [p,t]=DATA.PRICES[i]; $('prTag').textContent='£'+p; $('prTag').className='prtag '+(p<=DATA.BUDGET?'good':'bad'); $('prSt').textContent=t; $('prSp').dataset.a='FP_'+i; };
  $('frSize').addEventListener('input',sz); $('frPrice').addEventListener('input',pr); sz(); pr();
}
/* ---------- contrastive stress cards */
function contrastInit(){
  document.querySelectorAll('[data-ct]').forEach(c=>c.addEventListener('click',e=>{ if(e.target.closest('button')) return; c.classList.add('on'); }));
  document.getElementById('ctAll').onclick=()=>document.querySelectorAll('[data-ct]').forEach(c=>c.classList.add('on'));
  document.getElementById('ctReset').onclick=()=>document.querySelectorAll('[data-ct]').forEach(c=>c.classList.remove('on'));
}
/* ---------- two linked role-plays */
function rolePlayInit(){
  const $=id=>document.getElementById(id); let cur=-1, stage=1;
  const show=st=>{ stage=st; $('rpS1').classList.toggle('on',st===1); $('rpS2').classList.toggle('on',st===2); $('rpNext').textContent=st===1?'Next step → Return it':'↺ Back to step 1'; };
  $('rpNew').onclick=()=>{ let i; do{ i=Math.floor(Math.random()*DATA.SCENARIOS.length); }while(i===cur&&DATA.SCENARIOS.length>1); cur=i;
    const [em,item,size,col,bud,prob]=DATA.SCENARIOS[i];
    $('rpB1').innerHTML=`<div class="rpe">${em}</div><div class="rpl"><p>🛍 You want to buy <b>${esc(item)}</b>.</p><p>📏 Size: <b>${esc(size)}</b> · 🎨 Colour: <b>${esc(col)}</b></p><p>👛 Your budget: <b>£${bud}</b></p><p class="muted">Assistant: you have it in <b>${esc(DATA.COLOURS[(DATA.COLOURS.indexOf(col)+1)%DATA.COLOURS.length])}</b> only. Offer a discount!</p></div>`;
    $('rpB2').innerHTML=`<div class="rpe">${em}💔</div><div class="rpl"><p>🔁 One week later…</p><p>😟 Problem: <b>${esc(prob)}</b></p><p>🧾 You have the receipt.</p><p class="muted">Customer: refund or exchange? Tell the story with the linkers!</p></div>`;
    show(1); const c=$('rpS1'); c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); };
  $('rpNext').onclick=()=>{ if(cur<0) return; show(stage===1?2:1); };
}
/* ---------- real-life task: online shop chat */
function shopInit(){
  const $=id=>document.getElementById(id), body=$('ocBody');
  const add=(t,who)=>{ body.insertAdjacentHTML('beforeend',`<div class="om ${who}">${esc(t)}</div>`); body.scrollTop=body.scrollHeight; };
  const send=()=>{ const q=$('ocIn').value.trim(); if(!q) return; add(q,'me'); $('ocIn').value='';
    const low=q.toLowerCase(), hits=DATA.BOT.filter(([kw])=>kw.some(k=>low.includes(k)));
    setTimeout(()=>{ if(!hits.length){ add("Sorry, I don't understand. You can ask about size, colour, price or returns. 🙂",'bot'); return; }
      const seen=new Set(); hits.forEach(([kw,r,key])=>{ if(seen.has(r)) return; seen.add(r); add(r,'bot'); const c=$('oc_'+key); if(c&&!c.classList.contains('ok')){ c.classList.add('ok'); c.querySelector('i').textContent='☑'; } });
      if(document.querySelectorAll('.ocl.ok').length===4) add('🎉 Great questions! Thank you for shopping with us.','bot'); },500); };
  $('ocSend').onclick=send; $('ocIn').addEventListener('keydown',e=>{ if(e.key==='Enter') send(); });
}
/* ---------- game: returns desk */
function deskInit(){
  const $=id=>document.getElementById(id), N=DATA.CASES.length; let r=-1, score=0, done=true, order=shuffle([...Array(N).keys()]);
  const upd=()=>{ $('rdN').textContent=`Customer ${Math.max(r+1,0)} / ${N}`; $('rdScore').textContent='Score: '+score; };
  const opts=[...document.querySelectorAll('.rdo')];
  $('rdGo').onclick=()=>{ if(!done) return; if(r>=N-1){ $('rdCard').innerHTML=`<div class="rde">🏆</div><div class="rdt">Finished! Score: ${score} / ${N}</div>`; r=-1; score=0; order=shuffle(order); $('rdGo').textContent='Next customer →'; return; }
    r++; done=false; const [em,item,say,rc,days]=DATA.CASES[order[r]]; opts.forEach(o=>o.classList.remove('ok','no')); $('rdSay').hidden=true; upd();
    $('rdCard').innerHTML=`<div class="rde">${em}</div><div class="rdt">“${esc(say)}” <button class="play sm" data-a="RD_${order[r]}">${PLAY_SVG}</button></div><div class="rdi"><span class="${rc?'g':'b'}">🧾 ${rc?'receipt ✓':'no receipt ✗'}</span><span>📅 bought ${days} days ago</span></div>`; };
  opts.forEach(o=>o.onclick=()=>{ if(done||r<0) return; done=true; const ans=DATA.CASES[order[r]][5], k=+o.dataset.rd;
    opts[ans].classList.add('ok'); if(k!==ans) o.classList.add('no'); else score++; upd();
    $('rdSay').innerHTML=`<button class="play sm" data-a="RS_${ans}">${PLAY_SVG}</button> 🧑‍💼 “${esc(DATA.DESK_SAY[ans])}”`; $('rdSay').hidden=false;
    $('rdGo').textContent=r>=N-1?'🏆 See score':'Next customer →'; });
  $('rdAgain').onclick=()=>{ if(r>=0) play('RD_'+order[r],$('rdAgain')); };
  upd();
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=90;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['👕','size'],['📏','fit'],['🧾','receipt'],['🔁','exchange'],['💷','refund'],['🏷','discount'],['💔','damaged'],['😍','suits you']]);
  buildCloud('cloud2',[['🚚','delivery'],['🔧','repair'],['⚠️','issue'],['☎️','customer service'],['🔁','replacement'],['💳','charge'],['🟢','available'],['✅','confirm']]);
  clothesInit(); fitInit(); const mqReset=setupMC('mq',DATA.MAPQ,'mqScore','MQ'); contrastInit(); buildListen(); buildDialogue(); setupCard(); rolePlayInit(); shopInit(); deskInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL'||id==='EL2') return; if(b.closest('.clgrid,.fgrid,.frcap,.gfbox,.wq,.ctgrid,.fsbox,.sgrid,.rdc,.lftx')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
  const $=id=>document.getElementById(id);
  $('mqReset').onclick=mqReset;
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
