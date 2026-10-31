#!/usr/bin/env python3
"""inquisition_checker_imitation.py: do white-sea champions imitate the checkerboard beside the wall? (T-H2, DQ-034)

RUN-ON:     cpu (Python 3 + numpy), about a minute
COMMAND:    python3 tests/probes/inquisition_checker_imitation.py [WMAX=20]

The kit's normal form, as in inquisition_wall_census.py. For each W, every start is run to its death; at every even
time while alive, the agreement of depths 2..6 with the checkerboard phase that has depth 1 black (depth d black iff
d odd) is recorded. Prints the mean agreement over the champions' lives, and over the lives of all starts alive at
t = 4 (the comparison). Prediction P-H3 in reports/inquisition-20261031.md, committed before this ran.
"""
import sys
import numpy as np

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
CHECK = np.array([(d % 2) for d in range(2, 7)], dtype=np.uint8)[:, None]


def main():
    for W in range(8, WMAX + 1):
        n = 1 << W
        r = np.arange(n, dtype=np.int64)
        depth = 3 * W + 50
        x = np.zeros((depth + 2, n), dtype=np.uint8)
        for k in range(1, W + 1):
            x[k] = (r >> (k - 1)) & 1
        death = np.full(n, -1, dtype=np.int64)
        agree_sum = np.zeros(n)
        agree_cnt = np.zeros(n)
        t = 0
        while True:
            if t % 2 == 0:
                newly = (death < 0) & (x[1] == 0)
                death[newly] = t
                alive = death < 0
                if not np.any(alive[1:]):
                    break
                a = (x[2:7] == CHECK).mean(axis=0)
                agree_sum[alive] += a[alive]
                agree_cnt[alive] += 1
            nxt = np.zeros_like(x)
            nxt[1:depth] = x[2:depth + 1] ^ (x[1:depth] | x[0:depth - 1])
            x = nxt
            t += 1
        D = death[1:].max()
        champs = np.nonzero(death == D)[0]
        surv = np.nonzero(death > 4)[0]
        mean = lambda idx: float((agree_sum[idx] / np.maximum(agree_cnt[idx], 1)).mean())
        late = np.nonzero(death >= W)[0]
        print(f"W={W:2d} D={D:3d} champions {len(champs)}: mean agreement {mean(champs):.3f}; "
              f"alive at t=4 ({len(surv)}): {mean(surv):.3f}; dying at t >= W ({len(late)}): {mean(late):.3f}")
    print("IMITATION_DONE")


if __name__ == '__main__':
    main()
