#!/usr/bin/env python3
"""ether_episode_exact.py: the exact longest ether-pair episode M(k) behind a black right edge, k <= KMAX (L1258).

RUN-ON:     cpu (Python 3 + numpy), about a minute
COMMAND:    python3 tests/probes/ether_episode_exact.py [KMAX=20]

Frame: the edge code of Lowry's kit PR69 (head fcffbaa9, Rule30EtherGrounding). Digit 0 is constant black,
X_1(t+1) = X_1(t) XOR X_0(t), and X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) for j >= 2. Digits 0..j evolve
on their own (prefix autonomy), so the pair at depths k, k+1 depends only on the prefix X_1..X_(k+1). The map does
not depend on t and every prefix is a start, so the longest episode from any onset, over every black-edge row
(finite or not), is the longest initial run over all 2^(k+1) prefixes and all 32 ether phases (i mod 4, q mod 8).
An episode at phase (i, q) is a run of ticks with X_k(t) = ether(i, t+q) and X_(k+1)(t) = ether(i+1, t+q).
Prints, per k: M(k), the bounds ceil(2k/3) and floor(2k/3)+4 of GPT's GC2327-GC2328 sketches, the run of the
GC2328 witness (prefix X_j(0) = ether(j+3, 1), phase i = k+3, q = 1), and how many (prefix, phase) pairs attain M(k).
Controls: the edge map against a literal Rule 30 row with a rightmost black cell; PR69's ether_step and ether_pair
tables; the good-predicate maximal initial runs for k = 0..8 (GPT's GC2328 pilot reported 3,4,5,6,6,7,7,8,9).
Also (P-E5): the kit's period-seven wall sea, depths 1.. = 1100001 repeated, against the claimed depth-1 trace 1011.
Predictions P-E1..P-E5: reports/inquisition-20261031.md (round 3), committed before this ran.
"""
import sys
import numpy as np

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
WORDS = (43, 202, 178, 172)          # PR69 `ether`: column i mod 4, bit t mod 8


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


def good(r, u, v):
    r %= 8
    return [(not u) and v, u, (not u) and (not v), u, (not u) and (not v), u == (not v), u and (not v), u][r]


def step(X):
    """One edge-frame step on digits 0..len-1 (rows of X), every prefix at once."""
    Y = np.empty_like(X)
    Y[0] = 1
    Y[1] = X[1] ^ X[0]
    Y[2:] = X[2:] ^ (X[1:-1] | X[:-2])
    return Y


def start(k):
    n = 1 << (k + 1)
    r = np.arange(n, dtype=np.int64)
    X = np.zeros((k + 2, n), dtype=np.uint8)
    X[0] = 1
    for j in range(1, k + 2):
        X[j] = (r >> (j - 1)) & 1
    return X


def traces(k, H):
    X = start(k)
    a = np.empty((H, X.shape[1]), dtype=np.uint8)
    b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k + 1]
        X = step(X)
    return a, b


def controls():
    for i in range(4):
        for t in range(8):
            assert ether(i, t + 1) == ether(i, t) ^ (ether(i + 3, t) | ether(i + 2, t)), "ether_step"
            assert good(t + 2 * i, ether(i + 1, t), ether(i, t)), "ether_pair"
    rng = np.random.default_rng(20261031)
    T, depth = 40, 30
    for _ in range(200):
        width = 2 * T + depth + 10
        e = depth + 5
        row = np.zeros(width, dtype=np.uint8)
        row[e] = 1
        row[e - depth:e] = rng.integers(0, 2, depth, dtype=np.uint8)
        X = np.zeros((depth + 1, 1), dtype=np.uint8)
        X[:, 0] = row[e - np.arange(depth + 1)]
        for t in range(T):
            for j in range(depth + 1 - t):          # digits whose light cone stays inside the random prefix
                assert X[j, 0] == row[e + t - j], "edge map vs literal Rule 30"
            nxt = np.zeros_like(row)
            nxt[1:-1] = row[:-2] ^ (row[1:-1] | row[2:])
            row = nxt
            X = step(X)
    print("controls: ether_step, ether_pair, edge map vs literal Rule 30 (200 rows x 40 steps) PASS")


def good_runs(kmax=8):
    out = []
    for k in range(kmax + 1):
        H = (2 * k) // 3 + 6
        a, b = traces(k, H)
        best = 0
        for p in range(8):
            alive = np.ones(a.shape[1], dtype=bool)
            run = np.zeros(a.shape[1], dtype=np.int64)
            for t in range(H):
                u, v = b[t].astype(bool), a[t].astype(bool)
                r = (t + p) % 8
                g = [~u & v, u, ~u & ~v, u, ~u & ~v, u == ~v, u & ~v, u][r]
                alive &= g
                run += alive
            best = max(best, int(run.max()))
        out.append(best)
    print("good-predicate maximal initial runs, k = 0..8:", out)
    return out


def episodes(kmax):
    rows = []
    for k in range(1, kmax + 1):
        m = (2 * k) // 3
        lo, hi = -(-2 * k // 3), m + 4
        H = m + 6
        a, b = traces(k, H)
        best, nbest = 0, 0
        for i in range(4):
            for q in range(8):
                alive = np.ones(a.shape[1], dtype=bool)
                run = np.zeros(a.shape[1], dtype=np.int64)
                for t in range(H):
                    alive &= (a[t] == ether(i, t + q)) & (b[t] == ether(i + 1, t + q))
                    run += alive
                rm = int(run.max())
                if rm > best:
                    best, nbest = rm, int((run == rm).sum())
                elif rm == best:
                    nbest += int((run == rm).sum())
        wit = sum(ether(j + 3, 1) << (j - 1) for j in range(1, k + 2))
        wrun = 0
        for t in range(H):
            if a[t, wit] == ether(k + 3, t + 1) and b[t, wit] == ether(k + 4, t + 1):
                wrun += 1
            else:
                break
        flag = "OK" if lo <= best <= hi and wrun >= lo else "BOUND VIOLATED"
        print(f"k={k:2d} M={best:2d} bounds [{lo:2d},{hi:2d}] M-ceil={best - lo} witness run={wrun:2d} "
              f"attained by {nbest} (prefix, phase) pairs  {flag}")
        rows.append((k, best, lo, hi, wrun))
        assert best < H, "horizon reached: upper sketch refuted"
    return rows


def period_seven_sea(T=400):
    sea = [1, 1, 0, 0, 0, 0, 1]
    D = T + 10
    x = np.zeros(D + 2, dtype=np.uint8)            # x[0] is the white wall, depths 1..D, x[D+1] = 0
    for k in range(1, D + 1):
        x[k] = sea[(k - 1) % 7]
    trace = []
    for t in range(T):
        trace.append(int(x[1]))
        nxt = np.zeros_like(x)
        nxt[1:D + 1] = x[2:D + 2] ^ (x[1:D + 1] | x[0:D])
        x = nxt
    want = [1, 0, 1, 1] * (T // 4)
    ok = trace == want
    print(f"period-seven sea 1100001: depth-1 trace for t < {T} {'equals' if ok else 'DIFFERS from'} 1011 repeated; "
          f"first 16 {''.join(map(str, trace[:16]))}; even-time whites {sum(1 for t in range(0, T, 2) if not trace[t])}")
    return ok


def main():
    controls()
    g = good_runs()
    print("matches GPT's pilot 3,4,5,6,6,7,7,8,9:", g == [3, 4, 5, 6, 6, 7, 7, 8, 9])
    episodes(KMAX)
    period_seven_sea()
    print("ETHER_EPISODE_DONE")


if __name__ == '__main__':
    main()
