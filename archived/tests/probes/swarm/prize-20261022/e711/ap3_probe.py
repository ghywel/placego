# Probe: 3-multiple ("3-AP line") Hall violators. Lines (x,z) with A-offset x, C-offset z (same parity), B-offset
# (x+z)/2, modulus K+(z-x)/2. Points = A/B/C offsets used. Need a CRT-consistent set of lines with distinct moduli
# and more lines than points. Greedy random search per K; verify any hit by a CRT start and the Hall witness.
import math, random, time, sys
from hall_witness import witness
random.seed(711)
def crt_all(cons):
    r, M = 0, 1
    for a, k in cons:
        g = math.gcd(M, k)
        if (a - r) % g: return None
        t = ((a - r) // g * pow(M // g, -1, k // g)) % (k // g)
        r, M = r + M * t, M // g * k
        r %= M
    return r
G = [0, 1, 4, 10, 12, 17]
X = [2 * g for g in G]
cand = [(x, z) for x in X for z in X]
t0 = time.time(); best = None
for K in range(40, 400):
    for trial in range(30):
        random.shuffle(cand)
        chosen = []; used_d = set()
        for (x, z) in cand:
            d = (z - x) // 2
            if d in used_d: continue
            k = K + d
            ok = all(math.gcd(k, K + (z2 - x2) // 2) % 1 == 0 and
                     (x - x2) % math.gcd(k, K + (z2 - x2) // 2) == 0 for (x2, z2) in chosen)
            if ok: chosen.append((x, z)); used_d.add(d)
        pts = len({x for x, z in chosen}) + len({(x + z) // 2 for x, z in chosen}) + len({z for x, z in chosen})
        if len(chosen) > pts:
            # geometry: offsets a = K0 + x, need a - k <= 0, a + 3k > W
            K0 = min(K + (z - x) // 2 - x for x, z in chosen)   # a - k = K0 + x - K - d <= 0
            if K0 < 1: continue
            W = min(K0 + x + 3 * (K + (z - x) // 2) for x, z in chosen) - 1
            n = max(K + (z - x) // 2 for x, z in chosen)
            if any(K0 + x + 2 * (K + (z - x) // 2) > W for x, z in chosen): continue
            if best is None or (W + 2) - (3 * n - 17) > best[0]:
                m = crt_all([((-(K0 + x)) % (K + (z - x) // 2), K + (z - x) // 2) for x, z in chosen])
                best = ((W + 2) - (3 * n - 17), K, n, W + 2, len(chosen), pts, m)
    if time.time() - t0 > 240: print("time stop at K", K); break
print("best (excess over 3n-17, K, n, bound, lines, points, m):", best[:6] if best else None)
if best and best[6] is not None:
    _, K, n, bound, _, _, m = best
    w = witness(n, m, bound - 1)
    print("Hall witness at window bound-2:", "FOUND |S|=%d |N(S)|=%d" % (len(w[0]), len(w[1])) if w else "NONE (claim fails)")
