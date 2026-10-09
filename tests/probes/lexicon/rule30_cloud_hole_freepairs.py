#!/usr/bin/env python3
"""rule30_cloud_hole_freepairs.py: FP, free pairs in the true one-hole language (the construction route of CL104).

RUN-ON:     cpu, one core (Python 3 standard library); seconds
COMMAND:    NP_SCRATCH_TC=... python3 tests/probes/lexicon/rule30_cloud_hole_freepairs.py [LMAX=6]

Why. A lower bound on the true hole entropy needs exponentially many realised words. The simplest witness would be
a pair of hole words u != v, neither a prefix of the other, such that every concatenation of copies of u and v is
realised: then |L_n| >= 2^(n / max(|u|, |v|)) up to a constant, and the true entropy is at least 1/max(|u|, |v|)
bits a hole. TC (rule30_cloud_hole_truecount.py) leaves, for each period, the complete set F of true minimal
forbidden words up to the length it reached, N. A word of length at most N is realised exactly when it has no factor
in F, because the language is factorial. So "every concatenation of length at most N is realised" can be decided
exactly from F. Beyond N it is a hypothesis that a construction would have to prove.

Method. For each period, every pair (u, v) of words of lengths 1 .. LMAX, neither a prefix of the other, is tested.
An automaton over F's Aho-Corasick states explores every {u, v}-concatenation, stopping at total length N. The pair
passes when no reachable state outputs a forbidden word. Pairs are reported with the longest of the two words as
short as possible. A greedy free code of words of one length ell (every concatenation of them realised to N) is
also built, which gives the bound log2(size)/ell; greedy, so it may be smaller than the largest such code.

Record searched: "free (pair|code|concatenation)", "lower bound" with "one.hole" -> CL104 (this lane, the plan);
no free code is in the record.

PREDICTIONS, written 2026-10-09 22:07 BST, before TC's outcome was read and before any run of this script.
  FP-C1 (control, must hold): for each period the pair (u, v) = (0, 1) fails, since F is not empty; and at p = 5 the
         code {0} passes and {1, 0^4} fails (10000 is forbidden).
  FP-P1 (0.6): at p = 9 some free pair has max(|u|, |v|) <= 4, which bounds the entropy below by 1/4 bit a hole as far
         as N reaches.
  FP-P2 (0.5): at p = 5 no free pair has max(|u|, |v|) <= 3.
  FP-P3 (0.5): the best free code of a fixed length ell = 6 gives log2(size)/6 within a factor of 2 of HE's measured
         rates, about 0.11 (p = 5, h_12), 0.36 (p = 7) and 0.56 (p = 9) bits a hole.
  FP-U, the unexpected check (0.4): at every period the free pair with the shortest max length uses words with equal
         numbers of 1s.
  Counterfactual. If FP-P1 fails at every LMAX, short free pairs do not exist and a construction must use long
  blocks or genuinely non-free structure. A pass is evidence only to length N, not a proof.
"""
import itertools
import math
import os
import sys
from collections import deque

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
SCRATCH = os.environ.get('NP_SCRATCH_TC', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-tc'))


def load(p):
    with open(os.path.join(SCRATCH, 'tc_p%d.txt' % p)) as fh:
        lines = fh.read().split('\n')
    reached = int(lines[1].split()[1])
    F = [w for w in lines[4:] if w]
    return reached, F


class AC:
    def __init__(self, F):
        self.goto, self.fail, self.out = [{}], [0], [False]
        for w in F:
            s = 0
            for ch in w:
                if ch not in self.goto[s]:
                    self.goto.append({})
                    self.fail.append(0)
                    self.out.append(False)
                    self.goto[s][ch] = len(self.goto) - 1
                s = self.goto[s][ch]
            self.out[s] = True
        q = deque()
        for ch in '01':
            if ch in self.goto[0]:
                q.append(self.goto[0][ch])
            else:
                self.goto[0][ch] = 0
        while q:
            s = q.popleft()
            self.out[s] = self.out[s] or self.out[self.fail[s]]
            for ch in '01':
                if ch in self.goto[s]:
                    u = self.goto[s][ch]
                    self.fail[u] = self.goto[self.fail[s]][ch]
                    q.append(u)
                else:
                    self.goto[s][ch] = self.goto[self.fail[s]][ch]

    def run(self, s, w):
        for ch in w:
            s = self.goto[s][ch]
            if self.out[s]:
                return None
        return s


def free(ac, code, N):
    """Every concatenation of code words of total length <= N avoids F. States: (automaton state, length)."""
    seen = set()
    stack = [(0, 0)]
    while stack:
        s, n = stack.pop()
        for w in code:
            if n + len(w) > N:
                # a partial last word: every prefix of w must also be safe
                t = ac.run(s, w[:N - n])
                if t is None:
                    return False
                continue
            t = ac.run(s, w)
            if t is None:
                return False
            key = (t, n + len(w))
            if key not in seen:
                seen.add(key)
                stack.append(key)
    return True


def words(L):
    return [''.join(b) for b in itertools.product('01', repeat=L)]


def main():
    measured = {5: 0.11, 7: 0.36, 9: 0.56}
    res = {}
    for p in (5, 7, 9):
        N, F = load(p)
        ac = AC(F)
        c1 = not free(ac, ['0', '1'], N)
        if p == 5:
            c1 = c1 and free(ac, ['0'], N) and not free(ac, ['1', '0000'], N)
        best = None
        for m in range(1, LMAX + 1):
            cands = [w for L in range(1, m + 1) for w in words(L)]
            for u, v in itertools.combinations(cands, 2):
                if max(len(u), len(v)) != m or u.startswith(v) or v.startswith(u):
                    continue
                if free(ac, [u, v], N):
                    best = (m, u, v)
                    break
            if best:
                break
        # greedy largest free code of words of length 6
        ell = 6
        code = []
        for w in words(ell):
            if free(ac, code + [w], N):
                code.append(w)
        rate = math.log2(len(code)) / ell if len(code) > 1 else 0.0
        res[p] = (N, len(F), c1, best, len(code), rate, code[:8])
        print('p = %d: N = %d, |F| = %d; control %s; shortest free pair %s; greedy free code of length 6: %d words, '
              'log2(size)/6 = %.3f; first words %s' % (p, N, len(F), 'PASS' if c1 else 'FAIL', best, len(code), rate,
                                                        code[:8]), flush=True)
    ok = all(v[2] for v in res.values())
    nd = 'NOT DECIDED (controls)'
    b9 = res[9][3]
    print('FP-P1 (p = 9 free pair with max length <= 4): %s' % (nd if not ok else (
        'HELD' if b9 and b9[0] <= 4 else 'REFUTED')))
    b5 = res[5][3]
    print('FP-P2 (p = 5 has no free pair with max length <= 3): %s' % (nd if not ok else (
        'HELD' if not b5 or b5[0] > 3 else 'REFUTED')))
    p3 = all(measured[p] / 2 <= res[p][5] <= 2 * measured[p] for p in res)
    print('FP-P3 (greedy code rate within a factor 2 of HE): %s' % (nd if not ok else ('HELD' if p3 else 'REFUTED')))
    u = all(v[3] and v[3][1].count('1') == v[3][2].count('1') for v in res.values())
    print('FP-U (shortest free pairs have equal numbers of 1s): %s' % (nd if not ok else ('HELD' if u else 'REFUTED')))


if __name__ == '__main__':
    main()
