#!/usr/bin/env python3
"""rule30_silent_sources.py: SS, the exact age-0 classification of silent edge events (row Q6; CL054's ask (a), the
owner's red-object postulate; Local's weigh-in L308). Builds and runs rule30_silent_sources.c. Predictions pushed
before the run.

RUN-ON:     cpu, OpenMP (Homebrew libomp), minutes
COMMAND:    OMP_NUM_THREADS=4 python3 tests/probes/lexicon/rule30_silent_sources.py
COST:       to be recorded (J = 30).

Why age 0 decides "silent for every actual right half". The edge event at time t is read off the configuration at
time t, whose right half is some right half and whose left half is forced by it and by the clock from t on. So E_j is
silent at every time of a given colour exactly when no right half at time 0, in the matching phase, makes it fire:
E_j(0) = f_(j-2) AND NOT f_(j-1), in ZR's forced cells. Silence at white times is phase 0, at black times phase 1. A
source that is silent only on old rows (CL054 observed E14 on evolved right halves) shows up here as firing: that is
age-dependent silence, which GPT's ray argument (GC585) can still use, because the frontier ray reaches depth j at
time j - L - 2. It needs a separate, SAT-based measurement.

PREDICTIONS (Local's, published before the run):
  SS-C1 (control, proved facts): E_2 is silent in both phases (G240); E_1 is silent in phase 1 and fires in phase 0;
        E_4 is silent in phase 0 and E_6 in both phases (CL048's proofs, read by GPT in GC553).
  SS-C2 (control, a second instrument): pooled over the two phases, E_(j+2) is silent exactly where ZR's N(j, 1) is
        0 for j <= 22 (ZR found that only at j = 4, "depth 5 is black whenever depth 4 is").
  SS-P1 (blind, confidence 0.55): E_14 fires in phase 0 at age 0, so CL054's observed white-time silence of E_14 is an
         age effect of evolved right halves, not a property of every right half.
  SS-P2 (blind, confidence 0.5): no (j, phase) with 7 <= j <= 31 is silent at age 0: the age-0 silent set up to
         depth 31 is exactly E_1 black, E_2, E_4 white and E_6.
  D1 (descriptive): the firing fraction of every E_j in each phase, j <= 31.
OUTCOME: not yet run.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.environ.get('NP_SCRATCH_SS', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-ss'))
J = 30


def run_c(J):
    os.makedirs(SCRATCH, exist_ok=True)
    binary = os.path.join(SCRATCH, 'ss')
    lib = '/opt/homebrew/opt/libomp'
    subprocess.run(['cc', '-O3', '-Xpreprocessor', '-fopenmp', '-I' + lib + '/include', '-L' + lib + '/lib', '-lomp',
                    '-o', binary, os.path.join(HERE, 'rule30_silent_sources.c')], check=True)
    out = subprocess.run([binary, str(J)], capture_output=True, text=True, check=True).stdout
    E = {}
    for line in out.split('\n'):
        f = line.split()
        if f and f[0] == 'E':
            E[int(f[1]), int(f[2])] = int(f[3])
    return E


def zr_n1(Jz):
    sys.path.insert(0, HERE)
    import rule30_zero_runs as zr
    _, N, _ = zr.count(Jz, 1)
    return N


def main():
    E = run_c(J)
    total = 1 << J                                         # right parts per phase: cells 1 .. J free
    silent = sorted((j, ph) for (j, ph), n in E.items() if n == 0)
    c1 = all(E[j, ph] == 0 for j, ph in ((2, 0), (2, 1), (1, 1), (4, 0), (6, 0), (6, 1))) and E[1, 0] > 0
    N = zr_n1(22)
    c2 = all(((E[j + 2, 0] + E[j + 2, 1]) == 0) == (N[j, 1] == 0) for j in range(1, 22))
    print('silent at age 0 (j, phase):', silent)
    for j in range(1, J + 2):
        print('E_%-2d  phase 0 %.5f  phase 1 %.5f' % (j, E[j, 0] / total, E[j, 1] / total))
    print('SS-C1', 'PASS' if c1 else 'FAIL')
    print('SS-C2', 'PASS' if c2 else 'FAIL')
    print('SS-P1', 'HELD' if E[14, 0] > 0 else 'REFUTED', 'E_14 phase 0 count', E[14, 0])
    extra = [(j, ph) for j, ph in silent if 7 <= j <= 31]
    print('SS-P2', 'HELD' if not extra else 'REFUTED', 'silent pairs with 7 <= j <= 31:', extra)


if __name__ == '__main__':
    main()
