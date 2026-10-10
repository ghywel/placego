#!/usr/bin/env python3
"""rule30_cloud_rreal_trend.py: TR, is the realizable record R_real(d) bounded, or does it grow? (row Q6; the owner's
steer of 2026-10-10 made "R_real(d) <= C for every d, C about 17" the single target, on Cloud's recommendation.)

RUN-ON:     cpu (Python 3; the deep mode needs python-sat, whose CaDiCaL 1.9.5 it uses; four processes at a time)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_rreal_trend.py trend
            python3 tests/probes/lexicon/rule30_cloud_rreal_trend.py control
            python3 tests/probes/lexicon/rule30_cloud_rreal_trend.py deep [JOBS=4] [CAP=2400]     (resumable)
COST:       trend: instant. control: about 3 minutes. deep: up to 12 calls of at most CAP seconds, JOBS at a time.
            Checkpoint in NP_SCRATCH_TR (default ~/np-scratch/rule30-tr), outside git.

Why. The uniform target assumes R_real(d) stays near 17. §8.44's kick game found that every positive-entropy model of
column 1 has records growing like log2 of its number of histories (the coin law), and the real column 1 has positive
entropy (about 0.08 bits per visible bit, §8.20; at most 0.1236, the channel bound). If the coin law governs the real
records too, R_real(d) grows linearly with a small slope, and the uniform target is false. Two consequences would
follow at once: no finite list of forbidden words can keep relaxed records at or below any C (relaxK >= R_real), and
no certificate of GC970's form with a fixed counter C can exist (it would prove R_real <= C). Period 2 itself needs
only R_real(d) finite for every d, which a linear bound gives (and GC637 turns a linear deadline into Q1).

The query is RR's, unchanged (rule30_records_real_sat.py: cnf and check are imported): is there a configuration whose
column 0 follows 0101 (either phase) for times 0 .. d + L - 1 and whose time-0 cells at depths d .. d + L - 1 are
white? SAT at L means R_real(d) >= L. Every SAT model is checked by direct simulation (rr.check).

Data for the trend: RR2's exact values d = 20 .. 97 (rule30_records_real_sweep.py OUTCOME) and RR3's decided values
d = 98 .. 114 (RECORD-MAP.md, "Records R(d) and R_real(d)"; RR3 checkpoints).

Record searched: `record_find.py R_real defin|longest` -> 6 hits (RR, ZR2, GC549); `record_find.py RR2 R_real|records`
-> 21 hits (RR2's outcome, GC764's capped-maximum scope, RR3); `record_find.py kick game` -> §8.44.

PREDICTIONS for mode trend, written 2026-10-10 07:59 BST before its first run (exploratory: the data were in the record):
  TR-T1: the least-squares slope of R_real on d over d = 30 .. 114 is positive, between 0.04 and 0.10 per depth (the
         coin law with entropy <= 0.1236 bits per visible bit predicts about 0.03 to 0.06).
  TR-T2: block means over 20-depth blocks increase monotonically.
  TR-T3 (counterfactual that must fail): shuffling the values across depths destroys the slope (|slope| < 0.02 for most
         shuffles), so a positive slope is not an artefact of the plateau law's sawtooth.
OUTCOME of mode trend, 2026-10-10 07:59 BST (Cloud's cloud container; instant):
  TR-T1 HELD: slope 0.0853 per depth over d = 30 .. 114 (85 depths); 0.112 over 30 .. 70 and 0.100 over 70 .. 114.
  TR-T2 HELD: block means 8.70 (30 .. 49), 10.85 (50 .. 69), 11.75 (70 .. 89), 14.15 (90 .. 109), 14.20 (110 .. 114).
  TR-T3 as required: no shuffle of 2,000 reaches the observed slope; the median |shuffled slope| is 0.007.
  The running maximum is 8, 9, 11, 12, 14, 14, 16, 17, 17 at d = 30, 40, .., 100, 114.
  Reading (a measurement, not a theorem). The decided records climb at about 0.085 squares per depth, with no sign of
  levelling off. The size agrees with the coin law: the free records grow at 0.826 per depth with 1 bit of freedom per
  visible bit (§8.38), and 0.826 x (0.08 .. 0.1236) = 0.066 .. 0.102 for the real column 1.

PREDICTIONS for modes control and deep, written 2026-10-10 08:05 BST before either ran. One timing test ran first,
about 08:01 to 08:04, outside this script (pysat CaDiCaL: d = 40 SAT at 9 and UNSAT at 10 in about a second each; d = 100 SAT at 15 in
160 s, every witness checked); the control repeats it inside the script.
  TR-C0 (control): d = 40 is SAT at L = 9 and UNSAT at L = 10 (RR2's R_real(40) = 9), and d = 100 is SAT at L = 15
        (RR3's R_real(100) = 15), every witness checked by simulation.
  TR-P4 (blind, 0.65): at least one sampled depth in 121 .. 168 is SAT at L = 18, so R_real(d) >= 18 there, and the
        uniform bound 17 fails.
  TR-P5 (blind, 0.5): the smallest sampled depth found SAT at L = 18 is at most 140.
  TR-P6 (blind, cost, 0.6): every SAT call at L = 18 finishes within CAP = 2400 s here.
  REFUTED-BY: TR-C0 failing (the instrument). TR-P4 is refuted only if every sampled depth is decided UNSAT at 18; a
  capped call is UNKNOWN and refutes nothing.
  Counterfactual. If R_real were bounded near 17, L = 18 would be UNSAT at every sampled depth, and SAT calls would not
  appear; the trend reading would then be a transient, and the uniform target would stand.
ADDENDUM, 2026-10-10 09:15 BST, before the deep run's second start. The first start (08:08, pysat's CaDiCaL) never
  returned: its 2,400 s cap did not fire inside the solver (the interrupt timer is starved while the solver holds the
  interpreter), and all four workers were at 50 minutes with nothing written, so it was killed. The solver is now
  kissat 4.0.4, built from source here as RR3 did, with kissat's own --time cap (3,600 s), and the depths run deepest
  first, where the trend makes SAT at L = 18 likeliest. TR-P6 is read with the 3,600 s cap. The control ran again
  with kissat before the deep calls (its line is in the run log).
ADDENDUM 2, 2026-10-10 10:29 BST, before the third start. Second start: the control passed (d = 100 SAT at 15 in 750 s);
  the first batch, d = 168, 160, 152, 144 at L = 18, all CAPPED at 3,600 s (four unknowns, no verdict); the second
  batch (164, 156, 148, 140) was killed after about 25 minutes rather than spend three more hours on hour caps. Third
  start: only d = 140, 148, 156, 164 (bracketing the trend's crossing of 18, near d = 147), each with a 14,400 s
  cap, four at once, no further depths. TR-P6 is read with the 14,400 s cap. A capped call still refutes nothing.
"""
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, FIRST_COMPLETED, wait

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_records_real_sat as rr
sys.argv = _argv

MODE = sys.argv[1] if len(sys.argv) > 1 else 'trend'
SCRATCH = os.environ.get('NP_SCRATCH_TR', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-tr'))
CK = os.path.join(SCRATCH, 'tr.ck')
RR2 = """20:16 21:15 22:14 23:13 24:12 25:11 26:10 27:9 28:8 29:7 30:8 31:8 32:8 33:8 34:8 35:7 36:7 37:8 38:8 39:9 40:9
41:8 42:9 43:9 44:8 45:9 46:11 47:10 48:11 49:11 50:10 51:9 52:11 53:10 54:10 55:11 56:12 57:11 58:10 59:10 60:9
61:9 62:12 63:11 64:12 65:11 66:10 67:14 68:13 69:12 70:11 71:12 72:11 73:10 74:10 75:10 76:10 77:10 78:11 79:10
80:10 81:12 82:11 83:14 84:13 85:12 86:13 87:16 88:15 89:14 90:13 91:12 92:12 93:16 94:17 95:16 96:15 97:14"""
RR3 = [14, 13, 15, 15, 14, 14, 13, 13, 12, 14, 16, 15, 14, 15, 15, 14, 13]              # d = 98 .. 114
DEEP = [140, 148, 156, 164]           # third start: the bracket of the trend's crossing of 18, long caps (addendum 2)
L_DEEP = 18


def records():
    R = {int(a): int(b) for a, b in (t.split(':') for t in RR2.split())}
    for i, v in enumerate(RR3):
        R[98 + i] = v
    return R


def slope(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def trend():
    import random
    R = records()
    ds = [d for d in sorted(R) if 30 <= d <= 114]
    ys = [R[d] for d in ds]
    s = slope(ds, ys)
    print('TR-T1 slope over d = 30 .. 114: %.4f per depth (%d depths)' % (s, len(ds)))
    for lo, hi in [(30, 70), (70, 114)]:
        xs = [d for d in ds if lo <= d <= hi]
        print('  slope %d .. %d: %.4f' % (lo, hi, slope(xs, [R[d] for d in xs])))
    for lo in range(30, 115, 20):
        blk = [R[d] for d in ds if lo <= d < lo + 20]
        print('TR-T2 block %d .. %d: mean %.2f, max %d' % (lo, min(lo + 19, 114), sum(blk) / len(blk), max(blk)))
    random.seed(1)
    sh = []
    for _ in range(2000):
        y2 = ys[:]
        random.shuffle(y2)
        sh.append(slope(ds, y2))
    print('TR-T3 shuffles reaching the slope: %d of 2000; median |shuffled slope| %.4f'
          % (sum(1 for v in sh if v >= s), sorted(abs(v) for v in sh)[1000]))


KISSAT = os.environ.get('KISSAT', 'kissat')


def solve(d, L, cap):
    """one RR query with kissat under its own wall-clock cap (--time); returns (verdict, witness checked, seconds)"""
    import subprocess
    nv, cl, row, T = rr.cnf(d, L)
    os.makedirs(SCRATCH, exist_ok=True)
    path = os.path.join(SCRATCH, 'tr_%d_%d.cnf' % (d, L))
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(cl)))
        for c in cl:
            f.write(' '.join(map(str, c)) + ' 0\n')
    t0 = time.time()
    r = subprocess.run([KISSAT, '-q', '--time=%d' % cap, path], capture_output=True, text=True)
    secs = time.time() - t0
    os.remove(path)
    if r.returncode == 20:
        return 'UNSAT', None, secs
    if r.returncode != 10:
        return 'CAPPED', None, secs
    val = {}
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            for tok in line[2:].split():
                k = int(tok)
                if k:
                    val[abs(k)] = 1 if k > 0 else 0
    w = [val.get(v, 0) for v in row]
    return 'SAT', rr.check(w, T, d, L), secs


def control():
    ok = True
    for d, L, want in [(40, 9, 'SAT'), (40, 10, 'UNSAT'), (100, 15, 'SAT')]:
        v, wit, secs = solve(d, L, 3600)
        good = v == want and (v != 'SAT' or wit)
        ok = ok and good
        print('TR-C0 d = %d, L = %d: %s%s in %.1f s  %s' % (d, L, v, ' (witness checks)' if wit else '', secs,
                                                            'PASS' if good else 'FAIL'), flush=True)
    print('TR-C0', 'PASS' if ok else 'FAIL')
    return ok


def done():
    out = {}
    if os.path.exists(CK):
        for line in open(CK):
            p = line.split()
            if len(p) >= 6 and p[-1] == 'END':
                out[(int(p[0]), int(p[1]))] = line.strip()
    return out


def deep():
    jobs = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 2400
    os.makedirs(SCRATCH, exist_ok=True)
    have = done()
    todo = [(d, L_DEEP) for d in DEEP if (d, L_DEEP) not in have]
    with ProcessPoolExecutor(max_workers=jobs) as ex:
        live = {ex.submit(solve, d, L, cap): (d, L) for d, L in todo[:jobs]}
        rest = todo[jobs:]
        while live:
            fin, _ = wait(live, return_when=FIRST_COMPLETED)
            for f in fin:
                d, L = live.pop(f)
                v, wit, secs = f.result()
                line = '%d %d %s %s %.1f END' % (d, L, v, wit, secs)
                with open(CK, 'a') as fh:
                    fh.write(line + '\n')
                print(line, flush=True)
                if rest:
                    nd, nL = rest.pop(0)
                    live[ex.submit(solve, nd, nL, cap)] = (nd, nL)
    have = done()
    sat = sorted(d for (d, L), line in have.items() if L == L_DEEP and ' SAT True ' in line)
    print('SAT at L = %d (R_real(d) >= %d): %s' % (L_DEEP, L_DEEP, sat or 'none'))


if __name__ == '__main__':
    {'trend': trend, 'control': control, 'deep': deep}[MODE]()
