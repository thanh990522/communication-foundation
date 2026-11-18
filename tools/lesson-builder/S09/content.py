"""Lesson S09 — Everyday Services & Polite Requests.
Language limited to the S09 syllabus (+ simple A1 words already known):
  collocations : check the delivery status · book a repair service · report an issue · contact customer service ·
                 request a replacement · pay an extra charge · be available · confirm the details
  frames       : I'm calling about ___. · There seems to be a problem with ___. · Could you check ___ for me? · What are my options?
  grammar      : could / would for polite requests · there seems to be
  linkers      : first · because · therefore · if possible · finally
  pronunciation: polite intonation · sentence stress on the problem and the requested action
"""

# ---------------------------------------------------------------- warm-up: who do you call?
SERVICES = [('D', '🚚', 'Delivery company'), ('R', '🔧', 'Repair service'), ('C', '☎️', 'Customer service')]
PROBLEMS = [
    ('📦', "My order is three days late.", 'D'),
    ('🫧', "My washing machine doesn't work.", 'R'),
    ('👕', 'I got the wrong colour.', 'C'),
    ('📱', 'My phone screen is broken.', 'R'),
    ('🏠', 'The driver went to the wrong address.', 'D'),
    ('💳', 'I paid two times for one order.', 'C'),
    ('❄️', "My fridge isn't cold.", 'R'),
    ('🚪', "I wasn't at home. Where is my parcel?", 'D'),
]

# ---------------------------------------------------------------- input: the shape of a service call
CALL = [  # stage, linker, line, vi
    ('Hello', '', "Hello. My name is Linh. I'm calling about my order.", 'Xin chào. Tôi tên Linh. Tôi gọi về đơn hàng của tôi.'),
    ('Problem', 'First', 'First, there seems to be a problem with the delivery. It is five days late.', 'Trước tiên, có vẻ như có vấn đề với việc giao hàng. Nó trễ năm ngày.'),
    ('Why', 'because', "I need it this week because it's a birthday present.", 'Tôi cần nó trong tuần này vì nó là quà sinh nhật.'),
    ('Request', 'if possible', 'Could you check the delivery status for me, if possible?', 'Bạn có thể kiểm tra tình trạng giao hàng giúp tôi được không, nếu có thể?'),
    ('Options', 'therefore', "It's lost? Therefore, what are my options?", 'Nó bị thất lạc à? Vì vậy, tôi có những lựa chọn nào?'),
    ('Confirm', 'Finally', "Finally, could you confirm the details? A new one on Friday, and no extra charge.", 'Cuối cùng, bạn có thể xác nhận lại thông tin không? Một cái mới vào thứ Sáu, và không có phí thêm.'),
]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='delivery', w='delivery', pos='noun', ipa='/dɪˈlɪvəri/', vi='sự giao hàng',
         col='check the delivery status', kw='delivery', col_vi='kiểm tra tình trạng giao hàng', ex='Could you check the delivery status for me?'),
    dict(k='repair', w='repair', pos='noun', ipa='/rɪˈpeə(r)/', vi='sự sửa chữa',
         col='book a repair service', kw='repair', col_vi='đặt dịch vụ sửa chữa', ex="I'd like to book a repair service for my fridge."),
    dict(k='issue', w='issue', pos='noun', ipa='/ˈɪʃuː/', vi='vấn đề',
         col='report an issue', kw='issue', col_vi='báo cáo một vấn đề', ex="I'm calling to report an issue with my internet."),
    dict(k='customer service', w='customer service', pos='noun', ipa='/ˌkʌstəmə ˈsɜːvɪs/', vi='bộ phận chăm sóc khách hàng',
         col='contact customer service', kw='customer service', col_vi='liên hệ chăm sóc khách hàng', ex='Please contact customer service if there is a problem.'),
    dict(k='replacement', w='replacement', pos='noun', ipa='/rɪˈpleɪsmənt/', vi='sản phẩm thay thế',
         col='request a replacement', kw='replacement', col_vi='yêu cầu sản phẩm thay thế', ex='The box was damaged, so I want to request a replacement.'),
    dict(k='charge', w='charge', pos='noun', ipa='/tʃɑːdʒ/', vi='khoản phí',
         col='pay an extra charge', kw='charge', col_vi='trả thêm phí', ex='Do I need to pay an extra charge?'),
    dict(k='available', w='available', pos='adjective', ipa='/əˈveɪləbl/', vi='có sẵn, rảnh',
         col='be available', kw='available', col_vi='có mặt / rảnh', ex='Are you available on Friday morning?'),
    dict(k='confirm', w='confirm', pos='verb', ipa='/kənˈfɜːm/', vi='xác nhận',
         col='confirm the details', kw='confirm', col_vi='xác nhận thông tin', ex='Could you confirm the details, please?'),
]

# ---------------------------------------------------------------- grammar input
THERE = [  # direct -> softer "there seems to be"
    ('My laptop is broken.', 'There seems to be a problem with my laptop.'),
    ('You sent the wrong item.', 'There seems to be a problem with my order.'),
    ('The bill is wrong.', 'There seems to be an extra charge on my bill.'),
    ('The internet is not working.', 'There seems to be an issue with my internet.'),
]
POLITE = [  # three versions; the most polite answer
    (['Check my order.', 'Can you check my order?', 'Could you check my order for me, please?'], 2),
    (['Would you confirm the details, please?', 'Confirm the details.', 'Confirm the details now!'], 0),
    (['I want a replacement.', 'Give me a replacement.', 'Could I request a replacement, please?'], 2),
    (['Send a repair person tomorrow.', 'Would you book a repair service for tomorrow, if possible?', 'Repair it tomorrow.'], 1),
]
GRAM = [('Could you + verb…?', 'Bạn có thể … được không?', 'Could you check the delivery status for me?'),
        ('Would you + verb…?', 'Bạn vui lòng … được không?', 'Would you confirm the details, please?'),
        ('There seems to be + noun', 'Có vẻ như có …', 'There seems to be a problem with my order.')]

# ---------------------------------------------------------------- pronunciation: sentence stress (stressed words in CAPS)
STRESS = [
    "There seems to be a PROBLEM with my FRIDGE.",
    "Could you CHECK the DELIVERY for me?",
    "I'd like to BOOK a REPAIR.",
    "My ORDER is three days LATE.",
    "Could you CONFIRM the DETAILS, please?",
    "I'd like to REQUEST a REPLACEMENT.",
]

# ---------------------------------------------------------------- listening (real recording, played from the source)
LISTEN = {
    'title': 'Computer problems — at a repair service',
    'source': 'Oxford Online English · “Computer Problems” listening lesson',
    'page': 'https://www.oxfordonlineenglish.com/computer-problems',
    'url': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2015/01/PC-Problems_vbr9.mp3',
    'url_slow': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2021/03/Computer-Problems-slower.mp3',
    'dur': 65,
    'gloss': '🆕 fix = sửa · anti-virus program = phần mềm diệt virus · pick it up = đến lấy',
    'gist': ('Where is the woman?', ['at a computer repair service', 'at a bank'], 'at a computer repair service'),
    'detail': [
        ('What is the problem with her computer?', ["It's very slow.", "It doesn't turn on.", 'The screen is broken.'], "It's very slow."),
        ('What did she turn off?', ['her anti-virus programs', 'her computer', 'her phone'], 'her anti-virus programs'),
        ('How much is the repair if it is simple?', ['£100', '£200', '£50'], '£100'),
        ('How much is it if they have to reformat the computer?', ['£200', '£100', '£300'], '£200'),
        ('Does she want to think it over?', ['No — she needs it fixed.', 'Yes — she wants to think.'], 'No — she needs it fixed.'),
    ],
    'times': [
        ('And how much will you ___ to fix it?', ['charge']),
        ('So when can I ___ it up?', ['pick']),
        ("We'll call you in the next couple of ___.", ['days']),
    ],
}

# ---------------------------------------------------------------- model dialogue: calling customer service
DIALOGUE = [
    ('A', 'Good morning. Customer service. How can I help you?'),
    ('C', "Hello. I'm calling about my order. The order number is 4-7-2-9."),
    ('A', 'Thank you. What seems to be the problem?'),
    ('C', 'First, the delivery was two days late. And there seems to be a problem with the coffee machine. The box is damaged and it doesn\'t work.'),
    ('A', "I'm very sorry about that. Let me check… Yes, I can see your order."),
    ('C', 'What are my options?'),
    ('A', 'You can get a refund, or we can send a replacement.'),
    ('C', "I'd like to request a replacement, because I use it every day. Do I need to pay an extra charge?"),
    ('A', "No, there's no extra charge. Are you available on Friday morning?"),
    ('C', 'Yes, I am. Could you deliver it before ten, if possible?'),
    ('A', 'Sure. Therefore, the driver will come between eight and ten.'),
    ('C', 'Great. Finally, could you confirm the details, please?'),
    ('A', 'Of course. A new coffee machine, on Friday morning, between eight and ten, with no extra charge.'),
    ('C', 'Perfect. Thank you for your help!'),
]
DLG_NAMES = {'A': 'Agent', 'C': 'Customer'}
DLG_Q = [
    ('What two problems does the customer report?', ['late delivery + damaged machine', 'wrong colour + extra charge'], 'late delivery + damaged machine'),
    ('Why does she want a replacement?', ['She uses it every day.', 'She wants a cheaper one.'], 'She uses it every day.'),
]
CARD = [('Order number', '4729', ['4729', '4-7-2-9']), ('Solution', 'replacement', ['replacement', 'areplacement', 'newone', 'anewone']),
        ('Day', 'Friday', ['friday', 'fridaymorning']), ('Extra charge', 'no', ['no', 'none', 'noextracharge', '0', '£0', 'nothing'])]

# ---------------------------------------------------------------- speaking: 2-minute service call (caller card + agent screen)
CALLS = [  # emoji, caller problem, what caller wants, agent options, charge note
    ('📦', 'Your new headphones are five days late.', 'You need them this week for a trip.', ['Send them by express on Thursday', 'Give a refund'], 'Express delivery: no extra charge'),
    ('🔧', "Your washing machine doesn't work. It is one year old.", 'You want a repair this week.', ['Repair on Wednesday morning', 'Repair on Saturday'], 'Saturday repair: £20 extra charge'),
    ('📱', 'Your new phone arrived. The screen is broken.', 'You want a new phone.', ['Send a replacement on Friday', 'Give a refund'], 'Replacement: no extra charge'),
    ('🌐', "Your internet doesn't work at home.", 'You work at home. You need it today.', ['Check it on the phone now', 'Send a repair person tomorrow'], 'Repair person: £15 extra charge'),
    ('💳', 'There is an extra charge of £30 on your bill.', 'You want the money back.', ['Check the bill and send the money back', 'Give a £10 discount'], 'Money back in 3 days'),
    ('🛋', 'The driver brought the wrong sofa — grey, not blue.', 'You want the blue sofa.', ['Bring the blue sofa on Monday', 'Give a refund'], 'No extra charge'),
]
STAGES = [('👋', "Hello · I'm calling about…"), ('⚠️', 'There seems to be a problem with…'), ('🙏', 'Could you…? / Would you…?'),
          ('🔀', 'What are my options?'), ('✅', 'Could you confirm the details?')]

# ---------------------------------------------------------------- real-life task: 45-second voice message
VM_PLAN = [('1', "Hello, my name is ___. I'm calling about ___."), ('2', 'There seems to be a problem with ___.'),
           ('3', 'Could you ___, if possible?'), ('4', "I'm available on ___. My number is ___."), ('5', 'Thank you. Goodbye.')]

# ---------------------------------------------------------------- game: quick replies (agent answers)
REPLIES = [  # caller says, [options], answer index
    ("I'm calling about my order. It's very late.", ["I'm sorry. Could I have your order number, please?", 'Goodbye.', "Your order is very good."], 0),
    ('What are my options?', ['You can get a refund or a replacement.', 'Yes, I am available.', "It's a delivery."], 0),
    ('Do I need to pay an extra charge?', ["No, there's no extra charge.", 'Yes, it is broken.', "I'm calling about it."], 0),
    ('Are you available on Monday afternoon?', ["Yes, I'm free after two.", 'Could you check it?', 'There seems to be a problem.'], 0),
    ('Could you confirm the details, please?', ['Sure. A repair on Tuesday at nine, no extra charge.', 'No, thank you.', 'I want a refund.'], 0),
    ('There seems to be a problem with my fridge.', ["I'm sorry to hear that. What's wrong with it?", 'Great, thank you!', 'Your fridge is available.'], 0),
    ('Could you check the delivery status for me?', ["Of course. It's arriving tomorrow morning.", "No. It's my fridge.", 'Yes, I am.'], 0),
    ("I'd like to book a repair service.", ['Sure. When are you available?', 'Here is your replacement.', 'It is late.'], 0),
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name="I'm calling about…", q="I'm calling about ___.", vi_q='Tôi gọi về (việc) ___.',
         a='Of course. How can I help you?', vi_a='Vâng. Tôi có thể giúp gì cho bạn?',
         model='Customer service. How can I help you?',
         answers=[("I'm calling about my order.", 'Tôi gọi về đơn hàng của tôi.'),
                  ("I'm calling about the delivery of my new sofa.", 'Tôi gọi về việc giao chiếc ghế sofa mới.'),
                  ("I'm calling about an extra charge on my bill.", 'Tôi gọi về một khoản phí thêm trên hóa đơn.')],
         tr=[('Tôi gọi về chiếc máy giặt của tôi.', "I'm calling about my washing machine."),
             ('Tôi gọi về việc giao hàng.', "I'm calling about the delivery."),
             ('Tôi gọi để đặt dịch vụ sửa chữa.', "I'm calling to book a repair service.")]),
    dict(name='There seems to be a problem with…', q='There seems to be a problem with ___.', vi_q='Có vẻ như có vấn đề với ___.',
         a="I'm sorry to hear that. What's wrong?", vi_a='Tôi rất tiếc. Có chuyện gì vậy?',
         model='What seems to be the problem?',
         answers=[('There seems to be a problem with my internet.', 'Có vẻ như có vấn đề với mạng internet của tôi.'),
                  ('There seems to be a problem with my order. It is late.', 'Có vẻ như có vấn đề với đơn hàng. Nó bị trễ.'),
                  ('There seems to be an extra charge on my bill.', 'Có vẻ như có một khoản phí thêm trên hóa đơn.')],
         tr=[('Có vẻ như có vấn đề với tủ lạnh của tôi.', 'There seems to be a problem with my fridge.'),
             ('Có vẻ như có vấn đề với điện thoại mới của tôi.', 'There seems to be a problem with my new phone.'),
             ('Có vẻ như có vấn đề với việc giao hàng.', 'There seems to be a problem with the delivery.')]),
    dict(name='Could you check … for me?', q='Could you check ___ for me?', vi_q='Bạn có thể kiểm tra ___ giúp tôi được không?',
         a='Of course. Let me check.', vi_a='Tất nhiên. Để tôi kiểm tra.',
         model='Is there anything else?',
         answers=[('Could you check the delivery status for me?', 'Bạn có thể kiểm tra tình trạng giao hàng giúp tôi không?'),
                  ('Could you check my bill for me, please?', 'Bạn có thể kiểm tra hóa đơn giúp tôi không?'),
                  ('Would you confirm the details, please?', 'Bạn vui lòng xác nhận lại thông tin được không?')],
         tr=[('Bạn có thể kiểm tra đơn hàng giúp tôi được không?', 'Could you check my order for me?'),
             ('Bạn vui lòng xác nhận lại thông tin được không?', 'Would you confirm the details, please?'),
             ('Bạn có rảnh vào sáng thứ Hai không?', 'Are you available on Monday morning?')]),
    dict(name='What are my options?', q='What are my options?', vi_q='Tôi có những lựa chọn nào?',
         a='You can get a refund, or we can send a replacement.', vi_a='Bạn có thể được hoàn tiền, hoặc chúng tôi gửi sản phẩm thay thế.',
         model="I'm sorry. Your order is damaged.",
         answers=[('You can get a refund, or we can send a replacement.', 'Bạn có thể được hoàn tiền, hoặc chúng tôi gửi hàng thay thế.'),
                  ('We can book a repair service for Wednesday.', 'Chúng tôi có thể đặt dịch vụ sửa chữa vào thứ Tư.'),
                  ('You can pay an extra charge for a Saturday repair.', 'Bạn có thể trả thêm phí để sửa vào thứ Bảy.')],
         tr=[('Tôi có những lựa chọn nào?', 'What are my options?'),
             ('Tôi muốn yêu cầu một sản phẩm thay thế.', "I'd like to request a replacement."),
             ('Tôi có phải trả thêm phí không?', 'Do I need to pay an extra charge?')]),
]
