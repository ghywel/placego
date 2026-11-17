#!/usr/bin/env python3
"""Integer balance of adjacent triangle-hole paths; one fixed cost test.

RUN-ON: cpu, standard-library Python, no solver/census.
COMMAND: python3 tests/probes/lexicon/rule30_zero_triangle_hole_flux.py

Record searched: hole.count/hole.population/internal.hole/empty.pair
with integer/flux/monoton/creation/destruction -> one unrelated archived
single-hole count warning. GC1203/1204 and L689 read; G140/GC1108 keep
the family-count and lossless-recoding scopes separate.

PREDICTIONS before first execution (2026-10-13):
 F1: all16 local inputs obey integer delta h=AB-h(A+B), not merely
     its parity. Both signs occur: outer11/inner01 creates a hole;
     outer01/inner00 destroys one.
 F2 must hold: on24 fixed path cases from C2, when the first black
     guard passes, J_next-J_old equals the strict interior signed flux,
     J counting holes excluding the terminal visible sample.
 F3 blind(0.55): at the accepted125 fixture's a0/1/8, J_next>=J_old
     in all three. Refuted by any decrease. Counterfactual: each real
     no11-compatible black-clock step pays a monotone hole cost.
 Independent controls: literal Rule30 versus packed Boolean evolution,
     direct integer hole counts versus the local flux expression.
 Unexpected: the terminal signed flux is -q_old under the old black
     guard; dropping that guard invalidates its removal (input0000).
 No expanding sample, full-witness validation, survival census or tuning
     of alternative potentials follows if F3 fails.

OUTCOME: F1/F2 held (all16 local inputs,24 fixed paths,12 old-guard
cases). F3 REFUTED: actual125 at a0 gives J26->31 (22 births,17 deaths),
a1 gives31->26 (15,20), a8 gives31->29 (23,25). The first two visible
pairs are both00. Independent controls and the terminal counter pass.
Stop the proposed monotone J cost; no potential tuning or larger run.
"""
import json
from itertools import product
from pathlib import Path
from rule30_zero_triangle_guard_transport import literal, packed, seed_for
from rule30_zero_triangle_adjacent_charge import cell, h, path


def flux(a, b, c, d):
    return a * b - h(c, d) * (a + b)


def balance(rows, phase, d, a):
    e = 1 ^ ((phase + d) % 2)
    k, crop = d + 2 * a + e, a + 1
    n = k - crop
    old, _ = path(rows, phase, d, a, e)
    new, _ = path(rows, phase, d, a + 1, e)
    deltas = []
    for u in range(n):
        t, j = crop + u, n - u
        z = [cell(rows, phase, t, z) for z in (j + 2, j + 1, j, j - 1)]
        delta = flux(*z)
        assert new[u] - old[u] == delta
        deltas.append(delta)
    j_old, j_new = sum(old[:-1]), sum(new[:-1])
    passed = rows[k][1] == 1
    if passed:
        assert deltas[-1] == -old[-1]
        assert j_new - j_old == sum(deltas[:-1])
    return passed, (j_old, j_new), (deltas[:-1].count(1), deltas[:-1].count(-1))


def main():
    for a, b, c, d in product((0, 1), repeat=4):
        outer = (30 >> (4 * a + 2 * b + c)) & 1
        inner = (30 >> (4 * b + 2 * c + d)) & 1
        assert h(outer, inner) - h(c, d) == flux(a, b, c, d)
    assert flux(1, 1, 0, 1) == 1 and flux(0, 1, 0, 0) == -1
    cases, passed = 0, 0
    for d, a, phase, tail in product((2, 5, 8), (0, 1), (0, 1), (0, 1)):
        e = 1 ^ ((phase + d) % 2); k = d + 2 * a + e
        seed = seed_for(d, k + 2, tail)
        rows = packed(seed, phase, k + 2, 2 * k + 10)
        assert rows == literal(seed, phase, k + 2, 2 * k + 10)
        ok, _, _ = balance(rows, phase, d, a)
        passed += ok; cases += 1
    root = Path(__file__).resolve().parents[3]
    records = json.loads((root / 'site/wolframcollatzmahler/data/records.json').read_text())['rows']
    f = next(r for r in records if r['depth'] == 125 and r['phase'] == 1)
    assert f['L'] == 21 and len(f['left']) == 145 and f['left'][123] == '1'
    seed = {j: int(b) for j, b in enumerate(f['left'], 1)}
    rows = packed(seed, 1, 144, 290)
    assert rows == literal(seed, 1, 144, 290)
    monotone = True
    for a in (0, 1, 8):
        ok, (old, new), (births, deaths) = balance(rows, 1, 125, a)
        assert ok
        monotone &= new >= old
        print('F3 fixture a=%d: J %d->%d, births=%d deaths=%d' % (a, old, new, births, deaths))
    assert flux(0, 0, 0, 0) == 0 and -h(0, 0) == -1
    print('F1/F2 PASS:16 local inputs;', cases, 'fixed paths;', passed, 'old-guard cases; independent controls PASS.')
    print('F3', 'HELD on the fixed cases only' if monotone else 'REFUTED: a real step lowers J; stop the monotone J cost.')


if __name__ == '__main__':
    main()
