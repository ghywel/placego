#!/usr/bin/env python3
"""L1367 T55c (Local, 2026-11-03): adversarial local search for deep invasion of the classic ether.
reports/rule30-genealogy.md section 59a. Run: python3 tests/probes/ether_invasion_climb.py SECONDS T [T ...]

Ether at alignment (c0, c1) on x < 0 (alignments (4,3), (0,0), (6,1)); free right half on 0 .. 2T - 1 (bits beyond
cannot reach x <= 0 by T... they can reach x >= -T; we keep 2T so every cell that can influence the region x < 0 by
time T is free), white beyond. Objective: the depth -L(T) of the leftmost difference from the ether at time T.
Single-bit flips in random order, kept when the depth does not decrease; restart after 300 non-improving tries.
The best tail is replayed by a separate list oracle; its depth, digest, full bits (hex) and the front path L(t) at
t = T/4, T/2, 3T/4, T are printed. The loop stops on wall-clock time, so runs are not bit-reproducible: the printed
bits are the record (L1368 correction).
"""
import hashlib
import random
import sys
import time

SECS = float(sys.argv[1]); Ts = [int(a) for a in sys.argv[2:]]
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
rng = random.Random(553)


def setup(c0, c1, T):
    LO, HI = -3 * T - 20, 3 * T + 20
    n = HI - LO + 1; mask = (1 << n) - 1
    ref = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, HI + 1))
    left = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, 0))
    return LO, HI, mask, ref, left


def depth_path(a, ref, mask, LO, T, marks=()):
    out = {}
    r = ref
    for t in range(1, T + 1):
        a = ((a << 1) ^ (a | (a >> 1))) & mask
        r = ((r << 1) ^ (r | (r >> 1))) & mask
        if t in marks or t == T:
            d = (a ^ r) >> (t + 1) << (t + 1)
            out[t] = (d & -d).bit_length() - 1 + LO if d else None
    return out


def replay_depth(bits, c0, c1, T):
    lo, hi = -2 * T - 5, 2 * T + 5
    g = [TAB[(x + c0) % 7][c1] if x < 0 else (bits[x] if x < len(bits) else 0) for x in range(lo, hi + 1)]
    e = [TAB[(x + c0) % 7][c1] for x in range(lo, hi + 1)]
    for _ in range(T):
        g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]
        e = [e[i - 1] ^ (e[i] | e[i + 1]) for i in range(1, len(e) - 1)]
        lo += 1
    return next((lo + i for i in range(len(g)) if g[i] != e[i] and lo + i < 0), None)


for T in Ts:
    for (c0, c1) in [(4, 3), (0, 0), (6, 1)]:
        LO, HI, mask, ref, left = setup(c0, c1, T)
        free = list(range(0, 2 * T))
        score = lambda a: (lambda L: -L if L is not None else -10 ** 6)(depth_path(a, ref, mask, LO, T)[T])
        t0 = time.time(); best = (-10 ** 9, None); restarts = 0
        while time.time() - t0 < SECS / 3:
            a = left | sum(rng.getrandbits(1) << (x - LO) for x in free)
            s = score(a); stall = 0; restarts += 1
            while stall < 300 and time.time() - t0 < SECS / 3:
                x = rng.choice(free)
                a2 = a ^ (1 << (x - LO)); s2 = score(a2)
                if s2 >= s:
                    stall = 0 if s2 > s else stall + 1
                    a, s = a2, s2
                else:
                    stall += 1
            if s > best[0]:
                best = (s, a)
        s, a = best
        bits = [(a >> (x - LO)) & 1 for x in free]
        path = depth_path(a, ref, mask, LO, T, marks=(T // 4, T // 2, 3 * T // 4))
        rep = replay_depth(bits, c0, c1, T)
        print('T=%d alignment (%d,%d): best depth %d (%d restarts); replay leftmost difference at T: %s; front path %s; '
              'tail sha256 %s' % (T, c0, c1, s, restarts, rep, [path[k] for k in sorted(path)],
                                  hashlib.sha256(''.join(map(str, bits)).encode()).hexdigest()[:16]), flush=True)
        print('   tail bits 0..%d as hex (bit i = cell x = i, little-endian): %x' % (len(bits) - 1,
              sum(v << i for i, v in enumerate(bits))), flush=True)
print('ETHER_INVASION_CLIMB_DONE')
