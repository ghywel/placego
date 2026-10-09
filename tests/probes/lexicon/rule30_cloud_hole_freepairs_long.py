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
OUTCOME, 2026-10-10 00:07 BST (run at commit 03d1f06; STOPPED by Cloud after 67 minutes of CPU, inside p = 9's
  45-hole tail, where single calls were taking minutes): FP2-C1 PASS and FP2-C2 PASS on everything tested;
  FP2-P1 REFUTED, FP2-P4 REFUTED; FP2-P2, FP2-P3 and FP2-U NOT DECIDED (stopped before p = 7, p = 5 and the
  locality check).
  - How the partial results were read. The process never printed: its p = 9 family was still in the 15-block loop.
    Its local variables were read with py-spy (dump --locals, read-only) just before it was stopped.
  - p = 9, 10 blocks: the 1,200 s cap stopped the loop after 109 of 1,024 words, each call about 11 s on the
    45-hole formula. One is unrealised: 001001001000000001001000000000, 30 holes. Every realised 10-block word's
    model replayed, and every prefix within FP's N = 14 was realised. The 15-block words' models were not replayed
    (C1's scope, corrected after GPT's GC900).
  - That word was re-checked independently: kissat 4.0.4 on a fresh CNF of the 30-hole formula (68,644 variables,
    238,845 clauses, the hole bits as unit clauses) says UNSATISFIABLE. So it is a true forbidden word. Two solvers
    agree, though neither UNSAT is DRAT-checked.
  - p = 9, 15 blocks: 2 of the first 5 random words were unrealised (001001001000000000001001000001000001000001001
    and 000001001001000000000001000001001000000000001).
  - Reading. (000, 001) is NOT free at p = 9. Its freedom to 14 holes was local, since a constraint first bites
    within 30 holes. So FP's pairs are not lower-bound witnesses as they stand. A construction needs blocks that
    carry long-range structure, or a set of block words closed under the true constraints.
  - Lesson for the instrument: the formula should match each word's length, and each call needs a conflict
    budget, so that one hard call cannot hold a whole family.
AUDIT (GPT GC900, 2026-10-10 00:15 BST, applied 00:22 for any future run; the stopped run and its stated
  verdicts stand as written). Four fixes:
  - full() now REFUTES on any found failure once the controls pass, and HELD needs a completed family.
  - Each call has a conflict budget (BUDGET, default 2e6), and an exhausted call is recorded as UNKNOWN, not as
    unrealised.
  - The 15-block and white-tail loops now replay their SAT models too, and C1 covers every loop.
  - The time cap is now checked in every loop.
AUDIT 2 (GPT GC902, 2026-10-10 00:26 BST; applied by Cloud 00:30, for any future run; no rerun, the lane is
  parked). Every loop now keeps its own counts (attempted, then SAT, UNSAT or UNKNOWN), and verdicts() is a pure
  function of the results, so it can be tested without a solver.
  - C2 runs first, on its whole registered coverage (every whole-block concatenation of length 1 .. N: 30 words at
    p = 9 with N = 14, 112 at p = 7, 39 at p = 5, as GPT's GC905 counted; 6 only in the micro-run's N = 6), so no cap
    can cut it short. It PASSES only when every one of those calls is SAT, FAILS on any UNSAT, and is
    otherwise NOT DECIDED.
  - P4 and U, like P1 to P3: REFUTED on any UNSAT once the controls pass; HELD only when all 30 (32) registered
    calls were attempted and returned SAT; otherwise NOT DECIDED.
  - U's SAT models are decoded and checked to be white beyond half the cone, as well as replayed (now part of C1).
  - The caps remain elapsed-time checks between calls; a conflict budget is not a wall-clock deadline (GC902).
  Fixture predictions, written 00:30 BST before the fixtures were run (scratch harness, mocked results):
  F1, partial main loop, no failure, empty extras: P1, P4, U NOT DECIDED. F2, complete main loop with one UNKNOWN:
  P1 NOT DECIDED. F3, partial main loop with one failure: P1 REFUTED, P4 and U NOT DECIDED. F4, a 15-block UNSAT
  beside an UNKNOWN: P4 REFUTED. F5, one C2 prefix UNKNOWN: C2 and every P NOT DECIDED. F6, a U model black in its
  tail: C1 FAIL. F7, everything complete and SAT: both controls PASS and every P HELD.
  Unexpected check (a real micro-run, p = 9, 4-block words and two 10-block words on a 30-hole formula): the decoded
  rows of U's models are white beyond cell 130, and every model replays (0.95; a failure would be a decoding bug).
  Fixture and micro-run OUTCOME, 2026-10-10 00:33 BST: F1 to F7 PASS, all seven as predicted
  (rule30_cloud_hole_freepairs_long_selftest.py, no solver). Unexpected check HELD: the micro-run (run_family with
  p = 9, K = 4, N = 6, extra (10, 2), 80 s beside RR3's four kissat calls) gave C2 6 of 6 SAT, 16 of 16 main, 2 of 2
  ten-block and 32 of 32 U calls SAT, no UNKNOWN, no replay or white-tail failure. Scope: U's 4-block words reach
  only cells up to 100, so there the white tail tests decoding, not realisability. Post hoc, a negative control:
  without the white assumptions the same formula's model for 000001000001 is black at 132 of the 132 cells beyond
  130, so the tail check can fire.
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
BUDGET = int(sys.argv[2]) if len(sys.argv) > 2 else 2000000          # conflicts per SAT call (GC900)
FAMILIES = [(9, ('000', '001'), 10, 14), (7, ('00', '010'), 10, 15), (5, ('10', '111000'), 6, 17)]


def model_row(s, tri):
    m = s.get_model()
    return [1 if m[tri.var[(j, 0)] - 1] > 0 else 0 for j in range(1, tri.T + 2)]


def new_counts():
    """Per-loop call counts (GC902): attempted, then one of SAT, UNSAT, UNKNOWN once the call returns."""
    return {'attempted': 0, 'sat': 0, 'unsat': 0, 'unknown': 0}


def block_prefixes(pair, N):
    """C2's registered coverage: every concatenation of whole blocks with total length 1 .. N, deduplicated."""
    out, stack = set(), ['']
    while stack:
        w = stack.pop()
        for b in pair:
            v = w + b
            if len(v) <= N and v not in out:
                out.add(v)
                stack.append(v)
    return sorted(out, key=lambda v: (len(v), v))


def run_family(p, pair, K, N_fp, rng, extra=None):
    nmax = K * max(len(pair[0]), len(pair[1]))
    if extra:
        nmax = max(nmax, extra[0] * max(len(pair[0]), len(pair[1])))
    t0 = time.time()
    tri = tc.Triangle(p, nmax)
    s = Solver(name='cadical153', bootstrap_with=tri.clauses)
    holes = [tri.hole(k) for k in range(nmax)]
    stats = {'replay_bad': 0, 'tail_bad': 0}

    def realise(w, cnt, white_beyond=None):
        """True (realised, model replayed), False (unrealised) or None (budget exhausted: UNKNOWN)."""
        assum = [holes[k] if w[k] == '1' else -holes[k] for k in range(len(w))]
        if white_beyond is not None:
            assum += [-tri.var[(j, 0)] for j in range(white_beyond + 1, tri.T + 2)]
        cnt['attempted'] += 1
        s.conf_budget(BUDGET)
        r = s.solve_limited(assumptions=assum)
        cnt['sat' if r else ('unsat' if r is False else 'unknown')] += 1
        if r:
            row = model_row(s, tri)
            if tc.simulate(row, p, len(w)) != [int(c) for c in w]:
                stats['replay_bad'] += 1
            if white_beyond is not None and any(row[white_beyond:]):      # row[j - 1] is cell j (GC902)
                stats['tail_bad'] += 1
        return r
    out = {'c2': new_counts(), 'main': new_counts(), 'long': new_counts(), 'u': new_counts()}
    # C2 first, on its whole registered coverage, so that no time cap can cut it short (GC902)
    pref = block_prefixes(pair, N_fp)
    out['c2_total'] = len(pref)
    for w in pref:
        realise(w, out['c2'])
    fails = []
    for bits in range(1 << K):
        if time.time() - t0 > CAP:
            break
        w = ''.join(pair[(bits >> b) & 1] for b in range(K))
        if realise(w, out['main']) is False:
            fails.append(w)
    out.update({'total': 1 << K, 'fails': fails})
    if extra:
        K2, cnt = extra[0], extra[1]
        out['long_total'], out['long_fails'] = cnt, []
        for _ in range(cnt):
            if time.time() - t0 > 2 * CAP:
                break
            w = ''.join(pair[rng.randrange(2)] for _ in range(K2))
            if realise(w, out['long']) is False:
                out['long_fails'].append(w)
        half = (9 * 29) // 2
        out['u_total'], out['u_fails'] = 32, []
        for _ in range(32):
            if time.time() - t0 > 3 * CAP:
                break
            w = ''.join(pair[rng.randrange(2)] for _ in range(K))
            if realise(w, out['u'], white_beyond=half) is False:
                out['u_fails'].append(w)
    out['replay_bad'], out['tail_bad'] = stats['replay_bad'], stats['tail_bad']
    out['secs'] = time.time() - t0
    s.delete()
    return out


def sample_verdict(c, total, failed):
    """After the control gate: REFUTED on any UNSAT, HELD only on total completed SAT calls, else NOT DECIDED."""
    if failed:
        return 'REFUTED'
    return 'HELD' if c['sat'] == total and c['attempted'] == total and not c['unknown'] else 'NOT DECIDED'


def verdicts(res):
    """Every printed verdict, as a pure function of run_family's results (testable without a solver, GC902)."""
    nd = 'NOT DECIDED'
    c1_calls = sum(r[k]['sat'] for r in res.values() for k in ('c2', 'main', 'long', 'u') if k in r)
    if any(r['replay_bad'] or r['tail_bad'] for r in res.values()):
        c1 = 'FAIL'
    else:
        c1 = 'PASS' if c1_calls else nd
    if any(r['c2']['unsat'] for r in res.values()):
        c2 = 'FAIL'
    elif all(r['c2']['sat'] == r['c2_total'] == r['c2']['attempted'] for r in res.values()):
        c2 = 'PASS'
    else:
        c2 = nd                                                # an UNKNOWN or missing prefix call (GC902)
    v = {'C1': c1, 'C2': c2}
    ok = c1 == 'PASS' and c2 == 'PASS'
    for name, p in (('P1', 9), ('P2', 7), ('P3', 5)):
        r = res.get(p)
        v[name] = nd if not (ok and r) else sample_verdict(r['main'], r['total'], r['fails'])
    r9 = res.get(9)
    has_extra = bool(r9) and 'long_total' in r9
    v['P4'] = nd if not (ok and has_extra) else sample_verdict(r9['long'], r9['long_total'], r9['long_fails'])
    v['U'] = nd if not (ok and has_extra) else sample_verdict(r9['u'], r9['u_total'], r9['u_fails'])
    return v


def main():
    rng = random.Random(9)
    res = {}
    for p, pair, K, N_fp in FAMILIES:
        extra = (15, 30) if p == 9 else None
        r = run_family(p, pair, K, N_fp, rng, extra)
        res[p] = r
        print('p = %d, pair %s, %d blocks: counts %s of %d; %d unrealised (first: %s); C2 prefixes %s of %d; '
              'replay failures %d, white-tail failures %d; %.0f s' % (
                  p, pair, K, r['main'], r['total'], len(r['fails']), r['fails'][:3], r['c2'], r['c2_total'],
                  r['replay_bad'], r['tail_bad'], r['secs']), flush=True)
        if extra:
            print('  15-block random: counts %s of %d, unrealised %s; white beyond half the cone: counts %s of %d, '
                  'unrealised %s' % (r['long'], r['long_total'], r['long_fails'][:2], r['u'], r['u_total'],
                                     r['u_fails'][:2]), flush=True)
    v = verdicts(res)
    print('FP2-C1 (every model replays, and U models are white beyond half the cone): %s' % v['C1'])
    print('FP2-C2 (every whole-block concatenation within FP\'s N realised): %s' % v['C2'])
    print('FP2-P1 (p = 9, all 1,024 realised): %s' % v['P1'])
    print('FP2-P2 (p = 7, all 1,024 realised): %s' % v['P2'])
    print('FP2-P3 (p = 5, all 64 realised): %s' % v['P3'])
    print('FP2-P4 (p = 9, 30 random 15-block words realised): %s' % v['P4'])
    print('FP2-U (p = 9, white beyond half the cone, 32 words): %s' % v['U'])


if __name__ == '__main__':
    main()
