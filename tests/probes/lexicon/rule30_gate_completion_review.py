#!/usr/bin/env python3
"""rule30_gate_completion_review.py: RP, Local's reproduction of GC395 (GPT's finite completion census of the class-12
tail, rule30_gpt_gate_completion.py), asked for in GPT's review flag of 2026-10-07. Claimed in CLOUD-LOCAL.md with
these predictions pushed before the run.

RUN-ON:     cpu, one core; kissat for the witness (seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_gate_completion_review.py
COST:       to be recorded.

What differs from GPT's census. GPT builds its targets from the locked words and L240's reported difference sets.
This review re-solves GW's witness (rule30_class12_gate_check.py; the same CNF, so kissat returns the same model,
checked by its difference sets) and takes every target cell from the model itself. Its rows are integers in the
reverse bit order (column x at bit 20 - x), stepped by one shift-and-OR expression. The census: columns 0 .. 6 at
offset -14 are the witness's, columns 7 .. 19 range over all 8,192 values, column 0 then follows the wall, and a
candidate completes when columns 1 .. 5 match the witness at every offset from -14 to -1.

PREDICTIONS (Local's, published before the run; they are GC395's reported outcome, to be reproduced):
  RP-C0 (control): the re-solved witness has L240's difference sets, so it is GW's model.
  RP-C1 (control): GPT's reconstructed targets (locked words plus reported differences) equal the witness's actual
        cells for columns 1 .. 6 at every offset from -14 to -1.
  RP-P1 (reproduction): exactly 672 of the 8,192 candidates complete, every one with the same column-6 history,
        the witness's own, and column 6 at offset -6 is 0.
OUTCOME: not yet run.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_class12_gate_check as gw
import rule30_kick_bite_kissat as kk
sys.argv = _argv
import rule30_locked_core_review as rv
import rule30_locked_core_lock as lk

L240 = {1: [], 2: [1], 3: [2, 4], 4: [1, 3, 5], 5: [2, 3, 4, 6, 8, 10], 6: [1, 2, 3, 6, 7, 9, 11, 13]}
B = 20


def main():
    t0, d, a, N = 0, 2, 12, 126
    bits, s, E = gw.witness(t0, d, a, N)
    cols = gw.columns(t0, bits, E, width=20)
    src, dst, n = rv.graph(15, rv.wheel())
    alive, _ = rv.trim(src, dst, n)
    words = lk.words(alive, 15, (2, 3, 4, 5, 6))
    ref = lambda x, t: kk.U[(t - d) % kk.P] if x == 1 else int(words[x][(t - d) % kk.P])
    diffs = {x: sorted(s - t for t in range(s - 56, s) if cols[t][x] != ref(x, t)) for x in range(1, 7)}
    c0 = diffs == L240
    gpt = lambda x, k: ref(x, s + k) ^ (-k in L240[x])
    c1 = all(cols[s + k][x] == gpt(x, k) for x in range(1, 7) for k in range(-14, 0))
    start = s - 14
    base = sum(cols[start][x] << (B - x) for x in range(0, 7))
    want = {k: [cols[s + k][x] for x in range(1, 6)] for k in range(-14, 0)}
    own6 = tuple(cols[s + k][6] for k in range(-14, 0))
    complete, hist = 0, set()
    for seed in range(1 << 13):
        row = base | sum(((seed >> (x - 7)) & 1) << (B - x) for x in range(7, 20))
        h6, ok = [], True
        for k in range(-14, 0):
            if [(row >> (B - x)) & 1 for x in range(1, 6)] != want[k]:
                ok = False
                break
            h6.append((row >> (B - 6)) & 1)
            nxt = (row >> 1) ^ (row | (row << 1))
            nxt &= (1 << (B + 1)) - 1
            wall = (s + k + 1) % 2                     # column 0 at the next row is the wall, t mod 2
            row = (nxt & ~(1 << B)) | (wall << B)
        if ok:
            complete += 1
            hist.add(tuple(h6))
    p1 = complete == 672 and hist == {own6} and own6[8] == 0
    print('witness s = %d; difference sets %s' % (s, diffs))
    print('completions %d of 8192; distinct column-6 histories %d; the witness\'s own among them: %s; value at -6: %s'
          % (complete, len(hist), own6 in hist, sorted({h[8] for h in hist})))
    print('RP-C0', 'PASS' if c0 else 'FAIL')
    print('RP-C1', 'PASS' if c1 else 'FAIL')
    print('RP-P1', 'HELD' if p1 else 'REFUTED')


if __name__ == '__main__':
    main()
