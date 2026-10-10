#!/usr/bin/env python3
"""GC926 fixed physical continuation; no tree or peer implementation imports.
Record search and predictions in CLOUD-LOCAL, 2026-10-10 02:30 BST.
P1 target old8 source00101100 absorbs at400 and old clocks coalesce.
P2 blind: both period16 children re-coalesce within6 edges from (0,c).
C0 old4 source1101 absorbs29 and period8 children coalesce at lag6.
CF a flipped child bit fails the integration equation.
U paired root phases phi and phi+q retain absolute separationq even
when the clocks coalesce moduloq; no absolute equality inference.
Caps: 401 backward steps, 64 continuation edges, q<=16, one CPU.
FIRST EXECUTION: C0 entry-lag6 assertion FAILED, so target NOT RUN.
Diagnostic control1101: both entry lags7, counts2 until lag7 then1.
ADDENDUM 02:31 BST: check original GC922 source1011 gives entry lag7,
which is CL142's lag6 after the first doubled reset. P2 unchanged.
OUTCOME 02:32 BST: P1 held (absorption400, old residue5); P2 REFUTED:
both target entry lags29 (28 after first reset), two residues until then.
C0 original failed; C0 aligned held for1101 and original1011 (entry7,
after-first-reset6). CF and U held, absolute paired gaps8/16.
RETROSPECTIVE RECORD CONNECTION: target last reset uses driver depth429,
matching G6.3 SF2's existing first persistent coalescence at diagonal429.
This connection was missed in preflight; result is an independent fixed
reproduction/calibration, not new coalescence evidence or a new route.
Full-line only, no birth/run census.
"""
import json

def audit(source, depth):
    m=len(source);q=2*m
    a=list(map(int,source*2));zero=[0]*q
    shift=lambda v:v[1:]+v[:1]
    def back(pair):
        x,y=pair
        return ([s^(u|v) for s,u,v in zip(shift(y),x,y)],x[:])
    pair=(a,zero);ancestry=[pair]
    for _ in range(401):
        if not any(pair[0]+pair[1]):break
        pair=back(pair);ancestry.append(pair)
    else:raise RuntimeError('incomplete ancestry')
    assert len(ancestry)-1==depth
    path=list(reversed(ancestry[:-1]))
    assert path[0]==(zero,[1]*q)
    def check(x,y,z):
        return all(z[(t+1)%q]==x[t]^(y[t]|z[t]) for t in range(q))
    for (x,y),(y2,z) in zip(path,path[1:]):
        assert y==y2 and check(x,y,z)
    def reset(w,t):
        if not any(w):return t
        r=t
        while not w[r%q]:r+=1
        # independent finite list lookup control
        assert r-t==next(k for k in range(q) if w[(t+k)%q])
        return r+1
    clocks=list(range(2*q))
    for x,y in path[:-1]:clocks=[reset(y,t) for t in clocks]
    assert len({t%m for t in clocks})==1
    assert all(a[(t-1)%q] for t in clocks)
    def child(x,y):
        solutions=[]
        for initial in (0,1):
            z=[initial]
            for t in range(q):z.append(x[t]^(y[t]|z[-1]))
            if z.pop()==initial:solutions.append(z)
        assert len(solutions)==1
        return solutions[0]
    outcomes=[]
    for first in (0,1):
        c=[first]
        for bit in a:c.append(c[-1]^bit)
        assert c.pop()==first and check(a,zero,c)
        bad=c[:];bad[0]^=1
        assert not check(a,zero,bad)
        x,y=zero,c
        times=clocks[:];counts=[len({t%q for t in times})];lag=None
        for edge in range(1,65):
            z=child(x,y)
            assert check(x,y,z)
            times=[reset(y,t) for t in times]
            assert all(times[i+q]-times[i]==q for i in range(q))
            x,y=y,z
            counts.append(len({t%q for t in times}))
            if counts[-1]==1:
                lag=edge
                break
        outcomes.append(dict(child=''.join(map(str,c)),first_singleton_lag=lag,
                             residue_counts=counts,absolute_pair_gap=q))
    return dict(source=source,absorption=depth,old_residues=sorted({t%m for t in clocks}),
                branches=outcomes)

if __name__=='__main__':
    control=audit('1101',29)
    assert all(b['first_singleton_lag']==7 for b in control['branches'])
    original=audit('1011',29)
    assert all(b['first_singleton_lag']==7 for b in original['branches'])
    target=audit('00101100',400)
    p2=all(b['first_singleton_lag'] is not None and b['first_singleton_lag']<=6
           for b in target['branches'])
    print(json.dumps(dict(P1=True,P2=p2,C0_original=False,C0_aligned=True,CF=True,U=True,
                         control=control,original_fixture=original,target=target),indent=2))
