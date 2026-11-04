"""Build Homework S01 (Alphabet & Spelling).
Writes  homework/data/S01.json   (questions; auto-graded answers stored only as SHA-256 hashes)
        homework/audio/S01/*.mp3  (new spelling dictation audio, Microsoft neural voice via edge-tts)
Run:    SSL_CA_BUNDLE=... python3 build.py      (needs ffmpeg, numpy, edge-tts)
"""
import asyncio, hashlib, json, os, re, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SESSION = 'S01'
AUDIO_DIR = os.path.join(ROOT, 'homework', 'audio', SESSION)
CACHE = os.path.join(HERE, 'cache')
VOICE = 'en-GB-SoniaNeural'
SR = 24000

# ------------------------------------------------------------------ content
LETTER = lambda L: f'lessons/S01/audio/Letters/S01_letter_{L}.mp3'
DICT = [  # (id, text to spell)
    ('B1', 'KHANH'), ('B2', 'VUONG'), ('B3', 'THOMPSON'), ('B4', 'JOHNNY'),
    ('B5', 'hoa_le@yahoo.com'), ('B6', 'minh.tran88@gmail.com'),
]
HOMEWORK = {
    'session': SESSION,
    'title': 'Alphabet & Spelling Out Loud',
    'intro': 'Làm bài trong khoảng 20–25 phút. Phần A–D được chấm tự động; phần E–F thầy sẽ chấm và nhận xét.',
    'sections': [
        {'id': 'A', 'title': 'A. Listen & choose', 'vi': 'Nghe và chọn chữ cái đúng', 'items': [
            {'id': f'A{i+1}', 'type': 'listen_mcq', 'prompt': 'Which letter do you hear?', 'audio': LETTER(ans), 'options': opts, 'answer': [ans]}
            for i, (ans, opts) in enumerate([('G', ['J', 'G', 'Z']), ('E', ['I', 'A', 'E']), ('H', ['H', 'A', 'K']),
                                             ('R', ['A', 'O', 'R']), ('Y', ['I', 'Y', 'W']), ('Q', ['U', 'K', 'Q'])])]},
        {'id': 'B', 'title': 'B. Listen & write', 'vi': 'Nghe đánh vần và viết lại (tên viết IN HOA, email viết thường)', 'items': [
            {'id': qid, 'type': 'listen_type', 'prompt': ('Write the email address.' if '@' in txt else 'Write the name.'),
             'audio': f'homework/audio/{SESSION}/{SESSION}_HW_{qid}.mp3', 'placeholder': ('email…' if '@' in txt else 'NAME'),
             'answer': [txt]} for qid, txt in DICT]},
        {'id': 'C', 'title': 'C. Odd one out', 'vi': 'Chọn chữ cái có âm khác nhóm', 'items': [
            {'id': f'C{i+1}', 'type': 'mcq', 'prompt': 'Which letter has a different sound?', 'options': opts, 'answer': [ans]}
            for i, (opts, ans) in enumerate([(['A', 'J', 'K', 'E'], 'E'), (['B', 'C', 'F', 'D'], 'F'),
                                             (['O', 'Q', 'U', 'W'], 'O'), (['L', 'M', 'N', 'P'], 'P'), (['H', 'J', 'K', 'G'], 'G')])]},
        {'id': 'D', 'title': 'D. Complete the phrases', 'vi': 'Điền 1 từ vào chỗ trống', 'items': [
            {'id': 'D1', 'type': 'gap', 'prompt': 'How do you ____ your surname?', 'answer': ['spell']},
            {'id': 'D2', 'type': 'gap', 'prompt': 'Could you spell that ____, please?', 'answer': ['again']},
            {'id': 'D3', 'type': 'gap', 'prompt': 'Is that a ____ letter? (= chữ in hoa)', 'answer': ['capital']},
            {'id': 'D4', 'type': 'gap', 'prompt': 'My email is all ____ case. (= chữ thường)', 'answer': ['lower']},
            {'id': 'D5', 'type': 'gap', 'prompt': 'In an email address, "@" is read as ____.', 'answer': ['at']},
            {'id': 'D6', 'type': 'gap', 'prompt': '"_" is read as ____.', 'answer': ['underscore']},
        ]},
        {'id': 'E', 'title': 'E. Writing', 'vi': 'Viết — thầy chấm', 'items': [
            {'id': 'E1', 'type': 'writing', 'points': 10, 'minWords': 40,
             'prompt': 'Write a short dialogue (6–8 lines) at a hotel reception. The receptionist asks for your name and email, asks you to spell them, and uses "Could you spell that again, please?" once.'},
            {'id': 'E2', 'type': 'writing', 'points': 5, 'minWords': 6,
             'prompt': 'Write 3 English words you see every day and how you spell them. Example: KFC — K-F-C.'},
        ]},
        {'id': 'F', 'title': 'F. Voice note #1', 'vi': 'Ghi âm — thầy chấm', 'items': [
            {'id': 'F1', 'type': 'voice', 'points': 10, 'maxSec': 180,
             'prompt': 'Record 60–90 seconds: (1) say the alphabet by sound families (A-H-J-K, B-C-D-E…), (2) spell your full name and your email, (3) say and spell 3 English words you see every day.'},
        ]},
    ],
}

# ------------------------------------------------------------------ hashing (must match homework page + Code.gs)
def norm(s):
    return re.sub(r'[\s\-–—]+', '', str(s).lower())

def h(session, qid, ans):
    return hashlib.sha256(f'{session}|{qid}|{norm(ans)}'.encode('utf-8')).hexdigest()

# ------------------------------------------------------------------ audio
NUM = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def tokens(s):
    out = []; at = s.find('@'); loc = s if at < 0 else s[:at]; dom = '' if at < 0 else s[at + 1:]; i = 0
    while i < len(loc):
        c = loc[i]
        if c.isalpha():
            U = c.upper()
            if i + 1 < len(loc) and loc[i + 1].upper() == U: out.append('double ' + U); i += 2; continue
            out.append(U)
        elif c.isdigit(): out.append(NUM[int(c)])
        elif c == '.': out.append('dot')
        elif c == '_': out.append('underscore')
        elif c == '-': out.append('hyphen')
        i += 1
    if at >= 0:
        out.append('at')
        for k, p in enumerate(dom.split('.')):
            if k: out.append('dot')
            out.append(p)
    return out

def ck(t): return os.path.join(CACHE, hashlib.md5(f'{VOICE}|{t}'.encode()).hexdigest() + '.mp3')

async def fetch(texts):
    import certifi
    if os.environ.get('SSL_CA_BUNDLE'): certifi.where = lambda: os.environ['SSL_CA_BUNDLE']
    import edge_tts
    os.makedirs(CACHE, exist_ok=True)
    for t in texts:
        p = ck(t)
        if os.path.exists(p) and os.path.getsize(p) > 0: continue
        for _ in range(4):
            try:
                await edge_tts.Communicate(t, VOICE).save(p)
                if os.path.getsize(p) > 0: break
            except Exception as e:
                print('retry', t, e, file=sys.stderr); await asyncio.sleep(2)

def load(t):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', ck(t), '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); idx = np.where(np.abs(a) > 0.012)[0]
    return a if not len(idx) else a[max(0, idx[0] - int(.03 * SR)): idx[-1] + int(.06 * SR)]

def sil(s): return np.zeros(int(s * SR), np.float32)

def build_audio():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    allt = sorted({t for _, txt in DICT for t in tokens(txt)})
    asyncio.run(fetch(allt))
    for qid, txt in DICT:
        parts = [sil(.15)]
        toks = tokens(txt)
        for k, t in enumerate(toks):
            parts.append(load(t)); parts.append(sil(.38 if k < len(toks) - 1 else .1))
        # say it twice, like a real dictation
        once = np.concatenate(parts)
        a = np.concatenate([once, sil(1.2), once, sil(.3)])
        out = os.path.join(AUDIO_DIR, f'{SESSION}_HW_{qid}.mp3')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-codec:a', 'libmp3lame', '-b:a', '64k', out],
                       input=a.tobytes(), check=True)
    print('audio ->', AUDIO_DIR)

# ------------------------------------------------------------------ write json
def build_json():
    hw = json.loads(json.dumps(HOMEWORK))
    auto_max = 0
    for sec in hw['sections']:
        for it in sec['items']:
            it.setdefault('points', 1)
            if 'answer' in it:
                it['ah'] = [h(SESSION, it['id'], a) for a in it.pop('answer')]
                auto_max += it['points']
    hw['autoMax'] = auto_max
    out = os.path.join(ROOT, 'homework', 'data', f'{SESSION}.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(hw, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('json ->', out, 'auto max', auto_max)

if __name__ == '__main__':
    if '--json-only' not in sys.argv: build_audio()
    build_json()
