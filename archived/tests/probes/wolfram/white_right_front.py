#!/usr/bin/env python3
"""L1050: the ice front of the white-right past: where the left crystal ends, depth by depth (to 768 back).

Local, 2026-10-27. Exact rows as in white_right_past.py; reports the far-left crystal period and the last cell that
follows it. Measured: period 48 from t = -80 on; front at -640, -1542, -3146, -4472 at t = -128, -256, -512, -768.
"""
K=768; W=16000; n=W+1          # positions -W..0; right of x = 1-k is white anyway
seed=[0]*n; seed[W]=1; y=seed
out=[]
def far_period(row, span=3000):
    seg=row[:span]
    for p in range(1,1400):
        if all(seg[i]==seg[i+p] for i in range(span-p)): return p
    return None
for k in range(1,K+1):
    x=[0]*n
    for p in range(W, -1, -1):
        pos=p-W
        if pos >= 1-k: continue
        x[p]= y[p+1] ^ (x[p+1] | (x[p+2] if p+2<n else 0))
    y=x
    q=far_period(x)
    if q:
        e=q
        while e < n and x[e]==x[e-q]: e+=1
        lc=e-1-W
    else: lc=None
    chaos=[x[p] for p in range((lc+W+1) if lc is not None else 0, W+1-k+1)]
    dens=sum(chaos)/len(chaos) if chaos else None
    out.append((k,q,lc,dens))
for k,q,lc,d in out:
    if k%64==0: print('t=-%3d  left crystal period %s  ends at x=%s  irregular width %s  black density there %s'%(k,q,lc,(1-k-1-lc) if lc is not None else '>window', round(d,3) if d is not None else '-'))
