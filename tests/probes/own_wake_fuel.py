#!/usr/bin/env python3
"""L1321 T43 (Local, 2026-11-02): is an advancing front's own wake fuel? reports/rule30-genealogy.md section 46 (predictions
written first). Run: python3 tests/probes/own_wake_fuel.py PHASE S_E_FILE N K [K ...]   (PHASE: P1024 or 480)

Edge frame, Phi(x) = x ^ ((x << 1) | (x << 2) | 3). A row has random digits at depths 0 .. K-1 above the phase's clean tail,
at a random alignment (P1024: theta; 480: (a, q)). D(t) = Phi^t(X) xor E(t), the front R its deepest 1.
Per run, until 2,000 ticks after R first reaches 3K (cap 6K + 2,400 ticks):
- late drawdown at c = 2, 3: the largest (running maximum of R) - R over the H = 2,000 ticks after R first reaches cK;
- capture: the first tick with R >= 12 and the 8-cell state (class, window) in S_E_FILE (front_closure.py --all-theta
  --export; bit j-1 of the window = D_(R-j)); after capture every tick's state must stay in S_E (a soundness alarm if not),
  and the fall below the running maximum since capture is recorded;
- the drawdown after passing 3K split at capture.
Part 2 (section 46.3): the capture tick from t = 0, R - K at capture, and the early drawdown (the largest fall below the
running maximum before capture); no new random draws, so part 1's lines recur exactly.
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name, sefile, N = sys.argv[1], sys.argv[2], int(sys.argv[3])
Ks = [int(x) for x in sys.argv[4:]]
p, cols, _ = g['phases']()[name]; NC = len(cols)
W = 8; H = 2000
SE = set()
for line in open(sefile):
    if line.startswith('#') or not line.strip():
        continue
    c, w = line.split()
    assert len(w) == W
    SE.add((int(c), int(w, 2)))
rev = [int(format(b, '0%db' % W)[::-1], 2) for b in range(1 << W)]
print('%s: S_E %d states from %s' % (name, len(SE), os.path.basename(sefile)), flush=True)
DMAX = 2 * (6 * max(Ks) + 2400) + max(Ks) + 16
if name == 'P1024':
    col0 = cols[0]
    bits = [(col0 >> i) & 1 for i in range(p)]
    base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(DMAX))[::-1], 2) for k in range(p)]
else:
    pat = [''.join(str((cols[n] >> k) & 1) for n in range(NC)) for k in range(p)]


def pct(v, q):
    v = sorted(v)
    return v[min(len(v) - 1, int(q * len(v)))] if v else None


rng = random.Random(43)
for K in Ks:
    Tcap = 6 * K + 2400; depth = 2 * Tcap + K + 16; mask = (1 << depth) - 1
    dd = {2: [], 3: []}; ddat = []; notpass = {2: 0, 3: 0}; capd = []; precap = []; postcap = []; exits = 0; uncapt = 0
    before = 0; speeds = []; ctick = []; cdepth = []; early = []
    for it in range(N):
        if name == 'P1024':
            th = rng.randrange(p)
            def erow(t):
                return base[(th + t) % p] & mask
            def cls(R, t):
                return (th + t + 195 * R) % p
        else:
            a, q = rng.randrange(NC), rng.randrange(p)
            cache = {}
            def erow(t):
                k = (t + q) % p
                if k not in cache:
                    s0 = pat[k]; s0 = (s0[a:] + s0[:a]) * (depth // NC + 2)
                    cache[k] = int(s0[:depth][::-1], 2)
                return cache[k]
            def cls(R, t):
                return ((R + a) % NC) * p + (t + q) % p
        x = rng.getrandbits(K) | (erow(0) >> K << K)
        best = -2; passed = {2: None, 3: None}; ddc = {2: 0, 3: 0}; capt = None; best_c = None; post = 0; pre = 0; at = 0
        ear = 0
        t = 0
        while t <= Tcap:
            d = (x ^ erow(t)) & mask
            R = d.bit_length() - 1
            best = max(best, R)
            for c in (2, 3):
                if passed[c] is None and R >= c * K:
                    passed[c] = (t, R)
                if passed[c] is not None and t <= passed[c][0] + H:
                    if best - R > ddc[c]:
                        ddc[c] = best - R
                        if c == 3:
                            at = t - passed[3][0]
            if R >= 12:
                st = (cls(R, t), rev[(d >> (R - W)) & ((1 << W) - 1)])
                if capt is None and st in SE:
                    capt = t; best_c = R; ctick.append(t); cdepth.append(R - K)
                elif capt is not None:
                    if st not in SE:
                        exits += 1
                    best_c = max(best_c, R); post = max(post, best_c - R)
            if passed[3] is not None and capt is None:
                pre = max(pre, best - R)
            if capt is None and best >= 0:
                ear = max(ear, best - R)
            if passed[3] is not None and t >= passed[3][0] + H:
                break
            x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
            t += 1
        for c in (2, 3):
            if passed[c] is None:
                notpass[c] += 1
            else:
                dd[c].append(ddc[c])
        if passed[3] is not None:
            ddat.append(at); precap.append(pre)
            speeds.append((R - passed[3][1]) / max(1, t - passed[3][0]))
        early.append(ear)
        if capt is None:
            uncapt += 1
        else:
            postcap.append(post)
            if passed[3] is not None:
                if capt < passed[3][0]:
                    before += 1
                else:
                    capd.append(capt - passed[3][0])
    print('K=%d, %d runs: not past 2K %d, not past 3K %d; never captured %d' % (K, N, notpass[2], notpass[3], uncapt), flush=True)
    for c in (2, 3):
        if dd[c]:
            print('   late drawdown at c=%d (2,000 ticks after passing cK): max %d, 99%% %d, median %d' % (
                c, max(dd[c]), pct(dd[c], 0.99), pct(dd[c], 0.5)), flush=True)
    if ddat:
        print('   tick after passing 3K at which the late maximum drawdown (c=3) was first reached: median %d, max %d' % (
            pct(ddat, 0.5), max(ddat)), flush=True)
    print('   capture: before passing 3K %d; after it %d, delay median %s, 99%% %s, max %s' % (
        before, len(capd), pct(capd, 0.5), pct(capd, 0.99), max(capd) if capd else None), flush=True)
    print('   drawdown after passing 3K and before capture: max %s; after capture (below the running maximum since '
          'capture): max %s; post-capture ticks outside S_E %d (alarm if > 0); late speed min %.4f' % (
              max(precap) if precap else None, max(postcap) if postcap else None, exits, min(speeds) if speeds else -1),
          flush=True)
    if ctick:      # L1321 T43 part 2 (section 46.3): capture timed from the start
        print('   part 2: capture tick from t = 0: median %d, 99%% %d, max %d; R - K at capture: median %d, max %d; '
              'early drawdown (before capture): median %d, 99%% %d, max %d' % (
                  pct(ctick, 0.5), pct(ctick, 0.99), max(ctick), pct(cdepth, 0.5), max(cdepth), pct(early, 0.5),
                  pct(early, 0.99), max(early)), flush=True)
print('OWN_WAKE_FUEL_DONE')
