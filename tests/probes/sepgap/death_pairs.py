#!/usr/bin/env python3
"""SEP gap, step 1 (Local, 8 November 2026): do 00 pairs in the free bits relate to death?
Frame: zero-boundary left half as naturals (bit i = depth i + 1), F Y = (Y >> 1) ^ (Y | (Y << 1)). Free bits
f(s) = depth 1 at tick 2s + 1; death D = first even tick with depth 1 white (D = 2N, free bits f(0..N-1) defined).
Usage: death_pairs.py WMIN WMAX. Exhaustive over all starts of exact width w (top bit set, depth 1 black).
Background (a priori, recorded before the run): no local lemma 'a 00 forces death within k steps' can hold for finite
rows, since a far truncation of Theta f survives at least to about its truncation depth and every free prefix occurs.
Predictions, before the run:
 (a) the last free pair before death is 00 more often than 00 occurs among earlier free pairs (death sits at 00), P = 0.6;
 (b) the hazard of death at the next check is higher just after a 00 pair than after any other pair, P = 0.6;
 (c) the longest survivors of each width (top 1 % and the champions) have fewer 00 pairs per step in their late free
     bits (s >= w/2) than all starts, P = 0.65.
Counterfactual: no differences: 00 pairs carry no information about death, and the SEP gap class is not harder for
finite rows than its complement."""
import sys
def F(y): return (y >> 1) ^ (y | (y << 1))
def run(y):
    f = []; t = 0
    while True:
        if y & 1 == 0: return t, f          # even tick t: depth 1 white -> death at t
        y = F(y); t += 1                    # odd tick t
        f.append(y & 1)
        y = F(y); t += 1
wmin, wmax = int(sys.argv[1]), int(sys.argv[2])
for w in range(wmin, wmax + 1):
    lo, hi = 1 << (w - 1), 1 << w
    stats = []
    pair_counts = {}; last_counts = {}; hz = {}      # hz[pair] = [deaths at next check, total occurrences]
    for y in range(lo | 1, hi, 2):
        D, f = run(y)
        N = D // 2
        stats.append((D, y, f))
        if N >= 2:
            lp = (f[N - 2], f[N - 1]); last_counts[lp] = last_counts.get(lp, 0) + 1
        for s in range(N - 1):
            p = (f[s], f[s + 1])
            pair_counts[p] = pair_counts.get(p, 0) + 1
            h = hz.setdefault(p, [0, 0]); h[1] += 1
            if s + 1 == N - 1: h[0] += 1           # the pair ends at the last free bit: death at the next check
    stats.sort(key=lambda r: -r[0])
    n = len(stats); top = stats[:max(1, n // 100)]; champ = [r for r in stats if r[0] == stats[0][0]]
    def late00(rows):
        z = c = 0
        for D, y, f in rows:
            for s in range(w // 2, len(f) - 1):
                c += 1; z += (f[s] == 0 and f[s + 1] == 0)
        return z / c if c else float('nan'), c
    tot = sum(pair_counts.values()); tl = sum(last_counts.values())
    base00 = pair_counts.get((0, 0), 0) / tot; last00 = last_counts.get((0, 0), 0) / tl
    hzs = {''.join(map(str, p)): round(h[0] / h[1], 4) for p, h in sorted(hz.items())}
    print(f'w {w}: starts {n}, D max {stats[0][0]} ({len(champ)} champions), '
          f'00 share of pairs {base00:.4f}, of last pairs {last00:.4f}; hazard by pair {hzs}; '
          f'late-00 rate all {late00(stats)[0]:.4f}, top1% {late00(top)[0]:.4f}, champions {late00(champ)[0]:.4f}', flush=True)
