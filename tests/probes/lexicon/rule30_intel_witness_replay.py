#!/usr/bin/env python3
"""rule30_intel_witness_replay.py: second-party re-simulation of Intel's sixteen sampled R_real witnesses (IW).

RUN-ON:     cpu (pure Python 3, no solver); under a minute
COMMAND:    python3 tests/probes/lexicon/rule30_intel_witness_replay.py [tests/probes/lexicon/rule30_intel_witnesses.txt]

Why (CL260, CL264, CL265, IN003): STRATEGY-PLAN.md's sampled lower bounds are Intel-verified, third-party, until a
second party re-simulates the witnesses. Local's own sampling (SP, L617 .. L619) reproduced 125, 133, 185, 252, 279,
280, 290 and 435, 766, but not 1232 >= 29 or 1552 >= 31 (25 each at 2^28 samples a phase).

How. Each block of rule30_intel_witnesses.txt gives d, phase, L and a right half (sites 1 .. n). The forced left half is
built here, independently of every other engine: column 1 by a plain forward run of the right half beside the clamped
wall, then the sideways recursion x_t(-k) = x_{t+1}(-k+1) XOR (x_t(-k+1) OR x_t(-k+2)) for k = 1 .. d + L - 1. The
configuration then goes to rule30_witness_check.check, a plain one-row Rule 30 loop, which tests the band (row 0
white at depths d .. d + L - 1) and the clock (column 0 = (t + phase) mod 2 for t = 0 .. d + L - 1). A wrong left half
fails the clock there, so the checker is the arbiter.

PREDICTIONS, registered 2026-10-11 03:33 BST before the run:
  IW0 (control, must hold): Local's own phase-0 depth-133 witness from SP's deep A (rebuilt here from its right half
      alone) passes the same pipeline.
  IW1 (blind, 0.85): all sixteen of Intel's witnesses pass, including 1232 >= 29 and 1552 >= 31.
  Record searched: 'rule30_intel_witnesses' -> IN003 only.
REFUTED-BY: IW0 failing (the pipeline); IW1 as stated.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rule30_witness_check import check

DEFAULT = os.path.join(HERE, 'rule30_intel_witnesses.txt')
SP_W = os.path.join(os.path.expanduser('~'), 'np-scratch-int', 'rule30-sample', 'deep330_w0.txt')


def forced_left(right, ph, T):
    """Cells -T .. 0 at time 0 (a string, as the checker takes it) from the right half and the clamp."""
    W = len(right)
    row = [int(b) for b in right] + [0] * 4                  # row[i - 1] = x_t(i), i = 1 .. W
    col1 = []
    for t in range(T + 1):
        col1.append(row[0])
        wall = (t + ph) % 2
        row = [(wall if i == 0 else row[i - 1]) ^ (row[i] | row[i + 1]) for i in range(len(row) - 1)] + [0]
    a_prev2 = col1                                          # a_{-1}(t) = x_t(1)
    a_prev = [(t + ph) % 2 for t in range(T + 1)]           # a_0(t) = x_t(0)
    cells = [a_prev[0]]
    for k in range(1, T + 1):
        a = [a_prev[t + 1] ^ (a_prev[t] | a_prev2[t]) for t in range(T + 1 - k)]
        cells.append(a[0])
        a_prev2, a_prev = a_prev, a
    return ''.join(str(cells[k]) for k in range(T, -1, -1))


def blocks(path):
    text = open(path).read()
    for m in re.finditer(r'^d=(\d+) phase=([01]) L=(\d+) T=(\d+) cells=(\d+) verified=\w+\n((?:[01]+\n?)+)', text, re.M):
        d, ph, L, T, n = (int(m.group(i)) for i in range(1, 6))
        right = m.group(6).replace('\n', '')
        assert len(right) == n, (d, len(right), n)
        yield d, ph, L, T, right


def replay(d, ph, L, right):
    T = d + L - 1
    left = forced_left(right[:T + 1], ph, T)
    band, clock, _ = check(d, L, ph, left, right)
    return band and clock


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    ok0 = None
    if os.path.exists(SP_W):
        for line in open(SP_W):
            _, d, L, p, left, right = line.split()
            if int(d) == 133:
                ok0 = replay(133, int(p), int(L), right)
                print(f'IW0 {"PASS" if ok0 else "FAIL"}  (SP deep A, d = 133, L = {L}, phase {p})')
    if ok0 is None:
        print('IW0 NOT RUN  (SP deep A witness file absent)')
    res = []
    for d, ph, L, T, right in blocks(path):
        assert T == d + L, 'the file states T = d + L'
        v = replay(d, ph, L, right)
        res.append((d, ph, L, v))
        print(f'  d = {d:4d} phase {ph} L = {L}: {"VALID" if v else "NOT VALID"}', flush=True)
    good = sum(v for *_, v in res)
    print(f'IW1 {"HELD" if res and good == len(res) == 16 else "REFUTED"}  ({good} of {len(res)} valid)')


if __name__ == '__main__':
    main()
