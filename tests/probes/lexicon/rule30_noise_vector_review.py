#!/usr/bin/env python3
"""rule30_noise_vector_review.py: NV, Local's second reading of GC413 (GPT's vector noise ceiling I(F;Y) <= T(1 - h(q))
for the centre trace of Rule 30 from an iid fair initial cone), requested by GPT's review flag of 2026-10-08. The
proof was checked by hand (L249); this script reproduces GC413's exact values by an independent enumeration.
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule30_noise_vector_review.py
COST:       half a second.

Enumeration: every initial cone word X on positions -(T-1) .. T-1 and every flip mask N, with weights q^|N| (1-q)^(..);
Y = X XOR N; F = the centre at times 0 .. T-1, computed by stepping the whole row (integer bits, own code). I(F;Y) is
computed as H(F) + H(Y) - H(F, Y) from exact probabilities (fractions), converted to bits at the end.

PREDICTIONS (Local's, published before the run; GC413's reported numbers, to be reproduced):
  NV-C0 (control): F is uniform on its 2^T values (G97's fresh pivots).
  NV-P1: at q = 1/4, I(F;Y) = 0.188721875541, 0.305865811849, 0.409959079384, 0.508011779645 bits for T = 1 .. 4
        (to 1e-9), each at most T(1 - h(1/4)).
  NV-P2: at q = 0, I(F;Y) = T; at q = 1/2, I(F;Y) = 0 (T = 1 .. 4).
OUTCOME, 2026-10-08 01:06 (M5, one run at commit 3b4982f, 0.5 s; transcript outside Git). NV-C0 PASS (F uniform at T = 1
.. 4). NV-P1 HELD: 0.188721875541, 0.305865811849, 0.409959079384 and 0.508011779645 bits at T = 1 .. 4, GC413's
values to twelve digits, each under T(1 - h(1/4)) (equal at T = 1). NV-P2 HELD: exactly T at q = 0 and 0 at q = 1/2.
"""
from fractions import Fraction
from math import log2


def centre_trace(x, T):
    """x: list of bits for positions -(T-1) .. T-1; returns the centre at times 0 .. T-1"""
    row = list(x)
    out = [row[T - 1]]
    for t in range(1, T):
        row = [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, len(row) - 1)]
        out.append(row[len(row) // 2])
    return tuple(out)


def H(dist):
    return -sum(float(p) * log2(float(p)) for p in dist.values() if p > 0)


def info(T, q):
    n = 2 * T - 1
    pf, py, pfy = {}, {}, {}
    for xw in range(1 << n):
        x = [(xw >> i) & 1 for i in range(n)]
        f = centre_trace(x, T)
        for nw in range(1 << n):
            k = bin(nw).count('1')
            p = Fraction(1, 1 << n) * (q ** k) * ((1 - q) ** (n - k))
            if p == 0:
                continue
            y = xw ^ nw
            pf[f] = pf.get(f, 0) + p
            py[y] = py.get(y, 0) + p
            pfy[f, y] = pfy.get((f, y), 0) + p
    return pf, H(pf) + H(py) - H(pfy)


def main():
    h = lambda q: 0.0 if q in (0, 1) else -(q * log2(q) + (1 - q) * log2(1 - q))
    want = [0.188721875541, 0.305865811849, 0.409959079384, 0.508011779645]
    c0 = p1 = p2 = True
    for T in range(1, 5):
        pf, i_q = info(T, Fraction(1, 4))
        c0 &= len(pf) == 2 ** T and all(p == Fraction(1, 2 ** T) for p in pf.values())
        _, i0 = info(T, Fraction(0))
        _, ih = info(T, Fraction(1, 2))
        ceiling = T * (1 - h(0.25))
        p1 &= abs(i_q - want[T - 1]) < 1e-9 and i_q <= ceiling + 1e-12
        p2 &= abs(i0 - T) < 1e-9 and abs(ih) < 1e-9
        print('T %d: I(F;Y) at q = 1/4 is %.12f (ceiling %.12f); at q = 0 %.6f; at q = 1/2 %.6f'
              % (T, i_q, ceiling, i0, ih))
    print('NV-C0', 'PASS' if c0 else 'FAIL')
    print('NV-P1', 'HELD' if p1 else 'REFUTED')
    print('NV-P2', 'HELD' if p2 else 'REFUTED')


if __name__ == '__main__':
    main()
