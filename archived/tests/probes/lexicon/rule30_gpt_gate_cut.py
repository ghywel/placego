#!/usr/bin/env python3
"""GC400: test Local L243's reachable intermediate cut idea.
P1 before run: one cut at times4..8 admits <=5 cells jointly determining the
antecedent and consequent on the anchored reachable family (confidence0.5).
Counterfactual: a small empirical cut supplies unconditional symbolic factors.
Controls: the full cut determines both outputs; both deletion orders remain
collision-free; every retained feature has a collision if removed.
Unexpected scope: factors are asserted only on the enumerated reachable states.
OUTCOME: P1 HELD on the reachable family: time8 has32 cut rows, and four
selected cells (4,6,7,9 or1,6,7,9) give14 projection values determining both
outputs. BUT all14 fibres are ambiguous when the unselected cut bits are free;
none of the six antecedent-true projections universally forces the consequent.
Small empirical factors therefore do not supply unconditional symbolic factors.
4096 initial rows, no new widths or wall variants, no long preparation claim.
"""
import json


def main():
    samples = {t: {} for t in range(4, 9)}
    for free in range(4096):
        bits = 14 | (free & 1) | ((free >> 1) << 6)
        row = bits << 1
        cuts = {}
        a = None
        for t in range(13):
            row = (row & ~1) | (t % 2)
            if t in samples:
                cuts[t] = row >> 1
            if t == 8:
                a = (row >> 6) & 1
            if t < 12:
                row = ((row << 1) ^ (row | (row >> 1))) & ((1 << (17-t))-1)
        pair = (a, (row >> 5) & 1)
        for t, state in cuts.items():
            assert samples[t].get(state, pair) == pair
            samples[t][state] = pair
    results = []
    for t, states in samples.items():
        n = 17-t
        def collision_free(mask):
            seen = {}
            for state, pair in states.items():
                key = state & mask
                if key in seen and seen[key] != pair:
                    return False
                seen[key] = pair
            return True
        cores = []
        for order in (range(n), reversed(range(n))):
            mask = (1 << n)-1
            assert collision_free(mask)
            for i in order:
                trial = mask & ~(1 << i)
                if collision_free(trial):
                    mask = trial
            for i in range(n):
                if mask & (1 << i):
                    assert not collision_free(mask & ~(1 << i))
            table = {str(state & mask): list(pair) for state, pair in states.items()}
            cores.append({'columns': [i+1 for i in range(n) if mask & (1 << i)],
                          'reachable_projection_count': len(table)})
            if t == 8:
                fibres = {}
                for raw in range(1 << n):
                    cells = [0] + [(raw >> i) & 1 for i in range(n)]
                    for dt in range(4):
                        cells = [(9+dt) % 2] + [cells[j-1] ^ (cells[j] | cells[j+1])
                                                for j in range(1, len(cells)-1)]
                    fibres.setdefault(raw & mask, set()).add(cells[5])
                cores[-1]['reachable_fibres_with_unrestricted_ambiguity'] = sum(
                    len(fibres[int(key)]) > 1 for key in table)
                cores[-1]['antecedent_true_fibres_universally_one'] = sum(
                    pair[0] == 1 and fibres[int(key)] == {1} for key, pair in table.items())
                cores[-1]['antecedent_true_reachable_fibres'] = sum(pair[0] == 1 for pair in table.values())
        results.append({'time': t, 'reachable_cut_rows': len(states), 'cores': cores})
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
