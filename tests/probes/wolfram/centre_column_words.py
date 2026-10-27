#!/usr/bin/env python3
"""L1046: does any short word occur in the single seed's centre column only near the start?

Local, 2026-10-27. Simulates 2^17 steps of the single-seed Rule 30 evolution (rows as Python integers, bit index =
position), reads the centre column, and reports for words of length 12 the latest first appearance and the earliest
last appearance. A start-only word would show an early last appearance.
"""
T = 1 << 17
x, out = 1 << T, bytearray()
for t in range(T):
    out.append(48 + ((x >> T) & 1))
    x = (x << 1) ^ (x | (x >> 1))      # cell i <- cell(i-1) XOR (cell i OR cell(i+1))
s = out.decode()
assert s[:16] == '1101110011000101'    # the known opening of the centre column
n, first, last = 12, {}, {}
for i in range(len(s) - n + 1):
    w = s[i:i + n]
    first.setdefault(w, i)
    last[w] = i
print('length-12 words present: %d of 4096; latest first appearance %d; earliest last appearance %d (of %d)'
      % (len(first), max(first.values()), min(last.values()), T))
