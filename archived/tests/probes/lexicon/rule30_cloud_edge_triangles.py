#!/usr/bin/env python3
"""rule30_cloud_edge_triangles.py: the white triangles that touch the single cell's right edge.

RUN-ON:     cpu (Python 3 standard library; big-integer bit strings)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_edge_triangles.py [LOG2T=22] [K=72]
Exploratory: no prediction was pushed before the first run. It certifies the exact statements below on the window
computed, and measures the rest. Cloud, 2026-10-09, from the owner's observation of that day: "If at each depth you
take the right most visible black triangle, the beginning of the top right of each triangle is completely linearly
spaced. Every single black triangle touches the pyramid's right edge at a linear spacing interval, the only
difference is the size of the triangle." Rule 30's triangles are white (a white run shrinks by one cell at each end
per step; a black run breaks up), so these are the white triangles, which are dark on a dark-themed page.

Right diagonals: D_k(t) = x_t(t - k), so D_0 is the edge. Rule 30 gives D_k(t+1) = D_k(t) XOR (D_(k-1)(t) OR
D_(k-2)(t)), and every D_k is purely periodic with a power-of-2 period (RULE30-PRIZE.md §8.27; Jen 1990; Rowland).
Each D_k is the running XOR of the OR of the two diagonals to its right, computed here for every t at once as a
prefix XOR on a big integer whose bit t is time t.

The spacing, by hand. D_0 = 1 for ever, and D_1(t) = D_2(t) = t mod 2 (each is a running XOR of an all-ones
sequence, from 0). So at every even t >= 2 the cells t - 1 and t - 2 are white beside the black edge cell t, and at
every odd t the cell t - 1 is black. The white run ending at t - 1 starts a new triangle (the cell above it, at
t - 2 on row t - 1, is black). So exactly one triangle touches the edge every two rows, with its top-right corner on
the line x = t - 1, one cell inside the edge. Its width is L(t) = the number of consecutive white diagonals
D_1, D_2, ... at time t, at least 2.
Why the sizes look ordered: [L(t) >= k] reads only D_1 .. D_k, so it is periodic in t with period p_k, the period of
D_k. The size sequence is a stack of periodic layers whose periods double (a Toeplitz-type, hierarchical sequence),
which is the same nesting as the left band's and as the supertiles of a hierarchical tiling.
Proposition 23 (PROOFS.md entry 36) makes this exact for all time: L(t) = min{j >= 1 : p_j does not divide t} - 1.

OUTCOME of the first run, 2026-10-09 (08:42 BST, 6 s at LOG2T = 24, K = 64). Exploratory, labelled so above.
  The periods of D_0 .. D_54 are those of OEIS A094605, which notes that NKS p. 871 lists one 64 too few.
  At every even t < 2^24 the edge triangle's width depends only on the power of 2 in t. For v = 1 .. 23 it is
  2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, 33, 35, 36, 38, 40, 42, 47, 48, 50, 53, 54, 57, with spread 0 at every v.
  Each width equals Proposition 23's formula wherever the periods are determined (v <= 21).
  Direct simulation of the single cell, with no diagonal recurrence, agrees with the formula at every t from 1 to
  4095 (no difference). Odd times have no edge triangle.
"""
import sys

LOG2T = int(sys.argv[1]) if len(sys.argv) > 1 else 22
K = int(sys.argv[2]) if len(sys.argv) > 2 else 72
T = 1 << LOG2T
MASK = (1 << T) - 1


def prefix_xor(g):
    x, sh = g, 1
    while sh < T:
        x ^= (x << sh) & MASK
        sh <<= 1
    return x


def main():
    D = [MASK]                                              # D_0: the black edge
    prev2, prev1 = 0, MASK
    for k in range(1, K + 1):
        g = prev1 | prev2
        d = (prefix_xor(g) << 1) & MASK                     # D_k(t) = XOR of g(0 .. t-1)
        D.append(d)
        prev2, prev1 = prev1, d
    even = int("01" * (T // 2), 2)                          # bit t set for even t
    odd = MASK ^ even
    assert D[1] == odd and D[2] == odd, "D_1 and D_2 should be t mod 2"
    print(f"T = 2^{LOG2T} steps, diagonals 0 .. {K}")
    print("checked: D_0 = 1 and D_1 = D_2 = t mod 2 for every t < T, so one edge triangle starts at every even t")
    print("periods of the right diagonals (powers of 2; '>' means longer than T/2):")
    per = []
    for k in range(K + 1):
        p, found = 1, None
        while 2 * p <= T // 2:
            m = (1 << (T - p)) - 1
            if (D[k] >> p) & m == D[k] & m:
                found = p
                break
            p <<= 1
        per.append(found)
    print("  " + ", ".join(str(p) if p else ">" for p in per))
    # alive[k] = even times t >= 2 at which D_1 .. D_k are all white (width >= k)
    pc = (lambda x: x.bit_count()) if hasattr(int, "bit_count") else (lambda x: bin(x).count("1"))
    ev2 = even & ~1
    nev = pc(ev2)
    W, alive = 0, []
    for k in range(1, K + 1):
        W |= D[k]
        a = (~W) & ev2 & MASK
        if not a:
            break
        alive.append(a)
    kmax = len(alive)
    print("edge triangles of width >= k, as a share of the even times, and that share times 2^(k-2):")
    for k in range(1, kmax + 1):
        c = pc(alive[k - 1])
        print(f"  k = {k:2d}: {c:9d}  share {c / nev:.6f}  x 2^(k-2) = {c / nev * 2 ** (k - 2):.3f}")
    top = alive[-1]
    ts = []
    while top and len(ts) < 50:
        low = top & -top
        ts.append(low.bit_length() - 1)
        top ^= low
    print(f"widest edge triangles: width {kmax} at t = " + ", ".join(
        f"{t} (= {t // (t & -t)} x 2^{(t & -t).bit_length() - 1})" for t in ts[:12]))
    # the ruler comparison: the width's law given the 2-adic valuation of t
    print("width given v2(t), the exponent of 2 in t (a pure ruler sequence would make each row a single value):")
    for v in range(1, LOG2T):
        step = 1 << (v + 1)
        blk = 1 << v                                         # t = 2^v mod 2^(v+1)
        pattern = int(("0" * (step - 1 - blk) + "1" + "0" * blk), 2)
        Ev = int(format(pattern, f"0{step}b") * (T // step), 2) & MASK
        n = pc(Ev)
        if n == 0:
            break
        surv = [pc(alive[k - 1] & Ev) / n for k in range(1, kmax + 1)]
        mean = sum(surv)                                     # E L = sum over k >= 1 of P(L >= k)
        ex2 = sum((2 * k - 1) * sv for k, sv in enumerate(surv, 1))
        sd = max(0.0, ex2 - mean * mean) ** 0.5
        lo = next((k for k, sv in enumerate(surv, 1) if sv < 1), kmax + 1) - 1
        hi = max((k for k, sv in enumerate(surv, 1) if sv > 0), default=0)
        # Proposition 23's formula: the first diagonal whose period does not divide 2^v, minus one
        j = next((j for j in range(1, K + 1) if per[j] is None or per[j] > 2 ** v), None)
        form = (j - 1) if j is not None and per[j] is not None else None
        tag = "" if form is None else ("  = formula" if form == lo == hi else f"  FORMULA {form} DIFFERS")
        print(f"  v2(t) = {v:2d}: {n:8d} times, mean width {mean:6.2f}, spread {sd:5.2f}, from {lo} to {hi}{tag}")
    # independent cross-check by direct simulation of the single cell (no diagonal recurrence)
    S = 1 << 12
    x, bad = 1 << S, 0
    for t in range(S):
        if t >= 1:
            run, k = 0, 1
            while k <= t and not (x >> (S + t - k)) & 1:
                run, k = run + 1, k + 1
            v = (t & -t).bit_length() - 1
            want = 0 if t % 2 else next(j for j in range(1, K + 1) if per[j] > 2 ** v) - 1
            if run != want:
                bad += 1
        x = ((x << 1) ^ (x | (x >> 1))) & ((1 << (2 * S + 2)) - 1)
    print(f"direct simulation, t = 1 .. {S - 1}: the white run inside the edge differs from the formula {bad} times")

if __name__ == "__main__":
    main()
