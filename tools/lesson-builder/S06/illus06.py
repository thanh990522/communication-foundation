"""Original flat SVG illustrations for S06 (same palette/helpers as S02–S05)."""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..', 'S02')); sys.path.insert(0, os.path.join(D, '..', 'S03'))
from illus import svg, star, tick, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, RED, GREEN, GREEN2  # noqa

F = 'font-family="Be Vietnam Pro,sans-serif"'
WOOD = '#C98A4B'


def txt(x, y, t, s=12, c=N, w=900, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{c}" text-anchor="{anchor}" {F}>{t}</text>'


def shelf(x, y, w, items, s=20):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="2" fill="{WOOD}"/>'
    for k, e in enumerate(items):
        if e: out += emo(x + 14 + k * (w - 28) / max(len(items) - 1, 1), y - s * .55, e, s)
    return out


def carton(x, y, s=1, c=B, label='MILK'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 14L10 0H34L44 14V70H0Z" fill="{W}" stroke="{N}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<path d="M0 14H44" stroke="{N}" stroke-width="2"/><rect x="0" y="30" width="44" height="22" fill="{c}"/>'
            f'<text x="22" y="46" font-size="11" font-weight="900" fill="{W}" text-anchor="middle" {F}>{label}</text></g>')


def packet(x, y, s=1, c=Y, label='RICE'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M4 0H50L54 8V74Q54 80 48 80H6Q0 80 0 74V8Z" fill="{c}" stroke="{N}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<path d="M4 0L8 8H46L50 0" fill="none" stroke="{N}" stroke-width="2"/><rect x="8" y="28" width="38" height="22" rx="4" fill="{W}"/>'
            f'<text x="27" y="44" font-size="11" font-weight="900" fill="{N}" text-anchor="middle" {F}>{label}</text>'
            f'<text x="27" y="68" font-size="14" text-anchor="middle">🍚</text></g>')


def plate(x, y, r, food='', fs=26):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * .45}" fill="{W}" stroke="{N}" stroke-width="2.5"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{r * .7}" ry="{r * .3}" fill="none" stroke="{SKY2}" stroke-width="2"/>'
            + (emo(x, y - fs * .25, food, fs) if food else ''))


def bowl(x, y, w=80):
    return f'<path d="M{x - w / 2} {y}Q{x - w / 2} {y + w * .5} {x} {y + w * .5}Q{x + w / 2} {y + w * .5} {x + w / 2} {y}Z" fill="{B}" stroke="{N}" stroke-width="2.5"/>'


def trolley(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0H10L18 36H58L66 10H14" fill="none" stroke="{N}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="24" cy="46" r="5" fill="{N}"/><circle cx="52" cy="46" r="5" fill="{N}"/></g>')


# ------------------------------------------------------------------ word cards
WORD = {
    'ingredient': svg(bowl(100, 70, 92) + emo(76, 62, '🥕', 22) + emo(100, 56, '🍅', 24) + emo(124, 62, '🥚', 22) + emo(88, 46, '🧀', 18) + emo(114, 44, '🍗', 18)),
    'portion': svg(plate(100, 92, 70) + emo(100, 74, '🍚', 44) + emo(70, 86, '🍗', 22) + emo(132, 86, '🥕', 20) + badge(130, 14, 'LARGE', N, Y, 12, 58), YS),
    'fresh': svg(emo(76, 76, '🍅', 54) + emo(132, 70, '🥕', 50) + star(48, 30, 7) + star(160, 26, 6) + star(104, 116, 5)),
    'dairy': svg(carton(38, 40, 1.15) + emo(118, 92, '🧀', 40) + emo(160, 90, '🧈', 34) + emo(150, 44, '🥣', 30), YS),
    'aisle': svg(f'<rect x="0" y="0" width="56" height="140" fill="{W}"/><rect x="144" y="0" width="56" height="140" fill="{W}"/>'
                 + ''.join(shelf(4, 30 + k * 34, 48, ['🥫', '🧃'][:1 + k % 2], 15) + shelf(148, 30 + k * 34, 48, ['🍞', '🥛'][:1 + (k + 1) % 2], 15) for k in range(3))
                 + f'<path d="M56 140L84 70H116L144 140Z" fill="{SKY2}"/>' + f'<rect x="78" y="10" width="44" height="30" rx="6" fill="{B}"/>' + txt(100, 32, '3', 20, W)),
    'enough': svg(emo(52, 72, '🥚', 30) + emo(82, 72, '🥚', 30) + emo(112, 72, '🥚', 30) + emo(67, 46, '🥚', 30) + emo(97, 46, '🥚', 30)
                  + f'<circle cx="160" cy="62" r="24" fill="{G}"/>' + tick(149, 62, 1, W, 5) + badge(40, 104, '4 needed · 5 here', N, Y, 11, 120)),
    'out of stock': svg(f'<rect x="20" y="20" width="160" height="100" rx="6" fill="{W}" stroke="{N}" stroke-width="2.5"/>' + shelf(26, 60, 148, ['', '', '']) + shelf(26, 104, 148, ['', '🥛', ''])
                        + f'<g transform="rotate(-12 100 52)"><rect x="40" y="34" width="120" height="34" rx="8" fill="{RED}"/>' + txt(100, 57, 'SOLD OUT', 16, W) + '</g>', YS),
    'a packet of': svg(packet(74, 28, 1.05)),
}

# ------------------------------------------------------------------ collocation scenes
PHRASE = {
    'ingredient': svg(f'<rect x="0" y="104" width="200" height="36" fill="{WOOD}" fill-opacity=".5"/>' + bowl(70, 70, 86) + emo(56, 64, '🥕', 20) + emo(78, 58, '🍅', 22)
                      + emo(96, 66, '🧅', 18) + person(156, 62, Y, N, .75) + star(40, 24, 6) + badge(118, 10, 'FRESH!', G, W, 11, 60), YS),
    'portion': svg(plate(70, 100, 60) + emo(70, 80, '🍚', 52) + plate(160, 106, 26) + emo(160, 98, '🍚', 18) + txt(70, 26, 'LARGE', 14, RED) + txt(160, 70, 'small', 11, GR, 800)),
    'fresh': svg(f'<rect x="10" y="70" width="180" height="56" rx="8" fill="{WOOD}"/><path d="M6 30H194L180 6H20Z" fill="{RED}"/>'
                 + ''.join(f'<rect x="{20 + k * 40}" y="6" width="20" height="24" fill="{W}" fill-opacity=".7"/>' for k in range(4))
                 + emo(40, 86, '🍅', 26) + emo(80, 86, '🥕', 26) + emo(120, 86, '🍎', 26) + emo(160, 86, '🥬', 26), YS),
    'dairy': svg(carton(20, 36, 1) + emo(98, 86, '🧀', 36) + emo(140, 90, '🧈', 30) + emo(176, 88, '🥣', 28) + emo(110, 40, '🥛', 30) + badge(124, 12, 'DAIRY', B, W, 11, 56)),
    'aisle': svg(f'<rect x="0" y="0" width="200" height="140" fill="{W}"/><rect x="0" y="0" width="52" height="140" fill="{SKY}"/><rect x="148" y="0" width="52" height="140" fill="{SKY}"/>'
                 + ''.join(shelf(2, 30 + k * 36, 48, ['🍚', '🥫'], 14) + shelf(150, 30 + k * 36, 48, ['🍞', '🧃'], 14) for k in range(3))
                 + trolley(70, 74, 1) + person(100, 46, G, N, .6)),
    'enough': svg(f'<rect x="40" y="10" width="120" height="122" rx="10" fill="{W}" stroke="{N}" stroke-width="3"/>' + shelf(46, 50, 108, ['🥚', '🥚', '🥛'], 18)
                  + shelf(46, 86, 108, ['🧀', '🥕', '🍅'], 18) + shelf(46, 122, 108, ['🍎', '🍎', '🧈'], 18)
                  + f'<circle cx="170" cy="30" r="20" fill="{G}"/>' + tick(161, 30, .85, W, 4)),
    'out of stock': svg(f'<rect x="10" y="16" width="120" height="112" rx="6" fill="{W}" stroke="{N}" stroke-width="2.5"/>' + shelf(16, 56, 108, ['', '', ''])
                        + shelf(16, 100, 108, ['', '', '']) + badge(20, 64, 'OUT OF STOCK', RED, W, 10, 100) + person(164, 62, B, N, .7, False)
                        + txt(164, 18, '?', 22, B), YS),
    'a packet of': svg(packet(20, 30, .95) + packet(78, 30, .95, '#FDE68A') + trolley(132, 70, .9) + txt(100, 132, 'a packet of rice', 12, B2)),
}

ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h + '</body>')
