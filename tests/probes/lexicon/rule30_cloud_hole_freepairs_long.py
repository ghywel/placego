#!/usr/bin/env python3
"""rule30_cloud_hole_freepairs_long.py: FP2, the free pairs of FP (CL114) on far longer hole words, by SAT.

RUN-ON:     cpu, one core (Python 3, python-sat via rule30_cloud_hole_truecount.py); up to about an hour
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_hole_freepairs_long.py [CAP_SECONDS_PER_FAMILY=1200]

Why. FP found pairs of hole words whose every concatenation is realised as far as TC's exact language reaches:
(000, 001) at p = 9 to 14 holes, (00, 010) at p = 7 to 15, and (10, 111000) at p = 5 to 17. That is four or five
blocks. A pair free for ever would bound the true entropy below (1/3 bit a hole at p = 9), and so settle Local's
question for that wall. This probe tests the pairs on words two to three times longer, with TC's exact light-cone
formula (every assignment of the initial cells is an actual right half, so SAT means realised). It also reads one
property of the realising right halves that a construction would need: whether cells beyond half the light cone
can be white.

Record searched: "free pair", "free code" -> FP (rule30_cloud_hole_freepairs.py) and CL114 only.

PREDICTIONS, written 2026-10-09 22:58 BST, before any run of this script.
  FP2-C1 (control, must hold): every SAT model replays to its word by direct simulation.
  FP2-C2 (control, must hold): every concatenation of total length at most FP's N is SAT, as FP decided.
  FP2-P1 (0.6): p = 9: all 1,024 concatenations of 10 blocks from (000, 001), 30 holes, are realised.
  FP2-P2 (0.5): p = 7: all 1,024 concatenations of 10 blocks from (00, 010) are realised.
  FP2-P3 (0.4): p = 5: all 64 concatenations of 6 blocks from (10, 111000) are realised.
  FP2-P4 (0.5): p = 9: 30 random concatenations of 15 blocks, 45 holes, are all realised.
  FP2-U, the unexpected check (0.5): at p = 9, 32 random 10-block words are still realised when every initial cell
         beyond half the light cone (position > 9 * 29 / 2) is forced white.
  Counterfactual. A failing word is a true forbidden word of the family, so the pair is not free and gives no
  bound. P1 holding is evidence, not proof; a proof needs a construction for every length.
"""
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_cloud_hole_truecount as tc                       # noqa: E402
from pysat.solvers import Solver                               # noqa: E402
sys.argv = _argv

CAP = float(sys.argv[1]) if len(sys.argv) > 1 else 1200.0
FAMILIES = [(9, ('000', '001'), 10, 14), (7, ('00', '010'), 10, 15), (5, ('10', '111000'), 6, 17)]


def model_row(s, tri):
    m = s.get_model()
    return [1 if m[tri.var[(j, 0)] - 1] > 0 else 0 for j in range(1, tri.T + 2)]


def run_family(p, pair, K, N_fp, rng, extra=None):
    nmax = K * max(len(pair[0]), len(pair[1]))
    if extra:
        nmax = max(nmax, extra[0] * max(len(pair[0]), len(pair[1])))
    t0 = time.time()
    tri = tc.Triangle(p, nmax)
    s = Solver(name='cadical153', bootstrap_with=tri.clauses)
    holes = [tri.hole(k) for k in range(nmax)]

    def realise(w, white_beyond=None):
        assum = [holes[k] if w[k] == '1' else -holes[k] for k in range(len(w))]
        if white_beyond is not None:
            assum += [-tri.var[(j, 0)] for j in range(white_beyond + 1, tri.T + 2)]
        return s.solve(assumptions=assum)
    fails, replay_bad, short_bad, n = [], 0, 0, 0
    for bits in range(1 << K):
        if time.time() - t0 > CAP:
            break
        w = ''.join(pair[(bits >> b) & 1] for b in range(K))
        n += 1
        if realise(w):
            row = model_row(s, tri)
            if tc.simulate(row, p, len(w)) != [int(c) for c in w]:
                replay_bad += 1
        else:
            fails.append(w)
        # C2: the prefix of whole blocks of total length <= N_fp
        k, L = 0, 0
        while k < K and L + len(pair[(bits >> k) & 1]) <= N_fp:
            L += len(pair[(bits >> k) & 1])
            k += 1
        if not realise(w[:L]):
            short_bad += 1
    out = {'n': n, 'total': 1 << K, 'fails': fails, 'replay_bad': replay_bad, 'short_bad': short_bad,
           'secs': time.time() - t0}
    if extra:
        K2, cnt = extra[0], extra[1]
        f2 = []
        for _ in range(cnt):
            w = ''.join(pair[rng.randrange(2)] for _ in range(K2))
            if not realise(w):
                f2.append(w)
        out['long_fails'] = f2
        half = (9 * 29) // 2
        u_fail = 0
        for _ in range(32):
            w = ''.join(pair[rng.randrange(2)] for _ in range(K))
            if not realise(w, white_beyond=half):
                u_fail += 1
        out['u_fail'] = u_fail
    s.delete()
    return out


def main():
    rng = random.Random(9)
    res = {}
    for p, pair, K, N_fp in FAMILIES:
        extra = (15, 30) if p == 9 else None
        r = run_family(p, pair, K, N_fp, rng, extra)
        res[p] = r
        print('p = %d, pair %s, %d blocks: %d of %d tested, %d unrealised (first: %s); replay failures %d; '
              'short-prefix failures %d; %.0f s%s' % (
                  p, pair, K, r['n'], r['total'], len(r['fails']), r['fails'][:3], r['replay_bad'], r['short_bad'],
                  r['secs'], ('; 15-block random: %d of 30 unrealised; white beyond half the cone: %d of 32 '
                              'unrealised' % (len(r['long_fails']), r['u_fail'])) if extra else ''), flush=True)
    c1 = all(r['replay_bad'] == 0 for r in res.values())
    c2 = all(r['short_bad'] == 0 for r in res.values())
    print('FP2-C1 (every model replays): %s' % ('PASS' if c1 else 'FAIL'))
    print('FP2-C2 (prefixes within FP\'s N all realised): %s' % ('PASS' if c2 else 'FAIL'))
    nd = 'NOT DECIDED'
    ok = c1 and c2

    def full(p):
        r = res[p]
        return nd if not ok or r['n'] < r['total'] else ('HELD' if not r['fails'] else 'REFUTED')
    print('FP2-P1 (p = 9, all 1,024 realised): %s' % full(9))
    print('FP2-P2 (p = 7, all 1,024 realised): %s' % full(7))
    print('FP2-P3 (p = 5, all 64 realised): %s' % full(5))
    print('FP2-P4 (p = 9, 30 random 15-block words realised): %s' % (
        nd if not ok else ('HELD' if not res[9]['long_fails'] else 'REFUTED')))
    print('FP2-U (p = 9, white beyond half the cone, 32 words): %s' % (
        nd if not ok else ('HELD' if res[9]['u_fail'] == 0 else 'REFUTED')))


if __name__ == '__main__':
    main()
