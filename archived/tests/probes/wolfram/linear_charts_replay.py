#!/usr/bin/env python3
"""linear_charts_replay.py (Local, 11 November 2026; S-24, Cloud's K-10): the plain-Python replay of the worked-numbers
cell of the linear-charts essay. Usage: python3 linear_charts_replay.py

A shift-commuting law on one-sided bit sequences whose correction term has window w has the form
(x + y)_n = x_n xor y_n xor Q(x_(n+1..n+w), y_(n+1..n+w)). Enumerate the candidate Q of windows 1 and 2 with
Q(u, 0) = 0 and Q symmetric, and keep those whose law satisfies (x + y) + y = x on every pair of 6-cycles
(indices mod 6). Controls: drop symmetry (window 1), and drop Q(u, 0) = 0 (window 1).

Prediction (written before the first run, from the group-law lemma): exactly one survivor, Q = 0, at both windows
(2 and 64 candidates); without symmetry more than one survives (Q = w_0 gives a non-commutative law); without the
neutral element more than one survives (Q = 1 gives x xor y xor 1). Counterfactual: a second survivor at window 1 or 2
under both hypotheses refutes the lemma on cycles, or the cycle reduction; a single survivor in a control would show
that the hypothesis is not needed there. It prints {{candidates, survivors} at window 1, at window 2,
without symmetry, without the neutral element}."""
from itertools import product

M = 6


def law(Q, w):
    def op(x, y):
        return tuple(x[n] ^ y[n] ^ Q[(tuple(x[(n + 1 + i) % M] for i in range(w)), tuple(y[(n + 1 + i) % M] for i in range(w)))]
                     for n in range(M))
    return op


def survives(Q, w):
    op = law(Q, w)
    pts = list(product((0, 1), repeat=M))
    return all(op(op(x, y), y) == x for x in pts for y in pts)


def candidates(w, symmetric=True, neutral=True):
    words = list(product((0, 1), repeat=w))
    zero = tuple([0] * w)
    free = []
    for u in words:
        for v in words:
            if neutral and (v == zero or (symmetric and u == zero)):
                continue
            if symmetric and (v, u) in free:
                continue
            free.append((u, v))
    out = []
    for bits in product((0, 1), repeat=len(free)):
        Q = {}
        for (u, v), b in zip(free, bits):
            Q[(u, v)] = b
            if symmetric:
                Q[(v, u)] = b
        for u in words:
            for v in words:
                Q.setdefault((u, v), 0)
        out.append(Q)
    return out


def count(w, **kw):
    cs = candidates(w, **kw)
    return len(cs), sum(survives(Q, w) for Q in cs)


res = [count(1), count(2), count(1, symmetric=False), count(1, neutral=False)]
print('{' + ', '.join('{%d, %d}' % r for r in res) + '}')
