#!/usr/bin/env python3
"""healing_bound.py: the universal recruitment (healing) frontier of a periodic background: K(t+1) = K(t)+1 iff the lab cell (K-t, t) is
black. Known diagonals equal the background, so for ANY perturbation at x >= 0 at t = 0 the leftward damage speed is at most
1 - (long-run climb rate). Exact: a walk on the background's space-time torus. Cloud, Block 23. Corrected 2026-11-02 (CL687) after
GPT's GC2404: the cycle key must carry (t - x) mod N; the old key's output is kept as healing_bound_oldkey.out."""
import numpy as np
WORDS = {'G8': '1000', 'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000'}
for name, word in WORDS.items():
    y = np.array([int(c) for c in word], dtype=np.uint8); N = len(y)
    def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
    orb = [y.copy()]; cur = cst(y)
    while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
    orb = np.array(orb); q = len(orb)
    def E(x, t, r, s): return int(orb[(t + s) % q][((t - x) + r) % N])
    rates = []
    for r in range(N):
        for s in range(q):
            # frontier state: the background's own phase at the frontier, (t mod q, (t - x_K) mod N), since E depends on (t - x);
            # the earlier key (x mod N, t mod q) lost part of the spatial phase (GPT's GC2404 correction, G28); x_K(t+1) = x_K if
            # black else x_K - 1
            x, t = 0, 0; seen = {}
            while (t % q, (t - x) % N) not in seen:
                seen[(t % q, (t - x) % N)] = (x, t)
                if E(x, t, r, s) == 0: x -= 1
                t += 1
            x0, t0 = seen[(t % q, (t - x) % N)]
            rates.append((-(x - x0)) / (t - t0))     # leftward lab speed of the frontier over one cycle
    lab_period = next(p for p in range(1, 4*q+1) if all(E(x, t + p, 0, 0) == E(x, t, 0, 0) for x in range(N) for t in range(q)))
    print(f"{name}: lab period {lab_period}, spatial {N}; universal leftward bound on any perturbation's damage speed: max over phases {max(rates):.4f}, min {min(rates):.4f}, distinct {sorted(set(round(v,4) for v in rates))}")
print("HEALING_BOUND_DONE")
