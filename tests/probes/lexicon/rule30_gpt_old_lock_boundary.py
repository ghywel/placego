#!/usr/bin/env python3
"""OLD1: GC584's old-side observation boundary, preregistered in GC587.
RUN-ON: GPT CPU, Python standard library; one bounded proof-certificate audit.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_old_lock_boundary.py
COST: estimated under 30 CPU seconds; stop at 45 CPU seconds or 256 MiB RSS.
Reuses KL's advance and packed local rule: not an independent automaton.
No trajectory, SAT, random ensemble, or actual-right-side realizability claim.

PREDICTIONS BEFORE RUN:
OLD-C1: all phase-aligned 56-transition state sets are subsets of the 55 sets;
        the 56-transition kick table has classes 2,12,22,32,39,42,49,52.
OLD-C2: packed step agrees with independent decimal Rule 30 triples at m=4,5,
        every hidden state, both wall/companion/input bits.
OLD-CF (known-wrong variant must fail): one old observation and one matched
        old transition impose identical history constraints. Initial wall=0,
        companion=0, hidden site 2=1 satisfies the former but violates the latter.
OLD-P1 (blind): class 39's phase kick -9 survives the 55-transition projection.
OLD-P2 (blind): the 55- and 56-transition kick tables coincide.
UNEXPECTED OLD-U: report state-set differences even if kick tables coincide;
        equal output alphabets must not be reported as equal hidden histories.
REFUTED-BY: any control failure, cap, or contrary blind outcome is retained.
OUTCOME: NOT RUN. Publish this header before executing once in the next block.
"""
import json
import resource
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rule30_kick_layers as kl


def main():
    start = time.process_time()

    def guard():
        # macOS reports bytes for ru_maxrss; this audit is assigned to that host.
        if time.process_time() - start > 45:
            raise RuntimeError('CAP: 45 CPU seconds')
        if sys.platform == 'darwin' and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 256 * 1024**2:
            raise RuntimeError('CAP: 256 MiB RSS')

    for m in (4, 5):
        for h in range(1 << (m-1)):
            for wall in (0, 1):
                for c1 in (0, 1):
                    for inp in (0, 1):
                        cells = [wall, c1] + [(h >> b) & 1 for b in range(m-1)] + [inp]
                        bits = []
                        for site in range(1, m+1):
                            a, b, c = cells[site-1:site+2]
                            bits.append((30 >> (4*a + 2*b + c)) & 1)
                        want = (sum(bits[site] << (site-1) for site in range(1, m)), bits[0])
                        assert kl.step_row(h, wall, m, inp, c1) == want
    assert kl.U[0] == kl.U[1] == 0
    # Direct local control, not a comparison of endpoint state-set cardinalities.
    assert kl.step_row(1, 0, 4, 0, 0)[1] == 1
    print('OLD-C2 PASS; OLD-CF rejected', flush=True)

    m = 16
    sets = {n: [set() for _ in range(56)] for n in (55, 56)}
    # One traversal per start, snapshot both lengths at their own terminal phase.
    for phase in range(56):
        current = set(range(1 << (m-1)))
        for offset in range(56):
            t = (phase + offset) % 56
            current = kl.advance(current, t, m, kl.U[t], kl.U[(t+1) % 56], kl.step_row)
            count = offset + 1
            if count in sets:
                sets[count][(phase+count) % 56] |= current
            guard()
    assert all(b <= a for a, b in zip(sets[55], sets[56]))
    difference = [len(a-b) for a, b in zip(sets[55], sets[56])]
    kl.F = 20  # 21 new observations including departure, a necessary projection.
    tables = {}
    for count in (55, 56):
        tables[count] = kl.kicks_from(sets[count], m, kl.step_row)
        guard()
    assert sorted(tables[56]) == [2, 12, 22, 32, 39, 42, 49, 52]
    assert all(set(v) <= set(tables[55].get(a, [])) for a, v in tables[56].items())
    print(json.dumps(dict(controls='PASS', old_transitions=tables,
                         target_39_minus9_survives=-9 in tables[55].get(39, []),
                         tables_coincide=tables[55] == tables[56],
                         unexpected_state_differences=difference,
                         cpu_seconds=time.process_time()-start), sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
