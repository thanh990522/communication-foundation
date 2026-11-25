"""S10 · Past Events: What Happened? — 5-part homework content (only S10 language)."""
from hw5 import mcq, gap, TF, SONIA, RYAN, LIBBY

TITLE = 'Past Events: What Happened?'

VOCAB = [
    mcq('“tham dự một sự kiện” — ____ an event', ['attend', 'visit', 'return'], 'attend'),
    gap('On Sunday morning, we ____ a local market.', 'visited'),
    mcq('We stayed ____ in a small hotel.', ['overnight', 'memorable', 'exhausted'], 'overnight'),
    gap('We ____ home on Sunday evening.', 'returned'),
    mcq('I really ____ the experience. It was great!', ['enjoyed', 'attended', 'stayed'], 'enjoyed'),
    gap('After the long walk, I felt ____. I needed a long sleep.', 'exhausted'),
    mcq('It was a ____ trip. I will never forget it.', ['memorable', 'exhausted', 'local'], 'memorable'),
    gap('There was a big weekend ____ at the park.', 'event'),
    mcq('Last weekend, I ____ to the beach.', ['went', 'go', 'goed'], 'went'),
    mcq("We didn't ____ to the waterfall.", ['go', 'went', 'going'], 'go'),
]

READING = {
    'title': 'My weekend in Hoi An',
    'passage': """Last weekend, I visited Hoi An with my best friend, Lan. We left Da Nang on Saturday morning and arrived in Hoi An at nine o'clock.

First, we visited a local market. We ate some street food and I bought a small souvenir for my mother. Then we walked around the old town and took lots of photos. In the evening, we attended a weekend event by the river. There was music and there were lots of people. It was beautiful!

We stayed overnight in a small hotel near the river. It wasn't expensive, and the people were very friendly.

On Sunday, it rained all morning, so we didn't go to the beach. Although it rained, we enjoyed the experience. We had a chance to try a cooking class instead.

In the end, we returned home on Sunday evening. I was exhausted, but it was worth it. It was a memorable trip!""",
    'items': [
        mcq('Who did the writer go with?', ['her best friend', 'her mother', 'her family'], 'her best friend'),
        mcq('What did they do first?', ['They visited a local market.', 'They went to the beach.', 'They took a cooking class.'], 'They visited a local market.'),
        mcq('The writer bought a souvenir for her mother.', TF, 'True'),
        gap('In the evening, they attended a weekend ____ by the river.', 'event'),
        mcq('The hotel was very expensive.', TF, 'False'),
        mcq("Why didn't they go to the beach?", ['It rained.', 'They were tired.', 'It was closed.'], 'It rained.'),
        mcq('How did the writer feel at the end?', ['exhausted, but happy', 'bored', 'angry'], 'exhausted, but happy'),
    ],
}

A, B_ = LIBBY, RYAN
LISTEN = [{
    'title': "Minh's weekend", 'label': 'Two friends on Monday', 'hint': 'Nghe 2 lần rồi trả lời.',
    'lines': [
        (A, 'Sara', 'Hi Minh! How was your weekend?'),
        (B_, 'Minh', 'It was great, thanks. Last weekend, I attended a food event in the city centre.'),
        (A, 'Sara', 'Oh, nice!'),
        (B_, 'Minh', 'First, I met my cousins at the bus station. Then we went to the event together.'),
        (B_, 'Minh', 'I had a chance to try food from ten different countries. The best part was the Korean food.'),
        (A, 'Sara', 'Did you stay overnight in the city?'),
        (B_, 'Minh', "Yes, we stayed overnight at my cousin's apartment. We didn't sleep much!"),
        (A, 'Sara', 'Ha ha. When did you return home?'),
        (B_, 'Minh', 'I returned home on Sunday afternoon. Although the bus was late, I enjoyed the whole trip.'),
        (A, 'Sara', 'You look tired.'),
        (B_, 'Minh', 'I was exhausted, but it was worth it!'),
    ],
    'items': [
        mcq('What did Minh attend?', ['a food event', 'a music event', 'a cooking class'], 'a food event'),
        gap('First, he met his ____ at the bus station.', 'cousins'),
        gap('He tried food from ____ different countries.', 'ten', '10'),
        mcq('What was the best part?', ['the Korean food', 'the Thai food', 'the music'], 'the Korean food'),
        mcq('Where did they stay overnight?', ["at his cousin's apartment", 'in a hotel', 'at home'], "at his cousin's apartment"),
        mcq('They slept a lot.', TF, 'False'),
        mcq('When did Minh return home?', ['on Sunday afternoon', 'on Sunday evening', 'on Monday morning'], 'on Sunday afternoon'),
        mcq('What was late?', ['the bus', 'the train', 'his cousin'], 'the bus'),
    ],
}]

SHADOW = {
    'title': 'Tell me about your weekend',
    'voice': SONIA,
    'sentences': [
        'Last weekend, I visited a local market with my family.',
        'Then we attended a weekend event in the park.',
        'I had a chance to try some local food.',
        'The best part was the night market.',
        "It rained on Sunday, so we didn't go to the beach.",
        'I was exhausted, but it was worth it.',
    ],
}

TRANS = [
    ('Cuối tuần trước, tôi đã ghé thăm một khu chợ địa phương.', ['Last weekend, I visited a local market.'], 'Last weekend, I …'),
    ('Tôi đã có cơ hội tham dự một sự kiện lớn.', ['I had a chance to attend a big event.'], 'I had a chance to …'),
    ('Phần hay nhất là đồ ăn đường phố.', ['The best part was the street food.'], 'The best part was …'),
    ('Chúng tôi đã không ở lại qua đêm.', ["We didn't stay overnight.", 'We did not stay overnight.'], "didn't + verb"),
    ('Tôi đã kiệt sức, nhưng nó rất xứng đáng.', ['I was exhausted, but it was worth it.'], 'I was …, but it was worth it.'),
]
