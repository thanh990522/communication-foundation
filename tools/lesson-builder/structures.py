"""Structure slides (from S03 on): one main, substitutable structure per slide, revealed step by step.
Steps: structure + Vietnamese meaning → model question → each common answer → each VI prompt → its EN answer.
Navigation: →/Space/presenter = next step (then next slide), ← = step back. English items play when revealed."""
import html, os

e = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
JS = open(os.path.join(HERE, 'structures.js'), encoding='utf-8').read()
CSS = open(os.path.join(HERE, 'structures.css'), encoding='utf-8').read()


def blanks(t):
    return e(t).replace('___', '<span class="gap">___</span>')


def struct_slide(slide, head, P, i, n, st):
    """st: dict(name, q, a, vi_q, vi_a, model, answers=[(en, vi)], tr=[(vi, en)]) — audio ids STR_{i}_m, STR_{i}_a{j}, STR_{i}_t{j}"""
    k = 0
    def step(html_, aid=None):
        nonlocal k; k += 1
        return f'<div class="stp" data-step="{k}"{f" data-say={chr(34)}{aid}{chr(34)}" if aid else ""}>{html_}</div>'
    play = lambda aid: f'<button class="play sm" data-a="{aid}">{P}</button>'
    left = step(f'<div class="sfm"><div class="sfvi">🇻🇳 {e(st["vi_q"])}</div>'
                + (f'<div class="sfa">→ {blanks(st["a"])}</div><div class="sfvi">🇻🇳 {e(st["vi_a"])}</div>' if st.get('a') else '') + '</div>')
    left += step(f'<div class="smod"><span class="who q">Q</span><b>{e(st["model"])}</b>{play(f"STR_{i}_m")}</div>', f'STR_{i}_m')
    left += '<div class="sans-h stp" data-step="0">💬 Common answers</div>'
    for j, (en, vi) in enumerate(st['answers']):
        left += step(f'<div class="sans"><span class="who a">{"abc"[j]}</span><div><b>{e(en)}</b><small>{e(vi)}</small></div>{play(f"STR_{i}_a{j}")}</div>', f'STR_{i}_a{j}')
    right = ''
    for j, (vi, en) in enumerate(st['tr']):
        right += (f'<div class="str">' + step(f'<div class="strvi"><span class="n">{j + 1}</span>🇻🇳 {e(vi)}</div>')
                  + step(f'<div class="stren">🇬🇧 {e(en)} {play(f"STR_{i}_t{j}")}</div>', f'STR_{i}_t{j}') + '</div>')
    body = (f'  <div class="sgrid" data-steps="{k}"><div class="col sleft">{left}</div>'
            f'<div class="card sright"><div class="srh">⚡ Translate now · Dịch ngay</div>{right}</div></div>\n'
            f'  <div class="snav"><span class="sdots"></span><button class="btn sm ghost" data-sprev>←</button><button class="btn sm y" data-snext>Next step →</button><span class="shint">→ / Space / presenter</span></div>\n')
    return slide(f'Structure {i + 1}: {st["name"]}', head(f'Structure {i + 1} / {n}', 'c-input', blanks(st['q']).replace('<span class="gap">___</span>', '<em>___</em>')) + body)


def audio_clips(STRUCTS, sid, want, clip, Q, A):
    """register audio for gen_audio.py — Q voice for questions, A voice for answers"""
    for i, st in enumerate(STRUCTS):
        clip(f'STR_{i}_m', f'Structures/{sid}_structure{i + 1}_model.mp3', [want(Q, st['model'], '-5%')], st['model'])
        for j, (en, vi) in enumerate(st['answers']):
            clip(f'STR_{i}_a{j}', f'Structures/{sid}_structure{i + 1}_answer_{"abc"[j]}.mp3', [want(A, en, '-5%')], en)
        for j, (vi, en) in enumerate(st['tr']):
            clip(f'STR_{i}_t{j}', f'Structures/{sid}_structure{i + 1}_translate_{j + 1}.mp3', [want(A if not en.endswith('?') else Q, en, '-5%')], en)
