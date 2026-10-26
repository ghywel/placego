"""universal_ruler_check.py: exact guard on L1001's Theorem U (every finite seed's right edge is the single seed's ruler, cut off).

Local, 2026-10-27, L1001 (DQ-022). The theorem is proved by hand in reports/rule30-universal-ruler.md, from GC808's
2-adic edge map and 8.73's Proposition 23. This script replays it exactly on every seed of width up to 14.

Edge code. R_t's bit k is the cell at distance k from the rightmost black cell at time t. One step is
T(R) = R XOR (2R OR 4R) (GC808). The single seed is R = 1. An emission happens at time t exactly when bit 1 of R_(t-1)
is 1, and its width is the number of zero bits between bit 0 and the next 1 of R_t.

Depth k*. k*(R0) is the largest k such that R0 mod 2^k lies on the single seed's cycle {T^s(1) mod 2^k}. Theorem U:
with s0 the time at which T^s0(1) = R0 mod 2^k*, the seed emits at time t exactly when the single seed emits at
t + s0. Its width there equals the single seed's width when that is less than k* - 1, and is exactly k* - 1 otherwise.

Predictions (written before the run):
  U1  Every seed of width 1..14 (16,383 seeds) satisfies Theorem U at every emission in 1,200 steps.
  U2  k* + 1 is always a level at which the single seed's cycle length does not double; k* = 2 exactly for the rain
      edges (R0 = 3 or 5 mod 8).
  U3  The single seed never emits a width k - 2 for a non-doubling level k (Proposition 23's gap property), through
      t = 1,200 + max s0.
Counterfactual: any mismatch refutes U or my reading of GC808's isometry.
Record searched: "odometer" 48 (CPY 2007 via GC808/GC810, 8.64, 8.77), "A094605" 10 (8.73, PROOFS 36), "Toeplitz"
(8.72, 8.73), "half-ruler" 0, "spine" 0 in this sense.

Run: python3 -I tests/probes/wolfram/universal_ruler_check.py   (exit status 1 on any failure)

Outcome (2026-10-27, M5, 8.3 s): ALL CHECKS PASS, exit 0.
- U1: all 16,383 seeds of width up to 14 (the first draft said 8,191, which counts width-14 seeds alone), at every
  emission over 1,200 steps.
- U2: depths k* = 2 (8,191 seeds, exactly the rain edges), 5, 8, 10 to 14, and 17 to 19; 56 seeds are deeper than 40
  bits.
- U3: the single seed's widths are (doubling level) - 2 over 66,000 steps.
- The cycle lengths p_k for k = 1..40 match A094605, offset by one index.

Three harness slips of mine, none touching a result:
- the first version stored the full orbit as growing integers (about 600 MB);
- its probe orbit was shorter than p_48;
- my patch had an indentation error.
The setup was rewritten modulo 2^64, which is exact for widths below 63, with KMAX = 40.
"""
import sys

STEPS = 1200
WMAX = 14
KMAX = 40
fails = []


MASK = (1 << 64) - 1          # T's low bits depend only on low bits, so widths below 63 are exact modulo 2^64


def T(R):
    return (R ^ ((R << 1) | (R << 2))) & MASK


def width(R):
    """Zero bits between bit 0 and the next set bit."""
    x = R >> 1
    return (x & -x).bit_length() - 1 if x else None


# the single seed's orbit modulo 2^64, until every cycle length p_k (k <= KMAX) is seen; then STEPS more beyond the
# longest, so that every phase s0 < p_k has its full window
spine_orbit = [1]
p = {1: 1}
while len(p) < KMAX and len(spine_orbit) < (1 << 21):
    spine_orbit.append(T(spine_orbit[-1]))
    s = len(spine_orbit) - 1
    for k in range(2, KMAX + 1):
        if k not in p and (spine_orbit[s] & ((1 << k) - 1)) == 1:
            p[k] = s
if len(p) < KMAX:
    fails.append(("setup", "cycle lengths not all found", sorted(set(range(1, KMAX + 1)) - set(p))))
for _ in range(STEPS + 4):
    spine_orbit.append(T(spine_orbit[-1]))
doubling = {k for k in range(2, KMAX + 1) if k in p and k - 1 in p and p[k] > p[k - 1]}

# U3: the single seed's widths are exactly (doubling level) - 2
for t in range(1, len(spine_orbit)):
    if spine_orbit[t - 1] & 2:
        wd = width(spine_orbit[t])
        if wd is not None and wd + 2 <= KMAX and (wd + 2) not in doubling:
            fails.append(("U3", t, wd))
            break

# first-visit index of each residue on the spine, per k, for the phase s0
first_visit = {}
for k in range(2, KMAX + 1):
    m = (1 << k) - 1
    d = {}
    for s_ in range(p[k]):
        d.setdefault(spine_orbit[s_] & m, s_)
    first_visit[k] = d

stats = {}
for w in range(1, WMAX + 1):
    for bits in range(1 << (w - 1)):
        seed = bits | (1 << (w - 1))
        R0 = int(bin(seed)[2:][::-1], 2)              # the rightmost seed cell becomes bit 0
        kstar, s0 = 1, 0
        for k in range(2, KMAX + 1):
            hit = first_visit[k].get(R0 & ((1 << k) - 1))
            if hit is None:
                break
            kstar, s0 = k, hit
        if kstar == KMAX:
            stats["deep"] = stats.get("deep", 0) + 1
        else:
            if (kstar + 1) in doubling:
                fails.append(("U2-doubling", seed, kstar))
            if (kstar == 2) != ((R0 % 8) in (3, 5)):
                fails.append(("U2-rain", seed, kstar))
        stats[kstar] = stats.get(kstar, 0) + 1
        R = R0
        for t in range(1, STEPS + 1):
            emits = bool(R & 2)
            Rn = T(R)
            if emits != bool(spine_orbit[t - 1 + s0] & 2):
                fails.append(("U1-timing", seed, t))
                break
            if emits:
                ws = width(Rn)
                wsingle = width(spine_orbit[t + s0])
                expect = wsingle if (wsingle is not None and wsingle < kstar - 1) else kstar - 1
                if ws is None or ws >= 62:
                    fails.append(("U1-range", seed, t))
                    break
                if ws != expect:
                    fails.append(("U1-width", seed, t, ws, wsingle, kstar))
                    break
            R = Rn
        if len(fails) > 20:
            break

print("seeds by depth k*:", dict(sorted((k, v) for k, v in stats.items() if k != "deep")), "| deep:", stats.get("deep", 0))
print("cycle lengths p_k:", [p[k] for k in sorted(p)])
print("doubling levels <= %d:" % KMAX, sorted(doubling))
print("failures:", len(fails), fails[:5])
print("ALL CHECKS PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
