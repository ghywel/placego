"""staircase_rain_check.py: Local's independent check of GC1934 and of L999's link to the rain and the triangles.

Local, 2026-10-26, L999 (DQ-021, DQ-020). Own implementation; GPT's staircase_verify.py was read but not run or reused.
Standard orientation, x(i, t+1) = x(i-1, t) XOR (x(i, t) OR x(i+1, t)), black = 1. Every claim was derived by hand
first (L999 and reports/rule30-staircase-local-review.md); this script replays the finite cases.

Predictions (written before the run):
  S1  GC1934's alternative. For every maximal black bar [a, b] in column j of the single-seed orbit (with its future
      inside the grid), column j+1 has no 11 at adjacent times in [a, b+1]; it alternates there, or its first 00 at s
      gives column j+1 white on [s, b+1] and column j+2 black on [s, b+2].
  S2  Left companion. For the same bars, column j-1 is white on [a, b-1].
  S3  Front lemma (GC847, re-derived). In every row, a maximal alternating stretch [a, r] with r - a >= 2 keeps
      [a+1, r-1] unchanged, flips cell a, and so starts at exactly a+1 on the next row.
  S4  The front hangs a triangle. If that stretch starts with a black cell (x(a) = x(a-1) = 1), the next row is white
      exactly on [p+1, a+1], where [p, a] is the black run ending at a: width a+1-p >= 2, black at p and a+2.
  S5  After a front-hung triangle of width >= 3, the next one, hung two rows later at a+3, has width exactly 2,
      provided the stretch is still long enough (r >= a+5 on the first row).
  S6  The marked staircase (GC1934: global x 83..92, t 94..108). On each row from 94 to 108 the cells from the front
      to the last bar alternate, and the front moves right exactly one cell per row. Each white bar's last row is the
      top row of a hung triangle of width >= 2 whose right corner is that cell.
  S3 to S5 run on every row of length 18 (no wrap) and on every row of the single-seed orbit to t = 300.
Counterfactual: any violation means a slip in the hand derivation; S6 failing would mean the rain reading does not fit
the owner's staircase.
Record searched: "staircase" (GC1934 only), "rain" (CL094, GC847, L470: the (01) fixed point eaten from the left),
"alternating stretch" (GC847), "front.{0,30}triangle" 0, "hang" 0 outside L998.

Run: python3 -I tests/probes/wolfram/staircase_rain_check.py   (exit status 1 on any failure)

Outcome (2026-10-26, M5, 1.8 s): ALL CHECKS PASS, exit 0.
- S1: 22,321 single-seed bars; 16,607 alternate and 5,714 have a successor. S2: 11,238 left companions.
- S3: 111,446 instances, S4: 49,161, S5: 593, over every 18-cell row and 297 single-seed rows.
- S6: the front moves exactly one cell per row, from x = 78 at t = 94 to x = 91 at t = 107. The clock at x = 92 reads
  101010101 on t = 100..108, then 1. The hung triangles at white bars 84, 86, 88 and 90 have widths 2, 3, 2 and 4.
Every prediction held.

Three slips of mine, all in the harness or in my own test specification, fixed before any result was read as such:
- the first run's S6 took a maximum over an empty list at t = 108, where no bar is alive (the last ends at 107);
- my S6 specification wrongly treated the last bar's right neighbour, which is the clock, as a white bar;
- my first exhaustive window (16 cells) was too narrow to exercise S5 at all. It now uses 18 cells and prints counts.
"""
import sys


def step(row):
    n = len(row)
    return [(row[i - 1] if i else 0) ^ (row[i] | (row[i + 1] if i + 1 < n else 0)) for i in range(n)]


def stretches(row, lo, hi):
    """Maximal alternating stretches [a, r] with lo <= a-1 and r+1 <= hi (both breaking cells inside)."""
    out = []
    i = lo
    while i < hi:
        j = i
        while j + 1 <= hi and row[j + 1] != row[j]:
            j += 1
        if j - i >= 1 and i - 1 >= lo and row[i - 1] == row[i] and j + 1 <= hi and row[j + 1] == row[j]:
            out.append((i, j))
        i = j + 1
    return out


fails = []
count = {"S3": 0, "S4": 0, "S5": 0}


def front_checks(cur, nxt, nxt2, nxt3, lo, hi, tag):
    """S3, S4, S5 for one row; nxt2 and nxt3 may be None."""
    for a, r in stretches(cur, lo + 2, hi - 2):
        if r - a < 2:
            continue
        count["S3"] += 1
        if any(nxt[i] != cur[i] for i in range(a + 1, r)) or nxt[a] == cur[a]:
            fails.append(("S3", tag, a, r))
        if cur[a] == 1:
            p = a
            while p - 1 >= lo and cur[p - 1] == 1:
                p -= 1
            if p - 1 < lo:
                continue
            count["S4"] += 1
            ok = nxt[p] == 1 and nxt[a + 2] == 1 and all(nxt[k] == 0 for k in range(p + 1, a + 2))
            if not ok:
                fails.append(("S4", tag, a, r))
            width = a + 1 - p
            if width >= 3 and r >= a + 5 and nxt3 is not None:
                count["S5"] += 1
                ok5 = nxt3[a + 1] == 1 and nxt3[a + 2] == 0 and nxt3[a + 3] == 0 and nxt3[a + 4] == 1
                if not ok5:
                    fails.append(("S5", tag, a, r))


# S3 to S5 on every row of length 18 (cells within k of either end are untrusted after k steps)
N = 18
s345 = 0
for bits in range(1 << N):
    row = [(bits >> i) & 1 for i in range(N)]
    r1 = step(row)
    r2 = step(r1)
    r3 = step(r2)
    # only cells whose light cone stays inside the row are trusted: shrink the window by one per step
    front_checks(row, r1, r2, r3, 3, N - 4, ("all18", bits))
    s345 += 1

# single-seed orbit
T = 300
W = 2 * T + 3
g = [[0] * W]
g[0][T + 1] = 1
for t in range(T):
    g.append(step(g[-1]))
s1 = {"alternates": 0, "successor": 0}
s2 = 0
for j in range(2, W - 3):
    t = 0
    while t <= T:
        if g[t][j] != 1:
            t += 1
            continue
        a = t
        while t + 1 <= T and g[t + 1][j] == 1:
            t += 1
        b = t
        t += 1
        if a == 0 or b + 2 > T or (a > 0 and g[a - 1][j] == 1):
            continue
        z = [g[u][j + 1] for u in range(a, b + 2)]
        y = [g[u][j + 2] for u in range(a, b + 3)]
        if any(z[k] == z[k + 1] == 1 for k in range(len(z) - 1)):
            fails.append(("S1-11", j, a, b))
            continue
        s = next((k for k in range(len(z) - 1) if z[k] == z[k + 1] == 0), None)
        if s is None:
            s1["alternates"] += 1
        else:
            if any(v != 0 for v in z[s:]) or any(v != 1 for v in y[s:]):
                fails.append(("S1", j, a, b))
            s1["successor"] += 1
        if b > a:
            s2 += 1
            if any(g[u][j - 1] != 0 for u in range(a, b)):
                fails.append(("S2", j, a, b))
for t in range(T - 3):
    front_checks(g[t], g[t + 1], g[t + 2], g[t + 3], 1, W - 2, ("seed", t))

# S6: the marked staircase, global coordinates (seed at x = 0, t = 0); grid column = x + T + 1
X = lambda x: x + T + 1
bars = [(83, 94, 99), (85, 95, 101), (87, 95, 103), (89, 98, 105), (91, 100, 107)]
for x, a, b in bars:
    col = [g[u][X(x)] for u in range(a - 1, b + 2)]
    if col != [0] + [1] * (b - a + 1) + [0]:
        fails.append(("S6-bar", x, a, b))
clock = "".join(str(g[u][X(92)]) for u in range(100, 110))
if clock != "1010101011":
    fails.append(("S6-clock", clock))
fronts = []
for t in range(94, 108):                                        # rows with a black bar alive (the last ends at 107)
    row = g[t]
    right = max(x for x, a, b in bars if a <= t <= b)          # last black bar alive at t
    f = right
    while row[X(f - 1)] != row[X(f)]:
        f -= 1
    fronts.append((t, f))
for (t, f), (t2, f2) in zip(fronts, fronts[1:]):
    if f2 != f + 1:
        fails.append(("S6-front", t, f, f2))
hung = []
for x, a, b in bars[:-1]:                                        # the last bar's right neighbour is the clock
    c = x + 1                                                    # the white bar to the right of this black bar
    bw = b + 1                                                   # its last white row (black bar bottom + 1)
    if g[bw][X(c)] != 0 or g[bw + 1][X(c)] != 1:
        fails.append(("S6-whitebar", c, bw))
        continue
    p = c
    while g[bw][X(p - 1)] == 0:
        p -= 1
    hung.append((c, bw, c - p + 1))
    if c - p + 1 < 2:
        fails.append(("S6-hung", c, bw))

print("S1 GC1934 alternative on single-seed bars:", s1, "| S2 left companions checked:", s2)
print("S3-S5 rows checked:", s345, "of length 18, plus", T - 3, "single-seed rows; instances", count)
print("S6 fronts (t, x):", fronts[0], "...", fronts[-1], "| clock at x = 92, t = 100..109:", clock)
print("S6 hung triangles (white-bar column, row, width):", hung)
print("failures:", len(fails), fails[:5])
print("ALL CHECKS PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
