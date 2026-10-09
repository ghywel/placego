#!/usr/bin/env python3
"""GC886: bounded independent TC2 input/count consistency audit, not SAT evidence.
RUN-ON: cpu, Python3; COMMAND: python3 tests/probes/lexicon/rule30_gpt_tc2_input_audit.py
Predictions in CLOUD-LOCAL before execution: 746 ordered distinct binary words,
CL115 full digest and factor antichain; F-avoidance agrees with claimed counts
through39. Controls full binary, Fibonacci avoid11, finite-prefix F00/01.
Unexpected: word40 is outside completed levels; redundant111 fails antichain.
No peer code, layer/product graph, solver or spectral iteration is used.
RETAINED FAILURE: first run passed counts/digest then failed a one-word-at40
assertion inspired by CL115. Histogram shows46 at40; repair is observational,
not a fresh prediction or SAT verification.
OUTCOME: repaired bounded audit PASS;39 count matches,8030 prefix states,
46 words at40, and relaxed length40 count13755. SAT/minimality not verified.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path

EXPECTED = [2,3,5,8,12,17,25,36,50,68,91,119,156,199,251,316,393,
            487,596,721,875,1054,1255,1493,1780,2111,2483,2904,3378,
            3908,4502,5153,5875,6664,7541,8534,9649,10876,12231]
DIGEST = '2f8eba0f8ba384e449c7d3a318b42b0afe79a829c352ee4dd56e6f5bb29dd23b'


def antichain(F):
    return all(not (v != w and v in w) for v in F for w in F)


def counts(F, nmax):
    """Suffix-prefix automaton, constructed directly without failure links."""
    forbidden = set(F)
    lens = sorted({len(w) for w in F})
    prefixes = {''} | {w[:i] for w in F for i in range(1, len(w))}
    states = sorted(prefixes, key=lambda w: (len(w), w))
    idx = {w:i for i,w in enumerate(states)}
    transitions = []
    for w in states:
        row = []
        for b in '01':
            v = w + b
            if any(v[-k:] in forbidden for k in lens if k <= len(v)):
                row.append(None)
                continue
            while v not in prefixes:
                v = v[1:]
            row.append(idx[v])
        transitions.append(row)
    layer = [0] * len(states)
    layer[idx['']] = 1
    out = []
    for _ in range(nmax):
        nxt = [0] * len(states)
        for i, value in enumerate(layer):
            for j in transitions[i]:
                if j is not None:
                    nxt[j] += value
        layer = nxt
        out.append(sum(layer))
    return out, len(states)


def main():
    assert counts([], 8)[0] == [2**n for n in range(1,9)]
    assert counts(['11'], 6)[0] == [2,3,5,8,13,21]
    assert counts(['00','01'], 8)[0] == [2]*8
    assert not antichain(['11','111'])
    path = Path(__file__).with_name('rule30_cloud_channel_truecount_F.txt')
    raw = path.read_bytes()
    F = [w for w in raw.decode('utf8').splitlines() if w]
    assert len(F) == len(set(F)) == 746
    assert all(set(w) <= {'0','1'} for w in F)
    assert F == sorted(F, key=lambda w: (len(w),w))
    assert sha256('\n'.join(F).encode()).hexdigest() == DIGEST
    assert antichain(F)
    got, nstates = counts(F, 40)
    assert got[:39] == EXPECTED
    assert Counter(map(len,F))[40] == 46
    assert max(map(len,F)) == 40
    print('PASS: controls; full digest/order/binary/distinct/antichain')
    print('PASS: all39 F-avoidance counts agree; prefix states', nstates)
    print('input bytes', len(raw), 'length histogram', dict(sorted(Counter(map(len,F)).items())))
    print('unexpected partial-level40: relaxed count', got[39], 'not a true-language count claim')


if __name__ == '__main__':
    main()
