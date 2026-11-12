"""S01 · Alphabet & Spelling — 5-part homework content (only S01 language)."""
from hw5 import mcq, gap, TF, SONIA

TITLE = 'Alphabet & Spelling Out Loud'

VOCAB = [
    mcq('In an email address, how do you say “@”?', ['at', 'dot', 'underscore'], 'at'),
    mcq('How do you say “_” in linh_tran@gmail.com?', ['underscore', 'hyphen', 'dot'], 'underscore'),
    mcq('How do you say “-” in mai-le@gmail.com?', ['hyphen', 'underscore', 'at'], 'hyphen'),
    mcq('How do you say the “tt” in SCOTT?', ['double T', 'two T', 'T T'], 'double T'),
    mcq('Which letter is in the same sound family as A, H and K?', ['J', 'G', 'E'], 'J'),
    mcq('emma.t88@gmail.com has no capital letters. It’s all ____.', ['lower case', 'capital', 'double'], 'lower case'),
    gap('Sorry, could you spell that ____, please?', 'again'),
    gap('What’s your email ____? — It’s nam.le@gmail.com.', 'address'),
]

READING = {
    'title': 'At the reception desk',
    'passage': """Linh is a new student at Bright English Centre. Today she is at the reception desk. The receptionist asks, "What's your name, please?" Linh says, "My name's Linh Tran." "How do you spell your first name?" "It's L-I-N-H." Her surname is easy: T-R-A-N.

Then the receptionist asks, "What's your email address?" Linh says, "It's linh underscore tran ninety-nine at gmail dot com. It's all lower case." The receptionist says, "Sorry, could you spell that again, please?" Linh spells it again, slowly.

Linh's friend is also at the desk. His name is Matthew Kelly. Matthew has a double T, and Kelly has a double L. "Is that K or C?" asks the receptionist. "K," says Matthew. His email address is matt dot kelly at yahoo dot com. "Is that a capital M?" "No, it's all lower case." """,
    'items': [
        mcq('Linh is a teacher at Bright English Centre.', TF, 'False'),
        mcq('How do you spell Linh’s surname?', ['T-R-A-N', 'T-R-A-M', 'T-R-A-N-G'], 'T-R-A-N'),
        gap('Linh’s email: linh ____ tran99@gmail.com (write the symbol or the word)', '_', 'underscore'),
        mcq('The receptionist asks Linh to spell her email address again.', TF, 'True'),
        mcq('Which name has a double L?', ['Kelly', 'Matthew', 'Linh'], 'Kelly'),
        mcq('What is Matthew’s email address?', ['matt.kelly@yahoo.com', 'matt_kelly@yahoo.com', 'matt-kelly@yahoo.com'], 'matt.kelly@yahoo.com'),
        mcq('Matthew’s email address has a capital M.', TF, 'False'),
    ],
}

CALL_SCRIPT = [
    ['Receptionist', 'Good afternoon, Lakeside Hotel. How can I help you?'],
    ['Emma', "Hi. I'd like to book a room for three nights, please."],
    ['Receptionist', 'Certainly. Can I have your name, please?'],
    ['Emma', "Yes. It's Emma Thornton."],
    ['Receptionist', 'How do you spell your surname?'],
    ['Emma', 'T-H-O-R-N-T-O-N.'],
    ['Receptionist', 'Thank you. And which town are you from?'],
    ['Emma', "I'm from Norwich. That's N-O-R-W-I-C-H."],
    ['Receptionist', "Lovely. What's your address, please?"],
    ['Emma', "It's fourteen Belmont Road. B-E-L-M-O-N-T."],
    ['Receptionist', 'Sorry, could you spell that again, please?'],
    ['Emma', 'Sure. B-E-L-M-O-N-T.'],
    ['Receptionist', 'Thanks. And your email address?'],
    ['Emma', "It's E-M-M-A dot T 8 8 at G-M-A-I-L dot C-O-M."],
    ['Receptionist', 'Is that all lower case?'],
    ['Emma', "Yes, it's all lower case."],
    ['Receptionist', 'Perfect. And what day will you arrive?'],
    ['Emma', 'On Friday, in the afternoon.'],
    ['Receptionist', "Great. That's three nights from Friday. See you then, Ms Thornton!"],
]

LISTEN = [{
    'title': 'Booking a hotel room', 'label': 'Lakeside Hotel · phone call', 'hint': 'Nghe 2 lần, điền phiếu đặt phòng.',
    'audio': 'homework/audio/S01/S01_listen_hotel.mp3', 'script': CALL_SCRIPT, 'note': 'LAKESIDE HOTEL — Booking form',
    'items': [
        mcq('How many nights?', ['three', 'two', 'four'], 'three'),
        gap('Guest name: Emma ____', 'Thornton'),
        gap('Home town: ____', 'Norwich'),
        gap('Address: 14 ____ Road', 'Belmont', 'Belmont Road'),
        mcq('What does the receptionist ask her to spell again?', ['her address', 'her surname', 'her email'], 'her address'),
        gap('Email: ____', 'emma.t88@gmail.com'),
        mcq('Is the email address all lower case?', ['Yes', 'No'], 'Yes'),
        gap('Arrival day: ____', 'Friday', 'Fri'),
    ],
}]

SHADOW = {
    'title': 'Introduce yourself at the reception desk',
    'voice': SONIA,
    'sentences': [
        "Hello, my name's Linh Tran.",
        'My first name is L-I-N-H, and my surname is T-R-A-N.',
        "I'm a new student at Bright English Centre.",
        'My email address is linh underscore tran at gmail dot com.',
        "It's all lower case.",
        "What's your name?",
        'How do you spell your surname?',
        'Sorry, could you spell that again, please?',
    ],
    'free': ['Linh', 'Tran', 'gmail'],
}

TRANS = [
    ('Bạn đánh vần tên của giáo viên bạn như thế nào?', ["How do you spell your teacher's name?"], 'How do you spell …?'),
    ('Xin lỗi, bạn có thể đánh vần lại họ của bạn được không?',
     ['Sorry, could you spell your surname again, please?', 'Sorry, could you spell your surname again?', 'Could you spell your surname again, please?'], 'Sorry, could you spell … again, please?'),
    ('Địa chỉ email của bạn của bạn là gì?', ["What's your friend's email address?"], "What's … email address?"),
    ('Email của tôi là nam.le@gmail.com. Tất cả đều viết thường.',
     ["My email address is nam.le@gmail.com. It's all lower case.", "My email is nam.le@gmail.com. It's all lower case."], "My email address is … It's all lower case."),
    ('Có phải chữ J như trong “John” không?', ['Is that J as in John?'], 'Is that … as in …?'),
]
