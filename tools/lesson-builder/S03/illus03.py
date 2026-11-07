"""Original flat SVG illustrations for S03 (same palette/helpers as S02)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'S02'))
from illus import (svg, sun, star, tick, cup, bus, house, office, badge, ground, laptop,  # noqa: E402
                   N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART)

F = 'font-family="Be Vietnam Pro,sans-serif"'
GREEN, GREEN2, RED = '#22C55E', '#15803D', '#EF4444'


def emo(x, y, e, s=20):
    return f'<text x="{x}" y="{y}" font-size="{s}" text-anchor="middle" dominant-baseline="central">{e}</text>'


def tree(x, y, s=1, c=GREEN):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-3" y="0" width="6" height="18" rx="2" fill="#8B5A2B"/>'
            f'<circle cx="0" cy="-6" r="14" fill="{c}"/><circle cx="-8" cy="2" r="9" fill="{c}"/><circle cx="8" cy="2" r="9" fill="{c}"/></g>')


def person(cx, cy, body=B, hair=N, s=1, smile=True, long_hair=False):
    hr = (f'<path d="M-15 -4q2 -22 15 -20q13 -2 15 20q-2 -10 -15 -10q-13 0 -15 10z" fill="{hair}"/>' if not long_hair else
          f'<path d="M-16 10q-3 -32 16 -32q19 0 16 32l-5 -2q2 -18 -11 -18q-13 0 -11 18z" fill="{hair}"/>')
    sm = '<path d="M-5 5q5 5 10 0" fill="none" stroke="#7A3E1D" stroke-width="2" stroke-linecap="round"/>' if smile else ''
    return (f'<g transform="translate({cx} {cy}) scale({s})"><path d="M-28 52q0 -30 28 -30q28 0 28 30z" fill="{body}"/>'
            f'<circle cx="0" cy="0" r="15" fill="{SK}"/>{hr}<circle cx="-5" cy="-1" r="1.8" fill="{N}"/><circle cx="5" cy="-1" r="1.8" fill="{N}"/>{sm}</g>')


def head(cx, cy, c, r=9):
    return f'<path d="M{cx - r * 1.5} {cy + r * 2.6}q0 -{r * 1.6} {r * 1.5} -{r * 1.6}q{r * 1.5} 0 {r * 1.5} {r * 1.6}z" fill="{c}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{SK}"/>'


def pin(x, y, c=RED, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0q-14 -18 -14 -28a14 14 0 0 1 28 0q0 10 -14 28z" fill="{c}"/>'
            f'<circle cx="0" cy="-28" r="5.5" fill="{W}"/></g>')


def busstop(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-2" y="-40" width="4" height="40" fill="{N}"/>'
            f'<rect x="-13" y="-56" width="26" height="20" rx="5" fill="{B}"/><text x="0" y="-41" font-size="10" font-weight="900" fill="{W}" text-anchor="middle" {F}>BUS</text></g>')


def dumbbell(x, y, s=1, c=N):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-16" y="-2.5" width="32" height="5" rx="2" fill="{GR}"/>'
            f'<rect x="-22" y="-9" width="7" height="18" rx="2" fill="{c}"/><rect x="15" y="-9" width="7" height="18" rx="2" fill="{c}"/></g>')


def sofa(x, y, s=1, c=B):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="10" width="70" height="22" rx="6" fill="{c}"/>'
            f'<rect x="4" y="0" width="62" height="18" rx="6" fill="{B2}"/><rect x="-6" y="8" width="12" height="26" rx="5" fill="{N}"/>'
            f'<rect x="64" y="8" width="12" height="26" rx="5" fill="{N}"/><rect x="4" y="32" width="5" height="6" fill="{N}"/><rect x="61" y="32" width="5" height="6" fill="{N}"/></g>')


def plant(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0q-12 -14 -4 -28M0 0q12 -12 6 -26M0 0q0 -18 0 -30" fill="none" stroke="{GREEN2}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M-9 0h18l-3 14h-12z" fill="{Y2}"/></g>')


def arrow2(x1, y1, x2, y2, c=B):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<circle cx="{x1}" cy="{y1}" r="4" fill="{c}"/><circle cx="{x2}" cy="{y2}" r="4" fill="{c}"/>')


def bird(x, y):
    return f'<path d="M{x - 8} {y}q4 -5 8 0q4 -5 8 0" fill="none" stroke="{N}" stroke-width="2.5" stroke-linecap="round"/>'


def awning_shop(x, y, w=52, c=RED, sign=''):
    stripes = ''.join(f'<rect x="{x + k * w / 6:.1f}" y="{y}" width="{w / 12:.1f}" height="12" fill="{W}"/>' for k in range(6))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="46" fill="{W}" stroke="{N}" stroke-width="2.5"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="12" fill="{c}"/>{stripes}'
            f'<rect x="{x + 8}" y="{y + 20}" width="{w - 16}" height="22" rx="2" fill="{SKY2}"/>' + (emo(x + w / 2, y + 31, sign, 14) if sign else ''))


# ------------------------------------------------------------------ word cards
WORD = {
    'spacious': svg(f'<rect x="20" y="16" width="160" height="108" rx="6" fill="{W}" stroke="{N}" stroke-width="3"/>'
                    f'<rect x="20" y="96" width="160" height="28" fill="{YS}"/>'
                    f'<path d="M40 70h120M40 70l10 -7M40 70l10 7M160 70l-10 -7M160 70l-10 7" fill="none" stroke="{B}" stroke-width="4" stroke-linecap="round"/>'
                    f'<path d="M100 26v36M100 26l-7 10M100 26l7 10" fill="none" stroke="{B2}" stroke-width="4" stroke-linecap="round"/>'
                    + plant(160, 110, .7) + sofa(32, 92, .45)),
    'crowded': svg(''.join(head(22 + c * 26 + (r % 2) * 12, 40 + r * 26, [B, Y2, N, B2, RED, GREEN2][(r * 7 + c) % 6], 9)
                           for r in range(3) for c in range(7)) + f'<rect x="0" y="118" width="200" height="22" fill="{SKY2}"/>', YS),
    'peaceful': svg(sun(158, 34, 15) + bird(70, 30) + bird(92, 22) +
                    f'<rect x="0" y="104" width="200" height="36" fill="#BBF7D0"/>' + tree(46, 74, 1.5) +
                    f'<rect x="96" y="92" width="58" height="8" rx="3" fill="#8B5A2B"/><rect x="100" y="100" width="5" height="14" fill="#8B5A2B"/><rect x="145" y="100" width="5" height="14" fill="#8B5A2B"/>'
                    f'<rect x="96" y="80" width="58" height="6" rx="3" fill="#A86B32"/>'),
    'convenient': svg(ground() + house(18, 64, 1.0) + busstop(160, 118, 1.1) +
                      f'<path d="M70 108h70" stroke="{B}" stroke-width="3" stroke-dasharray="6 5"/>' + badge(78, 66, '2 min', Y, N, 14, 58) +
                      f'<circle cx="40" cy="30" r="18" fill="{G}"/>' + tick(30, 30, .95, W, 5)),
    'nearby': svg(f'<circle cx="100" cy="76" r="50" fill="{W}" stroke="{B}" stroke-width="3" stroke-dasharray="7 6"/>' + pin(100, 92, RED, 1.05) +
                  f'<circle cx="52" cy="50" r="15" fill="{Y}"/>' + emo(52, 51, '🛒', 15) +
                  f'<circle cx="150" cy="54" r="15" fill="{Y}"/>' + emo(150, 55, '🌳', 15) +
                  f'<circle cx="100" cy="124" r="13" fill="{Y}"/>' + emo(100, 125, '☕', 13)),
    'facility': svg(f'<rect x="34" y="24" width="132" height="94" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/>'
                    f'<rect x="34" y="24" width="132" height="22" rx="10" fill="{B}"/><rect x="34" y="36" width="132" height="10" fill="{B}"/>'
                    f'<text x="100" y="40" font-size="12" font-weight="900" fill="{W}" text-anchor="middle" letter-spacing="1.5" {F}>FACILITIES</text>'
                    + dumbbell(70, 74, 1.1) + f'<path d="M112 70q8 -8 16 0t16 0M112 84q8 -8 16 0t16 0" fill="none" stroke="{B2}" stroke-width="4" stroke-linecap="round"/>'
                    f'<rect x="56" y="96" width="88" height="10" rx="5" fill="{YS}"/>'),
    'neighbour': svg(ground() + house(14, 62, 1.0) + house(142, 62, 1.0) + person(100, 70, Y, '#8B4513', .8, True, True) +
                     f'<path d="M118 66l10 -14" stroke="{SK}" stroke-width="6" stroke-linecap="round"/>' + badge(64, 14, 'Hi!', B, W, 15, 46), SKY),
    'located': svg(f'<rect x="16" y="14" width="168" height="112" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/>'
                   f'<path d="M16 70h168M100 14v112M16 40h168M58 14v112M142 14v112M16 100h168" stroke="{SKY2}" stroke-width="5"/>'
                   f'<circle cx="100" cy="70" r="24" fill="{Y}" opacity=".45"/><circle cx="100" cy="70" r="12" fill="{Y}" opacity=".8"/>' + pin(100, 74, RED, .95)),
}

# ------------------------------------------------------------------ collocation scenes
PHRASE = {
    'spacious': svg(f'<rect x="0" y="0" width="200" height="140" rx="18" fill="{YS}"/>'
                    f'<rect x="58" y="12" width="84" height="56" rx="4" fill="{SKY}" stroke="{N}" stroke-width="3"/><path d="M100 12v56M58 40h84" stroke="{N}" stroke-width="2.5"/>'
                    f'<rect x="0" y="104" width="200" height="36" fill="#F2D7A6"/>' + sofa(64, 72, .95) + plant(30, 104, .9) + plant(176, 104, .7) +
                    f'<path d="M14 124h172" stroke="{B}" stroke-width="3" stroke-dasharray="6 5"/>', YS),
    'crowded': svg(awning_shop(8, 22, 56, RED, '🍜') + awning_shop(72, 22, 56, B, '👕') + awning_shop(136, 22, 56, Y2, '🍎') +
                   f'<rect x="0" y="70" width="200" height="70" fill="{SKY2}"/>' +
                   ''.join(head(16 + c * 24 + (r % 2) * 11, 84 + r * 22, [B, Y2, N, B2, RED, GREEN2][(r * 5 + c) % 6], 7.5) for r in range(2) for c in range(8)), SKY),
    'peaceful': svg(sun(166, 28, 13) + bird(90, 26) + f'<rect x="0" y="110" width="200" height="30" fill="#BBF7D0"/>' +
                    house(10, 62, .9) + house(118, 62, .9) + tree(80, 92, 1.1) + tree(178, 98, .9) + tree(62, 104, .6)),
    'convenient': svg(ground() + house(78, 50, .95) +
                      busstop(28, 120, .9) + f'<circle cx="160" cy="44" r="18" fill="{Y}"/>' + emo(160, 45, '🛒', 18) +
                      f'<circle cx="160" cy="100" r="16" fill="{Y}"/>' + emo(160, 101, '☕', 15) +
                      arrow2(46, 96, 76, 90) + arrow2(124, 76, 144, 54) + arrow2(124, 92, 144, 100) + badge(10, 12, '5 min', N, Y, 13, 58)),
    'nearby': svg(house(78, 52, .95) + ''.join(f'<circle cx="{x}" cy="{y}" r="17" fill="{W}" stroke="{B}" stroke-width="2.5"/>' + emo(x, y + 1, e, 17)
                                              for x, y, e in [(30, 34, '🏋️'), (170, 34, '🏥'), (30, 106, '🛒'), (170, 106, '🌳')]) +
                  ''.join(f'<path d="M{a} {b}L{c} {d}" stroke="{B}" stroke-width="2.5" stroke-dasharray="5 5"/>' for a, b, c, d in [(46, 42, 80, 66), (154, 42, 120, 66), (46, 98, 80, 92), (154, 98, 120, 92)])),
    'facility': svg(f'<rect x="10" y="12" width="180" height="70" rx="8" fill="{SKY}" stroke="{N}" stroke-width="3"/><path d="M70 12v70M130 12v70" stroke="{N}" stroke-width="2.5"/>'
                    f'<rect x="0" y="104" width="200" height="36" fill="#E2E8F0"/>'
                    f'<path d="M24 104l18 -26h40l6 26z" fill="{N}"/><rect x="38" y="74" width="48" height="6" rx="3" fill="{B}"/><rect x="74" y="54" width="6" height="26" fill="{GR}"/><rect x="66" y="48" width="22" height="10" rx="3" fill="{N}"/>'
                    + dumbbell(140, 98, 1.1, B) + dumbbell(140, 116, 1.1, N) + star(170, 30, 6) + star(40, 30, 4), W),
    'neighbour': svg(f'<rect x="0" y="94" width="200" height="46" fill="#BBF7D0"/>' + person(58, 58, B, N, 1.05) + person(144, 58, Y, '#8B4513', 1.05, True, True) +
                     ''.join(f'<rect x="{8 + k * 24}" y="96" width="14" height="40" rx="3" fill="{W}" stroke="{GR}" stroke-width="1.5"/>' for k in range(8)) +
                     f'<rect x="0" y="106" width="200" height="6" fill="{W}"/>' + badge(18, 6, 'Hello!', B, W, 13, 66) + badge(114, 6, 'Hi! Welcome!', Y, N, 12, 84)),
    'located': svg(''.join(office(x, y, s, Y, W) for x, y, s in [(12, 64, .6), (40, 50, .75), (132, 54, .7), (162, 70, .55)]) +
                   f'<rect x="0" y="118" width="200" height="22" fill="{SKY2}"/>' +
                   f'<circle cx="100" cy="66" r="34" fill="{Y}" opacity=".35"/>' + pin(100, 84, RED, 1.15) + badge(50, 6, 'CITY CENTRE', N, Y, 12, 100)),
}


# ------------------------------------------------------------------ neighbourhood map (matches MAPQ answers)
def _blk(x, y, w, h, e, label, bg=W):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{N}" stroke-width="2.5"/>' + emo(x + w / 2, y + h / 2 - 8, e, 26) +
            f'<text x="{x + w / 2}" y="{y + h - 10}" font-size="13" font-weight="800" fill="{N}" text-anchor="middle" {F}>{label}</text>')


MAP = ('<svg viewBox="0 0 520 360" xmlns="http://www.w3.org/2000/svg" role="img"><rect width="520" height="360" rx="18" fill="#E8F5E9"/>'
       f'<rect x="0" y="160" width="520" height="40" fill="#CBD5E1"/><rect x="240" y="0" width="40" height="360" fill="#CBD5E1"/>'
       f'<path d="M0 180h520M260 0v360" stroke="{W}" stroke-width="3" stroke-dasharray="14 10"/>'
       + f'<rect x="16" y="14" width="210" height="132" rx="14" fill="#BBF7D0" stroke="{GREEN2}" stroke-width="2.5"/>' + tree(56, 70, 1.2) + tree(110, 60, 1.4) + tree(170, 76, 1.1)
       + f'<text x="121" y="134" font-size="14" font-weight="900" fill="{GREEN2}" text-anchor="middle" {F}>PARK</text>'
       + _blk(294, 14, 104, 70, '🛒', 'Supermarket') + _blk(406, 14, 100, 70, '☕', 'Café')
       + _blk(294, 92, 104, 58, '🧺', 'Market', YS) + _blk(406, 92, 100, 58, '☕', 'Café')
       + _blk(16, 214, 120, 132, '🏫', 'School') + _blk(146, 214, 80, 70, '🏢', 'Apartment')
       + f'<rect x="294" y="214" width="212" height="132" rx="14" fill="{YS}" stroke="{Y2}" stroke-width="3"/>' + house(366, 236, 1.5)
       + f'<text x="400" y="334" font-size="15" font-weight="900" fill="{N}" text-anchor="middle" {F}>MY HOME</text>'
       + busstop(228, 156, .9) + busstop(292, 246, .9)
       + '</svg>')

SCENE = svg(sun(176, 22, 11) + f'<rect x="0" y="104" width="200" height="36" fill="#CBD5E1"/><path d="M0 122h200" stroke="{W}" stroke-width="2" stroke-dasharray="10 8"/>'
            + office(8, 34, .95, Y, W) + awning_shop(66, 58, 50, RED, '☕') + tree(136, 86, 1.0) + tree(160, 92, .8)
            + busstop(186, 104, .8) + ''.join(head(122 + k * 13, 94, [B, Y2, N][k], 5.5) for k in range(3)), SKY)

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    h += f'<div style="grid-column:span 2">{MAP}</div><div>{SCENE}</div></body>'
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'illus_preview.html'), 'w').write(h)
