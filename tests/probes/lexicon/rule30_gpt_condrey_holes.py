#!/usr/bin/env python3
"""G11: audit the constant-wall mechanism and first-hole prefix analytically.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_condrey_holes.py
RUN-ON: GPT Intel CPU, one process, Python 3.10+ standard library.
COST: seconds; scalar checks only, no duplicate of Local's holes records.
PREDICTIONS before first run, 2026-10-06:
 CH0 control: constant-one forced left row is0,1,0,1,... independently
     of sigma. Constant-zero right-neighbour update is sigma OR right2;
     constant-one update is its complement, not a monotone latch.
 CH1 theorem control: at a hole of the word0 1^(p-1), the first p-1
     left cells are the truncation of [h,h,1-h,1,0,1,0,1,...], where
     h=1-sigma(hole). Test p3..64, four hole times,32 seeded sigma lists.
 CH2 theorem control: p>=5 forces a black cell at depth2*floor((p-1)/2),
     hence a left support radius smaller than that cannot realize the wall.
 CH3 control: first-hole witness p4,sigma0=1 has left prefix[0,0,1].
     The finite row with ones at-3 and1 has trace01110 through time4.
 CH4 unexpected check: p2,sigma0=1 has prefix[0,1], unlike p4's[0,0].
     Lower freedom does not order fixed-depth zero-run records pointwise.
 CF must reject: the first hole preserves the constant-one universal
     checkerboard. Its first three cells differ in CH3.
 REFUTED-BY: any theorem/scalar/finite-row check fails or CF not rejected.
 No blind asymptotic bound and no LR proof are asserted by this diagnostic.
"""
import random


def forced_columns(tau,sigma,depth):
    cols=[sigma[:],tau[:]]
    for j in range(depth):
        a,b=cols[-1],cols[-2]
        cols.append([a[t+1] ^ (a[t] | b[t]) for t in range(len(a)-1)])
    return cols[2:]


def prefix(h,n):
    return [h if j<=2 else 1-h if j==3 else int(j%2==0)
            for j in range(1,n+1)]


def finite_trace(ones,steps):
    row=set(ones);trace=[]
    for t in range(steps+1):
        trace.append(int(0 in row))
        if not row:continue
        row={i for i in range(min(row)-1,max(row)+2)
             if (int(i-1 in row) ^ (int(i in row) | int(i+1 in row)))}
    return trace


def main():
    rng=random.Random(2026100611);checks=0
    for _ in range(32):
        sigma=[rng.randrange(2) for _ in range(130)]
        cols=forced_columns([1]*130,sigma,64)
        assert [c[0] for c in cols]==[int(j%2==0) for j in range(1,65)]
    for s in [0,1]:
        for r in [0,1]:
            assert (0 ^ (s|r))>=s
            assert (1 ^ (s|r))==1-(s|r)
    print('PASS CH0: constant-one fibre and distinct zero/one boundary updates',flush=True)
    for p in range(3,65):
        n=6*p+3;tau=[int(t%p!=0) for t in range(n)]
        for _ in range(32):
            sigma=[rng.randrange(2) for _ in range(n)]
            cols=forced_columns(tau,sigma,p-1)
            for t in [0,p,2*p,3*p]:
                actual=[c[t] for c in cols];expected=prefix(1-sigma[t],p-1)
                assert actual==expected,(p,t,actual,expected)
                if p>=5:assert actual[2*((p-1)//2)-1]==1
                checks+=1
    print('PASS CH1/CH2: %d whole-prefix comparisons at p3..64; support obstruction p>=5'%checks,flush=True)
    tau=[int(t%4!=0) for t in range(12)];sigma=[1]+[0]*11
    witness=[c[0] for c in forced_columns(tau,sigma,3)]
    assert witness==[0,0,1]
    trace=finite_trace({-3,1},4);assert trace==[0,1,1,1,0]
    print('PASS CH3: p4 left[0,0,1]; finite seed ones(-3,1) trace01110',flush=True)
    tau2=[int(t%2!=0) for t in range(12)]
    two=[c[0] for c in forced_columns(tau2,sigma,2)]
    assert two==[0,1] and witness[:2]==[0,0]
    print('PASS CH4 unexpected: p2 cannot start with two zeros; p4 can',flush=True)
    assert witness!=[0,1,0]
    print('PASS CF rejected: first hole breaks the universal checkerboard',flush=True)
    print('ALL CONTROLS PASS',flush=True)


if __name__=='__main__':main()
