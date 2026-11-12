"""One-off patch: adds translate + shadow item types, section scripts and score breakdown to homework/index.html"""
import sys
p=sys.argv[1]; s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt, (a[:70], s.count(a)); s=s.replace(a,b)

rep("""@media (max-width:560px){""","""/* section extras */
.sec-h h2 small{display:block;font-size:13.5px;font-weight:600;color:var(--muted);margin-top:2px}
.opt.long{font-size:16px;height:auto;min-height:48px;padding:8px 14px;text-align:left;font-weight:800}
details.script{margin:12px 18px 0;border:2px solid var(--sky-2);border-radius:14px;background:#FBFCFF}
details.script summary{cursor:pointer;padding:10px 14px;font-weight:900;color:var(--blue)}
details.script .sl{padding:4px 14px;font-size:15.5px;line-height:1.55}
details.script .sl b{color:var(--navy);margin-right:6px}
details.script>div{padding-bottom:10px}
/* translate */
.vi{font-weight:800;color:var(--navy);font-size:17px}
.hint{font-size:13.5px;font-weight:700;color:#8A5300;background:var(--yellow-soft);border-radius:8px;padding:3px 9px;align-self:flex-start}
textarea.tr{min-height:64px;font-size:17px;font-weight:600;color:var(--navy)}
.trfb{display:flex;flex-direction:column;gap:4px;font-size:15px}
.trfb .w{border-radius:5px;padding:0 2px}
.w.ok{color:#15803D;background:var(--green-soft)}
.w.bad{color:#B91C1C;background:var(--red-soft);text-decoration:underline wavy #DC2626}
.mark.half{background:var(--yellow-soft);color:#8A5300}
.it.half .qn{background:var(--yellow);color:var(--navy)}
/* shadow */
.shbox{border:2px solid var(--sky-2);border-radius:16px;padding:14px;background:#FBFCFF;display:flex;flex-direction:column;gap:12px}
.shtools{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.shtools .lbl{font-weight:800;color:var(--navy)}
.pill{border:2px solid var(--line);background:#fff;border-radius:999px;padding:6px 12px;font-weight:800;font-size:13.5px;color:var(--navy);cursor:pointer}
.pill.on{background:var(--navy);color:var(--yellow);border-color:var(--navy)}
.shtext{font-size:19px;line-height:2;color:var(--ink);background:#fff;border:2px solid var(--line);border-radius:14px;padding:12px 16px}
.shs .sp{display:inline-flex;vertical-align:middle;width:26px;height:26px;border-radius:50%;border:none;background:var(--sky);cursor:pointer;margin:0 4px 0 2px;align-items:center;justify-content:center}
.shs .sp svg{width:11px;height:11px;fill:var(--blue);margin-left:2px}
.shs .sp.on{background:var(--yellow)}
.sw{border-radius:6px;padding:1px 2px;transition:background .2s}
.sw.ok{color:#15803D;background:var(--green-soft);font-weight:700}
.sw.bad{color:#B91C1C;background:var(--red-soft);font-weight:700;text-decoration:underline wavy #DC2626}
.shtext.self .sw{cursor:pointer}
.shres{display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.sc10{font-size:34px;font-weight:900;line-height:1;color:var(--navy)}
.sc10 small{font-size:16px;color:var(--muted)}
.sc10.hi{color:var(--green)}.sc10.mid{color:#B45309}.sc10.lo{color:var(--red)}
.shmeta{font-size:13.5px;font-weight:700;color:var(--muted)}
.heard{font-size:14px;color:var(--muted);font-style:italic}
.legend{font-size:13px;font-weight:700;color:var(--muted)}
.secbreak{margin:14px auto 0;max-width:520px;text-align:left;display:flex;flex-direction:column;gap:6px}
.secbreak div{display:flex;justify-content:space-between;gap:10px;background:#fff;border:1.5px solid var(--line);border-radius:10px;padding:7px 12px;font-weight:700;font-size:14.5px}
.secbreak b{color:var(--navy);white-space:nowrap}
@media (max-width:560px){
  .shtext{font-size:17px;padding:10px 12px}""")

rep("const AUTO=['mcq','listen_mcq','listen_type','gap'];","const AUTO=['mcq','listen_mcq','listen_type','gap','translate','shadow'];")
rep("""<h2>${esc(sec.title)}</h2>""","""<h2>${esc(sec.title)}${sec.sub?`<small>${esc(sec.sub)}</small>`:''}</h2>""")
rep("""<div><b>Listen to the call</b></div></div>`:''}""","""<div><b>${esc(sec.audioLabel||'Listen to the recording')}</b><small>${esc(sec.audioHint||'Nghe 2 lần rồi trả lời.')}</small></div></div>`:''}""")
rep("""    html+='</div></section>';""","""    html+='</div>';
    if(sec.script) html+=`<details class="script" hidden><summary>📜 Script — đọc lại sau khi nghe</summary><div>${sec.script.map(l=>Array.isArray(l)?`<div class="sl"><b>${esc(l[0])}:</b>${esc(l[1])}</div>`:`<div class="sl">${esc(l)}</div>`).join('')}</div></details>`;
    html+='</section>';""")
rep("""<div class="opts">${it.options.map(o=>`<button type="button" class="opt${v===o?' sel':''}\"""","""<div class="opts">${it.options.map(o=>`<button type="button" class="opt${String(o).length>4?' long':''}${v===o?' sel':''}\"""")
rep("""    case 'writing':""","""    case 'translate':
      return `<div class="vi">${esc(it.prompt)}</div>${it.hint?`<span class="hint">💡 ${esc(it.hint)}</span>`:''}<textarea class="tr" rows="2" data-q="${esc(it.id)}" placeholder="Viết câu tiếng Anh…" autocomplete="off" autocapitalize="sentences" spellcheck="false">${esc(v||'')}</textarea>${mark}`;
    case 'shadow':
      return shadowBody(it)+mark;
    case 'writing':""")
rep("""  f.querySelectorAll('[data-rec]').forEach(setupRecorder);""","""  f.querySelectorAll('[data-rec]').forEach(setupRecorder);
  f.querySelectorAll('[data-sh]').forEach(setupShadow);""")
rep("""    if(el.tagName==='TEXTAREA') wc(el.dataset.q);""","""    if(el.tagName==='TEXTAREA'&&!el.classList.contains('tr')) wc(el.dataset.q);""")
rep("""  if(it.type==='voice') return !!voice[it.id];""","""  if(it.type==='voice') return !!voice[it.id];
  if(it.type==='shadow') return !!(answers[it.id]&&answers[it.id].best);""")
rep("""    const pts=it.points||1; max+=pts;
    const v=String(answers[it.id]||'');
    const ok=v.trim()!=='' && it.answers.map(norm).includes(norm(v));
    if(ok) score+=pts;
    details[it.id]={v,ok};""","""    const pts=it.points||1; max+=pts;
    if(it.type==='shadow'){
      const r=answers[it.id], got=r&&r.best?Math.round(r.best.s*10)/10:0;
      score+=got; details[it.id]={ok:got>=8,got,pts}; continue;
    }
    if(it.type==='translate'){ const t=gradeTr(it,answers[it.id]||''); score+=t.got; details[it.id]=t; continue; }
    const v=String(answers[it.id]||'');
    const ok=v.trim()!=='' && it.answers.map(norm).includes(norm(v));
    if(ok) score+=pts;
    details[it.id]={v,ok,got:ok?pts:0,pts};""")
rep("""  for(const it of ITEMS){
    if(!AUTO.includes(it.type)||!it.answers) continue;""","""  for(const it of ITEMS){
    if(!AUTO.includes(it.type)||(!it.answers&&it.type!=='shadow')) continue;""")
rep("""  return {score,max,details};""","""  score=Math.round(score*10)/10;
  return {score,max,details};""")
rep("""    if(details[it.id]){ const ok=details[it.id].ok; el.classList.add(ok?'right':'wrong'); box.innerHTML=`<span class="mark ${ok?'right':'wrong'}">${ok?'✓ Correct':'✗ Wrong'}</span> <span class="key">Answer: <b>${esc(it.show||it.answers[0])}</b></span>`; }""","""    el.classList.remove('half');
    const d=details[it.id];
    if(d&&it.type==='shadow'){ const c=d.got>=8?'right':d.got>=5?'half':'wrong'; el.classList.add(c); box.innerHTML=`<span class="mark ${c}">🎙 Điểm đọc: ${fmt1(d.got)} / 10</span>`; }
    else if(d&&it.type==='translate'){
      const c=d.got>=d.pts?'right':d.got>0?'half':'wrong'; el.classList.add(c);
      box.innerHTML=`<div class="trfb"><div><span class="mark ${c}">${c==='right'?'✓ Correct':c==='half'?'≈ Gần đúng':'✗ Chưa đúng'} · ${d.got}/${d.pts}</span></div>${d.v.trim()?`<div>Bạn viết: ${d.html}</div>`:''}<div class="key" style="margin:0">Đáp án: <b>${esc(it.show||it.answers[0])}</b></div></div>`;
    }
    else if(d){ const ok=d.ok; el.classList.add(ok?'right':'wrong'); box.innerHTML=`<span class="mark ${ok?'right':'wrong'}">${ok?'✓ Correct':'✗ Wrong'}</span> <span class="key">Answer: <b>${esc(it.show||it.answers[0])}</b></span>`; }""")
rep("""function showMarks(details){""","""function showMarks(details){
  document.querySelectorAll('details.script').forEach(d=>d.hidden=false);""")
rep("""  stopAudio();
  const g=grade()""","""  stopAudio(); if(window.__shStop) window.__shStop();
  const g=grade()""")
rep("""  $('#hw').querySelectorAll('input,textarea,.opt,.recbtn').forEach(el=>{ el.disabled=on; });""","""  $('#hw').querySelectorAll('input,textarea,.opt,.recbtn,.shrec').forEach(el=>{ el.disabled=on; });""")
rep("""<div class="sub2">${g.score} / ${g.max}</div>""","""<div class="sub2">${fmt1(g.score)} / ${g.max} điểm</div>${breakdown(g)}""")
rep("""/* ---------------- status */""", open(sys.argv[2]).read()+"""
/* ---------------- status */""")
open(p,'w').write(s); print('patched')
