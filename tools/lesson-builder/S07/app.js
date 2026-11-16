/* =========================================================
   S07 · Eating Out: From Menu to Bill — lesson activities
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
/* ---------- warm-up: who says it? */
function whoInit(){
  let n=0; const sc=()=>document.getElementById('wsScore').textContent=`✓ ${n} / ${DATA.WHO.length}`;
  document.querySelectorAll('[data-ws]').forEach(b=>b.onclick=()=>{ const i=+b.dataset.ws, box=document.getElementById('ws'+i); if(box.dataset.done) return; box.dataset.done=1;
    const ans=DATA.WHO[i][1]; box.querySelectorAll('.opt').forEach(x=>{ if(x.dataset.o===ans) x.classList.add('ok'); }); if(b.dataset.o!==ans) b.classList.add('no'); else n++; box.classList.add(ans==='W'?'isw':'isc'); sc(); });
  document.getElementById('wsReset').onclick=()=>{ n=0; sc(); document.querySelectorAll('.wsc').forEach(w=>{ delete w.dataset.done; w.classList.remove('isw','isc'); w.querySelectorAll('.opt').forEach(x=>x.classList.remove('ok','no')); }); };
}
/* ---------- make it polite */
function politeInit(){
  document.querySelectorAll('[data-pl]').forEach(c=>c.addEventListener('click',e=>{ if(e.target.closest('button')) return; c.classList.toggle('on'); }));
  document.querySelectorAll('[data-plall]').forEach(b=>b.onclick=()=>document.querySelectorAll('[data-pl]').forEach(c=>c.classList.add('on')));
  document.querySelectorAll('[data-plreset]').forEach(b=>b.onclick=()=>document.querySelectorAll('[data-pl]').forEach(c=>c.classList.remove('on')));
}
const nm2=v=>String(v).toLowerCase().replace(/[^a-z0-9]/g,'');
/* ---------- waiter's pad */
function padInit(){
  const $=id=>document.getElementById(id), menu=$('menu2'), N=DATA.TAKE.length; let r=-1, sel=new Set(), done=true;
  const draw=()=>{ $('tkList').innerHTML=sel.size?[...sel].map(d=>`<div class="cto"><span>✓ ${esc(d)}</span></div>`).join(''):'<span class="muted">Click the dishes you hear on the menu.</span>';
    menu.querySelectorAll('.mni').forEach(b=>b.classList.toggle('sel',sel.has(b.dataset.dish))); $('tkN').textContent=`Customer ${Math.max(r+1,0)} / ${N}`; };
  menu.querySelectorAll('.mni').forEach(b=>b.onclick=()=>{ if(done) return; const d=b.dataset.dish; sel.has(d)?sel.delete(d):sel.add(d); draw(); });
  $('tkGo').onclick=()=>{ if(!done){ play('TK_'+r,$('tkGo')); return; } if(r>=N-1) r=-1; r++; done=false; sel=new Set(); $('tkWo').value=''; $('tkTx').hidden=true; $('tkTx').textContent='“'+DATA.TAKE[r][0]+'”';
    menu.querySelectorAll('.mni').forEach(b=>b.classList.remove('ok','no')); draw(); play('TK_'+r,$('tkGo')); };
  $('tkAgain').onclick=()=>{ if(r>=0) play('TK_'+r,$('tkAgain')); };
  $('tkShow').onclick=()=>{ if(r>=0) $('tkTx').hidden=!$('tkTx').hidden; };
  $('tkCheck').onclick=()=>{ if(r<0) return; done=true; const [t,ds,wo]=DATA.TAKE[r];
    menu.querySelectorAll('.mni').forEach(b=>{ const d=b.dataset.dish, need=ds.includes(d); if(need) b.classList.add('ok'); else if(sel.has(d)) b.classList.add('no'); });
    const okD=ds.length===sel.size&&ds.every(d=>sel.has(d)), okW=nm2($('tkWo').value)===nm2(wo)||(!wo&&!$('tkWo').value.trim());
    $('tkList').innerHTML=`<div class="cto ${okD&&okW?'':'bad'}"><span>${okD&&okW?'✅ Perfect order!':'❌ Check: '+esc(ds.join(', '))+(wo?' · without '+esc(wo):'')}</span></div>`; $('tkTx').hidden=false;
    $('tkGo').textContent=r>=N-1?'↺ Start again':'▶ Listen to the next customer'; };
  draw();
}
/* ---------- split the bill */
function billInit(){
  const $=id=>document.getElementById(id), num=v=>parseFloat(String(v).replace(/[£,\s]/g,''));
  const check=show=>DATA.BILL_Q.forEach(([l,v],i)=>{ const el=$('bq'+i), x=num(el.value), good=Math.abs(x-v)<0.005;
    el.classList.toggle('ok',good); el.classList.toggle('no',!good&&el.value!==''); $('bqa'+i).textContent=show?'£'+v.toFixed(2):''; });
  $('bqCheck').onclick=()=>check(false); $('bqShow').onclick=()=>check(true);
}
/* ---------- role-play cards */
let rcCur=-1;
function setupRC(){ document.getElementById('rcDraw').onclick=()=>{ let i; do{ i=Math.floor(Math.random()*DATA.ROLECARDS.length); }while(i===rcCur&&DATA.ROLECARDS.length>1); rcCur=i;
  const [em,t,x]=DATA.ROLECARDS[i]; const c=document.getElementById('rcard'); c.innerHTML=`<div class="rce">${em}</div><div class="rct">${esc(t)}</div><div class="rcx">${esc(x)}</div><div class="rcn">Card ${i+1} / ${DATA.ROLECARDS.length}</div>`; c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); }; }
/* ---------- my order builder */
function orderInit(){
  const $=id=>document.getElementById(id), menu=$('menu4'); let pick=[];
  const art=d=>/^[aeiou]/i.test(d)?'an':'a';
  const draw=()=>{ const by=s=>pick.filter(p=>p.sec===s).map(p=>p.d.toLowerCase());
    const st=by('Starters'), mc=by('Main courses'), sd=by('Side dishes'), ds=by('Desserts'), dr=by('Drinks'), wo=$('moWo').value.trim();
    const join=a=>a.length<2?a.join(''):a.slice(0,-1).join(', ')+' and '+a[a.length-1];
    const lines=[];
    if(st.length) lines.push(`To start with, I'll have the ${join(st)}.`);
    if(mc.length) lines.push(`For the main course, I'd like the ${join(mc)}${sd.length?' with '+join(sd):''}.`); else if(sd.length) lines.push(`I'd like ${join(sd)}.`);
    if(wo&&(mc.length||st.length)) lines.push(`Could I have it without ${wo}, please?`);
    if(ds.length) lines.push(`For dessert, I'll have the ${join(ds)}.`);
    if(dr.length) lines.push(`And ${dr.map(d=>art(d)+' '+d).join(' and ')}, please.`);
    $('moTxt').innerHTML=lines.length?lines.map(l=>`<p>${esc(l)}</p>`).join(''):'<span class="muted">Click dishes on the menu.</span>';
    const tot=pick.reduce((a,p)=>a+p.pr,0); $('moTot').textContent='£'+tot.toFixed(2)+(tot?` + 10% = £${(tot*1.1).toFixed(2)}`:'');
    menu.querySelectorAll('.mni').forEach(b=>b.classList.toggle('sel',pick.some(p=>p.d===b.dataset.dish))); };
  menu.querySelectorAll('.mni').forEach(b=>b.onclick=()=>{ const d=b.dataset.dish, k=pick.findIndex(p=>p.d===d); if(k>=0) pick.splice(k,1); else pick.push({d,pr:+b.dataset.pr,sec:b.dataset.sec}); draw(); });
  $('moWo').addEventListener('input',draw); $('moReset').onclick=()=>{ pick=[]; $('moWo').value=''; draw(); }; draw();
}
/* ---------- game: what's the total? */
function totalInit(){
  const $=id=>document.getElementById(id), N=DATA.TOTALS.length; let r=-1, score=0, done=true, order=[];
  const upd=()=>{ $('gtN').textContent=`Round ${Math.max(r+1,0)} / ${N}`; $('gtScore').textContent='Score: '+score; };
  $('gtGo').onclick=()=>{ if(!done){ play('GT_'+order[r],$('gtGo')); return; } if(r>=N-1){ $('gtQ').innerHTML=`<b>🏆 Finished!</b><span>Score: ${score} / ${N}</span>`; return; }
    r++; done=false; $('gtIn').value=''; $('gtIn').classList.remove('ok','no'); $('gtTx').hidden=true; $('gtTx').textContent='“'+DATA.TOTALS[order[r]][0]+'”'; upd();
    $('gtQ').innerHTML='<b>🎧 Listen…</b><span>Add up the prices on the menu.</span>'; play('GT_'+order[r],$('gtGo')); };
  $('gtAgain').onclick=()=>{ if(r>=0) play('GT_'+order[r],$('gtAgain')); };
  $('gtCheck').onclick=()=>{ if(done||r<0) return; done=true; const v=DATA.TOTALS[order[r]][1], x=parseFloat(String($('gtIn').value).replace(/[£,\s]/g,'')), good=Math.abs(x-v)<0.005;
    if(good) score++; $('gtIn').classList.add(good?'ok':'no'); upd(); $('gtTx').hidden=false;
    $('gtQ').innerHTML=good?`<b>✅ Correct!</b><span>The total is £${v.toFixed(2)}.</span>`:`<b>❌ Not quite</b><span>The total is £${v.toFixed(2)}.</span>`;
    $('gtGo').textContent=r>=N-1?'🏆 See score':'▶ Listen · next order'; };
  order=shuffle([...Array(N).keys()]); upd();
}

/* =========================================================
   INIT
   ========================================================= */
window.TK_SECS=90;
window.addEventListener('DOMContentLoaded',()=>{
  toBlobUrls();
  buildCloud('cloud',[['🍽','menu'],['🥣','starter'],['🍗','main course'],['🍟','side dish'],['👍','recommend'],['🥜','allergy'],['🧾','bill'],['➗','split']]);
  buildCloud('cloud2',[['👕','size'],['📏','fit'],['🧾','receipt'],['🔁','exchange'],['💷','refund'],['🏷','discount'],['💔','damaged'],['👌','suits you']]);
  whoInit(); politeInit(); padInit(); buildListen(); buildDialogue(); setupCard(); billInit(); setupRC(); orderInit(); totalInit();
  document.querySelectorAll('button[data-a]').forEach(b=>{ const id=b.dataset.a; if(!AUDIO[id]||id==='EL') return; if(b.closest('.wsgrid,.fgrid,.menu,.plgrid,.pgr,.lkbox,.sgrid')) return; if(b.nextElementSibling&&b.nextElementSibling.classList.contains('dl')) return; b.insertAdjacentHTML('afterend',dl(id)); });
  const $=id=>document.getElementById(id);
  document.querySelectorAll('[data-flipall]').forEach(b=>b.onclick=()=>flipAll(b,true));
  document.querySelectorAll('[data-flipreset]').forEach(b=>b.onclick=()=>flipAll(b,false));
  document.querySelectorAll('[data-rep]').forEach(b=>b.onclick=()=>repeatQueue(b));
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
