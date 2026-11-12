"""Inject the audio policy (no auto-reading; play only on ▶/🔊) + IPA styles into a built lesson page."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
JS = open(os.path.join(HERE, 'audiopolicy.js'), encoding='utf-8').read()
CSS = ('.spk{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;background:#EAF1FF;'
       'border:2px solid #D6E4FF;font-size:15px;cursor:pointer;margin-left:6px;vertical-align:middle;flex:none;line-height:1;user-select:none}'
       '.wchip .spk,.lline .spk,.pair .spk,.kw .spk,.gx .spk,.toc .spk,.fuq .spk{width:22px;height:22px;font-size:11px;border-width:1.5px;margin-left:5px}'
       '.spk:hover{background:#FFC72C;border-color:#FFC72C}.spk.on,.spk.playing{background:#FFC72C}'
       '.fipa{display:block;font-size:.62em;font-weight:700;color:#5B6B8C;font-family:"Segoe UI","Noto Sans",system-ui,sans-serif;letter-spacing:0;margin-top:2px}')
MARK = '<!--audiopolicy-->'


def apply(html):
    if MARK in html: return html
    i = html.rfind('</body>')
    return html[:i] + f'{MARK}<style>{CSS}</style><script>\n{JS}\n</script>\n' + html[i:]


def patch_file(p):
    h = open(p, encoding='utf-8').read(); open(p, 'w', encoding='utf-8').write(apply(h))


if __name__ == '__main__':
    for p in sys.argv[1:]: patch_file(p)
