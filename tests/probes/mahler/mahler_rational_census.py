#!/usr/bin/env python3
"""mahler_rational_census.py: Conjecture U, tested on rational starts (MAHLER.md section 2; the door drawn in L714).

Conjecture U (the swarm's adelic lane, L2-B(iv); GPT read it as strictly stronger than Mahler, GC1222/L711): no
2-adic rational y = A/B (B odd) that is not T-preperiodic has every tail u_j of its T-code below 1/2. Here
T(y) = (3y + (y mod 2))/2 on the 2-adic integers, which on numerators over a fixed odd B is A' = (3A + (A mod 2) B)/2,
so the denominator never changes. For B = 1 and A >= 1 this is Mahler. A positive y has t(y) = y + u_0 > 0, so it is
never preperiodic, and U predicts that every positive start dies. Negative starts in (-1, 0) can be preperiodic
with an admissible cycle (the control -9/19, code (100)^infinity), and U says nothing against those.

Why test it (the swarm's reading, kept as a filter on methods): several integer-side tools in the record see only
that a start is a rational of bounded height. If U failed for some B > 1, a positive rational would keep every
fractional tail below 1/2, and any proof of Mahler would have to use eventually-zero binary digits, not merely
eventually periodic ones.

Method. The census walker (mahler_census.c) with b=B: the free phase walks the low bits of the numerator, the
window is unchanged, and the numerator follows A' = (3A + par B)/2. Stragglers alive at step 124 are replayed here
exactly (dyadic window numerators, Python integers) to a cap of 4000 steps. Starts in (-B, 0) are run exactly, with
cycle detection, outside the walker.

RUN-ON:     cpu (M5), 9 workers; minutes in all.
COMMAND:    python3 tests/probes/mahler/mahler_rational_census.py

Record searched (record_find, 2026-10-14 11:46 BST): 'Conjecture U|rotating window' -> 3 hits in 3 files (MAHLER.md
section 2, the L711 summary, PRIOR-ART's swarm notes); 'rational start' 'Mahler|Z-number|ceil' -> 1 hit (unrelated
Collatz parity realization); 'odd denominator' -> 6 hits in 3 files (G29's signed fixed-odd-denominator extension,
COLLATZ-PRIZE section 5, the swarm notes). The swarm's own exploratory census (B <= 63, 27M starts, predictions not
committed first) is noted, not counted.

PREDICTIONS (written 2026-10-14 11:49 BST, before any run of this file; only the B = 1 check of the amended walker,
  the 2^20 receipt, was run first, and it reproduced 47 at 690773 with RECEIPT OK).
  U0 must hold (instrument): with b=1 the walker reproduces the 2^40 census exactly (the original receipt's 99 at
     704731028141), and for every B the positive free-phase identity holds: (positive survivors + 1) / 2^(w - T) is
     the integer A(T) of the B = 1 census at every T < w. The residue bijection does not see B; the + 1 is the
     numerator 0, which survives every finite horizon.
  U1 (the test): for every odd B from 3 to 255 at w = 44, and for B in {65, 211, 665, 2059} at w = 52, every positive
     numerator 1 <= A < 2^w has a finite horizon, and every straggler dies in exact replay. Counterfactual: a positive
     start still alive at 4000 steps, replayed exactly. That would be strong evidence against U at that B: a positive
     rational keeping every tail below 1/2 for 4000 steps.
  U2 (blind, 0.7): the record horizon H*(B) at w = 44 lies in [2.1 w, 2.9 w] = [92, 128] for every B, and at w = 52 in
     [109, 151]. A denominator adds about log2 B bits of height, which the free bits do not see.
  U3 (bounded region, exact): for each odd B <= 255, the starts -B < A < 0 alive at 4000 steps are exactly those
     whose numerator orbit has entered a cycle, and each such cycle's code has every tail below 1/2 (checked exactly
     from the periodic sum). Controls: B = 19 includes A = -9 (cycle (100), tails 9/19, 4/19, 6/19), and B = 1 has no
     start in the region. No aperiodic survivor appears. Counterfactual: an aperiodic start alive at 4000 steps would
     be a U counterexample candidate.
  Unexpected check: B = 3, A = -1 (y = -1/3) has T(-1/3) = 0, so it survives as the preimage of the zero cycle (GC1230's
     2-to-1 point). U3 must classify it as a preperiodic survivor, not as a death or an aperiodic survivor.
"""
import os, subprocess, sys, time
from collections import Counter
from fractions import Fraction as F
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(os.path.expanduser('~/np-scratch-int'), 'mahler', 'mahler_census_bin')
CAP = 4000


def horizon(A, B, cap=CAP):
    """Exact horizon of y = A/B: the first j at which the window of fractional parts is empty; None if alive at cap.
    Also returns the list of numerators seen (for cycle detection on bounded orbits)."""
    v, lo, hi, T, seen = A, 0, 1, 0, []
    while T < cap:
        b = v & 1
        D = 1 << (T + 1)
        nl, nh = 3 * lo, 3 * hi
        if b:
            nl, nh = max(nl - D, 0), max(nh - D, 0)
        nh = min(nh, D)
        if nl >= nh:
            return T + 1, seen
        lo, hi = nl, nh
        seen.append(v)
        v = (3 * v + b * B) // 2
        T += 1
    return None, seen


def cycle_of(seen):
    """If the numerator sequence has become periodic, return the cycle (list of numerators); else None."""
    last = {}
    for i, v in enumerate(seen):
        if v in last:
            return seen[last[v]:i]
        last[v] = i
    return None


def cycle_admissible(cyc):
    """Every tail of the periodic code below 1/2, exactly."""
    bits = [v & 1 for v in cyc]
    p = len(bits)
    for s in range(p):
        rot = bits[s:] + bits[:s]
        u = sum(F(c * 2 ** k, 3 ** (k + 1)) for k, c in enumerate(rot)) / (1 - F(2, 3) ** p)
        if u >= F(1, 2):
            return False
    return True


def build():
    subprocess.run(['cc', '-O3', '-o', BIN, os.path.join(HERE, 'mahler_census.c')], check=True)


def chunk(args):
    w, pb, prefix, B = args
    out = subprocess.run([BIN, str(w), str(pb), str(prefix), 'b=%d' % B], capture_output=True, text=True,
                         check=True).stdout
    hist, strag, mx = Counter(), [], (0, 0)
    for line in out.splitlines():
        f = line.split()
        if f[0] == 'H':
            hist[int(f[1])] += int(f[2])
        elif f[0] == 'S':
            strag.append(int(f[1]))
        elif f[0] == 'MAX':
            mx = (int(f[1]), int(f[2]))
    return hist, strag, mx


def census(pool, w, B, pb=6):
    hist, strag, best = Counter(), [], (0, 0)
    for h, s, mx in pool.imap_unordered(chunk, [(w, pb, p, B) for p in range(1 << pb)]):
        hist.update(h); strag.extend(s)
        if mx[0] > best[0]:
            best = mx
    alive = []
    for A in strag:
        h, _ = horizon(A, B)
        if h is None:
            alive.append(A)
            continue
        hist[h] += 1
        if h > best[0]:
            best = (h, A)
    return hist, best, len(strag), alive


def parry_counts(N):
    """c_n = 1 + sum_(i=1..n) d_i c_(n-i), d the greedy digits of 1 in base 3/2: the beta-shift word counts, which are
    the census's A(T) (the residue bijection; checked against the B = 1 census for every T < 63)."""
    d, x = [None], F(1)
    for _ in range(N):
        x *= F(3, 2); k = int(x); d.append(k); x -= k
    c = [1]
    for n in range(1, N):
        c.append(1 + sum(d[i] * c[n - i] for i in range(1, n + 1)))
    return c


def identity_ok(hist, w, Aref):
    surv, acc = {}, 0
    for T in range(max(hist), -1, -1):
        surv[T] = acc
        acc += hist.get(T, 0)
    for T in range(1, w):
        q, r = divmod(surv.get(T, 0) + 1, 1 << (w - T))
        if r or q != Aref[T]:
            return False
    return True


def main():
    build()
    t0 = time.time()
    with Pool(9) as pool:
        Aref = parry_counts(64)
        h1, b1, n1, a1 = census(pool, 40, 1)
        print('U0: b=1, w=40: max %s, total %d (2^40 - 1 = %d), unresolved %d, identity %s' % (
            b1, sum(h1.values()), (1 << 40) - 1, len(a1), identity_ok(h1, 40, Aref)), flush=True)
        bad, alive_all, rec = [], [], []
        plan = [(B, 44) for B in range(3, 256, 2)] + [(B, 52) for B in (65, 211, 665, 2059)]
        for B, w in plan:
            h, best, ns, alive = census(pool, w, B)
            ok = sum(h.values()) + len(alive) == (1 << w) - 1 and identity_ok(h, w, Aref)
            if not ok:
                bad.append((B, w))
            alive_all += [(B, A) for A in alive]
            rec.append((B, w, best[0], best[1], ns))
        print('U0: free-phase identity and mass hold for every B:', not bad, '| failures', bad[:10], flush=True)
        print('U1: positive starts alive at %d steps:' % CAP, alive_all if alive_all else 'none', flush=True)
        for w in (44, 52):
            hs = [r for r in rec if r[1] == w]
            lo, hi = min(hs, key=lambda r: r[2]), max(hs, key=lambda r: r[2])
            print('U2: w=%d: H* from %d (B=%d) to %d (B=%d, A=%d); band [%d, %d]; stragglers %d..%d' % (
                w, lo[2], lo[0], hi[2], hi[0], hi[3], int(2.1 * w) + 1, int(2.9 * w), min(r[4] for r in hs),
                max(r[4] for r in hs)), flush=True)
            out = [(r[0], r[2]) for r in hs if not (2.1 * w <= r[2] <= 2.9 * w)]
            print('     outside the band:', out if out else 'none', flush=True)
    # U3: the bounded region -B < A < 0, exactly, with cycle detection
    pre, aper, deaths = Counter(), [], 0
    examples = {}
    for B in range(1, 256, 2):
        for A in range(-B + 1, 0):
            h, seen = horizon(A, B)
            if h is not None:
                deaths += 1
                continue
            cyc = cycle_of(seen)
            if cyc is not None and cycle_admissible(cyc):
                pre[B] += 1
                examples.setdefault(B, (A, len(cyc)))
            else:
                aper.append((B, A, cyc is not None))
    print('U3: bounded region, odd B <= 255: deaths %d, preperiodic survivors %d (in %d denominators), aperiodic or '
          'inadmissible-cycle survivors %s' % (deaths, sum(pre.values()), len(pre), aper if aper else 'none'),
          flush=True)
    print('     controls: B=19 A=-9 survives:', 19 in pre and any(
        horizon(-9, 19)[0] is None for _ in [0]), '| B=3 A=-1:', horizon(-1, 3)[0] is None and
        cycle_of(horizon(-1, 3)[1]) == [0], flush=True)
    print('     first examples (B: A, cycle length):', dict(list(examples.items())[:12]), flush=True)
    print('total %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
