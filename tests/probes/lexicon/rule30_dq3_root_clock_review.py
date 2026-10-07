#!/usr/bin/env python3
"""Targeted scalar scope audit of DQ3's q4 witness; no tree/quotient job.
Before execution: expected ancestry length10 to constant-one root(0,15),
all four root start phases arrive at witness phase1 with absolute times
9,13,13,13. Unexpected guard: word rootedness does not give phase0 reach.
Counterfactual: phase0 passes the gate but is absent from those arrivals.
"""
def bit(w,t): return (w>>(t%4))&1

def D(w,r):
    if not w: return 0
    return next(j+1 for j in range(4) if bit(w,r+j))

def feat(a,b,r): return (D(a,r),D(b,r),D(a^b,r))

pair=(15,12); backwards=[pair]
while pair!=(0,15):
    assert len(backwards)<=16
    a,b=pair
    pair=(sum((bit(b,t+1)^(bit(a,t)|bit(b,t)))<<t for t in range(4)),a)
    backwards.append(pair)
path=backwards[::-1]
assert len(path)-1==10
for (a,b),(bb,c) in zip(path,path[1:]):
    assert b==bb
    assert all(bit(c,t+1)==(bit(a,t)^(bit(b,t)|bit(c,t))) for t in range(4))
arrivals=[]
for start in range(4):
    clock=start
    for a,b in path[:-1]: clock+=D(b,clock)
    arrivals.append(clock)
assert arrivals==[9,13,13,13]
assert all(t%4==1 for t in arrivals)
assert bit(15,-1)==1 and feat(15,12,0)==feat(12,2,3)==(1,3,1)
assert feat(15,12,1)==(1,2,1) and D(12,1)==2
print('scalar ancestry/forward compatibility/root clock/feature scope PASS')
print('path=',path,'arrivals=',arrivals)
