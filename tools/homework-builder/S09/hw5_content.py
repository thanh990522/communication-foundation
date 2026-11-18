"""S09 · Everyday Services & Polite Requests — 5-part homework content (only S09 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Everyday Services & Polite Requests'

VOCAB = [
    mcq('“sản phẩm thay thế” — request a ____', ['replacement', 'repair', 'delivery'], 'replacement'),
    gap('Could you check the ____ status for me? My parcel is late.', 'delivery'),
    mcq('My fridge is broken. I want to book a ____ service.', ['repair', 'charge', 'delivery'], 'repair'),
    gap("I'm calling to report an ____ with my internet.", 'issue'),
    mcq('If there is a problem, please contact customer ____.', ['service', 'charge', 'issue'], 'service'),
    gap('Do I need to pay an extra ____ for a Saturday repair?', 'charge'),
    mcq('Are you ____ on Friday morning? — Yes, I am free.', ['available', 'damaged', 'extra'], 'available'),
    gap('Could you ____ the details, please? — Sure. Friday at nine.', 'confirm'),
    mcq('There ____ to be a problem with my order.', ['seems', 'seem', 'is seems'], 'seems'),
    mcq('Which is the most polite?', ['Could you check my bill for me, please?', 'Check my bill.', 'I want you to check my bill.'], 'Could you check my bill for me, please?'),
]

READING = {
    'title': 'Help page: FastHome Delivery',
    'passage': """Thank you for shopping with FastHome! Here is how to get help.

Late orders: first, check the delivery status on our website. You need your order number. If your order is more than three days late, please contact customer service.

Damaged products: if your product arrives damaged, take a photo and report the issue within seven days. You can request a replacement or a refund. There is no extra charge for a replacement.

Repairs: if your product stops working in the first year, we can book a repair service at your home. Repairs from Monday to Friday are free. For a repair on Saturday, you need to pay an extra charge of £20.

Before the driver or repair person comes, we will call you to confirm the details. Please tell us when you are available. If possible, give us two times.""",
    'items': [
        mcq('What do you need to check the delivery status?', ['your order number', 'a photo', 'your receipt'], 'your order number'),
        mcq('When should you contact customer service about a late order?', ['when it is more than three days late', 'on the first day', 'after one month'], 'when it is more than three days late'),
        gap('Report a damaged product within ____ days.', 'seven', '7'),
        mcq('You pay an extra charge for a replacement.', TF, 'False'),
        mcq('A repair on Wednesday is free.', TF, 'True'),
        gap('A Saturday repair costs an extra ____ pounds.', 'twenty', '20'),
        mcq('Why will FastHome call you before the visit?', ['to confirm the details', 'to give you a discount', 'to sell a new product'], 'to confirm the details'),
    ],
}

A, Cu = RYAN, LIBBY
LISTEN = [{
    'title': 'Booking a repair', 'label': 'Customer service & customer', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (A, 'Agent', 'Good afternoon, customer service. How can I help you?'),
        (Cu, 'Customer', "Hello. I'm calling about my washing machine. There seems to be a problem with it. It doesn't start."),
        (A, 'Agent', "I'm sorry to hear that. How old is it?"),
        (Cu, 'Customer', "It's ten months old."),
        (A, 'Agent', 'OK. Then the repair is free. We can send a repair person on Tuesday or on Saturday.'),
        (Cu, 'Customer', 'Is there an extra charge on Saturday?'),
        (A, 'Agent', "Yes, there's an extra charge of fifteen pounds on Saturday."),
        (Cu, 'Customer', "Then Tuesday, please. I'm available in the morning, if possible."),
        (A, 'Agent', 'No problem. Could I have your address, please?'),
        (Cu, 'Customer', "It's 12 Green Street."),
        (A, 'Agent', 'Thank you. Finally, let me confirm the details. A free repair on Tuesday morning at 12 Green Street.'),
        (Cu, 'Customer', 'Perfect. Thank you for your help!'),
    ],
    'items': [
        mcq('What is the problem?', ["The washing machine doesn't start.", 'The fridge is not cold.', 'The delivery is late.'], "The washing machine doesn't start."),
        gap('The washing machine is ____ months old.', 'ten', '10'),
        mcq('The repair is free.', TF, 'True'),
        mcq('Which two days can the repair person come?', ['Tuesday or Saturday', 'Monday or Friday', 'Tuesday or Thursday'], 'Tuesday or Saturday'),
        gap('The extra charge on Saturday is ____ pounds.', 'fifteen', '15'),
        mcq('When is the customer available?', ['Tuesday morning', 'Saturday morning', 'Tuesday afternoon'], 'Tuesday morning'),
        gap('Her address is 12 ____ Street.', 'Green'),
        mcq('What does the agent do at the end?', ['confirms the details', 'gives a refund', 'sends a replacement'], 'confirms the details'),
    ],
}]

SHADOW = {
    'title': 'A polite service call',
    'voice': SONIA,
    'sentences': [
        "Hello. I'm calling about my order.",
        'There seems to be a problem with the delivery. It is five days late.',
        'Could you check the delivery status for me?',
        'What are my options?',
        "I'd like to request a replacement. Do I need to pay an extra charge?",
        "I'm available on Friday morning. Could you confirm the details, please?",
    ],
}

TRANS = [
    ('Tôi gọi về đơn hàng của tôi.', ["I'm calling about my order.", 'I am calling about my order.'], "I'm calling about …"),
    ('Có vẻ như có vấn đề với chiếc máy tính xách tay của tôi.', ['There seems to be a problem with my laptop.'], 'There seems to be a problem with …'),
    ('Bạn có thể kiểm tra tình trạng giao hàng giúp tôi được không?', ['Could you check the delivery status for me?', 'Could you check the delivery status for me, please?'], 'Could you check … for me?'),
    ('Tôi có những lựa chọn nào?', ['What are my options?'], 'What are my options?'),
    ('Tôi rảnh vào sáng thứ Sáu. Bạn có thể xác nhận lại thông tin không?', ["I'm available on Friday morning. Could you confirm the details?", "I am available on Friday morning. Could you confirm the details?", "I'm available on Friday morning. Could you confirm the details, please?"], 'be available · confirm the details'),
]
