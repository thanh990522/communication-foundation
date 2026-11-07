"""Lesson S04 — Time, Appointments & Arrangements.
Language limited to the S04 syllabus items plus the A1 time words taught on the 'on · at · in' slide:
  collocations : a busy schedule · make an appointment · be available · postpone a meeting ·
                 reschedule an appointment · confirm the time · meet a deadline · an available time slot
  frames       : Are you available on ___? · Does ___ work for you? · Could we move it to ___? · Let me confirm ___.
  grammar      : present continuous for future arrangements
  linkers      : first · unfortunately · instead · so · finally
  pronunciation: numbers, dates and times · rising intonation for confirmation questions
"""

# ---------------------------------------------------------------- warm-up: say the time / date
WARM = [  # front, emoji, answer (said)
    ('3:30', '🕞', 'three thirty / half past three'),
    ('9:15', '🕘', 'nine fifteen / quarter past nine'),
    ('7:45', '🕣', 'seven forty-five / quarter to eight'),
    ('12:00', '🕛', 'twelve o’clock'),
    ('Mon 3rd', '📅', 'Monday the third'),
    ('Fri 21st', '📅', 'Friday the twenty-first'),
    ('Sat 12th', '📅', 'Saturday the twelfth'),
    ('Sun 30th', '📅', 'Sunday the thirtieth'),
]

# ---------------------------------------------------------------- time words: on · at · in
TIMEW = [  # preposition, use, examples
    ('on', 'days · dates', ['on Monday', 'on Friday the 21st', 'on the weekend']),
    ('at', 'clock times', ['at 3 p.m.', 'at half past ten', 'at 9 o’clock']),
    ('in', 'parts of the day', ['in the morning', 'in the afternoon', 'in the evening']),
]
ORDINALS = ['1st', '2nd', '3rd', '4th', '12th', '20th', '21st', '22nd', '23rd', '30th']
ORD_SAY = ['first', 'second', 'third', 'fourth', 'twelfth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'thirtieth']

# ---------------------------------------------------------------- core words -> collocations
VOCAB = [
    dict(k='schedule', w='schedule', pos='noun', ipa='/ˈʃedjuːl/', vi='lịch trình',
         col='a busy schedule', kw='schedule', col_vi='một lịch trình bận rộn', ex='I have a busy schedule this week.'),
    dict(k='appointment', w='appointment', pos='noun', ipa='/əˈpɔɪntmənt/', vi='cuộc hẹn',
         col='make an appointment', kw='appointment', col_vi='đặt một cuộc hẹn', ex='I need to make an appointment with the dentist.'),
    dict(k='available', w='available', pos='adjective', ipa='/əˈveɪləbl/', vi='rảnh, có thể gặp',
         col='be available', kw='available', col_vi='rảnh, có thời gian', ex='Are you available on Monday?'),
    dict(k='postpone', w='postpone', pos='verb', ipa='/pəˈspəʊn/', vi='hoãn',
         col='postpone a meeting', kw='postpone', col_vi='hoãn một cuộc họp', ex='We are postponing the meeting to Friday.'),
    dict(k='reschedule', w='reschedule', pos='verb', ipa='/ˌriːˈʃedjuːl/', vi='đổi lịch',
         col='reschedule an appointment', kw='reschedule', col_vi='đổi lịch một cuộc hẹn', ex='I need to reschedule my appointment.'),
    dict(k='confirm', w='confirm', pos='verb', ipa='/kənˈfɜːm/', vi='xác nhận',
         col='confirm the time', kw='confirm', col_vi='xác nhận thời gian', ex='Let me confirm the time: Tuesday at 3 p.m.'),
    dict(k='deadline', w='deadline', pos='noun', ipa='/ˈdedlaɪn/', vi='hạn chót',
         col='meet a deadline', kw='deadline', col_vi='kịp hạn chót', ex='I am working late, so I can meet the deadline.'),
    dict(k='time slot', w='time slot', pos='noun', ipa='/ˈtaɪm slɒt/', vi='khung giờ',
         col='an available time slot', kw='time slot', col_vi='một khung giờ trống', ex='Is there an available time slot on Thursday?'),
]

COLL = [  # sentence, options, answer, illustration key
    ('I have a ___ schedule this week.', ['busy', 'available', 'late'], 'busy', 'schedule'),
    ('I need to ___ an appointment with the dentist.', ['make', 'meet', 'do'], 'make', 'appointment'),
    ('Are you ___ on Monday?', ['available', 'busy', 'free time'], 'available', 'available'),
    ('We are ___ the meeting to Friday.', ['postponing', 'confirming', 'meeting'], 'postponing', 'postpone'),
    ('I need to ___ my appointment. I am busy on Tuesday.', ['reschedule', 'confirm', 'meet'], 'reschedule', 'reschedule'),
    ('Let me ___ the time: Tuesday at 3 p.m.', ['confirm', 'postpone', 'make'], 'confirm', 'confirm'),
    ('I am working late, so I can ___ the deadline.', ['meet', 'make', 'confirm'], 'meet', 'deadline'),
    ('Is there an available time ___ on Thursday?', ['slot', 'line', 'table'], 'slot', 'time slot'),
]

# ---------------------------------------------------------------- grammar: present continuous for arrangements
GRAM = [  # title, pattern, example
    ('Arrangement +', 'I am / She is + V-ing + time', "I'm meeting Lan on Friday."),
    ('Arrangement –', "I'm not / She isn't + V-ing", "I'm not working on Sunday."),
    ('Question ?', 'Are you / Is she + V-ing …?', 'What are you doing on Saturday?'),
    ('Time words', 'on Monday · at 3 p.m. · this weekend · tomorrow', 'We are having a meeting tomorrow at 9.'),
]
GRAM_QA = [  # question, yes, no
    ('Are you working on Saturday?', 'Yes, I am.', "No, I'm not."),
    ('Is she meeting the teacher tomorrow?', 'Yes, she is.', "No, she isn't."),
]
# Mai's diary (illustration DIARY) and questions — answers match the diary
DIARY = [  # day, time, entry
    ('Mon', '10:00', 'meet her teacher'), ('Tue', '3:30', 'dentist appointment'),
    ('Wed', '—', 'free'), ('Thu', '7:00 p.m.', 'study call with Lan'), ('Fri', '5:00', 'deadline: report'),
]
DIARYQ = [
    ('On Monday, Mai ___ her teacher at 10.', ['is meeting', 'meets', 'meet'], 'is meeting'),
    ('On Tuesday, she ___ to the dentist at 3:30.', ['is going', 'goes', 'are going'], 'is going'),
    ('Is Mai available on Wednesday?', ['Yes, she is.', "No, she isn't."], 'Yes, she is.'),
    ('On Thursday, she ___ a study call with Lan.', ['is having', 'has', 'are having'], 'is having'),
    ('What time is the study call?', ['at 7 p.m.', 'at 10 a.m.', 'at 3:30'], 'at 7 p.m.'),
    ('Her deadline is on ___.', ['Friday', 'Monday', 'Wednesday'], 'Friday'),
]

# ---------------------------------------------------------------- pronunciation 1: numbers (13 vs 30)
PAIRS = [('13', '30', 'thirTEEN', 'THIRty'), ('14', '40', 'fourTEEN', 'FORty'), ('15', '50', 'fifTEEN', 'FIFty'),
         ('16', '60', 'sixTEEN', 'SIXty'), ('17', '70', 'sevenTEEN', 'SEVenty'), ('18', '80', 'eighTEEN', 'EIGHTy'),
         ('19', '90', 'nineTEEN', 'NINEty')]
# listen-and-choose: which one does the speaker say? (index into the pair)
PAIR_TEST = [('The meeting is on the ___th.', 0, 0), ('My appointment is at 3:___.', 1, 1), ('It costs ___ dollars.', 2, 0),
             ('Room ___, please.', 3, 1), ('Bus number ___.', 4, 0), ('The deadline is on the ___th.', 5, 0), ('I need ___ minutes.', 6, 1)]

# ---------------------------------------------------------------- pronunciation 2: rising intonation to confirm
CONFIRM_Q = ['So that’s Tuesday at three?', 'Monday the 21st?', 'Half past ten?', 'At 7 p.m. on Thursday?', 'The 13th, not the 30th?']
CONFIRM_S = ['Let me confirm: Tuesday at three.', 'Yes, Monday the 21st.', 'Yes, half past ten.', 'That’s right. Thursday at 7 p.m.', 'Yes, the 13th.']

# ---------------------------------------------------------------- listening (real recording)
LISTEN = {
    'title': 'Plans for the Weekend — Sarah & Todd',
    'source': 'elllo.org · A2 Lesson 14 · Present Continuous for Future (Todd Beuckens)',
    'page': 'https://elllo.org/english/grammar/A2-14-Present-Continuous-Future-Todd-Sarah-Hiking-Plans.htm',
    'file': 'Listening/S04_listening_Sarah_Todd_weekend_plans.mp3',
    'dur': 232,
    'names': {'S': 'Sarah', 'T': 'Todd'},
    'script': [
        ('T', 'So Sarah, what are your plans for the weekend?'),
        ('S', "I have really fun plans this weekend. On Saturday I'm meeting some friends, and we're going to hike up a nearby mountain. It's called Mount Tsurumi, and I think it'll be really fun."),
        ('T', 'Oh, cool. How are you getting up the mountain? How are you getting up to the hiking point?'),
        ('S', "We're going to take the bus, probably. So we'll take a bus until the base of the mountain, and then we can hike to the top. We'll hike about four or five hours, depending on how much time I spend resting."),
        ('T', 'Okay, which is a lot. So who is going with you?'),
        ('S', "I'm meeting three friends, and they are all English teachers like me. So my friends' names are Hannah and Ben and Michael."),
        ('T', "Oh, nice. So, I'm sorry, where are you hiking again?"),
        ('S', "So we're hiking at the mountain called Mount Tsurumi. It's pretty close to my house. It's not far, so I can see it from my window, my bedroom window. And I always think, oh, I would love to go to the top of that mountain. So I'm really happy on Saturday to go and hike the mountain. Then after we reach the top, we take the cable car down the mountain."),
        ('T', "Oh, I see. So you're hiking up the mountain, and then you're taking the cable car down."),
        ('S', "Yes, so it'll probably be six hours in total, between hiking and resting and cable car back down."),
        ('T', 'What time are you starting?'),
        ('S', "We're starting at 10 o'clock. We're starting at 10 o'clock so that we can finish at 4 o'clock, and I can still get my children from school. Their school finishes at 5 o'clock."),
        ('T', "Oh, wow. So you're really pushing it."),
        ('S', "Yeah, the timing will be tight, but I think it'll be okay."),
        ('T', 'Oh, cool.'),
        ('S', 'How about you, Todd? What are you doing on Saturday?'),
        ('T', "This weekend, I'm not really doing anything. I think I'm just gonna stay home. So I'm leaving for Thailand on Thursday. I'm flying out of Fukuoka."),
        ('S', 'Oh, that sounds really nice.'),
        ('T', "Yeah, but actually, now that I think of it, I am doing something on Saturday. My friend is having a dinner party, so I'm planning on attending that. So that should be fun."),
        ('S', 'Oh, that sounds fun. What time does it start?'),
        ('T', "I think it starts at about eight, right? So most people will probably be there around eight o'clock. I'm not planning on staying that long, so I'm just going to go and make a short appearance and then come back. Now, we are teachers, so we have grading to do. Are you doing any work this weekend? Are you grading any papers?"),
        ('S', "Yes, I'm grading some papers. My students are handing in their papers tomorrow, and then I'm grading them all day Sunday."),
        ('T', 'Yikes.'),
        ('S', "Yeah, so it won't be exciting, but I think if I work hard, I should be able to finish them."),
        ('T', "Yeah, I'm in the same boat, actually. So I have lots of papers to grade, and I want them finished. So I think I will do it on Friday night. I'm planning on staying late Friday and just doing it then."),
        ('S', 'Okay.'),
        ('T', "Yeah, so I'm not looking forward to it."),
        ('S', "So you'll be grading all night on Friday."),
        ('T', "I'll be grading all night on Friday. I won't be doing anything fun. But I'll be leaving on Sunday, so it'll be worth it."),
        ('S', 'Okay. Have fun. Have a good trip.'),
        ('T', 'You too. Enjoy the hike.'),
        ('S', 'Thanks.'),
    ],
    'gist': ('What is Sarah doing on Saturday?', ['hiking up a mountain', 'going to a dinner party'], 'hiking up a mountain'),
    'detail': [
        ('Sarah is meeting ___ friends.', ['two', 'three', 'four'], 'three'),
        ('Sarah and her friends are starting at ___.', ['8 o’clock', '10 o’clock', '4 o’clock'], '10 o’clock'),
        ("On Saturday, Todd's friend is having a ___.", ['dinner party', 'meeting', 'birthday party'], 'dinner party'),
        ('Sarah is grading papers all day on ___.', ['Friday', 'Saturday', 'Sunday'], 'Sunday'),
        ('Todd is staying late to grade papers on ___ night.', ['Thursday', 'Friday', 'Saturday'], 'Friday'),
    ],
    'times': [
        ('They want to finish the hike at ___ o’clock.', ['4', 'four', "4 o'clock", '4 o’clock', '4:00']),
        ("Sarah's children's school finishes at ___ o’clock.", ['5', 'five', "5 o'clock", '5 o’clock', '5:00']),
        ('The dinner party starts at about ___.', ['8', 'eight', "8 o'clock", '8 o’clock', '8:00', '8 pm', '8 p.m.']),
    ],
}

# ---------------------------------------------------------------- sentence frames
FRAMES = [
    ('Are you available on ___?', ['Are you available on Monday?', 'Are you available on Friday afternoon?']),
    ('Does ___ work for you?', ['Does 3 p.m. work for you?', 'Does Thursday at half past seven work for you?']),
    ('Could we move it to ___?', ['Could we move it to Wednesday?', 'Could we move it to 4:30?']),
    ('Let me confirm ___.', ['Let me confirm the time: Tuesday at 3 p.m.', 'Let me confirm the date: Friday the 21st.']),
]
LINKERS = ['first', 'unfortunately', 'instead', 'so', 'finally']

# ---------------------------------------------------------------- questions & answers
QA = [
    ('What are you doing on Saturday?', ["I'm meeting my friends at 10.", "I'm not doing anything. I'm free."]),
    ('Are you available on Monday?', ["Yes, I am. I'm free in the afternoon.", "Unfortunately, I'm not. I have a busy schedule."]),
    ('Does 3 p.m. work for you?', ['Yes, 3 p.m. works for me.', "Unfortunately, it doesn't. Could we move it to 4?"]),
    ('Could we move it to Thursday?', ['Sure. Thursday works for me.', "Sorry, I'm working on Thursday. Could we meet on Friday instead?"]),
    ('When is your deadline?', ['It is on Friday the 21st.', "It's tomorrow at 5 p.m., so I'm working late."]),
    ('Do you have an available time slot on Tuesday?', ['Yes. We have an available time slot at 3:30.', "Sorry, we're busy on Tuesday. Is Wednesday OK?"]),
    ('Why are you postponing the meeting?', ["Because the manager is meeting a client on Monday.", "Because I'm visiting a customer that day."]),
    ('So that’s Tuesday at three?', ["Yes, that's right. See you then.", 'No, Tuesday at half past three.']),
]

# ---------------------------------------------------------------- model dialogue (phone call: Nam & receptionist)
DIALOGUE = [
    ('R', 'Good morning, Smile Dental Clinic. How can I help you?'),
    ('N', 'Hi, this is Nam. I need to make an appointment, please.'),
    ('R', 'Of course. Are you available on Tuesday?'),
    ('N', "Unfortunately, I'm working all day on Tuesday. Do you have an available time slot on Wednesday?"),
    ('R', 'Let me check. Yes, we have a time slot at 10:30 or at 4:15.'),
    ('N', '4:15 works for me.'),
    ('R', "Great. What's your surname, please?"),
    ('N', "It's Tran. T-R-A-N."),
    ('R', "Thank you. So that's Wednesday the 13th at 4:15?"),
    ('N', 'The 13th? Not the 30th?'),
    ('R', 'Yes, the 13th. Wednesday the 13th at 4:15.'),
    ('N', 'Perfect. Let me confirm: Wednesday the 13th at 4:15.'),
    ('R', "That's right. See you on Wednesday, Mr Tran."),
    ('N', 'Thanks. Bye!'),
]
DLG_NAMES = {'R': 'Receptionist', 'N': 'Nam'}
DLG_Q = [
    ('Why is Tuesday no good for Nam?', ["He's working all day.", "He's meeting a friend."], "He's working all day."),
    ('Which day does Nam choose?', ['Tuesday', 'Wednesday', 'Thursday'], 'Wednesday'),
    ('What time is the appointment?', ['10:30', '4:15', '4:50'], '4:15'),
    ('What is the date?', ['the 13th', 'the 30th', 'the 3rd'], 'the 13th'),
]
CARD = [('Name', 'Nam Tran', ['tran', 'namtran', 'mrtran']), ('Day', 'Wednesday', ['wednesday', 'wed']),
        ('Date', '13th', ['13th', '13', 'thirteenth', 'the13th']), ('Time', '4:15', ['4:15', '4.15', '415', 'quarterpastfour', '4:15pm'])]

# ---------------------------------------------------------------- pair practice: find a time (information gap)
SLOTS = ['9:00', '11:00', '2:00', '4:30', '7:00']
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
DIARY_A = {('Mon', '9:00'): 'work meeting', ('Mon', '2:00'): 'dentist', ('Tue', '11:00'): 'English class', ('Tue', '4:30'): 'gym',
           ('Wed', '9:00'): 'work meeting', ('Wed', '7:00'): 'dinner with Mum', ('Thu', '2:00'): 'deadline', ('Thu', '7:00'): 'study call',
           ('Fri', '11:00'): 'meet a client', ('Fri', '4:30'): 'football', ('Mon', '7:00'): 'gym'}
DIARY_B = {('Mon', '11:00'): 'doctor', ('Mon', '4:30'): 'English class', ('Tue', '9:00'): 'work meeting', ('Tue', '2:00'): 'interview',
           ('Wed', '11:00'): 'shopping', ('Wed', '2:00'): 'busy', ('Thu', '9:00'): 'team meeting', ('Thu', '4:30'): 'swimming',
           ('Fri', '7:00'): 'cinema', ('Fri', '2:00'): 'deadline', ('Tue', '7:00'): 'dinner with friends', ('Fri', '9:00'): 'work meeting'}
GAP_FRAMES = ['Are you available on ___ at ___?', "Unfortunately, I'm ___ing then.", 'Does ___ work for you?', 'Let me confirm: ___ at ___.']

# ---------------------------------------------------------------- free practice (frame = model dialogue)
SITUATIONS = [
    {'e': '🦷', 't': 'Make a dentist appointment', 'a': 'Receptionist', 'b': 'You',
     'goal': 'Offer two time slots and confirm the day, date and time.',
     'card': ['Busy on Tuesday', 'Free Thursday afternoon', 'Choose the 14th or the 40th? → the 14th!']},
    {'e': '💼', 't': 'Reschedule a meeting', 'a': 'Colleague', 'b': 'You',
     'goal': 'Your meeting is on Monday at 9. Move it.',
     'card': ['Monday 9:00 — meeting a client', 'Free: Monday 4:30 or Tuesday 11:00', 'Deadline on Wednesday']},
]
FP_LINES = [
    ('A', 'Are you available on {day}?'),
    ('B', "Unfortunately, I'm {V-ing} on {day}. Could we move it to {day / time}?"),
    ('A', 'Let me check. We have an available time slot at {time} or at {time}.'),
    ('B', '{time} works for me.'),
    ('A', "So that's {day} the {date} at {time}?"),
    ('B', 'Yes. Let me confirm: {day} the {date} at {time}.'),
    ('A', "That's right. See you on {day}!"),
]

# ---------------------------------------------------------------- real-life task: arrange a study call by text
CHAT = [
    ('me', 'Hi Lan! Are you available on Thursday evening for a study call? 📞'),
    ('you', "Hi! Unfortunately, I'm working late on Thursday. Could we move it to Friday?"),
    ('me', 'Sure. Does 8 p.m. work for you?'),
    ('you', 'Yes! Let me confirm: Friday at 8 p.m. 👍'),
    ('me', 'Perfect. See you on Friday!'),
]
ROLECARDS = [
    ('📚', 'Study call', 'Arrange a study call with a classmate this week. You are busy on Wednesday.'),
    ('🦷', 'Dentist', 'Call the clinic. Make an appointment. Check the date: 15th or 50th?'),
    ('💼', 'Meeting', 'Your boss wants a meeting on Friday at 9. You have a deadline. Reschedule it.'),
    ('☕', 'Coffee', 'Invite a friend for coffee. Your friend postpones. Find a new time slot.'),
    ('🏋️', 'Gym class', 'Book a gym class. The 7 p.m. class is full. Ask for another time slot.'),
    ('🎂', 'Birthday', 'Plan a birthday dinner with a friend. Confirm the day, date and time.'),
]

# ---------------------------------------------------------------- game: sentence scramble
SCRAMBLE = [
    'Are you available on Monday?',
    'Does 3 p.m. work for you?',
    'Could we move it to Friday?',
    'Let me confirm the time.',
    "I'm meeting my teacher on Tuesday.",
    'I need to reschedule my appointment.',
    'We are postponing the meeting.',
    'Is there an available time slot?',
]
