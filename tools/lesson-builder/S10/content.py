"""Lesson S10 — Past Events: What Happened?
Language limited to the S10 syllabus (+ simple A1 words already known):
  collocations : attend an event · visit a local market · stay overnight · return home · enjoy the experience ·
                 feel exhausted · a memorable trip · a weekend event
  frames       : Last weekend, I ___. · I had a chance to ___. · The best part was ___. · I was ___, but it was worth it.
  grammar      : past simple affirmative and negative
  linkers      : first · then · after that · although · in the end
  pronunciation: -ed endings /t/ /d/ /ɪd/ · high-frequency irregular forms
"""

# ---------------------------------------------------------------- warm-up: weekend photos
PHOTOS = [
    ('🛒', 'Last weekend, I visited a local market.'),
    ('🎉', 'Last weekend, I attended a weekend event.'),
    ('🏨', 'Last weekend, I stayed overnight in a small hotel.'),
    ('🍜', 'Last weekend, I ate street food with my friends.'),
    ('📸', 'Last weekend, I took lots of photos.'),
    ('🌊', 'Last weekend, I went to the beach.'),
    ('🎬', 'Last weekend, I watched a film at home.'),
    ('😴', 'Last weekend, I felt exhausted, so I slept a lot.'),
]

# ---------------------------------------------------------------- input: verb time machine (present -> past)
REGULAR = [('visit', 'visited', '/ˈvɪzɪtɪd/'), ('stay', 'stayed', '/steɪd/'), ('enjoy', 'enjoyed', '/ɪnˈdʒɔɪd/'),
           ('return', 'returned', '/rɪˈtɜːnd/'), ('attend', 'attended', '/əˈtendɪd/'), ('walk', 'walked', '/wɔːkt/')]
IRREGULAR = [('go', 'went', '/went/'), ('have', 'had', '/hæd/'), ('eat', 'ate', '/eɪt/'), ('take', 'took', '/tʊk/'),
             ('see', 'saw', '/sɔː/'), ('buy', 'bought', '/bɔːt/'), ('feel', 'felt', '/felt/'), ('meet', 'met', '/met/'),
             ('get', 'got', '/ɡɒt/'), ('do', 'did', '/dɪd/'), ('be', 'was / were', '/wɒz/ /wɜː/'), ('sleep', 'slept', '/slept/')]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='attend', w='attend', pos='verb', ipa='/əˈtend/', vi='tham dự',
         col='attend an event', kw='attend', col_vi='tham dự một sự kiện', ex='Last Saturday, I attended an event in the city centre.'),
    dict(k='visit', w='visit', pos='verb', ipa='/ˈvɪzɪt/', vi='ghé thăm',
         col='visit a local market', kw='visit', col_vi='ghé thăm chợ địa phương', ex='On Sunday morning, we visited a local market.'),
    dict(k='stay', w='stay', pos='verb', ipa='/steɪ/', vi='ở lại',
         col='stay overnight', kw='stay', col_vi='ở lại qua đêm', ex='We stayed overnight in a small hotel.'),
    dict(k='return', w='return', pos='verb', ipa='/rɪˈtɜːn/', vi='trở về',
         col='return home', kw='return', col_vi='trở về nhà', ex='We returned home on Sunday evening.'),
    dict(k='enjoy', w='enjoy', pos='verb', ipa='/ɪnˈdʒɔɪ/', vi='thích, tận hưởng',
         col='enjoy the experience', kw='enjoy', col_vi='tận hưởng trải nghiệm', ex='It was my first trip alone, and I really enjoyed the experience.'),
    dict(k='exhausted', w='exhausted', pos='adjective', ipa='/ɪɡˈzɔːstɪd/', vi='kiệt sức',
         col='feel exhausted', kw='exhausted', col_vi='cảm thấy kiệt sức', ex='After the long walk, I felt exhausted.'),
    dict(k='memorable', w='memorable', pos='adjective', ipa='/ˈmemərəbl/', vi='đáng nhớ',
         col='a memorable trip', kw='memorable', col_vi='một chuyến đi đáng nhớ', ex='Our trip to Da Lat was a memorable trip.'),
    dict(k='event', w='event', pos='noun', ipa='/ɪˈvent/', vi='sự kiện',
         col='a weekend event', kw='event', col_vi='một sự kiện cuối tuần', ex='There was a big weekend event at the park.'),
]

# ---------------------------------------------------------------- pronunciation: -ed endings
ED_RULES = [('/t/', 'after p, k, s, sh, ch, f', 'walked · booked · missed · watched'),
            ('/d/', 'after voiced sounds & vowels', 'stayed · enjoyed · returned · played'),
            ('/ɪd/', 'after t and d', 'visited · attended · waited · needed')]
ED_WORDS = [('walked', '/t/'), ('stayed', '/d/'), ('visited', '/ɪd/'), ('enjoyed', '/d/'), ('booked', '/t/'), ('attended', '/ɪd/'),
            ('returned', '/d/'), ('missed', '/t/'), ('waited', '/ɪd/'), ('watched', '/t/'), ('played', '/d/'), ('needed', '/ɪd/')]

# ---------------------------------------------------------------- listening (real recording, played from the source)
LISTEN = {
    'title': 'How was your trip? — talking about a holiday',
    'source': 'Oxford Online English · “Talking About Holidays” listening lesson (A2)',
    'page': 'https://www.oxfordonlineenglish.com/talking-about-holidays',
    'url': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2021/04/Talking-about-holidays-full.mp3',
    'url_slow': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2021/04/Talking-about-holidays-25pc.mp3',
    'dur': 45,
    'gloss': '🆕 holiday of a lifetime = kỳ nghỉ tuyệt nhất đời · coast = bờ biển · souvenir = quà lưu niệm',
    'gist': ('How was her trip?', ['It was amazing.', 'It was boring.'], 'It was amazing.'),
    'detail': [
        ('Where did she go?', ['Pisa and Cinque Terre', 'Venice', 'Rome'], 'Pisa and Cinque Terre'),
        ('What can you do there?', ['swim and walk in the hills', 'go shopping', 'visit museums'], 'swim and walk in the hills'),
        ('Did she speak Italian?', ['No, not really.', 'Yes, a lot.'], 'No, not really.'),
        ('Why do people there speak English?', ['lots of tourists', 'English films', 'English schools'], 'lots of tourists'),
        ('Did she bring back an Italian boyfriend?', ['No, of course not!', 'Yes, she did.'], 'No, of course not!'),
    ],
    'times': [
        ('It was amazing! Holiday of a ___!', ['lifetime']),
        ('No! Where did you ___ that idea?', ['get']),
        ('I bet the ___ was good, though.', ['food']),
    ],
}

# ---------------------------------------------------------------- model dialogue: Monday morning
DIALOGUE = [
    ('A', 'Hi Nam! How was your weekend?'),
    ('N', 'It was great, thanks. Last weekend, I visited Da Lat with my family.'),
    ('A', 'Wow! Tell me about it.'),
    ('N', 'First, we visited a local market. Then we attended a weekend event. It was a flower festival.'),
    ('A', 'That sounds lovely.'),
    ('N', 'After that, we stayed overnight in a small hotel near the lake. I had a chance to try some local food.'),
    ('A', 'Nice! What was the best part?'),
    ('N', 'The best part was the night market. I really enjoyed the experience.'),
    ('A', 'And the weather?'),
    ('N', "It was cold, and it rained on Sunday morning, so we didn't go to the waterfall."),
    ('A', 'Oh no!'),
    ('N', 'Although it rained, it was a memorable trip. In the end, we returned home on Sunday evening.'),
    ('A', 'You look tired.'),
    ('N', 'Yes, I was exhausted, but it was worth it!'),
]
DLG_NAMES = {'A': 'Anna', 'N': 'Nam'}
DLG_Q = [
    ("Why didn't they go to the waterfall?", ['It rained.', 'It was closed.'], 'It rained.'),
    ('How did Nam feel at the end?', ['exhausted but happy', 'bored and angry'], 'exhausted but happy'),
]
CARD = [('City', 'Da Lat', ['dalat', 'đàlạt']), ('Event', 'a flower festival', ['flowerfestival', 'aflowerfestival', 'festival']),
        ('Best part', 'the night market', ['nightmarket', 'thenightmarket']), ('Returned', 'Sunday evening', ['sundayevening', 'onsundayevening', 'sunday'])]

# ---------------------------------------------------------------- speaking: build my weekend story
STORY_EVENTS = [('🛒', 'visited a local market'), ('🎉', 'attended a weekend event'), ('🏨', 'stayed overnight with friends'),
                ('🍜', 'ate street food'), ('📸', 'took lots of photos'), ('👨‍👩‍👧', 'met my cousins'), ('🎬', 'watched a film'),
                ('🌊', 'went to the beach'), ('🛍', 'bought some souvenirs'), ('🏠', 'returned home late')]
ALTHOUGH = ['it rained', 'it was very hot', 'the bus was late', 'I was tired']

# ---------------------------------------------------------------- speaking: two truths and a lie
TRUTH_TOPICS = ['last weekend', 'yesterday', 'last Sunday', 'last summer', 'your last trip', 'last night']

# ---------------------------------------------------------------- 90-second talk: six past verbs
TALK_VERBS = ['went', 'visited', 'stayed', 'ate', 'saw', 'enjoyed', 'took', 'met', 'had', 'returned', 'felt', 'was', 'bought', "didn't"]

# ---------------------------------------------------------------- game: irregular quick-fire
QUICK = [('go', ['went']), ('have', ['had']), ('eat', ['ate']), ('take', ['took']), ('see', ['saw']), ('buy', ['bought']),
         ('feel', ['felt']), ('meet', ['met']), ('get', ['got']), ('do', ['did']), ('sleep', ['slept']), ('be (I)', ['was'])]

# ---------------------------------------------------------------- real-life task: yesterday card
YESTERDAY = [('🌅', 'Yesterday morning, I ___.'), ('☀️', 'In the afternoon, I ___.'), ('🌙', "In the evening, I didn't ___."),
             ('⭐', 'The best part was ___.')]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name='Last weekend, I…', q='Last weekend, I ___.', vi_q='Cuối tuần trước, tôi đã ___.',
         a='Really? That sounds fun!', vi_a='Thật à? Nghe vui đấy!',
         model='How was your weekend?',
         answers=[('Last weekend, I visited a local market.', 'Cuối tuần trước, tôi đã đi chợ địa phương.'),
                  ('Last weekend, I attended a weekend event in the park.', 'Cuối tuần trước, tôi đã tham dự một sự kiện ở công viên.'),
                  ("Last weekend, I stayed at home. I didn't go out.", 'Cuối tuần trước, tôi ở nhà. Tôi đã không ra ngoài.')],
         tr=[('Cuối tuần trước, tôi đã về quê.', 'Last weekend, I returned to my hometown.'),
             ('Cuối tuần trước, tôi đã gặp anh họ của tôi.', 'Last weekend, I met my cousin.'),
             ('Cuối tuần trước, tôi đã không đi làm.', "Last weekend, I didn't go to work.")]),
    dict(name='I had a chance to…', q='I had a chance to ___.', vi_q='Tôi đã có cơ hội ___.',
         a='Wow! How was it?', vi_a='Ồ! Nó thế nào?',
         model='Did you do anything special?',
         answers=[('I had a chance to try some local food.', 'Tôi đã có cơ hội thử đồ ăn địa phương.'),
                  ('I had a chance to visit a local market.', 'Tôi đã có cơ hội ghé thăm chợ địa phương.'),
                  ('I had a chance to stay overnight on a boat.', 'Tôi đã có cơ hội ngủ qua đêm trên thuyền.')],
         tr=[('Tôi đã có cơ hội tham dự một sự kiện lớn.', 'I had a chance to attend a big event.'),
             ('Tôi đã có cơ hội gặp bạn cũ.', 'I had a chance to meet my old friends.'),
             ('Tôi đã có cơ hội chụp nhiều ảnh.', 'I had a chance to take lots of photos.')]),
    dict(name='The best part was…', q='The best part was ___.', vi_q='Phần hay nhất là ___.',
         a='That sounds great!', vi_a='Nghe tuyệt quá!',
         model='What was the best part?',
         answers=[('The best part was the night market.', 'Phần hay nhất là chợ đêm.'),
                  ('The best part was the food.', 'Phần hay nhất là đồ ăn.'),
                  ('The best part was the weekend event.', 'Phần hay nhất là sự kiện cuối tuần.')],
         tr=[('Phần hay nhất là bãi biển.', 'The best part was the beach.'),
             ('Phần hay nhất là gặp gia đình tôi.', 'The best part was meeting my family.'),
             ('Đó là một chuyến đi đáng nhớ.', 'It was a memorable trip.')]),
    dict(name='I was…, but it was worth it.', q="I was ___, but it was worth it.", vi_q='Tôi đã ___, nhưng nó rất xứng đáng.',
         a='I am happy for you!', vi_a='Tôi mừng cho bạn!',
         model='You look tired!',
         answers=[('I was exhausted, but it was worth it.', 'Tôi đã kiệt sức, nhưng rất xứng đáng.'),
                  ('I was tired, but it was worth it.', 'Tôi đã mệt, nhưng rất xứng đáng.'),
                  ('I was very busy, but it was worth it.', 'Tôi đã rất bận, nhưng rất xứng đáng.')],
         tr=[('Tôi đã kiệt sức, nhưng nó rất xứng đáng.', 'I was exhausted, but it was worth it.'),
             ('Tôi đã rất mệt, nhưng tôi thích trải nghiệm đó.', 'I was very tired, but I enjoyed the experience.'),
             ('Chúng tôi trở về nhà lúc nửa đêm.', 'We returned home at midnight.')]),
]
