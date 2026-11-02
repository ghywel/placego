#!/usr/bin/env python3
"""L1316 T41 part 2 (Local, 2026-11-02): is the clean front of a periodic-wake phase robust to everything behind its
window? reports/rule30-genealogy.md section 44. Run: python3 tests/probes/front_closure.py PHASE W [W ...] [--cap=N]
(PHASE: G8, G16, 480 or P1024)
--all-theta (P1024; L1318, GC2386): the clean states of every theta at ticks 600 .. 2,480, the runs and range that
wake_attractor.py --win compares against, their closure S_E^all, its verdict and digests; --export=PREFIX writes them.
L1321 (T43): --all-theta also for 480, over one alignment (a, q) per class of its 960 (a in 0..29, q in 0..31), with the
class ((R + a) mod 480) * 32 + (t + q) mod 32; it also counts the distinct clean-state sets (orbits) over the alignments.
L1322: --clock (with --all-theta) replays GC2389's finite clock facts on S_E^all: one (next class, advance) per class,
the class cycle, its advance word and least period, the potential range (P1024), singleton fibres and window-0 states.
--control=N: N exact checks per W. At a random tick of the clean run, every mismatch bit more than W behind the front
is replaced by a random bit; the row is evolved exactly for 3,000 ticks; each tick's (class, window) must lie in the
closure, and every k ticks must advance the front by at least 1 (k from the verdict). A failure is a soundness alarm.

The window automaton of front_cert.py (section 39): states (front class, the W mismatch bits above the front); one
tick computes depths R-W .. R+2 exactly, with the two bits below the window (R-W-1, R-W-2) unknown and branched, and
window bits left uncomputed after a retreat free and branched. Every real run is a path of it, whatever the mismatch
holds deeper than W behind the front. Here the automaton is not built whole: its forward closure is explored from the
clean front's own states (class, window) at ticks 600 .. 600 + 4 wake periods of a clean start. If the closure has no
FAIL edge (a retreat out of the window) and every path of length k in it advances by at least 1, then any row whose
front ever shows one of those states advances for ever at a positive least mean speed, whatever lies behind the window.
"""
import os
import sys
import runpy
import numpy as np
from collections import deque
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
fc = runpy.run_path(os.path.join(here, 'front_cert.py'), run_name='lib')
args = [a for a in sys.argv[1:] if not a.startswith('--')]
CAP = next((int(a[6:]) for a in sys.argv[1:] if a.startswith('--cap=')), 3_000_000)
NCTL = next((int(a[10:]) for a in sys.argv[1:] if a.startswith('--control=')), 0)
name = args[0]; Ws = [int(x) for x in args[1:]]
p, cols, _ = g['phases']()[name]; NC = len(cols)
PER = {'G8': 8, 'G16': 128, 'P1024': 208, '480': 288}[name]
if name == 'P1024':
    th0 = 780; col0 = cols[0]
    def E_bit(n, t):
        return (col0 >> ((th0 + t + 195 * n) % p)) & 1
    def cls(R, t):
        return (th0 + t + 195 * R) % p
    def bg(cl, o):
        return (col0 >> ((cl + 195 * o) % p)) & 1
    def nxt(cl, a):
        return (cl + 1 + 195 * a) % p
else:
    a0, q0 = {'480': (195, 21), 'G16': (3, 5)}.get(name, (0, 0))
    def E_bit(n, t):
        return (cols[(n + a0) % NC] >> ((t + q0) % p)) & 1
    def cls(R, t):
        return ((R + a0) % NC) * p + (t + q0) % p
    def bg(cl, o):
        return (cols[(cl // p + o) % NC] >> (cl % p)) & 1
    def nxt(cl, a):
        return ((cl // p + a) % NC) * p + (cl % p + 1) % p

# clean start (the alignments of layer_linear.py's runs), its states at ticks 600 .. 600 + 4 PER
T = 600 + 4 * PER; depth = 2 * (T + (3000 if NCTL else 0)) + 16; mask = (1 << depth) - 1   # room for the control's 3,000 ticks
clean_states = {W: set() for W in Ws}; xs = []
rows = {}
def erow(t):
    k = t % p
    if k not in rows:
        rows[k] = sum(E_bit(n, t) << n for n in range(depth))
    return rows[k]
x = erow(0)
for t in range(T + 1):
    xs.append(x)
    d = x ^ erow(t); R = d.bit_length() - 1
    if t >= 600:
        for W in Ws:
            win = 0
            for j in range(1, W + 1):
                win |= ((d >> (R - j)) & 1) << (j - 1)
            clean_states[W].add((cls(R, t), win))
    x = (x ^ ((x << 1) | (x << 2) | 3)) & mask


def successors(cl, win, W):
    """All edges of the window automaton from (cl, win): list of (cl2, win2, advance), and the FAIL count."""
    E = {o: bg(cl, o) for o in range(-W - 2, 3)}
    out = set(); fails = 0
    for unk in range(4):
        D = {o: 0 for o in range(-W - 2, 3)}
        D[0] = 1
        for j in range(1, W + 1):
            D[-j] = (win >> (j - 1)) & 1
        D[-W - 1] = unk & 1; D[-W - 2] = (unk >> 1) & 1
        N = {}
        for o in range(-W, 3):
            e1, e2 = E[o - 1], E[o - 2]
            N[o] = D[o] ^ (((e1 ^ D[o - 1]) | (e2 ^ D[o - 2])) ^ (e1 | e2))
        ones = [o for o in range(-W, 3) if N[o]]
        if not ones:
            fails += 1; continue
        a = max(ones)
        known = [N[a - j] if a - j >= -W else None for j in range(1, W + 1)]
        free = [i for i, v in enumerate(known) if v is None]
        c2 = nxt(cl, a); base = 0
        for i, v in enumerate(known):
            if v:
                base |= 1 << i
        for f in range(1 << len(free)):
            w2 = base
            for k, i in enumerate(free):
                if (f >> k) & 1:
                    w2 |= 1 << i
            out.add((c2, w2, a))
    return out, fails


for W in Ws:
    start = clean_states[W]
    index = {}; q = deque(); src = []; dst = []; adv = []; fails = 0; capped = False
    for s in start:
        index[s] = len(index); q.append(s)
    while q:
        s = q.popleft(); i = index[s]
        succ, f = successors(s[0], s[1], W); fails += f
        for (c2, w2, a) in succ:
            t2 = (c2, w2)
            if t2 not in index:
                if len(index) >= CAP:
                    capped = True; continue
                index[t2] = len(index); q.append(t2)
            src.append(i); dst.append(index[t2]); adv.append(a)
        if capped:
            break
    NS = len(index)
    print('%s W=%d: clean states %d; forward closure %d states%s, %d edges, FAIL edges %d, advances %s' % (
        name, W, len(start), NS, ' (CAPPED at %d: closure incomplete)' % CAP if capped else '', len(src), fails,
        sorted(set(adv))), flush=True)
    if capped:
        continue
    k, trace = fc['certify'](NS, np.array(src, dtype=np.int64), np.array(dst, dtype=np.int64), np.array(adv, dtype=np.int64))
    print('   least advance over paths of length k: %s' % trace, flush=True)
    print('   %s' % ('ROBUST: no FAIL edge in the closure and every path of length %d advances' % k if (k and fails == 0) else
                      'NOT ROBUST (FAIL edges in the closure)' if fails else 'NOT ROBUST (a path of length 600 with no advance)'),
          flush=True)
    if NCTL and k and fails == 0:
        import random
        rng = random.Random(4100 + W); bad_state = 0; bad_adv = 0; ticks = 0
        for it in range(NCTL):
            t0 = rng.randrange(600, T + 1); d = xs[t0] ^ erow(t0); R0 = d.bit_length() - 1
            low = rng.getrandbits(R0 - W) ^ (erow(t0) & ((1 << (R0 - W)) - 1))   # a random mismatch below the window
            y = (xs[t0] & ~((1 << (R0 - W)) - 1)) | low
            Rs = []
            for t in range(t0, t0 + 3000):
                dd = y ^ erow(t); R = dd.bit_length() - 1; Rs.append(R)
                win = 0
                for j in range(1, W + 1):
                    win |= ((dd >> (R - j)) & 1) << (j - 1)
                if (cls(R, t), win) not in index:
                    bad_state += 1; break
                y = (y ^ ((y << 1) | (y << 2) | 3)) & mask
            ticks += len(Rs)
            if any(Rs[i + k] - Rs[i] < 1 for i in range(len(Rs) - k)):
                bad_adv += 1
        print('   control: %d random wakes behind the window, %d exact ticks: states outside the closure %d, '
              '%d-tick stretches without advance in %d runs' % (NCTL, ticks, bad_state, k, bad_adv), flush=True)

if '--all-theta' in sys.argv and name in ('P1024', '480'):
    # L1318 T42 part 2 (GC2386's capture interface): U = the clean front's W-cell states at ticks 600 .. 2,480 for every
    # theta, the clean runs and tick range of wake_attractor.py; S_E^all = the forward closure of U.
    import hashlib
    TA = 2480; DA = 2 * TA + 16; MA = (1 << DA) - 1
    if name == 'P1024':
        base = [sum(((col0 >> ((k + 195 * n) % p)) & 1) << n for n in range(DA)) for k in range(p)]
        aligns = [(th, 0) for th in range(p)]
        def arow(al, t):
            return base[(al[0] + t) % p]
        def acls(al, R, t):
            return (al[0] + t + 195 * R) % p
    else:
        # L1321 T43 (480): one alignment (a, q) per class of the 960 cosets of <(30, 14), (0, 32)>: a in 0..29, q in 0..31
        pat = [''.join(str((cols[n] >> k) & 1) for n in range(NC)) for k in range(p)]
        reps = DA // NC + 2
        abase = {}
        def arow(al, t):
            key = (al[0], (t + al[1]) % p)
            if key not in abase:
                s0 = pat[key[1]]; s0 = (s0[key[0]:] + s0[:key[0]]) * reps
                abase[key] = int(s0[:DA][::-1], 2)
            return abase[key]
        def acls(al, R, t):
            return ((R + al[0]) % NC) * p + (t + al[1]) % p
        aligns = [(a, q) for a in range(30) for q in range(p)]
        assert all(arow((a0, q0), t) & ((1 << depth) - 1) == erow(t) for t in range(3)), 'the 480 row builder disagrees with erow'
    for W in Ws:
        rev = [int(format(b, '0%db' % W)[::-1], 2) for b in range(1 << W)]   # bit W-1 = D_(R-1)  ->  bit 0 = D_(R-1)
        U = set(); per_theta_in = 0
        S780 = None
        orbits = {}
        for al in aligns:
            x = arow(al, 0); own = set()
            for t in range(TA + 1):
                d = x ^ arow(al, t); R = d.bit_length() - 1
                if t >= 600:
                    own.add((acls(al, R, t), rev[(d >> (R - W)) & ((1 << W) - 1)]))
                x = (x ^ ((x << 1) | (x << 2) | 3)) & MA
            U |= own
            orbits[frozenset(own)] = orbits.get(frozenset(own), 0) + 1
        print('%s W=%d: %d alignments, %d distinct clean-state sets, sizes %s' % (
            name, W, len(aligns), len(orbits), sorted(set(len(o) for o in orbits))), flush=True)
        # the closure from U, and from theta 780's states alone, by the same breadth-first search
        def closure(start):
            index = {}; q = deque(); src = []; dst = []; adv = []; fails = 0
            for s in sorted(start):
                index[s] = len(index); q.append(s)
            while q:
                s = q.popleft(); i = index[s]
                succ, f = successors(s[0], s[1], W); fails += f
                for (c2, w2, a) in sorted(succ):
                    t2 = (c2, w2)
                    if t2 not in index:
                        index[t2] = len(index); q.append(t2)
                    src.append(i); dst.append(index[t2]); adv.append(a)
            return index, src, dst, adv, fails
        idx_all, src, dst, adv, fails = closure(U)
        k, trace = fc['certify'](len(idx_all), np.array(src, dtype=np.int64), np.array(dst, dtype=np.int64),
                                 np.array(adv, dtype=np.int64))
        idx780 = closure(clean_states[W])[0]
        print('%s W=%d, all %d alignments, ticks 600..%d: U %d states; S_E^all %d states, %d edges, FAIL edges %d, '
              'advances %s' % (name, W, len(aligns), TA, len(U), len(idx_all), len(src), fails, sorted(set(adv))), flush=True)
        print('   least advance over paths of length k: %s; %s' % (trace, (
            'ROBUST: every path of length %d advances' % k) if (k and fails == 0) else 'NOT ROBUST'), flush=True)
        # L1321 T43: the largest fall below a running maximum along paths of S_E^all (f' = max(f - advance, 0) from f = 0)
        out_e = {}
        for i, j, a in zip(src, dst, adv):
            out_e.setdefault(i, []).append((j, a))
        seen_f = {(i, 0) for i in range(len(idx_all))}; frontier = list(seen_f); fmax = 0
        while frontier and fmax <= 200:
            nxt_f = []
            for i, f in frontier:
                for j, a in out_e.get(i, []):
                    f2 = max(f - a, 0)
                    if (j, f2) not in seen_f:
                        seen_f.add((j, f2)); nxt_f.append((j, f2)); fmax = max(fmax, f2)
            frontier = nxt_f
        print('   largest fall below a running maximum along paths of S_E^all: %s' % (fmax if fmax <= 200 else '> 200'), flush=True)
        if '--clock' in sys.argv:
            # L1322 (Local's carrying read of GC2389): GPT's finite clock facts, replayed with this generator. Predictions in
            # genealogy section 47.1. Per class: the set of (next class, advance) over every edge out of S_E^all.
            keys = list(idx_all)
            proj = {}
            for i, j, a in zip(src, dst, adv):
                proj.setdefault(keys[i][0], set()).add((keys[j][0], a))
            det = all(len(v) == 1 for v in proj.values())
            print('   clock: %d classes in S_E^all; every class has one (next class, advance) over all its edges: %s' % (
                len(proj), det), flush=True)
            if det:
                nxt_c = {c: next(iter(v)) for c, v in proj.items()}
                c0 = min(nxt_c); cyc = [c0]
                while nxt_c[cyc[-1]][0] != c0 and len(cyc) <= len(nxt_c):
                    cyc.append(nxt_c[cyc[-1]][0])
                word = [nxt_c[c][1] for c in cyc]
                L = len(cyc); tot = sum(word)
                per = next(d for d in range(1, L + 1) if L % d == 0 and all(word[i] == word[(i + d) % L] for i in range(L)))
                print('   one cycle through all classes: %s; length %d, total advance %d, least period of the advance word %d' % (
                    L == len(nxt_c), L, tot, per), flush=True)
                print('   advance word from class %d: %s' % (c0, ','.join(map(str, word))), flush=True)
                if name == 'P1024':
                    ps = [0]
                    for a in word:
                        ps.append(ps[-1] + 13 * a - 17)
                    print('   potential: 13*advance - 17 summed round the cycle returns to %d; its range (max - min) %d' % (
                        ps[-1], max(ps) - min(ps)), flush=True)
                fib = {}
                for (c, w) in keys:
                    fib.setdefault(c, []).append(w)
                single = sorted((c, fib[c][0]) for c in fib if len(fib[c]) == 1)
                pos = {c: i for i, c in enumerate(cyc)}
                sp = [pos[c] for c, _ in single]
                wait = max(min((q - i) % L for q in sp) for i in range(L)) if sp else None
                print('   singleton fibres (class, window): %s; longest wait from any class to one: %s' % (single, wait), flush=True)
                zero = sorted((c, w) for (c, w) in keys if w == 0)
                print('   states with window 0: %s' % zero, flush=True)
        if idx780 is not None:
            print('   S_E(base alignment) %d states; U inside S_E(base): %d of %d; S_E(base) inside S_E^all: %s' % (
                len(idx780), sum(1 for s in U if s in idx780), len(U), all(s in idx_all for s in idx780)), flush=True)
        for nm, st in (('S_E_all', idx_all), ('U', U)):
            txt = ''.join('%d %s\n' % (c, format(w, '0%db' % W)) for c, w in sorted(st)).encode()
            path = next((a[9:] for a in sys.argv if a.startswith('--export=')), None)
            if path:
                with open('%s.%s.W%d.%s.txt' % (path, name, W, nm), 'wb') as f:
                    f.write((b'# one state per line: theta class' if name == 'P1024' else b'# one state per line: class (R + a mod 480) * 32 + (t + q mod 32)') +
                        b', then the window printed bit W-1 first, where bit j-1 = D_(R-j)\n' + txt)
            print('   %s: %d states, SHA-256 of its lines %s (lines "class window", window printed bit W-1 first)' % (
                nm, len(st), hashlib.sha256(txt).hexdigest()), flush=True)
