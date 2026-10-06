#!/usr/bin/env python3
"""G63 ST1-ST2 published at7eb8431 before this run.
ST1 MUST:7 disjoint-phase pairs,256 R words, times0..7;
C and R updates admit a farther stream => forcing on times2..5.
ST2 MUST: both period-six patterns,60 columns, disjoint phases.
CF MUST FAIL: forcing holds without temporal margins, using the
published L=00,C=10,R=[1,1,0,1,0,1,0,1] local boundary guard.
No blind predictions. A farther stream need not itself evolve.
"""
from itertools import product


def f(l,c,r):return (210>>(4*l+2*c+r))&1


def allowed(L,C,R):
    for t in range(7):
        if f(L[t%2],C[t%2],R[t])!=C[(t+1)%2]:return False
        if not any(f(C[t%2],R[t],z)==R[t+1] for z in (0,1)):return False
    return True


def main():
    phases=((0,0),(1,0),(0,1))
    tested=accepted=pairs=0
    for L,C in product(phases,repeat=2):
        if any(l*c for l,c in zip(L,C)):continue
        pairs+=1
        want=(C[1]^L[0],C[0]^L[1])
        for R in product((0,1),repeat=8):
            tested+=1
            if not allowed(L,C,R):continue
            accepted+=1
            assert all(R[t]==want[t%2] for t in range(2,6))
    assert pairs==7
    for a,period in ((0,((0,1),(0,0),(0,1),(1,0),(0,0),(1,0))),
                     (1,((0,1),(1,0),(0,0),(1,0),(0,1),(0,0)))):
        seq=[(0,1),(a,0)]
        while len(seq)<60:
            L,C=seq[-2:]
            seq.append((C[1]^L[0],C[0]^L[1]))
        assert all(v==period[i%6] for i,v in enumerate(seq))
        assert all(not any(l*c for l,c in zip(seq[i],seq[i+1])) for i in range(59))
    R=(1,1,0,1,0,1,0,1)
    assert allowed((0,0),(1,0),R) and R[0]!=0
    print('ST1 PASS:',pairs,'phase pairs;',tested,'words;',accepted,'accepted')
    print('ST2 PASS:2 patterns,120 column phases,118 adjacent pairs')
    print('CF REFUTED:accepted boundary guard differs at time0')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: ST1 PASS7 pairs/1792 words/15 accepted; ST2
# PASS120 phases/118 adjacent pairs; no-margin CF REFUTED.
