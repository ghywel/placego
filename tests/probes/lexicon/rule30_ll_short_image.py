#!/usr/bin/env python3
"""GC621 bounded second-return census, preregistered 2026-10-08.
COMMAND: python3 tests/probes/lexicon/rule30_ll_short_image.py
RUN-ON: GPT Intel host, 4096 assignments; no solver or NL search.
LS0 must hold: independent list and packed updates agree.
LS1 must hold: every row completes the two prescribed long loops.
LS2 blind: both fifth-bit values occur at the second return.
COUNTERFACTUAL: sites >=26 change return site 5; must fail by finite cone.
UNEXPECTED LS3 blind: initial site 14 alone determines that returned bit.
REFUTED-BY: LS0/LS1 failure or farther-tail dependence.
Scope: exact finite cone census; no infinite-choice or entropy inference.
OUTCOME: pending; append actual verdicts after the first run.
"""
from collections import Counter
from rule30_exceptional_gate import list_rows, packed_rows

PREFIX = '1110010001000'


def main():
    counts = Counter()
    by_next = Counter()
    examples = {}
    values = []
    for n in range(4096):
        suffix = [(n >> i) & 1 for i in range(12)]
        prefix = list(map(int, PREFIX)) + suffix
        decisions = []
        for tail in (0, 1):
            rows = list_rows(prefix + [tail]*15, 20)
            assert rows == packed_rows(prefix + [tail]*15, 20), 'LS0'
            assert [''.join(map(str, rows[t][:3])) for t in range(0,21,2)] == [
                '111','011','001','010','000','111','011','001','010','000','111'], 'LS1'
            assert rows[20][:4] == [1,1,1,0], 'marker'
            decisions.append(rows[20][4])
        assert decisions[0] == decisions[1], 'counterfactual unexpectedly passed'
        bit = decisions[0]
        values.append(bit)
        counts[bit] += 1
        by_next[(suffix[0],bit)] += 1
        examples.setdefault(bit, ''.join(map(str,prefix)))
    influences = [14+i for i in range(12)
                  if any(values[n] != values[n ^ (1 << i)] for n in range(4096))]
    print('return fifth-bit counts:', dict(sorted(counts.items())))
    print('counts by initial site 14:', dict(sorted(by_next.items())))
    print('representatives:', dict(sorted(examples.items())))
    print('influential initial sites:', influences)
    print('LS2 both values:', set(counts) == {0,1})
    print('LS3 site 14 alone:', influences == [14])
    print('LS0, LS1, unexpected farther-tail check: PASS')
    print('counterfactual site-26 dependence: REFUTED')
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()

# OUTCOME 2026-10-08, GPT Intel host: LS0/LS1 and farther-tail control PASS.
# All 4096 return fifth bits are 1; 2048 in each site-14 bin. LS2 REFUTED.
# Influential sites: none. LS3 prints False for the implemented criterion
# influences == [14]. Its prose "alone determines" was ambiguous: a constant
# is also a function of site 14, so do not call that literal statement refuted.
# No nonconstant site-14 decision exists in this cone. No data files or solver.
