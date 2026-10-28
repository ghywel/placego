#!/usr/bin/env python3
"""L1052: the Sierpinski twin: the white-right past of a Rule 60 seed is Pascal mod 2 near the corner of row 2^m.

Local, 2026-10-28. Rule 60 (x' = x(i-1) XOR x(i)) is Rule 30 beside a white right neighbour. The same backward
construction as white_right_past.py; asserts every past row equals row 4096 - k of Pascal's triangle mod 2 near its
right corner, k = 1..256, and writes a PNG. Usage: white_right_rule60.py OUT.png
"""
import zlib, struct, sys
K=256; WL=600; WR=300; n=WL+WR+1
# Rule 60: x'(i) = x(i-1) XOR x(i)  (Rule 30 with a white right neighbour)
seed=[0]*n; seed[WL]=1
past=[seed]; y=seed
for k in range(1,K+1):
    x=[0]*n
    for p in range(WL,-1,-1):          # white on [1-k, inf); x(i-1) = y(i) XOR x(i)
        if p-WL >= 1-k: continue
        x[p]=y[p+1]^x[p+1]
    for p in range(1,n): assert y[p]==x[p-1]^x[p]
    past.append(x); y=x
fut=[seed]; r=seed
for t in range(K): r=[(r[i-1] if i>0 else 0)^r[i] for i in range(n)]; fut.append(r)
rows=list(reversed(past))+fut[1:]
# compare with Pascal's triangle mod 2: row N-k of Pascal, right corner aligned with the seed
N=1<<12
import math
ok=True
for k in range(1,K+1):
    for pos in range(-WL, 1-k):
        j=N+pos              # row N-k: its right corner (j = N-k) sits at position -k
        # entry C(N-k, j) with j = (N-k) + pos  (pos <= 0 counts leftwards from the corner)
        if j<0: continue
        c=(math.comb(N-k,j) & 1)
        if c!=past[k][pos+WL]: ok=False; break
    if not ok: print('mismatch at k',k); break
print('Rule 60 white-right past equals Pascal row 4096-k (mod 2) near its right corner, k=1..%d:'%K, ok)
def png(path, rows):
    h=len(rows); w=len(rows[0]); raw=b''.join(b'\x00'+bytes(0 if v else 255 for v in r) for r in rows)
    ch=lambda t,d: struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    open(path,'wb').write(b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',w,h,8,0,0,0,0))+ch(b'IDAT',zlib.compress(raw,9))+ch(b'IEND',b''))
png(sys.argv[1], rows)
