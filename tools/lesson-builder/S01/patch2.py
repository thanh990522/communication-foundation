import re
P='dist/S01_embedded.html'
h=open(P,encoding='utf-8').read()
def rep(a,b):
    global h; assert a in h, a[:80]; h=h.replace(a,b)
css,rest=h.split('</style>',1)
# --- font scale-up (CSS + inline styles) ---
def bump(m):
    n=float(m.group(1))
    if n<=12.5: v=15
    elif n<=13.5: v=16
    elif n<=14.5: v=17
    elif n<=15.5: v=18
    elif n<=16.5: v=19
    elif n<=17: v=20
    elif n<=18: v=21
    else: return m.group(0)
    return f'font-size:{v}px'
css=re.sub(r'font-size:\s*([\d.]+)px',bump,css)
head,body=rest.split('<script>',1)
head=re.sub(r'font-size:\s*([\d.]+)px',bump,head)
js,tail=body.split('</script>',1)
js=re.sub(r'font-size:\s*([\d.]+)px',bump,js)
h=css+'</style>'+head+'<script>'+js+'</script>'+tail
# --- layout vars: content centred, decoration at screen edges ---
rep(".slide{position:absolute;inset:0;padding:40px 60px 58px;",".slide{position:absolute;inset:0;padding:calc(36px + var(--oy,0px)) calc(56px + var(--ox,0px)) calc(56px + var(--oy,0px));")
rep(".s-foot{position:absolute;left:60px;right:60px;bottom:18px;",".s-foot{position:absolute;left:calc(56px + var(--ox,0px));right:calc(56px + var(--ox,0px));bottom:calc(16px + var(--oy,0px));")
rep(".badges{position:absolute;top:44px;right:60px;",".badges{position:absolute;top:calc(40px + var(--oy,0px));right:calc(56px + var(--ox,0px));")
rep(".cloud{position:absolute;right:50px;top:110px;",".cloud{position:absolute;right:calc(50px + var(--ox,0px));top:calc(110px + var(--oy,0px));")
extra='''
#toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(20px);background:var(--navy);color:#fff;font-weight:700;font-size:16px;padding:12px 18px;border-radius:12px;box-shadow:var(--shadow);opacity:0;pointer-events:none;transition:.25s;z-index:90;max-width:90vw;text-align:center}
#toast.show{opacity:1;transform:translateX(-50%)}
.tile .tdl{position:absolute;top:6px;left:6px;padding:1px 6px;font-size:13px;opacity:.75}
.tile:hover .tdl{opacity:1}
.ln .dl{margin-left:auto;flex:none;padding:2px 7px}
.ph .dl,.sym .dl{flex:none;padding:3px 7px}
.acr .bk{flex-direction:column;gap:6px}
.acr .bk .dl{font-size:13px;padding:2px 8px}
.lb+.dl,.play+.dl,.btn+.dl{padding:3px 7px}
'''
rep('</style>',extra+'</style>')
rep('<div id="notesPanel"></div>','<div id="notesPanel"></div>\n<div id="toast"></div>')
h=re.sub(r'\s*<aside class="notes">.*?</aside>','',h,flags=re.S)
h=h.replace('<div id="notesPanel"></div>\n','')
h=re.sub(r'#notesPanel[^\n]*\n','',h)
h=h.replace('<span>Bấm vào chữ cái để nghe · <span class="kbd">←</span> <span class="kbd">→</span> chuyển slide · <span class="kbd">F</span> toàn màn hình</span>','<span>A1 → A2 Communication Accelerator · <b>S01</b></span>')
open(P,'w',encoding='utf-8').write(h)
print('patched', h.count('class="notes"'), h.count('Audio library'), h.count('<section class="slide'))
