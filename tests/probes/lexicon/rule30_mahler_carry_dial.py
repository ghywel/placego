#!/usr/bin/env python3
"""rule30_mahler_carry_dial.py: MD, the carry-length dial on Mahler's 3/2 map, the third corner of the owner's
Rule 30 / Collatz / Mahler triangle (2026-10-09, the owner: "Continue with the map"). Local's run (chat L457),
predictions pushed before it.

RUN-ON:     cpu (Python 3, kissat); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_mahler_carry_dial.py

Mahler's question: can frac(xi (3/2)^n) stay below 1/2 (first binary digit after the point 0) for every n >= 0? For
an integer part g = floor(xi), the survival horizon H(g) is the largest N for which some xi in [g, g + 1) keeps that
digit 0 at n = 0 .. N - 1. A Z-number with integer part g exists exactly when H(g) is infinite (Mahler: at most one
per unit interval; none is known).
  k = inf (the true map). Exact: within the surviving set the integer parts follow g -> ceil(3g/2) (RULE30-GPT.md
  GC616; COLLATZ-PRIZE.md), and with f = xi - g, frac(xi (3/2)^n) = (3/2)^n f - c_n with c_0 = 0,
  c_(n+1) = (3/2) c_n + (g_n mod 2) / 2. Each condition is an interval of f, so the survivors form one interval,
  tracked with exact fractions.
  k finite. The step x -> (x + 2x) / 2 with each carry of the addition travelling at most k places (born where both
  addend digits are 1, moving one place per digit while exactly one addend digit is 1, dropped past age k; the same
  rule as rule30_and_shadow.py). The new digit p is a(p + 1) xor a(p) xor carry(p + 1), so the map is local: digit -1
  at step N - 1 depends only on digits -1 - k(N - 1) - 1 .. N - 2 at step 0. H_k(g) is decided by SAT over that cone
  (integer digits fixed to g, fraction digits free, digit -1 = 0 at every step), raising N until UNSAT (UNSAT at N
  stays UNSAT at every larger N) or a cap.

PREDICTIONS (Local's, published before the run):
  MD-C1 (control): the SAT encoding agrees with brute force over every fraction-digit assignment of the cone, for
        k = 0 .. 3, g = 1 .. 7 and N = 1 .. 4 (exact finite dyadic simulation; digits below the cone cannot reach
        digit -1 in time).
  MD-C2 (control): no g <= 4096 has H_inf(g) >= 80 (no Z-number is known; Mahler's conjecture).
  MD-P1 (blind, confidence 0.6): at k = 0 every g <= 63 has H_0(g) <= 10.
  MD-P2 (blind, confidence 0.5): max over g <= 63 of H_k(g) is not monotone in k for k = 0 .. 8 (as AS found the
        Collatz dial non-monotone).
  MD-P3 (blind, confidence 0.4): some k in 1 .. 8 has a g <= 63 surviving to the cap N = 24 (a candidate
        "k-Z-number").
  MD-D1 (descriptive): the H_inf distribution for g <= 4096, and the table of H_k(g) for k = 0 .. 8, g <= 63.
  Disclosure: the instrument smoke (SAT against brute force at g = 9, 10, k = 1, 2, N <= 3) also printed
  H_inf(1 .. 5) = 4, 3, 2, 12, 6 before this header was pushed; no prediction above concerns those values.
OUTCOME, 2026-10-09 18:33 BST (M5, about 2 minutes, run at commit f2d78a75): MD-C1 PASS, MD-C2 PASS, MD-P1 HELD,
  MD-P2 HELD, MD-P3 HELD.
  k = inf (exact, g <= 4096): horizons from 2 to 29 (1024 at 2, falling roughly by half per step; one g at 26, two at
  27, two at 28, one at 29); no Z-number, as conjectured.
  k = 0 and k = 1: H(g) = v2(g) + 1 exactly for g <= 63 (1 2 1 3 1 2 1 4 ...), the ruler sequence.
  Max H over g <= 63 by k = 0 .. 8: 6, 6, 15, 24, 24, 24, 15, 24, 19 (24 is the cap); survivors to the cap: k = 3 (g =
  1, 22), k = 4 (g = 53), k = 5 (g = 1, 5, 38, 57), k = 7 (g = 1).
  Exploratory, after the run (no predictions): replaying each survivor's SAT model shows two kinds. At odd k (3, 5, 7)
  every survivor's integer part collapses to 0 within three steps (the dropped carries cancel it) and a small fraction
  then stays below 1/2: a degenerate survival, as carry-limited Collatz collapses to 0 at odd k (AS). At k = 4, g = 53
  survives with its integer part growing (53, 76, 114, 171, 224, 336, ... 397189 at step 23); followed further,
  H_4(53) = 30 (finite), against the true map's H_inf(53) = 25, the true map's longest survivor up to g = 63. Also
  H_2(53) = 2, H_6(53) = 10, H_8(53) = 19.
  Reading: the carry dial has the same odd/even split on Mahler's map as on Collatz (collapse at odd k), and the
  true map's record holder g = 53 is also the dial's genuine survivor at k = 4. These are finite-horizon measurements.
"""
import os
import subprocess
import sys
from fractions import Fraction as F

DIR = os.path.expanduser('~/np-scratch-int/rule30-md')
CAP = 24


def H_inf(g, cap=80):
    lo, hi = F(0), F(1, 2)                        # f in [lo, hi)
    A, c, gn = F(1), F(0), g
    for n in range(cap):
        # condition at step n: A f - c in [0, 1/2)
        lo, hi = max(lo, c / A), min(hi, (c + F(1, 2)) / A)
        if lo >= hi:
            return n
        c = F(3, 2) * c + F(gn % 2, 2)
        A = F(3, 2) * A
        gn = -(-3 * gn // 2)                       # ceil(3 g / 2)
    return cap


class CNF:
    def __init__(self):
        self.n, self.cl = 0, []

    def var(self):
        self.n += 1
        return self.n

    def AND(self, a, b):
        if a is False or b is False:
            return False
        if a is True:
            return b
        if b is True:
            return a
        y = self.var()
        self.cl += [[-y, a], [-y, b], [y, -a, -b]]
        return y

    def XOR(self, a, b):
        if isinstance(a, bool) and isinstance(b, bool):
            return a != b
        if isinstance(a, bool):
            a, b = b, a
        if isinstance(b, bool):
            return -a if b else a
        y = self.var()
        self.cl += [[-y, a, b], [-y, -a, -b], [y, -a, b], [y, a, -b]]
        return y

    def OR(self, xs):
        xs = [x for x in xs if x is not False]
        if any(x is True for x in xs):
            return True
        if not xs:
            return False
        if len(xs) == 1:
            return xs[0]
        y = self.var()
        for x in xs:
            self.cl.append([-x, y])
        self.cl.append([-y] + xs)
        return y


def build(g, k, N):
    """CNF whose models are fraction-digit assignments keeping digit -1 at 0 for steps 0 .. N-1 (None if trivial)"""
    f = CNF()
    L = [-1 - k * (N - 1 - t) - 1 for t in range(N)]
    R = [-1 + (N - 1 - t) for t in range(N)]
    a = {}
    for p in range(L[0], R[0] + 1):
        a[(0, p)] = bool((g >> p) & 1) if p >= 0 else f.var()
    for t in range(N - 1):
        e = {}

        def carry_age(q, j):                      # a carry of age j arrives at position q (time t)
            if (q, j) in e:
                return e[(q, j)]
            if q - j < L[t] + 1:
                raise ValueError('outside the cone')
            if j == 1:
                v = f.AND(a[(t, q - 1)], a[(t, q - 2)])
            else:
                v = f.AND(carry_age(q - 1, j - 1), f.XOR(a[(t, q - 1)], a[(t, q - 2)]))
            e[(q, j)] = v
            return v
        for p in range(L[t + 1], R[t + 1] + 1):
            q = p + 1
            c = f.OR([carry_age(q, j) for j in range(1, k + 1)]) if k > 0 else False
            a[(t + 1, p)] = f.XOR(f.XOR(a[(t, p + 1)], a[(t, p)]), c)
    for t in range(N):
        x = a[(t, -1)]
        if x is True:
            return None                            # digit -1 forced to 1: UNSAT outright
        if x is not False:
            f.cl.append([-x])
    return f


def sat(g, k, N, tag):
    f = build(g, k, N)
    if f is None:
        return False
    if not f.cl:
        return True
    os.makedirs(DIR, exist_ok=True)
    path = os.path.join(DIR, tag + '.cnf')
    with open(path, 'w') as fh:
        fh.write('p cnf %d %d\n' % (f.n, len(f.cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in f.cl))
    r = subprocess.run(['kissat', '-q', path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode not in (10, 20):
        raise RuntimeError('kissat gave %d' % r.returncode)
    return r.returncode == 10


def add_k(a, b, k):
    out, i, age = 0, 0, 0
    while a >> i or b >> i or age:
        ai, bi = (a >> i) & 1, (b >> i) & 1
        ci = 1 if age else 0
        out |= (ai ^ bi ^ ci) << i
        new = 1 if ai & bi else (age + 1 if (ai ^ bi) & ci else 0)
        age = new if 0 < new <= k else 0
        i += 1
    return out


def brute(g, k, N):
    D = 1 + k * (N - 1) + 1                        # fraction digits in the cone
    for frac in range(1 << D):
        X = (g << D) | frac                        # xi * 2^D
        ok = True
        for t in range(N):
            if (X >> (D - 1)) & 1:                 # digit -1
                ok = False
                break
            X = add_k(X, X << 1, k) >> 1
        if ok:
            return True
    return False


def H_k(g, k, cap=CAP):
    for N in range(1, cap + 1):
        if not sat(g, k, N, 'g%d-k%d-N%d' % (g, k, N)):
            return N - 1
    return cap


def main():
    bad = [(k, g, N) for k in range(4) for g in range(1, 8) for N in range(1, 5)
           if sat(g, k, N, 'c1') != brute(g, k, N)]
    print('MD-C1', 'PASS' if not bad else 'FAIL %s' % bad[:5], flush=True)
    hinf = {g: H_inf(g) for g in range(1, 4097)}
    dist = {}
    for v in hinf.values():
        dist[v] = dist.get(v, 0) + 1
    print('H_inf for g <= 4096: distribution', dict(sorted(dist.items())), '; max', max(hinf.values()),
          'at g =', [g for g, v in hinf.items() if v == max(hinf.values())][:6], flush=True)
    print('MD-C2', 'PASS' if max(hinf.values()) < 80 else 'FAIL')
    table = {}
    for k in range(0, 9):
        row = [H_k(g, k) for g in range(1, 64)]
        table[k] = row
        print('k = %d: max H %d at g = %s; H(g) for g = 1 .. 63: %s' % (
            k, max(row), [g for g, v in zip(range(1, 64), row) if v == max(row)][:6], ' '.join(map(str, row))),
            flush=True)
    print('k = inf (exact): H(g) for g = 1 .. 63:', ' '.join(str(hinf[g]) for g in range(1, 64)))
    print('MD-P1', 'HELD' if max(table[0]) <= 10 else 'REFUTED (max %d)' % max(table[0]))
    mx = [max(table[k]) for k in range(9)]
    print('MD-P2', 'HELD' if any(mx[i + 1] < mx[i] for i in range(8)) and any(mx[i + 1] > mx[i] for i in range(8))
          else 'REFUTED', '(max H by k:', mx, ')')
    surv = [(k, g) for k in range(1, 9) for g, v in zip(range(1, 64), table[k]) if v >= CAP]
    print('MD-P3', ('HELD %s' % surv[:8]) if surv else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    main()
