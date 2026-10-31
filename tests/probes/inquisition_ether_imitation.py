#!/usr/bin/env python3
"""inquisition_ether_imitation.py: do white-sea champions imitate the kit's period-seven ether beside the wall? (T-W)

RUN-ON:     cpu (Python 3 + numpy), a few minutes
COMMAND:    python3 tests/probes/inquisition_ether_imitation.py [WMAX=20] [PMAX=300]

The kit's normal form, as in inquisition_wall_census.py: depth 0 is the white wall, and for depths k >= 1
x_k(t+1) = x_(k+1)(t) XOR (x_k(t) OR x_(k-1)(t)). The clock lives while depth 1 is black at every even time.
Reference: the left half of the kit's 7 x 4 ether (Rule30PeriodTwoCoupled.etherLeft, ether_col1_black). Generated here by
running the wall form from the period-seven sea 1100001 repeated (GPT GC2329), with depth-1 trace 1011 repeated and
time period 4 (both checked).
Part 1 (P-W1): for each W <= WMAX, every start supported on depths 1..W is run to its death. At every even time while
alive, the agreement of depths 2..6 (and 2..14) with each of the ether's two even-time rows is accumulated. Each start's
score is its better alignment over its whole life (the ether row at its time t = 0 mod 4 is tau0 and at t = 2 mod 4 is
tau0 + 2). Means are printed for the champions (death = D(W)), for all starts alive at t = 4, and for starts dying at
t >= W. The checkerboard (T-H2's reference) is re-measured the same way as a control.
Part 2 (P-W2): the death time D_e(W) of the exact ether patch (depths 1..W = the ether at its phase 1, white beyond),
for W <= PMAX, against D(W) (exhaustive here for W <= WMAX) and the arrival time W of the white tail's news at depth 1.
Predictions P-W1, P-W2: reports/inquisition-20261031.md (round 6), committed before this ran.
"""
import sys
import numpy as np

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
PMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
SEA = (1, 1, 0, 0, 0, 0, 1)


def step(x):
    nxt = np.zeros_like(x)
    nxt[1:-1] = x[2:] ^ (x[1:-1] | x[:-2])
    return nxt


def ether_rows(depth):
    """The ether's left half on depths 0..depth-1 for times 0..7 (from the period-seven sea; depth 0 the wall)."""
    T = 8
    D = depth + 2 * T + 8
    x = np.zeros(D, dtype=np.uint8)
    for k in range(1, D - 1):
        x[k] = SEA[(k - 1) % 7]
    rows = []
    for t in range(T):
        rows.append(x[:depth].copy())
        x = step(x)
    rows = np.array(rows)
    assert all(rows[t, 1] == (1, 0, 1, 1)[t % 4] for t in range(T)), "depth-1 trace 1011"
    assert np.array_equal(rows[:4, :depth - 2 * T], rows[4:8, :depth - 2 * T]), "time period 4"
    return rows


def part1():
    ER = ether_rows(16)
    refs = {'ether': (ER[0], ER[2]), 'checker': (np.array([d % 2 for d in range(16)], dtype=np.uint8),) * 2}
    for W in range(8, WMAX + 1):
        n = 1 << W
        r = np.arange(n, dtype=np.int64)
        depth = 3 * W + 50
        x = np.zeros((depth + 2, n), dtype=np.uint8)
        for k in range(1, W + 1):
            x[k] = (r >> (k - 1)) & 1
        death = np.full(n, -1, dtype=np.int64)
        acc = {(nm, win, al): np.zeros(n) for nm in refs for win in (6, 14) for al in (0, 1)}
        cnt = np.zeros(n)
        t = 0
        while True:
            if t % 2 == 0:
                newly = (death < 0) & (x[1] == 0)
                death[newly] = t
                alive = death < 0
                if not np.any(alive[1:]):
                    break
                cnt[alive] += 1
                for nm, (r0, r2) in refs.items():
                    for al in (0, 1):
                        row = (r0, r2)[((t // 2) + al) % 2]
                        for win in (6, 14):
                            a = (x[2:win + 1] == row[2:win + 1, None]).mean(axis=0)
                            acc[(nm, win, al)][alive] += a[alive]
            x[1:depth + 1] = step(x[0:depth + 2])[1:depth + 1]
            t += 1
        D = death[1:].max()
        groups = {'champions': np.nonzero(death == D)[0], 'alive@4': np.nonzero(death > 4)[0],
                  'dying>=W': np.nonzero(death >= W)[0]}
        out = []
        for nm in refs:
            for win in (6, 14):
                score = np.maximum(acc[(nm, win, 0)], acc[(nm, win, 1)]) / np.maximum(cnt, 1)
                out.append(f"{nm}2..{win}: " + ', '.join(f"{g} {score[idx].mean():.3f}" for g, idx in groups.items()))
        print(f"W={W:2d} D={D:3d} champions {len(groups['champions'])} | " + ' | '.join(out), flush=True)
    return


def death_time(row_bits, cap):
    """Death time of one start (depths 1..len(row_bits)) in the wall form."""
    W = len(row_bits)
    depth = W + cap + 8
    x = np.zeros(depth + 2, dtype=np.uint8)
    x[1:W + 1] = row_bits
    for t in range(cap + 1):
        if t % 2 == 0 and x[1] == 0:
            return t
        x = step(x)
    return None


def part2(dtab):
    ER = ether_rows(PMAX + 2)
    print("ether patch: W, D_e(W), D_e(W) - W, and D(W) where known", flush=True)
    vals = []
    for W in range(2, PMAX + 1):
        de = death_time(ER[0, 1:W + 1], 4 * W + 100)
        vals.append((W, de))
        if W <= 40 or W % 20 == 0:
            print(f"  W={W:3d} D_e={de} D_e-W={None if de is None else de - W}"
                  + (f" D(W)={dtab[W]}" if W in dtab else ""), flush=True)
    excess = [de - W for W, de in vals if de is not None]
    print(f"D_e(W) - W over W = 2..{PMAX}: min {min(excess)}, max {max(excess)}; uncensored {len(excess)} of {len(vals)}")


def main():
    part1()
    dtab = {}
    from itertools import product
    for W in range(2, min(WMAX, 18) + 1):
        best = 0
        n = 1 << W
        r = np.arange(n, dtype=np.int64)
        depth = 3 * W + 50
        x = np.zeros((depth + 2, n), dtype=np.uint8)
        for k in range(1, W + 1):
            x[k] = (r >> (k - 1)) & 1
        death = np.full(n, -1, dtype=np.int64)
        t = 0
        while True:
            if t % 2 == 0:
                death[(death < 0) & (x[1] == 0)] = t
                if not np.any(death[1:] < 0):
                    break
            x[1:depth + 1] = step(x[0:depth + 2])[1:depth + 1]
            t += 1
        dtab[W] = int(death[1:].max())
    part2(dtab)
    print("ETHER_IMITATION_DONE")


if __name__ == '__main__':
    main()
