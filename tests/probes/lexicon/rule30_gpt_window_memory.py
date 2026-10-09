#!/usr/bin/env python3
"""GC780: a width-two future block retains dependence beyond the row cutoff.

Registered before this fixed 256-word replay; no random or single-seed run.
WM0 control: W0=(x0(0),x0(1)) and W2=(x2(0),x2(1)) have all
    16 joint states exactly 16 times over initial words on [-3,4].
WM1 predicted hand identity: E[S0(0)*S2(0)*S3(1)] = 1/8,
    S=(-1)^x. Its integer sum must be 32 over 256 words.
WM2 known-wrong counterfactual: independence of W0 from (W2,W3)
    forces that third moment to be zero; must fail.
Unexpected WM3 control: the fixed-column triple S0(0),S2(0),S3(0)
    has third moment zero, consistent with reviewed G97 iid columns.
REFUTED-BY: WM0 failure or a replay disagreement with WM1/WM3.
OUTCOME: NOT RUN.
"""
from collections import Counter
from itertools import product


def samples(bits):
    row = dict(zip(range(-3,5),bits))
    out = {0: (row[0],row[1])}
    for t in range(1,4):
        row = {i: row[i-1] ^ (row[i] | row[i+1])
               for i in range(-3+t,5-t)}
        out[t] = (row[0],row[1])
    return out


def main():
    pairs = Counter()
    mixed = fixed = 0
    for bits in product((0,1),repeat=8):
        out = samples(bits)
        pairs[(out[0],out[2])] += 1
        s0 = 1-2*out[0][0]
        s2 = 1-2*out[2][0]
        mixed += s0*s2*(1-2*out[3][1])
        fixed += s0*s2*(1-2*out[3][0])
    assert len(pairs)==16 and set(pairs.values())=={16}, 'WM0'
    assert mixed==32, 'WM1'
    assert mixed!=0, 'WM2 must fail'
    assert fixed==0, 'WM3'
    print('WM0 PASS: 16 joint states, each 16/256')
    print('WM1 PASS: mixed third moment 32/256 = 1/8')
    print('WM2 REFUTED as required; WM3 PASS: fixed triple sum 0/256')


if __name__=='__main__':
    main()
