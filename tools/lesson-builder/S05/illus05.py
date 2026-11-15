"""Original flat SVG illustrations for S05 (same palette/helpers as S02–S04) + the shared town map."""
import os, sys, importlib.util
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..', 'S02')); sys.path.insert(0, os.path.join(D, '..', 'S03'))
from illus import svg, star, tick, bus, house, office, badge, N, B, B2, SKY, SKY2, Y, Y2, YS, W, G, GR, SK, LISTEN_ART, TALK_ART  # noqa
from illus03 import person, emo, tree, pin, RED, GREEN, GREEN2  # noqa
_sp = importlib.util.spec_from_file_location('content05', os.path.join(D, 'content.py')); C = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(C)

F = 'font-family="Be Vietnam Pro,sans-serif"'
ROAD, ROAD2, LINE = '#CBD5E1', '#94A3B8', '#FFFFFF'


def txt(x, y, t, s=12, c=N, w=900, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{c}" text-anchor="{anchor}" {F}>{t}</text>'


def road_h(y, x0=0, x1=200, w=30):
    return (f'<rect x="{x0}" y="{y - w / 2}" width="{x1 - x0}" height="{w}" fill="{ROAD}"/>'
            f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="2.5" stroke-dasharray="9 7"/>')


def road_v(x, y0=0, y1=140, w=30):
    return (f'<rect x="{x - w / 2}" y="{y0}" width="{w}" height="{y1 - y0}" fill="{ROAD}"/>'
            f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="{LINE}" stroke-width="2.5" stroke-dasharray="9 7"/>')


def bld(x, y, w, h, c=W, roof=B, label='', ls=10):
    win = ''.join(f'<rect x="{x + 6 + k * 14}" y="{y + 12}" width="8" height="8" rx="2" fill="{SKY2}"/>' for k in range(int((w - 8) // 14)))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{c}" stroke="{N}" stroke-width="2.5"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="7" rx="3" fill="{roof}"/>{win}'
            + (txt(x + w / 2, y + h - 6, label, ls, N) if label else ''))


def car(x, y, c=RED, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="0" width="30" height="14" rx="5" fill="{c}"/>'
            f'<rect x="6" y="-7" width="17" height="9" rx="3" fill="{c}"/><rect x="8" y="-5" width="13" height="6" rx="2" fill="{SKY}"/>'
            f'<circle cx="8" cy="14" r="4" fill="{N}"/><circle cx="22" cy="14" r="4" fill="{N}"/></g>')


def walker(x, y, s=1, c=B):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-30" r="7" fill="{SK}"/>'
            f'<path d="M0 -22v18M0 -18l-9 9M0 -18l9 6M0 -4l-8 16M0 -4l8 16" stroke="{c}" stroke-width="5" stroke-linecap="round" fill="none"/></g>')


def light(x, y):
    return (f'<rect x="{x}" y="{y}" width="12" height="30" rx="4" fill="{N}"/><circle cx="{x + 6}" cy="{y + 7}" r="3.5" fill="{RED}"/>'
            f'<circle cx="{x + 6}" cy="{y + 15}" r="3.5" fill="{Y}"/><circle cx="{x + 6}" cy="{y + 23}" r="3.5" fill="{GREEN}"/><rect x="{x + 5}" y="{y + 30}" width="2" height="16" fill="{N}"/>')


def museum(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 22L40 0L80 22Z" fill="{Y}" stroke="{N}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<rect x="4" y="22" width="72" height="6" fill="{W}" stroke="{N}" stroke-width="2"/>'
            + ''.join(f'<rect x="{9 + k * 15}" y="28" width="7" height="30" fill="{W}" stroke="{N}" stroke-width="2"/>' for k in range(5)) +
            f'<rect x="0" y="58" width="80" height="7" fill="{W}" stroke="{N}" stroke-width="2"/></g>')


def dash(x1, y1, x2, y2, c=B, w=3.5):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{c}" stroke-width="{w}" stroke-dasharray="6 6" stroke-linecap="round" fill="none"/>'


def arr(d, c=B, w=6):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'


# ------------------------------------------------------------------ word cards
WORD = {
    'landmark': svg(f'<rect x="0" y="112" width="200" height="28" fill="{SKY2}"/>' + museum(60, 44, 1) + star(150, 30, 7) + pin(48, 60, RED, .8)
                    + badge(110, 112, 'FAMOUS', N, Y, 11, 60)),
    'intersection': svg(road_h(70, 0, 200, 34) + road_v(100, 0, 140, 34) + f'<rect x="83" y="53" width="34" height="34" fill="{ROAD}"/>'
                        + light(132, 14) + car(20, 76, RED, .9) + car(108, 18, B, .9)),
    'block': svg(road_h(96, 0, 200, 26) + bld(10, 20, 54, 62) + bld(73, 20, 54, 62, W, Y2) + bld(136, 20, 54, 62)
                 + road_v(68, 20, 110, 8) + road_v(131, 20, 110, 8) + txt(37, 128, '1', 14, B) + txt(100, 128, '2', 14, B)
                 + arr('M18 96H170M160 88L170 96L160 104', Y2, 4), YS),
    'entrance': svg(bld(36, 20, 128, 104, W, B) + f'<rect x="84" y="78" width="32" height="46" rx="3" fill="{Y}" stroke="{N}" stroke-width="2.5"/>'
                    + badge(58, 50, 'ENTRANCE', G, W, 12, 84) + arr('M100 136V128', G, 4)),
    'across from': svg(road_h(70, 0, 200, 30) + bld(20, 6, 58, 46, W, B, 'BANK', 10) + bld(122, 92, 58, 42, W, G, 'LIBRARY', 9)
                       + arr('M100 34V106M92 44L100 34L108 44M92 96L100 106L108 96', Y2, 4.5)),
    'on the corner': svg(road_h(96, 0, 200, 30) + road_v(84, 0, 140, 30) + bld(108, 18, 70, 58, W, Y2, 'CAFÉ', 11)
                         + f'<circle cx="106" cy="78" r="16" fill="none" stroke="{RED}" stroke-width="4"/>'),
    'within walking distance': svg(f'<rect x="0" y="104" width="200" height="36" fill="{SKY2}"/>' + house(14, 54, 1) + dash(66, 98, 140, 98, B)
                                   + walker(100, 98, 1, B) + bld(146, 52, 44, 52, W, G) + badge(70, 14, '5 min 🚶', N, Y, 13, 84)),
    'get to': svg(f'<rect x="0" y="104" width="200" height="36" fill="{SKY2}"/>' + walker(36, 98, 1, B) + dash(54, 92, 120, 70, B)
                  + bld(124, 44, 66, 60, W, RED, 'STATION', 10) + pin(156, 40, RED, .8)),
}

# ------------------------------------------------------------------ collocation scenes
PHRASE = {
    'landmark': svg(f'<rect x="0" y="104" width="200" height="36" fill="{GREEN}" fill-opacity=".35"/>' + museum(64, 30, 1.05)
                    + person(30, 84, Y, N, .55) + person(170, 86, B2, '#8B4513', .55, True, True)
                    + f'<rect x="156" y="70" width="14" height="10" rx="2" fill="{N}"/>' + star(30, 22, 6) + star(176, 26, 5), YS),
    'intersection': svg(road_h(70, 0, 200, 40) + road_v(100, 0, 140, 40) + f'<rect x="80" y="50" width="40" height="40" fill="{ROAD}"/>'
                        + ''.join(f'<rect x="{82 + k * 8}" y="92" width="5" height="12" fill="{W}"/>' for k in range(5))
                        + car(6, 74, RED) + car(40, 50, Y2) + car(140, 76, G) + car(84, 6, B) + car(108, 112, N) + light(150, 10)),
    'block': svg(road_h(110, 0, 200, 22) + bld(8, 26, 56, 70) + bld(72, 26, 56, 70, W, Y2) + bld(136, 26, 56, 70)
                 + walker(30, 118, .7, B) + arr('M44 110H180M170 102L180 110L170 118', B, 4) + badge(60, 4, 'walk two blocks', N, Y, 11, 104), YS),
    'entrance': svg(bld(20, 30, 160, 96, W, N) + f'<rect x="80" y="74" width="40" height="52" rx="3" fill="{Y}" stroke="{N}" stroke-width="2.5"/>'
                    + f'<rect x="24" y="44" width="152" height="20" rx="6" fill="{B}"/>' + txt(100, 59, 'MAIN ENTRANCE', 12, W)
                    + person(150, 100, G, N, .45) + arr('M100 136V128', RED, 4)),
    'across from': svg(road_h(70, 0, 200, 30) + bld(14, 6, 70, 46, W, B, 'BANK', 11) + bld(116, 92, 70, 42, W, G, 'LIBRARY', 10)
                       + bld(116, 6, 70, 46, W, GR, '', 10) + pin(150, 92, RED, .8) + txt(56, 120, 'across from', 12, B2)),
    'on the corner': svg(road_h(96, 0, 200, 30) + road_v(84, 0, 140, 30) + bld(106, 14, 80, 62, W, Y2, 'CAFÉ', 11)
                         + f'<rect x="20" y="26" width="58" height="18" rx="4" fill="{G}"/>' + txt(49, 39, 'High St', 10, W)
                         + f'<rect x="47" y="44" width="4" height="40" fill="{N}"/>' + pin(110, 82, RED, .7)),
    'within walking distance': svg(f'<rect x="0" y="104" width="200" height="36" fill="{SKY2}"/>' + house(10, 54, .9) + walker(70, 100, .9, G)
                                   + dash(82, 98, 146, 98, G) + bld(148, 44, 44, 60, W, RED, '🏥', 14) + badge(64, 12, '10 minutes on foot', G, W, 11, 112), YS),
    'get to': svg(f'<rect x="0" y="108" width="200" height="32" fill="{SKY2}"/>' + bld(96, 30, 96, 78, W, RED, 'STATION', 12)
                  + f'<rect x="170" y="62" width="16" height="26" fill="{Y}" stroke="{N}" stroke-width="2"/>' + person(40, 64, B, N, .75)
                  + f'<path d="M52 30q20 -18 40 -4" fill="none" stroke="{GR}" stroke-width="2"/>' + txt(60, 20, 'How do I get to…?', 10, B2)),
}

# ------------------------------------------------------------------ direction-basics icons (120 x 84)
def ic(body):
    return f'<svg viewBox="0 0 120 84" xmlns="http://www.w3.org/2000/svg" role="img"><rect width="120" height="84" rx="14" fill="{SKY}"/>{body}</svg>'


BASIC_ICON = {
    'L': ic(road_v(70, 0, 84, 26) + road_h(30, 0, 70, 26) + arr('M70 76V32H22M32 22L22 32L32 42', B)),
    'R': ic(road_v(50, 0, 84, 26) + road_h(30, 50, 120, 26) + arr('M50 76V32H98M88 22L98 32L88 42', B)),
    'S': ic(road_v(60, 0, 84, 30) + arr('M60 78V12M50 22L60 12L70 22', B)),
    'P': ic(road_v(46, 0, 84, 24) + bld(70, 22, 38, 38, W, Y2) + arr('M46 78V10M36 20L46 10L56 20', B) + f'<circle cx="46" cy="41" r="6" fill="{Y2}"/>'),
    'X': ic(road_h(42, 0, 120, 40) + ''.join(f'<rect x="{38 + k * 10}" y="24" width="6" height="36" fill="{W}"/>' for k in range(5))
            + walker(60, 78, .55, N) + arr('M90 64V22M82 30L90 22L98 30', B, 4)),
    'F': ic(road_v(80, 0, 84, 22) + road_h(56, 0, 80, 16) + road_h(20, 0, 80, 16) + arr('M80 80V56H26M36 48L26 56L36 64', B, 5) + txt(14, 62, '1', 12, RED) + txt(14, 26, '2', 12, GR)),
    'N': ic(bld(16, 22, 40, 46, W, B, 'BANK', 8) + bld(64, 22, 40, 46, W, G, 'POST', 8) + arr('M36 78H84', Y2, 4)),
    'B': ic(bld(6, 26, 34, 42, W, B) + bld(43, 26, 34, 42, W, G) + bld(80, 26, 34, 42, W, B) + arr('M60 14V22', RED, 4) + f'<circle cx="60" cy="10" r="5" fill="{RED}"/>'),
}

# ------------------------------------------------------------------ the town map (700 x 460)
V = [(150, 'Station Road'), (350, 'Market Street'), (550, 'Church Street')]
H = [(110, 'Park Road'), (250, 'High Street'), (390, 'River Road')]
COL = {'park': (GREEN, GREEN2), 'library': ('#E0E7FF', B), 'bank': ('#DBEAFE', B), 'post': ('#FEE2E2', RED), 'bookshop': ('#FEF3C7', Y2),
       'museum': ('#FEF9C3', Y2), 'cinema': ('#EDE9FE', '#7C3AED'), 'school': ('#FFEDD5', '#EA580C'), 'pharmacy': ('#DCFCE7', GREEN2),
       'supermarket': ('#E0F2FE', '#0284C7'), 'cafe': ('#FCE7F3', '#DB2777'), 'hospital': ('#FFFFFF', RED), 'hotel': ('#F1F5F9', N),
       'station': ('#E2E8F0', N)}


def town_map(mid, marker=False, clickable=True, entrance=True):
    o = [f'<svg class="town" id="{mid}" viewBox="0 0 700 460" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Town map">',
         f'<rect width="700" height="460" rx="18" fill="#F1F5E9"/>']
    for y, _ in H: o.append(f'<rect x="0" y="{y - 18}" width="700" height="36" fill="{ROAD}"/>')
    for x, _ in V: o.append(f'<rect x="{x - 18}" y="0" width="36" height="460" fill="{ROAD}"/>')
    for y, _ in H:
        for a, b in ((0, 132), (168, 332), (368, 532), (568, 700)): o.append(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="#fff" stroke-width="2.5" stroke-dasharray="10 8"/>')
    for x, _ in V:
        for a, b in ((0, 92), (128, 232), (268, 372), (408, 460)): o.append(f'<line x1="{x}" y1="{a}" x2="{x}" y2="{b}" stroke="#fff" stroke-width="2.5" stroke-dasharray="10 8"/>')
    # street names
    for y, n in H: o.append(txt(450 if y != 390 else 460, y + 5, n.upper(), 11.5, '#475569', 900))
    for x, n in V: o.append(f'<text transform="translate({x + 4} {60 if x != 150 else 330}) rotate(-90)" font-size="11.5" font-weight="900" fill="#475569" text-anchor="middle" {F}>{n.upper()}</text>')
    for pid, (label, em, x0, y0, x1, y1) in C.PLACES.items():
        fill, roof = COL[pid]; w, h = x1 - x0, y1 - y0
        g = [f'<g class="pl{" click" if clickable else ""}" data-place="{pid}">',
             f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{N}" stroke-width="2.2"/>',
             f'<rect x="{x0}" y="{y0}" width="{w}" height="6" rx="3" fill="{roof}"/>']
        if pid == 'park': g += [tree(x0 + 22, y0 + 36, .7), tree(x1 - 22, y0 + 40, .7)]
        words = label.split() if (w < 60 and ' ' in label) else [label]
        fs = min(12.5, max(w - 6, 20) / (max(len(x) for x in words) * .62))
        cy = y0 + h / 2 - (len(words) - 1) * 6
        g.append(emo(x0 + w / 2, cy - 4 if h > 50 else y0 + 18, em, 17 if h > 44 else 14))
        for k, wd in enumerate(words):
            g.append(txt(x0 + w / 2, (cy + 18 if h > 50 else y0 + h - 6) + k * 12, wd, fs, N))
        g.append('</g>')
        o += g
    if entrance:
        o.append(f'<rect x="440" y="219" width="20" height="7" fill="{Y2}" stroke="{N}" stroke-width="1.5"/>'
                 + txt(450, 214, 'MAIN ENTRANCE', 8.5, '#92400E'))
    sx, sy = C.START
    o.append(f'<g class="you"><circle cx="{sx}" cy="{sy}" r="11" fill="{Y}" stroke="{N}" stroke-width="2.5"/>' + txt(sx, sy + 4.5, '★', 12, N)
             + f'<rect x="{sx + 14}" y="{sy - 10}" width="76" height="20" rx="10" fill="{N}"/>' + txt(sx + 52, sy + 4, 'YOU ARE HERE', 8.5, Y) + '</g>')
    if marker:
        o.append(f'<path class="trail" d="M{sx} {sy}" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 10"/>'
                 f'<g class="mk" transform="translate({sx} {sy})"><circle r="13" fill="{RED}" stroke="{W}" stroke-width="3"/>{walker(0, 10, .42, W)}</g>')
    o.append('</svg>')
    return ''.join(o)


ART = {'LISTEN': LISTEN_ART, 'TALK': TALK_ART}

if __name__ == '__main__':
    h = '<body style="margin:0;display:grid;grid-template-columns:repeat(4,300px);gap:10px;padding:10px">'
    for d in (WORD, PHRASE):
        for k, v in d.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    for k, v in BASIC_ICON.items(): h += f'<div><b style="font:700 13px sans-serif">{k}</b>{v}</div>'
    h += f'<div style="grid-column:span 4">{town_map("m", True)}</div></body>'
    open(os.path.join(D, 'illus_preview.html'), 'w').write(h)
