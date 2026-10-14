#!/usr/bin/env python3
"""mahler_rung_search.py: door 0 of the Mahler room, the rung-g search past the 2^63 census (L717; MAHLER.md section 2).

The gap-g ladder (G294, PROVED): for g >= 3 and every a in [alpha_g, beta_g], with alpha_g = 3^(g-1)/(3^g - 2^g) and
beta_g = (1 + (2/3)^(g-1))/3, a real xi > 0 keeps every fractional part of xi (3/2)^j in [0, a) iff xi = n + u_0(n)
for an integer n >= 1 whose T-code (T(x) = ceil(3x/2)) has every two 1s at distance >= g. So a rung-g survivor is a
Mahler Z-number. A positive n with no rung-g survivor below 2^W means no xi in (0, 2^W) keeps every fractional part
below beta_g.

Rung-g codes form a shift of finite type with growth lambda_g (the largest root of x^g = x^(g-1) + 1): 1.4656 at
g = 3, 1.3803 at 4, 1.3247 at 5, 1.2852 at 6, 1.2321 at 8, against 3/2 for the full census. A residue tree that walks
only rung-pure prefixes therefore reaches far past 2^63 for the same work.

RUN-ON:     cpu (M5), 9 workers; mahler_rung_search.c (256-bit numerators).
COMMAND:    python3 tests/probes/mahler/mahler_rung_search.py control
            python3 tests/probes/mahler/mahler_rung_search.py run

Record searched (record_find, 2026-10-14 12:05 BST): 'rung|5 mod 8' 'Mahler|Z-number' -> the swarm's records only
(MAHLER.md section 2, the swarm tests); 'Y_3|lambda_g|finite type' 'Mahler' -> MAHLER.md section 2 and GC1221's
non-sofic remark; no search past 2^63 in the record. Literature: none known for windows [0, a) with a in
(1/3, 1/2), beyond the ladder's equivalence itself (novelty of that is UNKNOWN, GC1228).

PREDICTIONS (written 2026-10-14 12:05 BST, before any search; only the W = 20 control was run first, and it is recorded
  here as done).
  R0 must hold (done before this file, recorded below): at W = 20, for every g from 3 to 8, the walker's rung-horizon
     histogram equals a direct exact computation on every n in [1, 2^20).
  R0b must hold (instrument identity): for T < W, (#{1 <= n < 2^W : rung horizon > T} + 1) / 2^(W - T) = Y_g(T), the
     number of binary words of length T with every two 1s at distance >= g. The + 1 is the zero start.
  R1 (cross-instrument control): g = 3 at W = 63 gives maximum rung horizon 157, attained by 1541211973603965806,
     the census record. The judge found its first 156 bits rung-3-pure and the 157th breaking the rung. Since a
     rung-pure prefix never empties the census window, no start can exceed the census maximum 157.
  R2 (the searches): no rung-g survivor for g = 4 below 2^70, g = 5 below 2^80, g = 6 below 2^90, g = 8 below 2^100.
     Every start has a finite rung horizon, and every straggler alive at step 250 dies in exact replay. So no xi in
     (0, 2^W) keeps every fractional part below beta_g: 35/81 at g = 4 below 2^70, 97/243 at g = 5 below 2^80,
     275/729 at g = 6 below 2^90 and 2315/6561 at g = 8 below 2^100.
     Counterfactual: a survivor would be a Mahler Z-number candidate above 2^63, replayed exactly before any claim.
  R3 (blind, 0.7): the record rung horizon H*_g(W) lies within 20% of the coin law W / (1 - log2 lambda_g): about 131
     at g = 4, 135 at g = 5, 141 at g = 6 and 143 at g = 8.
  Unexpected check: the record holders at g = 6 and g = 8 have no binary structure in common (trailing zeros, low bits),
     as at the census.
  R0 RECORDED (run first, 12:05 BST): for every g from 3 to 8 at W = 20, the walker equals the exact computation and the
     identity holds. The maxima were 47 at 690773 for g = 3, 4 (the census record), 32 at 110464 for g = 5, 6, and 32
     at 340600 for g = 7, 8.

OUTCOME (2026-10-14 12:12 BST, M5, 9 workers, 358 s; machine output quoted; log ~/np-scratch-int/mahler/rung_search.log):
  R0 and R0b HELD: mass 2^W - 1 and the Y_g identity at every T < W, in every run.
  R1 HELD: g = 3 at W = 63 gives maximum rung horizon 157 at 1541211973603965806, the census record, from independent
     code (no windows; the gap condition only). Since rung-pure prefixes never empty the census window, this is a
     second-instrument replay of the census maximum.
  R2 HELD: no survivor and no straggler at step 250, in any run:
     g = 4 below 2^70: max 137 at 888784713284933952853 (43 s);
     g = 5 below 2^80: max 138 at 928708411130383264535893 (50 s);
     g = 6 below 2^90: max 147 at 244479157956375357271529614 (75 s);
     g = 8 below 2^100: max 147 at 882798358751616658686651027328 (18 s).
     So (COMPUTED, by G294): no xi in (0, 2^70) has every fractional part of xi (3/2)^n below 35/81; none in
     (0, 2^80) below 97/243; none in (0, 2^90) below 275/729; none in (0, 2^100) below 2315/6561.
  R3 HELD: ratios to the coin law W / (1 - log2 lambda_g) of 1.047, 1.025, 1.042 and 1.027 (and 1.118 at g = 3).
  Unexpected check HELD as registered: the g = 6 and g = 8 holders share no low-bit structure (low bytes 10001110 and
     10000000).
  POST HOC (not preregistered): the g = 4 and g = 5 holders both end in 01010101, n = 85 = -1/3 mod 256, so their first
     odd step is followed by seven even steps. The g = 8 holder ends in seven zeros. Both are 2-adic head starts near
     -1/3 and 0, the zero cycle and its 2-to-1 preimage (GC1230), which are rung-pure for ever. The g = 3 and g = 6
     holders show no such proximity.
  AMENDMENT (per GC1234, after the run; it changes no outcome): R0 and R1 are now hard gates; a failed range is
     quarantined; GPT's fixed control (rung horizon of 2^99 at g = 8 is 101) is checked before any search, and it
     gives 101.
  Reading: finite exclusions inside one rung each, past the 2^63 census, at the coin law; no step on the critical path.
"""
import math, os, subprocess, sys, time
from collections import Counter
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(os.path.expanduser('~/np-scratch-int'), 'mahler', 'mahler_rung_bin')


def T(x):
    return (3 * x + (x & 1)) // 2


def rung_horizon(n, g, cap=5000):
    """Exact: the number of code bits read when two 1s first come closer than g; None if still pure at cap."""
    last, x = -10 ** 9, n
    for j in range(cap):
        if x & 1:
            if j - last < g:
                return j + 1
            last = j
        x = T(x)
    return None


def Y(n, g):
    """Words of length n with every two 1s at distance >= g (the first 1 unconstrained)."""
    st = Counter({g: 1})
    for _ in range(n):
        nx = Counter()
        for s, k in st.items():
            nx[min(s + 1, g)] += k
            if s >= g:
                nx[1] += k
        st = nx
    return sum(st.values())


def lam(g):
    lo, hi = 1.0, 2.0
    for _ in range(100):
        m = (lo + hi) / 2
        if m ** g - m ** (g - 1) - 1 > 0:
            hi = m
        else:
            lo = m
    return lo


def build():
    os.makedirs(os.path.dirname(BIN), exist_ok=True)
    subprocess.run(['cc', '-O3', '-o', BIN, os.path.join(HERE, 'mahler_rung_search.c')], check=True)


def chunk(args):
    g, w, pb, prefix = args
    out = subprocess.run([BIN, str(g), str(w), str(pb), str(prefix)], capture_output=True, text=True, check=True).stdout
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


def search(pool, g, w, pb=8):
    hist, strag, best = Counter(), [], (0, 0)
    for h, s, mx in pool.imap_unordered(chunk, [(g, w, pb, p) for p in range(1 << pb)]):
        hist.update(h); strag.extend(s)
        if mx[0] > best[0] or (mx[0] == best[0] and mx[1] < best[1]):
            best = mx
    alive = []
    for n in strag:
        h = rung_horizon(n, g)
        if h is None:
            alive.append(n)
            continue
        hist[h] += 1
        if h > best[0]:
            best = (h, n)
    return hist, best, len(strag), alive


def identity_ok(hist, w, g, unresolved=0):
    surv, acc = {}, unresolved
    for t in range(max(hist), -1, -1):
        surv[t] = acc
        acc += hist.get(t, 0)
    for t in range(1, w):
        q, r = divmod(surv.get(t, 0) + 1, 1 << (w - t))
        if r or q != Y(t, g):
            return False
    return True


def control():
    build()
    with Pool(9) as pool:
        for g in range(3, 9):
            hist, best, ns, alive = search(pool, g, 20, 6)
            exact = Counter(rung_horizon(n, g) for n in range(1, 1 << 20))
            ok = hist == exact and identity_ok(hist, 20, g)
            print('R0 g=%d W=20: walker equals exact: %s | max %s | identity %s' % (
                g, hist == exact, best, identity_ok(hist, 20, g)), flush=True)
            if not ok:
                sys.exit('R0 FAILED at g=%d: the instrument gate failed (GC1234)' % g)


def run():
    build()
    if rung_horizon(2 ** 99, 8) != 101:                 # GPT's fixed control (GC1234)
        sys.exit('fixed control failed: rung horizon of 2^99 at g = 8 should be 101')
    t0 = time.time()
    plan = [(3, 63), (4, 70), (5, 80), (6, 90), (8, 100)]
    with Pool(9) as pool:
        for g, w in plan:
            t1 = time.time()
            hist, best, ns, alive = search(pool, g, w)
            total = sum(hist.values()) + len(alive)
            ok = total == (1 << w) - 1 and identity_ok(hist, w, g, len(alive))
            coin = w / (1 - math.log2(lam(g)))
            print('g=%d W=%d: mass %s, identity %s, max rung horizon %d at n = %d (%.3f W; coin %.1f, ratio %.3f), '
                  'stragglers %d, survivors %s, %.0f s' % (g, w, total == (1 << w) - 1, ok, best[0], best[1],
                  best[0] / w, coin, best[0] / coin, ns, alive if alive else 'none', time.time() - t1), flush=True)
            if not ok:
                print('   QUARANTINED: mass or identity failed at g=%d; no R2 claim for this range' % g, flush=True)
            if g == 3:
                r1 = best[0] == 157 and rung_horizon(1541211973603965806, 3) == 157
                print('   R1: max 157 and rung horizon of 1541211973603965806 = 157:', r1, flush=True)
                if not r1:
                    sys.exit('R1 FAILED: the cross-instrument gate failed, so no larger search is examined (GC1234)')
            print('   HIST', ' '.join('%d:%d' % (h, hist[h]) for h in sorted(hist)), flush=True)
    print('total %.0f s' % (time.time() - t0))


if __name__ == '__main__':
    control() if sys.argv[1] == 'control' else run()
