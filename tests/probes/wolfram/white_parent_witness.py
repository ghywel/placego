#!/usr/bin/env python3
"""white_parent_witness.py: GPT's discriminating test (GC2635), taken by Cloud (CL722). Can a completion of the seed's low
39,088 bits (bits 0 .. 39,087 as in the single seed, bit 39,088 and above free) give the opposite colour at wheel K = 87,867
at tick T = 122,880? GPT's guard (reset_path, GC2633-34): with 39,089 bits fixed every completion agrees with the seed through
K at T and forever; with 39,088 bits fixed, through K - 1, and the bit at K is then pinned forever either way (its common
parent K - 1 is white from T on). Only completions with bit 39,088 = 1 can witness a flip.
Wall frame, prefix truncated to bits 0 .. K (exact: bit j reads bits j - 2 .. j). The seed a(t) and each completion y(t)
are stepped together to T + 16. Reported per completion: J(T) (lowest differing bit, WIDTH if none), the colours at K at T
and the difference there at T and T + 16, the lag-16 edges B(T) (seed) and C(T) (row), t1 = the first tick after the last
tick with J < K (the merge front past K - 1 for good), and the two last times of GC2624's rule (last C != B, last J <= B).
Seed facts replayed first: B(T) = K, the two lag-16 hits at K at T and T + 16, the lag-32 return through K, tau = the seed's
last black at K - 1 before T, t_K = the first tick with B = K. Caps: the substitute (ulimit, timeout), this Linux host."""
import sys, time, numpy as np
from collections import deque
P = 16; K = 87867; T = 122880; FREE = 39088; WIDTH = K + 1; MASK = (1 << WIDTH) - 1
def step(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else WIDTH
t0 = time.time()
# seed facts
a = 1; ring = deque(maxlen=P + 1); B = []; tau = -1; tK = None; kept = {}
for t in range(T + 2 * P + 1):
    ring.append(a)
    if t in (T, T + P, T + 2 * P): kept[t] = a
    if t >= P:
        b = lowbit(ring[0] ^ a); B.append(b)          # B[t - P] = edge at tick t - P
        if tK is None and b == K: tK = t - P
    if t < T and (a >> (K - 1)) & 1: tau = t
    a = step(a)
assert B[T] == K and kept[T] ^ kept[T + P] == 1 << K and kept[T + P] ^ kept[T + 2 * P] == 1 << K and kept[T] == kept[T + 2 * P]
print(f"seed: B(T) = {B[T]} = K; lag-16 hits at K at T and T+16 and the lag-32 return through K: replayed; "
      f"t_K (first tick with B = K) = {tK}; tau (last black of wheel K-1 before T) = {tau}; B(32768) = {B[32768]}  ({time.time()-t0:.1f} s)")
Barr = np.array(B[:T + 1], dtype=np.int64)
def run(y0, label):
    a = 1; y = y0; ra = deque(maxlen=P + 1); ry = deque(maxlen=P + 1)
    lastJltK = -1; lastCneB = -1; lastJleB = -1; everdiff = False; out = {}
    for t in range(T + P + 1):
        ra.append(a); ry.append(y)
        if t <= T:
            J = lowbit(a ^ y)
            if J < WIDTH: everdiff = True
            if J < K: lastJltK = t
            if J <= B[t]: lastJleB = t
        if t >= P:
            tp = t - P
            C = lowbit(ry[0] ^ y)
            if C != B[tp]: lastCneB = tp
            if tp == T:
                out = dict(J=lowbit(ra[0] ^ ry[0]), aK=(ra[0] >> K) & 1, yK=(ry[0] >> K) & 1, C=C,
                           dK=((ra[0] ^ ry[0]) >> K) & 1, dK16=((a ^ y) >> K) & 1)
        a = step(a); y = step(y)
    t1 = lastJltK + 1
    print(f"  {label:34s} J(T)={out['J']:6d} aK={out['aK']} yK={out['yK']} dK(T)={out['dK']} dK(T+16)={out['dK16']} "
          f"B(T)={B[T]} C(T)={out['C']:6d}  t1={t1:7d} ({'before' if t1 <= tau else 'AFTER'} tau)  lastC!=B={lastCneB:7d} lastJ<=B={lastJleB:7d} "
          f"{'same' if lastCneB == lastJleB else 'DIFFER'}{'' if everdiff else ' (never differed)'}", flush=True)
    return out, t1, lastCneB, lastJleB
print("W1: the two-black-cell seed 1 + 2^39088")
r = run(1 | (1 << FREE), "1 + 2^39088")
flips = [("W1", r[0]['dK'])]
print("W3: single free bit j")
for j in (39089, 39090, 39100, 40000, 45000, 50000, 60000, 70000, 80000, 85000, 87000, 87800, 87865, 87866, 87867):
    r = run(1 | (1 << j), f"1 + 2^{j}"); flips.append((f"W3 j={j}", r[0]['dK']))
rng = np.random.default_rng(606)
def rand_bits(lo, hi):
    n = hi - lo + 1; bits = rng.integers(0, 2, size=n, dtype=np.uint8)
    return int.from_bytes(np.packbits(bits, bitorder='little').tobytes(), 'little') << lo
print("W2: twenty random completions of bits 39,088 .. K with bit 39,088 = 1")
for i in range(20):
    r = run(1 | (1 << FREE) | rand_bits(FREE + 1, K), f"random {i}"); flips.append((f"W2 {i}", r[0]['dK']))
print("W2s: two structured completions (all ones; alternating 1010.. from bit 39,088)")
r = run(1 | (((1 << (K - FREE + 1)) - 1) << FREE), "all ones from 39088"); flips.append(("W2s ones", r[0]['dK']))
alt = sum(1 << j for j in range(FREE, K + 1, 2)); r = run(1 | alt, "alternating from 39088"); flips.append(("W2s alt", r[0]['dK']))
print("W4 (control, GPT's guard): five random completions with bit 39,088 = 0, bits 39,089 .. K random")
for i in range(5):
    r = run(1 | rand_bits(FREE + 1, K), f"control {i}"); flips.append((f"W4 {i}", r[0]['dK']))
print(f"flips at K at T: {sum(d for _, d in flips)} of {len(flips)} completions; witnesses: {[n for n, d in flips if d]}")
print(f"total {time.time()-t0:.1f} s")
print("WHITE_PARENT_WITNESS_DONE")
