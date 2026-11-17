#!/usr/bin/env python3
"""L1383 (Local, 2026-11-03): independent exact check (Python Fractions) of GC2471's post-B boundaries.
Run: python3 tests/probes/mahler/post_b_boundary_check.py

r = 2/3; U_j(b) = (1/3) sum_k b_(j+k) r^k over a finite binary word (zeros after); max tail = max over j of U_j.
Checks: B, T_4, T_5, S_5 exactly as stated; 2/5 < B < T_4 < 81/200 < 1/2; for f = 5..10: T_f < S_f < T_(f-1),
T_f - T_(f+1) = q_f / 9, S_f - S_(f+1) = B q_f / (3 (1 - q_f)(1 - r q_f)); the finite five-one word with gaps 4,11,6,f has
max tail exactly T_f; the repeated-block family's max tails v_m increase to S_f (v_m < S_f, v_m -> S_f); the midpoint
a = (T_5 + S_5)/2 admits one block + final one and rejects two blocks; the one-extra-step relation D in {d, d + 1} on a
grid of a values in (B, T_4].
"""
from fractions import Fraction as F

r = F(2, 3)
third = F(1, 3)


def maxtail(ones):
    """Max over positions j of U_j for the word with ones at the given positions (zeros elsewhere)."""
    ones = sorted(ones)
    return max(third * sum(r ** (k - j) for k in ones if k >= j) for j in ones)


B = (1 + r ** 4 + r ** 15 + r ** 21) / 3
T = lambda f: B + r ** (21 + f) / 3
S = lambda f: B / (1 - r ** (21 + f))
print('B = %s (stated 12552580835/31381059609: %s)' % (B, B == F(12552580835, 31381059609)))
print('T_4 = %s (%s); T_5 = %s (%s); S_5 = %s (%s)' % (
    T(4), T(4) == F(1016792602067, 2541865828329), T(5), T(5) == F(3050344251769, 7625597484987),
    S(5), S(5) == F(203351809527, 508359743893)))
print('2/5 < B < T_4 < 81/200 < 1/2: %s' % (F(2, 5) < B < T(4) < F(81, 200) < F(1, 2)))
print('r^6 < 1/10, r^11 < 1/10, r^5 * 81/200 = 4/75: %s %s %s' % (r ** 6 < F(1, 10), r ** 11 < F(1, 10), r ** 5 * F(81, 200) == F(4, 75)))
okall = True
for f in range(5, 11):
    q = r ** (21 + f)
    o1 = T(f) < S(f) < T(f - 1)
    o2 = T(f) - T(f + 1) == q / 9
    o3 = S(f) - S(f + 1) == B * q / (3 * (1 - q) * (1 - r * q))
    o4 = maxtail([0, 4, 15, 21, 21 + f]) == T(f)
    v, ones, mts = [], [0], []
    for m in range(1, 5):                                   # m blocks (gaps 4, 11, 6, f) then a final one
        ones = [0] + [p + 21 + f for p in ones] if m > 1 else [0, 4, 15, 21, 21 + f]
        if m > 1:
            ones = sorted(set([0, 4, 15, 21] + [p + 21 + f for p in prev]))
        prev = ones
        mts.append(maxtail(ones))
    o5 = all(mts[i] < mts[i + 1] < S(f) for i in range(len(mts) - 1))
    okall &= o1 and o2 and o3 and o4 and o5
    print('f=%d: T_f < S_f < T_(f-1) %s; T-width %s; S-width %s; five-one max tail = T_f %s; v_1..v_4 increasing below S_f %s (S_f - v_4 = %.3e)' % (
        f, o1, o2, o3, o4, o5, float(S(f) - mts[-1])))
a = (T(5) + S(5)) / 2
one = maxtail([0, 4, 15, 21, 26])
two = maxtail([0, 4, 15, 21, 26, 30, 41, 47, 52])
print('midpoint a = %.20f: one block + final one max tail %.20f (< a: %s); two blocks %.20f (< a: %s)' % (
    float(a), float(one), one < a, float(two), two < a))
bad = 0
for k in range(1, 400):
    a = B + (T(4) - B) * F(k, 400)
    d = next(f for f in range(4, 400) if r ** (21 + f) / 3 < a - B)
    D = next(f for f in range(4, 400) if a * r ** (21 + f) <= a - B)
    bad += D not in (d, d + 1)
print('one extra step: D in {d, d + 1} on 399 grid points in (B, T_4]: violations %d' % bad)
print('all f checks pass: %s' % okall)
print('POST_B_DONE')
