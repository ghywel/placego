#!/usr/bin/env python3
"""GC853 first-exit projection control, registered in CLOUD-LOCAL before scratch.
P1: a new successor differs from the reference only at falling transitions of Y.
P2: their number is common across the reference and <=154.
X1: all 156 black ticks are free (must fail at sustained-black ticks).
OUTCOME: exactly121 falling ticks per column; P1/P2 PASS, X1 REFUTED.
Retained initial failure: the +29 indexed phase check failed; the literal
right-reading convention needs +126 = -29 modulo155. The corrected check passes.
Small reference arithmetic and literal bit projection, no branch enumeration,
no SAT query, no infinite-extension claim. GC798 supplies the projection method.
"""
from itertools import product
R = 0x35409b1caa645d715104db5291a2fe8415260ce
N, P = 155, 310

def check():
    row = [(R >> i) & 1 for i in range(N)]
    start = row[:]
    V = [[] for _ in row]
    for _ in range(P):
        for i, b in enumerate(row):
            V[i].append(b)
        row = [row[i] ^ (row[(i+1) % N] | row[(i+2) % N]) for i in range(N)]
    assert row == start
    counts = []
    for i in range(N):
        X, Y, refZ = V[i], V[(i+1) % N], V[(i+2) % N]
        free = 0
        for t in range(P):
            assert X[(t+2) % P] == V[(i+126) % N][t]
            dx, dy = X[t] ^ X[(t+1) % P], Y[t] ^ Y[(t+1) % P]
            possible = {z for z, w in product((0, 1), repeat=2)
                        if dx == (Y[t] | z) and dy == (z | w)}
            assert refZ[t] in possible
            fall = Y[t] == 1 and Y[(t+1) % P] == 0
            assert len(possible) == (2 if fall else 1)
            free += fall
        assert sum(Y) == 156 and free < sum(Y) and free <= 154
        counts.append(free)
    assert set(counts) == {121}
    print('GC853 PASS: literal two-edge projection, temporal phase identity; 121 free ticks')

if __name__ == '__main__':
    check()

# GC854 ADDENDUM: prediction registered in the ledger before the new count.
# Third equation should fix some falling bits, but leave an independent cube.
# Counterfactual that all121 remain free must fail. Exact outcome:56 free,65 fixed.
def check_third():
    row = [(R >> i) & 1 for i in range(N)]
    V = [[] for _ in row]
    for _ in range(P):
        for i, b in enumerate(row):
            V[i].append(b)
        row = [row[i] ^ (row[(i+1) % N] | row[(i+2) % N]) for i in range(N)]
    for i in range(N):
        X, Y, Z = V[i], V[(i+1) % N], V[(i+2) % N]
        falls = {t for t in range(P) if Y[t] == 1 and Y[(t+1) % P] == 0}
        free = {t for t in falls if Z[(t+1) % P] == 1 and
                (Y[(t-1) % P] == 1 or Z[(t-1) % P] == 1)}
        assert len(falls) == 121 and len(free) == 56
        assert all(Z[t] == 1 for t in falls - free)
        choices = [{0, 1} if t in free else {Z[t]} for t in range(P)]
        # Every local combination of surviving bits has a literal W,Q witness.
        # This checks the whole cube without enumerating2^56 complete words.
        for t in range(P):
            dy = Y[t] ^ Y[(t+1) % P]
            for z, zn in product(choices[t], choices[(t+1) % P]):
                literal = any(dy == (z | w) and (z ^ zn) == (w | q)
                              for w, q in product((0, 1), repeat=2))
                assert literal
        # Each removed bit's zero choice fails at its tick or the preceding one.
        for t in falls - free:
            bad = Z[:]
            bad[t] = 0
            assert any(not any((Y[s] ^ Y[(s+1) % P]) == (bad[s] | w)
                               and (bad[s] ^ bad[(s+1) % P]) == (w | q)
                               for w, q in product((0, 1), repeat=2))
                       for s in ((t-1) % P, t))
    print('GC854 PASS:56 independent bits survive three edges;65 forced; literal witnesses checked')

if __name__ == '__main__':
    check_third()
