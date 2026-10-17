# The index form of the odd-partition problem: odd 2i+1 -> index i, so bins with sizes c_j and odd-sums t_j correspond to a
# partition of {0..n-1} into sets with sizes c_j and index-sums s_j = (t_j - c_j)/2. Test the naive "interval" condition:
# each (c_j, s_j) must satisfy lo(c) = c(c-1)/2 <= s <= hi(c) = c(n-1) - c(c-1)/2, and sum s_j = n(n-1)/2. Is it sufficient?
import itertools, sys, time, collections
def lo(c): return c*(c-1)//2
def hi(c, n): return c*(n-1) - c*(c-1)//2
def exists(n, sizes, sums):
    k = len(sizes); rem_c = list(sizes); rem_s = list(sums)
    def rec(i):
        if i == n: return all(x == 0 for x in rem_c)
        tried = set()
        for b in range(k):
            key = (rem_c[b], rem_s[b])
            if rem_c[b] == 0 or rem_s[b] < i or key in tried: continue
            tried.add(key)
            rem_c[b] -= 1; rem_s[b] -= i
            # prune: remaining sum must lie within the interval achievable from remaining indices i+1..n-1 with rem_c[b] items
            c = rem_c[b]; r = rem_s[b]
            if (c == 0 and r == 0) or (c > 0 and c*(i+1) + c*(c-1)//2 <= r <= c*(n-1) - c*(c-1)//2):
                if rec(i + 1): return True
            rem_c[b] += 1; rem_s[b] += i
        return False
    return rec(0)
t0 = time.time(); res = {}
for n in range(4, 11):
    T = n*(n-1)//2
    for k in (2, 3, 4):
        if k > n: continue
        cnt = fail = 0; fails = []
        for sizes in itertools.combinations_with_replacement(range(1, n), k):
            if sum(sizes) != n: continue
            ranges = [range(lo(c), hi(c, n) + 1) for c in sizes]
            for sums in itertools.product(*ranges):
                if sum(sums) != T: continue
                # canonical: for equal sizes require nondecreasing sums
                ok = all(not (sizes[j] == sizes[j+1] and sums[j] > sums[j+1]) for j in range(k-1))
                if not ok: continue
                cnt += 1
                if not exists(n, list(sizes), list(sums)): fail += 1; fails.append((sizes, sums))
        res[(n, k)] = (cnt, fail); print(f"n={n} k={k}: interval-feasible (size,sum) vectors {cnt}, no partition {fail}", fails[:3], flush=True)
print(f"({time.time()-t0:.0f}s)")
