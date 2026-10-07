#!/usr/bin/env python3
"""GC398: attempt a local Boolean propagation certificate for GC397.
P1 before run: relation propagation alone contradicts6(time8)=1 and5(time12)=0
under initial2..6=11100 and alternating wall initially0 (confidence0.5).
Counterfactual: no branch-free local certificate emerges.
Controls: all eight Rule30 input tuples used, every forced reduction retained;
unexpected check changes only the wall phase, where GC397 has counterexamples.
OUTCOME: P1 REFUTED for this propagation procedure. Phase0 stalls after
8 reductions in2 rounds, no contradiction; phase1 after7 reductions, also none.
The phase0 fixed point is NOT SAT (GC397's census proves this case impossible).
This is a retained failure of single-cell relation propagation, not a proof
that all branch-free symbolic methods fail or that branching is necessary.
Finite cone only; a fixed point without contradiction is not satisfiability.
"""
import json

TABLE = [(a, b, c, a ^ (b | c)) for a in (0, 1) for b in (0, 1) for c in (0, 1)]


def propagate(phase):
    dom = {(t, j): {0, 1} for t in range(13) for j in range(18-t)}
    for t in range(13):
        dom[t, 0] = {(t+phase) % 2}
    for j, b in zip(range(2, 7), (1, 1, 1, 0, 0)):
        dom[0, j] = {b}
    dom[8, 6], dom[12, 5] = {1}, {0}
    rules = [((t, j-1), (t, j), (t, j+1), (t+1, j))
             for t in range(12) for j in range(1, 17-t)]
    trace = []
    rounds = 0
    while True:
        changed = False
        rounds += 1
        for cells in rules:
            valid = [r for r in TABLE if all(v in dom[c] for c, v in zip(cells, r))]
            if not valid:
                return {'contradiction': True, 'rounds': rounds,
                        'contradictory_rule': cells, 'reductions': len(trace)}, trace
            for i, c in enumerate(cells):
                new = dom[c] & {r[i] for r in valid}
                if new != dom[c]:
                    # Audit against the complete relation, not a shortcut rewrite.
                    assert all(r[i] in new for r in TABLE
                               if all(v in dom[d] for d, v in zip(cells, r)))
                    trace.append({'cell': c, 'value': sorted(new),
                                  'rule': cells,
                                  'prior_domains': [sorted(dom[d]) for d in cells]})
                    dom[c] = new
                    changed = True
        if not changed:
            return {'contradiction': False, 'rounds': rounds,
                    'reductions': len(trace),
                    'nontrivial_domains': sum(len(v)==1 for v in dom.values())}, trace


def main():
    for phase in (0, 1):
        result, trace = propagate(phase)
        print(json.dumps({'wall_phase': phase, **result}))
        with open('/tmp/placego-gc398-phase%d-trace.json' % phase, 'w') as f:
            json.dump(trace, f, indent=2)


if __name__ == '__main__':
    main()
