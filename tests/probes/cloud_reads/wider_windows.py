# Decisive test of the four-condition conjecture on wider windows: M = 20..26, all d-multisets of size <= 4 (entries <= n-1),
# all legal odd pairs; exhaustive truth over split, within-run orders and roots versus the criterion. Time-capped.
import itertools, sys, time, math
sys.path.insert(0, '.')
from b77_check import exists_cycle, criterion
t0 = time.time(); out = []
for M in (20, 22, 24, 26):
    n = M // 2; cases = mism = 0
    for N in range(1, 5):
        for d in itertools.combinations_with_replacement(range(1, n), N):
            K = sum(d)
            for p in range(1, 2*K, 2):
                q = 2*K - p
                if q < p or q > M - 3: continue
                conj = criterion(M, p, q, d) and not (p == q == M - 3) and N + 2 <= n
                truth = exists_cycle(M, p, q, list(d)); cases += 1
                if conj != truth: mism += 1; print("MISMATCH", M, p, q, d, truth, conj, flush=True)
            if time.time() - t0 > 1500: break
        if time.time() - t0 > 1500: break
    out.append((M, cases, mism)); print("window", M, "questions", cases, "mismatches", mism, f"({time.time()-t0:.0f}s)", flush=True)
    if time.time() - t0 > 1500: print("time cap reached"); break
print(out)
