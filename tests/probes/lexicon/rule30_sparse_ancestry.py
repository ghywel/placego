#!/usr/bin/env python3
"""SA1: exact inverse ancestry for inclusion two-pulse/singleton classes at q=4,8.

RUN-ON: CPU, Python standard library, one process.
COMMAND: python3 tests/probes/lexicon/rule30_sparse_ancestry.py
CAPS: 10 CPU seconds globally; at most 4**q+1 inverse steps per start.
Data/transcript outside Git. No q16 extension or forward-tree census.

Preregistered before execution. Shares only the reviewed inverse formula G156,
not a child constructor or Local's computational walk. Classify each of ten
starts (e0+er,e0), r=1..q-1, by exact absorption into (0,0) or exact repeated
pair. Absorption gives rooted depth steps-1; last nonzero pair must be the root.
An exact cycle excludes rooted ancestry. A cap is UNDECIDED, never rejection.

SA-C1: packed inverse agrees with independent per-bit literal inversion on all
256 pairs at q4 and every classified trajectory edge; roots at q2,4,8 absorb.
SA-C2: q4 r1 is nonrooted, as GC334's rotated return predicts.
SA-P1 (blind, uncertain): at q8 at least one r other than2 is rooted.
SA-CF: compatible forward triples alone need not have rooted ancestors; q2
pair(1,2) repeats after two inverse steps and never reaches the absorbing pair.
SA-U: if a start absorbs, inverse-reversing its entire saved chain gives a
literal rooted forward prefix, and its depth agrees with the first hit time.
No extrapolation of the finite rooted separation list to arbitrary q.
OUTCOME: NOT RUN; run only after the preregistration is published.
"""
import json
import resource
import sys


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def packed(a, b, q):
    return (((b >> 1) | ((b & 1) << (q - 1))) ^ (a | b), a)


def scalar(a, b, q):
    out = 0
    for t in range(q):
        v = ((b >> ((t + 1) % q)) & 1) ^ (((a >> t) & 1) | ((b >> t) & 1))
        out |= v << t
    return out, a


def classify(start, q, t0):
    seen, chain, state = {}, [], start
    for k in range(4**q + 1):
        if cpu() - t0 > 10:
            return {'status': 'UNDECIDED', 'reason': 'CPU cap'}
        if state == (0, 0):
            assert chain and chain[-1] == (0, (1 << q) - 1)
            # Scalar inversion independently validates the whole saved prefix.
            assert all(scalar(a, b, q) == nxt for (a, b), nxt in zip(chain, chain[1:] + [(0, 0)]))
            return {'status': 'ROOTED', 'depth': k - 1, 'first_zero_hit': k}
        if state in seen:
            return {'status': 'NONROOTED', 'preperiod': seen[state], 'cycle': k - seen[state]}
        seen[state] = k
        chain.append(state)
        nxt = packed(*state, q)
        assert nxt == scalar(*state, q)
        state = nxt
    return {'status': 'UNDECIDED', 'reason': 'state-count cap'}


def main():
    t0 = cpu()
    assert all(packed(a, b, 4) == scalar(a, b, 4) for a in range(16) for b in range(16))
    for q in (2, 4, 8):
        assert classify((0, (1 << q) - 1), q, t0)['depth'] == 0
    cf = classify((1, 2), 2, t0)
    assert cf['status'] == 'NONROOTED' and cf['cycle'] == 2
    rows = []
    for q in (4, 8):
        for r in range(1, q):
            rows.append({'q': q, 'r': r, **classify((1 | (1 << r), 1), q, t0)})
    assert rows[0]['status'] == 'NONROOTED'
    positives = [x for x in rows if x['q'] == 8 and x['r'] != 2 and x['status'] == 'ROOTED']
    undecided = [x for x in rows if x['q'] == 8 and x['r'] != 2 and x['status'] == 'UNDECIDED']
    verdict = 'HELD' if positives else ('UNDECIDED' if undecided else 'REFUTED')
    print(json.dumps({'rows': rows, 'SA_P1': verdict, 'controls': 'PASS', 'cpu': cpu() - t0}, indent=2))
    return 2 if any(x['status'] == 'UNDECIDED' for x in rows) else 0


if __name__ == '__main__':
    sys.exit(main())
