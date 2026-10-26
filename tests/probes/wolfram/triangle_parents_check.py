"""triangle_parents_check.py: exhaustive guard on the hand lemmas of L998 (Local, 2026-10-26; DQ-020, GC1932).

Standard orientation, f(L,C,R) = L XOR (C OR R). Every claim below was derived by hand first (L998 and
reports/rule30-triangle-ancestry-local-read.md); this script only replays them on every finite row of one length.

Predictions (written before the run):
  K1  GC1932's pair maps T_0, T_1 and its three block maps (001, 101, 101000) are as tabled; the chain
      101110 -> 101000 -> 101101 -> 001001 -> 111111 -> 000000 holds on period-6 rings; and the hand extension
      001000 -> 011100, 100111 -> 011100, 011100 -> 110010, 110010 -> 101110 holds too. On the 6-ring 011100 has
      exactly two preimages (001000, 100111) and each of 101000, 101110, 110010 has exactly one.
  K2  Parent trichotomy: every maximal white run [a, b] (length L >= 1, black at a-1 and b+1) of a row y = F(x) has
      exactly one of three parent shapes:
        C  x = 1 0^(L+2) 1   on [a-2, b+2]   (continuation of a run two wider),
        A  x = 0 1^(L+1) 0 0 on [a-2, b+2]   (a new cap),
        B  x = 0 1^L 0 1     on [a-2, b+1]   (hung from a white singleton at b).
      Exact window counts on all 2^N rows: C and A each 2^(N-(L+4)) per position, B 2^(N-(L+3)): ratio 1:1:2.
  K3  Singleton rule: if x(c) = 0, x(c-1) = x(c+1) = 1 and the black run ending at c-1 is [p, c-1] (x(p-1) = 0),
      then y is white exactly on [p+1, c], black at p and at c+1.
  K4  (added after K1 to K3 passed, before its own first run) An odd triangle's tip hangs its child with width k
      with probability exactly 2^-k under fair rows, first generation only: over all 2^15 free left parts behind a
      fixed tip window 1 0 0 0 1, the child of width k occurs exactly 2^(15-k) times.
Counterfactual: any failure means a slip in the hand algebra or in orientation.
Record searched: "singleton.{0,60}(white|zero)" 42 (GC847 has the width-1 case of K3 and the 1/16 versus 3/32
split), "1:1:2" 0, "two.thirds.{0,40}(top|triangle)" 0, "black run.{0,40}becomes.{0,20}white" 0, "011100"/"110010"/
"100111" only unrelated words, "in-tree" 3 (Q7 driver trees, a different object).

Run: python3 -I tests/probes/wolfram/triangle_parents_check.py   (about 10 s on the M5)
Outcome (2026-10-26, M5, 2.3 s): ALL CHECKS PASS. K1 PASS (6-ring preimages of 011100 are 001000 and 100111).
K2: 851,972 runs at N = 18, 0 failures, exact 1:1:2 counts at every position and length. K3: 425,986 cases,
0 failures. K4: counts 16384, 8192, 4096, ... exactly 2^(15-k). Every prediction held. K4's first run stopped on
its own assertion because I had placed the tip window one cell off (c = M-4 for M-3). This was an indexing slip in
the script, fixed before any count was read.
"""
from itertools import product


def f(l, c, r):
    return l ^ (c | r)


def ring_step(w):
    n = len(w)
    return tuple(f(w[i - 1], w[i], w[(i + 1) % n]) for i in range(n))


def T(b, pair):
    u, v = pair
    return (b ^ (u | v), u)


def block_map(target):
    """Right-to-left composition over the target word: pair (x_{i+p-1}, x_{i+p}) -> (x_{i-1}, x_i)."""
    def B(pair):
        for b in reversed(target):
            pair = T(b, pair)
        return pair
    return B


fails = 0
PAIRS = [(0, 0), (0, 1), (1, 0), (1, 1)]
w = lambda s: tuple(int(ch) for ch in s)

# K1
T0 = {p: T(0, p) for p in PAIRS}
T1 = {p: T(1, p) for p in PAIRS}
fails += T0 != {(0, 0): (0, 0), (0, 1): (1, 0), (1, 0): (1, 1), (1, 1): (1, 1)}
fails += T1 != {(0, 0): (1, 0), (0, 1): (0, 0), (1, 0): (0, 1), (1, 1): (0, 1)}
B001, B101, B101000 = block_map(w("001")), block_map(w("101")), block_map(w("101000"))
fails += [B001(p) for p in PAIRS] != [(1, 1), (0, 0), (1, 1), (1, 1)]
fails += [B101(p) for p in PAIRS] != [(0, 1), (1, 0), (0, 1), (0, 1)]
fails += [B101000(p) for p in PAIRS] != [(0, 1)] * 4
chain = ["001000", "011100", "110010", "101110", "101000", "101101", "001001", "111111", "000000"]
for a, b in zip(chain, chain[1:]):
    fails += ring_step(w(a)) != w(b)
fails += ring_step(w("100111")) != w("011100")
all6 = list(product((0, 1), repeat=6))
pre = {}
for x in all6:
    pre.setdefault(ring_step(x), []).append(x)
fails += sorted(pre.get(w("011100"), [])) != sorted([w("001000"), w("100111")])
for s in ("101000", "101110", "110010"):
    fails += len(pre.get(w(s), [])) != 1
print("K1 pair/block maps and chain:", "PASS" if fails == 0 else "FAIL", "| 6-ring preimages of 011100:",
      ["".join(map(str, p)) for p in pre.get(w("011100"), [])])

# K2 and K3 on all rows of length N (no wrap; only fully determined cells are used)
N = 18
counts = {}
k2_fail = k3_fail = k2_cases = k3_cases = 0
for bits in range(1 << N):
    x = [(bits >> i) & 1 for i in range(N)]
    y = [None] + [f(x[i - 1], x[i], x[i + 1]) for i in range(1, N - 1)] + [None]
    # K2: maximal white runs of y with black ends at a-1, b+1 and parent window [a-2, b+2] inside the row
    i = 1
    while i < N - 1:
        if y[i] == 0 and y[i - 1] == 1:
            a = i
            b = a
            while b + 1 < N - 1 and y[b + 1] == 0:
                b += 1
            if b + 1 < N - 1 and y[b + 1] == 1 and a - 2 >= 0 and b + 2 <= N - 1:
                L = b - a + 1
                seg = x[a - 2:b + 3]
                isC = seg == [1] + [0] * (L + 2) + [1]
                isA = seg == [0] + [1] * (L + 1) + [0, 0]
                isB = seg[:-1] == [0] + [1] * L + [0, 1]
                k2_cases += 1
                if isC + isA + isB != 1:
                    k2_fail += 1
                key = (a, L)
                c = counts.setdefault(key, [0, 0, 0])
                c[0] += isC
                c[1] += isA
                c[2] += isB
            i = b + 1
        else:
            i += 1
    # K3: isolated white cells with their left black run fully inside
    for c in range(2, N - 2):
        if x[c] == 0 and x[c - 1] == 1 and x[c + 1] == 1:
            p = c - 1
            while p - 1 >= 0 and x[p - 1] == 1:
                p -= 1
            if p - 1 < 0:
                continue
            k3_cases += 1
            ok = y[c + 1] == 1 and y[p] == 1 and all(y[k] == 0 for k in range(p + 1, c + 1))
            k3_fail += not ok

# K4: an odd triangle's tip hangs a child of width k with probability 2^-k (first generation, fair rows).
# Time s: a white triple at [c-1, c+1] flanked by black (window 1 0 0 0 1 on [c-2, c+2]); every other cell free.
# Time s+1: singleton at c. Time s+2: the white run ending at c has width k = the black run ending at c-1 at s+1.
M = 20
c = M - 3                                                  # cells 0 .. M-6 free, window on [c-2, c+2]
widths = {}
for bits in range(1 << (M - 5)):
    left = [(bits >> i) & 1 for i in range(M - 5)]       # cells 0 .. c-3
    x = left + [1, 0, 0, 0, 1] + [0]                       # cells c-2 .. c+2, then one more right cell
    y = [None] + [f(x[i - 1], x[i], x[i + 1]) for i in range(1, len(x) - 1)] + [None]
    z = [None, None] + [f(y[i - 1], y[i], y[i + 1]) for i in range(2, len(y) - 2)] + [None, None]
    assert y[c] == 0 and y[c - 1] == 1 and y[c + 1] == 1 and z[c] == 0 and z[c + 1] == 1
    k = 0
    j = c
    while j >= 2 and z[j] == 0:
        k += 1
        j -= 1
    if j < 2:
        continue                                           # child runs off the determined part: censored
    widths[k] = widths.get(k, 0) + 1
k4_ok = all(widths.get(k, 0) == (1 << (M - 5)) >> k for k in range(1, M - 9))
fails += not k4_ok
print("K4 tip-child widths (k: count):", {k: widths[k] for k in sorted(widths)[:8]},
      "| exact 2^(M-5-k) for k < M-9:", "PASS" if k4_ok else "FAIL")

ratio_ok = True
for (a, L), (nC, nA, nB) in counts.items():
    span_C = L + 4
    span_B = L + 3
    expect_C = 1 << (N - span_C)
    expect_B = 1 << (N - span_B)
    # B's window [a-2, b+1] must also sit inside; C/A need [a-2, b+2]; counts are per (a, L) over all rows,
    # but a run counted here also needed y[b+1] inside the row, so every key has the full C window available.
    if (nC, nA, nB) != (expect_C, expect_C, expect_B):
        ratio_ok = False
fails += k2_fail + k3_fail + (not ratio_ok)
print(f"K2 trichotomy: {k2_cases} runs, {k2_fail} failures; exact 1:1:2 window counts at every (position, length):",
      "PASS" if ratio_ok else "FAIL")
print(f"K3 singleton rule: {k3_cases} cases, {k3_fail} failures")
print("ALL CHECKS PASS" if fails == 0 else f"{fails} FAILURES")
