# Control 2: independent brute force (fresh Kuhn matching per m, no sliding window) vs the sweep's per-m output.
import subprocess, sys, time
def f_brute(n, m):
    H = n + 1
    while True:
        xs = list(range(m + 1, m + H))
        match = {}  # right x -> k
        def aug(k, seen):
            for x in xs:
                if x % k == 0 and x not in seen:
                    seen.add(x)
                    if x not in match or aug(match[x], seen):
                        match[x] = k; return True
            return False
        ok = all(aug(k, set()) for k in range(n, 0, -1))
        if ok: return H
        H += 1
t0 = time.time(); bad = 0; tot = 0
for n in range(1, 13):
    M = 3000
    out = subprocess.run(["./e711_sweep", str(n), "0", str(M), "60", "1"], capture_output=True, text=True).stdout
    vals = {}
    for line in out.splitlines():
        if line.startswith("m "):
            p = line.split(); vals[int(p[1])] = int(p[3])
    for m in range(0, M, 7 if n > 8 else 1):
        tot += 1
        if f_brute(n, m) != vals[m]: bad += 1; print("MISMATCH", n, m, f_brute(n, m), vals[m])
    if time.time() - t0 > 400: break
print("checked", tot, "pairs (n<=12, m<3000), mismatches", bad, "time %.0fs" % (time.time() - t0))
