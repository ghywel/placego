import itertools, sys, time
sys.path.insert(0, '.')
from b77_check import exists_cycle, criterion
t0 = time.time(); out = []
for M, Nmax in ((20, 6), (22, 6), (24, 5), (26, 5), (28, 5)):
    n = M // 2; cases = mism = 0; capped = False
    for N in range(5, Nmax + 1):
        for d in itertools.combinations_with_replacement(range(1, n), N):
            K = sum(d)
            if K > 2*n - 4: continue
            for p in range(1, 2*K, 2):
                q = 2*K - p
                if q < p or q > M - 3: continue
                conj = criterion(M, p, q, d) and not (p == q == M - 3) and N + 2 <= n
                truth = exists_cycle(M, p, q, list(d)); cases += 1
                if conj != truth: mism += 1; print("MISMATCH", M, p, q, d, truth, conj, flush=True)
            if time.time() - t0 > 270: capped = True; break
        if capped: break
    print("window", M, "N 5.." + str(Nmax), "questions", cases, "mismatches", mism, "capped" if capped else "complete", f"({time.time()-t0:.0f}s)", flush=True)
    if capped: break
