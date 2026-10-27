#!/usr/bin/env python3
"""L1037: exhaustive self-checks of the lemmas in the hand exclusion of 0z and 1z (z = 001000010001).

Local, 2026-10-27. Finite truth-table checks of the clamped two-step map only (wall x(t,0) = t mod 2; a row is cells
1, 2, ... at an even time). No solver, sampling or language census. Each assertion is one lemma of
reports/rule30-disappearing-words-hand.md, section L1037.
"""
import itertools


def step(x, wall):
    return [(wall if i == 0 else x[i - 1]) ^ (x[i] | x[i + 1]) for i in range(len(x) - 1)]


def two(x):
    return step(step(x, 0), 1)


def rows(n):
    return (list(t) for t in itertools.product((0, 1), repeat=n))


def s(t):
    return ''.join(map(str, t))


# Reset (GPT GC1992): next visible bit is 1 iff the row begins 000.
assert all((two(x)[0] == 1) == (x[:3] == [0, 0, 0]) for x in rows(5))
# Lemma B (pre-reset): two(X) begins 000 iff X begins 010, 01100, or 100 with (x4, x5) != 00.
pre = {s(x) for x in rows(5) if two(x)[:3] == [0, 0, 0]}
assert pre == {p for p in map(s, itertools.product((0, 1), repeat=5))
               if p[:3] == '010' or p == '01100' or (p[:3] == '100' and p[3:] != '00')}
# Lemma A: no row begins 0110 at an even time after time 0 (no two-step past).
assert all(s(two(x))[:4] != '0110' for x in rows(6))


def next_reset(tail, g):
    """Reset row 000+tail: is the next visible 1 exactly g zeros later? Returns (bool, row at that reset)."""
    x = [0, 0, 0] + list(tail)
    for k in range(1, g + 2):
        x = two(x)
        if x[:3] == [0, 0, 0]:
            return k == g + 1, x
    return False, x


# Lemma C (gap function, used for orientation only): the next gap is decided by the first four tail bits.
GAP = {1: {'0001', '0010', '0011'}, 2: {'1101', '1110', '1111'},
       3: {'0000', '0100', '0101', '0110', '0111'}, 4: {'1000', '1001', '1010', '1011', '1100'}}
for g, allowed in GAP.items():
    assert all(next_reset(t, g)[0] == (s(t[:4]) in allowed) for t in rows(2 * (g + 1) + 3))
# Lemma D (z's future): gap 4 and then gap 3 after a reset row 000+t forces t1..t6 = 100111 and (t7, t8) != 00.
for t in rows(14):
    ok, r2 = next_reset(t, 4)
    future = ok and s(r2[3:7]) in GAP[3]
    assert future == (s(t[:6]) == '100111' and t[6:8] != [0, 0])
# Lemma E: no X beginning 010 gives two(X) = 000 100111 ...
assert all(s(two([0, 1, 0] + x))[:9] != '000100111' for x in rows(8))
# Consequence: z occurs at no age >= 1, so 0z and 1z are absent (agrees with the certified phase-0 list).
assert all(not (s(two(two(x)))[:9] == '000100111' and two(x)[0] == 0) for x in rows(15))
print('all lemma checks pass')
