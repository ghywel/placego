#!/usr/bin/env python3
"""Cloud CL778, item L: the left edge of the integer lift of rule 30 modulo 2^k, every depth to 420.

Left diagonals u_n(t) = 1 + A_t(n - t) of the lift A' = l + c + r + c r from one cell obey
    u_n(t+1) = u_n(t) u_(n-1)(t) + u_(n-2)(t) - 1,   u_0 = 2, u_n = 1 for n < 0, u_n(0) = 1 for n > 0.
Modulo 2 this is rule 30 itself (u odd = white cell), whose left diagonals are eventually periodic with periods
powers of 2 (Jen 1986; Rowland; the kit's Rule30LeftReset), doubling at depths 3, 8, 29, 400 after the white
diagonals 2, 7, 28, 399 (record G2.3).  GPT proved (GC2931, GC2933; carried in CL778) that modulo 2^k depths 3, 5, 6
have least eventual period exactly 2^k and depths 2 and 4 are eventually constant.

Question: is there any clock on the left of the lift beyond rule 30's own left clock read to more digits?
For n <= 420 and k <= 6, to t = 2^17: each diagonal's least eventual period 2^e(n,k) on the tail [2^16, 2^17), the
prefix exponent E(n,k) = max_(m <= n) e(m,k), onsets, and the eventually constant diagonals.

Predictions (CL778, before the run):
  L1 (control)  E(n,1) = 1, 2, 3, 4 on 3..7, 8..28, 29..399, 400..420.
  L2 ("one clock", chance 0.5)  E(n,k) = E(n,1) + k - 1 for 3 <= n <= 420, 2 <= k <= 6.
  L2' (0.9)  E(n,k+1) = E(n,k) + 1 for k >= 3 at every depth, and E(n,k) - E(n,1) - (k-1) in {-1, 0, 1, 2}.
  Counterfactual: E(n,k) - E(n,1) >= 2(k-1) at some n >= 8 (a second independent 2-adic counter).
  L3 (exploratory, 0.6)  the only diagonals eventually constant modulo 64 are 2 (value 1) and 4 (value 0).
Usage: cloud_lift_left_2adic_census.py           (parts 1 and 2: depths to 420)
       cloud_lift_left_2adic_census.py --deep    (part 3: depths to 53,300)
       cloud_lift_left_2adic_census.py --deep 18 (part 3 again to t = 2^18, judged on the last 2^16 ticks)
"""
import sys, time
import numpy as np

K, DEPTH, LOGT, EMAX = 6, 420, 17, 14
T = 1 << LOGT; TAIL = T // 2


def simulate():
    mask = (1 << K) - 1
    u = np.ones(DEPTH + 2, dtype=np.int64); u[1] = 2          # index n + 1
    hist = np.empty((T, DEPTH + 1), dtype=np.uint8)           # column n: depth n, 0 <= n <= DEPTH
    for t in range(T):
        hist[t] = u[1:]
        nxt = u.copy()
        nxt[2:] = (u[2:] * u[1:-1] + u[:-2] - 1) & mask
        u = nxt
    return hist


def exponents(h):
    """Least e with the tail 2^e-periodic, per depth; -1 if none up to EMAX."""
    e = np.full(h.shape[1], -1, dtype=np.int64)
    for j in range(EMAX + 1):
        P = 1 << j
        ok = (h[TAIL:T - P] == h[TAIL + P:T]).all(axis=0)
        e[(e < 0) & ok] = j
    return e


def onsets(h, e):
    """Least t0 from which the diagonal has period 2^e, per depth (settled depths only)."""
    on = np.full(h.shape[1], -1, dtype=np.int64)
    for j in sorted(set(e.tolist()) - {-1}):
        cols = np.nonzero(e == j)[0]; P = 1 << j
        diff = h[:T - P][:, cols] != h[P:][:, cols]
        last = np.where(diff.any(axis=0), diff.shape[0] - 1 - np.argmax(diff[::-1], axis=0), -1)
        on[cols] = last + 1
    return on


def ranges(vals, lo=0):
    out = []; start = lo
    for n in range(lo + 1, len(vals) + 1):
        if n == len(vals) or vals[n] != vals[start]:
            out.append((start, n - 1, vals[start])); start = n
    return out


def main():
    t0 = time.time()
    hist = simulate()
    print(f"== left diagonals 0..{DEPTH} modulo 2^{K}, t < 2^{LOGT}; periods judged on [2^{LOGT - 1}, 2^{LOGT}); {time.time() - t0:.0f} s")
    e = {}; E = {}; on = {}
    for k in range(1, K + 1):
        h = hist & ((1 << k) - 1)
        e[k] = exponents(h); on[k] = onsets(h, e[k])
        E[k] = np.maximum.accumulate(e[k])
    unsettled = {k: np.nonzero(e[k] < 0)[0].tolist() for k in e}
    print("   depths not settled on the window:", {k: (v[:5], len(v)) for k, v in unsettled.items() if v} or "none")
    # --- controls
    b = e[1]
    stage = [(lo, hi, int(v)) for lo, hi, v in ranges(E[1].tolist(), 3)]
    print("   binary prefix exponent E(n,1) by depth range (from 3):", stage)
    c1 = stage == [(3, 7, 1), (8, 28, 2), (29, 399, 3), (400, 420, 4)]
    white = [n for n in range(2, DEPTH + 1) if b[n] == 0 and (hist[T - 1, n] & 1) == 1]
    black = [n for n in range(2, DEPTH + 1) if b[n] == 0 and (hist[T - 1, n] & 1) == 0]
    print(f"   L1 control (stages 3..7, 8..28, 29..399, 400..420): {c1} | white diagonals (u odd for good): {white}"
          f" | constant black diagonals: {len(black)}, first {black[:12]}")
    c2 = all(e[k][3] == k and e[k][5] == k and e[k][6] == k and e[k][2] == 0 and e[k][4] == 0 for k in e)
    print(f"   control (GC2931, GC2933): e(3,k) = e(5,k) = e(6,k) = k and depths 2, 4 constant, k <= {K}: {c2}")
    # --- L2
    delta = {k: (E[k] - E[1] - (k - 1)) for k in range(2, K + 1)}
    L2 = all((delta[k][3:] == 0).all() for k in delta)
    print(f"L2 (E(n,k) = E(n,1) + k - 1 for 3 <= n <= {DEPTH}, 2 <= k <= {K}): {L2}")
    for k in delta:
        rs = [(lo, hi, int(v)) for lo, hi, v in ranges(delta[k].tolist(), 3) if v != 0]
        print(f"   k = {k}: E(n,k) by depth range {[(lo, hi, int(v)) for lo, hi, v in ranges(E[k].tolist(), 3)]}"
              + (f" | deviation from the law on {rs}" if rs else " | no deviation"))
    step = all(((E[k + 1] - E[k])[3:] == 1).all() for k in range(3, K))
    inset = all(np.isin(delta[k][3:], (-1, 0, 1, 2)).all() for k in delta)
    print(f"L2' (one more digit, one more doubling, for k >= 3; deviation in -1..2): {step and inset} (steps {step}, range {inset})")
    cf = [(int(n), k) for k in delta for n in range(8, DEPTH + 1) if E[k][n] - E[1][n] >= 2 * (k - 1)]
    print(f"counterfactual (a second counter: E(n,k) - E(n,1) >= 2(k-1) at some n >= 8): {'seen at ' + str(cf[:6]) if cf else 'not seen'}")
    # --- scalar exponents and the constant diagonals
    const = [(n, int(hist[T - 1, n])) for n in range(0, DEPTH + 1) if e[K][n] == 0]
    print(f"L3: diagonals eventually constant modulo {1 << K}: {const}")
    print("   scalar exponents e(n,k), k = 1..6, depths 1..40:")
    for lo in range(1, 41, 8):
        print("     " + " | ".join(f"{n}: " + "".join(str(int(e[k][n])) if e[k][n] < 10 else "+" for k in range(1, K + 1)) for n in range(lo, lo + 8)))
    sd = {k: (e[k] - e[1] - (k - 1)) for k in range(2, K + 1)}
    for k in sd:
        vals, cnt = np.unique(sd[k][3:][e[1][3:] > 0], return_counts=True)
        print(f"   k = {k}: among depths whose binary diagonal is not constant, e(n,k) - e(n,1) - (k-1) takes values {dict(zip(vals.tolist(), cnt.tolist()))}")
    cb = [n for n in range(2, DEPTH + 1) if e[1][n] == 0]
    print(f"   binary-constant diagonals ({len(cb)}): their exponents modulo 2^k, k = 2..6, as (depth, colour, exponents):")
    print("     " + " ".join(f"({n},{'w' if hist[T - 1, n] & 1 else 'b'}," + "".join(str(int(e[k][n])) for k in range(2, K + 1)) + ")" for n in cb[:40]))
    # --- onsets
    for k in (1, K):
        sel = [3, 6, 8, 12, 20, 29, 50, 100, 200, 300, 399, 400, 420]
        print(f"   onset of periodicity modulo 2^{k} at depths {sel}: {[int(on[k][n]) for n in sel]}")
    r = on[1][20:] / np.arange(20, DEPTH + 1)
    late = [n for n in range(3, DEPTH + 1) if on[1][n] <= n]
    print(f"   binary onset divided by depth, depths 20..{DEPTH}: least {r.min():.3f}, median {np.median(r):.3f}, largest {r.max():.3f}"
          f" | depths whose diagonal is already periodic when it crosses the centre (onset <= n): {late}")
    print(f"seconds {time.time() - t0:.0f}")
    high_digits()


def high_digits():
    """Second part (CL778 addendum 1, prediction L4): digits 1..13 to t = 2^19, and the certificate of gamma(n)."""
    K2, LOGT2, EMAX2 = 13, 19, 17
    T2 = 1 << LOGT2; TAIL2 = T2 // 2
    t0 = time.time()
    mask = (1 << K2) - 1
    u = np.ones(DEPTH + 2, dtype=np.int64); u[1] = 2
    hist = np.empty((T2, DEPTH + 1), dtype=np.uint16)
    for t in range(T2):
        hist[t] = u[1:]
        nxt = u.copy()
        nxt[2:] = (u[2:] * u[1:-1] + u[:-2] - 1) & mask
        u = nxt
    print(f"== second part: modulo 2^{K2}, t < 2^{LOGT2}, periods judged on [2^{LOGT2 - 1}, 2^{LOGT2}); {time.time() - t0:.0f} s")
    E = {}
    for k in range(1, K2 + 1):
        h = hist & np.uint16((1 << k) - 1)
        e = np.full(h.shape[1], -1, dtype=np.int64)
        for j in range(EMAX2 + 1):
            if (e >= 0).all():
                break
            P = 1 << j
            ok = (h[TAIL2:T2 - P] == h[TAIL2 + P:T2]).all(axis=0)
            e[(e < 0) & ok] = j
        assert (e >= 0).all(), f"unsettled depths at k = {k}"
        E[k] = np.maximum.accumulate(e)
        print(f"   k = {k:2d}: E(n,k) by depth range {[(lo, hi, int(v)) for lo, hi, v in ranges(E[k].tolist(), 3)]}")
    gam = {(3, 7): 0, (8, 28): 1, (29, DEPTH): 2}
    L4 = all((E[k][lo:hi + 1] == k + g).all() for k in range(3, K2 + 1) for (lo, hi), g in gam.items())
    print(f"L4 (E(n,k) = k, k + 1, k + 2 on depths 3..7, 8..28, 29..{DEPTH} for 3 <= k <= {K2}): {L4}")
    print("   certificate of gamma(n) by the persistence lemma: a level k >= 2 with P_k >= 2 max(P_2, n P_1) and P_(k+1) = 2 P_k")
    for lo, hi in ((3, 7), (8, 28), (29, 399), (400, DEPTH)):
        P1 = 1 << int(E[1][hi]); P2 = 1 << int(E[2][hi])
        need = 2 * max(P2, hi * P1)
        k = next(k for k in range(2, K2) if (1 << int(E[k][lo:hi + 1].min())) >= need)
        grow = bool((E[k + 1][lo:hi + 1] == E[k][lo:hi + 1] + 1).all())
        g = sorted(set((E[k][lo:hi + 1] - k).tolist()))
        print(f"     depths {lo}..{hi}: P_1 = {P1}, P_2 = {P2}, threshold {need}; first level past it k = {k} (P_k = {1 << int(E[k][lo])});"
              f" P_(k+1) = 2 P_k at every depth of the range: {grow}; gamma = {g}")
    print(f"seconds {time.time() - t0:.0f}")


def deep():
    """Third part (CL778 addendum 2, prediction L5): depths to 53,300 modulo 2^8, by a rolling comparison.

    Nothing large is stored: a ring of the last 2^12 rows, and for each lag 2^j the OR over the last 2^15 ticks of
    row(t) xor row(t - 2^j).  A diagonal has period 2^j modulo 2^k on that window exactly when the low k bits of its
    OR are zero."""
    D2, K2, LOGT2, LOGW, JMAX = 53300, 8, 17, 15, 12
    if sys.argv[-1].isdigit():                       # robustness rerun: a later and longer window
        LOGT2 = int(sys.argv[-1]); LOGW = LOGT2 - 2
    T2 = 1 << LOGT2; W = 1 << LOGW; R = 1 << JMAX
    t0 = time.time()
    mask = (1 << K2) - 1
    u = np.ones(D2 + 2, dtype=np.int64); u[1] = 2
    ring = np.zeros((R, D2 + 1), dtype=np.uint8)
    acc = np.zeros((JMAX + 1, D2 + 1), dtype=np.uint8)
    for t in range(T2):
        if t >= T2 - W - R:
            row = u[1:].astype(np.uint8)
            if t >= T2 - W:
                for j in range(JMAX + 1):
                    acc[j] |= row ^ ring[(t - (1 << j)) % R]
            ring[t % R] = row
        nxt = u.copy()
        nxt[2:] = (u[2:] * u[1:-1] + u[:-2] - 1) & mask
        u = nxt
    last = u[1:].astype(np.uint8)
    print(f"== third part: left diagonals 0..{D2} modulo 2^{K2}, t < 2^{LOGT2}; periods up to 2^{JMAX} judged on the last 2^{LOGW} ticks; {time.time() - t0:.0f} s")
    e = {}; E = {}
    for k in range(1, K2 + 1):
        ek = np.full(D2 + 1, -1, dtype=np.int64)
        for j in range(JMAX + 1):
            ok = (acc[j] & ((1 << k) - 1)) == 0
            ek[(ek < 0) & ok] = j
        e[k] = ek
        bad = np.nonzero(ek < 0)[0]
        if len(bad):
            print(f"   k = {k}: {len(bad)} depths not settled on the window, the first at depth {int(bad[0])}")
            ek = np.where(ek < 0, JMAX + 1, ek)
        E[k] = np.maximum.accumulate(ek)
        print(f"   k = {k}: E(n,k) by depth range {[(lo, hi, int(v)) for lo, hi, v in ranges(E[k].tolist(), 3)]}")
    const = np.nonzero(e[1] == 0)[0]
    white = [int(n) for n in const if n >= 2 and last[n] & 1]
    black = [int(n) for n in const if n >= 2 and not last[n] & 1]
    print(f"   control: white diagonals (u odd on the whole window): {white} | constant black diagonals: {black}")
    c = white == [2, 7, 28, 399, 53207] and [(lo, hi, int(v)) for lo, hi, v in ranges(E[1].tolist(), 3)] == [(3, 7, 1), (8, 28, 2), (29, 399, 3), (400, D2, 4)]
    print(f"   control (white diagonals 2, 7, 28, 399, 53207; binary prefix period 16 from depth 400 to {D2}): {c}")
    gam = {k: sorted(set((E[k][29:] - k).tolist())) for k in range(3, K2 + 1)}
    stay = all(g == [2] for g in gam.values())
    rise = all((E[k][29:53208] == k + 2).all() and (E[k][53208:] == k + 3).all() for k in range(3, K2 + 1))
    print(f"L5: gamma = E(n,k) - k on depths 29..{D2}, by k: {gam}")
    print(f"L5: gamma stays 2 through depth {D2}: {stay} | rises to 3 exactly at depth 53208: {rise}")
    for k in (2, 3, 8):
        print(f"   scalar exponents e(n,{k}) at depths 53200..53215: {[int(x) for x in e[k][53200:53216]]}")
    print(f"seconds {time.time() - t0:.0f}")


if __name__ == "__main__":
    deep() if "--deep" in sys.argv else main()
