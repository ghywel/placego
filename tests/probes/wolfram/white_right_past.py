#!/usr/bin/env python3
"""L1050: the white-right past of the single seed (the 2-adic tower), traced far back, for the large view.

Local, 2026-10-27. A row whose right side is white has exactly one parent with a white right side, so this past is
unique and infinite. Each parent is solved leftwards from the white side (exact on any window) and checked against
its child. Writes packed bits for the viewer. Usage: white_right_past.py OUT.json
"""
import base64, json, sys
KP, KF, WL, WR = 512, 256, 3300, 300           # past depth, future depth, cells left and right of 0
n = WL + WR + 1
seed = [0]*n; seed[WL] = 1
past = [seed]; y = seed
for k in range(1, KP+1):
    x = [0]*n
    for p in range(WL, -1, -1):                   # positions 0 down to -WL; right of 1-k stays white
        if p - WL >= 1 - k: continue
        x[p] = y[p+1] ^ (x[p+1] | (x[p+2] if p+2 < n else 0))
    for p in range(1, WL + 1): assert y[p] == x[p-1] ^ (x[p] | x[p+1])
    past.append(x); y = x
fut = [seed]; r = seed
for t in range(1, KF+1):
    r = [(r[i-1] if i > 0 else 0) ^ (r[i] | (r[i+1] if i+1 < n else 0)) for i in range(n)]; fut.append(r)
rows = list(reversed(past)) + fut[1:]
packed = bytearray()
for row in rows:
    for i in range(0, n, 8):
        b = 0
        for j in range(8):
            b = (b << 1) | (row[i+j] if i+j < n else 0)
        packed.append(b)
json.dump({'w': n, 'h': len(rows), 'x0': -WL, 't0': -KP, 'stride': (n + 7)//8,
           'bits': base64.b64encode(bytes(packed)).decode()}, open(sys.argv[1], 'w'), separators=(',', ':'))
print('large view', n, 'x', len(rows), 'bytes', len(packed))
