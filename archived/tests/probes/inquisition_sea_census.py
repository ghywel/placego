#!/usr/bin/env python3
"""inquisition_sea_census.py: the wall beside a periodic sea instead of the white one (T-H, DQ-034).

RUN-ON:     cpu (Python 3 + numpy), about a minute
COMMAND:    python3 tests/probes/inquisition_sea_census.py [PMAX=6] [WP=8] [K=160]

The kit's normal form (see inquisition_wall_census.py): wall at depth 0 counted white, rule 30 on depths >= 1, the
clock lives while depth 1 is black at every even time, time 0 included. Here depths 1..WP hold a patch r
(0 <= r < 2^WP) and every depth d > WP holds the sea u[(d - WP - 1) mod p], for every word u of length p <= PMAX
(every rotation, so every phase). The window is cut at depth N = WP + K + 8; the cut's error reaches depth N - t at
time t, never depth 3 before K. Prints, per word, the longest life over all patches and the patches reaching K.
u = 0 is Q01 itself and is the control (D(1..8) of d1_engine). Predictions: reports/inquisition-20261031.md (T-H),
committed before this ran.
"""
import sys
import numpy as np

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
WP = int(sys.argv[2]) if len(sys.argv) > 2 else 8
K = int(sys.argv[3]) if len(sys.argv) > 3 else 160
KNOWN_D = {1: None, 2: 6, 3: 6, 4: 6, 5: 8, 6: 10, 7: 12, 8: 12}


def lives(u, wp):
    n = 1 << wp
    r = np.arange(n, dtype=np.int64)
    N = wp + K + 8
    x = np.zeros((N + 2, n), dtype=np.uint8)
    for k in range(1, wp + 1):
        x[k] = (r >> (k - 1)) & 1
    for d in range(wp + 1, N + 2):
        x[d] = u[(d - wp - 1) % len(u)]
    death = np.full(n, K + 1, dtype=np.int64)
    for t in range(K + 1):
        if t % 2 == 0:
            newly = (death > K) & (x[1] == 0)
            death[newly] = t
        nxt = x.copy()
        nxt[1:N + 1] = x[2:N + 2] ^ (x[1:N + 1] | x[0:N])
        nxt[0] = 0
        x = nxt
    return death


def main():
    for wp in range(2, WP + 1):
        d = lives((0,), wp)
        D = int(d[1:].max())
        assert D == KNOWN_D[wp], ("control", wp, D)
    print("CONTROL_PASS: the white sea reproduces D(2..%d)" % WP)
    rows = []
    for p in range(1, PMAX + 1):
        for w in range(1 << p):
            u = tuple((w >> i) & 1 for i in range(p))
            death = lives(u, WP)
            best = int(death.max())
            capped = [int(i) for i in np.nonzero(death > K)[0]]
            rows.append((''.join(map(str, u)), best, len(capped), capped[:4]))
    rows.sort(key=lambda z: -z[1])
    for word, best, nc, ex in rows[:25]:
        print(f"sea {word:>6s}: longest life {'>= cap' if best > K else best:>6}  patches at cap {nc}  e.g. {ex}")
    print("lives, all words:", [(w, b) for w, b, _, _ in rows])
    print("SEA_CENSUS_DONE")


if __name__ == '__main__':
    main()
