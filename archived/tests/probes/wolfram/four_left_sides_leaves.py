#!/usr/bin/env python3
"""leaves.py: the four branches through wheel 87,866 (L1512). Wall-frame rows on K = 87,867 bits."""
import sys, hashlib
sys.set_int_max_str_digits(0)
K = 87867
M = (1 << K) - 1
def step(v): return ((v << 2) ^ ((v << 1) | v)) & M
def settle(v, n):
    assert n % 16 == 0
    for _ in range(n): v = step(v)
    return v
def cyc(v):
    rows = []
    u = v
    for _ in range(16):
        rows.append(u); u = step(u)
    return rows, u == v
def info(name, v):
    rows, ok = cyc(v)
    orr = 0
    for r in rows: orr |= r
    white = [j for j in range(K) if not (orr >> j) & 1]
    print(name, 'return', ok, 'white', white, 'bitlen', v.bit_length())
    return rows, ok, white
# the seed's row, far enough out that all K wheels are settled at lag 16
s = 1
T = 16 * 8000     # 128,000 ticks
for _ in range(T): s = step(s)
rows, ok, white = info('seed', s)
A0 = s
# flip wheel 58,287 of the seed's strip
A1 = settle(A0 ^ (1 << 58287), 16 * 3000)
# flip wheel 53,208, settle above it
B0 = settle(A0 ^ (1 << 53208), 16 * 3500)
rB = info('B0', B0)
for name, v, f in (('A1', A1, 58287),):
    info(name, v)
# flip wheel 72,576 on the other side
B1 = settle(B0 ^ (1 << 72576), 16 * 2000)
info('B1', B1)
def low_equal(u, v, n): return (u & ((1 << n) - 1)) == (v & ((1 << n) - 1))
print('A0,A1 agree below 58,287', low_equal(A0, A1, 58287), 'complement there', ((A0 ^ A1) >> 58287) & 1)
print('A0,B0 agree below 53,208', low_equal(A0, B0, 53208), 'complement there', ((A0 ^ B0) >> 53208) & 1)
print('B0,B1 agree below 72,576', low_equal(B0, B1, 72576), 'complement there', ((B0 ^ B1) >> 72576) & 1)
for name, v in (('A0', A0), ('A1', A1), ('B0', B0), ('B1', B1)):
    r, ok = cyc(v)
    print(name, 'first wheel where rows at lag 16 differ', None if ok else ((r[0] ^ step(r[15])) & -(r[0] ^ step(r[15]))).bit_length() - 1)
    def wt(m, L): return sum((r[i] >> m) & 1 for i in range(L))
    print('  weights', {m: wt(m, 16) for m in (53206, 58285, 72574, 87865)})
    # every phase comparison on the fork wheels between branches, all phases
import pickle
pickle.dump({'A0': A0, 'A1': A1, 'B0': B0, 'B1': B1}, open('leaves.pkl', 'wb'))
