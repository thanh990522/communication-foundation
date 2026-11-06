"""One-off restructure of template.html to the new S01 flow (Nov 2026):
Warm-up → Alphabet → Read names easy→hard → Listening: spelling test → Email symbols →
Questions & answers → Model dialogue → Pair practice (own info / ID cards) → Free practice →
Spelling games → Wrap-up → Homework (listening, online)."""
import re

P = 'template.html'
h = open(P, encoding='utf-8').read()
head, rest = h.split('<div id="viewport"><div id="deck">', 1)
deck, tail = rest.split('\n</div></div>\n', 1)

sec = {}
for m in re.finditer(r'<!-- ================= (\d+)\.[^\n]*-->\n<section.*?</section>\n', deck, re.S):
    sec[int(m.group(1))] = m.group(0)
assert len(sec) == 22, len(sec)

PLAY = '<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>'
FOOT = '  <div class="s-foot"><span>A1 → A2 Communication Accelerator · <b>S01</b></span><span><b>00</b></span></div>\n'

def slide(title, body, cls='slide'):
    return f'<!-- ================= {title} ================= -->\n<section class="{cls}" data-title="{title}">\n{body}{FOOT}</section>\n'

# ---------------------------------------------------------------- lesson map
lesson_map = slide('Lesson map', '''  <div class="s-head"><span class="chip c-wrap">Lesson map · 90′</span><h2>Today's <em>journey</em></h2><p class="sub">Warm-up → Alphabet → Names → Listening → Email → Questions → Dialogue → Practice → Free practice → Game</p></div>
  <div class="agenda">
    <div class="ag warm"><div class="m">6′</div><div><b>1 · Warm-up · Say the letters!</b><small>ATM, KFC, VIP…</small></div></div>
    <div class="ag input"><div class="m">16′</div><div><b>2 · The alphabet</b><small>26 letters · 7 sound families · danger zone</small></div></div>
    <div class="ag speak"><div class="m">6′</div><div><b>3 · Read the names · easy → hard</b><small>Tom → Nguyen → Phillips</small></div></div>
    <div class="ag listen"><div class="m">8′</div><div><b>4 · Listening · Spelling test</b><small>Nghe đánh vần & tự viết tên</small></div></div>
    <div class="ag input"><div class="m">6′</div><div><b>5 · Email symbols</b><small>@ at · . dot · _ underscore</small></div></div>
    <div class="ag input"><div class="m">8′</div><div><b>6 · Questions &amp; answers</b><small>How do you spell…? → It's…</small></div></div>
    <div class="ag listen"><div class="m">5′</div><div><b>7 · Model dialogue</b><small>At the reception desk</small></div></div>
    <div class="ag speak"><div class="m">10′</div><div><b>8 · Pair practice</b><small>Thông tin cá nhân hoặc ID card</small></div></div>
    <div class="ag speak"><div class="m">12′</div><div><b>9 · Free practice</b><small>6 tình huống đời thực</small></div></div>
    <div class="ag prac"><div class="m">8′</div><div><b>10 · Spelling games</b><small>Mystery word · Letter wheel</small></div></div>
    <div class="ag wrap"><div class="m">3′</div><div><b>Wrap-up</b><small>Can-do check · exit ticket</small></div></div>
    <div class="ag listen"><div class="m">HW</div><div><b>Homework · Listening</b><small>Spelling test online — nộp trực tiếp</small></div></div>
  </div>
  <div class="row" style="margin-top:10px;align-items:center">
    <div class="grow"><div style="font-weight:800;color:var(--navy);font-size:14px">Tỉ trọng thời gian (ước tính)</div>
      <div class="ratio"><span style="width:33%;background:var(--blue)"></span><span style="width:15%;background:#FFB000"></span><span style="width:52%;background:var(--navy)"></span></div>
      <div class="legend" style="margin-top:6px"><span><i style="background:var(--blue)"></i>Input ≈ 33%</span><span><i style="background:#FFB000"></i>Listening ≈ 15%</span><span><i style="background:var(--navy)"></i>Học viên nói (pairs, role-play, games) ≈ 52%</span></div>
    </div>
  </div>
''')

objectives = slide('Objectives', '''  <div class="s-head"><span class="chip c-wrap">Can-do goals</span><h2>By the end of today, <em>you can…</em></h2><p class="sub">Sau buổi học này, bạn có thể…</p></div>
  <div class="obj">
    <div class="card"><div class="ic">🔤</div><b>Say all 26 letters clearly</b><p>Đọc đúng tên chữ cái theo 7 nhóm âm, không nhầm A/E/I, G/J.</p></div>
    <div class="card"><div class="ic">🗣</div><b>Spell names aloud</b><p>Đánh vần tên từ dễ đến khó, kể cả "double L".</p></div>
    <div class="card"><div class="ic">👂</div><b>Catch spelled names</b><p>Nghe một lần và viết đúng tên được đánh vần.</p></div>
    <div class="card"><div class="ic">📧</div><b>Read email addresses</b><p>@ at · . dot · _ underscore · all lower case.</p></div>
    <div class="card"><div class="ic">🙋</div><b>Ask &amp; answer</b><p>"How do you spell…?" · "Could you spell that again, please?"</p></div>
  </div>
  <div class="tip" style="margin-top:20px;font-size:17px">🎯 <b>Success criterion (theo syllabus):</b> spell personal details accurately with <b>≥ 80% accuracy</b> — đánh vần thông tin cá nhân chính xác từ 80% trở lên.</div>
  <div class="tip" style="margin-top:10px;background:var(--sky);border-color:var(--blue)">🗣 <b>Class rule today:</b> Every time you hear a letter — <b>say it back</b>. Unmute, speak, mute. Đừng chỉ nghe — hãy nói!</div>
''')

names_test = slide('Listening: Spelling test', '''  <div class="badges"><span class="badge y">⏱ 8′</span><span class="badge">👂 → ✍</span></div>
  <div class="s-head"><span class="chip c-listen">Listening · Spelling test</span><h2>Listen &amp; <em>write the names</em></h2><p class="sub">Mỗi câu: nghe tên → nghe đánh vần <b>1 lần</b> ở tốc độ tự nhiên → viết họ (surname) · dạng bài Spelling của IELTS Listening</p></div>
  <div class="row" style="gap:18px;flex:1;min-height:0">
    <div class="nt grow" id="nt"></div>
    <div class="col" style="width:300px">
      <div class="card" style="padding:14px">
        <div style="font-weight:900;color:var(--navy);margin-bottom:6px">Example</div>
        <div class="ntex"><span class="ntt">Mr</span><b>BLACK</b></div>
        <div style="font-size:14px;color:var(--muted);margin-top:4px">"Question one. Mister Black. B-L-A-C-K."</div>
      </div>
      <div class="tip" style="font-size:14px">⚠️ Tên có thể viết nhiều cách (Hayes / Hays). <b>Viết đúng như được đánh vần</b> — sai 1 chữ là sai cả câu.</div>
      <div class="row" style="flex-wrap:wrap"><button class="btn" id="ntAll">▶ Play all</button><button class="btn y" id="ntCheck">✓ Check</button><button class="btn ghost" id="ntShow">👁 Answers</button><button class="btn ghost" id="ntReset">↺</button></div>
      <span class="score" id="ntScore">— / 10</span>
      <div class="tip" style="font-size:14px;background:var(--sky);border-color:var(--blue)">✍ <b>Your turn:</b> viết <b>tên của bạn</b> bằng chữ IN HOA vào chat → unmute và đánh vần cho cả lớp nghe.</div>
    </div>
  </div>
''')

email = slide('Email symbols', '''  <div class="badges"><span class="badge y">⏱ 6′</span><span class="badge">👂 Listen → 🗣 Read aloud</span></div>
  <div class="s-head"><span class="chip c-input">Input · Email</span><h2>How to read <em>email addresses</em></h2><p class="sub">Nghe từng ký hiệu → nhắc lại → đọc to 4 email · bấm ▶ để kiểm tra</p></div>
  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="symg" id="symg"></div>
    <div class="col grow">
      <div style="font-weight:900;color:var(--navy);font-size:18px">🗣 Read these emails aloud</div>
      <div id="emails" class="col" style="gap:10px"></div>
      <div class="card" style="padding:12px 16px;display:flex;gap:18px;align-items:center;flex-wrap:wrap">
        <div class="row" style="align-items:center;gap:8px"><b style="font-size:40px;color:var(--navy);line-height:1">J</b><span><b style="color:var(--blue)">capital J</b><br><small style="color:var(--muted)">chữ in hoa</small></span><button class="play sm" data-a="CAP_J">''' + PLAY + '''</button></div>
        <div class="row" style="align-items:center;gap:8px"><b style="font-size:40px;color:var(--blue);line-height:1">j</b><span><b style="color:var(--blue)">small j</b><br><small style="color:var(--muted)">chữ thường</small></span><button class="play sm" data-a="SMALL_J">''' + PLAY + '''</button></div>
        <div class="row" style="align-items:center;gap:8px"><button class="play sm" data-a="PH_LOWER">''' + PLAY + '''</button><span>It's <b>all lower case</b>.</span></div>
      </div>
    </div>
  </div>
''')

qa = slide('Questions & answers', '''  <div class="badges"><span class="badge y">⏱ 8′</span><span class="badge">👂 → 🗣 Pairs</span></div>
  <div class="s-head"><span class="chip c-input">Input · Sentence patterns</span><h2>Ask &amp; <em>answer</em> — spelling questions</h2><p class="sub">Nghe câu hỏi (▶ xanh) và câu trả lời (▶ vàng) → nhắc lại → luyện theo cặp: A hỏi, B trả lời, rồi đổi vai</p></div>
  <div class="qa" id="qa"></div>
''')

practice = slide('Pair practice: your info or ID card', '''  <div class="badges"><span class="badge y">⏱ 10′</span><span class="badge">👥 Pairs · swap</span></div>
  <div class="s-head"><span class="chip c-speak">Speaking · Pair practice</span><h2>Your info <em>or an ID card</em></h2><p class="sub">B dùng thông tin thật của mình <b>hoặc</b> một ID card thầy phát · A hỏi theo khung và gõ lại vào chat để kiểm tra</p></div>
  <div class="row" style="gap:20px;flex:1;min-height:0">
    <div class="card grow" style="padding:16px 20px;font-size:18px;line-height:1.85">
      <div><b style="color:var(--blue)">A:</b> Hello! What's your name, please?</div>
      <div><b style="color:#B07800">B:</b> My name's <span class="blank">&nbsp;</span>.</div>
      <div><b style="color:var(--blue)">A:</b> How do you spell your first name / surname?</div>
      <div><b style="color:#B07800">B:</b> It's <span class="blank">&nbsp;</span>.</div>
      <div><b style="color:var(--blue)">A:</b> Sorry, could you spell that again, please?</div>
      <div><b style="color:var(--blue)">A:</b> Is that <span class="blank" style="min-width:50px">&nbsp;</span> as in <span class="blank" style="min-width:90px">&nbsp;</span>? <b style="color:#B07800">B:</b> Yes, that's right. / No, it's…</div>
      <div><b style="color:var(--blue)">A:</b> What's your email address?</div>
      <div><b style="color:#B07800">B:</b> It's <span class="blank">&nbsp;</span>. It's all lower case.</div>
      <div><b style="color:var(--blue)">A:</b> Let me check: <span class="blank">&nbsp;</span>. <b style="color:#B07800">B:</b> Perfect, thanks!</div>
    </div>
    <div class="col" style="width:400px">
      <div class="idc" id="idc"></div>
      <div class="row" style="flex-wrap:wrap"><button class="btn y" id="idDraw">🎲 Draw a card</button><button class="btn sm" id="idCopy">📋 Copy card</button><button class="btn sm ghost" id="idAll">📋 Copy all 10 cards</button></div>
      <div class="tip" style="font-size:14px">🔁 <b>Round 1:</b> B dùng thông tin thật · <b>Round 2:</b> B rút ID card · rồi đổi vai. A gõ tên + email vào chat → B xác nhận.</div>
    </div>
  </div>
''')

free = slide('Free practice: real situations', '''  <div class="badges"><span class="badge y">⏱ 12′</span><span class="badge">👥 Breakout pairs</span></div>
  <div class="s-head"><span class="chip c-speak">Free practice</span><h2>Real situations — <em>no script!</em></h2><p class="sub">Chọn (hoặc quay) 1 tình huống · tự nghĩ câu · dùng thông tin thật hoặc tự tạo · đổi vai sau mỗi tình huống</p></div>
  <div class="sit" id="sit"></div>
  <div class="row" style="margin-top:12px;align-items:stretch;gap:14px">
    <button class="btn y" id="sitPick">🎲 Random situation</button>
    <div class="tip grow" style="font-size:15px">✅ <b>Checklist:</b> chào hỏi · hỏi <i>"How do you spell…?"</i> · dùng <i>"Could you spell that again, please?"</i> · hỏi 1 email · đọc lại <i>"Let me check…"</i> · cảm ơn &amp; kết thúc.</div>
  </div>
''')

wrap = slide('Wrap-up & exit ticket', '''  <div class="badges"><span class="badge y">⏱ 3′</span><span class="badge">💬 Chat</span></div>
  <div class="s-head"><span class="chip c-wrap">Wrap-up</span><h2>What can you <em>do now</em>?</h2><p class="sub">Tự đánh giá · Error corner · Exit ticket</p></div>
  <div class="row" style="gap:20px;flex:1">
    <div class="col grow">
      <label class="chk"><input type="checkbox"> I can say all 26 letters clearly (A-E-I, G-J, H, R…).</label>
      <label class="chk"><input type="checkbox"> I can spell names aloud — even "double L".</label>
      <label class="chk"><input type="checkbox"> I can listen and write a spelled name.</label>
      <label class="chk"><input type="checkbox"> I can read an email address: at · dot · underscore.</label>
      <label class="chk"><input type="checkbox"> I can ask "How do you spell…?" &amp; "Could you spell that again, please?"</label>
    </div>
    <div class="col" style="width:420px">
      <div class="card" style="padding:14px;flex:1">
        <div style="font-weight:800;color:var(--red);margin-bottom:6px">🛠 Error corner</div>
        <div contenteditable="true" style="min-height:120px;font-size:15px;line-height:1.6;outline:none;border:2px dashed var(--line);border-radius:10px;padding:8px">• H → "hát" ✗ → /eɪtʃ/ ✓<br>• G ↔ J đảo ngược<br>• </div>
      </div>
      <div class="tip">🎟 <b>Exit ticket:</b> unmute và đánh vần <b>email</b> của bạn (hoặc email tự tạo) — cả lớp gõ lại vào chat.</div>
    </div>
  </div>
''')

homework = slide('Homework: Listening', '''  <div class="badges"><span class="badge y">HW</span></div>
  <div class="s-head"><span class="chip c-listen">Homework · Listening</span><h2>Spelling test — <em>online homework</em></h2><p class="sub">Làm và nộp trực tiếp trên website · chấm điểm ngay · thầy xem kết quả của từng bạn</p></div>
  <div class="hw">
    <div class="card"><h3>🎧 4 parts · 24 questions</h3>
      <div class="steps">
        <div class="step"><span class="n">1</span><div><b>People's names</b> — nghe "Mr / Mrs / Ms…" và viết họ (8 câu).</div></div>
        <div class="step"><span class="n">2</span><div><b>Street names</b> — viết tên đường được đánh vần (6 câu).</div></div>
        <div class="step"><span class="n">3</span><div><b>Towns &amp; cities</b> — viết tên thành phố (5 câu).</div></div>
        <div class="step"><span class="n">4</span><div><b>Booking form</b> — nghe cuộc gọi đặt phòng, điền form (5 câu) · dạng IELTS Listening Section 1.</div></div>
      </div>
    </div>
    <div class="col">
      <div class="card"><h3>🔗 Link làm bài</h3><p style="font-size:17px;line-height:1.5;word-break:break-all"><b>thanh990522.github.io/communication-foundation</b><br>→ <b>S01</b> → <b>📝 Homework</b></p><p style="font-size:15px;color:var(--muted);margin-top:6px">Đăng nhập bằng tên + email (dùng cùng email mỗi lần).</p></div>
      <div class="card"><h3>✅ Mẹo làm bài</h3><p style="font-size:15.5px;line-height:1.5">Nghe <b>1 lần</b> trước như thi thật, viết ngay. Sau đó mới nghe lại để kiểm tra. Mục tiêu: <b>≥ 80%</b> (20/24).</p></div>
    </div>
  </div>
''')

order = [
    sec[1], lesson_map, objectives, sec[4],          # cover, map, goals, warm-up
    sec[5], sec[7], sec[9], sec[8],                  # alphabet: 26 letters, families, clinic, odd one out
    sec[11],                                         # read the names easy -> hard
    names_test,                                      # listening
    email, qa,                                       # email symbols, questions & answers
    sec[13],                                         # model dialogue
    practice, free,                                  # pair practice, free practice
    sec[17], sec[18],                                # games
    wrap, homework, sec[22],
]
new_deck = '\n'.join(order)
# fix titles / chips of kept slides for the new stage names
new_deck = new_deck.replace('<span class="chip c-input">Input 1</span><h2>The <em>26 letters</em>', '<span class="chip c-input">Alphabet · 1</span><h2>The <em>26 letters</em>')
new_deck = new_deck.replace('<span class="chip c-input">Input 2</span><h2>7 <em>sound families</em>', '<span class="chip c-input">Alphabet · 2</span><h2>7 <em>sound families</em>')
new_deck = new_deck.replace('<span class="chip c-listen">Pronunciation clinic</span>', '<span class="chip c-listen">Alphabet · 3 · Danger zone</span>')
new_deck = new_deck.replace('<span class="chip c-prac">Controlled practice</span><h2>Odd one out', '<span class="chip c-prac">Alphabet · 4 · Check</span><h2>Odd one out')
new_deck = new_deck.replace('<span class="chip c-speak">Speaking · Spell it!</span>', '<span class="chip c-speak">Read the names</span>')
new_deck = new_deck.replace('<span class="chip c-prac">Game 1</span>', '<span class="chip c-prac">Spelling game 1</span>')
new_deck = new_deck.replace('<span class="chip c-prac">Game 2</span>', '<span class="chip c-prac">Spelling game 2</span>')
new_deck = new_deck.replace('Click từng chữ để nghe · "Play A–Z" để nghe cả bảng · Màu ở đáy = nhóm âm (xem slide sau)', 'Click từng chữ để nghe · "Play A–Z" để nghe cả bảng · Màu ở đáy = nhóm âm (slide sau)')
new_deck = new_deck.replace('<span class="badge y">⏱ 4′</span><span class="badge">👂 Listen twice</span>', '<span class="badge y">⏱ 5′</span><span class="badge">👂 Listen twice</span>')
new_deck = new_deck.replace('<span class="badge y">⏱ 3′</span><span class="badge">🎮 Whole class</span>', '<span class="badge y">⏱ 4′</span><span class="badge">🎮 Whole class</span>')
new_deck = new_deck.replace('<span class="badge y">⏱ 3′</span><span class="badge">🗣 Individual · 20s</span>', '<span class="badge y">⏱ 4′</span><span class="badge">🗣 Individual · 20s</span>')
new_deck = new_deck.replace('<div class="vn">Great job spelling today — keep saying letters out loud!</div>', '<div class="vn">Great job spelling today — don\'t forget your listening homework!</div>')

# renumber page numbers
n = [0]
def num(m):
    n[0] += 1
    return f'<span><b>{n[0]:02d}</b></span></div>'
new_deck = re.sub(r'<span><b>\d\d</b></span></div>', num, new_deck)

css = '''
/* ---------- spelling test ---------- */
.nt{display:grid;grid-template-columns:1fr 1fr;gap:10px;align-content:start}
.nti{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:8px 12px}
.nti .n{flex:none;width:30px;height:30px;border-radius:50%;background:var(--navy);color:var(--yellow);font-weight:900;display:flex;align-items:center;justify-content:center;font-size:14px}
.ntt{flex:none;min-width:46px;font-weight:900;color:var(--blue);font-size:18px}
.nti input{flex:1;min-width:0;height:42px;border:2px solid var(--line);border-radius:10px;padding:0 10px;font-size:19px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:1px}
.nti input.ok{border-color:var(--green);background:var(--green-soft)}
.nti input.no{border-color:var(--red);background:var(--red-soft)}
.nti .ans{flex:none;font-weight:900;color:var(--green);font-size:15px;min-width:0}
.nti.now{border-color:var(--yellow);box-shadow:0 0 0 3px var(--yellow-soft)}
.ntex{display:flex;align-items:center;gap:10px;font-size:22px;color:var(--navy)}
/* ---------- email symbols ---------- */
.symg{display:grid;grid-template-columns:1fr 1fr;gap:10px;width:470px;align-content:start}
.sy{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:8px 10px}
.sy .k{flex:none;min-width:58px;height:46px;padding:0 8px;border-radius:10px;background:var(--navy);color:var(--yellow);font-size:22px;font-weight:900;display:flex;align-items:center;justify-content:center;font-family:'Noto Sans',monospace}
.sy span{flex:1;font-weight:800;color:var(--navy);font-size:16px;line-height:1.2}
.em{display:flex;align-items:center;gap:12px;background:#fff;border:2px solid var(--line);border-radius:14px;padding:10px 14px}
.em b{flex:1;font-family:'Noto Sans',monospace;font-size:24px;color:var(--navy);letter-spacing:.3px}
.em .rv{font-size:14px;font-weight:700;color:var(--blue)}
/* ---------- questions & answers ---------- */
.qa{display:grid;grid-template-columns:1fr 1fr;gap:10px 16px;flex:1;align-content:start}
.qap{display:flex;flex-direction:column;gap:6px;background:#fff;border:2px solid var(--line);border-radius:16px;padding:8px 12px}
.qrow{display:flex;align-items:center;gap:10px}
.qrow .who{flex:none;width:26px;height:26px;border-radius:8px;font-weight:900;font-size:13px;display:flex;align-items:center;justify-content:center}
.qrow.q .who{background:var(--blue);color:#fff}.qrow.a .who{background:var(--yellow);color:var(--navy)}
.qrow span{flex:1;font-size:17px;font-weight:700;color:var(--navy);line-height:1.3}
.qrow.a span{color:#7A5200}
.qap .play.sm{width:30px;height:30px}
/* ---------- ID cards ---------- */
.idc{background:linear-gradient(135deg,var(--navy),var(--blue));color:#fff;border-radius:20px;padding:18px 20px;box-shadow:var(--shadow);position:relative;overflow:hidden;min-height:210px}
.idc::after{content:"";position:absolute;right:-40px;top:-40px;width:130px;height:130px;border-radius:50%;background:var(--yellow);opacity:.9}
.idc .lab{font-size:12px;font-weight:800;letter-spacing:1.4px;color:var(--yellow);text-transform:uppercase}
.idc .nm{font-size:30px;font-weight:900;margin:6px 0 10px;line-height:1.1;position:relative;z-index:1}
.idc .ln2{display:flex;gap:8px;font-size:16px;margin-top:4px}
.idc .ln2 i{font-style:normal;color:#C9D6FF;min-width:62px;font-weight:700}
.idc .ln2 b{font-family:'Noto Sans',monospace;font-weight:700}
.idc .no{position:absolute;right:18px;bottom:14px;font-weight:900;color:var(--yellow);font-size:14px}
/* ---------- free practice ---------- */
.sit{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;flex:1;align-content:start}
.st{background:#fff;border:2px solid var(--line);border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:6px;transition:.2s}
.st h4{font-size:17px;color:var(--navy);display:flex;gap:8px;align-items:center}
.st h4 .e{font-size:22px}
.st p{font-size:14px;line-height:1.4;color:#334155}
.st p b{color:var(--blue)}
.st.pick{border-color:var(--yellow);box-shadow:0 0 0 4px var(--yellow-soft);transform:scale(1.02)}
'''
head = head.replace('</style>', css + '</style>', 1)

open(P, 'w', encoding='utf-8').write(head + '<div id="viewport"><div id="deck">' + new_deck + '\n</div></div>\n' + tail)
print('slides:', new_deck.count('<section class="slide'))
