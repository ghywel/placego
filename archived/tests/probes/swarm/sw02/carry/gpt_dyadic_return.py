#!/usr/bin/env python3
"""GC2833: same-period return closure of the stored 480-state wave.

Fixed P=32 and node cap200000. No random roots, new period or full core census.
Positive control: P12/U. Unexpected test: independent temporal half-shifts of
the individual profiles, preserving their weights/least periods.
"""
from collections import Counter, deque
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gpt_period12_return import sccs

OUT = Path(os.environ['CAPPED_OUT'])
CAP = 200000


def rot(w, k, p):
    k %= p
    return ((w >> k) | (w << (p - k))) & ((1 << p) - 1)


def children(pair, p):
    c, d = pair
    drive = c | d
    if drive.bit_count() & 1:
        return ()
    mask = (1 << p) - 1
    value = drive
    k = 1
    while k < p:
        value ^= value << k
        k *= 2
    value = (value << 1) & mask
    return ((value, c), (value ^ mask, c))


def valid(child, pair, p):
    u, c = child
    return c == pair[0] and (rot(u, 1, p) ^ u) == (pair[0] | pair[1])


def least(pair, p):
    return next(k for k in range(1, p + 1) if p % k == 0 and
                all(rot(w, k, p) == w for w in pair))


def closure(seeds, p):
    ordered = list(dict.fromkeys(seeds))
    ids = {v: i for i, v in enumerate(ordered)}
    adj = {}
    pos = 0
    while pos < len(ordered):
        v = ordered[pos]
        adj[v] = list(children(v, p))
        for w in adj[v]:
            if w not in ids:
                if len(ordered) == CAP:
                    (OUT / 'cap-stop.json').write_text(json.dumps({'p': p, 'nodes': len(ordered), 'processed': pos}) + '\n')
                    raise RuntimeError('FIXED_NODE_CAP_STOP')
                ids[w] = len(ordered)
                ordered.append(w)
        pos += 1
    comps = sccs(adj)
    compof = {v: j for j, cm in enumerate(comps) for v in cm}
    with (OUT / f'p{p}-closure.tsv').open('w') as f:
        f.write(f'{p} {len(ordered)} {len(seeds)}\n')
        for c, d in ordered:
            f.write(f'{c} {d} {compof[c,d]}\n')
    cyc = [cm for cm in comps if len(cm) > 1 or next(iter(cm)) in adj[next(iter(cm))]]
    root = comps[compof[seeds[0]]]
    internal = sum(w in root for v in root for w in adj[v])
    cyclic = set().union(*cyc) if cyc else set()
    transient = set(adj) - cyclic
    pred = {v: [] for v in transient}
    remaining = {v: sum(w in transient for w in adj[v]) for v in transient}
    for v in transient:
        for w in adj[v]:
            if w in transient: pred[w].append(v)
    queue = deque(v for v in transient if remaining[v] == 0)
    rank = {}
    while queue:
        v = queue.popleft()
        rank[v] = 1 + max((rank.get(w, 0) for w in adj[v]), default=0)
        for w in pred[v]:
            remaining[w] -= 1
            if remaining[w] == 0: queue.append(w)
    assert len(rank) == len(transient)
    exits = [w for v in root for w in adj[v] if w not in root]
    result = {'p': p, 'nodes': len(ordered), 'edges': sum(map(len, adj.values())),
              'root_component': {'nodes': len(root), 'edges': internal,
                                 'branch_vertices': [v for v in sorted(root) if sum(w in root for w in adj[v]) > 1]},
              'cyclic_shapes': sorted((len(cm), sum(w in cm for v in cm for w in adj[v])) for cm in cyc),
              'all_components': len(comps), 'transient_nodes': len(transient),
              'maximum_transient_stretch': max(rank.values(), default=0),
              'maximum_stretch_after_root_exit': max((rank.get(w, 0) for w in exits), default=0),
              'root_exit_edges': len(exits), 'complete': True, 'node_cap': CAP}
    (OUT / f'p{p}-summary.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)
    return adj, root


def phase_gauge(profiles, p, name):
    """A marked spatial background; each column is shifted by 0 or p/2 ticks."""
    n = len(profiles)
    half = p // 2
    mask = (1 << p) - 1
    h = [w ^ rot(w, half, p) for w in profiles]
    options = [(0, 1) if x else (0,) for x in h]  # remove duplicate encodings
    allowed = []
    adj = {}
    overlap = []
    for i in range(n):
        c, d = profiles[i], profiles[i - 1]
        hc, hd = h[i], h[i - 1]
        A, B, C = hc & (mask ^ d), hd & (mask ^ c), hc & hd
        overlap.append(C.bit_count())
        row = []
        for ec, ed in itertools.product(options[i], options[i - 1]):
            v = (i, ec, ed)
            succ = []
            for eu in options[(i + 1) % n]:
                cp, dp = c ^ (ec * hc), d ^ (ed * hd)
                u = profiles[(i + 1) % n] ^ (eu * h[(i + 1) % n])
                direct = (rot(u, 1, p) ^ u) == (cp | dp)
                predicted = (((eu ^ ec) * A) ^ ((eu ^ ed) * B) ^ ((eu ^ (ec & ed)) * C)) == 0
                assert direct == predicted
                if direct:
                    assert not C or ec == ed  # one-tick overlapping-defect guard
                    succ.append(((i + 1) % n, eu, ec))
                    row.append((eu, ec, ed))
            adj[v] = succ
        allowed.append(row)
    comps = sccs(adj)
    cyc = [cm for cm in comps if len(cm) > 1 or next(iter(cm)) in adj[next(iter(cm))]]
    persistent = set().union(*cyc) if cyc else set()
    result = {'name': name, 'p': p, 'spatial_period': n, 'graph_nodes': len(adj),
              'graph_edges': sum(map(len, adj.values())), 'fixed_profile_count': h.count(0),
              'overlap_histogram': sorted(Counter(overlap).items()),
              'cyclic_shapes': sorted((len(cm), sum(w in cm for v in cm for w in adj[v])) for cm in cyc),
              'persistent_mixed_parent_states': [v for v in sorted(persistent) if v[1] != v[2]],
              'allowed_patterns_by_site': allowed}
    (OUT / (name + '-gauge.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'allowed_patterns_by_site'}), flush=True)


def period_loss_control():
    p = 6
    adj = {(c, d): list(children((c, d), p)) for c in range(1 << p) for d in range(1 << p)}
    comps = sccs(adj)
    waves = [cm for cm in comps if len(cm) == 10 and all(least(v, p) == 6 for v in cm)]
    assert len(waves) == 3
    rain = {(21, 42), (42, 21)}
    start = min(min(cm) for cm in waves)
    wave = next(cm for cm in waves if start in cm)
    queue = deque(sorted(wave)); parent = {v: None for v in wave}
    end = None
    while queue:
        v = queue.popleft()
        if v in rain:
            end = v; break
        for w in adj[v]:
            if w not in parent:
                parent[w] = v; queue.append(w)
    assert end is not None
    path = []
    while end is not None:
        path.append(end); end = parent[end]
    path.reverse()
    assert all(valid(w, v, p) for v, w in zip(path, path[1:]))
    cycle = [path[0]]
    while True:
        w = next(w for w in adj[cycle[-1]] if w in wave)
        if w == cycle[0]: break
        cycle.append(w)
    result = {'p': p, 'right_cycle': cycle, 'leftward_link': path,
              'pair_periods': [least(v, p) for v in path], 'rain_cycle': sorted(rain)}
    (OUT / 'period-loss-control.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


def main():
    path = Path('tests/probes/phase480_p32.txt')
    old = [tuple(int(x, 16) for x in row.split()) for row in path.read_text().splitlines() if not row.startswith('#')]
    seeds = [(v, u) for u, v in old]  # normalize to (c,d)->(u,c)
    assert len(seeds) == len(set(seeds)) == 480
    assert all(valid(w, v, 32) for v, w in zip(seeds, seeds[1:] + seeds[:1]))
    assert all(least((v[0], v[0]), 32) == 32 for v in seeds)
    adj12, root12 = closure([(1323, 2868)], 12)
    assert (len(root12), sum(w in root12 for v in root12 for w in adj12[v])) == (30, 32)
    U, V = (1323, 2868), (2772, 3372)
    selfpath = None
    for ch in adj12[U]:
        trace = [U, ch]
        while trace[-1] not in (U, V):
            nx = [w for w in adj12[trace[-1]] if w in root12]
            assert len(nx) == 1
            trace.append(nx[0])
        if trace[-1] == U: selfpath = trace[:-1]
    assert selfpath is not None and len(selfpath) == 14
    phase_gauge([v[0] for v in selfpath], 12, 'period12-stay')
    phase_gauge([v[0] for v in seeds], 32, 'period32-wave480')
    period_loss_control()
    closure(seeds, 32)
    lines = (OUT / 'p32-closure.tsv').read_text().splitlines()
    c, d, comp = map(int, lines[1].split())
    lines[1] = f'{c ^ 1} {d} {comp}'
    (OUT / 'p32-corrupted.tsv').write_text('\n'.join(lines) + '\n')
    print('DYADIC_RETURN_EXTRACTION_COMPLETE', flush=True)


if __name__ == '__main__': main()
