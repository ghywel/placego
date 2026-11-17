#!/usr/bin/env python3
"""zero_wall_diagonals_replay.py (Local, 10 November 2026; S-12): the plain-Python replay of the worked-numbers cell of
the zero-wall-diagonals essay. Usage: python3 zero_wall_diagonals_replay.py

Prediction (written before the first run): for the zero-boundary left half of rule 30 from the single black cell at
depth 1 (m = 1), with E(j, t) = zrow(t, m + t - j) for t <= 600 and j <= 12, the left-diagonal recurrence
E(j+2, t+1) = E(j, t) xor (E(j+1, t) or E(j+2, t)) holds at every point with j + 2 <= m + t, and fails at some point
with j + 2 = m + t + 1 (the guard is needed); over the window t in [400, 600) each E_j, j <= 10, is periodic with a
period dividing 2^j; and the Fibonacci word has p(n) = n + 1 factors and exactly one right-special factor of every
length n <= 12 (the boundary case the complexity theorem excludes for free words). Counterfactual: a failure inside
the guard means the entry lemma is misread. It prints
{guard holds inside, guard fails somewhere outside, periods divide 2^j, minimal late periods, Fibonacci counts}."""


def zrows(L, T, width):
    """zrow L t k for t <= T, k <= width; depth 0 is the white wall."""
    rows = [[0] * (width + 2) for _ in range(T + 1)]
    for k in range(1, width + 1):
        rows[0][k] = L(k)
    for t in range(T):
        r, n = rows[t], rows[t + 1]
        for k in range(1, width + 1):
            n[k] = r[k + 1] ^ (r[k] | r[k - 1])
    return rows


m, T, J = 1, 600, 12
rows = zrows(lambda k: 1 if k == m else 0, T + 1, m + T + 4)
E = lambda j, t: rows[t][m + t - j] if m + t - j >= 0 else 0
inside = all(E(j + 2, t + 1) == E(j, t) ^ (E(j + 1, t) | E(j + 2, t))
             for t in range(T) for j in range(J + 1) if j + 2 <= m + t)
outside = any(E(j + 2, t + 1) != E(j, t) ^ (E(j + 1, t) | E(j + 2, t))
              for t in range(T) for j in range(J + 1) if j + 2 == m + t + 1)


def late_period(j):
    seq = [E(j, t) for t in range(400, 600)]
    return next(p for p in range(1, 201) if all(seq[i] == seq[i + p] for i in range(len(seq) - p)))


periods = [late_period(j) for j in range(11)]
divides = all((2 ** j) % p == 0 for j, p in enumerate(periods))
fib = [0]
a, b = [0], [0, 1]
while len(b) < 20000:
    a, b = b, b + a
w = b[:20000]
counts = []
for n in range(1, 13):
    facs = {tuple(w[i:i + n]) for i in range(len(w) - n)}
    rs = sum(1 for u in facs if u + (0,) in {tuple(w[i:i + n + 1]) for i in range(len(w) - n - 1)}
             and u + (1,) in {tuple(w[i:i + n + 1]) for i in range(len(w) - n - 1)})
    counts.append((len(facs), rs))
fibok = all(c == (n + 1, 1) for n, c in zip(range(1, 13), counts))
print('{%s, %s, %s, {%s}, %s}' % (inside, outside, divides, ', '.join(map(str, periods)), fibok))
