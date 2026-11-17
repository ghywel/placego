#!/usr/bin/env python3
"""The two Wolfram Language cells of the edge-sep essay (Cloud's CL622), recomputed independently for the full-cell gate (Local, 2026-10-24).
A second implementation beside Cloud's expected_numbers.py (dictionary-based scalar rule 30): this one follows the essay's own list
semantics (run) and its lane semantics (laneWords, stepLanes, centers, sigs, longest) with Python integers as 2^n-bit lane words.
Usage: python3 -I edge_sep_expected.py   (prints the two expected values as JSON)"""
import json

PAIRS = [(-2, [1, 0, 0, 1, 1, 0, 1, 0, 0], -1, [1, 0, 0, 1, 0, 0, 0, 1], 8),
         (-4, [1, 1, 1, 0, 1, 1, 0, 1], -3, [1, 1, 0, 1, 0, 0, 1, 0, 0, 1], 13),
         (-3, [1, 0, 0, 0, 1], -2, [1, 1, 0, 0, 0, 0, 1], 14)]


def run(cells, lo, T):
    """The essay's run: the center cell at times 0..T-1 of the configuration whose leftmost listed cell sits at lo."""
    w, l, out = list(cells), lo, []
    for _ in range(T):
        out.append(w[-l] if 0 <= -l < len(w) else 0)
        z = [0, 0] + w + [0, 0]
        w = [z[j - 1] ^ (z[j] | z[j + 1]) for j in range(1, len(z) - 1)]
        l -= 1
    return out


def cell1():
    rows = []
    for a, ca, b, cb, m in PAIRS:
        ta, tb = run(ca, a, m + 1), run(cb, b, m + 1)
        rows.append([a, b, ta, tb, next(t for t in range(m + 1) if ta[t] != tb[t])])
    return rows


def pat(n, s):
    return sum(1 << l for l in range(1 << n) if (l >> s) & 1)


def centers(a, R, m):
    n = R - a; full = (1 << (1 << n)) - 1
    w = [0 if (p < a or p > R) else full if p == a else pat(n, p - a - 1) for p in range(-m, m + 1)]
    out = []
    for _ in range(m + 1):
        out.append(w[m])
        z = [0] + w + [0]
        w = [z[j - 1] ^ (z[j] | z[j + 1]) for j in range(1, len(z) - 1)]
    return out, n


def sigs(a, R, m):
    c, n = centers(a, R, m)
    return {tuple((c[t] >> l) & 1 for t in range(m + 1)) for l in range(1 << n)}


def longest(a, b, R, m):
    sa, sb = sigs(a, R, m), sigs(b, R, m); k = m + 1
    while k > 0 and not ({s[:k] for s in sa} & {s[:k] for s in sb}):
        k -= 1
    return k


def cell2():
    return [[longest(-2, -1, R, 10) for R in (6, 8, 10)], longest(-4, -3, 13, 13), longest(-3, -2, 14, 14)]


if __name__ == '__main__':
    print(json.dumps({'cell1': cell1(), 'cell2': cell2()}))
