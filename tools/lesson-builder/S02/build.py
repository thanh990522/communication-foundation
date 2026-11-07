"""Build lesson S02 → ../../../lessons/S02/ (index.html with MP3 files, offline single file, audio ZIP).
Run after gen_audio.py.  Uses the lesson-1 page shell (shell_head.html / shell_tail.html / core.js)."""
import base64, html, io, json, os, re, shutil, zipfile
import content as C
import illus as I

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'lessons', 'S02'))
SITE = 'https://thanh990522.github.io/communication-foundation/'
LESSON_URL = SITE + 'lessons/S02/'
HW_URL = SITE + 'homework/?s=S02'
P = '<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>'
FOOT = '  <div class="s-foot"><span>A1 → A2 Communication Accelerator · <b>S02</b></span><span><b>00</b></span></div>\n'
e = html.escape
SND_CLS = ['ss', 'zz', 'iz']
SOUND_OF = {w.split()[0]: k for w, k in C.SORT}


def slide(title, body, cls='slide'):
    return f'<section class="{cls}" data-title="{title}">\n{body}{FOOT}</section>\n'


def head(chip, chipcls, h2):
    return f'  <div class="s-head"><span class="chip {chipcls}">{chip}</span><h2>{h2}</h2></div>\n'


def pb(aid, cls=''):
    return f'<button class="play sm{" " + cls if cls else ""}" data-a="{aid}">{P}</button>'


def split_end(w, k):
    return (w[:-2], w[-2:]) if k == 2 or w in ('goes', 'does') else (w[:-1], w[-1:])


def mark(t):
    """*word* → coloured -s ending by its sound."""
    def f(m):
        w = m.group(1); k = SOUND_OF[w]; stem, end = split_end(w, k)
        return f'<b class="mk {SND_CLS[k]}">{e(stem)}<u>{e(end)}</u></b>'
    return re.sub(r'\*([^*]+)\*', f, e(t))


def ending(w):
    first, rest = (w.split(' ', 1) + [''])[:2]; k = SOUND_OF[first]; stem, end = split_end(first, k)
    return f'{e(stem)}<u class="{SND_CLS[k]}">{e(end)}</u>' + (' ' + e(rest) if rest else '')


def qr_svg(url):
    import qrcode, qrcode.image.svg as qs
    b = io.BytesIO(); qrcode.make(url, image_factory=qs.SvgPathImage, box_size=10, border=1).save(b)
    s = b.getvalue().decode()
    s = s[s.index('<svg'):]
    return re.sub(r'width="[^"]+" height="[^"]+"', 'class="qr"', s, count=1)


S = []
# 1 cover --------------------------------------------------------------------------------------
S.append(slide('Cover', '''  <span class="chip c-input">Week 01 · Session 02</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Routines,<br><span>Habits</span> &amp;<br>Real Schedules</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

# 2 lesson map ---------------------------------------------------------------------------------
AG = [('warm', '🔤', 'Warm-up · Spell it!', "Today's words"),
      ('input', '🃏', 'Words → collocations 1', 'productive · commute · shift · break'),
      ('input', '🧩', 'Words → collocations 2', 'usually · hardly ever · weekday · weekend'),
      ('input', '📊', 'How often?', 'always → never'),
      ('prac', '✅', 'Collocation check', 'Choose the word'),
      ('listen', '👄', '-s endings', '/s/ · /z/ · /ɪz/ · sort it!'),
      ('listen', '📣', 'Read aloud', 'word → phrase → sentence'),
      ('listen', '🎧', 'Listening', "John &amp; Sarah's mornings"),
      ('input', '🧱', 'Frames · Ask &amp; answer', 'How often do you…?'),
      ('listen', '💬', 'Model dialogue', 'Lucy &amp; Minh'),
      ('speak', '🗣', 'Interview · Free practice', 'Report · two situations'),
      ('speak', '⏱', '90-second talk · Game', 'Sentence scramble')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

# 3 objectives ---------------------------------------------------------------------------------
OBJ = [('🗓', 'Describe your routine', 'On weekdays…, whereas at weekends…'),
       ('📊', 'Say how often', 'always · usually · often · sometimes · hardly ever · never'),
       ('🙋', 'Ask about routines', 'How often do you…? What time do you…?'),
       ('👄', 'Say -s endings clearly', 'starts /s/ · goes /z/ · misses /ɪz/'),
       ('⏱', 'Talk for 90 seconds', 'first · then · after that · because')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up ------------------------------------------------------------------------------------
S.append(slide('Warm-up: Spell it!', head('Warm-up', 'c-warm', "Spell it! — <em>today's words</em>") + '''  <div class="wgrid" id="warm"></div>
  <div class="row" style="margin-top:14px;align-items:center"><button class="btn y" id="warmCheck">✓ Check</button><button class="btn ghost" id="warmShow">👁 Answers</button><span class="score" id="warmScore">— / 8</span></div>
'''))

# 5 word flip cards ----------------------------------------------------------------------------
def word_card(i, v):
    return (f'<div class="flip wc" data-flip><div class="in">'
            f'<div class="fc"><div class="art">{I.WORD[v["k"]]}</div>'
            f'<div class="fwd"><b>{e(v["w"])}</b>{pb("VW_" + str(i))}</div><span class="turn">↻</span></div>'
            f'<div class="bk"><span class="pos">{e(v["pos"])}</span><b>{e(v["w"])}</b><span class="ipa">{e(v["ipa"])}</span>'
            f'<span class="vi">{e(v["vi"])}</span>{pb("VW_" + str(i), "y")}</div></div></div>')


def phrase_card(i, v):
    col = e(v['col']).replace(e(v['kw']), f'<em>{e(v["kw"])}</em>', 1)
    return (f'<div class="flip pc" data-flip><div class="in">'
            f'<div class="fc"><div class="art">{I.PHRASE[v["k"]]}</div>'
            f'<div class="fwd"><b>{col}</b>{pb("VC_" + str(i))}</div><span class="turn">↻</span></div>'
            f'<div class="bk"><b>{e(v["col"])}</b><span class="vi">{e(v["col_vi"])}</span>'
            f'<span class="ex">“{e(v["ex"])}”</span>{pb("VC_" + str(i), "y")}</div></div></div>')


TOOLS = '  <div class="ftools"><span>↻ Click a card to flip</span><button class="btn sm ghost" data-flipall>🔄 Flip all</button><button class="btn sm ghost" data-flipreset>↺ Reset</button></div>\n'
for part, idx in ((1, range(0, 4)), (2, range(4, 8))):
    # top row: the word · bottom row: its collocation, directly underneath
    S.append(slide(f'Words → collocations {part}', head(f'Input · Words &amp; collocations {part}/2', 'c-input', 'Word → <em>collocation</em>') +
                   '  <div class="fgrid wcgrid">' + ''.join(word_card(i, C.VOCAB[i]) for i in idx) +
                   ''.join(phrase_card(i, C.VOCAB[i]) for i in idx) + '</div>\n' + TOOLS))
# 6 collocation flip cards ---------------------------------------------------------------------


# 7 frequency ----------------------------------------------------------------------------------
def week(d):
    return '<div class="wk">' + ''.join(f'<span class="{"on" if k < d else ""}">{"MTWTFSS"[k]}</span>' for k in range(7)) + '</div>'


FREQ_ROWS = ''.join(
    f'<div class="fq2"><div class="flip mf" data-flip><div class="in"><div class="fc"><b>{e(a)}</b></div><div class="bk"><b>{e(vi)}</b></div></div></div>'
    f'{pb("F_" + str(i))}{week(d)}<div class="fx">{e(ex).replace(e(a), f"<b>{e(a)}</b>", 1)}</div></div>'
    for i, (a, pc, ex, vi, d) in enumerate(C.FREQ))
S.append(slide('How often?', head('Input · Frequency', 'c-input', 'How often? — <em>always → never</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="freq2 grow">{FREQ_ROWS}</div>
    <div class="col" style="width:340px;flex:none;gap:12px">
      <div class="card rule"><div class="rh">📍 Where does it go?</div>
        <div class="rr">I <b class="adv">usually</b> <u>start</u> work at nine.</div>
        <div class="rr">She <b class="adv">hardly ever</b> <u>misses</u> breakfast.</div>
        <div class="rr">Do you <b class="adv">ever</b> <u>miss</u> breakfast?</div>
      </div>
      <div class="card rule ask"><div class="rh">🙋 Ask</div>
        <div class="rr big">How <b class="adv">often</b> do you <u>take</u> a break?</div>
        <div class="rr">— <b class="adv">Always.</b> / <b class="adv">Sometimes.</b> / <b class="adv">Never.</b></div>
      </div>
      <button class="btn" id="fAll">▶ always → never</button>
    </div>
  </div>
'''))

# 8 collocation check --------------------------------------------------------------------------
def coll_row(i, s, opts, k):
    btns = ''.join(f'<button class="opt" data-ci="{i}" data-o="{e(o)}">{e(o)}</button>' for o in opts)
    sent = e(s).replace('___', '<span class="gap">___</span>')
    return (f'<div class="cq2" id="cq{i}"><div class="ico">{I.WORD[k]}</div><div class="cbody"><div class="cs"><span class="n">{i + 1}</span><span>{sent}</span></div>'
            f'<div class="co">{btns}</div></div>{pb("CO_" + str(i), "y")}</div>')


COLL_ROWS = ''.join(coll_row(i, s, opts, k) for i, (s, opts, ans, k) in enumerate(C.COLL))
S.append(slide('Collocation check', head('Practice', 'c-prac', 'Choose the <em>right word</em>') +
               f'  <div class="coll2">{COLL_ROWS}</div>\n  <div class="ftools"><span class="score" id="collScore">✓ 0 / 8</span><button class="btn sm ghost" id="collReset">↺ Reset</button></div>\n'))

# 9 -s endings: three sounds -------------------------------------------------------------------
SYL = ('<div class="syl"><div class="slh">+1 syllable</div>'
       '<div class="sr"><span>miss</span><i class="d1"></i><b>→</b><span>miss·<u class="iz">es</u></span><i class="d1"></i><i class="d1"></i></div>'
       '<div class="sr"><span>fi·nish</span><i class="d1"></i><i class="d1"></i><b>→</b><span>fi·nish·<u class="iz">es</u></span><i class="d1"></i><i class="d1"></i><i class="d1"></i></div></div>')
SG = ''
for g, (snd, rule, tag, words, bases) in enumerate(C.S_GROUPS):
    pairs = ''.join(f'<button class="pair" data-a="PS_{g}_{j}"><span>{e(b)}</span><i>→</i><b>{ending(w)}</b></button>' for j, (w, b) in enumerate(zip(words, bases)))
    SG += (f'<div class="sg2 {SND_CLS[g]}"><div class="sgh2"><b class="ipa">{e(snd)}</b><div><span class="tag">{e(tag)}</span><span class="rl">{e(rule)}</span></div>{pb("PSG_" + str(g), "y")}</div>'
           f'<div class="pairs">{pairs}</div>' + (SYL if g == 2 else '') + '</div>')
STRESS = ''.join(f'<div class="stl">{pb("ST_" + str(i))}<span>{e(t)}</span></div>' for i, t in enumerate(C.STRESS))
STRESS = re.sub(r'\b([A-Z]{2,}(?: [A-Z]{2,})?)\b', r'<b>\1</b>', STRESS)
S.append(slide('-s endings: three sounds', head('Pronunciation', 'c-listen', 'He start<em>s</em> · he go<em>es</em> · he miss<em>es</em> — <em>3 sounds</em>') +
               f'  <div class="sgroups2">{SG}</div>\n  <div class="card stressbox"><div class="rh">🔊 Stress the frequency word</div>{STRESS}</div>\n'))

# 10 sort it -----------------------------------------------------------------------------------
BK = ''.join(f'<div class="bucket {SND_CLS[g]}" data-b="{g}"><div class="bh"><b class="ipa">{e(snd)}</b><span>{e(tag)}</span></div><div class="bz" id="bz{g}"></div></div>'
             for g, (snd, rule, tag, *_r) in enumerate(C.S_GROUPS))
S.append(slide('Sort it: /s/ /z/ /ɪz/', head('Practice · Pronunciation', 'c-prac', 'Sort it! — <em>/s/ · /z/ · /ɪz/</em>') + f'''  <div class="pool card" id="pool"></div>
  <div class="buckets">{BK}</div>
  <div class="ftools"><span class="score" id="sortScore">— / {len(C.SORT)}</span><button class="btn sm y" id="sortCheck">✓ Check</button><button class="btn sm ghost" id="sortShow">👁 Answers</button><button class="btn sm ghost" id="sortReset">↺ Reset</button></div>
'''))

# 11 read aloud: words → phrases ---------------------------------------------------------------
def lcol(g, body, qid):
    snd = C.S_GROUPS[g][0]
    return (f'<div class="lad {SND_CLS[g]}"><div class="ladh"><b class="ipa">{e(snd)}</b>'
            f'<button class="btn sm rep" data-rep="{qid}">🔁 Listen &amp; repeat</button></div>{body}</div>')


R1 = ''
for g, L in enumerate(C.LADDER):
    words = [(i, w) for i, (w, k) in enumerate(C.SORT) if k == g]
    body = ('<div class="tier">Words</div><div class="wchips">' + ''.join(f'<button class="wchip" data-a="SW_{i}">{ending(w)}</button>' for i, w in words) + '</div>'
            '<div class="tier">Phrases</div>' + ''.join(f'<button class="lline" data-a="LP_{g}_{j}">{P}<span>{mark(t)}</span></button>' for j, t in enumerate(L['phrases'])))
    R1 += lcol(g, body, ','.join([f'SW_{i}' for i, _ in words] + [f'LP_{g}_{j}' for j in range(len(L['phrases']))]))
S.append(slide('Read aloud: words → phrases', head('Pronunciation · Read aloud', 'c-listen', 'Read aloud — <em>word → phrase</em>') + f'  <div class="ladder">{R1}</div>\n'))

# 12 read aloud: sentences → challenge ---------------------------------------------------------
R2 = ''
for g, L in enumerate(C.LADDER):
    body = '<div class="tier">Sentences</div>' + ''.join(f'<button class="lline sent" data-a="LS_{g}_{j}">{P}<span>{mark(t)}</span></button>' for j, t in enumerate(L['sents']))
    R2 += lcol(g, body, ','.join(f'LS_{g}_{j}' for j in range(len(L['sents']))))
CH = ''.join(f'<button class="lline ch" data-a="LC_{i}">{P}<span>{mark(t)}</span></button>' for i, t in enumerate(C.CHALLENGE))
S.append(slide('Read aloud: sentences → challenge', head('Pronunciation · Read aloud', 'c-listen', 'Read aloud — <em>sentence → challenge</em>') +
               f'''  <div class="ladder short">{R2}</div>
  <div class="chal"><div class="chh">🔥 Challenge — all three sounds <button class="btn sm y rep" data-rep="LC_0,LC_1,LC_2">🔁 Listen &amp; repeat</button></div>{CH}</div>
'''))

# 13 listening ---------------------------------------------------------------------------------
L = C.LISTEN
S.append(slide('Listening: John & Sarah', head('Listening', 'c-listen', 'Morning routines — <em>John &amp; Sarah</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.LISTEN_ART}</div>
      <div class="card lsrc">
        <div class="lt">🎧 {L['title']}</div>
        <button class="btn" data-a="EL">▶ Play / ⏸ Stop</button>
        <div class="lsm">Source: {L['source']}</div>
      </div>
      <button class="btn y" id="lCheck">✓ Check times</button><button class="btn ghost" id="lScript">📜 Show script</button>
    </div>
    <div class="col grow" style="gap:6px;min-width:0;position:relative">
      <div id="lgist"></div>
      <div id="ldetail" class="col" style="gap:6px;flex:1"></div>
      <div class="lscript card" id="lscr" hidden></div>
    </div>
  </div>
'''))

# 14 frames ------------------------------------------------------------------------------------
S.append(slide('Sentence frames', head('Input · Sentence frames', 'c-input', 'Talk about <em>your day</em>') + '''  <div class="frames" id="frames"></div>
  <div class="linkers"><b>Linkers:</b> <span id="linkers"></span></div>
'''))
# 15 Q&A
S.append(slide('Questions & answers', head('Input · Questions', 'c-input', 'Ask &amp; <em>answer</em> — routines') + '  <div class="qa" id="qa"></div>\n'))
# 16 dialogue
S.append(slide('Model dialogue: Lucy & Minh', head('Model dialogue', 'c-listen', 'Lucy &amp; Minh — <em>two different days</em>') + '''  <div class="dlg">
    <div class="col">
      <div class="card form">
        <div class="fhd">❓ Listen &amp; answer</div>
        <div id="dq" class="col" style="gap:8px"></div>
      </div>
    </div>
    <div class="card" style="display:flex;flex-direction:column;min-height:0">
      <div class="row" style="padding:12px 14px 4px;align-items:center;flex-wrap:wrap;gap:8px">
        <button class="btn sm" id="dlgPlay">▶ Play dialogue</button>
        <button class="btn sm ghost" id="dlgStop">⏹ Stop</button>
        <button class="btn sm y" id="dlgScript">👁 Show script</button>
        <span id="dlgDl"></span>
      </div>
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">L = Lucy · M = Minh</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))
# 17 interview & report
S.append(slide('Interview & report', head('Speaking · Pairs', 'c-speak', 'Interview your partner — <em>then report</em>') + '''  <div class="ivwrap"><table class="ivt" id="iv"></table></div>
  <div class="tip rep2">🔁 <b>Report:</b> Lan usually start<b>s</b> work at eight. It takes <b>her</b> thirty minutes to get to work. She hardly ever miss<b>es</b> breakfast.</div>
'''))
# 18 free practice
S.append(slide('Free practice: two situations', head('Free practice', 'c-speak', 'Two real situations — <em>change the dialogue</em>') + '''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:380px;flex:none;gap:12px" id="sit"></div>
    <div class="card fpd grow" id="fpd"></div>
  </div>
'''))
# 19 fluency
S.append(slide('90-second routine talk', head('Fluency', 'c-speak', 'Your day in <em>90 seconds</em>') + f'''  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="col grow talk2" id="talk"></div>
    <div class="col" style="width:330px;flex:none;align-items:stretch;gap:12px">
      <div class="lart">{I.TALK_ART}</div>
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn y" id="tkStart">⏱ Start 90 seconds</button>
      <button class="btn" id="tkModel">▶ Model talk</button>
    </div>
  </div>
'''))
# 20 game
S.append(slide('Game: Sentence scramble', head('Game', 'c-prac', 'Sentence scramble — <em>put the words in order</em>') + '''  <div class="game2">
    <div class="row" style="align-items:center;justify-content:space-between"><span class="score" id="scN">1 / 8</span><div class="dots" id="scDots"></div><span class="score" id="scScore">Score: 0</span></div>
    <div class="scout" id="scOut"></div>
    <div class="scpool" id="scPool"></div>
    <div id="scMsg" class="scmsg"></div>
    <div class="row" style="justify-content:center"><button class="btn y" id="scCheck">✓ Check</button><button class="btn ghost" id="scReset">↺ Reset</button><button class="btn" id="scNext">Next →</button></div>
  </div>
'''))
# 21 wrap-up
WRAP = [('🗓', 'I can describe my routine on weekdays and at weekends.'),
        ('📊', 'I can say how often: always, usually, often, sometimes, hardly ever, never.'),
        ('🙋', 'I can ask: How often do you…? What time do you…?'),
        ('👄', 'I can say -s endings: starts /s/ · goes /z/ · misses /ɪz/.'),
        ('⏱', 'I can talk about my day for 90 seconds.')]
KEY = [v['col'] for v in C.VOCAB] + ['My day usually starts with…', 'It takes me … minutes to…', 'On weekdays…, whereas at weekends…']
S.append(slide('Wrap-up', head('Wrap-up', 'c-wrap', 'What can you <em>do now</em>?') + '  <div class="row" style="gap:18px;flex:1;min-height:0">\n    <div class="col grow wrap2">' +
               ''.join(f'<label class="chk"><span class="wi">{ic}</span><span class="grow">{e(t)}</span><input type="checkbox"></label>' for ic, t in WRAP) +
               '</div>\n    <div class="card keys"><div class="rh">🔑 Key language</div><div class="kchips">' +
               ''.join(f'<span>{e(k)}</span>' for k in KEY) + '</div></div>\n  </div>\n'))
# 22 homework
S.append(slide('Homework: Reading', head('Homework', 'c-listen', 'After class') + f'''  <div class="hw hw2">
    <div class="card"><h3>📖 Review today's lesson</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div>Flip the word &amp; collocation cards again</div></div>
        <div class="step"><span class="n">2</span><div>always → never · I <b>usually</b> start work at nine.</div></div>
        <div class="step"><span class="n">3</span><div>Read aloud: start<u>s</u> /s/ · go<u>es</u> /z/ · miss<u>es</u> /ɪz/</div></div>
        <div class="step"><span class="n">4</span><div>My day usually starts with… · It takes me… minutes to…</div></div>
        <div class="step"><span class="n">5</span><div>Record your 90-second talk</div></div>
      </div>
    </div>
    <div class="card qrcard"><h3>📚 Homework · Reading</h3>{qr_svg(HW_URL)}
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S02 → 📝 Homework</p><span class="pass">Pass mark: 80%</span></div>
  </div>
'''))
# 23 thank you
S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 03</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">People, Homes &amp; Neighbourhoods</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))

deck = '\n'.join(S)
n = [0]
def num(m):
    n[0] += 1; return f'<span><b>{n[0]:02d}</b></span></div>'
deck = re.sub(r'<span><b>\d\d</b></span></div>', num, deck)
home = '<a href="../../" style="color:var(--blue);font-weight:800;text-decoration:none">← Tất cả bài học</a> · '

CSS = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()


TRACK = lambda sid: ('<script src="../../assets/config.js"></script>'
    '<script>document.write(\'<script src="../../assets/sessions.js?t=\'+Date.now()+\'"><\\/script>\')</script>'
    '<script src="../../assets/student.js"></script>'
    f'<script>GT.guard("{sid}","../../")||GT.lessonOpened("{sid}")</script>\n</body>')


def build():
    head_ = open(os.path.join(HERE, 'shell_head.html'), encoding='utf-8').read().replace('</style>', CSS + '</style>', 1)
    tail_ = open(os.path.join(HERE, 'shell_tail.html'), encoding='utf-8').read()
    core = open(os.path.join(HERE, 'core.js'), encoding='utf-8').read()
    app = open(os.path.join(HERE, 'app.js'), encoding='utf-8').read()
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    man['EL'] = {'file': C.LISTEN['file'], 'label': C.LISTEN['title'], 'dur': 180}
    data = {k: getattr(C, k) for k in ['WARM', 'SORT', 'S_GROUPS', 'FRAMES', 'LINKERS', 'QA', 'DIALOGUE', 'DLG_Q', 'LISTEN', 'INTERVIEW', 'SITUATIONS', 'FP_LINES', 'TALK', 'SCRAMBLE']}
    data['COLL'] = [c[:3] for c in C.COLL]
    app = app.replace('/*DATA_JSON*/', json.dumps(data, ensure_ascii=False))

    def page(audio, base, with_home):
        js = core.replace('/*AUDIO_JSON*/', json.dumps(audio, ensure_ascii=False)).replace("/*ONLINE_BASE*/''", json.dumps(base))
        d = deck
        if with_home:
            first = d.find('<div class="s-foot"><span>'); d = d[:first] + d[first:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home, 1)
            last = d.rfind('<div class="s-foot"><span>'); d = d[:last] + d[last:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home, 1)
        return head_ + '<div id="viewport"><div id="deck">' + d + tail_ + '<script>\n' + js + '\n' + app + '\n</script>\n</body>\n</html>\n'

    def src_path(k, v):
        return os.path.join(HERE, 'listening', os.path.basename(v['file'])) if k == 'EL' else os.path.join(HERE, 'mp3', v['file'])
    web = {k: dict(v, src='audio/' + v['file']) for k, v in man.items()}
    off = {k: dict(v, src='data:audio/mpeg;base64,' + base64.b64encode(open(src_path(k, v), 'rb').read()).decode()) for k, v in man.items()}
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page(web, LESSON_URL, True).replace('</body>', TRACK('S02'), 1))
    open(os.path.join(OUT, 'S02_offline.html'), 'w', encoding='utf-8').write(page(off, '', False))
    shutil.copytree(os.path.join(HERE, 'mp3'), os.path.join(OUT, 'audio'))
    os.makedirs(os.path.join(OUT, 'audio', 'Listening'), exist_ok=True)
    shutil.copy(src_path('EL', man['EL']), os.path.join(OUT, 'audio', C.LISTEN['file']))
    with zipfile.ZipFile(os.path.join(OUT, 'S02_Audio_MP3.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for k, v in sorted(man.items(), key=lambda kv: kv[1]['file']):
            z.write(src_path(k, v), v['file'])
    print('S02 ->', OUT, deck.count('<section class="slide'), 'slides,', len(man), 'audio')


if __name__ == '__main__':
    build()
