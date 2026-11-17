#!/usr/bin/env python3
"""MI532: fixed can-fail diagnostic for alternating-path quota hulls.

Prediction before first execution: eight fixed forests have no integer
holes; geometric, weighted-normal, budget and literal supports agree.
Controls: alternating C4 and non-downward lattice segments have (1,1)
holes. Stop at the first failure. No parameter expansion or census.
CPU, standard library, instant. JSON result belongs outside git.
"""
import itertools
import json


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    def chain(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and cross(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out
    return chain(points)[:-1]+chain(points[::-1])[:-1]


def inside(poly, p):
    if len(poly) == 1:
        return p == poly[0]
    if len(poly) == 2:
        a, b = poly
        return cross(a, b, p) == 0 and all(min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))
    return all(cross(a, b, p) >= 0 for a, b in zip(poly, poly[1:]+poly[:1]))


def literal(edges):
    """Enumerate ALL edge subsets; no component formula or hull used."""
    out = set()
    for bits in range(1 << len(edges)):
        used = set()
        r = b = 0
        for i, (x, y, col) in enumerate(edges):
            if bits >> i & 1:
                if x in used or y in used:
                    break
                used.update((x, y))
                r += col == 'R'
                b += col == 'B'
        else:
            out.add((r, b))
    return out


def data(words):
    edges, ab, red, blue, K, start = [], [], [], [], 0, 0
    for word in words:
        assert all(a != b for a, b in zip(word, word[1:]))
        n, k = len(word), len(word)//2
        edges += [(start+i, start+i+1, col) for i, col in enumerate(word)]
        start += n+1
        K += k
        a = b = k
        if n % 2:
            if word[0] == 'R':
                a += 1
                red.append(k+1)
            else:
                b += 1
                blue.append(k+1)
        ab.append((a, b))
    return edges, ab, sorted(red), sorted(blue), K


def affordable(weights, budget):
    return max(j for j in range(len(weights)+1) if sum(weights[:j]) <= budget)


def check(words):
    edges, ab, red, blue, K = data(words)
    real = literal(edges)
    poly = hull(real)
    normals = {(1, 0), (0, 1)} | {(b, a) for a, b in ab if a*b}
    count = 0
    for r in range(sum(a for a, b in ab)+1):
        for s in range(sum(b for a, b in ab)+1):
            geometric = inside(poly, (r, s))
            weighted = all(p*r+q*s <= sum(max(p*a, q*b) for a, b in ab) for p, q in normals)
            budget = r+s <= K+affordable(red, r)+affordable(blue, s)
            actual = (r, s) in real
            assert geometric == weighted == budget == actual, (words, r, s, geometric, weighted, budget, actual)
            count += 1
    return dict(words=words, edges=len(edges), support=len(real), quotas=count, hull=poly)


def main():
    fixtures = [('', 'R', 'B'), ('RBRB',), ('RBRBR',),
                ('RBR', 'RBRBRBR'), ('RBR', 'BRB'),
                ('RBRBR', 'BRBRBRB', 'RB'),
                ('RBRBRBR', 'RBRBRBR'), ('RBRBRBRBR', 'BRB')]
    cycle = literal([(0, 1, 'R'), (1, 2, 'B'), (2, 3, 'R'), (3, 0, 'B')])
    assert inside(hull(cycle), (1, 1)) and (1, 1) not in cycle
    segment_sum = {(a[0]+b[0], a[1]+b[1]) for a, b in
                   itertools.product(((0, 0), (2, 1)), ((0, 0), (1, 2)))}
    assert inside(hull(segment_sum), (1, 1)) and (1, 1) not in segment_sum
    assert (2, 1) not in literal(data(('RBRBR',))[0])
    result = [check(words) for words in fixtures]
    print(json.dumps(dict(status='PASS', cases=result,
                          quotas=sum(x['quotas'] for x in result),
                          controls=['C4 hole', 'segment-sum hole', 'MI522 negative'])))


if __name__ == '__main__':
    main()
