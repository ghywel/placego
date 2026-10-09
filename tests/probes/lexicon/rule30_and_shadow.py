#!/usr/bin/env python3
"""rule30_and_shadow.py: AS, the intermediate maps between each prize's linear shadow and the prize itself (Cloud's
CL090 question 2, from the owner's "XOR plus AND" question). Local's run (chat L453), predictions pushed before it.

RUN-ON:     cpu (Python 3, numpy); a few minutes
COMMAND:    python3 tests/probes/lexicon/rule30_and_shadow.py

Collatz side. Write the odd step as (n + (2n + 1)) / 2 with the addition's carries allowed to travel at most k places:
a carry is born where both addends have a 1 (age 1), moves one place per bit, keeps moving while exactly one addend
bit is 1 there (age + 1), and is dropped once its age would exceed k; a carry meeting a fresh birth merges into the
fresh one. k = 0 is the carry-free map (n XOR 2n XOR 1) / 2, whose analogue over F_2[x] always reaches 1 (CL090,
reported); unlimited k is the Collatz map (3n + 1) / 2. Even steps halve. For every start n < 2^18 and each k, follow
the orbit for up to 100,000 steps or until it exceeds 2^60: it reaches 1, enters a cycle (recorded by its least
member), or is cut off.
Rule 30 side. Rule 30 is l xor c xor r xor (c AND r); Rule 150 is l xor c xor r. Apply the AND term only at cells in a
set S: x'(i) = x(i-1) xor x(i) xor x(i+1) xor [i in S] x(i) x(i+1). From one black cell at 0, run 4,096 rows (exact,
bit-sliced) and ask whether the centre column is periodic over rows 2,048 .. 4,095 (least period up to 1,024 tested
exactly), and its density there. S = mZ (the AND acts at the centre) and S = mZ + floor(m/2) (it does not, for m >= 2),
for m = 1 .. 32 and S empty.

PREDICTIONS (Local's, published before the run):
  AS-C1 (control): k = 0 sends every n < 2^18 to 1 (the reported F_2 theorem's integer analogue, checked to 2^21 in
        CL090); unlimited k (k = 64) sends every n < 2^18 to 1 (Collatz, long verified).
  AS-C2 (control): S empty (Rule 150) gives an all-black centre; S = Z (m = 1) is Rule 30, not periodic on the window.
  AS-P1 (NOT blind; see the disclosure below): some intermediate k in 1 .. 8 has a start n < 2^18 that does not reach
        1 (a cycle other than 1 -> 2 -> 1, or a cut-off orbit).
  AS-P1b (blind, confidence 0.5): there is a threshold k* <= 12 with every n < 2^18 reaching 1 for all k from k* to 12.
  Disclosure: the instrument smoke run before this header was pushed (n < 2^10, k = 3 only, to time the memoised
  orbit code) already showed 419 of 1,023 starts not reaching 1. P1 is therefore informed, not blind, and is kept
  only for the record; P1b, P2 and P3 concern things the smoke did not look at.
  AS-P2 (blind, confidence 0.6): with S = mZ, the centre column is aperiodic on the window for every m <= 32 (the AND
        at the centre itself suffices to break Rule 150's periodic centre).
  AS-P3 (blind, confidence 0.5): with S = mZ + floor(m/2), some m >= 2 keeps a periodic centre (the AND kept off the
        centre fails to break it).
  AS-D1 (descriptive): per k, the counts reaching 1 / cycling / cut off, and the cycles' least members; per S, period
        or aperiodic, and the window density.
"""
import sys

import numpy as np

KS = list(range(0, 13)) + [64]
NMAX = 1 << 18


def add_k(a, b, k):
    """a + b with each carry travelling at most k places (k = 64 is ordinary addition here)"""
    if k >= 64:
        return a + b
    out, i, carry_age = 0, 0, 0                       # carry_age 0: no carry coming into bit i
    while a >> i or b >> i or carry_age:
        ai, bi = (a >> i) & 1, (b >> i) & 1
        ci = 1 if carry_age else 0
        out |= ((ai ^ bi ^ ci) & 1) << i
        if ai & bi:
            new_age = 1                                # a fresh carry (an incoming one merges into it)
        elif (ai ^ bi) & ci:
            new_age = carry_age + 1                    # the carry moves on
        else:
            new_age = 0
        carry_age = new_age if 0 < new_age <= k else 0
        i += 1
    return out


MEMO = {}


def orbit_end(n, k, cap=100000, big=1 << 60):
    memo = MEMO.setdefault(k, {})
    seen, path = {}, []
    for s in range(cap):
        if n in memo:
            res = memo[n]
            for v in path:
                memo[v] = res
            return res
        if n == 1:
            for v in path:
                memo[v] = ('one', None)
            return 'one', None
        if n > big:
            return 'cut', None
        if n in seen:
            cyc = [n]
            m = n
            while True:
                m = m // 2 if m % 2 == 0 else add_k(m, 2 * m + 1, k) // 2
                if m == n:
                    break
                cyc.append(m)
            res = ('cycle', min(cyc))
            for v in path:
                memo[v] = res
            return res
        seen[n] = s
        path.append(n)
        n = n // 2 if n % 2 == 0 else add_k(n, 2 * n + 1, k) // 2
    return 'cut', None


def collatz_side():
    res = {}
    for k in KS:
        one = cut = 0
        cycles = {}
        for n in range(1, NMAX):
            e, c = orbit_end(n, k)
            if e == 'one':
                one += 1
            elif e == 'cut':
                cut += 1
            else:
                cycles[c] = cycles.get(c, 0) + 1
        res[k] = (one, cut, cycles)
        print('k = %2s: reach 1: %d; cut off: %d; cycles (least member: starts): %s' % (
            k if k < 64 else 'inf', one, cut, dict(sorted(cycles.items())[:8])), flush=True)
    return res


def centre_column(T, inS):
    W = 2 * T + 3
    off = T + 1
    x = np.zeros(W, dtype=np.uint8)
    x[off] = 1
    mask = np.array([1 if inS(i - off) else 0 for i in range(W)], dtype=np.uint8)
    col = []
    for _ in range(T):
        col.append(int(x[off]))
        l, r = np.roll(x, 1), np.roll(x, -1)
        x = l ^ x ^ r ^ (mask & x & r)
    return col


def periodic(seq, pmax=1024):
    for p in range(1, pmax + 1):
        if all(seq[t] == seq[t + p] for t in range(len(seq) - p)):
            return p
    return None


def rule_side():
    T = 4096
    out = {}
    cases = [('empty', lambda i: False)]
    for m in range(1, 33):
        cases.append(('mZ m=%d' % m, lambda i, m=m: i % m == 0))
        if m >= 2:
            cases.append(('mZ+%d m=%d' % (m // 2, m), lambda i, m=m: i % m == m // 2))
    for name, f in cases:
        col = centre_column(T, f)
        win = col[T // 2:]
        p = periodic(win)
        out[name] = p
        print('%-14s centre on rows %d..%d: %s; density %.3f' % (
            name, T // 2, T - 1, 'period %d' % p if p else 'aperiodic', sum(win) / len(win)), flush=True)
    return out


def main():
    cres = collatz_side()
    rres = rule_side()
    c1 = cres[0][0] == NMAX - 1 and cres[64][0] == NMAX - 1
    print('AS-C1', 'PASS' if c1 else 'FAIL')
    c2 = rres['empty'] == 1 and rres['mZ m=1'] is None
    print('AS-C2', 'PASS' if c2 else 'FAIL')
    p1 = [k for k in range(1, 9) if cres[k][0] < NMAX - 1]
    print('AS-P1', ('HELD at k = %s' % p1) if p1 else 'REFUTED')
    full = [k for k in range(0, 13) if cres[k][0] == NMAX - 1]
    kstar = next((k for k in range(13) if all(j in full for j in range(k, 13))), None)
    print('AS-P1b', ('HELD (k* = %d)' % kstar) if kstar is not None else 'REFUTED (no threshold up to 12)')
    p2 = [m for m in range(1, 33) if rres['mZ m=%d' % m] is not None]
    print('AS-P2', 'HELD' if not p2 else 'REFUTED at m = %s' % p2)
    p3 = [m for m in range(2, 33) if rres['mZ+%d m=%d' % (m // 2, m)] is not None]
    print('AS-P3', ('HELD at m = %s' % p3) if p3 else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    main()
