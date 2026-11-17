#!/usr/bin/env python3
"""rule30_cloud_wheel_slab.py: SL and N1R, is the wheel's locked block a forced slab, and was N1 a fair comparison?

RUN-ON:     cpu (Python 3 standard library and kissat; set KISSAT to the solver)
COMMAND:    KISSAT=path python3 tests/probes/lexicon/rule30_cloud_wheel_slab.py [part=all|slab|n1|depth]
COST:       expected several minutes (a few thousand small SAT calls).

Why (the owner, 2026-10-09: "Can you run some tests on this on our own here - I think GPT is busy"). Two items Cloud
had handed to others are taken back here.
  1. CL095 asked GPT whether the wheel's locked block (columns 1 to 4 fixed by the wheel's position in every clean
     stretch, VW in rule30_cloud_velocimetry.py) is a slab of the kind GC688 found for all-S traces: columns forced
     by the rule itself, whatever the right side does. VW measured it on realized orbits only.
  2. CL096 found a real interior kicking the wheel less than coin flips (KR-U), against §8.11's N1. Reading
     rule30_chaos.py shows that N1 computed only the coin engine's share of aligned 56-step windows that are exact
     rotations of U (60.2%). The 8.4% beside it is rule30_wheel.py's Q1, a different measure: a window equal to the
     previous window, with 12-cell right halves. So the old line compared two measures.

Method.
  SL. Fix column 0 = t mod 2 and column 1 = U from position p, on rows 0 .. 167 (three turns). The unknowns are
      columns 2 .. 10. Rule 30's equation x_(t+1)(k) = x_t(k-1) xor (x_t(k) or x_t(k+1)) is imposed for k = 1 .. 9,
      and for column 10 only that some column 11 exists (x_t(10) = 1 forces x_(t+1)(10) = x_t(9) xor 1). A cell is
      forced when the opposite value is UNSAT. Cells are tested on the middle turn, rows 56 .. 111, for every
      position p for which the window is satisfiable at all.
  DEPTH (the owner's question, 2026-10-09: why does a real interior kick less than coins?). Hypothesis: the wheel's
      lock reaches about ten columns into the right side (VW), and coins at column 13 cut it. Move the coin column
      out to c = 13, 16, 20, 26, 34 and 50 (columns 0 .. c - 1 by Rule 30, fresh coins at c), and measure KR's kick
      rate and clean fraction (rows 2048 .. 8135, 64 seeds) against a wide random real interior.
  N1R. The same measure for three engines over T = 4096 rows: the share of aligned 56-step windows that are exact
      rotations of U. The engines are N1's coin engine (columns 0 .. 12, fresh coins at column 13), real 12-cell
      right halves with white beyond, and wide random right halves. Q1's measure (a window equal to the one before)
      is also recomputed for the 12-cell halves at T = 2048.

PREDICTIONS, written 2026-10-09 20:16 BST, before any run of this script.
  SL-C (control): every satisfiable window has a model whose columns 2 .. 10 satisfy the equations when checked by
        separate code.
  SL-P1 (0.6): for every satisfiable position, columns 2, 3 and 4 are forced on all 56 middle rows: the block is a
        slab of the rule, not a habit of realized orbits.
  SL-P2 (0.6): column 5 is not forced on all middle rows at every position (VW found it 93% fixed, not 100%).
  SL-U, the unexpected check (0.5): exactly 28 of the 56 positions are satisfiable, one for each parity alignment.
  N1R-C (control, 0.8): the coin engine gives 55% to 65% exact U windows (N1 reported 60.2%), and Q1's measure on
        12-cell halves gives 5% to 12% (Q1 reported 8.4%).
  N1R-P (0.5): on the same measure, real 12-cell right halves give at least as many exact U windows as the coin
        engine, so the old N1 line's contrast came from comparing two measures.
  DEPTH-P (0.6): the kick rate falls as the coin column moves out and is within 15% of the real interior's by
        c = 34. The real interior is gentler because it keeps the wheel's partial lock, which coins at 13 cut.
  Counterfactual. If columns 2 .. 4 are not forced, the block is a habit of realized orbits, and GC688's slab is a
  different kind of object. If the coin engine beats real halves on one measure, §8.11's contrast stands and KR-U
  needs another explanation.

OUTCOME of the depth and n1 parts, 2026-10-09 (minutes; the slab part is reported below when it finishes).
  DEPTH-P HELD. A real wide interior kicks 0.0340 times a row (clean 0.715). Coins at column 13 kick 0.0549 (161%),
    at 16 0.0362 (106%), at 20 0.0380 (112%), at 26 0.0318 (93%), at 34 0.0302 (89%) and at 50 0.0315 (93%). The
    clean fractions at 34 and 50 (0.63, se 0.03) have ten times the spread across seeds of the others, which is not
    explained here. The surprise is the coins' placement: at column 13 they sit inside the wheel's partial lock.
  N1R-C HELD: the coin engine reproduces N1's 60.2% exactly, and Q1's measure on random 12-cell halves gives 11.6%
    (Q1: 8.4% over the unlocked ones of all 4,096 halves).
  N1R-P HELD: on N1's measure, real 12-cell right halves give 69.8% exact U windows and wide random ones 70.9%,
    against the coin engine's 60.2%. §8.11's "more cleanly" came from comparing two measures. RULE30-PRIZE.md
    §8.11 now carries a correction line.

OUTCOME of the slab part, 2026-10-09 (28 positions, about 25,000 SAT calls; under an hour beside RR3).
  SL-U HELD: exactly the 28 even positions are satisfiable, one per parity alignment.
  SL-C PASS: all 28 models pass the separate equation check.
  SL-P1 REFUTED as worded. With the registered window (168 rows, columns up to 10), column 2 is forced on all 56
    middle rows at every position. Columns 3 and 4 are forced on 55 and 52 of the 56 middle rows at every position.
    The counts per position are the same at all 28 positions: 56, 55, 52, 36, 21, 7, 7, 4, 1 for columns 2 .. 10.
  SL-P2 HELD: column 5 is forced on 36 of 56.
  POST HOC (position 0 only; written after the run). The free cells are the window's doing. With 280 rows and
    columns up to 10, the counts are unchanged (55, 52, 36). With columns up to 16, columns 3 and 4 are forced on
    all 56 middle rows (column 5 on 54 of 56 with 168 rows, and on all 56 with 280 rows).
  Reading: a clean wheel forces its neighbours by the rule itself, and the forced block deepens as more columns
    and turns are taken into account. So VW's locked block is a slab of the rule, as GC688's is for all-S traces,
    and not a habit of realized orbits. In real orbits the kicks keep the wheel from running exactly for long, which
    is why the measured lock fades after about ten columns.
  RERUN after GPT's GC855 (2026-10-09). solve() now accepts only exits 10 and 20 and checks every clause, the fixed
    units included. check() now also checks the clock and wheel units. The full slab part was rerun with these
    changes, and its output is identical line for line to the first run's.
  PRIOR RESULT, found afterwards (2026-10-09, on rejoining the pool; the board's row 6.1). SL re-derives known forcing,
    and is not new. GPT's G205 (GC373, GC374) certifies column 2 at the centre of any 13-observation wheel window and
    columns 2 .. 4 at the centre of any 143-observation window (even phases, arbitrary right exterior). Width 15
    forces columns 2 .. 6 next to the wheel (Local's LK, L236; GPT's G208). SL agrees with all three, so it is an
    independent check of them. Its "slab" reading should cite them first. I should have read row 6.1 before running.
"""
import os
import random
import subprocess
import sys
import tempfile

PART = sys.argv[1] if len(sys.argv) > 1 else 'all'
KISSAT = os.environ.get('KISSAT', 'kissat')
U = '00010011010001001101000100110100010011010001001101001101'
P = 56
L, K = 3 * P, 10


def build(p):
    """CNF for the window at position p. Returns (clauses, nvars, var)."""
    var = {}

    def v(t, k):
        if (t, k) not in var:
            var[(t, k)] = len(var) + 1
        return var[(t, k)]
    cl = []
    for t in range(L):
        cl.append([v(t, 0)] if t % 2 else [-v(t, 0)])
        cl.append([v(t, 1)] if U[(p + t) % P] == '1' else [-v(t, 1)])
        for k in range(2, K + 1):
            v(t, k)
    aux = [len(var)]

    def new():
        aux[0] += 1
        return aux[0]
    for t in range(L - 1):
        for k in range(1, K + 1):
            y, a, b = v(t + 1, k), v(t, k - 1), v(t, k)
            if k < K:
                c = v(t, k + 1)
                o = new()                              # o = b or c
                cl += [[-o, b, c], [o, -b], [o, -c]]
            else:
                o = b                                  # some column K + 1 exists: only rows with x_t(K) = 1 bind
                cl += [[-o, y, a], [-o, -y, -a]]       # y = a xor 1 when o = 1
                continue
            cl += [[-y, a, o], [-y, -a, -o], [y, -a, o], [y, a, -o]]   # y = a xor o
    return cl, aux[0], var


def solve(cl, nvars, extra=()):
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', delete=False) as f:
        f.write('p cnf %d %d\n' % (nvars, len(cl) + len(extra)))
        for c in list(cl) + [list(e) for e in extra]:
            f.write(' '.join(map(str, c)) + ' 0\n')
        name = f.name
    r = subprocess.run([KISSAT, '-q', name], capture_output=True, text=True)
    os.unlink(name)
    if r.returncode == 20:
        return None
    if r.returncode != 10:                             # GC855: only 10 (SAT) and 20 (UNSAT) are answers
        raise RuntimeError('kissat exit %d: %s' % (r.returncode, r.stderr[:200]))
    model = set()
    for line in r.stdout.split('\n'):
        if line.startswith('v '):
            model |= {int(x) for x in line[2:].split() if int(x) > 0}
    if not satisfies(model, list(cl) + [list(e) for e in extra]):
        raise RuntimeError('kissat model violates the CNF')
    return model


def satisfies(model, clauses):
    """GC855: every clause, the fixed units included, holds under the model (positive literals in model)."""
    return all(any((lit > 0) == (abs(lit) in model) for lit in c) for c in clauses)


def check(model, var, p):
    """Separate scalar check, including the clock and wheel units that GC855 found unchecked."""
    x = {key: int(v in model) for key, v in var.items()}
    for t in range(L):
        if x[(t, 0)] != t % 2 or x[(t, 1)] != int(U[(p + t) % P]):
            return False
    for t in range(L - 1):
        for k in range(1, K):
            if x[(t + 1, k)] != x[(t, k - 1)] ^ (x[(t, k)] | x[(t, k + 1)]):
                return False
        if x[(t, K)] and x[(t + 1, K)] != x[(t, K - 1)] ^ 1:
            return False
    return True


def slab():
    sat_positions, ok_models = [], 0
    forced = {k: 0 for k in range(2, K + 1)}
    full = {k: 0 for k in range(2, K + 1)}
    for p in range(P):
        cl, n, var = build(p)
        m = solve(cl, n)
        if m is None:
            continue
        sat_positions.append(p)
        ok_models += check(m, var, p)
        for k in range(2, K + 1):
            f = 0
            for t in range(P, 2 * P):
                lit = var[(t, k)]
                val = lit in m
                if solve(cl, n, [[-lit if val else lit]]) is None:
                    f += 1
            forced[k] += f
            full[k] += f == P
        print('position %2d: cumulative forced middle cells by column: %s'
              % (p, ' '.join('c%d %d' % (k, forced[k]) for k in range(2, K + 1))), flush=True)
    ns = len(sat_positions)
    print('SL-U: satisfiable positions %d: %s' % (ns, sat_positions))
    print('SL-C: models passing the separate check %d of %d' % (ok_models, ns))
    for k in range(2, K + 1):
        print('column %2d: forced %d of %d middle cells; fully forced at %d of %d positions'
              % (k, forced[k], ns * P, full[k], ns))


def n1():
    rotset = {U[i:] + U[:i] for i in range(P)}

    def coin(rng, n, width=13):
        mask = (1 << (width + 1)) - 1
        row, out = 0, []
        for t in range(n):
            row = (row & ~(1 << width)) | (rng.getrandbits(1) << width)
            out.append((row >> 1) & 1)
            new = ((row << 1) ^ (row | (row >> 1))) & mask
            row = (new & ~1 & ~(1 << width)) | ((t + 1) % 2)
        return out

    def driven(cells, n):
        row, out = cells, []
        for t in range(n):
            row = (row & ~1) | (t % 2)
            out.append((row >> 1) & 1)
            row = (row << 1) ^ (row | (row >> 1))
        return out

    def exact_u(c):
        w = [''.join(map(str, c[k * P:(k + 1) * P])) for k in range(len(c) // P)]
        return sum(x in rotset for x in w), len(w)

    def copies(c):
        w = [tuple(c[k * P:(k + 1) * P]) for k in range(len(c) // P)]
        return sum(w[k] == w[k - 1] for k in range(1, len(w))), len(w) - 1
    T = 4096
    rng = random.Random(1915)
    e = n = 0
    for _ in range(200):
        a, b = exact_u(coin(rng, T))
        e, n = e + a, n + b
    print('N1R coin engine: exact U windows %.1f%%' % (100 * e / n))
    rng = random.Random(12)
    e = n = cc = cn = 0
    for _ in range(200):
        cells = rng.getrandbits(12) << 1
        a, b = exact_u(driven(cells, T))
        e, n = e + a, n + b
        x, y = copies(driven(cells, 2048))
        cc, cn = cc + x, cn + y
    print('N1R real 12-cell halves: exact U windows %.1f%%; Q1 copies of the previous window (T = 2048) %.1f%%'
          % (100 * e / n, 100 * cc / cn))
    rng = random.Random(13)
    e = n = 0
    for _ in range(200):
        cells = rng.getrandbits(2 * T + 64) << 1
        a, b = exact_u(driven(cells, T))
        e, n = e + a, n + b
    print('N1R wide random halves: exact U windows %.1f%%' % (100 * e / n))


def depth():
    rot = {sum(int(U[(p + j) % P]) << j for j in range(P)) for p in range(P)}
    N, seeds = 8192, 64

    def flags(c1):
        n = len(c1) - P
        win = sum(c1[j] << j for j in range(P))
        out = []
        for t in range(n):
            if t:
                win = (win >> 1) | (c1[t + P - 1] << (P - 1))
            out.append(win in rot)
        return out

    def rates(fl):
        lo, hi = 2048, N - P - 1
        f = sum(fl[lo:hi]) / (hi - lo)
        k = sum(1 for t in range(lo, hi) if fl[t - 1] and not fl[t]) / (hi - lo)
        return f, k

    def coin(rng, n, width):
        mask = (1 << (width + 1)) - 1
        row, out = 0, []
        for t in range(n):
            row = (row & ~(1 << width)) | (rng.getrandbits(1) << width)
            out.append((row >> 1) & 1)
            new = ((row << 1) ^ (row | (row >> 1))) & mask
            row = (new & ~1 & ~(1 << width)) | ((t + 1) % 2)
        return out

    def driven(cells, n):
        row, out = cells, []
        for t in range(n):
            row = (row & ~1) | (t % 2)
            out.append((row >> 1) & 1)
            row = (row << 1) ^ (row | (row >> 1))
        return out

    def summary(xs):
        m = [sum(x[i] for x in xs) / len(xs) for i in (0, 1)]
        se = [(sum((x[i] - m[i]) ** 2 for x in xs) / (len(xs) - 1) / len(xs)) ** 0.5 for i in (0, 1)]
        return m, se
    real = [rates(flags(driven(random.Random(9000 + s).getrandbits(2 * N + 64) << 1, N))) for s in range(seeds)]
    (fr, kr), (sf, sk) = summary(real)
    print('DEPTH real wide interior: clean %.4f (se %.4f), kicks per row %.5f (se %.5f)' % (fr, sf, kr, sk))
    for c in (13, 16, 20, 26, 34, 50):
        xs = [rates(flags(coin(random.Random(5000 + 97 * c + s), N, c))) for s in range(seeds)]
        (f, k), (sf, sk) = summary(xs)
        print('DEPTH coins at column %2d: clean %.4f (se %.4f), kicks per row %.5f (se %.5f), %.0f%% of real'
              % (c, f, sf, k, sk, 100 * k / kr))


if __name__ == '__main__':
    if PART in ('all', 'depth'):
        depth()
    if PART in ('all', 'n1'):
        n1()
    if PART in ('all', 'slab'):
        slab()
