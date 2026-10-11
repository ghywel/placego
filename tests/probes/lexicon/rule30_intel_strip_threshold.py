#!/usr/bin/env python3
"""rule30_intel_strip_threshold.py: SX, the exactness threshold L(W) of the strip form for full traces, both phases
(KIMI-QUESTIONS-4, Q1; the swarm's door D4; assigned to Intel in CL297, section 8.89).

RUN-ON:     the Intel MacBook (16 logical cores); C with OpenMP (rule30_intel_strip_trace.c beside this file)
COMMAND:    python3 tests/probes/lexicon/rule30_intel_strip_threshold.py build
            python3 tests/probes/lexicon/rule30_intel_strip_threshold.py run PHASE N WMIN WMAX
            python3 tests/probes/lexicon/rule30_intel_strip_threshold.py report N
COST:       the real traces of length N from all 2^N rows (N = 32: 2^26 bit-sliced blocks, 0.5 GB, about a minute on
            16 threads); the strip walks take seconds to W = 14. Logs in NP_SCRATCH_SX (default ~/np-scratch/rule30-sx).

The object (KIMI-QUESTIONS-4). The wall is x_t(0) = (t + phase) mod 2. T(l) is the set of traces (column 1 at EVERY
time, y_0 .. y_{l-1}) of length l over all right halves; T^W(l) the traces of the width-W strip (sites 1..W, a free
input at site W+1 at every step). T(l) is contained in T^W(l). The exactness threshold is L(W) = max {l : T^W(l) =
T(l)}; Conjecture S is L(W) >= 2W - 1 for every W. Q1 asks for L(W) for W <= 10 in both phases, whether L(2k) =
L(2k+1), and what the traces of T^W(L(W)+1) outside T(L(W)+1) are.

Engine (rule30_intel_strip_trace.c, Intel's own code). Real traces: all rows of sites 1..N, 64 at a time bit-sliced,
the light cone run N steps; T(l) is the set of length-l prefixes of the length-N traces (a trace of length l depends
only on sites 1..l). Strip traces: a depth-first walk over trace bits whose state is the set of possible strip rows
(a bitset over 2^W rows); only real prefixes are extended, so at every length the walk counts the real strip traces
(the containment control) and the fresh extra traces (real prefix, not real). L(W) is the last length with no fresh
extra; extensions of an extra are extras, so the first failure is the threshold. This script's report adds, for every
extra trace f, its least excluding width w(f) by a separate subset walk (numpy) at widths W+1, W+2, ...

Record searched: `record_find.py 'Conjecture S'` -> KIMI-QUESTIONS-4 and older unrelated uses (8.36's R(d) <= d + 4,
GC746); `'exactness threshold'` -> KIMI-QUESTIONS-4 only (the calibration L(1..5) = 3, 6, 6, 10, 10, L(6) >= 15);
`'strip form'` -> 8.89 (the decision), KIMI-QUESTIONS-4; `'L.2k.'` -> KIMI-QUESTIONS-4's Q1 only. 8.83 holds
the 938 minimal absent traces to length 84 with w(f) <= ceil(|f|/2), tight at 2, 4, 7, 11, 35, 36, 61. Disclosed
third-party knowledge, read before this header: the swarm's door D4 report (outside git, an agent's output, unverified
until this probe), whose claims are SX-C1 below.

PREDICTIONS, registered 08:15 BST before the runs. Run before this header: only the published calibration (standard
phase, N = 16, W = 1..5), which the engine reproduces exactly: |T(1..16)| = 2 3 4 5 7 8 10 12 15 18 22 26 32 36 44 49,
L(1..5) = 3, 6, 6, 10, 10, the extra traces 0000 and 0101 (W = 1), 0001000 (W = 2, 3), 11001101001 (W = 4, 5),
each minimal absent, and 11 against 10 at W = 3, l = 7, 23 against 22 at W = 5, l = 11.
  SX-C0 (controls, must hold): at every W and l the walk finds every real trace (containment); L(W) is
         non-decreasing in W (T^{W+1} is contained in T^W); L(W) >= W + 2 (the proved w(f) <= |f| - 2).
  SX-C1 (third-party claims to reproduce): standard phase, T^W(2W) = T(2W) for every W reached and T^W(2W+1) differs
         from T(2W+1) exactly at W = 3 and 5 among W <= 15; odd phase, T^W(2W+1) differs at W = 1, 7 and 12 among
         W <= 13, and T^W(2W) at W = 12 among W <= 15. These give standard L(W) >= 2W + 1 for W = 6..15 and odd L(1) =
         2, L(7) = 14, L(12) = 23.
  SX-P1 (blind, 0.35): the standard phase pairs at k = 3, 4, 5: L(6) = L(7), L(8) = L(9), L(10) = L(11).
  SX-P2 (blind, 0.7): the odd phase breaks the pairing at least once among k = 1..5.
  SX-P3 (blind, 0.5): standard phase, L(W) <= 2W + 4 for every W = 6..10.
  SX-P4 (blind, 0.4): standard phase, at most two fresh extra traces at L(W) + 1 for every W = 6..10.
  SX-P5 (blind, 0.3): wherever L(2k) = L(2k+1), the two widths have the same extra traces, as at 2/3 and 4/5.
  SX-P6 (blind, 0.6): every fresh extra trace at L(W) + 1 is minimal absent (without its first two symbols it is real),
         for W = 1..14 in both phases.
  Counterfactual: a containment failure, a decrease of L in W, or an extra at a length <= W + 2 contradicts a proved
  fact and would refute the instrument, not the conjecture; so would a calibration value that moves.
  Unexpected check: the least excluding width w(f) of every extra trace, and whether it is tight (w(f) = ceil(|f|/2),
  the case that would make Conjecture S sharp at that length). Not predicted.
  Scope: N = 32 in both phases (traces to length 32), W = 1..14; L(W) is exact where L(W) + 1 <= 32 and is reported as
  a lower bound otherwise.

OUTCOME (2026-10-11 08:21 BST). Both phases, N = 32 (2^32 rows each, 8 s on 16 threads), W = 1..14. Tables, extra
traces and their least excluding widths: rule30_intel_strip_threshold.txt beside this file. All COMPUTED.
  L(W), W = 1..14, standard phase: 3, 6, 6, 10, 10, 17, 20, 20, 20, 26, 30, >= 32, >= 32, >= 32.
  L(W), W = 1..14, odd phase:      2, 7, 7, 11, 11, 14, 14, 19, 19, 23, 23, 23, 29, 29; and L(15) = 29 follows (below).
  Cross-check: an independent numpy enumeration of all 2^24 rows gives the same |T(l)| for l = 1..24 in both phases,
         and confirms every extra trace to length 24 absent, its prefix and its two-step suffix real, and its least
         excluding width (width w(f) - 1 produces it, w(f) does not).
  SX-C0: containment PASS at every W and l in both phases; L non-decreasing in W. The third clause, L(W) >= W + 2,
         holds at every W in the standard phase and FAILS in the odd phase at W = 1: L(1) = 2, because the trace 000
         is produced by the width-1 strip and by no right half. Checked by hand from the rule: with x_0(0) = 1,
         y_0 = y_1 = 0 forces x_0(2) = 1, so x_1(2) = 1 and y_2 = x_1(2) = 1; the strip takes e_0 = 1, e_1 = 0. The
         instrument is right; the registration was wrong to assume the lemma w(f) <= |f| - 2 in both phases. It is a
         standard-phase lemma (KIMI-QUESTIONS-4's setting) and false in the odd phase at |f| = 3.
  SX-C1 REPRODUCED in full: standard T^W(2W) = T(2W) for W <= 15 and T^W(2W+1) differs only at W = 3, 5 (W <= 15;
         W = 12..15 by L(12) >= 32 and monotonicity); odd T^W(2W+1) differs at W = 1, 7, 12 (W <= 13) and T^W(2W)
         at W = 12 and 15. The last follows from computed facts: L(15) >= L(14) = 29, and the length-30 extra trace
         below has w(f) = 16, so the width-15 strip produces it and L(15) <= 29.
  SX-P1 REFUTED: the standard phase pairs at k = 4 (20, 20) and not at k = 3 (17 against 20) or k = 5 (26 against 30).
  SX-P2 REFUTED: the odd phase pairs at every k = 1..5 (7, 11, 14, 19, 23) and first breaks at k = 6 (23 against 29).
  SX-P3 REFUTED: L(6) = 17, L(7) = 20 and L(10) = 26 exceed 2W + 4; held at W = 8, 9.
  SX-P4 HELD (2, 2, 2, 2, 1 extra traces at W = 6..10). SX-P5 HELD (every equal pair shares its extra traces).
  SX-P6 HELD: every extra trace at L(W) + 1 is minimal absent, both phases, every W reached.
  Unexpected check, the least excluding widths. Standard phase: w(f) = ceil(l/2) at l = 4, 7, 11 (w = 2, 4, 6) and
         well below it at l = 18, 21, 27, 31 (w = 7, 10, 11, 12 against 9, 11, 14, 16). Odd phase: w(f) = ceil(l/2)
         at l = 3, 8, 12, 15, 20, and ABOVE it at l = 24 and 30: 001000100110001001101000 has w = 13 > 12 and
         011001100010011001100110011000 has w = 16 > 15. So the per-trace form w(f) <= ceil(|f|/2) fails in the odd
         phase (the record has this from the swarm's agent and skeptic, STRATEGY-PLAN.md; here by Intel's own code,
         with the two shortest witnesses), while L(W) >= 2W - 1 holds there with no slack at W = 12 and 15
         (L = 23, 29). KIMI-QUESTIONS-4's "equivalently" between the two forms holds for odd lengths only.
  Reading (Q1). The pairing is not a law. L is a step function: L(W) + 1 is the length of the shortest absent trace
         that width W does not exclude, and a plateau ends exactly at the least excluding width of its extra traces
         (standard W = 7, 8, 9 share 000100110100010011000 and 110100110100010011000, both w = 10, and L jumps at 10).
         Plateaus of two widths come from extras whose w(f) is the next even width (standard w = 4, 6; odd w = 4, 6, 8,
         10); the odd plateaus of three widths (10..12, 13..15) come from the two extras with w = 13 and 16, the ones
         above ceil(l/2). So L(2k) = L(2k+1) fails exactly when an extra trace at L(2k) + 1 has w(f) = 2k + 1: standard
         k = 3 and 5 (w = 7, 11), odd k = 6 (w = 13); everywhere else to W = 14 the extras' w(f) is at least 2k + 2.
         The slack L(W) - (2W - 1)
         grows in the standard phase (2, 3, 1, 3, 1, 6, 7, 5, 3, 7, 9, then >= 9) and stays at most 4 in the odd
         phase (1, 4, 2, 4, 2, 3, 1, 4, 2, 4, 2, 0, 4, 2, 0). So if Conjecture S fails anywhere, the odd phase is
         where to look, and in the odd phase it cannot be improved to 2W. The extra traces form one family across
         the phases: dropping the first symbol (one time step, which swaps the phase) takes a threshold extra of one
         phase to a threshold extra of the other at four pairs: 0000 and 000, 0001000 and 10001000, 11001101001 and
         011001101001, 110100110100010011000 and 10100110100010011000. Six of the nine extra traces of length 18 or
         more end in 10011000.

SX-P7, registered 2026-10-11 09:30 BST before the extension runs (CL302 (a): push the odd phase beyond W = 15). The
  engine
now keeps the real traces in per-thread hash sets instead of a 2^N bitmap (output identical at N = 32 in both
phases), so N is bounded by time only: N = 38 (2^38 rows), odd phase first, then the standard phase, W = 1..20.
Disclosed third-party claims (the swarm's door D4, SAT with DRAT-checked UNSATs, unverified by Intel beyond W = 15):
in the odd phase T^W(2W-1) = T(2W-1) for W <= 18 and T^W(2W) = T(2W) except at W = 12, 15; that is, L(W) >= 2W at
W = 16, 17, 18.
  (a, blind 0.85) Conjecture S holds at every odd-phase width whose L(W) the run determines (L(W) >= 2W - 1).
  (b, blind 0.7) no zero slack at W = 16, 17, 18 in the odd phase (it rests on the door's claims).
  (c, blind 0.5) odd L(16) >= 33 (slack at least 2).
  (d, blind 0.5) standard L(12) >= 34.
  (e, blind 0.4) every new threshold extra trace is minimal absent and has a partner under first-symbol dropping
         among the other phase's threshold extras, as four of the earlier ones do.
  Counterfactual: an L(W) < 2W - 1 refutes Conjecture S in that phase; it would be reported with a strip witness and
  re-checked by SAT on the light cone before any claim.
"""
import os, re, subprocess, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'rule30_intel_strip_trace.c')
SCRATCH = os.environ.get('NP_SCRATCH_SX', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-sx'))
BIN = os.path.join(SCRATCH, 'rule30_intel_strip_trace')
OMP = ['-Xpreprocessor', '-fopenmp', '-I/usr/local/opt/libomp/include', '-L/usr/local/opt/libomp/lib', '-lomp'] \
    if sys.platform == 'darwin' else ['-fopenmp']
OUT = os.path.join(HERE, 'rule30_intel_strip_threshold.txt')


def build():
    os.makedirs(SCRATCH, exist_ok=True)
    subprocess.run(['cc', '-O2', *OMP, SRC, '-o', BIN], check=True)
    print('built', BIN)


def run(phase, n, wmin, wmax):
    os.makedirs(SCRATCH, exist_ok=True)
    log = os.path.join(SCRATCH, f'sx_p{phase}_n{n}_w{wmin}-{wmax}.log')
    t0 = time.time()
    with open(log, 'w') as fh:
        subprocess.run([BIN, str(phase), str(n), str(wmin), str(wmax)], stdout=fh, check=True)
    print(f'{log}: {time.time() - t0:.0f} s')
    return log


def parse(log):
    T, LW, X, contain, real, extra = {}, {}, {}, {}, {}, {}
    for line in open(log):
        p = line.split()
        if not p: continue
        if p[0] == 'T': T[int(p[1])] = int(p[2])
        elif p[0] == 'LW': LW[int(p[1])] = p[2]
        elif p[0] == 'X': X.setdefault(int(p[1]), []).append((int(p[2]), p[3], p[4]))
        elif p[0] == 'CONTAIN': contain[int(p[1])] = p[2]
        elif p[0] == 'W':
            w, l = int(p[1]), int(p[3].rstrip(':')); real[(w, l)] = int(p[5]); extra[(w, l)] = int(p[10])
    return T, LW, X, contain, real, extra


def strip_produces(f, V, phase):
    """True when the width-V strip (free input at site V+1) produces the trace f (string, y_0 first)."""
    n = np.arange(1 << V, dtype=np.int64); mask = (1 << V) - 1; S = np.ones(1 << V, dtype=bool)
    for t, ch in enumerate(f):
        S &= ((n & 1) == int(ch))
        if not S.any(): return False
        if t == len(f) - 1: return True
        wall = (t + phase) & 1; idx = np.flatnonzero(S); S2 = np.zeros(1 << V, dtype=bool)
        for e in (0, 1):
            c = idx; R = (c >> 1) | (e << (V - 1)); S2[((((c << 1) | wall) & mask) ^ (c | R)) & mask] = True
        S = S2
    return True


def least_width(f, phase, start, cap=22):
    for V in range(start, cap + 1):
        if not strip_produces(f, V, phase): return V
    return None


def report(n):
    out = ['# SX: exactness thresholds L(W) of the strip form, full traces (KIMI-QUESTIONS-4, Q1). Intel, 2026-10-11.',
           '# Engine rule30_intel_strip_trace.c; see rule30_intel_strip_threshold.py. Traces are written y_0 first.']
    LWall = {}
    for phase in (0, 1):
        log = os.path.join(SCRATCH, f'sx_p{phase}_n{n}_w1-14.log')
        T, LW, X, contain, real, extra = parse(log); LWall[phase] = LW
        out += ['', f'## phase {phase} (wall x_t(0) = (t + {phase}) mod 2), traces to length {n}',
                '|T(l)|, l = 1..%d: %s' % (n, ' '.join(str(T[l]) for l in range(1, n + 1)))]
        for w in sorted(LW):
            out.append(f'W = {w}: L(W) = {LW[w]}; containment {contain[w]}')
            for (l, f, mn) in X.get(w, []):
                wf = least_width(f, phase, w + 1)
                out.append(f'    extra at l = {l}: {f} ({mn}); w(f) = {wf}, ceil(l/2) = {(l + 1) // 2}'
                           f'{" TIGHT" if wf == (l + 1) // 2 else ""}')
    open(OUT, 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    if mode == 'build': build()
    elif mode == 'run': run(*[int(a) for a in sys.argv[2:6]])
    elif mode == 'report': report(int(sys.argv[2]) if len(sys.argv) > 2 else 32)
