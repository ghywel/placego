"""Independent Python cross-check of Claim A case 1 (and spot check of failures) using a different method:
unordered partitions into triples -> set of sorted sum-tuples; plus memoized backtracking for single instances."""
import itertools, sys, time
from functools import lru_cache

def L(r): return r*(r-1)//2

def key(us, cs):
    k = len(us); mu = None
    for J in range(1, (1 << k) - 1):
        r = sum(cs[i] for i in range(k) if J >> i & 1)
        u = sum(us[i] for i in range(k) if J >> i & 1)
        val = -1 if u < L(r) else (u - L(r)) // r
        mu = val if mu is None else min(mu, val)
    return mu

def triple_partitions(elems):
    if not elems:
        yield []
        return
    a = elems[0]; rest = elems[1:]
    for i in range(len(rest)):
        for j in range(i+1, len(rest)):
            b, c = rest[i], rest[j]
            rem = rest[:i] + rest[i+1:j] + rest[j+1:]
            for p in triple_partitions(rem):
                yield [a+b+c] + p

def feasible_bt(pool, cs, us):
    pool = tuple(pool); n = len(pool)
    @lru_cache(None)
    def go(i, mask):
        if i == len(cs): return mask == 0
        idxs = [j for j in range(n) if mask >> j & 1]
        for comb in itertools.combinations(idxs, cs[i]):
            if sum(pool[j] for j in comb) == us[i]:
                m2 = mask
                for j in comb: m2 &= ~(1 << j)
                if go(i+1, m2): return True
        return False
    return go(0, (1 << n) - 1)

def caseA_equal3(M, h, k=4):
    cs = (3,)*k
    nadm = 0; fails = []
    for H in itertools.combinations(range(M+1), h):
        S = [x for x in range(M+1) if x not in H]
        tot = sum(S)
        feas = set(tuple(sorted(p)) for p in triple_partitions(S))
        lo = L(3) + 3*h; hi = tot - (L(3*k-3) + h*(3*k-3))
        for us in itertools.product(range(lo, hi+1), repeat=k-1):
            last = tot - sum(us)
            v = us + (last,)
            if key(v, cs) >= h:
                nadm += 1
                if tuple(sorted(v)) not in feas:
                    fails.append((H, v))
    return nadm, fails

if __name__ == '__main__':
    t = time.time()
    print('M=14 h=3 (3,3,3,3):', caseA_equal3(14, 3), round(time.time()-t, 1), 's')
    # direct backtracking confirmation of the two claimed failures and their neighbours
    for M, H, v in [(14, (6,7,8), (21,21,21,21)), (15, (0,7,8,9), (24,24,24,24))]:
        S = [x for x in range(M+1) if x not in H]
        print(M, H, v, 'sum ok', sum(S) == sum(v), 'key', key(v, (3,3,3,3)),
              'feasible_bt', feasible_bt(S, (3,3,3,3), v))
