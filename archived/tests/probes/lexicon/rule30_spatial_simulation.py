#!/usr/bin/env python3
"""GC1000 bounded simulation-dominance test. Predictions in RULE30-GPT.md.
Uses GC999 exact spatial NFA, no further time images beyond two observations.
"""
from pathlib import Path
exec(compile(Path(__file__).with_name('rule30_spatial_nfa_observer.py').read_text().split('for src in ')[0], 'GC999-definitions', 'exec'))

def simulation(rows):
    n = len(rows)
    rel = [(1 << n)-1 for _ in rows]
    masks = [[sum(1 << r for r in edge) for edge in row] for row in rows]
    while True:
        check()
        new = rel.copy()
        for q in range(n):
            candidates = rel[q]
            while candidates:
                bit = candidates & -candidates
                candidates -= bit
                r = bit.bit_length()-1
                if any(not (rel[s] & masks[r][b]) for b in (0, 1) for s in rows[q][b]):
                    new[q] &= ~bit
        if new == rel:
            return rel
        rel = new

def prune(nfa, rel):
    rows, roots = nfa
    def maxima(xs):
        return {q for q in xs if not any(q != r and (rel[q] >> r & 1)
                 and (not (rel[r] >> q & 1) or q > r) for r in xs)}
    return reduce([tuple(maxima(edge) for edge in row) for row in rows], maxima(roots))

control = [({0}, {0}), ({1}, set())]
r = simulation(control)
assert r[1] & 1 and not (r[0] >> 1 & 1)
assert len(prune((control, {0, 1}), r)[0]) == 1
print('Strict-inclusion control PASS', flush=True)
nfa = FULL
try:
    for b in (1, 0):
        nfa = image(image(observe(nfa, b), 0), 1)
        rel = simulation(nfa[0])
        reduced = prune(nfa, rel)
        strict = sum(bool(rel[q] >> r & 1) and not (rel[r] >> q & 1)
                     for q in range(len(rel)) for r in range(len(rel)))
        for n in range(9):
            for w in itertools.product((0, 1), repeat=n):
                assert accepts(nfa, w) == accepts(reduced, w)
        print('states', len(nfa[0]), 'strict pairs', strict, 'roots', len(nfa[1]),
              'after prune', len(reduced[0]), 'roots', len(reduced[1]),
              'length8 language control PASS', flush=True)
except RuntimeError as e:
    print('STOP', str(e), flush=True)
