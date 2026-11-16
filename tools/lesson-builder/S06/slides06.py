# Slides for S06 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
S = []
S.append(slide('Cover', '''  <span class="chip c-input">Week 02 · Session 06</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Food,<br><span>Shopping Lists</span> &amp;<br>Quantities</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

AG = [('warm', '🧊', "Warm-up · What's in the fridge?", 'look, remember, say'),
      ('input', '📦', 'Containers', 'a packet of · a carton of…'),
      ('input', '🃏', 'Words → collocations', 'fresh ingredients…'),
      ('input', '⚖', 'Quantifiers', 'some/any · much/many · a few/a little'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('prac', '🍳', 'Enough or not enough?', 'recipe vs fridge'),
      ('listen', '🗣', 'Weak forms', 'some /səm/ · any'),
      ('listen', '🎧', 'Listening', "John's fridge"),
      ('listen', '📞', 'Phone call', 'From the supermarket'),
      ('speak', '🏪', 'At the supermarket', 'Which aisle? Out of stock!'),
      ('speak', '📝', 'My shopping list', '5 accurate quantities'),
      ('prac', '🛒', 'Game: Fill the trolley', 'listen &amp; count')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

OBJ = [('🧺', 'Name food &amp; containers', 'a carton of milk · a packet of rice'),
       ('❓', 'Ask about food at home', 'Do we have any eggs?'),
       ('⚖', 'Use quantities', 'a few apples · a little butter · enough rice'),
       ('⚠', 'Say what is missing', "We're running out of milk. It's out of stock."),
       ('📝', 'Make a shopping list', 'with 5 accurate quantities')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: what's in the fridge? (memory)
FR = ''.join(f'<div class="fri"><span class="fre">{em}</span><b>{e(q)} {e(f)}</b>{pb(f"FR_{i}", "y")}</div>' for i, (q, f, em) in enumerate(C.FRIDGE))
S.append(slide("Warm-up: What's in the fridge?", head('Warm-up', 'c-warm', "What's in the <em>fridge</em>? — look &amp; remember") + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="fridge covered" id="fridge"><div class="frdoor">{FR}</div><div class="frcover">🧊<b>Ready?</b><span>Look for 20 seconds — then remember!</span></div></div>
    <div class="col" style="width:330px;flex:none;gap:12px">
      <button class="btn y" id="frLook">👀 Look — 20 seconds</button>
      <div class="card tkc"><div id="frTime" class="tkt">0:20</div></div>
      <button class="btn ghost" id="frShow">👁 Show the fridge</button>
      <div class="card gapf"><div class="rh">🗣 Say it</div><div class="gf">There are <b>some</b> eggs.</div><div class="gf">There's <b>a carton of</b> milk.</div><div class="gf">There's <b>a little</b> butter.</div></div>
    </div>
  </div>
'''))

# 5 containers: build the list
CT = ''.join(f'<button class="ctb" data-ct="{i}"><b>{e(c)}</b><span class="fipa">{e(ip)}</span><small>{e(vi)}</small></button>' for i, (c, f, em, ip, vi) in enumerate(C.CONTAINERS))
import random as _r
_ord = list(range(len(C.CONTAINERS))); _r.Random('S06-ct').shuffle(_ord)
FD = ''.join(f'<button class="fdb" data-fd="{i}"><span>{C.CONTAINERS[i][2]}</span><b>{e(C.CONTAINERS[i][1])}</b></button>' for i in _ord)
S.append(slide('Containers', head('Input · Containers', 'c-input', 'a <em>packet</em> of rice · a <em>carton</em> of milk') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col ctcol">{CT}</div>
    <div class="col fdcol">{FD}</div>
    <div class="card ctlist"><div class="rh">🧾 Shopping list <span class="score" id="ctScore">0 / {len(C.CONTAINERS)}</span></div><div id="ctOut" class="ctout"></div>
      <div class="ftools" style="margin-top:auto"><span>Click a container, then a food.</span><button class="btn sm ghost" id="ctShow">👁 All</button><button class="btn sm ghost" id="ctReset">↺</button></div></div>
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


# 8 quantifiers
def coll_row(i, s, opts, pre='mq', aid='MQ'):
    btns = ''.join(f'<button class="opt" data-{pre}="{i}" data-o="{e(o)}">{e(o)}</button>' for o in opts)
    sent = e(s).replace('___', '<span class="gap">___</span>')
    return (f'<div class="cq2" id="{pre}q{i}"><div class="cbody"><div class="cs"><span class="n">{i + 1}</span><span>{sent}</span></div>'
            f'<div class="co">{btns}</div></div>{pb(f"{aid}_{i}", "y")}</div>')


GP = ''.join(f'<div class="gq"><div class="gqh"><b>{e(t)}</b><span>{e(r)}</span></div>' + ''.join(f'<div class="gqe">{pb(f"GR_{i}_{j}")}<span>{e(x)}</span></div>' for j, x in enumerate(xs)) + '</div>'
             for i, (t, r, xs) in enumerate(C.GRAM))
S.append(slide('Quantifiers', head('Input · Grammar', 'c-input', 'some · any · many · much · <em>a few · a little · enough</em>') +
               f'  <div class="row" style="gap:16px;flex:1;min-height:0"><div class="gqgrid">{GP}</div>'
               '<div class="col grow wq">' + ''.join(coll_row(i, s, o) for i, (s, o, a) in enumerate(C.MAPQ)) +
               f'<div class="ftools" style="margin-top:2px"><span class="score" id="mqScore">✓ 0 / {len(C.MAPQ)}</span><button class="btn sm ghost" id="mqReset">↺ Reset</button></div></div></div>\n'))

for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))

# 13 enough or not enough?
R = C.RECIPE
RR = ''.join(f'<div class="rcr" id="rc{i}"><span class="rce2">{em}</span><div class="rcn"><b>{e(f)}</b><small>need: {e(nd)} · fridge: {e(hv)}</small></div>'
             f'<button class="opt" data-en="{i}" data-v="1">✅ enough</button><button class="opt" data-en="{i}" data-v="0">❌ not enough</button></div>'
             for i, (f, em, nd, hv, ok) in enumerate(R['items']))
S.append(slide('Enough or not enough?', head('Practice · Quantities', 'c-prac', 'Enough or <em>not enough</em>?') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:8px;min-width:0"><div class="rch">🍳 {e(R['title'])}</div>{RR}
      <div class="ftools" style="margin-top:0"><span class="score" id="enScore">— / {len(R['items'])}</span><button class="btn sm y" id="enCheck">✓ Check</button><button class="btn sm ghost" id="enReset">↺ Reset</button></div></div>
    <div class="col" style="width:360px;flex:none;gap:10px">
      <div class="card gapf"><div class="rh">🗣 Say it</div><div class="gf">We have <b>enough</b> rice.</div><div class="gf">We <b>don't have enough</b> eggs.</div><div class="gf">We're <b>running out of</b> tomatoes.</div></div>
      <div class="card enlist"><div class="rh">🧾 So we need…</div><div id="enOut" class="ctout"><span class="muted">Check first!</span></div></div>
    </div>
  </div>
'''))

# 14 weak forms
WL = ''.join(f'<button class="lline lnk" data-a="WK_{i}">{P}<span>' + e(t).replace('*some*', '<b class="wkf">some<i>/səm/</i></b>').replace('*any*', '<b class="wkf">any<i>/əni/</i></b>') + '</span></button>' for i, t in enumerate(C.WEAK))
IDS = ','.join(f'WK_{i}' for i in range(len(C.WEAK)))
SWc = ''.join(f'<div class="swc">{pb(f"SS_{i}")}<div><b>{e(s)}</b><span class="fipa">{e(ip)}</span></div></div>' for i, (w, s, ip) in enumerate(C.STRESS_W))
S.append(slide('Weak forms & stress', head('Pronunciation', 'c-listen', 'Say it fast: <em>some /səm/</em> · <em>any /əni/</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="card lkbox" style="flex:1;width:auto"><div class="rh">🗣 Weak forms — short &amp; quick <button class="btn sm y rep" data-rep="{IDS}">🔁 Listen &amp; repeat</button></div>{WL}</div>
    <div class="card swbox"><div class="rh">🎯 Word stress — <b>BIG</b> syllable</div>{SWc}</div>
  </div>
'''))

# 15 listening
L = C.LISTEN
S.append(slide('Listening: John', head('Listening', 'c-listen', "What's in your fridge? — <em>John &amp; Todd</em>") + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.PHRASE['enough']}</div>
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
S.append(slide('Phone call: the shopping list', head('Model dialogue', 'c-listen', 'Calling home — <em>the shopping list</em>') + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec">
        <div class="fhd">🧾 Sam's list <span>LISTEN &amp; WRITE</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">S = Sam · L = Lucy</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# 17 supermarket stock board
AB = ''.join(f'<div class="aisle2"><div class="aih">{e(a)}</div>' + ''.join(f'<div class="sti2" data-sk="{e(n)}"><span>{em}</span><b>{e(n)}</b><i class="sst"></i></div>' for n, em in its) + '</div>'
             for a, its in C.AISLES)
S.append(slide('At the supermarket', head('Speaking · Role-play', 'c-speak', 'At the supermarket — <em>which aisle? out of stock!</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:8px;min-width:0">
      <div class="aisles">{AB}</div>
      <div class="row" style="gap:8px;align-items:center"><button class="btn sm y" id="skShuffle">🎲 New stock</button><span class="gnote2">✅ in stock · ⚠ only a few left · ❌ out of stock — only the <b>shop assistant</b> looks!</span></div>
    </div>
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="card slist"><div class="rh">🧾 Customer's list <button class="btn sm ghost" id="slNew">🎲</button></div><div id="slOut"></div></div>
      <div class="card gapf"><div class="rh">🗣 Use these</div><div class="gf">Excuse me, which aisle is the ___ in?</div><div class="gf">Is there any ___?</div><div class="gf">Sorry, it's out of stock. How about ___?</div><div class="gf">Is there anything else?</div></div>
    </div>
  </div>
'''))

# 18 my shopping list (checker)
OPTQ = ''.join(f'<option>{e(q)}</option>' for q in C.QTY)
OPTF = ''.join(f'<option>{e(f)}</option>' for f in C.FOODS)
ROWS = ''.join(f'<div class="msr" id="ms{i}"><span class="n">{i + 1}</span><span>We need</span><select class="msq"><option value="">quantity…</option>{OPTQ}</select>'
               f'<select class="msf"><option value="">food…</option>{OPTF}</select><span class="msv"></span></div>' for i in range(6))
S.append(slide('My shopping list', head('Real-life task', 'c-speak', 'My shopping list — <em>5 accurate quantities</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="card mslist"><div class="rh">📝 For: <input id="msFor" placeholder="dinner for my family / a party…" aria-label="Shopping for"></div>{ROWS}</div>
    <div class="col" style="width:330px;flex:none;gap:12px">
      <div class="card msgoal"><div class="msn" id="msN">0</div><span>accurate quantities</span><div class="tbar"><i id="msBar"></i></div><b id="msGoal">Goal: 5</b></div>
      <div class="card gapf"><div class="rh">🗣 Then tell your partner</div><div class="gf"><b>First</b>, we need ___. We <b>also</b> need ___.</div><div class="gf">We have ___, <b>but</b> we don't have enough ___.</div><div class="gf">We're running out of ___, <b>so</b> ___.</div></div>
      <div class="tip" style="font-size:16px">📲 After class: write a real shopping list in English with 3 quantity phrases.</div>
    </div>
  </div>
'''))

# 19 game: fill the trolley
TR = ''.join(f'<div class="tri" data-ti="{i}"><span class="tre">{em}</span><b>{e(n)}</b><div class="trc"><button class="trm" data-tm="{i}">−</button><span class="trn" id="tn{i}">0</span><button class="trp" data-tp="{i}">+</button></div></div>'
             for i, (n, em) in enumerate(C.TROLLEY))
S.append(slide('Game: Fill the trolley', head('Game', 'c-prac', 'Fill the trolley — <em>listen &amp; count!</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="trgrid">{TR}</div>
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="row" style="justify-content:space-between"><span class="score" id="tgN">Round 0 / {len(C.ORDERS)}</span><span class="score" id="tgScore">Score: 0</span></div>
      <div class="lfq" id="tgQ"><b>🛒 Ready?</b><span>Listen to the order. Put the right number of items in the trolley.</span></div>
      <button class="btn y" id="tgGo">▶ Listen · next order</button>
      <div class="row" style="gap:8px"><button class="btn sm ghost" id="tgAgain">🔊 Again</button><button class="btn sm" id="tgCheck">✓ Check trolley</button></div>
      <div class="lftx" id="tgTx" hidden></div>
    </div>
  </div>
'''))

WRAP = [('🧺', 'I can name food and containers: a carton of milk, a packet of rice.'),
        ('❓', 'I can ask: Do we have any eggs? How many / How much…?'),
        ('⚖', 'I can use a few, a little, some, any and enough.'),
        ('⚠', "I can say: We're running out of milk. It's out of stock."),
        ('📝', 'I can make a shopping list with 5 accurate quantities.')]
KEY = [v['col'] for v in C.VOCAB] + ['Do we have any…?', 'We need a few / a little…', 'We are running out of…', 'Is there anything else?', 'first · also · but · because · so']
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
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S06 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 07</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Eating Out: From Menu to Bill</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
