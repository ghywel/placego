#!/usr/bin/env python3
"""GC2357 fixed exact controls for uniform diagonal capture, not a speed fit.

All2048 width12 left-band starts with a black left edge, marked at that edge only.
67 updates; depths0..11; band exits D=0..9; no horizon or sample enlargement.
Integer colour/ancestry update compared with literal scalar Rule30 parent lookup.
"""
import json
import os
from pathlib import Path
from itertools import product
import time

WIDTH = 12
STEPS = 67
MASK = (1 << WIDTH)-1


def capture_time(j):
    return 0 if j == 0 else 1+j*(j-1)//2


def exit_time(d):
    return (d+2)*(d+3)//2


def one_step(a, m):
    child = ((a << 2) ^ ((a << 1) | a)) & MASK
    marked = child & ((m << 2) | (m << 1) | m)
    return child, marked


def scalar_step(a, m):
    colours, marks = [], []
    for j in range(WIDTH):
        indices = (j-2, j-1, j)
        p = [a[i] if i >= 0 else 0 for i in indices]
        q = [m[i] if i >= 0 else 0 for i in indices]
        value = (30 >> (4*p[0]+2*p[1]+p[2])) & 1
        colours.append(value)
        marks.append(int(value and any(q)))
    return colours, marks


def integer(bits):
    return sum(v << j for j, v in enumerate(bits))


def main():
    start = time.process_time()
    # W=(0,0), U=(1,0), M=(1,1); each marked site must be black.
    local_count = 0
    for parents in product(((0, 0), (1, 0), (1, 1)), repeat=3):
        a, m = zip(*parents)
        child = (30 >> (4*a[0]+2*a[1]+a[2])) & 1
        marked = int(child and any(m))
        if m[0] == a[0] and m[1] == a[1]:
            unmarked = int(child and not marked)
            rhs = int(a[2] and not m[2] and not (a[0] or a[1]))
            assert unmarked == rhs
            local_count += 1
    assert local_count == 12
    # The identity is for all-parent reach (also the leftmost-parent convention),
    # not an arbitrary chosen parent: 011 may choose its unmarked right parent.
    assert ((30 >> 3) & 1) == 1
    assert any((0, 1, 0)) and not (0, 1, 0)[2]
    # Without the black edge, a white pair can persist forever.
    assert one_step(0, 0) == (0, 0)

    last_unmarked = [-1]*WIDTH
    max_white = [0]*(WIDTH-1)
    max_exit = [0]*10
    steps_checked = 0
    for tail in range(1 << (WIDTH-1)):
        if tail % 64 == 0:
            assert time.process_time()-start < 20, 'frozen child CPU check'
        a, m = 1 | (tail << 1), 1
        scalar_a = [(a >> j) & 1 for j in range(WIDTH)]
        scalar_m = [1]+[0]*(WIDTH-1)
        white_runs = [0]*(WIDTH-1)
        first_exits = [None]*10
        front = 0
        for t in range(STEPS+1):
            assert a & 1 and m & 1
            assert m & ~a == 0
            assert integer(scalar_a) == a and integer(scalar_m) == m
            for j in range(WIDTH):
                unmarked = ((a & ~m) >> j) & 1
                if unmarked:
                    last_unmarked[j] = max(last_unmarked[j], t)
                if t >= capture_time(j):
                    assert not unmarked, (tail, j, t, 'capture failed')
            for n in range(WIDTH-1):
                white_runs[n] = white_runs[n]+1 if (a >> n) & 3 == 0 else 0
                max_white[n] = max(max_white[n], white_runs[n])
                assert white_runs[n] <= n, (tail, n, t, 'zero pair too long')
            if t == STEPS:
                break
            a, m = one_step(a, m)
            scalar_a, scalar_m = scalar_step(scalar_a, scalar_m)
            if front <= 9:
                front = (a & ((1 << (front+3))-1)).bit_length()-1
                # Until this bounded follower leaves9, all its descendants are
                # exactly the black prefix through front, independently marked.
                if front <= 9:
                    assert m & ((1 << (front+1))-1) == a & ((1 << (front+1))-1)
                    assert m >> (front+1) == 0
                for d in range(10):
                    if first_exits[d] is None and front > d:
                        first_exits[d] = t+1
            steps_checked += 1
        for d, when in enumerate(first_exits):
            assert when is not None and when <= exit_time(d), (tail, d, when)
            max_exit[d] = max(max_exit[d], when)
    result = dict(starts=1 << (WIDTH-1), width=WIDTH, steps=STEPS,
                  scalar_steps_checked=steps_checked, one_step_cases=local_count,
                  capture_bounds=[capture_time(j) for j in range(WIDTH)],
                  last_unmarked_times=last_unmarked, max_white_pair_runs=max_white,
                  exit_bounds=[exit_time(d) for d in range(10)], max_first_exits=max_exit,
                  cpu_seconds=time.process_time()-start)
    print(json.dumps(result, sort_keys=True))
    if os.environ.get('CAPPED_OUT'):
        Path(os.environ['CAPPED_OUT'], 'capture-controls.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
