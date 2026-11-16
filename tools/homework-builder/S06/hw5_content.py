"""S06 · Food, Shopping Lists & Quantities — 5-part homework content (only S06 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Food, Shopping Lists & Quantities'

VOCAB = [
    mcq('“nguyên liệu” in English is…', ['ingredient', 'portion', 'aisle'], 'ingredient'),
    gap('This café gives you a large ____ of rice.', 'portion'),
    mcq('Milk, cheese and butter are ____ products.', ['dairy', 'fresh', 'enough'], 'dairy'),
    gap('The market sells fresh ____ every morning: tomatoes, carrots, apples…', 'produce'),
    mcq('Which ____ is the rice in? — Aisle 3.', ['aisle', 'portion', 'packet'], 'aisle'),
    gap('Do we have ____ eggs for the cake? — Yes, we have six.', 'enough'),
    mcq('Sorry, the milk is out of ____ today.', ['stock', 'aisle', 'order'], 'stock'),
    mcq('Can you buy a ____ of rice, please?', ['packet', 'carton', 'loaf'], 'packet'),
    mcq('How ____ apples do we need?', ['many', 'much'], 'many'),
    mcq('We need a ____ butter.', ['little', 'few'], 'little'),
]

READING = {
    'title': "Mum's note",
    'passage': """Hi Tom,

I'm working late tonight, so can you go to the supermarket after school? We're having a party for Grandma on Saturday, and we need fresh ingredients.

We have enough rice, but we're running out of eggs, so please get six. We don't have any milk, so get two cartons. We also need a little butter and some cheese. They're in the dairy aisle, at the back of the supermarket. The fresh produce is at the front: please get a few tomatoes and a bag of apples.

Don't buy any cola, because Grandma doesn't like it. Get a bottle of orange juice instead. If the apples are out of stock, get some oranges.

The portions at Grandma's parties are always large, so please check: is there anything else we need?

Thanks!
Mum""",
    'items': [
        mcq('They need more rice.', TF, 'False'),
        mcq('How many cartons of milk should Tom get?', ['two', 'one', 'six'], 'two'),
        mcq('Where are the butter and cheese?', ['in the dairy aisle, at the back', 'at the front', 'next to the drinks'], 'in the dairy aisle, at the back'),
        gap('Tom should get a few ____.', 'tomatoes'),
        mcq("Why shouldn't Tom buy cola?", ["Grandma doesn't like it.", "It's out of stock.", 'They have enough cola.'], "Grandma doesn't like it."),
        mcq('If the apples are out of stock, Tom should get…', ['some oranges', 'a bag of tomatoes', 'some cheese'], 'some oranges'),
        mcq("The portions at Grandma's parties are small.", TF, 'False'),
    ],
}

C, A = LIBBY, RYAN
LISTEN = [{
    'title': 'At the supermarket', 'label': 'Customer & shop assistant', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (C, 'Customer', 'Excuse me. Which aisle is the rice in?'),
        (A, 'Assistant', "It's in aisle three, next to the bread."),
        (C, 'Customer', 'Thanks. And do you have any fresh tomatoes?'),
        (A, 'Assistant', "Yes, they're in aisle one with the fresh produce. But we're running out, so there are only a few."),
        (C, 'Customer', "That's fine. I need four. Is there any yoghurt?"),
        (A, 'Assistant', "Sorry, the yoghurt is out of stock today. How about some cheese instead? It's in the dairy aisle."),
        (C, 'Customer', 'OK, a little cheese, then. How much is a packet of rice?'),
        (A, 'Assistant', 'A small packet is two pounds, and a large packet is five pounds.'),
        (C, 'Customer', 'A large packet, please. We have a big family.'),
        (A, 'Assistant', 'Is there anything else?'),
        (C, 'Customer', 'Yes. Do you have any bottles of water?'),
        (A, 'Assistant', 'Yes, in aisle four. Three bottles are two pounds today.'),
        (C, 'Customer', "Great. I need six bottles, then. That's all, thanks!"),
    ],
    'items': [
        mcq('Where is the rice?', ['in aisle three', 'in aisle one', 'in aisle four'], 'in aisle three'),
        mcq('The rice is next to the ___.', ['bread', 'milk', 'water'], 'bread'),
        gap('The customer needs ____ tomatoes.', 'four', '4'),
        mcq('Why are there only a few tomatoes?', ['The shop is running out.', 'They are not fresh.', 'They are out of stock.'], 'The shop is running out.'),
        mcq('What is out of stock?', ['yoghurt', 'cheese', 'rice'], 'yoghurt'),
        gap('A large packet of rice is ____ pounds.', 'five', '5'),
        mcq('Three bottles of water are…', ['two pounds', 'three pounds', 'six pounds'], 'two pounds'),
        gap('The customer needs ____ bottles of water.', 'six', '6'),
    ],
}]

SHADOW = {
    'title': 'Call home from the supermarket',
    'voice': SONIA,
    'sentences': [
        "I'm at the supermarket now. Do we have any eggs at home?",
        'We need a few tomatoes and a little butter.',
        "We're running out of milk, so I'm getting two cartons.",
        'The apples are out of stock, but there are some fresh oranges.',
        'The rice is in the third aisle.',
        'Is there anything else?',
    ],
}

TRANS = [
    ('Chúng ta có táo nào không?', ['Do we have any apples?'], 'Do we have any …?'),
    ('Chúng ta cần vài củ cà rốt và một ít phô mai.', ['We need a few carrots and a little cheese.'], 'We need a few … and a little …'),
    ('Chúng ta sắp hết bơ rồi.', ["We're running out of butter."], 'We are running out of …'),
    ('Xin lỗi, nước cam đã hết hàng.', ['Sorry, the orange juice is out of stock.', 'Sorry, orange juice is out of stock.'], '… is out of stock'),
    ('Còn gì nữa không? — Có, một gói gạo.', ['Is there anything else? — Yes, a packet of rice.', 'Is there anything else? Yes, a packet of rice.'], 'Is there anything else?'),
]
