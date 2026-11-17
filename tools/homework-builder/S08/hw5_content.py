"""S08 · Shopping, Sizes, Returns & Refunds — 5-part homework content (only S08 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Shopping, Sizes, Returns & Refunds'

VOCAB = [
    mcq('“hoàn tiền” — get a ____', ['refund', 'receipt', 'discount'], 'refund'),
    gap('These jeans are size 32. I’m size 32. They ____ perfectly!', 'fit'),
    mcq('That red dress really ____ you. You look great!', ['suits', 'fits', 'exchanges'], 'suits'),
    gap('Keep the ____. You need it for a refund.', 'receipt'),
    mcq('Is this the correct ____? I’m a medium.', ['size', 'discount', 'refund'], 'size'),
    gap('Can I ____ this item for a bigger size?', 'exchange'),
    mcq('There’s a hole in it. It’s a ____ product.', ['damaged', 'correct', 'perfect'], 'damaged'),
    gap('Do you offer a ____ for students? — Yes, 10% off.', 'discount'),
    mcq('The shoes are size 38. I’m size 40. They are too ____.', ['small', 'big', 'cheap'], 'small'),
    mcq("The jacket is £30. I have £50. It's cheap ____.", ['enough', 'too', 'very'], 'enough'),
]

READING = {
    'title': 'Shop rules at Blue Star Clothes',
    'passage': """Welcome to Blue Star Clothes! Here are some rules for our customers.

Before you buy: you can try clothes on in our fitting rooms. If something is too small or too big, ask a shop assistant. We can check if we have it in the correct size or in a different colour.

Discounts: every Monday, we offer a discount of 20% for students. Please show your student card.

Returns: please keep the receipt. With the receipt, you can return an item within 30 days and get a refund. After 30 days, you can only exchange an item. Without the receipt, we cannot give you a refund, but you can exchange the item for a different size or colour.

Damaged products: if your item is damaged — for example, the zip is broken — bring it back with the receipt. You can get a full refund, or a new one instead.""",
    'items': [
        mcq('What can you do in the fitting rooms?', ['try clothes on', 'get a refund', 'pay'], 'try clothes on'),
        mcq('When is the student discount?', ['every Monday', 'every day', 'every weekend'], 'every Monday'),
        gap('The student discount is ____ per cent.', '20', 'twenty'),
        mcq('With the receipt, you can get a refund within 30 days.', TF, 'True'),
        mcq('After 30 days, you can…', ['only exchange an item', 'get a refund', 'get a discount'], 'only exchange an item'),
        mcq('Without the receipt, you can get a refund.', TF, 'False'),
        mcq('Your jacket is damaged and you have the receipt. You can get…', ['a full refund or a new one', 'only a discount', 'nothing'], 'a full refund or a new one'),
    ],
}

A, Cu = RYAN, LIBBY
LISTEN = [{
    'title': 'Returning a jacket', 'label': 'Shop assistant & customer', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (A, 'Assistant', 'Hello. Can I help you?'),
        (Cu, 'Customer', "Yes, please. I'd like to return this jacket."),
        (A, 'Assistant', "OK. What's the problem? Is it damaged?"),
        (Cu, 'Customer', "No, it isn't damaged. At first I liked it, but it's too big. It doesn't fit."),
        (A, 'Assistant', 'I see. Do you have the receipt?'),
        (Cu, 'Customer', "Yes, here's the receipt. I bought it last Saturday."),
        (A, 'Assistant', 'Thank you. Would you like a refund, or would you like to exchange it for a smaller size?'),
        (Cu, 'Customer', 'Do you have it in a small?'),
        (A, 'Assistant', "Let me check. Sorry, we only have it in large. But we have a small in black."),
        (Cu, 'Customer', "Hmm, black doesn't suit me. I'd like a refund instead, please."),
        (A, 'Assistant', 'No problem. That was forty-five pounds, with the discount. Here you are.'),
        (Cu, 'Customer', 'Thank you very much.'),
    ],
    'items': [
        mcq('What does the customer want to return?', ['a jacket', 'a dress', 'jeans'], 'a jacket'),
        mcq('The jacket is damaged.', TF, 'False'),
        mcq('What is the problem?', ["It's too big.", "It's too small.", "It's too expensive."], "It's too big."),
        mcq('Does she have the receipt?', ['Yes', 'No'], 'Yes'),
        gap('She bought it last ____.', 'Saturday'),
        mcq('The shop has a small jacket in…', ['black', 'blue', 'red'], 'black'),
        mcq('What does she get in the end?', ['a refund', 'a smaller size', 'a black jacket'], 'a refund'),
        gap('The refund is ____ pounds.', 'forty-five', '45', 'fortyfive'),
    ],
}]

SHADOW = {
    'title': 'Buy it, then return it',
    'voice': SONIA,
    'sentences': [
        'Excuse me. Do you have this jacket in a medium?',
        'Can I try it on?',
        "It's too small. It isn't big enough.",
        'This size fits perfectly, and the colour really suits me.',
        "I'd like to return this jacket. The zip is broken.",
        "Here's the receipt. Can I get a refund, please?",
    ],
}

TRANS = [
    ('Bạn có chiếc áo sơ mi này cỡ nhỏ không?', ['Do you have this shirt in a small?', 'Do you have this shirt in small?', 'Do you have this shirt in a small size?'], 'Do you have this in …?'),
    ('Tôi thử đôi giày này được không?', ['Can I try these shoes on?', 'Can I try on these shoes?'], 'Can I try … on?'),
    ('Chiếc quần jean này quá dài.', ['These jeans are too long.', 'The jeans are too long.'], 'too + adjective'),
    ('Chiếc váy này không đủ dài.', ["This dress isn't long enough.", 'This dress is not long enough.'], 'not + adjective + enough'),
    ('Tôi muốn trả lại chiếc áo khoác này. Đây là biên lai.', ["I'd like to return this jacket. Here's the receipt.", "I would like to return this jacket. Here is the receipt.", "I'd like to return this jacket. Here is the receipt."], "I'd like to return …"),
]
