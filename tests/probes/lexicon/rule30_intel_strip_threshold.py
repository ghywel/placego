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
