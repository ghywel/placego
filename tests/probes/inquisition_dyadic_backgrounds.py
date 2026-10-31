#!/usr/bin/env python3
"""inquisition_dyadic_backgrounds.py: which periodic backgrounds of the edge frame have a power-of-two time period?
(L1263, round 7, T-Y)

RUN-ON:     cpu (Python 3 + numpy), minutes, about 1.5 GB at p = 26
COMMAND:    python3 tests/probes/inquisition_dyadic_backgrounds.py [PMAX=26]

GC2335 (carried by Local in L1263): if a spatially periodic background R of the edge frame has a least temporal
period q that is not a power of two, no black-edge pair follows it forever, and M_R(k) <= 2^(k+1) + q - 1. Only dyadic
backgrounds can attach. This probe lists them for every spatial period p <= PMAX, with no cap on q.
The ring map on Z/p is f(s)_j = s_j XOR (s_(j-1) OR s_(j-2)) (`ring_step` of inquisition_ring_references.py), with
cell j as bit j of the state. Every cycle has length <= 2^p, so a state lies on a dyadic cycle iff f^(2^p)(s) = s.
f^(2^p) is p squarings of f as an array over all 2^p states, and its image is the set of all cycle states.
For every p it prints the number of cycle states, the number of dyadic cycle states, and each dyadic cycle of
primitive spatial period p, one per class (rotation and time shift), with q and the word of the class's least state
(the T-G convention).
Controls, each an explicit require(): (1) the array map agrees with ring_step on 2,000 random states per p (all
states for p <= 10); (2) white, alternating (p even) and PR69's ether (p = 0 mod 4) are dyadic cycle states at every
p where they exist; (3) the (5, 5) background 11100 is a cycle state at p = 5, 10, ..., but not dyadic; (4) for
p <= 12, the dyadic classes with q <= 72 are exactly the T-G census classes (`cycles(p, 72)`) whose q is a power of
two, and that census has no two classes sharing (p, q) (GC2335's identity guard); (5) every reported q is checked
by direct iteration to be the least period and a power of two.
Predictions P-Y1..P-Y3: reports/inquisition-20261031.md (round 7), committed before this ran.
"""
import os
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv, sys.argv = sys.argv, sys.argv[:1]          # the ring module parses argv at import
from inquisition_ring_references import cycles, ring_step  # noqa: E402
sys.argv = _argv

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 26


class CheckFailed(Exception):
    pass


def require(cond, msg=''):
    if not cond:
        raise CheckFailed(msg)


def rot(x, k, p):
    """Bit j of the result is bit (j - k) mod p of x (x an int or a uint32 array)."""
    k %= p
    if k == 0:
        return x
    return ((x << k) | (x >> (p - k))) & ((1 << p) - 1)


def step_int(x, p):
    return x ^ (rot(x, 1, p) | rot(x, 2, p))


def ring_map(p):
    s = np.arange(1 << p, dtype=np.uint32)
    mask = np.uint32((1 << p) - 1)
    f = s.copy() if p == 1 else (s << np.uint32(1)) | (s >> np.uint32(p - 1))
    f &= mask
    if p > 2:
        t = (s << np.uint32(2)) | (s >> np.uint32(p - 2))
        t &= mask
        f |= t
        del t
    else:
        f |= s                                    # rotation by 2 is the identity on a ring of size 1 or 2
    f ^= s
    return f


def tup(x, p):
    return tuple((x >> j) & 1 for j in range(p))


def word(x, p):
    return ''.join(str((x >> j) & 1) for j in range(p))


def primitive(x, p):
    return all(rot(x, d, p) != x for d in range(1, p) if p % d == 0)


def orbit_of(x, p):
    orb = [x]
    y = step_int(x, p)
    while y != x:
        orb.append(y)
        y = step_int(y, p)
        require(len(orb) <= (1 << p), "orbit longer than the state space")
    return orb


def main():
    rng = np.random.default_rng(20261031)
    pow2 = lambda q: q & (q - 1) == 0
    census = {}
    for p in range(1, 13):
        for pp, q, orb in cycles(p, 72):
            census.setdefault((p, q), []).append(orb)
    require(all(len(v) == 1 for v in census.values()), ("two census classes share (p, q)", census.keys()))
    print(f"T-G census (p <= 12, q <= 72): {len(census)} classes, no two share (p, q)", flush=True)
    for p in range(1, PMAX + 1):
        n = 1 << p
        f = ring_map(p)
        probe = np.arange(n) if p <= 10 else rng.integers(0, n, 2000)
        require(all(tup(int(f[x]), p) == ring_step(tup(int(x), p), p) for x in probe), ("map mismatch", p))
        g = f[f]
        del f
        for _ in range(p - 1):
            g = g[g]                              # g = f^(2^p) after p squarings in all
        mark = np.zeros(n, dtype=bool)
        mark[g] = True
        ncyc = int(mark.sum())
        del mark
        dy = np.flatnonzero(g == np.arange(n, dtype=np.uint32))
        require(int(g[0]) == 0, ("white not dyadic", p))
        if p % 2 == 0:
            alt = sum(1 << j for j in range(0, p, 2))
            require(int(g[alt]) == alt, ("alternating not dyadic", p))
        if p % 4 == 0:
            eth = sum(1 << j for j in range(0, p, 4))
            require(int(g[eth]) == eth, ("ether not dyadic", p))
        if p % 5 == 0:
            st = sum(1 << j for j in range(p) if j % 5 < 3)
            o = orbit_of(st, p)                   # returns, so 11100... is a cycle state
            require(len(o) == 5 and int(g[st]) != st, ("(5, 5) control", p))
        del g
        seen, classes = set(), []
        for x in map(int, dy):
            if x in seen or not primitive(x, p):
                continue
            orb = orbit_of(x, p)
            q = len(orb)
            require(pow2(q), ("dyadic state on a non-dyadic cycle", p, x, q))
            require(q == 1 or orb[q // 2] != x, ("q not least", p, x, q))
            cls = {rot(y, d, p) for y in orb for d in range(p)}
            seen |= cls
            classes.append((q, min(cls)))
        classes.sort()
        desc = ', '.join(f"(q={q}, {word(m, p)})" for q, m in classes) or 'none'
        print(f"p={p:2d}: {ncyc} cycle states, {len(dy)} dyadic cycle states; primitive dyadic classes: {desc}",
              flush=True)
        if p <= 12:
            want = sorted((q, int(''.join(map(str, orb[0]))[::-1], 2)) for (pp, q), [orb] in census.items()
                          if pp == p and pow2(q))
            got = sorted((q, m) for q, m in classes if q <= 72)
            require(got == want, ("census mismatch", p, got, want))
    print("DYADIC_BACKGROUNDS_DONE")


if __name__ == '__main__':
    main()
