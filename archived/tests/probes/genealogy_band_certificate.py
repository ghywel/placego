#!/usr/bin/env python3
"""GC2356 second frozen pilot: exact autonomous left band, no new long run.

Uses the eight finite words certified by the first pilot, with an input digest.
At most256 width21 band states, then <=19 periods for the minimal right follower.
An absorbing exit makes the one-period map monotone. No trap may be inferred
from merely spending a chosen number of steps in the band.
"""
import hashlib
import json
import os
from pathlib import Path
import sys
import time


def band_step(w, width):
    return ((w << 2) ^ ((w << 1) | w)) & ((1 << width)-1)


def scalar_step(w, width):
    out = 0
    for j in range(width):
        a = (w >> (j-2)) & 1 if j >= 2 else 0
        b = (w >> (j-1)) & 1 if j >= 1 else 0
        c = (w >> j) & 1
        # Ordinary Rule30 lookup at a physical left-edge coordinate.
        out |= ((30 >> (4*a+2*b+c)) & 1) << j
    return out


def run():
    start_cpu = time.process_time()
    raw = Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == sys.argv[2]
    packet = json.loads(raw)
    finite = [x for x in packet['certificates'] if x['finite']]
    assert len(finite) == 8
    maxima = []
    for item in finite:
        d = initial = item['length']
        peak = d
        for r, length in item['pattern']:
            peak = max(peak, d+2*r)
            d += 2*(r+1)-length
        assert d == initial
        maxima.append(peak)
    bound = max(maxima)
    assert bound == 18
    width = bound+3  # offsets0..D+2 required by the front update
    rows, seen = [], {}
    w = 1  # the actual single seed, in its left-edge frame
    while w not in seen:
        assert len(rows) < 256, 'frozen cycle-search cap; no automatic increase'
        assert band_step(w, width) == scalar_step(w, width)
        seen[w] = len(rows)
        rows.append(w)
        w = band_step(w, width)
    onset = seen[w]
    period = len(rows)-onset
    cycle = rows[onset:]
    assert cycle and all(row & 1 for row in cycle)
    top = bound+1

    def follow(position, phase, right=True):
        row = cycle[(phase+1) % period]
        if right:
            choices = row & ((1 << (position+3))-1)
            return choices.bit_length()-1
        choices = row >> position
        assert choices
        return position + ((choices & -choices).bit_length()-1)

    def period_map(position, phase=0, right=True):
        for t in range(period):
            if position == top:
                break  # exit is absorbing; a later reentry cannot undo escape
            position = min(top, follow(position, phase+t, right))
        return position

    maps = []
    for phase in range(period):
        mapping = [period_map(d, phase) for d in range(top+1)]
        assert mapping == sorted(mapping), ('nonmonotone', phase)
        assert all(mapping[d] != d for d in range(top))
        maps.append(mapping)
    d, chain = 0, [0]
    for _ in range(bound+1):
        if d == top:
            break
        new = maps[0][d]
        assert new > d, 'would certify a bounded fixed point, not permit a longer run'
        d = new
        chain.append(d)
    assert d == top
    # Corrected Local control, exactly on the recurrent band, every phase.
    assert all((row >> 4) & 1 for row in cycle)
    assert all(period_map(4, phase, right=False) == 4 for phase in range(period))
    # Synthetic static mask: a rightward fixed point at1 is detected.
    synthetic = lambda d: (3 & ((1 << (d+3))-1)).bit_length()-1
    assert synthetic(1) == 1
    result = dict(input_sha256=sys.argv[2], bound=bound, width=width,
                  onset=onset, period=period, band_rows=rows, period_maps=maps,
                  minimal_chain=chain, candidate_max_offsets=maxima,
                  no_trap=True, leftward_control=4,
                  cpu_seconds=time.process_time()-start_cpu)
    assert result['cpu_seconds'] < 20
    print(json.dumps(result, sort_keys=True))
    if os.environ.get('CAPPED_OUT'):
        Path(os.environ['CAPPED_OUT'], 'band-certificate.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    run()
