#!/usr/bin/env python3
"""One bounded forced-left audit of all sixteen four-gap S/L boundary words.
RUN-ON: cpu; tiny independent audit, not Local's physical return-language scan.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_mixed_left_cost.py
PREDICTIONS (before first execution, 2026-10-09):
 ML-C1: independent decimal Rule 30 evolution verifies every inverse clock prefix.
 ML-C2: pure S and pure L obey GC706's necessary J >= T - 2P.
 ML-P1 (blind): each four-gap word requires a black left bit at depth >= floor(T/2).
 Counterfactual: complementing every supplied right boundary bit leaves the decoded
 left prefix unchanged; ML-C3 must detect a difference for SSSS.
 Unexpected check: omit the terminal renewal sample; a final L can exit its marker.
 COST: 16 words, at most 40 observations; no sweep, fresh singleton data or full
 right realization. Failure of ML-P1 is retained. No asymptotic conclusion.
"""
from itertools import product
import json

LIFT = {'S': '110100', 'L': '1101000100'}

def decode(sigma):
    wall = [t % 2 for t in range(len(sigma))]
    a, b = wall, [int(v) for v in sigma]
    left = []
    while len(a) > 1:
        c = [a[t + 1] ^ (a[t] | b[t]) for t in range(len(a) - 1)]
        left.append(c[0])
        b, a = a, c
    return left

def literal_check(sigma, left):
    T = len(sigma)
    # Extra zero padding prevents the finite outer boundary reaching the wall.
    row = [0] * (2 * T + 3)
    c = len(row) - 1
    for d, bit in enumerate(left, 1):
        row[c - d] = bit
    for t in range(T - 1):
        row[c] = t % 2
        actual = (30 >> (4 * row[c - 1] + 2 * row[c] + int(sigma[t]))) & 1
        assert actual == (t + 1) % 2, (t, actual)
        nxt = [0] * len(row)
        for i in range(1, c):
            v = 4 * row[i - 1] + 2 * row[i] + row[i + 1]
            nxt[i] = (30 >> v) & 1
        row = nxt


def main():
    results = []
    for bits in product('SL', repeat=4):
        word = ''.join(bits)
        sigma = ''.join(LIFT[x] for x in word)
        left = decode(sigma)
        literal_check(sigma, left)
        J = max((d for d, bit in enumerate(left, 1) if bit), default=-1)
        T = len(sigma)
        if word in ('SSSS', 'LLLL'):
            P = len(LIFT[word[0]])
            assert J >= T - 2 * P, (word, J, T, P)
        results.append({'word': word, 'T': T, 'J': J, 'P1': J >= T // 2,
                        'left': ''.join(map(str, left))})
    s = LIFT['S'] * 4
    assert decode(s) != decode(''.join(str(1 - int(v)) for v in s))
    print(json.dumps({'ML-C1': 'PASS', 'ML-C2': 'PASS', 'ML-C3': 'PASS',
                      'ML-P1': 'HELD' if all(r['P1'] for r in results) else 'REFUTED',
                      'rows': results}, indent=2))

if __name__ == '__main__':
    main()
