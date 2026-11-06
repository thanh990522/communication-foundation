"""Lesson S02 — Routines, Habits & Real Schedules.
Language is limited to the syllabus items for S02 (plus A1 routine verbs and clock times):
  collocations : have a productive morning · make a daily commute · work the evening shift ·
                 take a short break · usually start work · hardly ever miss breakfast ·
                 on weekdays · at weekends
  frames       : My day usually starts with ___. · It takes me ___ minutes to ___. ·
                 I usually ___, but I hardly ever ___. · On weekdays ___, whereas at weekends ___.
  grammar      : present simple questions + adverbs of frequency
  linkers      : first · then · after that · but · whereas · because
  pronunciation: third-person -s endings · stress on frequency adverbs
"""

# ---------------------------------------------------------------- warm-up: spell today's words
WARM = ['SHIFT', 'BREAK', 'COMMUTE', 'WEEKDAYS', 'WEEKENDS', 'USUALLY', 'PRODUCTIVE', 'HARDLY']

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [  # key (illustration), word, part of speech, IPA, meaning; collocation, keyword, collocation meaning, example
    dict(k='productive', w='productive', pos='adjective', ipa='/prəˈdʌktɪv/', vi='hiệu quả, năng suất',
         col='have a productive morning', kw='productive', col_vi='có một buổi sáng làm việc hiệu quả', ex='I always have a productive morning.'),
    dict(k='commute', w='commute', pos='noun', ipa='/kəˈmjuːt/', vi='quãng đường đi làm hằng ngày',
         col='make a daily commute', kw='commute', col_vi='đi làm (di chuyển) hằng ngày', ex='I make a daily commute to the city.'),
    dict(k='shift', w='shift', pos='noun', ipa='/ʃɪft/', vi='ca làm việc',
         col='work the evening shift', kw='shift', col_vi='làm ca tối', ex='Minh works the evening shift.'),
    dict(k='break', w='break', pos='noun', ipa='/breɪk/', vi='giờ nghỉ, giải lao',
         col='take a short break', kw='break', col_vi='nghỉ giải lao một chút', ex='I take a short break at eleven.'),
    dict(k='usually', w='usually', pos='adverb', ipa='/ˈjuːʒuəli/', vi='thường thường',
         col='usually start work', kw='usually', col_vi='thường bắt đầu làm việc', ex='I usually start work at nine.'),
    dict(k='hardly ever', w='hardly ever', pos='adverb', ipa='/ˌhɑːdli ˈevə/', vi='hầu như không bao giờ',
         col='hardly ever miss breakfast', kw='hardly ever', col_vi='hầu như không bao giờ bỏ bữa sáng', ex='I hardly ever miss breakfast.'),
    dict(k='weekday', w='weekday', pos='noun', ipa='/ˈwiːkdeɪ/', vi='ngày trong tuần (thứ Hai – thứ Sáu)',
         col='on weekdays', kw='weekdays', col_vi='vào các ngày trong tuần', ex='On weekdays, I get up at six.'),
    dict(k='weekend', w='weekend', pos='noun', ipa='/ˌwiːkˈend/', vi='cuối tuần (thứ Bảy – Chủ nhật)',
         col='at weekends', kw='weekends', col_vi='vào cuối tuần', ex='At weekends, I get up late.'),
]

# ---------------------------------------------------------------- adverbs of frequency
FREQ = [  # adverb, percent, example, Vietnamese, days out of 7
    ('always', 100, 'I always take a short break at eleven.', 'luôn luôn', 7),
    ('usually', 80, 'I usually start work at nine.', 'thường thường', 6),
    ('often', 60, 'Lucy often has a productive morning.', 'thường, hay', 4),
    ('sometimes', 40, 'Minh sometimes works at weekends.', 'thỉnh thoảng', 3),
    ('hardly ever', 10, 'I hardly ever miss breakfast.', 'hầu như không bao giờ', 1),
    ('never', 0, 'Minh never works at weekends.', 'không bao giờ', 0),
]

# ---------------------------------------------------------------- collocation check (choose the word)
COLL = [  # sentence with ___, options, answer, illustration key
    ('I have a ___ morning.', ['productive', 'short', 'daily'], 'productive', 'productive'),
    ('I make a ___ commute.', ['daily', 'evening', 'short'], 'daily', 'commute'),
    ('She works the evening ___.', ['shift', 'break', 'commute'], 'shift', 'shift'),
    ('We take a short ___ at eleven.', ['break', 'shift', 'morning'], 'break', 'break'),
    ('I hardly ever ___ breakfast.', ['miss', 'take', 'make'], 'miss', 'hardly ever'),
    ('I usually ___ work at nine.', ['start', 'make', 'take'], 'start', 'usually'),
    ('___ weekdays, I get up at six.', ['On', 'At', 'In'], 'On', 'weekday'),
    ('___ weekends, I get up late.', ['At', 'On', 'In'], 'At', 'weekend'),
]

# ---------------------------------------------------------------- pronunciation
S_GROUPS = [  # sound, rule, tag, -s forms, base forms
    ('/s/', 'after /p/ /t/ /k/ /f/', 'voiceless · 1 syllable',
     ['starts', 'takes', 'works', 'makes', 'commutes', 'gets up'], ['start', 'take', 'work', 'make', 'commute', 'get up']),
    ('/z/', 'after vowels and /n/ /d/ /v/ …', 'voiced · 1 syllable',
     ['has', 'goes', 'does', 'mornings', 'weekdays', 'weekends'], ['have', 'go', 'do', 'morning', 'weekday', 'weekend']),
    ('/ɪz/', 'after /s/ /z/ /ʃ/ /tʃ/', '+1 syllable',
     ['misses', 'finishes'], ['miss', 'finish']),
]
SORT = [  # word, sound index 0=/s/ 1=/z/ 2=/ɪz/   (all from today's lesson)
    ('starts', 0), ('takes', 0), ('works', 0), ('makes', 0), ('commutes', 0), ('gets up', 0), ('wakes up', 0),
    ('minutes', 0), ('breaks', 0), ('shifts', 0),
    ('has', 1), ('goes', 1), ('does', 1), ('mornings', 1), ('weekdays', 1), ('weekends', 1),
    ('misses', 2), ('finishes', 2),
]
# reading ladder: *word* marks the -s ending to practise
LADDER = [
    {'snd': '/s/',
     'phrases': ['*starts* work', '*takes* a short break', '*makes* a daily commute', '*works* the evening shift'],
     'sents': ['She usually *starts* work at nine.', 'It *takes* me twenty *minutes* to get to work.', 'Minh *works* the evening shift.']},
    {'snd': '/z/',
     'phrases': ['*has* breakfast', '*has* a productive morning', '*goes* to work', 'on *weekdays* · at *weekends*'],
     'sents': ['Lucy *has* a productive morning.', 'He *goes* to work at four.', 'On *weekdays* I get up at six.']},
    {'snd': '/ɪz/',
     'phrases': ['*misses* breakfast', '*finishes* work', 'hardly ever *misses* breakfast', '*finishes* the evening shift'],
     'sents': ['She hardly ever *misses* breakfast.', 'He usually *finishes* work at five.', 'Minh *finishes* the evening shift at twelve.']},
]
CHALLENGE = [
    'She *gets* up at six, *has* breakfast and *starts* work at eight.',
    'He always *takes* a short break at eleven and *finishes* work at five.',
    'Minh hardly ever *misses* breakfast, and he never *works* at *weekends*.',
]
STRESS = [
    'I USUALLY start work at nine, but I HARDLY EVER finish at five.',
    'She ALWAYS takes a short break, but she NEVER misses breakfast.',
]

# ---------------------------------------------------------------- sentence frames
FRAMES = [  # frame, examples
    ('My day usually starts with ___.', ['My day usually starts with a cup of coffee.', 'My day usually starts with breakfast.']),
    ('It takes me ___ minutes to ___.', ['It takes me twenty minutes to get to work.', 'It takes me ten minutes to have breakfast.']),
    ('I usually ___, but I hardly ever ___.', ['I usually start work at nine, but I hardly ever finish at five.', 'I usually get up early, but I hardly ever miss breakfast.']),
    ('On weekdays ___, whereas at weekends ___.', ['On weekdays I get up at six, whereas at weekends I get up late.', 'On weekdays I work, whereas at weekends I never work.']),
]
LINKERS = ['first', 'then', 'after that', 'but', 'whereas', 'because']

# ---------------------------------------------------------------- questions & answers
QA = [
    ('What time do you usually start work?', ['I usually start work at nine.', 'At about eight.', 'I work the evening shift, so I start at four.']),
    ('How long does it take you to get to work?', ['It takes me twenty minutes to get to work.', 'About forty-five minutes. I make a daily commute to the city.']),
    ('How often do you take a break?', ['I always take a short break at eleven.', 'Sometimes.', 'I hardly ever take a break.']),
    ('Do you ever miss breakfast?', ['No, I never miss breakfast.', 'Yes, sometimes.', 'I hardly ever miss breakfast.']),
    ('What does your day usually start with?', ['My day usually starts with a cup of coffee.', 'It usually starts with breakfast.']),
    ('Do you work at weekends?', ['No, I never work at weekends.', 'Yes, I sometimes work the evening shift at weekends.']),
    ('Does she usually start work early?', ['Yes, she usually starts work at seven.', 'No, she works the evening shift.']),
    ('What do you do at weekends?', ['At weekends I usually get up late.', 'On weekdays I work, whereas at weekends I never work.']),
]

# ---------------------------------------------------------------- model dialogue (Lucy & Minh)
DIALOGUE = [
    ('L', "Hi Minh. Do you usually start work at nine?"),
    ('M', "No, I don't. I work the evening shift on weekdays. I usually start work at four."),
    ('L', "Really? What time do you get up?"),
    ('M', "At about nine. My day usually starts with a cup of coffee."),
    ('L', "How long does it take you to get to work?"),
    ('M', "It takes me twenty minutes. What about you, Lucy?"),
    ('L', "I make a daily commute to the city. It takes me forty-five minutes."),
    ('M', "Do you have a productive morning?"),
    ('L', "Yes, usually. I get up at six, and I hardly ever miss breakfast."),
    ('M', "How often do you take a break?"),
    ('L', "I always take a short break at eleven."),
    ('M', "And what about weekends?"),
    ('L', "On weekdays I get up at six, whereas at weekends I usually get up late."),
    ('M', "I never work at weekends, because I work every evening on weekdays."),
]
DLG_Q = [  # question, options, answer
    ('What time does Minh usually start work?', ['at nine', 'at four', 'at six'], 'at four'),
    ('How long does it take Lucy to get to work?', ['20 minutes', '45 minutes', '11 minutes'], '45 minutes'),
    ('When does Lucy take a short break?', ['at eleven', 'at six', 'at nine'], 'at eleven'),
    ('Does Minh work at weekends?', ['Yes, always', 'Yes, sometimes', 'No, never'], 'No, never'),
]

# ---------------------------------------------------------------- listening (real recording)
LISTEN = {
    'title': 'Morning Routine — John & Sarah',
    'source': 'elllo.org · A1 Lesson 20 · Adverbs of Frequency (Todd Beuckens)',
    'page': 'https://elllo.org/english/grammar/A1-20-Adverbs-of-Frequency-Routines.htm',
    'file': 'Listening/S02_listening_John_Sarah_morning_routine.mp3',
    'script': [
        ('S', "John, tell me about your day. What time do you wake up?"),
        ('J', "Well, let's see. Some days I wake up early, maybe about six o'clock. Yeah, sometimes I wake up at six o'clock. When I get up early, I like to get ready for the day, take a shower, and have breakfast. But other days, I don't like getting up early. Maybe I'll sleep in until ten or eleven."),
        ('S', "Wow."),
        ('J', "Yeah, I like sleeping in late, so sometimes I wake up at eleven. On those days, if I know I won't wake up until eleven, I'll take a shower the night before, before I go to bed. How about you, Sarah? When do you usually wake up?"),
        ('S', "Well, I like every day to be the same. So I wake up every day at eight o'clock."),
        ('J', "Eight?"),
        ('S', "Eight. And I always do the same thing. First, I make coffee right away. Then I wake up my kids, and we have breakfast together at about 8:30."),
        ('J', "Really?"),
        ('S', "Yes. We usually have something easy, like bread and yogurt and fruit."),
        ('J', "I like to have coffee every morning. Whether I wake up at six or at ten, I'm still going to have coffee. But I often skip breakfast. Do you always eat breakfast every day?"),
        ('S', "Yes. If I don't eat breakfast, I'm so hungry. What about lunch? What time do you have lunch?"),
        ('J', "Lunch is the same every day for me. I always eat lunch at 12:30 p.m. So whenever I wake up, I do some things, and then I always have lunch at 12:30 p.m. Just half past noon. And I always have a simple lunch. Maybe some soup or spaghetti or a sandwich. Something light. And it's always at half past noon. What time do you eat lunch?"),
        ('S', "That's interesting. I have breakfast at the same time every day, but lunch is always at a different time."),
        ('J', "Really?"),
        ('S', "Because I'm busy in the morning. I go out. Maybe I go shopping. Sometimes I clean the house. So I might have lunch at eleven o'clock or twelve o'clock. Sometimes as late as 2:30."),
        ('J', "Oh, that's getting late."),
        ('S', "Yes, but it's always an easy lunch, like you. Maybe crackers and cheese or a sandwich or a baked potato."),
        ('J', "I see."),
    ],
    'gist': ('Who gets up at the same time every day?', ['John', 'Sarah'], 'Sarah'),
    'detail': [  # statement with ___, options, answer
        ('John ___ wakes up at six.', ['always', 'sometimes', 'never'], 'sometimes'),
        ('Sarah ___ gets up at eight.', ['always', 'hardly ever', 'sometimes'], 'always'),
        ('Sarah ___ has breakfast.', ['never', 'always', 'hardly ever'], 'always'),
        ('John ___ misses breakfast.', ['often', 'never', 'always'], 'often'),
        ('John ___ has lunch at 12:30.', ['sometimes', 'always', 'hardly ever'], 'always'),
    ],
    'times': [  # question, answer
        ('Sarah wakes up at ___ every day.', ['8', 'eight', "8 o'clock", "eight o'clock", '8:00']),
        ('Sarah and her kids have breakfast at about ___.', ['8:30', '8.30', 'eight thirty', 'half past eight']),
        ('John has lunch at ___.', ['12:30', '12.30', 'twelve thirty', 'half past twelve']),
    ],
}

# ---------------------------------------------------------------- pair practice: interview & report
INTERVIEW = [  # question, report frame
    ('What time do you usually start work?', '___ usually starts work at ___.'),
    ('How long does it take you to get to work?', 'It takes ___ ___ minutes to get to work.'),
    ('How often do you take a break?', '___ ___ takes a short break.'),
    ('Do you ever miss breakfast?', '___ ___ misses breakfast.'),
    ('What do you do at weekends?', 'On weekdays ___, whereas at weekends ___.'),
]

# ---------------------------------------------------------------- free practice (2 situations, frame = model dialogue)
SITUATIONS = [
    {'e': '☕', 't': 'A new colleague', 'a': 'You', 'b': 'New colleague',
     'goal': 'Ask about start time, commute, breaks and weekends.',
     'card': ['Starts work at 8:30', 'Commute: 30 minutes', 'Break: always at 10:30', 'Weekends: never works']},
    {'e': '🌙', 't': 'A friend on the evening shift', 'a': 'You', 'b': 'Friend',
     'goal': 'Ask about the evening shift, mornings and weekends.',
     'card': ['Works the evening shift', 'Starts work at 5:00', 'Gets up at 10:00', 'Weekends: sometimes works']},
]
FP_LINES = [
    ('A', 'Do you usually start work at {time}?'),
    ('B', '{Yes / No}. I usually start work at {time}.'),
    ('A', 'What time do you get up?'),
    ('B', 'At {time}. My day usually starts with {activity}.'),
    ('A', 'How long does it take you to get to work?'),
    ('B', 'It takes me {number} minutes to get to work.'),
    ('A', 'How often do you take a break?'),
    ('B', 'I {always / usually / sometimes} take a short break at {time}.'),
    ('A', 'And what about weekends?'),
    ('B', 'On weekdays I {…}, whereas at weekends I {…}.'),
]

# ---------------------------------------------------------------- fluency: 90-second routine talk
TALK = [
    ('My day', 'My day usually starts with ___.'),
    ('First', 'First, I ___ at ___.'),
    ('Then', 'Then I ___. It takes me ___ minutes to ___.'),
    ('After that', 'After that, I usually ___, but I hardly ever ___.'),
    ('Weekends', 'On weekdays ___, whereas at weekends ___ because ___.'),
]
TALK_MODEL = ("My day usually starts with a cup of coffee. First, I get up at six. "
              "Then I make a daily commute to the city. It takes me forty-five minutes to get to work. "
              "I usually start work at eight. After that, I always take a short break at eleven, "
              "but I hardly ever finish work at five. On weekdays I get up at six, "
              "whereas at weekends I usually get up late, because I never work at weekends.")

# ---------------------------------------------------------------- game: sentence scramble
SCRAMBLE = [
    'I usually start work at nine.',
    'She hardly ever misses breakfast.',
    'It takes me twenty minutes to get to work.',
    'My day usually starts with a cup of coffee.',
    'Minh works the evening shift.',
    'We always take a short break at eleven.',
    'Do you ever miss breakfast?',
    'How often does he take a break?',
]
