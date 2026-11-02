#!/usr/bin/env python3
"""GC2394: small exact coordinate check, not a closure search.

Prediction: legacy (t mod q, A mod N) loses lab-background phase when the
ring's q-shift is not a spatial symmetry; G8/classic/s7_63 hide this because
N divides q. The corrected state (t mod q, (t-A+r) mod N) works in all four.
Counterfactual: if s9_57's actual row were invariant under shift q, no mismatch.
Controls: literal ring update; every phase of lcm(N,q); stay/retreat moves;
direct lab-rule comparison. No trajectory or alignment census is performed.
"""
from math import lcm

WORDS = {'G8': '1000', 'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000'}
for name, word in WORDS.items():
    seed = tuple(map(int, word))
    n = len(seed)
    orbit = [seed]
    while True:
        row = orbit[-1]
        nxt = tuple(row[j] ^ (row[(j-1) % n] | row[(j-2) % n]) for j in range(n))
        if nxt == seed:
            break
        assert nxt not in orbit, 'Seed not on a pure cycle'
        assert len(orbit) < 1000, 'Fixed small-control stop'
        orbit.append(nxt)
    q = len(orbit)

    def actual(x, t, r=0, s=0):
        return orbit[(t+s) % q][(t-x+r) % n]

    witness = None
    for t in range(lcm(n, q)):
        tau, anchor, r, s = t % q, -3, 2, 1
        h = (t-anchor+r) % n
        for i in range(-1, n+1):
            old = orbit[(tau+s) % q][(tau-(anchor % n+i)+r) % n]
            true = actual(anchor+i, t, r, s)
            if old != true and witness is None:
                witness = (t, anchor+i, old, true)
            assert orbit[(tau+s) % q][(h-i) % n] == true
            assert actual(anchor+i, t+1, r, s) == (
                actual(anchor+i-1, t, r, s) ^
                (actual(anchor+i, t, r, s) | actual(anchor+i+1, t, r, s)))
            for motion in (-1, 0):
                hnext = (h+1-motion) % n
                assert orbit[(tau+1+s) % q][(hnext-i) % n] == actual(anchor+motion+i, t+1, r, s)
    assert (witness is None) == (name != 's9_57')
    # Exact driver start time, r=s=A=0, independent of graph or long simulation.
    start = [(i, orbit[300 % q][(300 % q-i) % n], actual(i, 300))
             for i in range(n)
             if orbit[300 % q][(300 % q-i) % n] != actual(i, 300)]
    print(f'{name}: N={n}, q={q}, legacy witness={witness}; t0=300 mismatches={start}; corrected phase/control PASS')
print('ANCHOR_PHASE_CHECK_DONE')
