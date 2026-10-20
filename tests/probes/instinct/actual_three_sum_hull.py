#!/usr/bin/env python3
"""MI535: one fixed actual-three-sum quota-hull diagnostic (CPU, stdlib).

Forecast: no integer holes in the eight fixed fixtures. A hole refutes
automatic transfer of the two-target property; no hole proves no theorem.
Controls: simplex triangle; genuine C4 x third-edge hole; independent
edge masks, recursive matching support, reflection and colour permutation.
Stop first hole/disagreement or 20 CPU seconds. No domain expansion/retry.
"""
from functools import lru_cache
from itertools import combinations, product
from math import gcd
import json
import time

START = time.process_time()


def cap():
    if time.process_time()-START > 20:
        raise TimeoutError('20 CPU seconds')


def graph(pool, targets):
    return [(i, j, targets.index(x+y)) for i, x in enumerate(pool)
            for j, y in enumerate(pool) if i < j and x+y in targets]


def recursive(n, edges):
    adj = [[] for _ in range(n)]
    for i, (u, v, c) in enumerate(edges):
        adj[u].append((v, c, i)); adj[v].append((u, c, i))
    @lru_cache(None)
    def go(mask):
        cap()
        if not mask:
            return {(0, 0, 0): ()}
        u = (mask & -mask).bit_length()-1
        rest = mask ^ (1 << u)
        out = dict(go(rest))
        for v, c, i in adj[u]:
            if rest >> v & 1:
                for q, witness in go(rest ^ (1 << v)).items():
                    p = list(q); p[c] += 1
                    out.setdefault(tuple(p), witness+(i,))
        return out
    return go((1 << n)-1)


def edge_masks(edges):
    out = set()
    for bits in range(1 << len(edges)):
        if bits % 1024 == 0: cap()
        used = 0; q = [0, 0, 0]
        for i, (u, v, c) in enumerate(edges):
            if bits >> i & 1:
                add = (1 << u) | (1 << v)
                if used & add: break
                used |= add; q[c] += 1
        else:
            out.add(tuple(q))
    return out


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def bounds(points):
    """All facet normals occur among these exact support-triple normals."""
    assert (0, 0, 0) in points
    assert all(tuple(int(i == c) for i in range(3)) in points for c in range(3))
    normals = set()
    for a, b, c in combinations(sorted(points), 3):
        cap()
        u = tuple(b[i]-a[i] for i in range(3))
        v = tuple(c[i]-a[i] for i in range(3))
        w = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        g = gcd(gcd(abs(w[0]), abs(w[1])), abs(w[2]))
        if not g: continue
        sign = 1 if next(x for x in w if x) > 0 else -1
        normals.add(tuple(sign*x//g for x in w))
    return [(w, min(dot(w, q) for q in points), max(dot(w, q) for q in points)) for w in sorted(normals)]


def contains(planes, q):
    return all(lo <= dot(w, q) <= hi for w, lo, hi in planes)


def audit(n, edges):
    real = recursive(n, edges)
    assert set(real) == edge_masks(edges), 'independent support disagreement'
    for q, witness in real.items():
        used = set(); counts = [0, 0, 0]
        for i in witness:
            u, v, c = edges[i]
            assert u not in used and v not in used
            used.update((u, v)); counts[c] += 1
        assert tuple(counts) == q
    return real


def check(pool, targets):
    edges = graph(pool, targets); real = audit(len(pool), edges)
    M = max(pool)
    reflected = recursive(len(pool), graph(sorted(M-x for x in pool), tuple(2*M-u for u in targets)))
    assert set(reflected) == set(real), 'reflection disagreement'
    perm = recursive(len(pool), graph(pool, targets[::-1]))
    assert set(perm) == {q[::-1] for q in real}, 'colour permutation disagreement'
    planes = bounds(real)
    ranges = [range(max(q[i] for q in real)+1) for i in range(3)]
    total = 0
    for q in product(*ranges):
        cap(); total += 1
        if q in real or not contains(planes, q): continue
        midpoint = None
        for a in real:
            b = tuple(2*q[i]-a[i] for i in range(3))
            if b in real:
                midpoint = [dict(quota=a, edges=[edges[i] for i in real[a]]),
                            dict(quota=b, edges=[edges[i] for i in real[b]])]
                break
        return dict(pool=pool, targets=targets, edges=edges, support=sorted(real),
                    hole=q, midpoint=midpoint, bounds=planes, quotas_checked=total)
    return dict(pool=pool, targets=targets, edges=len(edges), support=len(real),
                normal_directions=len(planes), quotas_checked=total, hole=None)


def main():
    cases = []
    try:
        triangle = audit(3, [(0, 1, 0), (0, 2, 1), (1, 2, 2)])
        assert len(triangle) == 4
        assert not contains(bounds(triangle), (1, 1, 0))
        cycle = audit(6, [(0, 1, 0), (1, 2, 1), (2, 3, 0), (3, 0, 1), (4, 5, 2)])
        assert (1, 1, 0) not in cycle and contains(bounds(cycle), (1, 1, 0))
        fixtures = [(7, None, (5, 7, 9)), (7, None, (4, 7, 10)),
                    (8, 4, (7, 8, 9)), (9, None, (6, 9, 12)),
                    (9, 1, (6, 9, 12)), (11, None, (8, 11, 14)),
                    (11, None, (9, 11, 13)), (12, 6, (9, 12, 15))]
        for M, hole, targets in fixtures:
            row = check([x for x in range(M+1) if x != hole], targets); cases.append(row)
            if row['hole'] is not None:
                print(json.dumps(dict(status='HOLE', controls='PASS', cases=cases))); return
        print(json.dumps(dict(status='NO_HOLE_ON_FIXED_FIXTURES', controls='PASS', cases=cases)))
    except TimeoutError as e:
        print(json.dumps(dict(status='UNKNOWN', reason=str(e), completed=cases)))


if __name__ == '__main__':
    main()
