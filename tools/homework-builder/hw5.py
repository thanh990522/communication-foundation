"""5-part homework builder (vocabulary · reading · listening · shadowing · translation).

Usage:  SSL_CA_BUNDLE=/root/.ccr/ca-bundle.crt python3 hw5.py S01 [S02 ...]
Reads   tools/homework-builder/<S>/hw5_content.py
Writes  homework/data/<S>.json and homework/audio/<S>/<S>_H5_*.mp3 (TTS, cached in ./cache5)

Content module fields
  TITLE, VOCAB[items], READING{title,passage,items}, LISTEN[ {title, audio | lines[(voice,speaker,text)], script, note, items} ],
  SHADOW{title, sentences[str], voice, free[str]}, TRANS[(vi, [answers], hint)]
Items use the engine types: mcq · gap · listen_mcq · translate · shadow.
"""
import asyncio, hashlib, importlib.util, json, os, subprocess, sys
import numpy as np
if os.environ.get('SSL_CA_BUNDLE'):
    import certifi; certifi.where = lambda: os.environ['SSL_CA_BUNDLE']
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
CACHE = os.path.join(HERE, 'cache5')
SR = 24000
RATE = '-8%'
sys.path.insert(0, os.path.join(ROOT, 'tools', 'lesson-builder'))
from mcshuffle import shuffle_items  # noqa: E402

SONIA, RYAN, LIBBY = 'en-GB-SoniaNeural', 'en-GB-RyanNeural', 'en-GB-LibbyNeural'


def ck(v, t): return os.path.join(CACHE, hashlib.md5(f'{v}|{t}|{RATE}'.encode()).hexdigest() + '.mp3')


async def fetch(need):
    os.makedirs(CACHE, exist_ok=True); sem = asyncio.Semaphore(5)
    async def one(v, t):
        p = ck(v, t)
        if os.path.exists(p) and os.path.getsize(p): return
        async with sem:
            for _ in range(5):
                try:
                    await edge_tts.Communicate(t, v, rate=RATE).save(p)
                    if os.path.getsize(p): return
                except Exception as ex: print('retry', t[:40], ex, file=sys.stderr); await asyncio.sleep(2)
            raise SystemExit('TTS failed: ' + t)
    await asyncio.gather(*[one(v, t) for v, t in need])


def load(p):
    a = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32)
    idx = np.where(np.abs(a) > 0.012)[0]
    return a[max(0, idx[0] - int(.03 * SR)):min(len(a), idx[-1] + int(.08 * SR))] if len(idx) else a


def sil(s): return np.zeros(int(s * SR), np.float32)


def save(a, path):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-codec:a', 'libmp3lame', '-b:a', '64k', path],
                   input=np.concatenate([sil(.12), a, sil(.25)]).tobytes(), check=True)


def module(sid):
    sp = importlib.util.spec_from_file_location(f'hw5_{sid}', os.path.join(HERE, sid, 'hw5_content.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


def build(sid):
    C = module(sid)
    aud_dir = os.path.join(ROOT, 'homework', 'audio', sid); os.makedirs(aud_dir, exist_ok=True)
    for f in os.listdir(aud_dir):
        if f.startswith(f'{sid}_H5_'): os.remove(os.path.join(aud_dir, f))
    rel = lambda f: f'homework/audio/{sid}/{f}'
    sh = C.SHADOW; sv = sh.get('voice', SONIA)
    need = {(sv, s) for s in sh['sentences']}
    for L in C.LISTEN:
        for v, _, t in L.get('lines', []): need.add((v, t))
    asyncio.run(fetch(need))

    sections = []
    sections.append({'id': 'V', 'title': 'Part 1 · Vocabulary test', 'sub': 'Chọn hoặc điền từ / cụm từ đã học.', 'items': C.VOCAB})
    R = C.READING
    sections.append({'id': 'R', 'title': 'Part 2 · Reading — ' + R['title'], 'sub': 'Đọc đoạn văn rồi trả lời câu hỏi.', 'passage': R['passage'], 'items': R['items']})
    for k, L in enumerate(C.LISTEN):
        sec = {'id': f'L{k + 1}', 'title': 'Part 3 · Listening — ' + L['title'], 'sub': L.get('sub', 'Nghe và trả lời. Script hiện ra sau khi nộp bài.'), 'items': L['items'],
               'audioLabel': L.get('label', 'Listen to the recording'), 'audioHint': L.get('hint', 'Nghe 2 lần rồi trả lời.')}
        if L.get('lines'):
            parts = []
            for v, _, t in L['lines']: parts += [load(ck(v, t)), sil(.55)]
            f = f'{sid}_H5_listen{k + 1}.mp3'; save(np.concatenate(parts), os.path.join(aud_dir, f)); sec['audio'] = rel(f)
            sec['script'] = [[spk, t] for _, spk, t in L['lines']]
        else:
            assert os.path.exists(os.path.join(ROOT, L['audio'])), L['audio']
            sec['audio'] = L['audio']; sec['script'] = L['script']
        if L.get('note'): sec['note'] = L['note']
        sections.append(sec)
    # shadowing paragraph: one file per sentence + the full paragraph
    sents, full, dur = [], [], 0.0
    for i, s in enumerate(sh['sentences']):
        a = load(ck(sv, s)); f = f'{sid}_H5_shadow_{i + 1:02d}.mp3'; save(a, os.path.join(aud_dir, f))
        sents.append({'text': s, 'audio': rel(f)}); full += [a, sil(.45)]; dur += len(a) / SR + .45
    save(np.concatenate(full), os.path.join(aud_dir, f'{sid}_H5_shadow_full.mp3'))
    sections.append({'id': 'S', 'title': 'Part 4 · Speaking — Shadowing', 'sub': 'Nghe mẫu → đọc theo → ghi âm. Máy chấm điểm trên thang 10 và tô màu từng từ.',
                     'items': [{'id': 'S1', 'type': 'shadow', 'points': 10, 'prompt': sh['title'], 'audio': rel(f'{sid}_H5_shadow_full.mp3'),
                                'sentences': sents, 'dur': round(dur, 1), 'free': sh.get('free', [])}]})
    sections.append({'id': 'T', 'title': 'Part 5 · Translation (Việt → Anh)', 'sub': 'Viết lại câu bằng cấu trúc đã học. Đúng hoàn toàn: 2 điểm · sai 1 từ: 1 điểm.',
                     'items': [{'id': f'T{i + 1}', 'type': 'translate', 'points': 2, 'prompt': vi, 'answers': ans, 'show': ans[0], 'hint': hint}
                               for i, (vi, ans, hint) in enumerate(C.TRANS)]})
    # ids, points, shuffled options
    mx = 0
    for sec in sections:
        for i, it in enumerate(sec['items']):
            it.setdefault('id', f"{sec['id']}{i + 1}"); it.setdefault('points', 1)
            if it['type'] in ('mcq', 'listen_mcq', 'gap'): it.setdefault('show', it['answers'][0])
            mx += it['points']
        shuffle_items(sec['items'], f"{sid}-H5-{sec['id']}")
    hw = {'session': sid, 'title': C.TITLE, 'kind': '5-part', 'pass': 80, 'autoMax': mx, 'sections': sections}
    out = os.path.join(ROOT, 'homework', 'data', f'{sid}.json')
    json.dump(hw, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(sid, '->', out, '| points', mx, '| shadow', round(dur), 's')


# ---------------------------------------------------------------- tiny helpers for content files
TF = ['True', 'False']
def mcq(prompt, options, answer, **kw): return dict(type='mcq', prompt=prompt, options=list(options), answers=[answer], **kw)
def gap(prompt, *answers, **kw): return dict(type='gap', prompt=prompt, answers=list(answers), **kw)


if __name__ == '__main__':
    for s in sys.argv[1:] or ['S01', 'S02', 'S03', 'S04']: build(s.upper())
