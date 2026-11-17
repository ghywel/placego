#!/usr/bin/env python3
"""GC2405: literal arithmetic review controls, no new seed/trajectory census.

Prediction before execution: two-cell T merges; the k3,P128 weighted closure
has constant1 and a redundant-resolution guard stops; the stated five-state
chain has exact stationary mean2/5. Counterfactual: any assertion fails, so
return to the displayed hand calculation, not a wider experiment.
Record searched: CL645/GC2201/GC2205 and CL686 complete carrying sources;
current kit c42f6e51 RightProfiles/RightPeriods/DifferenceOrder.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path


def left(x):
    return tuple((x[j-2] if j >= 2 else 0) ^
                 ((x[j-1] if j else 0) | x[j]) for j in range(len(x)))


assert left((1, 0)) == left((1, 1)) == (1, 1)
image = {left(x) for x in ((0, 0), (0, 1), (1, 0), (1, 1))}
assert image == {(0, 0), (0, 1), (1, 1)}
assert {left(x) for x in image} == image
print('two-cell left map: merging; image stabilizes after one step')

# One fixed formal boundary calculation. This does not assert root realization.
P = 128
c = [1]
K = 0
for r in range(4):
    half = P // 2
    assert half % len(c) == 0
    K ^= (half // len(c) * sum(c)) & 1
    P = half
    if r < 3:
        total = (P // len(c) * sum(c)) & 1
        assert total == 0  # hence the unknown initial diagonal bit drops out
        pre = 0
        c2 = []
        for u in range(2 * len(c)):
            pre ^= c[u % len(c)]
            c2.append(total ^ pre)
        c = c2
assert (P, c, K) == (8, [1, 0, 0, 0, 1, 0, 0, 0], 0)
assert (P // 2) % len(c) != 0  # literal source stops SMALL_R
assert c[:4] == c[4:]  # reduced coefficient period is four
assert K ^ (sum(c[:4]) & 1) == 1
assert all(c[u] == comb(u + 3, 3) % 2 for u in range(8))
q0, k = 4, 3
q = (2 ** k) * q0
assert q >= 2 ** (k + 2) and k == q0 - 1
print('k3,P128: reduced forcing constant1, source SMALL_R; ruler condition agrees')

T = {
    'F': [(Q(1), 'H', 0)],
    'H': [(Q(1, 2), 'F', 1), (Q(1, 2), 'Z', 0)],
    'Z': [(Q(1, 2), 'A', 1), (Q(1, 2), 'Z', 0)],
    'A': [(Q(1, 2), 'F', 1), (Q(1, 2), 'B', 0)],
    'B': [(Q(1, 2), 'A', 1), (Q(1, 2), 'Z', 0)],
}
pi = dict(zip(T, map(lambda x: Q(x, 10), (2, 2, 3, 2, 1))))
assert sum(pi.values()) == 1
incoming = {s: Q(0) for s in T}
for s, edges in T.items():
    for p, dest, bit in edges:
        incoming[dest] += pi[s] * p
assert incoming == pi
assert sum(pi[s] * p * bit for s in T for p, dest, bit in T[s]) == Q(2, 5)
print('five-state random model: exact stationary mean2/5; no actual-seed transfer')

# Audit existing records only; no Phi iterations or fresh seeds.
records = {}
for name in ('edge_shift_tree.out', 'edge_shift_tree64.out'):
    seed = None
    for line in (Path(__file__).parent / 'wolfram' / name).read_text().splitlines():
        if line.startswith('# seed='):
            seed = line.split()[1][5:]
            records[seed] = {}
        elif seed is not None and line and line[0].isdigit():
            f = line.split()
            records[seed][int(f[0])] = f
rows = [r for dd in records.values() for r in dd.values()]
assert len(records) == 64 and len(rows) == 3584
assert sum(r[-1] == 'ok' for r in rows) == 3456
assert not any(r[-1] == 'FAIL' for r in rows)
assert sum(r[4] == 'FORCED' for r in rows) == 832
assert sum(r[4].startswith('SMALL_') for r in rows) == 31
k3_q_exp = []
small_family = []
for seed, dd in records.items():
    for j, row in dd.items():
        for k in (3, 6, 7):
            ctx = '11' + '01' * k
            if all(i in dd for i in range(j - len(ctx), j)) and ''.join(
                    dd[i][2] for i in range(j - len(ctx), j)) == ctx:
                if k == 3:
                    k3_q_exp.append(int(dd[j-4][1]))
                if row[4].startswith('SMALL_'):
                    small_family.append((k, row[4]))
assert min(k3_q_exp) == 8
assert sorted(small_family) == [(6, 'SMALL_R'), (7, 'SMALL_R')]
print('retained records:3456 checks,832 FORCED,31 SMALL; k3 q>=256; k6/7 SMALL_R')
print('CLOUD_DESCENT_REVIEW_CONTROLS_DONE')
