#!/usr/bin/env python3
"""rule30_all_l_slab.py: ALS, does every all-L stretch carry the same near-wall slab as the 155-cell ring? (The L twin
of GPT's GC688; portfolio question 4, serves Q6.) Local's run (chat L381), claimed in CLOUD-LOCAL.md with these
predictions pushed before it.

RUN-ON:     cpu (Python 3 and kissat, NL's encoder); a minute or two
COMMAND:    python3 tests/probes/lexicon/rule30_all_l_slab.py

AL (rule30_all_l_period10.py, L380) found the rigid 155-cell all-L ring. GC688 showed for S that every marker-aligned
all-S trace has the ring's five columns next to the wall, whatever lies further out. Here, finite right halves are
sampled with NL's light-cone encoder (rule30_neutral_concat.py, mode A, the clamped wall white at even times): the
visible word L^K and its closing 1, GC623's long entrance 111001 on sites 1 .. 6 at time 0, and six random unit
clauses on deep initial cells to spread the samples (seeded). Each sampled row is replayed directly. At every loop k
with a following L, sites 1 .. m at times 10k .. 10k + 9 are compared with the ring's sites 1 .. m at times 0 .. 9.

PREDICTIONS (Local's, published before the run):
  ALS-C1 (control): every sampled row replays its targets.
  ALS-P1 (blind, confidence 0.6): sites 1 .. 5 agree with the ring at every loop with a following L in every sample
         (a universal five-column L slab).
  ALS-D1 (descriptive): the largest m with no disagreement over all sampled loops.
  UNEXPECTED CHECK ALS-U (blind, confidence 0.6): the exteriors vary: at the first site beyond that m, the samples
         show more than one distinct history, so the agreement is a slab and not the whole ring.
Counterfactual: a disagreement at sites 1 .. 5 in some sample would mean L, unlike S, has no five-column slab.
Finite samples are evidence for a hand statement, not a proof.
OUTCOME: not yet run.
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_neutral_concat as nl                                    # noqa: E402

RING = 0x35409b1caa645d715104db5291a2fe8415260ce
N = 155
K = 8
SAMPLES = 40
MMAX = 12


def ring_columns():
    row = [(RING >> i) & 1 for i in range(N)]
    hist = [row]
    for _ in range(9):
        row = [row[(i - 1) % N] ^ (row[i] | row[(i + 1) % N]) for i in range(N)]
        hist.append(row)
    return {(t, i): hist[t][i % N] for t in range(10) for i in range(1, MMAX + 2)}


def main():
    ref = ring_columns()
    assert [ref[(0, i)] for i in range(1, 7)] == [1, 1, 1, 0, 0, 1]
    rng = random.Random(381)
    cons, Tend = nl.targets('L' * K, 'A', 0)
    cons = cons + [(0, i, v) for i, v in zip(range(2, 7), (1, 1, 0, 0, 1))]
    sols, tries, replay_ok = {}, 0, True
    while len(sols) < SAMPLES and tries < 400:
        tries += 1
        width0 = 6 + Tend
        extra = ['%d 0' % (i if rng.getrandbits(1) else -i) for i in rng.sample(range(8, width0 - 2), 6)]
        text, ninit = nl.cnf_text(cons, Tend, extra)
        r = nl.kissat(text, 120)
        if r.returncode != 10:
            continue
        init = nl.model(r.stdout, ninit)
        replay_ok &= nl.replay(cons, Tend, init)
        sols[''.join(map(str, init))] = init
    print('ALS-C1', 'PASS' if replay_ok and sols else 'FAIL', '(%d distinct rows in %d tries)' % (len(sols), tries))
    first_bad = {}
    beyond = {}
    loops = 0
    for key, init in sols.items():
        right = sum(v << k for k, v in enumerate(init))
        rows = nl.rows_from(right, Tend + 1)
        for k in range(K - 1):
            loops += 1
            for i in range(1, MMAX + 1):
                if any(nl.site(rows[10 * k + s], i) != ref[(s, i)] for s in range(10)):
                    first_bad[i] = first_bad.get(i, 0) + 1
                    break
    m = (min(first_bad) - 1) if first_bad else MMAX
    for key, init in sols.items():
        rows = nl.rows_from(sum(v << k for k, v in enumerate(init)), Tend + 1)
        for k in range(K - 1):
            beyond.setdefault(''.join(str(nl.site(rows[10 * k + s], m + 1)) for s in range(10)), 0)
            beyond[''.join(str(nl.site(rows[10 * k + s], m + 1)) for s in range(10))] += 1
    print('loops compared:', loops, '; first disagreeing site per loop (count):', dict(sorted(first_bad.items())))
    print('ALS-P1', 'HELD' if m >= 5 else 'REFUTED', '(sites 1 .. 5)')
    print('ALS-D1: every sampled loop agrees with the ring on sites 1 ..', m)
    print('ALS-U', 'HELD' if len(beyond) > 1 else 'REFUTED', '(%d distinct site-%d histories)' % (len(beyond), m + 1))
    print('COMPLETE')


if __name__ == '__main__':
    main()
