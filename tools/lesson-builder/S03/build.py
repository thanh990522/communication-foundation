"""Build lesson S03 → ../../../lessons/S03/ (index.html with MP3 files, offline single file, audio ZIP).
Run after gen_audio.py.  Same page shell and architecture as S02."""
import base64, html, io, json, os, re, shutil, zipfile
import content as C
import sys as _s; _s.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mcshuffle import shuffle_content; shuffle_content(C, 'S03')
import illus03 as I
from structures import struct_slide, JS as STRUCT_JS, CSS as STRUCT_CSS

HERE = os.path.dirname(os.path.abspath(__file__))
SID = 'S03'
OUT = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'lessons', SID))
SITE = 'https://thanh990522.github.io/communication-foundation/'
LESSON_URL = SITE + f'lessons/{SID}/'
HW_URL = SITE + f'homework/shadow.html?s={SID}'
P = '<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>'
FOOT = f'  <div class="s-foot"><span>A1 → A2 Communication Accelerator · <b>{SID}</b></span><span><b>00</b></span></div>\n'
e = html.escape
COLS = ['ss', 'zz', 'iz']


def slide(title, body, cls='slide'):
    return f'<section class="{cls}" data-title="{title}">\n{body}{FOOT}</section>\n'


def head(chip, chipcls, h2):
    return f'  <div class="s-head"><span class="chip {chipcls}">{chip}</span><h2>{h2}</h2></div>\n'


def pb(aid, cls=''):
    return f'<button class="play sm{" " + cls if cls else ""}" data-a="{aid}">{P}</button>'


def fin(w, col):
    """highlight the final consonant letters of a word"""
    m = re.search(r'([bcdfghjklmnpqrstvwxz]+)$', w)
    return f'{e(w[:m.start()])}<u class="{col}">{e(m.group(1))}</u>' if m else e(w)


def mark(t, col):
    return re.sub(r'\*([^*]+)\*', lambda m: f'<b class="mk">{fin(m.group(1), col)}</b>', e(t))


def qr_svg(url):
    import qrcode, qrcode.image.svg as qs
    b = io.BytesIO(); qrcode.make(url, image_factory=qs.SvgPathImage, box_size=10, border=1).save(b)
    s = b.getvalue().decode(); s = s[s.index('<svg'):]
    return re.sub(r'width="[^"]+" height="[^"]+"', 'class="qr"', s, count=1)


S = []
# 1 cover --------------------------------------------------------------------------------------
S.append(slide('Cover', '''  <span class="chip c-input">Week 01 · Session 03</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>People,<br><span>Homes</span> &amp;<br>Neighbourhoods</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))

# 2 lesson map ---------------------------------------------------------------------------------
AG = [('warm', '🏠', 'Warm-up · This or that?', 'I live in…'),
      ('input', '📍', 'Places near me', 'park · gym · bus stop…'),
      ('input', '🃏', 'Words → collocations', 'a spacious apartment…'),
      ('prac', '🔗', 'Match the halves', 'a spacious + apartment'),
      ('input', '🧱', '4 key structures', 'step by step + translate'),
      ('prac', '🗺', 'Look at the map', 'is · are · isn’t · aren’t'),
      ('listen', '👄', 'Word stress · final sounds', 'con·VE·ni·ent · par<u>k</u>'),
      ('listen', '🎧', 'Listening', "Sarah &amp; John's hometowns"),
      ('listen', '🎭', 'Model dialogue', 'Tom &amp; Mai'),
      ('speak', '🎙', 'Interview · Free practice', 'Report · two situations'),
      ('speak', '🗣', 'Picture task · 90-second talk', 'Describe your neighbourhood'),
      ('prac', '🧠', 'Game: Memory picture', 'There is / There are…')]
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '  <div class="agenda ag2">\n' +
               ''.join(f'    <div class="ag {c}"><div class="m">{i + 1}</div><span class="agi">{ic}</span><div><b>{t}</b><small>{s}</small></div></div>\n'
                       for i, (c, ic, t, s) in enumerate(AG)) + '  </div>\n'))

# 3 objectives ---------------------------------------------------------------------------------
OBJ = [('🏠', 'Describe your home', 'a spacious apartment · centrally located'),
       ('📍', 'Say what is near you', 'There is a park near my home.'),
       ('❓', 'Ask about a place', 'Is there a…? · Are there any…?'),
       ('👍', 'Say what you like / don’t like', 'One thing I like is… · The only problem is…'),
       ('⏱', 'Talk for 90 seconds', 'and · but · because · so · however')]
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '  <div class="obj obj2">\n' +
               ''.join(f'    <div class="card"><div class="ic">{ic}</div><b>{t}</b><p>{p}</p></div>\n' for ic, t, p in OBJ) + '  </div>\n'))

# 4 warm-up: this or that ----------------------------------------------------------------------
TOT = ''.join(f'<div class="tot"><span class="n">{i + 1}</span>'
              f'<button class="toc" data-a="WA_{i}_0"><span class="te">{ea}</span><b>{e(wa)}</b></button><span class="or">or</span>'
              f'<button class="toc y" data-a="WA_{i}_1"><span class="te">{eb}</span><b>{e(wb)}</b></button></div>'
              for i, (ea, wa, eb, wb, sa, sb) in enumerate(C.WARM))
S.append(slide('Warm-up: This or that?', head('Warm-up', 'c-warm', 'This or that? — <em>where do you live?</em>') +
               f'  <div class="row" style="gap:18px;flex:1;min-height:0"><div class="totg grow">{TOT}</div>'
               '<div class="card frame1"><div class="rh">🗣 Answer</div><div class="fbig">I live in <span class="gap">___</span>.</div><div class="fbig">My home is <span class="gap">___</span>.</div>'
               '<div class="fbig">I live <span class="gap">___</span>.</div><div class="fsm">— And you?</div></div></div>\n'))

# 5 places -------------------------------------------------------------------------------------
PL = ''.join(f'<div class="flip plc" data-flip><div class="in"><div class="fc"><span class="pe">{em}</span><div class="fwd"><b>{e(w)}</b>{pb(f"PL_{i}")}</div><span class="turn">↻</span></div>'
             f'<div class="bk"><b>{e(w)}</b><span class="vi">{e(vi)}</span><span class="ex">“There is a {e(w)} near my home.”</span>{pb(f"PL_{i}", "y")}</div></div></div>'
             for i, (w, em, vi) in enumerate(C.PLACES))
TOOLS = '  <div class="ftools"><span>↻ Click a card to flip</span><button class="btn sm ghost" data-flipall>🔄 Flip all</button><button class="btn sm ghost" data-flipreset>↺ Reset</button></div>\n'
S.append(slide('Places near me', head('Input · Places', 'c-input', 'Places <em>near me</em>') + f'  <div class="fgrid">{PL}</div>\n' + TOOLS))


# 6-7 words → collocations ---------------------------------------------------------------------
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


for part, idx in ((1, range(0, 4)), (2, range(4, 8))):
    S.append(slide(f'Words → collocations {part}', head(f'Input · Words &amp; collocations {part}/2', 'c-input', 'Word → <em>collocation</em>') +
                   '  <div class="fgrid wcgrid">' + ''.join(word_card(i, C.VOCAB[i]) for i in idx) +
                   ''.join(phrase_card(i, C.VOCAB[i]) for i in idx) + '</div>\n' + TOOLS))


# 8 collocation check --------------------------------------------------------------------------
def coll_row(i, s, opts, k, pre='ci', aid='CO'):
    btns = ''.join(f'<button class="opt" data-{pre}="{i}" data-o="{e(o)}">{e(o)}</button>' for o in opts)
    sent = e(s).replace('___', '<span class="gap">___</span>')
    ico = f'<div class="ico">{I.WORD[k]}</div>' if k else ''
    return (f'<div class="cq2" id="{pre}q{i}">{ico}<div class="cbody"><div class="cs"><span class="n">{i + 1}</span><span>{sent}</span></div>'
            f'<div class="co">{btns}</div></div>{pb(f"{aid}_{i}", "y")}</div>')


MT_L = ''.join(f'<button class="mt l" data-mt="{i}"><b>{e(a)}</b></button>' for i, (a, b) in enumerate(C.MATCH))
import random as _r
_R = list(enumerate(C.MATCH)); _r.Random('S03-match').shuffle(_R)
MT_R = ''.join(f'<button class="mt r" data-mr="{e(b)}"><b>{e(b)}</b></button>' for i, (a, b) in _R)
S.append(slide('Match the halves', head('Practice · Collocations', 'c-prac', 'Match the halves — <em>make a collocation</em>') +
               f'  <div class="mtgrid"><div class="mtcol">{MT_L}</div><div class="mtmid">🔗</div><div class="mtcol">{MT_R}</div></div>\n'
               '  <div class="ftools"><span>Click a word on the left, then its partner on the right</span><span class="score" id="mtScore">✓ 0 / 8</span><button class="btn sm ghost" id="mtReset">↺ Reset</button></div>\n'))

# 9-12 main structures (step by step)
for _i, _st in enumerate(C.STRUCTS):
    S.append(struct_slide(slide, head, P, _i, len(C.STRUCTS), _st))

# 10 map practice ------------------------------------------------------------------------------
S.append(slide('Look at the map', head('Practice · There is / are', 'c-prac', 'Look at the map — <em>my neighbourhood</em>') +
               f'  <div class="row" style="gap:16px;flex:1;min-height:0"><div class="mapbox">{I.MAP}</div>'
               '<div class="col grow mapq">' + ''.join(coll_row(i, s, o, None, 'mq', 'MQ') for i, (s, o, a) in enumerate(C.MAPQ)) +
               '<div class="ftools" style="margin-top:4px"><span class="score" id="mqScore">✓ 0 / 8</span><button class="btn sm ghost" id="mqReset">↺ Reset</button></div></div></div>\n'))

# 11 word stress: sort -------------------------------------------------------------------------
BK = ''.join(f'<div class="bucket {COLS[g]}" data-b="{g}"><div class="bh"><b class="pat">{e(dots)}</b><span>{e(name)}</span>{pb(f"PAT_{g}", "y" if g == 1 else "")}</div><div class="bz" id="bz{g}"></div></div>'
             for g, (name, dots) in enumerate(C.PATTERNS))
S.append(slide('Word stress', head('Pronunciation · Word stress', 'c-listen', 'SPA·cious · con·<em>VE</em>·ni·ent · fa·<em>CI</em>·li·ty') +
               f'''  <div class="keyw">{''.join(f'<button class="kw" data-a="SW_{i}"><b>{e(syl)}</b><span>{e(C.PATTERNS[k][1])}</span></button>' for i, (w, syl, k) in enumerate(C.STRESS_WORDS) if w in ('spacious', 'convenient', 'facility'))}<div class="kwr"><span>Say the <b>BIG</b> syllable <b>louder</b> &amp; <b>longer</b>.</span></div></div>
  <div class="pool card" id="pool"></div>
  <div class="buckets">{BK}</div>
  <div class="ftools"><span class="score" id="sortScore">— / {len(C.STRESS_WORDS)}</span><button class="btn sm y" id="sortCheck">✓ Check</button><button class="btn sm ghost" id="sortShow">👁 Answers</button><button class="btn sm ghost" id="sortReset">↺ Reset</button></div>
'''))


# 12-13 final consonants ladder ----------------------------------------------------------------
def lcol(g, body, qid):
    return (f'<div class="lad {COLS[g]}"><div class="ladh"><b class="ipa">{e(C.FINALS[g]["snd"])}</b>'
            f'<button class="btn sm rep" data-rep="{qid}">🔁 Listen &amp; repeat</button></div>{body}</div>')


R1 = R2 = ''
for g, L in enumerate(C.FINALS):
    col = COLS[g]
    body = ('<div class="tier">Words</div><div class="wchips">' + ''.join(f'<button class="wchip" data-a="FW_{g}_{j}">{fin(w, col)}</button>' for j, w in enumerate(L['words'])) + '</div>'
            '<div class="tier">Phrases</div>' + ''.join(f'<button class="lline" data-a="LP_{g}_{j}">{P}<span>{mark(t, col)}</span></button>' for j, t in enumerate(L['phrases'])))
    R1 += lcol(g, body, ','.join([f'FW_{g}_{j}' for j in range(len(L['words']))] + [f'LP_{g}_{j}' for j in range(len(L['phrases']))]))
    body = '<div class="tier">Sentences</div>' + ''.join(f'<button class="lline sent" data-a="LS_{g}_{j}">{P}<span>{mark(t, col)}</span></button>' for j, t in enumerate(L['sents']))
    R2 += lcol(g, body, ','.join(f'LS_{g}_{j}' for j in range(len(L['sents']))))
S.append(slide('Final sounds: words → phrases', head('Pronunciation · Final sounds', 'c-listen', 'Don’t drop the <em>last sound</em> — word → phrase') + f'  <div class="ladder">{R1}</div>\n'))
CH = ''.join(f'<button class="lline ch" data-a="LC_{i}">{P}<span>{mark(t, "ss")}</span></button>' for i, t in enumerate(C.CHALLENGE))
S.append(slide('Final sounds: sentences → challenge', head('Pronunciation · Final sounds', 'c-listen', 'Final sounds — <em>sentence → challenge</em>') +
               f'''  <div class="ladder short">{R2}</div>
  <div class="chal"><div class="chh">🔥 Challenge — keep every final sound <button class="btn sm y rep" data-rep="LC_0,LC_1,LC_2">🔁 Listen &amp; repeat</button></div>{CH}</div>
'''))

# 14 listening ---------------------------------------------------------------------------------
L = C.LISTEN
S.append(slide('Listening: Sarah & John', head('Listening', 'c-listen', 'My hometown — <em>Sarah &amp; John</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none;gap:10px">
      <div class="lart">{I.LISTEN_ART}</div>
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
# 17 dialogue
S.append(slide('Model dialogue: Tom & Mai', head('Model dialogue', 'c-listen', 'Tom &amp; Mai — <em>a new neighbour</em>') + '''  <div class="dlg">
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
      <div style="padding:0 14px;font-size:15px;color:var(--muted);font-weight:600">T = Tom · M = Mai</div>
      <div class="script blur" id="script"></div>
    </div>
  </div>
'''))
# 18 interview
S.append(slide('Interview & report', head('Speaking · Pairs', 'c-speak', 'Interview your partner — <em>then report</em>') + '''  <div class="ivwrap"><table class="ivt" id="iv"></table></div>
  <div class="tip rep2">🔁 <b>Report:</b> Lan live<b>s</b> in a spacious apartment. It's peaceful <b>because</b> there is a park near <b>her</b> home. The only problem is the crowded market.</div>
'''))
# 19 free practice
S.append(slide('Free practice: two situations', head('Free practice', 'c-speak', 'Two real situations — <em>change the dialogue</em>') + '''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:380px;flex:none;gap:12px" id="sit"></div>
    <div class="card fpd grow" id="fpd"></div>
  </div>
'''))
# 20 picture task
PF = ''.join(f'<label class="pfr"><input type="checkbox"><span class="n">{i + 1}</span><span>{e(t).replace("___", "<span class=gap>___</span>")}</span></label>' for i, t in enumerate(C.PIC_FRAMES))
S.append(slide('Picture: five sentences', head('Speaking · Real-life task', 'c-speak', 'Describe the picture — <em>5 sentences</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="picbox">{I.SCENE}</div>
    <div class="col" style="width:420px;flex:none;gap:10px">
      <div class="col pfl">{PF}</div>
      <div class="row" style="align-items:center;gap:10px"><div class="pict" id="picTime">1:00</div><button class="btn y grow" id="picStart">⏱ Start 60 seconds</button></div>
    </div>
  </div>
'''))
# 21 fluency
S.append(slide('90-second place description', head('Fluency', 'c-speak', 'My neighbourhood in <em>90 seconds</em>') + f'''  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="col grow talk2" id="talk"></div>
    <div class="col" style="width:340px;flex:none;align-items:stretch;gap:10px">
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn y" id="tkStart">⏱ Start 90 seconds</button>
      <button class="btn" id="tkModel">▶ Model talk</button>
      <div class="card fuq"><div class="rh">🙋 Follow-up questions</div>{''.join(f'<button class="gx" data-a="FU_{i}">{P}<span>{e(q)}</span></button>' for i, q in enumerate(C.FOLLOW_UP))}</div>
    </div>
  </div>
'''))
# 22 game: memory picture
MEM = ''.join(f'<button class="memc" data-mem="{i}" data-a="MEM_{i}"><span class="q">?</span><span class="ans"><i>{em}</i>{e(t)}</span></button>' for i, (em, t) in enumerate(C.MEMORY))
S.append(slide('Game: Memory picture', head('Game', 'c-prac', 'Memory picture — <em>what can you remember?</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="memart" id="memArt">{I.MEMORY_ART}<div class="memcover" id="memCover"><b>🧠</b><span>What is in the picture?</span><small>Say: There is a… · There are…</small></div></div>
    <div class="col" style="width:400px;flex:none;gap:10px">
      <div class="row" style="justify-content:space-between;align-items:center"><span class="pict" id="memTime">0:20</span><span class="score" id="memScore">✓ 0 / {len(C.MEMORY)}</span></div>
      <div class="row" style="gap:8px"><button class="btn y grow" id="memStart">👀 Look for 20 seconds</button><button class="btn ghost" id="memShow">🖼 Show</button></div>
      <div class="memg">{MEM}</div>
      <div class="tip" style="font-size:15px;padding:8px 12px">Teams take turns. Correct sentence → click a card to reveal it.</div>
    </div>
  </div>
'''))
# 23 wrap-up
WRAP = [('🏠', 'I can describe my home: a spacious apartment, centrally located.'),
        ('📍', 'I can say what is near me: There is a park near my home.'),
        ('❓', 'I can ask: Is there a…? Are there any…?'),
        ('👍', 'I can say what I like and the only problem.'),
        ('⏱', 'I can describe my neighbourhood for 90 seconds.')]
KEY = [v['col'] for v in C.VOCAB] + ['There is / There are…', 'One thing I like is…', 'It is … because…', 'The only problem is…', 'and · but · so · however']
S.append(slide('Wrap-up', head('Wrap-up', 'c-wrap', 'What can you <em>do now</em>?') + '  <div class="row" style="gap:18px;flex:1;min-height:0">\n    <div class="col grow wrap2">' +
               ''.join(f'<label class="chk"><span class="wi">{ic}</span><span class="grow">{e(t)}</span><input type="checkbox"></label>' for ic, t in WRAP) +
               '</div>\n    <div class="card keys"><div class="rh">🔑 Key language</div><div class="kchips">' +
               ''.join(f'<span>{e(k)}</span>' for k in KEY) + '</div></div>\n  </div>\n'))
# 24 homework
S.append(slide('Homework: Shadowing', head('Homework', 'c-listen', 'After class') + f'''  <div class="hw hw2">
    <div class="card"><h3>🎙 Speaking homework · Shadowing</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div><b>Listen</b> to the whole conversation with the script.</div></div>
        <div class="step"><span class="n">2</span><div><b>Shadow</b> each line: listen → speak at the same time.</div></div>
        <div class="step"><span class="n">3</span><div><b>Record</b> each line and listen to yourself.</div></div>
        <div class="step"><span class="n">4</span><div>Keep every <b>final sound</b> and the <b>word stress</b>: con·VE·ni·ent.</div></div>
        <div class="step"><span class="n">5</span><div>Press <b>Nộp bài</b> — you need <b>80%</b> or do it again.</div></div>
      </div>
    </div>
    <div class="card qrcard"><h3>📝 Open the homework</h3>{qr_svg(HW_URL)}
      <p><b>thanh990522.github.io/communication-foundation</b><br>→ S03 → 📝 Homework</p><span class="pass">Pass mark: 80%</span></div>
  </div>
'''))
# 25 thank you
S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:560px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 04</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">Time, Appointments &amp; Arrangements</div>
  </div>
  <div class="cloud" id="cloud2"></div>
''', 'slide cover'))

deck = '\n'.join(S)
n = [0]
def num(m):
    n[0] += 1; return f'<span><b>{n[0]:02d}</b></span></div>'
deck = re.sub(r'<span><b>\d\d</b></span></div>', num, deck)
home = '<a href="../../" style="color:var(--blue);font-weight:800;text-decoration:none">← Tất cả bài học</a> · '
CSS = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read() + STRUCT_CSS


TRACK = lambda sid: ('<script src="../../assets/config.js"></script>'
    '<script>document.write(\'<script src="../../assets/sessions.js?t=\'+Date.now()+\'"><\\/script>\')</script>'
    '<script src="../../assets/student.js"></script>'
    f'<script>GT.guard("{sid}","../../")||GT.lessonOpened("{sid}")</script>\n</body>')


def build():
    head_ = open(os.path.join(HERE, 'shell_head.html'), encoding='utf-8').read().replace('</style>', CSS + '</style>', 1)
    tail_ = open(os.path.join(HERE, 'shell_tail.html'), encoding='utf-8').read()
    core = open(os.path.join(HERE, 'core.js'), encoding='utf-8').read()
    app = open(os.path.join(HERE, 'app.js'), encoding='utf-8').read() + '\n' + STRUCT_JS
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    man['EL'] = {'file': C.LISTEN['file'], 'label': C.LISTEN['title'], 'dur': C.LISTEN['dur']}
    data = {k: getattr(C, k) for k in ['WARM', 'DIALOGUE', 'DLG_NAMES', 'DLG_Q', 'LISTEN', 'INTERVIEW', 'SITUATIONS', 'FP_LINES', 'TALK', 'MATCH', 'MEMORY']}
    data['COLL'] = [c[:3] for c in C.COLL]
    data['MAPQ'] = C.MAPQ
    data['SORT'] = [[w, k, syl] for w, syl, k in C.STRESS_WORDS]
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
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page(web, LESSON_URL, True).replace('</body>', TRACK('S03'), 1))
    open(os.path.join(OUT, f'{SID}_offline.html'), 'w', encoding='utf-8').write(page(off, '', False))
    shutil.copytree(os.path.join(HERE, 'mp3'), os.path.join(OUT, 'audio'))
    os.makedirs(os.path.join(OUT, 'audio', 'Listening'), exist_ok=True)
    shutil.copy(src_path('EL', man['EL']), os.path.join(OUT, 'audio', C.LISTEN['file']))
    with zipfile.ZipFile(os.path.join(OUT, f'{SID}_Audio_MP3.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for k, v in sorted(man.items(), key=lambda kv: kv[1]['file']):
            z.write(src_path(k, v), v['file'])
    print(SID, '->', OUT, deck.count('<section class="slide'), 'slides,', len(man), 'audio')


if __name__ == '__main__':
    build()
