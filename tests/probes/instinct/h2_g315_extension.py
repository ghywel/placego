#!/usr/bin/env python3
"""MI498, G326: preregistered ingredient audit, not an H2 census/proof.

Before first invocation: TWO internal holes U6..18, all structured H/K V7..20;
predicted gap tables must equal complete literal missing sets. All written
repairs l2..20,c3..20; high-repair alternate l1..20; G315 repair a2..20,
remaining size2..10. Check full original-pool partitions and target sums.
Independent pair generation; reflection algebra; low-repair priority tie.
Counterfactuals: omit the {3,4}->4 gap, and omit high reflected gaps.
Unexpected: tie priority is actual original lower/upper slack equality3.
Stop at first mismatch;10s,5000 pools,5000 repairs; no edit/retry or larger run.
Raw JSONL outside git. Finite PASS is NOT carrying verification.

OUTCOME, MI498: one invocation PASS,1128 pools,932 literal repairs,
2041 reflection identities,19 priority ties;0.09660283895209432 seconds.
No H2 census or independent review. This outcome was added after execution.
"""
from itertools import combinations
import json
import time

L = lambda r: r*(r-1)//2
T = lambda r: r*(r+1)//2


def spectrum(pool):
    actual = {sum(a) for a in combinations(pool, 2)}
    alternative = {v for v in range(2*max(pool)+1)
                   if any(x < v-x and v-x in pool for x in pool)}
    assert actual == alternative, ('independent pairs', pool)
    return actual


def gaps(pool):
    ss = spectrum(pool)
    return set(range(min(ss), max(ss)+1))-ss


def two_low(holes):
    h = set(holes)
    out = set()
    if 2 in h and max(h) >= 3: out.add(2)
    if h in ({1, 3}, {2, 3}): out.add(3)
    if h in ({1, 4}, {3, 4}): out.add(4)
    return out


def h_low(v, p):
    out = {2, 3} if p == 2 else {4} if p == 3 else set()
    if v == 7 and p in (1, 4): out = out | {6}
    return out


def k_low(v, t):
    return {3, 4} if t == 3 else {4} if t == 4 else set()


def check_partition(m, q, aa, bb, cc, sizes, targets):
    bins = (tuple(aa), tuple(bb), tuple(cc))
    flat = sum((list(x) for x in bins), [])
    assert len(flat) == len(set(flat)), ('overlap', m, q, bins)
    assert set(flat) == set(range(m+1))-{q}, ('coverage', m, q, bins)
    assert tuple(map(len, bins)) == sizes, ('sizes', m, q, bins)
    assert tuple(map(sum, bins)) == targets, ('sums', m, q, bins, targets)


def main():
    start = time.monotonic()
    pools = repairs = reflection = ties = 0
    assert 4 in gaps(tuple(x for x in range(7) if x not in (3, 4)))
    assert 4 not in two_low((3, 4))-{4}
    pool = tuple(x for x in range(7) if x not in (2, 3))
    assert gaps(pool)-two_low((2, 3)), 'low-only counterfactual must fail'
    for u in range(6, 19):
        for holes in combinations(range(1, u), 2):
            pool = tuple(x for x in range(u+1) if x not in holes)
            expected = two_low(holes) | {2*u-x for x in two_low(tuple(u-h for h in holes))}
            assert gaps(pool) == expected, ('two hole', u, holes, sorted(gaps(pool)), sorted(expected))
            pools += 1
    for v in range(7, 21):
        for p in range(v-2):
            pool = tuple(x for x in range(v+1) if x not in (p, p+1, v-1))
            t = v-p-1
            expected = h_low(v, p) | {2*v-x for x in k_low(v, t)}
            assert gaps(pool) == expected, ('H', v, p, sorted(gaps(pool)), sorted(expected))
            reflected = tuple(sorted(v-x for x in pool))
            expected_k = k_low(v, t) | {2*v-x for x in h_low(v, p)}
            assert gaps(reflected) == expected_k, ('K', v, t)
            assert spectrum(reflected) == {2*v-x for x in spectrum(pool)}
            pools += 2
    for ell in range(2, 21):
        for c in range(3, 21):
            m = ell+c+3
            for q0, p, tail in ((3, 4, (ell+1, ell+2)), (4, 3, (ell, ell+2))):
                aa = tuple(range(ell-1))+tail
                bb = (ell-1, ell+5)
                cc = tuple(x for x in range(m+1) if x not in aa+bb and x != ell+q0)
                sa = L(ell+1)+p
                ub = 2*ell+4
                check_partition(m, ell+q0, aa, bb, cc, (ell+1, 2, c), (sa, ub, T(m)-ell-q0-sa-ub))
                repairs += 1
        for c, q0, p, core_m, core_q, ac, bc, dc in (
            (3, 3, 2, 8, 5, (0, 2, 3), (4, 8), (1, 6, 7)),
            (3, 2, 3, 8, 4, (1, 2, 3), (5, 7), (0, 6, 8)),
            (4, 4, 3, 9, 6, (0, 2, 4), (5, 9), (1, 3, 7, 8))):
            shift = ell-2
            aa = tuple(range(ell-2))+tuple(x+shift for x in ac)
            bb = tuple(x+shift for x in bc)
            cc = tuple(x+shift for x in dc)
            check_partition(core_m+shift, core_q+shift, aa, bb, cc,
                            (ell+1, 2, c),
                            (L(ell+1)+p, 2*ell+2*c+2, L(c)+5+ell*c))
            repairs += 1
        m, q = ell+6, ell+3
        pool = tuple(x for x in range(m+1) if x != q)
        selected = L(ell+1)+3
        pair = 2*ell+8
        assert selected-sum(pool[:ell+1]) == sum(pool[-2:])-pair == 3
        ties += 1
    for a in range(2, 21):
        for c in range(2, 11):
            m, q = a+3+c, a+4
            aa = tuple(range(a-2))+(a-1, a)
            bb = (a-2, a+2, a+3)
            cc = tuple(x for x in range(m+1) if x not in aa+bb and x != q)
            check_partition(m, q, aa, bb, cc, (a, 3, c),
                            (L(a)+2, 3*a+3, T(m)-q-L(a)-2-3*a-3))
            repairs += 1
    for ell in range(1, 21):
        m, q = ell+7, ell+4
        aa = tuple(range(ell-1))+(ell, ell+3, ell+7)
        bb = (ell+1, ell+5)
        cc = (ell-1, ell+2, ell+6)
        check_partition(m, q, aa, bb, cc, (ell+2, 2, 3),
                        (L(ell)+2*ell+11, 2*ell+6, 3*ell+7))
        repairs += 1
    for m in range(8, 21):
        for q in range(1, m):
            total = T(m)-q
            for r in range(2, m-1):
                assert r*m-total+T(m-r) == L(r)+q
                reflection += 1
    assert pools <= 5000 and repairs <= 5000 and time.monotonic()-start <= 10, 'CAP'
    print(json.dumps({'result': 'INGREDIENT AUDIT PASS', 'pools': pools,
                      'literal_repairs': repairs, 'reflection_identities': reflection,
                      'priority_ties': ties, 'seconds': time.monotonic()-start,
                      'scope': 'finite ingredients, NOT full H2 proof or independent review'}))


if __name__ == '__main__':
    main()
