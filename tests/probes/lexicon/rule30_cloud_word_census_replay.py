#!/usr/bin/env python3
"""rule30_cloud_word_census_replay.py: WR2, an independent replay of Local's WC census (L499) of the one-sided route.

RUN-ON:     cpu, one core (Python 3 standard library); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_word_census_replay.py

Why. L498's route, second-read in CL110 and filed as PROOFS.md entry 40 for the white end, excludes a periodic column
word w from finite seeds when a width-k relaxation determines column +1 at every tick from the macro's stable set.
Column +1 is then eventually periodic with w's period, and Theorem A (entry 5) applies. Local's WC
(rule30_word_jen_census.py) ran it on every primitive word: 14 of the 2,515 of period 7 .. 14 at width 8, listed by
name; 24 at width 10 (per period 0, 0, 0, 2, 3, 3, 7, 9); and 15, 20, 31, 49 of periods 15 .. 18 at width 8. With
the transfer accepted, these exclusions rest only on the per-word computations. This is an independent
implementation, with no shared code: Lyndon words by Duval's algorithm, successor tables, set-valued macro images,
and the per-tick reading of x1 from the stable set.

Record searched: "WC" with "census" and "jen" -> L499 and rule30_word_jen_census.py (the claims above); entry 40;
CL110's WR (the white end only). No replay of WC.

PREDICTIONS, written 2026-10-09 22:39 BST, before any run of this script.
  WR2-C1 (control, must hold): the white-end words 0^q 1 for q = 10 .. 13 are determined at width 8 (WR), and no
         word of period 7 .. 9 is determined at width 8.
  WR2-P1 (0.85): at width 8, exactly 14 Lyndon words of period 7 .. 14 are determined, and they are L499's list.
  WR2-P2 (0.8): at width 10, exactly 24, with 0, 0, 0, 2, 3, 3, 7, 9 for p = 7 .. 14.
  WR2-P3 (0.8): at width 8, periods 15 .. 18 give 15, 20, 31 and 49.
  WR2-U, the unexpected check (0.5): every determined word at width 8 has a stable set of at most 16 states.
  Counterfactual. Any disagreement leaves the affected words unfiled until it is traced.
"""
import sys

L499 = {'0011111111', '00000000001', '00000000011', '000000000001', '000000000011', '0000000000001',
        '0000000000011', '0000000001011', '00000000000001', '00000000000011', '00000000001011', '00000000010011',
        '00000000010111', '00000000011011'}


def lyndon(n):
    """Binary Lyndon words of length exactly n (Duval's generation)."""
    out, w = [], [-1]
    while w:
        w[-1] += 1
        m = len(w)
        if m == n:
            out.append(''.join(map(str, w)))
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == 1:
            w.pop()
    return out


def tables(k):
    succ = {}
    for b in (0, 1):
        t = []
        for s in range(1 << k):
            x = [(s >> j) & 1 for j in range(k)]
            outs = []
            for inp in (0, 1):
                y = 0
                for j in range(k):
                    left = b if j == 0 else x[j - 1]
                    right = inp if j == k - 1 else x[j + 1]
                    y |= (left ^ (x[j] | right)) << j
                outs.append(y)
            t.append(outs)
        succ[b] = t
    return succ


def determined(word, succ, k):
    walls = [int(c) for c in word]
    S = frozenset(range(1 << k))
    while True:
        T = S
        for b in walls:
            T = frozenset(y for s in T for y in succ[b][s])
        if T == S:
            break
        S = T
    cur = S
    for b in walls:
        if len({s & 1 for s in cur}) != 1:
            return False, len(S)
        cur = frozenset(y for s in cur for y in succ[b][s])
    return True, len(S)


def census(periods, k):
    succ = tables(k)
    res = {}
    for p in periods:
        res[p] = [(w, sz) for w in lyndon(p) for det, sz in [determined(w, succ, k)] if det]
        print('width %d, p = %d: %d of %d determined' % (k, p, len(res[p]), len(lyndon(p))), flush=True)
    return res


def main():
    assert [len(lyndon(n)) for n in range(7, 15)] == [18, 30, 56, 99, 186, 335, 630, 1161]
    w8 = census(range(7, 15), 8)
    succ8 = tables(8)
    c1 = all(determined('0' * q + '1', succ8, 8)[0] for q in range(10, 14)) and not any(w8[p] for p in (7, 8, 9))
    print('WR2-C1: %s' % ('PASS' if c1 else 'FAIL'))
    got = {w for p in w8 for w, _ in w8[p]}
    p1 = got == L499
    print('WR2-P1 (width 8: exactly L499\'s 14 words): %s%s' % ('HELD' if p1 else 'REFUTED', '' if p1 else
                                                              ' extra %s missing %s' % (sorted(got - L499),
                                                                                         sorted(L499 - got))))
    w10 = census(range(7, 15), 10)
    per10 = [len(w10[p]) for p in range(7, 15)]
    print('WR2-P2 (width 10: 24 words, per period 0 0 0 2 3 3 7 9): %s %s' % (
        per10, 'HELD' if per10 == [0, 0, 0, 2, 3, 3, 7, 9] else 'REFUTED'))
    w8b = census(range(15, 19), 8)
    per8b = [len(w8b[p]) for p in range(15, 19)]
    print('WR2-P3 (width 8, p = 15 .. 18: 15, 20, 31, 49): %s %s' % (
        per8b, 'HELD' if per8b == [15, 20, 31, 49] else 'REFUTED'))
    sizes = [sz for d in (w8, w8b) for p in d for _, sz in d[p]]
    print('WR2-U (stable sets of determined words at width 8 have <= 16 states): max %d, %s' % (
        max(sizes), 'HELD' if max(sizes) <= 16 else 'REFUTED'))
    print('width 10 words: %s' % sorted(w for p in w10 for w, _ in w10[p]))


if __name__ == '__main__':
    main()
