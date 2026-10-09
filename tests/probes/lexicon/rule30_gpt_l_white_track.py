#!/usr/bin/env python3
"""GC768: reproducible static certificate arithmetic for GC767/G251.

The original GC767 predictions preceded its one-off calculation outside git:
stride -33 least period155; blind white maximum <=12; reversed stride agrees.
This file is a disclosed replay, not a new blind result. No CA evolution.

Replay predictions, written before this instrument runs:
LT0: bit-list and integer-mask reads agree at every sample (control).
LT1: both signs of33 give period155, black68, white87, white maximum7
     (expected reproduction of GC767, not blind).
LT2: ignoring the diagonal's motion and using -31 reproduces the same
     track statistics (known-wrong counterfactual; must fail).
LT3: maximum7 has a literal eight-sample obstruction at all155 starts
     (unexpected exhaustive endpoint check, independent of max routine).
REFUTED-BY: LT0/LT1 disagreement or any all-white eight-sample window.
OUTCOME (2026-10-09, GPT, static replay): LT0/LT1/LT3 PASS. Both signs
of33 give (period,black,white,maxwhite)=(155,68,87,7). LT2 REFUTED
as required: phase-zero stride-31 gives (1,0,155,155), an all-white
track. This checks the arithmetic and endpoints, not the ring dynamics
or the universal settling certificate.
"""
from math import gcd

N = 155
R = int('35409b1caa645d715104db5291a2fe8415260ce', 16)


def track(stride):
    bits = [(R >> i) & 1 for i in range(N)]
    xs = [bits[(stride*u) % N] for u in range(N)]
    ys = [int(bool(R & (1 << ((stride*u) % N)))) for u in range(N)]
    assert xs == ys, 'LT0'
    period = next(p for p in range(1,N+1)
                  if N % p == 0 and all(xs[i] == xs[i % p] for i in range(N)))
    run = best = 0
    for x in xs + xs:
        run = run + 1 if x == 0 else 0
        best = max(best, run)
    return xs, (period, sum(xs), N-sum(xs), min(best,N))


def main():
    expected = (155,68,87,7)
    for stride in (-33,33):
        xs, stats = track(stride)
        assert gcd(abs(stride),N) == 1
        assert stats == expected, 'LT1'
        assert all(any(xs[(i+j)%N] for j in range(8)) for i in range(N)), 'LT3'
        assert any(all(xs[(i+j)%N] == 0 for j in range(7)) for i in range(N))
        print('stride', stride, 'period/black/white/maxwhite', stats)
    _, wrong = track(-31)
    assert wrong != expected, 'LT2 counterfactual failed to fail'
    print('counterfactual stride -31:', wrong)
    print('LT0/LT1/LT3 PASS; LT2 REFUTED as required')


if __name__ == '__main__':
    main()
