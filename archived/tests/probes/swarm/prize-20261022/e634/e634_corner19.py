#!/usr/bin/env python3
"""N=19 in the Group-1 isosceles shape (alpha+beta, alpha+beta, alpha), tile (a,b,c)=(mk, k^2-m^2, k^2).
Arithmetic: N = s^2/(k^2-m^2) => k^2-m^2 = 19 t^2, s = 19 t; legs s*k, base s*m.
Necessary corner/boundary test (conservative: degenerate one-edge sides are never used to kill):
  apex A (angle alpha): one tile, its b- and c-sides along the two legs (WLOG b on AB, c on AC);
  base corners B, C (angle alpha+beta): one alpha-tile (sides b,c there) and one beta-tile (sides a,c there),
  one tile's side on the leg, the other's on the base.
  Each side minus its two end edges must be a non-negative integer combination of a, b, c.
Prediction: (k,m,t)=(10,9,1) fails (base 171 = 9*19 forces b-edges at both base ends); larger solutions pass."""
import math, time
T0 = time.time()

def in_S(x, a, b, c):
    if x < 0: return False
    for nc in range(x // c + 1):
        r1 = x - nc * c
        for nb in range(r1 // b + 1):
            if (r1 - nb * b) % a == 0:
                return True
            if time.time() - T0 > 500: raise SystemExit("time limit")
    return False

def feasible(a, b, c, L, B):
    alpha_set, beta_set = (b, c), (a, c)
    corner = [(x, y) for x in alpha_set for y in beta_set] + [(y, x) for x in alpha_set for y in beta_set]
    # corner pairs as (edge on leg, edge on base)
    for eBl, eBb in corner:
        if not (L == b == eBl or in_S(L - b - eBl, a, b, c)):
            continue
        for eCl, eCb in corner:
            okC = (L == c == eCl) or in_S(L - c - eCl, a, b, c)
            okBase = (B == eBb == eCb) or in_S(B - eBb - eCb, a, b, c)
            if okC and okBase:
                return (eBl, eBb, eCl, eCb)
    return None

sols = []
for k in range(2, 1200):
    for m in range(1, k):
        if math.gcd(m, k) != 1: continue
        d = k * k - m * m
        if d % 19: continue
        t2 = d // 19
        t = math.isqrt(t2)
        if t * t != t2: continue
        sols.append((k, m, t))
sols.sort(key=lambda x: x[0])
killed, passed = [], []
for k, m, t in sols:
    a, b, c = m * k, k * k - m * m, k * k
    s = 19 * t
    L, B = s * k, s * m
    w = feasible(a, b, c, L, B)
    (passed if w else killed).append(((k, m, t), (a, b, c), (L, L, B), w))
print(f"solutions with k<1200: {len(sols)}; killed by corner/boundary test: {len(killed)}; passed: {len(passed)}")
print("killed:", [x[0] for x in killed][:30])
print("first passed (k,m,t), tile, triangle, witness (B-leg, B-base, C-leg, C-base):")
for x in passed[:8]:
    print("   ", x)
print(f"done {time.time()-T0:.1f}s")
