#!/usr/bin/env python3
"""rule30_zero_runs.py: ZR, the white runs of Rule 30's forced left half after a black cell at depth j (row Q1, drawn
under draw-and-work on 2026-10-07; Local's claim in CLOUD-LOCAL.md at 22:20 BST, predictions pushed before the run).

RUN-ON:     cpu, one core
COMMAND:    python3 tests/probes/lexicon/rule30_zero_runs.py        (ZR, J = 22)
            python3 tests/probes/lexicon/rule30_zero_runs.py zr2    (ZR2, J = 28; below)
            OMP_NUM_THREADS=5 python3 tests/probes/lexicon/rule30_zero_runs.py zr3   (ZR3, J = 36; below; about 85 min)
COST:       half a second at J = 22.

L225 identified Q1's count at hull position j with the zero runs of the forced left half: for T > j, N_(w,j)(T)
counts the right parts whose forced left half is black at depth j and white from j + 1 to T - 1. rule30_zero_runs.c
computes the forced left half f_1 .. f_22 for every right part (cells 0 .. 22) and both phases of column 0 = 0101,
and counts N(j, k) = #{f_j = 1, f_(j+1) = .. = f_(j+k) = 0}. The step ratio N(j, k) / N(j, k - 1) is the k-th white
step after the black cell, exact and width-free once w >= 2(j + k) + 2. k = 0 is L224's rho_j.

PREDICTIONS (Local's, pushed in the claim row before the run; wording kept):
  ZR-C0 (control): k = 0 gives L224's rho_j (the exact fractions for j = 1 .. 9 and the table's four decimals for
         j = 10 .. 22), and j = 3 gives L225's direct count at w = 16 (steps 2944/3328 and 512/2944, then 0).
  ZR-P1 (blind): within k <= 6, at least one step is free (ratio 1) for some j in 2 .. 16, as section 8.52 found at
         finite w.
  ZR-P2 (blind): the geometric mean per step over k = 1 .. 6 lies in 0.35 .. 0.65 for every j in 2 .. 16.
OUTCOME, 2026-10-07 22:35 (M5, one run, 0.5 s; transcript outside Git). ZR-C0 PASS: rho_1 .. rho_9 are L224's
fractions, rho_10 .. rho_22 its decimals, and j = 3 gives L225's 23/26, 4/23, then 0. ZR-P1 HELD: ten steps equal 1,
at (j, k) = (2, 2), (2, 3), (5, 3), (8, 4), (8, 5), (8, 6), (9, 3), (12, 2), (13, 2), (15, 5). ZR-P2 REFUTED, and
not narrowly: at 11 of the 15 depths the white run reaches a step equal to 0 within six cells, so the geometric mean
is 0. After a black cell at depth j the white run never exceeds 4, 2, 0, 3, 3, 2, 4, 2, 2, 3 and 5 cells for j = 2,
3, 4, 5, 6, 7, 10, 11, 12, 13 and 14. (At j = 4, depth 5 is black for every right part.) L225's own count at j = 3
already showed the 0, so this prediction should not have been made as it was. The finding is the reverse of a coin:
the forced left half's white runs are cut off by exact local implications, with steps of exactly 0 and 1 among them.
Because the right part ranges over all cells 0 .. 22, these bounds hold for every configuration, finite or not, whose
leftmost black cell is at -j and whose column 0 follows 0101 for that long.

ZR2 (Local's follow-up; predictions written and pushed before it runs). The same count at J = 28, plus R_real(d), the
longest run of white forced cells starting at depth d over every configuration, compared with section 8.36's
records R(d) (rule30_records.py's list for d = 1 .. 61).
  ZR2-C0 (control): every N(j, k) of the J = 22 run (j <= 16, k <= 6) is reproduced, times 2^6, and rho_23 ..
         rho_26 equal the earlier exact values 8010579/2^24, 18853614/2^25, 31387561/2^26 and 53706918/2^27.
  ZR2-C1 (control, nesting): R_real(d) <= R(d) at every depth whose run ends before depth J. R(d) is a maximum over
         every column 1, and a configuration produces one column 1.
  ZR2-P1 (blind, confidence 0.7): R_real(d) < R(d) at some depth d <= 20. The argument: R(13) = 17 and R(12) = 6,
         so a record witness at 13 has a black cell at depth 12, while ZR finds at most 2 white cells after a black
         cell at depth 12 in any configuration. If this fails, the two definitions differ somewhere, and C1 will say
         where.
OUTCOME of ZR2, 2026-10-07 22:39 (M5, one run, about a minute; transcript outside Git). ZR2-C0 PASS (the J = 22
counts times 2^6, and rho_23 .. rho_26 exactly). ZR2-C1 PASS (R_real(d) <= R(d) wherever the run closes). ZR2-P1
HELD: R_real(d) is below the record at d = 6 and at every depth from 9 to 19, and equal at 1 .. 5, 7 and 8:

    d       1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
    R_real  1  6  5  4  3  3  3  2  8  7  6  5  4  3  5  6  9  8  7
    R(d)    1  6  5  4  3  4  3  2  9  8  7  6 17 16 15 16 15 14 15

From d = 20 the runs reach depth 28 and stay open. The gap itself is not new. Section 8.12 already shows that one
cell of layer between column 0 and a free column 1 tames the adversary, and its "real right halves, up to 12 cells"
row gives 9 from depth 17. That is ZR2's R_real(17) = 9 exactly, from a different program (ladder.c) and a different
population (finite right halves of up to 12 cells, against every right part here). What ZR2 adds is exactness: these
are maxima over every configuration whose column 0 follows 0101 long enough, not over a sample. The prediction's
argument was right, but I made it without first reading section 8.12, which already contained the answer.

ZR3 (Local's, row Q1 drawn again under draw-and-work on 2026-10-08; predictions written and pushed before it runs).
L224 and L240 left open whether rho_j tends to 1/2: from j = 14 to 26 its distance from 1/2 stayed between about
0.02 and 0.06 with no clear decay. ZR3 extends the exact count to J = 36 (rho_j to j = 35) with the same C file, now
parallel under OpenMP (per-thread counts merged at the end; a plain build is unchanged and is the control).
  ZR3-C0 (control): the OpenMP build at J = 28 reproduces the plain build's J = 28 output line for line, and the
         J = 36 run's N(j, k) for j + k <= 28 equal the J = 28 values times 2^8.
  ZR3-C1 (control, a second instrument): R_real(d) for the depths whose run closes by J = 36 agrees with RR's SAT
         values, 15, 11 and 7 at d = 21, 25 and 29 (L247; Cloud's RRX in an independent encoding).
  ZR3-P1 (blind, confidence 0.7): |rho_j - 1/2| >= 0.01 for at least 6 of j = 27 .. 35 (the bias persists).
  ZR3-P2 (blind, confidence 0.5): max over j = 27 .. 35 of |rho_j - 1/2| >= 0.05.
  ZR3-P3 (blind, confidence 0.6): the mean of log2 rho_j over j = 23 .. 35 lies in [-1.15, -0.95] (L224: -1.11 over
         j = 1 .. 12; section 8.52: -1.04 over all right-paid steps).
OUTCOME of ZR3, 2026-10-08 21:11 (M5, one run at commit 78f7025, five threads, 4,260 s): ZR3-C0 PASS (plain and
OpenMP builds identical at J = 28; J = 36 counts equal J = 28 times 2^8). ZR3-C1 PASS: R_real = 15, 11, 7 at d = 21,
25, 29, as RR found by SAT. ZR3-P1 HELD (8 of j = 27 .. 35 at least 0.01 from 1/2), ZR3-P2 HELD (max |rho - 1/2| =
0.0865 at j = 33), ZR3-P3 HELD (mean log2 rho over j = 23 .. 35 = -1.0242). rho_27 .. rho_35 = 0.5500, 0.5092,
0.4855, 0.4700, 0.5276, 0.5722, 0.4135, 0.5241, 0.4674; the distance from 1/2 shows no decay to j = 35. Post-hoc:
the exact R_real(d) for every d <= 29 (all closed at J = 36) agrees with RR2's SAT values at all ten depths
20 .. 29 (16, 15, 14, 13, 12, 11, 10, 9, 8, 7), an independent instrument for that stretch of RR2.
"""
import os
import subprocess
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.environ.get('NP_SCRATCH_ZR', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-zr'))
J, K = 22, 6
# section 8.36's records R(d), d = 1 .. 61 (rule30_records.py's outcome)
R_REC = [1, 6, 5, 4, 3, 4, 3, 2, 9, 8, 7, 6, 17, 16, 15, 16, 15, 14, 15, 14, 17, 16, 19, 20, 19, 18, 17, 16, 19, 20,
         23, 24, 33, 32, 31, 30, 29, 32, 31, 38, 37, 36, 35, 34, 43, 42, 41, 40, 39, 44, 47, 46, 45, 44, 43, 42, 45, 46,
         51, 50, 49]
RHO_23_26 = {23: F(8010579, 1 << 24), 24: F(18853614, 1 << 25), 25: F(31387561, 1 << 26), 26: F(53706918, 1 << 27)}
RHO_EXACT = ['3/4', '3/8', '13/16', '3/32', '11/16', '29/64', '159/256', '163/512', '723/1024']
RHO_TABLE = {10: 0.5430, 11: 0.5452, 12: 0.2366, 13: 0.3965, 14: 0.6149, 15: 0.5137, 16: 0.5704, 17: 0.5671,
             18: 0.4674, 19: 0.4331, 20: 0.4677, 21: 0.4870, 22: 0.5102}


def count(J, K, omp=False, raw=False):
    os.makedirs(SCRATCH, exist_ok=True)
    binary = os.path.join(SCRATCH, 'zr_omp' if omp else 'zr')
    src = os.path.join(HERE, 'rule30_zero_runs.c')
    if omp:
        lib = '/opt/homebrew/opt/libomp'
        subprocess.run(['cc', '-O3', '-Xpreprocessor', '-fopenmp', '-I' + lib + '/include', '-L' + lib + '/lib',
                        '-lomp', '-o', binary, src], check=True)
    else:
        subprocess.run(['cc', '-O3', '-o', binary, src], check=True)
    text = subprocess.run([binary, str(J), str(K)], capture_output=True, text=True, check=True).stdout
    if raw:
        return text
    out = text.split('\n')
    total = int(out[0].split()[1])
    N, R = {}, {}
    for line in out[1:]:
        f = line.split()
        if f and f[0] == 'N':
            N[int(f[1]), int(f[2])] = int(f[3])
        elif f and f[0] == 'R':
            R[int(f[1])] = (int(f[2]), f[3])
    return total, N, R


def zr2():
    t22, n22, _ = count(22, 6)
    total, N, R = count(28, 6)
    c0 = all(N[j, k] == n22[j, k] << 6 for j in range(1, 17) for k in range(K + 1))
    c0 &= all(F(N[j, 0], total) == v for j, v in RHO_23_26.items())
    c1, below = True, []
    for d in range(1, 29):
        L, state = R[d]
        rec = R_REC[d - 1]
        mark = ''
        if state == 'closed':
            c1 &= L <= rec
            if L < rec:
                below.append(d)
                mark = '  below the record'
            elif L > rec:
                mark = '  ABOVE the record'
        print('d %2d  R_real %2d%s  R(d) %2d%s' % (d, L, '+' if state == 'open' else ' ', rec, mark))
    print('ZR2-C0', 'PASS' if c0 else 'FAIL')
    print('ZR2-C1', 'PASS' if c1 else 'FAIL')
    print('ZR2-P1', 'HELD' if any(d <= 20 for d in below) else 'REFUTED', 'depths below the record:', below)


def zr3():
    import math
    import time
    t0 = time.time()
    plain = count(28, 6, raw=True)
    par = count(28, 6, omp=True, raw=True)
    _, n28, _ = count(28, 6, omp=True)
    total, N, R = count(36, 8, omp=True)
    c0 = plain == par and all(N[j, k] == n28[j, k] << 8 for (j, k) in n28 if j + k <= 28)
    rr = {21: 15, 25: 11, 29: 7}
    c1 = all(R[d] == (v, 'closed') for d, v in rr.items())
    rho = {j: N[j, 0] / total for j in range(1, 36)}
    for j in range(23, 36):
        print('j %2d  rho %d/2^%d = %.6f  |rho - 1/2| = %.4f' % (j, N[j, 0], 37, rho[j], abs(rho[j] - 0.5)))
    far = [j for j in range(27, 36) if abs(rho[j] - 0.5) >= 0.01]
    mx = max(abs(rho[j] - 0.5) for j in range(27, 36))
    mean = sum(math.log2(rho[j]) for j in range(23, 36)) / 13
    print('R_real at 21, 25, 29:', [R[d] for d in (21, 25, 29)])
    print('ZR3-C0', 'PASS' if c0 else 'FAIL')
    print('ZR3-C1', 'PASS' if c1 else 'FAIL')
    print('ZR3-P1', 'HELD' if len(far) >= 6 else 'REFUTED', len(far), 'of 9 at least 0.01 from 1/2')
    print('ZR3-P2', 'HELD' if mx >= 0.05 else 'REFUTED', 'max %.4f' % mx)
    print('ZR3-P3', 'HELD' if -1.15 <= mean <= -0.95 else 'REFUTED', 'mean log2 rho over 23 .. 35 = %.4f' % mean)
    print('closed runs:', {d: R[d][0] for d in range(1, 37) if R[d][1] == 'closed'})
    print('%.0f s' % (time.time() - t0))


def main():
    total, N, _ = count(J, K)
    c0 = [str(F(N[j, 0], total)) for j in range(1, 10)] == RHO_EXACT
    c0 &= all(round(N[j, 0] / total, 4) == v for j, v in RHO_TABLE.items())
    c0 &= F(N[3, 1], N[3, 0]) == F(2944, 3328) and F(N[3, 2], N[3, 1]) == F(512, 2944) and N[3, 3] == 0
    free, gm_ok = [], True
    for j in range(1, 17):
        steps = []
        for k in range(1, K + 1):
            steps.append(F(N[j, k], N[j, k - 1]) if N[j, k - 1] else None)
        gm = (N[j, K] / N[j, 0]) ** (1 / K)
        if 2 <= j <= 16:
            free += [(j, k + 1) for k, s in enumerate(steps) if s == 1]
            gm_ok &= 0.35 <= gm <= 0.65
        print('j %2d  rho %.4f  white steps %s  geometric mean %.3f' % (j, N[j, 0] / total, ' '.join(
            '%.4f' % s if s is not None else '  -   ' for s in steps), gm))
    print('steps equal to 1 (j, k):', free)
    print('ZR-C0', 'PASS' if c0 else 'FAIL')
    print('ZR-P1', 'HELD' if free else 'REFUTED')
    print('ZR-P2', 'HELD' if gm_ok else 'REFUTED')


if __name__ == '__main__':
    import sys
    {('zr2',): zr2, ('zr3',): zr3}.get(tuple(sys.argv[1:]), main)()
