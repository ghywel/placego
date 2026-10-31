#!/usr/bin/env python3
"""inquisition_coarse_grain.py: exhaustive Israeli-Goldenfeld coarse-grainings for block size N <= 4 (T-C, DQ-033).

RUN-ON:     cpu (Python 3 + numpy), a few minutes
COMMAND:    python3 tests/probes/inquisition_coarse_grain.py [NMAX=4]

A projection P: {0,1}^N -> {0,1} coarse-grains elementary rule R onto elementary rule g when
P(F_R^N(abc)) = g(P(a), P(b), P(c)) for all N-cell blocks a, b, c (Israeli and Goldenfeld, PRE 2006: cell size and
time both scale by N). Constant P is excluded. For each rule and N, every P is tested: the induced map from
(P(a), P(b), P(c)) to P(middle block after N steps) must be single-valued. Prints each consistent P with the target
rules it allows (classes never hit leave g free). Controls: Rules 90 and 150 at N = 2 with P = first cell. Known
answer (prior art) for Rule 30 and its images 86, 135, 149: none, to N = 7 (Song and Aaron, arXiv 2012.12153).
Predictions P-C1, P-C2: reports/inquisition-20261031.md (round 2), committed before this ran.
"""
import sys
import numpy as np

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4


def step(w, L, rule):
    """One step of an elementary rule on L-cell words (bit i = cell i, left to right); returns L - 2 cells."""
    out = np.zeros_like(w)
    for idx in range(1, L - 1):
        l = (w >> (idx - 1)) & 1
        c = (w >> idx) & 1
        r = (w >> (idx + 1)) & 1
        v = (rule >> (4 * l + 2 * c + r)) & 1
        out |= v << (idx - 1)
    return out


def middle_after(N, rule):
    L = 3 * N
    w = np.arange(1 << L, dtype=np.int64)
    cur, length = w.copy(), L
    for _ in range(N):
        cur = step(cur, length, rule)
        length -= 2
    assert length == N
    mask = (1 << N) - 1
    return w & mask, (w >> N) & mask, (w >> (2 * N)) & mask, cur


def search(N, rule):
    a, b, c, mid = middle_after(N, rule)
    nproj = 1 << (1 << N)
    found = []
    chunk = max(1, (1 << 24) // len(a))
    for p0 in range(1, nproj - 1, chunk):
        P = np.arange(p0, min(nproj - 1, p0 + chunk), dtype=np.int64)[:, None]
        key = ((P >> a) & 1) * 4 + ((P >> b) & 1) * 2 + ((P >> c) & 1)
        val = (P >> mid) & 1
        flat = (np.arange(len(P))[:, None] * 16 + key * 2 + val).ravel()
        pres = np.bincount(flat, minlength=len(P) * 16).reshape(len(P), 8, 2) > 0
        ok = ~np.any(pres[:, :, 0] & pres[:, :, 1], axis=1)
        for i in np.nonzero(ok)[0]:
            hit = pres[i, :, 0] | pres[i, :, 1]
            fixed = sum(int(pres[i, k, 1]) << k for k in range(8))
            free = [k for k in range(8) if not hit[k]]
            targets = sorted({fixed | sum(((s >> j) & 1) << free[j] for j in range(len(free)))
                              for s in range(1 << len(free))})
            found.append((int(P[i, 0]), targets))
    return found


def main():
    for rule, Ns in [(90, [2]), (150, [2])]:
        for N in Ns:
            res = search(N, rule)
            firstcell = 0b1010
            ok = any(p == firstcell and rule in t for p, t in res)
            print(f"control rule {rule} N={N}: {len(res)} non-constant coarse-grainings; first-cell P found onto itself: {ok}")
            assert ok, "control failed"
    for rule in (30, 86, 135, 149):
        for N in range(2, NMAX + 1):
            res = search(N, rule)
            print(f"rule {rule} N={N}: {len(res)} non-constant coarse-grainings" +
                  (f"; e.g. {res[:3]}" if res else ""))
    print("COARSE_GRAIN_DONE")


if __name__ == '__main__':
    main()
