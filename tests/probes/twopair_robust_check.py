#!/usr/bin/env python3
"""L1521 control for the robust backward front: literal 2-adic rows, not the window program. Every window of B_11 sits on random lower bits with rain above;
the top must rise by exactly 3 at each of 100 backward ticks. Negative control: how many other windows fail on random rows. A window outside B_11 may still be robust in truth: B_11 is what a window of 11 cells can certify."""
import random
random.seed(20261104)
W=400
def inv(y):
    x=y&1; p1=1; p2=0
    for j in range(1,W):
        o=((y>>j)&1)^(p1|p2); x|=o<<j; p2=p1; p1=o
    return x
def phi(x): return (x^((x<<1)|(x<<2)))&((1<<W)-1)
def top(x):
    e=(~(x^(x>>1)))&((1<<(W-2))-1)&~1
    return e.bit_length()-1
def row(win,w,low):
    """low random bits (bit 0 black), then the window, then rain"""
    x=1|(random.getrandbits(low-1)<<1)
    for i in range(w):
        if (win>>i)&1: x|=1<<(low+i)
    b=(win>>(w-1))&1
    for j in range(low+w,W):
        b^=1
        if b: x|=1<<j
    return x
w=11
B=[int(l) for l in open('twopair_B11.txt')]
full=lambda m: m|(((m>>(w-2))&1)<<(w-1))
print('B_11 windows (low to high):')
for m in sorted(B):
    print('  ',''.join('#' if (full(m)>>i)&1 else '.' for i in range(w)))
fails=0; trials=0
for m in B:
    for rep in range(400):
        low=random.randint(3,40)
        x=row(full(m),w,low); d=top(x); assert d==low+w-2
        y=x
        for t in range(100):
            z=inv(y); assert phi(z)==y
            dz=top(z); trials+=1
            if dz!=d+3: fails+=1; break
            d=dz; y=z
print('positive control: ticks tested',trials,'failures',fails)
bad=[]; allw=0
Bset=set(m&((1<<(w-1))-1) for m in B)
W=200
for m in range(1<<(w-1)):
    if m in Bset: continue
    allw+=1; broke=False
    for rep in range(3000):
        low=random.randint(3,40)
        x=row(full(m),w,low); d=top(x); y=x
        for t in range(40):
            z=inv(y); dz=top(z)
            if dz!=d+3: broke=True; break
            d=dz; y=z
        if broke: break
    if not broke: bad.append(m)
print('negative control: windows outside B_11',allw,'that never failed in 3000 random rows',len(bad))
still=[]
for m in bad:
    broke=False
    for rep in range(20000):
        low=random.randint(3,24)
        x=row(full(m),w,low); d=top(x); y=x
        for t in range(14):
            z=inv(y); dz=top(z)
            if dz!=d+3: broke=True; break
            d=dz; y=z
        if broke: break
    if not broke: still.append(m)
    print('  ',''.join('#' if (full(m)>>i)&1 else '.' for i in range(w)),('failed after %d rows'%(rep+1)) if broke else 'did not fail in 20000 rows',flush=True)
print('windows outside B_11 never seen to fail:',len(still))
