#!/usr/bin/env python3
"""L1362 T54 (Local, 2026-11-03): a rooted-front observer, sharper than A2, for GC2430's tail question.
reports/rule30-genealogy.md section 58 (predictions written first). Run:
python3 tests/probes/rooted_front.py W [W ...]

Background E: the A1 reference at (c0, c1) = (4, 3) (ether left of 0, black at 0, white right). Cut b: rows agreeing
with E at time 0 on x <= b, anything beyond. Target: L(222) >= -23, L the leftmost difference (agreement on x <= -24).
delta = G XOR E evolves by the exact mismatch identity with E's values as coefficients:
    delta' = dl ^ (~r & dc) ^ (~c & dr) ^ (dc & dr),   c = E(t, x), r = E(t, x + 1).
A rooted state (L, w) at time t: delta = 0 left of L, delta(L) = 1, w = ternary delta on L+1 .. L+W (2 = unknown),
unknown beyond. A half-line state (m) at time t: delta = 0 on x <= m, unknown beyond; it is the union of rooted
(m + 1, unknown word) and the half-line state (m + 1). A2 (three-valued simulation of a half-line state) certifies
(t, m) iff m >= thr[t], with thr[222] = -24 and thr[t] = thr[t+1] if E(t, thr[t+1]) is black, else thr[t+1] + 1
(GC2423's h_t). One tick: evaluate delta' three-valued on L-1 .. L+W, then branch on unknown cells, scanning right
from L-1, until the new front is found (rooted) or the window runs out (half-line state at L+W). Rooted states with
A2 certifying (t, L - 1) are pruned (safe). At 222 a live state is safe iff L >= -23. No unsafe state proves the
target for every tail (all real trajectories lie in some branch).
Controls: thr[0] = 112 (GC2423); cut 112 certified; cut 86 must NOT certify (the flip at 87 is a real witness);
containment replay of actual whole-line trajectories (random tails, the flip-87 witness) against the live states.
"""
import random
import sys
import time

ALL = '--all' in sys.argv
ONLY = [tuple(int(v) for v in a.split(',')) for a in sys.argv[1:] if ',' in a]   # e.g. 0,3: restrict --all
Ws = [int(a) for a in sys.argv[1:] if a != '--all' and ',' not in a] or [0, 4, 8]
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
# A1's 28 entries (c0, c1): (t1, xB), from EtherEdgeZero.lean / the A1 essay.
ENTRY = {(0, 0): (81, -19), (0, 1): (13, -5), (0, 2): (10, 2), (0, 3): (186, -26), (1, 0): (185, -27), (1, 1): (17, -6),
         (1, 2): (9, 1), (1, 3): (9, 1), (2, 0): (8, 0), (2, 1): (17, -7), (2, 2): (16, -7), (2, 3): (8, 0),
         (3, 0): (7, -1), (3, 1): (7, -1), (3, 2): (16, -8), (3, 3): (7, -1), (4, 0): (6, -2), (4, 1): (148, -23),
         (4, 2): (6, -2), (4, 3): (222, -37), (5, 0): (221, -38), (5, 1): (148, -24), (5, 2): (5, -3), (5, 3): (5, -3),
         (6, 0): (4, -4), (6, 1): (25, -11), (6, 2): (4, -4), (6, 3): (82, -18)}
LO, HI = -1300, 1300
X = 2

# Three-valued mismatch identity: TERN[dl, dc, dr, c, r].
TERN = {}
for dl in (0, 1, X):
    for dc in (0, 1, X):
        for dr in (0, 1, X):
            for c in (0, 1):
                for r in (0, 1):
                    vals = {a ^ ((1 - r) & b) ^ ((1 - c) & d) ^ (b & d)
                            for a in ((0, 1) if dl == X else (dl,))
                            for b in ((0, 1) if dc == X else (dc,))
                            for d in ((0, 1) if dr == X else (dr,))}
                    TERN[dl, dc, dr, c, r] = vals.pop() if len(vals) == 1 else X


def setup(c0, c1):
    """The A1 reference at (c0, c1) and its entry target: sets the globals used below."""
    global C0, C1, T, Q, rows, thr
    C0, C1 = c0, c1
    t1, xB = ENTRY[c0, c1]
    T, Q = t1, xB + 13
    rows = [[E0(x) for x in range(LO, HI + 1)]]
    for t in range(T):
        r = rows[-1]
        rows.append([0] + [r[i - 1] ^ (r[i] | r[i + 1]) for i in range(1, len(r) - 1)] + [0])
    assert all(E(T, x) == TAB[(x + C0) % 7][(T + C1) % 4] for x in range(-300, xB + 1)), 'E is the ether left of xB'
    thr = [0] * (T + 1)
    thr[T] = Q
    for t in range(T - 1, -1, -1):
        thr[t] = thr[t + 1] if E(t, thr[t + 1]) else thr[t + 1] + 1


def E0(x):
    return TAB[(x + C0) % 7][C1 % 4] if x < 0 else int(x == 0)


def E(t, x):
    assert LO + t < x < HI - t, (t, x)
    return rows[t][x - LO]


def cert(t, m):
    return m >= thr[t]


def expand_half(t, m, W, out):
    """Rooted states covering the half-line state (zero up to m) at time t, A2-certified tails dropped."""
    while not cert(t, m):
        out.add((m + 1, (X,) * W))
        m += 1


def step(t, L, w, W, out):
    """Successor states at t + 1 of rooted (L, w) at time t."""
    d = {L - 2: 0, L - 1: 0, L: 1}
    for i, v in enumerate(w):
        d[L + 1 + i] = v
    get = lambda x: d.get(x, X)
    nd = {x: TERN[get(x - 1), get(x), get(x + 1), E(t, x), E(t, x + 1)] for x in range(L - 1, L + W + 1)}
    nget = lambda x: nd.get(x, X)
    p = L - 1
    while True:
        if p > L + W:
            expand_half(t + 1, L + W, W, out)        # zero through L + W, unknown beyond
            return
        v = nget(p)
        if v != 0:                                   # 1, or unknown branched to 1
            out.add((p, tuple(nget(p + 1 + i) for i in range(W))))
        if v == 1:
            return
        p += 1                                       # 0, or unknown branched to 0


def run(b, W, track=None):
    """Live rooted states per tick from cut b; returns (certified, max live, unsafe states at T)."""
    live = set()
    expand_half(0, b, W, live)
    peak = len(live)
    for t in range(T):
        if track is not None:
            track(t, live)
        nxt = set()
        for L, w in live:
            step(t, L, w, W, nxt)
        live = {(L, w) for L, w in nxt if not cert(t + 1, L - 1)}
        peak = max(peak, len(live))
    if track is not None:
        track(T, live)
    unsafe = sorted(L for L, w in live if L <= Q)
    return not unsafe, peak, unsafe


def contained(L, win, live):
    return any(L == L2 and all(a == X or a == bb for a, bb in zip(w2, win)) for L2, w2 in live)


def replay(b, W, row0):
    """Actual trajectory of a whole-line row against the live states: returns the first uncovered tick, or None."""
    lo = LO
    g = list(row0)
    act = []
    for t in range(T + 1):
        dl = [g[i] ^ rows[t][i] for i in range(t + 1, len(g) - t - 1)]
        L = next((lo + i + t + 1 for i, v in enumerate(dl) if v), None)
        act.append((L, None if L is None else tuple(dl[L - lo - t - 1 + 1 + k] for k in range(W))))
        g = [0] + [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)] + [0]
    bad = []
    done = [False]

    def track(t, live):
        if done[0] or bad:
            return
        L, win = act[t]
        if L is None or cert(t, L - 1):
            done[0] = True                           # healed or A2-safe from here on
            return
        if not contained(L, win, live):
            bad.append(t)
    run(b, W, track)
    return bad[0] if bad else None, act[T][0]


def flips():
    """Single flips p in [0, thr[0]] that change a target cell: each shows that cut p - 1 does not suffice."""
    n = HI - LO + 1
    mask = (1 << n) - 1
    base = sum(E0(x) << (x - LO) for x in range(LO, HI + 1))
    ref = base
    for t in range(T):
        ref = ((ref << 1) ^ (ref | (ref >> 1))) & mask
    win = sum(1 << (x - LO) for x in range(LO + T + 1, Q + 1))   # valid cells x <= Q at time T
    out = []
    for p in range(0, thr[0] + 1):
        a = base ^ (1 << (p - LO))
        for t in range(T):
            a = ((a << 1) ^ (a | (a >> 1))) & mask
        if (a ^ ref) & win:
            out.append(p)
    return out


def least_cut(W):
    """Least b with every cut from b to thr[0] certified (certification is monotone in b, checked downward)."""
    b = thr[0]
    while b > Q - T and run(b - 1, W)[0]:
        b -= 1
    return b


rng = random.Random(54)
if ALL:
    worst = {}
    for (c0, c1) in sorted(ONLY or ENTRY):
        setup(c0, c1)
        fl = flips()
        line = ['(%d,%d) t1 %3d xB %3d: A2 cut %3d' % (c0, c1, T, Q - 13, thr[0])]
        for W in Ws:
            lc = least_cut(W)
            worst[W] = max(worst.get(W, -10**9), lc)
            line.append('rooted W=%d cut %3d' % (W, lc))
        line.append('largest witness flip %s -> cut %s fails' % ((fl[-1], fl[-1] - 1) if fl else ('none', '-')))
        print('; '.join(line), flush=True)
    print('common cutoff over these entries: A2 112 over all 28 (GC2421); rooted %s' % ', '.join(
        'W=%d %d' % (W, worst[W]) for W in Ws))
    print('ROOTED_FRONT_ALL_DONE')
    sys.exit(0)
setup(4, 3)
print('A2 threshold thr[0] = %d (GC2423: 112)' % thr[0])
assert thr[0] == 112
for W in Ws:
    t0 = time.time()
    res = {}
    for b in (112, 111, 110, 105, 100, 95, 90, 88, 87, 86):
        ok, peak, unsafe = run(b, W)
        res[b] = ok
        print('W=%2d cut %3d: %s; peak live states %d; unsafe at 222: %d (min L %s)' % (
            W, b, 'CERTIFIED' if ok else 'not certified', peak, len(unsafe), unsafe[0] if unsafe else '-'), flush=True)
    assert res[112] and not res[86], 'soundness control failed'
    least = min(b for b in res if all(res[c] for c in res if c >= b))
    print('W=%2d least cut certified with every larger tested cut: %d (%.1f s)' % (W, least, time.time() - t0), flush=True)
    # Containment replay: the flip-87 witness at cut 86, random tails at cuts 86, 100, 111.
    cases = [(86, 'flip at 87', [E0(x) ^ (x == 87) for x in range(LO, HI + 1)])]
    for b in (86, 100, 111):
        for k in range(4):
            cases.append((b, 'random tail', [E0(x) if x <= b else rng.getrandbits(1) for x in range(LO, HI + 1)]))
    unc = 0
    for b, name, row0 in cases:
        first, Lend = replay(b, W, row0)
        unc += first is not None
        if first is not None or name.startswith('flip'):
            print('   replay cut %d %s: actual L(222) = %s; first uncovered tick %s' % (b, name, Lend, first), flush=True)
    print('W=%2d containment replay: %d of %d trajectories uncovered (must be 0)' % (W, unc, len(cases)), flush=True)
    assert unc == 0
print('ROOTED_FRONT_DONE')
