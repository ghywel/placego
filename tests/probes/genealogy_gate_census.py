#!/usr/bin/env python3
"""L1285 T6 (Local, 2026-11-01): which elementary rules admit GC2357's capture argument. Predictions in
reports/rule30-genealogy.md section 19.3, written first. Run: python3 tests/probes/genealogy_gate_census.py  (a few minutes)

For every rule 0..255 and every 12-bit left prefix with a black edge (bit 0 = 1), zeros beyond, 67 steps:
  edge:    the leftmost black cell moves left by exactly one each step (so left-edge coordinates make sense);
  pair:    no adjacent diagonals (n, n+1), n <= 10, both white for n+1 consecutive times;
  capture: with all-parent marks from the edge, no unmarked black cell on diagonal j <= 11 at time >= C_j;
  exit:    the marked front leaves band 0..D (D <= 9) within E(D) = (D+2)(D+3)/2 steps of any start time <= 20.
A rule failing the edge test is not tested further. Witnesses are the first failing prefix.
"""
import numpy as np

NB, S = 12, 67
NP = 1 << (NB - 1)
W = NB + 2 * S + 6
pref = ((np.arange(NP)[:, None] >> np.arange(NB - 1)) & 1).astype(np.uint8)
Cj = np.array([0] + [1 + j * (j - 1) // 2 for j in range(1, 12)])
ED = np.array([(D + 2) * (D + 3) // 2 for D in range(10)])
edge_rules, pass_all, fails = [], [], {}
for rule in range(256):
    table = np.array([(rule >> k) & 1 for k in range(8)], dtype=np.uint8)
    rows = np.zeros((NP, W), dtype=np.uint8)
    rows[:, S + 1] = 1
    rows[:, S + 2:S + 2 + NB - 1] = pref
    # left-edge index 0 at time t sits at column S + 1 - t
    marks = np.zeros_like(rows)
    marks[:, S + 1] = 1
    edge_ok = True
    last_unmarked = np.full((NP, 12), -1, dtype=np.int64)
    runs = np.zeros((NP, 11), dtype=np.int64)
    pair_bad = np.zeros(NP, dtype=bool)
    front = np.zeros((NP, S + 1), dtype=np.int64)        # left-edge index of the marked front at each time
    for t in range(S + 1):
        e = S + 1 - t
        if t > 0:
            idx = 4 * rows[:, :-2] + 2 * rows[:, 1:-1] + rows[:, 2:]
            new = np.zeros_like(rows)
            new[:, 1:-1] = table[idx]
            nm = np.zeros_like(marks)
            nm[:, 1:-1] = new[:, 1:-1] & (marks[:, :-2] | marks[:, 1:-1] | marks[:, 2:])
            rows, marks = new, nm
            if not (np.all(rows[:, e] == 1) and not rows[:, :e].any()):
                edge_ok = False
                break
        band = rows[:, e:e + 12]
        mb = marks[:, e:e + 12]
        um = (band == 1) & (mb == 0)
        last_unmarked[um] = t
        pw = (rows[:, e:e + 11] == 0) & (rows[:, e + 1:e + 12] == 0)
        runs = np.where(pw, runs + 1, 0)
        pair_bad |= (runs >= np.arange(11) + 1).any(axis=1)
        front[:, t] = (marks[:, e:] * np.arange(W - e)).max(axis=1)
    if not edge_ok:
        continue
    edge_rules.append(rule)
    cap_bad = (last_unmarked >= Cj).any(axis=1)
    exit_bad = np.zeros(NP, dtype=bool)
    for t0 in range(0, 21):
        for D in range(10):
            win = front[:, t0:t0 + ED[D] + 1]
            exit_bad |= ~(win > D).any(axis=1)
    bad = cap_bad | exit_bad | pair_bad
    if not bad.any():
        pass_all.append(rule)
    else:
        k = int(np.flatnonzero(bad)[0])
        fails[rule] = (''.join(map(str, [1] + pref[k].tolist())), bool(pair_bad[k]), bool(cap_bad[k]), bool(exit_bad[k]))
has3 = [r for r in range(256) if (r & 1) == 0 and (r >> 1) & 1 and (r >> 4) & 1]
print(f'edge rules (leftmost black cell moves left one per step on every prefix): {len(edge_rules)}; '
      f'equal to the rules with f(000)=0, f(001)=1: {edge_rules == [r for r in range(256) if (r & 1) == 0 and (r >> 1) & 1]}')
print(f'rules passing white-pair, capture and exit bounds on every prefix: {len(pass_all)}: {pass_all}')
print(f'equal to the 32 rules with f(000)=0, f(001)=1, f(100)=1: {pass_all == has3}')
others = [r for r in edge_rules if r not in has3]
print(f'the other {len(others)} edge rules: failing {sum(1 for r in others if r in fails)}; witnesses (prefix from the edge; pair/capture/exit):')
for r in others:
    if r in fails:
        print(f'  rule {r}: {fails[r]}')
    else:
        print(f'  rule {r}: passes (f(100)=0)')
print('GENEALOGY_GATE_CENSUS_DONE')
