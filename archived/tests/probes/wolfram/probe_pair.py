#!/usr/bin/env python3
"""probe_pair.py D T1: two probes and the nonlinear residue (inquisition round 14, H3; Cloud, CL692). Flips at x1 and x2 = x1 + D at
the same time, on a fair row (control) and in the single seed's core (t0 = 2048, x1 = +300). D1, D2, D12 are the damages; the residue
R = D12 ^ D1 ^ D2 is zero where the rule acts linearly. Report the first tick with a nonzero residue against the meeting of the
fronts, the residue density over the interval covering both damages and the residue, and the residue's left front speed.
Output: probe_pair.out. Scope (GC2520): a residue can appear before the damage supports overlap, since rho_next(x) =
delta1(x) delta2(x+1) + delta2(x) delta1(x+1) when rho = 0 (GPT's neighbouring-input identity, with a hand counterexample on the
all-black row); the equality of the first-residue and meeting ticks here (36, 34) is a fact about these two runs, not a law. The
"overlap" density is measured on the covering interval, not the literal intersection of the two supports."""
import sys, numpy as np
D, T1 = int(sys.argv[1]), int(sys.argv[2]); rng = np.random.default_rng(3)
def step(r):
    n = np.zeros_like(r); n[1:-1] = r[:-2] ^ (r[1:-1] | r[2:]); return n
def run(a, c1, c2):
    b1 = a.copy(); b1[c1] ^= 1; b2 = a.copy(); b2[c2] ^= 1; b12 = a.copy(); b12[c1] ^= 1; b12[c2] ^= 1
    first = None; dens = []; rfront = []; meet = None
    for t in range(1, T1 + 1):
        a, b1, b2, b12 = step(a), step(b1), step(b2), step(b12)
        d1 = a ^ b1; d2 = a ^ b2; d12 = a ^ b12; r = d12 ^ d1 ^ d2
        i1 = np.flatnonzero(d1); i2 = np.flatnonzero(d2)
        if len(i1) and len(i2) and meet is None and i1.max() >= i2.min(): meet = t
        nz = np.flatnonzero(r)
        if len(nz):
            if first is None: first = t
            lo, hi = (i2.min(), i1.max()) if len(i1) and len(i2) else (nz.min(), nz.max())
            lo = min(lo, nz.min()); hi = max(hi, nz.max())
            dens.append(r[lo:hi + 1].mean()); rfront.append(nz.min())
    return first, meet, dens, rfront
for name, a, c1 in (("fair row", rng.integers(0, 2, 4 * T1 + 400).astype(np.uint8), 2 * T1 + 200), ("single seed core", None, None)):
    if a is None:
        T0 = 2048; M = T0 + T1 + 64; W = 2 * M + 1; c = M; a = np.zeros(W, dtype=np.uint8); a[c] = 1
        for t in range(T0): a = step(a)
        c1 = c + 300
    first, meet, dens, rfront = run(a, c1, c1 + D)
    dens = np.array(dens); rf = np.array(rfront)
    print(f"{name}: D={D}, T1={T1}: fronts meet at tick {meet}, first nonzero residue at tick {first}; "
          f"residue density in the overlap: mean {dens.mean():.3f} (first 50 ticks {dens[:50].mean():.3f}, last 100 {dens[-100:].mean():.3f}); "
          f"residue left front speed over its life {(rf[0] - rf[-1]) / max(1, len(rf) - 1):.4f}")
print("PROBE_PAIR_DONE")
