"""closure_finite_look.py: are the single seed's forward rows the only finite edge codes in its 2-adic orbit closure?

Local, 2026-10-27, L1002, answering GC1935's open obligation. A look before a hand proof, run with predictions written
first. It decides plausibility only; a finite search proves nothing about every code.

Setting (GC808, L1001). T(R) = R XOR (2R OR 4R) on edge codes. C_k is the cycle of 1 modulo 2^k, and p_k = |C_k|. The
closure is Omega = {R : R mod 2^k in C_k for all k}. GC1935's assertion A: the finite odd codes in Omega are exactly
T^tau(1), tau >= 0.

Predictions (written before the run):
  A1  Among all odd R < 2^24, the ones with R mod 2^K in C_K, for K = 44, are exactly T^tau(1) for tau = 0..11 (12 codes,
      degree 2 tau < 24).
  A2  For every other odd R < 2^24, the depth k*(R) < 44, and k*+1 is not a doubling level (Theorem U).
  A3  The largest depth reached by a non-orbit code below 2^24 grows with the degree bound but stays far below K.
Counterfactual: any non-orbit odd R < 2^24 with R mod 2^K in C_K is a candidate counterexample to A; it would then be
checked to greater depth before any conclusion.
Record searched: "orbit closure" (GC808, CPY), "finite.{0,20}closure" 0, "T\\^tau" 0 (GC1935 is the source).

Run: python3 -I tests/probes/wolfram/closure_finite_look.py

Outcome (2026-10-27, M5, 2.1 s):
- A1 held exactly. Of all 8,388,608 odd codes below 2^24, the 12 that lie in C_44 are T^tau(1) for tau = 0..11.
- A2 and A3 were not separately asserted. A1 implies A2.
- Second question: B1 held. Over 131,071 single-seed rows no non-edge black run reaches bit 63 from z <= 40. The
  longest by z = 1..40 are 0, 2, 4, 3, 5, 5, 4, 5, 3, 7, 6, 6, 8, 8, 5, 9, 12, 16, 8, 11, 11, 17, 19, 15, 14, 16, 15,
  14, 14, 14, 15, 17, 16, 16, 15, 17, 15, 19, 16, 15. B2 was a shape judgment, not an assertion. The bound is far below
  linear growth in this window.
- One slip of mine: the first run of the second part never executed, because the first part ended with sys.exit(0).
  The exit was moved to the end before any second-part result was read.
- This supports, and does not prove, assertion A (L1002).
- Third question: C1, C2 and C3 held. T^-1(1) = -1, T^-2(1) is the 001 layer and T^-3(1) the 101 layer; the cap formula
  has no mismatch over u < 2^17. These are hand facts (L1002) with a finite replay.
"""
import sys

K = 44
MASK = (1 << 64) - 1


def T(R):
    return (R ^ ((R << 1) | (R << 2))) & MASK


orbit = [1]
p = {1: 1}
while len(p) < K:
    orbit.append(T(orbit[-1]))
    s = len(orbit) - 1
    for k in range(2, K + 1):
        if k not in p and (orbit[s] & ((1 << k) - 1)) == 1:
            p[k] = s
mk = (1 << K) - 1
CK = {orbit[s] & mk for s in range(p[K])}
print("p_k:", [p[k] for k in range(1, K + 1)])
print("|C_%d| = %d" % (K, len(CK)))

forward = []
R = 1
while R < (1 << 24):
    forward.append(R)
    R = R ^ ((R << 1) | (R << 2))
hits = [R for R in range(1, 1 << 24, 2) if (R & mk) in CK]
print("odd R < 2^24 with R mod 2^%d in C_%d: %d" % (K, K, len(hits)))
print("equal to the forward rows T^tau(1), tau = 0..%d?" % (len(forward) - 1), hits == forward)
extra = sorted(set(hits) - set(forward))
print("non-orbit hits:", extra[:10])


# ---- Second question (appended after A1 held; predictions written before this part ran) ----
# Hand reduction (L1002): A holds iff -1 = T^-1(1) is the only eventually-all-ones point of Omega, iff in the single
# seed's rows a black run that does NOT touch the edge cell (it starts at distance z+1 >= 2 with distance z white)
# has bounded length for each z. Prediction B1: over t < 2^17, for every z <= 40, the longest such run is bounded and
# never reaches bit 63; B2: the bound grows at most linearly in z. Counterfactual: a run from z <= 20 reaching bit 63
# would point toward a second eventually-ones point and against A.
longest = {}
reach63 = []
for t in range(1, 1 << 17):
    R = orbit[t] if t < len(orbit) else None
    if R is None:
        break
    z = 1
    while z < 62:
        if (R >> z) & 1 == 0 and (R >> (z + 1)) & 1 == 1:
            L = 0
            while z + 1 + L < 64 and (R >> (z + 1 + L)) & 1:
                L += 1
            if z + 1 + L >= 64:
                reach63.append((t, z))
            elif z <= 40:
                longest[z] = max(longest.get(z, 0), L)
            z = z + 1 + L
        else:
            z += 1
print("times scanned:", min(len(orbit), 1 << 17) - 1)
print("runs reaching bit 63 from z <= 40:", [r for r in reach63 if r[1] <= 40][:5])
print("longest non-edge black run by start z+1 (z = 1..40):", [longest.get(z, 0) for z in range(1, 41)])

# ---- Third question (appended; predictions written before it ran) ----
# C1: T^-1(1) = -1 (all ones) modulo 2^64. C2: T^-2(1) has bits set exactly at multiples of 3 (the 001 layer), and
# T^-3(1) is 1 then the period-3 word 110 (the 101 layer). C3, the cap formula: for every u < 2^17 the single seed's
# edge black run (the ones from bit 0 up) has length max{L <= 40 : p_L divides u + 1}, capped at 40.
def T_inv(R):
    q = [0, 0]
    out = 0
    for j in range(64):
        b = ((R >> j) & 1) ^ (q[-1] | q[-2])
        q.append(b)
        out |= b << j
    return out


m1 = T_inv(1)
m2 = T_inv(m1)
m3 = T_inv(m2)
c1 = m1 == MASK
c2 = all(((m2 >> j) & 1) == (1 if j % 3 == 0 else 0) for j in range(64))
c3w = all(((m3 >> j) & 1) == (1 if j == 0 else (0 if j % 3 == 0 else 1)) for j in range(64))
bad = 0
for u in range(1 << 17):
    R = orbit[u]
    L = 0
    while L < 40 and (R >> L) & 1:
        L += 1
    pred = max(Lk for Lk in range(1, 41) if (u + 1) % p[Lk] == 0)
    if min(L, 40) != pred:
        bad += 1
print("C1 T^-1(1) = -1:", c1, "| C2 T^-2(1) = 001 layer:", c2, "| T^-3(1) = 1 then 110 repeated:", c3w)
print("C3 cap formula mismatches over u < 2^17:", bad)
a1_ok = hits == forward and not extra
b1_ok = not [r for r in reach63 if r[1] <= 40]
print("A1:", "PASS" if a1_ok else "FAIL", "| B1:", "PASS" if b1_ok else "FAIL",
      "| C1-C3:", "PASS" if (c1 and c2 and c3w and bad == 0) else "FAIL")
# GC1936: A1 and B1 now enter the exit status too (they had only printed)
sys.exit(0 if (a1_ok and b1_ok and c1 and c2 and c3w and bad == 0) else 1)
