#!/usr/bin/env python3
"""Independent literal P1024 certificate checker and same-400-row replay.

No imports from Local's graph/simulation scripts. See GC2388 freeze.
"""
import hashlib
import json
import os
from pathlib import Path
import random
import time
from collections import deque

import networkx as nx


def states(path, expected_sha):
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected_sha
    rows = [line.split() for line in raw.decode().splitlines() if not line.startswith('#')]
    result = {(int(c), int(w, 2)) for c, w in rows}
    assert len(result) == len(rows)
    assert all(0 <= c < 1024 and 0 <= w < 256 for c, w in result)
    return result


def successors(state, column):
    phase, word = state
    base = {i: (column >> ((phase + 195*i) % 1024)) & 1 for i in range(-10, 3)}
    edges = set()
    fail = 0
    for low in range(4):
        mismatch = {i: 0 for i in range(-10, 3)}
        mismatch[0] = 1
        for j in range(1, 9):
            mismatch[-j] = (word >> (j-1)) & 1
        mismatch[-9], mismatch[-10] = low & 1, low >> 1
        other = {i: base[i] ^ mismatch[i] for i in base}
        evolve = lambda row, i: row[i] ^ (row[i-1] | row[i-2])
        after = {i: evolve(base, i) ^ evolve(other, i) for i in range(-8, 3)}
        changed = [i for i in after if after[i]]
        if not changed:
            fail += 1
            continue
        advance = max(changed)
        # Enumerate all 256 possible next windows, retain those consistent with outputs.
        for candidate in range(256):
            if all(advance-j not in after or ((candidate >> (j-1)) & 1) == after[advance-j]
                   for j in range(1, 9)):
                edges.add((((phase+1+195*advance) % 1024, candidate), advance))
    return edges, fail


def reconstruct():
    bits = (Path(__file__).parent / 'phase1024_ring.txt').read_text().strip()
    assert len(bits) == 1024 and set(bits) <= {'0', '1'}
    initial = sum(int(b) << i for i, b in enumerate(bits))
    ring_mask = (1 << 1024)-1
    row = initial
    orbit = []
    for _ in range(1024):
        orbit.append(row)
        one = ((row << 1) | (row >> 1023)) & ring_mask
        two = ((row << 2) | (row >> 1022)) & ring_mask
        row ^= one | two
    assert row == initial
    column = sum((row & 1) << t for t, row in enumerate(orbit))
    # Pin the spatial/time dictionary without relying on the graph implementation.
    assert all(((initial >> n) & 1) == ((column >> ((195*n) % 1024)) & 1) for n in range(1024))
    for phase in range(1024):
        bit = lambda j: (column >> (j % 1024)) & 1
        assert bit(phase+1) == bit(phase) ^ (bit(phase-195) | bit(phase-390))
    return orbit, column


def main():
    start = time.process_time()
    inputs = Path(os.environ['CAPTURE_INPUT'])
    out = Path(os.environ['CAPPED_OUT'])
    certified = states(inputs/'S_E_all.txt', 'eeb62a45f0dc278d887b63bed66c1d65f8e25f360431fc05963c601c96928e47')
    clean = states(inputs/'U.txt', 'bf6ad11cff5601a5c5e57cd982316b870caea1909fefb1e5a82f2f0fc32e1fcb')
    assert len(certified) == 389 and len(clean) == 52 and clean <= certified
    orbit, column = reconstruct()
    for word in range(256):
        packed = (word ^ ((word << 1) | (word << 2) | 3)) & 255
        scalar = 0
        for n in range(8):
            gate = 1 if n < 2 else ((word >> (n-1)) | (word >> (n-2))) & 1
            scalar |= (((word >> n) & 1) ^ gate) << n
        assert scalar == packed
    graph = {}
    for state in sorted(certified):
        edges, fail = successors(state, column)
        assert not fail and edges
        assert all(v in certified for v, a in edges)
        graph[state] = edges
    reachable = set(clean)
    queue = deque(clean)
    while queue:
        for v, _ in graph[queue.popleft()]:
            if v not in reachable:
                reachable.add(v)
                queue.append(v)
    assert reachable == certified
    values = {s: 0 for s in certified}
    minima = []
    for _ in range(3):
        values = {s: min(a+values[v] for v, a in graph[s]) for s in certified}
        minima.append(min(values.values()))
    assert minima[-1] >= 1
    # Independent negative control: deletion of a reached state must violate closure/start inclusion.
    removed = min(certified-clean)
    assert any(v == removed for edges in graph.values() for v, _ in edges)

    # Bounded extra question: does the certified graph force the measured exact speed?
    directed = nx.DiGraph()
    directed.add_nodes_from(certified)
    directed.add_edges_from((s, v) for s in graph for v, _ in graph[s])
    components = []
    potentials = []
    for component in nx.strongly_connected_components(directed):
        cyclic = len(component) > 1 or any(v == s for s in component for v, _ in graph[s])
        if not cyclic:
            continue
        root = min(component)
        potential = {root: 0}
        queue = deque([root])
        conflicts = []
        while queue:
            s = queue.popleft()
            for v, a in sorted(graph[s]):
                if v not in component:
                    continue
                wanted = potential[s]+13*a-17
                if v not in potential:
                    potential[v] = wanted
                    queue.append(v)
                elif potential[v] != wanted:
                    conflicts.append((s, v, a, wanted-potential[v]))
        components.append({'size': len(component), 'speed17over13_potential': not conflicts,
                           'conflicts': conflicts[:8]})
        if not conflicts:
            potentials.extend([list(s)+[potential[s]] for s in sorted(component)])
    (out/'graph.json').write_text(json.dumps([{'state': s, 'edges': sorted(graph[s])} for s in sorted(graph)])+'\n')
    (out/'potentials.json').write_text(json.dumps(potentials)+'\n')

    rng = random.Random(39)
    trials = []
    summaries = []
    for width in (40, 80):
        horizon = 6*width+2000
        depth = 2*horizon+width+16
        mask = (1 << depth)-1
        background = [sum(row << i for i in range(0, depth, 1024)) & mask for row in orbit]
        for index in range(200):
            phase = rng.randrange(1024)
            prefix = rng.getrandbits(width)
            x = (background[phase] >> width << width) | prefix
            passed = None
            entry = None
            for t in range(horizon+1):
                difference = x ^ background[(phase+t) % 1024]
                front = difference.bit_length()-1
                assert front <= width-1+2*t
                if passed is None and front >= 3*width:
                    passed = t
                if passed is not None and front >= 12:
                    near = sum(((difference >> (front-j)) & 1) << (j-1) for j in range(1, 9))
                    state = ((phase+t+195*front) % 1024, near)
                    if state in certified:
                        entry = {'time': t, 'front': front, 'state': state, 'after_pass': t-passed}
                        break
                x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
            trials.append({'width': width, 'index': index, 'theta': phase, 'prefix_hex': hex(prefix),
                           'passed_3K': passed, 'horizon': horizon, 'entry': entry})
        group = trials[-200:]
        entries = [r['entry'] for r in group if r['entry']]
        summaries.append({'width': width, 'captured': len(entries), 'trials': 200,
                          'max_after_pass': max((r['after_pass'] for r in entries), default=None),
                          'min_entry_front': min((r['front'] for r in entries), default=None)})
    (out/'trials.json').write_text(json.dumps(trials, indent=2)+'\n')
    summary = {'status': 'PASS' if all(x['captured'] == 200 for x in summaries) else 'COUNTERFACTUAL',
               'states': len(certified), 'clean_states': len(clean),
               'edges': sum(map(len, graph.values())), 'min_advance_k1_k2_k3': minima,
               'cyclic_components': components, 'trials': summaries,
               'cpu_seconds': time.process_time()-start,
               'scope': 'exact finite certificate check and same400 inputs; no universal capture theorem'}
    (out/'capture-summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
