# Refined condition SS: for EVERY sub-collection J of bins, lo(C_J) <= S_J <= hi(C_J) where C_J, S_J are its total size and sum.
# (a) exhaustive sufficiency test on small n, k; (b) on B57's 2,000 mixed E28 targets, does some size vector satisfy SS?
import itertools, sys, time, json
sys.path.insert(0, '.')
from sizes_sums import exists, lo, hi
def SS(n, sizes, sums):
    k = len(sizes)
    for mask in range(1, 1 << k):
        C = sum(sizes[j] for j in range(k) if mask >> j & 1); S = sum(sums[j] for j in range(k) if mask >> j & 1)
        if not (lo(C) <= S <= hi(C, n)): return False
    return True
t0 = time.time()
for n in range(4, 11):
    T = n*(n-1)//2
    for k in (2, 3, 4, 5):
        if k > n: continue
        cnt = fail = 0; fails = []
        for sizes in itertools.combinations_with_replacement(range(1, n), k):
            if sum(sizes) != n: continue
            for sums in itertools.product(*[range(lo(c), hi(c, n) + 1) for c in sizes]):
                if sum(sums) != T or not all(not (sizes[j] == sizes[j+1] and sums[j] > sums[j+1]) for j in range(k-1)): continue
                if not SS(n, sizes, sums): continue
                cnt += 1
                if not exists(n, list(sizes), list(sums)): fail += 1; fails.append((sizes, sums))
        print(f"n={n} k={k}: SS-feasible vectors {cnt}, no partition {fail}", fails[:4], flush=True)
print(f"small cases ({time.time()-t0:.0f}s)")
# (b) E28 sample: index form n=28, s_j = (t_j - c_j)/2, c_j = t_j mod 2, c_j >= 2
rows = [r['targets'] for r in json.load(open(sys.argv[1]))['groups'][1]['rows']]
def size_vectors(t):
    out = []
    def rec(j, rem, acc):
        if j == 8:
            if rem == 0: out.append(tuple(acc))
            return
        for c in range(2 + (t[j] % 2 == 1 and 1 or 0), rem - 2*(7-j) + 1, 2):
            if c % 2 != t[j] % 2: continue
            rec(j+1, rem - c, acc + [c])
    rec(0, 28, []); return out
ok = 0; bad = []; nvec = 0; t1 = time.time()
for t in rows:
    found = False
    for c in size_vectors(t):
        s = [(t[j] - c[j])//2 for j in range(8)]
        if any(x < 0 for x in s): continue
        nvec += 1
        if SS(28, c, s): found = True; break
    if found: ok += 1
    else: bad.append(t)
print(f"E28 sample: targets with an SS-feasible size vector {ok}/{len(rows)}; none: {bad[:3]}; ({time.time()-t1:.0f}s)")
