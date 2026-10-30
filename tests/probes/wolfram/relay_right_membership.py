#!/usr/bin/env python3
"""GC2275: one finite right-language query, fixed nine white-time samples.

Enumerate at most 2^17 right prefixes; stop at first witness. No widening.
If found, independently check literal driven and full physical trajectories.
"""
import hashlib
import json
import os
from pathlib import Path
import time

WIDTH = 17
TARGET = "010101001"
MASK = (1 << WIDTH)-1
START = time.process_time()


def samples(r):
    word = []
    for t in range(17):
        if t % 2 == 0:
            word.append(str(r & 1))
        r = (((r << 1) | (t & 1)) ^ (r | (r >> 1))) & MASK
    return "".join(word)


def literal_half(r):
    a = [(r >> i) & 1 for i in range(WIDTH)]
    answer = []
    table = [0, 1, 1, 1, 1, 0, 0, 0]  # neighborhoods 000 through 111
    for t in range(17):
        if t % 2 == 0:
            answer.append(str(a[0]))
        a = [table[4*((t & 1) if i == 0 else a[i-1])+2*a[i]+(a[i+1] if i+1 < WIDTH else 0)]
             for i in range(WIDTH)]
    return "".join(answer)


def physical(r):
    row = {0, 7} | {9+i for i in range(WIDTH) if r >> i & 1}
    history = []
    for t in range(20):
        history.append(sorted(row))
        row = {i for i in range(min(row)-1, max(row)+2)
               if ((i-1 in row) != ((i in row) or (i+1 in row)))}
    return history


def main():
    out = Path(os.environ["CAPPED_OUT"])
    for r in list(range(64))+[1 << k for k in range(WIDTH)]+[MASK, 288]:
        assert samples(r) == literal_half(r), (r, "two half-rule implementations")
    assert samples(288) == "010101000"  # original four-cell witness, one sample short
    h = physical(288)
    assert next(t for t, row in enumerate(h) if int(8 in row) != (t & 1)) == 17
    found = None
    tested = 0
    for r in range(1 << WIDTH):
        if r % 256 == 0 and time.process_time()-START > 25:
            raise RuntimeError("25s payload CPU guard; incomplete query")
        tested += 1
        if samples(r) == TARGET:
            found = r
            break
    result = {"width": WIDTH, "target": TARGET, "tested": tested,
              "status": "SAT" if found is not None else "EXHAUSTED_NO_MATCH",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if found is not None:
        assert literal_half(found) == TARGET
        history = physical(found)
        trace = "".join(str(int(8 in row)) for row in history)
        failure = next(t for t, v in enumerate(trace) if int(v) != (t & 1))
        assert failure == 18, (found, failure, "physical transfer of membership failed")
        result.update({"right_prefix": found, "right_prefix_bits": "".join(str(found >> i & 1) for i in range(WIDTH)),
                       "initial_black_sites": history[0], "trace": trace,
                       "first_failure": failure, "rows": history})
    result["cpu_seconds"] = time.process_time()-START
    (out/'membership.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))


if __name__ == '__main__':
    main()
