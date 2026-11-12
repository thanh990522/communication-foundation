"""Lesson S03 — People, Homes & Neighbourhoods.
Language is limited to the syllabus items for S03 plus the A1 place words taught on the 'Places' slide:
  collocations : a spacious apartment · a crowded area · a peaceful neighbourhood · a convenient location ·
                 nearby facilities · modern facilities · a friendly neighbour · centrally located
  frames       : There is/are ___ near ___. · One thing I like is ___. · It is ___ because ___. ·
                 The only problem is ___.
  grammar      : There is / There are (+ negatives, questions) + descriptive clauses with because
  linkers      : and · but · because · so · however
  pronunciation: word stress (spacious, convenient, facility …) · final consonants
"""

# ---------------------------------------------------------------- warm-up: this or that?
WARM = [  # emoji A, word A, emoji B, word B, sentence A, sentence B
    ('🏙', 'the city', '🌳', 'the countryside', 'I live in the city.', 'I live in the countryside.'),
    ('🏢', 'an apartment', '🏠', 'a house', 'I live in an apartment.', 'I live in a house.'),
    ('🐘', 'big', '🐭', 'small', 'My home is big.', 'My home is small.'),
    ('📍', 'near my work', '🗺', 'far from my work', 'I live near my work.', 'I live far from my work.'),
]

# ---------------------------------------------------------------- places (A1 words for There is/are)
PLACES = [  # word, emoji, Vietnamese
    ('park', '🌳', 'công viên'), ('supermarket', '🛒', 'siêu thị'), ('bus stop', '🚏', 'trạm xe buýt'),
    ('hospital', '🏥', 'bệnh viện'), ('gym', '🏋️', 'phòng tập gym'), ('school', '🏫', 'trường học'),
    ('café', '☕', 'quán cà phê'), ('market', '🧺', 'chợ'),
]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='spacious', w='spacious', pos='adjective', ipa='/ˈspeɪʃəs/', vi='rộng rãi',
         col='a spacious apartment', kw='spacious', col_vi='một căn hộ rộng rãi', ex='I live in a spacious apartment.'),
    dict(k='crowded', w='crowded', pos='adjective', ipa='/ˈkraʊdɪd/', vi='đông đúc',
         col='a crowded area', kw='crowded', col_vi='một khu vực đông đúc', ex='The market is in a crowded area.'),
    dict(k='peaceful', w='peaceful', pos='adjective', ipa='/ˈpiːsfl/', vi='yên bình',
         col='a peaceful neighbourhood', kw='peaceful', col_vi='một khu phố yên bình', ex='I live in a peaceful neighbourhood.'),
    dict(k='convenient', w='convenient', pos='adjective', ipa='/kənˈviːniənt/', vi='thuận tiện',
         col='a convenient location', kw='convenient', col_vi='một vị trí thuận tiện', ex='My home is in a convenient location.'),
    dict(k='nearby', w='nearby', pos='adjective', ipa='/ˌnɪəˈbaɪ/', vi='gần đó',
         col='nearby facilities', kw='nearby', col_vi='các tiện ích gần đó', ex='There are lots of nearby facilities.'),
    dict(k='facility', w='facility', pos='noun', ipa='/fəˈsɪləti/', vi='tiện ích, cơ sở vật chất',
         col='modern facilities', kw='facilities', col_vi='tiện ích hiện đại', ex='The gym has modern facilities.'),
    dict(k='neighbour', w='neighbour', pos='noun', ipa='/ˈneɪbə/', vi='hàng xóm',
         col='a friendly neighbour', kw='neighbour', col_vi='một người hàng xóm thân thiện', ex='I have a friendly neighbour.'),
    dict(k='located', w='located', pos='adjective', ipa='/ləʊˈkeɪtɪd/', vi='nằm ở',
         col='centrally located', kw='located', col_vi='nằm ở trung tâm', ex='My apartment is centrally located.'),
]

# ---------------------------------------------------------------- collocation check
COLL = [  # sentence, options, answer, illustration key
    ('I live in a ___ apartment.', ['spacious', 'crowded', 'nearby'], 'spacious', 'spacious'),
    ('The market is in a ___ area.', ['crowded', 'friendly', 'modern'], 'crowded', 'crowded'),
    ('It is a ___ neighbourhood.', ['peaceful', 'located', 'nearby'], 'peaceful', 'peaceful'),
    ('My home is in a convenient ___.', ['location', 'facility', 'neighbour'], 'location', 'convenient'),
    ('There are lots of ___ facilities.', ['nearby', 'centrally', 'friendly'], 'nearby', 'nearby'),
    ('The gym has modern ___.', ['facilities', 'neighbours', 'locations'], 'facilities', 'facility'),
    ('I have a ___ neighbour.', ['friendly', 'crowded', 'spacious'], 'friendly', 'neighbour'),
    ('My apartment is ___ located.', ['centrally', 'nearby', 'peaceful'], 'centrally', 'located'),
]

# ---------------------------------------------------------------- grammar: There is / There are
GRAM = [  # title, pattern, example
    ('One thing', 'There is a + noun', 'There is a park near my home.'),
    ('Two or more', 'There are + two / lots of + nouns', 'There are two cafés near my home.'),
    ('Negative', "There isn't a … · There aren't any …", "There isn't a hospital. There aren't any gyms."),
    ('Question ?', 'Is there a …? · Are there any …?', 'Is there a supermarket near here?'),
]
GRAM_QA = [  # question, yes, no
    ('Is there a park near your home?', 'Yes, there is.', "No, there isn't."),
    ('Are there any cafés near your home?', 'Yes, there are.', "No, there aren't."),
]
# neighbourhood map practice (answers match the map in illus03.MAP)
MAPQ = [  # sentence with ___, options, answer
    ('There ___ a park near my home.', ['is', 'are', "isn't"], 'is'),
    ('There ___ two cafés near my home.', ['is', 'are', "aren't"], 'are'),
    ('There ___ a hospital near my home.', ['is', "isn't", 'are'], "isn't"),
    ('There ___ any gyms near my home.', ['are', "aren't", 'is'], "aren't"),
    ('There ___ two bus stops near my home.', ['are', 'is', "isn't"], 'are'),
    ('There ___ a supermarket near the park.', ['is', 'are', "aren't"], 'is'),
    ('Is there a market near my home?', ['Yes, there is.', "No, there isn't."], 'Yes, there is.'),
    ('Are there any hospitals near my home?', ['Yes, there are.', "No, there aren't."], "No, there aren't."),
]

# ---------------------------------------------------------------- pronunciation 1: word stress
STRESS_WORDS = [  # word, syllables with stressed one in CAPS, pattern index 0=Oo 1=oOo 2=oOoo
    ('spacious', 'SPA·cious', 0), ('peaceful', 'PEACE·ful', 0), ('crowded', 'CROWD·ed', 0),
    ('neighbour', 'NEIGH·bour', 0), ('modern', 'MO·dern', 0), ('friendly', 'FRIEND·ly', 0),
    ('located', 'lo·CA·ted', 1), ('location', 'lo·CA·tion', 1), ('apartment', 'a·PART·ment', 1),
    ('convenient', 'con·VE·ni·ent', 2), ('facility', 'fa·CI·li·ty', 2),
]
PATTERNS = [('Oo', '● •'), ('oOo', '• ● •'), ('oOoo', '• ● • •')]

# ---------------------------------------------------------------- pronunciation 2: final consonants
# *word* marks the word whose final consonant is practised
FINALS = [
    {'snd': '/t/', 'words': ['apartment', 'market', 'supermarket', 'convenient'],
     'phrases': ['a spacious *apartment*', 'near the *market*', 'a big *supermarket*'],
     'sents': ['I live in a spacious *apartment*.', 'There is a *market* near my home.', 'It is *convenient*.']},
    {'snd': '/d/', 'words': ['crowded', 'located', 'neighbourhood'],
     'phrases': ['a *crowded* area', 'centrally *located*', 'a peaceful *neighbourhood*'],
     'sents': ['It is a *crowded* area.', 'My apartment is centrally *located*.', 'I live in a peaceful *neighbourhood*.']},
    {'snd': '/k/ /p/ /l/ /m/', 'words': ['park', 'bus stop', 'peaceful', 'school', 'hospital', 'gym'],
     'phrases': ['near the *park*', 'at the bus *stop*', 'a modern *gym*'],
     'sents': ['There is a *park* near my home.', 'There are two bus *stops* near the *school*.', 'There is a *gym* near the *hospital*.']},
]
CHALLENGE = [
    "There's a *park* near my *apartment*, so it's *peaceful*.",
    "It's centrally *located*, but it's a *crowded* area.",
    'One thing I like is the modern *gym* near the bus *stop*.',
]

# ---------------------------------------------------------------- listening (real recording)
LISTEN = {
    'title': 'My Hometown — Sarah & John',
    'source': 'elllo.org · A1 Lesson 21 · There is / There are (Todd Beuckens)',
    'page': 'https://elllo.org/english/grammar/A1-21-There-is-are-Hometowns.htm',
    'file': 'Listening/S03_listening_Sarah_John_hometowns.mp3',
    'dur': 344,
    'names': {'S': 'Sarah', 'J': 'John'},
    'script': [
        ('J', "So, Sarah, what can you tell me about your hometown?"),
        ('S', "My hometown. Well, my hometown is called Eau Claire, Wisconsin, and it's a really great city. There are about 80,000 people. There are lots of things to do. There are three movie theaters. I love to watch movies."),
        ('J', "Me too."),
        ('S', "There's lots of shopping. You can find anything you want there. There are lots of malls and stores."),
        ('J', "Are there many restaurants?"),
        ('S', "Yes. The thing I like is you can eat any type of food. There are Chinese restaurants and Korean restaurants, Italian restaurants. There is a big variety of restaurants, and they're all good."),
        ('J', "That sounds great. What about parks? Are there many places to see nature in your town?"),
        ('S', "Yes. We have a lot of rivers and lakes and hills. My hometown has four seasons. So in summer, it's great because there are lots of lakes to swim in, lots of forests to play in. In winter, there is a lot of snow. So you can go ice skating or ice fishing or even skiing."),
        ('J', "Wow, that sounds really fun."),
        ('S', "Yeah, it's a really nice city. It's also really safe. There are lots of nice people there."),
        ('J', "Good. Is there much to do at night?"),
        ('S', "Well, maybe not. There's not many things to do at night. There aren't any nightclubs. There aren't many bars. So actually, maybe there isn't much nightlife."),
        ('J', "That's okay. It sounds like a nice place to have a family."),
        ('S', "Yeah, it is. It's a great place to have a family. There's lots of good schools and libraries. So John, where are you from?"),
        ('J', "My hometown is very small. It's a little town in the countryside, in Wisconsin. There are only 5,000 people there."),
        ('S', "Wow, there aren't very many people."),
        ('J', "No, it's very small. There aren't very many businesses. There isn't a shopping mall. There are a lot of grocery stores. And there are a lot of gas stations. But there isn't much to do there."),
        ('S', "Oh really? Are there any movie theaters?"),
        ('J', "Well, there is one movie theater. So that's a nice thing to do. In fact, there are many screens in the theater. There are eight different movies showing."),
        ('S', "How about at night? What's fun to do? Is there very much nightlife?"),
        ('J', "Yeah, there's not so much. But there is a bowling alley. It's fun to go bowling with friends. There's a bowling alley and the movie theater. There's one restaurant where you can go for tacos and burritos. And there's one more restaurant for pizza and spaghetti."),
        ('S', "Ah."),
        ('J', "But during the daytime, you can go to the park. There's a river that goes through the town. So in the middle of town, there's a river. And there's a park that goes along both sides of the river. And at the park, there is a tennis court and a disc golf course."),
        ('S', "Disc golf?"),
        ('J', "Yeah, I like to play disc golf with my friends. It's really fun. And after we finish playing disc golf, we usually go to the pizza restaurant."),
        ('S', "Oh, I see. How about schools? Are there very many schools?"),
        ('J', "Let's see. No, there aren't very many. There is only one elementary school, one junior high school, and one high school. That's it."),
        ('S', "Interesting."),
        ('J', "Yeah, there aren't very many schools, but the town doesn't need more schools, because there aren't very many people there."),
        ('S', "I see. Are there any mountains?"),
        ('J', "No, the whole area is very flat. There are no mountains, but there are a lot of trees. In fact, there are trees on my town's sign, because my town is famous for all the trees on every street."),
        ('S', "Oh, wow. It sounds like a great city."),
    ],
    'gist': ('Whose hometown is bigger?', ["Sarah's", "John's"], "Sarah's"),
    'detail': [
        ("In Sarah's town, there ___ three movie theaters.", ['is', 'are', "aren't"], 'are'),
        ("Sarah: “The thing I like is you can eat any ___ of food.”", ['type', 'place', 'time'], 'type'),
        ("In Sarah's town, there ___ any nightclubs.", ['are', "aren't", 'is'], "aren't"),
        ("In John's town, there ___ a shopping mall.", ['is', "isn't", 'are'], "isn't"),
        ("In the middle of John's town, there is a ___.", ['river', 'lake', 'mall'], 'river'),
    ],
    'times': [  # typed answers
        ("There are about ___ people in Sarah's town.", ['80,000', '80000', '80.000', 'eighty thousand']),
        ("There are only ___ people in John's town.", ['5,000', '5000', '5.000', 'five thousand']),
        ("John's town is famous for its ___.", ['trees', 'tree']),
    ],
}

# ---------------------------------------------------------------- sentence frames
FRAMES = [
    ('There is / are ___ near ___.', ['There is a big park near my home.', 'There are two bus stops near my apartment.']),
    ('One thing I like is ___.', ['One thing I like is my friendly neighbour.', 'One thing I like is the modern gym.']),
    ('It is ___ because ___.', ['It is convenient because there is a bus stop near my home.', 'It is peaceful because there is a big park nearby.']),
    ('The only problem is ___.', ['The only problem is the crowded market.', "The only problem is the bus stop. It's a crowded area."]),
]
LINKERS = ['and', 'but', 'because', 'so', 'however']

# ---------------------------------------------------------------- questions & answers
QA = [
    ('Where do you live?', ['I live in an apartment near the market.', 'I live in a house in a peaceful neighbourhood.']),
    ("What's your neighbourhood like?", ["It's peaceful and convenient.", "It's a crowded area, but it's convenient."]),
    ('Is there a park near your home?', ["Yes, there is. There's a big park near my apartment.", "No, there isn't. However, there is a gym nearby."]),
    ('Are there any nearby facilities?', ['Yes, there are lots of nearby facilities.', "Yes, there's a supermarket, a gym and a hospital."]),
    ('Is your apartment spacious?', ["Yes, it's very spacious.", "No, it isn't, but it's centrally located."]),
    ('What do you like about it?', ['One thing I like is my friendly neighbour.', 'One thing I like is the park. It is peaceful.']),
    ("Is there anything you don't like?", ['The only problem is the crowded market.', "The only problem is the bus stop. It's a crowded area."]),
    ('What are your neighbours like?', ['They are very friendly.', 'I have a friendly neighbour, so I am happy.']),
]

# ---------------------------------------------------------------- model dialogue (Tom & Mai)
DIALOGUE = [
    ('T', "Hi, I'm Tom. I'm your new neighbour."),
    ('M', "Hi Tom, I'm Mai. Welcome to the neighbourhood!"),
    ('T', "Thanks! What's the neighbourhood like?"),
    ('M', "It's very peaceful, and it's centrally located."),
    ('T', "Great. Is there a supermarket near here?"),
    ('M', "Yes, there is. There's a big supermarket near the bus stop."),
    ('T', "Are there any nearby facilities, like a gym?"),
    ('M', "Yes, there are. There's a gym with modern facilities near the park."),
    ('T', "That's convenient. What do you like about the area?"),
    ('M', "One thing I like is the park. It's peaceful because there are lots of trees."),
    ('T', "Is there anything you don't like?"),
    ('M', "The only problem is the market. It's a crowded area at weekends."),
    ('T', "I see. And is your apartment spacious?"),
    ('M', "Not really. However, it's very convenient, so I'm happy here."),
]
DLG_NAMES = {'T': 'Tom', 'M': 'Mai'}
DLG_Q = [
    ('Is there a supermarket near the bus stop?', ['Yes, there is.', "No, there isn't."], 'Yes, there is.'),
    ('Where is the gym?', ['near the park', 'near the market', 'near the hospital'], 'near the park'),
    ('What does Mai like?', ['the park', 'the market', 'the gym'], 'the park'),
    ('What is the only problem?', ['the crowded market', 'the small park', 'the bus stop'], 'the crowded market'),
]

# ---------------------------------------------------------------- pair practice: interview & report
INTERVIEW = [
    ('Where do you live?', '___ lives in ___.'),
    ("What's your neighbourhood like?", "It's ___ and ___."),
    ('Is there a ___ near your home?', "There is / isn't a ___ near ___'s home."),
    ('What do you like about it?', 'One thing ___ likes is ___.'),
    ("Is there anything you don't like?", 'The only problem is ___.'),
]

# ---------------------------------------------------------------- free practice (frame = model dialogue)
SITUATIONS = [
    {'e': '👋', 't': 'A new neighbour', 'a': 'New neighbour', 'b': 'You',
     'goal': 'Ask about the neighbourhood, places and problems.',
     'card': ['Peaceful · centrally located', 'Supermarket near the bus stop', 'Likes: the park', 'Problem: crowded market']},
    {'e': '🏢', 't': 'Looking for an apartment', 'a': 'Renter', 'b': 'Agent',
     'goal': 'Ask about the apartment and the area.',
     'card': ['A spacious apartment', 'Gym with modern facilities', 'Likes: convenient location', 'Problem: a crowded area']},
]
FP_LINES = [
    ('A', "What's the neighbourhood like?"),
    ('B', "It's {adjective} and {adjective}."),
    ('A', 'Is there a {place} near here?'),
    ('B', "{Yes, there is. / No, there isn't.} There's a {place} near the {place}."),
    ('A', 'Are there any nearby facilities?'),
    ('B', "{Yes, there are. / No, there aren't.} There's a {place} with {modern facilities}."),
    ('A', 'What do you like about the area?'),
    ('B', 'One thing I like is {…}. It is {adjective} because {…}.'),
    ('A', "Is there anything you don't like?"),
    ('B', 'The only problem is {…}. However, {…}.'),
]

# ---------------------------------------------------------------- picture task (real-life task)
PIC_FRAMES = ['There is a ___ near ___.', 'There are ___.', 'It is ___ because ___.', 'One thing I like is ___.', 'The only problem is ___.']

# ---------------------------------------------------------------- fluency: 90-second place description
TALK = [
    ('Where', 'I live in ___. It is centrally located / near ___.'),
    ('There is', 'There is ___ near ___. There are ___.'),
    ('I like', 'One thing I like is ___. It is ___ because ___.'),
    ('Problem', 'The only problem is ___. However, ___.'),
    ('Neighbour', 'My neighbour is ___, so ___.'),
]
TALK_MODEL = ("I live in a spacious apartment in a peaceful neighbourhood. It is centrally located. "
              "There is a big park near my home, and there are two bus stops near the market. "
              "There are lots of nearby facilities, like a supermarket and a gym with modern facilities. "
              "One thing I like is the park. It is peaceful because there are lots of trees. "
              "The only problem is the market. It is a crowded area at weekends. However, it is very convenient. "
              "My neighbour is very friendly, so I am happy here.")
FOLLOW_UP = ['Is there a hospital near your home?', 'Are there any cafés?', 'What is your neighbour like?', 'Is it convenient?']

# ---------------------------------------------------------------- game: sentence scramble
SCRAMBLE = [
    'There is a park near my home.',
    'I live in a spacious apartment.',
    'My apartment is centrally located.',
    'There are lots of nearby facilities.',
    'One thing I like is my friendly neighbour.',
    'It is convenient because there is a bus stop.',
    'The only problem is the crowded market.',
    'Is there a supermarket near here?',
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name='There is / are', q='Is there a ___ near ___?', vi_q='Có ___ gần ___ không?',
         a='There is a ___ near ___. / There are ___ near ___.', vi_a='Có một ___ gần ___. / Có (nhiều) ___ gần ___.',
         model='Is there a supermarket near your home?',
         answers=[("Yes, there is. There's a big supermarket near my home.", 'Có. Có một siêu thị lớn gần nhà tôi.'),
                  ("No, there isn't. But there's a market nearby.", 'Không. Nhưng có một cái chợ ở gần đó.'),
                  ('Yes, there are two supermarkets near my apartment.', 'Có, có hai siêu thị gần căn hộ của tôi.')],
         tr=[('Có một phòng gym gần trường của tôi.', 'There is a gym near my school.'),
             ('Có hai trạm xe buýt gần công viên.', 'There are two bus stops near the park.'),
             ('Có bệnh viện nào gần nhà bạn không?', 'Is there a hospital near your home?')]),
    dict(name="What's it like?", q="What's your neighbourhood like?", vi_q='Khu phố của bạn như thế nào?',
         a="It's ___ and ___.", vi_a='Nó ___ và ___.',
         model="What's your neighbourhood like?",
         answers=[("It's peaceful and convenient.", 'Nó yên bình và thuận tiện.'),
                  ("It's a crowded area, but it's centrally located.", 'Đó là một khu vực đông đúc, nhưng nằm ở trung tâm.'),
                  ("It's very peaceful, so I'm happy there.", 'Nó rất yên bình, nên tôi thấy vui khi sống ở đó.')],
         tr=[('Khu phố của tôi đông đúc nhưng thuận tiện.', "My neighbourhood is crowded, but it's convenient."),
             ('Căn hộ của chị tôi rộng rãi và hiện đại.', "My sister's apartment is spacious and modern."),
             ('Khu phố của bạn có yên bình không?', 'Is your neighbourhood peaceful?')]),
    dict(name='One thing I like', q='What do you like about it?', vi_q='Bạn thích điều gì ở đó?',
         a='One thing I like is ___.', vi_a='Một điều tôi thích là ___.',
         model='What do you like about your neighbourhood?',
         answers=[('One thing I like is the park.', 'Một điều tôi thích là công viên.'),
                  ('One thing I like is my friendly neighbour.', 'Một điều tôi thích là người hàng xóm thân thiện của tôi.'),
                  ('One thing I like is the modern gym.', 'Một điều tôi thích là phòng gym hiện đại.')],
         tr=[('Một điều tôi thích là quán cà phê gần nhà tôi.', 'One thing I like is the café near my home.'),
             ('Một điều mẹ tôi thích là khu chợ.', 'One thing my mum likes is the market.'),
             ('Bạn thích điều gì ở căn hộ của bạn?', 'What do you like about your apartment?')]),
    dict(name='The only problem', q="Is there anything you don't like?", vi_q='Có điều gì bạn không thích không?',
         a='The only problem is ___. (It is ___ because ___.)', vi_a='Vấn đề duy nhất là ___. (Nó ___ vì ___.)',
         model="Is there anything you don't like?",
         answers=[('The only problem is the crowded market.', 'Vấn đề duy nhất là khu chợ đông đúc.'),
                  ("The only problem is the bus stop. It's very crowded.", 'Vấn đề duy nhất là trạm xe buýt. Nó rất đông.'),
                  ("Not really. It's a peaceful neighbourhood.", 'Không hẳn. Đó là một khu phố yên bình.')],
         tr=[('Vấn đề duy nhất là căn hộ của tôi. Nó không rộng rãi.', "The only problem is my apartment. It isn't spacious."),
             ('Vấn đề duy nhất là bệnh viện. Nó ở xa đây.', "The only problem is the hospital. It's far from here."),
             ('Nó thuận tiện vì có một trạm xe buýt gần nhà tôi.', "It's convenient because there is a bus stop near my home.")]),
]

# ---------------------------------------------------------------- practice: match the halves
MATCH = [('a spacious', 'apartment'), ('a crowded', 'area'), ('a peaceful', 'neighbourhood'), ('a convenient', 'location'),
         ('nearby', 'facilities'), ('modern', 'facilities'), ('a friendly', 'neighbour'), ('centrally', 'located')]

# ---------------------------------------------------------------- game: memory picture
MEMORY = [  # emoji, sentence
    ('🌳', 'There are three trees.'), ('☕', 'There is a café.'), ('🛒', 'There is a supermarket.'), ('🚏', 'There is a bus stop.'),
    ('🏥', 'There is a hospital.'), ('🚶', 'There are four people.'), ('🏋️', 'There is a gym.'), ('🏫', 'There is a school.'),
]
