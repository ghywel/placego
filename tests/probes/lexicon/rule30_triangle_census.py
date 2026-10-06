#!/usr/bin/env python3
"""rule30_triangle_census.py: CONSTELLATION.md row 13, the triangle census of the single cell. The shrink theorem of
section 8.18 (checked by rule30_triangles.py on a million runs): a maximal white run of length L >= 2 becomes exactly
the run one cell shorter at each end a step later, so every white triangle is an exact isosceles triangle fixed by
its birth. A run is the TOP of a triangle exactly when it is not the continuation of the run above, i.e. when the
cells above it, one wider on each side, are not all white. rule30_triangles.py followed the triangles next to a
clamped wall (the owner's kick lead); this census counts the tops of the single cell's own pyramid by width L and by
position x/t in the light cone (whose edges are black at every step, so no run touches them) to T = 10^5 steps,
listing every top of width >= 24. Three regions: the left band (x/t < -0.6, the periodic diagonals), the core
(|x/t| <= 0.3), the nested right side (x/t > 0.7). (Local, 2026-10-06; RULE30-PRIZE.md section 8.68.)

RUN-ON:     cpu, one core (numpy)
COMMAND:    python3 tests/probes/lexicon/rule30_triangle_census.py [T=100000]
COST:       a few minutes.

SEEN BEFORE these predictions: the pictures everyone has seen (large triangles on the nested right side; a core that
looks random); the band's periodic diagonals; section 8.18's exploratory note that next to the wall sizes fall off
by about a factor 4 per 2 cells of width; no count of the single cell's triangles. Literature to check afterwards:
Wolfram 1984 ("Universality and complexity in cellular automata") measured triangle-size distributions as a statistic
of class 3 rules; recorded in PRIOR-ART.md as a lead, not read.

PREDICTIONS, written 2026-10-06 before the first run.
  TC0 (control, must hold): over the first 60 rows the vectorised census equals an independent set-based census
      (every run matched to the run above it), top by top.
  CF  (counterfactual, must fail): over the whole cone the counts by width are geometric, N(L + 1) / N(L) in
      [0.4, 0.6] for every L from 3 to L_max - 6. The nested right side's large triangles must break this.
  TC1 (blind): in the core the counts are geometric with ratio one half: N(L + 1) / N(L) in [0.4, 0.6] for every L
      from 3 to 12, the coin seen through triangles (section 8.18's factor 4 per 2 cells is the same ratio).
  TC2 (blind): the widest top in the core to 10^5 steps is between 26 and 40 cells.
  TC3 (blind): the widest top of the whole cone lies on the right side (x/t > 0.7) and is more than twice the core's
      widest.
  TC4 (blind): the left band's tops are bounded: the widest at x/t < -0.6 is under 12 cells.
REFUTED-BY: TC0 failing or CF holding (the instrument); TC1 to TC4 the other way. What would change my mind: a core
ratio away from one half (the core's white runs would not be coin-like at the level of triangles, which bears on
Problem 2), or a left band with a large triangle (the band's bounded periods would have to allow it).

OUTCOME of the first run, 2026-10-06 (T = 10^5, 4 minutes). TC0, CF PASSED. TC1 HELD far beyond its bracket: the core's
  ratios are 0.500, 0.500, 0.500, 0.499, 0.503, 0.500, 0.496, 0.495, 0.507, 0.485 for L = 3 .. 12, and the counts
  themselves are 281,011,418; 140,641,871; 70,333,586; 35,178,509; 17,580,624; 8,797,846; ... ; 137,109 (L = 12);
  ... 29 (one top of width 29, two of 28). Derived AFTER the run and then matched: the uniform measure is invariant
  under Rule 30 (a surjective rule), and under it a maximal white run [i, j] of length L has probability 2^-(L+2),
  while the continuation (the cells above, one wider each side, all white, and black beyond them so that the run is
  exactly [i, j]) has probability 2^-(L+4); so the density of tops of width L is 3 * 2^-(L+4) per cell. Against the
  core's area 0.3 T^2 = 3.0 * 10^9 that predicts 281,250,000; 140,625,000; 70,312,500; 35,156,250; 17,578,125 for L =
  1 .. 5 (measured within 0.09%, 0.01%, 0.03%, 0.06%, 0.02%) and 549,316 at L = 10 (measured 547,147, -0.4%), 17,166
  at L = 15 (16,585), 536 at L = 20 (505), 1.05 at L = 29 (2). The widest core top, 29, is where 3 * 2^-(L+4) * area
  = 1, i.e. L = 29.1. TC2 HELD (29). TC3 REFUTED in its second clause: the widest tops of the cone sit ON the right
  edge (x/t = 1.000) at the times m * 2^k: 40 at 65,536, 38 at 32,768 and 98,304, 36 at 16,384, 49,152, 81,920, 35 at
  8,192 and the odd multiples of it; they grow like log2 t + 22 and so are not twice the core's 29. TC4 REFUTED: the
  left band has tops of widths 15 (21,916 of them) and 16 (5,882) and none wider; its ratios are near 1/2 to L = 9
  and then structured (0.61 at 10, 0.88 at 15). Not pre-registered and so only a reading: the band's widest run
  equals its period 16.

RANDOM-ROW ADDENDUM, written 2026-10-06 before the second run (python3 rule30_triangle_census.py 50000 random): the same
  census on a random row of width 300,003 (seed 20261006), counted only inside the inner light cone (cells no
  boundary can have reached), where the field is EXACTLY the uniform measure at every time (the rule is surjective,
  so the uniform measure is invariant). Area 1.25 * 10^10 cells, four times the single cell's core.
  TR0 (control, must hold): the white density in the inner cone is 0.5 within 10^-4.
  TR1 (the derivation, must hold): the tops' counts are 3 * 2^-(L+4) * area within 0.05% for L = 1 .. 6.
  TR2 (blind): the single cell's -0.09% at L = 1 does NOT appear here (the random row's L = 1 count is within 0.02%
      of the law), so the deficit belongs to the single cell's orbit, not to the law.
  CF  (counterfactual, must fail): no top wider than 16 (the band's cutoff). The law expects about 140 tops of width
      24 and a widest near 31.
  REFUTED-BY: TR0 or TR1 failing (the derivation of 3 * 2^-(L+4) misses a correlation); TR2 the other way (the deficit
  is the law's and the derivation is only approximate); CF holding.
  OUTCOME of the second run, 2026-10-06 (random; T = 50,000, 3 minutes): TR0 PASSED (0.500001). TR1 PASSED: the
  deviations from 3 * 2^-(L+4) * area are -0.002%, +0.003%, -0.006%, +0.000%, -0.004%, +0.004% for L = 1 .. 6 (counts
  1,171,848,670; 585,956,651; 292,950,068; ...), Poisson-sized; at L = 10, 15, 20, 24: 2,290,402 (law 2,288,818),
  71,594 (71,526), 2,187 (2,235), 117 (140); widest 31 (CF PASSED). TR2 HELD: the L = 1 count is -0.002% from the
  law, so the single cell's -0.09% is the orbit's, not the law's. The derivation is exact as stated.

BLOCK ADDENDUM, written 2026-10-06 before the third run (python3 rule30_triangle_census.py 100000 blocks), after
  GPT's pushback (C080): tops on a deterministic space-time are dependent, so "fifteen sigma" from the total count
  alone is not justified; the calibration is replicates. The core is split into ten time blocks of 10^4 rows and
  two halves (x/t in [-0.3, 0) and [0, 0.3)); for each, the counts of tops of width 1 .. 4 against the law and the
  white density.
  TB0 (control, must hold): the twenty cells' counts sum to the first run's core counts exactly.
  TB1 (blind, the calibration): the width-1 deficit is systematic: every one of the ten time blocks shows a
      deviation between -0.05% and -0.15% from 3 * 2^-5 * block area. If the blocks scatter with mixed signs, GPT's
      caution stands and the sigma claim is withdrawn in the record.
  TB2 (blind): the core's white density is within 0.01% of 1/2 in every block, so the deficit is not a density
      effect (a white excess of 0.02% would be needed to produce it).
  TB3 (blind): the two halves of the core show the deficit alike, within a factor of 2 of each other.
  CF  (counterfactual, must fail): the width-2 tops show the same systematic deficit (every block between -0.05%
      and -0.15%). The first run's L = 2 total was +0.012%, so this must fail.
  REFUTED-BY: TB0 failing (the instrument); TB1 failing (then "fifteen sigma" is withdrawn); TB2, TB3 the other way;
  CF holding.
  OUTCOME of the third run, 2026-10-06 (blocks; 4 minutes). TB0, CF PASSED. TB1 REFUTED, and GPT's caution stands: the
  width-1 deviation by time block is -0.034%, -0.220%, +0.034%, -0.314%, +0.087%, -0.189%, -0.100%, -0.074%, +0.025%,
  -0.136% (total -0.086%): mixed signs, a scatter of about 0.13% against a Poisson 0.02% per block. "Fifteen sigma"
  is WITHDRAWN. TB3 REFUTED: the deficit lives in the LEFT half of the core (x/t in [-0.3, 0): -0.161%, blocks from
  -0.641% to +0.213%) while the right half is at -0.011% with blocks within +-0.06%. TB2 REFUTED by the left half as
  well: its white density by block is 0.50000, 0.50019, 0.49984, 0.50016, 0.50002, 0.50000, 0.50017, 0.49998, 0.49967,
  0.49995 (up to 0.033% off), the right half's within 0.003%. So the single cell's core is uniform-measure-like to
  about 0.01% on its right half and only to about 0.1 - 0.3% on its left half, block by block, where the ordered
  side's influence still reaches; the -0.09% total is an average of that, not a constant of the orbit.
"""
import sys
import numpy as np

T = int(next((a for a in sys.argv[1:] if a.isdigit()), 100000))
LMAX = 64
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def runs_of_zeros(row):
    """start and end (inclusive) of every maximal zero run in a 0/1 row whose first and last cells are 1."""
    d = np.diff(row.astype(np.int8))
    starts = np.nonzero(d == -1)[0] + 1
    ends = np.nonzero(d == 1)[0]
    return starts, ends


def census(T, record=True):
    """the histogram H[L, bin] (bins of x/t of width 0.1 from -1 to 1), the big tops, and the first rows' tops."""
    W = 2 * T + 3
    a = np.zeros(W, dtype=np.uint8); c = W // 2; a[c] = 1
    H = np.zeros((LMAX + 1, 20), dtype=np.int64)
    big, first = [], {}
    prev = a.copy()
    for t in range(1, T + 1):
        l = np.empty_like(a); l[1:] = a[:-1]; l[0] = 0
        r = np.empty_like(a); r[:-1] = a[1:]; r[-1] = 0
        a = l ^ (a | r)
        lo, hi = c - t, c + t                       # the cone; both edge cells are black
        row = a[lo:hi + 1]
        s, e = runs_of_zeros(row)
        if len(s):
            L = e - s + 1
            P = np.concatenate(([0], np.cumsum(prev[lo - 1:hi + 2], dtype=np.int64)))   # prev over [lo-1, hi+1]
            cont = (P[e + 3] - P[s]) == 0            # prev[s-1 .. e+1] all white (row index s -> prev index s-1 -> P index s)
            top = ~cont
            xs = (s[top] + lo - c) + (L[top] - 1) / 2.0   # centre of the run relative to the seed
            Lt = L[top]
            bins = np.clip(((xs / t + 1.0) * 10).astype(int), 0, 19)
            np.add.at(H, (np.minimum(Lt, LMAX), bins), 1)
            if record:
                for k in np.nonzero(Lt >= 24)[0]:
                    big.append((t, float(xs[k]), int(Lt[k])))
            if t <= 60:
                first[t] = sorted((int(s[k] + lo - c), int(L[k])) for k in np.nonzero(top)[0])
        prev = a
    return H, big, first


def census_slow(T):
    """independent control: rows as Python sets of white cells, runs matched to the run above."""
    cells = {0}
    out, prevruns = {}, set()
    for t in range(1, T + 1):
        new = set()
        for x in range(-t, t + 1):
            l, cc, r = (x - 1) in cells, x in cells, (x + 1) in cells
            if l ^ (cc or r):
                new.add(x)
        cells = new
        runs = set()
        x = -t
        while x <= t:
            if x not in cells:
                y = x
                while y + 1 <= t and (y + 1) not in cells:
                    y += 1
                runs.add((x, y)); x = y + 1
            else:
                x += 1
        out[t] = sorted((x, y - x + 1) for (x, y) in runs if (x - 1, y + 1) not in prevruns)
        prevruns = runs
    return out


def census_random(T, W, seed=20261006):
    rng = np.random.default_rng(seed)
    a = rng.integers(0, 2, W, dtype=np.uint8)
    H = np.zeros((LMAX + 1,), dtype=np.int64)
    white, area, widest_seen = 0, 0, 0
    prev = a.copy()
    for t in range(1, T + 1):
        l = np.empty_like(a); l[1:] = a[:-1]; l[0] = 0
        r = np.empty_like(a); r[:-1] = a[1:]; r[-1] = 0
        a = l ^ (a | r)
        lo, hi = t + 1, W - 2 - t                   # the inner cone, one cell inside what the edges could reach
        row = a[lo:hi + 1]
        area += hi - lo + 1; white += int(row.size - row.sum())
        # runs inside the window only: cut the window with black sentinels so no run touches its ends
        rw = np.concatenate(([1], row, [1]))
        s, e = runs_of_zeros(rw)
        if len(s):
            s = s - 1 + lo; e = e - 1 + lo              # back to array indices
            L = e - s + 1
            P = np.concatenate(([0], np.cumsum(prev[lo - 1:hi + 2], dtype=np.int64)))
            cont = (P[e - lo + 3] - P[s - lo]) == 0
            top = ~cont
            Lt = L[top]
            np.add.at(H, np.minimum(Lt, LMAX), 1)
        prev = a
    return H, white / area, area


def random_mode():
    W = 300003
    H, dens, area = census_random(T, W)
    print(f"   random row: area {area}, white density {dens:.6f}")
    print("   counts by width: " + " ".join(f"{L}:{int(H[L])}" for L in range(1, LMAX + 1) if H[L]))
    pred = [3 * 2.0 ** -(L + 4) * area for L in range(LMAX + 1)]
    devs = [(H[L] - pred[L]) / pred[L] for L in range(1, 7)]
    print("   deviations from 3 * 2^-(L+4) * area, L = 1 .. 6: " + " ".join(f"{d * 100:+.3f}%" for d in devs))
    print("   L = 10, 15, 20, 24: " + " ".join(f"{int(H[L])} (law {pred[L]:.0f})" for L in (10, 15, 20, 24)))
    report("TR0 white density 0.5 within 1e-4", abs(dens - 0.5) <= 1e-4, f"{dens:.6f}")
    report("TR1 counts within 0.05% of the law for L = 1 .. 6", all(abs(d) <= 5e-4 for d in devs))
    verdict("TR2 the L = 1 count is within 0.02% of the law (the single cell's -0.09% is the orbit's)", abs(devs[0]) <= 2e-4, f"{devs[0] * 100:+.3f}%")
    nz = np.nonzero(H)[0]
    report("CF  tops wider than 16 exist", int(nz[-1]) > 16, f"widest {int(nz[-1])}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def census_blocks(T, nb=10):
    """the core only: counts of tops of width 1 .. 8 and white cells, by time block and by half of the core."""
    W = 2 * T + 3
    a = np.zeros(W, dtype=np.uint8); c = W // 2; a[c] = 1
    H = np.zeros((9, nb, 2), dtype=np.int64)
    white = np.zeros((nb, 2), dtype=np.int64); area = np.zeros((nb, 2), dtype=np.int64)
    prev = a.copy()
    bs = T // nb
    for t in range(1, T + 1):
        l = np.empty_like(a); l[1:] = a[:-1]; l[0] = 0
        r = np.empty_like(a); r[:-1] = a[1:]; r[-1] = 0
        a = l ^ (a | r)
        lo, hi = c - t, c + t
        row = a[lo:hi + 1]
        s, e = runs_of_zeros(row)
        b = min((t - 1) // bs, nb - 1)
        # white density and area by half, cells with x/t in [-0.3, 0) and [0, 0.3)
        xl = int(np.ceil(-0.3 * t)); xr = int(np.ceil(0.3 * t)) - 1       # cells -0.3t <= x < 0.3t
        seg = a[c + xl:c + xr + 1]; mid = -xl
        area[b, 0] += mid; area[b, 1] += seg.size - mid
        white[b, 0] += mid - int(seg[:mid].sum()); white[b, 1] += (seg.size - mid) - int(seg[mid:].sum())
        if len(s):
            L = e - s + 1
            P = np.concatenate(([0], np.cumsum(prev[lo - 1:hi + 2], dtype=np.int64)))
            cont = (P[e + 3] - P[s]) == 0
            top = ~cont
            xs = (s[top] + lo - c) + (L[top] - 1) / 2.0
            Lt = L[top]
            sel = (xs >= -0.3 * t) & (xs < 0.3 * t) & (Lt <= 8)
            half = (xs[sel] >= 0).astype(int)
            np.add.at(H, (Lt[sel], b, half), 1)
        prev = a
    return H, white, area


def blocks_mode():
    H, white, area = census_blocks(T)
    nb = H.shape[1]
    tot = H.sum(axis=(1, 2))
    print("   core totals by width 1 .. 8:", [int(tot[L]) for L in range(1, 9)])
    dens = white / area
    print("   white density by block (left half | right half): " + " ".join(f"{dens[b, 0]:.5f}|{dens[b, 1]:.5f}" for b in range(nb)))
    dev = {}
    for L in (1, 2, 3, 4):
        law = 3 * 2.0 ** -(L + 4) * area
        dev[L] = (H[L] - law) / law
        print(f"   width {L}: deviation by block, left|right: " + " ".join(f"{dev[L][b, 0] * 100:+.3f}%|{dev[L][b, 1] * 100:+.3f}%" for b in range(nb)))
        both = (H[L].sum(axis=1) - law.sum(axis=1)) / law.sum(axis=1)
        print(f"            both halves: " + " ".join(f"{v * 100:+.3f}%" for v in both) + f"   total {(H[L].sum() - law.sum()) / law.sum() * 100:+.3f}%")
    first = [281011418, 140641871, 70333586, 35178509]
    report("TB0 the block counts sum to the first run's core counts for L = 1 .. 4",
           [int(tot[L]) for L in range(1, 5)] == first, f"{[int(tot[L]) for L in range(1, 5)]}")
    b1 = (H[1].sum(axis=1) - (3 / 32) * area.sum(axis=1)) / ((3 / 32) * area.sum(axis=1))
    verdict("TB1 every time block's width-1 deviation lies in [-0.15%, -0.05%]", all(-1.5e-3 <= v <= -5e-4 for v in b1),
            " ".join(f"{v * 100:+.3f}%" for v in b1))
    verdict("TB2 the white density is within 0.01% of 1/2 in every block", bool(np.all(np.abs(dens - 0.5) <= 1e-4)),
            f"max |dens - 1/2| = {float(np.max(np.abs(dens - 0.5))):.6f}")
    lh = (H[1][:, 0].sum() - (3 / 32) * area[:, 0].sum()) / ((3 / 32) * area[:, 0].sum())
    rh = (H[1][:, 1].sum() - (3 / 32) * area[:, 1].sum()) / ((3 / 32) * area[:, 1].sum())
    verdict("TB3 the two halves show the width-1 deficit alike (within a factor 2)",
            lh < 0 and rh < 0 and 0.5 <= lh / rh <= 2, f"left {lh * 100:+.3f}%, right {rh * 100:+.3f}%")
    b2 = (H[2].sum(axis=1) - (3 / 64) * area.sum(axis=1)) / ((3 / 64) * area.sum(axis=1))
    report("CF  width-2 tops do NOT show the same systematic deficit in every block", not all(-1.5e-3 <= v <= -5e-4 for v in b2),
           " ".join(f"{v * 100:+.3f}%" for v in b2))
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if "blocks" in sys.argv[1:]:
        blocks_mode()
        return
    if "random" in sys.argv[1:]:
        random_mode()
        return
    H, big, first = census(T)
    slow = census_slow(60)
    report("TC0 the vectorised census equals the set-based census over the first 60 rows",
           all(first.get(t, []) == slow[t] for t in range(1, 61)))
    core = H[:, 7:13].sum(axis=1)       # x/t in [-0.3, 0.3)
    left = H[:, 0:4].sum(axis=1)        # x/t < -0.6
    right = H[:, 17:20].sum(axis=1)     # x/t >= 0.7
    whole = H.sum(axis=1)

    def widest(v):
        nz = np.nonzero(v)[0]
        return int(nz[-1]) if len(nz) else 0
    for name, v in (("core", core), ("left", left), ("right", right)):
        print(f"   counts by width, {name}: " + " ".join(f"{L}:{int(v[L])}" for L in range(1, 41) if v[L]), flush=True)
    print("   widest top: core", widest(core), " left", widest(left), " right", widest(right), " whole", widest(whole))
    bigs = sorted(big, key=lambda b: -b[2])[:12]
    print("   the widest tops (t, x/t, L): " + ", ".join(f"({b[0]}, {b[1] / b[0]:+.3f}, {b[2]})" for b in bigs))
    ratios_whole = [whole[L + 1] / whole[L] for L in range(3, max(4, widest(whole) - 6)) if whole[L]]
    report("CF  whole-cone counts are NOT geometric at every width up to L_max - 6",
           not all(0.4 <= q <= 0.6 for q in ratios_whole), f"ratios {[round(q, 2) for q in ratios_whole]}")
    ratios_core = [core[L + 1] / core[L] for L in range(3, 13)]
    verdict("TC1 core ratios N(L+1)/N(L) in [0.4, 0.6] for L = 3 .. 12", all(0.4 <= q <= 0.6 for q in ratios_core),
            f"{[round(q, 3) for q in ratios_core]}")
    verdict("TC2 widest core top between 26 and 40", 26 <= widest(core) <= 40, f"{widest(core)}")
    wb = bigs[0] if bigs else (1, 0, 0)
    verdict("TC3 the widest top of the cone is on the right side and more than twice the core's widest",
            bool(bigs) and wb[1] / wb[0] > 0.7 and wb[2] > 2 * widest(core), f"widest {wb}, core {widest(core)}")
    verdict("TC4 the left band's widest top is under 12", widest(left) < 12, f"{widest(left)}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
