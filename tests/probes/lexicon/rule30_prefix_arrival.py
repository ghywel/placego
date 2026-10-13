#!/usr/bin/env python3
"""A one-step-behind defect identity explains L651's failed prefix repetition.

RUN-ON: cpu, standard-library Python; no survivor census or solver.
COMMAND: python3 tests/probes/lexicon/rule30_prefix_arrival.py

Record searched: black.run|birth.excess|beta with 8.82|CL215|three.shape
->8 hits6files; first.*difference|difference.*front|perturb.*front|one.off|
second.*arrival with diagonal|XOR|parity|charge|pivot ->43 hits13files.
Read8.82, G18.4/G25, GC1166 and Local's jump source. This is an extension
of the known extreme-path pivot, not a new horizon engine.

PREDICTIONS, before the first execution (2026-10-13):
 P1: if two initial rows first differ at depth k, their wall-neighbour
     difference at tick k equals their initial difference at k+1 XOR
     (k mod2) XOR the baseline diagonal sum x_t(k-t-1), t=0..k-1.
 P2: for both L651 cores behind one P20, this diagonal sum at k=34 is1.
     Adding a second P20 therefore flips the black check at tick34.
 CF: flipping the new depth35 bit from0 to1 restores that check; no
     implication about later checks is predicted.
 Unexpected control: recover the standard-phase predecessor of each
     successful black-phase record. Predict its long zero band is born
     from a black/P shape, not a long parent zero band (8.82).
 Independent controls: literal Wolfram-table forward updates, the defect
 identity, and spatial left-parent reconstruction; short rows use both
 wall phases, both original depth-k bits, both depth-(k+1) differences,
 and two farther tails. Fixed controls stop at tick34, not at a horizon.

OUTCOME (2026-10-13): P1 held in2016 literal short controls. P2 held
for both named cores: charge1, failure at34. CF held: depth35=1 restores
that check. Unexpected control held: both choices of parent depth1 give
the P shape 1 at31, 0 at32, ones33..67, 0 at68. General far-tail
independence follows from the cone and the proved identity, not a scan.
"""
from itertools import product

P20 = "10011100101110100100"
CORES = ("10111010101", "10111100011")


def seed(word):
    return {j: int(b) for j, b in enumerate(reversed(word), 1)}


def evolution(a, phase, ticks):
    """Literal rule table; increasing depth points to the spatial left."""
    rows = [dict(a)]
    width = max(a, default=0)
    for t in range(ticks):
        x = rows[-1]
        row = {}
        for j in range(1, width + t + 2):
            left, me = x.get(j+1, 0), x.get(j, 0)
            right = (phase+t) % 2 if j == 1 else x.get(j-1, 0)
            row[j] = (30 >> (4*left + 2*me + right)) & 1
        rows.append(row)
    return rows


def charge(rows, phase, k):
    q = 0
    for t in range(k):
        j = k-t-1
        q ^= rows[t].get(j, 0) if j else (phase+t) % 2
    return q


def neighbour_difference_check(a, b, phase, k):
    ra, rb = evolution(a, phase, k), evolution(b, phase, k)
    assert all(ra[t].get(1, 0) == rb[t].get(1, 0) for t in range(k-1))
    assert ra[k-1].get(1, 0) ^ rb[k-1].get(1, 0) == 1
    expected = a.get(k+1, 0) ^ b.get(k+1, 0) ^ (k % 2) ^ charge(ra, phase, k)
    assert ra[k].get(1, 0) ^ rb[k].get(1, 0) == expected


def main():
    n = 0
    for k in range(1, 7):
        for bits in product((0, 1), repeat=k+1):
            a = {j: bits[j-1] for j in range(1, k+2)}
            for phase, dn, far in product((0, 1), repeat=3):
                b = dict(a)
                b[k] ^= 1
                b[k+1] ^= dn
                b[k+2] = far
                b[k+4] = 1-far
                neighbour_difference_check(a, b, phase, k)
                n += 1
    print("P1 short independent literal controls:", n, "PASS")

    for c in CORES:
        a = seed(P20+c)
        rows = evolution(a, 1, 34)
        assert all(rows[t].get(1, 0) == 1 for t in range(0, 35, 2))
        q = charge(rows, 1, 34)
        assert q == 1
        # Only the first two new arrivals are relevant at tick34.
        b = dict(a); b[34] = 1; b[35] = 0
        neighbour_difference_check(a, b, 1, 34)
        bad = evolution(b, 1, 34)
        assert bad[34][1] == 0
        b[35] = 1
        assert evolution(b, 1, 34)[34][1] == 1

        # GC1166 completion fixes the record's first black endpoint,67.
        z = dict(a); z[67] = 1
        parents = []
        for u in (0, 1):
            x = {0: 0, 1: u}
            for j in range(1, 68):
                x[j+1] = z.get(j, 0) ^ (x[j] | x[j-1])
            image = evolution({j: x[j] for j in range(1, 69)}, 0, 1)[1]
            assert all(image[j] == z.get(j, 0) for j in range(1, 68))
            shape = "zero" if not x[31] and not x[32] else ("P" if x[31] and not x[32] else "black")
            assert shape != "zero"
            assert all(x[j] == 1 for j in range(33, 68))
            assert x[68] == 0
            parents.append((u, shape, x[31], x[32]))
        print("core", c, "k34 charge", q, "tick34 failure/countercontrol PASS; parents", parents)
    print("ALL CHECKS PASS; no general deadline or prefix-pumping claim")


if __name__ == "__main__":
    main()
