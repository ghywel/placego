#!/usr/bin/env python3
"""rule30_races.py: the owner's question (2026-10-06): an await that is almost always kept, with a little fuzz at the
last moment. Rule 30 with rare race conditions (races.c): with probability eps per cell per step a cell reads one
neighbour's NEW value. How long does the ideal history survive, and does it matter which neighbour races?

RUN-ON:     cpu (races.c via cc; Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_races.py [JOBS=10]
COST:       about a minute on ten cores.

What a race injects (exact). Write the row as ... x_(i-2) x_(i-1) x_i x_(i+1) x_(i+2) ... and the synchronous update
x'_i = x_(i-1) XOR (x_i OR x_(i+1)).
  Left race (the left neighbour finished first): the cell reads x'_(i-1) for x_(i-1), so its error is
  x'_(i-1) XOR x_(i-1) = R210(x_(i-2), x_(i-1), x_i): the left neighbour's velocity (section 8.70). On a fair row it
  is 1 with probability 1/2.
  (These are for an ISOLATED race, whose neighbour did not race. GPT's G092: when adjacent cells both race, the second
  can read a raced value, adding a propagation term; it is second order in eps, and the step-1 fractions measured at
  eps = 0.01 include it, consistent with the right-race fraction 0.1281; GPT's G102 gives the bulk value 1/(8 - 4 eps) = 0.12563 at eps = 0.01,
  and the run's 0.0032 standard error cannot separate it from the isolated 1/8.)
  Right race: the cell reads x'_(i+1) inside the OR, so its error is NOT x_i AND (x'_(i+1) XOR x_(i+1)), and with
  x_i = 0 the right neighbour's velocity is R210(0, x_(i+1), x_(i+2)) = NOT x_(i+1) AND x_(i+2). On a fair row the
  error is 1 with probability 1/2 * 1/4 = 1/8. The OR masks races from the right four times as often.
How an error spreads (section 8.66): a difference moves right at exactly 1 (left permutivity: it never dies) and
left at about 0.246 on a random background, and two histories differ at about half the cells inside the damaged
region. So a cell is undamaged at time t when no injected error lies in a backward cone of area about
(1 + 0.246) t^2 / 2 = 0.623 t^2, and the fraction of differing cells is about (1 - exp(-0.623 p eps t^2)) / 2, with
p = 1/2 (left) or 1/8 (right). It reaches 1/4 at t_half = sqrt(ln 2 / (0.623 p eps)).

PREDICTIONS, written 2026-10-06 before this script's first run (no run of races.c beyond a compile):
  RC0 (instrument, exact): with eps = 0 the two runs never differ.
  RC1 (exact for fair rows; measured in step 1 at eps = 0.01, eight seeds): the fraction of races that inject an error
      is 1/2 +- 0.02 for left races and 1/8 +- 0.01 for right races.
  RC2 (blind; dimension): t_half scales as eps^(-1/2): over eps = 1e-3 .. 1e-7 the fitted exponent is -0.5 +- 0.05,
      for each mode.
  RC3 (blind; the masking): t_half(right) / t_half(left) is in [1.8, 2.2] at every eps (sqrt of 4).
  RC4 (blind, riskier; the absolute law): t_half(left) is within 30% of sqrt(ln 2 / (0.623 eps / 2)) at every eps.
  D1 (descriptive): the fuzzy row's density and fraction of unequal neighbours at the end.

OUTCOME, 2026-10-06 (M5, ten cores, ten seconds). The first run had an instrument fault: when a run has fewer steps
than checkpoints (left races at eps = 1e-3, T = 286 < 400) the schedule stalled after step 3, and t_half was
interpolated between steps 3 and 286 (143.6 against 47.2). That one point made RC2, RC3 and RC4 read REFUTED. The
schedule now always advances (races.c); the run was repeated with the same predictions, and the first run's verdicts
are kept here. Second run: RC0 PASS. RC1 HELD: races inject an error at 0.5016 (left) and 0.1281 (right) of 10,470
each. RC2 HELD: exponents -0.501 (left) and -0.493 (right). RC4 HELD: left t_half / law = 0.964, 0.994, 0.999, 1.009,
0.968 for eps = 1e-3 .. 1e-7. RC3 REFUTED narrowly: right/left ratios 2.022, 1.914, 1.901, 2.073 and 1.758 (eps =
1e-7, below 1.8). Post hoc, not changing the verdict: four more seeds at eps = 1e-7 give left 5465, 4764, 5369, 5197
and right 10212, 9460, 7531, 10827, a ratio of means 1.83; at that rate a run averages only about a dozen independent
damage regions, so one seed varies by about 15%, and the band was too tight for one seed. D1: density 0.497 to 0.502
and unequal neighbours 0.497 to 0.503 in every fuzzy run: the statistics survive while the history is replaced.
"""
import math
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
EXE = os.path.join(tempfile.gettempdir(), 'rule30_races')
subprocess.run(['cc', '-O3', '-o', EXE, os.path.join(HERE, 'races.c'), '-lm'], check=True)
W = 1 << 17
EPS = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]


def run(T, eps, mode, seed, checks=400):
    out = subprocess.run([EXE, str(W), str(T), repr(eps), mode, str(seed), str(checks)], capture_output=True,
                         check=True, text=True).stdout.split('\n')
    res = {'F': []}
    for line in out:
        f = line.split()
        if not f:
            continue
        if f[0] == 'INJ':
            res['inj'] = (int(f[1]), int(f[2]))
        elif f[0] == 'F':
            res['F'].append((int(f[1]), int(f[2]) / W))
        elif f[0] in ('D', 'P'):
            res[f[0]] = float(f[1])
    return res


def t_half(F):
    prev = (0, 0.0)
    for t, f in F:
        if f >= 0.25:
            t0, f0 = prev
            return t0 + (0.25 - f0) * (t - t0) / (f - f0) if f > f0 else t
        prev = (t, f)
    return None


def predicted(eps, p):
    return math.sqrt(math.log(2) / (0.623 * p * eps))


def main():
    jobs = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    r0 = run(2000, 0.0, 'L', 1, 20)
    rc0 = all(f == 0 for _, f in r0['F'])
    print('RC0', 'PASS' if rc0 else 'FAIL', '(eps = 0: never differ over 2000 steps)')
    with ThreadPoolExecutor(jobs) as ex:
        inj = {m: [ex.submit(run, 1, 0.01, m, s, 1) for s in range(1, 9)] for m in 'LR'}
        cfg = [(m, e) for m in 'LR' for e in EPS]
        futs = {(m, e): ex.submit(run, int(5 * predicted(e, 0.5 if m == 'L' else 0.125)) + 50, e, m, 7) for m, e in cfg}
        inj = {m: [f.result()['inj'] for f in v] for m, v in inj.items()}
        res = {k: f.result() for k, f in futs.items()}
    frac = {m: sum(b for _, b in v) / sum(a for a, _ in v) for m, v in inj.items()}
    rc1 = abs(frac['L'] - 0.5) <= 0.02 and abs(frac['R'] - 0.125) <= 0.01
    print('RC1', 'HELD' if rc1 else 'REFUTED', 'injected fraction: left %.4f (%d races), right %.4f (%d races)' % (
        frac['L'], sum(a for a, _ in inj['L']), frac['R'], sum(a for a, _ in inj['R'])))
    th = {k: t_half(r['F']) for k, r in res.items()}
    print('%5s %8s %10s %10s %8s %8s' % ('mode', 'eps', 't_half', 'predicted', 'ratio', 'density'))
    for (m, e), r in sorted(res.items()):
        p = 0.5 if m == 'L' else 0.125
        print('%5s %8.0e %10.1f %10.1f %8.3f %8.4f  unequal-neighbours %.4f' % (m, e, th[(m, e)], predicted(e, p),
                                                                               th[(m, e)] / predicted(e, p), r['D'], r['P']))
    rc2 = True
    for m in 'LR':
        xs = [math.log(e) for e in EPS]
        ys = [math.log(th[(m, e)]) for e in EPS]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        print('  exponent', m, '%.4f' % slope)
        rc2 &= abs(slope + 0.5) <= 0.05
    print('RC2', 'HELD' if rc2 else 'REFUTED')
    ratios = [th[('R', e)] / th[('L', e)] for e in EPS]
    print('RC3', 'HELD' if all(1.8 <= q <= 2.2 for q in ratios) else 'REFUTED', ['%.3f' % q for q in ratios])
    rel = [th[('L', e)] / predicted(e, 0.5) for e in EPS]
    print('RC4', 'HELD' if all(0.7 <= q <= 1.3 for q in rel) else 'REFUTED', ['%.3f' % q for q in rel])


if __name__ == '__main__':
    main()
