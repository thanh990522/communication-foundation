"""Lesson S06 — Food, Shopping Lists & Quantities.
Language limited to the S06 syllabus plus the food words and containers taught on the warm-up / containers slides:
  collocations : fresh ingredients · a large portion · fresh produce · dairy products · the supermarket aisle ·
                 have enough · be out of stock · a packet of rice
  frames       : Do we have any ___? · We need a few/a little ___. · We are running out of ___. · Is there anything else?
  grammar      : quantifiers some/any, much/many, a few/a little, enough
  linkers      : first · also · but · because · so
  pronunciation: weak forms of some /səm/ and any · word stress in ingredient
"""

# ---------------------------------------------------------------- warm-up: what's in the fridge? (memory game)
FRIDGE = [  # quantity phrase, food, emoji
    ('six', 'eggs', '🥚'), ('a carton of', 'milk', '🥛'), ('some', 'cheese', '🧀'), ('a little', 'butter', '🧈'),
    ('a few', 'apples', '🍎'), ('three', 'carrots', '🥕'), ('some', 'tomatoes', '🍅'), ('a loaf of', 'bread', '🍞'),
    ('a packet of', 'rice', '🍚'), ('some', 'chicken', '🍗'), ('two', 'yoghurts', '🥣'), ('a bottle of', 'orange juice', '🧃'),
]

# ---------------------------------------------------------------- containers
CONTAINERS = [  # container, food, emoji, IPA of the container word, Vietnamese
    ('a packet of', 'rice', '🍚', '/ˈpækɪt/', 'một gói'),
    ('a carton of', 'milk', '🥛', '/ˈkɑːtn/', 'một hộp (giấy)'),
    ('a bottle of', 'water', '💧', '/ˈbɒtl/', 'một chai'),
    ('a loaf of', 'bread', '🍞', '/ləʊf/', 'một ổ'),
    ('a bag of', 'apples', '🍎', '/bæɡ/', 'một túi'),
    ('a jar of', 'jam', '🍯', '/dʒɑː/', 'một hũ'),
    ('a can of', 'cola', '🥤', '/kæn/', 'một lon'),
    ('a kilo of', 'chicken', '🍗', '/ˈkiːləʊ/', 'một ký'),
]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='ingredient', w='ingredient', pos='noun', ipa='/ɪnˈɡriːdiənt/', vi='nguyên liệu',
         col='fresh ingredients', kw='ingredients', col_vi='nguyên liệu tươi', ex='I always cook with fresh ingredients.'),
    dict(k='portion', w='portion', pos='noun', ipa='/ˈpɔːʃn/', vi='khẩu phần, phần ăn',
         col='a large portion', kw='portion', col_vi='một phần ăn lớn', ex='This café gives you a large portion of rice.'),
    dict(k='fresh', w='fresh', pos='adjective', ipa='/freʃ/', vi='tươi',
         col='fresh produce', kw='fresh', col_vi='nông sản tươi (rau, củ, quả)', ex='The market sells fresh produce every morning.'),
    dict(k='dairy', w='dairy', pos='adjective', ipa='/ˈdeəri/', vi='(làm) từ sữa',
         col='dairy products', kw='dairy', col_vi='các sản phẩm từ sữa', ex='Milk, cheese and butter are dairy products.'),
    dict(k='aisle', w='aisle', pos='noun', ipa='/aɪl/', vi='lối đi giữa các kệ hàng',
         col='the supermarket aisle', kw='aisle', col_vi='lối đi trong siêu thị', ex='The rice is in the third supermarket aisle.'),
    dict(k='enough', w='enough', pos='determiner', ipa='/ɪˈnʌf/', vi='đủ',
         col='have enough', kw='enough', col_vi='có đủ', ex='Do we have enough eggs for the cake?'),
    dict(k='out of stock', w='out of stock', pos='phrase', ipa='/ˌaʊt əv ˈstɒk/', vi='hết hàng',
         col='be out of stock', kw='out of stock', col_vi='bị hết hàng', ex='Sorry, the milk is out of stock today.'),
    dict(k='a packet of', w='a packet of', pos='phrase', ipa='/ə ˈpækɪt əv/', vi='một gói',
         col='a packet of rice', kw='a packet of', col_vi='một gói gạo', ex='Can you buy a packet of rice, please?'),
]

# ---------------------------------------------------------------- grammar: quantifiers
GRAM = [  # title, rule, examples
    ('some · any', '+ some  ·  ? / – any', ['We have some eggs.', 'Do we have any milk?', "We don't have any bread."]),
    ('many · much', 'many + count · much + no count', ['How many eggs do we need?', 'How much milk is there?']),
    ('a few · a little', 'a few + count · a little + no count', ['We need a few apples.', 'We need a little butter.']),
    ('enough', 'enough + noun · not enough', ['We have enough rice.', "We don't have enough eggs."]),
]
COUNT = ['eggs', 'apples', 'tomatoes', 'carrots', 'yoghurts']
NOCOUNT = ['milk', 'butter', 'cheese', 'rice', 'bread', 'water', 'orange juice', 'chicken']
MAPQ = [  # quick check (MC rows)
    ('How ___ eggs do we need?', ['many', 'much'], 'many'),
    ('How ___ milk is there?', ['much', 'many'], 'much'),
    ('We need ___ apples.', ['a few', 'a little'], 'a few'),
    ('We need ___ butter.', ['a little', 'a few'], 'a little'),
    ('Do we have ___ cheese?', ['any', 'a few'], 'any'),
    ("We don't have ___ eggs for the cake.", ['enough', 'much'], 'enough'),
]

# ---------------------------------------------------------------- practice: enough or not enough? (recipe vs fridge)
RECIPE = {'title': 'Fried rice for four people', 'items': [  # food, emoji, need, have, enough?
    ('rice', '🍚', 'a packet of rice', 'a packet of rice', True),
    ('eggs', '🥚', '4 eggs', '2 eggs', False),
    ('carrots', '🥕', '3 carrots', '5 carrots', True),
    ('chicken', '🍗', 'a little chicken', 'no chicken', False),
    ('butter', '🧈', 'a little butter', 'a little butter', True),
    ('tomatoes', '🍅', '4 tomatoes', '1 tomato', False),
]}

# ---------------------------------------------------------------- pronunciation
WEAK = [  # sentences with some/any in weak form (marked *)
    'We need *some* milk.', "There's *some* cheese in the fridge.", "I'd like *some* apples, please.",
    'Do we have *any* eggs?', 'Is there *any* juice?', "We don't have *any* bread.",
]
STRESS_W = [  # word, syllables (stressed in CAPS), IPA
    ('ingredient', 'in·GRE·di·ent', '/ɪnˈɡriːdiənt/'), ('portion', 'POR·tion', '/ˈpɔːʃn/'), ('dairy', 'DAI·ry', '/ˈdeəri/'),
    ('produce', 'PRO·duce', '/ˈprɒdjuːs/'), ('aisle', 'aisle (no “s”!)', '/aɪl/'), ('enough', 'e·NOUGH', '/ɪˈnʌf/'),
]

# ---------------------------------------------------------------- listening (real recording)
LISTEN = {
    'title': "What's in your fridge? — John & Todd",
    'source': 'elllo.org · Views #209 The Fridge (John & Todd) · © elllo productions',
    'page': 'https://elllo.org/english/0201/209-John-Fridge.htm',
    'file': 'Listening/S06_listening_John_fridge.mp3',
    'dur': 158,
    'names': {'T': 'Todd', 'J': 'John'},
    'script': [
        ('T', 'OK, John, at your house do you have a refrigerator?'),
        ('J', 'Yes, a very small refrigerator.'),
        ('T', 'OK, what is in your refrigerator?'),
        ('J', "Let's see. There are some eggs, a carton of milk, some strawberry jam, some butter, some cheese, maybe some tofu, some green onions, carrots, some lettuce, and maybe some ice tea."),
        ('T', 'OK, so do you follow a healthy diet?'),
        ('J', 'Ah, sometimes. I say about every other day I try to eat healthy and then on some days I just go donut and candy crazy.'),
        ('T', "So donuts are your thing? You're really crazy about donuts."),
        ('J', 'Yeah, baked goods, cakes, donuts, cheesecake, any kind of cake or sweet bread.'),
        ('T', 'Mm, actually you brought donuts today!'),
        ('J', "Yeah, I was given donuts by a student so, yeah, I was glad there was other people to help me eat them so I didn't eat them all."),
        ('T', 'That was very nice of your students. Um, do you prefer to cook at home or eat out?'),
        ('J', "Um, usually I prefer to cook at home, just because there are a few dishes that my wife and I like to make and that we're pretty good at, and that we're real comfortable with, but if I'm real tired, if it's been a long day at work there's nothing better than just going to a restaurant and being served your food right away, not having to wait."),
        ('T', 'So with your wife do you usually cook together or do you take turns cooking? Do you alternate?'),
        ('J', "We usually take turns. When we first started dating we would cook together. We had a big kitchen, where she was living there was a big kitchen and there was room enough for both of us to move around, and we were still really comfortable with each other, and open and we always wanted to share ideas, but now we have a really small kitchen and there's really only room for one of us, and also too we're at the point in our relationship where I know that she makes fried chicken better than I do and she knows that I make chili better than she does so the other person should just get out of the kitchen, and let the one who's cooking, you know, do their job."),
    ],
    'gist': ('Where does John usually prefer to eat?', ['at home', 'at a restaurant'], 'at home'),
    'detail': [
        ('John has a very ___ refrigerator.', ['small', 'big', 'new'], 'small'),
        ('In his fridge, there is a ___ of milk.', ['carton', 'bottle', 'packet'], 'carton'),
        ('John tries to eat healthy food about ___.', ['every other day', 'every day', 'once a week'], 'every other day'),
        ('John is crazy about ___.', ['donuts and cake', 'cheese', 'carrots'], 'donuts and cake'),
        ('John and his wife usually ___ cooking.', ['take turns', 'cook together', 'stop'], 'take turns'),
    ],
    'times': [
        ('There is some strawberry ___ in the fridge.', ['jam']),
        ('His wife makes better fried ___.', ['chicken']),
        ('John makes better ___.', ['chili', 'chilli']),
    ],
}

# ---------------------------------------------------------------- model dialogue (phone call from the supermarket)
DIALOGUE = [
    ('S', "Hi Lucy, I'm at the supermarket. Do we have any eggs?"),
    ('L', 'Let me check the fridge… We have a few eggs, but not enough for the cake. Can you get six?'),
    ('S', 'Six eggs. OK. What else?'),
    ('L', "We're running out of milk. Get two cartons, please."),
    ('S', 'Two cartons of milk. Do we need any cheese?'),
    ('L', 'No, we have enough cheese. But we need a little butter.'),
    ('S', 'OK. And fresh produce?'),
    ('L', 'Yes, a few tomatoes and some apples.'),
    ('S', 'Hmm, the apples are out of stock. How about oranges?'),
    ('L', 'Sure, oranges are fine. Oh, and a packet of rice.'),
    ('S', 'Which aisle is the rice in?'),
    ('L', "I think it's in aisle five, next to the bread."),
    ('S', 'Got it. Is there anything else?'),
    ('L', "No, that's all. Thanks, Sam!"),
]
DLG_NAMES = {'S': 'Sam', 'L': 'Lucy'}
DLG_Q = [
    ('Why does Sam not buy apples?', ['They are out of stock.', 'They are not fresh.'], 'They are out of stock.'),
    ('Do they need any cheese?', ['No, they have enough.', 'Yes, a little.'], 'No, they have enough.'),
]
CARD = [('Eggs', '6', ['6', 'six', '6eggs', 'sixeggs']),
        ('Milk', '2 cartons', ['2', 'two', '2cartons', 'twocartons', '2cartonsofmilk']),
        ('Fruit', 'oranges', ['oranges', 'orange', 'someoranges']),
        ('Rice', 'aisle 5', ['5', 'five', 'aisle5', 'aislefive'])]

# ---------------------------------------------------------------- speaking: supermarket stock board
AISLES = [  # aisle, items
    ('Aisle 1 · Fresh produce', [('apples', '🍎'), ('tomatoes', '🍅'), ('carrots', '🥕')]),
    ('Aisle 2 · Dairy products', [('milk', '🥛'), ('cheese', '🧀'), ('yoghurt', '🥣')]),
    ('Aisle 3 · Rice & bread', [('rice', '🍚'), ('bread', '🍞'), ('eggs', '🥚')]),
    ('Aisle 4 · Drinks', [('water', '💧'), ('orange juice', '🧃'), ('cola', '🥤')]),
]
SHOP_LISTS = [
    ['a carton of milk', 'a few apples', 'a packet of rice', 'some cheese'],
    ['two bottles of water', 'a loaf of bread', 'a few tomatoes', 'some yoghurt'],
    ['six eggs', 'a little butter', 'a bag of carrots', 'orange juice'],
    ['a can of cola', 'some chicken', 'a few carrots', 'a carton of milk'],
]

# ---------------------------------------------------------------- real-life task: my shopping list (quantifier checker)
QTY = ['a few', 'a little', 'some', 'enough', 'two', 'a packet of', 'a carton of', 'a bottle of', 'a loaf of', 'a bag of']
FOODS = ['eggs', 'apples', 'tomatoes', 'carrots', 'milk', 'butter', 'cheese', 'rice', 'bread', 'water', 'orange juice', 'chicken']
FITS = {  # quantity → foods it can go with
    'a few': COUNT, 'two': COUNT, 'a little': NOCOUNT, 'some': COUNT + NOCOUNT, 'enough': COUNT + NOCOUNT,
    'a packet of': ['rice'], 'a carton of': ['milk', 'orange juice'], 'a bottle of': ['water', 'orange juice', 'milk'],
    'a loaf of': ['bread'], 'a bag of': ['apples', 'tomatoes', 'carrots', 'rice'],
}

# ---------------------------------------------------------------- game: fill the trolley
TROLLEY = [('eggs', '🥚'), ('apples', '🍎'), ('tomatoes', '🍅'), ('carrots', '🥕'),
           ('cartons of milk', '🥛'), ('packets of rice', '🍚'), ('bottles of water', '💧'), ('loaves of bread', '🍞')]
ORDERS = [  # spoken order, {trolley item: count}
    ('We need six eggs and two cartons of milk.', {'eggs': 6, 'cartons of milk': 2}),
    ('Can you get a packet of rice, three tomatoes and a loaf of bread?', {'packets of rice': 1, 'tomatoes': 3, 'loaves of bread': 1}),
    ("We're running out of water. Get four bottles of water and three apples, please.", {'bottles of water': 4, 'apples': 3}),
    ('Get two loaves of bread, five carrots and one carton of milk.', {'loaves of bread': 2, 'carrots': 5, 'cartons of milk': 1}),
    ('We need ten eggs, two packets of rice and two bottles of water.', {'eggs': 10, 'packets of rice': 2, 'bottles of water': 2}),
    ('Please get four apples, four tomatoes and three cartons of milk.', {'apples': 4, 'tomatoes': 4, 'cartons of milk': 3}),
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name='Do we have any…?', q='Do we have any ___?', vi_q='Chúng ta có ___ nào không?',
         a="Yes, we have some / a few… · No, we don't have any.", vi_a='Có, chúng ta có một ít/vài… · Không, không có chút nào.',
         model='Do we have any eggs?',
         answers=[('Yes, we have a few eggs.', 'Có, chúng ta có vài quả trứng.'),
                  ('Yes, but not enough for the cake.', 'Có, nhưng không đủ để làm bánh.'),
                  ("No, we don't have any.", 'Không, chúng ta không có quả nào.')],
         tr=[('Chúng ta có sữa nào không?', 'Do we have any milk?'),
             ('Chúng ta không có bánh mì nào cả.', "We don't have any bread."),
             ('Chúng ta có đủ gạo không?', 'Do we have enough rice?')]),
    dict(name='We need a few / a little…', q='We need a few / a little ___.', vi_q='Chúng ta cần vài / một ít ___.',
         a='a few + eggs, apples… · a little + milk, butter…', vi_a='a few + danh từ đếm được · a little + danh từ không đếm được',
         model='What do we need for dinner?',
         answers=[('We need a few eggs.', 'Chúng ta cần vài quả trứng.'),
                  ('We need a little butter.', 'Chúng ta cần một ít bơ.'),
                  ('We need a carton of milk and a few apples.', 'Chúng ta cần một hộp sữa và vài quả táo.')],
         tr=[('Chúng ta cần vài quả cà chua.', 'We need a few tomatoes.'),
             ('Chúng ta cần một ít phô mai.', 'We need a little cheese.'),
             ('Chúng ta cần một gói gạo và vài củ cà rốt.', 'We need a packet of rice and a few carrots.')]),
    dict(name='We are running out of…', q='We are running out of ___.', vi_q='Chúng ta sắp hết ___.',
         a="We're running out of ___, so we need ___.", vi_a='Chúng ta sắp hết ___, nên chúng ta cần ___.',
         model='Is there anything we need?',
         answers=[("Yes, we're running out of milk.", 'Có, chúng ta sắp hết sữa.'),
                  ("We're running out of eggs, so we need a few.", 'Chúng ta sắp hết trứng, nên cần vài quả.'),
                  ('No, we have enough food.', 'Không, chúng ta có đủ đồ ăn.')],
         tr=[('Chúng ta sắp hết nước rồi.', "We're running out of water."),
             ('Siêu thị sắp hết bánh mì.', 'The supermarket is running out of bread.'),
             ('Chúng ta sắp hết cà rốt, nên chúng ta cần một túi.', "We're running out of carrots, so we need a bag.")]),
    dict(name='Is there anything else?', q='Is there anything else?', vi_q='Còn gì nữa không?',
         a="Yes, ___, please. · No, that's all.", vi_a='Có, ___. · Không, vậy thôi.',
         model='Is there anything else?',
         answers=[('Yes, a bottle of water, please.', 'Có, một chai nước.'),
                  ('Yes, we need some fresh produce.', 'Có, chúng ta cần ít rau củ quả tươi.'),
                  ("No, that's all. Thank you.", 'Không, vậy thôi. Cảm ơn.')],
         tr=[('Còn gì nữa không? — Không, vậy thôi.', "Is there anything else? — No, that's all."),
             ('Có, chúng ta cũng cần một hộp sữa.', 'Yes, we also need a carton of milk.'),
             ('Còn gì khác ở khu đồ sữa không?', 'Is there anything else in the dairy aisle?')]),
]
