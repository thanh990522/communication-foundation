"""Lesson S07 — Eating Out: From Menu to Bill.
Language limited to the S07 syllabus plus the dishes on the lesson menu:
  collocations : order a starter · choose a main course · a side dish · recommend a dish · a food allergy ·
                 ask for the bill · a service charge · split the bill
  frames       : What do you recommend? · I'll have ___. · Could I have it without ___? · Could we split the bill?
  grammar      : polite ordering with would like, will and could
  linkers      : to start with · for the main course · however · because · finally
  pronunciation: polite falling-rising intonation · linking in could‿I and I'll‿have
"""

# ---------------------------------------------------------------- warm-up: who says it?
WHO = [  # sentence, W = waiter / C = customer
    ('Are you ready to order?', 'W'), ('Could I see the menu, please?', 'C'), ('What do you recommend?', 'C'),
    ('I recommend the fish and chips.', 'W'), ("I'll have the chicken, please.", 'C'), ('Would you like a side dish?', 'W'),
    ('Could I have it without onions?', 'C'), ('Do you have any food allergies?', 'W'), ('Could we have the bill, please?', 'C'),
    ('The service charge is included.', 'W'),
]

# ---------------------------------------------------------------- the menu (used on several slides)
MENU = [  # section, [(dish, price, emoji, tags)]  tags: V = vegetarian, N = contains nuts
    ('Starters', [('Tomato soup', 4.50, '🍅', 'V'), ('Garlic bread', 3.50, '🥖', 'V'), ('Green salad', 4.00, '🥗', 'V')]),
    ('Main courses', [('Grilled chicken', 12.00, '🍗', ''), ('Fish and chips', 11.50, '🐟', ''), ('Vegetable curry', 10.00, '🍛', 'V N'), ('Beef burger', 9.50, '🍔', '')]),
    ('Side dishes', [('Chips', 3.00, '🍟', 'V'), ('Rice', 2.50, '🍚', 'V'), ('Mixed vegetables', 3.00, '🥦', 'V')]),
    ('Desserts', [('Chocolate cake', 5.00, '🍰', 'V N'), ('Ice cream', 4.00, '🍨', 'V')]),
    ('Drinks', [('Water', 1.50, '💧', ''), ('Orange juice', 2.50, '🧃', ''), ('Coffee', 2.00, '☕', ''), ('Tea', 1.50, '🍵', '')]),
]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='starter', w='starter', pos='noun', ipa='/ˈstɑːtə/', vi='món khai vị',
         col='order a starter', kw='starter', col_vi='gọi món khai vị', ex="Let's order a starter: the tomato soup."),
    dict(k='main course', w='main course', pos='noun', ipa='/ˌmeɪn ˈkɔːs/', vi='món chính',
         col='choose a main course', kw='main course', col_vi='chọn món chính', ex='I always choose the chicken for my main course.'),
    dict(k='side dish', w='side dish', pos='noun', ipa='/ˈsaɪd dɪʃ/', vi='món ăn kèm',
         col='a side dish', kw='side dish', col_vi='một món ăn kèm', ex='Would you like a side dish? — Chips, please.'),
    dict(k='recommend', w='recommend', pos='verb', ipa='/ˌrekəˈmend/', vi='gợi ý, giới thiệu',
         col='recommend a dish', kw='recommend', col_vi='gợi ý một món ăn', ex='Can you recommend a dish for me?'),
    dict(k='allergy', w='allergy', pos='noun', ipa='/ˈælədʒi/', vi='dị ứng',
         col='a food allergy', kw='allergy', col_vi='dị ứng thực phẩm', ex="I have a food allergy. I can't eat nuts."),
    dict(k='bill', w='bill', pos='noun', ipa='/bɪl/', vi='hóa đơn',
         col='ask for the bill', kw='bill', col_vi='xin hóa đơn', ex="Let's ask for the bill. — Could we have the bill, please?"),
    dict(k='service charge', w='service charge', pos='noun', ipa='/ˈsɜːvɪs tʃɑːdʒ/', vi='phí phục vụ',
         col='a service charge', kw='service charge', col_vi='một khoản phí phục vụ', ex='There is a ten per cent service charge.'),
    dict(k='split', w='split', pos='verb', ipa='/splɪt/', vi='chia',
         col='split the bill', kw='split', col_vi='chia hóa đơn', ex='Could we split the bill, please?'),
]

# ---------------------------------------------------------------- grammar: make it polite
POLITE = [  # rude / direct, polite
    ('Give me the menu.', 'Could I see the menu, please?'),
    ('I want water.', "I'd like some water, please."),
    ('Chicken.', "I'll have the chicken, please."),
    ('No onions!', 'Could I have it without onions, please?'),
    ('What is good?', 'What do you recommend?'),
    ('Bill!', 'Could we have the bill, please?'),
]
GRAM = [  # form, use, example
    ("I'd like…", 'polite wish', "I'd like the tomato soup, please."),
    ("I'll have…", 'decide now', "I'll have the fish and chips."),
    ('Could I…? / Could we…?', 'polite request', 'Could I have it without onions?'),
]

# ---------------------------------------------------------------- practice: take the order (waiter's pad)
TAKE = [  # spoken order, dishes, "without" note
    ("To start with, I'll have the tomato soup. For the main course, I'd like the grilled chicken with rice, please.", ['Tomato soup', 'Grilled chicken', 'Rice'], ''),
    ("I'll have the beef burger, please. Could I have it without onions? And a side dish of chips.", ['Beef burger', 'Chips'], 'onions'),
    ("Could I have the vegetable curry? I have a food allergy, so could I have it without nuts? And an orange juice, please.", ['Vegetable curry', 'Orange juice'], 'nuts'),
    ("For the main course, I'd like the fish and chips. And for dessert, the chocolate cake. Oh, and a coffee, please.", ['Fish and chips', 'Chocolate cake', 'Coffee'], ''),
]

# ---------------------------------------------------------------- pronunciation: linking + polite intonation
LINKS = [  # (text with ‿, arrow)
    ('Could‿I see the menu, please?', '↗'), ("I'll‿have the fish, please.", '↘'), ('Could‿I have it without onions?', '↗'),
    ('Would‿you like a side dish?', '↗'), ("I'd‿like some water, please.", '↘'), ('Could we split‿the bill?', '↗'),
]

# ---------------------------------------------------------------- listening (real recording)
LISTEN = {
    'title': 'At the restaurant — waitress & customer',
    'source': 'elllo.org · Views #512 At the Restaurant (Akane & Ruth) · © elllo productions',
    'page': 'https://elllo.org/english/0501/512-Akane-Restaurant.html',
    'file': 'Listening/S07_listening_at_the_restaurant.mp3',
    'dur': 190,
    'names': {'W': 'Waitress', 'C': 'Customer'},
    'script': [
        ('W', 'Hi, welcome to our restaurant.'), ('C', 'Thank you very much.'),
        ('W', 'How many people are there?'), ('C', 'Just the one.'),
        ('W', 'Just one person, ok. Smoking or non-smoking?'), ('C', 'Non-smoking please.'),
        ('W', 'Come along and have a seat right here.'), ('C', 'Thanks.'),
        ('W', 'Here are your menus and a glass of water. Can I get you something to drink?'),
        ('C', "Mmm I was wondering about this wine actually. What's your house wine?"),
        ('W', "Our house wine is this red wine right here and it's 10 dollars."),
        ('C', "Oh, I think I'll have a glass of that actually."), ('W', 'Just a glass?'), ('C', 'How much is it for a bottle?'),
        ('W', '10 dollars.'), ('C', "Oh sorry. Yeah I'll have a bottle then, thanks."),
        ('W', 'Can I take your order for an appetiser?'),
        ('C', 'Mmm I quite like the look of several of these. Now the melon, does that come with anything else?'),
        ('W', "The melon? It just comes with some garnish. But it's pretty much just plain melon with garnish and some whipped cream."),
        ('C', 'What would you recommend?'),
        ('W', "Well I really recommend the fries. They're quite good and they come with cheese and tomatoes and some chile on top."),
        ('C', "Oh they sound nice. Ok, I'll have those thanks."),
        ('W', 'Are you ready to order your meal?'),
        ('C', "Yes I think I'm ready now. I think I'll have this vegetable goulash. Can you tell me, is it vegetarian?"),
        ('W', "It is, actually. It's all vegetarian but it does come with cheese."),
        ('C', "Oh that's ok, I eat cheese. Do I get anything with it?"),
        ('W', 'It comes with a side order of rice or potatoes.'), ('C', "I'd like rice please."), ('W', 'Ok.'),
        ('W', 'Did you enjoy your meal?'), ('C', 'It was delicious, thank you.'), ('W', 'Can I get you anything else?'),
        ('C', "Oh, I'd like to look at the dessert menu please. Mm these all look nice. Oh I think I must go for this chocolate cake here."),
        ('W', "Chocolate cake. Very good choice. That's our most popular dish."), ('C', 'Could I get cream with it please?'),
        ('W', 'Would you like custard or whipped cream?'), ('C', 'Whipped cream please.'), ('W', 'Coming right up.'),
        ('C', 'Could I have the bill please?'), ('W', 'Certainly. Here you go.'),
        ('C', "Mmm 30 dollars. Oh that's ok, that's not too bad."), ('W', 'Thank you for coming.'), ('C', 'Ok no problem.'),
        ('W', 'Bye, come again!'), ('C', 'Bye!'),
    ],
    'gist': ('What does the customer have for the main course?', ['the vegetable goulash', 'the chocolate cake'], 'the vegetable goulash'),
    'detail': [
        ('How many people are there?', ['just one', 'two', 'four'], 'just one'),
        ('What does the waitress recommend as a starter?', ['the fries', 'the melon', 'the soup'], 'the fries'),
        ('The goulash comes with a side order of ___.', ['rice or potatoes', 'salad', 'bread'], 'rice or potatoes'),
        ('For dessert, the customer chooses ___.', ['chocolate cake', 'melon', 'ice cream'], 'chocolate cake'),
        ('With her dessert, she wants ___.', ['whipped cream', 'custard', 'nothing'], 'whipped cream'),
    ],
    'times': [
        ('The house wine is ___ dollars.', ['10', 'ten']),
        ('Is the goulash vegetarian? ___ (yes / no)', ['yes', 'yes it is']),
        ('The bill is ___ dollars.', ['30', 'thirty']),
    ],
}

# ---------------------------------------------------------------- model dialogue
DIALOGUE = [
    ('W', 'Good evening. Are you ready to order?'),
    ('M', 'Almost. What do you recommend?'),
    ('W', 'The grilled chicken is very popular. The fish and chips is good today, too.'),
    ('M', "OK. To start with, I'll have the tomato soup."),
    ('W', 'And for the main course?'),
    ('M', "I'd like the vegetable curry, please. However, I have a food allergy. Could I have it without nuts?"),
    ('W', 'Of course. Would you like a side dish with that?'),
    ('M', 'Yes, rice, please.'),
    ('K', "And I'll have the fish and chips, please, because Mai says it's very good."),
    ('W', 'Great choice. Anything to drink?'),
    ('K', 'Two orange juices, please.'),
    ('W', "Thank you. I'll be back with your drinks."),
    ('K', 'Excuse me. Could we have the bill, please?'),
    ('W', 'Of course. The total is forty pounds. That includes the service charge.'),
    ('M', 'Could we split the bill?'),
    ('W', "Sure. That's twenty pounds each."),
]
DLG_NAMES = {'W': 'Waiter', 'M': 'Mai', 'K': 'Ken'}
DLG_Q = [
    ('What does the waiter recommend?', ['the grilled chicken', 'the vegetable curry'], 'the grilled chicken'),
    ('What side dish does Mai have?', ['rice', 'chips', 'mixed vegetables'], 'rice'),
]
CARD = [("Mai's starter", 'tomato soup', ['tomatosoup', 'soup', 'thetomatosoup']),
        ('Mai cannot eat', 'nuts', ['nuts', 'nut']),
        ("Ken's main course", 'fish and chips', ['fishandchips', 'fish', 'fish&chips', 'thefishandchips']),
        ('Each person pays', '£20', ['20', '£20', 'twenty', '20pounds', 'twentypounds'])]

# ---------------------------------------------------------------- practice: split the bill
BILL = [('Garlic bread', 3.50), ('Green salad', 4.00), ('Grilled chicken', 12.00), ('Fish and chips', 11.50),
        ('Beef burger', 9.50), ('Rice', 2.50), ('2 × Orange juice', 5.00), ('3 × Coffee', 6.00)]
BILL_Q = [('Subtotal', 54.00), ('Service charge (10%)', 5.40), ('Total', 59.40), ('Each person (3 people)', 19.80)]

# ---------------------------------------------------------------- speaking: role-play customer cards
ROLECARDS = [
    ('🥜', 'Food allergy', "You can't eat nuts. Ask about the curry and the cake."),
    ('🥦', 'Vegetarian', "You don't eat meat or fish. Ask: What do you recommend?"),
    ('🧅', 'No onions', 'Order a burger without onions and a side dish.'),
    ('💷', '£15 budget', 'Order a starter, a main course and a drink. Check the prices!'),
    ('👥', 'Two friends', 'Order for two people, then ask to split the bill.'),
    ('🍰', 'Dessert lover', 'Order a main course and a dessert. Then ask for the bill.'),
]

# ---------------------------------------------------------------- game: what's the total?
TOTALS = [  # spoken order, total (£)
    ('Two coffees and a chocolate cake, please.', 9.00),
    ('A tomato soup and an orange juice, please.', 7.00),
    ('Fish and chips and a water, please.', 13.00),
    ('Two teas and two ice creams, please.', 11.00),
    ("I'll have a beef burger, chips and a coffee.", 14.50),
    ("I'd like the grilled chicken with rice and a green salad.", 18.50),
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name='What do you recommend?', q='What do you recommend?', vi_q='Bạn gợi ý món gì?',
         a="I recommend the ___. It's very ___.", vi_a='Tôi gợi ý món ___. Món này rất ___.',
         model='What do you recommend?',
         answers=[("I recommend the grilled chicken. It's very popular.", 'Tôi gợi ý món gà nướng. Món này rất được ưa chuộng.'),
                  ('The fish and chips is very good today.', 'Món cá và khoai tây chiên hôm nay rất ngon.'),
                  ('For a starter, I recommend the tomato soup.', 'Về món khai vị, tôi gợi ý súp cà chua.')],
         tr=[('Bạn gợi ý món tráng miệng nào?', 'What dessert do you recommend?'),
             ('Bạn có thể gợi ý một món cho tôi không?', 'Can you recommend a dish for me?'),
             ('Tôi gợi ý món cà ri rau.', 'I recommend the vegetable curry.')]),
    dict(name="I'll have…", q="I'll have ___. / I'd like ___.", vi_q='Tôi sẽ gọi ___. / Tôi muốn ___.',
         a="To start with, I'll have ___. For the main course, I'd like ___.", vi_a='Trước tiên, tôi gọi ___. Món chính, tôi muốn ___.',
         model='Are you ready to order?',
         answers=[("Yes. I'll have the tomato soup, please.", 'Vâng. Tôi gọi súp cà chua.'),
                  ("To start with, I'd like the garlic bread.", 'Trước tiên, tôi muốn bánh mì bơ tỏi.'),
                  ("For the main course, I'll have the fish and chips.", 'Món chính, tôi gọi cá và khoai tây chiên.')],
         tr=[('Tôi sẽ gọi gà nướng với cơm.', "I'll have the grilled chicken with rice."),
             ('Món chính, tôi muốn món cà ri rau.', "For the main course, I'd like the vegetable curry."),
             ('Chúng tôi sẽ gọi hai cà phê.', "We'll have two coffees.")]),
    dict(name='Could I have it without…?', q='Could I have it without ___?', vi_q='Tôi có thể dùng món đó mà không có ___ không?',
         a="Of course. / I'm sorry, it comes with ___.", vi_a='Tất nhiên. / Xin lỗi, món này có kèm ___.',
         model='Could I have the burger without onions?',
         answers=[('Of course. No problem.', 'Tất nhiên. Không vấn đề gì.'),
                  ('Sure. Do you have a food allergy?', 'Được. Anh/chị có dị ứng thực phẩm không?'),
                  ("I'm sorry, the curry comes with nuts.", 'Xin lỗi, món cà ri có kèm các loại hạt.')],
         tr=[('Tôi có thể dùng món salad mà không có phô mai không?', 'Could I have the salad without cheese?'),
             ('Tôi bị dị ứng thực phẩm. Tôi không ăn được các loại hạt.', "I have a food allergy. I can't eat nuts."),
             ('Cho tôi món cá mà không có khoai tây chiên được không?', 'Could I have the fish without chips?')]),
    dict(name='Could we split the bill?', q='Could we split the bill?', vi_q='Chúng tôi chia hóa đơn được không?',
         a="Sure. That's ___ each.", vi_a='Được. Mỗi người ___.',
         model='Could we have the bill, please?',
         answers=[('Of course. Here you are.', 'Tất nhiên. Của anh/chị đây.'),
                  ('Could we split the bill, please?', 'Chúng tôi chia hóa đơn được không?'),
                  ("Sure. That's twelve pounds each.", 'Được. Mỗi người mười hai bảng.')],
         tr=[('Phí phục vụ đã bao gồm chưa?', 'Is the service charge included?'),
             ('Vậy là mỗi người mười lăm bảng.', "So that's fifteen pounds each."),
             ('Chúng tôi muốn chia hóa đơn, làm ơn.', "We'd like to split the bill, please.")]),
]

MENU_IPA = {'Tomato soup': '/təˈmɑːtəʊ suːp/', 'Garlic bread': '/ˈɡɑːlɪk bred/', 'Green salad': '/ɡriːn ˈsæləd/',
            'Grilled chicken': '/ɡrɪld ˈtʃɪkɪn/', 'Fish and chips': '/ˌfɪʃ ən ˈtʃɪps/', 'Vegetable curry': '/ˈvedʒtəbl ˈkʌri/',
            'Beef burger': '/ˈbiːf ˌbɜːɡə/', 'Chips': '/tʃɪps/', 'Rice': '/raɪs/', 'Mixed vegetables': '/mɪkst ˈvedʒtəblz/',
            'Chocolate cake': '/ˈtʃɒklət keɪk/', 'Ice cream': '/ˌaɪs ˈkriːm/', 'Water': '/ˈwɔːtə/', 'Orange juice': '/ˈɒrɪndʒ dʒuːs/',
            'Coffee': '/ˈkɒfi/', 'Tea': '/tiː/'}
SECTION_IPA = {'Starters': '/ˈstɑːtəz/', 'Main courses': '/ˌmeɪn ˈkɔːsɪz/', 'Side dishes': '/ˈsaɪd ˌdɪʃɪz/', 'Desserts': '/dɪˈzɜːts/', 'Drinks': '/drɪŋks/'}
