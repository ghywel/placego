#!/usr/bin/env python3
"""first_check_degree_replay.py (Local, 10 November 2026; S-06): the plain-Python replay of the worked-numbers cell of
the first-check-degree essay. Usage: python3 first_check_degree_replay.py

Prediction (written before the first run): for n = 1..12 the check c_(2n+1)(0) of the kit phase (column -1 black at
even times, free bits f_s at time 2s + 1) is black on a number of words congruent to n mod 2, and for n = 2..12 the
words with f_1 = 0 give n + 1 mod 2 (`ones_parity`, `omit_coefficient`); the ANF degree of the check is n for odd n and
n - 1 for even n, for n = 1..10 (`check_degree`); the rows of width at most 2n black at column -1 at every even tick
through 2n number 1, 2, 3, 4, 17, 38 for n = 1..6, by direct simulation (`first_check_parity` gives their parities);
the Walsh sum 2^n - 2 ones(n) is 0, 0, 2, 0, 2, ... mod 4 (`walsh_mod_four`, `walsh_one`); and in the other phase
(free bits at even times, column -1 black at odd times) the check at depth 2n is black on an odd number of words for
n = 1..12 (`other_phase_odd`). Counterfactual: any mismatch means a recurrence or a convention is misread.

Depth k = 0 is the white wall; recon(a, k, t) is the cell at depth k and time t. It prints
{kit parities hold, omitted coefficients hold, degrees n = 1..10, survivors n = 1..6, Walsh mod 4 n = 1..12,
other phase odd}."""
import itertools
from functools import lru_cache


def recon_of(a):
    @lru_cache(None)
    def rc(k, t):
        if k == 0:
            return 0
        if k == 1:
            return a(t)
        return rc(k - 1, t + 1) ^ (rc(k - 1, t) | rc(k - 2, t))
    return rc


def check(n, w):
    return recon_of(lambda t: 1 if t % 2 == 0 else (w[t // 2] if t // 2 < len(w) else 0))(2 * n + 1, 0)


def other(n, w):
    return recon_of(lambda t: (w[t // 2] if t // 2 < len(w) else 0) if t % 2 == 0 else 1)(2 * n, 0)


def cube(n):
    return list(itertools.product((0, 1), repeat=n))


def degree(n, F):
    """ANF degree by the Moebius transform of the truth table, word index = sum w_i 2^i."""
    tt = [0] * (1 << n)
    for w in cube(n):
        tt[sum(b << i for i, b in enumerate(w))] = F(n, w)
    for i in range(n):
        for x in range(1 << n):
            if x >> i & 1:
                tt[x] ^= tt[x ^ (1 << i)]
    return max((bin(x).count('1') for x in range(1 << n) if tt[x]), default=-1)


def step(row):
    """One zero-boundary step on depths 1..len(row); the row grows by one cell."""
    r = [0] + list(row) + [0, 0]
    return [r[i + 1] ^ (r[i] | r[i - 1]) for i in range(1, len(row) + 2)]


def survivors(n):
    c = 0
    for row in cube(2 * n):
        cur, ok = list(row), True
        for t in range(2 * n + 1):
            if t % 2 == 0 and not cur[0]:
                ok = False
                break
            cur = step(cur)
        c += ok
    return c


ones = {n: sum(check(n, w) for w in cube(n)) for n in range(1, 13)}
kit = all(ones[n] % 2 == n % 2 for n in ones)
omit = all(sum(check(n, w) for w in cube(n) if w[1] == 0) % 2 == (n + 1) % 2 for n in range(2, 13))
degs = [degree(n, check) for n in range(1, 11)]
surv = [survivors(n) for n in range(1, 7)]
walsh = [(2 ** n - 2 * ones[n]) % 4 for n in range(1, 13)]
odd = all(sum(other(n, w) for w in cube(n)) % 2 == 1 for n in range(1, 13))
print('{%s, %s, {%s}, {%s}, {%s}, %s}' % (kit, omit, ','.join(map(str, degs)), ','.join(map(str, surv)),
                                          ','.join(map(str, walsh)), odd))
