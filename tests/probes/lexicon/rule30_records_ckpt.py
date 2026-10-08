#!/usr/bin/env python3
"""rule30_records_ckpt.py: RK, the zero-run record R(93) for column 0 = 0101..., by the resumable search
records_bits_ckpt.c (row Q6, drawn under draw-and-work on 2026-10-07: a heavy run, started in the background, capped
and checkpointed; Local's run, claimed in CLOUD-LOCAL.md with these predictions pushed before it started).

RUN-ON:     cpu, 6 of the M5's 10 cores (the rest stay free for other work); Homebrew libomp
            Moved 2026-10-08 15:37 to a spare machine of the owner's (6 cores, Linux, gcc 14 -O3 -fopenmp build of the
            same C source, in a container), after the owner's laptop shutdown had stopped it at 1,926 tasks (resumed
            on the M5 at 15:22 meanwhile, 1,932 at the move). Validated first: checkpoint lines and R, H and W output
            identical to the M5's at D 53 (1,024 tasks) and D 61 (4,096 tasks); depth-93 tasks 0 .. 5 were held
            back from the moved checkpoint, recomputed there, and match the M5's lines exactly. The status command
            here reads the M5's copy, which stops at 1,932; the live checkpoint is on that machine.
COMMAND:    python3 tests/probes/lexicon/rule30_records_ckpt.py start | status | resume
            (start launches a detached process; resume relaunches it after any interruption; both append to the same
            checkpoint, so no finished task is lost)
COST:       days. R(85) took about 3 hours and R(89) about 14 on 10 cores (§8.37); 93 is about four times 89, so
            roughly 56 hours on 10 cores and 4 days on 6.

Why resumable (draw-and-work: "If the program cannot resume from a checkpoint, making it resumable is the job").
records_bits.c kept every result in memory until the end. records_bits_ckpt.c writes each of its 2^SPLIT tasks to a
checkpoint line as it finishes and skips finished tasks on restart. Validated before this claim (2026-10-07, M5):
identical R and H lines and the same W set as records_bits at depths 53, 61 and 69; at 69, a run stopped by its
deadline at 693 of 4,096 tasks, with a torn half-line appended to imitate a kill mid-write, resumed to COMPLETE with
R, H and all 18 W lines identical, the torn line ignored. The validation found two bugs first (a pass that trusted
any line starting with a task number, and an append that merged into a torn line), fixed before the claim.

PREDICTIONS (Local's, published before the run):
  RK-P1 (the doubling conjecture's test at a new depth): R(93) <= 97, that is d + 4.
  RK-P2 (blind, uncertain): R(93) lies in 71 .. 83 (R(85) = 73, R(89) = 75).
  RK-P3 (blind): R(93) >= R(89) - 3 = 72 (the largest fall in the recorded table over at most four depths is 3,
         from R(53) = 45 to R(56) = 42).
OUTCOME: not yet run.
"""
import os
import subprocess
import sys

D, THREADS, SPLIT = 93, 6, 14
SCRATCH = os.environ.get('NP_SCRATCH', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-rk'))
BIN = os.path.join(SCRATCH, 'records_bits_ckpt')
CK = os.path.join(SCRATCH, 'd%d.ck' % D)
LOG = os.path.join(SCRATCH, 'd%d.log' % D)
HERE = os.path.dirname(os.path.abspath(__file__))


def build():
    omp = '/opt/homebrew/opt/libomp'
    subprocess.run(['cc', '-O3', '-mcpu=apple-m1', '-Xpreprocessor', '-fopenmp', '-I' + omp + '/include',
                    '-L' + omp + '/lib', '-lomp', '-o', BIN, os.path.join(HERE, 'records_bits_ckpt.c')], check=True)


def launch():
    os.makedirs(SCRATCH, exist_ok=True)
    build()
    with open(LOG, 'a') as log:
        subprocess.Popen(['nohup', BIN, str(D), str(THREADS), str(SPLIT), CK], stdout=log, stderr=log,
                         stdin=subprocess.DEVNULL, start_new_session=True)
    print('launched D %d on %d threads, split %d; checkpoint %s; log %s' % (D, THREADS, SPLIT, CK, LOG))


def status():
    n = sum(1 for _ in open(CK)) if os.path.exists(CK) else 0
    print('D %d: %d of %d tasks checkpointed' % (D, n, 1 << SPLIT))
    if os.path.exists(LOG):
        print(open(LOG).read()[-600:])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    {'start': launch, 'resume': launch, 'status': status}[cmd]()
