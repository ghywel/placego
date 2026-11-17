#!/usr/bin/env python3
"""period_two_onset_replay.py (Local, 10 November 2026; S-21, Cloud's K-02): the plain-Python replay of the
worked-numbers cell of the period-two onset essay. Usage: python3 period_two_onset_replay.py

Columns 1..b of rule 30 beside a column 0 that is white at even and black at odd ticks; column b + 1 is free at every
tick. One double step from a white tick maps a window x to dstep(r1, r2, x). Scalar rule 30, written independently of
the Lean module (no shared code).

Prediction (written before the first run, from GPT's GC2843 and the L1646 prototype): the first images have 20 and 38
windows at b = 5, 6 and are closed; every word of the kit's lists col1Forbidden is excluded from them, and so is
101010000 at width 6; the minimal excluded words of length at most 13 are the kit's four at width 5, and at width 6
the kit's nine with 1010100001 replaced by 101010000; read from all windows, without the first double step, only 11
and 00000 (and 101001 at width 6) are excluded. Counterfactual: any mismatch refutes the finite certificate or the
essay's description of it. It prints {|img5|, |img6|, img5 closed, img6 closed, kit words excluded, 101010000 excluded,
minimal words at 5, minimal words at 6, kit words excluded without the first double step at 5, the same at 6}."""
from itertools import product

KIT5 = ['11', '00000', '100101', '10010001']
KIT6 = KIT5 + ['101001', '1010100001', '1010001001', '10010000101', '1001000010001']
MAXLEN = 13


def tick(left, right, x):
    """One tick of rule 30 on the window x, with the cells left and right beside it."""
    cells = (left,) + x + (right,)
    return tuple(cells[i - 1] ^ (cells[i] | cells[i + 1]) for i in range(1, len(x) + 1))


def succs(x):
    return {tick(1, r2, tick(0, r1, x)) for r1 in (0, 1) for r2 in (0, 1)}


def reads(S, w):
    """The windows reached while column 1 reads w, starting from windows of S."""
    L = {x for x in S if x[0] == int(w[0])}
    for c in w[1:]:
        L = {y for x in L for y in succs(x) if y[0] == int(c)}
    return L


def minimal_words(S):
    out = []

    def go(w, L):
        if len(w) == MAXLEN:
            return
        for c in '01':
            L2 = {y for x in L for y in succs(x) if y[0] == int(c)}
            if not L2:
                if reads(S, (w + c)[1:]):
                    out.append(w + c)
            else:
                go(w + c, L2)
    for c in '01':
        L0 = {x for x in S if x[0] == int(c)}
        if L0:
            go(c, L0)
        else:
            out.append(c)
    return sorted(out, key=lambda s: (len(s), s))


res = {}
for b in (5, 6):
    every = set(product((0, 1), repeat=b))
    img = set().union(*(succs(x) for x in every))
    closed = all(succs(x) <= img for x in img)
    kit = KIT5 if b == 5 else KIT6
    res[b] = (len(img), closed, all(not reads(img, w) for w in kit), minimal_words(img),
              [w for w in kit if not reads(every, w)], img)
short = not reads(res[6][5], '101010000')
q = lambda ws: '{' + ', '.join('"%s"' % w for w in ws) + '}'
print('{%d, %d, %s, %s, %s, %s, %s, %s, %s, %s}' % (res[5][0], res[6][0], res[5][1], res[6][1], res[5][2] and res[6][2],
                                                  short, q(res[5][3]), q(res[6][3]), q(res[5][4]), q(res[6][4])))
