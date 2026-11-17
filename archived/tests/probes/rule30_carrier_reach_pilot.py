#!/usr/bin/env python3
"""GC2252: one frozen period-16 reachability pilot from named older cycles.

No full pair census, temporal rollout, subprocess, thread or automatic extension.
The independent oracle integrates the literal decimal Rule30 truth table.
"""
from collections import deque
import hashlib
import json
import os
from pathlib import Path
import resource
import time

Q = 16
CAP = 4096
RULE30 = (0, 1, 1, 1, 1, 0, 0, 0)


def successors(a, b, q):
    mask = (1 << q) - 1
    f = a | b
    if f.bit_count() % 2:
        return []
    u, shift = f, 1
    while shift < q:
        u ^= u << shift
        shift *= 2
    c = (u << 1) & mask
    return [(b, c), (b, c ^ mask)]


def literal_successors(a, b, q):
    found = []
    for initial in (0, 1):
        c, value = 0, initial
        for t in range(q):
            c |= value << t
            value = RULE30[4 * value + 2 * ((b >> t) & 1) + ((a >> t) & 1)]
        if value == initial:
            found.append((b, c))
    return found


def rotate(v, t, q):
    return ((v >> t) | (v << (q - t))) & ((1 << q) - 1)


def primitive16(v):
    return (v & 255) != (v >> 8)


def main():
    start = time.monotonic()
    out = Path(os.environ['CAPPED_OUT'])
    assert resource.getrlimit(resource.RLIMIT_CPU) == (60, 60)
    assert resource.getrlimit(resource.RLIMIT_FSIZE) == (16 << 20, 16 << 20)
    inputs = {'q': Q, 'state_cap': CAP, 'threads': 1, 'subprocesses': 0,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / 'inputs.json').write_text(json.dumps(inputs, indent=2) + '\n')

    # Full small local control, not a dynamical graph census.
    for a in range(16):
        for b in range(16):
            assert sorted(successors(a, b, 4)) == sorted(literal_successors(a, b, 4))
    carrier = (86, 149, 101, 89)
    exit_path = (86, 149, 154, 21, 234, 170, 85, 170)
    for j in range(4):
        a, b, c = (carrier[(j + k) % 4] for k in range(3))
        assert (b, c) in literal_successors(a, b, 8)
    for a, b, c in zip(exit_path, exit_path[1:], exit_path[2:]):
        assert (b, c) in literal_successors(a, b, 8)
    assert (149, 100) not in literal_successors(86, 149, 8)
    # Odd forcing is not a cyclic solution: ignoring the last tick is unsound.
    assert successors(1, 0, 4) == literal_successors(1, 0, 4) == []
    controls = {'all_256_q4_pair_oracles': True, 'known_carrier_cycle': True,
                'known_carrier_to_rain': True, 'flipped_carrier_bit_rejected': True,
                'missing_cyclic_closure_mutant_rejected': True}
    (out / 'controls.json').write_text(json.dumps(controls, indent=2) + '\n')

    roots = {(0, 0), (0x5555, 0xAAAA), (0xAAAA, 0x5555)}
    for t in range(8):
        for j in range(4):
            a, b = (rotate(carrier[(j + k) % 4], t, 8) for k in range(2))
            roots.add((a | (a << 8), b | (b << 8)))
    roots = sorted(roots)
    todo = deque(roots)
    parents = {v: None for v in roots}
    graph = {}
    cap_hit = False
    while todo:
        v = todo.popleft()
        following = successors(*v, Q)
        assert sorted(following) == sorted(literal_successors(*v, Q))
        graph[v] = following
        for w in following:
            if w not in parents:
                if len(parents) == CAP:
                    cap_hit = True
                    break
                parents[w] = v
                todo.append(w)
        if cap_hit:
            break
    certificate = {'roots': roots,
                   'nodes': [{'pair': v, 'parent': parents[v], 'successors': graph.get(v)}
                             for v in sorted(parents)], 'complete': not cap_hit}
    result = {'status': 'STATE_CAP_INCONCLUSIVE' if cap_hit else 'COMPLETE',
              'reached': len(parents), 'expanded': len(graph),
              'primitive16_reached': sum(any(map(primitive16, v)) for v in parents),
              'root_count': len(roots), 'controls_pass': True}
    if not cap_hit:
        assert set(graph) == set(parents)
        assert all(w in graph for following in graph.values() for w in following)
        reverse = {v: [] for v in graph}
        for v, following in graph.items():
            for w in following:
                reverse[w].append(v)
        degree = {v: len(following) for v, following in graph.items()}
        dead = deque(v for v in graph if degree[v] == 0)
        ranks = {}
        while dead:
            v = dead.popleft()
            ranks[v] = 1 + max((ranks[w] for w in graph[v]), default=0)
            for u in reverse[v]:
                degree[u] -= 1
                if degree[u] == 0:
                    dead.append(u)
        live = set(graph) - set(ranks)
        # A second certificate check uses the scalar oracle, not peeling counts.
        for v, rank in ranks.items():
            for w in literal_successors(*v, Q):
                assert w in ranks and ranks[w] < rank
        for v in live:
            assert any(w in live for w in literal_successors(*v, Q))
        high_live = sorted(v for v in live if any(map(primitive16, v)))
        result.update({'surviving': len(live), 'primitive16_surviving': len(high_live),
                       'max_dead_rank': max(ranks.values(), default=0),
                       'max_primitive16_rank': max((ranks[v] for v in ranks
                                                   if any(map(primitive16, v))), default=0)})
        certificate['dead_ranks'] = [[*v, rank] for v, rank in sorted(ranks.items())]
        certificate['live'] = sorted(live)
        if high_live:
            v = high_live[0]
            prefix, here = [], v
            while here is not None:
                prefix.append(here)
                here = parents[here]
            prefix.reverse()
            suffix, seen, here = [], {}, v
            while here not in seen:
                seen[here] = len(suffix)
                suffix.append(here)
                here = next(w for w in graph[here] if w in live)
            certificate['witness'] = {'prefix': prefix, 'suffix': suffix,
                                      'cycle_starts_at': seen[here]}
    result['wall_s'] = time.monotonic() - start
    usage = resource.getrusage(resource.RUSAGE_SELF)
    result['process_cpu_s'] = usage.ru_utime + usage.ru_stime
    (out / 'certificate.json').write_text(json.dumps(certificate, indent=2) + '\n')
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
