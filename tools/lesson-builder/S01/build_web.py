"""Turn the embedded-audio lesson (dist/S01_embedded.html) into the website version:
audio is served as separate MP3 files next to the page, so every ▶ plays a real file
and every ⬇ downloads a real MP3 link. Output goes to ../../../lessons/S01/."""
import json, os, re, shutil, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'dist', 'S01_embedded.html')
OUT = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'lessons', 'S01'))
MP3 = os.path.join(HERE, 'mp3')

h = open(SRC, encoding='utf-8').read()
SITE = 'https://thanh990522.github.io/communication-foundation/'
LESSON_URL = SITE + 'lessons/S01/'
offline = h  # single-file version: audio embedded, works with no Internet

# 1) replace the embedded AUDIO table with relative MP3 paths
m = re.search(r'const AUDIO = (\{.*?\});\s*const ONLINE_BASE', h, re.S)
assert m, 'AUDIO table not found'
audio = json.loads(m.group(1))
for v in audio.values():
    v['src'] = 'audio/' + v['file']
h = h[:m.start(1)] + json.dumps(audio, ensure_ascii=False) + h[m.end(1):]
assert "/*ONLINE_BASE*/''" in h
h = h.replace("/*ONLINE_BASE*/''", json.dumps(LESSON_URL))

# 2) link back to the course home on the cover and the closing slide
home = '<a href="../../" style="color:var(--blue);font-weight:800;text-decoration:none">← Tất cả bài học</a>'
first = h.find('<div class="s-foot"><span>')
h = h[:first] + h[first:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home + ' · ', 1)
last = h.rfind('<div class="s-foot"><span>')
h = h[:last] + h[last:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home + ' · ', 1)

# 3) write page + audio + zip
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
track = ('<script src="../../assets/config.js"></script>'
         '<script>document.write(\'<script src="../../assets/sessions.js?t=\'+Date.now()+\'"><\\/script>\')</script>'
         '<script src="../../assets/student.js"></script>'
         '<script>GT.guard("S01","../../")||GT.lessonOpened("S01")</script>\n</body>')
import sys; sys.path.insert(0, os.path.dirname(HERE)); from audiopolicy import apply as audio_policy
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(audio_policy(h).replace('</body>', track, 1))
open(os.path.join(OUT, 'S01_offline.html'), 'w', encoding='utf-8').write(audio_policy(offline))
shutil.copytree(MP3, os.path.join(OUT, 'audio'))
with zipfile.ZipFile(os.path.join(OUT, 'S01_Audio_MP3.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(MP3):
        for f in sorted(files):
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, MP3))
print('web lesson ->', OUT, f'{len(h)/1e3:.0f} KB page,', len(audio), 'audio clips')
