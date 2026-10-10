#!/usr/bin/env python3
"""GC1014: couple exact marker prehistory to GC629's next-return gate.
Predictions and scope: RULE30-GPT, Temporal coupling block (2026-10-10).
Finite truth tables and an exact residual cycle; no membership solver.
"""
from itertools import product
from rule30_marker_prehistory import image_language, advance


def step(r, wall):
    truth = (0, 1, 1, 1, 1, 0, 0, 0)
    return [truth[4*(wall if i == 0 else r[i-1])+2*r[i]+r[i+1]]
            for i in range(len(r)-1)]


def main():
    actual = set()
    for row in product((0, 1), repeat=11):
        out = step(step(row, 0), 1)
        if out[:5] == [1, 1, 1, 0, 1]:
            actual.add(tuple(out[5:]))
    edges = image_language()
    root = frozenset(range(4, 8))
    counts = [0, 0]
    for v in product((0, 1), repeat=4):
        a, b, c, d = v
        word = ''.join(map(str, v))
        allowed = ((not a or b) and (a or not b or c)
                   and (a or b or not c or d))
        assert bool(allowed) == (v in actual)
        assert bool(advance(edges, root, '1'+word)) == (v in actual)
        g = (not(c or d)) if (a, b) == (0, 0) else 1 if (a, b) == (0, 1) else not c if (a, b) == (1, 0) else (c or d)
        # Startup has valid forward SS/SL behavior even when past is absent.
        for tail in ([0]*30, [1]*30, [0, 1]*15):
            row = [1, 1, 1, 0, 1]+list(v)+tail
            ones = []
            for t in range(21):
                if t % 2 == 0 and row[0]:
                    ones.append(t//2)
                row = step(row, t % 2)
            assert ones[:3] == [0, 3, 6 if g else 8]
        if allowed:
            counts[0 if g else 1] += 1
    assert counts == [6, 3]
    assert (0, 0, 1, 0) not in actual  # G239's SL startup control.
    # Exact self-loop proves the whole forbidden family, not a finite scan.
    B, C = frozenset((13, 14, 15)), frozenset((10, 11, 12))
    assert advance(edges, root, '1') == B
    assert advance(edges, B, '0') == B
    assert advance(edges, B, '1') == C
    assert not advance(edges, C, '0')
    print('PASS: nine exact mature prefixes; SS=6, SL=3; startup and residual-cycle controls')


if __name__ == '__main__':
    main()
