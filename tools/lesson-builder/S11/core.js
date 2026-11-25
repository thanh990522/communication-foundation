const AUDIO = /*AUDIO_JSON*/;
const ONLINE_BASE = /*ONLINE_BASE*/'';

/* =========================================================
   AUDIO PLAYER
   ========================================================= */
const pause = ms => new Promise(r=>setTimeout(r,ms));
function toBlobUrls(){
  for(const id in AUDIO){
    const a=AUDIO[id];
    if(!String(a.src).startsWith('data:')){ a.blob=null; continue; }
    try{
      const b64=a.src.split(',')[1], bin=atob(b64), u=new Uint8Array(bin.length);
      for(let i=0;i<bin.length;i++) u[i]=bin.charCodeAt(i);
      a.blob=URL.createObjectURL(new Blob([u],{type:'audio/mpeg'}));
    }catch(e){ a.blob=null; }
  }
}
const srcOf = id => AUDIO[id].blob || AUDIO[id].src;
let toastT=null;
function toast(msg){ const t=document.getElementById('toast'); if(!t) return; t.textContent=msg; t.classList.add('show'); clearTimeout(toastT); toastT=setTimeout(()=>t.classList.remove('show'),4500); }
let curAudio=null, curResolve=null, qid=0;
function haltCurrent(){ if(curAudio){ curAudio.pause(); curAudio=null; } if(curResolve){ const r=curResolve; curResolve=null; r(); } }
const isRel = u => !/^(data:|blob:|https?:)/.test(u);
function candidates(id){
  const a=AUDIO[id], list=[];
  if(a.blob) list.push(a.blob);
  if(location.protocol!=='file:' || !isRel(a.src)) list.push(a.src);
  if(ONLINE_BASE && isRel(a.src)) list.push(ONLINE_BASE+a.src);
  return [...new Set(list)];
}
function playOne(id){
  return new Promise(res=>{
    const a=AUDIO[id]; if(!a){ res(); return; }
    const srcs=candidates(id); let k=0;
    const el=new Audio(); el.preload='auto'; curAudio=el; curResolve=res;
    const done=()=>{ if(curResolve===res){curResolve=null;curAudio=null;} res(); };
    const next=()=>{
      if(curAudio!==el) return done();
      if(k>=srcs.length){ toast('Không phát được audio. Kiểm tra kết nối Internet rồi bấm ▶ lại.'); return done(); }
      el.src=srcs[k++];
      el.play().catch(err=>{
        if(err&&err.name==='NotAllowedError'){ toast('Trình duyệt đang chặn âm thanh — bấm lại nút ▶ một lần nữa.'); return done(); }
        if(err&&err.name==='AbortError') return;
        next();
      });
    };
    el.onended=done;
    el.onerror=()=>next();
    next();
  });
}
/* warm the audio of the current slide so the first ▶ starts instantly */
const warmed=new Set();
function warmSlide(slide){
  if(location.protocol==='file:' && !ONLINE_BASE) return;
  const ids=new Set();
  slide.querySelectorAll('[data-a]').forEach(e=>ids.add(e.dataset.a));
  slide.querySelectorAll('[data-letter]').forEach(e=>ids.add('L_'+e.dataset.letter));
  ids.forEach(id=>{
    const a=AUDIO[id]; if(!a||a.blob||warmed.has(id)) return; warmed.add(id);
    const u=candidates(id)[0]; if(u) fetch(u).catch(()=>{});
  });
}
async function playQueue(ids,onEach,gap=0,btn){
  const my=++qid; haltCurrent(); clearSpeaking();
  if(btn) btn.classList.add('speaking');
  for(let i=0;i<ids.length;i++){
    if(my!==qid) return false;
    onEach&&onEach(i);
    await playOne(ids[i]);
    if(my!==qid) return false;
    if(gap) await pause(gap);
  }
  onEach&&onEach(-1);
  if(btn) btn.classList.remove('speaking');
  return true;
}
const play = (id,btn) => playQueue([id],null,0,btn);
function clearSpeaking(){ document.querySelectorAll('.speaking').forEach(e=>e.classList.remove('speaking')); }
function stopAll(){ qid++; haltCurrent(); clearSpeaking(); document.querySelectorAll('.lit').forEach(e=>e.classList.remove('lit')); hl(-1); }

document.addEventListener('click',e=>{
  if(e.target.closest('a')) return;
  const el = e.target.closest('[data-letter],[data-a]');
  if(!el) return;
  if(el.dataset.letter) play('L_'+el.dataset.letter,el);
  else play(el.dataset.a,el);
});
const PLAY_SVG='<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>';
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const fname = id => AUDIO[id].file.split('/').pop();
const dlHref = id => { const c=candidates(id); return c[0]||srcOf(id); };
const dl = (id,label) => `<a class="dl" href="${dlHref(id)}" download="${esc(fname(id))}" title="Download ${esc(fname(id))}">⬇${label?' '+label:''}</a>`;

function copyText(txt,btn){
  const ok=()=>{ const o=btn.innerHTML; btn.innerHTML='✓ Copied!'; setTimeout(()=>btn.innerHTML=o,1400); };
  const fallback=()=>{ const ta=document.createElement('textarea'); ta.value=txt; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');ok();}catch(e){alert(txt);} ta.remove(); };
  if(navigator.clipboard && window.isSecureContext){ navigator.clipboard.writeText(txt).then(ok,fallback); } else fallback();
}

/* beep */
function beep(){
  try{ const C=new (window.AudioContext||window.webkitAudioContext)();
    [0,.35,.7].forEach(t=>{const o=C.createOscillator(),g=C.createGain();o.frequency.value=880;o.connect(g);g.connect(C.destination);g.gain.setValueAtTime(.25,C.currentTime+t);g.gain.exponentialRampToValueAtTime(.001,C.currentTime+t+.3);o.start(C.currentTime+t);o.stop(C.currentTime+t+.3);});
  }catch(e){}
}
/* 30s timer (shown only when used) */
const TM={total:30,left:30,run:null};
function tDraw(){ const m=Math.floor(TM.left/60),s=TM.left%60; document.getElementById('tD').textContent=String(m).padStart(2,'0')+':'+String(s).padStart(2,'0'); }
function tStart(sec){
  const box=document.getElementById('timer'); box.classList.add('show'); box.classList.remove('end');
  clearInterval(TM.run); TM.total=TM.left=sec; tDraw();
  TM.run=setInterval(()=>{TM.left--;tDraw();if(TM.left<=0){clearInterval(TM.run);box.classList.add('end');beep();setTimeout(()=>box.classList.remove('show'),4000);}},1000);
}

/* =========================================================
   DECK — fills the whole screen, no on-screen controls
   ========================================================= */
const slides=[...document.querySelectorAll('.slide')]; let cur=0;
function fit(){
  const W=window.innerWidth, H=window.innerHeight, deck=document.getElementById('deck');
  const s=Math.min(W/1280,H/720);
  const dw=W/s, dh=H/s;
  const ox=Math.max(0,(dw-Math.min(dw,1480))/2), oy=Math.max(0,(dh-720)/2);
  deck.style.width=dw+'px'; deck.style.height=dh+'px';
  deck.style.setProperty('--ox',ox+'px'); deck.style.setProperty('--oy',oy+'px');
  deck.style.transform=`scale(${s})`;
}
function go(i){
  i=Math.max(0,Math.min(slides.length-1,i));
  slides[cur].classList.remove('active'); cur=i; slides[cur].classList.add('active');
  try{ history.replaceState(null,'','#'+(cur+1)); }catch(e){}
  warmSlide(slides[cur]);
  stopAll();
}
document.addEventListener('keydown',e=>{
  if(['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName)||e.target.isContentEditable) return;
  const k=e.key;
  if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='ArrowDown'){e.preventDefault();go(cur+1);}
  else if(k==='ArrowLeft'||k==='PageUp'||k==='ArrowUp'){e.preventDefault();go(cur-1);}
  else if(k==='Home') go(0); else if(k==='End') go(slides.length-1);
  else if(k==='f'||k==='F') fullscreen();
  else if(k==='Escape') stopAll();
});
/* swipe on touch screens */
let tx0=null;
document.addEventListener('touchstart',e=>{tx0=e.touches[0].clientX;},{passive:true});
document.addEventListener('touchend',e=>{ if(tx0==null) return; const dx=e.changedTouches[0].clientX-tx0; if(Math.abs(dx)>70) go(cur+(dx<0?1:-1)); tx0=null; });
function fullscreen(){ try{ if(!document.fullscreenElement){ const r=document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen(); r&&r.catch&&r.catch(()=>toast('Trình duyệt chặn toàn màn hình ở chế độ xem trước — hãy tải file về và mở bằng Chrome/Edge.')); } else document.exitFullscreen(); }catch(e){ toast('Không bật được toàn màn hình ở chế độ này.'); } }

