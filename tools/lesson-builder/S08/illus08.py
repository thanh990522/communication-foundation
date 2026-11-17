"""Original flat SVG illustrations for S08 (same palette/helpers as S02–S07)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
for _p in ('S02', 'S03', 'S06', 'S07'): sys.path.insert(0, os.path.join(D, '..', _p))
from illus import svg, star, tick, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa
from illus06 import txt  # noqa
from illus07 import bubble, receipt  # noqa


def tag(x, y, label, c=Y, fc=N, w=54):
    return (f'<path d="M{x} {y}h{w}l12 13l-12 13h-{w}z" fill="{c}" stroke="{N}" stroke-width="2" stroke-linejoin="round"/>'
            f'<circle cx="{x + w + 3}" cy="{y + 13}" r="3" fill="{W}" stroke="{N}" stroke-width="1.5"/>' + txt(x + w / 2, y + 18, label, 13, fc))


def mirror(x, y, w=64, h=110):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#DCEBFF" stroke="{N}" stroke-width="3"/><path d="M{x + 10} {y + 18}l18 -10M{x + 10} {y + 34}l30 -18" stroke="{W}" stroke-width="4" stroke-linecap="round"/>'


def box(x, y, w=70, h=50, c='#E8B878'):
    return (f'<path d="M{x} {y + 12}l{w / 2} -12l{w / 2} 12v{h}l-{w / 2} 10l-{w / 2} -10z" fill="{c}" stroke="{N}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<path d="M{x} {y + 12}l{w / 2} 10l{w / 2} -10M{x + w / 2} {y + 22}v{h}" fill="none" stroke="{N}" stroke-width="2"/>')


WORD = {
    'fit': svg(emo(100, 70, '👖', 70) + f'<path d="M40 30v80M160 30v80" stroke="{G}" stroke-width="4" stroke-dasharray="6 5"/>' + badge(66, 112, 'fits ✓', G, W, 13, 68), YS),
    'suit': svg(person(80, 52, B, N, 1) + mirror(124, 18) + emo(156, 76, '👔', 34) + star(40, 28, 6) + star(176, 116, 5)),
    'size': svg(''.join(badge(14 + k * 37, 54, s, B if s == 'M' else W, W if s == 'M' else N, 14, 32) for k, s in enumerate(['XS', 'S', 'M', 'L', 'XL'])) + emo(100, 106, '👕', 34), YS),
    'receipt': svg(receipt(62, 12, 76, 108, ('', '', '', ''), '£32.00')),
    'exchange': svg(emo(52, 72, '👕', 46) + emo(148, 72, '👕', 46) + txt(52, 120, 'S', 15, N) + txt(148, 120, 'M', 15, N)
                    + f'<path d="M80 56h40l-8 -8M120 88h-40l8 8" fill="none" stroke="{B}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>', YS),
    'refund': svg(emo(60, 64, '💷', 52) + f'<path d="M140 44a26 26 0 1 1 -22 -6" fill="none" stroke="{G}" stroke-width="5" stroke-linecap="round"/><path d="M114 30l6 10l-10 4" fill="none" stroke="{G}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
                  + badge(40, 108, 'money back', G, W, 12, 120)),
    'damaged': svg(emo(100, 72, '🧥', 74) + f'<path d="M86 60l10 10l-8 8l12 12" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' + badge(130, 16, 'broken', RED, W, 12, 58), YS),
    'discount': svg(tag(36, 40, '-20%', RED, W, 70) + txt(70, 100, '£40', 18, GR) + f'<line x1="50" y1="94" x2="90" y2="94" stroke="{RED}" stroke-width="3"/>' + txt(140, 100, '£32', 22, G)),
}

PHRASE = {
    'fit': svg(person(70, 50, B, N, 1) + emo(70, 96, '👖', 34) + bubble(108, 18, 84, 38, G) + txt(150, 34, 'They fit', 12, W) + txt(150, 49, 'perfectly!', 12, W)),
    'suit': svg(person(56, 52, Y, '#8B4513', .9, True, True) + person(150, 52, B, N, .9) + bubble(96, 10, 100, 30, G, 'right') + txt(146, 30, 'Blue suits you!', 11, W), YS),
    'size': svg(person(56, 52, G, N, .9) + bubble(92, 12, 100, 40, B) + txt(142, 29, 'Is this the', 11, W) + txt(142, 44, 'correct size?', 11, W) + tag(100, 92, 'M', Y, N, 40)),
    'receipt': svg(person(58, 52, B, N, .9) + receipt(110, 22, 58, 80, ('', '', ''), '£45') + f'<path d="M80 70q14 0 28 0" stroke="{SK}" stroke-width="8" stroke-linecap="round"/>' + badge(96, 112, 'keep it!', N, Y, 11, 70), YS),
    'exchange': svg(person(48, 52, Y, N, .85) + box(108, 64) + bubble(76, 8, 116, 40, B) + txt(134, 25, "I'd like to", 11, W) + txt(134, 40, 'exchange it.', 11, W)),
    'refund': svg(person(52, 52, G, '#8B4513', .85, True, True) + emo(140, 92, '💷', 34) + bubble(84, 10, 108, 40, G) + txt(138, 27, "I'd like to", 11, W) + txt(138, 42, 'get a refund.', 11, W), YS),
    'damaged': svg(box(30, 56, 80, 54) + f'<path d="M46 86l12 8l-6 10l14 4" fill="none" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>' + emo(150, 70, '😟', 44) + badge(118, 112, 'damaged', RED, W, 12, 70)),
    'discount': svg(person(150, 52, N, N, .85) + tag(14, 24, 'SALE', RED, W, 58) + bubble(14, 70, 112, 40, B) + txt(70, 87, "We're offering", 11, W) + txt(70, 102, 'a 20% discount.', 11, W), YS),
}

SHOP_ART = svg(f'<rect x="20" y="40" width="160" height="96" fill="{W}" stroke="{N}" stroke-width="3"/>' + ''.join(f'<path d="M{20 + k * 32} 40l16 -22h0l16 22z" fill="{RED if k % 2 else W}" stroke="{N}" stroke-width="2"/>' for k in range(5))
               + f'<rect x="20" y="18" width="160" height="6" fill="{N}"/>' + emo(60, 86, '👕', 30) + emo(100, 86, '👖', 30) + emo(140, 86, '👗', 30) + badge(56, 112, 'REFUNDS', N, Y, 11, 88), YS)

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE, {'shop': SHOP_ART}):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h + '</body>')
