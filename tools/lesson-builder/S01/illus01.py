"""Original flat SVG illustrations for S01 — same palette and helpers as S02."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'S02'))
from illus import svg, badge, star, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK  # noqa: E402

F = 'font-family="Be Vietnam Pro,sans-serif"'


def tiles(x, y, letters, s=22, gap=4, bg=B, fg=W):
    out = ''
    for k, L in enumerate(letters):
        cx = x + k * (s + gap)
        out += (f'<rect x="{cx}" y="{y}" width="{s}" height="{s}" rx="5" fill="{bg if k % 2 == 0 else Y}"/>'
                f'<text x="{cx + s / 2}" y="{y + s * .74}" font-size="{s * .62:.0f}" font-weight="900" fill="{fg if k % 2 == 0 else N}" text-anchor="middle" {F}>{L}</text>')
    return out


def person(cx, cy, body, hair, long_hair=False):
    hr = (f'<path d="M{cx - 15} {cy - 4}q2 -22 15 -20q13 -2 15 20q-2 -10 -15 -10q-13 0 -15 10z" fill="{hair}"/>' if not long_hair else
          f'<path d="M{cx - 16} {cy + 10}q-3 -32 16 -32q19 0 16 32l-5 -2q2 -18 -11 -18q-13 0 -11 18z" fill="{hair}"/>')
    return (f'<path d="M{cx - 30} {cy + 56}q0 -32 30 -32q30 0 30 32z" fill="{body}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="15" fill="{SK}"/>' + hr)


LISTEN = svg(
    # headphones
    f'<path d="M30 78v-14q0 -36 36 -36q36 0 36 36v14" fill="none" stroke="{N}" stroke-width="8" stroke-linecap="round"/>'
    f'<rect x="20" y="70" width="22" height="36" rx="9" fill="{B}"/><rect x="90" y="70" width="22" height="36" rx="9" fill="{B}"/>'
    f'<path d="M50 88q8 -8 0 -16M58 94q14 -14 0 -28" fill="none" stroke="{Y2}" stroke-width="4" stroke-linecap="round"/>'
    # notepad
    f'<rect x="122" y="22" width="64" height="98" rx="8" fill="{W}" stroke="{N}" stroke-width="3"/>'
    f'<rect x="140" y="16" width="28" height="12" rx="4" fill="{Y}"/>'
    f'<text x="130" y="48" font-size="11" font-weight="900" fill="{B}" {F}>Mr</text>'
    + ''.join(f'<text x="{129 + k * 10}" y="68" font-size="12" font-weight="900" fill="{N}" {F}>{L}</text>' for k, L in enumerate('BLACK')) +
    f'<rect x="130" y="74" width="48" height="3" rx="1.5" fill="{Y}"/>'
    f'<rect x="130" y="90" width="40" height="5" rx="2.5" fill="{SKY2}"/><rect x="130" y="102" width="30" height="5" rx="2.5" fill="{SKY2}"/>', SKY)

DESK = svg(
    person(64, 46, B, N) +
    f'<rect x="10" y="78" width="180" height="50" rx="8" fill="{N}"/><rect x="10" y="78" width="180" height="10" rx="5" fill="{B2}"/>'
    f'<text x="100" y="114" font-size="15" font-weight="900" fill="{Y}" text-anchor="middle" letter-spacing="2" {F}>RECEPTION</text>'
    # bell
    f'<path d="M136 74q0 -16 14 -16q14 0 14 16z" fill="{Y}"/><rect x="132" y="73" width="36" height="5" rx="2.5" fill="{Y2}"/><circle cx="150" cy="56" r="3" fill="{Y2}"/>'
    # form
    f'<g transform="rotate(-8 112 66)"><rect x="96" y="50" width="30" height="26" rx="3" fill="{W}" stroke="{GR}" stroke-width="1.5"/>'
    f'<rect x="100" y="56" width="20" height="3" rx="1.5" fill="{SKY2}"/><rect x="100" y="63" width="16" height="3" rx="1.5" fill="{SKY2}"/></g>'
    + star(176, 22, 5) + star(24, 20, 4), YS)

PAIR = svg(
    person(46, 82, B, N) + person(154, 82, Y, '#8B4513', True) +
    f'<rect x="8" y="10" width="92" height="40" rx="12" fill="{B}"/><path d="M36 50l-4 12l16 -12z" fill="{B}"/>'
    f'<text x="54" y="27" font-size="10.5" font-weight="800" fill="{W}" text-anchor="middle" {F}>How do you</text>'
    f'<text x="54" y="41" font-size="10.5" font-weight="800" fill="{W}" text-anchor="middle" {F}>spell that?</text>'
    f'<rect x="102" y="14" width="92" height="34" rx="12" fill="{W}" stroke="{Y2}" stroke-width="3"/><path d="M160 48l6 12l-16 -12z" fill="{Y2}"/>'
    + tiles(110, 20, 'LINH', 17, 3), SKY)

if __name__ == '__main__':
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'illus_preview.html'), 'w').write(
        '<body style="display:flex;gap:12px">' + ''.join(f'<div style="width:320px">{a}</div>' for a in (LISTEN, DESK, PAIR)) + '</body>')
