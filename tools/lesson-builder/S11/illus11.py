"""Original flat SVG illustrations for S11 (same palette/helpers as S02–S10)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
for _p in ('S02', 'S03', 'S06', 'S07', 'S08', 'S09', 'S10'): sys.path.insert(0, os.path.join(D, '..', _p))
from illus import svg, star, tick, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa
from illus06 import txt  # noqa
from illus07 import bubble  # noqa
from illus09 import truck  # noqa


def bus(x, y, s=1):
    return (f'<rect x="{x}" y="{y}" width="{90 * s}" height="{44 * s}" rx="8" fill="{Y}" stroke="{N}" stroke-width="2.5"/>'
            + ''.join(f'<rect x="{x + (8 + k * 20) * s}" y="{y + 8 * s}" width="{14 * s}" height="{12 * s}" rx="2" fill="{SKY2}"/>' for k in range(4))
            + f'<circle cx="{x + 18 * s}" cy="{y + 44 * s}" r="{7 * s}" fill="{N}"/><circle cx="{x + 72 * s}" cy="{y + 44 * s}" r="{7 * s}" fill="{N}"/>')


def bulb(x, y, s=1):
    return f'<circle cx="{x}" cy="{y}" r="{14 * s}" fill="{Y}" stroke="{N}" stroke-width="2.5"/><rect x="{x - 6 * s}" y="{y + 12 * s}" width="{12 * s}" height="{8 * s}" fill="{GR}"/>'


WORD = {
    'happen': svg(emo(100, 64, '❓', 60) + emo(46, 100, '😮', 32) + emo(156, 100, '😮', 32) + star(40, 30, 6), YS),
    'suddenly': svg(emo(100, 70, '⚡', 66) + badge(56, 110, 'suddenly!', RED, W, 13, 90)),
    'fortunately': svg(emo(100, 66, '🍀', 64) + emo(150, 104, '😊', 30) + star(46, 34, 6) + star(160, 30, 5), YS),
    'miss': svg(bus(90, 52, 1) + f'<path d="M80 74h-30M80 86h-20" stroke="{GR}" stroke-width="3" stroke-linecap="round"/>' + emo(36, 92, '🏃', 34)),
    'realise': svg(person(80, 58, B, N, 1) + bulb(128, 30, 1) + f'<path d="M116 14l-6 -6M140 14l6 -6M128 8v-6" stroke="{Y2}" stroke-width="3"/>', YS),
    'decide': svg(person(100, 60, G, N, 1) + f'<path d="M70 30l-26 -12M130 30l26 -12" stroke="{N}" stroke-width="3" stroke-dasharray="4 4"/>' + emo(36, 20, '⏳', 22) + emo(166, 20, '🚶', 22)),
    'eventually': svg(f'<path d="M20 110q60 -80 160 -60" stroke="{B}" stroke-width="4" fill="none" stroke-dasharray="6 6"/>' + emo(176, 46, '🏁', 34) + emo(30, 104, '🐢', 28), YS),
    'while': svg(emo(64, 70, '🧍', 54) + emo(140, 50, '☔', 46) + badge(48, 110, 'at the same time', N, Y, 11, 110)),
}

PHRASE = {
    'happen': svg(person(56, 54, Y, '#8B4513', .85, True, True) + bubble(88, 10, 106, 44, B) + txt(141, 28, "You'll never guess", 9.5, W) + txt(141, 43, 'what happened!', 10, W) + emo(150, 104, '😲', 30), YS),
    'suddenly': svg(person(60, 56, B, N, .85) + bulb(106, 30, .8) + bubble(124, 14, 70, 30, RED) + txt(159, 34, 'Oh no!', 12, W) + emo(150, 100, '👛', 30)),
    'fortunately': svg(person(60, 56, G, N, .85) + emo(120, 96, '👜', 34) + emo(156, 74, '📱', 26) + bubble(96, 12, 98, 34, G) + txt(145, 34, 'Found it!', 12, W), YS),
    'miss': svg(bus(100, 50, .9) + emo(48, 86, '🏃', 34) + bubble(14, 14, 86, 30, RED) + txt(57, 34, 'Wait!!', 12, W)),
    'realise': svg(emo(60, 76, '🚆', 50) + emo(130, 70, '😱', 40) + badge(84, 14, 'wrong train!', RED, W, 11, 84), YS),
    'decide': svg(person(60, 56, B, N, .85) + bubble(92, 12, 102, 40, B) + txt(143, 29, "I'll wait", 11, W) + txt(143, 44, 'for the next one.', 9.5, W) + emo(150, 104, '⏳', 28)),
    'eventually': svg(bus(70, 60, .9) + emo(40, 50, '⏰', 26) + badge(56, 114, 'after 1 hour…', N, Y, 11, 90), YS),
    'while': svg(person(58, 58, Y, N, .85) + emo(58, 104, '🧳', 26) + emo(140, 70, '✈️', 44) + badge(100, 14, 'while travelling', B, W, 10, 94)),
}

AIRPORT_ART = svg(f'<rect x="20" y="90" width="160" height="12" rx="6" fill="{GR}"/>' + emo(60, 76, '🧳', 34) + emo(140, 50, '✈️', 44) + badge(26, 14, 'LOST PROPERTY', N, Y, 11, 110), YS)

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE, {'airport': AIRPORT_ART}):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h + '</body>')
