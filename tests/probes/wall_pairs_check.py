#!/usr/bin/env python3
"""Check of L1528's hand relations on random rows: y(11) = not b, y(11) or y(12) = 1, and the pair rule read from (y(12), y(13)) one tick deeper."""
import random
random.seed(9)
W=900
def inv(y):
    x=y&1; p1=1; p2=0
    for j in range(1,W):
        o=((y>>j)&1)^(p1|p2); x|=o<<j; p2=p1; p1=o
    return x
def top(x):
    e=(~(x^(x>>1)))&((1<<(W-2))-1)&~1
    return e.bit_length()-1
A=(1,1,0,0,0,1,1,1,1,0,0); B=(1,1,0,0,0,1,1,1,0,1,0)   # by offset k = 0..10
def off(x,d,k): return (x>>(d+1-k))&1
tests=0; bad=0; tally={}
for r in range(400):
    low=40
    x=1|(random.getrandbits(low-1)<<1); b=(x>>(low-1))&1
    for j in range(low,W):
        b^=1
        if b: x|=1<<j
    prev=None
    for t in range(120):
        d=top(x); win=tuple(off(x,d,k) for k in range(11))
        L='A' if win==A else 'B' if win==B else None
        if L:
            bit=1 if L=='B' else 0
            y11,y12,y13=off(x,d,11),off(x,d,12),off(x,d,13)
            tests+=1
            if prev and y11!=1-bit: bad+=1
            if prev and (y11|y12)!=1: bad+=1
            if prev:
                key=(L,prev,y12,y13); tally[key]=tally.get(key,0)+1
                want={('A','A'):[(0,0)],('A','B'):[(1,0),(0,1)],('B','A'):[(1,1)]}[(L,prev)]
                if (y12,y13) not in want: bad+=1
        prev=L
        x=inv(x)
print('ticks tested',tests,'violations',bad); print(sorted(tally.items()))
