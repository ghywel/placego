#!/usr/bin/env python3
"""Couple two GC1203 hole charges; fixed controls, no solver or census.

RUN-ON: cpu, Python standard library.
COMMAND: python3 tests/probes/lexicon/rule30_zero_triangle_adjacent_charge.py

Record searched: adjacent-diagonal/parity with transport/charge ->12hits7files;
empty-pair/visible/no11/source ->16hits10files. GC1203, GC717, GC549
checkpoint4 and G240's near-wall source/cancellation read. Those sources
are credited; no new no11 or shrink theorem is asserted.

PREDICTIONS before first execution (2026-10-13):
 C1: on all16 literal four-cell inputs A,B,C,D (depths j+2..j-1),
     h_(t+1)(j+1) XOR h_t(j) = AB XOR h_t(j)(A XOR B).
 C2: at d2/5/8,a0/1, both phases and two fixed tails (24 cases),
     the path-shift formula Q_next=Q_old XOR sum(Dsource) XOR terminal
     holds. If the two tested black guards pass, the parity R of the
     source excluding the old terminal satisfies R=1 XOR q_old XOR q_next.
     No actual right realization or earlier clock pass is inferred.
 C3: the existing phase1,d125,L21 fixture at a0/1/8 has R=1/1/0,
     respectively for visible pairs00/00/10. Predictions follow from
     the already-read GC1199 prefix at white125/127,127/129,141/143.
 Independent: literal Wolfram30 versus packed Boolean evolution; direct
     adjacent hole counts versus the local source polynomial.
 Counterfactual/unexpected: dropping the old black guard loses the
     terminal identity. Literal input0000 has source0, demanded visible1.
     With that guard, B=1-C and the identity holds for both A values.
 This checks the new relation, not the fixture's full validity or any
     membership, record, survival, period or language census.

OUTCOME: C1 all16, C2 all24 (eight passing two-guard cases) and C3
all three actual pairs held. Independent engines and the dropped-guard
counter passed. No instrument failure.
"""
import json
from itertools import product
from pathlib import Path

from rule30_zero_triangle_guard_transport import literal, packed, seed_for


def h(a, b):
    return (1 - a) * (1 - b)


def source(a, b, c, d):
    return (a * b) ^ (h(c, d) * (a ^ b))


def cell(rows, phase, t, j):
    return rows[t][j] if j else (phase + t) % 2


def path(rows, phase, d, a, e):
    k, crop = d + 2 * a + e, a + 1
    n = k - crop
    holes, sources = [], []
    for u in range(n):
        t, j = crop + u, n - u
        c, inner = cell(rows, phase, t, j), cell(rows, phase, t, j - 1)
        outer, b = cell(rows, phase, t, j + 2), cell(rows, phase, t, j + 1)
        holes.append(h(c, inner))
        sources.append(source(outer, b, c, inner))
        assert h(cell(rows, phase, t + 1, j + 1), cell(rows, phase, t + 1, j)) == holes[-1] ^ sources[-1]
    return holes, sources


def check(rows, phase, d, a):
    e = 1 ^ ((phase + d) % 2)
    k = d + 2 * a + e
    old, sources = path(rows, phase, d, a, e)
    new, _ = path(rows, phase, d, a + 1, e)
    assert sum(new) % 2 == (sum(old) % 2) ^ (sum(sources) % 2) ^ new[-1]
    r = sum(sources[:-1]) % 2
    q_old, q_new = 1 ^ rows[k - 1][1], 1 ^ rows[k + 1][1]
    passed = rows[k][1] == rows[k + 2][1] == 1
    if passed:
        assert sources[-1] == q_old
        assert r == 1 ^ q_old ^ q_new
    return passed, r, (q_old, q_new)


def main():
    for a, b, c, d in product((0, 1), repeat=4):
        outer = (30 >> (4 * a + 2 * b + c)) & 1
        inner = (30 >> (4 * b + 2 * c + d)) & 1
        assert h(outer, inner) ^ h(c, d) == source(a, b, c, d)
    count, passes = 0, 0
    for d, a, phase, tail in product((2, 5, 8), (0, 1), (0, 1), (0, 1)):
        e = 1 ^ ((phase + d) % 2)
        k = d + 2 * a + e
        seed = seed_for(d, k + 2, tail)   # zeros through k+3
        width = 2 * k + 10
        rows = packed(seed, phase, k + 2, width)
        assert rows == literal(seed, phase, k + 2, width)
        ok, _, _ = check(rows, phase, d, a)
        passes += ok
        count += 1
    root = Path(__file__).resolve().parents[3]
    records = json.loads((root / 'site/wolframcollatzmahler/data/records.json').read_text())['rows']
    f = next(r for r in records if r['depth'] == 125 and r['phase'] == 1)
    assert f['L'] == 21 and len(f['left']) == 145 and f['left'][123] == '1'
    seed = {j: int(b) for j, b in enumerate(f['left'], 1)}
    rows = packed(seed, 1, 144, 290)
    assert rows == literal(seed, 1, 144, 290)
    for a, expected, pair in ((0, 1, (0, 0)), (1, 1, (0, 0)), (8, 0, (1, 0))):
        ok, r, visible = check(rows, 1, 125, a)
        assert ok and r == expected and visible == pair
        k = 126 + 2 * a
        assert visible == tuple(int(f['visible'][(t - 1) // 2]) for t in (k - 1, k + 1))
        assert r == h(*visible)
    assert source(0, 0, 0, 0) == 0 and 1 - 0 == 1
    for a, c in product((0, 1), repeat=2):
        assert source(a, 1 - c, c, 0) == 1 - c
    print('C1 PASS:16 literal local inputs. C2 PASS:', count, 'fixed path pairs;', passes, 'two-guard cases.')
    print('C3 PASS: actual125 pairs00/00/10 give R1/1/0; independent engines and terminal counter PASS.')


if __name__ == '__main__':
    main()
