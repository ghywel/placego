#!/usr/bin/env python3
"""rule30_kick_strain_long.py: KT2L, the N = 560 half of Cloud's strain question with long caps: the six cases that
KT2 (rule30_kick_strain_kissat.py) found satisfiable at N = 336, each asked at N = 560 with a 4-hour cap. By GC377 a
case unsatisfiable at 336 is unsatisfiable at 560, so these six are the natural first candidates. Claimed in
CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, 3 kissat processes (overnight, beside RK)
COMMAND:    python3 tests/probes/lexicon/rule30_kick_strain_long.py start | status | resume
COST:       4 hours (two waves on 3 cores; the class-42 instances finished in minutes, the others at the cap).

The instances are KT2's (KK's encoding), solved with KT2's solve(); only the cap and the checkpoint file differ, so
a 30-minute UNKNOWN in KT2's checkpoint and a 4-hour answer here never mix.

PREDICTIONS (Local's, published before the run):
  KT2L-C1 (control): every SAT model replays by direct simulation.
  KT2L-P1 (blind, confidence 0.4): at least one of the six instances is SAT within its 4-hour cap.
  If a class-32 and a class-52 instance are both SAT, Cloud's KT-P2 and KT2-P1 hold at N = 560 as well; a SAT
  class-42 instance refutes Cloud's KT-P3 and holds KT2-P2. An UNSAT answer kills only that case, not its class.
OUTCOME, 2026-10-08 04:34 (M5; checkpoint and log outside Git). KT2L-C1 PASS, vacuously (no SAT model came back).
KT2L-P1 REFUTED: no instance is SAT within its 4-hour cap. Class 32 (0, 2), class 32 (0, 4) and class 52 (0, 4) are
UNKNOWN at the cap. Class 42 is UNSAT at N = 560 in all three of its cases, (0, 0), (0, 2) and (0, 4), each within
minutes, though each was SAT at N = 336 (KT2): those cases die between 336 and 560 steps on the wheel. That points to
Cloud's KT-P3 (class 42 dies by 560) against Local's KT2-P2, but three cases are not the class; KT2C
(rule30_kick_class42_560.py) asks all 56 cases with drat-trim certificates.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_strain_kissat as kt2
sys.argv = _argv

kt2.CAP = 14400
kt2.CK = os.path.join(kt2.SCRATCH, 'kt2l.ck')
LOG = os.path.join(kt2.SCRATCH, 'kt2l.log')
TASKS = [(560, 32, 0, 2), (560, 52, 0, 4), (560, 42, 0, 0), (560, 32, 0, 4), (560, 42, 0, 2), (560, 42, 0, 4)]


def run():
    os.makedirs(kt2.SCRATCH, exist_ok=True)
    kt2.batch(TASKS)
    have = kt2.done()
    sat = [t for t in TASKS if have.get(t, ('',))[0] == 'SAT']
    c1 = all(have[t][1] == 'replay-pass' for t in sat)
    print('SAT at 560:', sat)
    print('KT2L-C1', 'PASS' if c1 else 'FAIL')
    print('KT2L-P1', 'HELD' if sat else 'REFUTED')
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(kt2.SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched; checkpoint %s; log %s' % (kt2.CK, LOG))


def status():
    print('%d of %d instances checkpointed' % (len(kt2.done()), len(TASKS)))
    if os.path.exists(LOG):
        print(open(LOG).read()[-1200:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run}[cmd]()
