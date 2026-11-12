"""S04 · Appointments, dates & schedules — 5-part homework content (only S04 language)."""
from hw5 import mcq, gap, TF, SONIA

TITLE = 'Appointments: numbers, dates & messages'

VOCAB = [
    mcq('“hoãn (một cuộc họp)” in English is…', ['postpone', 'confirm', 'be available'], 'postpone'),
    mcq('“đổi lịch một cuộc hẹn” in English is…', ['reschedule an appointment', 'meet a deadline', 'confirm the time'], 'reschedule an appointment'),
    gap('I need to make an ____ with the dentist.', 'appointment'),
    gap('Are you ____ on Monday? — Yes, I’m free after 2 p.m.', 'available'),
    mcq('I have a busy ____ this week. I’m working every evening.', ['schedule', 'deadline', 'time slot'], 'schedule'),
    gap('Let me ____ the time: Tuesday at 3 p.m.', 'confirm'),
    mcq('I’m working late, so I can meet the ____.', ['deadline', 'appointment', 'schedule'], 'deadline'),
    mcq('Is there an available time ____ on Thursday?', ['slot', 'schedule', 'deadline'], 'slot'),
    mcq('The meeting is ____ Friday ____ 10 a.m.', ['on … at', 'at … on', 'in … at'], 'on … at'),
]

READING = {
    'title': 'Three short emails',
    'passage': """Hi Mr Brown,
I'm sorry, but I need to reschedule our appointment. It's on Wednesday the 13th at 2:30, but I'm meeting a client then. I have a busy schedule this week. Are you available on Thursday the 14th? Does 10 a.m. work for you?
Best, Mai

Hi Mai,
No problem. Unfortunately, I'm not available on Thursday morning because I have a deadline. But there is an available time slot on Friday the 15th at 3:15. Does that work for you?
Best, David Brown

Hi Mr Brown,
Yes, Friday works for me. Let me confirm: Friday the 15th at 3:15. See you then!
Mai""",
    'items': [
        mcq('Why does Mai need to reschedule?', ["She's meeting a client.", 'She has a deadline.', "She's at the dentist."], "She's meeting a client."),
        gap('The old appointment: Wednesday the ____', '13th', '13', 'thirteenth'),
        mcq('Mai has a busy schedule this week.', TF, 'True'),
        mcq('Mr Brown is available on Thursday morning.', TF, 'False'),
        mcq("Why isn't Mr Brown available on Thursday?", ['He has a deadline.', "He's meeting a client.", "He's having dinner with his family."], 'He has a deadline.'),
        gap('New appointment: Friday the 15th at ____', '3:15', '3.15', '315', 'quarterpastthree', '3:15pm', '3.15pm', '15:15'),
        mcq('In the last email, Mai…', ['confirms the time', 'postpones the meeting', 'makes a new appointment'], 'confirms the time'),
    ],
}

MSG_SCRIPT = [['Hoa (voicemail)', "Hi Nam, it's Hoa. Unfortunately, I'm meeting a client on Monday morning, so we are postponing our team meeting. "
               "Could we move it to Tuesday the 30th at half past ten instead? Does that work for you? Call me back. Thanks!"]]
CALL_SCRIPT = [
    ['Receptionist', 'Good afternoon, City Gym. How can I help you?'],
    ['Ken', 'Hi. I need to make an appointment for a yoga class, please. Are you available on Wednesday evening?'],
    ['Receptionist', 'Let me check. Unfortunately, the 7 p.m. class is full. We have an available time slot at 8:15.'],
    ['Ken', "8:15 doesn't work for me. I'm having dinner with my family then. Do you have a time slot on Thursday?"],
    ['Receptionist', 'Yes. Thursday at 6:30 is available.'],
    ['Ken', 'Great. 6:30 works for me.'],
    ['Receptionist', "So that's Thursday the 19th at 6:30?"],
    ['Ken', 'The 19th? Yes. Let me confirm: Thursday the 19th at 6:30.'],
    ['Receptionist', "That's right. What's your name, please?"],
    ['Ken', "It's Ken Lee. L-E-E."],
    ['Receptionist', 'Thank you, Mr Lee. See you on Thursday!'],
]

LISTEN = [
    {'title': "Hoa's voicemail", 'label': 'Voicemail · team meeting', 'hint': 'Nghe 2 lần, ghi lại thông tin.',
     'audio': 'homework/audio/S04/S04_listen_message.mp3', 'script': MSG_SCRIPT, 'items': [
         mcq('Why is Hoa postponing the meeting?', ["She's meeting a client.", "She's at the dentist.", 'She has a deadline.'], "She's meeting a client."),
         gap('New day: ____', 'Tuesday', 'Tue', 'Tues'),
         gap('New date: the ____', '30th', '30', 'thirtieth'),
         gap('New time: ____', '10:30', '10.30', '1030', 'halfpastten', '10:30am', '10.30am', '10:30a.m.'),
     ]},
    {'title': 'Booking a yoga class', 'label': 'City Gym · phone call', 'hint': 'Nghe 2 lần, điền phiếu đặt lịch.',
     'audio': 'homework/audio/S04/S04_listen_call.mp3', 'script': CALL_SCRIPT, 'note': 'CITY GYM — yoga class booking', 'items': [
         mcq('Why is the 7 p.m. class no good?', ['It is full.', 'It is late.', 'It is postponed.'], 'It is full.'),
         mcq("Why doesn't 8:15 work for Ken?", ["He's having dinner with his family.", "He's working late.", "He's meeting a client."], "He's having dinner with his family."),
         gap('Date: Thursday the ____', '19th', '19', 'nineteenth'),
         gap('Time: ____', '6:30', '6.30', '630', 'halfpastsix', '6:30pm', '6.30pm', '6:30p.m.', '18:30'),
     ]},
]

SHADOW = {
    'title': 'Leave a voicemail to reschedule a meeting',
    'voice': SONIA,
    'sentences': [
        "Hi Mark, it's Lan.",
        "I'm calling about our meeting on Monday.",
        "Unfortunately, I have a busy schedule on Monday, and I'm meeting a client in the afternoon.",
        'Could we move it to Wednesday the 13th instead?',
        "I'm available after 2 p.m. Does 3:30 work for you?",
        'Call me back, and let me confirm the time. Thanks!',
    ],
    'free': ['Mark', 'Lan'],
}

TRANS = [
    ('Bạn có rảnh vào chiều thứ Năm không?', ['Are you available on Thursday afternoon?'], 'Are you available on …?'),
    ('Tôi sẽ gặp bạn của tôi lúc 9 giờ sáng thứ Hai.',
     ["I'm meeting my friend at 9 a.m. on Monday.", "I'm meeting my friend on Monday at 9 a.m.", "I'm meeting my friend at 9 on Monday morning.", "I'm meeting my friend on Monday morning at 9."], "I'm …ing at / on … (kế hoạch)"),
    ('Thứ Sáu lúc 4 giờ chiều có tiện cho bạn không?', ['Does Friday at 4 p.m. work for you?', 'Does 4 p.m. on Friday work for you?'], 'Does … work for you?'),
    ('Chúng ta có thể dời cuộc hẹn sang ngày 20 không?', ['Could we move the appointment to the 20th?', 'Could we move our appointment to the 20th?'], 'Could we move it to …?'),
    ('Để tôi xác nhận lại: thứ Ba ngày 13 lúc 10 giờ 30.',
     ['Let me confirm: Tuesday the 13th at 10:30.', 'Let me confirm: Tuesday the 13th at half past ten.', 'Let me confirm the time: Tuesday the 13th at 10:30.'], 'Let me confirm: …'),
]
