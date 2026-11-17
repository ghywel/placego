"""chink_tree.py: the sixteen left sides by chink (CL749). A strip's name in the tree (`A0.f1.f2...`) lists the forks at
which it departs from the seed's path. Starting from the seed on 894,236 wheels, at each fork f of the name in order, once
the front has cleared the fork (the seed's own settling tick of f from TAU.npy plus a margin for the first, and from the
previous chink's tick at the front's slowest plausible speed 0.70 wheels a tick plus a margin for the rest), the cell on
the fork's child f + 1 is flipped: the child's parent is white for ever, the error never heals, and the configuration
switches to the other branch (the branch law, fork_rule_check.py). After the last chink the row is compared with every
strip at every phase every 2,048 ticks from the earliest plausible settling on, until it matches; the match, its tick
and the ticks after the last chink are printed with the target. Usage: python3 chink_tree.py ROWSDIR STRIPNAME TAU.npy"""
import sys, os, time
import numpy as np
ROWS = sys.argv[1]; NAME = sys.argv[2]; tau = np.load(sys.argv[3])
K = 894236; MASK = (1 << K) - 1; P = 32; SLOW = 0.70; MARGIN = 3000
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
strips = {}
for f in sorted(os.listdir(ROWS)):
    if f.endswith('.bin'):
        r = int.from_bytes(open(f"{ROWS}/{f}", 'rb').read(), 'little') & MASK; c = [r]
        for _ in range(P - 1): c.append(step(c[-1]))
        strips[f[:-4]] = c
forks = [int(p) for p in NAME.split('.')[1:]]
sched = []; prev_t = None; prev_c = None
for f in forks:
    t_f = int(tau[f]) + MARGIN if prev_t is None else prev_t + int((f - prev_c) / SLOW) + MARGIN
    sched.append((f + 1, t_f)); prev_t, prev_c = t_f, f + 1
print(f"target {NAME}: chinks at (wheel, tick) {sched}")
t0 = time.time(); x = 1; t = 0
for (c, tc) in sched:
    while t < tc: x = step(x); t += 1
    assert (x >> (c - 1)) & 1 == 0, f"the fork wheel {c-1} is not white at the chink tick {tc}: the front has not cleared it"
    x ^= (1 << c)
if not sched: c, tc = 0, 0
first_check = tc + int((K - 1 - c) / 0.80); match = None
while t < tc + 1800000:
    x = step(x); t += 1
    if t >= first_check and t % 2048 == 0:
        for name, cyc in strips.items():
            for ph in range(P):
                if x == cyc[ph]: match = (name, ph); break
            if match: break
        if match: break
print(f"  settled on {match[0] if match else None} (phase {match[1] if match else None}) by tick {t}, {t - tc} ticks after the last chink "
      f"(the front's climb from {c} at 0.757: {int((K - 1 - c) / 0.757)}); {'HIT' if match and match[0] == NAME else 'MISS'}; {time.time() - t0:.0f} s")
