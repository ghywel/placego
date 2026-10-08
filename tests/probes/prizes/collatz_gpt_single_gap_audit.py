#!/usr/bin/env python3
"""GC437: one fixed case width7,T48,t34; no scan.
A1 MUST HOLD: signed component sum, direct demand and literal H agree;
E-|S|=min(P,N), keeping weights positive and segment orientations signed.
A2 BLIND: P,N both positive, so component bound discards cancellation.
CF MUST FAIL: erasing component orientation preserves the signed sum.
Unexpected check: class-prefix sums independently from individual survivors,
including multiplicity when trajectories collide. OUTCOME: NOT RUN.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_segment_gap import segments
from collatz_gpt_superlevel_allocation import layer


def main():
    w, T, t = 7, 48, 34
    populations = states_at(w, T)
    parents = populations[t]
    f = backward(T)
    I = Counter()
    for x, a in parents:
        I[a] += 1 if x % 2 else -1
    B = {-1: 0}
    for a in range(T+2):
        B[a] = B[a-1]+I.get(a, 0)
        independent = sum(1 if x % 2 else -1 for x, b in parents if b <= a)
        assert B[a] == independent
    d = {a: f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
    rows = segments(I, d)
    positive = negative = Fraction()
    details = []
    for wt, lo, hi, l, r in rows:
        imbalance = B[r]-B[l-1]
        individual = sum(1 if x % 2 else -1 for x, a in parents if l <= a <= r)
        assert imbalance == individual
        term = wt*imbalance
        positive += max(term, 0)
        negative += max(-term, 0)
        details.append(dict(weight=str(wt), l=l, r=r, left=B[l-1], right=B[r],
                            imbalance=imbalance, signed_contribution=str(term/2)))
    S, E, old, M = layer(I, d)
    literal = sum((f[t+1][a] for _, a in populations[t+1]), Fraction())-sum((f[t][a] for _, a in parents), Fraction())
    assert S == literal == (positive-negative)/2
    assert E == (positive+negative)/2
    assert E-abs(S) == min(positive, negative)
    print(json.dumps(dict(w=w,T=T,t=t,parents=len(parents),distinct_states=len(set(parents)),
                          imbalances=dict(I),segments=details,P=str(positive),N=str(negative),
                          S=str(S),E=str(E),old=str(old),M=str(M),
                          cancellation=str(E-abs(S)),controls='PASS',
                          blind_both_signs=positive > 0 and negative > 0,
                          unsigned_counterfactual_refuted=E != S),indent=2))


if __name__ == '__main__':
    main()
