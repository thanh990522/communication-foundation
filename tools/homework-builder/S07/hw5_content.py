"""S07 · Eating Out: From Menu to Bill — 5-part homework content (only S07 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Eating Out: From Menu to Bill'

VOCAB = [
    mcq('“món khai vị” in English is…', ['starter', 'main course', 'side dish'], 'starter'),
    gap("For my main ____, I'll have the grilled chicken.", 'course'),
    mcq('Would you like a ____ dish? — Chips, please.', ['side', 'main', 'service'], 'side'),
    gap('Can you ____ a dish? — Try the fish and chips!', 'recommend'),
    mcq("I have a food ____. I can't eat nuts.", ['allergy', 'bill', 'charge'], 'allergy'),
    gap('Excuse me. Could we have the ____, please?', 'bill'),
    mcq('There is a ten per cent service ____.', ['charge', 'bill', 'split'], 'charge'),
    gap("The total is £40. Could we ____ the bill? That's £20 each.", 'split'),
]

READING = {
    'title': 'A review: The Blue Fish',
    'passage': """The Blue Fish is a small restaurant near the river. When you arrive, the waiter gives you the menu and a glass of water.

To start with, I recommend the tomato soup. It is hot, fresh and only £4. For the main course, you can choose fish, chicken or a vegetable dish. The fish and chips is the most popular dish, and the portion is very large! Every main course comes with a side dish: chips, rice or a green salad.

The waiters are friendly. If you have a food allergy, tell them. They can make most dishes without nuts, cheese or onions. However, the chocolate cake contains nuts.

When you ask for the bill, check it carefully, because there is a ten per cent service charge. With friends, you can split the bill easily. A meal for two usually costs about £40.""",
    'items': [
        mcq('Where is The Blue Fish?', ['near the river', 'in the city centre', 'near the station'], 'near the river'),
        mcq('What does the writer recommend as a starter?', ['the tomato soup', 'the chocolate cake', 'the green salad'], 'the tomato soup'),
        mcq('Every main course comes with a side dish.', TF, 'True'),
        mcq('What is the most popular dish?', ['the fish and chips', 'the tomato soup', 'the chicken'], 'the fish and chips'),
        mcq('The chocolate cake is OK for people with a nut allergy.', TF, 'False'),
        gap('The service charge is ____ per cent.', 'ten', '10'),
        mcq('A meal for two usually costs about…', ['£40', '£4', '£10'], '£40'),
    ],
}

W, Cu = RYAN, LIBBY
LISTEN = [{
    'title': 'Ordering at a café', 'label': 'Waiter & customer', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (W, 'Waiter', 'Hi, are you ready to order?'),
        (Cu, 'Customer', 'Yes, I think so. What do you recommend?'),
        (W, 'Waiter', 'The beef burger is very popular. It comes with a side dish of chips or salad.'),
        (Cu, 'Customer', "Hmm, I'm vegetarian. Is there a vegetarian main course?"),
        (W, 'Waiter', 'Yes, the vegetable curry. However, it contains nuts.'),
        (Cu, 'Customer', 'Oh no, I have a food allergy. Could I have it without nuts?'),
        (W, 'Waiter', 'Sure, no problem.'),
        (Cu, 'Customer', "Great. I'll have the vegetable curry, then, with rice. And to start with, a green salad, please."),
        (W, 'Waiter', 'Anything to drink?'),
        (Cu, 'Customer', 'An orange juice, please.'),
        (Cu, 'Customer', 'Excuse me, could I have the bill, please?'),
        (W, 'Waiter', "Of course. That's twenty-one pounds, with the service charge."),
        (Cu, 'Customer', 'Here you are. Thank you!'),
    ],
    'items': [
        mcq('What does the waiter recommend?', ['the beef burger', 'the vegetable curry', 'the green salad'], 'the beef burger'),
        mcq('The burger comes with…', ['chips or salad', 'rice', 'soup'], 'chips or salad'),
        mcq('The customer eats meat.', TF, 'False'),
        mcq('Why does she ask for no nuts?', ['She has a food allergy.', "She doesn't like them.", "They're expensive."], 'She has a food allergy.'),
        gap('Her main course: the vegetable ____', 'curry'),
        mcq('Her starter:', ['a green salad', 'tomato soup', 'garlic bread'], 'a green salad'),
        mcq('Her drink:', ['an orange juice', 'a coffee', 'water'], 'an orange juice'),
        gap('The bill is ____ pounds.', 'twenty-one', '21', 'twentyone'),
    ],
}]

SHADOW = {
    'title': 'Order a meal in a restaurant',
    'voice': SONIA,
    'sentences': [
        'Good evening. Could we see the menu, please?',
        'What do you recommend?',
        "To start with, I'll have the tomato soup.",
        "For the main course, I'd like the grilled chicken with rice.",
        'I have a food allergy. Could I have it without nuts?',
        'Could we have the bill, please? Could we split it?',
    ],
}

TRANS = [
    ('Bạn gợi ý món chính nào?', ['What main course do you recommend?', 'Which main course do you recommend?'], 'What … do you recommend?'),
    ('Tôi sẽ gọi cá và khoai tây chiên.', ["I'll have the fish and chips.", "I'll have fish and chips."], "I'll have …"),
    ('Tôi có thể dùng món burger mà không có phô mai không?', ['Could I have the burger without cheese?', 'Could I have the burger without cheese, please?'], 'Could I have it without …?'),
    ('Xin lỗi, chúng tôi có thể chia hóa đơn làm hai không?', ['Excuse me, could we split the bill in two?', 'Excuse me, could we split the bill?'], 'Could we split the bill?'),
    ('Trước tiên, tôi sẽ gọi bánh mì bơ tỏi.', ["To start with, I'll have the garlic bread.", "To start with, I'd like the garlic bread."], "To start with, I'll have …"),
]
