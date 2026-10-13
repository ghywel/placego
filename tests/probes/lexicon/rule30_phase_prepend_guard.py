#!/usr/bin/env python3
"""GC1169: a real black-phase word has no real white-phase prepend.

RUN-ON: CPU, standard library; no solver, CUT or language census.
COMMAND: python3 tests/probes/lexicon/rule30_phase_prepend_guard.py

Record searched: prepend/origin/phase-cut ->40 hits13files; both-prepend/
left-extension-pair/two-origin with phase/black/cut ->85 hits27files;
exact100101 with phase/prehistory ->7 hits5files, unrelated spatial
suffixes. Read GC1002..5, GC971/978, GC1159, G25 and8.82/8.83.

BEFORE EXPLORATORY CHECKS:
 E1: expect a B seed010 to expose both blocked S prepend bits by length43.
     Failed: it and two other fixed seeds gave no such prefix. A missing
     state predecessor alone does not prove an observable obstruction.
 P1: expect every compatible pair of origin-blocking phase0 cuts to
     contain a phase1 cut in its common suffix. Failed:571 pairs,335
     uncovered; shortest suffix100101. P2 (all phase0 cuts contain a
     phase1 cut) held. Data remained outside git.
 BEFORE WITNESS EXTRACTION (presence already inferred from the catalog):
     confirm100101 with one finite12-bit right cone. First witness found
     at integer68, black sites3,7. No whole language was computed.

CERTIFICATE CONTROLS (the example is now seen, these are replays):
 C1 literal and packed actual right evolution produce100101 in phase1.
 C2 formal S parents0w,1w map to the same B forced-left prefix, but their
     roots contain certified S cuts0100101 and11, respectively.
 C3 residual-subset prepend guard equals direct substring exclusion on
     every word of length<=10; no actual membership inferred from this.
 CF: imposing all S cuts on both formal parent roots is safe; the real
     child with both rejected parent origins refutes it.
 Unexpected: omitting the last sample leaves the prepend0 unblocked.
 Origin-only waiver accepts both roots: all their cuts start at0.

ADDITIONAL CONTROL before execution: complete the reconstructed low12
left cells by white, use the actual finite right seed at3,7 and centre1.
Predict its ordinary, unclamped centre matches the B clock at0..12.
The observed right word is the same100101; do not measure its horizon.
OUTCOME for the certificate controls:2047 direct/residual guards agree;
571 pairs confirm335 uncovered, shortest100101. Actual right witness,
both formal left parents and the terminal-sample countercontrol pass.
The full-seed control also passes:13 matching centre observations and
the actual six-bit right word. No duration beyond tick12 is reported.
"""
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
from rule30_prefix_realization import inverse, rule

CATALOG = Path(__file__).with_name('rule30_local_mfw44.txt')
DIGEST = '80eee0a74712632a4339f7cd0a7776f23dd2a45fea8e934b79e6f0aba390d378'
WORD = '100101'


def cuts():
    assert sha256(CATALOG.read_bytes()).hexdigest() == DIGEST
    out, phase = {0: [], 1: []}, None
    for line in CATALOG.read_text().splitlines():
        if line.startswith('## phase '):
            phase = int(line.split()[2].rstrip(':'))
        elif phase is not None and line and set(line) <= {'0', '1'}:
            out[phase].append(line)
    assert list(map(len, out.values())) == [1130, 1199]
    return out


def forbidden(word, fs):
    return any(f in word for f in fs)


def guard(fs):
    terminal = set(fs)
    prefixes = {''} | {f[:i] for f in fs for i in range(1, len(f))}

    @lru_cache(None)
    def step(state, bit):
        candidate = state+bit
        if any(candidate[i:] in terminal for i in range(len(candidate))):
            return None
        return next(candidate[i:] for i in range(len(candidate)+1)
                    if candidate[i:] in prefixes)

    def permitted(word):
        states = {step('', b) for b in '01'}-{None}
        for bit in word:
            states = {step(s, bit) for s in states}-{None}
        return bool(states)
    return permitted


def main():
    fs = cuts()
    accept = guard(fs[0])
    checks = 0
    for n in range(11):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            direct = any(not forbidden(u+w, fs[0]) for u in '01')
            assert accept(w) == direct
            checks += 1
    print('residual/direct finite-guard controls:', checks, 'PASS')
    pair_count = uncovered = 0
    shortest = None
    for a in fs[0]:
        if a[0] != '0':
            continue
        for b in fs[0]:
            if b[0] != '1':
                continue
            x, y = a[1:], b[1:]
            if not (x.startswith(y) or y.startswith(x)):
                continue
            w = max((x, y), key=len)
            pair_count += 1
            if not forbidden(w, fs[1]):
                uncovered += 1
                if shortest is None or (len(w), w) < (len(shortest), shortest):
                    shortest = w
    assert (pair_count, uncovered, shortest) == (571, 335, WORD)
    assert all(forbidden(f, fs[1]) for f in fs[0])
    print('pair prediction REFUTED:', pair_count, 'pairs,', uncovered,
          'uncovered; shortest', shortest, '; phase implication PASS')

    x, r, visible = {3: 1, 7: 1}, 68, []
    mask = (1 << 26)-1
    for t in range(12):
        assert (r & 1) == x.get(1, 0)
        if t % 2:
            visible.append(str(r & 1))
        wall = (1+t) % 2
        x = {j: rule(wall if j == 1 else x.get(j-1, 0),
                     x.get(j, 0), x.get(j+1, 0)) for j in range(1, 26)}
        r = ((r << 1 | wall) ^ (r | (r >> 1))) & mask
    assert ''.join(visible) == WORD
    assert not forbidden(WORD, fs[1])
    assert '0100101' in fs[0] and '11' in fs[0]
    assert not accept(WORD) and accept(WORD[:-1])
    print('actual finite B right witness: black sites3,7; word', WORD, 'PASS')

    child = inverse(list(map(int, WORD)), 1)
    parents = []
    for u, cut in (('0', '0100101'), ('1', '11')):
        v = u+WORD
        assert cut in v and not forbidden(v[1:], fs[0])
        parent = inverse(list(map(int, v)), 0)
        image = [rule(parent[j+1], parent[j], 0 if j == 0 else parent[j-1])
                 for j in range(12)]
        assert image == child
        parents.append(parent)
        print('formal S parent', v, 'cut', cut, '; left image PASS')
    # The child's zero band3..5 has different formal ancestry shapes.
    assert child[2:5] == [0, 0, 0]
    assert parents[0][1:6] == [0]*5
    assert parents[1][1:6] == [1, 0, 1, 1, 1]
    print('same real-child zero band: shrinking-zero/P formal origins PASS')
    full = {0: 1, 3: 1, 7: 1}
    full.update({-j-1: bit for j, bit in enumerate(child)})
    observed = []
    for t in range(13):
        assert full.get(0, 0) == (1+t) % 2
        if t % 2:
            observed.append(str(full.get(1, 0)))
        lo, hi = min(full), max(full)
        full = {j: rule(full.get(j-1, 0), full.get(j, 0), full.get(j+1, 0))
                for j in range(lo-1, hi+2)}
    assert ''.join(observed) == WORD
    print('ordinary finite full seed: centre clock0..12, actual word PASS')
    print('ALL CERTIFICATE CONTROLS PASS; no actual record-maxima claim')


if __name__ == '__main__':
    main()
