"""Build Homework S01 — LISTENING (spelling test, IELTS Listening "spelling" format).

Format adapted from the spelling-test series the teacher shared (people's names, street names,
town/city names, Section-1 form completion): each item is said once and spelled once at natural
speed — "Number one. Church Road. C-H-U-R-C-H." All names, streets, towns and the phone call are
ORIGINAL content recorded with Microsoft neural voices (edge-tts); no third-party audio is reused.

Writes  homework/data/S01.json   (answers stored only as SHA-256 hashes)
        homework/audio/S01/*.mp3
Run:    SSL_CA_BUNDLE=... python3 build.py      (needs ffmpeg, numpy, edge-tts)
"""
import asyncio, hashlib, json, os, re, shutil, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SESSION = 'S01'
AUDIO_DIR = os.path.join(ROOT, 'homework', 'audio', SESSION)
CACHE = os.path.join(HERE, 'cache')
NARR = 'en-GB-RyanNeural'      # test narrator
RECEP = 'en-GB-RyanNeural'     # hotel receptionist
CALLER = 'en-GB-LibbyNeural'   # caller
SR = 24000
NUMW = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
TITLE_SAY = {'Mr': 'Mister', 'Mrs': 'Missus', 'Ms': 'Ms', 'Dr': 'Doctor', 'Miss': 'Miss'}

# ------------------------------------------------------------------ content
PEOPLE = [('Ms', 'Carter'), ('Mr', 'Fletcher'), ('Mrs', 'Graham'), ('Dr', 'Shaw'),
          ('Miss', 'Kelly'), ('Mr', 'Vaughan'), ('Ms', 'Young'), ('Mrs', 'Jenkins')]
STREETS = [('Church', 'Road'), ('Garden', 'Street'), ('Kingsley', 'Avenue'),
           ('Wellington', 'Road'), ('Juniper', 'Drive'), ('Hazel', 'Lane')]
TOWNS = ['Cambridge', 'Leeds', 'Perth', 'Phoenix', 'Glasgow']
CALL = [  # (speaker, segments)  segments: str = say, ('s', text) = spell
    ('R', ['Good afternoon, Lakeside Hotel. How can I help you?']),
    ('C', ["Hi. I'd like to book a room for three nights, please."]),
    ('R', ['Certainly. Can I have your name, please?']),
    ('C', ["Yes. It's Emma Thornton."]),
    ('R', ['How do you spell your surname?']),
    ('C', ['T-H-O-R-N-T-O-N.']),
    ('R', ['Thank you. And which town are you from?']),
    ('C', ["I'm from Norwich. That's", ('s', 'NORWICH')]),
    ('R', ["Lovely. What's your address, please?"]),
    ('C', ["It's fourteen Belmont Road.", ('s', 'BELMONT')]),
    ('R', ['Sorry, could you spell that again, please?']),
    ('C', ['Sure.', ('s', 'BELMONT')]),
    ('R', ['Thanks. And your email address?']),
    ('C', ["It's", ('s', 'emma.t88@gmail.com')]),
    ('R', ['Is that all lower case?']),
    ('C', ["Yes, it's all lower case."]),
    ('R', ['Perfect. And what day will you arrive?']),
    ('C', ['On Friday, in the afternoon.']),
    ('R', ["Great. That's three nights from Friday. See you then, Ms Thornton!"]),
]
# the surname line is spelled letter by letter, not read as a sentence
CALL[5] = ('C', [('s', 'THORNTON')])

def people_items():
    return [{'id': f'P{i+1}', 'type': 'listen_type', 'prompt': f'Question {i+1} · {t} ______',
             'audio': f'homework/audio/{SESSION}/{SESSION}_HW_P{i+1}.mp3', 'placeholder': 'SURNAME',
             'answer': [n, f'{t} {n}', f'{t}. {n}']} for i, (t, n) in enumerate(PEOPLE)]

def street_items():
    return [{'id': f'R{i+1}', 'type': 'listen_type', 'prompt': f'Number {i+1} · ______ {kind}',
             'audio': f'homework/audio/{SESSION}/{SESSION}_HW_R{i+1}.mp3', 'placeholder': 'STREET NAME',
             'answer': [n, f'{n} {kind}']} for i, (n, kind) in enumerate(STREETS)]

def town_items():
    return [{'id': f'T{i+1}', 'type': 'listen_type', 'prompt': f'Number {i+1} · town / city',
             'audio': f'homework/audio/{SESSION}/{SESSION}_HW_T{i+1}.mp3', 'placeholder': 'TOWN',
             'answer': [n]} for i, n in enumerate(TOWNS)]

HOMEWORK = {
    'session': SESSION,
    'title': 'Alphabet & Spelling Out Loud',
    'kind': 'Listening',
    'intro': 'Listening homework · dạng Spelling của IELTS Listening. Mỗi câu chỉ đọc và đánh vần 1 lần ở tốc độ tự nhiên — '
             'hãy nghe 1 lần trước như thi thật, rồi mới nghe lại để kiểm tra. Viết đúng như được đánh vần: sai 1 chữ là sai cả câu. '
             'Khoảng 20 phút · tự chấm ngay khi nộp.',
    'sections': [
        {'id': 'A', 'title': "Part 1. People's names", 'vi': 'Nghe "Mr / Mrs / Ms…" rồi viết họ (surname)', 'items': people_items()},
        {'id': 'B', 'title': 'Part 2. Street names', 'vi': 'Viết tên đường được đánh vần (không cần viết Road / Street)', 'items': street_items()},
        {'id': 'C', 'title': 'Part 3. Towns & cities', 'vi': 'Viết tên thành phố được đánh vần', 'items': town_items()},
        {'id': 'D', 'title': 'Part 4. Booking form', 'vi': 'Nghe cuộc gọi đặt phòng khách sạn và điền form (dạng IELTS Listening Section 1)',
         'audio': f'homework/audio/{SESSION}/{SESSION}_HW_call.mp3',
         'note': 'LAKESIDE HOTEL — Booking form · Number of nights: 3 (example)',
         'items': [
             {'id': 'D1', 'type': 'gap', 'prompt': 'Guest name: Emma ____', 'answer': ['Thornton']},
             {'id': 'D2', 'type': 'gap', 'prompt': 'Home town: ____', 'answer': ['Norwich']},
             {'id': 'D3', 'type': 'gap', 'prompt': 'Address: 14 ____ Road', 'answer': ['Belmont', 'Belmont Road']},
             {'id': 'D4', 'type': 'gap', 'prompt': 'Email: ____', 'answer': ['emma.t88@gmail.com']},
             {'id': 'D5', 'type': 'gap', 'prompt': 'Arrival day: ____', 'answer': ['Friday', 'Fri']},
         ]},
    ],
}

# ------------------------------------------------------------------ hashing (must match homework page + Code.gs)
def norm(s): return re.sub(r'[\s\-–—]+', '', str(s).lower())
def h(session, qid, ans): return hashlib.sha256(f'{session}|{qid}|{norm(ans)}'.encode('utf-8')).hexdigest()

# ------------------------------------------------------------------ audio
DIG = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def tokens(s):
    out = []; at = s.find('@'); loc = s if at < 0 else s[:at]; dom = '' if at < 0 else s[at + 1:]; i = 0
    while i < len(loc):
        c = loc[i]
        if c.isalpha():
            U = c.upper()
            if i + 1 < len(loc) and loc[i + 1].upper() == U: out.append('double ' + U); i += 2; continue
            out.append(U)
        elif c.isdigit(): out.append(DIG[int(c)])
        elif c == '.': out.append('dot')
        elif c == '_': out.append('underscore')
        elif c == '-': out.append('hyphen')
        i += 1
    if at >= 0:
        out.append('at')
        for k, p in enumerate(dom.split('.')):
            if k: out.append('dot')
            if p in ('com', 'net', 'org') or len(p) > 3: out.append(p)
            else: out.extend(ch.upper() for ch in p)
    return out

def ck(v, t): return os.path.join(CACHE, hashlib.md5(f'{v}|{t}'.encode()).hexdigest() + '.mp3')
NEED = set()
def want(v, t): NEED.add((v, t)); return (v, t)

async def fetch():
    import certifi
    if os.environ.get('SSL_CA_BUNDLE'): certifi.where = lambda: os.environ['SSL_CA_BUNDLE']
    import edge_tts
    os.makedirs(CACHE, exist_ok=True)
    sem = asyncio.Semaphore(6)
    async def one(v, t):
        p = ck(v, t)
        if os.path.exists(p) and os.path.getsize(p) > 0: return
        async with sem:
            for _ in range(4):
                try:
                    await edge_tts.Communicate(t, v).save(p)
                    if os.path.getsize(p) > 0: return
                except Exception as e:
                    print('retry', t, e, file=sys.stderr); await asyncio.sleep(2)
            raise SystemExit('TTS failed: ' + t)
    await asyncio.gather(*[one(v, t) for v, t in NEED])

def load(key):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', ck(*key), '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); idx = np.where(np.abs(a) > 0.012)[0]
    return a if not len(idx) else a[max(0, idx[0] - int(.03 * SR)): idx[-1] + int(.06 * SR)]
def sil(s): return np.zeros(int(s * SR), np.float32)

def spell_plan(v, text, gap=.22):
    k = []
    for t in tokens(text): k += [want(v, t), gap]
    return k

def say_plan(v, segs):
    k = []
    for sg in segs:
        if isinstance(sg, str): k += [want(v, sg), .3]
        else: k += spell_plan(v, sg[1]) + [.15]
    return k

PLANS = {}
for i, (t, n) in enumerate(PEOPLE):
    PLANS[f'{SESSION}_HW_P{i+1}'] = [want(NARR, f'Question {NUMW[i]}.'), .7, want(NARR, f'{TITLE_SAY[t]} {n}.'), .45] + spell_plan(NARR, n.upper())
for i, (n, kind) in enumerate(STREETS):
    PLANS[f'{SESSION}_HW_R{i+1}'] = [want(NARR, f'Number {NUMW[i]}.'), .7, want(NARR, f'{n} {kind}.'), .45] + spell_plan(NARR, n.upper())
for i, n in enumerate(TOWNS):
    PLANS[f'{SESSION}_HW_T{i+1}'] = [want(NARR, f'Number {NUMW[i]}.'), .7, want(NARR, f'{n}.'), .45] + spell_plan(NARR, n.upper())
call = [want(NARR, 'Part four. You will hear a woman calling a hotel to book a room. Listen and complete the booking form.'), 1.2]
for who, segs in CALL:
    call += say_plan(RECEP if who == 'R' else CALLER, segs) + [.55]
PLANS[f'{SESSION}_HW_call'] = call

def render(plan):
    parts = [sil(.15)]
    for p in plan: parts.append(sil(p) if isinstance(p, (int, float)) else load(p))
    parts.append(sil(.35))
    return np.concatenate(parts)

def build_audio():
    asyncio.run(fetch())
    if os.path.isdir(AUDIO_DIR): shutil.rmtree(AUDIO_DIR)
    os.makedirs(AUDIO_DIR)
    for name, plan in PLANS.items():
        a = render(plan)
        out = os.path.join(AUDIO_DIR, name + '.mp3')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-codec:a', 'libmp3lame', '-b:a', '64k', out],
                       input=a.tobytes(), check=True)
    print('audio ->', AUDIO_DIR, len(PLANS), 'files')

def build_json():
    hw = json.loads(json.dumps(HOMEWORK))
    hw.pop('intro', None)
    for sec in hw['sections']: sec.pop('vi', None)
    hw['pass'] = 80
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
