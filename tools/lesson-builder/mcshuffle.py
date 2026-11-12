"""Balanced, deterministic option shuffling for multiple-choice items.
Correct answers are spread evenly over the positions (A/B/C…), never in the same position
three times in a row, and the result is the same on every build (seeded).
Yes/No and True/False pairs keep their natural order."""
import random


def _natural(opts):
    lo = [str(o).lower() for o in opts]
    return (len(opts) == 2 and (lo[0].startswith('yes') and lo[1].startswith('no') or lo == ['true', 'false']))


def _targets(ks, rng):
    """answer position per question: balanced (counts differ by at most 1–2), random-looking, no run of 3"""
    out, count = [], {}
    for k in ks:
        lo = min(count.get(p, 0) for p in range(k))
        cand = [p for p in range(k) if count.get(p, 0) <= lo + (1 if k > 2 else 0)]
        if len(out) >= 2 and out[-1] == out[-2] and len(cand) > 1:
            cand = [p for p in cand if p != out[-1]] or cand
        if k == 2 and len(out) >= 3 and out[-1] != out[-2] and out[-2] != out[-3] and out[-1] in cand and len(cand) > 1:
            cand = [out[-1]]                                # break strict ABAB alternation
        p = rng.choice(cand); out.append(p); count[p] = count.get(p, 0) + 1
    return out


def reorder(opts, ans, pos, rng):
    rest = [o for o in opts if o != ans]; rng.shuffle(rest)
    return rest[:pos] + [ans] + rest[pos:]


def shuffle_rows(rows, seed, qi=0, oi=1, ai=2):
    """rows: tuples like (question, options, answer, ...). Returns new list of tuples."""
    rng = random.Random(seed)
    idx = [i for i, r in enumerate(rows) if not _natural(r[oi])]
    tg = dict(zip(idx, _targets([len(rows[i][oi]) for i in idx], rng)))
    out = []
    for i, r in enumerate(rows):
        r = list(r)
        if i in tg: r[oi] = reorder(r[oi], r[ai], tg[i], rng)
        out.append(tuple(r))
    return out


def shuffle_items(items, seed):
    """homework item dicts with 'options' and 'answers' (mcq / listen_mcq)."""
    rng = random.Random(seed)
    idx = [i for i, it in enumerate(items) if it.get('type') in ('mcq', 'listen_mcq') and not _natural(it['options'])]
    tg = dict(zip(idx, _targets([len(items[i]['options']) for i in idx], rng)))
    for i, p in tg.items():
        items[i]['options'] = reorder(items[i]['options'], items[i]['answers'][0], p, rng)
    return items


def shuffle_content(C, sid):
    """apply to a lesson content module in place"""
    for name in ('COLL', 'MAPQ', 'DIARYQ', 'DLG_Q', 'RACE'):
        if hasattr(C, name): setattr(C, name, shuffle_rows(getattr(C, name), f'{sid}-{name}'))
    if hasattr(C, 'LISTEN'):
        L = C.LISTEN
        L['detail'] = [list(r) for r in shuffle_rows(L['detail'], f'{sid}-LD')]
        g = L['gist']
        if not _natural(g[1]):
            L['gist'] = (g[0], reorder(g[1], g[2], sum(map(ord, sid)) % len(g[1]), random.Random(sid)), g[2])
    return C
