#!/usr/bin/env python3
"""L1324 T44 (Local, 2026-11-02): is capture decided by the bottom L cells of the prefix? reports/rule30-genealogy.md
section 48 (predictions written first). Run: python3 tests/probes/capture_locality.py PHASE S_E_FILE NA M K [K ...]

Edge frame, Phi(x) = x ^ ((x << 1) | (x << 2) | 3), phase P1024 (theta) or 480 ((a, q)), as in own_wake_fuel.py. A base
row A has random digits at depths 0 .. K-1 above the clean tail. Its first capture tick T_A is the first tick with
R >= 12 and the 8-cell state (class, window) in S_E (front_closure.py --all-theta export). For each L in LS (L < K) and
each of M variants, a row B keeps A's bottom L prefix cells (depths K-L .. K-1) and redraws the upper K-L cells.
GC2390's cone guard: with b = K - L - 1, the mutual mismatch lies at depths <= b + 2t, so if b + 2t <= R_A(t) - 9 for
every t <= T_A the front states agree through T_A (a pair "protected" by the cone: a control). L* = K + 8 +
max_(t <= T_A) (2t - R_A(t)) is the least protected L. Pairs with L < L* are informative.
Per pair: identical front state (R, class, window) at every t <= T_A; T_B == T_A; the first tick t_diff at which the
front states differ, and t_reach, the first tick at which the cone reaches the window (b + 2t > R_A(t) - 9); a
difference before t_reach is a soundness alarm.
After capture (A and B) every tick is checked: R >= 10 (alarm below), and for R >= 10 the state lies in S_E (alarm if
not); the minimum post-capture depth is recorded (GC2390's coverage fix for T43).
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name, sefile, NA, M = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
Ks = [int(x) for x in sys.argv[5:]]
LS = [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]
p, cols, _ = g['phases']()[name]; NC = len(cols)
W = 8; EXTRA = 800
SE = set()
for line in open(sefile):
    if line.startswith('#') or not line.strip():
        continue
    c, w = line.split()
    SE.add((int(c), int(w, 2)))
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
DMAX = 3 * max(Ks) + 6 * EXTRA + 16
if name == 'P1024':
    col0 = cols[0]
    bits = [(col0 >> i) & 1 for i in range(p)]
    base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(DMAX))[::-1], 2) for k in range(p)]
else:
    pat = [''.join(str((cols[n] >> k) & 1) for n in range(NC)) for k in range(p)]


def background(al, depth):
    mask = (1 << depth) - 1
    if name == 'P1024':
        th = al
        return (lambda t: base[(th + t) % p] & mask), (lambda R, t: (th + t + 195 * R) % p)
    a, q = al
    cache = {}
    def erow(t):
        k = (t + q) % p
        if k not in cache:
            s0 = pat[k]; s0 = (s0[a:] + s0[:a]) * (depth // NC + 2)
            cache[k] = int(s0[:depth][::-1], 2)
        return cache[k]
    return erow, (lambda R, t: ((R + a) % NC) * p + (t + q) % p)


def run(prefix, K, al, T, depth, alarms):
    """Front states (R, class, window) for t = 0 .. T or until 300 ticks after capture; first capture tick."""
    erow, cls = background(al, depth); mask = (1 << depth) - 1
    x = prefix | (erow(0) >> K << K)
    hist = []; capt = None; minpost = None
    for t in range(T + 1):
        d = (x ^ erow(t)) & mask
        R = d.bit_length() - 1
        st = (R, cls(R, t), rev[(d >> (R - W)) & 255]) if R >= W + 2 else (R, None, None)
        hist.append(st)
        if capt is None and R >= 12 and (st[1], st[2]) in SE:
            capt = t
        elif capt is not None:
            minpost = R if minpost is None else min(minpost, R)
            if R < 10:
                alarms['post-capture depth below 10'] += 1
            elif (st[1], st[2]) not in SE:
                alarms['post-capture state outside S_E'] += 1
        if capt is not None and t >= capt + 300:
            break
        x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
    return hist, capt, minpost


def pct(v, q):
    v = sorted(v)
    return v[min(len(v) - 1, int(q * len(v)))] if v else None


rng = random.Random(44)
for K in Ks:
    alarms = {'post-capture depth below 10': 0, 'post-capture state outside S_E': 0, 'difference before the cone': 0,
              'protected pair differs': 0}
    depth = 3 * K + 6 * EXTRA + 16
    stats = {L: {'prot': 0, 'inf': 0, 'same_hist': 0, 'same_capt': 0, 'by_TA': 0, 'lag': [], 'dcapt': []}
             for L in LS if L < K}
    Ls_star = []; TAs = []; uncapt = 0; minposts = []
    for ia in range(NA):
        al = rng.randrange(p) if name == 'P1024' else (rng.randrange(NC), rng.randrange(p))
        pa = rng.getrandbits(K)
        hA, TA, mp = run(pa, K, al, K + 2 * EXTRA, depth, alarms)
        if TA is None:
            uncapt += 1; continue
        TAs.append(TA); minposts.append(mp)
        Lstar = K + 8 + max(2 * t - hA[t][0] for t in range(TA + 1)); Ls_star.append(Lstar)
        for L in stats:
            b = K - L - 1
            treach = next((t for t in range(TA + 1) if b + 2 * t > hA[t][0] - 9), None)
            prot = treach is None
            for im in range(M):
                upper = rng.getrandbits(K - L)
                if K - L > 0 and upper == pa & ((1 << (K - L)) - 1):
                    upper ^= 1                      # a nontrivial edit of the upper cells
                pb = (pa >> (K - L) << (K - L)) | upper
                hB, TB, mpb = run(pb, K, al, TA + EXTRA, depth, alarms)
                if TB is not None:
                    minposts.append(mpb)
                tdiff = next((t for t in range(min(TA + 1, len(hB))) if hB[t] != hA[t]), None)
                same = tdiff is None
                s = stats[L]
                if prot:
                    s['prot'] += 1
                    if not same or TB != TA:
                        alarms['protected pair differs'] += 1
                    continue
                s['inf'] += 1
                if tdiff is not None and tdiff < treach:
                    alarms['difference before the cone'] += 1
                s['same_hist'] += same; s['same_capt'] += (TB == TA); s['by_TA'] += (TB is not None and TB <= TA)
                if TB is not None:
                    s['dcapt'].append(TB - TA)
                s['lag'].append((tdiff if tdiff is not None else TA + 1) - treach)
    print('%s K=%d: %d base rows (%d not captured within the horizon); T_A median %s max %s; L* (least cone-protected L) '
          'median %s, min %s, max %s; minimum post-capture depth %s' % (
              name, K, NA, uncapt, pct(TAs, 0.5), max(TAs), pct(Ls_star, 0.5), min(Ls_star), max(Ls_star),
              min(m for m in minposts if m is not None)), flush=True)
    for L, s in stats.items():
        n = s['inf']
        print('   L=%3d: protected pairs %3d; informative %3d: same front history to T_A %3d (%5.1f%%), same capture tick %3d '
              '(%5.1f%%), captured by T_A %3d; ticks from the cone reaching the window to the first difference: median %s; '
              'T_B - T_A: median %s, 5%% %s, 95%% %s' % (
                  L, s['prot'], n, s['same_hist'], 100.0 * s['same_hist'] / n if n else 0, s['same_capt'],
                  100.0 * s['same_capt'] / n if n else 0, s['by_TA'], pct(s['lag'], 0.5), pct(s['dcapt'], 0.5),
                  pct(s['dcapt'], 0.05), pct(s['dcapt'], 0.95)), flush=True)
    print('   alarms: %s' % alarms, flush=True)
print('CAPTURE_LOCALITY_DONE')
