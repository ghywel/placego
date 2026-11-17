#!/usr/bin/env python3
"""GC397: audit initial-prefix assumptions of GC396's finite implication.
P1 before run: fewer than all six fixed initial bits suffice (confidence0.6).
Counterfactual: the four-update implication needs no initial anchor.
Independent controls: scalar replay of every retained counterexample; old prefix
must have zero violations and1376 antecedent-positive assignments (width17).
Unexpected check: flip wall phase while retaining the six initial bits.
OUTCOME: P1 HELD. Initial column1 can be freed; both deletion orders
retain exactly initial columns2..6=11100, each with a deletion counterexample.
15 of64 full six-bit prefixes obey the implication;49 have scalar-replayed
counterexamples. Original prefix has0 violations and1376 positive antecedents.
Flipping the wall phase gives544 violations with the original six-bit prefix.
131072 initial1..17 rows; supplied alternating wall; no long preparation claim.
"""
import json

ANCHOR = 14  # initial columns1..6: 0,1,1,1,0,0 (wall0 initially0).


def run(bits, wall=0, scalar=False):
    row = (bits << 1) | wall
    cells = [(row >> j) & 1 for j in range(18)] if scalar else None
    ant = None
    for t in range(13):
        if scalar:
            assert cells == [(row >> j) & 1 for j in range(len(cells))]
        if t == 8:
            ant = (row >> 6) & 1
        if t < 12:
            size = 17 - t
            row = ((row << 1) ^ (row | (row >> 1))) & ((1 << size) - 1)
            row = (row & ~1) | ((t + 1 + wall) % 2)
            if scalar:
                cells = [(t + 1 + wall) % 2] + [cells[j-1] ^ (cells[j] | cells[j+1])
                                                for j in range(1, len(cells)-1)]
    return ant, (row >> 5) & 1


def main():
    bad = [0] * 64
    antecedents = [0] * 64
    witnesses = {}
    for bits in range(1 << 17):
        a, c = run(bits)
        p = bits & 63
        antecedents[p] += a
        if a and not c:
            bad[p] += 1
            witnesses.setdefault(p, bits)
    assert bad[ANCHOR] == 0 and antecedents[ANCHOR] == 1376
    for bits in witnesses.values():
        assert run(bits, scalar=True) == (1, 0)
    def rejects(mask):
        return not any(n for p, n in enumerate(bad) if (p & mask) == (ANCHOR & mask))
    cores = []
    for order in (range(6), reversed(range(6))):
        keep = 63
        for i in order:
            trial = keep & ~(1 << i)
            if rejects(trial):
                keep = trial
        count = 0
        for i in range(6):
            if keep & (1 << i):
                trial = keep & ~(1 << i)
                assert any(n for p, n in enumerate(bad) if (p & trial) == (ANCHOR & trial))
                count += 1
        cores.append({'initial_cells': [[i+1, (ANCHOR >> i) & 1]
                                        for i in range(6) if keep & (1 << i)],
                      'deletion_witnesses': count})
    flip = sum(a and not c for a, c in
               (run(ANCHOR | (tail << 6), wall=1) for tail in range(1 << 11)))
    print(json.dumps({'initial_candidates': 1 << 17,
                      'valid_six_bit_prefixes': [p for p, n in enumerate(bad) if not n],
                      'bad_count_original': bad[ANCHOR],
                      'antecedent_count_original': antecedents[ANCHOR],
                      'cores': cores, 'flipped_wall_violations': flip,
                      'scalar_counterexamples_checked': len(witnesses)}, indent=2))


if __name__ == '__main__':
    main()
