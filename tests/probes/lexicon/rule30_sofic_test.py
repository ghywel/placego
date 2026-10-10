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
  SOF-P4 (blind, 0.35; added before the eventual-language run, after an early look at the full language's table):
         the EVENTUAL language plateaus where the full one does not. L^(m) holds the words that can occur at visible
         index >= m (w with uw in L for some u of length m), with the start-only transients (GC986/GC987, L560/L563)
         removed. At m = 10, its near-diagonal follower-class counts vary by at most 10% over the last four lengths.
  SOF-P4b (blind, 0.35; registered on GPT's GC989 before any eventual run): the same at m = 13, where the 4,4,4,4
         core's last start (index 12) is excluded too.
  CAVEAT (GPT GC991, before any verdict): Myhill-Nerode counts are observer sizes. A finite hidden cycle can give
         exponentially many classes through the subset construction (an 8-phase example gives 255), so growth is
         inconclusive and P2's 20 .. 120 is a guess, not a necessary scale.
  SOF-P5 (blind, 0.35; registered after GC991, before its run): the synchronizing-word test. w is synchronizing at
         context j and horizon l when F_l(uw) = F_l(w) for every u in L_j with uw in L. For a sofic language its
         synchronized follower sets are the Fischer cover's states, finitely many. With j = l = 10 and k = |w| up to
         20: at k = 20 at least 10% of words synchronize, and the number of distinct synchronized classes varies by at
         most 10% over k = 17 .. 20.
  Counterfactual. A plateau says the hidden-state lift exists at these lengths and sizes it; the next step is to
  build the automaton from the classes and test it against longer words. Steady growth along the diagonal says the
  language is not regular at these lengths either; then the lift needs an unbounded counter (the kick count, say),
  which is still a precise structural fact about the kicks.
OUTCOME, 2026-10-10 08:38 BST (M5, 3 cores; the language grew to n = 40 in about 50 minutes). C1, C2 PASS; P1, P3, P4, P4b
  and P5 REFUTED; P2 not applicable.
  - C_n, n = 1 .. 40, ends ..., 9649, 10876, 12231, 13730. The SAT-grown language equals the C-enumerated one to
    n = 18. The growth ratio falls steadily: about 1.21 per symbol at n = 20, 1.16 at 30, 1.12 at 40 (0.17 bits).
    P3 REFUTED: C_40 is 8.6 n^2, not quadratic.
  - Full language (P1 REFUTED). The near-diagonal follower-class counts climb ..., 514, 598, 627, 719 (t = 37 .. 40).
    Each row levels off near C_a, so nearly every word has its own future.
  - Eventual languages (P4, P4b REFUTED). L^(10) climbs ..., 161, 187, 204, 240 and L^(13) ..., 114, 123, 148, 155,
    still about 15% a step, so the start transients are not the cause.
  - Synchronizing words (P5 REFUTED as registered). With j = l = 10, the fraction of synchronizing words rises with
    length (0, then 6% at k = 6, 13% at 10, 28% at 16, 40% at 20). Their distinct synchronized follower sets keep
    growing: 81, 103, 125, 154 at k = 17 .. 20.
  - Reading, with GC991's caveat. None of this proves the language non-sofic: a finite lift larger than these lengths
    can resolve, such as GC993's width-9 right strip with its hundreds of states, would look the same. What it shows is
    that no small lift (about 150 states or fewer) is visible to n = 40. CORRECTION (GPT GC996, accepted in L571):
    that count bounds a DETERMINISTIC observer. 719 follower classes need 719 observer states, but only about 10
    hidden states of a nondeterministic machine (2^h >= 719), so "no lift of about 150 states" holds for observers
    only. The direct test is from the dynamics, not the
    language: the least strip width w(n) for which the width-w right-strip NFA reproduces the exact language to
    length n. A bounded w(n) gives an exact finite lift; a growing w(n) means the hidden state is unbounded.
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


PHASE = int(os.environ.get('SOF_PHASE', '0'))       # 1: the phase-1 language L1 (RLK L574), a black wall first


def path(n):
    return os.path.join(DIR, ('langsat%d.txt' if PHASE == 0 else 'langsatp1_%d.txt') % n)


def load(n):
    p = path(n)
    return set(open(p).read().split()) if os.path.exists(p) else None


def member(w):
    return w, (rlk.in_language(w) if PHASE == 0 else rlk.in_language_phase(w, 1))


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


def eventual(m, nmax):
    """Follower classes of L^(m): words that occur at visible index >= m."""
    L = {n: load(n) for n in range(1, nmax + 1)}
    L[1] = {'0', '1'}
    E = {}
    for n in range(1, nmax - m + 1):
        E[n] = {u[m:] for u in L[m + n]}
    top = nmax - m
    print('eventual language L^(%d): sizes n = 1 .. %d: %s' % (m, top, [len(E[n]) for n in range(1, top + 1)]))
    table = {}
    for total in range(2, top + 1):
        fol = {}
        for u in E[total]:
            for a in range(1, total):
                fol.setdefault((a, u[:a]), set()).add(u[a:])
        for a in range(1, total):
            table[(a, total - a)] = len({frozenset(fol[(a, w)]) for w in E[a] if (a, w) in fol})
    for a in range(1, top):
        print('a=%2d ' % a + ' '.join('%4d' % table[(a, l)] for l in range(1, top - a + 1)))
    diag = {t: max(table[(a, t - a)] for a in range(max(1, t // 2 - 2), min(t, t // 2 + 3))) for t in range(4, top + 1)}
    print('near-diagonal maxima:', diag)
    last = [diag[t] for t in range(top - 3, top + 1)]
    print('SOF-P4', 'HELD' if max(last) <= 1.1 * min(last) else 'REFUTED', last)


def sync(j, l, kmax):
    """Synchronizing words (F_l(uw) = F_l(w) for all u in L_j with uw in L) and their distinct follower sets."""
    L = {n: load(n) for n in range(1, j + kmax + l + 1)}
    L[1] = {'0', '1'}
    rows = {}
    for k in range(1, kmax + 1):
        fw = {}
        for x in L[k + l]:
            fw.setdefault(x[:k], set()).add(x[k:])
        fuw = {}
        for x in L[j + k + l]:
            fuw.setdefault((x[:j], x[j:j + k]), set()).add(x[j + k:])
        bad = {w for (u, w), vs in fuw.items() if vs != fw.get(w, set())}
        good = [w for w in L[k] if w not in bad]
        cls = {frozenset(fw[w]) for w in good}
        rows[k] = (len(L[k]), len(good), len(cls))
        print('k=%2d words %6d synchronizing %6d (%.0f%%) distinct synchronized classes %5d' % (
            k, len(L[k]), len(good), 100.0 * len(good) / len(L[k]), len(cls)), flush=True)
    frac = rows[kmax][1] / rows[kmax][0]
    last = [rows[k][2] for k in range(kmax - 3, kmax + 1)]
    ok = frac >= 0.10 and max(last) <= 1.1 * min(last)
    print('SOF-P5', 'HELD' if ok else 'REFUTED', '(sync fraction %.2f at k = %d; classes %s)' % (frac, kmax, last))


def main():
    os.makedirs(DIR, exist_ok=True)
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'classes'
    if cmd == 'sync':
        sync(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif cmd == 'eventual':
        eventual(int(sys.argv[2]), int(sys.argv[3]))
    elif cmd == 'grow':
        grow(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 3)
    else:
        classes(int(sys.argv[2]) if len(sys.argv) > 2 else max(n for n in range(1, 200) if load(n) is not None))


if __name__ == '__main__':
    main()
