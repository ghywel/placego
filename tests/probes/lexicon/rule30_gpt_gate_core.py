#!/usr/bin/env python3
"""GC396: isolate target observations forcing column6(s-6)=0 in GC395.
Prediction before run: a strict subset of the28 target4/5 cells suffices (P1).
No claim that the greedy core has minimum cardinality. Counterfactual: every
observed target cell is needed. Controls: removing any retained cell admits an
alternative initial row; forward and reversed deletion orders both stay sound.
Unexpected check: find first temporal prefix rejecting all alternatives.
OUTCOME: P1 HELD. Both deletion orders give a single observation,
column5(s-2)=0. All5504 candidates with column6(s-6)=1 violate it.
Dropping that observation admits a counterexample. First blocking prefix ends-2.
Fixed initial0..6 is0011100 at offset-14; retaining this anchor is essential.
Same8192 finite-cone initial rows, supplied wall; no126-step preparation claim.
"""
import json
from rule30_gpt_gate_completion import target, OFFSETS

CELLS = [(j, k) for k in OFFSETS for j in (4, 5)]


def main():
    failures = []
    for seed in range(8192):
        row = [0] + [target(j, -14) for j in range(1, 7)]
        row += [(seed >> i) & 1 for i in range(13)]
        mask = 0
        alt = False
        for k in OFFSETS:
            for j in (4, 5):
                if row[j] != target(j, k):
                    mask |= 1 << CELLS.index((j, k))
            if k == -6:
                alt = row[6] == 1
            if k != -1:
                row = [(k + 1) % 2] + [row[j-1] ^ (row[j] | row[j+1])
                                      for j in range(1, len(row)-1)]
        if alt:
            failures.append((seed, mask))
    full = (1 << len(CELLS)) - 1
    assert failures and all(mask & full for _, mask in failures)
    def blocks(keep):
        return all(mask & keep for _, mask in failures)
    results = []
    for order in (range(len(CELLS)), reversed(range(len(CELLS)))):
        keep = full
        for i in order:
            trial = keep & ~(1 << i)
            if blocks(trial):
                keep = trial
        witnesses = []
        for i in range(len(CELLS)):
            if keep & (1 << i):
                trial = keep & ~(1 << i)
                witness = next(seed for seed, mask in failures if not mask & trial)
                witnesses.append(witness)
        assert blocks(keep)
        results.append({'cells': [[j, k, target(j, k)] for i, (j, k) in enumerate(CELLS)
                                  if keep & (1 << i)],
                        'deletion_witnesses': len(witnesses)})
    first = next(k for k in OFFSETS if blocks(sum(1 << i for i, (_, t) in enumerate(CELLS) if t <= k)))
    print(json.dumps({'alternative_initial_rows': len(failures), 'cores': results,
                      'first_blocking_prefix_end': first,
                      'scope': 'inclusion-minimal observation sets, fixed initial1..6'}, indent=2))


if __name__ == '__main__':
    main()
