#!/usr/bin/env python3
"""GC2011: complete reachable right-diagonal graphs at P=2,4,8,16.

Frozen specification, predictions, controls and caps:
reports/rule30-bounded-period-graph.md. Standard library only; no Local imports.
Each bit of a packed integer is one time tick, least-significant tick first.
"""
import collections
import hashlib
import itertools
import json
import os
from pathlib import Path

RULE = (0, 1, 1, 1, 1, 0, 0, 0)  # index 4*left+2*centre+right
STATE_CAP = 50_000


def least(word, p):
    while p > 1:
        h = p // 2
        if word & ((1 << h) - 1) != word >> h:
            break
        word &= (1 << h) - 1
        p = h
    return p


def child(a, b, p, bit):
    g = a | b
    if g.bit_count() % 2:
        return None
    c = 0
    for t in range(p):
        c |= bit << t
        bit ^= (g >> t) & 1
    assert bit == (c & 1)
    return c


def scalar_children(a, b, p):
    aa = [(a >> t) & 1 for t in range(p)]
    bb = [(b >> t) & 1 for t in range(p)]
    result = []
    for start in (0, 1):
        now = start
        trace = []
        for t in range(p):
            trace.append(now)
            now = RULE[4 * now + 2 * bb[t] + aa[t]]
        if now == start:
            result.append(sum(x << t for t, x in enumerate(trace)))
    return result


def components(edges):
    n = len(edges)
    reverse = [[] for _ in edges]
    for i, es in enumerate(edges):
        for j in es:
            reverse[j].append(i)
    seen, order = set(), []
    for start in range(n):
        if start in seen:
            continue
        stack = [(start, False)]
        while stack:
            i, done = stack.pop()
            if done:
                order.append(i)
            elif i not in seen:
                seen.add(i)
                stack.append((i, True))
                stack.extend((j, False) for j in edges[i] if j not in seen)
    seen, groups = set(), []
    for start in reversed(order):
        if start in seen:
            continue
        group, stack = [], [start]
        seen.add(start)
        while stack:
            i = stack.pop()
            group.append(i)
            for j in reverse[i]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        groups.append(sorted(group))
    return groups


def longest_path(vertices, edges):
    vertices = set(vertices)
    indeg = {i: 0 for i in vertices}
    for i in vertices:
        for j in edges[i]:
            if j in vertices:
                indeg[j] += 1
    queue = collections.deque(i for i in vertices if indeg[i] == 0)
    length = {i: 1 for i in vertices}
    processed = 0
    while queue:
        i = queue.popleft()
        processed += 1
        for j in edges[i]:
            if j not in vertices:
                continue
            length[j] = max(length[j], length[i] + 1)
            indeg[j] -= 1
            if indeg[j] == 0:
                queue.append(j)
    return max(length.values(), default=0) if processed == len(vertices) else None


def build(p):
    root = (0, (1 << p) - 1)
    nodes, lookup, parents, edges = [root], {root: 0}, [None], []
    exits, drops = [], []
    for i, (a, b) in enumerate(nodes):
        es = []
        for bit in (0, 1):
            c = child(a, b, p, bit)
            if c is None:
                exits.append([i, bit])
                continue
            key = (b, c)
            if key not in lookup:
                if len(nodes) == STATE_CAP:
                    return {"period_cap": p, "complete": False, "state_limit": STATE_CAP}
                lookup[key] = len(nodes)
                nodes.append(key)
                parents.append([i, bit])
            j = lookup[key]
            es.append(j)
            if least(c, p) < least(b, p):
                drops.append([i, bit, j])
        edges.append(es)
    # Independent local verification, parent accessibility, and closure.
    for i, (a, b) in enumerate(nodes):
        expected = scalar_children(a, b, p)
        assert [nodes[j] for j in edges[i]] == [(b, c) for c in expected]
        if i:
            parent, bit = parents[i]
            assert parent < i
            pa, pb = nodes[parent]
            assert a == pb and (b & 1) == bit
            assert b in scalar_children(pa, pb, p)
    groups = components(edges)
    cycles = [g for g in groups if len(g) > 1 or g[0] in edges[g[0]]]
    cycle_data = [{"nodes": g, "periods": sorted({least(nodes[i][1], p) for i in g})}
                  for g in cycles]
    assert any(g["periods"] == [2] for g in cycle_data), "alternating countercontrol missing"
    summary = {"period_cap": p, "complete": True, "states": len(nodes),
               "edges": sum(map(len, edges)), "exit_choices": len(exits),
               "cycle_components": cycle_data, "period_drops": drops,
               "max_consecutive_period_cap_diagonals": longest_path(
                   (i for i, (_, b) in enumerate(nodes) if least(b, p) == p), edges),
               "max_diagonals_above_period_two": longest_path(
                   (i for i, (_, b) in enumerate(nodes) if least(b, p) > 2), edges)}
    cert = {"period_cap": p, "nodes": nodes, "parents": parents, "edges": edges,
            "exits": exits, "summary": summary}
    return cert


def integrate_lists(a, b, bit):
    p = max(len(a), len(b))
    out = []
    for t in range(2 * p):
        out.append(bit)
        bit = RULE[4 * bit + 2 * b[t % len(b)] + a[t % len(a)]]
    period = 2 * p
    while period > 1 and out[:period // 2] == out[period // 2:period]:
        period //= 2
    return out[:period]


def controls():
    universal = collections.Counter()
    for phase in (0, 1):
        for bits in itertools.product((0, 1), repeat=7):
            a = b = [phase, 1 - phase]
            ps = []
            for bit in bits:
                a, b = b, integrate_lists(a, b, bit)
                ps.append(len(b))
            assert ps[:6] == [4, 8, 8, 16, 32, 32]
            assert ps[6] in (32, 64)
            universal[ps[6]] += 1
    assert dict(universal) == {32: 128, 64: 128}
    count = 0
    tmax, dmax = 64, 8
    for seed in range(256):
        bits = [1] + [(seed >> d) & 1 for d in range(dmax)]
        ds, a, b = [[1]], [0], [1]
        for bit in bits[1:]:
            a, b = b, integrate_lists(a, b, bit)
            ds.append(b)
        assert max(map(len, ds)) <= 32
        off = tmax + dmax + 2
        row = [0] * (2 * off + 1)
        for d, bit in enumerate(bits):
            row[off - d] = bit
        for t in range(tmax + 1):
            for d, seq in enumerate(ds):
                assert row[off + t - d] == seq[t % len(seq)]
                count += 1
            row = [0] + [RULE[4 * row[i - 1] + 2 * row[i] + row[i + 1]]
                         for i in range(1, len(row) - 1)] + [0]
    return {"universal_start_cases": 256, "next_period_counts": dict(universal),
            "literal_spatial_cell_comparisons": count}


def main():
    out = Path(os.environ['CAPPED_OUT'])
    result = {"controls": controls(), "graphs": []}
    for p in (2, 4, 8, 16):
        cert = build(p)
        data = json.dumps(cert, sort_keys=True, separators=(',', ':')).encode()
        name = f'graph-p{p}.json'
        (out / name).write_bytes(data)
        summary = cert.get('summary', cert)
        result['graphs'].append(summary | {"certificate": name, "sha256": hashlib.sha256(data).hexdigest()})
        print(json.dumps(result['graphs'][-1], sort_keys=True), flush=True)
        if not cert.get('summary', cert)['complete']:
            break
    (out / 'result.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result['controls'], sort_keys=True))


if __name__ == '__main__':
    main()
