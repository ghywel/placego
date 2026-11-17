#!/usr/bin/env python3
"""rule30_rc2_export.py: export RC2's certificates (RULE30-GPT.md §G181, GPT's GC223 request) as one JSON artifact for
GPT's static checker. The RC2 run (rule30_rc2.py) kept no arrays, so this regenerates them with the same code
(rule30_rq3.reached, rule30_rqo.feat, rule30_rc2.context_test), deterministically and inside RC2's caps (60 CPU s,
128 MiB). The artifact stays outside Git; its SHA-256 and the producing commit are recorded in the ledger.

COMMAND:    python3 tests/probes/lexicon/rule30_rc2_export.py OUT.json

Format, per q in 1, 2, 4, 8 (words as integers, bit t = time t; states aligned at arrival phase 0):
  root: vertex index of the root (0, 2^q - 1);
  vertices: [{"state": [a, b], "parent_edge": edge index or null}];
  edges: [{"source": vertex index, "target": vertex index, "delay": d}] (every actual reached edge);
  K: [{"label": [phi(s), phi(t)], "K": value}] for every edge label, terminal labels included;
  summary: counts, K max and the lifted h max, recomputed here.
"""
import json
import os
import resource
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_rq3 as r3                                   # noqa: E402
import rule30_rqo as ro                                   # noqa: E402
import rule30_rc2 as rc                                   # noqa: E402


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (65, 65))
    t0 = time.process_time()
    out = {'producer': 'tests/probes/lexicon/rule30_rc2_export.py', 'note': 'regenerated (RC2 kept no arrays)'}
    for q in (1, 2, 4, 8):
        root, depth, parent, edges, exits = r3.reached(q)
        verts = sorted(depth, key=lambda s: (depth[s], s))
        vid = {s: i for i, s in enumerate(verts)}
        eidx = {(s, t, d): i for i, (s, t, d) in enumerate(edges)}
        lab = {s: ro.feat(s, q) for s in depth}
        feas, K, quot, cyc, n_arcs, L = rc.context_test(edges, lambda v: lab[v], lambda e: 2 * e[2] - 5)
        assert feas
        ok, h = rc.lift(edges, L, K, lambda e: 2 * e[2] - 5, list(depth))
        assert ok
        vrows = []
        for s in verts:
            pe = None
            if parent[s] is not None:
                prev, d, c = parent[s]
                pe = eidx[(prev, s, d)]
            vrows.append({'state': list(s), 'parent_edge': pe})
        out[str(q)] = {
            'root': vid[root],
            'vertices': vrows,
            'edges': [{'source': vid[s], 'target': vid[t], 'delay': d} for s, t, d in edges],
            'K': [{'label': [list(x[0]), list(x[1])], 'K': K[x]} for x in sorted(K)],
            'summary': {'vertices': len(verts), 'edges': len(edges), 'labels': len(K), 'cap_exits': exits,
                        'K_max': max(K.values()), 'h_max': max(h.values())},
        }
        print('q = %d: vertices %d, edges %d, labels %d, K max %d, h max %d' % (
            q, len(verts), len(edges), len(K), max(K.values()), max(h.values())))
    with open(sys.argv[1], 'w') as f:
        json.dump(out, f, sort_keys=True, separators=(',', ':'))
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('written %s; CPU %.2f s, peak RSS %.1f MiB' % (sys.argv[1], time.process_time() - t0, rus.ru_maxrss / 1048576))


if __name__ == '__main__':
    main()
