#!/usr/bin/env python3
"""L1367 (Local, 2026-11-03; GC2441's request): an independently checkable certificate for T55b's strip bound 7/44 at
S = 13. Run: python3 tests/probes/ether_strip_potentials.py make OUT.json | check IN.json

make: build the S = 13 strip graph with ether_strip.py's step (all 4 * 2^13 nodes, both inputs), reweight each edge to
w = 44 * drift + 7 (drift 0 or -7, so w = 7 or -301), and compute potentials pi by Bellman-Ford from a virtual source
(numpy). It writes pi and the 44-tick cycle of ether_strip_cycle.py's extraction.
check: rebuilds every edge with its OWN implementation of the strip step (written separately below, bit by bit from
the rule), verifies pi(v) <= pi(u) + w(u, v) on all 65,536 edges (so every cycle has total w >= 0, i.e. mean drift
>= -7/44), and verifies that the stored cycle is a closed walk of the graph with one re-anchoring in 44 ticks (mean
exactly -7/44). Together: the minimum cycle mean of the S = 13 strip model is exactly -7/44.
"""
import json
import os
import sys

TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
S = 13
here = os.path.dirname(os.path.abspath(__file__))


def check_step(ph, s, u):
    """Independent strip step: cells as a list, anchor at index 0 (ether column 2 at phase ph)."""
    cells = [TAB[(2 + i) % 7][ph] for i in (-1, 0)] + [(s >> j) & 1 for j in range(S)] + [u]   # a-1, a, a+1..a+13, a+14
    new = [cells[i - 1] ^ (cells[i] | cells[i + 1]) for i in range(1, len(cells) - 1)]     # a, a+1 .. a+13
    ph2 = (ph + 1) % 4
    if new[0] != TAB[2][ph2]:
        strip = [TAB[(2 + i) % 7][ph2] for i in range(-6, 0)] + new[0:S - 6]                # a-6 .. a+6
        return ph2, sum(b << j for j, b in enumerate(strip)), -7
    return ph2, sum(b << j for j, b in enumerate(new[1:])), 0


if sys.argv[1] == 'make':
    import numpy as np
    g = {}
    src = open(os.path.join(here, 'ether_strip.py')).read()
    saved = sys.argv
    sys.argv = ['ether_strip.py', '13']
    exec(compile(src[:src.index('for S in Ss:')], 'ether_strip', 'exec'), g)
    sys.argv = saved
    step = g['step']
    N = 4 << S
    U, V, W = [], [], []
    for ph in range(4):
        for s in range(1 << S):
            for u in (0, 1):
                ph2, s2, d = step(ph, s, u, S)
                U.append(ph * (1 << S) + s); V.append(ph2 * (1 << S) + s2); W.append(44 * d + 7)
    U, V, W = np.array(U), np.array(V), np.array(W, dtype=np.int64)
    pi = np.zeros(N, dtype=np.int64)
    for it in range(N + 1):
        cand = np.full(N, np.iinfo(np.int64).max, dtype=np.int64)
        np.minimum.at(cand, V, pi[U] + W)
        new = np.minimum(pi, cand)
        if np.array_equal(new, pi):
            break
        pi = new
    else:
        raise SystemExit('no convergence: a negative cycle under 44d + 7')
    cyc = []
    for line in os.popen('%s %s' % (sys.executable, os.path.join(here, 'ether_strip_cycle.py'))).read().splitlines():
        if line.startswith('ph'):
            ph = int(line.split()[1]); strip = line.split('strip ')[1].split()[0]
            u = int(line.split('input ')[1].split()[0])
            cyc.append([ph, sum(int(b) << j for j, b in enumerate(strip)), u])
    json.dump({'S': S, 'weights': '44*drift+7', 'iterations': it, 'pi': [int(x) for x in pi], 'cycle': cyc},
              open(sys.argv[2], 'w'))
    print('potentials converged after %d iterations; min %d, max %d; cycle of %d ticks written' % (
        it, int(pi.min()), int(pi.max()), len(cyc)))
else:
    d = json.load(open(sys.argv[2]))
    pi = d['pi']
    bad = 0; edges = 0; reanch = 0
    for ph in range(4):
        for s in range(1 << S):
            for u in (0, 1):
                ph2, s2, dr = check_step(ph, s, u)
                a, b = ph * (1 << S) + s, ph2 * (1 << S) + s2
                edges += 1; reanch += dr < 0
                if pi[b] > pi[a] + 44 * dr + 7:
                    bad += 1
    print('check: %d edges (%d re-anchoring), potential inequality violated on %d' % (edges, reanch, bad))
    cyc = d['cycle']; tot = 0; ok = True
    for i, (ph, s, u) in enumerate(cyc):
        ph2, s2, dr = check_step(ph, s, u)
        nph, ns, _ = cyc[(i + 1) % len(cyc)]
        ok &= (ph2, s2) == (nph, ns); tot += dr
    print('stored cycle: closed walk %s, %d ticks, total drift %d, mean %s' % (ok, len(cyc), tot,
          '%d/%d' % (tot, len(cyc))))
    print('VERDICT: minimum cycle mean of the S = 13 strip model is exactly -7/44: %s' % (bad == 0 and ok and
          tot * 44 == -7 * len(cyc)))
