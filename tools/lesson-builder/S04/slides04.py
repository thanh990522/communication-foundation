# Slides for S04 — executed inside build.py (uses slide, head, pb, e, P, C, I, qr_svg, HW_URL)
S = []
# 1 cover ---------------------------------------------------------------------------------------
S.append(slide('Cover', '''  <span class="chip c-input">Week 02 · Session 04</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Time,<br><span>Appointments</span> &amp;<br>Arrangements</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

# 2 lesson map ----------------------------------------------------------------------------------
AG = [('warm', '🕒', 'Warm-up · Say it!', 'times &amp; dates'),
      ('input', '📅', 'on · at · in', '1st · 2nd · 21st…'),
      ('input', '🃏', 'Words → collocations', 'make an appointment…'),
      ('prac', '💬', 'Fix the message', 'type the missing word'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('prac', '📒', "Mai's week", 'is meeting · is having'),
      ('listen', '🔢', '13 or 30? · Confirm ↗', 'thirTEEN · THIRty'),
      ('listen', '🎧', 'Listening', "Sarah &amp; Todd's weekend"),
      ('listen', '📞', 'Phone call', 'Making an appointment'),
      ('speak', '🗓', 'Find a time · Text a friend', 'Arrange a study call'),
      ('speak', '🎭', 'Role-play cards', 'Arrange &amp; reschedule'),
      ('prac', '🏁', 'Game: Listen &amp; click race', '13th or 30th?')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

# 3 objectives ----------------------------------------------------------------------------------
OBJ = [('📅', 'Say times &amp; dates', 'at half past three · on the 21st'),
       ('🗓', 'Talk about arrangements', "I'm meeting Lan on Friday."),
       ('🙋', 'Ask if someone is free', 'Are you available on…? Does 3 p.m. work for you?'),
       ('🔁', 'Reschedule politely', 'Unfortunately… Could we move it to…?'),
       ('✅', 'Confirm the details', 'Let me confirm: Tuesday at 3. ↗')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: say it (flip) ----------------------------------------------------------------------
WC = ''.join(f'<div class="flip wc wt" data-flip><div class="in"><div class="fc"><div class="art">{I.warm_art(f)}</div><div class="fwd"><b>{e(f)}</b>{pb(f"WA_{i}")}</div><span class="turn">↻</span></div>'
             f'<div class="bk"><b>{e(f)}</b><span class="vi">{e(a)}</span>{pb(f"WA_{i}", "y")}</div></div></div>' for i, (f, em, a) in enumerate(C.WARM))
TOOLS = '  <div class="ftools"><span>↻ Say it first — then click to check</span><button class="btn sm ghost" data-flipall>🔄 Flip all</button><button class="btn sm ghost" data-flipreset>↺ Reset</button></div>\n'
S.append(slide('Warm-up: Say it!', head('Warm-up', 'c-warm', 'Say it! — <em>times &amp; dates</em>') + f'  <div class="fgrid">{WC}</div>\n' + TOOLS))

# 5 on · at · in + ordinals ---------------------------------------------------------------------
TW = ''.join(f'<div class="twc t{i}"><div class="twp">{e(p)}</div><div class="twu">{e(u)}</div>' +
             ''.join(f'<button class="gx" data-a="TW_{i}_{j}">{P}<span>{e(x)}</span></button>' for j, x in enumerate(xs)) + '</div>'
             for i, (p, u, xs) in enumerate(C.TIMEW))
OR = ''.join(f'<button class="ordc" data-a="OR_{i}"><b>{e(o)}</b><span>{e(w)}</span></button>' for i, (o, w) in enumerate(zip(C.ORDINALS, C.ORD_SAY)))
S.append(slide('on · at · in', head('Input · Time words', 'c-input', '<em>on</em> Monday · <em>at</em> 3 p.m. · <em>in</em> the morning') +
               f'  <div class="twgrid">{TW}</div>\n  <div class="card ordbox"><div class="rh">📅 Dates: say the <b>ordinal</b> — Friday <b>the 21st</b></div><div class="ords">{OR}</div></div>\n'))

# 6-7 words → collocations ----------------------------------------------------------------------
WTOOLS = TOOLS.replace('Say it first — then click to check', 'Click a card to flip')


def word_card(i, v):
    return (f'<div class="flip wc" data-flip><div class="in"><div class="fc"><div class="art">{I.WORD[v["k"]]}</div>'
            f'<div class="fwd"><b>{e(v["w"])}</b>{pb("VW_" + str(i))}</div><span class="turn">↻</span></div>'
            f'<div class="bk"><span class="pos">{e(v["pos"])}</span><b>{e(v["w"])}</b><span class="ipa">{e(v["ipa"])}</span><span class="vi">{e(v["vi"])}</span>{pb("VW_" + str(i), "y")}</div></div></div>')


def phrase_card(i, v):
    col = e(v['col']).replace(e(v['kw']), f'<em>{e(v["kw"])}</em>', 1)
    return (f'<div class="flip pc" data-flip><div class="in"><div class="fc"><div class="art">{I.PHRASE[v["k"]]}</div>'
            f'<div class="fwd"><b>{col}</b>{pb("VC_" + str(i))}</div><span class="turn">↻</span></div>'
            f'<div class="bk"><b>{e(v["col"])}</b><span class="vi">{e(v["col_vi"])}</span><span class="ex">“{e(v["ex"])}”</span>{pb("VC_" + str(i), "y")}</div></div></div>')


for part, idx in ((1, range(0, 4)), (2, range(4, 8))):
    S.append(slide(f'Words → collocations {part}', head(f'Input · Words &amp; collocations {part}/2', 'c-input', 'Word → <em>collocation</em>') +
                   '  <div class="fgrid wcgrid">' + ''.join(word_card(i, C.VOCAB[i]) for i in idx) + ''.join(phrase_card(i, C.VOCAB[i]) for i in idx) + '</div>\n' + WTOOLS))


# 8 collocation check ---------------------------------------------------------------------------
def coll_row(i, s, opts, k, pre='ci', aid='CO'):
    btns = ''.join(f'<button class="opt" data-{pre}="{i}" data-o="{e(o)}">{e(o)}</button>' for o in opts)
    sent = e(s).replace('___', '<span class="gap">___</span>')
    ico = f'<div class="ico">{I.WORD[k]}</div>' if k else ''
    return (f'<div class="cq2" id="{pre}q{i}">{ico}<div class="cbody"><div class="cs"><span class="n">{i + 1}</span><span>{sent}</span></div>'
            f'<div class="co">{btns}</div></div>{pb(f"{aid}_{i}", "y")}</div>')


MF = ''.join(f'<div class="msg {w}">' + e(t).replace('___', f'<input class="mfin" id="mf{i}" autocomplete="off" spellcheck="false" aria-label="gap {i + 1}">') + f'<span class="mfa" id="mfa{i}"></span></div>' for i, (w, t, a) in enumerate(C.MSGFIX))
import random as _r
_B = list(C.MSG_BANK); _r.Random('S04-bank').shuffle(_B)
S.append(slide('Fix the message', head('Practice · Collocations', 'c-prac', 'Fix the message — <em>type the missing word</em>') + f'''  <div class="row" style="gap:20px;flex:1;min-height:0;align-items:stretch">
    <div class="phonebox wide"><div class="ph-top">💬 Lan</div><div class="ph-msgs">{MF}</div></div>
    <div class="col" style="width:330px;flex:none;gap:12px">
      <div class="card gapf"><div class="rh">🧩 Word bank</div><div class="bank">{''.join(f'<span>{e(w)}</span>' for w in _B)}</div></div>
      <button class="btn y" id="mfCheck">✓ Check</button><button class="btn ghost" id="mfShow">👁 Answers</button><button class="btn ghost" id="mfReset">↺ Reset</button>
      <span class="score" id="mfScore" style="align-self:flex-start">— / {len(C.MSGFIX)}</span>
    </div>
  </div>
'''))

# 9-12 main structures (step by step)
for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))

# 10 Mai's week ---------------------------------------------------------------------------------
S.append(slide("Mai's week", head('Practice · Arrangements', 'c-prac', "Look at <em>Mai's week</em>") +
               f'  <div class="row" style="gap:16px;flex:1;min-height:0"><div class="mapbox">{I.diary(C.DIARY)}</div>'
               '<div class="col grow mapq dq6">' + ''.join(coll_row(i, s, o, None, 'mq', 'MQ') for i, (s, o, a) in enumerate(C.DIARYQ)) +
               '<div class="ftools" style="margin-top:4px"><span class="score" id="mqScore">✓ 0 / 6</span><button class="btn sm ghost" id="mqReset">↺ Reset</button></div></div></div>\n'))

# 11 numbers 13 / 30 ----------------------------------------------------------------------------
PR = ''.join(f'<div class="pairc"><button class="pn" data-a="NP_{i}_0"><b>{a}</b><span>{e(sa)}</span></button><span class="vs">vs</span>'
             f'<button class="pn y" data-a="NP_{i}_1"><b>{b}</b><span>{e(sb)}</span></button></div>' for i, (a, b, sa, sb) in enumerate(C.PAIRS))
PT = ''.join(f'<div class="ptq" id="pt{i}"><span class="n">{i + 1}</span>{pb(f"PT_{i}")}<span class="pts">{e(s)}</span>'
             '<div class="co">' + ''.join(f'<button class="opt" data-pt="{i}" data-o="{k}">{C.PAIRS[pi][k]}</button>' for k in (0, 1)) + '</div></div>'
             for i, (s, pi, ans) in enumerate(C.PAIR_TEST))
S.append(slide('Numbers: 13 or 30?', head('Pronunciation · Numbers', 'c-listen', 'thir<em>TEEN</em> or <em>THIR</em>ty?') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="card pairbox"><div class="rh">🔊 Listen &amp; repeat — stress!</div>{PR}<div class="ptip">-<b>TEEN</b>: stress at the end, long /iːn/ · -<b>ty</b>: stress at the start, short /ti/</div></div>
    <div class="col grow ptbox"><div class="rh">🎧 Which number do you hear?</div>{PT}<div class="ftools" style="margin-top:2px"><span class="score" id="ptScore">✓ 0 / {len(C.PAIR_TEST)}</span><button class="btn sm ghost" id="ptReset">↺ Reset</button></div></div>
  </div>
'''))

# 12 confirm intonation -------------------------------------------------------------------------
CQ = ''.join(f'<div class="cfr"><button class="lline up" data-a="CQ_{i}">{P}<span>{e(q)} <b class="arr">↗</b></span></button>'
             f'<button class="lline dn" data-a="CS_{i}">{P}<span>{e(a)} <b class="arr">↘</b></span></button></div>'
             for i, (q, a) in enumerate(zip(C.CONFIRM_Q, C.CONFIRM_S)))
IDS = ','.join(f'CQ_{i},CS_{i}' for i in range(len(C.CONFIRM_Q)))
S.append(slide('Confirm: rising intonation', head('Pronunciation · Intonation', 'c-listen', 'Checking? Go <em>up ↗</em> — Confirming? Go <em>down ↘</em>') +
               f'''  <div class="cfh"><span class="up">↗ Check (question)</span><span class="dn">↘ Confirm (answer)</span><button class="btn sm y rep" data-rep="{IDS}">🔁 Listen &amp; repeat</button></div>
  <div class="cfg">{CQ}</div>
'''))

# 13 listening ----------------------------------------------------------------------------------
L = C.LISTEN
S.append(slide('Listening: Sarah & Todd', head('Listening', 'c-listen', 'Plans for the weekend — <em>Sarah &amp; Todd</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.LISTEN_ART.replace('>John<', '>Todd<')}</div>
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

# 16 phone call + appointment card --------------------------------------------------------------
CF = ''.join(f'<div class="cfld"><label>{e(lb)}</label><input id="cf{i}" autocomplete="off" spellcheck="false"><span class="cfa" id="cfa{i}"></span></div>'
             for i, (lb, a, ok) in enumerate(C.CARD))
S.append(slide('Phone call: an appointment', head('Model dialogue', 'c-listen', 'Calling the clinic — <em>make an appointment</em>') + f'''  <div class="dlg">
    <div class="col" style="gap:10px;min-height:0">
      <div class="card form apcard">
        <div class="fhd">🦷 Smile Dental Clinic <span>APPOINTMENT CARD</span></div>
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">R = Receptionist · N = Nam</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))


# 17 find a time (information gap) --------------------------------------------------------------
def dtable(d, who):
    rows = ''.join(f'<tr><th>{s}</th>' + ''.join(f'<td class="{"busy" if (dd, s) in d else "free"}">{e(d.get((dd, s), ""))}</td>' for dd in C.DAYS) + '</tr>' for s in C.SLOTS)
    return f'<table class="gapt" id="gap{who}"{" hidden" if who == "B" else ""}><tr><th></th>' + ''.join(f'<th>{x}</th>' for x in C.DAYS) + f'</tr>{rows}</table>'


FREE = [f'{d} {s}' for d in C.DAYS for s in C.SLOTS if (d, s) not in C.DIARY_A and (d, s) not in C.DIARY_B]
GF = ''.join(f'<div class="gf">{e(f).replace("___", "<span class=gap>___</span>")}</div>' for f in C.GAP_FRAMES)
S.append(slide('Find a time', head('Speaking · Pairs', 'c-speak', 'Find a time — <em>when are you both free?</em>') + f'''  <div class="row" style="gap:16px;flex:1;min-height:0">
    <div class="col grow" style="gap:8px;min-width:0">
      <div class="row" style="gap:8px;align-items:center"><button class="btn sm" data-gap="A">🅰 Student A's diary</button><button class="btn sm ghost" data-gap="B">🅱 Student B's diary</button><span class="gnote2">Don't show your diary — ask &amp; answer!</span></div>
      {dtable(C.DIARY_A, 'A')}{dtable(C.DIARY_B, 'B')}
    </div>
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="card gapf"><div class="rh">🗣 Use these</div>{GF}</div>
      <button class="btn y" id="gapAns">👁 Free for both?</button><div class="gapans" id="gapAnsT" hidden>✅ {' · '.join(FREE)}</div>
    </div>
  </div>
'''))

# 19 real-life task: text messages --------------------------------------------------------------
CH = ''.join(f'<div class="msg {w}">{e(t)}</div>' for w, t in C.CHAT)
S.append(slide('Arrange a study call by text', head('Real-life task', 'c-speak', 'Arrange a <em>study call</em> by text') + f'''  <div class="row" style="gap:22px;flex:1;min-height:0;align-items:stretch">
    <div class="phonebox"><div class="ph-top">💬 Lan</div><div class="ph-msgs">{CH}</div><div class="ph-in">Type a message…</div></div>
    <div class="col grow" style="gap:12px">
      <div class="card ttask"><div class="rh">✍ Your turn — write in the chat box</div>
        <div class="tstep"><span class="n">1</span><div>Invite: <b>Are you available on ___?</b></div></div>
        <div class="tstep"><span class="n">2</span><div>Partner: <b>Unfortunately, I'm ___ing. Could we move it to ___?</b></div></div>
        <div class="tstep"><span class="n">3</span><div>Offer: <b>Does ___ work for you?</b></div></div>
        <div class="tstep"><span class="n">4</span><div>Confirm: <b>Let me confirm: ___ at ___.</b></div></div>
      </div>
      <div class="tip" style="font-size:18px">📲 After class: arrange a <b>real</b> study call in English by text or voice.</div>
    </div>
  </div>
'''))

# 20 role-play cards ----------------------------------------------------------------------------
S.append(slide('Role-play cards', head('Speaking · Role-play', 'c-speak', 'Arrange &amp; <em>reschedule</em> — role-play cards') + '''  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="rcard" id="rcard"><div class="rce">🎲</div><div class="rct">Draw a card</div><div class="rcx">Student A starts. Student B is busy — reschedule!</div></div>
    <div class="col" style="width:340px;flex:none;gap:12px">
      <button class="btn y" id="rcDraw">🎲 Draw a card</button>
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn" id="tkStart">⏱ Start 90 seconds</button>
      <div class="card fuq"><div class="rh">✅ Must use</div><div class="gf">Are you available on…?</div><div class="gf">Could we move it to…?</div><div class="gf">Let me confirm…</div><div class="gf">unfortunately · instead · so</div></div>
    </div>
  </div>
'''))

# 21 game: listen & click race
S.append(slide('Game: Listen & click race', head('Game', 'c-prac', 'Listen &amp; click race — <em>which one do you hear?</em>') + f'''  <div class="race">
    <div class="row" style="align-items:center;justify-content:space-between"><span class="score" id="rcN">Round 0 / {len(C.RACE)}</span><div class="tbar" style="flex:1;margin:0 16px"><i id="rcBar"></i></div><span class="score" id="rcScore">Score: 0</span></div>
    <div class="rcq" id="rcQ"><b>🏁 Ready?</b><span>Listen to the time or date — click the right card as fast as you can!</span></div>
    <div class="rcopts" id="rcOpts"></div>
    <div class="row" style="justify-content:center;gap:10px"><button class="btn y" id="rcGo">▶ Start / Next round</button><button class="btn ghost" id="rcAgain">🔊 Again</button><button class="btn ghost" id="rcReset">↺ Reset</button></div>
  </div>
'''))
# 22 wrap-up ------------------------------------------------------------------------------------
WRAP = [('📅', 'I can say times and dates: at half past three, on the 21st.'),
        ('🗓', "I can talk about arrangements: I'm meeting Lan on Friday."),
        ('🙋', 'I can ask: Are you available on…? Does 3 p.m. work for you?'),
        ('🔁', 'I can reschedule: Unfortunately… Could we move it to…?'),
        ('✅', 'I can check with rising intonation: Tuesday at three? ↗')]
KEY = [v['col'] for v in C.VOCAB] + ['Are you available on…?', 'Does … work for you?', 'Could we move it to…?', 'Let me confirm…', 'first · unfortunately · instead · so · finally']
S.append(slide('Wrap-up', head('Wrap-up', 'c-wrap', 'What can you <em>do now</em>?') + '  <div class="row" style="gap:18px;flex:1;min-height:0">\n    <div class="col grow wrap2">' +
               ''.join(f'<label class="chk"><span class="wi">{ic}</span><span class="grow">{e(t)}</span><input type="checkbox"></label>' for ic, t in WRAP) +
               '</div>\n    <div class="card keys"><div class="rh">🔑 Key language</div><div class="kchips">' + ''.join(f'<span>{e(k)}</span>' for k in KEY) + '</div></div>\n  </div>\n'))

# 23 homework -----------------------------------------------------------------------------------
S.append(slide('Homework: Listening', head('Homework', 'c-listen', 'After class') + f'''  <div class="hw hw2">
    <div class="card"><h3>🎧 Listening homework · Messages &amp; calls</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div>Listen to <b>phone messages</b> about appointments.</div></div>
        <div class="step"><span class="n">2</span><div>Write the <b>day, date and time</b> — careful: <b>13 or 30?</b></div></div>
        <div class="step"><span class="n">3</span><div>Who is <b>rescheduling</b>? What is the <b>new time</b>?</div></div>
        <div class="step"><span class="n">4</span><div>Press <b>Nộp bài</b> — you need <b>80%</b> or do it again.</div></div>
        <div class="step"><span class="n">5</span><div>Real-life: arrange a <b>study call</b> in English this week.</div></div>
      </div>
    </div>
    <div class="card qrcard"><h3>📝 Open the homework</h3>{qr_svg(HW_URL)}
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S04 → 📝 Homework</p><span class="pass">Pass mark: 80%</span></div>
  </div>
'''))

# 24 thank you ----------------------------------------------------------------------------------
S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 05</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Directions &amp; Getting Around Town</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))
