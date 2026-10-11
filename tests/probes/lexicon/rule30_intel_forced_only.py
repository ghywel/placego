#!/usr/bin/env python3
"""rule30_intel_forced_only.py: FO, the forced-only records R^F(d) of the check-free conjecture, exact, both phases
(RULE30-PRIZE.md 8.88; STRATEGY-PLAN.md section 1, the first week's first item; decided in CL260 and CL263).

RUN-ON:     the Intel MacBook (16 logical cores); C with OpenMP (forced_only_x4.c beside this file)
COMMAND:    python3 tests/probes/lexicon/rule30_intel_forced_only.py build
            python3 tests/probes/lexicon/rule30_intel_forced_only.py calib
            python3 tests/probes/lexicon/rule30_intel_forced_only.py run LANG PHASE MAXM [MAXSTATES [DFSMAX]]
            (LANG x4|gm|maw12|dfa=FILE; MAXM is the last merged level; DFSMAX extends depth-first without merging)
            python3 tests/probes/lexicon/rule30_intel_layer_dfa.py WIDTH PHASE OUT.dfa   (the layer automata)
            python3 tests/probes/lexicon/rule30_intel_mfw_dfa.py PHASE K OUT.dfa     (the cutoff-K language X_K)
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
pair (A_m, A_{m-1} masked where A_m's next bit is black) plus the language state (the last twelve visible bits, or
the automaton state) and the last four visible bits (they name the death word), merged with the longest streak of
white forced cells ending at m kept (8.38's MG0b: equal masked pairs have equal futures). From every state
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
  FO-P7 (registered 2026-10-11 03:54 BST, after the width-4, 8 and 12 results below and before the width-16 and width-20
         runs; disclosed: the width-8 death split, 44% at 11, 13% at 00000, 43% at a longer word, was seen while
         testing the revised engine). The automata (rule30_intel_layer_dfa.py) give h = 0.21158 at width 16 and
         0.15187 at width 20 (under the record's certified bounds 0.2130 and 0.1533), so h/(1 - h) = 0.268 and 0.179.
         (a, 0.7 each) the phase-0 forced-only slope over d = 40..122 lies in 0.7..1.05 times h/(1 - h): 0.19..0.28
         at width 16 and 0.13..0.19 at width 20; (b, 0.6 each) the phase-1 slope lies in 0.6..0.95 times it: 0.16..0.26
         and 0.11..0.17; (c, 0.9) R^F(width 16) <= R^F(width 12) and R^F(width 20) <= R^F(width 16) at every depth in
         both phases; (d, 0.5) at widths 16 and 20, 11 is the most frequent of the three death kinds in both phases.
         Controls run before this registration: the revised engine (the last four visible bits in the merging key, the
         death word classified as 11, 00000 or longer) reproduces every earlier table, X_4 to 42 in both phases and the
         width-8 layer to 122 with equal level counts; the width-4 automaton reproduces X_4's table to depth 62.
  FO-P8 (registered 2026-10-11 08:15 BST, before any run over these automata; CL282's request, CL297's first item). The
         language is X_40: the words avoiding every minimal forbidden word of length <= 40 of L (phase 0, 771 words) or
         L1 (phase 1, 832), from rule30_visible_language_handoff.md (rule30_intel_mfw_dfa.py). It equals the real
         visible language at every length <= 40 and contains it at every length, so the check-free conjecture covers
         it. Run before this registration, as controls of the automaton only: its word counts equal the handoff's C_n
         at every n = 1..40 in both phases; minimal automata 4,967 and 5,390 states; growth h = 0.15081 and 0.14843
         bits per visible bit, so h/(1 - h) = 0.1776 and 0.1743. A forced-only record R^F(d) over X_40 is the exact
         record over L when d + R^F(d) <= 79 (phase 0; 80 in phase 1: the run then ends inside the first 40 visible
         bits), and an upper bound otherwise, with R^F_L(d) >= 80 - d (81 - d) there.
         (a, control, must hold) R^F(X_40) <= R^F(X_4) at every depth (X_40 is inside X_4); where exact, the larger
         of the two phases' R^F is at least the real record R_real(d) (dropping the checks only adds runs).
         (b, blind 0.85) no forced-only orbit reaches the cap of 3m + 300 steps (the kill does not fire over X_40).
         (c, blind 0.6) the exact horizon (the last d with d' + R^F(d') <= 79, resp. 80, for every d' <= d) is at
         least 50 in both phases.
         (d, blind 0.6) the least-squares slope over d = 40..122 (121) lies in 0.7..1.2 times h/(1 - h): 0.124..0.213
         (phase 0) and 0.122..0.209 (phase 1).
         (e, blind 0.6) R^F(X_40) <= R^F(width 20) at 90% or more of the depths in both phases (CL282's "the width-20
         run is the control it must fall below"; X_40 and the width-20 layer are not nested beyond length 40, so
         this can fail).
         Unexpected check: the death split (11, 00000, a longer word) over X_40 against the width-20 layer's 31/15/54.

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

ADDENDUM (2026-10-11 04:36 BST): the depth-first tail of X_4 to depth 122 and the layer languages of width 8, 12, 16 and
  20, both phases; FO-P7's verdicts. All COMPUTED and exact; no forced-only orbit of any prefix in any language
  reached the cap of 3m + 300 steps, so the conjecture's kill did not fire to these depths (FO-P4 HELD throughout).
  X_4 phase 0: merged to level 97 (51.7 million states), depth-first to 121 with path inheritance (1924 s on 16
         threads, 15.81 x 10^9 paths): exact to depth 122; R^F(100, 110, 112, 120, 122) = 143, 157, 159, 155, 165;
         slope 1.388 over d = 40..122 (1.486 over 40..112). Phase 1: merged to 98 (61.8 million), tail to 120
         (1507 s, 12.36 x 10^9 paths): exact to 121; R^F(100, 110, 111, 120, 121) = 126, 156, 155, 158, 163; slope
         1.340 over 40..121 (1.334 over 40..111). Deaths over the evaluated paths: 13,629,433,404 at 11 against
         2,182,738,215 at 00000 (phase 0, 86%); 10,653,847,573 against 1,708,604,937 (phase 1).
  Layer languages (automata by rule30_intel_layer_dfa.py; widths 8, 12, 16, 20 with 56, 402, 2260, 12749 states in
         phase 0 and 60, 407, 2307, 13009 in phase 1; growth h = 0.3562, 0.2578, 0.2116, 0.1519; X_4 is width 4 with
         h = 0.6174), merged throughout, exact to 122 (phase 0) and 121 (phase 1) in 4 to 11 s on 4 threads each:
         width    h    h/(1-h)   slope p0 (ratio)   slope p1 (ratio)   R^F(120) p0/p1   deaths % 11 / 00000 / longer
            4   0.617   1.614    1.388 (0.86)       1.340 (0.83)        155 / 158        86.2 / 13.8 / 0
            8   0.356   0.553    0.475 (0.86)       0.391 (0.71)         59 / 58         43.8 / 13.3 / 42.9
           12   0.258   0.347    0.357 (1.03)       0.256 (0.74)         45 / 38         35.8 / 14.4 / 49.8
           16   0.212   0.268    0.319 (1.19)       0.216 (0.81)         45 / 36         33.2 / 14.8 / 52.0
           20   0.152   0.179    0.154 (0.86)       0.164 (0.92)         35 / 36         31.2 / 15.3 / 53.5
         (slopes by least squares over d = 40..top; ratio = slope / (h/(1-h)); the death split is over evaluated
         paths in phase 0, phase 1 within 0.5 of it; the twelve-word class: 0.660 and 0.346, deaths 47.9/12.9/39.2.)
  Nesting (a check of the automata and the engine): R^F(X_4) >= R^F(8) >= R^F(12) >= R^F(16) >= R^F(20) at every
         exact depth in both phases, strict at 103, 62, 48, 59 of the depths (phase 0). R^F(122) = 61 at widths 8, 12
         and 16 in phase 0: one orbit is the record at 122 in all three.
  FO-P3 at the final depths: phase 0 1.388 over 40..122 (in 1.3..1.9, HELD; 1.451 at 92, 1.486 at 112), phase 1
         1.340 over 40..121 (HELD; 1.215 at 93, 1.334 at 111). The other first-block verdicts are unchanged.
  FO-P7 (a) HELD at width 20 (0.154 in 0.13..0.19), REFUTED at width 16 (0.319 above 0.28); (b) HELD at both widths
         (0.216 in 0.16..0.26, 0.164 in 0.11..0.17); (c) HELD; (d) REFUTED at both widths and both phases: the most
         frequent death kind at widths 12, 16 and 20 is a word longer than 00000 (50 to 54%), 11 second (31 to 36%).
  Reading (MEASURED, these depths). The forced-only slope falls with the width: 1.39, 0.48, 0.36, 0.32, 0.15 (phase 0)
         and 1.34, 0.39, 0.26, 0.22, 0.16 (phase 1), tracking h/(1-h) within a factor 0.71..1.19 at every width; the
         scatter is the record's own (R^F moves by 10 to 20 between neighbouring depths; a slope over 80 depths is
         good to about 0.05). If the same law holds for the real language, h_top <= 0.1236 puts its forced-only
         slope at or below 0.14 against the real record's 0.08: the forced cells alone, over the true language,
         would still leave about a factor 1.75 in slope for the checks to remove. As the language tightens the kill
         moves from 11 (86% in X_4, 44% at width 8, 31% at width 20) to the longer forbidden words (0, 43%, 54%).
  Controls: the revised engine reproduces every earlier table (X_4 to 42 both phases, the widths 8 and 12 and the
         twelve-word class to 122/121, level counts equal); the width-4 automaton reproduces X_4 to depth 62; the
         builder is byte-identical to the first one at widths 8 and 12 and gives the record's state counts at 16, 20.
  Exact tables, witnesses and death counts for every run: rule30_intel_forced_only.txt. Logs outside git. The DFS
         tail (X_4) is the only part that costs hours; it is CPU-bound and threads well; no shader work was needed.
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
        elif p[0] == 'K': kinds.append(tuple(int(x) for x in p[1:]))
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
