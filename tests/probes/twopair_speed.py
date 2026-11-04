#!/usr/bin/env python3
"""Forward top speed of a cloud in the rain, in depth per tick, for a few small clouds, against the white-background left edge of chaos."""
import time
def rain_extend(x,w,W):
    b=(x>>(w-1))&1
    for j in range(w,W):
        b^=1
        if b: x|=1<<j
    return x
T=6000; W=4*T+200; M=(1<<W)-1
def top(x):
    e=(~(x^(x>>1)))&((1<<(W-2))-1)&~1
    return e.bit_length()-1
for name,start,w in (('defect',0b1,3),('core',int('111011110101'[::-1],2),12),('x=11',0b1011,6),('x=0b100111',0b100111,8)):
    x=rain_extend(start,w,W); pts=[]
    for t in range(T+1):
        if t in (500,1000,2000,3000,4000,5000,6000): pts.append((t,top(x)))
        x=(x^((x<<1)|(x<<2)))&M
    print(name,pts,'slope late',round((pts[-1][1]-pts[1][1])/(pts[-1][0]-pts[1][0]),4),flush=True)
