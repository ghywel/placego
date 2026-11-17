#!/usr/bin/env python3
"""Lock family, step 1 (Local, 8 November 2026): the period-14 column words of lock-7 (R = 74) and lock-7b (R = 3793493).
Prediction, before the run: (a) both rows have exactly period 14 on columns 1..L with L = 25 and 50 (BN-13), sharing the
words of columns 1..9 and differing at 10; (b) no spatial repeat (column p equal to column p + d up to a time shift)
with d < 30 inside lock-7b's locked zone (BN-13), P = 0.8; (c) lock-7b's columns 26..50 are not a time-shift of
lock-7's columns 1..25, P = 0.85. Counterfactual for (c): they are, and the two locks are the first two members of a
doubling family, which a construction should then extend.
Frame: driven right half, center black at even ticks, bit p - 1 = column p."""
def step(x, t): return ((x << 1) | (1 if t % 2 == 0 else 0)) ^ (x | (x >> 1))
def late(R, T):
    x = R
    for t in range(T): x = step(x, t)
    rows = [x]
    for t in range(T, T + 28): x = step(x, t); rows.append(x)
    return rows                                  # rows[i] = tick T + i, T a multiple of 14
def words(rows, maxc):
    out = []
    for c in range(1, maxc + 1):
        w = tuple((rows[i] >> (c - 1)) & 1 for i in range(28))
        out.append(w[:14] if w[:14] == w[14:] else None)
    return out
T = 14 * 600
A = words(late(74, T), 64); B = words(late(3793493, T), 64)
LA = next(i for i, w in enumerate(A) if w is None); LB = next(i for i, w in enumerate(B) if w is None)
print('locked columns: lock-7', LA, '; lock-7b', LB)
same = [i + 1 for i in range(min(LA, LB)) if A[i] == B[i]]
print('columns with equal words (same time base):', same)
fmt = lambda w: ''.join(map(str, w)) if w else '-' * 14
for c in range(1, max(LA, LB) + 2):
    print('%2d  %s  %s' % (c, fmt(A[c-1]) if c <= len(A) else '', fmt(B[c-1])))
rot = lambda w, k: w[k:] + w[:k]
def eq_upto_shift(u, v): return [k for k in range(14) if rot(u, k) == v]
rep = [(p, d, eq_upto_shift(B[p-1], B[p-1+d])) for p in range(1, LB + 1) for d in range(1, 30) if p + d <= LB and eq_upto_shift(B[p-1], B[p-1+d])]
print('lock-7b column pairs equal up to a time shift (p, d, shifts), d < 30:', len(rep), rep[:12])
blocks = [(off, k) for off in range(0, LB - LA + 1) for k in range(14) if all(B[off+i] == rot(A[i], k) for i in range(LA))]
print("lock-7's 25 words found as a time-shifted block inside lock-7b at (offset, shift):", blocks)
# aligned comparison: the common time shift of column 1
ks = [k for k in range(14) if rot(A[0], k) == B[0]]
print('time shifts taking lock-7 column 1 to lock-7b column 1:', ks)
for k in ks:
    agree = [i + 1 for i in range(min(LA, LB)) if rot(A[i], k) == B[i]]
    first = next((i + 1 for i in range(min(LA, LB)) if rot(A[i], k) != B[i]), None)
    print(' shift', k, ': columns agreeing', agree, '; first difference at column', first)
