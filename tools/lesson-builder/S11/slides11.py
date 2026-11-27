# Slides for S11 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
S = []
S.append(slide('Cover', '''  <span class="chip c-input">Week 04 · Session 11</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Past Questions<br><span>&amp; Storytelling</span></h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

AG = [('warm', '🔍', 'Warm-up · Guess the story', '3 picture clues'),
      ('input', '⛰', 'The story mountain', 'at first → suddenly → in the end'),
      ('input', '🃏', 'Words → collocations', 'miss the bus · suddenly realise…'),
      ('input', '📘', 'Grammar', 'Did…? · Was / Were…? · Who called?'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('prac', '❓', 'Question maker', 'answer → question'),
      ('listen', '🎵', 'Follow-up questions', '↗ ↘ · pause after linkers'),
      ('listen', '🎧', 'Listening', 'Lost property'),
      ('listen', '🚌', 'Model dialogue', "Linh's bad morning"),
      ('speak', '🎲', 'Story dice', '2-minute story + 3 questions'),
      ('speak', '💬', 'Real-life task', '3 follow-up questions'),
      ('prac', '🧩', 'Game: Story jigsaw', 'put the story in order')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

OBJ = [('😲', 'Start a story', "You'll never guess what happened!"),
       ('⏳', 'Set the scene', 'While I was waiting for the bus, …'),
       ('⚡', 'Tell it in order', 'at first · suddenly · fortunately · eventually · in the end'),
       ('❓', 'Ask past questions', 'Did you…? Were you…? Where did you…?'),
       ('🔁', 'Keep the story going', 'What happened next?')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: guess the story
CL = ''.join(f'<div class="gsc" data-gs data-k="0"><div class="gse">' + ''.join(f'<span class="gsi" data-n="{k}">{x}</span>' for k, x in enumerate(cl)) +
             f'</div><div class="gst">{pb(f"GS_{i}")}<span>{e(t)}</span></div><div class="gsh">👆 Click for the next clue</div></div>' for i, (cl, t) in enumerate(C.CLUES))
S.append(slide('Warm-up: Guess the story', head('Warm-up', 'c-warm', 'Guess the story — <em>what happened?</em>') +
               f'  <div class="gsgrid">{CL}</div>\n  <div class="ftools"><span>Each click = one more clue · guess before the last click!</span><button class="btn sm ghost" id="gsAll">👁 All</button><button class="btn sm ghost" id="gsReset">↺ Reset</button></div>\n'))

# 5 story mountain
MT = ''.join(f'<button class="mts" data-mt="{i}" style="--x:{[3, 13, 22, 50, 58, 64][i]}%;--y:{[84, 58, 24, 16, 52, 84][i]}%"><b>{i + 1}</b>{e(l)}</button>' for i, (l, t) in enumerate(C.MOUNTAIN))
ML = ''.join(f'<div class="mtl" id="mtl{i}">{pb(f"MT_{i}")}<span>{e(t).replace(e(l), f'<b>{e(l)}</b>', 1)}</span></div>' for i, (l, t) in enumerate(C.MOUNTAIN))
S.append(slide('The story mountain', head('Input · Storytelling', 'c-input', 'The story <em>mountain</em> ⛰') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card mtbox"><svg viewBox="0 0 100 60" preserveAspectRatio="none" class="mtsvg"><path d="M0 58 L24 30 L42 10 L58 10 L76 30 L100 58 Z" fill="#E0ECFF" stroke="#1D4ED8" stroke-width=".6"/><path d="M6 52 L24 33 L42 13 L58 13 L76 33 L94 52" fill="none" stroke="#F59E0B" stroke-width=".8" stroke-dasharray="2 1.4"/></svg>{MT}</div>
    <div class="col grow mtlist" style="min-width:0">{ML}</div>
  </div>
  <div class="ftools"><span>Click each step on the mountain · listen · say it</span><button class="btn sm ghost" id="mtAll">👁 All</button><button class="btn sm ghost" id="mtReset">↺ Reset</button></div>
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

# question maker
QM = ''.join(f'<div class="qmr" id="qm{i}"><span class="n">{i + 1}</span><div class="qma">💬 {e(a)}</div><div class="qmq"><i>{e(h)}</i><input class="qmin" autocomplete="off" spellcheck="false" placeholder="Your question…"></div><span class="qmok"></span></div>'
             for i, (a, qs, h) in enumerate(C.QMAKER))
S.append(slide('Question maker', head('Practice · Past questions', 'c-prac', 'Question maker — <em>what was the question?</em>') +
               f'  <div class="qmgrid">{QM}</div>\n  <div class="ftools"><span>Type the question · then ask your partner the same question!</span><span class="score" id="qmScore">✓ 0 / {len(C.QMAKER)}</span><button class="btn sm" id="qmCheck">✓ Check</button><button class="btn sm y" id="qmShow">👁 Answers</button><button class="btn sm ghost" id="qmReset">↺ Reset</button></div>\n'))

# pronunciation: follow-up questions + pauses
FQ = ''.join(f'<button class="lline lnk {"up" if a == "↗" else "dn"}" data-a="FQ_{i}">{P}<span>{e(t)} <b class="arr">{a}</b></span></button>' for i, (t, a) in enumerate(C.FOLLOW))
PS = ''.join(f'<button class="lline pz" data-a="PZ_{i}">{P}<span>{e(t).replace("|", "<b class=pzm>‖</b>")}</span></button>' for i, t in enumerate(C.PAUSES))
I1 = ','.join(f'FQ_{i}' for i in range(len(C.FOLLOW))); I2 = ','.join(f'PZ_{i}' for i in range(len(C.PAUSES)))
S.append(slide('Follow-up questions & pauses', head('Pronunciation', 'c-listen', 'Follow-up questions <em>↗ ↘</em> · pause after linkers <em>‖</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card lkbox" style="flex:1;width:auto"><div class="rh">❓ Follow-up questions <button class="btn sm y rep" data-rep="{I1}">🔁 Listen &amp; repeat</button></div>{FQ}
      <div class="tip" style="font-size:14.5px">Wh- question ↘ (What, Where, How) · Yes/No question ↗ (Did…? Were…?)</div></div>
    <div class="card lkbox" style="flex:1;width:auto"><div class="rh">‖ Pause after the linker <button class="btn sm y rep" data-rep="{I2}">🔁 Listen &amp; repeat</button></div>{PS}
      <div class="tip" style="font-size:14.5px">Small pause after <b>At first, Suddenly, Fortunately…</b> → the listener waits for the next part! 😮</div></div>
  </div>
'''))

# listening (real recording, played from the source)
L = C.LISTEN
SLOW = f'<button class="btn ghost" data-a="EL2">▶ Slower</button>' if L['url_slow'] else ''
S.append(slide('Listening: Lost property', head('Listening', 'c-listen', 'Lost property — <em>a real conversation</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.AIRPORT_ART}</div>
      <div class="card lsrc">
        <div class="lt">🎧 {e(L['title'])}</div>
        <div class="row" style="gap:8px"><button class="btn" data-a="EL">▶ Play</button>{SLOW}</div>
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
S.append(slide("Model dialogue: Linh's morning", head('Model dialogue', 'c-listen', "You'll never guess… — <em>Linh's bad morning</em>") + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec nc8">
        <div class="fhd">📝 Story notes <span>LISTEN &amp; WRITE</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">L = Linh · T = Tom</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# story dice
QK = ''.join(f'<label class="stg"><input type="checkbox"><span>{ic}</span>{e(t)}</label>' for ic, t in (('❓', 'Did you…?'), ('❓', 'Was / Were…?'), ('❓', 'Where / What / How…?'), ('🔁', 'What happened next?')))
S.append(slide('Story dice', head('Speaking · Output', 'c-speak', 'Story dice 🎲 — <em>a 2-minute story</em>') + f'''  <div class="row" style="gap:14px;flex:1;min-height:0">
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="dice"><div class="die" id="dP"><span>📍 Place</span><b>?</b></div><div class="die" id="dR"><span>⚠️ Problem</span><b>?</b></div><div class="die" id="dL"><span>🍀 Luck</span><b>?</b></div></div>
      <div class="card dplan"><div class="rh">🗺 Your story</div>
        <p>😲 <b>You'll never guess what happened!</b></p><p>⏳ <b>At first,</b> … <b>While I was</b> … (place)</p>
        <p>⚡ <b>Suddenly,</b> … (problem) · 🍀 <b>Fortunately,</b> … (luck)</p><p>🏁 <b>Eventually,</b> … <b>In the end,</b> …</p></div>
    </div>
    <div class="col" style="width:290px;flex:none;gap:8px">
      <button class="btn y" id="dRoll">🎲 Roll the dice</button>
      <div class="card tkc"><div id="tkTime" class="tkt">2:00</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn ghost" id="tkStart">⏱ Start 2 minutes</button>
      <div class="card stgs"><div class="rh">✋ Listener: ask 3 questions</div>{QK}</div>
    </div>
  </div>
'''))

# real-life task: three follow-up questions
FS = ''.join(f'<button class="fqs" data-fq="{e(s)}">{e(s)}</button>' for s in C.FOLLOW_STARTERS)
S.append(slide('Real-life task: follow-up questions', head('Real-life task', 'c-speak', 'Ask <em>3 follow-up questions</em> about the weekend') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col" style="width:380px;flex:none;gap:10px">
      <div class="card fqlead"><div class="rh">💬 Your friend says:</div><p>“Last weekend, I went to Vung Tau with my friends.”</p></div>
      <div class="card fqbank"><div class="rh">🧰 Question starters <span class="muted">click one</span></div><div class="fqss">{FS}</div></div>
    </div>
    <div class="card fqout"><div class="rh">✍️ My 3 questions</div>
      <div class="fqin"><b>1</b><input id="fq0" autocomplete="off" placeholder="Where did you stay?"></div>
      <div class="fqin"><b>2</b><input id="fq1" autocomplete="off" placeholder="…"></div>
      <div class="fqin"><b>3</b><input id="fq2" autocomplete="off" placeholder="…"></div>
      <button class="btn sm" id="fqCheck">✓ Check my questions</button><div class="fqres" id="fqRes"></div>
      <div class="tip" style="font-size:15px">📲 After class: ask a friend or family member 3 follow-up questions about their weekend — in English!</div></div>
  </div>
'''))

# game: story jigsaw
S.append(slide('Game: Story jigsaw', head('Game', 'c-prac', 'Story jigsaw 🧩 — <em>put the story in order</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col jgbank" style="width:520px;flex:none"><div class="rh2" id="jgTitle">Click “New story”</div><div class="jgb" id="jgBank"></div></div>
    <div class="card jgout"><div class="rh">📖 The story <span class="score" id="jgScore">Score: 0</span></div><ol class="jgl" id="jgLine"></ol>
      <div class="row" style="gap:8px"><button class="btn y" id="jgNew">🧩 New story</button><button class="btn sm" id="jgCheck">✓ Check</button><button class="btn sm ghost" id="jgUndo">↩ Undo</button></div><div class="jgres" id="jgRes"></div></div>
  </div>
'''))

WRAP = [('😲', "I can start a story: You'll never guess what happened!"),
        ('⏳', 'I can set the scene: While I was waiting for the bus, it started to rain.'),
        ('⚡', 'I can tell a story in order: at first · suddenly · fortunately · eventually · in the end'),
        ('❓', 'I can ask past questions: Did you…? Were you…? Where did you…?'),
        ('🔁', 'I can keep a story going: What happened next?')]
KEY = [v['col'] for v in C.VOCAB] + ["You'll never guess what happened.", 'While I was…, …', 'What happened next?', 'In the end, …', 'at first · while · suddenly · fortunately · eventually · in the end']
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
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S11 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 12</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Checkpoint 1: Everyday Life Simulation</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
