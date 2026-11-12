"""S03 · Describing your neighbourhood — 5-part homework content (only S03 language)."""
import json, os
from hw5 import mcq, gap, TF, SONIA, ROOT

TITLE = 'Describing Your Neighbourhood'

VOCAB = [
    mcq('“rộng rãi” in English is…', ['spacious', 'crowded', 'peaceful'], 'spacious'),
    gap('The market is in a ____ area. There are always lots of people.', 'crowded'),
    gap('My apartment is centrally ____. It is in the city centre.', 'located'),
    mcq('I have a ____ neighbour. She always says hello.', ['friendly', 'spacious', 'nearby'], 'friendly'),
    mcq('There are lots of ____ facilities: a gym, a park and a café.', ['nearby', 'located', 'crowded'], 'nearby'),
    mcq('“yên bình” in English is…', ['peaceful', 'convenient', 'modern'], 'peaceful'),
    gap('The gym has modern ____.', 'facilities'),
    mcq('My home is in a ____ location. The bus stop is very near.', ['convenient', 'crowded', 'spacious'], 'convenient'),
]

READING = {
    'title': "Hoa's neighbourhood",
    'passage': """Hoa lives in a spacious apartment in a peaceful neighbourhood. Her apartment isn't centrally located, but it's in a convenient location. There is a bus stop near her building, and it takes her fifteen minutes to get to the city centre by bus.

There are lots of nearby facilities. There is a supermarket, a small café and a gym with modern facilities. There isn't a hospital near her home, but there is a big hospital in the city centre.

One thing Hoa likes is her neighbour, Mrs Lan. She is a very friendly neighbour, and she always says hello in the morning.

The only problem is the market. It's in a crowded area, and it is very crowded at weekends. Hoa usually goes to the park on Sundays because it's very peaceful.""",
    'items': [
        mcq("Hoa's apartment is small.", TF, 'False'),
        mcq("Hoa's apartment is centrally located.", TF, 'False'),
        gap('It takes her ____ minutes to get to the city centre by bus.', 'fifteen', '15'),
        mcq('Which place is NOT near her home?', ['a hospital', 'a gym', 'a supermarket'], 'a hospital'),
        mcq('Who is Mrs Lan?', ['her friendly neighbour', 'her teacher', 'her sister'], 'her friendly neighbour'),
        mcq('What is the only problem?', ['the crowded market', 'the bus stop', 'the gym'], 'the crowded market'),
        mcq('Why does Hoa go to the park on Sundays?', ["It's peaceful.", "It's crowded.", "It's centrally located."], "It's peaceful."),
    ],
}

# listening = Linh & Ben dialogue (audio already recorded for S03)
_d = json.load(open(os.path.join(ROOT, 'tools', 'homework-builder', 'S03', 'dialogue.json'), encoding='utf-8'))
LISTEN = [{
    'title': "Linh's neighbourhood", 'label': 'Linh & Ben · conversation', 'hint': 'Bài nghe dài ~2 phút. Nghe 2 lần rồi trả lời.',
    'audio': 'homework/audio/S03/S03_listen_neighbourhood.mp3', 'script': [[_d['speakers'][w], t] for w, t in _d['lines']],
    'items': [
        mcq('Where does Linh live?', ['in a spacious apartment', 'in a small house', 'in a small apartment'], 'in a spacious apartment'),
        mcq('Where is the big supermarket?', ['near the bus stop', 'near the park', 'near the school'], 'near the bus stop'),
        gap('There are ____ cafés.', 'two', '2'),
        mcq("Why is Linh's home convenient?", ['There are two bus stops near it.', 'There is a hospital near it.', "It's near the market."], 'There are two bus stops near it.'),
        mcq('Why is the park peaceful?', ['There are lots of trees.', "It's centrally located.", 'There is a gym.'], 'There are lots of trees.'),
        gap("Linh's friendly neighbour is called ____.", 'Mai'),
        mcq("Is there a hospital near Linh's home?", ['Yes', 'No'], 'No'),
        mcq("What does Ben like about his neighbourhood?", ['his apartment', 'the parks', 'the market'], 'his apartment'),
    ],
}]

SHADOW = {
    'title': 'Describe your neighbourhood',
    'voice': SONIA,
    'sentences': [
        'I live in a spacious apartment in a peaceful neighbourhood.',
        "It's centrally located, so it's very convenient.",
        'There is a big supermarket near my home, and there are two bus stops nearby.',
        'There are lots of nearby facilities, like a gym and a café.',
        'One thing I like is my friendly neighbour.',
        "The only problem is the market. It's a crowded area at weekends.",
    ],
}

TRANS = [
    ('Có một quán cà phê gần văn phòng của tôi.', ['There is a café near my office.', "There's a cafe near my office."], 'There is a … near …'),
    ('Có ba công viên trong khu phố của tôi.', ['There are three parks in my neighbourhood.'], 'There are … in …'),
    ('Khu phố của bạn tôi yên bình và thuận tiện.', ["My friend's neighbourhood is peaceful and convenient."], '… is … and …'),
    ('Một điều tôi thích là phòng gym hiện đại gần nhà tôi.', ['One thing I like is the modern gym near my home.', 'One thing I like is the modern gym near my house.'], 'One thing I like is …'),
    ('Vấn đề duy nhất là trạm xe buýt. Nó rất đông đúc.', ["The only problem is the bus stop. It's very crowded."], "The only problem is … It's …"),
]
