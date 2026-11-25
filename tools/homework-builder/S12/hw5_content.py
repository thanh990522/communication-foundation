"""S12 · Checkpoint 1: Everyday Life Simulation — written/listening TEST (homework format, no speaking part).
Reviews S01–S11 language; speaking is assessed live by the teacher."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

KIND = 'test'
TITLE = 'Checkpoint 1: Everyday Life Simulation'

VOCAB = [
    gap('How do you ____ your name? — L-I-N-H.', 'spell'),
    mcq('I usually have breakfast, but I ____ ever eat lunch at home.', ['hardly', 'never', 'always'], 'hardly'),
    mcq('Our apartment is centrally ____. Everything is near.', ['located', 'spacious', 'crowded'], 'located'),
    gap("I'm busy on Monday. Could we ____ the meeting to Tuesday?", 'move', 'reschedule'),
    mcq('The bank is across ____ the hospital.', ['from', 'to', 'of'], 'from'),
    gap("We're running ____ of milk. Can you buy some?", 'out'),
    mcq('Could we ____ the bill? That is twenty pounds each.', ['split', 'charge', 'recommend'], 'split'),
    gap("Please keep the ____. You need it for a refund.", 'receipt'),
    mcq('Could you check the delivery ____ for me? My order is late.', ['status', 'charge', 'replacement'], 'status'),
    gap('After the long trip, I felt ____ — I slept for ten hours!', 'exhausted'),
    mcq('I got up late and ____ the bus.', ['missed', 'lost', 'realised'], 'missed'),
    mcq('Thank you for your ____. It helps me improve my English.', ['feedback', 'challenge', 'solution'], 'feedback'),
]

GRAMMAR = [
    mcq('___ she work at weekends?', ['Does', 'Do', 'Is'], 'Does'),
    mcq('I ___ late for class.', ['am never', 'never am', 'never be'], 'am never'),
    mcq('There ___ two supermarkets near my home.', ['are', 'is', 'be'], 'are'),
    mcq("I ___ my teacher on Friday at 3 p.m. It's in my calendar.", ["'m meeting", 'meet', 'meeting'], "'m meeting"),
    mcq('Turn left ___ the intersection, then go straight on.', ['at', 'on', 'in'], 'at'),
    mcq('We need ___ eggs and a little butter.', ['a few', 'a little', 'much'], 'a few'),
    mcq('___ the tomato soup, please.', ["I'd like", 'I like', 'I want to'], "I'd like"),
    mcq("These jeans aren't long ___.", ['enough', 'too', 'very'], 'enough'),
    mcq('Could you ___ the details, please?', ['confirm', 'confirming', 'to confirm'], 'confirm'),
    mcq('There ___ to be a problem with my order.', ['seems', 'seem', 'is seems'], 'seems'),
    mcq('Last weekend, we ___ to the beach.', ['went', 'go', 'goed'], 'went'),
    mcq("We ___ stay overnight. We returned home at ten.", ["didn't", "weren't", "don't"], "didn't"),
    mcq('___ you late for work yesterday?', ['Were', 'Did', 'Was'], 'Were'),
    mcq('While I ___ waiting for the bus, it started to rain.', ['was', 'were', 'did'], 'was'),
]

READING = {
    'title': "Anna's busy Saturday",
    'passage': """Last Saturday was a very busy day for Anna.

In the morning, she went to a clothes shop in the city centre. She wanted to return a jacket because it was too small. Fortunately, she had the receipt, so she exchanged it for a bigger size. The shop assistant also offered her a ten per cent discount on a new T-shirt.

At twelve o'clock, she met her friend Mai at a small restaurant across from the park. To start with, they had tomato soup. For the main course, Anna had grilled chicken, but Mai has a nut allergy, so she asked for a curry without nuts. When the bill came, they split it — it was fifteen pounds each.

In the afternoon, Anna went home and called customer service. There seemed to be a problem with her new fridge — it wasn't cold enough. The agent was very helpful. He booked a repair service for Wednesday morning, with no extra charge.

In the evening, Anna was exhausted, but she was happy. It was a busy day, but everything was fine in the end.""",
    'items': [
        mcq('Why did Anna return the jacket?', ['It was too small.', 'It was damaged.', 'It was too expensive.'], 'It was too small.'),
        mcq('Anna got a refund for the jacket.', TF, 'False'),
        gap('The shop offered a ____ per cent discount on a T-shirt.', 'ten', '10'),
        mcq('Where was the restaurant?', ['across from the park', 'next to the shop', 'on the corner'], 'across from the park'),
        mcq('Why did Mai ask for a curry without nuts?', ['She has a nut allergy.', "She doesn't like nuts.", 'Nuts are expensive.'], 'She has a nut allergy.'),
        gap('They split the bill. It was ____ pounds each.', 'fifteen', '15'),
        mcq('What was the problem with the fridge?', ["It wasn't cold enough.", 'It was too big.', 'It was the wrong colour.'], "It wasn't cold enough."),
        mcq('When is the repair service?', ['Wednesday morning', 'Saturday afternoon', 'Monday morning'], 'Wednesday morning'),
    ],
}

A, C_ = RYAN, LIBBY
LISTEN = [
    {'title': 'A phone call: making an appointment', 'label': 'Receptionist & caller', 'hint': 'Nghe 2 lần rồi trả lời.',
     'lines': [
         (A, 'Receptionist', 'Good morning, City Dental Clinic. How can I help you?'),
         (C_, 'Caller', "Hello. I'm calling about my appointment. It's on Thursday at ten, but I'm working on Thursday morning."),
         (A, 'Receptionist', 'No problem. Could we move it to Friday? We have a time slot at half past two.'),
         (C_, 'Caller', 'Sorry, could you say that again, please?'),
         (A, 'Receptionist', 'Of course. Friday at half past two.'),
         (C_, 'Caller', 'Yes, Friday at two thirty works for me.'),
         (A, 'Receptionist', 'Great. Could you spell your surname, please?'),
         (C_, 'Caller', "Sure. It's Nguyen. N-G-U-Y-E-N."),
         (A, 'Receptionist', 'Thank you. Let me confirm: Friday at two thirty, Ms Nguyen.'),
         (C_, 'Caller', "That's right. Thank you very much."),
     ],
     'items': [
         mcq('When was the first appointment?', ['Thursday at ten', 'Friday at ten', 'Thursday at two thirty'], 'Thursday at ten'),
         mcq('Why does the caller want to change it?', ["She's working.", "She's ill.", "She's on holiday."], "She's working."),
         mcq('What is the new time?', ['Friday at 2:30', 'Friday at 10:00', 'Thursday at 2:30'], 'Friday at 2:30'),
         mcq('What does the caller ask the receptionist to do?', ['say it again', 'spell the name', 'call back later'], 'say it again'),
         gap("The caller's surname is ____.", 'Nguyen'),
     ]},
    {'title': 'A weekend story', 'label': 'Two friends on Monday', 'hint': 'Nghe 2 lần rồi trả lời.',
     'lines': [
         (C_, 'Lan', "You'll never guess what happened last weekend!"),
         (A, 'Ben', 'What happened?'),
         (C_, 'Lan', 'I visited Hue with my cousin. At first, everything was fine. We visited a local market and ate street food.'),
         (A, 'Ben', 'Nice! Did you stay overnight?'),
         (C_, 'Lan', 'Yes, we stayed in a small hotel. But on Sunday, while we were travelling to the station, I suddenly realised my bag was in the taxi!'),
         (A, 'Ben', 'Oh no! Did you get it back?'),
         (C_, 'Lan', 'Yes. Fortunately, the driver called the hotel. Eventually, he brought it to the station.'),
         (A, 'Ben', 'That was lucky! Did you miss the train?'),
         (C_, 'Lan', "No, we didn't. In the end, we got home at nine. I was exhausted, but it was a memorable trip!"),
     ],
     'items': [
         mcq('Where did Lan go last weekend?', ['to Hue', 'to Da Lat', 'to Hoi An'], 'to Hue'),
         mcq('Who did she go with?', ['her cousin', 'her sister', 'her friend Ben'], 'her cousin'),
         mcq('What did she realise?', ['Her bag was in the taxi.', 'She missed the train.', 'Her phone was at the hotel.'], 'Her bag was in the taxi.'),
         mcq('They missed the train.', TF, 'False'),
         gap('In the end, they got home at ____.', 'nine', '9'),
     ]},
]

TRANS = [
    ('Bạn đánh vần lại được không?', ['Could you spell that again?', 'Could you spell that again, please?', 'Could you spell it again, please?'], 'Could you … again?'),
    ('Có một siêu thị lớn gần nhà tôi.', ['There is a big supermarket near my home.', "There's a big supermarket near my home.", 'There is a big supermarket near my house.'], 'There is …'),
    ('Thứ Sáu có tiện cho bạn không?', ['Does Friday work for you?'], 'Does … work for you?'),
    ('Tôi muốn đổi chiếc áo khoác này lấy cỡ lớn hơn.', ["I'd like to exchange this jacket for a bigger size.", 'I would like to exchange this jacket for a bigger size.'], "I'd like to exchange …"),
    ('Có vẻ như có vấn đề với đơn hàng của tôi.', ['There seems to be a problem with my order.'], 'There seems to be …'),
    ('Cuối tuần trước, tôi đã ghé thăm một khu chợ địa phương.', ['Last weekend, I visited a local market.'], 'Last weekend, I …'),
    ('Trong khi tôi đang chờ, trời bắt đầu mưa.', ['While I was waiting, it started to rain.'], 'While I was …'),
]
