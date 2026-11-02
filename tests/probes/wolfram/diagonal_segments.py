#!/usr/bin/env python3
"""diagonal_segments.py T: the single seed to time T; the centre column as the parity of OR-events along its past diagonal
x = s - t; the four segments; settledness of the band samples (period dividing 32 in s for fixed left diagonal e). Cloud, Block 18."""
import sys, numpy as np
T = int(sys.argv[1]); W = 2*T + 3; c = T + 1
X = np.zeros((T+1, W), dtype=np.uint8); X[0, c] = 1
for t in range(T):
    r = X[t]; n = np.zeros_like(r)
    n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); X[t+1] = n
centre = X[:, c]
# OR-event bits along the diagonal of time t: o(s) = x_{s-t}(s) OR x_{s-t+1}(s)
def events(t):
    s = np.arange(t); xs = X[s, c + s - t + 1]; xs1 = X[s, c + s - t + 2]; return xs | xs1
ok = 0; bad = 0
for t in range(64, T+1):
    e = events(t); par = int(e.sum() & 1)
    ok += (par == int(centre[t])); bad += (par != int(centre[t]))
print(f"parity identity x_0(t) = XOR of OR-events: holds {ok}, fails {bad}")
# settledness: for diagonal e (= 2s - t) sampled at s = (e+t)/2 with e <= t/3: compare with the value at the same s mod 32 on a late time
# build the eternal-strip values: left diagonal e at time s is X[s, c - s + e]; take reference from the latest settled time with the same s mod 32
import collections
samples = collections.defaultdict(set); counts = collections.Counter()
tot = 0; near = 0
for t in range(96, T+1, 3):
    for s in range(t//2, 2*t//3 + 1):
        e = 2*s - t + 1
        if e < 0 or e > t//3: continue
        v = int(X[s, c - s + e] | X[s, c - s + e + 1])
        samples[(e, s % 32)].add(v); tot += 1
confl = sum(1 for k, v in samples.items() if len(v) > 1)
print(f"band samples: {tot} (e <= t/3); distinct (e, s mod 32) keys {len(samples)}; keys with conflicting values {confl} ({confl/len(samples):.4f})")
# where are the conflicts (e relative to its largest t)?
conf_e = sorted(k[0] for k, v in samples.items() if len(v) > 1)
print("  conflicting e values (first 30):", conf_e[:30], "max e", max(conf_e) if conf_e else None)
# densities of OR-events per segment at a few t
for t in (1024, 2048, 4096, T):
    if t > T: continue
    e = events(t); seg = [(0, t//2), (t//2, 2*t//3), (2*t//3, int(0.8*t)), (int(0.8*t), t)]
    print(f"t={t}: OR-event density by segment (white, settled band, settling zone, core):", [round(float(e[a:b].mean()), 3) if b > a else None for a, b in seg])
print("DIAG_DONE")
