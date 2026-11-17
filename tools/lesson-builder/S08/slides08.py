# Slides for S08 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL, struct_slide)
S = []
S.append(slide('Cover', '''  <span class="chip c-input">Week 03 · Session 08</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Shopping:<br><span>Sizes, Returns</span><br>&amp; Refunds</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

AG = [('warm', '⚡', 'Warm-up · Speed naming', 'clothes in 3 seconds'),
      ('input', '🪞', 'The fitting room', 'too big · fits · cheap enough'),
      ('input', '🃏', 'Words → collocations', 'fit perfectly · get a refund…'),
      ('prac', '✅', 'too or enough?', 'choose &amp; say'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('listen', '🎯', 'Stress the difference', 'No, the BLUE one!'),
      ('listen', '🎧', 'Listening', 'Getting a refund'),
      ('listen', '👖', 'Model dialogue', 'buying jeans'),
      ('speak', '🎭', 'Two linked role-plays', 'buy it → return it'),
      ('speak', '💬', 'Real-life task', 'ask an online shop'),
      ('prac', '🧾', 'Game: Returns desk', 'what can you offer?'),
      ('wrap', '🏁', 'Wrap-up &amp; homework', '5 parts')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

OBJ = [('👕', 'Ask for a size or colour', 'Do you have this in a medium?'),
       ('🪞', 'Try clothes on', 'Can I try it on?'),
       ('📏', 'Say what is wrong', "It's too small. · It isn't long enough."),
       ('🔁', 'Return or exchange', "I'd like to exchange this."),
       ('🧾', 'Talk about refunds', 'Keep the receipt · get a refund')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: speed naming
CL = ''.join(f'<div class="clc" id="cl{i}" data-cl="{i}"><span class="cle">{em}</span><div class="clw"><b>{e(w)}</b><span class="fipa">{e(ip)}</span></div>{pb(f"CW_{i}")}</div>'
             for i, (w, em, ip) in enumerate(C.CLOTHES))
S.append(slide('Warm-up: Speed naming', head('Warm-up', 'c-warm', 'Speed naming — <em>say it in 3 seconds!</em>') +
               f'  <div class="clgrid">{CL}</div>\n  <div class="ftools"><span>Click a picture to check · ⚡ = a new picture every 3 seconds</span>'
               '<span class="score" id="clN">0 / 12</span><button class="btn sm y" id="clGo">⚡ Speed round</button><button class="btn sm ghost" id="clAll">👁 All</button><button class="btn sm ghost" id="clReset">↺ Reset</button></div>\n'))

# 5 the fitting room
SZ = ''.join(f'<span>{s}</span>' for s, _, _ in C.SIZES)
GB = ''.join(f'<div class="gfr"><b>{e(f)}</b><span>{e(v)}</span><div class="gqe">{pb(f"GR_{i}")}<span>{e(x)}</span></div></div>' for i, (f, v, x) in enumerate(C.GRAM))
S.append(slide('The fitting room', head('Input · too / enough', 'c-input', 'The fitting room — <em>too big? big enough?</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card frm2">
      <div class="rh">🪞 Size <span class="muted">move the slider</span></div>
      <div class="frstage"><div class="frbody">👕</div><div class="frshirt" id="frShirt">👕</div><span class="frnote">dashed = your size (M)</span></div>
      <input type="range" min="0" max="{len(C.SIZES) - 1}" value="0" id="frSize" class="frr"><div class="frlab">{SZ}</div>
      <div class="frcap"><button class="play sm" data-a="FS_0" id="frSp">{P}</button><div><b id="frSt"></b><span id="frSv"></span></div></div>
    </div>
    <div class="card frm2">
      <div class="rh">💷 Price <span class="wal">👛 Budget: £{C.BUDGET}</span></div>
      <div class="frstage"><div class="prtag" id="prTag">£15</div></div>
      <input type="range" min="0" max="{len(C.PRICES) - 1}" value="0" id="frPrice" class="frr"><div class="frlab">{''.join(f'<span>£{p}</span>' for p, _ in C.PRICES)}</div>
      <div class="frcap"><button class="play sm" data-a="FP_0" id="prSp">{P}</button><div><b id="prSt"></b></div></div>
    </div>
    <div class="col gfbox">{GB}<div class="tip" style="font-size:15px">💡 <b>too</b> = a problem 😟 · <b>enough</b> = OK 🙂<br><b>enough</b> goes <u>after</u> the adjective.</div></div>
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


# 8 too or enough? (MC)
def coll_row(i, s, opts, pre='mq', aid='MQ'):
    btns = ''.join(f'<button class="opt" data-{pre}="{i}" data-o="{e(o)}">{e(o)}</button>' for o in opts)
    sent = e(s).replace('___', '<span class="gap">___</span>')
    return (f'<div class="cq2" id="{pre}q{i}"><div class="cbody"><div class="cs"><span class="n">{i + 1}</span><span>{sent}</span></div>'
            f'<div class="co">{btns}</div></div>{pb(f"{aid}_{i}", "y")}</div>')


S.append(slide('too or enough?', head('Practice · too / enough / fit / suit', 'c-prac', 'Choose — <em>then say the sentence</em>') +
               '  <div class="col grow wq mq8">' + ''.join(coll_row(i, s, o) for i, (s, o, a) in enumerate(C.MAPQ)) +
               f'<div class="ftools" style="margin-top:2px"><span>fit = right size 📏 · suit = looks good on you 😍</span><span class="score" id="mqScore">✓ 0 / {len(C.MAPQ)}</span><button class="btn sm ghost" id="mqReset">↺ Reset</button></div></div>\n'))

for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))


# 13 contrastive stress + final sounds
def caps(t):
    import re as _re
    return _re.sub(r'\b([A-Z]{2,})\b', lambda m: f'<b class="cst">{m.group(1)}</b>', e(t))


CT = ''.join(f'<div class="ctc" data-ct><div class="ctq">{pb(f"CQ_{i}")}<span>{e(q)}</span></div><div class="cta">{pb(f"CA_{i}", "y")}<span>{caps(a)}</span></div><div class="ctm">👆 Answer, then click</div></div>'
             for i, (q, a) in enumerate(C.CONTRAST))
FN = ''.join(f'<button class="lline fsn" data-a="FN_{i}">{P}<span><b>{e(w)}</b> <span class="fipa">{e(ip)}</span><small>{e(n)}</small></span></button>' for i, (w, ip, n) in enumerate(C.FINALS))
IDS = ','.join(f'FN_{i}' for i in range(len(C.FINALS)))
S.append(slide('Stress the difference', head('Pronunciation', 'c-listen', 'No, the <em>BLUE</em> one! — stress the difference') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:8px;min-width:0"><div class="ctgrid">{CT}</div>
      <div class="ftools" style="margin-top:0"><span>Partner A asks · Partner B answers with a STRONG word</span><button class="btn sm ghost" id="ctAll">👁 All</button><button class="btn sm ghost" id="ctReset">↺ Reset</button></div></div>
    <div class="card lkbox fsbox"><div class="rh">🔚 Final sounds <button class="btn sm y rep" data-rep="{IDS}">🔁 Listen &amp; repeat</button></div>{FN}
      <div class="tip" style="font-size:14.5px">re<b>ceipt</b>: the <b>p</b> is silent! · Say the last sound clearly.</div></div>
  </div>
'''))

# 14 listening (real recording, hotlinked from the source)
L = C.LISTEN
S.append(slide('Listening: Getting a refund', head('Listening', 'c-listen', 'Getting a refund — <em>a real conversation</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.SHOP_ART}</div>
      <div class="card lsrc">
        <div class="lt">🎧 {e(L['title'])}</div>
        <div class="row" style="gap:8px"><button class="btn" data-a="EL">▶ Normal</button><button class="btn ghost" data-a="EL2">▶ Slower</button></div>
        <div class="lsm">Source: {e(L['source'])} · 🆕 <b>vouchers</b> = phiếu mua hàng</div>
      </div>
      <button class="btn y" id="lCheck">✓ Check answers</button><a class="btn ghost" id="lScript" href="{L['page']}" target="_blank" rel="noopener">📜 Script (source page) ↗</a>
    </div>
    <div class="col grow" style="gap:6px;min-width:0;position:relative">
      <div id="lgist"></div>
      <div id="ldetail" class="col" style="gap:6px;flex:1"></div>
    </div>
  </div>
'''))

# 15 model dialogue
CF = ''.join(f'<div class="cfld"><label>{e(lb)}</label><input id="cf{i}" autocomplete="off" spellcheck="false"><span class="cfa" id="cfa{i}"></span></div>'
             for i, (lb, a, ok) in enumerate(C.CARD))
S.append(slide('Model dialogue: buying jeans', head('Model dialogue', 'c-listen', 'Buying jeans — <em>size, colour, price</em>') + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard notec nc8">
        <div class="fhd">🏷 Shopping notes <span>LISTEN &amp; WRITE</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">A = Shop assistant · C = Customer</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))

# 16 two linked role-plays
LKR = ''.join(f'<span><b>{e(a)}</b> {e(b)}</span>' for a, b in C.LINKERS)
S.append(slide('Two linked role-plays', head('Speaking · Role-play', 'c-speak', 'Buy it → <em>return it</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:10px;min-width:0">
      <div class="rpst">
        <div class="rps on" id="rpS1"><div class="rpn">1 · BUY IT 🛍</div><div class="rpb" id="rpB1"><span class="muted">Draw a shopping card.</span></div>
          <div class="rpf">Do you have this in…? · Can I try it on? · It's too… / It isn't … enough. · How much…?</div></div>
        <div class="rps" id="rpS2"><div class="rpn">2 · RETURN IT 🔁 <small>one week later</small></div><div class="rpb" id="rpB2"><span class="muted">After role-play 1…</span></div>
          <div class="rpf">I'd like to return / exchange… · Here's the receipt. · Can I get a refund?</div></div>
      </div>
      <div class="card lkr"><div class="rh">🔗 In role-play 2, tell the story:</div><div class="lkrs">{LKR}</div>
        <div class="lkre">“<b>At first</b> they were OK, <b>but</b> after one day the zip broke. I'd like a refund <b>because</b> it's damaged.” — “I'm sorry. <b>Therefore</b> you can get a refund. Or would you like a new one <b>instead</b>?”</div></div>
    </div>
    <div class="col" style="width:300px;flex:none;gap:10px">
      <button class="btn y" id="rpNew">🎲 New shopping card</button>
      <button class="btn" id="rpNext">Next step → Return it</button>
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn ghost" id="tkStart">⏱ Start 90 seconds</button>
      <div class="tip" style="font-size:15px">👥 Then swap: customer ↔ shop assistant.</div>
    </div>
  </div>
'''))

# 17 real-life task: ask an online shop
SH = C.SHOP
CHK = ''.join(f'<div class="ocl" id="oc_{k}"><i>☐</i>{t}</div>' for k, t in (('size', '📏 size'), ('colour', '🎨 colour'), ('price', '💷 price'), ('return', '🔁 returns')))
S.append(slide('Real-life task: online shop', head('Real-life task', 'c-speak', 'Ask an <em>online shop</em> — say it, then type it') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col" style="width:300px;flex:none;gap:10px">
      <div class="card oprod"><div class="ope">{SH['emoji']}</div><b>{e(SH['item'])}</b><span class="opp">{SH['price']}</span><span class="muted">{e(SH['name'])} · ⭐⭐⭐⭐⭐</span></div>
      <div class="card ochk"><div class="rh">✅ Ask about…</div>{CHK}</div>
    </div>
    <div class="card ochat">
      <div class="och">💬 {e(SH['name'])} · Live chat <span class="odot"></span></div>
      <div class="ocb" id="ocBody"><div class="om bot">Hi! 👋 How can I help you today?</div></div>
      <div class="oci"><input id="ocIn" autocomplete="off" placeholder="Say it aloud, then type your question…"><button class="btn sm" id="ocSend">Send</button></div>
    </div>
  </div>
  <div class="tip" style="font-size:15px;margin-top:8px">📲 After class: ask <b>one</b> real question in English — in a shop or in an online shop's chat. Screenshot it for the class!</div>
'''))

# 18 game: returns desk
POL = ''.join(f'<div class="pol">{e(p)}</div>' for p in C.POLICY)
OPT = ''.join(f'<button class="opt rdo" data-rd="{i}">{e(o)}</button>' for i, o in enumerate(C.OPTIONS))
S.append(slide('Game: Returns desk', head('Game', 'c-prac', 'Returns desk — <em>what can you offer?</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card polb"><div class="rh">📋 Shop policy</div>{POL}<div class="tip" style="font-size:14.5px">🗣 Say it: “Sorry, … / No problem. You can…”</div></div>
    <div class="col grow lfbox" style="min-width:0">
      <div class="row" style="justify-content:space-between"><span class="score" id="rdN">Customer 0 / {len(C.CASES)}</span><span class="score" id="rdScore">Score: 0</span></div>
      <div class="rdc" id="rdCard"><div class="rde">🧾</div><div class="rdt">Ready? Click “Next customer”.</div></div>
      <div class="rdos">{OPT}</div>
      <div class="row" style="gap:8px;justify-content:center"><button class="btn y" id="rdGo">Next customer →</button><button class="btn sm ghost" id="rdAgain">🔊 Again</button></div>
      <div class="lftx" id="rdSay" hidden></div>
    </div>
  </div>
'''))

WRAP = [('👕', 'I can ask: Do you have this in a medium / in black?'),
        ('🪞', 'I can ask: Can I try it on? — It fits perfectly!'),
        ('📏', "I can say: It's too small. It isn't long enough."),
        ('🔁', "I can say: I'd like to return / exchange this. Here's the receipt."),
        ('💷', 'I can ask: Can I get a refund? Do you offer a discount?')]
KEY = [v['col'] for v in C.VOCAB] + ['Do you have this in…?', 'Can I try it on?', "It's too… / It isn't … enough.", "I'd like to exchange / return…", 'at first · but · because · therefore · instead']
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
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S08 → 📝 Homework</p><span class="pass">Each part: 80%</span></div>
  </div>
'''))

S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 09</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Everyday Services &amp; Polite Requests</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
