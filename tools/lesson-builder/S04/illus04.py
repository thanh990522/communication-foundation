"""Original flat SVG illustrations for S04 (same palette/helpers as S02–S03)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..', 'S02')); sys.path.insert(0, os.path.join(D, '..', 'S03'))
from illus import svg, clock, sun, star, tick, cup, laptop, badge, ground, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa

F = 'font-family="Be Vietnam Pro,sans-serif"'


def txt(x, y, t, s=12, c=N, w=900, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{c}" text-anchor="{anchor}" {F}>{t}</text>'


def page(x, y, w, h, day='21', mon='MAY', top=RED):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h * .28:.0f}" rx="10" fill="{top}"/><rect x="{x}" y="{y + h * .18:.0f}" width="{w}" height="{h * .1:.0f}" fill="{top}"/>'
            + txt(x + w / 2, y + h * .22, mon, min(h * .15, w * 1.3 / max(len(mon), 1)), W) + txt(x + w / 2, y + h * .78, day, min(h * .42, w * 1.45 / max(len(day), 1)), N))


def week_grid(x, y, w, h, blocks, cols=5, rows=4):
    cw, rh = w / cols, (h - 16) / rows
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{W}" stroke="{N}" stroke-width="2.5"/>'
    out += ''.join(txt(x + cw * c + cw / 2, y + 12, 'MTWTF'[c], 10, N) for c in range(cols))
    for (c, r, col) in blocks:
        out += f'<rect x="{x + cw * c + 3:.1f}" y="{y + 16 + rh * r + 2:.1f}" width="{cw - 6:.1f}" height="{rh - 4:.1f}" rx="4" fill="{col}"/>'
    return out


def phone(x, y, s=1, screen=SKY, body=N):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="0" width="56" height="100" rx="12" fill="{body}"/>'
            f'<rect x="5" y="10" width="46" height="78" rx="5" fill="{screen}"/><rect x="20" y="4" width="16" height="3" rx="1.5" fill="{GR}"/></g>')


def bubble(x, y, w, h, c=B, tail='left'):
    t = f'<path d="M{x + 14} {y + h}l-4 10l14 -10z" fill="{c}"/>' if tail == 'left' else f'<path d="M{x + w - 14} {y + h}l4 10l-14 -10z" fill="{c}"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}"/>' + t


def arrow(x1, y, x2, c=B, w=5):
    return f'<path d="M{x1} {y}H{x2}M{x2 - 9} {y - 8}L{x2} {y}L{x2 - 9} {y + 8}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def flag(x, y):
    return (f'<rect x="{x}" y="{y}" width="4" height="46" fill="{N}"/>'
            + ''.join(f'<rect x="{x + 4 + (k % 4) * 8}" y="{y + (k // 4) * 8}" width="8" height="8" fill="{N if (k + k // 4) % 2 else W}"/>' for k in range(12))
            + f'<rect x="{x + 4}" y="{y}" width="32" height="24" fill="none" stroke="{N}" stroke-width="1.5"/>')


# ------------------------------------------------------------------ word cards
WORD = {
    'schedule': svg(week_grid(30, 18, 140, 108, [(0, 0, B), (0, 2, Y), (1, 1, B2), (1, 3, RED), (2, 0, Y), (2, 1, B), (2, 3, B2),
                                                  (3, 0, RED), (3, 2, B), (4, 1, Y), (4, 2, B2), (4, 3, B)])),
    'appointment': svg(page(36, 24, 84, 96, '21', 'MAY') + clock(146, 84, 28, 3, 0) + star(170, 30, 5), YS),
    'available': svg(clock(70, 70, 40, 2, 0) + f'<rect x="118" y="44" width="70" height="52" rx="14" fill="{G}"/>' + txt(153, 78, 'FREE', 18, W)
                     + tick(130, 108, .9, G, 5)),
    'postpone': svg(page(14, 34, 62, 74, 'TUE', 'MEETING', B) + page(124, 34, 62, 74, 'FRI', 'MEETING', G) + arrow(82, 70, 118, Y2, 6)
                    + badge(72, 112, 'LATER', N, Y, 12, 58)),
    'reschedule': svg(page(20, 30, 64, 78, '2:00', 'OLD', GR) + page(116, 30, 64, 78, '4:30', 'NEW', B)
                      + f'<path d="M86 52q14 -18 28 0" fill="none" stroke="{Y2}" stroke-width="5" stroke-linecap="round"/><path d="M108 44l6 8l-9 3" fill="none" stroke="{Y2}" stroke-width="4"/>'
                      + f'<path d="M114 90q-14 18 -28 0" fill="none" stroke="{Y2}" stroke-width="5" stroke-linecap="round"/><path d="M92 98l-6 -8l9 -3" fill="none" stroke="{Y2}" stroke-width="4"/>', YS),
    'confirm': svg(phone(72, 18, 1.05) + bubble(80, 34, 42, 22, B) + txt(101, 49, 'Tue 3?', 9.5, W) + bubble(88, 64, 40, 22, G, 'right')
                   + txt(108, 79, 'Yes ✓✓', 9.5, W) + f'<circle cx="160" cy="40" r="20" fill="{G}"/>' + tick(149, 40, 1, W, 5)),
    'deadline': svg(page(26, 26, 80, 92, '5', 'FRI', RED) + f'<circle cx="66" cy="94" r="22" fill="none" stroke="{RED}" stroke-width="4"/>'
                    + flag(130, 38) + badge(118, 96, 'DUE', RED, W, 13, 52), YS),
    'time slot': svg(f'<rect x="14" y="56" width="172" height="34" rx="8" fill="{W}" stroke="{N}" stroke-width="2.5"/>'
                     + ''.join(f'<rect x="{18 + k * 34}" y="60" width="30" height="26" rx="5" fill="{G if k == 3 else SKY2}"/>' for k in range(5))
                     + ''.join(txt(33 + k * 34, 106, t, 10, N, 800) for k, t in enumerate(['9', '11', '1', '3', '5']))
                     + badge(110, 22, 'FREE', G, W, 12, 50) + f'<path d="M135 48v8" stroke="{G}" stroke-width="3"/>'),
}

# ------------------------------------------------------------------ collocation scenes
PHRASE = {
    'schedule': svg(f'<rect x="0" y="102" width="200" height="38" fill="#F2D7A6"/>' + person(56, 46, B, N, .95, False)
                    + f'<path d="M78 34q4 -6 2 -12" stroke="{B2}" stroke-width="3" fill="none"/>' + laptop(28, 82, .9)
                    + week_grid(108, 12, 84, 84, [(c, r, [B, Y, RED, B2][(c + r) % 4]) for c in range(5) for r in range(4) if (c * 3 + r) % 5]), YS),
    'appointment': svg(person(50, 50, Y, '#8B4513', .95, True, True) + phone(66, 44, .42, SKY, N)
                       + bubble(92, 14, 98, 34, B) + txt(141, 36, 'Dentist · 3 pm?', 11, W)
                       + page(118, 62, 64, 66, '14', 'JUNE', B)),
    'available': svg(person(60, 50, B, N, 1) + bubble(98, 20, 92, 34, G) + txt(144, 42, "I'm free!", 14, W)
                     + week_grid(110, 66, 80, 62, [(0, 0, RED), (1, 2, RED), (3, 1, RED)] + [(c, r, G) for c, r in [(2, 0), (2, 1), (4, 0)]], 5, 3)),
    'postpone': svg(f'<rect x="14" y="70" width="80" height="12" rx="6" fill="#A86B32"/>' + ''.join(f'<circle cx="{24 + k * 20}" cy="58" r="9" fill="{c}"/>' for k, c in enumerate([B, Y2, N, B2]))
                    + txt(54, 106, 'MON 9:00', 13, GR) + f'<line x1="18" y1="102" x2="90" y2="102" stroke="{RED}" stroke-width="3"/>'
                    + arrow(98, 72, 128, Y2, 6) + page(134, 36, 56, 70, 'FRI', 'NEW', G)),
    'reschedule': svg(f'<rect x="28" y="20" width="144" height="100" rx="12" fill="{W}" stroke="{N}" stroke-width="3"/>'
                      + f'<rect x="28" y="20" width="144" height="24" rx="12" fill="{B}"/><rect x="28" y="34" width="144" height="10" fill="{B}"/>'
                      + txt(100, 37, 'APPOINTMENT CARD', 11, W) + txt(100, 72, 'Wed 2:00', 18, GR)
                      + f'<line x1="56" y1="66" x2="144" y2="66" stroke="{RED}" stroke-width="3.5"/>' + txt(100, 104, 'Thu 4:30', 22, G), YS),
    'confirm': svg(phone(30, 18, 1.05) + bubble(38, 32, 40, 20, B) + txt(58, 46, 'Tue 3?', 9, W) + bubble(44, 60, 40, 20, G, 'right') + txt(64, 74, 'Yes ✓', 9, W)
                   + page(108, 30, 70, 82, '3:00', 'TUE', B) + f'<circle cx="170" cy="34" r="16" fill="{G}"/>' + tick(161, 34, .8, W, 4)),
    'deadline': svg(f'<rect x="0" y="102" width="200" height="38" fill="#F2D7A6"/>' + laptop(26, 56, 1.05) + tick(44, 76, 1.2, G, 5)
                    + clock(150, 48, 26, 11, 55) + flag(132, 82) + badge(12, 10, 'DONE ON TIME', G, W, 11, 98)),
    'time slot': svg(f'<rect x="20" y="14" width="160" height="112" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/>'
                     + ''.join(f'<rect x="58" y="{22 + k * 20}" width="112" height="16" rx="4" fill="{G if k == 3 else (SKY2 if k % 2 else "#FDE68A")}"/>' + txt(44, 34 + k * 20, t, 10, N, 800)
                               for k, t in enumerate(['9:00', '11:00', '1:00', '3:00', '5:00']))
                     + txt(114, 94, 'AVAILABLE', 10, W), SKY),
}

# ------------------------------------------------------------------ Mai's diary (matches content.DIARY)
def diary(entries):
    out = ['<svg viewBox="0 0 520 330" xmlns="http://www.w3.org/2000/svg" role="img"><rect width="520" height="330" rx="18" fill="#FFFDF5" stroke="#E9D9A8" stroke-width="3"/>',
           f'<rect x="0" y="0" width="520" height="54" rx="18" fill="{N}"/><rect x="0" y="36" width="520" height="18" fill="{N}"/>',
           txt(260, 36, "MAI'S WEEK", 22, Y)]
    for k, (d, t, e) in enumerate(entries):
        y = 66 + k * 52; free = e == 'free'
        out.append(f'<rect x="16" y="{y}" width="488" height="44" rx="10" fill="{G if free else W}" fill-opacity="{.15 if free else 1}" stroke="{SKY2}" stroke-width="2"/>')
        out.append(f'<rect x="16" y="{y}" width="78" height="44" rx="10" fill="{B}"/>' + txt(55, y + 28, d.upper(), 17, W))
        out.append(txt(112, y + 28, t, 17, B, 900, 'start'))
        out.append(txt(220, y + 28, e, 18, G if free else N, 800, 'start'))
        ic = {'meet her teacher': '👩‍🏫', 'dentist appointment': '🦷', 'free': '✅', 'study call with Lan': '📞', 'deadline: report': '⏰'}[e]
        out.append(emo(478, y + 22, ic, 22))
    out.append('</svg>')
    return ''.join(out)


ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    sys.path.insert(0, D); import importlib.util as u; sp = u.spec_from_file_location('c4', os.path.join(D, 'content.py')); C = u.module_from_spec(sp); sp.loader.exec_module(C)
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    h += f'<div style="grid-column:span 2">{diary(C.DIARY)}</div></body>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h)


def warm_art(front):
    if ':' in front:
        h, m = map(int, front.split(':'))
        return svg(clock(100, 70, 52, h, m), SKY)
    wd, d = front.split()
    return svg(page(60, 14, 80, 112, d, wd.upper(), RED), YS)
