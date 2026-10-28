#!/usr/bin/env python3
"""Local, 2026-10-28 (L1069): how long a narrow strip determines its own future in Rule 30.

Take the single seed's row at time T0, keep only cells in a strip [c - W/2, c + W/2), and make every outside cell
unknown. Evolve with three-valued Rule 30, new(i) = x(i-1) XOR (x(i) OR x(i+1)): the OR is known when either input is
a known 1, or both are known. Report how many steps the strip's centre cell stays determined, and the erosion of the
known region's two ends (cells per step). Left-permutivity predicts the left end erodes at exactly 1 per step.
Usage: strip_self_determination.py T0 W [CENTRE ...]
"""
import sys
T0, W = int(sys.argv[1]), int(sys.argv[2]); centres = [int(c) for c in sys.argv[3:]] or [0]
OFF = T0 + 4 * W + 8
x = 1 << OFF
for _ in range(T0): x = (x << 1) ^ (x | (x >> 1))
for c in centres:
    lo, hi = c - W // 2, c + W // 2
    K = ((1 << (hi - lo)) - 1) << (lo + OFF); V = x & K
    steps = 0; ends = []
    while True:
        l_k, l_v = K << 1, V << 1; r_k, r_v = K >> 1, V >> 1
        or_k = (K & r_k) | (K & V) | (r_k & r_v); or_v = (V | r_v) & or_k
        K, V = l_k & or_k, (l_v ^ or_v) & (l_k & or_k)
        steps += 1
        if not K: break
        left = (K & -K).bit_length() - 1 - OFF; right = K.bit_length() - 1 - OFF
        ends.append((left, right))
        if not (K >> (c + OFF)) & 1 and 'life' not in locals(): life = steps - 1
    life = locals().get('life', steps)
    L0, R0 = lo, hi - 1
    # erosion speeds over the first half of the known region's lifetime
    h = max(1, len(ends) // 2); l1, r1 = ends[h - 1]
    print(f"T0={T0} W={W} centre {c}: centre determined for {life} steps ({life / W:.3f} W); known region lasts {len(ends)}; "
          f"left end speed {(l1 - L0) / h:+.3f}, right end speed {(r1 - R0) / h:+.3f} cells/step")
    del life
