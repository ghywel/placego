"""GC2629: exact first-black waiting times, given the visited wheel and arrival phase.

Only the previously retained step bytes and terminal 16-phase parent words are read.
Uniformizing the arrival phase keeps the same multiset of visited parents.
"""
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path

P, START, END, WIDTH = 16, 16384, 65536, 87868
ROW_BYTES = (WIDTH + 7) // 8


def read_pinned(name, digest):
    data = Path(os.environ[name]).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest
    return data


def phase_waits(bits):
    if not any(bits):
        return [None] * len(bits)
    return [1 + next(h for h in range(len(bits)) if bits[(r + h) % len(bits)])
            for r in range(len(bits))]


def main():
    steps = read_pinned('WHITE_STEPS', '04a1881585330e22f3661519d0bc8766f596984dd37d3434f32e23b4a7a79ad7')
    raw = read_pinned('WHITE_SEED_CYCLE', '28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71')
    assert len(steps) == END - START + 1 and max(steps) < 17  # no truncated jump
    assert len(raw) == 33 * ROW_BYTES
    phases = [raw[r*ROW_BYTES:(r+1)*ROW_BYTES] for r in range(P)]
    def bit(j, phase):
        return (phases[phase % P][j // 8] >> (j % 8)) & 1
    def word(j):
        return [bit(j, r) for r in range(P)]

    assert phase_waits(word(WIDTH-2)) == [None] * P
    edge = 12285  # GC2621, inclusive settled prefix through 12284
    observed, uniform = Counter(), Counter()
    by_jump = defaultdict(lambda: [0, 0, 0, 0, 0])  # n, immediate, uniform immediate, sum L, sum uniform L
    by_half = defaultdict(lambda: [0, 0, 0, 0, 0])
    plus_one_fails = step_one = step_two = second_chance = step_three = 0
    previous = None
    for t, jump in enumerate(steps, START):
        if t == 32768:
            assert edge == 24465
        assert bool(jump) == bool(bit(edge-1,t))
        if jump:
            if previous is not None:
                h, old, size = previous
                length = t-h
                arrivals = phase_waits(word(edge-1))
                assert None not in arrivals and arrivals[(h+1) % P] == length
                plus_one_fails += arrivals[(h+2) % P] != length
                if size == 1:
                    assert (length == 1) == (bit(old-2,h) == 0)
                    step_one += 1
                elif size == 2:
                    assert length >= 2
                    assert (length == 2) == (bit(old-3,h) != bit(old-2,h))
                    step_two += 1
                    second_chance += length == 2
                elif size == 3:
                    assert length == 1
                    step_three += 1
                observed[length] += 1
                uniform.update(arrivals)
                for row in (by_jump[size],by_half[int(h >= 40960)]):
                    for i, value in enumerate((1, int(length==1), arrivals.count(1), length, sum(arrivals))):
                        row[i] += value
            previous = (t,edge,jump)
        edge += jump
    n = observed.total()
    assert n == 20060 and uniform.total() == n*P and observed[1] == 5351
    assert plus_one_fails > 0
    result = {'n':n,'last_edge_after_final_tick':edge,'observed_waits':dict(sorted(observed.items())),
              'uniform_phase_waits':dict(sorted(uniform.items())),'by_jump':dict(sorted(by_jump.items())),
              'by_half':dict(by_half),'wrong_phase_errors':plus_one_fails,
              'checked_jump_1_2_3':[step_one, step_two, step_three], 'length_two_after_jump_two':second_chance}
    (Path(os.environ['CAPPED_OUT'])/'waits.json').write_text(json.dumps(result,indent=2)+'\n')
    print('WHITE_PARENT_WAITS_DONE',n)


if __name__ == '__main__':
    main()
