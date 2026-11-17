#!/usr/bin/env python3
"""GC2389: tiny exact check of saved GC2388 graph, independent of its generator."""
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path


def main(root):
    def read(name, digest):
        raw = (root/name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        return json.loads(raw)
    rows = read('graph.json', '58e2d667d2608a33a43aae14f5d8c57c68d9aca3f0d41a680385000b4441d4e4')
    h = {(c,w):v for c,w,v in read('potentials.json', '2ffb573d82d088a6a7309f22fcde74d2386ccfd7faba402cac29371dec16e649')}
    fibres, projected = defaultdict(set), defaultdict(set)
    edge_count = 0
    for row in rows:
        state = tuple(row['state'])
        fibres[state[0]].add(state[1])
        for dest, advance in row['edges']:
            dest = tuple(dest)
            assert h[dest]-h[state] == 13*advance-17
            assert dest[0] == (state[0]+1+195*advance) % 1024
            projected[state[0]].add((dest[0], advance))
            edge_count += 1
    assert len(rows) == len(h) == 389 and edge_count == 520
    assert len(projected) == 52 and all(len(v) == 1 for v in projected.values())
    assert all(len({h[c,w] for w in words}) == 1 for c,words in fibres.items())
    cycle, visited, phase = [], set(), min(projected)
    while phase not in visited:
        visited.add(phase)
        nxt, advance = next(iter(projected[phase]))
        cycle.append([phase, advance, h[phase,min(fibres[phase])]])
        phase = nxt
    assert phase == cycle[0][0] and visited == set(projected)
    advances = [a for c,a,v in cycle]
    period = next(p for p in range(1,53) if 52 % p == 0 and all(advances[i] == advances[(i+p)%52] for i in range(52)))
    resets = {c: min(words) for c, words in fibres.items() if len(words) == 1}
    waits = [next(n for n in range(52) if cycle[(i+n)%52][0] in resets) for i in range(52)]
    # Every edge of the original passes; changing one advance must fail its equation.
    first = rows[0]
    dest,a = first['edges'][0]
    assert h[tuple(dest)]-h[tuple(first['state'])] != 13*(a+1)-17
    result = {'cycle': cycle, 'period': len(cycle), 'total_advance': sum(advances),
              'least_advance_word_period': period, 'potential_range': [min(h.values()),max(h.values())],
              'resets': resets, 'max_reset_wait': max(waits), 'negative_control': 'PASS',
              'scope': 'saved finite graph; actual-front transfer is a separate hand claim'}
    (root/'clock-certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'cycle'}, indent=2))


if __name__ == '__main__':
    main(Path(sys.argv[1]))
