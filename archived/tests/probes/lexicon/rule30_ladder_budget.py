#!/usr/bin/env python3
"""rule30_ladder_budget.py: does a zero run cost one bit per cell? The ladder's runs against the coin-flip null.

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_ladder_budget.py
COST:       about ten minutes on one core, and 2.5 GB of memory at its largest point (m = 5, s = 93).

The deep ladder (rule30_ladder_deep.py) refuted every "bounded" prediction: R(m, s) grows with the depth s at every
layer width m up to 12. Read after that run, the table follows one rule. For m >= 4 and s >= 33, R(m, s) is close
to log2 G(m, s), where G is the number of start groups (the visible column-1 prefixes the layer can produce before
depth s); the ratio lies between 0.81 and 1.26. With column 1 free (m = 0) the ratio is near 2.

The reading. Inside a zero run, Lemma 4 forces column 1's visible bits, so a run is a deterministic function of its
start group. It survives a cell when the left side's forced cell is 0 (the odd depths) and when the layer can supply
the demanded bit (the even depths). If both behave like fair coins, a run costs one bit per cell, and the best of G
starts lasts about log2 G cells: the adversary does no better than chance. With column 1 free the demanded bits cost
nothing, and a run costs half a bit per cell. This script tests that reading on points the deep run did not compute,
and through the histogram of all start groups' run lengths, not only the longest (ladder.c's hist mode).

PREDICTIONS, written 2026-10-05 before this script's first run. Fresh points: m = 0 at s = 37 and 45, and
m = 5, 7, 9, 11, 14, 16 at s = 45, 61, 77, 93; none of them was computed before (the cost probe that timed four of
them discarded their output).
  BL0 (control): the hist mode gives the same R and G as the run mode at six points of the deep run, and every
      histogram sums to G.
  C2  (control for the bands below): for the fresh points' own G, the longest of G simulated fair-coin runs (each
      cell survives with probability 1/2; seeded) lies within BL1's band, and with half a bit per cell, within BL2's.
  BL1 (blind; one bit per cell): at every fresh point with m >= 5, R / log2 G lies in [0.75, 1.35].
  BL2 (blind; half a bit per cell with column 1 free): R(0, s) / log2 G(0, s) lies in [1.5, 2.2] for s = 37, 45.
  BL3 (blind; the cost per cell, from the whole histogram): S(k) is the number of start groups whose run is at least
      k. A least-squares line through log2 S(k), for k = 1 up to the largest k with S(k) >= 20, falls by beta bits
      per cell, with beta in [0.8, 1.25] at every fresh point with m >= 5, and in [0.4, 0.6] at m = 0.
  BL4 (blind; the start groups' entropy): h_m = (log2 G(m, 93) - log2 G(m, 45)) / 24 bits per visible bit never rises
      with m over m = 5, 7, 9, 11, 14, 16 (to within 0.005), and h_16 lies in [0.15, 0.28]: it is still falling, but
      it has not vanished.
  BL5 (cross-instrument; real right halves): Z(W) is the longest zero run of the forced left half starting at a depth
      s in {41, 57, 73, 89, 105}, over every right half of at most W cells. Z(W) <= W + 3 for W = 8, 10, 12, 14, 16,
      and Z(16) >= Z(8) + 3: runs grow with the information the right half carries. (Z(12) = 10 is already known
      from rule30_ladder_deep.py's DL5, so W = 12 is not blind.)
REFUTED-BY: BL0 or C2 failing (the instrument, or bands that chance alone would break); BL1 to BL5 failing.

OUTCOME of the first run, 2026-10-05 (about eight minutes): BL0 passed. C2 FAILED: for the fresh points' own G, the
simulated fair-coin maximum left the band at 2 of 26 points (m = 7, s = 45: 0.747; m = 16, s = 45: 1.387). At G near
1,000 the best of G coins swings by about 2 cells, so BL1's band is too narrow there for chance alone; BL1's holding
is weaker evidence than it looks at the shallow points.
  BL1 HELD: R / log2 G lies between 0.775 and 1.280 at all 24 fresh points with m >= 5.
  BL2 HELD: 1.611 (s = 37) and 1.955 (s = 45) with column 1 free.
  BL3 REFUTED: the bulk of the histogram falls by 0.71 to 1.09 bits per cell for m >= 5 (m = 5 about 0.75 at every
      depth; 0.92 to 1.09 at m = 14 and 16), below the band at 9 of 24 points. At m = 0 it falls by 0.47 and 0.49, as
      predicted. So the longest run is shorter than the bulk's slope implies (log2 G / beta): the far tail is steeper
      than the bulk.
  BL4 HELD: h_m = 0.509, 0.378, 0.323, 0.297, 0.262, 0.242 for m = 5, 7, 9, 11, 14, 16: falling, not vanished.
  BL5 REFUTED: Z(W) = 9, 9, 10, 10, 11 for W = 8, 10, 12, 14, 16. The bound Z(W) <= W + 3 holds, but runs grow by only
      2 cells from W = 8 to 16. Real right halves do far worse than one bit per cell: their bits mostly do not reach
      column 1 where a run needs them.
  Seen in the m = 0 histograms (printed, not predicted): structured families far beyond the geometric tail. At s = 33,
  21 starts reach exactly 33 cells while none reach 25 to 31. At s = 45, 8 starts reach 43 while none reach 35 to 41.
"""
import math, pathlib, random, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
KNOWN = {(0, 33): (33, 65536), (1, 41): (15, 17711), (6, 57): (14, 17092), (8, 73): (16, 46788),
         (10, 89): (16, 153020), (12, 105): (20, 347219)}          # (R, G) from rule30_ladder_deep.py's first run
FRESH = [(0, 37), (0, 45)] + [(m, s) for m in (5, 7, 9, 11, 14, 16) for s in (45, 61, 77, 93)]
BAND1, BAND2 = (0.75, 1.35), (1.5, 2.2)
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def beta_fit(hist):
    """Bits lost per cell: the slope of log2 S(k) over k = 1 .. the largest k with S(k) >= 20."""
    S = [sum(hist[k:]) for k in range(len(hist))]
    ks = [k for k in range(1, len(S)) if S[k] >= 20]
    if len(ks) < 3:
        return float("nan")
    xs, ys = ks, [math.log2(S[k]) for k in ks]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return -sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def null_max(rng, G, bits_per_cell):
    """The longest of G runs in which each cell survives with probability 2^-bits_per_cell (inverse CDF)."""
    u, k = rng.random(), 0
    while (1 - 2.0 ** (-bits_per_cell * (k + 1))) ** G < u:
        k += 1
    return k


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "ladder"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "ladder.c")], check=True)

    def hist(m, s):
        out = subprocess.run([str(exe), "hist", str(m), str(s)], capture_output=True, text=True, timeout=7200).stdout
        h = {int(a): int(b) for a, b in re.findall(r"^H \d+ \d+ (\d+) (\d+)$", out, re.M)}
        line = re.search(r"^R M .*$", out, re.M).group(0)
        R, G = int(re.search(r"= (\d+)", line).group(1)), int(re.search(r"of (\d+) start", line).group(1))
        return R, G, "CAPPED" in line, [h.get(k, 0) for k in range(R + 1)], line

    bad = []
    for (m, s), (R0, G0) in KNOWN.items():
        R, G, _, h, _ = hist(m, s)
        if (R, G) != (R0, G0) or sum(h) != G:
            bad.append((m, s, R, G, sum(h)))
        if m == 0:
            print(f"   histogram m 0 s {s}: " + " ".join(f"{k}:{v}" for k, v in enumerate(h) if v), flush=True)
    report("BL0 the hist mode reproduces the deep run's R and G, and each histogram sums to G", not bad,
           f"differing: {bad}")

    res = {}
    for m, s in FRESH:
        R, G, cap, h, line = hist(m, s)
        res[(m, s)] = (R, G, cap, h)
        print(f"   {line}   beta {beta_fit(h):.3f}   R / log2 G {R / math.log2(G):.3f}", flush=True)
        if m == 0:
            print(f"   histogram m 0 s {s}: " + " ".join(f"{k}:{v}" for k, v in enumerate(h) if v), flush=True)

    rng = random.Random(1990)
    null_out = []
    for (m, s), (R, G, cap, h) in res.items():
        b = 0.5 if m == 0 else 1.0
        band = BAND2 if m == 0 else BAND1
        r = null_max(rng, G, b) / math.log2(G)
        if not band[0] <= r <= band[1]:
            null_out.append((m, s, round(r, 3)))
    report("C2 simulated fair-coin maxima for the same G stay inside the bands", not null_out,
           f"outside: {null_out}")

    capped = [(m, s) for (m, s), v in res.items() if v[2]]
    r1 = {(m, s): v[0] / math.log2(v[1]) for (m, s), v in res.items() if m >= 5}
    verdict("BL1 one bit per cell: R / log2 G in [0.75, 1.35] at every fresh point with m >= 5",
            all(BAND1[0] <= r <= BAND1[1] for r in r1.values()),
            f"range {min(r1.values()):.3f} to {max(r1.values()):.3f}; outside: "
            f"{[(k, round(r, 3)) for k, r in r1.items() if not BAND1[0] <= r <= BAND1[1]]}")
    r2 = {s: res[(0, s)][0] / math.log2(res[(0, s)][1]) for s in (37, 45)}
    verdict("BL2 half a bit per cell with column 1 free: R(0, s) / log2 G in [1.5, 2.2] at s = 37, 45",
            all(BAND2[0] <= r <= BAND2[1] for r in r2.values()), ", ".join(f"s {s}: {r:.3f}" for s, r in r2.items()))
    betas = {k: beta_fit(v[3]) for k, v in res.items()}
    ok3 = all((0.4 <= b <= 0.6) if k[0] == 0 else (0.8 <= b <= 1.25) for k, b in betas.items())
    verdict("BL3 beta in [0.8, 1.25] bits per cell for m >= 5, and in [0.4, 0.6] for m = 0", ok3,
            "; ".join(f"m {m} s {s}: {b:.3f}" for (m, s), b in betas.items()))
    hm = {m: (math.log2(res[(m, 93)][1]) - math.log2(res[(m, 45)][1])) / 24 for m in (5, 7, 9, 11, 14, 16)}
    ms = sorted(hm)
    ok4 = all(hm[b] <= hm[a] + 0.005 for a, b in zip(ms, ms[1:])) and 0.15 <= hm[16] <= 0.28
    verdict("BL4 h_m never rises with m, and h_16 in [0.15, 0.28]", ok4,
            ", ".join(f"h_{m} {hm[m]:.3f}" for m in ms))

    tau = [t % 2 for t in range(131)]
    depths = (41, 57, 73, 89, 105)
    Z = {}
    best = 0
    for R0 in range(1, 1 << 16):
        L = r30.forced_left(R0, tau, 130)
        for s in depths:
            n = 0
            while s - 1 + n < len(L) and L[s - 1 + n] == 0:
                n += 1
            best = max(best, n)
        if (R0 + 1) in {1 << W for W in (8, 10, 12, 14, 16)}:
            Z[(R0 + 1).bit_length() - 1] = best
    ok5 = all(Z[W] <= W + 3 for W in Z) and Z[16] >= Z[8] + 3
    verdict("BL5 real right halves: Z(W) <= W + 3, and Z(16) >= Z(8) + 3", ok5,
            ", ".join(f"Z({W}) = {Z[W]}" for W in sorted(Z)))
    print(f"   capped: {capped or 'none'}")
    print("\n   R(m, s) / log2 G and beta, rows m, columns s")
    for m in sorted({m for m, _ in res}):
        cells = [f"s {s}: R {res[(m, s)][0]} G {res[(m, s)][1]} ratio {res[(m, s)][0] / math.log2(res[(m, s)][1]):.2f}"
                 f" beta {betas[(m, s)]:.2f}" for s in sorted(s for mm, s in res if mm == m)]
        print(f"   m = {m:>2}: " + " | ".join(cells))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
