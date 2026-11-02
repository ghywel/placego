#!/usr/bin/env python3
"""GC2359: fixed independent audit of L1292, p=2,4,8,16,32,64 only.
Literal temporal integration, exhaustive small-ring controls, Kahn acyclicity.
No p=128, no dynamic enlargement; <=200000 states per graph.
"""
from collections import deque
import hashlib
import json
import os
from pathlib import Path
import time


def literal(u, v, p):
    bits = [0]
    for t in range(p):
        bits.append(bits[-1] ^ (((u >> t) | (v >> t)) & 1))
    if bits[-1]:
        return ()
    w = sum(b << t for t, b in enumerate(bits[:-1]))
    return ((v, w), (v, w ^ ((1 << p)-1)))


def packed(u, v, p):
    mask = (1 << p)-1
    d = u | v
    if d.bit_count() & 1:
        return ()
    y, s = d, 1
    while s < p:
        y ^= (y << s) & mask
        s *= 2
    w = (y << 1) & mask
    return ((v, w), (v, w ^ mask))


def kahn(edges):
    degree = dict.fromkeys(edges, 0)
    for ns in edges.values():
        for n in ns:
            degree[n] += 1
    q = deque(n for n, d in degree.items() if d == 0)
    order = []
    while q:
        n = q.popleft()
        order.append(n)
        for w in edges[n]:
            degree[w] -= 1
            if degree[w] == 0:
                q.append(w)
    return order, len(order) == len(edges)


def period(w, p):
    for k in (1, 2, 4, 8, 16, 32, 64):
        if k > p:
            break
        if all(((w >> t) & 1) == ((w >> (t % k)) & 1) for t in range(p)):
            return k
    raise AssertionError('period')


def run(p, started):
    mask = (1 << p)-1
    a = sum(1 << t for t in range(1, p, 2))
    b = a ^ mask
    roots = ((a, a), (b, b))
    rain = {(a, b), (b, a)}
    first = literal(0, mask, p)
    assert {y for x in first for y in literal(*x, p)} == rain | set(roots)
    # Positive cycle control: the rain subgraph really cycles.
    re = {s: tuple(n for n in literal(*s, p) if n in rain) for s in rain}
    assert not kahn(re)[1]
    edges = dict.fromkeys(roots)
    q = deque(roots)
    into = 0
    while q:
        s = q.popleft()
        ns = literal(*s, p)
        assert ns == packed(*s, p)
        edges[s] = tuple(n for n in ns if n not in rain)
        into += sum(n in rain for n in ns)
        for n in edges[s]:
            if n not in edges:
                edges[n] = None
                q.append(n)
        assert len(edges) <= 200000, 'frozen state cap'
        if len(edges) % 1024 == 0:
            assert time.process_time()-started < 90, 'frozen child CPU guard'
    order, acyclic = kahn(edges)
    assert acyclic and into == 0, (p, acyclic, into)
    height = {}
    for s in reversed(order):
        height[s] = 1 + max((height[n] for n in edges[s]), default=0)
    h = max(height[s] for s in roots)
    payload = ''.join(f'{u},{v},{height[(u,v)]}\n' for u,v in sorted(edges)).encode()
    out = os.environ.get('CAPPED_OUT')
    if out:
        Path(out, f'ranks-{p}.txt').write_bytes(payload)
    # A local certificate inequality, checked against all independently generated edges.
    assert all(height[s] > height[n] for s, ns in edges.items() for n in ns)
    sample = None
    if p <= 16:
        for s, ns in edges.items():
            ps = max(period(s[0],p), period(s[1],p))
            for n in ns:
                pn = max(period(n[0],p), period(n[1],p))
                if ps == p and pn == p:
                    sample = dict(state=s, successor=n, joint_period=p)
                    break
            if sample:
                break
    return dict(p=p, states=len(edges), into_rain=into, acyclic=acyclic,
                max_vertices_in_path=h, max_additional_columns_after_defect=h-1,
                rank_sha256=hashlib.sha256(payload).hexdigest(), rank_bytes=len(payload),
                same_period_successor=sample)


def main():
    start = time.process_time()
    controls = 0
    for p in (2, 4, 8):
        for u in range(1 << p):
            for v in range(1 << p):
                assert literal(u, v, p) == packed(u, v, p)
                controls += 1
    # An odd driver cannot close; an invented self-loop must fail acyclicity.
    assert literal(1, 0, 8) == ()
    assert not kahn({0:(0,)})[1]
    results = [run(p, start) for p in (2, 4, 8, 16, 32, 64)]
    assert [r['states'] for r in results] == [2, 6, 30, 62, 2110, 171774]
    assert [r['max_vertices_in_path'] for r in results] == [1, 2, 4, 5, 15, 104]
    result = dict(controls=controls, results=results, cpu_seconds=time.process_time()-start)
    data = json.dumps(result, indent=2)+'\n'
    print(data)
    if os.environ.get('CAPPED_OUT'):
        Path(os.environ['CAPPED_OUT'], 'review.json').write_text(data)


if __name__ == '__main__':
    main()
