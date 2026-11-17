#!/usr/bin/env python3
"""Robust backward front. A window is the w bits just below and including the top wall pair, bits low..top+1, with rain above it.
One backward tick: read the window from a lower state s in {00,01,10,11} (the two output bits below the window), then the rain tail.
The new window is the w bits ending at the new top pair. Keep windows whose every lower state gives top + 3 and a window in the set."""
import sys
def back(win,w,s):
    """win: list of w bits low..high, last two equal (top wall). s=(p1,p2). returns (delta, list of output bits for window region + above)"""
    # input: win then rain
    inp=list(win)
    b=inp[-1]
    for i in range(16):
        b^=1; inp.append(b)
    p1,p2=s
    out=[]
    for bit in inp:
        o=bit^(p1|p2); out.append(o); p2=p1; p1=o
    # top of the output: highest k with out[k]==out[k+1], below the last few bits
    k=len(out)-2
    while k>=0 and out[k]!=out[k+1]: k-=1
    return k,out
def run(w):
    wins=[]
    for m in range(1<<(w-1)):
        bits=[(m>>i)&1 for i in range(w-1)]
        bits.append(bits[-1])
        wins.append(tuple(bits))
    alive=set(wins)
    D=w-2 # index of the low bit of the top pair
    while True:
        new=set()
        for win in alive:
            ok=True
            for s in ((0,0),(0,1),(1,0),(1,1)):
                k,out=back(win,w,s)
                if k!=D+3: ok=False;break
                nw=tuple(out[k+2-w:k+2])
                if len(nw)!=w or nw not in alive: ok=False;break
            if ok: new.add(win)
        if new==alive: break
        alive=new
    return alive
for w in range(6,23):
    a=run(w)
    print('w',w,'robust windows',len(a), sorted(''.join('#' if b else '.' for b in x) for x in list(a))[:6],flush=True)
