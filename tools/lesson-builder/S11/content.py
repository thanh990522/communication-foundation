"""Lesson S11 — Past Questions & Storytelling.
Language limited to the S11 syllabus (+ S10 past simple and simple A1 words):
  collocations : something happened · suddenly realise · fortunately find · miss the bus · realise the mistake ·
                 decide to wait · eventually arrive · while travelling
  frames       : You'll never guess what happened. · While I was ___, ___. · What happened next? · In the end, ___.
  grammar      : past simple questions with did / was / were + sequencing
  linkers      : at first · while · suddenly · fortunately · eventually · in the end
  pronunciation: intonation in follow-up questions · pausing after sequence markers
"""

# ---------------------------------------------------------------- warm-up: guess the story (3 clues)
CLUES = [
    (['🏃', '🚌💨', '😩'], 'I ran to the bus stop, but I missed the bus.'),
    (['✈️', '🧳', '😱'], 'I got off the plane, and suddenly I realised my bag was still on it.'),
    (['☔', '🙅', '🥶'], "It rained, and I didn't have an umbrella."),
    (['📱', '🔍', '😅'], 'I lost my phone, but fortunately I found it in my bag.'),
    (['🚗', '⏳', '🏁'], 'There was a lot of traffic, but eventually we arrived.'),
    (['🎂', '😮', '🎉'], 'I came home and suddenly my friends shouted “Surprise!”'),
]

# ---------------------------------------------------------------- input: story mountain
MOUNTAIN = [
    ('At first', 'At first, everything was fine. I left home at eight.'),
    ('While', 'While I was walking to the bus stop, it started to rain.'),
    ('Suddenly', 'Suddenly, I realised I didn’t have my phone.'),
    ('Fortunately', 'Fortunately, I found it in my bag.'),
    ('Eventually', 'I missed the bus, so I decided to wait. Eventually, the next bus came.'),
    ('In the end', 'In the end, I arrived at work at ten. What a morning!'),
]

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='happen', w='happen', pos='verb', ipa='/ˈhæpən/', vi='xảy ra',
         col='something happened', kw='happen', col_vi='có chuyện đã xảy ra', ex="You'll never guess what happened yesterday!"),
    dict(k='suddenly', w='suddenly', pos='adverb', ipa='/ˈsʌdənli/', vi='đột nhiên',
         col='suddenly realise', kw='suddenly', col_vi='đột nhiên nhận ra', ex='Suddenly, I realised my bag was on the bus.'),
    dict(k='fortunately', w='fortunately', pos='adverb', ipa='/ˈfɔːtʃənətli/', vi='may mắn thay',
         col='fortunately find', kw='fortunately', col_vi='may mắn tìm thấy', ex='Fortunately, I found my wallet in my jacket.'),
    dict(k='miss', w='miss', pos='verb', ipa='/mɪs/', vi='lỡ, bỏ lỡ',
         col='miss the bus', kw='miss', col_vi='lỡ chuyến xe buýt', ex='I got up late and missed the bus.'),
    dict(k='realise', w='realise', pos='verb', ipa='/ˈrɪəlaɪz/', vi='nhận ra',
         col='realise the mistake', kw='realise', col_vi='nhận ra lỗi sai', ex='At the station, I realised the mistake. It was the wrong train!'),
    dict(k='decide', w='decide', pos='verb', ipa='/dɪˈsaɪd/', vi='quyết định',
         col='decide to wait', kw='decide', col_vi='quyết định chờ', ex='The bus was late, so we decided to wait.'),
    dict(k='eventually', w='eventually', pos='adverb', ipa='/ɪˈventʃuəli/', vi='cuối cùng (sau một thời gian dài)',
         col='eventually arrive', kw='eventually', col_vi='cuối cùng cũng đến nơi', ex='We waited for an hour. Eventually, the train arrived.'),
    dict(k='while', w='while', pos='conjunction', ipa='/waɪl/', vi='trong khi',
         col='while travelling', kw='while', col_vi='trong khi đi du lịch', ex='I lost my phone while travelling in Hue.'),
]

# ---------------------------------------------------------------- pronunciation: follow-up questions + pauses
FOLLOW = [('What happened next?', '↘'), ('Where were you?', '↘'), ('Did you miss the bus?', '↗'), ('Were you OK?', '↗'),
          ('How did you get home?', '↘'), ('Did you find it?', '↗')]
PAUSES = ['At first, | everything was fine.', 'Suddenly, | I realised the mistake.', 'Fortunately, | I found my phone.',
          'Eventually, | the bus arrived.', 'In the end, | I got home at ten.']

# ---------------------------------------------------------------- listening (real recording, played from the source)
LISTEN = {
    'title': 'Lost property — at the airport',
    'source': 'Oxford Online English · “Baggage Reclaim” listening lesson (A1–A2)',
    'page': 'https://www.oxfordonlineenglish.com/baggage-reclaim-listening-lesson-a1-a2',
    'url': 'https://www.oxfordonlineenglish.com/wp-content/uploads/2025/08/baggage-reclaim_2a_full_with-sfx.mp3',
    'url_slow': '',
    'dur': 48,
    'gloss': '🆕 lost property = đồ thất lạc · suitcase = vali · overhead locker = ngăn hành lý trên đầu · get off = xuống (máy bay)',
    'gist': ('What happened to the woman?', ['She lost her bag.', 'She missed her flight.'], 'She lost her bag.'),
    'detail': [
        ('Where is the help desk?', ['at baggage reclaim', 'at check-in', 'on the plane'], 'at baggage reclaim'),
        ('What does her bag look like?', ['small, green, with wheels', 'big and black', 'small and blue'], 'small, green, with wheels'),
        ('Where did she leave it?', ['on the plane', 'in a taxi', 'at the hotel'], 'on the plane'),
        ('Did she check the bag in?', ['No, hand luggage only.', 'Yes, she did.'], 'No, hand luggage only.'),
        ('What does the man ask at the end?', ['Which flight were you on?', "What's your name?", 'Where do you live?'], 'Which flight were you on?'),
    ],
    'times': [
        ('I think I ___ it on the plane.', ['left']),
        ('I remember I ___ it down from the overhead locker.', ['took']),
        ('Then I somehow got ___ the plane without it.', ['off']),
    ],
}

# ---------------------------------------------------------------- model dialogue: a bad morning
DIALOGUE = [
    ('L', "Tom! You'll never guess what happened this morning."),
    ('T', 'Oh no. What happened?'),
    ('L', 'At first, everything was fine. I left home at eight, as usual.'),
    ('T', 'And then?'),
    ('L', 'While I was walking to the bus stop, it started to rain. I ran, but I missed the bus.'),
    ('T', 'Oh no! What happened next?'),
    ('L', "Suddenly, I realised I didn't have my phone. I was so worried!"),
    ('T', 'Did you go back home?'),
    ('L', 'No, I didn’t. Fortunately, I found it in my bag. It was under my umbrella!'),
    ('T', 'Ha ha! Were you late for work?'),
    ('L', 'Yes, I was. I decided to wait for the next bus. Eventually, it came after twenty minutes.'),
    ('T', 'What time did you arrive?'),
    ('L', 'In the end, I arrived at ten. My manager wasn’t happy!'),
    ('T', 'What a morning!'),
]
DLG_NAMES = {'L': 'Linh', 'T': 'Tom'}
DLG_Q = [
    ('Why did Linh miss the bus?', ['It started to rain and she was late.', 'She got up at ten.'], 'It started to rain and she was late.'),
    ('Where was her phone?', ['in her bag', 'at home'], 'in her bag'),
]
CARD = [('Missed', 'the bus', ['bus', 'thebus']), ('Phone was', 'in her bag', ['inherbag', 'bag', 'inthebag', 'underherumbrella']),
        ('Waited', '20 minutes', ['20', '20minutes', 'twentyminutes', 'twenty']), ('Arrived at', '10 o\'clock', ['10', 'ten', '10oclock', 'tenoclock', '1000'])]

# ---------------------------------------------------------------- practice: question maker (answer -> question)
QMAKER = [
    ('I went to Da Lat.', ['where did you go'], 'Where…?'),
    ('I went with my sister.', ['who did you go with'], 'Who…?'),
    ('Yes, I missed the bus.', ['did you miss the bus'], 'Did…?'),
    ('It was very cold.', ['how was the weather', 'what was the weather like'], 'How / What … like?'),
    ('Yes, we were very tired.', ['were you tired', 'were you very tired'], 'Were…?'),
    ('We arrived at ten.', ['what time did you arrive', 'when did you arrive'], 'What time…?'),
    ('I found it in my bag.', ['where did you find it'], 'Where…?'),
    ('We decided to wait.', ['what did you decide to do', 'what did you do'], 'What…?'),
]

# ---------------------------------------------------------------- speaking: story dice
DICE_PLACE = ['at the airport', 'on the bus', 'at the supermarket', 'at a weekend event', 'in a restaurant', 'at the train station']
DICE_PROBLEM = ['I missed the bus', 'I lost my phone', 'it started to rain', 'I got on the wrong train', 'I forgot my wallet', 'my bag was very heavy']
DICE_LUCK = ['a kind person helped me', 'I found it in my bag', 'the next bus came quickly', 'my friend called me', 'I met an old friend', 'the shop was still open']

# ---------------------------------------------------------------- real-life task: three follow-up questions
FOLLOW_STARTERS = ['Where did you…?', 'Who did you… with?', 'What did you…?', 'Did you…?', 'Was it…?', 'Were you…?', 'What happened next?', 'How did you feel?']

# ---------------------------------------------------------------- game: story jigsaw
JIGSAW = [
    ('🚌 The bus story', ['At first, everything was fine.', 'While I was waiting at the bus stop, it started to rain.', 'Suddenly, I realised I was at the wrong bus stop!',
                         'Fortunately, a kind woman helped me.', 'Eventually, the right bus arrived.', 'In the end, I got to work on time.']),
    ('✈️ The airport story', ['At first, the trip was great.', 'While I was travelling home, I slept on the plane.', 'Suddenly, I realised my phone was not in my pocket.',
                             'Fortunately, the staff found it under my seat.', 'Eventually, they brought it to the help desk.', 'In the end, I got my phone back.']),
    ('🛒 The shopping story', ['At first, I was happy with my shopping.', 'While I was walking home, my bag broke.', 'Suddenly, all the apples were on the road!',
                              'Fortunately, two students helped me.', 'Eventually, we found every apple.', 'In the end, I bought a new bag.']),
]

# ---------------------------------------------------------------- main structures (step-by-step slides)
STRUCTS = [
    dict(name="You'll never guess what happened.", q="You'll never guess what happened ___.", vi_q='Bạn sẽ không đoán được chuyện gì đã xảy ra ___ đâu.',
         a='What happened?', vi_a='Chuyện gì đã xảy ra vậy?',
         model='Hi! How was your day?',
         answers=[("You'll never guess what happened this morning!", 'Bạn không đoán được sáng nay có chuyện gì đâu!'),
                  ("You'll never guess what happened at the airport.", 'Bạn không đoán được chuyện gì xảy ra ở sân bay đâu.'),
                  ("You'll never guess what happened on the bus!", 'Bạn không đoán được chuyện gì xảy ra trên xe buýt đâu!')],
         tr=[('Bạn sẽ không đoán được chuyện gì đã xảy ra hôm qua đâu!', "You'll never guess what happened yesterday!"),
             ('Chuyện gì đã xảy ra vậy?', 'What happened?'),
             ('Bạn đã ở đâu?', 'Where were you?')]),
    dict(name='While I was…, …', q='While I was ___, ___.', vi_q='Trong khi tôi đang ___, thì ___.',
         a='Oh no! What did you do?', vi_a='Ôi không! Bạn đã làm gì?',
         model='What happened?',
         answers=[('While I was waiting for the bus, it started to rain.', 'Trong khi tôi đang chờ xe buýt, trời bắt đầu mưa.'),
                  ('While I was travelling in Hue, I lost my phone.', 'Trong khi tôi đang du lịch ở Huế, tôi làm mất điện thoại.'),
                  ('While I was walking home, I met an old friend.', 'Trong khi tôi đang đi bộ về nhà, tôi gặp một người bạn cũ.')],
         tr=[('Trong khi tôi đang chờ, tôi đột nhiên nhận ra lỗi sai.', 'While I was waiting, I suddenly realised the mistake.'),
             ('Trong khi chúng tôi đang đi du lịch, trời bắt đầu mưa.', 'While we were travelling, it started to rain.'),
             ('Trong khi tôi đang ăn trưa, điện thoại reo.', 'While I was having lunch, my phone rang.')]),
    dict(name='What happened next?', q='What happened next?', vi_q='Chuyện gì xảy ra tiếp theo?',
         a='Suddenly / Fortunately, ___.', vi_a='Đột nhiên / May mắn thay, ___.',
         model='I missed the bus.',
         answers=[('Suddenly, I realised I didn’t have my phone.', 'Đột nhiên, tôi nhận ra tôi không có điện thoại.'),
                  ('Fortunately, I found it in my bag.', 'May mắn thay, tôi tìm thấy nó trong túi.'),
                  ('I decided to wait for the next bus.', 'Tôi quyết định chờ chuyến xe buýt tiếp theo.')],
         tr=[('Chuyện gì xảy ra tiếp theo?', 'What happened next?'),
             ('Bạn có lỡ chuyến xe buýt không?', 'Did you miss the bus?'),
             ('May mắn thay, tôi tìm thấy ví của mình.', 'Fortunately, I found my wallet.')]),
    dict(name='In the end, …', q='In the end, ___.', vi_q='Cuối cùng, ___.',
         a='What a day!', vi_a='Thật là một ngày dài!',
         model='So, did you get to work?',
         answers=[('In the end, I arrived at work at ten.', 'Cuối cùng, tôi đến chỗ làm lúc 10 giờ.'),
                  ('In the end, everything was fine.', 'Cuối cùng, mọi thứ đều ổn.'),
                  ('Eventually, the bus arrived, and in the end I was only five minutes late.', 'Cuối cùng xe buýt cũng đến, và rốt cuộc tôi chỉ trễ năm phút.')],
         tr=[('Cuối cùng, chúng tôi về nhà lúc nửa đêm.', 'In the end, we returned home at midnight.'),
             ('Cuối cùng chuyến tàu cũng đến.', 'Eventually, the train arrived.'),
             ('Bạn có mệt không?', 'Were you tired?')]),
]
