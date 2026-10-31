#!/usr/bin/env python3
"""inquisition_wall_census.py: the wall-form death census for the 31 October inquisition (T-A, T-F, T-G).

RUN-ON:     cpu (Python 3 + numpy), about a minute to W = 20
COMMAND:    python3 tests/probes/inquisition_wall_census.py [WMAX=20]

The kit's normal form (Rule30ZeroBoundary): the wall is depth 0 and counts as white; the left world is depths
1, 2, ...; rule 30 gives x_k(t+1) = x_(k+1)(t) XOR (x_k(t) OR x_(k-1)(t)). A start is r with 0 < r < 2^W, bit k-1 of r
being depth k (depths 1..W). The clock lives while depth 1 is black at every even time, time 0 included; the death time
is the first even t with depth 1 white (d1_engine.py's convention).

Per width it prints:
  T-A  D(W); deaths at t = 0; among deaths at t >= 2, the kind: starved (x_2, x_1) = (0, 0) at t - 1, or cancelled
       (1, 1); and asserts the hand law: x_2 = x_1 at t - 1, and that pair is the complement of (x_3, x_2) at t - 2.
  T-F  survivors at each even time; the tick ratio; the champions' margin over t* = 2W - 2; mean death time by the
       near-wall pattern (depths 1..4) among starts alive at t = 4.
  T-G  every champion's radar: true width, black density, black runs, longest white run inside the support,
       near-wall bits, death kind, D - (2W - 2); and whether each new champion's restriction to depths 1..W-1 is a
       champion of W - 1.
Predictions and the record search are in reports/inquisition-20261031.md (written and committed before this ran).
"""
import sys
import numpy as np

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
KNOWN_D = {2: 6, 3: 6, 4: 6, 5: 8, 6: 10, 7: 12, 8: 12, 9: 18, 10: 18, 11: 30, 12: 30, 13: 30, 14: 32, 15: 32,
           16: 32, 17: 32, 18: 32, 19: 38, 20: 38, 21: 38, 22: 40, 23: 40, 24: 42}


def census(W):
    n = 1 << W
    r = np.arange(n, dtype=np.int64)
    tmax = 2 * W + 40
    depth = W + tmax + 3
    x = np.zeros((depth + 2, n), dtype=np.uint8)          # row k = depth k; row 0 is the wall, always 0
    for k in range(1, W + 1):
        x[k] = (r >> (k - 1)) & 1
    death = np.full(n, -1, dtype=np.int64)
    kind = np.full(n, -1, dtype=np.int8)                  # 0 starved, 1 cancelled, 2 died at t = 0
    alive_counts = []
    hist = []                                             # (x_1, x_2, x_3) at each time, for the hand-law check
    t = 0
    while True:
        hist.append((x[1].copy(), x[2].copy(), x[3].copy()))
        if t % 2 == 0:
            newly = (death < 0) & (x[1] == 0)
            if t == 0:
                kind[newly] = 2
            else:
                x1p, x2p, _ = hist[t - 1]
                assert np.all(x1p[newly] == x2p[newly]), "hand law: x_2 = x_1 at t - 1"
                _, x2pp, x3pp = hist[t - 2]
                assert np.all(x2p[newly] == 1 - x3pp[newly]), "hand law: complement of x_3 at t - 2"
                assert np.all(x1p[newly] == 1 - x2pp[newly]), "hand law: complement of x_2 at t - 2"
                kind[newly] = x1p[newly]
            death[newly] = t
            alive_counts.append((t, int(np.sum((death < 0) & (r > 0)))))
            if np.all(death[1:] >= 0):
                break
        assert t < tmax, "census cap reached"
        nxt = np.zeros_like(x)
        nxt[1:depth] = x[2:depth + 1] ^ (x[1:depth] | x[0:depth - 1])
        x = nxt
        t += 1
    return r, death, kind, alive_counts


def radar(start, W):
    bits = [(start >> i) & 1 for i in range(W)]          # depth 1 first
    top = max(i for i in range(W) if bits[i]) + 1
    sup = bits[:top]
    runs = sum(1 for i in range(top) if sup[i] and (i == 0 or not sup[i - 1]))
    white, best = 0, 0
    for b in sup:
        white = white + 1 if b == 0 else 0
        best = max(best, white)
    near = ''.join(str(b) for b in bits[:4])
    return dict(width=top, density=round(sum(sup) / top, 2), runs=runs, white_run=best, near=near)


def main():
    prev_champs, prevD = set(), None
    summary = []
    for W in range(2, WMAX + 1):
        r, death, kind, alive = census(W)
        death, kind = death[1:], kind[1:]
        rr = r[1:]
        D = int(death.max())
        assert KNOWN_D.get(W, D) == D, f"control: D({W}) = {D}, expected {KNOWN_D.get(W)}"
        later = kind[death >= 2]
        starved, cancelled = int(np.sum(later == 0)), int(np.sum(later == 1))
        bytime = {}
        for tt in sorted(set(int(v) for v in death[death >= 2])):
            sel = death == tt
            bytime[tt] = (int(np.sum(kind[sel] == 0)), int(np.sum(kind[sel] == 1)))
        champs = [int(s) for s in rr[death == D]]
        ckinds = sorted(set(int(k) for k in kind[death == D]))
        # T-F: tick ratios
        ratios = []
        for (t0, a0), (t1, a1) in zip(alive, alive[1:]):
            if a0 >= 16:
                ratios.append((t1, a1 / a0))
        exact = all(alive[i][1] * 2 == alive[i - 1][1] or alive[i][0] > W for i in range(1, len(alive)))
        early = [(t1, round(q, 3)) for t1, q in ratios if t1 <= W]
        late = [(t1, round(q, 3)) for t1, q in ratios if t1 > W]
        # P-F4: near-wall patterns among starts alive at t = 4
        alive4 = death > 4
        near = (rr & 15)
        means = {}
        for p in range(16):
            sel = alive4 & (near == p)
            if np.any(sel):
                means[format(p, '04b')[::-1]] = round(float(death[sel].mean()), 2)
        spread = (max(means.values()) - min(means.values())) if means else 0
        # T-G
        rad = [radar(s, W) for s in champs]
        nested = None
        if prevD is not None and D > prevD:
            restr = [s & ((1 << (W - 1)) - 1) for s in champs]
            nested = sum(1 for s in restr if s in prev_champs)
        print(f"W={W:2d} D={D:3d} t*={2*W-2:3d} margin={D-(2*W-2):+d}  dead@0={int(np.sum(kind==2))}  "
              f"starved={starved} cancelled={cancelled} ({100*starved/max(1,starved+cancelled):.1f}% starved)  "
              f"champions={len(champs)} kinds={ckinds}")
        print(f"      kinds by death time (starved, cancelled): {bytime}")
        print(f"      halving exact to W: {exact}; early ratios {early[:6]}...; late ratios (>=16 alive) {late}")
        print(f"      mean death by near-wall bits (alive at t=4): spread {spread:.2f}; {means}")
        for s, rd in list(zip(champs, rad))[:6]:
            print(f"      champ {s:>8d}: {rd}")
        if nested is not None:
            print(f"      D rose: {nested} of {len(champs)} new champions restrict to a champion of W-1")
        summary.append((W, D, starved, cancelled, ckinds, spread, nested))
        prev_champs, prevD = set(champs), D
    print("SUMMARY", summary)
    print("WALL_CENSUS_DONE")


if __name__ == '__main__':
    main()
