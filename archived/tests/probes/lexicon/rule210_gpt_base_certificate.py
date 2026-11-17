"""GC467 independent finite base leaf for L274, not a deeper CL census.
P1: exactly R survives the full centre clock through depth121.
C0: scalar list evolution agrees for every 8-bit seed, times0..8.
CF0: calling depth120 unique must fail (two survivors expected).
Unexpected C1: distant tail alterations leave centre times0..121 unchanged.
REFUTED-BY: any differing prefix, scalar mismatch or tail influence.
OUTCOME: P1 HELD; C0 PASS256; CF0 rejected with2 depth120 survivors;
unexpected C1 PASS3. Full causal cone argument is GC467, not these samples.
"""
from math import gcd
D=121
OFF=D+2
WIDTH=2*D+5
MASK=(1<<WIDTH)-1

def step(row):
    planes=(row<<1,row,row>>1)
    out=0
    for code in range(8):
        if (210>>code)&1:
            term=MASK
            for plane,k in zip(planes,(2,1,0)):
                term &= plane if (code>>k)&1 else MASK^plane
            out |= term
    return out&MASK

def trace(seed,depth,tail=0):
    row=(seed<<(OFF+1))|tail
    result=[]
    for t in range(depth+1):
        result.append((row>>OFF)&1)
        row=step(row)
    return result

def scalar(seed,depth):
    row={i+1:(seed>>i)&1 for i in range(depth)}
    result=[]
    for t in range(depth+1):
        result.append(row.get(0,0))
        row={i: row.get(i-1,0)^((1-row.get(i,0))*row.get(i+1,0))
             for i in range(-depth,depth+1)}
    return result

if __name__=='__main__':
    for seed in range(256):
        assert trace(seed,8)==scalar(seed,8)
    alive=[0];counts={}
    for d in range(1,D+1):
        alive=[p|(v<<(d-1)) for p in alive for v in (0,1)
               if trace(p|(v<<(d-1)),d)==[t%2 for t in range(d+1)]]
        counts[d]=len(alive)
    R=sum(1<<(i-1) for i in range(1,D+1) if gcd(i,6)==1)
    assert alive==[R]
    assert counts[120]==2  # CF0: threshold120 is not yet unique.
    tails=[0,1<<(OFF+D+1),((1<<WIDTH)-1)^((1<<(OFF+D+1))-1)]
    for tail in tails:
        assert trace(R,D,tail)==trace(R,D)
    print('PASS unique base121; depth120 survivors',counts[120],
          '; scalar controls256; distant-tail controls',len(tails))
