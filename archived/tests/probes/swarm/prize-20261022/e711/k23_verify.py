# Verification of the K_{2,3} construction: exact f(n,m) by the C sweep (n <= 64), and an independent Python Hall
# witness at window length 3K-1 (i.e. (m, m+3K) fails) for n <= 400.
import subprocess, time
from k23_search import best_K
from hall_witness import witness
t0 = time.time(); badC = 0; nC = 0; badP = 0; nP = 0; excess = {}
for n in range(13, 401):
    K, cfg, m = best_K(n); bound = 3 * K + 1
    if n <= 64:
        out = subprocess.run(["./e711_sweep", str(n), str(m), "1"], capture_output=True, text=True).stdout.split()
        f = int(out[out.index("best") + 1]); nC += 1
        excess[f - bound] = excess.get(f - bound, 0) + 1
        if f < bound: badC += 1
    w = witness(n, m, 3 * K)   # (m, m+3K) holds offsets 1..3K-1
    nP += 1
    if w is None: badP += 1; print("NO WITNESS", n, K, cfg, m)
    if time.time() - t0 > 400: print("time stop at n", n); break
print("C exact f >= bound: checked", nC, "failures", badC, "; f - bound histogram", excess)
print("Python Hall witness at window 3K-1: checked", nP, "missing", badP, "time %.0fs" % (time.time() - t0))
