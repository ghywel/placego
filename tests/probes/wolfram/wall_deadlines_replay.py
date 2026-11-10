#!/usr/bin/env python3
"""wall_deadlines_replay.py (Local, 10 November 2026; S-18): the plain-Python replay of the worked-numbers cell of the
wall-deadlines essay. Usage: python3 wall_deadlines_replay.py

Prediction (written before the first run): beside a white wall, with depth 1 required black at every even tick, the
latest first white even tick over the starts of width at most W is kstar W - 1 for rule 90 (kstar W the least odd number
above W not divisible by 3) and 2 ceil(W/2) for rule 150, for W = 1..12, giving 4,4,4,4,6,6,10,10,10,10,12,12 and
2,2,4,4,6,6,8,8,10,10,12,12; and the starts attaining it are exactly those whose odd depths follow Fibonacci mod 2
(rule 90) or are all black (rule 150), 2^floor(W/2) of them. Counterfactual: a mismatch refutes the closed form or its
sharpness. It prints {rule 90 matches, rule 150 matches, the rule 90 deadlines, the rule 150 deadlines,
the extremal rows are exactly the pattern rows}."""


def first_white(y, W, h, T=60):
    r = [0] + [(y >> (d - 1)) & 1 for d in range(1, W + 1)] + [0] * (T + 3)
    for t in range(T + 1):
        if t % 2 == 0 and not r[1]:
            return t
        r = [0] + [r[k + 1] ^ h(r[k], r[k - 1]) for k in range(1, len(r) - 1)] + [0]
    return None


def kstar(W):
    k = W + 1
    while k % 2 == 0 or k % 3 == 0:
        k += 1
    return k


h90 = lambda b, c: c
h150 = lambda b, c: b ^ c
fib = lambda k: 0 if k % 3 == 0 else 1
D90, D150, ok90, ok150, pattern = [], [], True, True, True
for W in range(1, 13):
    f90 = [first_white(y, W, h90) for y in range(1 << W)]
    f150 = [first_white(y, W, h150) for y in range(1 << W)]
    D90.append(max(f90))
    D150.append(max(f150))
    ok90 &= max(f90) == kstar(W) - 1
    ok150 &= max(f150) == 2 * ((W + 1) // 2)
    p90 = {y for y in range(1 << W) if all(((y >> (k - 1)) & 1) == fib(k) for k in range(1, W + 1, 2))}
    p150 = {y for y in range(1 << W) if all((y >> (k - 1)) & 1 for k in range(1, W + 1, 2))}
    pattern &= ({y for y, f in enumerate(f90) if f == max(f90)} == p90 and len(p90) == 2 ** (W // 2)
                and {y for y, f in enumerate(f150) if f == max(f150)} == p150 and len(p150) == 2 ** (W // 2))
print('{%s, %s, {%s}, {%s}, %s}' % (ok90, ok150, ', '.join(map(str, D90)), ', '.join(map(str, D150)), pattern))
