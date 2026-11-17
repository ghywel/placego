#!/usr/bin/env python3
"""GC773: independent finite audit of CL078's first three diagonal correlations.

Predictions before this fixed128-word replay (no random/single-seed scan):
DM0 control: each lag's output is fair; flipping the leading input flips
    every observed diagonal spin (left-permutivity control).
DM1 expected replay, not blind: rho1=-1/2, rho2=1/4, rho3=-1/4.
DM2 known-wrong counterfactual: rho3=rho1**3=-1/8 (must fail).
Unexpected check: rho2=rho1**2 holds despite DM2 failing.
REFUTED-BY: DM0 failure or a replay disagreement with DM1.
OUTCOME (2026-10-09, GPT): DM0/DM1 PASS on128 equally weighted
initial7-bit words. rho1=-1/2, rho2=1/4, rho3=-1/4. DM2 REFUTED
as required, since -1/4 != -1/8; unexpected rho2 equality HELD.
"""
from fractions import Fraction
from itertools import product


def diagonal(word):
    row = list(word)
    spins = [1-2*row[0]]
    for _ in range(3):
        row = [row[i] ^ (row[i+1] | row[i+2]) for i in range(len(row)-2)]
        spins.append(1-2*row[0])
    return spins


def main():
    sums = [0]*4
    marginals = [0]*4
    for word in product((0,1), repeat=7):
        z = diagonal(word)
        other = diagonal((1-word[0],)+word[1:])
        assert other == [-v for v in z], 'DM0 leading-bit symmetry'
        for k in range(4):
            sums[k] += z[0]*z[k]
            marginals[k] += z[k]
    assert marginals == [0]*4, 'DM0 fairness'
    rho = [Fraction(s,128) for s in sums]
    assert rho[1:] == [Fraction(-1,2), Fraction(1,4), Fraction(-1,4)], 'DM1'
    assert rho[2] == rho[1]**2
    assert rho[3] != rho[1]**3, 'DM2 counterfactual failed to fail'
    print('DM0/DM1 PASS; rho1..3:', rho[1:])
    print('DM2 REFUTED as required:', rho[3], '!=', rho[1]**3)
    print('unexpected rho2 equality:',rho[2])


if __name__ == '__main__':
    main()
