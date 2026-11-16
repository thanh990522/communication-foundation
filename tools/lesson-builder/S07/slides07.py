# Slides for S07 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
S = []
S.append(slide('Cover', '''  <span class="chip c-input">Week 03 · Session 07</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Eating Out:<br><span>From Menu</span><br>to Bill</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

AG = [('warm', '🙋', 'Warm-up · Who says it?', 'waiter or customer?'),
      ('input', '📋', 'The menu', 'starters · main courses · desserts'),
      ('input', '🃏', 'Words → collocations', 'order a starter…'),
      ('input', '🎩', 'Make it polite', "I'd like · I'll have · Could I…?"),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('prac', '📝', "Waiter's pad", 'take the order'),
      ('listen', '🔗', 'Linking &amp; polite tone', 'could‿I · I’ll‿have'),
      ('listen', '🎧', 'Listening', 'At the restaurant'),
      ('listen', '🍽', 'Model dialogue', 'Mai &amp; Ken order dinner'),
      ('prac', '🧾', 'Split the bill', 'service charge · each'),
      ('speak', '🎭', 'Restaurant role-play', 'allergy · budget · split'),
      ('prac', '💷', "Game: What's the total?", 'listen &amp; add up')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

OBJ = [('📋', 'Read a menu', 'starter · main course · side dish'),
       ('👍', 'Ask for advice', 'What do you recommend?'),
       ('🍽', 'Order politely', "I'll have… · I'd like…"),
       ('🥜', 'Make a special request', 'Could I have it without nuts?'),
       ('🧾', 'Pay the bill', 'Could we split the bill?')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: who says it?
WS = ''.join(f'<div class="wsc" id="ws{i}">{pb(f"WS_{i}")}<span class="wst">{e(t)}</span><div class="wsb"><button class="opt" data-ws="{i}" data-o="W">🤵 Waiter</button><button class="opt" data-ws="{i}" data-o="C">🙋 Customer</button></div></div>'
             for i, (t, w) in enumerate(C.WHO))
S.append(slide('Warm-up: Who says it?', head('Warm-up', 'c-warm', 'Who says it? — <em>waiter or customer?</em>') +
               f'  <div class="wsgrid">{WS}</div>\n  <div class="ftools"><span class="score" id="wsScore">✓ 0 / {len(C.WHO)}</span><button class="btn sm ghost" id="wsReset">↺ Reset</button></div>\n'))


# 5 the menu
def menu_html(mid, click=False, prices=True, ipa=False, compact=False):
    k = 0; out = f'<div class="menu{" compact" if compact else ""}" id="{mid}"><div class="mnh">🍽 THE CORNER CAFÉ <span>MENU</span></div><div class="mncols">'
    for sec, items in C.MENU:
        out += f'<div class="mnsec"><div class="mnst">{e(sec)}' + (f' <span class="fipa">{e(C.SECTION_IPA[sec])}</span>' if ipa else '') + '</div>'
        for (d, pr, em, tags) in items:
            tg = ''.join(f'<i class="mtag {t}">{t}</i>' for t in tags.split())
            body = f'<span class="mne">{em}</span><span class="mnd"><b>{e(d)}{tg}</b>' + (f'<span class="fipa">{e(C.MENU_IPA[d])}</span>' if ipa else '') + '</span>' + (f'<span class="mnp">£{pr:.2f}</span>' if prices else '')
            if click: out += f'<button class="mni" data-dish="{e(d)}" data-pr="{pr}" data-sec="{e(sec)}">{body}</button>'
            else: out += f'<div class="mni">{body}{pb(f"MN_{k}") if ipa else ""}</div>'
            k += 1
        out += '</div>'
    return out + '</div><div class="mnf"><i class="mtag V">V</i> vegetarian · <i class="mtag N">N</i> contains nuts · 10% service charge</div></div>'


S.append(slide('The menu', head('Input · The menu', 'c-input', 'Read the <em>menu</em>') + f'  <div class="row" style="flex:1;min-height:0">{menu_html("menu1", ipa=True)}</div>\n'))

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

# 8 make it polite
GR = ''.join(f'<div class="pgr"><b>{e(f)}</b><span>{e(u)}</span><div class="gqe">{pb(f"GP_{i}")}<span>{e(x)}</span></div></div>' for i, (f, u, x) in enumerate(C.GRAM))
PL = ''.join(f'<div class="plc" data-pl><div class="plr">😐 {e(r)}</div><div class="plp">😊 <b>{e(p)}</b>{pb(f"PO_{i}", "y")}</div><div class="plm"><i></i></div></div>' for i, (r, p) in enumerate(C.POLITE))
S.append(slide('Make it polite', head('Input · Polite ordering', 'c-input', 'Make it <em>polite</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col" style="width:380px;flex:none;gap:10px">{GR}<div class="tip" style="font-size:16px">💡 Say <b>please</b> and go <b>up ↗</b> at the end of a request.</div></div>
    <div class="plgrid">{PL}</div>
  </div>
  <div class="ftools"><span>Click a card: rude → polite. Say the polite version!</span><button class="btn sm ghost" data-plall>👁 All</button><button class="btn sm ghost" data-plreset>↺ Reset</button></div>
'''))

for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))

# 13 waiter's pad
S.append(slide("Waiter's pad", head('Practice · Listening for orders', 'c-prac', "Waiter's pad — <em>take the order</em>") + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    {menu_html("menu2", click=True, prices=False, compact=True)}
    <div class="col pad" style="width:330px;flex:none;gap:9px">
      <div class="padh">📝 Table 5 · <span id="tkN">Customer 0 / {len(C.TAKE)}</span></div>
      <button class="btn y" id="tkGo">▶ Listen to the next customer</button>
      <div class="padl" id="tkList"><span class="muted">Click the dishes you hear on the menu.</span></div>
      <div class="cfld"><label>without</label><input id="tkWo" autocomplete="off" spellcheck="false" placeholder="—"></div>
      <div class="row" style="gap:8px"><button class="btn sm ghost" id="tkAgain">🔊 Again</button><button class="btn sm" id="tkCheck">✓ Check</button><button class="btn sm ghost" id="tkShow">👁 Text</button></div>
      <div class="lftx" id="tkTx" hidden></div>
    </div>
  </div>
'''))

# 14 linking & polite tone
LK = ''.join(f'<button class="lline lnk {"up" if a == "↗" else "dn"}" data-a="LK_{i}">{P}<span>{e(t).replace("‿", "<b class=lkm>‿</b>")} <b class="arr">{a}</b></span></button>' for i, (t, a) in enumerate(C.LINKS))
IDS = ','.join(f'LK_{i}' for i in range(len(C.LINKS)))
S.append(slide('Linking & polite tone', head('Pronunciation', 'c-listen', 'could‿I · I’ll‿have — <em>polite tone ↗</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="card lkbox" style="flex:1;width:auto"><div class="rh">🔗 Link the words &amp; follow the arrow <button class="btn sm y rep" data-rep="{IDS}">🔁 Listen &amp; repeat</button></div>{LK}</div>
    <div class="col" style="width:340px;flex:none;gap:12px">
      <div class="card pnote"><div class="rh">🔗 Linking</div><p><b>could‿I</b> = /kʊˈdaɪ/</p><p><b>I'll‿have</b> = /aɪlˈhæv/</p><p><b>would‿you</b> = /wʊˈdʒuː/</p></div>
      <div class="card pnote"><div class="rh">🎵 Polite tone</div><p><b>↗</b> requests &amp; questions: <i>Could I…? Would you…?</i></p><p><b>↘</b> orders: <i>I'll have the fish, please.</i></p><p>Flat voice = rude. Friendly voice = polite! 🙂</p></div>
    </div>
  </div>
'''))

# 15 listening
L = C.LISTEN
S.append(slide('Listening: At the restaurant', head('Listening', 'c-listen', 'At the restaurant — <em>from menu to bill</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.PHRASE['recommend']}</div>
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

# 16 model dialogue
CF = ''.join(f'<div class="cfld"><label>{e(lb)}</label><input id="cf{i}" autocomplete="off" spellcheck="false"><span class="cfa" id="cfa{i}"></span></div>'
             for i, (lb, a, ok) in enumerate(C.CARD))
S.append(slide('Model dialogue: dinner', head('Model dialogue', 'c-listen', 'Dinner at the Corner Café — <em>Mai &amp; Ken</em>') + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec">
        <div class="fhd">🧾 Order notes <span>LISTEN &amp; WRITE</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">W = Waiter · M = Mai · K = Ken</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# 17 split the bill
BL = ''.join(f'<div class="bll"><span>{e(n)}</span><b>£{p:.2f}</b></div>' for n, p in C.BILL)
BQ = ''.join(f'<div class="cfld bq"><label>{e(l)}</label><span class="pnd">£</span><input id="bq{i}" inputmode="decimal" autocomplete="off"><span class="cfa" id="bqa{i}"></span></div>' for i, (l, v) in enumerate(C.BILL_Q))
S.append(slide('Split the bill', head('Practice · The bill', 'c-prac', 'Split the bill — <em>how much each?</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="rcpt"><div class="rch2">🧾 THE CORNER CAFÉ · Table 3</div>{BL}<div class="bll sum"><span>+ service charge 10%</span><b>?</b></div></div>
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="card form">{BQ}<div class="row"><button class="btn sm" id="bqCheck">✓ Check</button><button class="btn sm y" id="bqShow">👁 Answers</button></div></div>
      <div class="card gapf"><div class="rh">🗣 Then say it</div><div class="gf">Could we have the bill, please?</div><div class="gf">The total is ___ pounds. Is the service charge included?</div><div class="gf">Could we split the bill? — Sure. That's ___ each.</div></div>
    </div>
  </div>
'''))

# 18 role-play
S.append(slide('Restaurant role-play', head('Speaking · Role-play', 'c-speak', 'Restaurant role-play — <em>from menu to bill</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    {menu_html("menu3", compact=True)}
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="rcard small" id="rcard"><div class="rce">🎲</div><div class="rct">Customer card</div><div class="rcx">Draw a card. The waiter starts: “Are you ready to order?”</div></div>
      <button class="btn y" id="rcDraw">🎲 Draw a customer card</button>
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn" id="tkStart">⏱ Start 90 seconds</button>
    </div>
  </div>
'''))

# 19 real-life task: my order
S.append(slide('My order', head('Real-life task', 'c-speak', 'Build your order — <em>then say it!</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    {menu_html("menu4", click=True, compact=True)}
    <div class="col" style="width:360px;flex:none;gap:10px">
      <div class="card myord"><div class="rh">🗣 My order <span class="score" id="moTot">£0.00</span></div><div id="moTxt" class="motxt"><span class="muted">Click dishes on the menu.</span></div>
        <div class="cfld"><label>without</label><input id="moWo" autocomplete="off" spellcheck="false" placeholder="onions / nuts / cheese…"></div></div>
      <button class="btn ghost" id="moReset">↺ Start again</button>
      <div class="tip" style="font-size:16px">📲 After class: order a drink or a meal in English when you can — at a café, or online.</div>
    </div>
  </div>
'''))

# 20 game: what's the total?
S.append(slide("Game: What's the total?", head('Game', 'c-prac', "What's the <em>total</em>? — listen &amp; add up") + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    {menu_html("menu5", compact=True)}
    <div class="col lfbox" style="width:360px;flex:none">
      <div class="row" style="justify-content:space-between"><span class="score" id="gtN">Round 0 / {len(C.TOTALS)}</span><span class="score" id="gtScore">Score: 0</span></div>
      <div class="lfq" id="gtQ"><b>💷 Ready?</b><span>Listen to the order. Use the menu prices. Type the total.</span></div>
      <button class="btn y" id="gtGo">▶ Listen · next order</button>
      <div class="cfld bq"><label>Total</label><span class="pnd">£</span><input id="gtIn" inputmode="decimal" autocomplete="off"></div>
      <div class="row" style="gap:8px"><button class="btn sm ghost" id="gtAgain">🔊 Again</button><button class="btn sm" id="gtCheck">✓ Check</button></div>
      <div class="lftx" id="gtTx" hidden></div>
    </div>
  </div>
'''))

WRAP = [('📋', 'I can read a menu: starter, main course, side dish, dessert.'),
        ('👍', 'I can ask: What do you recommend?'),
        ('🍽', "I can order politely: To start with, I'll have… For the main course, I'd like…"),
        ('🥜', 'I can ask: Could I have it without nuts? I have a food allergy.'),
        ('🧾', "I can ask for the bill and split it: That's twenty pounds each.")]
KEY = [v['col'] for v in C.VOCAB] + ['What do you recommend?', "I'll have…", 'Could I have it without…?', 'Could we split the bill?', 'to start with · for the main course · however · because · finally']
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
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S07 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 08</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Shopping, Sizes, Returns &amp; Refunds</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
