import itertools, sys, time
sys.path.insert(0, '.')
from sizes_sums import exists, lo, hi
from sizes_sums2 import SS
t0 = time.time()
for n in range(13, 17):
    T = n*(n-1)//2
    for k in (3, 4, 5):
        if 3*k > n: continue
        cnt = fail = 0; fails = []
        for sizes in itertools.combinations_with_replacement(range(3, n), k):
            if sum(sizes) != n: continue
            for sums in itertools.product(*[range(lo(c), hi(c, n) + 1) for c in sizes]):
                if sum(sums) != T or not all(not (sizes[j] == sizes[j+1] and sums[j] > sums[j+1]) for j in range(k-1)): continue
                if not SS(n, sizes, sums): continue
                cnt += 1
                if not exists(n, list(sizes), list(sums)): fail += 1; fails.append((sizes, sums))
            if time.time() - t0 > 1500: break
        print(f"sizes>=3 n={n} k={k}: SS-feasible {cnt}, no partition {fail}", fails[:3], f"({time.time()-t0:.0f}s)", flush=True)
        if time.time() - t0 > 1500: print("time cap"); sys.exit()
