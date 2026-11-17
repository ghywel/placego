#!/usr/bin/env python3
"""L1279 T1d (Local, 2026-11-01): the left founder's black-reach front B(t) in the single-seed Rule 30 orbit.

Run: python3 tests/probes/genealogy_front.py   (about a minute on the M5; no files written)

B(t) = rightmost black cell reachable from (-1, 1) through black parents. Front rule (hand induction,
reports/rule30-genealogy.md section 5): B(t+1) = B + 1 if x_(B+1)(t) = x_(B+2)(t) = 0, else the rightmost black cell
of row t+1 at or left of B. Part 1 checks the rule against the reach set on every row to 20,000 and
records the step statistics. Part 2 runs the rule alone on bit-packed rows to t = 100,000.
Predictions P1h-P1j are in the report, written before the first run.
"""
import numpy as np

# Part 1: reach set against the rule, unpacked rows
TL = 20000
WL = 2 * TL + 5
C = TL + 2
row = np.zeros(WL, dtype=bool)
row[C] = True
row1 = np.zeros(WL, dtype=bool)
row1[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
row = row1                                   # t = 1
reach = np.zeros(WL, dtype=bool)
reach[C - 1] = True
B = -1
steps = []
for t in range(1, TL):
    nrow = np.zeros_like(row)
    nrow[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
    sp = np.zeros_like(reach)
    sp[1:-1] = reach[:-2] | reach[1:-1] | reach[2:]
    reach = sp & nrow
    if not row[C + B + 1] and not row[C + B + 2]:
        Bn = B + 1
    else:
        Bn = int(np.flatnonzero(nrow[:C + B + 1]).max()) - C
    blk = np.flatnonzero(nrow) - C
    inside = blk[blk <= Bn]
    assert Bn == int(np.flatnonzero(reach).max()) - C, t
    assert np.array_equal(np.flatnonzero(reach) - C, inside), t     # every black cell of [-t-1, B] is reached
    steps.append(Bn - B)
    B, row = Bn, nrow
st = np.array(steps)
vals, cnts = np.unique(st, return_counts=True)
print(f'Part 1: rule = reach front, and reach = all black cells of [-t, B(t)], on every row t = 2..{TL}: PASS')
print('  step distribution: ' + ', '.join(f'{v:+d}: {c / len(st):.4f}' for v, c in zip(vals, cnts)) +
      f'; mean {st.mean():+.4f}')
for a, b in ((1000, 5000), (5000, 10000), (10000, 15000), (15000, 20000)):
    print(f'  mean step on t in [{a}, {b}): {st[a - 1:b - 1].mean():+.4f}')

# Part 2: the rule alone on packed rows to t = 100000
T2 = 100000
NW = (2 * T2 + 260) // 64 + 2
OFF = 64 * (NW // 2)                         # bit index of position 0
x = np.zeros(NW, dtype=np.uint64)


def setbit(arr, k):
    arr[k >> 6] |= np.uint64(1) << np.uint64(k & 63)


def bit(arr, k):
    return int((int(arr[k >> 6]) >> (k & 63)) & 1)


setbit(x, OFF)
ONE = np.uint64(1)
S63 = np.uint64(63)


def step(x):
    # bit k holds position k - OFF; left neighbour = bit k-1, right neighbour = bit k+1
    left = (x << ONE) | np.concatenate(([np.uint64(0)], x[:-1] >> S63))
    right = (x >> ONE) | np.concatenate((x[1:] << S63, [np.uint64(0)]))
    return left ^ (x | right)


def rightmost_black_at_or_below(arr, k):
    w = k >> 6
    word = int(arr[w]) & ((1 << ((k & 63) + 1)) - 1)
    while word == 0:
        w -= 1
        word = int(arr[w])
    return 64 * w + word.bit_length() - 1


x = step(x)                                  # t = 1
B = -1
checkpoints = {}
for t in range(1, T2):
    nx = step(x)
    if bit(x, OFF + B + 1) == 0 and bit(x, OFF + B + 2) == 0:
        B = B + 1
    else:
        B = rightmost_black_at_or_below(nx, OFF + B) - OFF
    x = nx
    if (t + 1) % 10000 == 0:
        checkpoints[t + 1] = B
assert checkpoints[20000] == int(np.flatnonzero(reach).max()) - C   # agrees with Part 1 at t = 20000
print('Part 2 (packed): B(t) and B(t)/t: ' + '; '.join(f'{t}: {b} ({b / t:.4f})' for t, b in checkpoints.items()))
ts = np.array(list(checkpoints)); bs = np.array(list(checkpoints.values()))
alpha = np.polyfit(np.log(ts), np.log(bs), 1)[0]
print(f'  log-log slope of B(t) on t = 10^4..10^5: {alpha:.3f}')
print('GENEALOGY_FRONT_DONE')

# Part 3 (T1e): the same front rule on Rule 30 from fair-coin rows
rng = np.random.default_rng(12791)
WR, TR = 60001, 20000
speeds = []
for run in range(10):
    r = rng.integers(0, 2, size=WR).astype(bool)
    mid = WR // 2
    B = mid + int(np.flatnonzero(r[mid:]).min())       # a black cell at or right of the middle
    tot = 0
    for t in range(TR):
        nr = np.zeros_like(r)
        nr[1:-1] = r[:-2] ^ (r[1:-1] | r[2:])
        if not r[B + 1] and not r[B + 2]:
            Bn = B + 1
        else:
            Bn = int(np.flatnonzero(nr[:B + 1]).max())
        assert 1000 + t < Bn < WR - 1000 - t                # inside the region the boundary has not reached
        tot += Bn - B
        B, r = Bn, nr
    speeds.append(tot / TR)
print('Part 3 (fair-coin rows, 10 runs, 20000 steps): mean step per run ' + ' '.join(f'{v:+.4f}' for v in speeds) +
      f'; overall {np.mean(speeds):+.4f}, spread {np.std(speeds):.4f}')
print('GENEALOGY_FRONT_PART3_DONE')
