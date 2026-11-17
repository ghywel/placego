"""Claim C: k bins of size 3, S = {0,1} u [h+2, M], M = 3k+h-1 (so |S| = 3k, holes = [2, h+1]).
One bin target t, k-1 bins target T, (k-1)T + t = sum(S). Find least h with an admitted, infeasible instance."""
import sys, time
from functools import lru_cache

def L(r): return r*(r-1)//2

def mu_of(k, t, T):
    # bins: index 0 has target t, others T; all size 3. Proper nonempty J: (a, j) with a in {0,1}, j T-bins.
    mu = None
    for a in (0, 1):
        for j in range(0, k):
            m = a + j
            if m == 0 or m == k: continue
            if j > k - 1: continue
            r = 3*m; u = a*t + j*T
            val = -1 if u < L(r) else (u - L(r)) // r
            mu = val if mu is None else min(mu, val)
    return mu

def feasible(S, k, t, T):
    S = tuple(sorted(S)); n = len(S)
    triples_by_sum = {}
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                triples_by_sum.setdefault(S[a]+S[b]+S[c], []).append((1<<a)|(1<<b)|(1<<c))
    tT = triples_by_sum.get(T, []); tt = triples_by_sum.get(t, [])
    # T-triples indexed by lowest element, for canonical covering of identical bins
    byLow = {}
    for m in tT:
        low = (m & -m).bit_length() - 1
        byLow.setdefault(low, []).append(m)
    @lru_cache(None)
    def coverT(mask):
        if mask == 0: return True
        low = (mask & -mask).bit_length() - 1
        for m in byLow.get(low, []):
            if m & mask == m and coverT(mask & ~m): return True
        return False
    full = (1 << n) - 1
    for m in tt:
        if coverT(full & ~m): return True
    return False

def run(k, hmax=14):
    first = None
    for h in range(0, hmax+1):
        M = 3*k + h - 1
        S = [0, 1] + list(range(h+2, M+1)); assert len(S) == 3*k
        tot = sum(S); found = []; nadm = 0
        for t in range(0, tot+1):
            if (tot - t) % (k-1): continue
            T = (tot - t) // (k-1)
            if mu_of(k, t, T) >= h:
                nadm += 1
                if not feasible(S, k, t, T): found.append((t, T))
        print(f'k={k} h={h}: admitted={nadm} infeasible-admitted={found}', flush=True)
        if found and first is None:
            first = h
            break
    return first

if __name__ == '__main__':
    for k in (5, 6, 7):
        t0 = time.time(); f = run(k)
        print(f'==> k={k}: least h = {f}  ({time.time()-t0:.1f}s)', flush=True)
