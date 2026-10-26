"""run_rule_check.py: exhaustive guard on L1000's run rule, the patch law and their general consequences.

Local, 2026-10-26, L1000. Standard orientation f(L,C,R) = L XOR (C OR R), black = 1. Every statement was proved by
hand first (reports/rule30-run-rule.md); this script replays them on every state of the stated finite sizes.

Predictions (written before the run):
  G1  Run rule. On every ring of length 2..16, Rule 30's next row equals the run image applied in place:
      black run B_m -> 1 0^(m-1); white run W_1 -> 0; white run W_n (n >= 2) -> 1 0^(n-2) 1
      (an all-black ring -> all white; an all-white ring -> all white).
  G2  Patch law (two orbits). For backgrounds y in {0, 1, rain in both phases, every period-3 ring point, and four
      fixed random rows} and every row x of length 14: for each maximal interval [a, r] of agreement between x and y
      with r >= a+1, fully inside the trusted window, the next rows disagree at a, agree on [a+1, r-1], and agree at r
      exactly when the shared cell x(r) = y(r) is black. For r = a (both neighbours disagree), they agree at a exactly
      when the shared cell is white.
  G3  Black assembly. On every ring of length 4..16 with at least one white and one black run, every black run of
      length L in the next row lies over exactly r whole units B_1 W_2 (the word 100) of the current row, with
      3r + 1 <= L <= 3r + 4.
  G4  Counting (rings). black(t+1) = #black runs + 2 #(white runs of length >= 2); and
      #black runs(t+1) - #black runs(t) = #units(m >= 2, n >= 3) - #units(m = 1, n = 2).
  G5  Edge law, every finite seed. For every seed supported in [0, w-1] with its rightmost cell black, w <= 12,
      evolved 300 steps: the edge black run's length L alternates between 1 and >= 2; when L_t >= 2 the next row has
      a white run of width exactly L_t - 1 just left of the edge cell; consecutive emitted widths w -> w' obey
      1 -> 1, >= 3 -> 2, 2 -> >= 3.
  G5b (added after G1 to G6 had run, before its own first run) The edge type is fixed by one bit at time 0: with c1, c2 the
      two cells left of the seed's rightmost black cell, every emission has width 1 when c1 XOR c2 = 1 (a rain edge),
      and no emission has width 1 when c1 = c2 (a half-ruler: widths alternate between exactly 2 and at least 3).
  G6  The single seed's edge widths at even t = 2^v * odd equal 8.73's w(v) = 2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28,
      33 for v = 1..12, and obey G5's rhythm through t = 4200.
Counterfactual: any failure means a slip in the hand proofs or in orientation.
Record searched: "run substitution" 0, "first cell of (each|every|a|its) black run" 0, "1 0^{m-1}" 0, "run.length"
139 (no run rule), "jigsaw" (8.72's eight tiles, a different object), "agreement (interval|set|region)" 8 (G7/G8's
gate charging, a different object), "damage.{0,30}(spread|front)" 29: 8.66's front identity is the patch law's right
half. Web (two standard searches): no run-by-run statement of Rule 30 found; Wolfram states it per cell.

Run: python3 -I tests/probes/wolfram/run_rule_check.py   (exit status 1 on any failure)
Outcome (2026-10-26, M5, 3.8 s): ALL CHECKS PASS, exit 0. Every prediction held.
- G1: the run rule matched Rule 30 on all 131,068 rings of length 2..16.
- G2: 409,620 patch intervals and 491,520 single-cell ones, over 20 backgrounds. The ring search to length 12 found
  exactly 12 period-3 points, the record's count (Epperlein, 8.77).
- G3: 491,512 black runs. G4: 131,030 rings.
- G5: 4,095 seeds and 608,107 width pairs; G5b split them into 2,048 half-rulers and 2,047 rain edges.
- G6: the widths are 8.73's 2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, 33.

Three slips of mine in this checker, none a counterexample:
- G4b first failed on the 12 rings made only of 100 units, which turn all black in one step: I had counted that ring
  as one black run, but the law counts heads and an all-black ring has none. Convention fixed.
- The period-3 backgrounds were first searched only on rings of length 8 or less, where none exist, so that control
  was vacuous. The search now goes to length 12.
- G5 was first written with Python lists and would have taken many minutes. I stopped it before it printed anything
  and rewrote it with integer rows.
"""
import random
import sys

fails = []
count = {}


def bump(k, n=1):
    count[k] = count.get(k, 0) + n


def ring_step(x):
    n = len(x)
    return [x[i - 1] ^ (x[i] | x[(i + 1) % n]) for i in range(n)]


def line_step(x):
    n = len(x)
    return [(x[i - 1] if i else 0) ^ (x[i] | (x[i + 1] if i + 1 < n else 0)) for i in range(n)]


def ring_runs(x):
    """Cyclic maximal runs as (start, length, colour), starting at a boundary; None if the ring is constant."""
    n = len(x)
    s0 = next((i for i in range(n) if x[i] != x[i - 1]), None)
    if s0 is None:
        return None
    runs = []
    i = s0
    while True:
        j = i
        L = 0
        while True:
            L += 1
            j = (j + 1) % n
            if x[j] != x[i]:
                break
        runs.append((i, L, x[i]))
        i = j
        if i == s0:
            return runs


def run_image(x):
    n = len(x)
    runs = ring_runs(x)
    if runs is None:
        return [0] * n
    y = [None] * n
    for s, L, c in runs:
        img = ([1] + [0] * (L - 1)) if c == 1 else ([0] if L == 1 else [1] + [0] * (L - 2) + [1])
        for k in range(L):
            y[(s + k) % n] = img[k]
    return y


# G1 and G3 and G4 on rings
for n in range(2, 17):
    for bits in range(1 << n):
        x = [(bits >> i) & 1 for i in range(n)]
        nxt = ring_step(x)
        bump("G1")
        if run_image(x) != nxt:
            fails.append(("G1", n, bits))
        runs = ring_runs(x)
        if runs is None or n < 4:
            continue
        # units: (black run, following white run)
        units = []
        for idx, (s, L, c) in enumerate(runs):
            if c == 1:
                ws, wl, wc = runs[(idx + 1) % len(runs)]
                units.append((s, L, wl))
        nb = len(units)
        nw2 = sum(1 for s, L, c in runs if c == 0 and L >= 2)
        bump("G4")
        if sum(nxt) != nb + 2 * nw2:
            fails.append(("G4a", n, bits))
        nruns = ring_runs(nxt)
        nb_next = 0 if nruns is None else sum(1 for s, L, c in nruns if c == 1)   # heads; an all-black ring has none
        long_long = sum(1 for s, m, w in units if m >= 2 and w >= 3)
        bridge = sum(1 for s, m, w in units if m == 1 and w == 2)
        if nb_next - nb != long_long - bridge:
            fails.append(("G4b", n, bits))
        # G3: black runs of the next row versus whole 100 units inside them
        if nruns is None:
            continue
        for s, L, c in nruns:
            if c != 1:
                continue
            cells = {(s + k) % n for k in range(L)}
            r = sum(1 for us, m, w in units if m == 1 and w == 2 and {(us + k) % n for k in range(3)} <= cells)
            bump("G3")
            if not (3 * r + 1 <= L <= 3 * r + 4):
                fails.append(("G3", n, bits, s, L, r))

# G2 patch law
N = 14
backgrounds = [("zero", [0] * (N + 4)), ("one", [1] * (N + 4)),
               ("rain01", [i % 2 for i in range(N + 4)]), ("rain10", [(i + 1) % 2 for i in range(N + 4)])]
for q in range(1, 13):                                         # period-3 points on rings of length q
    for bits in range(1 << q):
        z = [(bits >> i) & 1 for i in range(q)]
        if ring_step(ring_step(ring_step(z))) == z and ring_step(z) != z:
            backgrounds.append(("p3-q%d-%d" % (q, bits), [z[i % q] for i in range(N + 4)]))
rng = random.Random(1000)
for k in range(4):
    backgrounds.append(("random%d" % k, [rng.randint(0, 1) for _ in range(N + 4)]))
for name, ybig in backgrounds:
    y = ybig[:N]
    y1 = line_step(y)
    for bits in range(1 << N):
        x = [(bits >> i) & 1 for i in range(N)]
        x1 = line_step(x)
        i = 1
        while i < N - 1:                                       # trusted cells after one step: 1 .. N-2
            if x[i] != y[i]:
                i += 1
                continue
            a = i
            while i + 1 < N and x[i + 1] == y[i + 1]:
                i += 1
            r = i
            i += 1
            if a - 1 < 0 or r + 1 > N - 1 or x[a - 1] == y[a - 1] or x[r + 1] == y[r + 1] or r > N - 2:
                continue
            if r >= a + 1:
                bump("G2")
                ok = x1[a] != y1[a] and all(x1[k] == y1[k] for k in range(a + 1, r)) and \
                    ((x1[r] == y1[r]) == (x[r] == 1))
                if not ok:
                    fails.append(("G2", name, bits, a, r))
            else:
                bump("G2-single")
                if (x1[a] == y1[a]) != (x[a] == 0):
                    fails.append(("G2-single", name, bits, a))
count["G2-backgrounds"] = len(backgrounds)

# G5 edge law for every finite seed of width <= 12 (big-int rows: bit i is a cell, left neighbour at bit i-1)
T5 = 300


def ones_down(x, e):
    k = 0
    while (x >> (e - k)) & 1:
        k += 1
    return k


def zeros_down(x, e):
    k = 0
    while not (x >> (e - k)) & 1:
        k += 1
    return k


for w in range(1, 13):
    for bits in range(1 << (w - 1)):
        xi = (bits | (1 << (w - 1))) << (T5 + 4)
        prevL = None
        widths = []
        bad = False
        for t in range(T5):
            e = xi.bit_length() - 1
            L = ones_down(xi, e)
            if prevL is not None:
                if (prevL >= 2) != (L == 1):
                    fails.append(("G5-alt", w, bits, t))
                    bad = True
                    break
                if prevL >= 2:
                    k = zeros_down(xi, e - 1)
                    if k != prevL - 1:
                        fails.append(("G5-width", w, bits, t))
                        bad = True
                        break
                    widths.append(k)
            prevL = L
            xi = (xi << 1) ^ (xi | (xi >> 1))
        # G5b: the edge type is fixed at time 0 by the two cells left of the seed's rightmost black cell
        c1 = (bits >> (w - 2)) & 1 if w >= 2 else 0
        c2 = (bits >> (w - 3)) & 1 if w >= 3 else 0
        rain_predicted = (c1 ^ c2) == 1
        if widths and (all(v == 1 for v in widths) != rain_predicted or (not rain_predicted and 1 in widths)):
            fails.append(("G5b-type", w, bits))
        bump("G5b-rain" if rain_predicted else "G5b-half-ruler")
        for u, v in zip(widths, widths[1:]):
            bump("G5-pairs")
            if (u == 1 and v != 1) or (u >= 3 and v != 2) or (u == 2 and v < 3):
                fails.append(("G5-rhythm", w, bits, u, v))
                break
        bump("G5-seeds")

# G6 the single seed's edge (big-int rows: bit i is cell i - OFF)
T6 = 4200
OFF = T6 + 2
xint = 1 << OFF
mask = (1 << (2 * OFF + 2)) - 1
expected = {1: 2, 2: 3, 3: 5, 4: 6, 5: 8, 6: 14, 7: 15, 8: 23, 9: 24, 10: 26, 11: 28, 12: 33}
seen = {}
widths6 = []
for t in range(T6):
    if t >= 2 and t % 2 == 0:
        e = xint.bit_length() - 1
        if (xint >> (e - 1)) & 1:
            fails.append(("G6-shape", t))
        k = 0
        while not (xint >> (e - 1 - k)) & 1:
            k += 1
        v = (t & -t).bit_length() - 1
        widths6.append(k)
        if v in expected:
            seen.setdefault(v, set()).add(k)
    xint = ((xint << 1) ^ (xint | (xint >> 1))) & mask
for v, ws in seen.items():
    if ws != {expected[v]}:
        fails.append(("G6-ruler", v, sorted(ws)))
for u, v in zip(widths6, widths6[1:]):
    bump("G6-pairs")
    if (u == 1 and v != 1) or (u >= 3 and v != 2) or (u == 2 and v < 3):
        fails.append(("G6-rhythm", u, v))
        break

print("instances:", count)
print("G6 widths by v:", {v: sorted(ws) for v, ws in sorted(seen.items())})
print("failures:", len(fails), fails[:5])
print("ALL CHECKS PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
