"""Build lesson S04 → ../../../lessons/S03/ (index.html with MP3 files, offline single file, audio ZIP).
Run after gen_audio.py.  Same page shell and architecture as S02."""
import base64, html, io, json, os, re, shutil, zipfile
import content as C
import sys as _s; _s.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mcshuffle import shuffle_content; shuffle_content(C, 'S04')
import illus04 as I
from structures import struct_slide, JS as STRUCT_JS, CSS as STRUCT_CSS

HERE = os.path.dirname(os.path.abspath(__file__))
SID = 'S04'
OUT = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'lessons', SID))
SITE = 'https://thanh990522.github.io/communication-foundation/'
LESSON_URL = SITE + f'lessons/{SID}/'
HW_URL = SITE + f'homework/?s={SID}'
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



exec(open(os.path.join(HERE, 'slides04.py'), encoding='utf-8').read())

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


__import__('sys').path.insert(0, os.path.dirname(HERE)); from audiopolicy import apply as audio_policy

def build():
    head_ = open(os.path.join(HERE, 'shell_head.html'), encoding='utf-8').read().replace('</style>', CSS + '</style>', 1)
    tail_ = open(os.path.join(HERE, 'shell_tail.html'), encoding='utf-8').read()
    core = open(os.path.join(HERE, 'core.js'), encoding='utf-8').read()
    app = open(os.path.join(HERE, 'app.js'), encoding='utf-8').read() + '\n' + STRUCT_JS
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    man['EL'] = {'file': C.LISTEN['file'], 'label': C.LISTEN['title'], 'dur': C.LISTEN['dur']}
    data = {k: getattr(C, k) for k in ['WARM', 'DIALOGUE', 'DLG_NAMES', 'LISTEN', 'MSGFIX', 'RACE']}
    data['COLL'] = [c[:3] for c in C.COLL]
    data['MAPQ'] = C.DIARYQ
    data['DLG_Q'] = C.DLG_Q[:2]
    data['CARD'] = C.CARD
    data['PAIR_TEST'] = C.PAIR_TEST
    data['ROLECARDS'] = C.ROLECARDS
    app = app.replace('/*DATA_JSON*/', json.dumps(data, ensure_ascii=False))

    def page(audio, base, with_home):
        js = core.replace('/*AUDIO_JSON*/', json.dumps(audio, ensure_ascii=False)).replace("/*ONLINE_BASE*/''", json.dumps(base))
        d = deck
        if with_home:
            first = d.find('<div class="s-foot"><span>'); d = d[:first] + d[first:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home, 1)
            last = d.rfind('<div class="s-foot"><span>'); d = d[:last] + d[last:].replace('<div class="s-foot"><span>', '<div class="s-foot"><span>' + home, 1)
        return audio_policy(head_ + '<div id="viewport"><div id="deck">' + d + tail_ + '<script>\n' + js + '\n' + app + '\n</script>\n</body>\n</html>\n')

    def src_path(k, v):
        return os.path.join(HERE, 'listening', os.path.basename(v['file'])) if k == 'EL' else os.path.join(HERE, 'mp3', v['file'])
    web = {k: dict(v, src='audio/' + v['file']) for k, v in man.items()}
    off = {k: dict(v, src='data:audio/mpeg;base64,' + base64.b64encode(open(src_path(k, v), 'rb').read()).decode()) for k, v in man.items()}
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page(web, LESSON_URL, True).replace('</body>', TRACK('S04'), 1))
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
