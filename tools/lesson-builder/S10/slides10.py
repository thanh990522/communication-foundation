# Slides for S10 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
S = []
S.append(slide('Cover', '''  <span class="chip c-input">Week 04 · Session 10</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Past Events:<br><span>What</span><br>Happened?</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

AG = [('warm', '📸', 'Warm-up · Weekend photos', 'Last weekend, I…'),
      ('input', '⏪', 'Verb time machine', 'visit → visited · go → went'),
      ('input', '🃏', 'Words → collocations', 'attend an event · return home…'),
      ('input', '📘', 'Grammar', 'past simple ➕ ➖ · was / were'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('listen', '🔊', '-ed endings', '/t/ · /d/ · /ɪd/'),
      ('listen', '🎧', 'Listening', 'How was your trip?'),
      ('listen', '🌸', 'Model dialogue', "Nam's weekend in Da Lat"),
      ('speak', '🧩', 'My weekend story', 'first → then → in the end'),
      ('speak', '🤥', 'Two truths and a lie', "No, you didn't…!"),
      ('speak', '⏱', '90-second talk', 'six past verbs'),
      ('prac', '⚡', 'Game: Irregular quick-fire', '6 seconds each')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

OBJ = [('📅', 'Say what you did', 'Last weekend, I visited a local market.'),
       ('🚫', "Say what you didn't do", "We didn't go to the waterfall."),
       ('⭐', 'Give the best part', 'The best part was the night market.'),
       ('😩', 'Say how you felt', 'I was exhausted, but it was worth it.'),
       ('🧩', 'Tell a 90-second story', 'first · then · after that · although · in the end')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: weekend photos
PH = ''.join(f'<div class="phc" data-ph><div class="phe">{em}</div><div class="pht">{pb(f"PH_{i}")}<span>{e(t)}</span></div><div class="phq">❓ What did I do?</div></div>'
             for i, (em, t) in enumerate(C.PHOTOS))
S.append(slide('Warm-up: Weekend photos', head('Warm-up', 'c-warm', "Teacher's weekend photos — <em>what did I do?</em>") +
               f'  <div class="phgrid">{PH}</div>\n  <div class="ftools"><span>Guess first: “Last weekend, you…” · then click the photo</span><button class="btn sm ghost" id="phAll">👁 All</button><button class="btn sm ghost" id="phReset">↺ Reset</button></div>\n'))

# 5 verb time machine
def vt(i, b, p_, ip, kind):
    return (f'<div class="vtc {kind}" data-vt><div class="vtb">{e(b)}</div><div class="vtp"><b>{e(p_)}</b><span class="fipa">{e(ip)}</span></div>'
            f'{pb(f"VT_{i}")}</div>')


RG = ''.join(vt(i, b, p_, ip, 'reg') for i, (b, p_, ip) in enumerate(C.REGULAR))
IR = ''.join(vt(i + len(C.REGULAR), b, p_, ip, 'irr') for i, (b, p_, ip) in enumerate(C.IRREGULAR))
S.append(slide('Verb time machine', head('Input · Past forms', 'c-input', 'Verb time machine ⏪ — <em>now → past</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col vtcol" style="width:330px;flex:none"><div class="vth reg">✅ Regular: verb + <b>-ed</b></div><div class="vtgrid vg2">{RG}</div>
      <div class="tip" style="font-size:14.5px">stay → stay<b>ed</b> · visit → visit<b>ed</b><br>enjoy → enjoy<b>ed</b></div></div>
    <div class="col vtcol grow" style="min-width:0"><div class="vth irr">⚡ Irregular: learn by heart!</div><div class="vtgrid vg4">{IR}</div></div>
  </div>
  <div class="ftools"><span>Click a card: present → past · say both forms</span><button class="btn sm ghost" id="vtAll">⏪ All</button><button class="btn sm ghost" id="vtReset">↺ Reset</button></div>
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

for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))

# -ed endings
RU = ''.join(f'<div class="edr"><b>{e(s)}</b><span>{e(r)}</span><i>{e(x)}</i></div>' for s, r, x in C.ED_RULES)
EW = ''.join(f'<div class="edw" id="ed{i}">{pb(f"ED_{i}")}<b>{e(w)}</b><span class="edo">' + ''.join(f'<button class="opt" data-ed="{i}" data-o="{s}">{s}</button>' for s in ('/t/', '/d/', '/ɪd/')) + '</span></div>'
             for i, (w, s) in enumerate(C.ED_WORDS))
S.append(slide('-ed endings', head('Pronunciation', 'c-listen', '-ed endings — <em>/t/ · /d/ · /ɪd/</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col edrules" style="width:330px;flex:none">{RU}<div class="tip" style="font-size:14.5px">💡 Only <b>/ɪd/</b> adds a new syllable: vis-i-<b>ted</b> · at-ten-<b>ded</b>.<br>walked = /wɔːkt/ (1 syllable!)</div></div>
    <div class="edgrid">{EW}</div>
  </div>
  <div class="ftools"><span>🔊 Listen · choose the sound · say it</span><span class="score" id="edScore">✓ 0 / {len(C.ED_WORDS)}</span><button class="btn sm ghost" id="edReset">↺ Reset</button></div>
'''))

# listening (real recording, played from the source)
L = C.LISTEN
S.append(slide('Listening: How was your trip?', head('Listening', 'c-listen', 'How was your trip? — <em>a real conversation</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.HOLIDAY_ART}</div>
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

# model dialogue
CF = ''.join(f'<div class="cfld"><label>{e(lb)}</label><input id="cf{i}" autocomplete="off" spellcheck="false"><span class="cfa" id="cfa{i}"></span></div>'
             for i, (lb, a, ok) in enumerate(C.CARD))
S.append(slide("Model dialogue: Nam's weekend", head('Model dialogue', 'c-listen', "Monday morning — <em>Nam's weekend</em>") + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec nc8">
        <div class="fhd">📝 Weekend notes <span>LISTEN &amp; WRITE</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">A = Anna · N = Nam</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# my weekend story builder
EV = ''.join(f'<button class="sev" data-sev="{i}"><span>{em}</span>{e(t)}</button>' for i, (em, t) in enumerate(C.STORY_EVENTS))
AL = ''.join(f'<button class="opt sal" data-al="{e(a)}">{e(a)}</button>' for a in C.ALTHOUGH)
S.append(slide('My weekend story', head('Speaking · Story builder', 'c-speak', 'My weekend story — <em>first → then → in the end</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col" style="width:420px;flex:none;gap:8px">
      <div class="rh2">1️⃣ Click 4 things you did — in order</div><div class="sevs">{EV}</div>
      <div class="rh2">2️⃣ Although…</div><div class="sals">{AL}</div>
      <button class="btn sm ghost" id="stReset">↺ Start again</button>
    </div>
    <div class="card stout"><div class="rh">🗣 My story <span class="muted" id="stN">0 / 4</span></div><div id="stTx" class="sttx"><span class="muted">Your story appears here. Then tell it to your partner!</span></div></div>
  </div>
'''))

# two truths and a lie
S.append(slide('Two truths and a lie', head('Speaking · Game', 'c-speak', "Two truths and a lie — <em>No, you didn't…!</em>") + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="ttcard" id="ttTopic"><span>🎲</span><b>Topic: last weekend</b></div>
      <div class="card ttsteps">
        <div class="tts"><b>1</b><span>Speaker: say <b>3 sentences</b> about the topic — 2 true, 1 false.<br><i>Last weekend, I visited a local market. I stayed overnight at my friend's house. I didn't eat any street food.</i></span></div>
        <div class="tts"><b>2</b><span>Listeners: find the lie!<br><i>I think you didn't stay overnight at your friend's house!</i></span></div>
        <div class="tts"><b>3</b><span>Speaker: <i>Yes, that's the lie! / No — I really stayed there! I was exhausted, but it was worth it.</i></span></div>
      </div>
    </div>
    <div class="col" style="width:290px;flex:none;gap:10px">
      <button class="btn y" id="ttNew">🎲 New topic</button>
      <div class="card tkc"><div id="ttTime" class="tkt">1:00</div><div class="tbar"><i id="ttBar"></i></div></div>
      <button class="btn ghost" id="ttStart">⏱ Start 60 seconds</button>
      <div class="tip" style="font-size:15px">➖ Negative: <b>didn't + verb</b><br>❌ I didn't went ✅ I didn't <b>go</b></div>
    </div>
  </div>
'''))

# 90-second talk: six past verbs
TV = ''.join(f'<button class="tvb" data-tv>{e(v)}</button>' for v in C.TALK_VERBS)
S.append(slide('90-second talk', head('Speaking · Output', 'c-speak', '90-second talk — <em>use six past verbs</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="card tvplan"><div class="rh">🗺 Plan</div>
        <p>👉 <b>Last weekend, I…</b> (where? who with?)</p><p>👉 <b>First… Then… After that…</b> (3 things you did)</p>
        <p>👉 <b>I had a chance to…</b> · <b>The best part was…</b></p><p>👉 <b>Although…</b> · <b>In the end, I was…, but it was worth it.</b></p></div>
      <div class="card tvbox"><div class="rh">✋ Listener: click each past verb you hear <span class="score" id="tvN">0 / 6</span></div><div class="tvs">{TV}</div></div>
    </div>
    <div class="col" style="width:290px;flex:none;gap:10px">
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn y" id="tkStart">⏱ Start 90 seconds</button><button class="btn sm ghost" id="tvReset">↺ Reset verbs</button>
      <div class="tip" style="font-size:15px">🎯 Goal: <b>6 past verbs</b> + 1 negative (<b>didn't</b>).</div>
    </div>
  </div>
'''))

# real-life task: yesterday card
YC = ''.join(f'<div class="ycl"><span>{em}</span><label>{e(t.split("___")[0])}</label><input id="yc{i}" autocomplete="off" placeholder="…">{e(t.split("___")[1])}</div>' for i, (em, t) in enumerate(C.YESTERDAY))
S.append(slide('Real-life task: yesterday', head('Real-life task', 'c-speak', 'Tell someone about <em>yesterday</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card ycard"><div class="rh">📝 My yesterday</div>{YC}<button class="btn sm" id="ycMake">✨ Make my text</button></div>
    <div class="card ycout"><div class="rh">🗣 Say it</div><div id="ycTx" class="sttx"><span class="muted">Fill in the card, then click “Make my text”.</span></div>
      <div class="tip" style="font-size:15px">📲 After class: tell <b>one person</b> in English about one thing you did yesterday.</div></div>
  </div>
'''))

# game: irregular quick-fire
S.append(slide('Game: Irregular quick-fire', head('Game', 'c-prac', 'Irregular quick-fire ⚡ — <em>type the past form</em>') + f'''  <div class="col lfbox qfbox" style="flex:1;min-height:0">
    <div class="row" style="justify-content:space-between"><span class="score" id="qfN">Round 0 / {len(C.QUICK)}</span><span class="qrt" id="qfT">⏱ 6</span><span class="score" id="qfScore">Score: 0</span></div>
    <div class="qfq" id="qfQ"><b>⚡ Ready?</b><span>A verb appears. Type the past form in 6 seconds!</span></div>
    <div class="row" style="gap:8px;justify-content:center"><input id="qfIn" class="qfin" autocomplete="off" spellcheck="false" placeholder="past form"><button class="btn" id="qfOk">✓</button></div>
    <div class="row" style="gap:8px;justify-content:center"><button class="btn y" id="qfGo">Next verb →</button></div>
  </div>
'''))

WRAP = [('📅', 'I can say what I did: Last weekend, I visited a local market.'),
        ('🚫', "I can say what I didn't do: We didn't go to the waterfall."),
        ('⭐', 'I can say: I had a chance to… The best part was…'),
        ('😩', 'I can say: I was exhausted, but it was worth it.'),
        ('🔊', 'I can say -ed endings: walked /t/ · stayed /d/ · visited /ɪd/')]
KEY = [v['col'] for v in C.VOCAB] + ['Last weekend, I…', 'I had a chance to…', 'The best part was…', 'I was…, but it was worth it.', 'first · then · after that · although · in the end']
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
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S10 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 11</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Past Questions &amp; Storytelling</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
