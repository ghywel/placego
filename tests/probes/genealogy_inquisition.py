#!/usr/bin/env python3
"""L1283 (Local, 2026-11-01): T5 of reports/rule30-genealogy.md section 15 (predictions written there first).
Run: python3 tests/probes/genealogy_inquisition.py   (about a minute; no files written)

(a) The deep-side law on the actual single-seed orbit: at every episode start to t = 5000, with w the first K = 64
    cells behind the front, check L = 1 + lead1(Phi^r w) and next deep word = sigma^L Phi^(r+1) w (determined digits),
    where Phi(w)_j = w_j XOR (w_(j-1) OR w_(j-2)), w_0 = 1, w_(-1) = 0 (the right-edge map).
(b) Traps in the left band: rightward prefix fronts B(t+1) = max{i <= B+1 : black} started at every black cell
    within 300 of the left edge at t0 = 2000 and 8000, run 4000 steps; positive control, the leftward follower
    L(t+1) = min{i >= L-1 : black} started 300 from the left edge (planned control; its prediction was wrong) and
    from the first black cell at offset >= 3 (added control).
(d) T5d: rightward prefix fronts at every black offset 0..40 at each of 64 start times t0 = 3000..3063, 2000 steps.
"""
import numpy as np


def Phi(w):
    """one step of the right-edge map on a digit array w[0..K-1] (digit j+1 at index j)."""
    w1 = np.concatenate(([1, 0][::-1], w))           # index 0 = digit -1 (white), 1 = digit 0 (black front)
    out = w ^ (w1[1:-1] | w1[:-2])
    return out


T = 5000 + 4000 + 8000
T = 12000
W = 2 * T + 9
C = T + 4
rows = np.zeros((T + 1, W), dtype=np.uint8)
rows[0, C] = 1
for t in range(T):
    rows[t + 1, 1:-1] = rows[t, :-2] ^ (rows[t, 1:-1] | rows[t, 2:])

# (a) episodes of the left founder's front, B(1) = -1
K = 64
B = -1
t = 1
checked = fails = 0
while t < 5000:
    u, Bu = t, B
    w = rows[u, C + Bu - np.arange(1, K + 1)].astype(np.uint8)
    q = np.flatnonzero(rows[u, C + Bu + 1:])[0]      # white gap M = q
    r = q // 2
    v, Bv = u + r, Bu + r
    for s in range(r):                                # the front advances r times
        assert rows[u + s + 1, C + Bu + s + 1] == 1
    actual = rows[v, C + Bv - np.arange(1, K + 1)]
    pred = w.copy()
    for _ in range(r):
        pred = Phi(pred)
    if not np.array_equal(pred, actual):
        fails += 1
    lead = int(np.argmin(pred)) if (pred == 0).any() else K
    L = 1 + lead
    Bn = int(np.flatnonzero(rows[v + 1, :C + Bv + 2]).max()) - C
    if Bn != Bv - (L - 1):
        fails += 1
    wn = rows[v + 1, C + Bn - np.arange(1, K + 1)]
    predn = Phi(pred)[L:]
    if not np.array_equal(predn, wn[:K - L]):
        fails += 1
    checked += 1
    t, B = v + 1, Bn
print(f'(a) deep-side law on the seed: {checked} episodes to t = {t}, {fails} failures '
      f'(Phi^r on 64 digits, L = 1 + lead1, next word = sigma^L Phi^(r+1) w)')

# (b) traps
for t0 in (2000, 8000):
    left = C - t0                                     # index of the left edge at t0
    starts = [k for k in range(0, 301) if rows[t0, left + k] == 1]
    fronts = np.array([left + k for k in starts])
    lf = left + 300
    while rows[t0, lf] == 0:
        lf += 1
    lf2 = left + 3                                    # added control: started next to the edge
    while rows[t0, lf2] == 0:
        lf2 += 1
    minoff = np.full(len(fronts), 10 ** 9)
    for s in range(4000):
        tt = t0 + s
        nxt = rows[tt + 1]
        new = []
        for b in fronts:
            seg = np.flatnonzero(nxt[:b + 2])
            new.append(seg.max())
        fronts = np.array(new)
        edge = C - (tt + 1)
        off = fronts - edge
        if s >= 2000:
            minoff = np.minimum(minoff, off)
        seg = np.flatnonzero(nxt[lf - 1:])
        lf = lf - 1 + seg.min()
        seg = np.flatnonzero(nxt[lf2 - 1:])
        lf2 = lf2 - 1 + seg.min()
    final = fronts - (C - (t0 + 4000))
    lfoff = lf - (C - (t0 + 4000))
    lf2off = lf2 - (C - (t0 + 4000))
    trapped = int(np.sum(final <= 1000))
    print(f'(b) t0 = {t0}: {len(starts)} rightward prefix fronts from offsets 0..300; final offsets min {final.min()}, '
          f'median {int(np.median(final))}, max {final.max()}; ending within 1000 of the left edge: {trapped}; '
          f'min offset over the last 2000 steps {int(minoff.min())}; leftward follower from offset 300 ends at {lfoff} '
          f'(planned control, wrong prediction); from the first black at offset >= 3 ends at {lf2off} (added control)')
worst = 10 ** 9
nfront = 0
for t0 in range(3000, 3064):
    left = C - t0
    fr = [left + k for k in range(41) if rows[t0, left + k] == 1]
    nfront += len(fr)
    for s in range(2000):
        nxt = rows[t0 + s + 1]
        fr = [int(np.flatnonzero(nxt[:b + 2]).max()) for b in fr]
    worst = min(worst, min(b - (C - (t0 + 2000)) for b in fr))
print(f'(d) {nfront} rightward prefix fronts over 64 start times, offsets 0..40; smallest final offset after 2000 steps: {worst}')
print('GENEALOGY_INQUISITION_DONE')
