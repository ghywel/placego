#!/usr/bin/env python3
"""Local, 2026-10-28 (L1064): the tree of possible right-diagonal period beginnings.

From the universal start (universal_start.py: first diagonal j with period > 2 has two equal alternating feeders),
the periods of D_j, D_(j+1), ... are a function of the start bits s_j, s_(j+1), ... alone, and every bit string occurs
for some row. Enumerates all 2 * 2^L choices (feeder phase and L start bits) and counts the distinct period sequences of
length k for k <= L, and counts period drops (p_(d) < max earlier period) anywhere in the complete tree.
Usage: beginnings_tree.py L
"""
import sys, itertools
import numpy as np
L = int(sys.argv[1])
def least(a):
    while len(a) > 1 and len(a) % 2 == 0 and np.array_equal(a[:len(a)//2], a[len(a)//2:]): a = a[:len(a)//2]
    return a
def step(p2, p1, bit):
    q = max(len(p1), len(p2)); g = np.tile(p1, q // len(p1)) | np.tile(p2, q // len(p2))
    D = (np.concatenate(([0], np.bitwise_xor.accumulate(g)[:-1])) ^ bit).astype(np.uint8)
    if g.sum() & 1: D = np.concatenate((D, 1 - D))
    return least(D)
# depth-first over start bits, sharing prefixes
seqs = [set() for _ in range(L + 1)]; drops = [0]
def dfs(p2, p1, pers):
    k = len(pers); seqs[k].add(tuple(pers))
    if k == L: return
    for b in (0, 1):
        D = step(p2, p1, b); e = len(D).bit_length() - 1
        if e < max(pers + [1]): drops[0] += 1
        dfs(p1, D, pers + [e])
for f in ([0, 1], [1, 0]):
    a = np.array(f, np.uint8); dfs(a, a, [])
print("period drops in the complete tree:", drops[0])
for k in range(1, L + 1):
    print(f"length {k:2d}: {len(seqs[k]):6d} distinct period sequences  (log2 {np.log2(len(seqs[k])):.2f})")
