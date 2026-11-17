import itertools, sys, time, json
sys.path.insert(0, '.')
from sizes_sums import exists, lo, hi
from sizes_sums2 import SS, size_vectors
t0 = time.time()
for minsize in (2, 3):
    for n in range(2*minsize, 13):
        T = n*(n-1)//2
        for k in (2, 3, 4, 5):
            if k * minsize > n: continue
            cnt = fail = 0; fails = []
            for sizes in itertools.combinations_with_replacement(range(minsize, n), k):
                if sum(sizes) != n: continue
                for sums in itertools.product(*[range(lo(c), hi(c, n) + 1) for c in sizes]):
                    if sum(sums) != T or not all(not (sizes[j] == sizes[j+1] and sums[j] > sums[j+1]) for j in range(k-1)): continue
                    if not SS(n, sizes, sums): continue
                    cnt += 1
                    if not exists(n, list(sizes), list(sums)): fail += 1; fails.append((sizes, sums))
            if cnt: print(f"minsize>={minsize} n={n} k={k}: SS-feasible {cnt}, no partition {fail}", fails[:3], flush=True)
            if time.time() - t0 > 240: break
        if time.time() - t0 > 240: break
    if time.time() - t0 > 240: print("time cap"); break
print(f"({time.time()-t0:.0f}s)")
rows = [r['targets'] for r in json.load(open(sys.argv[1]))['groups'][1]['rows']]
ok = 0
for t in rows:
    if any(min(c) >= 3 and SS(28, c, [(t[j]-c[j])//2 for j in range(8)]) for c in size_vectors(t)): ok += 1
print("E28 sample: SS-feasible size vector with all sizes >= 3:", ok, "/", len(rows))
