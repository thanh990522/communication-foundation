"""Homework S03 — SPEAKING (shadowing a long conversation).
Only the language of lesson S03: the 8 collocations, the place words, There is/are (+ negatives, questions),
One thing I like is… · It is … because… · The only problem is… · and/but/because/so/however.
Writes homework/audio/S03/*.mp3 and homework/data/S03.json.
Run: SSL_CA_BUNDLE=/root/.ccr/ca-bundle.crt python3 build.py
"""
import asyncio, hashlib, json, os, subprocess, sys
import numpy as np
if os.environ.get('SSL_CA_BUNDLE'):
    import certifi; certifi.where = lambda: os.environ['SSL_CA_BUNDLE']
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SESSION = 'S03'
AUD = os.path.join(ROOT, 'homework', 'audio', SESSION)
CACHE = os.path.join(HERE, 'cache')
SR = 24000
VOICE = {'L': 'en-GB-LibbyNeural', 'B': 'en-GB-RyanNeural'}
RATE = '-8%'
GAP = 0.7

SPEAKERS = {'L': 'Linh', 'B': 'Ben'}
LINES = [
    ('B', 'Hi Linh! Is this your neighbourhood?'),
    ('L', "Yes, it is. Welcome! It's a peaceful neighbourhood, and it's centrally located."),
    ('B', "It's really peaceful. Do you live in an apartment or a house?"),
    ('L', 'I live in a spacious apartment near the park.'),
    ('B', "That's great. Is there a supermarket near your apartment?"),
    ('L', "Yes, there is. There's a big supermarket near the bus stop."),
    ('B', 'Are there any nearby facilities, like a gym?'),
    ('L', "Yes, there are lots of nearby facilities. There's a gym with modern facilities, and there are two cafés."),
    ('B', "So it's a convenient location."),
    ('L', "Yes, it is. It's convenient because there are two bus stops near my home."),
    ('B', 'What do you like about the area?'),
    ('L', "One thing I like is the park. It's peaceful because there are lots of trees."),
    ('B', 'And what are your neighbours like?'),
    ('L', "I have a friendly neighbour. Her name is Mai, and she's very nice."),
    ('B', 'Is there a hospital near here?'),
    ('L', "No, there isn't. However, there's a school and a market."),
    ('B', "Is there anything you don't like?"),
    ('L', "The only problem is the market. It's a crowded area at weekends."),
    ('B', "I see. My neighbourhood is very different. It's a crowded area, and there aren't any parks."),
    ('L', 'Oh no! So what do you like about it?'),
    ('B', "One thing I like is my apartment. It's small, but it's centrally located, so it's convenient."),
    ('L', 'Then come to my neighbourhood at weekends. The park is very peaceful!'),
    ('B', 'Great idea. Thanks, Linh!'),
]


def ck(v, t): return os.path.join(CACHE, hashlib.md5(f'{v}|{t}|{RATE}'.encode()).hexdigest() + '.mp3')


async def fetch():
    os.makedirs(CACHE, exist_ok=True); sem = asyncio.Semaphore(5)
    async def one(v, t):
        p = ck(v, t)
        if os.path.exists(p) and os.path.getsize(p): return
        async with sem:
            for _ in range(4):
                try:
                    await edge_tts.Communicate(t, v, rate=RATE).save(p)
                    if os.path.getsize(p): return
                except Exception as ex: print('retry', t, ex, file=sys.stderr); await asyncio.sleep(2)
            raise SystemExit('failed ' + t)
    await asyncio.gather(*[one(VOICE[w], t) for w, t in LINES])


def load(p):
    a = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32)
    idx = np.where(np.abs(a) > 0.012)[0]
    return a[max(0, idx[0] - int(.03 * SR)):min(len(a), idx[-1] + int(.08 * SR))] if len(idx) else a


def save(a, path):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-codec:a', 'libmp3lame', '-b:a', '64k', path], input=a.tobytes(), check=True)


def build():
    asyncio.run(fetch())
    os.makedirs(AUD, exist_ok=True)
    pad = np.zeros(int(.12 * SR), np.float32)
    full, t, lines = [pad], len(pad) / SR, []
    for i, (w, txt) in enumerate(LINES):
        a = load(ck(VOICE[w], txt))
        fn = f'S03_shadow_line{i + 1:02d}.mp3'
        save(np.concatenate([pad, a, pad]), os.path.join(AUD, fn))
        lines.append({'who': w, 'text': txt, 'audio': f'audio/{SESSION}/{fn}', 'dur': round(len(a) / SR + .24, 2), 'start': round(t, 2)})
        full += [a, np.zeros(int(GAP * SR), np.float32)]; t += len(a) / SR + GAP
    save(np.concatenate(full), os.path.join(AUD, 'S03_shadow_FULL.mp3'))
    hw = {'session': SESSION, 'title': 'Shadowing: Linh’s neighbourhood', 'kind': 'Speaking · Shadowing', 'pass': 80,
          'speakers': SPEAKERS, 'free': ['Mai'], 'full': f'audio/{SESSION}/S03_shadow_FULL.mp3', 'fullDur': round(t, 2), 'lines': lines}
    out = os.path.join(ROOT, 'homework', 'data', f'{SESSION}.json')
    json.dump(hw, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('json ->', out, len(lines), 'lines,', round(t), 's')


if __name__ == '__main__':
    build()
