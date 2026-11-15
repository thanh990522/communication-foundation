"""Lesson S05 — Directions & Getting Around Town.
Language limited to the S05 syllabus plus the A1 direction basics taught on the 'Direction basics' slide:
  collocations : a famous landmark · a busy intersection · walk two blocks · the main entrance · across from the bank ·
                 on the corner · within walking distance · get to the station
  frames       : What's the best way to get to ___? · Go past ___, then ___. · It is across from ___. · It takes about ___ minutes.
  grammar      : imperatives + sequence markers for multi-step directions
  linkers      : first · then · after that · until · finally
  pronunciation: linking in go‿past, turn‿right · clear stress on landmarks
"""

# ---------------------------------------------------------------- warm-up: where do you go to …?
WARM = [  # place, clue, emoji, IPA
    ('pharmacy', 'buy medicine', '💊', '/ˈfɑːməsi/'),
    ('train station', 'take a train', '🚆', '/ˈtreɪn ˌsteɪʃn/'),
    ('post office', 'send a letter', '📮', '/ˈpəʊst ˌɒfɪs/'),
    ('library', 'borrow books', '📚', '/ˈlaɪbrəri/'),
    ('hospital', 'see a doctor', '🏥', '/ˈhɒspɪtl/'),
    ('bank', 'get money', '🏦', '/bæŋk/'),
    ('supermarket', 'buy food', '🛒', '/ˈsuːpəmɑːkɪt/'),
    ('museum', 'see old things and art', '🏛', '/mjuˈziːəm/'),
]

# ---------------------------------------------------------------- direction basics (A1)
BASICS = [  # phrase, IPA, Vietnamese, example, icon key
    ('turn left', '/tɜːn ˈleft/', 'rẽ trái', 'Turn left at the bank.', 'L'),
    ('turn right', '/tɜːn ˈraɪt/', 'rẽ phải', 'Turn right into High Street.', 'R'),
    ('go straight on', '/ɡəʊ ˈstreɪt ɒn/', 'đi thẳng', 'Go straight on for two blocks.', 'S'),
    ('go past', '/ɡəʊ ˈpɑːst/', 'đi qua', 'Go past the post office.', 'P'),
    ('cross the road', '/ˌkrɒs ðə ˈrəʊd/', 'băng qua đường', 'Cross the road at the intersection.', 'X'),
    ('take the first left', '/teɪk ðə ˌfɜːst ˈleft/', 'rẽ trái ở ngã rẽ đầu tiên', 'Take the first left after the café.', 'F'),
    ('next to', '/ˈnekst tə/', 'bên cạnh', 'The bank is next to the post office.', 'N'),
    ('between', '/bɪˈtwiːn/', 'ở giữa', 'The post office is between the bank and the bookshop.', 'B'),
]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='landmark', w='landmark', pos='noun', ipa='/ˈlændmɑːk/', vi='địa điểm mốc',
         col='a famous landmark', kw='landmark', col_vi='một địa điểm mốc nổi tiếng', ex='The City Museum is a famous landmark.'),
    dict(k='intersection', w='intersection', pos='noun', ipa='/ˌɪntəˈsekʃn/', vi='giao lộ, ngã tư',
         col='a busy intersection', kw='intersection', col_vi='một giao lộ đông đúc', ex='Turn left at the busy intersection.'),
    dict(k='block', w='block', pos='noun', ipa='/blɒk/', vi='dãy phố (đoạn giữa hai ngã tư)',
         col='walk two blocks', kw='blocks', col_vi='đi bộ hai dãy phố', ex='Walk two blocks and turn right.'),
    dict(k='entrance', w='entrance', pos='noun', ipa='/ˈentrəns/', vi='lối vào',
         col='the main entrance', kw='entrance', col_vi='lối vào chính', ex='Meet me at the main entrance of the station.'),
    dict(k='across from', w='across from', pos='preposition', ipa='/əˈkrɒs frəm/', vi='đối diện',
         col='across from the bank', kw='across from', col_vi='đối diện ngân hàng', ex='The library is across from the bank.'),
    dict(k='on the corner', w='on the corner', pos='phrase', ipa='/ɒn ðə ˈkɔːnə/', vi='ở góc đường',
         col='on the corner of High Street', kw='on the corner', col_vi='ở góc đường High', ex='The café is on the corner of Market Street and High Street.'),
    dict(k='within walking distance', w='within walking distance', pos='phrase', ipa='/wɪˈðɪn ˈwɔːkɪŋ ˌdɪstəns/', vi='trong khoảng cách đi bộ',
         col='within walking distance', kw='walking distance', col_vi='đi bộ đến được', ex='The hospital is within walking distance.'),
    dict(k='get to', w='get to', pos='verb', ipa='/ˈɡet tə/', vi='đi đến, tới',
         col='get to the station', kw='get to', col_vi='đi đến nhà ga', ex='How do I get to the station?'),
]

# ---------------------------------------------------------------- the town map (shared by four slides)
# streets: vertical x=150 Station Road · x=350 Market Street · x=550 Church Street
#          horizontal y=110 Park Road · y=250 High Street · y=390 River Road
PLACES = {  # id: (label, emoji, x0, y0, x1, y1)
    'park': ('Park', '🌳', 174, 6, 326, 86),
    'library': ('Library', '📚', 6, 134, 126, 226),
    'bank': ('Bank', '🏦', 174, 168, 222, 226),
    'post': ('Post office', '📮', 228, 168, 276, 226),
    'bookshop': ('Bookshop', '📖', 282, 168, 326, 226),
    'museum': ('City Museum', '🏛', 374, 134, 526, 226),
    'cinema': ('Cinema', '🎬', 574, 168, 652, 226),
    'school': ('School', '🏫', 6, 274, 126, 316),
    'pharmacy': ('Pharmacy', '💊', 66, 324, 126, 366),
    'supermarket': ('Supermarket', '🛒', 174, 314, 250, 366),
    'cafe': ('Café', '☕', 270, 274, 326, 310),
    'hospital': ('Hospital', '🏥', 374, 274, 526, 366),
    'hotel': ('Hotel', '🏨', 574, 274, 694, 366),
    'station': ('Train station', '🚆', 20, 412, 130, 456),
}
START = (70, 390)   # in front of the train station, on River Road

# follow-the-route slide: each step reveals text and moves the marker through its points
ROUTES = [
    dict(to='cafe', title='Route 1', steps=[
        ('First, go out of the station and turn right.', []),
        ('Then go along River Road. Go past the pharmacy and the supermarket.', [(350, 390)]),
        ('After that, turn left into Market Street.', [(350, 372)]),
        ('Walk until you get to the corner.', [(350, 292)]),
        ('Finally, it is on your left, on the corner of Market Street and High Street.', [])]),
    dict(to='cinema', title='Route 2', steps=[
        ('First, go out of the station and turn right.', []),
        ('Then go straight on along River Road until you get to Church Street. That is the third intersection.', [(550, 390)]),
        ('After that, turn left into Church Street and go past the hotel.', [(550, 250)]),
        ('Cross High Street.', [(550, 214)]),
        ('Finally, it is on the corner, on your right.', [])]),
    dict(to='library', title='Route 3', steps=[
        ('First, go out of the station and turn right.', []),
        ('At the first intersection, turn left into Station Road.', [(150, 390)]),
        ('Then go straight on. Go past the pharmacy and cross High Street.', [(150, 250), (150, 196)]),
        ('Finally, it is on your left. It is across from the bank.', [])]),
    dict(to='bookshop', title='Route 4', steps=[
        ('First, go out of the station and turn right.', []),
        ('Then walk two blocks along River Road and turn left into Market Street.', [(350, 390)]),
        ('After that, go past the café until you get to High Street.', [(350, 250)]),
        ('Cross High Street.', [(350, 214)]),
        ('Finally, it is on the corner, on your left. It is across from the café.', [])]),
]

# where-is-it check (map) — answers match the map
MAPQ = [
    ('The bank is ___ the corner of Station Road and High Street.', ['on', 'in', 'at'], 'on'),
    ('The post office is ___ the bank and the bookshop.', ['between', 'across from', 'on the corner'], 'between'),
    ('The City Museum is ___ the hospital.', ['across from', 'next to', 'between'], 'across from'),
    ('The pharmacy is ___ the supermarket.', ['across from', 'next to', 'between'], 'across from'),
    ('The café is on the ___ of Market Street and High Street.', ['corner', 'entrance', 'block'], 'corner'),
    ('The main ___ of the museum is on High Street.', ['entrance', 'corner', 'block'], 'entrance'),
    ('The hospital is ___ walking distance of the station.', ['within', 'on', 'across'], 'within'),
]

# ---------------------------------------------------------------- order the steps (linkers)
ORDER = [
    dict(title='Hotel → City Museum', steps=[
        'First, go out of the hotel and turn left.',
        'Then go straight on for two blocks.',
        'After that, turn right at the bank.',
        'Walk along High Street until you get to the post office.',
        'Finally, the museum is on your left, across from the hospital.']),
    dict(title='School → train station', steps=[
        'First, cross the road at the intersection.',
        'Then go past the park and the café.',
        'After that, take the first left.',
        'Walk straight on until you get to River Road.',
        "Finally, the station is on your right. You can't miss it."]),
]
LINKERS = ['first', 'then', 'after that', 'until', 'finally']

# ---------------------------------------------------------------- pronunciation: linking + word stress
LINKS = [  # shown with ‿, spoken plain
    'go‿past the bank', 'turn‿right at the café', 'turn‿left into Station Road', 'walk‿along River Road',
    "it's‿across from the park", 'get‿to the station', 'it takes‿about ten minutes',
]
STRESS = [  # word, syllables, stressed index, IPA
    ('landmark', ['land', 'mark'], 0, '/ˈlændmɑːk/'),
    ('intersection', ['in', 'ter', 'sec', 'tion'], 2, '/ˌɪntəˈsekʃn/'),
    ('entrance', ['en', 'trance'], 0, '/ˈentrəns/'),
    ('supermarket', ['su', 'per', 'mar', 'ket'], 0, '/ˈsuːpəmɑːkɪt/'),
    ('hospital', ['hos', 'pi', 'tal'], 0, '/ˈhɒspɪtl/'),
    ('museum', ['mu', 'se', 'um'], 1, '/mjuˈziːəm/'),
    ('library', ['li', 'bra', 'ry'], 0, '/ˈlaɪbrəri/'),
    ('pharmacy', ['phar', 'ma', 'cy'], 0, '/ˈfɑːməsi/'),
    ('hotel', ['ho', 'tel'], 1, '/həʊˈtel/'),
    ('between', ['be', 'tween'], 1, '/bɪˈtwiːn/'),
]

# ---------------------------------------------------------------- listening (real recording)
LISTEN = {
    'title': 'How to get to my house — Todd',
    'source': 'elllo.org · SixPix #12 Directions (Todd Beuckens) · © elllo productions',
    'page': 'https://www.elllo.org/english/sixpix/G012-Directions.html',
    'file': 'Listening/S05_listening_Todd_directions.mp3',
    'dur': 198,
    'names': {'T': 'Todd'},
    'script': [
        ('T', "OK, here is how to get to my house from the train station. Go out of the train station and turn left. Go about half a block and you will see a pub. At that intersection, turn right and go down that street for about three and a half blocks."),
        ('T', "Go past the post office, and you'll go past a river, and past a hospital, and the first road past the hospital, you want to turn right. Go down that block two houses and you'll see my house on the right. It's the second house on the right and it's right next to the petrol station."),
        ('T', "OK, if I'm not home, then just go to my friend's house, so I might be busy at work, so in that case, from my house turn right down the street and go past the gas station and keep going straight until you get to a bookstore. At the bookstore, turn right and go down the street until you get to the river."),
        ('T', "Go across the river and right across the river, my friend's house will be on the right-hand side. It is the first house across the river and it's right next to a 7-11."),
        ('T', "OK, if my friend's not home then just go and wait for me at Miki's Tavern. So, from my friend's house, go out and turn left. So go towards the river and turn left. Go past 7-11 and keep going down the road and go past the cafe and you will see a garden."),
        ('T', "The garden has a pathway that goes through it so go left into the garden and walk through the garden to the street on the other side. When you get to the other side, turn right. Go past the post office and past the intersection, keep going and you will see a police station on the right."),
        ('T', "Go all the way to the end of the street. At that street, at the end of the street, turn left. Go down the street and Miki's Tavern is on the corner. It will be the second building on your left. You can't miss it."),
    ],
    'gist': ('Todd and his friend are not home. Where do you wait for Todd?', ["at Miki's Tavern", 'at the train station'], "at Miki's Tavern"),
    'detail': [
        ('Out of the train station, first turn ___.', ['left', 'right', 'straight on'], 'left'),
        ('At the pub, turn right and go about ___ blocks.', ['two and a half', 'three and a half', 'four'], 'three and a half'),
        ("Todd's house is right next to the ___.", ['petrol station', 'post office', 'hospital'], 'petrol station'),
        ("His friend's house is the first house across the ___.", ['river', 'road', 'garden'], 'river'),
        ('On the way to the tavern, you walk through a ___.', ['garden', 'park', 'station'], 'garden'),
    ],
    'times': [
        ("Todd's house is the ___ house on the right.", ['second', '2nd', '2']),
        ("His friend's house is next to a ___.", ['7-11', '711', '7-eleven', '7eleven', 'seven eleven', 'seveneleven']),
        ("Miki's Tavern is on the ___.", ['corner', 'the corner']),
    ],
}

# ---------------------------------------------------------------- model dialogue (asking the way at the station)
DIALOGUE = [
    ('T', "Excuse me. What's the best way to get to the City Museum?"),
    ('L', "The museum? It's within walking distance. It takes about ten minutes."),
    ('T', 'Great. How do I get there?'),
    ('L', 'First, go out of the station and turn right. Then turn left into Station Road.'),
    ('T', 'Turn left into Station Road. OK.'),
    ('L', "Go straight on until you get to High Street. That's the first intersection. Then turn right."),
    ('T', 'Right at High Street.'),
    ('L', 'After that, go past the bank and the post office, then cross Market Street.'),
    ('T', 'Go past the bank, then cross Market Street.'),
    ('L', "Finally, the museum is on your left. It's across from the hospital. You can't miss it. It's a famous landmark."),
    ('T', 'Is the main entrance on High Street?'),
    ('L', 'Yes, it is. The main entrance is on High Street.'),
    ('T', 'Thank you so much!'),
    ('L', "You're welcome. Enjoy the museum!"),
]
DLG_NAMES = {'T': 'Tourist', 'L': 'Local'}
DLG_Q = [
    ('How long does it take to walk to the museum?', ['about ten minutes', 'about twenty minutes'], 'about ten minutes'),
    ('Where is the main entrance?', ['on High Street', 'on Market Street', 'on Station Road'], 'on High Street'),
]
CARD = [('Destination', 'City Museum', ['museum', 'citymuseum', 'thecitymuseum', 'themuseum']),
        ('It takes about', '10 minutes', ['10', '10minutes', 'ten', 'tenminutes', '10mins']),
        ('Turn left into', 'Station Road', ['stationroad', 'station']),
        ('Across from', 'the hospital', ['hospital', 'thehospital'])]

# ---------------------------------------------------------------- speaking: secret destination
STARTS = ['the train station ★', 'the hotel', 'the school', 'the cinema', 'the park', 'the hospital']

# ---------------------------------------------------------------- real-life task: my home → a nearby place
PLAN_MODEL = [
    'First, go out of my building and turn left.',
    'Then walk two blocks and go past the pharmacy.',
    'After that, turn right at the busy intersection.',
    'Go straight on until you get to the park.',
    "Finally, the supermarket is on the corner, across from the bank. It takes about eight minutes.",
]

# ---------------------------------------------------------------- game: listen & find (spoken directions from the station)
GAME = [  # spoken directions, answer place id
    ("Go out of the station and turn right. Turn left into Station Road. Go straight on until you get to High Street, then turn right. "
     "Go past the bank and the post office, and cross Market Street. It's on your left, across from the hospital.", 'museum'),
    ("Go out of the station and turn right. Turn left into Station Road and walk one block to High Street. Turn right and go past the bank. "
     "It's on your left, between the bank and the bookshop.", 'post'),
    ("Go out of the station and turn right. Turn left into Station Road. Go straight on until you get to Park Road. Turn right. "
     "It's on your left. It takes about ten minutes.", 'park'),
    ("Go out of the station and turn right. Go along River Road. Go past the supermarket and cross Market Street. "
     "It's on your left. It's within walking distance.", 'hospital'),
    ("Go out of the station and turn right. Walk along River Road and go past the hospital. Turn left into Church Street. It's on your right.", 'hotel'),
    ("Go out of the station and turn right. Turn left into Station Road. Go past the pharmacy. It's on your left, before High Street.", 'school'),
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name="What's the best way…?", q="What's the best way to get to ___?", vi_q='Cách tốt nhất để đến ___ là gì?',
         a="It's within walking distance. / Take the bus…", vi_a='Nó ở trong khoảng cách đi bộ. / Hãy đi xe buýt…',
         model="What's the best way to get to the museum?",
         answers=[("It's within walking distance. Just walk two blocks.", 'Nó ở trong khoảng cách đi bộ. Chỉ cần đi bộ hai dãy phố.'),
                  ('The best way is by bus. Take bus number 15.', 'Cách tốt nhất là đi xe buýt. Hãy đi xe buýt số 15.'),
                  ('Walk to the intersection and turn left.', 'Đi bộ đến giao lộ rồi rẽ trái.')],
         tr=[('Cách tốt nhất để đến bệnh viện là gì?', "What's the best way to get to the hospital?"),
             ('Cách tốt nhất để đến khách sạn của bạn là gì?', "What's the best way to get to your hotel?"),
             ('Cách tốt nhất là đi bộ. Nó ở trong khoảng cách đi bộ.', "The best way is to walk. It's within walking distance.")]),
    dict(name='Go past …, then …', q='Go past ___, then ___.', vi_q='Đi qua ___, rồi ___.',
         a='first → then → after that → until → finally', vi_a='trước tiên → rồi → sau đó → cho đến khi → cuối cùng',
         model='How do I get to the café?',
         answers=[('Go past the post office, then turn right.', 'Đi qua bưu điện, rồi rẽ phải.'),
                  ('Go past the park, then cross the road.', 'Đi qua công viên, rồi băng qua đường.'),
                  ('First, go past the bank. Then go straight on until you get to the corner.', 'Trước tiên, đi qua ngân hàng. Rồi đi thẳng cho đến khi bạn tới góc đường.')],
         tr=[('Đi qua siêu thị, rồi rẽ trái.', 'Go past the supermarket, then turn left.'),
             ('Đi qua bệnh viện, rồi đi bộ hai dãy phố.', 'Go past the hospital, then walk two blocks.'),
             ('Đi qua ngân hàng, rồi băng qua đường ở giao lộ.', 'Go past the bank, then cross the road at the intersection.')]),
    dict(name='It is across from …', q='Where is the ___? — It is across from ___.', vi_q='___ ở đâu? — Nó ở đối diện ___.',
         a="It's across from ___. / It's on the corner of ___.", vi_a='Nó ở đối diện ___. / Nó ở góc đường ___.',
         model="Where's the bank?",
         answers=[("It's across from the library.", 'Nó ở đối diện thư viện.'),
                  ("It's on the corner of Station Road and High Street.", 'Nó ở góc đường Station và đường High.'),
                  ("It's next to the post office.", 'Nó ở cạnh bưu điện.')],
         tr=[('Khách sạn ở đối diện bệnh viện.', 'The hotel is across from the hospital.'),
             ('Lối vào chính ở đối diện công viên.', 'The main entrance is across from the park.'),
             ('Quán cà phê ở góc đường, đối diện hiệu sách.', 'The café is on the corner, across from the bookshop.')]),
    dict(name='It takes about … minutes', q='How long does it take? — It takes about ___ minutes.', vi_q='Mất bao lâu? — Mất khoảng ___ phút.',
         a='It takes about ___ minutes (on foot / by bus).', vi_a='Mất khoảng ___ phút (đi bộ / đi xe buýt).',
         model='How long does it take to get to the station?',
         answers=[('It takes about five minutes on foot.', 'Mất khoảng năm phút đi bộ.'),
                  ('It takes about twenty minutes by bus.', 'Mất khoảng hai mươi phút đi xe buýt.'),
                  ("Not long. It's within walking distance.", 'Không lâu đâu. Nó ở trong khoảng cách đi bộ.')],
         tr=[('Mất khoảng mười phút để đến bảo tàng.', 'It takes about ten minutes to get to the museum.'),
             ('Mất bao lâu để đi bộ đến trường?', 'How long does it take to walk to the school?'),
             ('Mất khoảng mười lăm phút đi bộ từ nhà tôi.', 'It takes about fifteen minutes on foot from my home.')]),
]
