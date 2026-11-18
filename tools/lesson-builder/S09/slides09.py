# Slides for S09 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
import re as _re
S = []
S.append(slide('Cover', '''  <span class="chip c-input">Week 03 · Session 09</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Everyday<br><span>Services &amp;</span><br>Polite Requests</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

AG = [('warm', '☎️', 'Warm-up · Who do you call?', 'delivery · repair · customer service'),
      ('input', '🪜', 'The shape of a call', 'first → because → if possible → finally'),
      ('input', '🃏', 'Words → collocations', 'report an issue · confirm the details…'),
      ('input', '🪶', 'Softer &amp; politer', 'there seems to be · could · would'),
      ('prac', '🌡', 'Politeness meter', 'choose the most polite'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('listen', '🎯', 'Find the stress', 'PROBLEM + ACTION'),
      ('listen', '🎧', 'Listening', 'Computer problems'),
      ('listen', '☕', 'Model dialogue', 'a broken coffee machine'),
      ('speak', '📞', '2-minute service call', 'caller card + agent screen'),
      ('speak', '🎙', 'Real-life task', 'a 45-second voice message'),
      ('prac', '⏱', 'Game: Quick replies', 'answer in 10 seconds')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

OBJ = [('☎️', 'Start a service call', "I'm calling about my order."),
       ('⚠️', 'Explain a problem politely', 'There seems to be a problem with…'),
       ('🙏', 'Make polite requests', 'Could you check… for me? · Would you…?'),
       ('🔀', 'Ask for options', 'What are my options?'),
       ('✅', 'Confirm the solution', 'Could you confirm the details?')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: who do you call?
PR = ''.join(f'<button class="wpr" data-wp="{i}"><span class="wpe">{em}</span><span class="wpt">{e(t)}</span></button>' for i, (em, t, s) in enumerate(C.PROBLEMS))
BN = ''.join(f'<div class="wbin" data-wb="{k}"><div class="wbh"><span>{em}</span>{e(n)}</div><div class="wbl" id="wbl{k}"></div></div>' for k, em, n in C.SERVICES)
S.append(slide('Warm-up: Who do you call?', head('Warm-up', 'c-warm', 'Who do you <em>call</em>?') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="wprs">{PR}</div>
    <div class="col wbins">{BN}</div>
  </div>
  <div class="ftools"><span>1️⃣ Click a problem · 2️⃣ Click the right phone · then say: “I'm calling about…”</span><span class="score" id="wpScore">✓ 0 / {len(C.PROBLEMS)}</span><button class="btn sm ghost" id="wpReset">↺ Reset</button></div>
'''))

# 5 the shape of a call
def lk(t, w):
    return e(t).replace(e(w), f'<b class="lkx">{e(w)}</b>', 1) if w else e(t)


ST = ''.join(f'<div class="cst2" id="cs{i}"><div class="csn"><span>{i + 1}</span>{e(s)}</div><div class="csb">{pb(f"CL_{i}")}<div><p>{lk(t, w)}</p><small>{e(v)}</small></div></div></div>'
             for i, (s, w, t, v) in enumerate(C.CALL))
S.append(slide('The shape of a call', head('Input · A service call', 'c-input', 'The <em>shape</em> of a service call') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col" style="width:300px;flex:none;gap:10px"><div class="lart">{I.CALL_ART}</div>
      <div class="card lkflow"><div class="rh">🔗 Linkers</div><div class="lkchain"><b>first</b>→<b>because</b>→<b>if possible</b>→<b>therefore</b>→<b>finally</b></div></div>
      <div class="row" style="gap:8px"><button class="btn y grow" id="csNext">Next step →</button><button class="btn ghost" id="csAll">👁 All</button></div>
      <button class="btn sm ghost" id="csReset">↺ Reset</button>
    </div>
    <div class="col grow csflow">{ST}</div>
  </div>
'''))

# 6-7 words → collocations
WTOOLS = '  <div class="ftools"><span>↻ Click a card to flip</span><button class="btn sm ghost" data-flipall>🔄 Flip all</button><button class="btn sm ghost" data-flipreset>↺ Reset</button></div>\n'


def word_card(i, v):
    return (f'<div class="flip wc" data-flip><div class="in"><div class="fc"><div class="art">{I.WORD[v["k"]]}</div>'
            f'<div class="fwd"><b>{e(v["w"])}<span class="fipa">{e(v["ipa"])}</span></b>{pb("VW_" + str(i))}</div><span class="turn">↻</span></div>'
            f'<div class="bk"><span class="pos">{e(v["pos"])}</span><b>{e(v["w"])}</b><span class="ipa">{e(v["ipa"])}</span><span class="vi">{e(v["vi"])}</span>{pb("VW_" + str(i), "y")}</div></div></div>')


def phrase_card(i, v):
    col = e(v['col']).replace(e(v['kw']), f'<em>{e(v["kw"])}</em>', 1)
    return (f'<div class="flip pc" data-flip><div class="in"><div class="fc"><div class="art">{I.PHRASE[v["k"]]}</div>'
            f'<div class="fwd"><b>{col}</b>{pb("VC_" + str(i))}</div><span class="turn">↻</span></div>'
            f'<div class="bk"><b>{e(v["col"])}</b><span class="vi">{e(v["col_vi"])}</span><span class="ex">“{e(v["ex"])}”</span>{pb("VC_" + str(i), "y")}</div></div></div>')


for part, idx in ((1, range(0, 4)), (2, range(4, 8))):
    S.append(slide(f'Words → collocations {part}', head(f'Input · Words &amp; collocations {part}/2', 'c-input', 'Word → <em>collocation</em>') +
                   '  <div class="fgrid wcgrid">' + ''.join(word_card(i, C.VOCAB[i]) for i in idx) + ''.join(phrase_card(i, C.VOCAB[i]) for i in idx) + '</div>\n' + WTOOLS))

# 8 softer & politer (grammar input)
GB = ''.join(f'<div class="gfr"><b>{e(f)}</b><span>{e(v)}</span><div class="gqe">{pb(f"GR_{i}")}<span>{e(x)}</span></div></div>' for i, (f, v, x) in enumerate(C.GRAM))
TH = ''.join(f'<div class="thc" data-th><div class="thd">😐 {e(d)}</div><div class="ths">{pb(f"TH_{i}", "y")}<span>🙂 {e(s).replace("There seems to be", "<b>There seems to be</b>")}</span></div><div class="thm">👆 Say it softer, then click</div></div>'
             for i, (d, s) in enumerate(C.THERE))
S.append(slide('Softer & politer', head('Input · Grammar', 'c-input', '<em>There seems to be…</em> · Could you…? · Would you…?') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col gfbox" style="width:400px;flex:none">{GB}<div class="tip" style="font-size:15px">💡 <b>There seems to be</b> = softer than “X is broken”. It sounds calm and polite.</div></div>
    <div class="col grow" style="gap:8px;min-width:0"><div class="thgrid">{TH}</div>
      <div class="ftools" style="margin-top:0"><span>Direct 😐 → softer 🙂</span><button class="btn sm ghost" id="thAll">👁 All</button><button class="btn sm ghost" id="thReset">↺ Reset</button></div></div>
  </div>
'''))

# 9 politeness meter
PM = ''.join(f'<div class="pmr" id="pm{i}"><span class="n">{i + 1}</span><div class="pmo">' + ''.join(f'<button class="opt" data-pm="{i}" data-o="{k}">{e(o)}</button>' for k, o in enumerate(opts)) + '</div></div>'
             for i, (opts, a) in enumerate(C.POLITE))
S.append(slide('Politeness meter', head('Practice · Polite requests', 'c-prac', 'Politeness meter — <em>choose the most polite</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow pmbox" style="min-width:0">{PM}</div>
    <div class="card pmeter"><div class="rh">🌡 Politeness</div><div class="pmbar"><i id="pmFill"></i></div><div class="pmlab"><span>😊 polite</span><span>😐 OK</span><span>😠 rude</span></div><div class="score" id="pmScore">✓ 0 / {len(C.POLITE)}</div></div>
  </div>
  <div class="ftools"><span>Then read the polite one aloud with a friendly voice ↗</span><button class="btn sm ghost" id="pmReset">↺ Reset</button></div>
'''))

for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))


# 14 find the stress
def stress_row(i, t):
    ws = t.split()
    btns = ''.join(f'<button class="swd" data-sw="{i}" data-st="{1 if _re.sub(r"[^A-Za-z]", "", w).isupper() and len(_re.sub(r"[^A-Za-z]", "", w)) > 1 else 0}">{e(w if not (_re.sub(r"[^A-Za-z]", "", w).isupper() and len(_re.sub(r"[^A-Za-z]", "", w)) > 1) else w.lower())}</button>' for w in ws)
    return f'<div class="swr" id="sr{i}">{pb(f"ST_{i}")}<div class="sws">{btns}</div></div>'


S.append(slide('Find the stress', head('Pronunciation', 'c-listen', 'Find the <em>stress</em> — PROBLEM + ACTION') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow swbox2" style="min-width:0">{''.join(stress_row(i, t) for i, t in enumerate(C.STRESS))}</div>
    <div class="col" style="width:300px;flex:none;gap:10px">
      <div class="card pnote"><div class="rh">🎯 Two strong words</div><p>Make the <b>problem</b> and the <b>action</b> words <b>BIG</b>:</p><p>Could you <b>CHECK</b> the <b>DELIVERY</b>?</p></div>
      <div class="card pnote"><div class="rh">🎵 Polite voice</div><p><b>↗</b> Could you…? Would you…?</p><p>Friendly, not flat. Say <b>please</b>. 🙂</p></div>
      <button class="btn y" id="swCheck">✓ Check</button><button class="btn sm ghost" id="swReset">↺ Reset</button>
    </div>
  </div>
  <div class="ftools" style="margin-top:6px"><span>🔊 Listen · click the 2 strong words in each sentence · then say it</span><span class="score" id="swScore">🎯 ?</span></div>
'''))

# 15 listening (real recording, played from the source)
L = C.LISTEN
S.append(slide('Listening: Computer problems', head('Listening', 'c-listen', 'Computer problems — <em>a real conversation</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.REPAIR_ART}</div>
      <div class="card lsrc">
        <div class="lt">🎧 {e(L['title'])}</div>
        <div class="row" style="gap:8px"><button class="btn" data-a="EL">▶ Normal</button><button class="btn ghost" data-a="EL2">▶ Slower</button></div>
        <div class="lsm">Source: {e(L['source'])}<br>{e(L['gloss'])}</div>
      </div>
      <button class="btn y" id="lCheck">✓ Check answers</button><a class="btn ghost" id="lScript" href="{L['page']}" target="_blank" rel="noopener">📜 Script (source page) ↗</a>
    </div>
    <div class="col grow" style="gap:6px;min-width:0;position:relative">
      <div id="lgist"></div>
      <div id="ldetail" class="col" style="gap:6px;flex:1"></div>
    </div>
  </div>
'''))

# 16 model dialogue
CF = ''.join(f'<div class="cfld"><label>{e(lb)}</label><input id="cf{i}" autocomplete="off" spellcheck="false"><span class="cfa" id="cfa{i}"></span></div>'
             for i, (lb, a, ok) in enumerate(C.CARD))
S.append(slide('Model dialogue: customer service', head('Model dialogue', 'c-listen', 'Calling customer service — <em>a broken coffee machine</em>') + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec nc8">
        <div class="fhd">🎫 Service ticket <span>LISTEN &amp; WRITE</span></div>
        {CF}
        <div class="row"><button class="btn sm" id="cfCheck">✓ Check</button><button class="btn sm y" id="cfShow">👁 Answers</button></div>
      </div>
      <div id="dq" class="col" style="gap:8px"></div>
    </div>
    <div class="card" style="display:flex;flex-direction:column;min-height:0">
      <div class="row" style="padding:12px 14px 4px;align-items:center;flex-wrap:wrap;gap:8px">
        <button class="btn sm" id="dlgPlay">▶ Play dialogue</button>
        <button class="btn sm ghost" id="dlgStop">⏹ Stop</button>
        <button class="btn sm y" id="dlgScript">👁 Show script</button>
        <span id="dlgDl"></span>
      </div>
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">A = Agent · C = Customer</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# 17 2-minute service call
STG = ''.join(f'<label class="stg"><input type="checkbox"><span>{ic}</span>{e(t)}</label>' for ic, t in C.STAGES)
S.append(slide('2-minute service call', head('Speaking · Service call', 'c-speak', 'A 2-minute <em>service call</em>') + f'''  <div class="row" style="gap:14px;flex:1;min-height:0">
    <div class="rcard small sccard" id="scCaller"><div class="rce">📞</div><div class="rct">Caller card</div><div class="rcx">Click “New call”. The caller reads this card only.</div></div>
    <div class="card scagent"><div class="sch">🖥 Agent screen <button class="btn sm ghost" id="scHide">🙈 Hide</button></div><div id="scAgent" class="sca"><span class="muted">Options appear here. Only the agent looks!</span></div></div>
    <div class="col" style="width:290px;flex:none;gap:8px">
      <button class="btn y" id="scNew">🎲 New call</button>
      <div class="card tkc"><div id="tkTime" class="tkt">2:00</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn ghost" id="tkStart">⏱ Start 2 minutes</button>
      <div class="card stgs"><div class="rh">✅ Listener ticks:</div>{STG}</div>
    </div>
  </div>
'''))

# 18 real-life task: 45-second voice message
PL = ''.join(f'<div class="vmp"><span class="n">{n}</span>{e(t)}</div>' for n, t in C.VM_PLAN)
S.append(slide('Real-life task: voice message', head('Real-life task', 'c-speak', 'Record a <em>45-second</em> voice message') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card vmplan"><div class="rh">📝 Plan your message <button class="btn sm ghost" id="vmIdea">🎲 Idea</button></div><div class="vmidea" id="vmIdeaTx">Choose a problem: late delivery · broken TV · extra charge…</div>{PL}</div>
    <div class="card vmrec">
      <div class="vmt" id="vmTime">0:45</div><div class="tbar"><i id="vmBar"></i></div>
      <div class="vmst" id="vmSt">🎙 Press record and speak to customer service.</div>
      <div class="row" style="gap:8px;justify-content:center"><button class="btn y" id="vmRec">● Record</button><button class="btn ghost" id="vmStop" disabled>■ Stop</button></div>
      <audio id="vmAudio" controls hidden></audio><a class="btn sm ghost" id="vmDl" hidden download="S09_voice_message.webm">⬇ Download my message</a>
      <div class="tip" style="font-size:14.5px">📲 After class: record your message (45 s) and send it to the class group.</div>
    </div>
  </div>
'''))

# 19 game: quick replies
S.append(slide('Game: Quick replies', head('Game', 'c-prac', 'Quick replies — <em>you are the agent!</em>') + f'''  <div class="col lfbox qrbox" style="flex:1;min-height:0">
    <div class="row" style="justify-content:space-between"><span class="score" id="qrN">Call 0 / {len(C.REPLIES)}</span><span class="qrt" id="qrT">⏱ 10</span><span class="score" id="qrScore">Score: 0 · 🔥 0</span></div>
    <div class="qrq" id="qrQ"><b>☎️ Ready?</b><span>A customer calls. Choose the best reply in 10 seconds — then say it!</span></div>
    <div class="qros" id="qrO"></div>
    <div class="row" style="gap:8px;justify-content:center"><button class="btn y" id="qrGo">Next call →</button><button class="btn sm ghost" id="qrAgain">🔊 Again</button></div>
  </div>
'''))

WRAP = [('☎️', "I can start a call: Hello. I'm calling about my order."),
        ('⚠️', 'I can explain: There seems to be a problem with…'),
        ('🙏', 'I can ask politely: Could you check… for me? Would you…?'),
        ('🔀', 'I can ask: What are my options? — I\'d like to request a replacement.'),
        ('✅', 'I can finish: Could you confirm the details? Thank you for your help!')]
KEY = [v['col'] for v in C.VOCAB] + ["I'm calling about…", 'There seems to be a problem with…', 'Could you check … for me?', 'What are my options?', 'first · because · therefore · if possible · finally']
S.append(slide('Wrap-up', head('Wrap-up', 'c-wrap', 'What can you <em>do now</em>?') + '  <div class="row" style="gap:18px;flex:1;min-height:0">\n    <div class="col grow wrap2">' +
               ''.join(f'<label class="chk"><span class="wi">{ic}</span><span class="grow">{e(t)}</span><input type="checkbox"></label>' for ic, t in WRAP) +
               '</div>\n    <div class="card keys"><div class="rh">🔑 Key language</div><div class="kchips">' + ''.join(f'<span>{e(k)}</span>' for k in KEY) + '</div></div>\n  </div>\n'))

S.append(slide('Homework', head('Homework', 'c-listen', 'After class') + f'''  <div class="hw hw2">
    <div class="card"><h3>📝 Homework · 5 parts</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div><b>Vocabulary test</b> — today's words &amp; collocations</div></div>
        <div class="step"><span class="n">2</span><div><b>Reading</b> — a text with today's words</div></div>
        <div class="step"><span class="n">3</span><div><b>Listening</b> — audio, script after you finish</div></div>
        <div class="step"><span class="n">4</span><div><b>Shadowing</b> — read aloud &amp; record → score <b>/10</b> (<span style="color:#16A34A">green</span> = correct, <span style="color:#DC2626">red</span> = fix it)</div></div>
        <div class="step"><span class="n">5</span><div><b>Translation</b> — Vietnamese → English with today's structures</div></div>
      </div>
    </div>
    <div class="card qrcard"><h3>📝 Open the homework</h3>{qr_svg(HW_URL)}
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S09 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 10</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Past Events: What Happened?</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
