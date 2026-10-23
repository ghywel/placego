#!/usr/bin/env python3
"""CL587 job 1: fixed-domain proof controls; predictions/caps in GPT-PROOFS32-CHAIN.md.
No randomness. Stop on first assertion; no automatic retry or domain expansion.
"""
import hashlib
import importlib.util
import json
import resource
import sys
import time
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START = time.monotonic()


def tick():
    assert time.monotonic() - START < 90, 'wall cap'


def rows(seed, T, H):
    off = H
    mask = (1 << (2 * H + 1)) - 1
    row = sum(1 << (i + off) for i in seed if -H <= i <= H)
    out = [row]
    for _ in range(T):
        row = ((row << 1) ^ ((~row) & (row >> 1))) & mask
        out.append(row)
    return out


def bit(history, t, i, H):
    return (history[t] >> (i + H)) & 1


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (75, 76))
    resource.setrlimit(resource.RLIMIT_DATA, (256 << 20, 256 << 20))
    sys.path.insert(0, str(ROOT / 'tests/probes/lexicon'))
    import rule210_gpt_abstract_pulse as ap
    marker = 0
    for U in range(2):
        for B in range(2):
            for P in range(2):
                for Q in range(2):
                    pp = (210 >> (4 * U + 2 * B + P)) & 1
                    qq = (210 >> (4 * B + 2 * P + Q)) & 1
                    assert (1 - pp) * qq == ((1 - U) * B) ^ ((1 - U) * ((1 - P) * Q))
                    marker += 1
    assert ((210 >> 2) & 1, (210 >> 5) & 1) == (0, 0)  # no-clearing negative
    abstract = witnesses = 0
    for tau in range(4):
        for w in range(4):
            for post in range(16):
                for tail in range(1 << (2 * w + 1)):
                    Y, X = ap.orbit(tau, w, post, tail)
                    t = tau
                    for j in range(w + 1):
                        if j and not X[t][2 * j]:
                            t += 1
                        T = tau + j + 1
                        assert t <= tau + j and X[t][2 * j] == 1
                        assert all((1 - X[s][2*j])*X[s][2*j+1] == 0 for s in range(t,T))
                        assert X[T][2*j:2*j+2] == [0, 1]
                        for s in range(T, len(Y)):
                            assert X[s][2*j] == 0
                            assert X[s][2*j+1] ^ Y[s][2*j+1] == Y[0][2*j+1]
                        witnesses += 1
                    abstract += 1
        tick()
    Y, X = ap.orbit(0, 1, 0, 0, permanent=True)
    assert any(ap.violations(Y, X, 0, 1))

    # Independently evaluate full physical orbits, not the diagonal recurrence.
    H, horizon = 110, 45
    physical = pair_checks = 0
    sharp = fail_front = long_spans = 0
    for leftmask in range(32):
        left = {-(2*j+1) for j in range(5) if leftmask >> j & 1}
        bg = {i for i in range(1, H+1) if i % 6 in (1,5)}
        bg.symmetric_difference_update({-i for i in left})
        bg.update(left)
        Y = rows(bg, horizon, H)
        assert all(bit(Y,t,0,H) == t%2 for t in range(horizon+1))
        for e in range(2, 15, 2):
            tau = next(s for s in range(e) if bit(Y,s,e-1-s,H))
            w = next(j for j in range(12) if e+2*j+1 in bg)
            span = 2*w+1
            stop = e+span
            assert stop <= horizon
            if span <= 9:
                tails = range(1 << span)
            else:
                long_spans += 1
                tails = sorted({0, (1<<span)-1,
                                sum(1<<j for j in range(0,span,2)),
                                sum(1<<j for j in range(1,span,2))})
            for tail in tails:
                seed = {i for i in bg if not e <= i <= e+span}
                seed.add(e)
                seed.update(e+1+j for j in range(span) if tail >> j & 1)
                X = rows(seed, stop, H)
                assert all(bit(X,t,0,H) == t%2 for t in range(stop))
                assert bit(X,stop,0,H) != stop%2
                for j in range(w+1):
                    T = tau+j+1
                    def pair_at(s):
                        return (bit(X,s,e+2*j-s,H),bit(X,s,e+2*j+1-s,H))
                    assert pair_at(T) == (0,1)
                    for s in range(T, e+2*j+2):
                        p,q = pair_at(s)
                        assert p == 0
                        assert q ^ bit(Y,s,e+2*j+1-s,H) == int(e+2*j+1 in bg)
                        pair_checks += 1
                    p,q = pair_at(T-1)
                    sharp += int(p != 0 or q ^ bit(Y,T-1,e+2*j+2-T,H) != int(e+2*j+1 in bg))
                fail_front += int(pair_at(tau+w+1) == (0,1))
                physical += 1
            tick()
    assert sharp and fail_front == physical

    # Literal truth table gives an independent check of the integer update.
    scalar_cells = classified = 0
    for seedmask in range(1 << 13):
        seed = {j-4 for j in range(13) if seedmask >> j & 1}
        X = rows(seed, 8, 20)
        a = {i:int(i in seed) for i in range(-20,21)}
        clock = True
        for t in range(9):
            for i in range(-12,13):
                assert bit(X,t,i,20) == a[i]
                scalar_cells += 1
            if t <= 4:
                clock &= a[0] == t % 2
            a = {i:(210 >> (4*a.get(i-1,0)+2*a[i]+a.get(i+1,0)))&1 for i in range(-20,21)}
        if clock:
            assert not any(i in seed for i in (-4,-2,0))
            classified += 1
        if not seedmask % 256:
            tick()

    for m in range(64):
        n = 2*m+1
        excluded = sum(comb(n,k) for k in range(n+1) if k%3 == (m+2)%3)
        included_half = sum(comb(n,k) for k in range(m+1) if (n-2*k)%3 != 0)
        assert 3*excluded+2 == 2**n
        assert 3*included_half == 2**n+1 and included_half%2 == 1
    trunc = rows({i for i in range(1,32) if i%6 in (1,5)}, 65, 90)
    assert any(bit(trunc,t,0,90) != t%2 for t in range(66))
    receipt = dict(verdict='PASS', marker_identities=marker, abstract_cases=abstract,
                   front_witnesses=witnesses, actual_tail_cases=physical,
                   actual_pair_cells=pair_checks, longer_span_pattern_cases=long_spans,
                   sharp_early_failures=sharp, failing_gate_has_front=fail_front,
                   full_seed_domain=8192, scalar_cell_checks=scalar_cells,
                   clock_prefix_parity_cases=classified, binomial_cases=64,
                   negative_controls=['no-clearing','permanent-pulse','finite-truncation'],
                   wall_seconds=time.monotonic()-START,
                   max_rss_platform_units=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(receipt,sort_keys=True))


if __name__ == '__main__':
    main()
