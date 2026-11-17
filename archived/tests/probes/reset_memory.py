#!/usr/bin/env python3
"""L1329 T47 (Local, 2026-11-02): after a pair reset, how much history still matters? reports/rule30-genealogy.md section 51
(predictions written first). Run: python3 tests/probes/reset_memory.py PHASE S_E_FILE N K

Edge frame and phases as in own_wake_fuel.py. A reset tick is a pre-capture tick (front R >= 12, before the first S_E
state) whose class has E_R = E_(R+1) = 0 and E_(R+2) = E_(R+3) (GC2393: the next two moves are +2 and the trailing pair is
reset). Reported: reset ticks as a share of pre-capture ticks; blocked moves (look-ahead bit 1) between consecutive resets.
At up to 5 resets per run, two ticks after the reset tick (front R'), one cell j behind R' is flipped (j = 3, 4, 6, 8, 12,
16) and both rows run 200 ticks; the front path differs or not, and the first tick of difference.
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name, sefile, N, K = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
p, cols, _ = g['phases']()[name]; NC = len(cols)
W = 8; H = 200; JS = [3, 4, 6, 8, 12, 16]
SE = set()
for line in open(sefile):
    if not line.startswith('#') and line.strip():
        c, w = line.split(); SE.add((int(c), int(w, 2)))
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
T = 6 * K + 2400; depth = 2 * (T + H) + K + 16; mask = (1 << depth) - 1
if name == 'P1024':
    col0 = cols[0]
    bits = [(col0 >> i) & 1 for i in range(p)]
    base = [int(''.join(str(bits[(k + 195 * n) % p]) for n in range(depth))[::-1], 2) for k in range(p)]


def phi(x):
    return (x ^ ((x << 1) | (x << 2) | 3)) & mask


def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(q * len(v)))] if v else None


rng = random.Random(47)
pre_ticks = 0; resets = 0; gaps = []; trials = {j: 0 for j in JS}; changed = {j: 0 for j in JS}; first = {j: [] for j in JS}
for it in range(N):
    if name == 'P1024':
        th = rng.randrange(p)
        erow = lambda t, th=th: base[(th + t) % p]
        cls = lambda R, t, th=th: (th + t + 195 * R) % p
    else:
        a0, q0 = rng.randrange(NC), rng.randrange(p)
        cache = {}
        def erow(t, a0=a0, q0=q0, cache=cache):
            k = (t + q0) % p
            if k not in cache:
                s0 = ''.join(str((cols[(n + a0) % NC] >> k) & 1) for n in range(NC)) * (depth // NC + 2)
                cache[k] = int(s0[:depth][::-1], 2)
            return cache[k]
        cls = lambda R, t, a0=a0, q0=q0: ((R + a0) % NC) * p + (t + q0) % p
    x = rng.getrandbits(K) | (erow(0) >> K << K)
    blocked_since = None; done = 0; pending = []
    for t in range(T + 1):
        e = erow(t); d = (x ^ e) & mask; R = d.bit_length() - 1
        if R >= 12:
            if (cls(R, t), rev[(d >> (R - W)) & 255]) in SE:
                break                                       # captured: pre-capture part over
            pre_ticks += 1
            E = lambda o: (e >> (R + o)) & 1
            if E(1):
                blocked_since = (blocked_since or 0) + 1 if blocked_since is not None else None
            if E(0) == 0 and E(1) == 0 and E(2) == E(3):
                resets += 1
                if blocked_since is not None:
                    gaps.append(blocked_since)
                blocked_since = 0
                if done < 5:
                    pending.append(t + 2); done += 1
        if pending and t == pending[0]:
            pending.pop(0)
            Rp = R
            for j in JS:
                if Rp - j < 0:
                    continue
                xa, xb = x, x ^ (1 << (Rp - j)); diff = None
                for s in range(1, H + 1):
                    xa, xb = phi(xa), phi(xb)
                    ee = erow(t + s)
                    if ((xa ^ ee) & mask).bit_length() != ((xb ^ ee) & mask).bit_length():
                        diff = s; break
                trials[j] += 1
                if diff is not None:
                    changed[j] += 1; first[j].append(diff)
        x = phi(x)
print('%s K=%d, %d runs: pre-capture ticks at R >= 12: %d; reset ticks %d (%.1f%%); blocked moves between consecutive '
      'resets: median %s, 90%% %s, max %s' % (name, K, N, pre_ticks, resets, 100.0 * resets / max(1, pre_ticks),
      pct(gaps, 0.5), pct(gaps, 0.9), max(gaps) if gaps else None), flush=True)
for j in JS:
    print('   flip at j=%2d behind the front two ticks after a reset: %d trials, front path changed within %d ticks in %d '
          '(%.1f%%); first difference: median %s, max %s' % (j, trials[j], H, changed[j],
          100.0 * changed[j] / max(1, trials[j]), pct(first[j], 0.5), max(first[j]) if first[j] else None), flush=True)
print('RESET_MEMORY_DONE')
