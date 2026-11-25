"""Original flat SVG illustrations for S10 (same palette/helpers as S02–S09)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
for _p in ('S02', 'S03', 'S06', 'S07', 'S08', 'S09'): sys.path.insert(0, os.path.join(D, '..', _p))
from illus import svg, star, tick, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa
from illus06 import txt  # noqa
from illus07 import bubble  # noqa


def cal(x, y, label, c=B):
    return (f'<rect x="{x}" y="{y}" width="58" height="56" rx="8" fill="{W}" stroke="{N}" stroke-width="2.5"/><rect x="{x}" y="{y}" width="58" height="16" rx="8" fill="{c}"/>'
            + txt(x + 29, y + 12, label, 10, W))


def back_arrow(x, y, w=60):
    return f'<path d="M{x + w} {y}H{x + 10}l8 -8M{x + 10} {y}l8 8" stroke="{RED}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'


WORD = {
    'attend': svg(emo(100, 64, '🎤', 54) + emo(48, 104, '🙋', 30) + emo(100, 108, '🙋', 30) + emo(152, 104, '🙋', 30) + star(30, 26, 6) + star(172, 26, 6), YS),
    'visit': svg(f'<rect x="30" y="54" width="140" height="70" fill="{W}" stroke="{N}" stroke-width="3"/>' + ''.join(f'<path d="M{30 + k * 28} 54l14 -20l14 20z" fill="{RED if k % 2 else Y}" stroke="{N}" stroke-width="2"/>' for k in range(5))
                 + emo(64, 96, '🥭', 26) + emo(100, 96, '🐟', 26) + emo(136, 96, '🥬', 26)),
    'stay': svg(f'<rect x="56" y="30" width="88" height="90" fill="{W}" stroke="{N}" stroke-width="3"/>' + txt(100, 50, 'HOTEL', 13, B)
                + ''.join(f'<rect x="{68 + (k % 3) * 24}" y="{60 + (k // 3) * 24}" width="16" height="14" fill="{Y if k == 4 else SKY2}"/>' for k in range(6)) + emo(160, 34, '🌙', 26), YS),
    'return': svg(f'<path d="M40 110V70l40 -32l40 32v40z" fill="{W}" stroke="{N}" stroke-width="3"/><rect x="70" y="84" width="20" height="26" fill="{B}"/>' + back_arrow(118, 80, 60) + emo(170, 58, '🚶', 30)),
    'enjoy': svg(emo(100, 68, '😄', 66) + star(40, 30, 7) + star(162, 34, 6) + star(150, 108, 5), YS),
    'exhausted': svg(emo(100, 66, '😩', 66) + f'<path d="M150 30q6 10 0 18" stroke="{B}" stroke-width="4" fill="none"/>' + badge(60, 110, 'so tired!', RED, W, 12, 80)),
    'memorable': svg(f'<rect x="44" y="24" width="112" height="86" rx="6" fill="{W}" stroke="{N}" stroke-width="3" transform="rotate(-6 100 67)"/>' + emo(100, 66, '🌅', 54) + emo(160, 104, '❤️', 26), YS),
    'event': svg(emo(100, 62, '🎉', 60) + badge(54, 106, 'SAT · 7 PM', N, Y, 12, 92)),
}

PHRASE = {
    'attend': svg(person(48, 54, B, N, .85) + bubble(82, 12, 112, 40, G) + txt(138, 29, 'I attended', 11, W) + txt(138, 44, 'an event!', 11, W) + emo(140, 100, '🎤', 30), YS),
    'visit': svg(person(48, 54, Y, '#8B4513', .85, True, True) + emo(126, 90, '🛒', 40) + bubble(84, 10, 110, 40, B) + txt(139, 27, 'We visited', 11, W) + txt(139, 42, 'a local market', 10, W)),
    'stay': svg(emo(60, 74, '🏨', 56) + emo(130, 60, '🌙', 30) + emo(150, 100, '🛏', 34) + badge(96, 14, '1 night', N, Y, 12, 70), YS),
    'return': svg(f'<path d="M110 112V78l34 -26l34 26v34z" fill="{W}" stroke="{N}" stroke-width="3"/>' + person(52, 54, G, N, .85) + f'<path d="M78 92h28l-6 -6M106 92l-6 6" stroke="{B}" stroke-width="4" fill="none" stroke-linecap="round"/>' + badge(120, 18, 'Sunday', B, W, 11, 60)),
    'enjoy': svg(person(56, 54, B, N, .85) + bubble(90, 12, 104, 44, G) + txt(142, 30, 'I really enjoyed', 10, W) + txt(142, 45, 'the experience!', 10, W) + emo(150, 104, '🎢', 28), YS),
    'exhausted': svg(person(70, 60, GR, N, .9) + emo(70, 112, '🥾', 22) + bubble(104, 14, 90, 36, RED) + txt(149, 37, 'I felt exhausted.', 9.5, W) + emo(160, 94, '😩', 32)),
    'memorable': svg(f'<rect x="20" y="30" width="70" height="56" rx="4" fill="{W}" stroke="{N}" stroke-width="2.5" transform="rotate(-8 55 58)"/>' + emo(55, 58, '🌴', 32)
                     + f'<rect x="96" y="40" width="70" height="56" rx="4" fill="{W}" stroke="{N}" stroke-width="2.5" transform="rotate(6 131 68)"/>' + emo(131, 68, '🎡', 32) + badge(50, 108, 'a memorable trip', N, Y, 11, 104), YS),
    'event': svg(cal(26, 30, 'SAT') + txt(55, 70, '12', 18, N) + emo(130, 64, '🎶', 46) + badge(92, 104, 'weekend event', B, W, 11, 92)),
}

HOLIDAY_ART = svg(f'<rect x="0" y="92" width="200" height="48" fill="#7DD3FC"/>' + emo(46, 56, '☀️', 40) + emo(140, 66, '🍕', 44) + emo(70, 108, '⛵', 26) + badge(112, 14, 'ITALY', RED, W, 12, 60), YS)

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE, {'holiday': HOLIDAY_ART}):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h + '</body>')
