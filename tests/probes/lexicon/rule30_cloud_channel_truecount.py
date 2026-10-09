#!/usr/bin/env python3
"""rule30_cloud_channel_truecount.py: TC2, the TRUE language of column 1 next to 0101 (§8.20's channel), by SAT.

RUN-ON:     cpu, one core (Python 3, python-sat); up to CAP_SECONDS
COMMAND:    NP_SCRATCH_TC=... python3 tests/probes/lexicon/rule30_cloud_channel_truecount.py [NMAX=120] [CAP=1800]

Why. §8.20 bounds the information column 1 can carry next to the period-2 column 0101 by layer relaxations: a layer
of m cells fed ANY input. The certified value is 0.1236 bits per visible bit at m = 28 (SQ6). Power iteration levels
off near 0.122. "Whether the limit is exactly positive is not proved." The one-hole wall at p = 2 is exactly 0101,
and TC (rule30_cloud_hole_truecount.py, audited by GPT's GC871) decides membership in the TRUE language: no free
input, only actual right halves. Its words grow slowly here (about 2^0.12 a hole), so much longer words are in reach
than for the odd walls. This probe runs TC's search at p = 2 and certifies a ceiling from the true minimal
forbidden words F. It uses the spectral radius rho of F's Aho-Corasick automaton, pruned to states with an
infinite future, bounded above by Collatz-Wielandt: rho <= max_i (A v)_i / v_i for any positive v, evaluated with
v from power iteration plus a 1e-9 floor and a 1e-12 margin. Since the true language avoids F, its entropy is at
most log2 rho bits per visible bit, whatever the right half. TC's a_400^(1/400) is printed beside it.

Record searched: "channel" with "(true|real) (language|right halves?)" and "(SAT|bound|certif)" -> §8.20 (layer
relaxations; 0.1229 and 0.1222 at m = 27, 28; certified 0.1236 in SQ6), rule30_bottleneck.py (real right halves
never left the width-16 layer's language), rule30_one_hole_widths.py. L494's XC: OHC at p = 2 reproduces §8.20's
table to width 22. No true-language count at p = 2 is in the record.

PREDICTIONS, written 2026-10-09 22:16 BST, before any run of this script.
  TC2-C1 (control, must hold): the counts |L_n| for n <= 11 equal a direct enumeration of every initial row on 21
         cells (bit-sliced).
  TC2-C2 (control, must hold): 200 reservoir-sampled SAT models replay to their words by direct simulation.
  TC2-P1 (0.6): the certified true ceiling log2 rho at the largest N reached is below §8.20's certified 0.1236.
  TC2-P2 (0.4): it is below 0.110.
  TC2-P3 (consistency, 0.8): it is above the measured typical rate of 0.080 bits per visible bit (§8.20,
         rule30_metric.py). A failure would mean that the measurement or this instrument is wrong.
  TC2-U, the unexpected check (0.4): some true minimal forbidden word is longer than 28 holes, one turn of the wheel.
  Counterfactual. If TC2-P1 fails, the true language's constraints up to N holes are no stronger than a 28-cell
  layer's, and the layer bound stays the record's best. If it holds, the record gains a sharper certified ceiling
  on the channel, and with it on the cost side of Q1.
"""
import math
import os
import random
import sys
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_cloud_hole_truecount as tc                       # noqa: E402

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 120
tc.CAP = float(sys.argv[2]) if len(sys.argv) > 2 else 1800.0
P = 2
BOUND_820 = 0.1236
MEASURED = 0.080


def brute_counts(nmax):
    T = (nmax - 1) * P
    n = T + 1
    full = (1 << (1 << n)) - 1
    x = tc_masks(n) + [0, 0]
    holes = []
    for t in range(T + 1):
        if t % P == 0:
            holes.append(x[0])
        w = tc.wall(t, P)
        left = [full if w else 0] + x[:-1]
        right = x[1:] + [0]
        x = [left[i] ^ (x[i] | right[i]) for i in range(len(x))]
    counts = []
    for N in range(1, nmax + 1):
        c = 0
        for w in range(1 << N):
            m = full
            for k in range(N):
                m &= holes[k] if (w >> k) & 1 else ~holes[k]
                if not m:
                    break
            c += 1 if m else 0
        counts.append(c)
    return counts


def tc_masks(n):
    nbytes = max(1, (1 << n) // 8)
    out = []
    for i in range(n):
        if i < 3:
            pat = bytes([(0xAA, 0xCC, 0xF0)[i]]) * nbytes
        else:
            b = 1 << (i - 3)
            pat = (b'\x00' * b + b'\xff' * b) * (nbytes // (2 * b))
        out.append(int.from_bytes(pat, 'little') & ((1 << (1 << n)) - 1))
    return out


def spectral_ceiling(F):
    """Collatz-Wielandt upper bound on the spectral radius of the F-avoiding automaton (live states only)."""
    goto, fail, out = [{}], [0], [False]
    for w in F:
        s = 0
        for ch in w:
            if ch not in goto[s]:
                goto.append({})
                fail.append(0)
                out.append(False)
                goto[s][ch] = len(goto) - 1
            s = goto[s][ch]
        out[s] = True
    q = deque()
    for ch in '01':
        if ch in goto[0]:
            q.append(goto[0][ch])
        else:
            goto[0][ch] = 0
    while q:
        s = q.popleft()
        out[s] = out[s] or out[fail[s]]
        for ch in '01':
            if ch in goto[s]:
                u = goto[s][ch]
                fail[u] = goto[fail[s]][ch]
                q.append(u)
            else:
                goto[s][ch] = goto[fail[s]][ch]
    states = [s for s in range(len(goto)) if not out[s]]
    succ = {s: [goto[s][ch] for ch in '01' if not out[goto[s][ch]]] for s in states}
    alive = set(states)
    changed = True
    while changed:                                         # keep states with an infinite future
        changed = False
        for s in list(alive):
            if not any(u in alive for u in succ[s]):
                alive.discard(s)
                changed = True
    live = sorted(alive)
    idx = {s: i for i, s in enumerate(live)}
    adj = [[idx[u] for u in succ[s] if u in alive] for s in live]
    v = [1.0] * len(live)
    acc = [0.0] * len(live)
    for it in range(900):
        nv = [sum(v[j] for j in adj[i]) for i in range(len(live))]
        mx = max(nv)
        v = [x / mx for x in nv]
        if it >= 600:                                      # average late iterates (handles periodic classes)
            acc = [a + x for a, x in zip(acc, v)]
    w = [a + 1e-9 for a in acc]
    ratio = max(sum(w[j] for j in adj[i]) / w[i] for i in range(len(live)))
    return ratio + 1e-12, len(live)


def main():
    random.seed(7)
    os.makedirs(tc.SCRATCH, exist_ok=True)
    bc = brute_counts(11)
    print('direct counts n = 1 .. 11: %s' % bc, flush=True)
    levels, mfw, models, reached = tc.run(P, NMAX)
    counts = [len(levels[n]) for n in range(1, reached + 1)]
    c1 = len(counts) >= 11 and counts[:11] == bc
    c2 = len(models) >= 200 and all(tc.simulate(row, P, len(w)) == [int(ch) for ch in w] for w, row in models)
    F = sorted(set(mfw), key=lambda w: (len(w), w))
    with open(os.path.join(tc.SCRATCH, 'tc_p2.txt'), 'w') as fh:
        fh.write('counts %s\nreached %d\n' % (counts, reached))
        fh.write('\n'.join(F) + '\n')
    rho, nlive = spectral_ceiling(F)
    a, ceil6 = tc.avoid_count_bound(F, 400)
    by_len = {}
    for w in F:
        by_len[len(w)] = by_len.get(len(w), 0) + 1
    print('TC2-C1 (counts to 11 equal the direct enumeration): %s' % ('PASS' if c1 else 'FAIL'))
    print('TC2-C2 (%d models replayed): %s' % (len(models), 'PASS' if c2 else 'FAIL'))
    print('reached N = %d; counts %s' % (reached, counts))
    print('minimal forbidden words by length: %s' % sorted(by_len.items()))
    print('certified ceiling: rho <= %.9f (%d live states), log2 = %.6f bits per visible bit; a_400^(1/400) <= %.6f'
          % (rho, nlive, math.log2(rho), ceil6), flush=True)
    ok = c1 and c2
    nd = 'NOT DECIDED (controls)'
    hb = math.log2(rho)
    print('TC2-P1 (below 0.1236): %s' % (nd if not ok else ('HELD' if hb < BOUND_820 else 'REFUTED')))
    print('TC2-P2 (below 0.110): %s' % (nd if not ok else ('HELD' if hb < 0.110 else 'REFUTED')))
    print('TC2-P3 (above the measured 0.080): %s' % (nd if not ok else ('HELD' if hb > MEASURED else 'REFUTED')))
    print('TC2-U (a minimal forbidden word longer than 28): %s' % (nd if not ok else (
        'HELD' if any(len(w) > 28 for w in F) else 'REFUTED')))


if __name__ == '__main__':
    main()
