import re,json,base64,os
h=open('template.html',encoding='utf-8').read()
def rep(a,b,count=1):
    global h
    assert a in h, a[:80]
    h=h.replace(a,b,count)
P='<svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg>'
# ---- CSS: full-screen deck, no toolbar ----
rep("#viewport{position:fixed;inset:0 0 56px 0;overflow:hidden}","#viewport{position:fixed;inset:0;overflow:hidden;background:#fff}")
rep("#deck{position:absolute;left:50%;top:50%;width:1280px;height:720px;transform-origin:center center;background:#fff;box-shadow:0 20px 60px rgba(11,31,92,.18);border-radius:6px;overflow:hidden}",
    "#deck{position:absolute;left:0;top:0;width:1280px;height:720px;transform-origin:0 0;background:#fff;overflow:hidden}")
rep("html,body{height:100%;background:#E9EEF8;","html,body{height:100%;background:#fff;")
rep("#notesPanel{position:fixed;left:16px;right:16px;bottom:66px;","#notesPanel{position:fixed;left:16px;right:16px;bottom:16px;")
rep("#noVoice{","/*x*/#noVoiceX{")
extra_css='''
.dl{display:inline-flex;align-items:center;gap:4px;font-size:12px;font-weight:800;color:var(--blue);text-decoration:none;background:var(--sky);border:1.5px solid var(--sky-2);padding:4px 8px;border-radius:8px;white-space:nowrap}
.dl:hover{background:var(--yellow-soft);border-color:var(--yellow)}
.fcol .ff{gap:6px;align-items:center}
.lib{flex:1;min-height:0;overflow:auto;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;align-items:start;padding-right:6px}
.lg{background:#fff;border:2px solid var(--line);border-radius:14px;padding:10px 12px}.lg.wide{grid-column:1/-1}.lg.wide .lgl{display:grid;grid-template-columns:repeat(4,1fr);column-gap:18px}
.lg h4{font-size:14.5px;color:var(--navy);margin-bottom:6px;display:flex;justify-content:space-between}
.lg h4 small{color:var(--muted);font-weight:600}
.li{display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px dashed var(--line);font-size:13px;font-weight:600}
.li:last-child{border-bottom:none}.li span{flex:1}.li small{color:var(--muted);font-size:11px}
.li .play.sm{width:26px;height:26px}.li .play.sm svg{width:10px;height:10px}
'''
rep("</style>",extra_css+"</style>")
# ---- remove banner, toolbar, menu; simplify timer ----
h=re.sub(r'<div id="noVoice">.*?</div>\n','',h,count=1,flags=re.S)
h=re.sub(r'<!-- ================= TOOLBAR ================= -->.*?<div id="menuPanel"></div>\n','<div id="notesPanel"></div>\n',h,count=1,flags=re.S)
h=re.sub(r'<div id="timer">.*?\n</div>\n','<div id="timer"><div class="d" id="tD">00:30</div></div>\n',h,count=1,flags=re.S)
rep("#timer{position:fixed;top:14px;right:14px;z-index:70;background:#fff;border:3px solid var(--navy);border-radius:18px;box-shadow:var(--shadow);padding:10px 12px;display:none;width:236px}",
    "#timer{position:fixed;top:14px;right:14px;z-index:70;background:#fff;border:3px solid var(--navy);border-radius:18px;box-shadow:var(--shadow);padding:6px 18px;display:none}")
# ---- buttons using TTS -> audio ids ----
rep("""data-seq='["capital J"]'""",'data-a="CAP_J"'); rep("""data-seq='["small J"]'""",'data-a="SMALL_J"')
rep("""data-seq='["It is all lower case."]'""",'data-a="PH_LOWER"'); rep("""data-seq='["It is all capitals."]'""",'data-a="PH_CAPS"')
rep("""data-seq='["Is that a capital letter?"]'""",'data-a="PH_CAPQ"')
rep("""data-seq='["car"]'""",'data-a="W_CAR"'); rep("""data-seq='["why"]'""",'data-a="W_WHY"')
h=re.sub(r"""data-seq='\["Hi, my name is Linh\.".*?\]'""",'data-a="MODEL"',h,count=1)
rep('<button class="lb" data-letter="U">U</button><button class="lb" data-letter="Z">Z</button>',
    '<button class="lb" data-letter="U">U</button><button class="lb" data-letter="Z">Z 🇬🇧</button><button class="lb" data-a="L_Z_US">Z 🇺🇸</button>')
assert 'data-seq' not in h.split('<script>')[0]
# ---- download slots ----
rep('<div class="tip grow" style="padding:9px 14px">🅰 <b>5 vowel letters</b>','<span id="azDl"></span><div class="tip grow" style="padding:9px 14px">🅰 <b>5 vowel letters</b>')
rep('<button class="btn" id="famAll">▶ Chant all 7 families</button>','<button class="btn" id="famAll">▶ Chant all 7 families</button><span id="famDl"></span>')
rep('<span style="font-size:12px;color:var(--muted);font-weight:600">Click 1 dòng để nghe riêng dòng đó</span>','<span id="dlgDl"></span>')
rep('<div class="script blur" id="script"></div>','<div style="padding:0 14px;font-size:12px;color:var(--muted);font-weight:600">Click 1 dòng để nghe riêng dòng đó · R = Receptionist · L = Linh</div><div class="script blur" id="script"></div>')
# ---- text updates ----
rep('<span>Bấm vào chữ cái để nghe · <span class="kbd">←</span> <span class="kbd">→</span> chuyển slide · <span class="kbd">N</span> ghi chú GV</span>',
    '<span>Bấm vào chữ cái để nghe · <span class="kbd">←</span> <span class="kbd">→</span> chuyển slide · <span class="kbd">F</span> toàn màn hình</span>')
rep('<li>Mở file bằng <b>Chrome hoặc Edge</b>, có Internet để có giọng đọc tự nhiên (Google / Microsoft Natural). Chọn giọng UK/US và tốc độ ở thanh công cụ dưới cùng.</li>',
    '<li>Toàn bộ audio là file MP3 thật đã nhúng sẵn trong file (giọng Anh–Anh), chạy offline, không cần Internet. Mỗi bài nghe có nút ⬇ để tải MP3; slide cuối là "Audio library" chứa toàn bộ file.</li>')
h=h.replace('Phím tắt: <span class="kbd">←/→</span> chuyển slide · <span class="kbd">F</span> toàn màn hình · <span class="kbd">N</span> ghi chú · <span class="kbd">T</span> đồng hồ · <span class="kbd">M</span> mục lục · <span class="kbd">Esc</span> dừng audio.',
    'Phím tắt (không có thanh điều khiển trên màn hình): <span class="kbd">←/→</span> hoặc bút trình chiếu để chuyển slide · <span class="kbd">F</span> toàn màn hình · <span class="kbd">N</span> bật/tắt ghi chú GV · <span class="kbd">Esc</span> dừng audio.')
h=re.sub(r'<li>Z: đổi UK/US ở thanh công cụ.*?</li>','<li>Z: file dùng giọng Anh–Anh ("zed"). Muốn nghe kiểu Mỹ ("zee") → slide Pronunciation clinic, nút Z 🇺🇸.</li>',h,count=1)
h=re.sub(r'<li>Lưu ý chọn UK/US:.*?</li>','<li>Audio dùng giọng Anh–Anh: Z ở nhóm /e/ (zed). Tiếng Mỹ: Z = zee (nhóm /iː/), O ~ /oʊ/, R ~ /ɑːr/.</li>',h,count=1)
h=re.sub(r'Đổi tốc độ[^<]*<','Dùng nút <b>SLOW</b> nếu nghe chưa kịp, hoặc tải MP3 về điện thoại để nghe lại.<',h,count=1)
# ---- library slide (before Thank-you? append at end as appendix) ----
lib='''
<!-- ================= 23. AUDIO LIBRARY ================= -->
<section class="slide" data-title="Audio library">
  <div class="s-head"><span class="chip c-wrap">Appendix · Audio</span><h2>Audio <em>library</em> — nghe &amp; tải MP3</h2><p class="sub">Toàn bộ audio của buổi học (giọng neural Anh–Anh) · bấm ▶ để nghe · bấm ⬇ để tải từng file</p></div>
  <div class="lib" id="lib"></div>
  <div class="s-foot"><span>A1 → A2 Communication Accelerator · <b>S01</b></span><span><b>23</b></span></div>
  <aside class="notes"><h4>Ghi chú</h4><ul><li>Tất cả file cũng có trong gói ZIP gửi kèm, sắp xếp theo thư mục hoạt động.</li></ul></aside>
</section>
'''

# ---- script ----
man=json.load(open('manifest.json'))
for k,v in man.items():
    v['src']='data:audio/mpeg;base64,'+base64.b64encode(open('mp3/'+v['file'],'rb').read()).decode()
js=open('script.js',encoding='utf-8').read().replace('/*AUDIO_JSON*/',json.dumps(man,ensure_ascii=False))
h=re.sub(r'<script>.*</script>',lambda m:'<script>\n'+js+'\n</script>',h,count=1,flags=re.S)
os.makedirs('dist',exist_ok=True)
open('dist/S01_embedded.html','w',encoding='utf-8').write(h)
print(len(h)/1e6,'MB', h.count('<section class="slide'))
h=open('dist/S01_embedded.html',encoding='utf-8').read()
h=re.sub(r'/\* ---------- toolbar ---------- \*/\n(?:#toolbar[^\n]*\n|#voiceInfo[^\n]*\n)+','',h)
h=re.sub(r'#menuPanel[^\n]*\n','',h)
h=re.sub(r'/\*x\*/#noVoiceX[^\n]*\n','',h)
h=re.sub(r'#timer \.(ps|ct)[^\n]*\n','',h)
open('dist/S01_embedded.html','w',encoding='utf-8').write(h)
print('cleaned', 'toolbar' in h)
