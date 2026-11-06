"""Build lesson S02 → ../../../lessons/S02/ (index.html with MP3 files, offline single file, audio ZIP).
Run after gen_audio.py.  Uses the lesson-1 page shell (shell_head.html / shell_tail.html / core.js)."""
import base64, json, os, re, shutil, zipfile
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'lessons', 'S02'))
SITE = 'https://thanh990522.github.io/communication-foundation/'
LESSON_URL = SITE + 'lessons/S02/'
P = '<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>'
FOOT = '  <div class="s-foot"><span>A1 → A2 Communication Accelerator · <b>S02</b></span><span><b>00</b></span></div>\n'

def slide(title, body, cls='slide'):
    return f'<section class="{cls}" data-title="{title}">\n{body}{FOOT}</section>\n'

def head(chip, chipcls, h2):
    return f'  <div class="s-head"><span class="chip {chipcls}">{chip}</span><h2>{h2}</h2></div>\n'

S = []
# 1 cover
S.append(slide('Cover', '''  <span class="chip c-input">Week 01 · Session 02</span>
  <div style="font-weight:800;color:var(--blue);font-size:19px;letter-spacing:.5px;margin-bottom:8px">A1 → A2 COMMUNICATION ACCELERATOR</div>
  <h1>Routines,<br><span>Habits</span> &amp;<br>Real Schedules</h1>
  <div class="meta"><div>⏱ 90 minutes</div><div>💻 Online class</div><div>🗣 Speaking</div></div>
  <div class="teacher"><div class="av">HT</div><div><b>Mr. Hà Chí Thanh</b><span>Lexical Communication Syllabus</span></div></div>
  <div class="cloud" id="cloud"></div>
''', 'slide cover'))
# 2 lesson map
S.append(slide('Lesson map', head('Lesson map', 'c-wrap', "Today's <em>journey</em>") + '''  <div class="agenda">
    <div class="ag warm"><div class="m">1</div><div><b>Warm-up · Spell it!</b><small>Today's words</small></div></div>
    <div class="ag input"><div class="m">2</div><div><b>Words &amp; collocations</b><small>commute · shift · break…</small></div></div>
    <div class="ag input"><div class="m">3</div><div><b>How often?</b><small>always → never</small></div></div>
    <div class="ag prac"><div class="m">4</div><div><b>Collocation check</b><small>Choose the word</small></div></div>
    <div class="ag listen"><div class="m">5</div><div><b>Pronunciation</b><small>-s endings · stress</small></div></div>
    <div class="ag listen"><div class="m">6</div><div><b>Listening</b><small>John &amp; Sarah's mornings</small></div></div>
    <div class="ag input"><div class="m">7</div><div><b>Sentence frames</b><small>My day usually starts with…</small></div></div>
    <div class="ag input"><div class="m">8</div><div><b>Ask &amp; answer</b><small>How often do you…?</small></div></div>
    <div class="ag listen"><div class="m">9</div><div><b>Model dialogue</b><small>Lucy &amp; Minh</small></div></div>
    <div class="ag speak"><div class="m">10</div><div><b>Interview &amp; report</b><small>She usually starts…</small></div></div>
    <div class="ag speak"><div class="m">11</div><div><b>Free practice</b><small>Two situations</small></div></div>
    <div class="ag speak"><div class="m">12</div><div><b>90-second talk · Game</b><small>Sentence scramble</small></div></div>
  </div>
'''))
# 3 objectives
S.append(slide('Objectives', head('Can-do goals', 'c-wrap', 'By the end of today, <em>you can…</em>') + '''  <div class="obj">
    <div class="card"><div class="ic">🗓</div><b>Describe your routine</b><p>On weekdays… whereas at weekends…</p></div>
    <div class="card"><div class="ic">📊</div><b>Say how often</b><p>always · usually · often · sometimes · hardly ever · never</p></div>
    <div class="card"><div class="ic">🙋</div><b>Ask about routines</b><p>How often do you…? What time do you…?</p></div>
    <div class="card"><div class="ic">🔁</div><b>Report a routine</b><p>She usually starts work at eight.</p></div>
    <div class="card"><div class="ic">⏱</div><b>Talk for 90 seconds</b><p>first · then · after that · because</p></div>
  </div>
'''))
# 4 warm-up
S.append(slide('Warm-up: Spell it!', head('Warm-up', 'c-warm', 'Spell it! — <em>today\'s words</em>') + '''  <div class="wgrid" id="warm"></div>
  <div class="row" style="margin-top:14px;align-items:center"><button class="btn y" id="warmCheck">✓ Check</button><button class="btn ghost" id="warmShow">👁 Answers</button><span class="score" id="warmScore">— / 8</span></div>
'''))
# 5 vocabulary
S.append(slide('Words & collocations', head('Input · Words', 'c-input', 'Core words → <em>collocations</em>') + '  <div class="vocab" id="vocab"></div>\n'))
# 6 frequency
S.append(slide('How often?', head('Input · Frequency', 'c-input', 'How often? — <em>always → never</em>') + f'''  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="freq grow" id="freq"></div>
    <div class="col" style="width:360px;flex:none">
      <div class="card rule"><div class="rh">Where?</div>
        <div class="rr">I <b class="adv">usually</b> <u>start</u> work at nine.</div>
        <div class="rr">She <b class="adv">hardly ever</b> <u>misses</u> breakfast.</div>
        <div class="rr">Do you <b class="adv">ever</b> <u>miss</u> breakfast?</div>
        <div class="rr">How <b class="adv">often</b> do you <u>take</u> a break?</div>
      </div>
      <button class="btn" id="fAll">▶ always → never</button>
    </div>
  </div>
'''))
# 7 collocation check
S.append(slide('Collocation check', head('Practice', 'c-prac', 'Choose the <em>right word</em>') + '  <div class="coll" id="coll"></div>\n'))
# 8 pronunciation
S.append(slide('Pronunciation', head('Pronunciation', 'c-listen', 'He start<em>s</em> · she miss<em>es</em> — <em>-s endings</em>') + '''  <div class="sgroups" id="sgroups"></div>
  <div class="card stressbox"><div class="rh">Stress the frequency word</div><div id="stress"></div></div>
'''))
# 9 listening
L = C.LISTEN
S.append(slide('Listening: John & Sarah', head('Listening', 'c-listen', 'Morning routines — <em>John &amp; Sarah</em>') + f'''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:330px;flex:none">
      <div class="card lsrc">
        <div class="rh">🎧 Real recording</div>
        <div class="lt">{L['title']}</div>
        <a class="btn" href="{L['page']}" target="_blank" rel="noopener">▶ Open &amp; play on elllo.org</a>
        <div class="lsm">{L['source']}</div>
      </div>
      <button class="btn y" id="lCheck">✓ Check times</button>
      <button class="btn ghost" id="lScript">📜 Script (after listening)</button>
    </div>
    <div class="col grow" style="gap:6px;min-width:0">
      <div id="lgist"></div>
      <div id="ldetail" class="col" style="gap:6px"></div>
    </div>
  </div>
'''))
# 10 frames
S.append(slide('Sentence frames', head('Input · Sentence frames', 'c-input', 'Talk about <em>your day</em>') + '''  <div class="frames" id="frames"></div>
  <div class="linkers"><b>Linkers:</b> <span id="linkers"></span></div>
'''))
# 11 Q&A
S.append(slide('Questions & answers', head('Input · Questions', 'c-input', 'Ask &amp; <em>answer</em> — routines') + '  <div class="qa" id="qa"></div>\n'))
# 12 dialogue
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
# 13 interview & report
S.append(slide('Interview & report', head('Speaking · Pairs', 'c-speak', 'Interview your partner — <em>then report</em>') + '''  <table class="ivt" id="iv"></table>
  <div class="tip" style="margin-top:12px;font-size:17px">🔁 <b>Report:</b> Lan usually start<b>s</b> work at eight. It takes <b>her</b> thirty minutes to get to work. She hardly ever miss<b>es</b> breakfast.</div>
'''))
# 14 free practice
S.append(slide('Free practice: two situations', head('Free practice', 'c-speak', 'Two real situations — <em>change the dialogue</em>') + '''  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="col" style="width:380px;flex:none;gap:12px" id="sit"></div>
    <div class="card fpd grow" id="fpd"></div>
  </div>
'''))
# 15 fluency
S.append(slide('90-second routine talk', head('Fluency', 'c-speak', 'Your day in <em>90 seconds</em>') + '''  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="col grow" id="talk"></div>
    <div class="col" style="width:330px;flex:none;align-items:stretch">
      <div class="card tkc"><div id="tkTime" class="tkt">1:30</div><div class="tbar"><i id="tkBar"></i></div></div>
      <button class="btn y" id="tkStart">⏱ Start 90 seconds</button>
      <button class="btn" id="tkModel">▶ Model talk</button>
    </div>
  </div>
'''))
# 16 game
S.append(slide('Game: Sentence scramble', head('Game', 'c-prac', 'Sentence scramble — <em>put the words in order</em>') + '''  <div class="row" style="align-items:center;justify-content:space-between"><span class="score" id="scN">1 / 8</span><span class="score" id="scScore">Score: 0</span></div>
  <div class="scout" id="scOut"></div>
  <div class="scpool" id="scPool"></div>
  <div id="scMsg" class="scmsg"></div>
  <div class="row" style="justify-content:center"><button class="btn y" id="scCheck">✓ Check</button><button class="btn ghost" id="scReset">↺ Reset</button><button class="btn" id="scNext">Next →</button></div>
'''))
# 17 wrap-up
S.append(slide('Wrap-up', head('Wrap-up', 'c-wrap', 'What can you <em>do now</em>?') + '''  <div class="col grow">
    <label class="chk"><input type="checkbox"> I can describe my routine on weekdays and at weekends.</label>
    <label class="chk"><input type="checkbox"> I can say how often: always, usually, often, sometimes, hardly ever, never.</label>
    <label class="chk"><input type="checkbox"> I can ask: How often do you…? What time do you…?</label>
    <label class="chk"><input type="checkbox"> I can report a routine: She usually starts work at eight.</label>
    <label class="chk"><input type="checkbox"> I can talk about my day for 90 seconds.</label>
  </div>
'''))
# 18 homework
S.append(slide('Homework: Reading', head('Homework', 'c-listen', 'After class') + '''  <div class="hw">
    <div class="card"><h3>📖 Review today's lesson</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div>Words &amp; collocations · always → never</div></div>
        <div class="step"><span class="n">2</span><div>My day usually starts with… · It takes me… minutes to…</div></div>
        <div class="step"><span class="n">3</span><div>On weekdays…, whereas at weekends…</div></div>
      </div>
    </div>
    <div class="card"><h3>📚 Homework · Reading</h3><p style="font-size:19px;line-height:1.6;word-break:break-all"><b>thanh990522.github.io/<br>communication-foundation</b><br>→ <b>S02</b> → <b>📝 Homework</b></p><p style="font-size:17px;margin-top:8px"><b>Pass mark: 80%</b></p></div>
  </div>
'''))
# 19 thank you
S.append(slide('Thank you', '''  <span class="chip c-warm">See you next time!</span>
  <h1 style="font-size:76px">Thank <span>you!</span></h1>
  <div class="card" style="margin-top:28px;padding:18px 22px;max-width:620px;border-color:var(--blue)">
    <div style="font-weight:800;color:var(--blue);font-size:16px;letter-spacing:1px">NEXT · SESSION 03</div>
    <div style="font-size:26px;font-weight:900;color:var(--navy);margin-top:4px">People, Homes &amp; Neighbourhoods</div>
  </div>
''', 'slide cover'))

deck = '\n'.join(S)
n = [0]
def num(m):
    n[0] += 1; return f'<span><b>{n[0]:02d}</b></span></div>'
deck = re.sub(r'<span><b>\d\d</b></span></div>', num, deck)
home = '<a href="../../" style="color:var(--blue);font-weight:800;text-decoration:none">← Tất cả bài học</a> · '

CSS = '''
/* ===== S02 ===== */
.cover .cloud .wtag{position:absolute;display:flex;align-items:center;gap:8px;padding:12px 18px;border-radius:18px;font-size:24px;font-weight:900;box-shadow:var(--shadow)}
.cover .cloud .wtag span{font-size:26px}
.wgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.wu{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:10px 14px}
.wu .n,.cq .n,.lq .n,.frm .n{flex:none;width:30px;height:30px;border-radius:50%;background:var(--navy);color:var(--yellow);font-weight:900;display:flex;align-items:center;justify-content:center;font-size:15px}
.wu input{flex:1;min-width:0;height:44px;border:2px solid var(--line);border-radius:10px;padding:0 12px;font-size:21px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:1px}
.wu input.ok,.tin.ok{border-color:var(--green);background:var(--green-soft)}.wu input.no,.tin.no{border-color:var(--red);background:var(--red-soft)}
.wu .ans{font-weight:900;color:var(--green);font-size:17px}
.vocab{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;flex:1;align-content:start}
.vc{background:#fff;border:2px solid var(--line);border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:6px}
.vc .vh{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.vc .vh b{font-size:21px;color:var(--navy);font-weight:900}
.vc .vh b{flex:1}
.vc .vh small{order:3;flex-basis:100%;font-size:15px;color:var(--muted);font-weight:600;margin-top:-4px}
.vc .col{font-size:18px;font-weight:800;color:var(--blue);background:var(--sky);border-radius:10px;padding:5px 9px}
.vc .ex{font-size:16px;color:#334155;line-height:1.35}
.freq{display:flex;flex-direction:column;gap:10px;align-content:start}
.fq{display:grid;grid-template-columns:200px 200px 1fr;align-items:center;gap:14px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:8px 14px}
.fbar{height:16px;border-radius:999px;background:var(--sky);position:relative}
.fbar i{display:block;height:100%;border-radius:999px;background:linear-gradient(90deg,var(--blue),var(--yellow))}
.fbar span{position:absolute;right:-2px;top:-22px;font-size:15px;font-weight:800;color:var(--muted)}
.fw{display:flex;align-items:center;gap:8px}.fw b{font-size:22px;color:var(--navy);font-weight:900}
.fx{font-size:17px;color:#334155}
.rule{padding:14px 16px;display:flex;flex-direction:column;gap:8px}
.rh{font-weight:900;color:var(--navy);font-size:17px;margin-bottom:2px}
.rr{font-size:18px;color:var(--ink)}.rr .adv{color:var(--blue)}.rr u{text-decoration-color:var(--yellow);text-decoration-thickness:4px}
.coll{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px;align-content:start}
.cq{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:8px 12px}
.cq .cs{flex:1;font-size:18px;font-weight:700;color:var(--navy)}
.gap{display:inline-block;min-width:38px;text-align:center;color:var(--blue);font-weight:900;border-bottom:3px solid var(--yellow)}
.co{display:flex;gap:6px;flex-wrap:wrap}
.co .opt{height:36px;white-space:nowrap;padding:0 11px;border-radius:10px;border:2px solid var(--line);background:#F8FAFF;font-size:16px;font-weight:800;color:var(--navy)}
.co .opt.ok{background:var(--green-soft);border-color:var(--green);color:var(--green)}
.co .opt.no{background:var(--red-soft);border-color:var(--red);color:var(--red)}
.sgroups{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.sg{background:#fff;border:2px solid var(--line);border-radius:16px;overflow:hidden}
.sgh{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:var(--navy);color:var(--yellow)}
.sgh b{font-size:28px}
.sgw{display:flex;flex-wrap:wrap;gap:8px;padding:12px}
.lb2{height:44px;padding:0 14px;border-radius:12px;background:var(--sky);border:2px solid var(--sky-2);font-size:19px;font-weight:800;color:var(--navy)}
.lb2 u{text-decoration:none;color:var(--red)}
.stressbox{margin-top:14px;padding:14px 18px}
.stl{display:flex;align-items:center;gap:10px;font-size:20px;color:var(--ink);padding:5px 0}
.stl b{color:var(--blue);font-weight:900}
.lsrc{padding:14px 16px;display:flex;flex-direction:column;gap:10px}
.lsrc a.btn{text-decoration:none;justify-content:center}
.lsrc .lt{font-size:19px;font-weight:900;color:var(--navy)}
.lsrc .lsm{font-size:13px;color:var(--muted);font-weight:600}
.lau{width:100%;height:36px}
.lq{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:4px 12px;min-height:44px}
#dq .lq{flex-wrap:wrap;padding:8px 12px}#dq .qt{flex-basis:calc(100% - 44px)}#dq .co{margin-left:40px}
.lq .qt{flex:1;font-size:16.5px;font-weight:700;color:var(--navy)}
.tin{width:130px;height:36px;border:2px solid var(--line);border-radius:9px;padding:0 8px;font-size:17px;font-weight:800;color:var(--navy);text-align:center}
.tans{font-weight:900;color:var(--green);font-size:16px;min-width:50px}
.frames{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;flex:1;align-content:start}
.frm{background:#fff;border:2px solid var(--line);border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.frm .fh{display:flex;align-items:center;gap:10px}.frm .fh b{font-size:20px;color:var(--navy)}
.fe{display:flex;align-items:center;gap:8px;font-size:17px;color:#334155}
.linkers{margin-top:12px;font-size:19px;color:var(--navy);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.lk{background:var(--yellow);color:var(--navy);font-weight:900;padding:5px 12px;border-radius:999px}.arr{color:var(--muted)}
.qa{display:grid;grid-template-columns:1fr 1fr;gap:8px 16px;flex:1;align-content:start}
.qap{display:flex;flex-direction:column;gap:3px;background:#fff;border:2px solid var(--line);border-radius:16px;padding:6px 12px}
.qrow{display:flex;align-items:center;gap:10px}
.qrow .who{flex:none;width:24px;height:24px;border-radius:8px;font-weight:900;font-size:13px;display:flex;align-items:center;justify-content:center}
.qrow.q .who{background:var(--blue);color:#fff}.qrow.a .who{background:var(--yellow);color:var(--navy)}
.qrow span{flex:1;font-size:16px;font-weight:700;color:var(--navy);line-height:1.25}
.qrow.a span{color:#7A5200}
.qap .play.sm{width:28px;height:28px}
.ivt{width:100%;border-collapse:separate;border-spacing:0;border:2px solid var(--line);border-radius:16px;overflow:hidden;font-size:18px}
.ivt th{background:var(--navy);color:#fff;text-align:left;padding:10px 14px;font-size:16px}
.ivt th:nth-child(1){width:34%}.ivt th:nth-child(2){width:20%}
.ivt td{padding:9px 14px;border-top:1.5px solid var(--line);color:var(--navy)}
.ivt td.rpt{color:#7A5200;font-weight:700}
.ivn{width:100%;height:38px;border:2px dashed var(--sky-2);border-radius:9px;padding:0 10px;font-size:17px;color:var(--navy)}
.sit2{border:2px solid var(--line);border-radius:18px;background:#fff;padding:12px 14px;cursor:pointer;display:flex;flex-direction:column;gap:6px}
.sit2.on{border-color:var(--yellow);box-shadow:0 0 0 4px var(--yellow-soft)}
.sit2 h4{font-size:20px;color:var(--navy);display:flex;align-items:center;gap:8px}
.sit2 .rl{display:flex;gap:8px;font-size:16px;line-height:1.35;color:#334155}
.sit2 .rl b{flex:none;width:22px;height:22px;border-radius:6px;display:inline-flex;align-items:center;justify-content:center;font-size:13px;color:#fff;background:var(--blue)}
.sit2 .rl.b b{background:var(--yellow);color:var(--navy)}
.sit2 .card2{background:var(--sky);border-radius:10px;padding:6px 10px;font-size:15.5px;color:var(--navy);font-weight:700}
.fpd{padding:14px 18px;display:flex;flex-direction:column;gap:6px;font-size:18px;line-height:1.35}
.fpd .ln2{display:flex;gap:8px;align-items:baseline}
.fpd .who{flex:none;width:24px;height:24px;border-radius:7px;font-weight:900;font-size:13px;display:inline-flex;align-items:center;justify-content:center;color:#fff;background:var(--blue)}
.fpd .ln2.b .who{background:var(--yellow);color:var(--navy)}
.fpd .slot{display:inline-block;background:var(--yellow-soft);border:2px dashed var(--yellow-2);color:#7A5200;font-weight:800;border-radius:8px;padding:0 7px;margin:0 2px;font-size:17px}
.fpd .hd{font-weight:900;color:var(--navy);font-size:17px;margin-bottom:4px}
.tk2{display:flex;align-items:center;gap:14px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:12px 16px;font-size:21px;color:var(--navy);font-weight:600}
.tkk{flex:none;width:118px;background:var(--navy);color:var(--yellow);font-weight:900;font-size:16px;border-radius:10px;padding:5px 8px;text-align:center}
.tkc{padding:16px;text-align:center}.tkt{font-size:64px;font-weight:900;color:var(--navy);font-variant-numeric:tabular-nums}
.scout{min-height:76px;border:3px dashed var(--sky-2);border-radius:16px;padding:12px;display:flex;flex-wrap:wrap;gap:10px;margin:14px 0;background:#FBFCFF}
.scpool{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;min-height:60px}
.chipw{height:52px;padding:0 18px;border-radius:14px;border:2px solid var(--line);background:#fff;font-size:24px;font-weight:800;color:var(--navy);box-shadow:var(--shadow-s)}
.chipw.on{background:var(--navy);color:var(--yellow);border-color:var(--navy)}
.chipw:disabled{opacity:.25}
.scmsg{text-align:center;font-size:22px;font-weight:800;min-height:34px;margin:10px 0}
.scmsg.good{color:var(--green)}.scmsg.bad{color:var(--red)}
'''

def build():
    head_ = open(os.path.join(HERE, 'shell_head.html'), encoding='utf-8').read().replace('</style>', CSS + '</style>', 1)
    tail_ = open(os.path.join(HERE, 'shell_tail.html'), encoding='utf-8').read()
    core = open(os.path.join(HERE, 'core.js'), encoding='utf-8').read()
    app = open(os.path.join(HERE, 'app.js'), encoding='utf-8').read()
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    data = {k: getattr(C, k) for k in ['WARM', 'VOCAB', 'FREQ', 'COLL', 'S_GROUPS', 'STRESS', 'FRAMES', 'LINKERS', 'QA', 'DIALOGUE', 'DLG_Q', 'LISTEN', 'INTERVIEW', 'SITUATIONS', 'FP_LINES', 'TALK', 'SCRAMBLE']}
    app = app.replace('/*DATA_JSON*/', json.dumps(data, ensure_ascii=False))

    def page(audio, base, with_home):
        js = core.replace('/*AUDIO_JSON*/', json.dumps(audio, ensure_ascii=False)).replace("/*ONLINE_BASE*/''", json.dumps(base))
        d = deck
        if with_home:
            first = d.find('<div class="s-foot"><span>'); d = d[:first] + d[first:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home, 1)
            last = d.rfind('<div class="s-foot"><span>'); d = d[:last] + d[last:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home, 1)
        return head_ + '<div id="viewport"><div id="deck">' + d + tail_ + '<script>\n' + js + '\n' + app + '\n</script>\n</body>\n</html>\n'

    web = {k: dict(v, src='audio/' + v['file']) for k, v in man.items()}
    off = {}
    for k, v in man.items():
        off[k] = dict(v, src='data:audio/mpeg;base64,' + base64.b64encode(open(os.path.join(HERE, 'mp3', v['file']), 'rb').read()).decode())
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page(web, LESSON_URL, True))
    open(os.path.join(OUT, 'S02_offline.html'), 'w', encoding='utf-8').write(page(off, '', False))
    shutil.copytree(os.path.join(HERE, 'mp3'), os.path.join(OUT, 'audio'))
    with zipfile.ZipFile(os.path.join(OUT, 'S02_Audio_MP3.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(os.path.join(HERE, 'mp3')):
            for f in sorted(files):
                p = os.path.join(root, f); z.write(p, os.path.relpath(p, os.path.join(HERE, 'mp3')))
    print('S02 ->', OUT, deck.count('<section class="slide'), 'slides,', len(man), 'audio')

if __name__ == '__main__':
    build()
