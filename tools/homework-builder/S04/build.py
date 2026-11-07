"""Homework S04 — LISTENING (numbers, dates, times; voicemails about appointments).
Only the language of lesson S04. Writes homework/audio/S04/*.mp3 and homework/data/S04.json.
Run: SSL_CA_BUNDLE=/root/.ccr/ca-bundle.crt python3 build.py
"""
import asyncio, hashlib, json, os, shutil, subprocess, sys
import numpy as np
if os.environ.get('SSL_CA_BUNDLE'):
    import certifi; certifi.where = lambda: os.environ['SSL_CA_BUNDLE']
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SESSION = 'S04'
AUD = os.path.join(ROOT, 'homework', 'audio', SESSION)
CACHE = os.path.join(HERE, 'cache')
SR = 24000
SONIA, RYAN, LIBBY = 'en-GB-SoniaNeural', 'en-GB-RyanNeural', 'en-GB-LibbyNeural'

# ---------------------------------------------------------------- Part 1: 13 or 30?
NUMS = [  # sentence spoken, options, answer
    ('The meeting is on the 13th.', ['13th', '30th'], '13th'),
    ('My appointment is at 4:40.', ['4:14', '4:40'], '4:40'),
    ('The deadline is on the 15th.', ['15th', '50th'], '15th'),
    ('Is there an available time slot at 2:50?', ['2:15', '2:50'], '2:50'),
    ("We're meeting in room 16.", ['16', '60'], '16'),
    ('The study call is 70 minutes.', ['17', '70'], '70'),
    ('Could we move it to the 18th?', ['18th', '80th'], '18th'),
    ('There are 90 people in the class.', ['19', '90'], '90'),
]
# ---------------------------------------------------------------- Part 2: three voicemails
MSG = [
    (LIBBY, "Hello, this is Smile Dental Clinic. This message is for Ms Linh Pham. I'm calling to confirm your appointment. "
            "It's on Thursday the 14th at 3:45 in the afternoon. That's Thursday the 14th at 3:45. Please call us to reschedule. Thank you."),
    (SONIA, "Hi Nam, it's Hoa. Unfortunately, I'm meeting a client on Monday morning, so we are postponing our team meeting. "
            "Could we move it to Tuesday the 30th at half past ten instead? Does that work for you? Call me back. Thanks!"),
    (RYAN, "Hey Mai, it's Tom. I'm really sorry, but I have a deadline on Friday, so I'm working late on Thursday. "
           "I'm not available for our study call on Thursday. Are you available on Saturday morning instead? Does 9:15 work for you? Text me. Bye!"),
]
# ---------------------------------------------------------------- Part 3: phone call (gym class)
CALL = [
    (LIBBY, 'Good afternoon, City Gym. How can I help you?'),
    (RYAN, 'Hi. I need to make an appointment for a yoga class, please. Are you available on Wednesday evening?'),
    (LIBBY, "Let me check. Unfortunately, the 7 p.m. class is full. We have an available time slot at 8:15."),
    (RYAN, "8:15 doesn't work for me. I'm having dinner with my family then. Do you have a time slot on Thursday?"),
    (LIBBY, 'Yes. Thursday at 6:30 is available.'),
    (RYAN, 'Great. 6:30 works for me.'),
    (LIBBY, "So that's Thursday the 19th at 6:30?"),
    (RYAN, 'The 19th? Yes. Let me confirm: Thursday the 19th at 6:30.'),
    (LIBBY, "That's right. What's your name, please?"),
    (RYAN, "It's Ken Lee. L-E-E."),
    (LIBBY, 'Thank you, Mr Lee. See you on Thursday!'),
]

T = lambda *a: [x for x in a]
HOMEWORK = {
    'session': SESSION, 'title': 'Appointments: numbers, dates & messages', 'kind': 'Listening', 'pass': 80,
    'sections': [
        {'id': 'A', 'title': 'Part 1. 13 or 30? Listen and choose', 'items': [
            {'id': f'A{i + 1}', 'type': 'listen_mcq', 'prompt': f'Number {i + 1} · Which one do you hear?', 'audio': f'homework/audio/{SESSION}/S04_HW_num_{i + 1}.mp3',
             'options': o, 'answers': [a]} for i, (s, o, a) in enumerate(NUMS)]},
        {'id': 'B', 'title': 'Part 2. Message 1 · Smile Dental Clinic', 'audio': f'homework/audio/{SESSION}/S04_HW_message_1.mp3',
         'note': 'APPOINTMENT — Linh Pham', 'items': [
             {'id': 'B1', 'type': 'gap', 'prompt': 'Day: ____', 'answers': ['Thursday', 'Thu']},
             {'id': 'B2', 'type': 'gap', 'prompt': 'Date: the ____', 'answers': ['14th', '14', 'fourteenth', 'the14th']},
             {'id': 'B3', 'type': 'gap', 'prompt': 'Time: ____', 'answers': ['3:45', '3.45', '345', '3:45pm', '3.45pm', '3:45p.m.', 'quartertofour', '15:45']},
         ]},
        {'id': 'C', 'title': 'Part 3. Message 2 · Hoa (team meeting)', 'audio': f'homework/audio/{SESSION}/S04_HW_message_2.mp3', 'items': [
             {'id': 'C1', 'type': 'mcq', 'prompt': 'Why is Hoa postponing the meeting?', 'options': ["She's meeting a client.", "She's at the dentist.", 'She has a deadline.'], 'answers': ["She's meeting a client."]},
             {'id': 'C2', 'type': 'gap', 'prompt': 'Old day: ____ morning', 'answers': ['Monday', 'Mon']},
             {'id': 'C3', 'type': 'gap', 'prompt': 'New day: ____', 'answers': ['Tuesday', 'Tue', 'Tues']},
             {'id': 'C4', 'type': 'gap', 'prompt': 'New date: the ____', 'answers': ['30th', '30', 'thirtieth', 'the30th']},
             {'id': 'C5', 'type': 'gap', 'prompt': 'New time: ____', 'answers': ['10:30', '10.30', '1030', 'halfpastten', '10:30am', '10.30am', '10:30a.m.']},
         ]},
        {'id': 'D', 'title': 'Part 4. Message 3 · Tom (study call)', 'audio': f'homework/audio/{SESSION}/S04_HW_message_3.mp3', 'items': [
             {'id': 'D1', 'type': 'gap', 'prompt': 'Tom has a deadline on ____.', 'answers': ['Friday', 'Fri']},
             {'id': 'D2', 'type': 'gap', 'prompt': 'He is working late on ____.', 'answers': ['Thursday', 'Thu']},
             {'id': 'D3', 'type': 'mcq', 'prompt': 'New day for the study call:', 'options': ['Saturday morning', 'Saturday evening', 'Sunday morning'], 'answers': ['Saturday morning']},
             {'id': 'D4', 'type': 'gap', 'prompt': 'New time: ____', 'answers': ['9:15', '9.15', '915', 'quarterpastnine', '9:15am', '9.15am', '9:15a.m.']},
         ]},
        {'id': 'E', 'title': 'Part 5. Phone call · City Gym', 'audio': f'homework/audio/{SESSION}/S04_HW_call.mp3',
         'note': 'BOOKING — yoga class', 'items': [
             {'id': 'E1', 'type': 'mcq', 'prompt': 'Why is the 7 p.m. class no good?', 'options': ['It is full.', 'It is late.', 'It is postponed.'], 'answers': ['It is full.']},
             {'id': 'E2', 'type': 'mcq', 'prompt': "Why doesn't 8:15 work for Ken?", 'options': ["He's having dinner with his family.", "He's working late.", "He's meeting a client."], 'answers': ["He's having dinner with his family."]},
             {'id': 'E3', 'type': 'gap', 'prompt': 'Day: ____', 'answers': ['Thursday', 'Thu']},
             {'id': 'E4', 'type': 'gap', 'prompt': 'Date: the ____', 'answers': ['19th', '19', 'nineteenth', 'the19th']},
             {'id': 'E5', 'type': 'gap', 'prompt': 'Time: ____', 'answers': ['6:30', '6.30', '630', 'halfpastsix', '6:30pm', '6.30pm', '6:30p.m.', '18:30']},
             {'id': 'E6', 'type': 'gap', 'prompt': 'Surname: Ken ____', 'answers': ['Lee']},
         ]},
    ],
}


def ck(v, t, r): return os.path.join(CACHE, hashlib.md5(f'{v}|{t}|{r}'.encode()).hexdigest() + '.mp3')


NEED = set()
for s, o, a in NUMS: NEED.add((RYAN, s, '-6%'))
for v, t in MSG: NEED.add((v, t, '-6%'))
for v, t in CALL: NEED.add((v, t, '-6%'))


async def fetch():
    os.makedirs(CACHE, exist_ok=True); sem = asyncio.Semaphore(5)
    async def one(v, t, r):
        p = ck(v, t, r)
        if os.path.exists(p) and os.path.getsize(p): return
        async with sem:
            for _ in range(4):
                try:
                    await edge_tts.Communicate(t, v, rate=r).save(p)
                    if os.path.getsize(p): return
                except Exception as ex: print('retry', t[:40], ex, file=sys.stderr); await asyncio.sleep(2)
            raise SystemExit('failed ' + t)
    await asyncio.gather(*[one(*n) for n in NEED])


def load(p):
    a = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32)
    idx = np.where(np.abs(a) > 0.012)[0]
    return a[max(0, idx[0] - int(.03 * SR)):min(len(a), idx[-1] + int(.08 * SR))] if len(idx) else a


def sil(s): return np.zeros(int(s * SR), np.float32)


def save(a, name):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-codec:a', 'libmp3lame', '-b:a', '64k', os.path.join(AUD, name)],
                   input=np.concatenate([sil(.15), a, sil(.3)]).tobytes(), check=True)


def build():
    asyncio.run(fetch())
    if os.path.isdir(AUD): shutil.rmtree(AUD)
    os.makedirs(AUD)
    for i, (s, o, a) in enumerate(NUMS):
        x = load(ck(RYAN, s, '-6%')); save(np.concatenate([x, sil(1.2), x]), f'S04_HW_num_{i + 1}.mp3')   # said twice
    beep = (0.25 * np.sin(2 * np.pi * 880 * np.arange(int(.18 * SR)) / SR)).astype(np.float32)
    for i, (v, t) in enumerate(MSG):
        save(np.concatenate([beep, sil(.6), load(ck(v, t, '-6%'))]), f'S04_HW_message_{i + 1}.mp3')
    parts = []
    for v, t in CALL: parts += [load(ck(v, t, '-6%')), sil(.55)]
    save(np.concatenate(parts), 'S04_HW_call.mp3')
    hw = json.loads(json.dumps(HOMEWORK)); mx = 0
    for sec in hw['sections']:
        for it in sec['items']:
            it.setdefault('points', 1); it['show'] = it['answers'][0]; mx += it['points']
    hw['autoMax'] = mx
    out = os.path.join(ROOT, 'homework', 'data', f'{SESSION}.json')
    json.dump(hw, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('json ->', out, 'items', mx)


if __name__ == '__main__':
    build()
