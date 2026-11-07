"""Visual v2 pass (after patch2): S02-style layout CSS, illustrations, homework QR code."""
import io, os, re
import illus01 as A
P = 'dist/S01_embedded.html'
h = open(P, encoding='utf-8').read()
h = h.replace('</style>', open('style_v2.css', encoding='utf-8').read() + '</style>', 1)
for k in ('LISTEN', 'DESK', 'PAIR'):
    assert f'<!--ART:{k}-->' in h, k
    h = h.replace(f'<!--ART:{k}-->', getattr(A, k))
import qrcode, qrcode.image.svg as qs
b = io.BytesIO(); qrcode.make('https://thanh990522.github.io/communication-foundation/homework/?s=S01', image_factory=qs.SvgPathImage, box_size=10, border=1).save(b)
q = b.getvalue().decode(); q = q[q.index('<svg'):]; q = re.sub(r'width="[^"]+" height="[^"]+"', 'class="qr"', q, count=1)
assert '<!--QR-->' in h
h = h.replace('<!--QR-->', q)
open(P, 'w', encoding='utf-8').write(h)
print('visual v2 applied')
