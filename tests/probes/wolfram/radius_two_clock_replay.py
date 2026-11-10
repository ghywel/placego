#!/usr/bin/env python3
"""radius_two_clock_replay.py (Local, 10 November 2026; S-07): the plain-Python replay of the worked-numbers cell of the
radius-two clock essay. Usage: python3 radius_two_clock_replay.py

Prediction (written before the first run): for each of the four rules N(p, q), from the black cells 0 and 2, the
columns -2 and -1 equal t mod 2 for t < 200; the rule reads exactly 14 distinct four-cell windows (the arguments of g)
on that orbit, never one of the two exceptional windows; from the black cells 2 and 4, column 0 alternates; and the
black cells at time t lie in [-2t, 2t + 2]. Counterfactual: any failure means the row formula or the clock is misread.

new x(i) = x(i - 2) xor g(x(i - 1), x(i), x(i + 1), x(i + 2)), g = not all of the last three equal, except
g(1,1,0,1) = p and g(1,0,1,1) = q. It prints {clocks, windows read, exceptional windows read, column 0 clock, support}."""


def g(p, q, a, b, c, d):
    if (a, b, c, d) == (1, 1, 0, 1):
        return p
    if (a, b, c, d) == (1, 0, 1, 1):
        return q
    return 0 if b == c == d else 1


def run(p, q, black, T=200):
    row = set(black)
    cols, windows, support = [], set(), True
    for t in range(T):
        x = lambda i: 1 if i in row else 0
        cols.append((x(-2), x(-1), x(0)))
        support = support and all(-2 * t <= i <= 2 * t + 2 for i in row)
        lo, hi = min(row) - 2, max(row) + 2
        new = set()
        for i in range(lo, hi + 1):
            w = (x(i - 1), x(i), x(i + 1), x(i + 2))
            windows.add(w)
            if x(i - 2) ^ g(p, q, *w):
                new.add(i)
        row = new
    return cols, windows, support


clocks, wins, exc, sup = True, set(), 0, True
for p in (0, 1):
    for q in (0, 1):
        cols, w, s = run(p, q, {0, 2})
        clocks = clocks and all(c[0] == t % 2 and c[1] == t % 2 for t, c in enumerate(cols))
        wins |= w
        exc += sum(1 for v in w if v in ((1, 1, 0, 1), (1, 0, 1, 1)))
        sup = sup and s
col0 = all(all(c[2] == t % 2 for t, c in enumerate(run(p, q, {2, 4})[0])) for p in (0, 1) for q in (0, 1))
out = [clocks, len(wins), exc, col0, sup]
print('{' + ', '.join(('True' if v else 'False') if isinstance(v, bool) else str(v) for v in out) + '}')
assert out == [True, 14, 0, True, True], out
