"""Original flat SVG illustrations for S09 (same palette/helpers as S02–S08)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
for _p in ('S02', 'S03', 'S06', 'S07', 'S08'): sys.path.insert(0, os.path.join(D, '..', _p))
from illus import svg, star, tick, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa
from illus06 import txt  # noqa
from illus07 import bubble, receipt  # noqa
from illus08 import box  # noqa


def phone(x, y, s=1, scr=SKY2):
    return (f'<rect x="{x}" y="{y}" width="{34 * s}" height="{60 * s}" rx="{6 * s}" fill="{N}"/>'
            f'<rect x="{x + 3 * s}" y="{y + 7 * s}" width="{28 * s}" height="{44 * s}" rx="2" fill="{scr}"/><circle cx="{x + 17 * s}" cy="{y + 55 * s}" r="{2 * s}" fill="{W}"/>')


def headset(cx, cy, s=1):
    return person(cx, cy, B, N, s) + f'<path d="M{cx - 11 * s} {cy}a{11 * s} {11 * s} 0 0 1 {22 * s} 0" fill="none" stroke="{N}" stroke-width="{3 * s}"/><path d="M{cx + 11 * s} {cy + 2 * s}q0 {10 * s} -{8 * s} {11 * s}" fill="none" stroke="{N}" stroke-width="{2 * s}"/><circle cx="{cx + 3 * s}" cy="{cy + 13 * s}" r="{2.4 * s}" fill="{N}"/>'


def truck(x, y, s=1):
    return (f'<rect x="{x}" y="{y}" width="{70 * s}" height="{40 * s}" rx="4" fill="{Y}" stroke="{N}" stroke-width="2.4"/>'
            f'<path d="M{x + 70 * s} {y + 12 * s}h{20 * s}l{12 * s} {14 * s}v{14 * s}h-{32 * s}z" fill="{B}" stroke="{N}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<circle cx="{x + 18 * s}" cy="{y + 42 * s}" r="{8 * s}" fill="{N}"/><circle cx="{x + 84 * s}" cy="{y + 42 * s}" r="{8 * s}" fill="{N}"/>')


WORD = {
    'delivery': svg(truck(40, 50, 1) + emo(76, 40, '📦', 26) + f'<path d="M14 70h18M8 82h22" stroke="{GR}" stroke-width="3" stroke-linecap="round"/>', YS),
    'repair': svg(f'<rect x="40" y="22" width="76" height="96" rx="8" fill="{W}" stroke="{N}" stroke-width="3"/><line x1="40" y1="42" x2="116" y2="42" stroke="{N}" stroke-width="2.5"/>'
                  f'<circle cx="54" cy="32" r="3.5" fill="{B}"/><circle cx="66" cy="32" r="3.5" fill="{Y}"/><circle cx="78" cy="78" r="26" fill="{SKY2}" stroke="{N}" stroke-width="3"/><path d="M62 82q8 -8 16 0t16 0" stroke="{B}" stroke-width="3" fill="none"/>'
                  + emo(150, 66, '🔧', 44) + star(178, 30, 6)),
    'issue': svg(emo(100, 66, '⚠️', 70) + badge(60, 112, 'problem', RED, W, 13, 80), YS),
    'customer service': svg(headset(100, 54, 1.2) + bubble(128, 12, 64, 30, G) + txt(160, 32, 'Hello!', 12, W)),
    'replacement': svg(box(18, 50, 64, 46) + f'<path d="M30 70l12 10l-6 8" stroke="{RED}" stroke-width="4" fill="none"/>' + f'<path d="M92 76h24l-6 -6M116 76l-6 6" stroke="{B}" stroke-width="4" fill="none" stroke-linecap="round"/>'
                       + box(122, 50, 64, 46, '#F3C98B') + star(178, 40, 6), YS),
    'charge': svg(receipt(52, 14, 70, 100, ('', '', ''), '+ £20') + emo(150, 70, '💳', 40)),
    'available': svg(f'<rect x="40" y="20" width="120" height="100" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/><rect x="40" y="20" width="120" height="24" rx="10" fill="{B}"/>'
                     + txt(100, 37, 'FRIDAY', 13, W) + f'<rect x="56" y="58" width="88" height="22" rx="6" fill="{G}"/>' + txt(100, 74, '9:00 ✓ free', 12, W)
                     + f'<rect x="56" y="88" width="88" height="22" rx="6" fill="{SKY2}"/>' + txt(100, 104, '2:00 busy', 12, GR), YS),
    'confirm': svg(f'<rect x="46" y="16" width="108" height="108" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/>'
                   + ''.join(f'<rect x="60" y="{34 + k * 22}" width="60" height="7" rx="3" fill="{SKY2}"/>' for k in range(4))
                   + ''.join(tick(128, 30 + k * 22, .55, G, 3) for k in range(4)) + badge(64, 112, 'OK ✓', G, W, 12, 72)),
}

PHRASE = {
    'delivery': svg(person(48, 52, Y, N, .85) + phone(80, 56, .7) + bubble(98, 10, 96, 44, B) + txt(146, 28, 'Where is my', 11, W) + txt(146, 44, 'parcel? 📦', 11, W)),
    'repair': svg(headset(150, 52, .85) + bubble(10, 12, 112, 40, G) + txt(66, 29, 'Book a repair', 11, W) + txt(66, 44, 'for Monday?', 11, W) + emo(56, 104, '🔧', 30), YS),
    'issue': svg(person(52, 52, G, '#8B4513', .85, True, True) + phone(84, 54, .7) + bubble(100, 10, 94, 44, RED) + txt(147, 28, 'There seems', 11, W) + txt(147, 44, 'to be a problem', 10, W)),
    'customer service': svg(person(46, 54, Y, N, .8) + phone(70, 58, .6) + f'<path d="M100 70q14 -16 28 0" stroke="{B}" stroke-width="3" fill="none" stroke-dasharray="4 4"/>' + headset(160, 54, .8), YS),
    'replacement': svg(box(20, 56, 58, 42) + f'<line x1="22" y1="56" x2="78" y2="104" stroke="{RED}" stroke-width="4"/>' + bubble(92, 14, 100, 40, B) + txt(142, 31, 'A new one,', 11, W) + txt(142, 46, 'please!', 11, W) + box(118, 74, 50, 38, '#F3C98B')),
    'charge': svg(receipt(28, 14, 70, 106, ('', '', ''), '£45', '+ £15') + person(150, 56, B, N, .8) + emo(150, 106, '😮', 26), YS),
    'available': svg(headset(50, 52, .8) + bubble(84, 10, 108, 40, B) + txt(138, 27, 'Are you available', 10, W) + txt(138, 42, 'on Friday?', 11, W) + emo(140, 100, '📅', 34)),
    'confirm': svg(person(52, 52, Y, '#8B4513', .85, True, True) + bubble(88, 10, 104, 44, G) + txt(140, 28, 'Could you confirm', 10, W) + txt(140, 44, 'the details?', 11, W) + tick(120, 92, 1, G, 5), YS),
}

CALL_ART = svg(person(46, 54, Y, N, .9) + phone(74, 60, .6) + f'<path d="M98 66q20 -22 40 0" stroke="{B}" stroke-width="3" fill="none" stroke-dasharray="4 4"/>' + headset(160, 54, .9), YS)
REPAIR_ART = svg(f'<rect x="30" y="40" width="100" height="70" rx="6" fill="{N}"/><rect x="38" y="48" width="84" height="54" rx="3" fill="{SKY2}"/>'
                 + emo(80, 76, '🐢', 34) + f'<rect x="20" y="110" width="120" height="8" rx="3" fill="{GR}"/>' + emo(160, 70, '🔧', 40) + badge(118, 16, '£100?', RED, W, 12, 60), YS)

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE, {'call': CALL_ART, 'repair': REPAIR_ART}):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h + '</body>')
