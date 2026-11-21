"""Grammar theory slide + practice slide for every lesson.

`inject(html)` is called from audiopolicy.apply() for every built page (web + offline), so all lessons get the
two slides automatically:  it finds the lesson id in the footer, inserts the slides before G[sid]['before'],
renumbers the slide footers, adds CSS/JS and registers the grammar audio in AUDIO.

Audio:  python3 grammar.py audio [S01 S02 …]   → site/grammar/audio/Sxx/*.mp3 + manifest.json
        (web pages play them from ../../grammar/audio/Sxx/, offline pages embed them as data URIs)
"""
import base64, html as _h, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from grammar_data import G

SITE = os.path.normpath(os.path.join(HERE, '..', '..'))
AUD = os.path.join(SITE, 'grammar', 'audio')
P = '<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>'
e = _h.escape
MARK = '<!--grammar-->'


def plain(t): return t.replace('*', '')


def hl(t): return re.sub(r'\*([^*]+)\*', r'<b class="gm-hl">\1</b>', e(t))


def pb(aid, cls=''): return f'<button class="play sm{" " + cls if cls else ""}" data-a="{aid}">{P}</button>'


def clips(sid):
    g = G[sid]; out = []
    for b, box in enumerate(g['boxes']):
        for j, x in enumerate(box['ex']): out.append((f'GMX_{b}_{j}', f'{sid}_grammar_example_{b + 1}_{j + 1}.mp3', plain(x), 'ex'))
    pr = g['practice']
    for i, it in enumerate(pr['items']):
        t = it[0] if pr['type'] == 'order' else it[0].replace('___', it[2] if pr['type'] == 'choose' else it[1][0])
        out.append((f'GMP_{i}', f'{sid}_grammar_practice_{i + 1}.mp3', t[0].upper() + t[1:], 'pr'))
    return out


# ------------------------------------------------------------------ slides
def formula(line):
    out = []
    for k, (t, kind) in enumerate(line):
        if kind == 'p':
            out.append(f'<span class="gm-p">{e(t)}</span>'); continue
        if out and line[k - 1][1] != 'p': out.append('<i class="gm-plus">+</i>')
        out.append(f'<span class="gm-t gm-{kind}">{e(t)}</span>')
    return '<div class="gm-fl">' + ''.join(out) + '</div>'


def slides(sid, foot):
    g = G[sid]
    boxes = ''
    for b, box in enumerate(g['boxes']):
        ex = ''.join(f'<div class="gm-ex">{pb(f"GMX_{b}_{j}")}<span>{hl(x)}</span></div>' for j, x in enumerate(box['ex']))
        boxes += (f'<div class="gm-box"><div class="gm-tag">{box["tag"]}</div><div class="gm-f">{"".join(formula(l) for l in box["f"])}</div>'
                  f'<div class="gm-vi">{e(box["vi"])}</div>{ex}</div>')
    scale = ''
    if g.get('scale'):
        scale = '<div class="gm-scale">' + ''.join(f'<span><b>{e(a)}</b><i>{e(p)}</i></span>' for a, p in g['scale']) + '</div>'
    notes = '<div class="gm-notes"><b class="gm-nh">💡 Remember</b>' + ''.join(f'<span>{n}</span>' for n in g['notes']) + '</div>'
    legend = ('<div class="gm-leg"><span class="gm-t gm-s">subject</span><span class="gm-t gm-a">be / aux</span><span class="gm-t gm-v">verb</span>'
              '<span class="gm-t gm-k">key word</span></div>')
    theory = (f'<section class="slide" data-title="Grammar: {e(g["short"])}">\n'
              f'  <div class="s-head"><span class="chip c-input">Grammar · Theory</span><h2>{g["title"]}</h2></div>\n'
              f'  <div class="gm-sub"><span>📘 {e(g["vi"])}</span>{legend}</div>\n'
              f'  <div class="gm-grid">{boxes}</div>\n  {scale}{notes}\n{foot}</section>\n')

    pr = g['practice']; t = pr['type']; rows = ''
    for i, it in enumerate(pr['items']):
        if t == 'choose':
            s, opts, a = it
            body = (f'<span class="gm-q">{e(s).replace("___", "<span class=gm-gap>___</span>")}</span>'
                    f'<span class="gm-opts">' + ''.join(f'<button class="opt" data-o="{e(o)}">{e(o)}</button>' for o in opts) + '</span>')
        elif t == 'type':
            s, ans, hint = it
            body = (f'<span class="gm-q">{e(s).replace("___", f"<input class=gm-in autocomplete=off spellcheck=false>")}'
                    + (f' <i class="gm-hint">{e(hint)}</i>' if hint else '') + '</span><span class="gm-ans"></span>')
        else:
            s, vi = it
            body = f'<div class="gm-ord"><span class="gm-vq">🇻🇳 {e(vi)}</span><div class="gm-line"></div><div class="gm-bank"></div></div>'
        rows += f'<div class="gm-row" data-i="{i}"><span class="n">{i + 1}</span>{body}<span class="gm-say" hidden>{pb(f"GMP_{i}", "y")}</span></div>'
    btns = ('<button class="btn sm" data-gm="check">✓ Check</button>' if t != 'choose' else '') + \
        '<button class="btn sm y" data-gm="show">👁 Answers</button><button class="btn sm ghost" data-gm="reset">↺ Reset</button>'
    hint = {'choose': 'Click an answer · then 🔊 listen and say the sentence',
            'type': 'Type the word · ✓ Check · then 🔊 listen and say it',
            'order': 'Click the words to build the sentence · click again to remove · ✓ Check'}[t]
    practice = (f'<section class="slide" data-title="Grammar practice">\n'
                f'  <div class="s-head"><span class="chip c-prac">Grammar · Practice</span><h2>{pr["title"]}</h2></div>\n'
                f'  <div class="gm-prac gm-{t}" id="gmPrac" data-type="{t}">{rows}</div>\n'
                f'  <div class="ftools"><span>{hint}</span><span class="score" id="gmScore">✓ 0 / {len(pr["items"])}</span>{btns}</div>\n{foot}</section>\n')
    return theory + practice


CSS = r'''
.gm-sub{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:-6px 0 8px;font-size:15px;font-weight:700;color:var(--muted)}
.gm-leg{display:flex;gap:6px;flex:none}.gm-leg .gm-t{font-size:12px;padding:2px 8px}
.gm-grid{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:10px;min-height:0}
.gm-box{background:#fff;border:2px solid var(--line);border-radius:18px;padding:7px 12px;display:flex;flex-direction:column;gap:4px;min-height:0;justify-content:center;box-shadow:var(--shadow-s,0 2px 6px rgba(15,23,42,.06))}
.gm-tag{font-weight:900;color:var(--blue);font-size:16px;letter-spacing:.2px}
.gm-f{border:3px solid var(--navy);background:var(--yellow-soft,#FFF8E1);border-radius:12px;padding:5px 8px;display:flex;flex-direction:column;gap:4px;box-shadow:4px 4px 0 var(--yellow,#FFC72C)}
.gm-fl{display:flex;flex-wrap:wrap;align-items:center;gap:4px}
.gm-t{display:inline-flex;align-items:center;border-radius:8px;padding:2px 8px;font-weight:800;font-size:15px;line-height:1.25;border:2px solid transparent}
.gm-s{background:#DBEAFE;color:#1D4ED8;border-color:#93C5FD}
.gm-a{background:var(--navy,#0B1F4D);color:var(--yellow,#FFC72C)}
.gm-v{background:#DCFCE7;color:#15803D;border-color:#86EFAC}
.gm-k{background:var(--yellow,#FFC72C);color:var(--navy,#0B1F4D)}
.gm-n{background:#fff;color:var(--navy,#0B1F4D);border-color:#CBD5E1;border-style:dashed}
.gm-plus{font-style:normal;font-weight:900;color:#94A3B8;font-size:15px}
.gm-p{font-weight:900;color:var(--navy);font-size:18px}
.gm-vi{font-size:13.5px;font-weight:700;color:var(--muted)}
.gm-ex{display:flex;align-items:center;gap:8px;font-size:15.5px;font-weight:600;color:var(--navy);line-height:1.25}
.gm-ex .play.sm{width:24px;height:24px;flex:none}.gm-box .dl,.gm-prac .dl{display:none!important}
.gm-hl{color:#C2410C;background:#FFEDD5;border-radius:5px;padding:0 3px}
.gm-scale{display:flex;gap:6px;margin-top:6px;flex:none}
.gm-scale span{flex:1;display:flex;flex-direction:column;align-items:center;background:linear-gradient(180deg,#EFF6FF,#fff);border:2px solid #BFDBFE;border-radius:10px;padding:1px 4px}
.gm-scale b{font-size:15px;color:var(--navy)}.gm-scale i{font-style:normal;font-size:13px;font-weight:800;color:var(--blue)}
.gm-notes{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:6px;background:#FEF3C7;border-left:6px solid var(--yellow-2,#F59E0B);border-radius:12px;padding:5px 12px;flex:none;row-gap:2px}
.gm-nh{color:#92400E;font-size:14.5px}.gm-notes span{font-size:14.5px;font-weight:600;color:var(--navy)}.gm-notes span+span::before{content:"·";margin-right:10px;color:#D97706;font-weight:900}
.gm-prac{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:10px;min-height:0}
.gm-order .gm-row{align-items:center}
.gm-row{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:6px 12px;min-height:0;min-width:0}
.gm-row>.n{flex:none;width:28px;height:28px;border-radius:50%;background:var(--navy);color:var(--yellow);font-weight:900;display:flex;align-items:center;justify-content:center;font-size:14px}
.gm-row.ok{border-color:var(--green,#16A34A);background:var(--green-soft,#ECFDF5)}.gm-row.no{border-color:var(--red,#DC2626);background:var(--red-soft,#FEF2F2)}
.gm-q{flex:1;font-size:18px;font-weight:700;color:var(--navy);line-height:1.35;min-width:0}
.gm-gap{display:inline-block;min-width:54px;text-align:center;border-bottom:3px solid var(--blue);color:var(--blue)}
.gm-opts{display:flex;flex-direction:column;gap:5px;flex:none}.gm-opts .opt{height:34px;font-size:15.5px;padding:0 12px}
.gm-in{width:130px;height:36px;border:2px solid var(--line);border-radius:9px;padding:0 8px;font-size:17px;font-weight:800;color:var(--navy);margin:0 3px}
.gm-in.ok{border-color:var(--green,#16A34A);background:#fff}.gm-in.no{border-color:var(--red,#DC2626);background:#fff}
.gm-hint{font-style:normal;font-size:14px;color:var(--muted);font-weight:700}
.gm-ans{flex:none;font-size:15px;font-weight:900;color:#15803D}
.gm-say[hidden]{display:none}.gm-say .play.sm{width:30px;height:30px}
.gm-ord{flex:1;display:flex;flex-direction:column;gap:4px;min-width:0}
.gm-vq{font-size:14px;font-weight:700;color:var(--muted)}
.gm-line{min-height:36px;border-bottom:3px dashed #93C5FD;display:flex;flex-wrap:wrap;gap:5px;align-items:center;padding-bottom:3px}
.gm-bank{display:flex;flex-wrap:wrap;gap:5px}
.gm-w{border:2px solid #CBD5E1;background:#F8FAFC;border-radius:9px;padding:3px 10px;font-size:16.5px;font-weight:800;color:var(--navy);cursor:pointer}
.gm-line .gm-w{background:#DBEAFE;border-color:#93C5FD}.gm-w:hover{border-color:var(--yellow-2,#F59E0B)}
.gm-row.ok .gm-line .gm-w{background:#DCFCE7;border-color:#86EFAC}
'''

JS = r'''
(function(){
  const box=document.getElementById('gmPrac'); if(!box) return;
  const T=box.dataset.type, D=window.GM_DATA, rows=[...box.querySelectorAll('.gm-row')], N=rows.length;
  const nm=s=>String(s).toLowerCase().replace(/[’`]/g,"'").replace(/\s+/g,' ').replace(/[.?!,]+$/,'').trim();
  const sc=()=>{ document.getElementById('gmScore').textContent=`✓ ${rows.filter(r=>r.classList.contains('ok')).length} / ${N}`; };
  const mark=(r,ok)=>{ r.classList.remove('ok','no'); r.classList.add(ok?'ok':'no'); r.querySelector('.gm-say').hidden=false; sc(); };
  const shuf=a=>{ a=a.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
  const toks=s=>s.split(' ');
  function setupOrder(r){ const i=+r.dataset.i, w=toks(D.items[i][0]); let o; do{ o=shuf(w); }while(w.length>2&&o.join(' ')===w.join(' '));
    r.querySelector('.gm-line').innerHTML=''; r.querySelector('.gm-bank').innerHTML=o.map(t=>`<button class="gm-w">${t.replace(/&/g,'&amp;').replace(/</g,'&lt;')}</button>`).join(''); }
  function reset(){ rows.forEach(r=>{ r.classList.remove('ok','no'); delete r.dataset.done; r.querySelector('.gm-say').hidden=true;
      r.querySelectorAll('.opt').forEach(o=>o.classList.remove('ok','no')); const g=r.querySelector('.gm-gap'); if(g) g.textContent='___';
      r.querySelectorAll('.gm-in').forEach(x=>{ x.value=''; x.classList.remove('ok','no'); }); const a=r.querySelector('.gm-ans'); if(a) a.textContent='';
      if(T==='order') setupOrder(r); }); sc(); }
  if(T==='choose') rows.forEach(r=>r.querySelectorAll('.opt').forEach(b=>b.onclick=()=>{ if(r.dataset.done) return; r.dataset.done=1; const a=D.items[+r.dataset.i][2];
      r.querySelectorAll('.opt').forEach(o=>{ if(o.dataset.o===a) o.classList.add('ok'); }); if(b.dataset.o!==a) b.classList.add('no'); r.querySelector('.gm-gap').textContent=a; mark(r,b.dataset.o===a); }));
  if(T==='order') box.addEventListener('click',ev=>{ const w=ev.target.closest('.gm-w'); if(!w) return; const r=w.closest('.gm-row'); if(r.classList.contains('ok')) return;
      r.classList.remove('no'); (w.parentElement.classList.contains('gm-bank')?r.querySelector('.gm-line'):r.querySelector('.gm-bank')).appendChild(w); });
  function check(show){ rows.forEach(r=>{ const it=D.items[+r.dataset.i];
      if(T==='type'){ const x=r.querySelector('.gm-in'); if(show){ x.value=it[1][0]; } if(!x.value.trim()&&!show) return; const ok=it[1].map(nm).includes(nm(x.value)); x.classList.toggle('ok',ok); x.classList.toggle('no',!ok); if(!ok) r.querySelector('.gm-ans').textContent='→ '+it[1][0]; mark(r,ok); }
      else if(T==='order'){ const line=r.querySelector('.gm-line');
        if(show){ const bank=r.querySelector('.gm-bank'); const all=[...line.children,...bank.children]; const used=new Set(); toks(it[0]).forEach(t=>{ const b=all.find(x=>!used.has(x)&&x.textContent===t); used.add(b); line.appendChild(b); }); }
        const got=[...line.children].map(b=>b.textContent).join(' '); if(!got&&!show) return; mark(r,got===it[0]); }
      else if(show&&!r.dataset.done){ const a=it[2]; r.dataset.done=1; r.querySelectorAll('.opt').forEach(o=>{ if(o.dataset.o===a) o.classList.add('ok'); }); r.querySelector('.gm-gap').textContent=a; r.querySelector('.gm-say').hidden=false; }
    }); }
  document.querySelectorAll('[data-gm]').forEach(b=>b.onclick=()=>{ const k=b.dataset.gm; if(k==='reset') reset(); else check(k==='show'); });
  reset();
})();
'''


def inject(page):
    if MARK in page: return page
    m = re.search(r'<b>(S\d\d)</b></span><span><b>\d\d</b></span></div>', page)
    if not m or m.group(1) not in G: return page
    sid = m.group(1); g = G[sid]
    anchor = page.find(f'<section class="slide" data-title="{e(g["before"], quote=True)}"')
    if anchor < 0: anchor = page.find(f'<section class="slide" data-title="{g["before"]}"')
    if anchor < 0: raise SystemExit(f'grammar: anchor slide not found in {sid}: {g["before"]}')
    foot = f'  <div class="s-foot"><span>A1 → A2 Communication Accelerator · <b>{sid}</b></span><span><b>00</b></span></div>\n'
    page = page[:anchor] + slides(sid, foot) + page[anchor:]
    n = [0]
    def num(mm): n[0] += 1; return f'<span><b>{n[0]:02d}</b></span></div>'
    page = re.sub(r'<span><b>\d\d</b></span></div>', num, page)
    # audio
    man_p = os.path.join(AUD, sid, 'manifest.json')
    man = json.load(open(man_p)) if os.path.exists(man_p) else {}
    offline = 'data:audio/mpeg;base64,' in page
    audio = {}
    for cid, fn, text, kind in clips(sid):
        if cid not in man: continue
        src = ('data:audio/mpeg;base64,' + base64.b64encode(open(os.path.join(AUD, sid, fn), 'rb').read()).decode()) if offline else f'../../grammar/audio/{sid}/{fn}'
        audio[cid] = {'file': f'Grammar/{fn}', 'label': text, 'src': src}
    pr = g['practice']
    data = {'type': pr['type'], 'items': pr['items']}
    i = page.find('<!--audiopolicy-->') if '<!--audiopolicy-->' in page else page.rfind('</body>')
    blob = (f'{MARK}<style>{CSS}</style><script>Object.assign(AUDIO,{json.dumps(audio, ensure_ascii=False)});'
            f'window.GM_DATA={json.dumps(data, ensure_ascii=False)};\n{JS}</script>\n')
    return page[:i] + blob + page[i:]


# ------------------------------------------------------------------ audio generation
def gen_audio(sids):
    import asyncio, certifi
    if os.environ.get('SSL_CA_BUNDLE'): certifi.where = lambda: os.environ['SSL_CA_BUNDLE']
    import edge_tts
    SONIA, LIBBY = 'en-GB-SoniaNeural', 'en-GB-LibbyNeural'

    async def run():
        sem = asyncio.Semaphore(6)
        async def one(p, text, voice):
            if os.path.exists(p) and os.path.getsize(p) > 0: return
            async with sem:
                for _ in range(4):
                    try:
                        await edge_tts.Communicate(text, voice, rate='-6%').save(p)
                        if os.path.getsize(p) > 0: return
                    except Exception as ex: print('retry', text, ex); await asyncio.sleep(2)
                raise SystemExit('failed ' + text)
        jobs = []
        for sid in sids:
            d = os.path.join(AUD, sid); os.makedirs(d, exist_ok=True); man = {}
            mp = os.path.join(d, 'manifest.json'); old = json.load(open(mp)) if os.path.exists(mp) else {}
            for cid, fn, text, kind in clips(sid):
                man[cid] = {'file': fn, 'label': text}
                if cid in old and old[cid]['label'] != text and os.path.exists(os.path.join(d, fn)): os.remove(os.path.join(d, fn))
                jobs.append(one(os.path.join(d, fn), text.replace(' — ', '. '), SONIA if kind == 'ex' else LIBBY))
            # drop stale files from an earlier version of the content
            for f in os.listdir(d):
                if f.endswith('.mp3') and f not in {v['file'] for v in man.values()}: os.remove(os.path.join(d, f))
            json.dump(man, open(os.path.join(d, 'manifest.json'), 'w'), indent=1, ensure_ascii=False)
        await asyncio.gather(*jobs)
    asyncio.run(run())


if __name__ == '__main__':
    if sys.argv[1:2] == ['audio']:
        gen_audio(sys.argv[2:] or sorted(G)); print('grammar audio ok')
