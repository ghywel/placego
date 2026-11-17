#!/usr/bin/env python3
"""MI500: G326 actual-root/recipe audit on OLD counts233/234 only.

Before first run: independent six-cut and interval admissions give602+1057
targets. Every allowed least-slack root (pair first on ties), every legal/
formal prefix/suffix/pivot, both missing-pivot repairs must complete with
an exact scalar oracle OR G326's explicit replacements. No unrestricted
partition fallback. Whole combination/bitmask scalar maps agree; literal
original witnesses and physical root reflection agree.
Counterfactuals: unprotected(8,6,20),M8,q2, and wrong size3 upper tie
on(4,18,11),M8,q3, must expose an unhandled branch.
Stop first unexpected failure;20s/50000 branches,one invocation/no retry,
no larger census. This finite audit does not verify the infinite proof.

OUTCOME, MI501: OLD-DOMAIN PASS on602+1057 targets,1793 allowed roots,
1975 recipe branches:1741 legal direct,219 low direct,2 high direct,
11 legal low replacements,2 old triple replacements.136 whole scalar
maps independently agree. Both wrong controls fail as intended.
0.13245169701986015 seconds,one invocation,no retry. Same-worker audit only.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
import time

L = lambda r: r*(r-1)//2
T = lambda r: r*(r+1)//2
START = time.monotonic()
COUNTS = Counter()


class AuditFailure(Exception):
    def __init__(self, **detail):
        self.detail = detail
        super().__init__(str(detail))


@lru_cache(None)
def subsetmap(pool, size):
    primary, ref, witness = Counter(), Counter(), {}
    for b in combinations(pool, size):
        primary[sum(b)] += 1
        witness.setdefault(sum(b), b)
    for mask in range(1 << len(pool)):
        if mask.bit_count() == size:
            ref[sum(x for i, x in enumerate(pool) if mask >> i & 1)] += 1
    if primary != ref:
        raise AuditFailure(kind='oracle disagreement', pool=pool, size=size)
    return witness


def roots(pool, sizes, sums, priority=True):
    entries = []
    for i, r in enumerate(sizes):
        entries += [(sums[i]-sum(pool[:r]), i, 0),
                    (sum(pool[-r:])-sums[i], i, 1)]
    h = min(a[0] for a in entries)
    out = [(i, side) for slack, i, side in entries if slack == h]
    if priority and any(sizes[i] == 2 for i, _ in out):
        out = [(i, side) for i, side in out if sizes[i] == 2]
    return out


def literal(pool, sizes, sums, bins, context):
    flat = [x for i in range(3) for x in bins[i]]
    if (len(flat) != len(set(flat)) or set(flat) != set(pool) or
        tuple(len(bins[i]) for i in range(3)) != sizes or
        tuple(sum(bins[i]) for i in range(3)) != sums):
        raise AuditFailure(kind='invalid partition', bins=bins, **context)
    return bins


def direct(pool, sizes, sums, i, aa, context):
    if len(aa) != sizes[i] or sum(aa) != sums[i] or len(set(aa)) != len(aa) or not set(aa) <= set(pool):
        raise AuditFailure(kind='bad chosen bin', A=aa, **context)
    rem = tuple(x for x in pool if x not in aa)
    jj = [j for j in range(3) if j != i]
    j = next((j for j in jj if sizes[j] == 2), jj[0])
    k = next(k for k in jj if k != j)
    bb = subsetmap(rem, sizes[j]).get(sums[j])
    if bb is None:
        return None
    bins = {i: tuple(aa), j: bb, k: tuple(x for x in rem if x not in bb)}
    return literal(pool, sizes, sums, bins, context)


def from_pair(pool, sizes, sums, i, aa, j, bb, context):
    k = next(k for k in range(3) if k not in (i, j))
    bins = {i: tuple(aa), j: tuple(bb), k: tuple(x for x in pool if x not in aa and x not in bb)}
    return literal(pool, sizes, sums, bins, context)


def old_triple_repair(pool, sizes, sums, i, q, context):
    a = sizes[i]
    if q != a+4 or sums[i] != L(a)+2:
        return None
    for j in range(3):
        if j != i and sizes[j] == 3 and sums[j] == 3*a+3:
            aa = tuple(range(a-2))+(a-1, a)
            return from_pair(pool, sizes, sums, i, aa, j,
                             (a-2, a+2, a+3), context)
    return None


def repair(pool, sizes, sums, i, q, ell, k, pivot, kind, context):
    a = sizes[i]
    if kind == 'legal':
        aa = tuple(sorted(pool[:ell] + (pool[-k:] if k else ()) + (pivot,)))
    elif kind == 'high':
        u0 = max(pool)-k+1
        aa = tuple(sorted(pool[:ell] + tuple(x for x in pool[-k:] if x != u0) + (q+1, u0-1)))
    else:
        aa = tuple(sorted(tuple(x for x in pool[:ell] if x != ell-1) + (pool[-k:] if k else ()) + (ell, q-1)))
    result = direct(pool, sizes, sums, i, aa, context)
    if result is not None:
        COUNTS[kind+'_direct'] += 1
        return result
    if kind == 'legal':
        result = old_triple_repair(pool, sizes, sums, i, q, context)
        if result is not None:
            COUNTS['old_triple_repair'] += 1
            return result
    if a == 2:
        raise AuditFailure(kind='selected pair branch failed', chosen_A=aa, **context)
    j = next(j for j in range(3) if j != i and sizes[j] == 2)
    c = next(sizes[z] for z in range(3) if z not in (i, j))
    m = max(pool)
    if kind == 'legal' and k == 0:
        q0, p, pair = q-ell, pivot-ell, sums[j]-2*ell
        if pair == 4 and (q0, p) in ((3, 4), (4, 3)):
            tail = (ell+1, ell+2) if q0 == 3 else (ell, ell+2)
            aa = tuple(range(ell-1))+tail
            bb = (ell-1, ell+5)
            COUNTS['legal_low_replacement'] += 1
            return from_pair(pool, sizes, sums, i, aa, j, bb, context)
        cores = {(3, 3, 2): ((0, 2, 3), (4, 8)),
                 (3, 2, 3): ((1, 2, 3), (5, 7)),
                 (4, 4, 3): ((0, 2, 4), (5, 9))}
        if pair == 2*c+2 and (c, q0, p) in cores:
            ac, bc = cores[c, q0, p]
            shift = ell-2
            aa = tuple(range(ell-2))+tuple(x+shift for x in ac)
            bb = tuple(x+shift for x in bc)
            COUNTS['legal_upper_core'] += 1
            return from_pair(pool, sizes, sums, i, aa, j, bb, context)
    if kind == 'high' and c == 3 and k == 1 and q-ell == 4 and sums[j]-2*ell == 6 and m == ell+7:
        aa = tuple(range(ell-1))+(ell, ell+3, ell+7)
        bb = (ell+1, ell+5)
        COUNTS['high_alternate_low'] += 1
        return from_pair(pool, sizes, sums, i, aa, j, bb, context)
    raise AuditFailure(kind='uncovered construction branch', chosen_A=aa, **context)


def audit_root(pool, sizes, sums, root):
    m, i, upper = max(pool), root[0], root[1]
    q = next(x for x in range(m+1) if x not in pool)
    if upper:
        oriented_pool = tuple(sorted(m-x for x in pool))
        oriented_sums = tuple(r*m-s for r, s in zip(sizes, sums))
        q = m-q
    else:
        oriented_pool, oriented_sums = pool, sums
    a, count = sizes[i], 0
    base = {'M': m, 'original_q': next(x for x in range(m+1) if x not in pool),
            'sizes': sizes, 'targets': sums, 'root': root,
            'oriented_q': q, 'oriented_targets': oriented_sums}
    for k in range(a):
        ell = a-1-k
        low, high = oriented_pool[:ell], oriented_pool[-k:] if k else ()
        mid = oriented_pool[ell:len(oriented_pool)-k if k else len(oriented_pool)]
        pivot = oriented_sums[i]-sum(low)-sum(high)
        choices = []
        if pivot in mid:
            choices.append('legal')
        elif pivot == q and min(mid) < q < max(mid):
            u0 = m-k+1
            if k >= 1 and u0-q >= 3:
                choices.append('high')
            if ell >= 1 and q-(ell-1) >= 3:
                choices.append('low')
            if not choices:
                raise AuditFailure(kind='missing pivot without repair', ell=ell, k=k, **base)
        for kind in choices:
            COUNTS['branches'] += 1
            if COUNTS['branches'] > 50000 or time.monotonic()-START > 20:
                raise AuditFailure(kind='CAP', **base)
            context = {**base, 'ell': ell, 'k': k, 'pivot': pivot, 'recipe': kind}
            bins = repair(oriented_pool, sizes, oriented_sums, i, q, ell, k, pivot, kind, context)
            original = {j: tuple(sorted(m-x for x in bins[j])) if upper else bins[j] for j in range(3)}
            literal(pool, sizes, sums, original, context)
            count += 1
    if not count:
        raise AuditFailure(kind='no actual/formal recipe', **base)
    COUNTS['roots'] += 1


def protected(sizes, sums):
    return all(sum(sums[i] for i in range(3) if mask >> i & 1) >=
               T(sum(sizes[i] for i in range(3) if mask >> i & 1))
               for mask in range(1, 7))


def main():
    for q, sums, wrong in ((2, (8, 6, 20), None), (3, (4, 18, 11), (1, 1))):
        pool = tuple(x for x in range(9) if x != q)
        expected = False
        try:
            for root in [wrong] if wrong else roots(pool, (2, 3, 3), sums):
                audit_root(pool, (2, 3, 3), sums, root)
        except AuditFailure as e:
            assert e.detail['kind'] == 'uncovered construction branch', e.detail
            expected = True
        assert expected, ('counterfactual unexpectedly passed', q, sums)
    COUNTS.clear()
    totals = []
    for b, c, expected_count in ((3, 3, 602), (3, 4, 1057)):
        m, sizes = 2+b+c, (2, b, c)
        seen = 0
        for q in range(1, m):
            total = T(m)-q
            primary = {(u, v, total-u-v)
                       for u in range(3, 2*m-q)
                       for v in range(max(T(b), T(b+2)-u),
                                      min(total-u-T(c), total-T(c+2))+1)}
            reference = {(u, v, total-u-v)
                         for u in range(total+1) for v in range(total-u+1)
                         if protected(sizes, (u, v, total-u-v))}
            assert primary == reference, ('admission', m, q)
            pool = tuple(x for x in range(m+1) if x != q)
            for sums in sorted(primary):
                allowed = roots(pool, sizes, sums)
                reflected = tuple(sorted(m-x for x in pool))
                rsums = tuple(r*m-s for r, s in zip(sizes, sums))
                assert set(roots(reflected, sizes, rsums)) == {(i, 1-side) for i, side in allowed}
                for root in allowed:
                    audit_root(pool, sizes, sums, root)
                seen += 1
        assert seen == expected_count, ('old frozen domain count', b, c, seen)
        totals.append(seen)
    print(json.dumps({'result': 'OLD-DOMAIN ROOT/RECIPE AUDIT PASS',
                      'targets': totals, 'counts': dict(COUNTS),
                      'scalar_maps': subsetmap.cache_info().currsize,
                      'seconds': time.monotonic()-START,
                      'scope': 'finite SAME-WORKER interface audit, not carrying verification'}))


if __name__ == '__main__':
    try:
        main()
    except AuditFailure as error:
        print(json.dumps({'result': 'FIRST FAILURE', **error.detail,
                          'counts': dict(COUNTS), 'seconds': time.monotonic()-START}), flush=True)
        raise SystemExit(1)
