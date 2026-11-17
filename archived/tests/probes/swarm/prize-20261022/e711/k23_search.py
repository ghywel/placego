# Explicit K_{2,3} construction (PROOF-SKETCH in the report): hubs at offsets K-delta, K; leaves at 2K, 2K+a, 2K+b.
# Moduli K+{0,a,b} (hub K) and K+delta+{0,a,b} (hub K-delta): six distinct moduli, each with exactly its two
# designated multiples in the window [1, 3K-1], on five points -> Hall fails -> f(n,m) >= 3K+1 for n >= K+delta+b.
# CRT: m = -K mod lcm(K+{0,a,b}), m = -(K-delta) mod lcm(K+delta+{0,a,b}); consistent iff every cross gcd | delta.
import math, subprocess, sys, time
def crt(r1, m1, r2, m2):
    g = math.gcd(m1, m2)
    if (r2 - r1) % g: return None
    l = m1 // g * m2
    t = ((r2 - r1) // g * pow(m1 // g, -1, m2 // g)) % (m2 // g)
    return (r1 + m1 * t) % l, l
def configs(maxsum):
    for s in range(3, maxsum + 1):
        for d in range(1, s):
            b = s - d
            for a in range(1, b):
                if d not in (a, b, b - a): yield d, a, b
CF = list(configs(40))
def best_K(n):
    for K in range(n, 4, -1):
        for d, a, b in CF:
            if K + d + b > n or K - d < 1 or b > K - 1: continue
            M2 = [K, K + a, K + b]; M1 = [K + d, K + d + a, K + d + b]
            if all(d % math.gcd(x, y) == 0 for x in M1 for y in M2):
                l1 = math.lcm(*M1); l2 = math.lcm(*M2)
                r = crt((-(K - d)) % l1, l1, (-K) % l2, l2)
                if r is None: continue
                return K, (d, a, b), r[0]
    return None
if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    t0 = time.time(); worst = {}; viol = []
    for n in range(13, N + 1):
        res = best_K(n)
        K, cfg, m = res
        bound = 3 * K + 1
        formula = 3 * n - 17 if n % 3 else 3 * n - 20
        if bound < formula: viol.append((n, bound, formula))
        worst[n] = (bound, cfg, m)
    print("n range 13..%d: K23 bound below the formula 3n-17 (3!|n) / 3n-20 (3|n) at:" % N, viol[:10], "count", len(viol))
    print("bound - formula distribution:", sorted(set(worst[n][0] - (3*n-17 if n % 3 else 3*n-20) for n in worst)))
    for n in [17, 19, 20, 22, 23, 24, 25, 30, 50, 100]:
        if n <= N: print("n", n, "bound", worst[n][0], "cfg(delta,a,b)", worst[n][1], "m", worst[n][2])
    # independent verification of the constructed m with the C sweep (exact f at that m), n <= 300
    bad = 0; checked = 0
    for n in list(range(13, min(N, 300) + 1)):
        bound, cfg, m = worst[n]
        if m >= 2**62: continue
        out = subprocess.run(["./e711_sweep", str(n), str(m), "1"], capture_output=True, text=True).stdout.split()
        f = int(out[out.index("best") + 1]); checked += 1
        if f < bound: bad += 1; print("FAIL", n, m, f, bound)
    print("verified f(n,m) >= bound at the constructed m for", checked, "values of n; failures", bad, "time %.0fs" % (time.time() - t0))
