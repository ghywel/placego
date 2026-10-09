#!/usr/bin/env python3
"""rule30_cloud_shunted_column.py: shunt the centre column left or right through the single cell's pyramid.

RUN-ON:     cpu (Python 3 standard library; big-integer rows)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_shunted_column.py [LOG2T=16]
COST:       expected about a minute at LOG2T = 16.

Why (the owner, 2026-10-09, after Cloud's reading of their front argument against period 2, which they accepted and
asked GPT to audit with priority, CL079): "I'll add an additional wrinkle, move the centre column. It is just a
descending column of alternating coins, so shunt it left or right and see what happens."

Known before the run (reasoning from the record, not measured here).
  Rule 30 is shift-invariant, so column c of the single seed is the centre column of the seed moved to -c: the
    prize question has the same form for every column. Jen (1990): no two adjacent columns are both eventually
    periodic.
  The band's edge (§8.74, B(t) with P = 2^10) moves left at about 0.245 cells a step. A column c < 0 is born on the
    left edge at row |c|, so it starts inside the band and should leave it near row |c| / 0.245, about 4.1 |c|. The
    right ordered strip is about 2.8 log2 t cells wide (§8.30), so a column c > 0, born on the right edge at row c,
    spends only a few rows in it. Every column ends in the core, between the two fronts, where the centre is.

Definitions. Column c at row t (t >= |c|) is bit t + c of V_t (V_t has bit e = x_t(-t + e)). The cell is in the band
when t + c < B(t), with B(t) the lowest set bit of V_t xor V_(t+P), P = 2^10, as in rule30_cloud_left_boundary.py.
A column's band interval runs from its birth to its first row outside the band (sigma_c); tau_c is its last band row.
An alternating stretch is a maximal run of rows in which every cell differs from the one above it (0101...).

PREDICTIONS, written 2026-10-09 12:48 BST, before any run of this script (LOG2T = 16; columns -8000 to 8000 in steps
of 100, plus -50, -25, -10, -5, -1, 1, 5, 10, 25, 50).
  SH1 (the front crosses each column once; confidence 0.8). For every c <= -100, the band rows are one interval from
      the birth row |c| to sigma_c, plus at most re-entries within 64 rows of sigma_c (the front's jaggedness), and
      none later; for |c| >= 500, tau_c / |c| lies in [3.3, 5.5] (about 4.1 expected from the speed). For every
      c >= 1, no band row after row 20.
  SH2 (low confidence, 0.55). A column is not periodic while in the band: for every c <= -500, the second half of
      its band interval has no period q <= a quarter of its length.
  SH3 (0.8). In the band a column is far simpler than in the core: for every c <= -1000, the second half of its band
      interval has at most a quarter as many distinct 10-bit words as a stretch of the same length from the same
      column's core.
  SH4 (0.8). In the core, columns' longest alternating stretches look like fair coins: over the columns, the mean of
      (longest stretch - log2 n), n the core length, is within 1.5 of the same mean for fair coins of the same
      lengths, and no core column has an alternating stretch longer than 2 log2 n. The centre column is included.
  SH5, the unexpected check (0.6). No memory of the band: in the first 256 core rows after each column leaves the
      band (c <= -500, pooled), cells differ from the cell above at a rate within 0.03 of 1/2, the core's rate
      (§8.70: a step in place reads Rule 210, a coin).
  Counterfactuals. If SH1 fails late (a column re-enters the band long after it left), the front comes back, which
      §8.74 has not seen. If SH2 fails (band columns periodic), the band hosts periodic column stretches and the
      front's crossing is where a column's periodicity ends: the owner's picture would be literal for columns, though
      still no proof for the centre column, which leaves the band at row 20. If SH4 fails, some column carries
      alternation beyond chance, which would be a lead for period 2 itself.
"""
import math
import random
import sys
from collections import deque

LOG2T = int(sys.argv[1]) if len(sys.argv) > 1 else 16
P = 1 << 10
T = 1 << LOG2T
COLS = sorted(set(range(-8000, 8001, 100)) | {-50, -25, -10, -5, -1, 1, 5, 10, 25, 50})


def longest_alt(s):
    best = run = 1 if s else 0
    for i in range(1, len(s)):
        run = run + 1 if s[i] != s[i - 1] else 1
        best = max(best, run)
    return best


def least_period(s, qmax):
    for q in range(1, qmax + 1):
        if all(s[i] == s[i + q] for i in range(len(s) - q)):
            return q
    return None


def words(s, k=10):
    return len({tuple(s[i:i + k]) for i in range(len(s) - k + 1)})


def simulate():
    bits = {c: bytearray() for c in COLS}
    band = {c: bytearray() for c in COLS}
    win, V = deque(), 1
    for s in range(T + P):
        win.append(V)
        if len(win) > P:
            Vt = win.popleft()
            t = s - P
            d = Vt ^ V
            B = (d & -d).bit_length() - 1
            raw = Vt.to_bytes((2 * t + 1 + 7) // 8, "little")
            for c in COLS:
                if abs(c) <= t:
                    k = t + c
                    bits[c].append((raw[k >> 3] >> (k & 7)) & 1)
                    band[c].append(1 if k < B else 0)
        V = (V << 2) ^ ((V << 1) | V)
    return bits, band


def main():
    bits, band = simulate()
    print(f"T = 2^{LOG2T}, P = 2^10, {len(COLS)} columns")
    rnd = random.Random(30)
    sh1, ratios, late, right_late = True, [], [], []
    sh2, sh3, sh5a, sh5b, bandflip = [], [], [0, 0], [0, 0], [0, 0]
    core_stats = []
    for c in COLS:
        s, b, birth = bits[c], band[c], abs(c)
        rows = [birth + i for i, f in enumerate(b) if f]
        if c >= 1:
            if rows and max(rows) > 20:
                right_late.append((c, max(rows)))
            core_from = max(21, birth + 64) - birth
        elif c == 0:
            core_from = 21
        else:
            sigma = next((birth + i for i, f in enumerate(b) if not f), None)
            tau = max(rows)
            if sigma is None:
                print(f"  c = {c}: never leaves the band by T")
                continue
            if tau - sigma > 64:
                late.append((c, sigma, tau))
            if c <= -100 and abs(c) >= 500:
                ratios.append((c, tau / abs(c)))
            core_from = tau + 1 - birth
            if c <= -500:
                H = s[(sigma - birth) // 2: sigma - birth]
                q = least_period(H, len(H) // 4)
                sh2.append((c, len(H), q))
                bandflip[0] += sum(H[i] != H[i - 1] for i in range(1, len(H)))
                bandflip[1] += len(H) - 1
                first = s[core_from: core_from + 257]
                later = s[core_from + 257:]
                sh5a[0] += sum(first[i] != first[i - 1] for i in range(1, len(first)))
                sh5a[1] += len(first) - 1
                sh5b[0] += sum(later[i] != later[i - 1] for i in range(1, len(later)))
                sh5b[1] += len(later) - 1
                if c <= -1000:
                    C = s[core_from: core_from + len(H)]
                    if len(C) == len(H):
                        sh3.append((c, len(H), words(H), words(C)))
        K = s[core_from:]
        n = len(K)
        if n > 1000:
            fair = bytes(rnd.getrandbits(1) for _ in range(n))
            core_stats.append((c, n, longest_alt(K), longest_alt(fair)))
    print("SH1: re-entries more than 64 rows after the first exit:", late or "none")
    print("     columns c >= 1 with a band row after row 20:", right_late or "none")
    if ratios:
        rs = [r for _, r in ratios]
        print(f"     tau/|c| for |c| >= 500: min {min(rs):.3f}, max {max(rs):.3f}, mean {sum(rs) / len(rs):.3f}")
    print("     ratios at |c| = 500, 1000, 2000, 4000, 8000:",
          [f"{c}: {r:.3f}" for c, r in ratios if abs(c) in (500, 1000, 2000, 4000, 8000)])
    per = [(c, h, q) for c, h, q in sh2 if q is not None]
    print(f"SH2: band halves with a period <= a quarter of their length: {len(per)} of {len(sh2)}", per[:12])
    if sh3:
        worst = max(sh3, key=lambda r: r[2] / r[3])
        print(f"SH3: distinct 10-bit words, band half vs core stretch (worst ratio): c = {worst[0]}, length {worst[1]},"
              f" {worst[2]} vs {worst[3]}; all ratios <= 1/4: {all(4 * a <= b for _, _, a, b in sh3)}")
        print("     samples:", [(c, h, a, b) for c, h, a, b in sh3 if c in (-1000, -2000, -4000, -8000)])
    m_core = sum(L - math.log2(n) for _, n, L, _ in core_stats) / len(core_stats)
    m_fair = sum(F - math.log2(n) for _, n, _, F in core_stats) / len(core_stats)
    over = [(c, n, L) for c, n, L, _ in core_stats if L > 2 * math.log2(n)]
    print(f"SH4: mean (longest alternating stretch - log2 n): core {m_core:+.2f}, fair coins {m_fair:+.2f};"
          f" columns over 2 log2 n: {over or 'none'}")
    top = sorted(core_stats, key=lambda r: r[2] - math.log2(r[1]), reverse=True)[:5]
    print("     the five most alternating core columns (c, n, longest, fair-coin twin):", top)
    print("     centre column:", [r for r in core_stats if r[0] == 0])
    print(f"SH5: flip rate in the first 256 core rows {sh5a[0] / sh5a[1]:.4f} ({sh5a[1]} steps);"
          f" later core rows {sh5b[0] / sh5b[1]:.4f}; band halves {bandflip[0] / bandflip[1]:.4f}")


if __name__ == "__main__":
    main()
