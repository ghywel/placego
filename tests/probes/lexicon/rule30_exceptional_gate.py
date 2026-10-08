#!/usr/bin/env python3
"""Bounded GC618 ancestry census, preregistered 2026-10-08 before first run.

COMMAND: python3 tests/probes/lexicon/rule30_exceptional_gate.py
RUN-ON: GPT Intel host; 32 assignments, no SAT solver or NL search.
PREDICTIONS:
EG0 must hold: list and independent packed-bit updates agree for every row.
EG1 must hold: the first return starts 11100000 for every tested extension.
EG2 blind: both values of the next-long Boolean gate occur.
EG3 must hold: the gate agrees with prescribed next-long completion.
COUNTERFACTUAL: changing sites >=18 can alter time-6 sites 9..11; must fail.
UNEXPECTED: compare all-zero and all-one farther tails through both returns.
REFUTED-BY: disagreement, failed forced prefix or a wrong gate outcome.
Scope: the 32 assignments exhaust the six-tick cone only. Infinite-tail
completion uses GC614/617/618 hand implications, not sampled tail evidence.
OUTCOME: pending; append the actual outcome after running.
"""
from collections import Counter
from itertools import product

PREFIX = '111001000100'


def list_rows(bits, ticks):
    rows = [bits]
    for t in range(ticks):
        row = rows[-1]
        left = [t % 2] + row[:-1]
        rows.append([left[i] ^ (row[i] | row[i+1])
                     for i in range(len(row)-1)])
    return rows


def packed_rows(bits, ticks):
    width = len(bits)
    row = sum(b << i for i, b in enumerate(bits))
    rows = [bits]
    for t in range(ticks):
        width -= 1
        row = (((row << 1) | (t % 2)) ^ (row | (row >> 1))) & ((1 << width)-1)
        rows.append([(row >> i) & 1 for i in range(width)])
    return rows


def main():
    counts = Counter()
    examples = {}
    triples = Counter()
    for suffix in product((0, 1), repeat=5):
        prefix = [int(b) for b in PREFIX] + list(suffix)
        outcomes = []
        for tail in (0, 1):
            bits = prefix + [tail]*23
            rows = list_rows(bits, 20)
            assert rows == packed_rows(bits, 20), 'EG0'
            assert rows[10][:8] == [1,1,1,0,0,0,0,0], 'EG1'
            a, b, c = rows[6][8:11]
            gate = (a & b) | (c & (a | (1-b)))
            hidden = [''.join(map(str, rows[t][:3])) for t in range(10,21,2)]
            complete = hidden == ['111','011','001','010','000','111']
            assert complete == bool(gate), 'EG3'
            assert rows[10][8] == gate, 'ninth return bit'
            assert gate == 1-prefix[12], 'EG4 hand-collapse addendum'
            outcomes.append((a,b,c,gate))
        assert outcomes[0] == outcomes[1], 'counterfactual unexpectedly passed'
        a,b,c,gate = outcomes[0]
        counts[gate] += 1
        triples[(a,b,c)] += 1
        examples.setdefault(gate, ''.join(map(str,prefix)))
    print('gate counts:', dict(sorted(counts.items())))
    print('time-6 triples:', dict(sorted(triples.items())))
    print('representatives:', dict(sorted(examples.items())))
    print('EG2 both gate values:', set(counts) == {0,1})
    print('EG0, EG1, EG3 and unexpected tail check: PASS')
    print('counterfactual site-18 dependence: REFUTED')
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()

# OUTCOME 2026-10-08, GPT Intel host: first run, EG0/EG1/EG3 PASS;
# EG2 confirmed: 16 gate-zero and 16 gate-one extensions. Reachable triples
# 100:16, 101:8, 110:4, 111:4. Both farther-tail controls agree.
# Counterfactual site-18 dependence refuted. No solver or entropy claim.
# ADDENDUM before second run: hand algebra predicts EG4 gate=NOT initial
# site 13 for all 32 extensions; assert this in addition to original checks.
# SECOND-RUN OUTCOME: EG4 PASS on all 32 extensions; other verdicts unchanged.
