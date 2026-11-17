#!/usr/bin/env python3
"""rule30_strip_width.py: SW, how much of the right half does column 1's visible language need? Strip width w(n).

RUN-ON:     cpu (Python 3, kissat 4.0.4 as KISSAT); a few cores, minutes
COMMAND:    python3 tests/probes/lexicon/rule30_strip_width.py [NMAX=40] [JOBS=3]
DATA:       the exact visible language L_n, n <= 40, grown by SOF (rule30_sofic_test.py; NP_SCRATCH_RLK)

Why (the owner's steer, 2026-10-10: work one dimension up; SOF L564 .. L568 found no small lift visible to n = 40).
The visible language is the shadow of the right half's dynamics. A width-w strip keeps cells 1 .. w beside the wall
(clamped 0101, white at even times), with every initial strip allowed and a FREE input at cell w + 1 at every step.
Its visible language S_w is a superset of the true L, shrinking with w, and exact for the words of length n once w
>= 2n - 1 (the light cone). Each strip is a finite machine (2^w states), so a bounded need for width would give an
exact finite lift, the hidden coordinate made explicit. GC993 found gap order visible at width 9; GC994 found width
9 insufficient.

Method. S_w is factor-closed (any later strip state is an allowed initial one), so S_w agrees with L to length n
exactly when it excludes every minimal forbidden word f of L with |f| <= n. For each such f (extracted from L_n,
n <= 40, by RRL's rule: f absent, f[:-1] and f[1:] present), w_min(f) is the least w whose strip excludes f, found
by SAT (monotone in w; at w = 2|f| - 1 the strip is RLK's exact cone, which excludes f). Then
w(n) = max over |f| <= n of w_min(f).

Record searched: `record_find.py strip width` -> GC993/GC994 (width 9 shows gap order, and is insufficient) and §8.17
(information reaches column 1 at about 0.2 cells a step); `record_find.py "minimal forbidden"` -> RRL, RLK, L556 ..
L563; no width curve on record.

PREDICTIONS (Local's, pushed before any run of this script):
  SW-C1 (control): at w = 2|f| - 1 every minimal forbidden word is excluded (the exact cone); every sampled word of
        L_n (200 per length, n = 10, 20, 30) is admitted at w = 1 and at w = 2n - 1.
  SW-C2 (control): the minimal forbidden words of length <= 18 are RLK's 25.
  SW-P1 (blind, 0.7): the needed width grows: max w_min over words of length 31 .. 40 exceeds the max over lengths
        11 .. 20 by at least 5. So no finite strip is an exact lift.
  SW-P2 (blind, 0.5): for |f| >= 25 the median w_min(f) / |f| lies between 0.3 and 0.7, near the information speed
        (about 0.2 cells a step over 2|f| steps).
  SW-P3 (the unexpected check, 0.5): some minimal forbidden word of length >= 25 is already excluded at w <= 9, a
        long but narrow constraint.
  Counterfactual. If w(n) stops growing, the strip of that width is an exact finite machine for column 1, the lifted
  automaton GC970 can take as input. If it grows linearly, the hidden coordinate is unbounded, about c n cells for
  words of length n, and a proof must handle an unbounded right context (as the records' slow climb suggests).
OUTCOME, 2026-10-10 08:45 BST (M5, 3 cores, under two minutes): C1, C2 PASS; P1, P2 HELD; P3 REFUTED.
  - There are 771 minimal forbidden words to length 40, and their number per length grows (8 at length 19, 71 at
    length 40). C2: the 25 to length 18 are RLK's.
  - w(n) = 7 at n = 10, 18 at n = 20, 27 at n = 30 and 35 at n = 40 (full table in L570's run output).
  - P1 HELD: the largest w_min over lengths 11 .. 20 is 18, and over 31 .. 40 it is 35.
  - P2 HELD: the median w_min/|f| for |f| >= 25 is 0.62.
  - P3 REFUTED: no word of length >= 25 is excluded at w <= 9.
  - Reading. The width of right half needed grows about linearly, 0.6 .. 0.9 n cells.
  - CORRECTION (GPT GC996, accepted in L571). The result is a finite lower bound: free-boundary strips of width <= 34
    are not exact to length 40. It does not show that no finite strip, or no other finite encoding, is an exact lift,
    and "the hidden coordinate is unbounded" overreached.
"""
import os
import subprocess
import sys
import tempfile
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_sofic_test as sof                              # noqa: E402  (the grown language)
sys.argv = _argv
DIR = sof.DIR
KISSAT = os.environ.get('KISSAT', 'kissat')
RLK25 = ('11 00000 101001 0100101 010010001 0101000101 0101010000 01010001001 10010001001 010010000101 010100010001 '
         '100100010000 0001000010001 1001000010001 00100010000101 01000010001001 10101000010000 001000100001001 '
         '010000100010000 0101000010000101 1000100001010001 00100010001010100 001000010001010100 010000101000010001 '
         '010001000100010101').split()


def strip_admits(f, w):
    """Is the visible word f produced by some width-w strip (free initial strip, free input at cell w + 1)?"""
    k = len(f)
    T = 2 * k - 2
    var, nv, cl = {}, [0], []

    def v(key):
        if key not in var:
            nv[0] += 1
            var[key] = nv[0]
        return var[key]
    for t in range(T):
        for i in range(1, w + 1):
            if i > 2 * k - 1 - t:                               # outside the cone of column 1 at time T
                continue
            y, c = v(('x', t + 1, i)), v(('x', t, i))
            r = v(('x', t, i + 1)) if i < w else v(('b', t))     # the free boundary input at cell w + 1
            nv[0] += 1
            o = nv[0]
            cl += [[-c, o], [-r, o], [c, r, -o]]
            if i == 1:                                          # left input: the wall, t mod 2
                cl += ([[-y, -o], [y, o]] if t % 2 else [[-y, o], [y, -o]])
            else:
                l = v(('x', t, i - 1))
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for s, b in enumerate(f):
        x = v(('x', 2 * s, 1))
        cl.append([x] if b == '1' else [-x])
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', dir=DIR, delete=False) as fh:
        fh.write('p cnf %d %d\n' % (nv[0], len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
        name = fh.name
    try:
        rc = subprocess.run([KISSAT, '-q', '-n', name], capture_output=True).returncode
    finally:
        os.unlink(name)
    assert rc in (10, 20), rc
    return rc == 10


def wmin(f):
    lo, hi = 1, 2 * len(f) - 1                                  # admits at lo? excluded at hi (C1 checks hi)
    if strip_admits(f, hi):
        return f, None                                          # C1 failure: the exact cone admits f
    if not strip_admits(f, lo):
        return f, lo
    while hi - lo > 1:                                          # invariant: admits at lo, excluded at hi
        mid = (lo + hi) // 2
        if strip_admits(f, mid):
            lo = mid
        else:
            hi = mid
    return f, hi


def admitted(args):
    word, w = args
    return strip_admits(word, w)


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    jobs = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    L = {n: sof.load(n) for n in range(1, nmax + 1)}
    L[1] = {'0', '1'}
    mfw = []
    for n in range(2, nmax + 1):
        for w in sorted(L[n - 1]):
            for b in '01':
                u = w + b
                if u not in L[n] and u[1:] in L[n - 1]:
                    mfw.append(u)
    short = [f for f in mfw if len(f) <= 18]
    print('minimal forbidden words up to length %d: %d; per length %s' % (
        nmax, len(mfw), {n: sum(len(f) == n for f in mfw) for n in range(2, nmax + 1)}), flush=True)
    c2 = sorted(short) == sorted(RLK25)
    print('SW-C2', 'PASS' if c2 else 'FAIL', flush=True)
    t0 = time.time()
    with Pool(jobs) as pool:
        res = dict(pool.map(wmin, mfw, chunksize=1))
        sample = []
        for n in (10, 20, 30):
            ws = sorted(L[n])[:: max(1, len(L[n]) // 200)][:200]
            sample += [(u, 1) for u in ws] + [(u, 2 * n - 1) for u in ws]
        adm = pool.map(admitted, sample, chunksize=4)
    c1 = all(v is not None for v in res.values()) and all(adm)
    print('SW-C1', 'PASS' if c1 else 'FAIL', '(%.0f s)' % (time.time() - t0), flush=True)
    for f in mfw:
        print('  |f| = %2d  w_min = %s  %s' % (len(f), res[f], f))
    wn = {}
    best = 0
    for n in range(2, nmax + 1):
        best = max([best] + [res[f] for f in mfw if len(f) == n and res[f] is not None])
        wn[n] = best
    print('w(n) = max w_min over |f| <= n:', wn)
    m1 = max([res[f] for f in mfw if 11 <= len(f) <= 20] + [0])
    m2 = max([res[f] for f in mfw if 31 <= len(f) <= 40] + [0])
    print('SW-P1', 'HELD' if m2 >= m1 + 5 else 'REFUTED', '(max w_min: lengths 11 .. 20 -> %d, 31 .. 40 -> %d)' % (m1, m2))
    ratios = sorted(res[f] / len(f) for f in mfw if len(f) >= 25 and res[f] is not None)
    med = ratios[len(ratios) // 2] if ratios else None
    print('SW-P2', 'HELD' if med is not None and 0.3 <= med <= 0.7 else 'REFUTED', '(median w_min/|f|, |f| >= 25: %s)' % med)
    narrow = [f for f in mfw if len(f) >= 25 and res[f] is not None and res[f] <= 9]
    print('SW-P3', 'HELD' if narrow else 'REFUTED', '(%d long words excluded at w <= 9)' % len(narrow))


if __name__ == '__main__':
    main()
