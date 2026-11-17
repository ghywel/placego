#!/usr/bin/env python3
"""inquisition_trace_grammar.py: how much freedom two adjacent traces of Rule 30 have, by direction (T-S, DQ-033).

RUN-ON:     cpu (Python 3 + numpy), a few minutes
COMMAND:    python3 tests/probes/inquisition_trace_grammar.py [NROW=16] [NCOL=13] [NDIAG=9]

N(n) is the number of distinct patterns a strip of n steps can carry in a Rule 30 spacetime. Strips: two rows, two
columns, two right diagonals (up-right), two left diagonals (up-left), and single lines as controls. Exact: Rule 30
is onto, so every finite row has a past, and the valid patches of a window of height h are exactly the evolutions of
every base row covering the strip's light cone (its positions widened by h - 1 on each side). Base rows are bit-packed
(bit i is position base + i) and enumerated in chunks. Prints N(n), the growth N(n)/N(n-1) and N(n)/4^n.
Predictions P-S1..P-S3: reports/inquisition-20261031.md (round 2), committed before this ran.
"""
import sys
import numpy as np

NROW = int(sys.argv[1]) if len(sys.argv) > 1 else 16
NCOL = int(sys.argv[2]) if len(sys.argv) > 2 else 13
NDIAG = int(sys.argv[3]) if len(sys.argv) > 3 else 9
CHUNK = 1 << 22


def strip(kind, n):
    if kind == 'two rows':
        return [(i, t) for t in range(2) for i in range(n)]
    if kind == 'two columns':
        return [(p, t) for t in range(n) for p in (0, 1)]
    if kind == 'two right diagonals':
        return [(t + d, t) for t in range(n) for d in (0, 1)]
    if kind == 'two left diagonals':
        return [(-t + d, t) for t in range(n) for d in (0, 1)]
    if kind == 'one column':
        return [(0, t) for t in range(n)]
    if kind == 'one right diagonal':
        return [(t, t) for t in range(n)]
    if kind == 'one left diagonal':
        return [(-t, t) for t in range(n)]
    raise ValueError(kind)


def count(cells):
    h = max(t for _, t in cells) + 1
    lo = min(p for p, _ in cells) - (h - 1)
    hi = max(p for p, _ in cells) + (h - 1)
    B = hi - lo + 1
    assert B <= 62
    by_t = {}
    for m, (p, t) in enumerate(cells):
        by_t.setdefault(t, []).append((m, p - lo))
    total = 1 << B
    seen = np.zeros(0, dtype=np.uint64)
    one = np.uint64(1)
    for start in range(0, total, CHUNK):
        row = np.arange(start, min(total, start + CHUNK), dtype=np.uint64)
        pat = np.zeros_like(row)
        for t in range(h):
            for m, idx in by_t.get(t, []):
                pat |= ((row >> np.uint64(idx)) & one) << np.uint64(m)
            if t + 1 < h:
                row = (row << one) ^ (row | (row >> one))
        seen = np.union1d(seen, np.unique(pat))
    return len(seen), B


def main():
    plans = [('two rows', NROW), ('one column', NCOL), ('one right diagonal', NDIAG), ('one left diagonal', NDIAG),
             ('two columns', NCOL), ('two right diagonals', NDIAG), ('two left diagonals', NDIAG)]
    for kind, nmax in plans:
        prev = None
        out = []
        for n in range(1, nmax + 1):
            N, B = count(strip(kind, n))
            g = N / prev if prev else float('nan')
            lines = 2 if kind.startswith('two') else 1
            out.append(f"n={n:2d} N={N:9d} growth={g:.4f} N/{2**lines}^n={N / (2 ** lines) ** n:.4f} (base {B})")
            prev = N
        print(kind)
        for line in out:
            print("   ", line)
    print("TRACE_GRAMMAR_DONE")


if __name__ == '__main__':
    main()
