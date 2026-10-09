#!/usr/bin/env python3
"""rule30_all_l_future.py: ALF, how much all-L future forces the slab's sites 5 and 6 (GPT's finite-future gate after
L384/GC745). Local's run (chat L387), claimed in CLOUD-LOCAL.md with these predictions pushed before it.

RUN-ON:     cpu (Python 3 and kissat, NL's encoder via rule30_all_l_slab_sat.py); about a minute
COMMAND:    python3 tests/probes/lexicon/rule30_all_l_future.py

For loop k of the word L^K (entrance 111001, closing 1, NL's mode-A cone: any right exterior), ALX's exact query asks
whether sites 5 and 6 at times 10k .. 10k + 9 can differ from the 155-ring's. Here F5(k) and F56(k) are the least future
f = K - k - 1 (the number of L's after loop k) such that the deviation is UNSAT for every K' with K' - k - 1 >= f, up to
K = 18; and "never" if loop k can always deviate. Monotonicity in K is checked, not assumed: a word extends a shorter
one, so UNSAT at K implies UNSAT at every longer K (an extension of a witness would be a witness for the shorter word).

PREDICTIONS (Local's, published before the run):
  ALF-C1 (control): every UNSAT found at some K stays UNSAT at every larger K tried (the monotonicity above).
  ALF-P1 (blind, confidence 0.8): F5(k) and F56(k) are "never" for k = 0, 1 (the start-up loops can always deviate).
  ALF-P2 (blind, confidence 0.55): F56(k) is the same finite number for every k = 3 .. 8, at most 8.
  ALF-D1 (descriptive): the table of F5(k) and F56(k) for k = 0 .. 8.
Counterfactual: F56 growing with k would mean the deviation can be carried along, not that it dies out.
OUTCOME: not yet run.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_all_l_slab_sat as alx                                   # noqa: E402

KMAX = 18
LOOPS = range(0, 9)


def main():
    ref = alx.ring_cols(8)
    table, mono = {}, True
    for k in LOOPS:
        row = {}
        for sites, name in (((5,), 'F5'), ((5, 6), 'F56')):
            verdicts = {}
            for K in range(k + 2, KMAX + 1):
                v, _ = alx.query('L' * K, k, sites, ref)
                verdicts[K] = v
            seen_unsat = False
            for K in sorted(verdicts):
                if verdicts[K] == 'UNSAT':
                    seen_unsat = True
                elif seen_unsat:
                    mono = False
            first = next((K for K in sorted(verdicts) if all(verdicts[K2] == 'UNSAT' for K2 in verdicts if K2 >= K)), None)
            row[name] = (first - k - 1) if first is not None else 'never'
            row[name + '_raw'] = ''.join('U' if verdicts[K] == 'UNSAT' else ('S' if verdicts[K] == 'SAT' else '?')
                                         for K in sorted(verdicts))
        table[k] = row
        print('loop %d: F5 = %s (%s), F56 = %s (%s)' % (k, row['F5'], row['F5_raw'], row['F56'], row['F56_raw']), flush=True)
    print('ALF-C1', 'PASS' if mono else 'FAIL')
    print('ALF-P1', 'HELD' if all(table[k]['F5'] == 'never' and table[k]['F56'] == 'never' for k in (0, 1)) else 'REFUTED')
    f = {table[k]['F56'] for k in range(3, 9)}
    print('ALF-P2', 'HELD' if len(f) == 1 and isinstance(next(iter(f)), int) and next(iter(f)) <= 8 else 'REFUTED', sorted(map(str, f)))
    print('COMPLETE')


if __name__ == '__main__':
    main()
