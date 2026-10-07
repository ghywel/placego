#!/usr/bin/env python3
"""GC399: individual wall-time sensitivity of GC397's anchored implication.
Before run: P1 at least one wall flip at time0..7 breaks it (confidence0.8).
P2 flips at8..11 do not, by radius-one causality. Counterfactual: only a
collective wall-phase change breaks it, while every single flip passes.
Controls: baseline zero violations; all-wall flip with initial1=0 reproduces544
violations. Scalar replay of one counterexample per failing mutation.
Unexpected check: individual survival does not establish joint dispensability.
OUTCOME: P1 and P2 HELD. Every single flip0..7 admits counterexamples
(counts2444,864,240,976,848,812,1340,1504); flips8..11 give none.
Baseline zero; all-wall flip gives544 violations with initial1=0, as GC397.
Every failing schedule has a scalar-replayed counterexample. The late times
are jointly irrelevant by locality, not just by the single-flip measurements.
4096 exterior/initial1 assignments per14 schedules; finite cone only.
"""
import json


def run(bits, flips, scalar=False):
    row = bits << 1
    cells = [(row >> j) & 1 for j in range(18)] if scalar else None
    a = None
    for t in range(13):
        wall = (t % 2) ^ (t in flips)
        row = (row & ~1) | wall
        if scalar:
            cells[0] = wall
            assert cells == [(row >> j) & 1 for j in range(len(cells))]
        if t == 8:
            a = (row >> 6) & 1
        if t < 12:
            n = 17-t
            row = ((row << 1) ^ (row | (row >> 1))) & ((1 << n)-1)
            if scalar:
                cells = [0] + [cells[j-1] ^ (cells[j] | cells[j+1])
                               for j in range(1, len(cells)-1)]
    return a, (row >> 5) & 1


def main():
    schedules = [frozenset()] + [frozenset([t]) for t in range(12)] + [frozenset(range(12))]
    result = []
    for flips in schedules:
        bad = fixed1bad = 0
        witness = None
        for free in range(4096):
            bits = 14 | (free & 1) | ((free >> 1) << 6)
            a, c = run(bits, flips)
            if a and not c:
                bad += 1
                fixed1bad += not (bits & 1)
                witness = bits if witness is None else witness
        if witness is not None:
            assert run(witness, flips, scalar=True) == (1, 0)
        result.append({'flips': sorted(flips), 'violations': bad,
                       'violations_initial1_zero': fixed1bad})
    assert result[0]['violations'] == 0
    assert result[-1]['violations_initial1_zero'] == 544
    assert all(r['violations'] == 0 for r in result if r['flips'] in ([8], [9], [10], [11]))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
