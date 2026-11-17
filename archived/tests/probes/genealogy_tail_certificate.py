#!/usr/bin/env python3
"""GC2356: close Local's 60-digit forced words by an exact spatial recurrence.

Fixed 35 patterns, r<=2, L<=6, temporal length<=6, light-speed sum L=2T.
At most 2^(2T)<=4096 spatial states per pattern; no sample/horizon escalation.
Scalar Boolean-array oracle versus integer Rule30 recurrence. No subprocesses.
"""
import hashlib
import json
import os
from pathlib import Path
from itertools import product
import time

START = time.process_time()
N = 60


def guard():
    assert time.process_time() - START < 20, 'fixed 20-second child CPU stop'


def phi_array(w):
    a = [0, 1] + w
    return [bit ^ (a[j] | a[j+1]) for j, bit in enumerate(w)]


def phi_int(w):
    return w ^ ((w << 1) | (w << 2) | 3)


def reads(w, pattern, count):
    out, phase = [], 0
    while len(out) < count:
        r, length = pattern[phase % len(pattern)]
        for _ in range(r):
            w = phi_array(w)
        out += w[:min(length, count-len(out))]
        w = phi_array(w)[length:]
        phase += 1
    return out


def forced(pattern):
    target = []
    while len(target) < N:
        for _, length in pattern:
            target += [1]*(length-1)+[0]
    w = [0]*N
    for j in range(N):
        w[j] ^= reads(w, pattern, j+1)[j] ^ target[j]
    assert reads(w, pattern, N) == target[:N]
    return w


def integer(bits):
    return sum(bit << j for j, bit in enumerate(bits))


def full_cycle(w, pattern):
    for r, length in pattern:
        for _ in range(r):
            w = phi_int(w)
        assert w & ((1 << length)-1) == (1 << (length-1))-1
        w = phi_int(w) >> length
    return w


def spatial_step(state, duration):
    # Missing highest initial bit is zero; no boundary clamps in this bulk cone.
    w = state
    for _ in range(duration):
        w ^= (w << 1) | (w << 2)
    k = 2*duration
    new = (state & 1) ^ ((w >> k) & 1)
    return (state >> 1) | (new << (k-1)), new


def scalar_new(state, duration):
    k = 2*duration
    a = [(state >> j) & 1 for j in range(k)] + [0]
    for _ in range(duration):
        old = [0, 0] + a
        a = [bit ^ (old[j] | old[j+1]) for j, bit in enumerate(a)]
    return (state & 1) ^ a[k]


def main():
    # Independent scalar truth-table-cone control for every transition state used.
    total = 0
    for duration in range(1, 7):
        for state in range(1 << (2*duration)):
            assert spatial_step(state, duration)[1] == scalar_new(state, duration)
            total += 1
        guard()
    choices = list(product(range(3), range(1, 7)))
    patterns = [(p,) for p in choices if p[1] == 2*(p[0]+1)]
    patterns += [(a, b) for a, b in product(choices, repeat=2)
                 if a != b and a[1]+b[1] == 2*(a[0]+b[0]+2)]
    assert len(patterns) == 35
    records = []
    for pattern in patterns:
        guard()
        duration = sum(r+1 for r, _ in pattern)
        k = sum(length for _, length in pattern)
        assert k == 2*duration and k <= 12 and N-k > 2*duration
        head = forced(pattern)
        w = integer(head)
        mask = (1 << (N-k))-1
        assert full_cycle(w, pattern) & mask == w & mask
        state = integer(head[-k:])
        states, added, seen = [], [], {}
        while state not in seen:
            assert len(states) < 1 << k
            seen[state] = len(states)
            states.append(state)
            state, bit = spatial_step(state, duration)
            added.append(bit)
        mu = seen[state]
        period = len(states)-mu
        cycle = added[mu:]
        finite = not any(cycle)
        item = dict(pattern=pattern, duration=duration, width=k,
                    initial60=''.join(map(str, head)), transient=mu,
                    period=period, cycle=''.join(map(str, cycle)),
                    cycle_state=state, visited=len(states), finite=finite)
        if finite:
            assert state == 0
            candidate = integer(head + added[:mu])
            assert full_cycle(candidate, pattern) == candidate
            item['word_integer'] = candidate
            item['length'] = candidate.bit_length()
        # Check full boundary-aware map on the transient plus >one tail period.
        extra = added[:mu] + cycle * (1 + (period+2*k)//period)
        bits = head + extra
        sample = integer(bits)
        valid = len(bits)-k
        assert full_cycle(sample, pattern) & ((1 << valid)-1) == sample & ((1 << valid)-1)
        # Independent array replay of the same boundary map, not just bulk recurrence.
        a = bits[:]
        for r, length in pattern:
            for _ in range(r):
                a = phi_array(a)
            assert a[:length] == [1]*(length-1)+[0]
            a = phi_array(a)[length:]
        assert a == bits[:valid]
        records.append(item)
        print(json.dumps(item, separators=(',', ':')))
    summary = dict(patterns=len(records), finite=sum(x['finite'] for x in records),
                   infinite=sum(not x['finite'] for x in records),
                   transition_controls=total, max_visited=max(x['visited'] for x in records),
                   cpu_seconds=time.process_time()-START)
    print(json.dumps(summary, sort_keys=True))
    out = os.environ.get('CAPPED_OUT')
    if out:
        packet = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      summary=summary, certificates=records)
        Path(out, 'certificates.json').write_text(json.dumps(packet, indent=2)+'\n')


if __name__ == '__main__':
    main()
