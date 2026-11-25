"""S11 · Past Questions & Storytelling — 5-part homework content (only S11 language + S10 past simple)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Past Questions & Storytelling'

VOCAB = [
    mcq('“lỡ chuyến xe buýt” — ____ the bus', ['miss', 'lose', 'decide'], 'miss'),
    gap("You'll never guess what ____ yesterday!", 'happened'),
    mcq('____, I realised my bag was on the bus.', ['Suddenly', 'Fortunately', 'In the end'], 'Suddenly'),
    gap('I lost my wallet, but ____ I found it in my jacket.', 'fortunately'),
    mcq('At the station, I realised the ____. It was the wrong train!', ['mistake', 'bus', 'event'], 'mistake'),
    gap('The bus was late, so we ____ to wait.', 'decided'),
    mcq('We waited for an hour. ____, the train arrived.', ['Eventually', 'Suddenly', 'At first'], 'Eventually'),
    gap('I lost my phone ____ travelling in Hue.', 'while'),
    mcq('____ you miss the bus?', ['Did', 'Were', 'Was'], 'Did'),
    mcq('____ you late for work?', ['Were', 'Did', 'Was'], 'Were'),
]

READING = {
    'title': 'The wrong train',
    'passage': """You'll never guess what happened to me last Saturday!

At first, everything was fine. I wanted to visit my aunt in Bien Hoa, so I went to the train station early. While I was waiting, I bought a coffee and read a book.

At nine o'clock, I got on the train. I was very happy because there were lots of free seats. Suddenly, I realised the mistake. The train was going to Nha Trang, not Bien Hoa!

Fortunately, a kind man helped me. He told me to get off at the next station and wait for the train back. I decided to wait. Eventually, the right train arrived after two hours.

In the end, I arrived at my aunt's house at two o'clock in the afternoon — five hours late! My aunt asked me, "Where were you? Did you get lost?" We laughed a lot. It was a long day, but it was a good story!""",
    'items': [
        mcq('Where did the writer want to go?', ['to Bien Hoa', 'to Nha Trang', 'to Da Lat'], 'to Bien Hoa'),
        mcq('What did the writer do while waiting?', ['bought a coffee and read a book', 'called her aunt', 'ate breakfast'], 'bought a coffee and read a book'),
        mcq('The train was full.', TF, 'False'),
        mcq('What was the mistake?', ['She got on the wrong train.', 'She missed the train.', 'She lost her ticket.'], 'She got on the wrong train.'),
        mcq('Who helped her?', ['a kind man', 'her aunt', 'a student'], 'a kind man'),
        gap('The right train arrived after ____ hours.', 'two', '2'),
        mcq('She arrived at her aunt\'s house on time.', TF, 'False'),
    ],
}

A, B_ = LIBBY, RYAN
LISTEN = [{
    'title': "Mai's weekend story", 'label': 'Two friends', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (A, 'Mai', "You'll never guess what happened on Sunday!"),
        (B_, 'Dan', 'What happened?'),
        (A, 'Mai', 'I went to the cinema with my sister. At first, everything was fine.'),
        (B_, 'Dan', 'Did you enjoy the film?'),
        (A, 'Mai', 'Yes, we did. But while we were walking home, it started to rain.'),
        (B_, 'Dan', 'Oh no! Were you wet?'),
        (A, 'Mai', 'Very! And suddenly I realised I didn\'t have my phone.'),
        (B_, 'Dan', 'What happened next? Did you go back to the cinema?'),
        (A, 'Mai', 'Yes, we did. Fortunately, a man at the cinema found it under my seat.'),
        (B_, 'Dan', 'That\'s lucky! What time did you get home?'),
        (A, 'Mai', 'Eventually, we got a taxi. In the end, we got home at eleven.'),
    ],
    'items': [
        mcq('Where did Mai go on Sunday?', ['to the cinema', 'to the beach', 'to a restaurant'], 'to the cinema'),
        gap('She went with her ____.', 'sister'),
        mcq('They enjoyed the film.', TF, 'True'),
        mcq('What happened while they were walking home?', ['It started to rain.', 'They missed the bus.', 'They met a friend.'], 'It started to rain.'),
        mcq('What did Mai realise?', ["She didn't have her phone.", "She didn't have her wallet.", 'The cinema was closed.'], "She didn't have her phone."),
        mcq('Where was the phone?', ['under her seat', 'in her bag', 'in the taxi'], 'under her seat'),
        mcq('How did they get home?', ['by taxi', 'by bus', 'on foot'], 'by taxi'),
        gap('They got home at ____.', 'eleven', '11'),
    ],
}]

SHADOW = {
    'title': 'Tell a short story',
    'voice': SONIA,
    'sentences': [
        "You'll never guess what happened yesterday!",
        'At first, everything was fine.',
        'While I was waiting for the bus, it started to rain.',
        "Suddenly, I realised I didn't have my phone.",
        'Fortunately, I found it in my bag.',
        'In the end, I arrived at work at ten.',
    ],
}

TRANS = [
    ('Bạn sẽ không đoán được chuyện gì đã xảy ra đâu!', ["You'll never guess what happened!", 'You will never guess what happened!'], "You'll never guess what happened."),
    ('Trong khi tôi đang chờ xe buýt, trời bắt đầu mưa.', ['While I was waiting for the bus, it started to rain.'], 'While I was …, …'),
    ('Chuyện gì xảy ra tiếp theo?', ['What happened next?'], 'What happened next?'),
    ('Bạn có lỡ chuyến xe buýt không?', ['Did you miss the bus?'], 'Did …?'),
    ('Cuối cùng, tôi đến chỗ làm lúc mười giờ.', ['In the end, I arrived at work at ten.', 'In the end, I got to work at ten.'], 'In the end, …'),
]
