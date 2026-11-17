#!/usr/bin/env python3
"""rule30_cloud_front_spectrum.py: the single cell's left-band edge, its Fourier spectrum, and a proved floor.

RUN-ON:     cpu (Python 3 standard library; big-integer rows; a pure-Python FFT)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_front_spectrum.py [LOG2T=19]
COST:       about two minutes at LOG2T = 19.

Why (the owner, 2026-10-09): "since the wave front line is jagged, it is well suited a Fourier transformation itself
to inspect for frequency spikes. Second, if the front wanders left on average always, does it ever literally reach
the left edge, does it tend towards it but never reach it, or does it settle on some distance limit it can never go
past." And, after the owner's screenshot of the left front's chart: "the graph looks really weird run to its end, it
follows the curve and then rapidly spikes up crossing the 0 root" (the deviation B(t) - 0.754 t falls to about -700
near 2^18, then rises to +600 by 2^19; §8.74 recorded -533 at 2^17 and +592 at 2^19).

The front is §8.74's exact edge: V_t has bit e = x_t(-t + e), V' = (V << 2) ^ ((V << 1) | V), B(t) = the lowest set
bit of V_t ^ V_(t+P) with P = 2^10, and the edge is the cell x = B(t) - t. Its distance from the left edge is B(t).
The signal transformed is the front's step dB(t) = B(t + 1) - B(t), which is stationary where B grows linearly (its
running sum is the front itself, so the front's spectrum is dB's divided by f^2).

Part 1, by hand (before the run; elementary, and the settling step of L382). Write D_e(t) for left diagonal e. Rule
30 gives D_e(t + 1) = D_(e-2)(t) XOR (D_(e-1)(t) OR D_e(t)). Suppose D_(e-1) and D_(e-2) are periodic from time s
with common period p.
  (a) If D_(e-1) has a black cell in its period, the first black time r >= s resets D_e: D_e(r + 1) =
      NOT D_(e-2)(r), whatever D_e(r) was. From r + 1 on, D_e is a function of its parents' periodic values, so it is
      periodic from r + 1 with period p. And r <= s + W, where W is the longest white run in D_(e-1)'s cycle.
  (b) If D_(e-1) is white from s on, D_e(t + 1) = D_e(t) XOR D_(e-2)(t), so D_e is periodic from s with period p or
      2p (2p exactly when D_(e-2)'s cycle has an odd number of black cells: the period doubling of §8.27).
So every left diagonal settles at a finite time, and tau(e) <= max(tau(e-1), tau(e-2)) + c_(e-1) with c = 1 + W in
case (a) and c = 0 in case (b). Consequences: the edge never reaches the left edge (B(t) >= 1, diagonal 0 is black
for ever) and its distance from it, B(t), grows without bound. Iterating the bound with the c's read off the settled
stripes gives a floor U(e) >= tau(e), so B(t) >= max{e : U(e') <= t for all e' < e}: a slope the band cannot fall
below while those stripes hold, the same for every seed with the universal stripes of §8.31.

PREDICTIONS, written 2026-10-09 before any run of this script (LOG2T = 19).
  FS1 (control). B never decreases; B(T)/T is within 0.002 of §8.74's 0.7563 slope; the mean of dB equals
      (B(end) - B(start)) / N in each window (the FFT's zero bin); and U(e) >= tau(e) for every e < B(T) (part 1's
      bound holds on the data).
  FS2 (blind; the band's rhythm). In the late window t in [2^18, 2^19), dB's periodogram has at least 3 spikes, a
      spike being a bin with at least 20 times the median power of the 128 bins around it. Every spike lies at a
      multiple of 1/128 cycles per step, and the strongest lies at a multiple of 1/16. Reason: the band's stripes have
      periods 16 to 64 at those depths (§8.30, §8.31), and §8.31 found the band's decisions timed by its own rhythm
      (11 mod 16). Confidence 0.55.
  FS3 (blind; the random-walk part). Away from the spikes, dB's spectrum is close to flat: a log-log slope between
      -0.4 and +0.3 over f in [2^-14, 2^-7] (a random-walk front, §8.74's alpha = 0.53, gives 1 - 2 alpha = -0.06).
      Confidence 0.6.
  FS4 (blind; the floor). The mean of c over the settled diagonals, c_bar, lies between 2.5 and 4.5, so the proved
      floor holds the front at x >= -(1 - 1/c_bar) t + O(1), a line between -0.6 t and -0.78 t, well left of the
      measured -0.244 t. Confidence 0.5.
UNEXPECTED CHECK, FS5: the rhythm changes with depth. In the early window t in [2^12, 2^13) (B near 3,000 to 6,000,
  stripes of period 16) every spike lies at a multiple of 1/16, while the late window has at least one spike at an
  odd multiple of 1/32 or finer. Confidence 0.4.
  FS6a (from the screenshot, so not blind). The late rise is real and is a change of the band's speed, not of the
      drawing: B is exact (a repeat proves periodicity, and lag 2P gives the same B), and its mean speed over
      [2^18, 2^19) exceeds its mean over [2^16, 2^17) by at least 0.002 diagonals per step. The log time axis puts
      262,144 rows in the last octave, which is why a gentle change looks like a spike.
  FS6b (blind). The change of speed coincides with a change in the stripes: an eventually-white diagonal (where the
      period may double, §8.27) lies at a depth the band reaches between t = 2^17.5 and 2^18.5. Confidence 0.35.
      Counterfactual: none there means the rise is the band's own random-walk wander, made sharp by the log axis.
Counterfactual: no spikes would mean the front's jaggedness carries no trace of the stripes' periods, pure noise; a
  spike off the dyadic grid (near 1/3, 1/7 or 1/56, say) would mean a second clock, which nothing here predicts.
REFUTED-BY: FS1 failing (the definition, the FFT or the bound); FS2 to FS5 failing as worded.
Disclosed: after writing these predictions and before pushing them, a smoke test at LOG2T = 14 (to exercise the code)
  showed c_bar = 4.61 there and no spikes in the early window. The predictions above are unchanged.

OUTCOME, 2026-10-09 (three runs between 10:29 and 10:34 BST, 55 s each, LOG2T = 19). The first run skipped the late
  window: dB stopped one row short of t = 2^19 (fixed, range(T); every other number was unchanged on rerun). The
  third run added the `posthoc` lines (tallest peaks, folds), chosen after seeing no spikes.
  FS1 PASS. B never decreases; B(T)/T = 0.7551 (§8.74's slope 0.7563); each window's zero bin matches its B
    difference; U(e) >= tau(e) at all 395,905 settled diagonals.
  FS2 REFUTED. No spike in the late window, nor in the early or middle ones. Post hoc, the tallest peaks are 13.5,
    19.6 and 17.1 times the local median in windows of 2^11, 2^14 and 2^17 bins, where pure noise (each bin's ratio
    exceeds r with chance 2^-r) gives about 11, 14 and 17. Folding the steps by t mod 16, 32 and 64 gives
    chi-squared 11.5 to 69.4 on 15 to 63 degrees of freedom: no rhythm at the stripes' periods.
  FS3 HELD: slope -0.027 (random walk -0.06). The step variance is 1.15 to 1.25 per row, so the front strays
    about sqrt(1.25 t) cells, 810 at 2^19: the chart's +-sqrt(t) guides are the right yardstick.
  FS4 REFUTED as worded: c_bar = 5.33 (4.61 to 4.65 where the stripes have period 16, 5.52 where they have period
    32). The floor holds the front at x >= -0.78 t at 2^18 and -0.81 t asymptotically, far weaker than the true
    -0.245 t: real diagonals settle 1.32 rows apart on average, not the bound's 5.3.
  FS5 REFUTED: no spikes anywhere, so no change of rhythm with depth.
  FS6a HELD: mean band speed 0.75187 over [2^16, 2^17), 0.75789 over [2^18, 2^19), +0.0060. FS6b REFUTED: the
    eventually-white diagonals are 2, 7, 28, 399, 53207, 58286 and 87866, and the band reaches the last at t =
    117,324 (2^16.84), where the stripes' period goes from 16 to 32; none lies in [2^17.5, 2^18.5].
  The late rise, post hoc. From t = 311,296 (deviation -605) to 2^19 (+593) the edge climbs 1,198 cells in 212,991
    rows. 234 of them are the dashed line's slope, 0.754, sitting below the band's long-run 0.7551; the other 964
    are a fast stretch (0.7597) of 1.9 random-walk standard deviations (sqrt(1.25 x 212,991) = 516), picked out
    after the fact. The 2^14-row window speeds range from 0.740 to 0.777. So the climb is real, ordinary for this
    walk, and looks sudden because the doubling time axis gives its last octave half of all the rows.

CORRECTED 2026-10-09 after GPT's GC748, GC749 and GC752 (read by hand: correct) and Local's L390; the text above
  is kept as registered and first written.
  Part 1's "its distance from it, B(t), grows without bound" is wrong for a fixed lag. B_P(t) <= j_P, the first
    diagonal whose eventual period does not divide P (GC736), and it eventually equals j_P (L390 shows B_2 .. B_16 at
    their caps in data). What grows without bound is the unrestricted settled prefix, and the age-t ordered prefix
    C(t) = B_Q(t) with Q the largest power of 2 at most t (GC752); no rate is proved. The front never reaching the
    left edge stands (B >= 1).
  The array tau is the P-prefix onset min{t : B_P(t) > e}, not each diagonal's own settling time, so U >= tau and
    c_bar are a floor for the measured prefix (395,905 diagonals) only. FS4's "-0.81 t asymptotically" should read:
    a finite-prefix floor, from which no asymptotic floor follows.
  Lag 2P gave the same B at every t <= 2^19 (§8.74), so by GC752's plateau lemma B_1024(t) = C(t) at every
    1,024 <= t <= 2^19: within the run, the measured curve is the age-t ordered prefix.
"""
import cmath
import math
import sys
from collections import deque

LOG2T = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 19
POSTHOC = "posthoc" in sys.argv[1:]                     # added after the first runs: tallest peaks and fold tests
P = 1 << 10
T = 1 << LOG2T


def fft(a):
    """In-place iterative radix-2 FFT of a list of complex numbers (length a power of 2)."""
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    size = 2
    while size <= n:
        w = cmath.exp(-2j * math.pi / size)
        half = size // 2
        tw = [w ** k for k in range(half)]
        for start in range(0, n, size):
            for k in range(half):
                u = a[start + k]
                v = a[start + k + half] * tw[k]
                a[start + k] = u + v
                a[start + k + half] = u - v
        size <<= 1
    return a


def spectrum(dB, lo, n):
    seg = dB[lo:lo + n]
    m = sum(seg) / n
    X = fft([complex(v - m) for v in seg])
    return m, [abs(X[k]) ** 2 / n for k in range(n // 2 + 1)]


def spikes(pw, n, ratio=20.0, half=64):
    out = []
    for k in range(1, n // 2 + 1):
        nb = [pw[q] for q in range(max(1, k - half), min(n // 2, k + half) + 1) if abs(q - k) > 2]
        nb.sort()
        med = nb[len(nb) // 2] if nb else 0.0
        if med > 0 and pw[k] >= ratio * med:
            out.append((pw[k] / med, k))
    return out


def dyadic(k, n):
    """k/n as a reduced fraction a/2^m."""
    g = math.gcd(k, n)
    return f"{k // g}/{n // g}"


def main():
    win, V, B = deque(), 1, []
    for s in range(T + P + 1):
        win.append(V)
        if len(win) > P:
            d = win.popleft() ^ V
            B.append((d & -d).bit_length() - 1)
        V = (V << 2) ^ ((V << 1) | V)
    rows = list(win)                                       # rows T+1 .. T+P: one full period of every settled diagonal
    assert all(B[i + 1] >= B[i] for i in range(T - 1)), "FS1: B decreased"
    print(f"T = 2^{LOG2T}, P = 2^10; B(T-1) = {B[T - 1]}, B/T = {B[T - 1] / T:.4f}")
    dB = [B[t + 1] - B[t] for t in range(T)]            # B has T + 1 entries (the first run had T - 1)

    # ---- part 2: the spectrum of the front's steps ----
    for name, lo, n in [("early", 1 << 12, 1 << 12), ("middle", 1 << 15, 1 << 15), ("late", 1 << 18, 1 << 18)]:
        if lo + n > len(dB):
            continue
        m, pw = spectrum(dB, lo, n)
        mean_chk = (B[lo + n] - B[lo]) / n
        sp = sorted(spikes(pw, n), reverse=True)
        if POSTHOC:
            top = sorted(spikes(pw, n, ratio=0.0), reverse=True)[:5]
            var = sum(pw[1:n // 2]) / (n // 2 - 1)
            print(f"  posthoc: step variance {var:.4f}; tallest peaks (x local median): " +
                  ", ".join(f"{r:.1f} at f = {dyadic(k, n)}" for r, k in top))
            for q in (16, 32, 64):
                fold = [0.0] * q
                for t in range(lo, lo + n):
                    fold[t % q] += dB[t] - m
                chi = sum(v * v for v in fold) / (var * n / q)            # about chi-squared, q - 1 dof, if no rhythm
                print(f"  posthoc: fold by t mod {q}: chi-squared {chi:.1f} on {q - 1} degrees of freedom")
        print(f"\n{name} window t in [{lo}, {lo + n}): mean step {m:.5f} (B check {mean_chk:.5f}); {len(sp)} spikes")
        for r, k in sp[:24]:
            print(f"  f = {dyadic(k, n):>9s} = {k / n:.6f} cycles/step (period {n / k:8.2f}): {r:7.1f} x local median")
        off = [k for r, k in sp if k % (n // 128)]
        print(f"  spikes off the 1/128 grid: {len(off)}"
              + (f" ({', '.join(dyadic(k, n) for k in off[:8])})" if off else ""))
        fine = [k for r, k in sp if k % (n // 16)]
        print(f"  spikes off the 1/16 grid: {len(fine)}"
              + (f" ({', '.join(dyadic(k, n) for k in fine[:8])})" if fine else ""))
        if name == "late":
            # low-frequency slope away from the spikes, log-binned
            spk = {k for r, k in sp}
            xs, ys = [], []
            for j in range(4, 11):                       # f in [2^-14, 2^-7) for n = 2^18: bins 2^4 .. 2^11
                ks = [k for k in range(1 << j, 1 << (j + 1)) if k not in spk]
                if ks:
                    xs.append(j - math.log2(n))
                    ys.append(math.log2(sum(pw[k] for k in ks) / len(ks)))
            mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
            slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
            print(f"  low-frequency log-log slope of the step spectrum over f in [2^-14, 2^-7): {slope:+.3f}")
            # the folded profile: the mean step by t mod 64
            fold = [0.0] * 64
            for t in range(lo, lo + n):
                fold[t % 64] += dB[t]
            fold = [v / (n / 64) for v in fold]
            print("  mean step by t mod 64:", " ".join(f"{v:.2f}" for v in fold))

    # ---- part 3: the late rise in the chart ----
    print("\nthe deviation B(t) - 0.754 t along the last three octaves (the chart's curve):")
    for k in range(LOG2T - 3, LOG2T):
        pts = [int(2 ** (k + j / 8)) for j in range(0, 8, 2)]
        print("  " + "  ".join(f"2^{math.log2(u):.3f}: {B[min(T - 1, u)] - 0.754 * u:+6.0f}" for u in pts))
    print("the band's local speed (diagonals per step) over windows of 2^14 rows, with the depth reached:")
    sp_rows = []
    for lo in range(1 << 14, T - (1 << 14) + 1, 1 << 14):
        hi = lo + (1 << 14)
        sp_rows.append((lo, (B[hi - 1] - B[lo]) / (hi - 1 - lo), B[lo]))
    for lo, v, d in sp_rows:
        print(f"  t from {lo:7d} (2^{math.log2(lo):.2f}), depth {d:7d}: speed {v:.4f}, front speed {1 - v:.4f}")
    if LOG2T >= 19:
        m16 = (B[(1 << 17) - 1] - B[1 << 16]) / ((1 << 16) - 1)
        m18 = (B[T - 1] - B[1 << 18]) / ((1 << 18) - 1)
        print(f"mean speed over [2^16, 2^17): {m16:.5f}; over [2^18, 2^19): {m18:.5f}; difference {m18 - m16:+.5f}")

    # ---- part 1's floor: the reset bound with the settled stripes' white runs ----
    Bm = B[T - 1]
    mask = (1 << Bm) - 1
    rows = [r & mask for r in rows]
    anyblack = 0
    for r in rows:
        anyblack |= r
    white_for_ever = mask & ~anyblack                   # diagonals white through the whole cycle (case b)
    # W_e = the longest cyclic white run of diagonal e: grow windows of L consecutive rows
    W = {}
    orwin = rows[:]                                     # orwin[s] = OR of rows s .. s+L-1 (cyclic), L = 1
    alive = 0
    for s in range(P):
        alive |= ~orwin[s] & mask
    alive &= anyblack
    L = 1
    while alive:
        L += 1
        orwin = [orwin[s] | rows[(s + L - 1) % P] for s in range(P)]
        nxt = 0
        for s in range(P):
            nxt |= ~orwin[s] & mask
        nxt &= alive
        dead = alive & ~nxt
        while dead:
            low = dead & -dead
            W[low.bit_length() - 1] = L - 1
            dead ^= low
        alive = nxt
    tau, t = [], 0
    for e in range(Bm):
        while B[t] <= e:
            t += 1
        tau.append(t)
    c = [0 if (white_for_ever >> e) & 1 else 1 + W.get(e, 0) for e in range(Bm)]
    U = [tau[0], tau[1]] + [0] * (Bm - 2)
    for e in range(2, Bm):
        U[e] = max(U[e - 1], U[e - 2]) + c[e - 1]
    bad = sum(1 for e in range(Bm) if U[e] < tau[e])
    nb = sum(1 for e in range(Bm) if (white_for_ever >> e) & 1)
    print(f"\nfloor: {Bm} settled diagonals, {nb} white for ever; U(e) < tau(e) at {bad} diagonals (FS1 wants 0)")
    hist = {}
    for e in range(Bm):
        hist[c[e]] = hist.get(c[e], 0) + 1
    print("  c = 1 + longest white run (0 for a white diagonal): " +
          ", ".join(f"{k}: {v}" for k, v in sorted(hist.items())))
    # the stripes by depth: eventually-white diagonals, and the joint period of each stretch between them
    whites = [e for e in range(Bm) if (white_for_ever >> e) & 1]
    print("  eventually-white diagonals (period doublings can follow, §8.27):", whites)
    edges = [0] + [w + 1 for w in whites] + [Bm]
    for a, b in zip(edges, edges[1:]):
        if b <= a:
            continue
        rm = ((1 << b) - 1) ^ ((1 << a) - 1)
        per = next(q for q in [1 << j for j in range(11)]
                   if all(((rows[s] ^ rows[(s + q) % P]) & rm) == 0 for s in range(P)))
        tr = tau[a] if a < Bm else None
        print(f"    diagonals {a:6d} .. {b - 1:6d}: period {per:4d}, mean c {sum(c[a:b]) / (b - a):.3f}, "
              f"band reaches diagonal {a} at t = {tr} (2^{math.log2(max(1, tr)):.2f})")
    for lo_d in range(0, Bm - 25000, 25000):
        print(f"    mean c over diagonals {lo_d} .. {lo_d + 24999}: {sum(c[lo_d:lo_d + 25000]) / 25000:.4f}")
    cbar = sum(c) / Bm
    print(f"  c_bar = {cbar:.4f}; floor slope 1/c_bar = {1 / cbar:.4f}; "
          f"front held at x >= -{1 - 1 / cbar:.4f} t + O(1)")
    for k in range(10, LOG2T):
        tt = 1 << k
        lo_e = 0
        while lo_e < Bm and U[lo_e] <= tt:
            lo_e += 1
        print(f"  t = 2^{k}: B = {B[tt]:7d} (x/t {(B[tt] - tt) / tt:+.4f}); "
              f"floor B >= {lo_e:7d} (x/t >= {(lo_e - tt) / tt:+.4f})")


if __name__ == "__main__":
    main()
