"""Lesson S08 — Shopping, Sizes, Returns & Refunds.
Language limited to the S08 syllabus plus the clothes words taught on the warm-up slide:
  collocations : fit perfectly · suit you · the correct size · keep the receipt · exchange an item · get a refund ·
                 a damaged product · offer a discount
  frames       : Do you have this in ___? · Can I try it on? · It is too ___ / not ___ enough. · I'd like to exchange/return ___.
  grammar      : too + adjective · adjective + enough · polite return requests
  linkers      : at first · but · because · therefore · instead
  pronunciation: contrastive stress on size/colour · final sounds in receipt and refund
"""

# ---------------------------------------------------------------- warm-up: name the clothes (speed naming)
CLOTHES = [('T-shirt', '👕', '/ˈtiː ʃɜːt/'), ('jeans', '👖', '/dʒiːnz/'), ('dress', '👗', '/dres/'), ('jacket', '🧥', '/ˈdʒækɪt/'),
           ('trainers', '👟', '/ˈtreɪnəz/'), ('cap', '🧢', '/kæp/'), ('scarf', '🧣', '/skɑːf/'), ('socks', '🧦', '/sɒks/'),
           ('shirt', '👔', '/ʃɜːt/'), ('boots', '👢', '/buːts/'), ('gloves', '🧤', '/ɡlʌvz/'), ('shorts', '🩳', '/ʃɔːts/')]

# ---------------------------------------------------------------- input: the fitting room (too / enough)
SIZES = [('XS', "It's much too small.", 'Nó quá nhỏ.'), ('S', "It's too small. It isn't big enough.", 'Nó quá nhỏ. Không đủ rộng.'),
         ('M', 'It fits perfectly!', 'Vừa khít!'), ('L', "It's too big.", 'Nó quá rộng.'), ('XL', "It's much too big.", 'Nó quá rộng.')]
PRICES = [(15, "It's cheap enough. 🙂"), (25, "It's cheap enough. 🙂"), (35, "It's cheap enough. 🙂"), (45, "It's too expensive. It isn't cheap enough."),
          (60, "It's too expensive."), (80, "It's much too expensive!")]
BUDGET = 40

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='fit', w='fit', pos='verb', ipa='/fɪt/', vi='vừa (kích thước)',
         col='fit perfectly', kw='fit', col_vi='vừa khít', ex='These jeans fit perfectly.'),
    dict(k='suit', w='suit', pos='verb', ipa='/suːt/', vi='hợp với (ai)',
         col='suit you', kw='suit', col_vi='hợp với bạn', ex='That blue shirt really suits you.'),
    dict(k='size', w='size', pos='noun', ipa='/saɪz/', vi='kích cỡ',
         col='the correct size', kw='size', col_vi='đúng cỡ', ex="Is this the correct size? I'm a medium."),
    dict(k='receipt', w='receipt', pos='noun', ipa='/rɪˈsiːt/', vi='biên lai, hóa đơn mua hàng',
         col='keep the receipt', kw='receipt', col_vi='giữ biên lai', ex='Keep the receipt. You need it for a refund.'),
    dict(k='exchange', w='exchange', pos='verb', ipa='/ɪksˈtʃeɪndʒ/', vi='đổi (hàng)',
         col='exchange an item', kw='exchange', col_vi='đổi một món hàng', ex='Can I exchange this item for a bigger size?'),
    dict(k='refund', w='refund', pos='noun', ipa='/ˈriːfʌnd/', vi='tiền hoàn lại',
         col='get a refund', kw='refund', col_vi='được hoàn tiền', ex="I'd like to get a refund, please."),
    dict(k='damaged', w='damaged', pos='adjective', ipa='/ˈdæmɪdʒd/', vi='bị hư, bị hỏng',
         col='a damaged product', kw='damaged', col_vi='một sản phẩm bị hỏng', ex="This is a damaged product. There's a hole in it."),
    dict(k='discount', w='discount', pos='noun', ipa='/ˈdɪskaʊnt/', vi='giảm giá',
         col='offer a discount', kw='discount', col_vi='giảm giá', ex='Do you offer a discount for students?'),
]

# ---------------------------------------------------------------- practice: too or enough? (MC rows)
MAPQ = [
    ('The jeans are size 28. I need size 32. They are too ___.', ['small', 'big'], 'small'),
    ("This jacket is £120. I only have £50. It's too ___.", ['expensive', 'cheap'], 'expensive'),
    ('My feet are size 38. These shoes are size 38. They ___ perfectly.', ['fit', 'suit'], 'fit'),
    ("The dress is short. It isn't long ___ for the party.", ['enough', 'too'], 'enough'),
    ('Blue is a great colour on you. It really ___ you.', ['suits', 'fits'], 'suits'),
    ("The T-shirt is only £8. That's cheap ___!", ['enough', 'too'], 'enough'),
]

# ---------------------------------------------------------------- pronunciation: contrastive stress + final sounds
CONTRAST = [  # question, answer with the stressed word in CAPS
    ('Do you want the red one?', 'No, the BLUE one, please.'), ('Is it a small?', "No, it's a MEDIUM."),
    ('Is it twenty pounds?', "No, it's TWELVE pounds."), ('Do you want a refund?', "No, I'd like an EXCHANGE."),
    ('Are they too big?', "No, they're too SMALL."), ('Is the receipt in your bag?', "No, it's in my POCKET."),
]
FINALS = [('receipt', '/rɪˈsiːt/', 'no “p”! · final /t/'), ('refund', '/ˈriːfʌnd/', 'final /d/'), ('damaged', '/ˈdæmɪdʒd/', 'final /dʒd/'),
          ('exchanged', '/ɪksˈtʃeɪndʒd/', 'final /dʒd/'), ('size', '/saɪz/', 'final /z/'), ('fits', '/fɪts/', 'final /ts/')]

# ---------------------------------------------------------------- listening (real recording, linked from the source)
LISTEN = {
    'title': 'Getting a refund — at the shop',
    'source': 'Oxford Online English · “Getting a Refund” listening lesson (A2)',
    'page': 'https://www.oxfordonlineenglish.com/shopping-refund',
    'url': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2021/08/Getting-a-Refund-full.mp3',
    'url_slow': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2021/08/Getting-a-Refund-25pc-slower.mp3',
    'file': 'Listening/S08_listening_getting_a_refund.mp3',
    'dur': 102,
    'names': {},
    'script': [],
    'gist': ('What does the customer want to do?', ['return a fan', 'buy a fan'], 'return a fan'),
    'detail': [
        ('Why is she returning the fan?', ["It's too big.", "It's damaged.", "It's the wrong colour."], "It's too big."),
        ('What has she forgotten?', ['her receipt', 'her bag', 'her card'], 'her receipt'),
        ('Without the receipt, the shop can give her…', ['vouchers', 'cash', 'a card refund'], 'vouchers'),
        ('Can the shop take the fan today and give her money another day?', ['No', 'Yes'], 'No'),
        ('What does she choose in the end?', ['the vouchers', 'to come back another day', 'to keep the fan'], 'the vouchers'),
    ],
    'times': [
        ('She can get a cash or card refund within ___ weeks of her purchase.', ['two', '2']),
        ('Do the vouchers have an expiry date? ___ (yes / no)', ['no']),
        ("The shop can't take the fan because they haven't got anywhere to ___ it.", ['put']),
    ],
}

# ---------------------------------------------------------------- model dialogue (buying jeans)
DIALOGUE = [
    ('A', 'Hello. Can I help you?'),
    ('C', 'Yes, please. Do you have these jeans in a size 32?'),
    ('A', 'Let me check. Yes, we do. Here you are.'),
    ('C', 'Thanks. Can I try them on?'),
    ('A', 'Of course. The fitting room is over there.'),
    ('A', 'How do they fit?'),
    ('C', "At first I thought they were OK, but they're too small. Do you have a bigger size?"),
    ('A', "Sure. Here's a size 34."),
    ('C', 'These fit perfectly! Do you have them in black?'),
    ('A', 'Sorry, we only have them in blue. But blue really suits you.'),
    ('C', 'OK. How much are they?'),
    ('A', "They're forty pounds, but we're offering a twenty per cent discount today, therefore they're thirty-two pounds."),
    ('C', 'Great. Can I return them if there is a problem?'),
    ('A', 'Yes, within thirty days. Please keep the receipt.'),
]
DLG_NAMES = {'A': 'Assistant', 'C': 'Customer'}
DLG_Q = [
    ('Why does he need a bigger size?', ['The jeans are too small.', 'The jeans are too long.'], 'The jeans are too small.'),
    ('Why are the jeans cheaper today?', ['There is a discount.', 'They are damaged.'], 'There is a discount.'),
]
CARD = [('Size that fits', '34', ['34', 'size34', 'thirtyfour']), ('Colour', 'blue', ['blue']),
        ('Price today', '£32', ['32', '£32', '32pounds', 'thirtytwo', 'thirtytwopounds']),
        ('Return within', '30 days', ['30', '30days', 'thirty', 'thirtydays'])]

# ---------------------------------------------------------------- speaking: two linked role-plays (buy → return)
SCENARIOS = [  # emoji, item, size, colour, budget, problem
    ('🧥', 'a jacket', 'medium', 'black', 50, 'The zip is broken.'),
    ('👟', 'trainers', 'size 42', 'white', 60, "They aren't big enough."),
    ('👖', 'jeans', 'size 32', 'blue', 40, "They aren't long enough."),
    ('🧣', 'a scarf', 'one size', 'green', 15, "It's a damaged product. There's a hole in it."),
    ('👕', 'a T-shirt', 'large', 'yellow', 12, "It doesn't suit you."),
    ('👗', 'a dress', 'small', 'red', 45, "It's too big."),
]
COLOURS = ['black', 'white', 'blue', 'green', 'red', 'yellow']

# ---------------------------------------------------------------- real-life task: ask an online shop (chat)
SHOP = {'name': 'Sunny Days Store', 'item': 'Classic denim jacket', 'price': '£45', 'emoji': '🧥'}
BOT = [  # keywords, reply, checklist key
    (['size', 'small', 'medium', 'large', 'big'], 'It comes in small, medium and large. 🙂', 'size'),
    (['colour', 'color', 'black', 'blue', 'white'], 'We have it in blue and black.', 'colour'),
    (['price', 'much', 'cost', 'discount', 'cheap', 'expensive', '£'], "It's £45. This week we're offering a 10% discount, so it's £40.50.", 'price'),
    (['return', 'refund', 'exchange', 'receipt'], 'You can return or exchange it within 30 days. Please keep the receipt.', 'return'),
    (['fit', 'try'], 'Most customers say it fits perfectly. If it doesn’t fit, you can exchange it.', 'size'),
]

# ---------------------------------------------------------------- game: returns desk
POLICY = ['✅ Receipt + within 14 days → refund or exchange', '🧾 No receipt → vouchers only',
          '📅 Receipt + after 14 days → exchange only', '💔 Damaged product + receipt → refund']
OPTIONS = ['Refund or exchange', 'Exchange only', 'Vouchers only', "Refund — it's damaged"]
CASES = [  # emoji, item, problem (said by the customer), receipt?, days, answer index
    ('👕', 'T-shirt', "I'd like to return this T-shirt. It doesn't suit me.", True, 3, 0),
    ('👖', 'jeans', "I'd like to return these jeans. They're too big. Sorry, I don't have the receipt.", False, 2, 2),
    ('👟', 'trainers', "I'd like to exchange these trainers. They aren't big enough.", True, 20, 1),
    ('🧣', 'scarf', "This scarf is a damaged product. There's a hole in it. Here's the receipt.", True, 25, 3),
    ('👗', 'dress', "I'd like to return this dress. I don't like the colour. I don't have the receipt.", False, 30, 2),
    ('🧢', 'cap', "I'd like to return this cap. It's too small. Here's the receipt.", True, 10, 0),
    ('👢', 'boots', "I'd like to return these boots. They're too expensive for me. Here's the receipt.", True, 16, 1),
    ('🧤', 'gloves', "These gloves are damaged, but I don't have the receipt.", False, 5, 2),
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name='Do you have this in…?', q='Do you have this in ___?', vi_q='Bạn có cái này cỡ / màu ___ không?',
         a='Yes, we do. / Sorry, we only have it in ___.', vi_a='Có. / Xin lỗi, chúng tôi chỉ có cỡ / màu ___.',
         model='Do you have this in a medium?',
         answers=[('Yes, we do. Here you are.', 'Có. Của bạn đây.'),
                  ('Sorry, we only have it in small and large.', 'Xin lỗi, chúng tôi chỉ có cỡ nhỏ và lớn.'),
                  ('Let me check. Yes, we have it in blue, too.', 'Để tôi kiểm tra. Có, chúng tôi cũng có màu xanh dương.')],
         tr=[('Bạn có đôi giày này cỡ 40 không?', 'Do you have these shoes in a size 40?'),
             ('Bạn có áo khoác này màu đen không?', 'Do you have this jacket in black?'),
             ('Xin lỗi, chúng tôi chỉ có cỡ vừa.', 'Sorry, we only have it in a medium.')]),
    dict(name='Can I try it on?', q='Can I try it on?', vi_q='Tôi thử nó được không?',
         a='Of course. The fitting room is over there.', vi_a='Tất nhiên. Phòng thử đồ ở đằng kia.',
         model='Can I try it on?',
         answers=[('Of course. The fitting room is over there.', 'Tất nhiên. Phòng thử đồ ở đằng kia.'),
                  ('Sure. How does it fit?', 'Được thôi. Nó có vừa không?'),
                  ('It fits perfectly. It really suits you!', 'Nó vừa khít. Rất hợp với bạn!')],
         tr=[('Tôi thử chiếc váy này được không?', 'Can I try this dress on?'),
             ('Chiếc quần jean này vừa khít.', 'These jeans fit perfectly.'),
             ('Màu đỏ rất hợp với bạn.', 'Red really suits you.')]),
    dict(name="It's too… / not … enough", q="It's too ___. / It isn't ___ enough.", vi_q='Nó quá ___. / Nó không đủ ___.',
         a='Would you like a bigger / smaller size?', vi_a='Bạn có muốn cỡ lớn hơn / nhỏ hơn không?',
         model='How does it fit?',
         answers=[("It's too small. Do you have a bigger size?", 'Nó quá nhỏ. Bạn có cỡ lớn hơn không?'),
                  ("It isn't long enough.", 'Nó không đủ dài.'),
                  ("It's too expensive for me.", 'Nó quá đắt đối với tôi.')],
         tr=[('Đôi giày này quá to.', 'These shoes are too big.'),
             ('Chiếc áo khoác này không đủ ấm.', "This jacket isn't warm enough."),
             ('Nó quá đắt, vì vậy tôi không mua.', "It's too expensive, so I'm not buying it.")]),
    dict(name="I'd like to exchange / return…", q="I'd like to exchange / return ___.", vi_q='Tôi muốn đổi / trả lại ___.',
         a='Do you have the receipt? / You can get a refund.', vi_a='Bạn có biên lai không? / Bạn có thể được hoàn tiền.',
         model='Can I help you?',
         answers=[("I'd like to return this jacket. The zip is broken.", 'Tôi muốn trả lại chiếc áo khoác này. Khóa kéo bị hỏng.'),
                  ("I'd like to exchange these jeans for a bigger size.", 'Tôi muốn đổi chiếc quần jean này lấy cỡ lớn hơn.'),
                  ("It's a damaged product. Can I get a refund?", 'Đây là sản phẩm bị hỏng. Tôi được hoàn tiền không?')],
         tr=[('Tôi muốn đổi chiếc áo sơ mi này lấy màu khác.', "I'd like to exchange this shirt for a different colour."),
             ('Tôi muốn trả lại đôi giày này. Đây là biên lai.', "I'd like to return these shoes. Here's the receipt."),
             ('Tôi có được hoàn tiền không?', 'Can I get a refund?')]),
]

# ---------------------------------------------------------------- grammar box (too / enough)
GRAM = [('too + adjective', 'quá … (có vấn đề)', "It's too big."),
        ('adjective + enough', 'đủ …', "It's cheap enough."),
        ('not + adjective + enough', 'không đủ …', "It isn't long enough.")]

# ---------------------------------------------------------------- returns desk: what the assistant says
DESK_SAY = ['No problem. You can get a refund or exchange it.',
            "Sorry, it's after fourteen days. You can only exchange it.",
            'Sorry, without the receipt we can only offer vouchers.',
            "I'm sorry it's damaged. You can get a refund."]

# ---------------------------------------------------------------- role-play 2 linker frame
LINKERS = [('At first', 'Lúc đầu'), ('but', 'nhưng'), ('because', 'bởi vì'), ('therefore', 'vì vậy'), ('instead', 'thay vào đó')]
