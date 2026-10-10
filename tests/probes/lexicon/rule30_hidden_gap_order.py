#!/usr/bin/env python3
"""GC993: locate GC992's gap-order discriminator in an exact right strip.
Prediction (registered in RULE30-GPT before original run): separating k<=10.
No SAT, invariant or all-depth bound. Full compatible state sets retained.
Controls: bitwise whole-row update vs literal Rule30 table; split continuation;
unexpected check: projection from width k to k-1. Data not saved.
COMMAND: python3 tests/probes/lexicon/rule30_hidden_gap_order.py
"""
X, Y, Z = '100010100001', '101000100001', '0001'
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)

def transitions(k):
    mask = (1 << k) - 1
    tables = []
    for wall in (0, 1):
        table = []
        for q in range(1 << k):
            row = []
            for d in (0, 1):
                left = ((q << 1) | wall) & mask
                right = (q >> 1) | (d << (k - 1))
                out = left ^ (q | right)
                literal = 0
                for i in range(k):
                    a = wall if i == 0 else (q >> (i - 1)) & 1
                    b = (q >> i) & 1
                    c = d if i == k - 1 else (q >> (i + 1)) & 1
                    literal |= TABLE[4*a + 2*b + c] << i
                assert out == literal
                row.append(out)
            table.append(row)
        tables.append(table)
    return tables

def extend(tables, states, word):
    for b in word:
        states = {r for q in states for r in tables[0][q]}
        states = {r for q in states for r in tables[1][q]}
        states = {q for q in states if (q & 1) == int(b)}
    return states

def run(k, tables, word):
    initial = {q for q in range(1 << k) if (q & 1) == int(word[0])}
    return extend(tables, initial, word[1:])

previous = None
for k in range(1, 11):
    t = transitions(k)
    sets = [run(k, t, w) for w in (X, Y, X+Z, Y+Z)]
    assert sets[0] and sets[1] and sets[2]
    assert extend(t, sets[0], Z) == sets[2]
    assert extend(t, sets[1], Z) == sets[3]
    if previous is not None:
        mask = (1 << (k-1)) - 1
        assert all({q & mask for q in s} <= p for s, p in zip(sets, previous))
    print(k, *(len(s) for s in sets))
    previous = sets
    if not sets[3]:
        assert k == 9
        print('First separating width9; literal/split/projection controls PASS')
        break
else:
    raise AssertionError('registered prediction failed')

# GC994: a strip reset can conceal an actual future distinction.
marker = '01'
mx = run(9, t, X + marker)
my = run(9, t, Y + marker)
assert mx == my and len(mx) == 19
assert mx == extend(t, run(9, t, X), marker)
assert my == extend(t, run(9, t, Y), marker)
assert run(9, t, X + marker + Z) == run(9, t, Y + marker + Z)
assert run(9, t, Y + marker + Z)
forbidden = '1000100001010001'
assert forbidden in Y + marker + Z
assert forbidden not in X + marker + Z
print('GC994 marker01: equal19-state sets, but actual future0001 separates by K18')
