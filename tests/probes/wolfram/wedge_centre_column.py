#!/usr/bin/env python3
"""L1053: the real centre column is written into the white-right past, on the columns x = -2^m.

Local, 2026-10-28. Traces the white-right past exactly to depth 4096 (solving leftwards; cells right of 1 - k stay
white) and reads column x = -2^m from time -2^m downwards, against the seed's centre column. Measured agreement:
4, 6, 7, 9, 15, 16, 24, 25, 27, 29, 34 bits for 2^m = 4 .. 4096, equal to the number of right diagonals whose
period divides 2^m. Usage: wedge_centre_column.py OUT.json
"""
import json, sys
K=4096; WL=4200                  # depth and cells kept left of 0 (the recurrence only needs cells to the right)
n=WL+1
seed=[0]*n; seed[WL]=1; y=seed
past={}                          # past[k][pos] for the columns we read
cols=[-(1<<m) for m in range(2,13)]
for k in range(1,K+1):
    x=[0]*n
    for p in range(WL,-1,-1):
        if p-WL >= 1-k: continue
        x[p]=y[p+1]^(x[p+1]|(x[p+2] if p+2<n else 0))
    past[k]={c:x[c+WL] for c in cols if c+WL>=0}
    y=x
# the real centre column
T=200; r=1<<(T+2); cen=[]
for t in range(T):
    cen.append((r>>(T+2))&1); r=(r<<1)^(r|(r>>1))
out={}
for m in range(2,13):
    P=1<<m; col=-P
    seq=[past[P-s][col] for s in range(0,min(P,T)) if (P-s)>=1]      # wedge column x=-P at times -P+s, s=0..
    agree=next((s for s,(a,b) in enumerate(zip(seq,cen)) if a!=b), len(seq))
    out[m]=agree
    print('column x = -%4d: matches the centre column for its first %3d bits   wedge: %s   centre: %s'%(P,agree,''.join(map(str,seq[:36])),''.join(map(str,cen[:36]))))
json.dump({'agree':out,'centre':''.join(map(str,cen[:64])),'cols':{str(m):''.join(str(past[(1<<m)-s][-(1<<m)]) for s in range(0,min(1<<m,64))) for m in range(2,13)}},open(sys.argv[1],'w'))
