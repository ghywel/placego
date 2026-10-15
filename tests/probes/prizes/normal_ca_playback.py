#!/usr/bin/env python3
"""GC1270/G300: exact controls for an eight-state periodic playback CA.

Predictions registered in CHAT-LEDGER GC1270 before this program was run.
Record searched: shift.register|playback|reflect.*lane|opposite.*lane (16 hits).
C1: total 512-entry radius-one rule; stable Q/R and two-state port.
C2: all 680 loadings, m=1..4, match independent word rotation for 11376
updates. C3: one-hot least period 2m+1; constants period 1.
Counterfactual period 2m must fail. Unexpected check: m=1 interfaces coincide.
C4: one-bit insertion into de Bruijn cycles k=1..6 obeys discrepancy
at most (h+1)/(2**k+1), for all h<=k, by exact integer counts.
REFUTED-BY: any failed assertion. No inference from these finite controls
to an unbounded normal column, or to an elementary rule. No output data files.
OUTCOME GC1271: all controls pass: 512 triples, 680 loadings, 11376 updates,
240 de Bruijn word checks. Counterfactual 2m refuted; unexpected m=1 passes.
"""

from collections import Counter
from itertools import product
import json

Q, P0, P1, R = range(4)


def data(a, b):
    return 4 + 2 * a + b


def rule(left, center, right):
    if center in (Q, R):
        return center
    if center in (P0, P1):
        return P0 + ((right - 4) % 2 if right >= 4 else 0)
    a = (center - 4) // 2
    forward = left - P0 if left in (P0, P1) else (
        (left - 4) // 2 if left >= 4 else 0)
    backward = a if right == R else ((right - 4) % 2 if right >= 4 else 0)
    return data(forward, backward)


TABLE = {triple: rule(*triple) for triple in product(range(8), repeat=3)}


def load(word):
    """Independent format: W=z,b1,...,bm,am,...,a1; two Q pads."""
    m = (len(word) - 1) // 2
    return [Q, Q, P0 + word[0]] + [
        data(word[-j], word[j]) for j in range(1, m + 1)
    ] + [R, Q, Q]


def step(row):
    # Q at the finite simulation boundary has Q on its infinite outer side.
    padded = [Q] + row + [Q]
    return [TABLE[tuple(padded[j:j + 3])] for j in range(len(row))]


def de_bruijn(k):
    """Binary FKM construction; exact cyclic counts independently certify it."""
    a, out = [0] * (2 * k + 1), []

    def visit(t, p):
        if t > k:
            if k % p == 0:
                out.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            visit(t + 1, p)
            for bit in range(a[t - p] + 1, 2):
                a[t] = bit
                visit(t + 1, t)

    visit(1, 1)
    return tuple(out)


def counts(word, h):
    return Counter(tuple(word[(j + d) % len(word)] for d in range(h))
                   for j in range(len(word)))


def main():
    assert len(TABLE) == 512 and all(0 <= x < 8 for x in TABLE.values())
    for (l, c, r), v in TABLE.items():
        if c in (Q, R):
            assert v == c
        if c in (P0, P1):
            assert v in (P0, P1)
    loadings = updates = 0
    for m in range(1, 5):
        p = 2 * m + 1
        for bits in product((0, 1), repeat=p):
            row = load(bits)
            for t in range(2 * p):
                rotated = bits[t % p:] + bits[:t % p]
                assert row == load(rotated), (m, bits, t, row)
                row = step(row)
                updates += 1
            loadings += 1
        onehot = (1,) + (0,) * (p - 1)
        row, observed = load(onehot), []
        for _ in range(2 * p):
            observed.append(row[2] - P0)
            row = step(row)
        least = next(d for d in range(1, p + 1)
                     if all(observed[t] == observed[t + d]
                            for t in range(2 * p - d)))
        assert least == p
        assert observed[0] != observed[2 * m]  # wrong period excludes port
        for bit in (0, 1):
            row = load((bit,) * p)
            assert step(row) == row
    word_checks = 0
    for k in range(1, 7):
        d = de_bruijn(k)
        q = 2 ** k
        assert len(d) == q
        w = (0,) + d
        row = load(w)
        for t in range(2 * len(w)):
            assert row[2] - P0 == w[t % len(w)]
            row = step(row)
        for h in range(1, k + 1):
            dc, wc = counts(d, h), counts(w, h)
            for word in product((0, 1), repeat=h):
                assert dc[word] == q // (2 ** h)
                assert abs(wc[word] - dc[word]) <= h
                assert abs(wc[word] * 2 ** h - (q + 1)) <= (h + 1) * 2 ** h
                word_checks += 1
    assert (loadings, updates) == (680, 11376)
    print(json.dumps(dict(rule_triples=512, loadings=loadings,
                          global_updates=updates, de_bruijn_word_checks=word_checks,
                          counterfactual_period_2m="REFUTED for m=1..4",
                          unexpected_m1="PASS", verdict="ALL CONTROLS PASS")))


if __name__ == "__main__":
    main()
