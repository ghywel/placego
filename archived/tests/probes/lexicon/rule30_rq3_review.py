#!/usr/bin/env python3
"""Targeted independent RQ3 witness audit; no Local imports or graph traversal.
Known expectations before execution: q8 aligned edge (183,176)->(133,208),
delay5, feature(1,5,1,8), depths190/191, target absolute arrival365
from root clock0. Reconstruct unique absolute-word ancestry backwards.
Unexpected check: carry every root residue, not just the reported clock0.
Counterfactual: toggling one source bit must break the edge recurrence.
This does not verify the full census or q4 quotient feasibility.
"""
import time
import resource

q=8
mask=(1<<q)-1

def bit(w,t): return (w>>(t%q))&1

def rotate(w,d): return sum(bit(w,t+d)<<t for t in range(q))

def D(w,t):
    return 0 if w==0 else next(j+1 for j in range(q) if bit(w,t+j))

def compatible(a,b,c):
    return all(bit(c,t+1)==(bit(a,t)^(bit(b,t)|bit(c,t))) for t in range(q))

def feat(a,b,t):
    p=next(d for d in (1,2,4,8) if rotate(a,d)==a and rotate(b,d)==b)
    return (D(a,t),D(b,t),D(a^b,t),p)

t0=time.process_time()
source=(183,176)
aligned_target=(133,208)
delay=5
assert rotate(source[1],delay)==aligned_target[0]
c=rotate(aligned_target[1],-delay)
assert compatible(*source,c)
assert not compatible(source[0]^1,source[1],c)
assert D(source[1],0)==delay
assert feat(*source,0)==feat(source[1],c,delay)==(1,5,1,8)
assert bit(source[0],-1)==bit(source[1],delay-1)==1
pair=source
back=[pair]
while pair!=(0,mask):
    assert len(back)<=191, 'reported depth190 not reconstructed'
    a,b=pair
    pair=(sum((bit(b,t+1)^(bit(a,t)|bit(b,t)))<<t for t in range(q)),a)
    back.append(pair)
path=back[::-1]
assert len(path)-1==190
path.append((source[1],c))
for (a,b),(bb,cc) in zip(path,path[1:]):
    assert b==bb and compatible(a,b,cc)
arrivals=[]
for start in range(q):
    clock=start
    source_clock=None
    for depth,(a,b) in enumerate(path[:-1]):
        if depth==190: source_clock=clock
        clock+=D(b,clock)
    arrivals.append((source_clock,clock))
assert arrivals[0]==(360,365)
assert rotate(path[190][0],360)==source[0]
assert rotate(path[190][1],360)==source[1]
assert (rotate(path[191][0],365),rotate(path[191][1],365))==aligned_target
print('RQ3 scalar ancestry/compatibility/root-clock/features/counterfactual PASS')
print('unaligned child',c,'root residues source/target arrivals',arrivals)
print('depths190/191, delay5, reward5, identical features(1,5,1,8)')
print('CPU %.4f s, RSS %.1f MiB'%(time.process_time()-t0,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576))
