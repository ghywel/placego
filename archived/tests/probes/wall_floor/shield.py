#!/usr/bin/env python3
"""shield.py (Local, L1532): how the lower state travels up a row. For a window read from its low end, the set of possible states after each cell, starting from all four. A merge is a set of one state.
Printed for the four windows of the lock and for the three phases of the quiet AAB layer."""
import json,random
from locklib import *
def states(win):
    """win low..high; then rain. Returns list of (cell, sorted states after reading it)"""
    S={(0,0),(0,1),(1,0),(1,1)}; out=[]
    inp=list(win); b=inp[-1]
    for i in range(6):
        b^=1; inp.append(b)
    for c in inp:
        T=set()
        for (p1,p2) in S:
            o=c^(p1|p2); T.add((o,p1))
        S=T; out.append((c,sorted(S)))
    return out
def show(win,name):
    r=states(win)
    s=''.join('#' if c else '.' for c,_ in r)
    n=''.join(str(len(S)) for _,S in r)
    print(f'{name}\n  {s}\n  {n}')
S45=json.load(open('lock45.json'))
for i,v in enumerate(S45): show(v,f'lock window {i}')
# the quiet AAB layer
random.seed(5)
low=40
x=1|(random.getrandbits(low-1)<<1); b=(x>>(low-1))&1
for j in range(low,W):
    b^=1
    if b: x|=1<<j
y=x
for t in range(600): y=inv(y)
rows=[]
for t in range(12):
    rows.append(y); y=inv(y)
for i,r in enumerate(rows[:6]):
    d=top(r); L=letter(window(r,11,d))
    show(window(r,64,d),f'AAB row, letter {L}')
