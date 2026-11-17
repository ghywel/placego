#!/usr/bin/env python3
"""inquisition_plateaus.py: which starts pass a late plateau together? (T-P, DQ-031/DQ-032)

RUN-ON:     cpu (Python 3 + numpy), about a minute
COMMAND:    python3 tests/probes/inquisition_plateaus.py [WMIN=14] [WMAX=20]

The kit's normal form (see inquisition_wall_census.py). For each W, every start is run to its death; at every even
time t >= W - 2 the near-wall 7-word (depths 1..7) of every start is kept. For each late tick t -> t + 2 with at
least 16 alive it prints the tick ratio, the number of distinct 7-words among the survivors at t, the largest
7-word's share, and:
  plateau ticks (ratio >= 0.75): within the largest 7-word cluster, the mean pairwise Hamming distance of the
     starting rows, its ratio to W, the share of disagreements in the deepest third of the support, and the
     members' true widths;
  cliff ticks (ratio <= 0.35): the share of the deaths coming from the single largest 7-word cluster at t.
Predictions P-L1..P-L3 are in reports/inquisition-20261031.md (round 2), committed before this ran.
"""
import sys
from itertools import combinations
import numpy as np

WMIN = int(sys.argv[1]) if len(sys.argv) > 1 else 14
WMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20
KW = 7


def popcount(v):
    return bin(v).count('1')


def run(W):
    n = 1 << W
    r = np.arange(n, dtype=np.int64)
    depth = 3 * W + 50
    x = np.zeros((depth + 2, n), dtype=np.uint8)
    for k in range(1, W + 1):
        x[k] = (r >> (k - 1)) & 1
    death = np.full(n, -1, dtype=np.int64)
    words = {}
    t = 0
    while True:
        if t % 2 == 0:
            newly = (death < 0) & (x[1] == 0)
            death[newly] = t
            if t >= W - 2:
                w = np.zeros(n, dtype=np.int64)
                for k in range(1, KW + 1):
                    w |= x[k].astype(np.int64) << (k - 1)
                words[t] = w
            if not np.any(death[1:] < 0):
                break
        nxt = np.zeros_like(x)
        nxt[1:depth] = x[2:depth + 1] ^ (x[1:depth] | x[0:depth - 1])
        x = nxt
        t += 1
    return r, death, words


def main():
    rows = []
    for W in range(WMIN, WMAX + 1):
        r, death, words = run(W)
        print(f"W={W} D={death[1:].max()}")
        for t in sorted(words):
            alive = np.nonzero((death > t) & (r > 0))[0]
            if len(alive) < 16:
                continue
            passed = alive[death[alive] > t + 2]
            ratio = len(passed) / len(alive)
            w = words[t][alive]
            vals, counts = np.unique(w, return_counts=True)
            top = vals[np.argmax(counts)]
            share = counts.max() / len(alive)
            line = (f"  t={t:3d} alive={len(alive):6d} ratio={ratio:.3f} distinct7={len(vals):6d} "
                    f"({len(vals)/len(alive):.2f} of alive) top7={format(int(top), '07b')[::-1]} share={share:.2f}")
            kind = 'late'
            if ratio >= 0.75:
                kind = 'plateau'
                members = [int(s) for s in alive[w == top]]
                pairs = list(combinations(members, 2))[:20000]
                if pairs:
                    dist = [popcount(a ^ b) for a, b in pairs]
                    mean = sum(dist) / len(dist)
                    widths = [m.bit_length() for m in members]
                    deep = 0
                    tot = 0
                    for a, b in pairs:
                        d = a ^ b
                        hi = max(widths)
                        for k in range(hi):
                            if (d >> k) & 1:
                                tot += 1
                                if k >= (2 * hi) // 3:
                                    deep += 1
                    line += (f" | cluster {len(members)}: mean Hamming {mean:.2f} = {mean / W:.2f} W; "
                             f"deep-third share {deep / max(1, tot):.2f}; widths {sorted(set(widths))}")
                else:
                    line += f" | cluster {len(members)}"
            elif ratio <= 0.35:
                kind = 'cliff'
                died = alive[death[alive] == t + 2]
                wd = words[t][died]
                dv, dc = np.unique(wd, return_counts=True)
                line += f" | cliff: {len(died)} deaths, largest 7-word cluster gives {dc.max() / len(died):.2f}"
            print(line)
            rows.append((W, t, kind, len(alive), round(ratio, 3), len(vals) / len(alive), round(share, 3)))
    for kind in ('plateau', 'late', 'cliff'):
        sel = [z for z in rows if z[2] == kind]
        if sel:
            print(f"SUMMARY {kind}: {len(sel)} ticks; mean distinct/alive {np.mean([z[5] for z in sel]):.2f}; "
                  f"mean top share {np.mean([z[6] for z in sel]):.2f}")
    print("PLATEAUS_DONE")


if __name__ == '__main__':
    main()
