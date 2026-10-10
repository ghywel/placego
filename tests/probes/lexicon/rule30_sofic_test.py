#!/usr/bin/env python3
"""rule30_sofic_test.py: SOF, is column 1's visible language beside the 0101 wall regular (sofic)? Myhill-Nerode.

RUN-ON:     cpu (Python 3, kissat 4.0.4 as KISSAT); a few cores
COMMAND:    python3 tests/probes/lexicon/rule30_sofic_test.py grow NMAX [JOBS]   (exact language by SAT, resumable)
            python3 tests/probes/lexicon/rule30_sofic_test.py classes [NMAX]     (follower-class table and verdicts)
COST:       minutes to an hour; data in NP_SCRATCH_RLK (default ~/np-scratch-int/rule30-rlk), never in git.

Why (the owner's question of 2026-10-10, "what would a 2-dimensional irrational look like", Euler and quaternions:
work one dimension up). RLK (L555 .. L559) found the visible language is not of finite type at any K <= 18: each
longer forbidden-word list moves the records' first excess deeper, and the next missing word sits just past the
list (lengths 14, 17, 21). A sofic language is the shadow of a finite-type one with a hidden coordinate (Weiss): its
forbidden words can be unboundedly long while a finite automaton still recognises it, as for the even shift. The
natural hidden coordinate is the wheel's phase, the 17/56 rotation on the 8 x 7 torus. If the visible language is
regular, its Myhill-Nerode right classes (words with the same set of possible futures) are finitely many, and the
automaton they form is the lifted machine GC970's certificate format can take as input.

Method. The language is RLK's: column 1 at the wall's white times, from an arbitrary right half, from a white start
(factor- and prefix-closed). `grow` extends it level by level: L_(n+1) = {wb : w in L_n, b in {0, 1}, wb[1:] in L_n,
wb in L}, membership by RLK's in_language (SAT over the right cone of the last visible symbol, kissat). `classes`
computes, for every split a + l <= NMAX, N(a, l) = the number of distinct exact-length follower sets
F_l(w) = {v : |v| = l, wv in L} over w in L_a. A regular language with s right classes has N(a, l) <= s for every a
and l; a non-regular one has N(a, l) unbounded as a and l grow together.

Record searched: `record_find.py sofic` -> 12 hits in 4 files, none on this language:
  - PERIOD-TWO §6: §8.20's channel is a sofic UPPER constraint on column 1, a relaxation;
  - PRIOR-ART: the Kari-Kopra p/q automaton's trace subshift is neither sofic nor synchronising (arXiv:2005.05112;
    Mahler's problem, not Rule 30), a reminder that cellular-automaton traces are often non-sofic;
  - CONSTELLATION E: Rule 30's width-2 trace would be sofic given right pseudo-orbit tracing (Jalonen and Kari 2020),
    an open candidate question.
  `Myhill` and `"follower set"` -> no hit. RLK (L555 .. L563) and RRL (CL041) hold the language to length 18.

PREDICTIONS (Local's, pushed before any run of this script):
  SOF-C1 (control): the SAT-grown L_n equals RLK's C-enumerated language for every n <= 18 (C_18 = 487 words).
  SOF-C2 (control): every SAT-grown level is prefix- and factor-closed, and C_n is non-decreasing.
  SOF-P1 (blind, 0.4): regular-looking. At the largest NMAX reached (at least 32), the diagonal counts
         N(a, NMAX - a) for a near NMAX / 2 vary by at most 10% over the last four NMAX values, below 400.
  SOF-P2 (blind, 0.35): if a plateau appears, its size is between 20 and 120, the scale of the wheel's 28 visible or
         56 temporal phases.
  SOF-P3 (the unexpected check, 0.5): C_n keeps growing roughly quadratically to NMAX, between 1.0 and 1.6 n^2 at
         n = NMAX (C_18 = 487 = 1.50 n^2).
  Counterfactual. A plateau says the hidden-state lift exists at these lengths and sizes it; the next step is to
  build the automaton from the classes and test it against longer words. Steady growth along the diagonal says the
  language is not regular at these lengths either; then the lift needs an unbounded counter (the kick count, say),
  which is still a precise structural fact about the kicks.
"""
import os
import sys
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_relaxed_records_k as rlk                       # noqa: E402  (in_language, the C-enumerated language)
sys.argv = _argv
DIR = rlk.DIR


def path(n):
    return os.path.join(DIR, 'langsat%d.txt' % n)


def load(n):
    p = path(n)
    return set(open(p).read().split()) if os.path.exists(p) else None


def member(w):
    return w, rlk.in_language(w)


def grow(nmax, jobs=3):
    L = {1: {'0', '1'}}
    for n in range(2, nmax + 1):
        got = load(n)
        if got is not None:
            L[n] = got
            continue
        prev = L[n - 1]
        cand = sorted(w + b for w in prev for b in '01' if (w + b)[1:] in prev)
        t0 = time.time()
        with Pool(jobs) as pool:
            res = pool.map(member, cand, chunksize=8)
        L[n] = {w for w, ok in res if ok}
        with open(path(n) + '.tmp', 'w') as f:
            f.write('\n'.join(sorted(L[n])) + '\n')
        os.replace(path(n) + '.tmp', path(n))
        print('n=%2d candidates %5d words %5d (%.0f s)' % (n, len(cand), len(L[n]), time.time() - t0), flush=True)
    return L


def controls(L, nmax):
    ref = rlk.language(18)
    c1 = all(L[n] == ref[n] for n in range(1, 19) if n in L)
    c2 = all(all(w[:-1] in L[n - 1] and w[1:] in L[n - 1] for w in L[n]) for n in range(2, nmax + 1))
    c2 &= all(len(L[n]) >= len(L[n - 1]) for n in range(2, nmax + 1))
    return c1, c2


def classes(nmax):
    L = {n: load(n) for n in range(1, nmax + 1)}
    L[1] = {'0', '1'}
    if any(L[n] is None for n in range(1, nmax + 1)):
        raise SystemExit('grow to %d first' % nmax)
    c1, c2 = controls(L, nmax)
    print('C_n, n = 1 .. %d: %s' % (nmax, [len(L[n]) for n in range(1, nmax + 1)]))
    print('SOF-C1', 'PASS' if c1 else 'FAIL', ' SOF-C2', 'PASS' if c2 else 'FAIL')
    table = {}
    for total in range(2, nmax + 1):
        fol = {}
        for u in L[total]:
            for a in range(1, total):
                fol.setdefault((a, u[:a]), set()).add(u[a:])
        for a in range(1, total):
            l = total - a
            sets = {frozenset(fol[(a, w)]) for w in L[a] if (a, w) in fol}
            table[(a, l)] = len(sets)
    print('N(a, l): rows a, columns l (a + l <= %d)' % nmax)
    for a in range(1, nmax):
        print('a=%2d ' % a + ' '.join('%4d' % table[(a, l)] for l in range(1, nmax - a + 1)))
    diag = {t: max(table[(a, t - a)] for a in range(max(1, t // 2 - 2), min(t, t // 2 + 3))) for t in range(4, nmax + 1)}
    print('near-diagonal maxima N(~t/2, ~t/2) by total length t:', diag)
    last = [diag[t] for t in range(nmax - 3, nmax + 1)]
    p1 = nmax >= 32 and max(last) <= 1.1 * min(last) and max(last) < 400
    print('SOF-P1', 'HELD' if p1 else 'REFUTED', last)
    print('SOF-P2', ('HELD' if 20 <= max(last) <= 120 else 'REFUTED') if p1 else 'not applicable (no plateau)')
    c = len(L[nmax]) / nmax ** 2
    print('SOF-P3', 'HELD' if 1.0 <= c <= 1.6 else 'REFUTED', 'C_%d / %d^2 = %.3f' % (nmax, nmax, c))


def main():
    os.makedirs(DIR, exist_ok=True)
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'classes'
    if cmd == 'grow':
        grow(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 3)
    else:
        classes(int(sys.argv[2]) if len(sys.argv) > 2 else max(n for n in range(1, 200) if load(n) is not None))


if __name__ == '__main__':
    main()
