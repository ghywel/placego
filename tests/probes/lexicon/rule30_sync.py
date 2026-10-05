#!/usr/bin/env python3
"""rule30_sync.py: are the wheel's slips synchronised in time across right halves? The untested hint of section
8.10 (the window-by-window mean speed swings far more than independent right halves would give), a small item on
PERIOD-TWO.md's board. (Local, 2026-10-06; section 8.60.)

RUN-ON:     cpu, one core (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_sync.py [W=12] [T=4096]   |   ... wide   |   ... dedup   |   ... long
COST:       a minute.

METHOD. As in rule30_wheelspeed.py: for every unlocked right half up to W cells, column 1 over T steps is cut into
windows of 56 steps; a window is exact when column 1 equals the wheel U at some phase, and a slip window otherwise.
Let s_h(k) = 1 when half h slips at window k, and N(k) = sum over halves. If halves slipped independently of one
another (whatever each one's own rate), N(k) would be a sum of independent indicators and its Fano factor
Var_k N / Mean_k N over a range of windows would be at most 1. A Fano factor well above 1 means the halves tend
to slip at the same windows: synchrony in time, whether from a common clock (all halves start at time 0 against
the same wall, so the wheel's formation is a shared event) or from anything else. The control: each half's slip
series is circularly shifted by its own random offset within the range, which keeps every half's rate and
pattern and destroys only the alignment across halves. The same is done for the mean excess speed v(k) of
section 8.10 (the summed kicks per window, averaged over halves): its spread over windows, real against shifted.
Three ranges: early (windows 2 to 11, the formation), middle (12 to 39), late (40 to 72).

SEEN BEFORE these predictions: section 8.10's run (the swings of v(k), from -0.21 to +0.15 notches per window;
+-0.04 was the back-of-envelope expectation for independent halves). No Fano factor has been computed.

PREDICTIONS, written 2026-10-06 before this script's first run.
  S0 (control, must hold): every phase change between exact windows is an even time shift (as in rule30_wheelspeed).
  S1 (blind): the halves slip together early: the Fano factor of N(k) over the early range is at least 3.
  S2 (blind): the synchrony fades: the Fano factor over the late range is at most 1.5.
  S3 (blind): the spread of v(k) over the early range is at least twice the shifted control's; over the late
      range it is less than twice the control's.
  CF  (counterfactual, must fail): the shifted control shows synchrony. It must not: its Fano factor lies in
      [0.8, 1.25] in every range.
REFUTED-BY: S0 or CF failing (the instrument); S1 to S3 the other way. If S2 is refuted the synchrony is not the
  formation's and is worth a section of its own.

OUTCOME of the first run, 2026-10-06 (W = 12, T = 4096, 19 seconds): 3,936 unlocked halves, 73 windows. S0 PASSED.
  Slips per window: early 1131, middle 1017, late 989 of 3,936 (a quarter of the halves slip in any window).
  Fano factors, real against shifted: early 5.82 / 0.49; middle 2.65 / 0.86; late 3.14 / 0.92.
  Spread of v(k), real against shifted: early 0.0856 / 0.0389; middle 0.1218 / 0.0360; late 0.0944 / 0.0363.
  S1 HELD (5.82). S2 REFUTED: the synchrony does not fade; the late Fano factor is 3.14 against 0.92. S3 REFUTED in
  its late half (ratios 2.20 early, 2.60 late). CF FAILED BY DESIGN: the band [0.8, 1.25] assumed rare slips; for
  independent halves with rates p_h the Fano factor is 1 - sum p_h^2 / sum p_h, below 1 - mean p, and the control
  sits there (0.49 with the early range's strong trend, 0.86, 0.92). So the halves slip at the same windows at every
  time, three times the independent variance even late. An exploratory look (no predictions written): at windows
  10 to 70 the wheel's phase across halves is always even and favours 4, 6 and 8 (about 8.5% each, against 3.6% for a
  uniform even phase), a stationary preference, not a lock to the clock; the late slip counts, 884 to 1135, show
  spikes at single windows rather than a slow trend.

ADDENDUM, written 2026-10-06 after the first run and before the second (python3 rule30_sync.py wide). Is the
  synchrony a property of the wall and the wheel (a common clock, which any population of right halves would
  share) or of the sample (halves that share their cells nearest the wall)? Two disjoint populations decide it.
  SA0 (control, must hold): the shifted control's Fano factor lies within 0.1 of the independence value
      1 - sum p_h^2 / sum p_h in every range, for the population of width <= 12.
  SA1 (blind; a common component scales with the population): with all unlocked halves of width <= 14 (about
      four times as many), the late Fano factor minus its independence value is at least three times the same
      excess for width <= 12.
  SA2 (blind; the two populations co-vary): the slip counts per window of the halves of width <= 12 and of the
      halves of width exactly 13 or 14 (disjoint sets) have correlation at least 0.5 over windows 12 to 72.
  SA3 (blind; window-local, not a drift): the lag-1 autocorrelation of the width <= 12 slip counts over windows
      12 to 72 is below 0.3.
REFUTED-BY: SA0 failing (the instrument); SA1 to SA3 the other way. SA2 refuted would mean the synchrony is the
  sample's, not the wheel's.

OUTCOME of the second run, 2026-10-06 (wide; 75 seconds): SA0 PASSED (the shifted control sits at the independence
  value in every range). SA1 REFUTED: the late excess Fano factor at width <= 14 (15,744 halves) is 2.05 against
  2.42 at width <= 12: it does not grow with the population, so the synchrony is not a modulation shared by all
  halves. SA2 and SA3 were NOT computed: the harness failed (statistics.correlation needs Python 3.10; this Mac
  runs 3.9), and SA2 was in any case ill designed: a half of width 13 shares its 12 cells nearest the wall with
  a half of width 12, so the two populations were not disjoint in what matters.

SECOND ADDENDUM, written 2026-10-06 before the third run (python3 rule30_sync.py wide). The excess that does not
  scale with the population points at clusters: halves that share their cells nearest the wall slipping together,
  which would mean the wheel shields the wall from the interior (section 8.30's handedness: a change arriving from
  the right of a black cell is hidden). Sisters: R and R + 2^12 differ only by a black cell at position 13.
  SB0 (control, must hold): every sister pair has identical columns 1 for the first 12 steps (the light cone).
  SB1 (blind; shielding): at least 20% of sister pairs, R unlocked, have identical columns 1 over all T steps, and
      the median first differing time over the pairs that differ is above 200 steps.
  SB2 (blind): over the late range, the correlation of the slip indicators of sister pairs that do differ is at
      least 0.3 on average, and that of random pairs is below 0.05.
  SB3 (blind; the clock test done right): grouping the unlocked halves of width <= 12 by their 6 cells nearest the
      wall (64 groups), the mean correlation between different groups' slip counts over windows 12 to 72 is below
      0.1: no common clock. Within groups the Fano factor over the late range exceeds its independence value by
      at least 1 (the sisters).
REFUTED-BY: SB0 failing (the harness); SB1 to SB3 the other way. SB3's first half refuted would restore the clock.

OUTCOME of the third run, 2026-10-06 (wide; 38 seconds): SB0 PASSED. 1,479 of the 3,936 sister pairs (37.6%) have
  identical columns 1 over all 4,096 steps; the rest first differ at a median of 34 steps (quartiles 26 and 50).
  SB1 REFUTED by its second half (the median 34, not above 200: a sister's extra cell either reaches the wall
  within about 50 steps or never). SB2 REFUTED: sisters that do differ have no late correlation (0.001; random
  pairs 0.004). SB3 HELD: cross-group correlation 0.009 (no common clock); within-group excess Fano 1.24.
  So the synchrony of the first run is duplication: halves whose columns 1 are the same sequence.

THIRD ADDENDUM, written 2026-10-06 before the fourth run (python3 rule30_sync.py dedup). Damage in Rule 30 always
  spreads right at speed 1 (the XOR of the left neighbour), so a difference at cell 13 rides with the right edge;
  it reaches the wall only if its left front escapes into the chaotic core. The claims to test:
  SC1 (blind): the number of distinct columns 1 among the 3,936 unlocked halves of width <= 12 is between 2,000 and
      3,200.
  SC2 (blind; duplication is the whole story): after keeping one half per distinct column 1, the late Fano factor
      is within 0.3 of its independence value.
  SC3 (blind; the damage rides the edge): for at least 90% of the identical sister pairs, the leftmost cell where
      the two patterns differ at time 4,096 lies within 60 cells of the right edge (cell 13 + 4,096).
REFUTED-BY: SC1 to SC3 the other way.

OUTCOME of the fourth run, 2026-10-06 (dedup; 40 seconds; a first attempt crashed on a missing sister column, a
  harness error, and was fixed): SC1 REFUTED by 32: 1,968 distinct columns 1 among the 3,936 unlocked halves (983
  traces from one half, 495 from two, 241 from three, ... one from twelve; pairs differ in their outermost cell or
  two). SC2 HELD: after deduplication the late Fano factor is 0.75 against an independence value of 0.73 (shifted
  0.68): the synchrony is duplication and nothing else. SC3 HELD: for all 1,479 identical sister pairs the damage's
  leftmost cell at time 4,096 lies within 60 cells of the right edge.

FOURTH ADDENDUM, written 2026-10-06 before the fifth run (python3 rule30_sync.py long).
  SC4 (blind; the damage never comes back): of the first 200 identical sister pairs (in order of R), at least 95%
      still have identical columns 1 at 16,384 steps.
REFUTED-BY: SC4 the other way.

OUTCOME of the fifth run, 2026-10-06 (long; 21 seconds): SC4 HELD, 200 of 200 identical sister pairs stay identical
  to 16,384 steps. Exploratory afterwards (no predictions): grouping all 4,096 halves by their outermost k cells, the
  share of identical sisters is 0 or 1 in 56 of the 64 groups at k = 6 (9 of 16 at k = 4): the capture is decided
  by the far end, in the first few steps.
"""
import math, pathlib, random, statistics, sys

_nums = [a for a in sys.argv[1:] if a not in ("wide", "dedup", "long")]
WIDE = "wide" in sys.argv[1:]
DEDUP = "dedup" in sys.argv[1:]
LONG = "long" in sys.argv[1:]
W = int(_nums[0]) if len(_nums) > 0 else 12
T = int(_nums[1]) if len(_nums) > 1 else 4096
P = 56
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
ROT = {tuple(U[(t - d) % P] for t in range(P)): d for d in range(P)}
FAILS = 0
RANGES = {"early": (2, 12), "middle": (12, 40), "late": (40, 73)}


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column1(R, n):
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = R << 1, []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return out


def fano(counts):
    m = statistics.fmean(counts)
    return statistics.pvariance(counts) / m if m > 0 else float("nan")


def population(halves, nwin):
    """per half: the slip indicator per window (locked halves dropped)"""
    out = []
    for R in halves:
        c = column1(R, T)
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad < T - P - 400:
            continue
        out.append([1 if ROT.get(tuple(c[k * P:(k + 1) * P])) is None else 0 for k in range(nwin)])
    return out


def excess(slips, a, b, rng):
    """the Fano factor over windows a..b-1, its independence value, and a shifted control's"""
    N = [sum(s[k] for s in slips) for k in range(a, b)]
    n = b - a
    p = [sum(s[a:b]) / n for s in slips]
    indep = 1 - sum(x * x for x in p) / sum(p)
    Nc = [0] * n
    for s in slips:
        off = rng.randrange(n)
        for j in range(n):
            Nc[j] += s[a + (j + off) % n]
    return fano(N), indep, fano(Nc), N


def corr(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x); syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy) if sxx > 0 and syy > 0 else 0.0


def wide():
    nwin = T // P
    rng = random.Random(31)
    cols, slips, unlocked = {}, {}, []
    for R in list(range(1 << 12)) + [r + (1 << 12) for r in range(1 << 12)]:
        c = column1(R, T)
        cols[R] = c
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        slips[R] = [1 if ROT.get(tuple(c[k * P:(k + 1) * P])) is None else 0 for k in range(nwin)]
        if last_bad >= T - P - 400 and R < (1 << 12):
            unlocked.append(R)
    ok0, same, firstdiff = True, 0, []
    for R in unlocked:
        c, s = cols[R], cols[R + (1 << 12)]
        d = next((t for t in range(T) if c[t] != s[t]), None)
        ok0 &= d is None or d >= 12
        if d is None:
            same += 1
        else:
            firstdiff.append(d)
    report("SB0 every sister pair has identical columns 1 for the first 12 steps", ok0)
    firstdiff.sort()
    med = firstdiff[len(firstdiff) // 2] if firstdiff else None
    print(f"   {len(unlocked)} unlocked halves; sisters identical over all {T} steps: {same} ({same / len(unlocked):.3f}); "
          f"median first differing time of the rest: {med}; quartiles {firstdiff[len(firstdiff) // 4]}, "
          f"{firstdiff[3 * len(firstdiff) // 4]}", flush=True)
    verdict("SB1 at least 20% of sister pairs identical throughout, and the median first difference above 200",
            same / len(unlocked) >= 0.2 and med is not None and med > 200)
    a, b = RANGES["late"]
    sis = [corr(slips[R][a:b], slips[R + (1 << 12)][a:b]) for R in unlocked
           if cols[R] != cols[R + (1 << 12)]]
    rnd = [corr(slips[R][a:b], slips[R2][a:b]) for R, R2 in
           ((rng.choice(unlocked), rng.choice(unlocked)) for _ in range(len(sis))) if R != R2]
    ms, mr = sum(sis) / len(sis), sum(rnd) / len(rnd)
    verdict("SB2 late-range slip correlation: sisters that differ >= 0.3 on average, random pairs < 0.05",
            ms >= 0.3 and mr < 0.05, f"sisters {ms:.3f} ({len(sis)} pairs), random {mr:.3f}")
    groups = {}
    for R in unlocked:
        groups.setdefault(R & 63, []).append(R)
    a2, b2 = 12, nwin
    series = {g: [sum(slips[R][k] for R in Rs) for k in range(a2, b2)] for g, Rs in groups.items()}
    keys = sorted(series)
    cross = [corr(series[g], series[h]) for i, g in enumerate(keys) for h in keys[i + 1:]]
    mc = sum(cross) / len(cross)
    within = []
    for g, Rs in groups.items():
        if len(Rs) < 8:
            continue
        N = [sum(slips[R][k] for R in Rs) for k in range(a, b)]
        n = b - a
        p = [sum(slips[R][a:b]) / n for R in Rs]
        within.append(fano(N) - (1 - sum(x * x for x in p) / sum(p)))
    mw = sum(within) / len(within)
    verdict("SB3 no common clock: mean cross-group correlation below 0.1; within groups the excess Fano >= 1",
            mc < 0.1 and mw >= 1, f"cross-group {mc:.3f} ({len(cross)} pairs of {len(keys)} groups); "
            f"within-group excess {mw:.2f}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def rows_right(R, n):
    """the right half's rows (column 0 clamped to 0101...) as integers, bit i = cell i, for n steps"""
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = R << 1, []
    for t in range(n):
        out.append(row)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return out


def dedup():
    nwin = T // P
    rng = random.Random(32)
    cols, slips, unlocked = {}, {}, []
    for R in range(1 << 12):
        c = column1(R, T)
        cols[R] = c
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad >= T - P - 400:
            unlocked.append(R)
            slips[R] = [1 if ROT.get(tuple(c[k * P:(k + 1) * P])) is None else 0 for k in range(nwin)]
    distinct = {}
    for R in unlocked:
        distinct.setdefault(tuple(cols[R]), R)
    reps = list(distinct.values())
    verdict("SC1 distinct columns 1 among the unlocked halves between 2,000 and 3,200", 2000 <= len(reps) <= 3200,
            f"{len(reps)} of {len(unlocked)}")
    a, b = RANGES["late"]
    f, indep, fc, _ = excess([slips[R] for R in reps], a, b, rng)
    verdict("SC2 after deduplication the late Fano factor is within 0.3 of its independence value",
            abs(f - indep) <= 0.3, f"Fano {f:.2f}, independence {indep:.2f}, shifted {fc:.2f}")
    near, pairs = 0, 0
    for R in unlocked:
        if cols[R] != column1(R + (1 << 12), T):
            continue
        pairs += 1
        x, y = rows_right(R, T)[-1], rows_right(R + (1 << 12), T)[-1]
        d = x ^ y
        leftmost = (d & -d).bit_length() - 1 if d else None
        near += leftmost is not None and leftmost >= 13 + T - 60
    verdict("SC3 for >= 90% of identical sister pairs the damage's leftmost cell is within 60 of the right edge",
            pairs > 0 and near / pairs >= 0.9, f"{near} of {pairs}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def long_run():
    pairs, same = [], 0
    for R in range(1 << 12):
        if len(pairs) >= 200:
            break
        c = column1(R, T)
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad >= T - P - 400 and c == column1(R + (1 << 12), T):
            pairs.append(R)
    for R in pairs:
        same += column1(R, 4 * T) == column1(R + (1 << 12), 4 * T)
    verdict("SC4 at least 95% of the first 200 identical sister pairs stay identical to 16,384 steps",
            same / len(pairs) >= 0.95, f"{same} of {len(pairs)}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if LONG:
        long_run()
        return
    if DEDUP:
        dedup()
        return
    if WIDE:
        wide()
        return
    nwin = T // P
    slips, kicks = [], []                                  # per half: slip indicator per window; kick per window
    odd = 0
    for R in range(1 << W):
        c = column1(R, T)
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad < T - P - 400:
            continue                                       # locked
        ph = [ROT.get(tuple(c[k * P:(k + 1) * P])) for k in range(nwin)]
        slips.append([1 if d is None else 0 for d in ph])
        ex = [(k, d) for k, d in enumerate(ph) if d is not None]
        kick = [0.0] * nwin
        for (k, d), (k2, d2) in zip(ex, ex[1:]):
            delta = (d2 - d) % P
            odd += delta % 2
            nn = (-17 * delta) % P
            nn = nn - P if nn > P // 2 else nn
            nn //= 2
            for j in range(k, k2):
                kick[j] += nn / (k2 - k)
        kicks.append(kick)
    H = len(slips)
    report("S0 every phase change between exact windows is an even time shift", odd == 0,
           f"{odd} odd shifts; {H} unlocked halves, {nwin} windows")
    rng = random.Random(30)
    F, Fc, spread, spreadc = {}, {}, {}, {}
    for name, (a, b) in RANGES.items():
        n = b - a
        N = [sum(s[k] for s in slips) for k in range(a, b)]
        F[name] = fano(N)
        v = [sum(kk[k] for kk in kicks) / H for k in range(a, b)]
        spread[name] = statistics.pstdev(v)
        fc, sc = [], []
        for _ in range(5):                                  # five shifted controls, averaged
            Nc, vc = [0] * n, [0.0] * n
            for s, kk in zip(slips, kicks):
                off = rng.randrange(n)
                for j in range(n):
                    Nc[j] += s[a + (j + off) % n]
                    vc[j] += kk[a + (j + off) % n] / H
            fc.append(fano(Nc)); sc.append(statistics.pstdev(vc))
        Fc[name] = statistics.fmean(fc); spreadc[name] = statistics.fmean(sc)
        print(f"   {name} (windows {a}-{b - 1}): slips per window {statistics.fmean(N):.1f} of {H}; Fano {F[name]:.2f} "
              f"(shifted {Fc[name]:.2f}); spread of v {spread[name]:.4f} (shifted {spreadc[name]:.4f})", flush=True)
    verdict("S1 Fano factor of the slip counts over the early range at least 3", F["early"] >= 3, f"{F['early']:.2f}")
    verdict("S2 Fano factor over the late range at most 1.5", F["late"] <= 1.5, f"{F['late']:.2f}")
    verdict("S3 the spread of v(k): at least twice the control's early, less than twice late",
            spread["early"] >= 2 * spreadc["early"] and spread["late"] < 2 * spreadc["late"],
            f"early ratio {spread['early'] / spreadc['early']:.2f}, late ratio {spread['late'] / spreadc['late']:.2f}")
    report("CF  the shifted control shows no synchrony: Fano in [0.8, 1.25] in every range",
           all(0.8 <= x <= 1.25 for x in Fc.values()), ", ".join(f"{k} {x:.2f}" for k, x in Fc.items()))
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
