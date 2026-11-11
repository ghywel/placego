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
Usage: cloud_lift_left_2adic_census.py
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
    print(f"   binary onset divided by depth, depths 20..{DEPTH}: least {r.min():.3f}, median {np.median(r):.3f}, largest {r.max():.3f}"
          f" | every onset exceeds its depth (the centre is read at t = n): {bool((on[1][3:] > np.arange(3, DEPTH + 1)).all())}")
    print(f"seconds {time.time() - t0:.0f}")


if __name__ == "__main__":
    main()
