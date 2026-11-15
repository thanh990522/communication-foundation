# Slides for S05 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
S = []
# 1 cover ---------------------------------------------------------------------------------------
S.append(slide('Cover', '''  <span class="chip c-input">Week 02 · Session 05</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Directions &amp;<br><span>Getting Around</span><br>Town</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

# 2 lesson map ----------------------------------------------------------------------------------
AG = [('warm', '🏙', 'Warm-up · Where do you go?', 'pharmacy · bank · museum…'),
      ('input', '↰', 'Direction basics', 'turn left · go past · between'),
      ('input', '🃏', 'Words → collocations', 'a famous landmark…'),
      ('prac', '🗺', 'Where is it?', 'across from · on the corner'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('prac', '🔢', 'Order the steps', 'first → then → finally'),
      ('prac', '🚶', 'Follow the route', 'move on the map'),
      ('listen', '🔗', 'Linking &amp; stress', 'go‿past · LANDmark'),
      ('listen', '🎧', 'Listening', "Todd: how to get to my house"),
      ('listen', '🚉', 'Asking the way', 'At the station'),
      ('speak', '🤫', 'Secret destination · My route', 'Give 4 steps + 2 landmarks'),
      ('prac', '🎯', 'Game: Listen &amp; find', 'Where are you?')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

# 3 objectives ----------------------------------------------------------------------------------
OBJ = [('🙋', 'Ask the way', "What's the best way to get to the museum?"),
       ('🧭', 'Give directions', 'Go past the bank, then turn left.'),
       ('📍', 'Say where it is', "It's across from the park. It's on the corner."),
       ('⏱', 'Say how long', 'It takes about ten minutes.'),
       ('🗺', 'Use 4 steps + 2 landmarks', 'first → then → after that → finally')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: where do you go to …? (reveal tiles) --------------------------------------------------
RV = ''.join(f'<div class="rv" data-rv><div class="rvq"><span class="rve">❓</span><small>Where do you go to</small><b>{e(c)}?</b></div>'
             f'<div class="rva"><span class="rve">{em}</span><b>the {e(p)}</b><span class="fipa">{e(ip)}</span>{pb(f"WA_{i}", "y")}</div></div>'
             for i, (p, c, em, ip) in enumerate(C.WARM))
S.append(slide('Warm-up: Where do you go?', head('Warm-up', 'c-warm', 'Where do you go to <em>…?</em>') +
               f'  <div class="rvgrid">{RV}</div>\n  <div class="ftools"><span>🗣 Answer first: <b>You go to the ___.</b> — then click the card</span>'
               '<button class="btn sm ghost" data-rvall>👁 Show all</button><button class="btn sm ghost" data-rvreset>↺ Reset</button></div>\n'))

# 5 direction basics ------------------------------------------------------------------------------
BT = ''.join(f'<div class="bt"><div class="bti">{I.BASIC_ICON[k]}</div><div class="btx"><b>{e(p)}</b><span class="fipa">{e(ip)}</span>'
             f'<small>{e(vi)}</small><i>{e(ex)}</i></div>{pb(f"BA_{i}")}</div>' for i, (p, ip, vi, ex, k) in enumerate(C.BASICS))
S.append(slide('Direction basics', head('Input · Direction basics', 'c-input', 'Turn left · go past · <em>between</em>') + f'  <div class="btgrid">{BT}</div>\n'))

# 6-7 words → collocations ----------------------------------------------------------------------
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


# 8 where is it? (map + choose) -------------------------------------------------------------------
def coll_row(i, s, opts, pre='mq', aid='MQ'):
    btns = ''.join(f'<button class="opt" data-{pre}="{i}" data-o="{e(o)}">{e(o)}</button>' for o in opts)
    sent = e(s).replace('___', '<span class="gap">___</span>')
    return (f'<div class="cq2" id="{pre}q{i}"><div class="cbody"><div class="cs"><span class="n">{i + 1}</span><span>{sent}</span></div>'
            f'<div class="co">{btns}</div></div>{pb(f"{aid}_{i}", "y")}</div>')


S.append(slide('Where is it?', head('Practice · Places on the map', 'c-prac', 'Where is it? — <em>look at the map</em>') +
               f'  <div class="row" style="gap:16px;flex:1;min-height:0"><div class="mapwrap">{I.town_map("map1", False, False)}</div>'
               '<div class="col grow wq">' + ''.join(coll_row(i, s, o) for i, (s, o, a) in enumerate(C.MAPQ)) +
               f'<div class="ftools" style="margin-top:2px"><span class="score" id="mqScore">✓ 0 / {len(C.MAPQ)}</span><button class="btn sm ghost" id="mqReset">↺ Reset</button></div></div></div>\n'))

# 9-12 main structures (step by step)
for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))

# 13 order the steps ------------------------------------------------------------------------------
OT = ''.join(f'<button class="btn sm{" ghost" if k else ""}" data-ot="{k}">{e(o["title"])}</button>' for k, o in enumerate(C.ORDER))
S.append(slide('Order the steps', head('Practice · Sequence', 'c-prac', 'Order the steps — <em>first → then → finally</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="row" style="gap:8px;align-items:center">{OT}<span class="gnote2">Click the steps in the right order.</span></div>
      <div class="ocards" id="ocards"></div>
      <div class="ftools" style="margin-top:0"><span class="score" id="oScore">— / 5</span><button class="btn sm y" id="oCheck">✓ Check</button><button class="btn sm ghost" id="oShow">👁 Answer</button><button class="btn sm ghost" id="oReset">↺ Reset</button></div>
    </div>
    <div class="col" style="width:300px;flex:none;gap:12px">
      <div class="card linkbox"><div class="rh">🔗 Linkers</div>{''.join(f'<div class="lkr"><b>{e(l)}</b></div>' for l in C.LINKERS)}</div>
      <div class="tip" style="font-size:17px">💡 Look for the linker at the start of each step. <b>until</b> = cho đến khi.</div>
    </div>
  </div>
'''))

# 14 follow the route ----------------------------------------------------------------------------
RB = ''.join(f'<button class="btn sm{" ghost" if k else ""}" data-rt="{k}">{e(r["title"])}</button>' for k, r in enumerate(C.ROUTES))
S.append(slide('Follow the route', head('Practice · Directions', 'c-prac', 'Follow the route — <em>where are you?</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="mapwrap" id="rtMapBox">{I.town_map("map2", True, True)}</div>
    <div class="col grow" style="gap:8px;min-width:0">
      <div class="row" style="gap:6px;flex-wrap:wrap">{RB}</div>
      <div class="rtsteps" id="rtSteps"></div>
      <div class="rtq" id="rtQ">Read each step. The marker moves on the map.</div>
      <div class="row" style="gap:8px;justify-content:flex-end"><button class="btn sm ghost" id="rtBack">← Back</button><button class="btn sm y" id="rtNext">Next step →</button><button class="btn sm ghost" id="rtReset">↺ Restart</button></div>
    </div>
  </div>
'''))

# 15 linking + stress -----------------------------------------------------------------------------
LK = ''.join(f'<button class="lline lnk" data-a="LK_{i}">{P}<span>{e(t).replace("‿", "<b class=lkm>‿</b>")}</span></button>' for i, t in enumerate(C.LINKS))
IDS = ','.join(f'LK_{i}' for i in range(len(C.LINKS)))
ST = ''.join(f'<div class="stw" id="st{i}">{pb(f"SW_{i}")}<div class="sts">' + ''.join(f'<button class="syl" data-st="{i}" data-k="{k}">{e(sy)}</button>' for k, sy in enumerate(syl))
             + f'</div><span class="fipa sti">{e(ip)}</span></div>' for i, (w, syl, k_, ip) in enumerate(C.STRESS))
S.append(slide('Linking & stress', head('Pronunciation', 'c-listen', 'Link the words — <em>stress the landmark</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="card lkbox"><div class="rh">🔗 Link the words <button class="btn sm y rep" data-rep="{IDS}">🔁 Listen &amp; repeat</button></div>{LK}</div>
    <div class="card stbox"><div class="rh">🎯 Tap the <b>stressed</b> syllable</div><div class="stgrid">{ST}</div>
      <div class="ftools" style="margin-top:4px"><span class="score" id="stScore">✓ 0 / {len(C.STRESS)}</span><button class="btn sm ghost" id="stReset">↺ Reset</button></div></div>
  </div>
'''))

# 16 listening ----------------------------------------------------------------------------------
L = C.LISTEN
S.append(slide('Listening: Todd', head('Listening', 'c-listen', 'How to get to my house — <em>Todd</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.WORD['get to'].replace('viewBox="0 0 200 140"', 'viewBox="0 0 200 140" preserveAspectRatio="xMidYMid slice"')}</div>
      <div class="card lsrc">
        <div class="lt">🎧 {L['title']}</div>
        <button class="btn" data-a="EL">▶ Play / ⏸ Stop</button>
        <div class="lsm">Source: {L['source']}</div>
      </div>
      <button class="btn y" id="lCheck">✓ Check answers</button><button class="btn ghost" id="lScript">📜 Show script</button>
    </div>
    <div class="col grow" style="gap:6px;min-width:0;position:relative">
      <div id="lgist"></div>
      <div id="ldetail" class="col" style="gap:6px;flex:1"></div>
      <div class="lscript card" id="lscr" hidden></div>
    </div>
  </div>
'''))

# 17 model dialogue -----------------------------------------------------------------------------
CF = ''.join(f'<div class="cfld"><label>{e(lb)}</label><input id="cf{i}" autocomplete="off" spellcheck="false"><span class="cfa" id="cfa{i}"></span></div>'
             for i, (lb, a, ok) in enumerate(C.CARD))
S.append(slide('Asking the way', head('Model dialogue', 'c-listen', 'At the station — <em>asking the way</em>') + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec">
        <div class="fhd">📝 Tourist's notes <span>LISTEN &amp; WRITE</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">T = Tourist · L = Local</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# 18 secret destination ----------------------------------------------------------------------------
S.append(slide('Secret destination', head('Speaking · Pairs', 'c-speak', 'Secret destination — <em>guess the place!</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="mapwrap">{I.town_map("map3", False, False)}</div>
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="card sdcard"><div class="rh">🎲 Start at…</div><div class="sdst" id="sdStart">the train station ★</div><button class="btn sm y" id="sdDraw">🎲 New start</button></div>
      <div class="card gapf"><div class="rh">🅰 Choose a place secretly. Give directions — don't say the name!</div>
        <div class="gf">First, go out of ___ and turn ___.</div><div class="gf">Go past ___, then ___.</div><div class="gf">It is across from ___ / on the corner.</div><div class="gf">It takes about ___ minutes.</div></div>
      <div class="tip" style="font-size:16.5px">🅱 Follow on the map and guess: <b>Is it the ___?</b></div>
    </div>
  </div>
'''))

# 19 real-life task: my route ------------------------------------------------------------------------
LBL = ['First,', 'Then', 'After that,', 'until…', 'Finally,']
PL = ''.join(f'<div class="pls"><span class="plk">{e(l)}</span><input class="plin" id="pl{i}" autocomplete="off" spellcheck="false" placeholder="{e(C.PLAN_MODEL[i])}"></div>' for i, l in enumerate(LBL))
S.append(slide('My route', head('Real-life task', 'c-speak', 'From <em>my home</em> to a nearby place') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="card plan">
      <div class="plt"><input id="plFrom" value="my home" aria-label="From"><span>→</span><input id="plTo" placeholder="the supermarket / the park / school…" aria-label="To"></div>
      {PL}
      <div class="pls"><span class="plk">🏛 Landmarks</span><input class="plin lm" id="plL0" placeholder="landmark 1 (the bank…)"><input class="plin lm" id="plL1" placeholder="landmark 2 (the park…)"></div>
    </div>
    <div class="col" style="width:330px;flex:none;gap:12px">
      <div class="card plchk"><div class="rh">✅ Checklist</div><div class="pc1" id="pcSteps">⬜ At least 4 steps</div><div class="pc1" id="pcLm">⬜ 2 landmarks</div><div class="pc1" id="pcLink">⬜ first · then · finally</div><button class="btn sm ghost" data-a="PLAN">▶ Listen to a model</button></div>
      <div class="card tkc"><div id="tkTime" class="tkt">1:00</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn" id="tkStart">⏱ Read it aloud — 60 s</button>
      <div class="tip" style="font-size:16px">📲 After class: send your directions in English to a classmate.</div>
    </div>
  </div>
'''))

# 20 game: listen & find --------------------------------------------------------------------------
S.append(slide('Game: Listen & find', head('Game', 'c-prac', 'Listen &amp; find — <em>where are you?</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="mapwrap" id="lfMapBox">{I.town_map("map4", False, True)}</div>
    <div class="col grow lfbox">
      <div class="row" style="justify-content:space-between;align-items:center"><span class="score" id="lfN">Round 0 / {len(C.GAME)}</span><span class="score" id="lfScore">Score: 0</span></div>
      <div class="lfq" id="lfQ"><b>🎯 Ready?</b><span>Start at the station ★. Listen, follow on the map, then click the place.</span></div>
      <div class="lftx" id="lfTx" hidden></div>
      <button class="btn y" id="lfGo">▶ Listen · next round</button>
      <div class="row" style="gap:8px"><button class="btn sm ghost" id="lfAgain">🔊 Again</button><button class="btn sm ghost" id="lfShow">👁 Show text</button><button class="btn sm ghost" id="lfReset">↺ Reset</button></div>
    </div>
  </div>
'''))

# 21 wrap-up ------------------------------------------------------------------------------------
WRAP = [('🙋', "I can ask: What's the best way to get to the museum?"),
        ('🧭', 'I can give directions: Go past the bank, then turn left.'),
        ('📍', "I can say where: It's across from the park. It's on the corner."),
        ('⏱', 'I can say how long: It takes about ten minutes.'),
        ('🗺', 'I can give 4 steps with 2 landmarks: first → then → after that → finally.')]
KEY = [v['col'] for v in C.VOCAB] + ["What's the best way to get to…?", 'Go past …, then …', 'It is across from…', 'It takes about … minutes.', 'first · then · after that · until · finally']
S.append(slide('Wrap-up', head('Wrap-up', 'c-wrap', 'What can you <em>do now</em>?') + '  <div class="row" style="gap:18px;flex:1;min-height:0">\n    <div class="col grow wrap2">' +
               ''.join(f'<label class="chk"><span class="wi">{ic}</span><span class="grow">{e(t)}</span><input type="checkbox"></label>' for ic, t in WRAP) +
               '</div>\n    <div class="card keys"><div class="rh">🔑 Key language</div><div class="kchips">' + ''.join(f'<span>{e(k)}</span>' for k in KEY) + '</div></div>\n  </div>\n'))

# 22 homework -----------------------------------------------------------------------------------
S.append(slide('Homework', head('Homework', 'c-listen', 'After class') + f'''  <div class="hw hw2">
    <div class="card"><h3>📝 Homework · 5 parts</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div><b>Vocabulary test</b> — today's words &amp; collocations</div></div>
        <div class="step"><span class="n">2</span><div><b>Reading</b> — a text with today's words</div></div>
        <div class="step"><span class="n">3</span><div><b>Listening</b> — real audio, script after you finish</div></div>
        <div class="step"><span class="n">4</span><div><b>Shadowing</b> — read aloud &amp; record → score <b>/10</b> (<span style="color:#16A34A">green</span> = correct, <span style="color:#DC2626">red</span> = fix it)</div></div>
        <div class="step"><span class="n">5</span><div><b>Translation</b> — Vietnamese → English with today's structures</div></div>
      </div>
    </div>
    <div class="card qrcard"><h3>📝 Open the homework</h3>{qr_svg(HW_URL)}
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S05 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

# 23 thank you ----------------------------------------------------------------------------------
S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 06</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Food, Shopping Lists &amp; Quantities</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
