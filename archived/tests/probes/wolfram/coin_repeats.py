#!/usr/bin/env python3
"""coin_repeats.py T L: the owner's repeat test (inquisition round 14; Cloud, CL692). The single seed to T (pattern (T+1) x (2T+1))
and an iid control array of the same shape. For the centre column (t >= 64) find every L-bit window that occurs elsewhere in any
column (x != 0), row, right ray (x - t const) or left ray (x + t const), count the matches against the expectation pairs * 2^-L, and
extend each match to its full length; report the longest repeat and where it is. Output: coin_repeats.out."""
import sys, numpy as np
T, L = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(9)
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
def pattern(T):
    W = 2 * T + 1; A = np.zeros((T + 1, W), dtype=np.uint8); A[0, T] = 1
    for t in range(T): A[t + 1] = step(A[t])
    return A
POW = (1 << np.arange(L)[::-1]).astype(np.uint64)
def windows(seq):
    if len(seq) < L: return np.zeros(0, dtype=np.uint64)
    return (np.lib.stride_tricks.sliding_window_view(seq, L).astype(np.uint64) @ POW)
def families(A):
    T1, W = A.shape; c = (W - 1) // 2
    yield "column", ((x - c, A[:, x]) for x in range(W) if x != c)
    yield "row", ((t, A[t, :]) for t in range(T1))
    yield "right ray", ((o, np.diagonal(A, offset=o)) for o in range(-T1 + 1, W))      # cells (t, t+o): x - t = o - c
    yield "left ray", ((o, np.diagonal(A[:, ::-1], offset=o)) for o in range(-T1 + 1, W))
def analyse(A, label):
    T1, W = A.shape; c = (W - 1) // 2; centre = A[64:, c]; cw = windows(centre); cset = np.unique(cw)
    total_pairs = 0; matches = 0; best = (0, None)
    for fam, gen in families(A):
        for idx, seq in gen:
            w = windows(seq); total_pairs += len(w) * len(cw)
            if len(w) == 0: continue
            hit = np.flatnonzero(np.isin(w, cset))
            for h in hit:
                # positions in the centre with this word
                for p in np.flatnonzero(cw == w[h]):
                    if fam == "column" and False: pass
                    matches += 1
                    # extend forward and backward
                    m = L
                    while p + m < len(centre) and h + m < len(seq) and centre[p + m] == seq[h + m]: m += 1
                    k = 1
                    while p - k >= 0 and h - k >= 0 and centre[p - k] == seq[h - k]: k += 1
                    tot = m + k - 1
                    if tot > best[0]: best = (tot, (fam, int(idx), int(h - (k - 1)), int(p - (k - 1)) + 64))
    exp = total_pairs / 2.0**L
    print(f"{label}: pattern {A.shape}, centre words {len(cw)}, pairs {total_pairs:.3e}, expected {L}-bit matches {exp:.2f}, found {matches}; "
          f"longest repeat {best[0]} bits at {best[1]} (family, index, offset in it, centre time)")
A = pattern(T); analyse(A, "single seed")
C = rng.integers(0, 2, A.shape).astype(np.uint8); analyse(C, "iid control")
print("COIN_REPEATS_DONE")
