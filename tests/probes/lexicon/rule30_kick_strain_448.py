#!/usr/bin/env python3
"""rule30_kick_strain_448.py: KT2M, the strain question between 336 and 560 steps on the wheel for the two classes
still open: the three cases of classes 32 and 52 that KT2 found satisfiable at N = 336 and KT2L left UNKNOWN at
N = 560 under 4-hour caps, asked at N = 448 with 4-hour caps on the three cores KT2C freed. Row 6.1 (KS strain);
Cloud's KT-P2 (classes 32 and 52 stay satisfiable at 560). Claimed in CLOUD-LOCAL.md with these predictions pushed
before the run.

RUN-ON:     cpu, 3 kissat processes beside RK and RR2
COMMAND:    python3 tests/probes/lexicon/rule30_kick_strain_448.py start | status | resume
COST:       to be recorded (at most 4 hours: three instances in one wave on 3 cores).

The instances are KT2's (KK's encoding), solved with KT2's solve(); only N, the cap and the checkpoint file differ.
By GC377 a case unsatisfiable at 448 is unsatisfiable at 560, and a case satisfiable at 448 is satisfiable at 336.

PREDICTIONS (Local's, published before the run):
  KT2M-C1 (control): every SAT model replays by direct simulation.
  KT2M-P1 (blind, confidence 0.6): at least one of the three is SAT at N = 448 within its cap.
  KT2M-P2 (blind, confidence 0.7): none of the three is UNSAT at 448 (class 42's 560 UNSATs all came within minutes;
          a quick UNSAT here would be the same signature and would point to death before 560).
OUTCOME, 2026-10-08 19:24 (M5, relaunch of 15:22 at commit 4f7cf4c's instances; 4-hour caps): KT2M-C1 PASS, KT2M-P1
HELD, KT2M-P2 HELD. Class 52 case (0, 4) is SAT at N = 448 (solved by 16:53, model replayed), so class 52 is still
possible after 448 steps on the wheel. Both class-32 cases, (0, 2) and (0, 4), are UNKNOWN at the 4-hour cap. No case
is UNSAT. Class 32 stays known alive only to 336 (KT2). Cloud's CL042 prediction (both alive at 448) holds for 52
and is undecided for 32.
History: first launch 2026-10-08 05:34; the owner's laptop shutdown killed it with nothing recorded.
Its class-52 case had finished at about 07:07 (its instance file was deleted then), but KT2's batch() reported in
submission order, so the answer waited behind the two class-32 cases and was lost. batch() now writes each result
as it finishes. Relaunched from an empty checkpoint at 15:22 with the same tasks, caps and predictions.
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
kt2.CK = os.path.join(kt2.SCRATCH, 'kt2m.ck')
LOG = os.path.join(kt2.SCRATCH, 'kt2m.log')
TASKS = [(448, 32, 0, 2), (448, 32, 0, 4), (448, 52, 0, 4)]


def run():
    os.makedirs(kt2.SCRATCH, exist_ok=True)
    kt2.batch(TASKS)
    have = kt2.done()
    sat = [t for t in TASKS if have.get(t, ('',))[0] == 'SAT']
    uns = [t for t in TASKS if have.get(t, ('',))[0] == 'UNSAT']
    c1 = all(have[t][1] == 'replay-pass' for t in sat)
    print('SAT at 448:', sat, '; UNSAT at 448:', uns)
    print('KT2M-C1', 'PASS' if c1 else 'FAIL')
    print('KT2M-P1', 'HELD' if sat else 'REFUTED')
    print('KT2M-P2', 'HELD' if not uns else 'REFUTED')
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
