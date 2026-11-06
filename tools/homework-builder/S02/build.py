"""Homework S02 — READING (two A2 texts).
Texts and questions use only the language of lesson S02 (routines, collocations, frequency adverbs,
present simple, first/then/after that/but/whereas/because) plus A1 routine verbs and clock times.
Writes homework/data/S02.json.  Run: python3 build.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SESSION = 'S02'

TEXT1 = """My name is Lucy. On weekdays, my day usually starts with a cup of coffee at six o'clock. I always have a productive morning because I get up early. I hardly ever miss breakfast.

First, I have breakfast at home. Then I make a daily commute to the city. It takes me forty-five minutes to get to work. I usually start work at eight. At eleven, I always take a short break. After that, I work until five, and I usually get home at six.

At weekends, my day is very different. I hardly ever get up early, and I never go to work. On weekdays I get up at six, whereas at weekends I usually get up at nine."""

TEXT2 = """Minh works the evening shift. On weekdays, he usually starts work at four o'clock and finishes at midnight. Because he finishes work late, he hardly ever gets up before nine.

His day usually starts with breakfast at ten. He doesn't make a long commute: it takes him ten minutes to get to work. He often has a productive morning before work. At work, he always takes a short break at eight.

Minh works every evening on weekdays, whereas at weekends he never works. He sometimes works on Friday evening, but he never works on Saturday or Sunday."""

TF = ['True', 'False']

def mcq(i, prompt, opts, ans):
    return {'id': i, 'type': 'mcq', 'prompt': prompt, 'options': opts, 'answers': [ans], 'show': ans, 'points': 1}

def gap(i, prompt, answers):
    return {'id': i, 'type': 'gap', 'prompt': prompt, 'answers': answers, 'show': answers[0], 'points': 1}

HOMEWORK = {
    'session': SESSION,
    'title': 'Routines, Habits & Real Schedules',
    'kind': 'Reading',
    'pass': 80,
    'sections': [
        {'id': 'A', 'title': "Text 1. Lucy's weekdays and weekends", 'passage': TEXT1, 'items': [
            mcq('A1', "Lucy's day usually starts with breakfast.", TF, 'False'),
            mcq('A2', 'Lucy often misses breakfast.', TF, 'False'),
            mcq('A3', 'It takes Lucy forty-five minutes to get to work.', TF, 'True'),
            mcq('A4', 'Lucy always takes a short break at eleven.', TF, 'True'),
            mcq('A5', 'Lucy sometimes goes to work at weekends.', TF, 'False'),
            gap('A6', 'Lucy usually starts work at ____.', ['eight', '8', "eight o'clock", "8 o'clock", '8:00']),
            gap('A7', 'At weekends, Lucy usually gets up at ____.', ['nine', '9', "nine o'clock", "9 o'clock", '9:00']),
        ]},
        {'id': 'B', 'title': "Text 2. Minh's evening shift", 'passage': TEXT2, 'items': [
            mcq('B1', 'What time does Minh usually start work?', ['at four', 'at ten', 'at midnight'], 'at four'),
            mcq('B2', 'How long does it take him to get to work?', ['four minutes', 'ten minutes', 'forty-five minutes'], 'ten minutes'),
            mcq('B3', 'How often does Minh get up before nine?', ['always', 'usually', 'hardly ever'], 'hardly ever'),
            mcq('B4', "Minh's day usually starts with…", ['a cup of coffee', 'breakfast at ten', 'a short break'], 'breakfast at ten'),
            mcq('B5', 'When does he take a short break?', ['at four', 'at eight', 'at ten'], 'at eight'),
            mcq('B6', 'Does Minh work at weekends?', ['Yes, always', 'Yes, sometimes', 'No, never'], 'No, never'),
        ]},
        {'id': 'C', 'title': 'Part 3. Language from the texts', 'items': [
            mcq('C1', 'Minh ____ the evening shift.', ['work', 'works', 'working'], 'works'),
            mcq('C2', 'Lucy hardly ever ____ breakfast.', ['miss', 'misses', 'missing'], 'misses'),
            mcq('C3', 'I make a ____ commute to the city.', ['daily', 'short', 'evening'], 'daily'),
            mcq('C4', '____ weekends, I usually get up late.', ['On', 'At', 'In'], 'At'),
            mcq('C5', 'On weekdays I work, ____ at weekends I never work.', ['because', 'whereas', 'then'], 'whereas'),
            mcq('C6', 'He hardly ever gets up before nine ____ he finishes work late.', ['because', 'whereas', 'first'], 'because'),
            gap('C7', 'It ____ me twenty minutes to get to work.', ['takes']),
            gap('C8', 'How ____ do you take a break? — I always take a short break at eleven.', ['often']),
        ]},
    ],
}

def build():
    hw = json.loads(json.dumps(HOMEWORK))
    hw['autoMax'] = sum(it['points'] for s in hw['sections'] for it in s['items'])
    out = os.path.join(ROOT, 'homework', 'data', f'{SESSION}.json')
    json.dump(hw, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('json ->', out, 'items', hw['autoMax'])

if __name__ == '__main__':
    build()
