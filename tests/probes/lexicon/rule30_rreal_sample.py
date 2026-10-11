#!/usr/bin/env python3
"""rule30_rreal_sample.py: lower bounds on R_real(d) by sampling random right halves, with a sample-size curve (SP).

RUN-ON:     cpu (C engine rule30_rreal_sample.c, OpenMP; Python 3 driver, no solver)
COMMAND:    python3 tests/probes/lexicon/rule30_rreal_sample.py control          (T = 180, depths 20 .. 160)
            python3 tests/probes/lexicon/rule30_rreal_sample.py deep T DMIN DMAX ROUNDS [SEED]
COST:       control: about a minute at two threads (2^28 samples a phase). deep at T = 1700: about 25 minutes a phase.

Why (CL260, Cloud's decision on Intel's STRATEGY-PLAN.md section 1): lower bounds on R_real come from sampling, and
SAT hours go to upper bounds only. Intel's sampling (2 x 10^8 random right halves a phase) matched the exact R_real
at 100 of the 101 depths 20 .. 120 and gave R_real(125) >= 21, (133) >= 23, (185) >= 22, (280) >= 26, (435) >= 29,
(657) >= 30, (766) >= 33, (1232) >= 29, (1552) >= 31. This is Local's own instrument for the same thing.

How. Column 0 is clamped to (t + PHASE) mod 2 through T. A sample is a uniformly random right half (sites 1 .. T + 1),
run forward against the clamp for column 1; the forced left half follows sideways, so row 0 is known to depth T and
the clock holds through T. A white run of row 0 at depths d .. d + L - 1 gives R_real(d) >= L (the definition of
rule30_witness_check.py, L596). The engine is bit-sliced (256 samples a batch, round r runs 2^(r-1) batches, so the
cumulative count doubles each round) and prints the best L per depth after every round: the sample-size curve.
Every improvement keeps an explicit witness, and every witness is re-simulated here by rule30_witness_check.check,
a plain one-row Rule 30 loop that shares no code with the engine.

Smoke (2026-10-11 02:18 BST, before the predictions): 4.2 x 10^6 samples a phase, T = 180: all 101 phase-0 witnesses
pass the checker; no depth in 20 .. 120 exceeds the exact value; 83 of 101 equal it; R_real(125) >= 21 already.

PREDICTIONS, registered 2026-10-11 02:20 BST before the control run (2^28 samples a phase, T = 180, depths 20 .. 160):
  SP0 (control, must hold): no sampled bound exceeds the exact R_real at 20 .. 120 (RR2, RR3), nor 17 at 121 .. 124
      (cake_lpr, both phases), nor 17 at 132, 140, 144 (kissat on cake_lpr-verified cuts, L612, L613). An excess is an
      instrument failure or a refutation of a certificate, and stops everything.
  SP1 (control, must hold): every witness written passes rule30_witness_check.check (band, clock).
  SP2 (blind, 0.7): the two phases' maximum equals the exact R_real at >= 97 of the 101 depths 20 .. 120.
  SP3 (blind, 0.5): R_real(133) >= 23 is reproduced (Intel's bound) at 2^28 samples a phase.
  SP4 (blind, 0.5): at 121 .. 160 the bound at 2^28 samples exceeds the bound at 2^22 at half the depths or more (the
      curve is not flat a hundredfold past the smoke).
  Record searched: 'sampl' 'R_real' -> no prior sampling instrument in the record (STRATEGY-PLAN.md is the source).
REFUTED-BY: SP0 or SP1 failing (the instrument); SP2 to SP4 as stated.

OUTCOME, 2026-10-11 02:20 BST (control, 2^28 samples a phase, T = 180, 14 s a phase at two threads):
  SP0 PASS: no excess anywhere; at the certified depths the sampled bounds are 121:15 122:14 123:14 124:15 132:16
      140:15 144:16, all <= 17.
  SP1 PASS: every witness (both phases, depths 20 .. 160) passes rule30_witness_check.check.
  SP2 HELD: 97 of 101 depths equal the exact R_real; short by sampling at 86, 105, 107, 115.
  SP3 REFUTED: R_real(133) >= 18 only (the bound reached 18 at 131,072 samples and never rose); Intel's >= 23 is not
      reproduced, so its witness is wanted for re-simulation (CL260 asked Intel to publish the nine).
  SP4 HELD: 24 of 40 depths in 121 .. 160 rose from 2^22 to 2^28.
  Bounds 121 .. 160: 15 14 14 15 21 20 19 18 19 18 17 16 18 18 19 18 17 16 15 15 18 17 17 16 16 15 17 17 17 16 18
      17 16 17 16 15 15 20 19 18. New beyond SAT: R_real(125) >= 21 (so 126 >= 20, 127 >= 19 by the plateau law),
      129 >= 19, 135 >= 19, 158 >= 20.

PREDICTIONS, registered 2026-10-11 02:21 BST before the deep runs (deep A: T = 330, depths 120 .. 300, 23 rounds,
2^30 samples a phase; deep B: T = 1700, depths 300 .. 1600, 21 rounds, 2^28 samples a phase):
  SP5 (control, must hold): every witness of both runs passes rule30_witness_check.check; deep A agrees with the
      control's bounds at 121 .. 160 or exceeds them (it has 4 times the samples), and stays <= 17 at 121 .. 124, 132,
      140, 144.
  SP6 (blind, 0.5): the sampled R_real(200) >= 19, so the plan's branch "R_real(200) <= 18" is closed by sampling
      alone and the SAT test at 200 is set at one above the sampled bound.
  SP7 (blind, 0.5): Intel's deep bounds (185 >= 22, 280 >= 26, 435 >= 29, 657 >= 30, 766 >= 33, 1232 >= 29,
      1552 >= 31) are reached to within 2 cells at 5 or more of the 7 depths.
  Record searched: 'R_real\(200\)' -> STRATEGY-PLAN.md section 1 only (the pre-registered SAT test).

OUTCOME, deep A (2026-10-11 02:27 BST; T = 330, depths 120 .. 300, 2^30 samples a phase, seeds 11 and 12, 173 s a
phase at two threads):
  SP5 PASS (deep A): every witness valid; every bound at 121 .. 160 equals or exceeds the control's; the certified
      depths stay <= 17 (121:15 122:14 123:14 124:15 132:17 140:16 144:16; 132 now sits at its ceiling).
  SP3, re-read: R_real(133) >= 23 IS reached at 2^30 (phase 0, seed 11; rule30_witness_check VALID, T = 155). The
      control's 18 at 2^28 (seeds 1, 2) was a sample-size effect: the event is rare, not wrong. Intel's bound stands,
      now second-party verified. SP3 stays REFUTED as registered (it named 2^28).
  SP6 REFUTED: R_real(200) >= 16 only (199: 17, 201: 17, 202: 19). The branch "R_real(200) <= 18" stays open, so the
      pre-registered SAT test is live at L = 19.
  Bounds 120 .. 300 (two phases' maximum): 133 >= 23, 185 >= 22 (Intel's, reproduced), 252 >= 24, 279 >= 28,
      280 >= 27 (Intel: 26), 290 >= 26; the full table is in deepA.out (outside git).
  SP7 is scored after deep B.

SAT-200 (registered 2026-10-11 02:28 BST, before its run; STRATEGY-PLAN.md section 1's one pre-registered upper bound,
CL260, CL264): R_real(200) at L = 19, both phases, relax40 (40p1) plus the MFC-verified cuts, CUT at caps that total
two days, launched when the 137 .. 151 sweep leaves cores (CL260). Before it, a focused sampling run (seeds 21, 22) at T = 240, depths
190 .. 210, 2^33 samples a phase. SAT-P1 (blind, 0.55): the focused sampling leaves R_real(200) <= 18 (no sample reaches
19). SAT-P2 (blind, 0.35): CUT returns UNSAT at L = 19 in both phases within the two days, so R_real(200) <= 18 and the
plan's first decision branch fires.
"""
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ompflags import OMP                    # Apple's clang needs libomp's flags
from rule30_witness_check import check

OUT = os.path.join(os.path.expanduser('~'), 'np-scratch-int', 'rule30-sample')
EXE = os.path.join(OUT, 'rreal_sample')
THREADS = os.environ.get('SP_THREADS', '2')
CERT17 = [121, 122, 123, 124, 132, 140, 144]          # R_real <= 17, both phases (L603 .. L613)


def exact():
    """Exact R_real(20 .. 120) as rule30_cloud_rreal_trend.py records it (RR2 strings, RR3 list)."""
    src = open(os.path.join(HERE, 'rule30_cloud_rreal_trend.py')).read()
    rr2 = re.search(r'RR2 = """(.*?)"""', src, re.S).group(1)
    R = {int(a): int(b) for a, b in (t.split(':') for t in rr2.split())}
    rr3 = re.search(r'RR3 = \[(.*?)\]', src, re.S).group(1)
    vals = [int(x) for line in rr3.split('\n') for x in re.findall(r'\d+', line.split('#')[0])]
    assert len(vals) == 23, 'RR3 lists d = 98 .. 120'
    for i, v in enumerate(vals):
        R[98 + i] = v
    assert sorted(R) == list(range(20, 121)), 'exact table must cover 20 .. 120'
    return R


def build():
    os.makedirs(OUT, exist_ok=True)
    subprocess.run(['cc', '-O3', *OMP, '-o', EXE, os.path.join(HERE, 'rule30_rreal_sample.c')], check=True)


def run(ph, T, rounds, seed, dmin, dmax, tag):
    wf = os.path.join(OUT, f'{tag}_w{ph}.txt')
    t0 = time.time()
    out = subprocess.run([EXE, str(ph), str(T), str(rounds), str(seed), str(dmin), str(dmax), wf],
                         check=True, capture_output=True, text=True, env={**os.environ, 'OMP_NUM_THREADS': THREADS}).stdout
    open(os.path.join(OUT, f'{tag}_p{ph}.out'), 'w').write(out)
    curve, cur = [], None
    for line in out.split('\n'):
        if line.startswith('C '):
            cur = (int(line.split()[1]), {})
            curve.append(cur)
        elif line.startswith('R '):
            _, d, L = line.split()
            cur[1][int(d)] = int(L)
    bad = 0
    for line in open(wf):
        _, d, L, p, left, right = line.split()
        band, clock, _v = check(int(d), int(L), int(p), left, right)
        bad += not (band and clock)
    print(f'phase {ph}: {curve[-1][0]:,} samples, {time.time() - t0:.0f} s; witnesses checked, {bad} invalid', flush=True)
    return curve, bad


def control():
    build()
    R = exact()
    c0, b0 = run(0, 180, 21, 1, 20, 160, 'control')
    c1, b1 = run(1, 180, 21, 2, 20, 160, 'control')
    both = lambda k: {d: max(c0[k][1][d], c1[k][1][d]) for d in c0[k][1]}
    s = both(-1)
    over = [d for d in range(20, 121) if s[d] > R[d]] + [d for d in CERT17 if s[d] > 17]
    print(f'SP0 {"PASS" if not over else "FAIL"}  (excess at {over})')
    print(f'SP1 {"PASS" if b0 + b1 == 0 else "FAIL"}  ({b0 + b1} invalid witnesses)')
    eq = sum(s[d] == R[d] for d in range(20, 121))
    print(f'SP2 {"HELD" if eq >= 97 else "REFUTED"}  ({eq} of 101 equal; short at '
          f'{[d for d in range(20, 121) if s[d] < R[d]]})')
    print(f'SP3 {"HELD" if s[133] >= 23 else "REFUTED"}  (R_real(133) >= {s[133]})')
    k22 = next(i for i, (n, _) in enumerate(c0) if n >= 1 << 22)
    s22 = both(k22)
    up = sum(s[d] > s22[d] for d in range(121, 161))
    print(f'SP4 {"HELD" if up >= 20 else "REFUTED"}  ({up} of 40 depths rose from 2^22 to 2^28)')
    print('curve (samples: the two phases\' maximum at 125, 133, 140, 152, 160):')
    for k in range(len(c0)):
        m = both(k)
        print(f'  {c0[k][0]:>12,}: ' + ' '.join(f'{d}:{m[d]}' for d in (125, 133, 140, 152, 160)))
    print('bounds 121 .. 160: ' + ' '.join(f'{d}:{s[d]}' for d in range(121, 161)))


def deep(T, dmin, dmax, rounds, seed=11):
    build()
    c0, b0 = run(0, T, rounds, seed, dmin, dmax, f'deep{T}')
    c1, b1 = run(1, T, rounds, seed + 1, dmin, dmax, f'deep{T}')
    s = {d: max(c0[-1][1][d], c1[-1][1][d]) for d in c0[-1][1]}
    print(f'witnesses: {b0 + b1} invalid')
    print('bounds: ' + ' '.join(f'{d}:{s[d]}' for d in range(dmin, dmax + 1)))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'control'
    if mode == 'control':
        control()
    elif mode == 'deep':
        deep(*map(int, sys.argv[2:7]))               # T DMIN DMAX ROUNDS [SEED, default 11; phase 1 uses SEED + 1]
    else:
        sys.exit('modes: control | deep T DMIN DMAX ROUNDS')
