#!/usr/bin/env python3
"""Bounded Intel audit of L954; owner explicitly permits Intel tests.

Record searched: conductor/tock/long.memory -> L954; XNOR/fall.*tock/trace.*triang
combined query -> no hits. Read both hand notebooks, RECORD-MAP and closed routes.
Predictions registered before execution:
 C0: outward reconstruction agrees with independent forward pivot inversion
     and literal forward replay on all 256 eight-tock prefixes.
 C1: Local's E7/O7/E8 formulas and k0..k3 hold exhaustively.
 C2: physical exhaustive widths <=4 die by6; <=5 by8; only 110101
     at width <=6 passes8. Its death is an open readout, capped at20.
 CF: deleting the old-bit term of k3 must be detected (known wrong).
 H: correction to XNOR vanishes on every prefix with no 10 fall.
     Blind expectation: holds on this small domain; not a universal prediction.
     Test k2..k8, stop this hypothesis at its first counterexample.
 Unexpected check: 1100 and 11 give the same physical history (padding is
     not support); constant-tock reconstructed rows have nonzero periodic tails.
 No fit, large census, GPU, Lean, data download, or automatic scope increase.
 Caps: one process, wall15s, CPU10s, RSS128MiB sampled every case,
     output/disk256KiB, <=256 trace prefixes and <=511 conductor prefixes,
     at most18 cells per reconstruction and20 physical updates. Failures retained.
 Outcome: appended after the sole run; see review report for scope.
"""
import hashlib
import itertools
import json
import resource
import signal
import sys
import time


def guard():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    if peak > 128 * 1024**2:
        raise RuntimeError('RSS cap exceeded')


def outward(a):
    prev, col, row = [0]*len(a), list(a), [a[0]]
    for _ in range(1, len(a)):
        nxt = [col[t+1] ^ (col[t] | prev[t]) for t in range(len(col)-1)]
        row.append(nxt[0])
        prev, col = col, nxt
    return row


def step(row):
    # Finite zero tail, literal cells; extra outward site included.
    padded = [0] + row + [0, 0]
    return [padded[j+1] ^ (padded[j] | padded[j-1])
            for j in range(1, len(row)+2)]


def forward_pivots(a):
    row = []
    for t, wanted in enumerate(a):
        trial = row + [0]
        for _ in range(t):
            trial = step(trial)
        row.append(wanted ^ trial[0])
    return row


def trace(b):
    return [c for bit in b for c in (1, bit)]


def conductor(prefix):
    return outward(trace(prefix + (0,)))[-1]


def word(xs):
    return ''.join(map(str, xs))


def main():
    start = time.monotonic()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('wall cap')))
    signal.alarm(15)
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    resource.setrlimit(resource.RLIMIT_FSIZE, (262144, 262144))
    count = 0
    for b in itertools.product((0, 1), repeat=8):
        guard()
        a = trace(b)
        row = outward(a)
        assert row == forward_pivots(a), ('C0 pivot', b)
        r = row[:]
        for t, wanted in enumerate(a):
            assert r[0] == wanted, ('C0 trace', b, t)
            r = step(r)
        u, v, w, s = b[:4]
        assert row[6] == (w | ((1-u) & v)), ('E7', b)
        assert step(row)[6] == (s ^ v ^ w ^ (u & (1-v) & w)), ('O7', b)
        assert row[7] == ((1-s) ^ v ^ w ^ (u & (1-v))), ('E8', b)
        count += 1
    k = []
    for m in range(4):
        vals = []
        for p in itertools.product((0, 1), repeat=m):
            got = conductor(p)
            expected = 1 if m < 2 else ((1 ^ p[0] ^ p[1]) if m == 2
                      else (1 ^ p[1] ^ p[2] ^ (p[0] & (1-p[1]))))
            assert got == expected, ('C1 k', p)
            vals.append(got)
        k.append(vals)
    assert conductor((1, 0, 0)) != (1 ^ 0 ^ 0), 'CF failed to detect mutant'
    deaths, passing8 = {}, []
    for bits in itertools.product((0, 1), repeat=5):
        row = [1] + list(bits)
        width = max(i+1 for i, bit in enumerate(row) if bit)
        r = row[:]
        death = None
        for t in range(21):
            if t % 2 == 0 and r[0] == 0:
                death = t
                break
            r = step(r)
        assert death is not None, ('C2 horizon', row)
        deaths[word(row)] = death
        assert width > 4 or death <= 6, ('C2 width4', row, death)
        assert width > 5 or death <= 8, ('C2 width5', row, death)
        if death > 8:
            passing8.append(word(row))
    assert passing8 == ['110101'], ('C2 unique', passing8)
    r, s = [1, 1], [1, 1, 0, 0]
    for _ in range(20):
        assert r + [0, 0] == s, 'padding'
        r, s = step(r), step(s)
    for bit in (0, 1):
        row = outward(trace((bit,)*8))
        assert all(row[j-1] == (bit if j % 2 else 1-bit)
                   for j in range(2, 17)), 'infinite control'
    tested, bad = 0, None
    for m in range(2, 9):
        for p in itertools.product((0, 1), repeat=m):
            guard()
            if any(p[i:i+2] == (1, 0) for i in range(m-1)):
                continue
            tested += 1
            actual = conductor(p)
            baseline = 1 ^ p[-2] ^ p[-1]
            if actual != baseline:
                bad = {'m': m, 'prefix': word(p), 'k': actual, 'baseline': baseline,
                       'row_with_last_tock_zero': word(outward(trace(p+(0,))))}
                break
        if bad:
            break
    result = {'controls': 'PASS', 'trace_prefixes': count, 'k0_to_k3': k,
              'deaths_padded_width6': deaths, 'only_past8': passing8,
              'no_fall_hypothesis': 'REFUTED' if bad else 'HELD_THROUGH_K8',
              'no_fall_cases': tested, 'counterexample': bad,
              'elapsed_seconds': time.monotonic()-start,
              'source_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
