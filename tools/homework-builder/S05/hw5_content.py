"""S05 · Directions & Getting Around Town — 5-part homework content (only S05 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Directions & Getting Around Town'

VOCAB = [
    mcq('“địa điểm mốc” in English is…', ['landmark', 'entrance', 'block'], 'landmark'),
    gap('Turn left at the busy ____. There are lots of cars.', 'intersection'),
    gap('Walk two ____ and turn right.', 'blocks'),
    mcq('Meet me at the main ____ of the station.', ['entrance', 'corner', 'block'], 'entrance'),
    mcq('The bank is ____ from the library.', ['across', 'next', 'between'], 'across'),
    mcq('The café is on the ____ of High Street and Park Road.', ['corner', 'entrance', 'block'], 'corner'),
    gap('It’s within walking ____. It takes five minutes.', 'distance'),
    mcq('How do I ____ to the museum?', ['get', 'take', 'walk'], 'get'),
]

READING = {
    'title': "Mai's directions",
    'passage': """Hi Lan,

Welcome to my neighbourhood! Here is the best way to get to my house from the bus stop. It's within walking distance. It takes about ten minutes.

The bus stop is across from the City Museum. It's a famous landmark, so you can't miss it. First, walk along Green Street for two blocks until you get to a busy intersection. There is a pharmacy on the corner.

After that, turn right and go past the library and a small café. Don't cross the road! Finally, my house is on your left, between the bookshop and the bank. It's the blue house. The main entrance is at the side of the house.

See you on Saturday!
Mai""",
    'items': [
        mcq("Mai's house is within walking distance of the bus stop.", TF, 'True'),
        mcq('How long does it take to walk to her house?', ['about ten minutes', 'about two minutes', 'about twenty minutes'], 'about ten minutes'),
        mcq('The bus stop is across from the ___.', ['City Museum', 'pharmacy', 'library'], 'City Museum'),
        gap('Walk ____ blocks until you get to a busy intersection.', 'two', '2'),
        mcq('What is on the corner of the intersection?', ['a pharmacy', 'a café', 'a bookshop'], 'a pharmacy'),
        mcq('Lan crosses the road after the café.', TF, 'False'),
        mcq("Mai's house is between…", ['the bookshop and the bank', 'the library and the café', 'the pharmacy and the bank'], 'the bookshop and the bank'),
    ],
}

A, Bn = LIBBY, RYAN
LISTEN = [{
    'title': "Anna's phone call", 'label': 'Anna & Ben · phone call', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (A, 'Anna', "Hi Ben, it's Anna. I'm at the train station. What's the best way to get to your apartment?"),
        (Bn, 'Ben', "Hi Anna! It's within walking distance. It takes about fifteen minutes."),
        (A, 'Anna', 'Great. How do I get there?'),
        (Bn, 'Ben', 'First, go out of the main entrance and turn left.'),
        (A, 'Anna', 'Turn left. OK.'),
        (Bn, 'Ben', "Then walk two blocks until you get to a busy intersection. There's a big bank on the corner."),
        (A, 'Anna', 'A bank on the corner. Got it.'),
        (Bn, 'Ben', 'After that, turn right and go past the supermarket and the park.'),
        (A, 'Anna', 'Go past the supermarket and the park.'),
        (Bn, 'Ben', "Finally, my building is on your left. It's across from the post office."),
        (A, 'Anna', 'Across from the post office. Is there a landmark near it?'),
        (Bn, 'Ben', "Yes. There's a famous old cinema next to my building. You can't miss it."),
        (A, 'Anna', 'Perfect. See you in fifteen minutes!'),
    ],
    'items': [
        gap('Anna is at the ____.', 'train station', 'station', 'the train station'),
        mcq('How long does it take to walk?', ['about fifteen minutes', 'about fifty minutes', 'about five minutes'], 'about fifteen minutes'),
        mcq('First, go out of the main entrance and turn ___.', ['left', 'right', 'straight on'], 'left'),
        gap('Walk two ____ until you get to a busy intersection.', 'blocks'),
        mcq('What is on the corner?', ['a big bank', 'a supermarket', 'a park'], 'a big bank'),
        mcq('After that, Anna goes past…', ['the supermarket and the park', 'the bank and the cinema', 'the post office'], 'the supermarket and the park'),
        mcq("Ben's building is across from the ___.", ['post office', 'bank', 'cinema'], 'post office'),
        mcq('What landmark is next to his building?', ['an old cinema', 'a museum', 'a hospital'], 'an old cinema'),
    ],
}]

SHADOW = {
    'title': 'Give directions from the hotel to the station',
    'voice': SONIA,
    'sentences': [
        'The station is within walking distance. It takes about ten minutes.',
        'First, go out of the hotel and turn left.',
        'Then walk two blocks until you get to a busy intersection.',
        'After that, go past the bank, then turn right.',
        'Finally, the station is on the corner, across from a famous landmark.',
        'The main entrance is on River Road.',
    ],
}

TRANS = [
    ('Cách tốt nhất để đến trường của bạn là gì?', ["What's the best way to get to your school?"], "What's the best way to get to …?"),
    ('Đi qua công viên, rồi rẽ phải ở giao lộ.',
     ['Go past the park, then turn right at the intersection.', 'Go past the park and then turn right at the intersection.'], 'Go past …, then …'),
    ('Hiệu thuốc ở đối diện siêu thị.', ['The pharmacy is across from the supermarket.'], '… is across from …'),
    ('Mất khoảng hai mươi phút đi bộ.', ['It takes about twenty minutes on foot.', 'It takes about twenty minutes to walk.'], 'It takes about … minutes.'),
    ('Trước tiên, rẽ trái. Sau đó đi bộ hai dãy phố cho đến khi bạn tới ngân hàng.',
     ['First, turn left. Then walk two blocks until you get to the bank.', 'First, turn left. After that, walk two blocks until you get to the bank.'], 'First … Then … until …'),
]
