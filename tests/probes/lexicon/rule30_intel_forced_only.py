#!/usr/bin/env python3
"""rule30_intel_forced_only.py: FO, the forced-only records R^F(d) of the check-free conjecture, exact, both phases
(RULE30-PRIZE.md 8.88; STRATEGY-PLAN.md section 1, the first week's first item; decided in CL260 and CL263).

RUN-ON:     the Intel MacBook (16 logical cores); C with OpenMP (forced_only_x4.c beside this file)
COMMAND:    python3 tests/probes/lexicon/rule30_intel_forced_only.py build
            python3 tests/probes/lexicon/rule30_intel_forced_only.py calib
            python3 tests/probes/lexicon/rule30_intel_forced_only.py run LANG PHASE MAXM [MAXSTATES [DFSMAX]]
            (LANG x4|gm|maw12|dfa=FILE; MAXM is the last merged level; DFSMAX extends depth-first without merging)
COST:       calib about a minute. The merged stage is bounded by memory, not time: the engine merges states on the
            record's masked anti-diagonal pair (8.38) and stops before a level whose children would exceed MAXSTATES
            (default 3e7, about 5 GB); the depth-first tail past it costs about 1.5 x per level of CPU time (X_4 from
            level 97 to 121: hours at 16 threads). Logs in NP_SCRATCH_FO (default ~/np-scratch/rule30-fo), outside git.

The object (8.88). Beside the alternating wall the forced left half is a function of the visible bits. In phase 0
(column 0 reads t mod 2) the newest visible bit v_k decides row 0's depth 2k+1 as a plain XOR (the forced cell) and
depth 2k+2 as a check; in phase 1 the parities swap and depth 1 is black. The forced-only orbit of a prefix takes the
whitening bit at every forced depth, ignores the checks, and dies when that bit leaves the language K. R^F_K(d) is the
longest run of depths from d on with every forced cell white, over the prefixes in K. The check-free conjecture: over
K = X_4 = {no 11, no 00000}, which contains the real language in both phases, no orbit lives for ever; R^F finite at
every d for X_4 (or for any language containing L) implies period 2 for every finite configuration.

Engine. Breadth-first over visible prefixes, one level per forced index m (two anti-diagonals apart). A state is the
pair (A_m, A_{m-1} masked where A_m's next bit is black) plus the last twelve visible bits, merged with the longest
streak of white forced cells ending at m kept (8.38's MG0b: equal masked pairs have equal futures). From every state
the forced-only path is run to its death (or a cap of 3m + 300 anti-diagonal steps, which marks the depth censored),
and R^F(d) is updated for every d whose run that path and the streak cover. Each level prints its distinct-state
count, so the merge rate of K-prefixes is a by-product.

Record searched: `record_find.py 'forced-only|check-free'` -> 8.88 (the object, Cloud's replication of the depth
1..16 values), STRATEGY-PLAN.md, IN002; `record_find.py 'masked pair|MG0b'` -> 8.38 (the merging rule and the count
2^(0.41 d) of distinct walks for free prefixes); `record_find.py 'no 11.*00000'` -> 8.88 only.

PREDICTIONS, written before the registered runs (the engine was smoke-tested on depths to 22 against the Python
values of 8.88 before this header was pushed; those are the calibration numbers below, not new runs):
  FO-P0 (control, must hold): calib reproduces R^F(1..9) = 2 17 16 15 14 13 12 11 10 (phase 0) and R^F(1..16) =
         9 8 7 6 5 4 7 6 15 14 17 16 15 14 23 22 (phase 1) over X_4; merging on and off give identical R^F(d) for
         every d <= 42 in both phases (the mask is exact); the golden-mean control (gm, phase 1) is censored at every
         depth (the all-zero sequence keeps the forced cells white for ever there).
  FO-P1 (control, third-party number): phase 0, X_4: R^F(60) = 94 (door D2 and its skeptic: from depth 60 the best
         orbit reaches depth 154).
  FO-P2 (blind): the distinct-state count per level grows like 2^(c k) in the number k of visible bits, with c between
         0.40 and 0.55 over levels k = 20..40 in phase 0 (X_4 words grow at 0.617 per bit; merging cuts the exponent).
  FO-P3 (blind, 0.6): the least-squares slope of R^F_{X_4}(d) over d = 40..(deepest exact depth) lies in 1.3..1.9 in
         both phases (judge B's heuristic 1.6 d); the smoke test's R^F(20) = 53 in phase 0 (2.65 d) says the early
         ratio is higher, so no absolute bound is predicted.
  FO-P4 (blind, 0.8): no forced-only orbit from any state at any depth reached survives to the cap in X_4: the
         conjecture's kill does not fire; every death is at 11 or at 00000.
  FO-P5 (blind, 0.6): the twelve-word class (maw12) has R^F(d) <= R^F_{X_4}(d) at every d, strictly smaller at most
         d >= 30, and a smaller slope over 40..reached.
  FO-P6 (blind, 0.5): with MAXSTATES = 3e7 the phase-0 X_4 run reaches an exact depth of at least 90.
  Counterfactual that must fail: the gm control of FO-P0 (an engine reporting it finite is broken), and FO-P0's
  merging-off equality (a mask that hides a live bit would show a difference by depth 42).
  REFUTED-BY: FO-P0 failing refutes the instrument, not the conjecture; a surviving orbit at the cap refutes FO-P4 and
  is reported with its prefix, as the plan's kill criterion requires (it moves the conjecture to the width-8 language).
  Unexpected check: at which forbidden word the orbits die, by level (11 against 00000), and whether that ratio moves
  with depth. Not predicted.

OUTCOME, first block (2026-10-11 03:28 BST): the merged stage of X_4 and the full twelve-word class, both phases, on
  16 threads.
  The depth-first tail of X_4 to depth 121 and the width-8 and width-12 layer languages are running; ADDENDUM below.
  FO-P0 HELD: R^F(1..9) and R^F(1..16) equal 8.88's in both phases; merging on and off give identical records to
         depth 42 in both phases; the golden-mean control is censored at every depth 1..20 in phase 1.
  FO-P1 HELD: phase 0 R^F(60) = 95, the run covering depths 60..154 inclusive (D2's "reaches depth 154").
  FO-P2 REFUTED as worded, held later: merged states grow as 2^(0.386) per visible bit over levels 21..41 (phase 1:
         0.413), below the band, then 0.519 over 41..61 and 0.516 over 61..91 (phase 1: 0.519, 0.516); the ratio per
         level settles at 1.429. X_4's words grow at 0.617 per bit, so merging removes 0.10 bit per visible bit, as it
         removes 0.09 in the free case (0.5 -> 0.41, 8.38).
  FO-P3 HELD in phase 0 (least-squares slope 1.451 over d = 40..92), REFUTED in phase 1 (1.215 over 40..93); R^F/d
         is 1.58, 1.51, 1.42 at d = 60, 80, 92 (phase 0) and 1.27, 1.35, 1.41 at 60, 80, 93 (phase 1).
  FO-P4 HELD at every depth reached: no path reached the cap (3m + 300). The kill did not fire.
  FO-P5 HELD: the twelve-word class is <= X_4 at every common depth and strictly smaller at every depth 30..92
         (phase 0) and 30..93 (phase 1); its slopes are 0.660 (phase 0, d = 40..122) and 0.346 (phase 1, 40..121).
  FO-P6 HELD: X_4 exact to depth 92 (phase 0) and 93 (phase 1) at the 3 x 10^7-state cap (17.7 and 21.2 million
         merged states at the last level); the twelve-word class is exact to 122 and 121 with 4.4 and 3.9 million
         states at the top (growth 2^0.333 per bit). Every merged run took under 25 s; the twelve-word class 6 s.
  Counterfactual: as required (the golden-mean control is infinite; merging on and off agree).
  Exact tables and one witness prefix per depth: rule30_intel_forced_only.txt beside this file.
  Unexpected check: the death word. In X_4, 85% of the forced-only orbits die by producing 11 (phase 0: 49,904,154
         against 9,009,169 at 00000; phase 1: 59,657,063 against 10,775,372); in the twelve-word class about half die
         at 11 (10,322,441 against 11,229,032; phase 1: 9,204,499 against 10,006,972). Not predicted; the plan's
         expectation (judge B) was deaths at 00000.
  Reading (MEASURED, these depths): R^F over X_4 grows at about 1.4 d where the real record grows at 0.08 d and the
         free record at 0.83 d, so the check-free relaxation is loose by a factor of about 17 in slope and finite at
         every depth computed; the twelve shortest absent words cut the forced-only slope to 0.66 and 0.35, so the
         longer absent words, not the two of X_4, do most of the killing. The record prefixes at the top depths begin
         with alternating runs (0101.. or 1010.., the wheel's two-gap train) followed by sparse 1s.

ADDENDUM: (the depth-first tail of X_4 to 121 and the width-8 and width-12 layers, with their verdicts)
"""
import os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'forced_only_x4.c')
SCRATCH = os.environ.get('NP_SCRATCH_FO', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-fo'))
BIN = os.path.join(SCRATCH, 'forced_only_x4')
OMP = ['-Xpreprocessor', '-fopenmp', '-I/usr/local/opt/libomp/include', '-L/usr/local/opt/libomp/lib', '-lomp'] \
    if sys.platform == 'darwin' else ['-fopenmp']

EXPECT = {0: [2, 17, 16, 15, 14, 13, 12, 11, 10], 1: [9, 8, 7, 6, 5, 4, 7, 6, 15, 14, 17, 16, 15, 14, 23, 22]}


def build():
    os.makedirs(SCRATCH, exist_ok=True)
    subprocess.run(['cc', '-O2', *OMP, SRC, '-o', BIN], check=True)
    print('built', BIN)


def run(lang, phase, maxm, maxstates='30000000', nodedup=0, threads=None, tag=None, dfsmax=0):
    os.makedirs(SCRATCH, exist_ok=True)
    env = dict(os.environ)
    if threads: env['OMP_NUM_THREADS'] = str(threads)
    tag = tag or f"{lang.replace('dfa=', '').replace('/', '_')}_p{phase}_m{maxm}" + ('_nodedup' if nodedup else '') + (f'_dfs{dfsmax}' if dfsmax else '')
    log = os.path.join(SCRATCH, tag + '.log')
    t0 = time.time()
    with open(log, 'w') as fh:
        subprocess.run([BIN, str(phase), lang, str(maxm), str(maxstates), str(nodedup), str(dfsmax)], stdout=fh, check=True, env=env)
    R, cens, wit, levels, kinds = {}, {}, {}, [], []
    for line in open(log):
        p = line.split()
        if not p: continue
        if p[0] == 'D': R[int(p[1])] = int(p[2]); cens[int(p[1])] = int(p[3]); wit[int(p[1])] = p[4] if len(p) > 4 else ''
        elif p[0] == 'L': levels.append((int(p[1]), int(p[2]), int(p[3]), float(p[4])))
        elif p[0] == 'K': kinds.append((int(p[1]), int(p[2]), int(p[3]), int(p[4])))
    exact = [d for d in R if not cens.get(d, 0)]
    print(f'{tag}: {time.time() - t0:.0f} s; exact to depth {max(exact) if exact else 0}; censored depths {sum(cens.values())}; log {log}')
    return R, cens, wit, levels, kinds


def calib():
    ok = True
    for phase in (0, 1):
        R, cens, _, _, _ = run('x4', phase, 21 if phase == 0 else 20, threads=8)
        got = [R.get(d, 0) for d in range(1, len(EXPECT[phase]) + 1)]
        print(f'phase {phase} R^F(1..{len(got)}) = {got}  expected {EXPECT[phase]}  ->', 'MATCH' if got == EXPECT[phase] else 'MISMATCH')
        ok &= got == EXPECT[phase]
        R2, _, _, _, _ = run('x4', phase, 41, threads=8)
        R3, _, _, _, _ = run('x4', phase, 41, nodedup=1, threads=8)
        same = all(R2.get(d) == R3.get(d) for d in range(1, 43))
        print(f'phase {phase} merging on/off identical to depth 42:', same); ok &= same
    Rg, censg, _, _, _ = run('gm', 1, 20, threads=8)
    allc = all(censg.get(d, 0) == 1 for d in range(1, 21))
    print('gm control, phase 1, censored at every depth 1..20:', allc); ok &= allc
    print('CALIBRATION', 'PASSES' if ok else 'FAILS')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'calib'
    if mode == 'build': build()
    elif mode == 'calib': calib()
    elif mode == 'run':
        lang, phase, maxm = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        maxstates = sys.argv[5] if len(sys.argv) > 5 else '30000000'
        dfsmax = int(sys.argv[6]) if len(sys.argv) > 6 else 0
        R, cens, wit, levels, kinds = run(lang, phase, maxm, maxstates, dfsmax=dfsmax)
        print('levels (m, states, children, s):', levels[-3:])
        print('R^F(d):', ' '.join(f"{d}:{R[d]}{'*' if cens[d] else ''}" for d in sorted(R)))
        print('deaths (m, at 11, at other, capped):', kinds[-1] if kinds else None)
    else:
        print(__doc__)
