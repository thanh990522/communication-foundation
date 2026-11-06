"""Original flat SVG illustrations for S02 (blue / yellow palette). viewBox 0 0 200 140."""
import math

N, B, B2, SKY, SKY2 = '#0B1F5C', '#1D4ED8', '#2563EB', '#EAF1FF', '#D6E4FF'
Y, Y2, YS, W, G, GR, SK = '#FFC72C', '#FFB000', '#FFF6D6', '#FFFFFF', '#16A34A', '#94A3B8', '#F6C9A0'


def svg(body, bg=SKY):
    return (f'<svg viewBox="0 0 200 140" xmlns="http://www.w3.org/2000/svg" role="img">'
            f'<rect width="200" height="140" rx="18" fill="{bg}"/>{body}</svg>')


def clock(cx, cy, r, h, m, face=W, rim=N):
    ah = math.radians((h % 12 + m / 60) * 30 - 90); am = math.radians(m * 6 - 90)
    ticks = ''.join(f'<line x1="{cx + (r - 3) * math.cos(math.radians(k * 30)):.1f}" y1="{cy + (r - 3) * math.sin(math.radians(k * 30)):.1f}" '
                    f'x2="{cx + (r - 7) * math.cos(math.radians(k * 30)):.1f}" y2="{cy + (r - 7) * math.sin(math.radians(k * 30)):.1f}" stroke="{rim}" stroke-width="2"/>' for k in range(12))
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{face}" stroke="{rim}" stroke-width="4"/>{ticks}'
            f'<line x1="{cx}" y1="{cy}" x2="{cx + r * .5 * math.cos(ah):.1f}" y2="{cy + r * .5 * math.sin(ah):.1f}" stroke="{rim}" stroke-width="4" stroke-linecap="round"/>'
            f'<line x1="{cx}" y1="{cy}" x2="{cx + r * .75 * math.cos(am):.1f}" y2="{cy + r * .75 * math.sin(am):.1f}" stroke="{B}" stroke-width="3" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="3" fill="{Y2}"/>')


def sun(cx, cy, r):
    rays = ''.join(f'<line x1="{cx + (r + 5) * math.cos(math.radians(a)):.1f}" y1="{cy + (r + 5) * math.sin(math.radians(a)):.1f}" '
                   f'x2="{cx + (r + 13) * math.cos(math.radians(a)):.1f}" y2="{cy + (r + 13) * math.sin(math.radians(a)):.1f}" stroke="{Y2}" stroke-width="4" stroke-linecap="round"/>' for a in range(0, 360, 45))
    return rays + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{Y}"/>'


def moon(cx, cy, r, cut=SKY):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{Y}"/><circle cx="{cx + r * .45}" cy="{cy - r * .35}" r="{r * .85}" fill="{cut}"/>'


def star(x, y, s=5, c=Y):
    return f'<path d="M{x} {y - s}L{x + s * .3} {y - s * .3}L{x + s} {y}L{x + s * .3} {y + s * .3}L{x} {y + s}L{x - s * .3} {y + s * .3}L{x - s} {y}L{x - s * .3} {y - s * .3}Z" fill="{c}"/>'


def tick(x, y, s=1, c=W, w=4):
    return f'<path d="M{x} {y}l{5 * s} {5 * s}l{10 * s} {-11 * s}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


def cup(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-6 0q-4 -10 2 -18q6 -8 0 -16M8 0q-4 -10 2 -18q6 -8 0 -16" fill="none" stroke="{GR}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M-18 6h44l-5 38q-1 8 -9 8h-16q-8 0 -9 -8z" fill="{B}"/>'
            f'<path d="M26 14q14 0 12 12q-2 10 -15 9" fill="none" stroke="{B}" stroke-width="5"/>'
            f'<rect x="-24" y="52" width="56" height="6" rx="3" fill="{N}"/>'
            f'<rect x="-10" y="20" width="18" height="12" rx="3" fill="{Y}"/></g>')


def bus(x, y, s=1, c=Y):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="0" y="0" width="110" height="50" rx="12" fill="{c}"/>'
            f'<rect x="0" y="34" width="110" height="8" fill="{Y2 if c == Y else N}"/>'
            + ''.join(f'<rect x="{8 + k * 24}" y="8" width="18" height="18" rx="4" fill="{SKY}"/>' for k in range(4)) +
            f'<rect x="98" y="8" width="10" height="26" rx="3" fill="{SKY}"/>'
            f'<circle cx="26" cy="50" r="10" fill="{N}"/><circle cx="26" cy="50" r="4" fill="{GR}"/>'
            f'<circle cx="86" cy="50" r="10" fill="{N}"/><circle cx="86" cy="50" r="4" fill="{GR}"/></g>')


def house(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 22L22 4L44 22V50H0Z" fill="{W}" stroke="{N}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M-4 24L22 2L48 24" fill="none" stroke="{B}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<rect x="16" y="30" width="12" height="20" rx="2" fill="{Y}"/></g>')


def office(x, y, s=1, lit=Y, wall=W):
    win = ''.join(f'<rect x="{8 + c * 14}" y="{10 + r * 15}" width="9" height="9" rx="2" fill="{lit if (r + c) % 3 else SKY2}"/>' for r in range(4) for c in range(3))
    return f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="0" width="52" height="74" rx="4" fill="{wall}" stroke="{N}" stroke-width="3"/>{win}</g>'


def laptop(x, y, s=1, screen=SKY):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="0" width="70" height="46" rx="5" fill="{N}"/>'
            f'<rect x="5" y="5" width="60" height="36" rx="2" fill="{screen}"/>'
            f'<path d="M-10 48h90l-6 8h-78z" fill="{B}"/></g>')


def calendar(x, y, w, filled, col=B, labels='MTWTFSS', fillmark='tick'):
    cw = w / 7; h = cw * 1.9
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h + 14}" rx="9" fill="{W}" stroke="{N}" stroke-width="3"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="9" fill="{N}"/><rect x="{x}" y="{y + 8}" width="{w}" height="6" fill="{N}"/>']
    for k in range(7):
        cx = x + cw * k + cw / 2
        out.append(f'<text x="{cx:.1f}" y="{y + 30}" font-size="{cw * .42:.1f}" font-weight="800" fill="{N}" text-anchor="middle" font-family="Be Vietnam Pro,sans-serif">{labels[k]}</text>')
        on = k in filled
        out.append(f'<rect x="{cx - cw * .36:.1f}" y="{y + 36}" width="{cw * .72:.1f}" height="{cw * .72:.1f}" rx="5" fill="{col if on else SKY}"/>')
        if on and fillmark == 'tick':
            out.append(tick(cx - cw * .2, y + 36 + cw * .38, cw / 50, W, 3))
    return ''.join(out)


def plate(x, y):
    return (f'<ellipse cx="{x}" cy="{y}" rx="44" ry="16" fill="{W}" stroke="{N}" stroke-width="3"/>'
            f'<ellipse cx="{x - 10}" cy="{y - 2}" rx="16" ry="7" fill="{W}" stroke="{GR}" stroke-width="2"/><circle cx="{x - 10}" cy="{y - 2}" r="5" fill="{Y}"/>'
            f'<rect x="{x + 6}" y="{y - 12}" width="24" height="18" rx="5" fill="#E9B872" stroke="#B9813A" stroke-width="2"/>')


def bed(x, y):
    return (f'<rect x="{x}" y="{y + 18}" width="110" height="26" rx="6" fill="{B}"/><rect x="{x}" y="{y - 6}" width="12" height="62" rx="4" fill="{N}"/>'
            f'<rect x="{x + 14}" y="{y + 4}" width="30" height="16" rx="7" fill="{W}"/><path d="M{x + 40} {y + 18}q30 -18 70 0z" fill="{Y}"/>'
            f'<rect x="{x + 98}" y="{y + 14}" width="12" height="42" rx="4" fill="{N}"/>')


def zzz(x, y):
    return (f'<text x="{x}" y="{y}" font-size="22" font-weight="900" fill="{B}" font-family="Be Vietnam Pro,sans-serif">Z</text>'
            f'<text x="{x + 16}" y="{y - 14}" font-size="16" font-weight="900" fill="{B2}" font-family="Be Vietnam Pro,sans-serif">z</text>'
            f'<text x="{x + 28}" y="{y - 26}" font-size="12" font-weight="900" fill="{B2}" font-family="Be Vietnam Pro,sans-serif">z</text>')


def badge(x, y, txt, bg=N, fg=Y, fs=15, w=None):
    w = w or len(txt) * fs * .62 + 16
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{fs + 12}" rx="{(fs + 12) / 2}" fill="{bg}"/>'
            f'<text x="{x + w / 2:.1f}" y="{y + fs + 3}" font-size="{fs}" font-weight="900" fill="{fg}" text-anchor="middle" font-family="Be Vietnam Pro,sans-serif">{txt}</text>')


def ground(c=SKY2):
    return f'<rect x="0" y="118" width="200" height="22" fill="{c}"/><rect x="0" y="118" width="200" height="22" rx="0" fill="{c}"/>'


# ------------------------------------------------------------------ word cards (simple, iconic)
WORD = {
    'productive': svg(sun(158, 34, 16) +
                      '<rect x="46" y="20" width="84" height="108" rx="10" fill="#fff" stroke="%s" stroke-width="4"/>' % N +
                      '<rect x="70" y="12" width="36" height="16" rx="5" fill="%s"/>' % B +
                      ''.join(f'<rect x="58" y="{44 + k * 26}" width="18" height="18" rx="4" fill="{G}"/>{tick(61, 53 + k * 26, .8, W, 3)}'
                              f'<rect x="84" y="{49 + k * 26}" width="{36 - k * 6}" height="8" rx="4" fill="{SKY2}"/>' for k in range(3)) +
                      f'<path d="M140 120l16 -22l10 8l16 -26" fill="none" stroke="{B}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
                      f'<path d="M172 78h12v12" fill="none" stroke="{B}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'),
    'commute': svg(ground() + house(10, 66, .95) + office(152, 44, .62) +
                   f'<path d="M34 60q70 -60 136 -24" fill="none" stroke="{B}" stroke-width="3" stroke-dasharray="7 6"/>' +
                   bus(48, 70, .9) + star(100, 22, 6)),
    'shift': svg(moon(160, 32, 18) + star(126, 20, 5) + star(182, 64, 4) +
                 ground() + office(20, 40, .9, Y, W) + clock(118, 76, 32, 4, 0)),
    'break': svg(cup(78, 40, 1.1) + f'<circle cx="150" cy="54" r="26" fill="{N}"/>'
                 f'<rect x="140" y="42" width="7" height="24" rx="2" fill="{Y}"/><rect x="153" y="42" width="7" height="24" rx="2" fill="{Y}"/>', YS),
    'usually': svg(calendar(18, 34, 164, {0, 1, 2, 3, 4, 5}, B) + badge(64, 6, '6 / 7', Y, N, 15, 72), SKY),
    'hardly ever': svg(calendar(18, 34, 164, {2}, B) + badge(64, 6, '1 / 7', N, Y, 15, 72), YS),
    'weekday': svg(calendar(18, 40, 164, {0, 1, 2, 3, 4}, B) +
                   f'<rect x="56" y="8" width="88" height="26" rx="8" fill="{N}"/><text x="100" y="27" font-size="15" font-weight="900" fill="{Y}" text-anchor="middle" font-family="Be Vietnam Pro,sans-serif">MON–FRI</text>'),
    'weekend': svg(calendar(18, 40, 164, {5, 6}, Y2) +
                   f'<rect x="56" y="8" width="88" height="26" rx="8" fill="{Y}"/><text x="100" y="27" font-size="15" font-weight="900" fill="{N}" text-anchor="middle" font-family="Be Vietnam Pro,sans-serif">SAT–SUN</text>', YS),
}

# ------------------------------------------------------------------ phrase cards (little scenes)
PHRASE = {
    'productive': svg(f'<rect x="0" y="0" width="200" height="140" rx="18" fill="{YS}"/>' + sun(40, 84, 22) +
                      f'<rect x="0" y="92" width="200" height="48" fill="{SKY2}"/><rect x="0" y="92" width="200" height="4" fill="{B}"/>' +
                      laptop(96, 46, 1.05, W) + ''.join(f'{tick(110, 60 + k * 11, .55, G, 3)}<rect x="124" y="{56 + k * 11}" width="34" height="5" rx="2.5" fill="{SKY2}"/>' for k in range(3)) +
                      badge(118, 10, '7:00', N, Y, 16, 62), YS),
    'commute': svg(ground() + house(8, 66, .9) + office(150, 44, .62) + bus(46, 72, .88, B) +
                   clock(100, 30, 20, 7, 30) + badge(130, 14, '45 min', Y, N, 13, 62)),
    'shift': svg(f'<rect width="200" height="140" rx="18" fill="{N}"/>' + moon(160, 34, 18, N) + star(120, 22, 4) + star(186, 72, 3) + star(40, 18, 3) +
                 office(26, 40, 1.05, Y, '#1E3A8A') + f'<rect x="0" y="118" width="200" height="22" fill="#132A6B"/>' +
                 badge(88, 92, '4 pm → 12 am', Y, N, 13, 108), N),
    'break': svg(f'<rect x="0" y="104" width="200" height="36" fill="{SKY2}"/>' + laptop(108, 52, .95) + cup(58, 50, .9) +
                 clock(160, 30, 18, 11, 0) + badge(16, 10, '10 min', N, Y, 13, 64), YS),
    'usually': svg(f'<rect x="0" y="100" width="200" height="40" fill="{SKY2}"/>' + laptop(26, 50, 1.0) +
                   clock(150, 56, 32, 9, 0) + badge(124, 102, '9:00', B, W, 16, 54)),
    'hardly ever': svg(plate(92, 96) + cup(160, 54, .62) +
                       f'<circle cx="40" cy="38" r="22" fill="{G}"/>' + tick(29, 38, 1.05, W, 5) + badge(70, 14, 'every day ✓', N, Y, 13, 92), YS),
    'weekday': svg(calendar(12, 44, 132, {0, 1, 2, 3, 4}, B) +
                   f'<g transform="translate(152 70)"><rect x="0" y="10" width="40" height="30" rx="6" fill="{N}"/><rect x="12" y="2" width="16" height="10" rx="3" fill="none" stroke="{N}" stroke-width="4"/><rect x="0" y="22" width="40" height="4" fill="{Y}"/></g>' +
                   badge(14, 10, 'get up at 6', N, Y, 13, 92)),
    'weekend': svg(sun(168, 30, 14) + bed(30, 66) + zzz(100, 66) + badge(14, 10, 'SAT · SUN', Y2, N, 13, 82), YS),
}

# ------------------------------------------------------------------ other slides
LISTEN_ART = svg(
    f'<circle cx="56" cy="62" r="30" fill="{B}"/><circle cx="56" cy="54" r="13" fill="{SK}"/><path d="M34 86q22 -22 44 0" fill="{SK}"/>'
    f'<path d="M43 50q13 -14 26 0" fill="{N}"/>'
    f'<circle cx="144" cy="62" r="30" fill="{Y}"/><circle cx="144" cy="54" r="13" fill="{SK}"/><path d="M122 86q22 -22 44 0" fill="{SK}"/>'
    f'<path d="M128 56q2 -20 16 -18q14 -2 16 18q-2 -10 -16 -10q-14 0 -16 10z" fill="#8B4513"/>' +
    badge(30, 104, 'John', N, W, 14, 52) + badge(118, 104, 'Sarah', N, Y, 14, 52) +
    f'<path d="M86 30q14 -14 28 0" fill="none" stroke="{N}" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M92 38q8 -7 16 0" fill="none" stroke="{N}" stroke-width="4" stroke-linecap="round"/>', SKY)

TALK_ART = svg(
    f'<rect x="20" y="24" width="96" height="58" rx="14" fill="{B}"/><path d="M40 82l-6 18l22 -18z" fill="{B}"/>'
    f'<rect x="34" y="40" width="68" height="7" rx="3.5" fill="{W}"/><rect x="34" y="56" width="46" height="7" rx="3.5" fill="{SKY2}"/>'
    f'<rect x="96" y="58" width="86" height="52" rx="14" fill="{Y}"/><path d="M160 110l8 16l-22 -16z" fill="{Y}"/>'
    f'<rect x="110" y="72" width="58" height="7" rx="3.5" fill="{N}"/><rect x="110" y="88" width="38" height="7" rx="3.5" fill="#B07800"/>', YS)

ICON = {k: WORD[k] for k in WORD}

if __name__ == '__main__':
    import os
    html = '<html><body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:12px;padding:12px;background:#fff">'
    for d in (WORD, PHRASE):
        for k, v in d.items(): html += f'<div><div style="font:700 14px sans-serif">{k}</div>{v}</div>'
    html += f'<div>{LISTEN_ART}</div><div>{TALK_ART}</div></body></html>'
    open(os.path.join(os.path.dirname(__file__), 'illus_preview.html'), 'w').write(html)
