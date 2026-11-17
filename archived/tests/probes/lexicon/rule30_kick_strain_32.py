#!/usr/bin/env python3
"""rule30_kick_strain_32.py: KT2N, class 32's strain between 336 and 448 steps on the wheel, with longer caps (row 6.1, KS
strain; the open half of Cloud's CL042 alternation prediction after KT2M left both class-32 cases UNKNOWN at 448 under
4-hour caps). Local's run, claimed in CLOUD-LOCAL.md with these predictions pushed before it.

RUN-ON:     cpu, 4 kissat processes beside RV3 and RR2
COMMAND:    python3 tests/probes/lexicon/rule30_kick_strain_32.py start | status | resume
COST:       to be recorded (at most 12 hours: four instances in one wave).

The instances are KT2's (KK's encoding, kt2.solve(), which replays every SAT model); only N, the cap and the checkpoint
differ. The two cases are the ones KT2 found SAT at N = 336; KT2 stopped at its first wave, so the other 53 class-32
cases were never tested. A SAT here shows class 32 alive at N; two non-SAT answers would not show it dead. By GC377 a
case SAT at N is SAT at every smaller N. Results are written as each finishes.

PREDICTIONS (Local's, published before the run):
  KT2N-C1 (control): every SAT model replays by direct simulation.
  KT2N-P1 (blind, confidence 0.6): at least one case is SAT at N = 392.
  KT2N-P2 (blind, confidence 0.5): at least one case is SAT at N = 448 within the 12-hour cap (Cloud's CL042 says
          alive; KT2M's 4-hour caps did not decide it).
  KT2N-P3 (blind, confidence 0.7): no case is UNSAT at 392.
OUTCOME, 2026-10-09 08:11 BST (M5; restarted from its checkpoint after the NVMe drop of 2026-10-08, the wave resumed
  on the internal disk; N = 392 decided 21:32 and 21:57, N = 448 at 06:12 and 08:11, each inside the 12-hour cap):
  KT2N-C1 PASS: all four models replay by direct simulation.
  KT2N-P1 HELD and KT2N-P3 HELD: both cases are SAT at N = 392.
  KT2N-P2 HELD: both cases, (0, 2) and (0, 4), are SAT at N = 448, so class 32 is alive at 448 (by GC377 at every
  N <= 448). Cloud's CL042 alternation reading survives: class 42 dead by 560 (KT2C), classes 32 and 52 alive at 448.
  Nothing is decided above 448 for class 32; KT2L's 4-hour caps left it UNKNOWN at 560.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_strain_kissat as kt2
sys.argv = _argv

kt2.CAP = 43200
kt2.JOBS = 4
kt2.CK = os.path.join(kt2.SCRATCH, 'kt2n.ck')
LOG = os.path.join(kt2.SCRATCH, 'kt2n.log')
TASKS = [(392, 32, 0, 2), (392, 32, 0, 4), (448, 32, 0, 2), (448, 32, 0, 4)]


def run():
    os.makedirs(kt2.SCRATCH, exist_ok=True)
    kt2.batch(TASKS)
    have = kt2.done()
    v = {t: have.get(t, ('', ''))[0] for t in TASKS}
    sat = [t for t in TASKS if v[t] == 'SAT']
    c1 = all(have[t][1] == 'replay-pass' for t in sat)
    print('verdicts:', v)
    print('KT2N-C1', 'PASS' if c1 else 'FAIL')
    print('KT2N-P1', 'HELD' if any(t[0] == 392 for t in sat) else 'REFUTED')
    print('KT2N-P2', 'HELD' if any(t[0] == 448 for t in sat) else 'REFUTED')
    print('KT2N-P3', 'HELD' if not any(t[0] == 392 and v[t] == 'UNSAT' for t in TASKS) else 'REFUTED')
    print('COMPLETE', flush=True)


def launch():
    os.makedirs(kt2.SCRATCH, exist_ok=True)
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', sys.executable, os.path.abspath(__file__), 'run'], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched; checkpoint %s; log %s' % (kt2.CK, LOG))


def status():
    print('%d of %d instances checkpointed' % (len([t for t in kt2.done() if t in TASKS]), len(TASKS)))
    if os.path.exists(LOG):
        print(open(LOG).read()[-1200:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status, 'run': run}[cmd]()
