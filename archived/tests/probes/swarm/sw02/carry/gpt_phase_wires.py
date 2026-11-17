#!/usr/bin/env python3
"""GC2834: exact half-phase equality graphs on the existing three34tiles.

No wider core. Tests the algebraic reduction on all legal small triples, then
classifies periodic equality graphs by integer translation voltages. Replays
the35-pair exit-height certificate by independent synchronous leaf deletion.
"""
from collections import deque
from fractions import Fraction
import itertools
import json
from math import gcd
import os
from pathlib import Path

OUT = Path(os.environ['CAPPED_OUT'])
PRIOR = Path(os.environ['DYADIC_PRIOR'])


def rot(x, k, p):
    k %= p
    return ((x >> k) | (x << (p - k))) & ((1 << p) - 1)


def scalar_children(c, d, p):
    acc = 0; word = 0
    for t in range(p):
        word |= acc << t
        acc ^= ((c >> t) & 1) | ((d >> t) & 1)
    return [] if acc else [(word, c), (word ^ ((1 << p) - 1), c)]


def literal(u, c, d, p):
    return all(((u >> ((t + 1) % p)) & 1) ==
               (((u >> t) & 1) ^ (((c >> t) & 1) | ((d >> t) & 1))) for t in range(p))


def wires(u, c, d, p):
    mask = (1 << p) - 1; L = p // 2
    hu, hc, hd = [x ^ rot(x, L, p) for x in (u, c, d)]
    A, B, C = hc & (mask ^ d), hd & (mask ^ c), hc & hd
    edges = []
    if C:
        edges.append((1, 2))
        if rot(hu, 1, p) ^ hu: edges.append((0, 1))
    else:
        if A: edges.append((0, 1))
        if B: edges.append((0, 2))
    h = (hu, hc, hd)
    assert all(h[a] and h[b] for a, b in edges)
    return edges


def small_triples():
    result = []
    for p in (2, 4, 6):
        checks = 0; triples = 0
        for c, d in itertools.product(range(1 << p), repeat=2):
            for u, _ in scalar_children(c, d, p):
                edges = wires(u, c, d, p); triples += 1
                for e in itertools.product((0, 1), repeat=3):
                    z = [rot(x, e0 * (p // 2), p) for x, e0 in zip((u, c, d), e)]
                    assert literal(*z, p) == all(e[a] == e[b] for a, b in edges)
                    checks += 1
        result.append({'p': p, 'legal_triples': triples, 'spin_checks': checks})
    return result


def read_graph(p):
    lines = (PRIOR / f'p{p}-closure.tsv').read_text().splitlines()
    pp, n, roots = map(int, lines[0].split()); assert pp == p and n == len(lines) - 1
    rows = [tuple(map(int, x.split())) for x in lines[1:]]
    adj = {(c, d): scalar_children(c, d, p) for c, d, _ in rows}
    assert all(w in adj for v in adj for w in adj[v])
    return rows, adj


def exit_height():
    rows, adj = read_graph(32)
    root_id = rows[0][2]
    remaining = {(c, d) for c, d, j in rows if j != root_id}
    layers = []
    while remaining:
        dead = {v for v in remaining if not any(w in remaining for w in adj[v])}
        assert dead, 'UNEXPECTED_OFF_CYCLE'
        layers.append(len(dead)); remaining -= dead
    assert len(layers) == 35 and sum(layers) == 4992
    return {'p': 32, 'off_cycle_rows': sum(layers), 'height': len(layers), 'leaf_layers': layers}


def classify(profiles, p, name):
    n = len(profiles); half = p // 2
    h = [x ^ rot(x, half, p) for x in profiles]
    adj = {i: [] for i in range(n) if h[i]}
    for i in range(n):
        idx = (i + 1, i, i - 1)
        u, c, d = (profiles[j % n] for j in idx)
        assert literal(u, c, d, p)
        for a, b in wires(u, c, d, p):
            qa, ra = divmod(idx[a], n); qb, rb = divmod(idx[b], n)
            adj[ra].append((rb, qb - qa)); adj[rb].append((ra, qa - qb))
    seen = set(); parts = []; finite = []; infinity = 0
    for root in adj:
        if root in seen: continue
        pot = {root: 0}; todo = [root]; seen.add(root); g = 0
        while todo:
            v = todo.pop()
            for w, k in adj[v]:
                expect = pot[v] + k
                if w in pot: g = gcd(g, abs(expect - pot[w]))
                else: pot[w] = expect; seen.add(w); todo.append(w)
        part = {'quotient_vertices': sorted(pot), 'translation_gcd': g}
        if g:
            infinity += g
        else:
            cells = sorted(v + n * q for v, q in pot.items())
            part['one_finite_lift'] = cells
            changed = set(cells)
            def new(j):
                return rot(profiles[j % n], half, p) if j in changed else profiles[j % n]
            for j in range(min(cells) - 2, max(cells) + 3):
                assert literal(new(j + 1), new(j), new(j - 1), p)
            visible = [j for j in cells if (profiles[j % n] ^ new(j)) & 1]
            assert visible, 'FINITE_PHASE_CHANGE_INVISIBLE_AT_TIME_ZERO'
            part['visible_tick0_cells'] = visible
            finite.append(cells)
        parts.append(part)
    assert infinity <= 2
    result = {'name': name, 'temporal_period': p, 'spatial_period': n,
              'live_profiles': len(adj), 'finite_component_orbits': len(finite),
              'infinite_components': infinity, 'entropy_bits_per_cell': str(Fraction(len(finite), n)),
              'components': parts, 'profiles_leftward': profiles}
    (OUT / (name + '-wires.json')).write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    tests = small_triples(); height = exit_height()
    rows, adj = read_graph(12); cid = rows[0][2]
    comp = {(c, d) for c, d, j in rows if j == cid}
    U, V = (1323, 2868), (2772, 3372)
    routes = {}
    for s in (U, V):
        for child in adj[s]:
            path = [s, child]
            while path[-1] not in (U, V):
                nx = [w for w in adj[path[-1]] if w in comp]; assert len(nx) == 1
                path.append(nx[0])
            routes[s, path[-1]] = path
    cases = {}
    for word in ('0', '11', '011', '101', '110'):
        s = U; path = []
        for bit in word:
            target = s if bit == '0' else V if s == U else U
            route = routes[s, target]; path += route[:-1]; s = target
        assert s == U
        profiles = [v[0] for v in path]
        cases[word] = classify(profiles, 12, 'p12-' + word)
    old = [tuple(int(x, 16) for x in row.split()) for row in Path('tests/probes/phase480_p32.txt').read_text().splitlines() if not row.startswith('#')]
    cases['480'] = classify([v for u, v in old], 32, 'p32-480')
    comparisons = []
    for a, b in itertools.combinations(('011', '101', '110'), 2):
        aa, bb = cases[a]['profiles_leftward'], cases[b]['profiles_leftward']
        bad = [i for i, (x, y) in enumerate(zip(aa, bb)) if y not in (x, rot(x, 6, 12))]
        comparisons.append({'a': a, 'b': b, 'same_halfshift_profile_class': not bad,
                            'outside_indices': bad, 'changed_indices': [i for i in range(34) if aa[i] != bb[i]]})
    summary = {'small_truth_tables': tests, 'independent_exit_height': height,
               'cases': [{k: v for k, v in c.items() if k not in ('components', 'profiles_leftward')} for c in cases.values()],
               'tile_comparisons': comparisons}
    (OUT / 'phase-wire-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary), flush=True)
    print('PHASE_WIRE_CLASSIFICATION_PASS', flush=True)


if __name__ == '__main__': main()
