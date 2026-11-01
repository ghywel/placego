#!/usr/bin/env python3
"""L1286 (Local, 2026-11-01): the eight F2 rules (f(p,q,0) = q) of section 20 of reports/rule30-genealogy.md.
Predictions P8a-P8d are written there first. Run: python3 tests/probes/genealogy_eight_rules.py   (seconds)
"""
import numpy as np

f = lambda r, p, q, c: (r >> (4 * p + 2 * q + c)) & 1
edge = [r for r in range(256) if f(r, 0, 0, 0) == 0 and f(r, 0, 0, 1) == 1]
F1 = [r for r in edge if f(r, 1, 0, 0) == 1]
F2 = [r for r in edge if all(f(r, p, q, 0) == q for p in (0, 1) for q in (0, 1))]
rest = [r for r in edge if r not in F1 and r not in F2]
assert len(F1) == 32 and F2 == [70, 78, 102, 110, 198, 206, 230, 238] and len(rest) == 24

NB, S = 12, 67
NP = 1 << (NB - 1)
W = NB + 2 * S + 6
pref = ((np.arange(NP)[:, None] >> np.arange(NB - 1)) & 1).astype(np.uint8)
E2 = np.array([(D + 1) * (D + 2) // 2 + 1 for D in range(10)])


def run(rule, nprefix=NP, prefix=None):
    table = np.array([(rule >> k) & 1 for k in range(8)], dtype=np.uint8)
    rows = np.zeros((nprefix, W), dtype=np.uint8)
    rows[:, S + 1] = 1
    if prefix is not None:
        rows[:, S + 2:S + 2 + NB - 1] = prefix
    marks = np.zeros_like(rows)
    marks[:, S + 1] = 1
    runs = np.zeros((nprefix, 11), dtype=np.int64)
    single_bad = np.zeros(nprefix, dtype=bool)
    front = np.zeros((nprefix, S + 1), dtype=np.int64)
    for t in range(S + 1):
        e = S + 1 - t
        if t > 0:
            idx = 4 * rows[:, :-2] + 2 * rows[:, 1:-1] + rows[:, 2:]
            new = np.zeros_like(rows)
            new[:, 1:-1] = table[idx]
            nm = np.zeros_like(marks)
            nm[:, 1:-1] = new[:, 1:-1] & (marks[:, :-2] | marks[:, 1:-1] | marks[:, 2:])
            rows, marks = new, nm
            assert np.all(rows[:, e] == 1) and not rows[:, :e].any()
        wh = rows[:, e:e + 11] == 0
        runs = np.where(wh, runs + 1, 0)
        single_bad |= (runs >= np.arange(11) + 1).any(axis=1)
        front[:, t] = (marks[:, e:] * np.arange(W - e)).max(axis=1)
    return single_bad, front


print('P8a/P8b, the F2 rules on every 12-bit prefix:')
for r in F2:
    sb, front = run(r, NP, pref)
    exit_bad = np.zeros(NP, dtype=bool)
    for t0 in range(21):
        for D in range(10):
            exit_bad |= ~(front[:, t0:t0 + E2[D] + 1] > D).any(axis=1)
    print(f'  rule {r}: single-diagonal windows violated on {int(sb.sum())} prefixes; sharper exit bound violated on {int(exit_bad.sum())}')
sb30, _ = run(30, NP, pref)
print(f'  Rule 30: single-diagonal windows violated on {int(sb30.sum())} of {NP} prefixes (the mechanisms differ)')
print('P8c, the lone edge under the other 24 edge rules:')
confined = 0
for r in rest:
    _, front = run(r, 1, None)
    confined += int(front.max() <= 1)
print(f'  front confined to band 0..1 for all {S} steps: {confined} of {len(rest)}')
print('P8d, single seed, each F2 rule, the marked front D(t) at t = 2000:')
T = 2000
for r in F2:
    table = np.array([(r >> k) & 1 for k in range(8)], dtype=np.uint8)
    Wd = 2 * T + 9
    x = np.zeros(Wd, dtype=np.uint8); x[T + 4] = 1
    m = x.copy()
    for t in range(T):
        idx = 4 * x[:-2] + 2 * x[1:-1] + x[2:]
        nx = np.zeros_like(x); nx[1:-1] = table[idx]
        nm = np.zeros_like(m); nm[1:-1] = nx[1:-1] & (m[:-2] | m[1:-1] | m[2:])
        x, m = nx, nm
    e = int(np.flatnonzero(x).min()); B = int(np.flatnonzero(m).max()); right = int(np.flatnonzero(x).max())
    print(f'  rule {r}: edge at {e - T - 4}, marked front at {B - T - 4}, D = {B - e}, rightmost black at {right - T - 4}, black cells {int(x.sum())}')
print('GENEALOGY_EIGHT_RULES_DONE')
