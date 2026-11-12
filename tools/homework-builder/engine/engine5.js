/* ---------------- 5-part homework helpers: translate + shadow */
const fmt1=x=>{ const r=Math.round(x*10)/10; return Number.isInteger(r)?String(r):r.toFixed(1); };
function breakdown(g){
  const rows=HW.sections.map(sec=>{
    let sc=0,mx=0; sec.items.forEach(it=>{ const d=g.details[it.id]; if(d){ sc+=d.got||0; mx+=d.pts||it.points||1; } });
    return mx?`<div><span>${esc(sec.title)}</span><b>${fmt1(sc)} / ${mx}</b></div>`:'';
  }).join('');
  return rows?`<div class="secbreak">${rows}</div>`:'';
}
/* ---- word normalisation shared by translate + shadow */
const CONTR={"i'm":"i am","you're":"you are","we're":"we are","they're":"they are","he's":"he is","she's":"she is","it's":"it is","there's":"there is","that's":"that is","what's":"what is","where's":"where is","who's":"who is","how's":"how is","isn't":"is not","aren't":"are not","wasn't":"was not","weren't":"were not","don't":"do not","doesn't":"does not","didn't":"did not","can't":"can not","cannot":"can not","won't":"will not","couldn't":"could not","haven't":"have not","hasn't":"has not","i've":"i have","you've":"you have","we've":"we have","i'll":"i will","you'll":"you will","we'll":"we will","i'd":"i would","let's":"let us","name's":"name is"};
const ONES=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'];
const TENS=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'];
const ORD={one:'first',two:'second',three:'third',five:'fifth',eight:'eighth',nine:'ninth',twelve:'twelfth',twenty:'twentieth',thirty:'thirtieth',forty:'fortieth',fifty:'fiftieth',sixty:'sixtieth',seventy:'seventieth',eighty:'eightieth',ninety:'ninetieth'};
function numW(n){ n=+n; if(n<20) return [ONES[n]]; if(n<100) return n%10?[TENS[Math.floor(n/10)],ONES[n%10]]:[TENS[n/10]]; if(n<1000) return [ONES[Math.floor(n/100)],'hundred'].concat(n%100?numW(n%100):[]); return String(n).split('').map(d=>ONES[+d]); }
function ordW(n){ const w=numW(n); const l=w[w.length-1]; w[w.length-1]=ORD[l]||(l+'th'); return w; }
const SPELL={neighbour:'neighbor',neighbours:'neighbors',neighbourhood:'neighborhood',neighbourhoods:'neighborhoods',centre:'center',centrally:'centrally',favourite:'favorite',colour:'color',mum:'mom',okay:'ok',email:'email','e-mail':'email',cafe:'cafe'};
/* returns [{raw, toks:[...]}] for each written word */
function wordsOf(text){
  let t=String(text||'').replace(/[’‘]/g,"'").replace(/é/g,'e').replace(/\b([ap])\.\s?m\b\.?/gi,'$1m').replace(/\bo'clock\b/gi,'')
    .replace(/[\w.\-]+@[\w\-]+(\.[\w\-]+)+/g,m=>m.replace(/@/g,' at ').replace(/\./g,' dot ').replace(/_/g,' underscore ').replace(/-/g,' hyphen '))
    .replace(/([A-Za-z0-9])\.(com|net|org|vn|edu)\b/gi,'$1 dot $2');
  const raw=t.match(/[A-Za-z0-9][A-Za-z0-9'@.:\-]*/g)||[];
  return raw.map(r=>({raw:r,toks:normTok(r)}));
}
function normTok(r){
  let w=r.toLowerCase().replace(/[’‘]/g,"'").replace(/[éè]/g,'e').replace(/[.,!?;"]+$/,'').replace(/^[.,'"]+|'+$/g,'');
  if(!w) return [];
  if(/^[a-z](-[a-z])+$/.test(w)) return [w.replace(/-/g,'')];          // spelled letters L-I-N-H → linh
  let m=w.match(/^(\d{1,2})[:.](\d{2})$/); if(m) return numW(m[1]).concat(+m[2]?(+m[2]<10?['oh'].concat(numW(m[2])):numW(m[2])):[]);
  m=w.match(/^(\d{1,2})(?:[:.](\d{2}))?(am|pm)$/); if(m) return normTok(m[1]+(m[2]?':'+m[2]:'')).concat([m[3]]);
  m=w.match(/^(\d+)(st|nd|rd|th)$/); if(m) return ordW(m[1]);
  if(/^\d+$/.test(w)) return numW(w);
  if(CONTR[w]) return CONTR[w].split(' ');
  if(/-/.test(w)) return w.split('-').filter(Boolean).flatMap(x=>normTok(x));
  w=w.replace(/'s$/,'s').replace(/'/g,'').replace(/[^a-z0-9]/g,'');
  if(SPELL[w]) w=SPELL[w];
  if(w==='oclock') return [];
  if(w==='lowercase') return ['lower','case'];
  return w?[w]:[];
}
function joinLetters(toks){ // heard "l i n h" → "linh"
  const out=[]; let run=[];
  const flush=()=>{ if(run.length>=3) out.push(run.join('')); else out.push(...run); run=[]; };
  toks.forEach(t=>{ if(t.length===1&&/[a-z]/.test(t)) run.push(t); else { flush(); out.push(t); } }); flush(); return out;
}
function lcsMatch(a,b){ // returns boolean array for a: token matched in order
  const n=a.length,m=b.length,D=Array.from({length:n+1},()=>new Uint16Array(m+1));
  for(let i=n-1;i>=0;i--) for(let j=m-1;j>=0;j--) D[i][j]=a[i]===b[j]?D[i+1][j+1]+1:Math.max(D[i+1][j],D[i][j+1]);
  const ok=new Array(n).fill(false); let i=0,j=0;
  while(i<n&&j<m){ if(a[i]===b[j]){ ok[i]=true; i++; j++; } else if(D[i+1][j]>=D[i][j+1]) i++; else j++; }
  return ok;
}
function editDist(a,b){ const D=Array.from({length:a.length+1},(_,i)=>[i]); for(let j=1;j<=b.length;j++) D[0][j]=j;
  for(let i=1;i<=a.length;i++) for(let j=1;j<=b.length;j++) D[i][j]=Math.min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(a[i-1]===b[j-1]?0:1)); return D[a.length][b.length]; }
/* ---- translate grading: exact (after normalising) = full points, one word off = half */
function gradeTr(it,v){
  const pts=it.points||2, W=wordsOf(v), mine=W.flatMap(w=>w.toks);
  let best=null;
  it.answers.forEach(a=>{ const t=wordsOf(a).flatMap(w=>w.toks), d=editDist(mine,t); if(!best||d<best.d) best={d,t}; });
  let got=0; if(mine.length&&best){ if(best.d===0) got=pts; else if(best.d===1&&best.t.length>=5) got=Math.round(pts/2*10)/10; }
  // colour the learner's words against the closest model answer
  const okTok=best?lcsMatch(mine,best.t):[]; let k=0;
  const html=W.map(w=>{ let good=w.toks.length>0; w.toks.forEach(()=>{ if(!okTok[k]) good=false; k++; }); return `<span class="w ${good?'ok':'bad'}">${esc(w.raw)}</span>`; }).join(' ');
  return {v,got,pts,ok:got>=pts,html};
}
/* ---- shadowing: listen, record, speech-recognition scoring /10 */
let audRate=1;
const SRC=window.SpeechRecognition||window.webkitSpeechRecognition;
function shadowBody(it){
  const sents=it.sentences.map((s,i)=>`<span class="shs"><button type="button" class="sp" data-audio="${esc(s.audio)}" aria-label="Nghe câu ${i+1}">${PLAY}</button>${wordsOf(s.text).length?spanWords(s.text,i):''}</span>`).join(' ');
  return `<div class="prompt">${esc(it.prompt||'Nghe mẫu, sau đó ghi âm giọng đọc của bạn.')}</div>
  <div class="shbox" data-sh="${esc(it.id)}">
    <div class="shtools"><button type="button" class="play" data-audio="${esc(it.audio)}" aria-label="Nghe cả đoạn">${PLAY}</button><span class="lbl">Nghe cả đoạn</span>
      <span style="flex:1"></span><button type="button" class="pill" data-rate="0.8">🐢 Chậm</button><button type="button" class="pill on" data-rate="1">Bình thường</button></div>
    <div class="shtext">${sents}</div>
    <div class="legend">Bấm ▶ trước mỗi câu để nghe riêng câu đó. Sau khi chấm: <span class="sw ok">đọc đúng</span> · <span class="sw bad">đọc sai / thiếu</span> — luyện lại những từ màu đỏ rồi ghi âm lần nữa.</div>
    <div class="rec-row"><button type="button" class="recbtn go shrec"><span class="dot"></span>Ghi âm & chấm điểm</button><span class="timer">00:00</span><div class="meter"><i></i></div></div>
    <div class="heard" hidden></div>
    <div class="shout"></div>
  </div>`;
}
function spanWords(text,si){ return String(text).split(/(\s+)/).map(p=>/^\s+$/.test(p)||!p?p:`<span class="sw" data-s="${si}">${esc(p)}</span>`).join(''); }
function setupShadow(box){
  const id=box.dataset.sh, it=ITEMS.find(x=>x.id===id);
  const btn=box.querySelector('.shrec'), timer=box.querySelector('.timer'), meter=box.querySelector('.meter i'), heardEl=box.querySelector('.heard'), out=box.querySelector('.shout'), txt=box.querySelector('.shtext');
  const spans=[...txt.querySelectorAll('.sw')];
  const wtoks=spans.map(sp=>normTok(sp.textContent.replace(/^[^A-Za-z0-9]+|[^A-Za-z0-9.]+$/g,'')));
  const FREE=new Set((it.free||[]).flatMap(w=>normTok(w)));
  const total=wtoks.reduce((a,t)=>a+t.length,0);
  box.querySelectorAll('.pill').forEach(p=>p.onclick=()=>{ audRate=+p.dataset.rate; box.querySelectorAll('.pill').forEach(x=>x.classList.toggle('on',x===p)); if(player) player.playbackRate=audRate; });
  box.querySelectorAll('.sp').forEach(b=>b.onclick=()=>playAudio(b,b.dataset.audio));
  let rec=null,stream=null,chunks=[],sr=null,finals=[],interim='',recording=false,t0=0,tick=null,ctx=null,raf=null,lastUrl=null,srErr='';
  const fmt=s=>String(Math.floor(s/60)).padStart(2,'0')+':'+String(Math.floor(s%60)).padStart(2,'0');
  function paint(res){
    spans.forEach((sp,i)=>{ sp.classList.remove('ok','bad'); if(res&&res.m) sp.classList.add(res.m[i]?'ok':'bad'); });
    txt.classList.toggle('self',!!(res&&res.self&&!submitted));
  }
  function show(){
    const r=answers[id];
    paint(r&&r.last);
    if(!r||!r.last){ out.innerHTML=''; return; }
    const s=r.last.s, cls=s>=8?'hi':s>=5?'mid':'lo';
    out.innerHTML=`<div class="shres"><div class="sc10 ${cls}">${fmt1(s)}<small> / 10</small></div><div class="shmeta">${r.last.self?'Tự chấm: bấm vào từ bạn đọc sai để chuyển sang màu đỏ.<br>':''}Đúng ${r.last.ok}/${r.last.tot} từ · Điểm cao nhất: <b>${fmt1(r.best.s)}/10</b> · ${r.tries||1} lần ghi âm</div>${lastUrl?`<audio controls src="${lastUrl}" style="max-width:260px"></audio>`:''}</div>`;
  }
  function score(alts){
    // alts: array of transcripts (best first). Align best transcript in order, then accept words found in other alternatives.
    const heard=joinLetters(alts[0]?wordsOf(alts[0]).flatMap(w=>w.toks):[]);
    const flat=[], owner=[]; wtoks.forEach((t,i)=>t.forEach(x=>{ flat.push(x); owner.push(i); }));
    const ok=lcsMatch(flat,heard);
    const pool={}; alts.slice(1).forEach(a=>joinLetters(wordsOf(a).flatMap(w=>w.toks)).forEach(x=>pool[x]=(pool[x]||0)+1));
    flat.forEach((x,k)=>{ if(!ok[k]&&FREE.has(x)) ok[k]=true; else if(!ok[k]&&pool[x]>0){ pool[x]--; ok[k]=true; } });
    const m=wtoks.map(()=>true); flat.forEach((x,k)=>{ if(!ok[k]) m[owner[k]]=false; });
    const good=ok.filter(Boolean).length;
    return {s:total?Math.round(good/total*100)/10:0,m,ok:good,tot:total};
  }
  function commit(res){
    const r=answers[id]||{tries:0}; r.tries=(r.tries||0)+1; r.last=res; if(!r.best||res.s>=r.best.s) r.best=res;
    answers[id]=r; saveDraft(); show(); updateProgress();
  }
  txt.addEventListener('click',e=>{
    const sp=e.target.closest('.sw'), r=answers[id]; if(!sp||submitted||!r||!r.last||!r.last.self) return;
    const i=spans.indexOf(sp); r.last.m[i]=!r.last.m[i];
    let good=0; wtoks.forEach((t,k)=>{ if(r.last.m[k]) good+=t.length; });
    r.last.ok=good; r.last.s=total?Math.round(good/total*100)/10:0; r.best=r.last; saveDraft(); show();
  });
  function cleanup(){ clearInterval(tick); cancelAnimationFrame(raf); if(stream) stream.getTracks().forEach(t=>t.stop()); if(ctx) ctx.close().catch(()=>{}); stream=null; ctx=null; meter.style.width='0'; }
  async function start(){
    if(submitted) return;
    stopAudio();
    if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia){ toast('Trình duyệt này không ghi âm được. Hãy dùng Chrome hoặc Edge.',5000); return; }
    try{ stream=await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:true,noiseSuppression:true}}); }
    catch(e){ toast('Chưa được phép dùng micro. Hãy cho phép micro rồi thử lại.',5000); return; }
    finals=[]; interim=''; srErr=''; chunks=[]; recording=true;
    const mime=pickMime();
    try{ rec=new MediaRecorder(stream,mime?{mimeType:mime}:undefined); rec.ondataavailable=e=>{ if(e.data&&e.data.size) chunks.push(e.data); }; rec.start(500); }catch(e){ rec=null; }
    if(SRC){
      sr=new SRC(); sr.lang='en-GB'; sr.continuous=true; sr.interimResults=true; sr.maxAlternatives=3;
      sr.onresult=e=>{ interim=''; for(let i=e.resultIndex;i<e.results.length;i++){ const r=e.results[i]; if(r.isFinal) finals.push([...r].map(a=>a.transcript)); else interim+=r[0].transcript; }
        heardEl.hidden=false; heardEl.textContent='🎧 '+(finals.map(f=>f[0]).join(' ')+' '+interim).trim(); };
      sr.onerror=e=>{ srErr=e.error||'error'; };
      sr.onend=()=>{ if(recording&&!/not-allowed|service-not-allowed|language/.test(srErr)) try{ sr.start(); }catch(e){} };
      try{ sr.start(); }catch(e){ srErr='start'; }
    }
    try{ ctx=new (window.AudioContext||window.webkitAudioContext)(); const an=ctx.createAnalyser(); an.fftSize=512; ctx.createMediaStreamSource(stream).connect(an);
      const buf=new Uint8Array(an.fftSize); const draw=()=>{ an.getByteTimeDomainData(buf); let m=0; for(const x of buf) m=Math.max(m,Math.abs(x-128)); meter.style.width=Math.min(100,m/128*180)+'%'; raf=requestAnimationFrame(draw); }; draw(); }catch(e){}
    t0=Date.now(); const maxS=Math.max(30,(it.dur||30)*2.5);
    btn.className='recbtn stop shrec'; btn.innerHTML='<span class="dot"></span>Dừng & chấm điểm';
    heardEl.hidden=!SRC; heardEl.textContent='🎧 Đang nghe… hãy đọc to, rõ ràng.';
    tick=setInterval(()=>{ const s=(Date.now()-t0)/1000; timer.textContent=fmt(s); if(s>=maxS) stop(); },250);
    window.__shStop=()=>{ if(recording) stop(true); };
  }
  function stop(silent){
    if(!recording) return; recording=false; window.__shStop=null;
    btn.className='recbtn go shrec'; btn.innerHTML='<span class="dot"></span>Đang chấm…'; btn.disabled=true;
    const sec=(Date.now()-t0)/1000;
    if(rec&&rec.state!=='inactive'){ rec.onstop=()=>{ if(chunks.length){ if(lastUrl) URL.revokeObjectURL(lastUrl); lastUrl=URL.createObjectURL(new Blob(chunks,{type:rec.mimeType||'audio/webm'})); } show(); }; rec.stop(); }
    if(sr) try{ sr.stop(); }catch(e){}
    cleanup();
    setTimeout(()=>{
      if(sr){ sr.onend=null; sr.onresult=null; }
      btn.disabled=submitted; btn.innerHTML='<span class="dot"></span>Ghi âm lại & chấm điểm';
      if(silent) return;
      if(sec<2){ toast('Bản ghi quá ngắn, hãy thử lại.'); return; }
      const alts=[finals.map(f=>f[0]).join(' ')+' '+interim, finals.map(f=>f[1]||'').join(' '), finals.map(f=>f[2]||'').join(' ')];
      if(SRC&&!/not-allowed|service-not-allowed|network|start|language/.test(srErr)){
        if(!alts[0].trim()){ toast('Chưa nghe được giọng đọc. Kiểm tra micro và đọc to hơn nhé.',5000); }
        commit(score(alts));
      }else{
        // no speech recognition on this browser → self-check
        toast('Trình duyệt này không tự chấm được. Hãy nghe lại bản ghi và bấm vào từ bạn đọc sai.',6500);
        const m=wtoks.map(()=>true); commit({s:10,m,ok:total,tot:total,self:true});
      }
    },SRC?900:50);
  }
  btn.onclick=()=>{ if(recording) stop(); else start(); };
  if(!SRC) box.querySelector('.legend').insertAdjacentHTML('beforeend','<br>⚠ Trình duyệt này chưa hỗ trợ chấm tự động — hãy dùng <b>Google Chrome</b> hoặc <b>Microsoft Edge</b> để được chấm điểm.');
  show();
}
