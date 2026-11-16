"""Original flat SVG illustrations for S07 (same palette/helpers as S02–S06)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..', 'S02')); sys.path.insert(0, os.path.join(D, '..', 'S03')); sys.path.insert(0, os.path.join(D, '..', 'S06'))
from illus import svg, star, tick, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa
from illus06 import plate, txt  # noqa

F = 'font-family="Be Vietnam Pro,sans-serif"'
CLOTH = '#FDE2E2'


def bubble(x, y, w, h, c=B, tail='left'):
    t = f'<path d="M{x + 14} {y + h}l-4 10l14 -10z" fill="{c}"/>' if tail == 'left' else f'<path d="M{x + w - 14} {y + h}l4 10l-14 -10z" fill="{c}"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}"/>' + t


def receipt(x, y, w=76, h=104, lines=('', '', ''), total='', extra=''):
    zig = ''.join(f'L{x + k * w / 8 + w / 16:.1f} {y + h + (5 if k % 2 == 0 else 0)}L{x + (k + 1) * w / 8:.1f} {y + h}' for k in range(8))
    out = f'<path d="M{x} {y}H{x + w}V{y + h}{zig[0:0]}' + ''.join(f'L{x + w - k * w / 8 - w / 16:.1f} {y + h + (5 if k % 2 == 0 else 0)}L{x + w - (k + 1) * w / 8:.1f} {y + h}' for k in range(8)) + f'Z" fill="{W}" stroke="{N}" stroke-width="2.2" stroke-linejoin="round"/>'
    for k, l in enumerate(lines):
        out += f'<rect x="{x + 8}" y="{y + 14 + k * 14}" width="{w * .45:.0f}" height="5" rx="2" fill="{SKY2}"/><rect x="{x + w - 22}" y="{y + 14 + k * 14}" width="14" height="5" rx="2" fill="{SKY2}"/>'
    if extra: out += txt(x + w / 2, y + h - 30, extra, 11, RED)
    if total: out += f'<line x1="{x + 6}" y1="{y + h - 22}" x2="{x + w - 6}" y2="{y + h - 22}" stroke="{N}" stroke-width="1.5"/>' + txt(x + w / 2, y + h - 7, total, 12, N)
    return out


def table(y=104):
    return f'<rect x="0" y="{y}" width="200" height="{140 - y}" fill="{CLOTH}"/><rect x="0" y="{y}" width="200" height="4" fill="#F9B4B4"/>'


def waiter(cx, cy, s=1):
    return person(cx, cy, N, N, s) + f'<path d="M{cx - 6 * s} {cy + 24 * s}l6 {6 * s}l6 -{6 * s}z" fill="{W}"/>'


WORD = {
    'starter': svg(table() + plate(100, 104, 52) + emo(100, 88, '🥣', 40) + badge(14, 12, '1 · STARTER', B, W, 11, 86), YS),
    'main course': svg(table() + plate(100, 106, 66) + emo(86, 90, '🍗', 36) + emo(120, 92, '🥦', 24) + badge(14, 12, '2 · MAIN', N, Y, 11, 70)),
    'side dish': svg(table() + plate(78, 106, 58) + emo(78, 90, '🐟', 34) + plate(164, 110, 26) + emo(164, 102, '🍟', 22)
                     + f'<path d="M150 70q8 -18 18 -4" fill="none" stroke="{RED}" stroke-width="3"/>' + txt(170, 60, 'side', 12, RED), YS),
    'recommend': svg(waiter(64, 52, 1) + bubble(104, 18, 86, 34, G) + txt(147, 40, 'Try this!', 13, W) + emo(150, 96, '👍', 34) + star(178, 74, 6)),
    'allergy': svg(emo(100, 72, '🥜', 54) + f'<circle cx="100" cy="72" r="44" fill="none" stroke="{RED}" stroke-width="7"/><line x1="70" y1="42" x2="130" y2="102" stroke="{RED}" stroke-width="7"/>', YS),
    'bill': svg(receipt(62, 14, 76, 104, ('', '', '', ''), '£40.00')),
    'service charge': svg(receipt(40, 14, 76, 104, ('', ''), '£44.00', '+ 10%') + badge(128, 50, 'SERVICE', N, Y, 11, 62), YS),
    'split': svg(receipt(62, 10, 76, 70, ('', ''), '£40') + f'<line x1="100" y1="6" x2="100" y2="90" stroke="{RED}" stroke-width="3" stroke-dasharray="5 4"/>'
                 + badge(26, 98, '£20', B, W, 13, 50) + badge(124, 98, '£20', G, W, 13, 50)),
}

PHRASE = {
    'starter': svg(table(100) + waiter(150, 44, .8) + f'<rect x="168" y="62" width="22" height="28" rx="3" fill="{W}" stroke="{N}" stroke-width="2"/>'
                   + plate(64, 104, 44) + emo(64, 92, '🥣', 30) + bubble(10, 12, 96, 30, B) + txt(58, 32, 'Soup, please!', 11, W), YS),
    'main course': svg(f'<rect x="38" y="10" width="124" height="120" rx="10" fill="{W}" stroke="{N}" stroke-width="2.5"/>' + txt(100, 30, 'MENU', 14, RED)
                       + ''.join(f'<rect x="52" y="{42 + k * 18}" width="70" height="7" rx="3" fill="{SKY2}"/><rect x="128" y="{42 + k * 18}" width="20" height="7" rx="3" fill="{SKY2}"/>' for k in range(5))
                       + f'<rect x="46" y="74" width="108" height="16" rx="5" fill="none" stroke="{G}" stroke-width="3"/>' + emo(168, 82, '👈', 26)),
    'side dish': svg(table() + plate(70, 106, 56) + emo(70, 90, '🍔', 34) + plate(144, 108, 24) + emo(144, 101, '🍟', 20) + plate(184, 112, 16) + emo(184, 107, '🥗', 14)
                     + badge(110, 14, 'with a side dish', N, Y, 10, 84), YS),
    'recommend': svg(waiter(50, 50, .9) + bubble(84, 12, 108, 40, G) + txt(138, 30, 'I recommend', 11, W) + txt(138, 45, 'the fish!', 12, W) + table(108) + plate(140, 112, 34) + emo(140, 104, '🐟', 26)),
    'allergy': svg(person(56, 50, B, N, .9) + bubble(92, 14, 100, 40, RED) + txt(142, 32, 'No nuts,', 12, W) + txt(142, 47, 'please!', 12, W) + table(108) + emo(150, 112, '🥜', 22)
                   + f'<line x1="136" y1="100" x2="164" y2="124" stroke="{RED}" stroke-width="4"/>', YS),
    'bill': svg(person(60, 50, Y, N, .9) + f'<path d="M84 50l10 -26" stroke="{SK}" stroke-width="8" stroke-linecap="round"/>' + bubble(100, 14, 92, 30, B) + txt(146, 34, 'The bill, please!', 10, W)
                + receipt(128, 60, 52, 66, ('', ''), '£30')),
    'service charge': svg(receipt(30, 10, 104, 120, ('', '', ''), '£55.00', 'Service 10%  £5.00') + emo(162, 70, '🙋', 34), YS),
    'split': svg(person(44, 50, B, N, .75) + person(156, 50, G, '#8B4513', .75, True, True) + receipt(78, 30, 44, 60, ('', ''), '') + txt(100, 110, '½ + ½', 16, RED) + table(118)),
}

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h + '</body>')
