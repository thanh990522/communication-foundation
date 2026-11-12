"""S02 · Routines, Habits & Real Schedules — 5-part homework content (only S02 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Routines, Habits & Real Schedules'

VOCAB = [
    mcq('“hiệu quả, năng suất” in English is…', ['productive', 'daily', 'short'], 'productive'),
    gap('I make a daily ____ to the city. It takes me forty minutes.', 'commute'),
    gap('Minh works the evening ____. He starts at four and finishes at midnight.', 'shift'),
    gap('I always ____ a short break at eleven.', 'take'),
    mcq('“hầu như không bao giờ” in English is…', ['hardly ever', 'usually', 'always'], 'hardly ever'),
    gap('I hardly ever ____ breakfast. I always have it at seven.', 'miss'),
    mcq('____ weekdays, I get up at six.', ['On', 'At', 'In'], 'On'),
    mcq('____ weekends, I usually get up late.', ['At', 'On', 'In'], 'At'),
]

READING = {
    'title': "Nam and Hoa's week",
    'passage': """Hi, I'm Nam. On weekdays, my day usually starts with a cup of tea at six o'clock. I hardly ever miss breakfast, and I always have a productive morning after a good breakfast.

I make a daily commute to the city by bus. It takes me forty minutes to get to work. I usually start work at eight, and I always take a short break at ten. I usually get home at six.

My sister Hoa works at a hospital. She works the evening shift, so she usually gets up late. It takes her only ten minutes to get to work. She hardly ever takes a break because the hospital is very busy.

On weekdays I get up early, whereas at weekends I usually get up at nine. I never work at weekends. Hoa sometimes works on Saturdays, but she never works on Sundays.""",
    'items': [
        mcq("Nam's day usually starts with breakfast.", TF, 'False'),
        mcq('How long does it take Nam to get to work?', ['forty minutes', 'ten minutes', 'fourteen minutes'], 'forty minutes'),
        mcq('When does Nam take a short break?', ['at ten', 'at eight', 'at six'], 'at ten'),
        mcq('Who works the evening shift?', ['Hoa', 'Nam', 'Nam and Hoa'], 'Hoa'),
        mcq('Hoa often takes a break at work.', TF, 'False'),
        gap('At weekends, Nam usually gets up at ____.', 'nine', '9', "nine o'clock", "9 o'clock", '9:00'),
        mcq('How often does Hoa work on Sundays?', ['never', 'sometimes', 'usually'], 'never'),
    ],
}

K, T = LIBBY, RYAN
LISTEN = [{
    'title': "Tom's evening shift", 'label': 'Kate & Tom · conversation', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (K, 'Kate', 'Hi Tom. You look tired!'),
        (T, 'Tom', 'Yes, I am. I work the evening shift this month.'),
        (K, 'Kate', 'Really? What time do you usually start work?'),
        (T, 'Tom', 'I usually start work at four in the afternoon, and I finish at midnight.'),
        (K, 'Kate', 'How do you get to work?'),
        (T, 'Tom', 'I make a daily commute by train. It takes me thirty minutes.'),
        (K, 'Kate', 'Do you ever take a break?'),
        (T, 'Tom', 'Yes. I always take a short break at eight.'),
        (K, 'Kate', 'And what about breakfast?'),
        (T, 'Tom', 'I hardly ever have breakfast before ten. My day usually starts with a cup of coffee.'),
        (K, 'Kate', 'What about weekends?'),
        (T, 'Tom', 'On weekdays I work, whereas at weekends I never work. I usually play football on Saturdays.'),
        (K, 'Kate', 'That sounds great!'),
    ],
    'items': [
        gap('Tom works the ____ shift.', 'evening'),
        gap('He usually starts work at ____ in the afternoon.', 'four', '4', "four o'clock", "4 o'clock", '4:00', '4pm', '4p.m.'),
        mcq('When does he finish work?', ['at midnight', 'at ten', 'at eight'], 'at midnight'),
        mcq('How does Tom get to work?', ['by train', 'by bus', 'He walks.'], 'by train'),
        gap('It takes him ____ minutes to get to work.', 'thirty', '30'),
        mcq('When does he take a short break?', ['at eight', 'at four', 'at ten'], 'at eight'),
        mcq("Tom's day usually starts with…", ['a cup of coffee', 'breakfast', 'a short break'], 'a cup of coffee'),
        mcq('What does Tom usually do on Saturdays?', ['He plays football.', 'He works.', 'He gets up early.'], 'He plays football.'),
    ],
}]

SHADOW = {
    'title': 'My weekday routine',
    'voice': SONIA,
    'sentences': [
        "My day usually starts with a cup of coffee at six o'clock.",
        'I hardly ever miss breakfast.',
        'I make a daily commute to the city, and it takes me forty minutes to get to work.',
        'I usually start work at eight, and I always take a short break at eleven.',
        'On weekdays I have a productive morning, whereas at weekends I usually get up late.',
    ],
}

TRANS = [
    ('Ngày của tôi thường bắt đầu với một ly nước.', ['My day usually starts with a glass of water.'], 'My day usually starts with …'),
    ('Mất khoảng hai mươi phút để tôi đến trường.',
     ['It takes me about twenty minutes to get to school.', 'It takes me twenty minutes to get to school.'], 'It takes me … minutes to …'),
    ('Chị tôi làm ca tối vào các ngày trong tuần.',
     ['My sister works the evening shift on weekdays.', 'On weekdays, my sister works the evening shift.'], 'work the evening shift · on weekdays'),
    ('Tôi thường bắt đầu làm việc lúc chín giờ, nhưng tôi hầu như không bao giờ nghỉ giải lao.',
     ['I usually start work at nine, but I hardly ever take a break.', 'I usually start work at nine, but I hardly ever take a short break.'], 'I usually …, but I hardly ever …'),
    ('Vào các ngày trong tuần tôi dậy lúc sáu giờ, trong khi cuối tuần tôi dậy lúc mười giờ.',
     ['On weekdays I get up at six, whereas at weekends I get up at ten.', 'On weekdays I get up at six, whereas on weekends I get up at ten.'], 'On weekdays …, whereas at weekends …'),
]
