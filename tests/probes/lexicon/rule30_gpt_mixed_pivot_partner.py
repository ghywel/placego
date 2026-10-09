#!/usr/bin/env python3
"""Bounded reuse audit of GC708's stored sixteen rows; no new words or horizons.
RUN-ON: cpu; COMMAND: feed GC708's output JSON on standard input.
Predictions before execution (2026-10-09):
 MP-P1: at every two-gap prefix, S/L third-letter branches have the same
 even partner bit at depth B+8, beside their opposite B+7 pivots.
 MP-P2: at least one of the four prefixes has that common partner black,
 so an all-zero continuation of its decoded earlier bits rejects both choices.
 Counterfactual: choosing the zero odd pivot always suffices for the next guard.
 Controls: rows agree through B+6 and disagree at B+7; stored forward replay
 controls must be PASS. Unexpected: the LL pair uses depth 28 and needs samples
 past the third short closing tick, supplied here by the fourth gap.
 Only necessary decoded conditions, no actual right realization or survival claim.
 OUTCOME: controls PASS; MP-P1 REFUTED (SS and LL partners depend on choice);
 MP-P2 HELD (SL and LS partners are both black). Predictions retained unchanged.
"""
import json, sys

r = json.load(sys.stdin)
assert all(r[k] == 'PASS' for k in ('ML-C1', 'ML-C2', 'ML-C3'))
rows = {x['word']: x['left'] for x in r['rows']}
out = []
for prefix in ('SS', 'SL', 'LS', 'LL'):
    B = sum(6 if x == 'S' else 10 for x in prefix)
    d = B + 7
    a, b = rows[prefix + 'SS'], rows[prefix + 'LS']
    assert len(a) >= d + 1 and len(b) >= d + 1
    assert a[:d-1] == b[:d-1] and a[d-1] != b[d-1]
    out.append({'prefix': prefix, 'B': B, 'pivot': [int(a[d-1]), int(b[d-1])],
                'partner': [int(a[d]), int(b[d])]})
print(json.dumps({'MP-controls': 'PASS',
 'MP-P1': 'HELD' if all(x['partner'][0] == x['partner'][1] for x in out) else 'REFUTED',
 'MP-P2': 'HELD' if any(x['partner'] == [1,1] for x in out) else 'REFUTED',
 'rows': out}, indent=2))
