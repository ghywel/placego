#!/usr/bin/env python3
"""rule30_cloud_hole_truecount.py: TC, the true one-hole language by SAT, far past OHD's direct enumeration.

RUN-ON:     cpu, one core (Python 3 and python-sat, CaDiCaL); minutes per period
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_hole_truecount.py [P=all] [NMAX=default] [CAP_SECONDS=1200]

Why. Local's offer (1) of 21:17 asks whether the true hole entropy of the walls 0 1^(p - 1) is zero at p = 5, 7, 9.
OHD (rule30_one_hole_direct.c) counted the true language exactly by simulating every initial right half, which stops
at 7, 5 and 4 holes (2^31 rows). OHC's relaxations count further, but they are only supersets. HE (CL104) measured
positive rates under random right halves, which bound nothing. This probe decides membership in the TRUE language
for much longer words.

Method. For N holes, T = (N - 1) p. The cells that can reach x1 by time T are (j, t) with j <= T + 1 - t. They are
variables, the wall column is a constant, and every update x(j, t+1) = x(j-1, t) XOR (x(j, t) OR x(j+1, t)) is a
clause set. The free variables are exactly the initial cells x(1..T+1, 0), and every assignment of them fixes the
rest, so a hole prefix (as assumptions on x(1, kp)) is satisfiable iff some actual right half realises it. One formula
at NMAX serves every shorter prefix. A depth-first search extends only realisable prefixes, so it counts |L_n|
exactly for every n <= NMAX. The language is factorial, since a right half evolved by p steps is again a right half
before a hole. So a word whose prefix and suffix are realisable and which is not realisable is a true MINIMAL
forbidden word. Let F be the minimal forbidden words found. The true language avoids F, so the number a_m of words
of length m avoiding F bounds |L_m|. By submultiplicativity a_m^(1/m) is a certified upper bound on the true growth,
for every m. It is computed in exact integers on F's Aho-Corasick automaton.

Record searched: "one.hole" (headings), "minimal forbidden", OHD, GC858, GC859 -> OH, OHC and OHD (the header of
rule30_one_hole_widths.py): exact true counts to 7, 5, 4 holes; the relaxation's minimal forbidden counts at width 22
(p = 5, lengths 5 .. 18: 1, 0, 8, 13, 14, 4, 32, 47, ...); GC859's withdrawal (minimality in a relaxation does not
transfer to the truth); the certified width-22 bounds 1.543759, 1.652210, 1.742260. No true count beyond OHD's.

PREDICTIONS, written 2026-10-09 21:45 BST, before any run of this script.
  TC-C1 (control, must hold): the counts equal OHD's: p = 5: 2, 4, 8, 16, 31, 60, 108; p = 7: 2, 4, 8, 16, 30; p = 9:
         2, 4, 8, 16.
  TC-C2 (control, must hold): 200 random realisable words per period, their SAT models replayed by direct
         simulation of the initial row, reproduce their words; and 10000 is a minimal forbidden word at p = 5.
  TC-P1 (0.6): at the largest n reached, |L_n| / |L_(n-1)| exceeds 1.3 for all three periods.
  TC-P2 (0.5): the forbidden-word bound a_m^(1/m) at m = 400 is below the width-22 bound for at least two of the
         three periods.
  TC-P3 (0.5): every period has a true minimal forbidden word at every length from 7 to the largest reached.
  TC-U, the unexpected check (0.5): at p = 5 the truth has more minimal forbidden words than the width-22 relaxation
         at some length from 6 to 12. That would mean the relaxation misses constraints already at length 12 or less.
  Counterfactual. If TC-P1 fails with the ratios falling towards 1, the zero-entropy side gains weight; HE's random
  rates would then belong to typical right halves that become rare in counts. If TC-P2 holds, the record's best
  certified ceilings come from the truth, not the relaxation.
AUDIT (GPT GC871, 2026-10-09 21:50 BST, applied before any complete run). The first launch, at 21:46, was stopped
at p = 5, n = 16 (its interim counts are in CL106 and are reproduced by the rerun). Applied: TC-C2 needs 200
replayed models, drawn by reservoir sampling over every realisable word. Each verdict is gated on its controls and
on a completed, non-empty range, and prints NOT DECIDED otherwise. The 10000 check joins the control gate. The full
forbidden set and the exact a_400 are kept in scratch (NP_SCRATCH_TC). The ceiling is certified in integers: the
smallest six-decimal c with (10^6 c)^400 >= a_400 10^2400. Scope: replays check SAT witnesses only. The UNSAT
verdicts are CaDiCaL's, with no independently checked proof, so the counts are exact only up to that solver's
verdicts. A level cut by the cap contributes its forbidden words to the bound, which is still sound, but its list
is incomplete and it is not counted as reached.
"""
import os
import random
import sys
import time

from pysat.solvers import Solver

PERIODS = [int(sys.argv[1])] if len(sys.argv) > 1 and sys.argv[1] != 'all' else [5, 7, 9]
NMAX_ARG = int(sys.argv[2]) if len(sys.argv) > 2 else None
CAP = float(sys.argv[3]) if len(sys.argv) > 3 else 1200.0
NMAX_DEFAULT = {5: 24, 7: 20, 9: 18}
OHD = {5: [2, 4, 8, 16, 31, 60, 108], 7: [2, 4, 8, 16, 30], 9: [2, 4, 8, 16]}
WIDTH22 = {5: 1.543759, 7: 1.652210, 9: 1.742260}
OHC_MFW5 = {5: 1, 6: 0, 7: 8, 8: 13, 9: 14, 10: 4, 11: 32, 12: 47}
SCRATCH = os.environ.get('NP_SCRATCH_TC', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-tc'))


def wall(t, p):
    return 0 if t % p == 0 else 1


class Triangle:
    def __init__(self, p, nmax):
        self.p, self.T = p, (nmax - 1) * p
        self.nv = 0
        self.var = {}
        self.clauses = []
        T = self.T
        for j in range(1, T + 2):
            self.var[(j, 0)] = self.new()
        for t in range(T):
            for j in range(1, T + 1 - t):
                self.var[(j, t + 1)] = self.new()
                self.update(j, t)

    def new(self):
        self.nv += 1
        return self.nv

    def update(self, j, t):
        y = self.var[(j, t + 1)]
        b, c = self.var[(j, t)], self.var[(j + 1, t)]
        o = self.new()                                     # o = b OR c
        self.clauses += [[-o, b, c], [o, -b], [o, -c]]
        if j == 1:
            a = wall(t, self.p)                           # y = a XOR o with a constant
            self.clauses += [[-y, o], [y, -o]] if a == 0 else [[y, o], [-y, -o]]
        else:
            a = self.var[(j - 1, t)]
            self.clauses += [[-y, a, o], [-y, -a, -o], [y, -a, o], [y, a, -o]]

    def hole(self, k):
        return self.var[(1, k * self.p)]


def simulate(row, p, n):
    """Direct forward simulation of an initial right half (list of bits x1 ..), returning n hole bits."""
    x = list(row) + [0, 0]
    out = []
    for t in range((n - 1) * p + 1):
        if t % p == 0:
            out.append(x[0])
        left = [wall(t, p)] + x[:-1]
        right = x[1:] + [0]
        x = [left[i] ^ (x[i] | right[i]) for i in range(len(x))]
    return out[:n]


def avoid_count_bound(F, m):
    """Exact count of binary words of length m avoiding every word in F (Aho-Corasick), and its m-th root."""
    goto, fail, out = [{}], [0], [False]
    for w in F:
        s = 0
        for ch in w:
            if ch not in goto[s]:
                goto.append({})
                fail.append(0)
                out.append(False)
                goto[s][ch] = len(goto) - 1
            s = goto[s][ch]
        out[s] = True
    from collections import deque
    q = deque()
    for ch in '01':
        if ch in goto[0]:
            fail[goto[0][ch]] = 0
            q.append(goto[0][ch])
        else:
            goto[0][ch] = 0
    while q:
        s = q.popleft()
        out[s] = out[s] or out[fail[s]]
        for ch in '01':
            if ch in goto[s]:
                u = goto[s][ch]
                fail[u] = goto[fail[s]][ch]
                q.append(u)
            else:
                goto[s][ch] = goto[fail[s]][ch]
    cnt = {0: 1}
    for _ in range(m):
        nxt = {}
        for s, c in cnt.items():
            for ch in '01':
                u = goto[s][ch]
                if not out[u]:
                    nxt[u] = nxt.get(u, 0) + c
        cnt = nxt
    a = sum(cnt.values())
    if not a:
        return 0, 0.0
    c = int(a ** (1.0 / m) * 10 ** 6)                      # float guess, then exact correction
    while (c - 1) ** m >= a * 10 ** (6 * m) and c > 1:
        c -= 1
    while c ** m < a * 10 ** (6 * m):
        c += 1
    return a, c / 10 ** 6                                  # smallest six-decimal c with c^m >= a_m


def run(p, nmax):
    t0 = time.time()
    tri = Triangle(p, nmax)
    s = Solver(name='cadical153', bootstrap_with=tri.clauses)
    holes = [tri.hole(k) for k in range(nmax)]
    levels = {0: ['']}
    models = []                                            # reservoir of (word, initial row), size 200
    seen = 0
    mfw = []
    calls = 0
    reached = 0
    for n in range(1, nmax + 1):
        prev = set(levels[n - 1])
        cur = []
        for u in levels[n - 1]:
            for b in '01':
                w = u + b
                if n >= 2 and w[1:] not in prev:
                    continue                               # a forbidden factor: w is neither minimal nor realisable
                assum = [holes[k] if w[k] == '1' else -holes[k] for k in range(n)]
                calls += 1
                if s.solve(assumptions=assum):
                    cur.append(w)
                    seen += 1
                    slot = len(models) if len(models) < 200 else random.randrange(seen)
                    if slot < 200:
                        m = s.get_model()
                        row = [1 if m[tri.var[(j, 0)] - 1] > 0 else 0 for j in range(1, tri.T + 2)]
                        if slot == len(models):
                            models.append((w, row))
                        else:
                            models[slot] = (w, row)
                else:
                    mfw.append(w)
            if time.time() - t0 > CAP:
                break
        if time.time() - t0 > CAP:
            print('p = %d: cap reached during n = %d (%d calls); stopping at n = %d' % (p, n, calls, n - 1),
                  flush=True)
            break
        levels[n] = cur
        reached = n
        nm = sum(1 for w in mfw if len(w) == n)
        print('p = %d: |L_%d| = %d  (ratio %.4f; minimal forbidden of length %d: %d; %d calls, %.0f s)' % (
            p, n, len(cur), len(cur) / max(1, len(levels[n - 1])), n, nm, calls, time.time() - t0), flush=True)
    s.delete()
    return levels, mfw, models, reached


def main():
    random.seed(7)
    os.makedirs(SCRATCH, exist_ok=True)
    summary = {}
    for p in PERIODS:
        nmax = NMAX_ARG or NMAX_DEFAULT[p]
        levels, mfw, models, reached = run(p, nmax)
        counts = [len(levels[n]) for n in range(1, reached + 1)]
        c1 = len(counts) >= len(OHD[p]) and counts[:len(OHD[p])] == OHD[p]
        c2 = len(models) >= 200 and all(simulate(row, p, len(w)) == [int(ch) for ch in w] for w, row in models)
        F = sorted(set(mfw), key=lambda w: (len(w), w))
        c3 = ('10000' in F) if p == 5 else True
        a, ceil6 = avoid_count_bound(F, 400)
        by_len = {}
        for w in F:
            by_len[len(w)] = by_len.get(len(w), 0) + 1
        with open(os.path.join(SCRATCH, 'tc_p%d.txt' % p), 'w') as fh:
            fh.write('counts %s\nreached %d\na_400 %d\nceiling %.6f\n' % (counts, reached, a, ceil6))
            fh.write('\n'.join(F) + '\n')
        ok = c1 and c2 and c3
        summary[p] = (counts, ceil6, by_len, reached, ok)
        print('p = %d: TC-C1 %s; TC-C2 %d models replayed %s%s' % (
            p, 'PASS' if c1 else 'FAIL', len(models), 'PASS' if c2 else 'FAIL',
            ('; TC-C2 10000 minimal forbidden: %s' % ('PASS' if c3 else 'FAIL')) if p == 5 else ''))
        print('p = %d: exact counts %s' % (p, counts))
        print('p = %d: minimal forbidden words by length: %s' % (p, sorted(by_len.items())))
        print('p = %d: certified ceiling from F (smallest six-decimal c with c^400 >= a_400): %.6f '
              '(width-22 bound %.6f); |F| = %d' % (p, ceil6, WIDTH22[p], len(F)), flush=True)
        print('p = %d: shortest minimal forbidden words: %s' % (p, F[:12]), flush=True)
    if len(summary) < 3:
        return
    ctl = all(v[4] for v in summary.values())
    nd = 'NOT DECIDED'
    if not ctl:
        print('controls failed: every prediction NOT DECIDED')
        return
    p1 = nd if any(len(v[0]) < 2 for v in summary.values()) else (
        'HELD' if all(v[0][-1] / v[0][-2] > 1.3 for v in summary.values()) else 'REFUTED')
    p2 = 'HELD' if sum(1 for p, v in summary.items() if v[1] < WIDTH22[p]) >= 2 else 'REFUTED'
    if any(v[3] < 7 for v in summary.values()):
        p3 = nd
    else:
        p3 = 'HELD' if all(all(v[2].get(L, 0) > 0 for L in range(7, v[3] + 1)) for v in summary.values()) \
            else 'REFUTED'
    bl5, r5 = summary[5][2], summary[5][3]
    hit = any(bl5.get(L, 0) > OHC_MFW5[L] for L in range(6, min(12, r5) + 1))
    u = 'HELD' if hit else (nd if r5 < 12 else 'REFUTED')
    print('TC-P1 (last ratio > 1.3 for all): %s' % p1)
    print('TC-P2 (certified ceiling below width 22 for >= 2 periods): %s' % p2)
    print('TC-P3 (a minimal forbidden word at every length 7 .. reached): %s' % p3)
    print('TC-U (p = 5 truth has more minimal forbidden words than width 22 at some length 6 .. 12): %s' % u)


if __name__ == '__main__':
    main()
