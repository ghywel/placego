#!/usr/bin/env python3
"""rule30_bottleneck.py: how fast does a right half's information reach column 1, next to column 0 = 0101...?

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_bottleneck.py
COST:       about five minutes on one core, 1.6 GB of memory at W = 24.

rule30_merge.py found that the 65,535 right halves of at most 16 cells give only 2^12.2 to 2^13.6 distinct visible
histories of column 1 by times 80 to 144 (RULE30-PRIZE.md section 8.16): most of their bits have not arrived.
bottleneck.c counts D(W, t), the distinct visible histories (column 1 at even times below t) over every right half
of at most W cells; I(W, t) = log2 D(W, t) is the information the left side can have received by time t. The ladder
gives an exact ceiling: a layer of width m fed any input can produce every visible prefix a real right half can, so
D(W, t) <= G(m, t + 1) for every W and m (G as in rule30_ladder_budget.py; G(16, 45) = 1,092, G(16, 61) = 4,711,
G(16, 77) = 17,613, G(16, 93) = 61,665).

PREDICTIONS, written 2026-10-05 before this script's first run:
  BN0 (controls): D(16, t) at t = 80, 96, 112, 128, 144 equals rule30_merge.py's counts (4,703, 6,493, 8,351, 10,314,
      12,352); D never decreases with t or with W; D(W, t) <= min(2^W - 1, 2^(t/2)); and the ladder's ceiling holds,
      D(W, t) <= G(16, t + 1) at t = 44, 60, 76, 92, for every W.
  BN1 (blind; the channel, not the seed, limits early delivery): at t = 64 the information delivered is the same for
      W = 20, 22 and 24 within 0.5 bits, and at most 9.6 bits (0.15 bits per step).
  BN2 (blind; the channel's rate): at W = 24, I grows by at most 0.30 bits per visible bit from t = 128 to t = 256
      (the ladder's start groups grow at 0.24 bits per visible bit at m = 16, an upper bound in the limit).
  BN3 (blind; delivery is slow and never quite complete): at t = 512, I(W, 512) lies between W - 3 and W - 0.5 for
      W = 16, 18, 20.
  BN4 (the random-chaos step: single flips in random right halves): 2,000 seeded random right halves of 40 cells, each
      with cell j flipped, j = 8, 16, 24, 32. A flip "arrives" at the first even time at which column 1 differs. The
      median arrival time grows with j at 1.5 to 3.5 steps per cell (information moves left at 0.3 to 0.65 cells per
      step; the walls of section 8.8 move at one half), and at least 5% of the flips at j = 32 have not arrived by
      t = 512.
REFUTED-BY: BN0 failing (the instrument); BN1 to BN4 failing.

OUTCOME of the first run, 2026-10-05 (about six minutes): BN0 passed (the merge counts reproduced exactly; monotone;
within the counting bound; and no right half of any width produced a visible prefix the width-16 layer cannot).
  I(W, t) in bits, for W = 16, 20, 24:  t = 44: 9.92, 10.03, 10.04 | t = 64: 11.52, 12.14, 12.30 |
      t = 128: 13.33, 15.16, 16.27 | t = 256: 14.64, 17.72, 19.96 | t = 512: 14.91, 18.88, 22.73.
  BN1 REFUTED: at t = 64 the delivered information is the same for W = 20, 22, 24 within 0.16 bits (that half held),
      but it is 12.1 to 12.3 bits, not at most 9.6. Early on, column 1 carries about 0.19 bits per step. At t = 44
      real right halves of 20 or more cells fill 2^10.04 = 1,052 of the 1,092 prefixes a width-16 layer can make.
  BN2 HELD as worded (0.058 bits per visible bit from t = 128 to 256 at W = 24), but it measured the wrong thing: by
      then the 24-bit seed, not the channel, limits delivery (19.96 of 24 bits delivered by t = 256).
  BN3 HELD: at t = 512, 1.09, 1.10 and 1.12 bits are still missing for W = 16, 18, 20.
  BN4 REFUTED: a single flip's median arrival is 18, 50, 92 and 128 steps from cells 8, 16, 24, 32, a slope of 4.65
      steps per cell: information moves left at about 0.21 cells per step, not 0.3 to 0.65. Flips never seen by
      t = 512: 0.2%, 1.2%, 2.8%, 3.9%, below the 5% predicted at j = 32.
"""
import math, pathlib, random, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
WS = [8, 10, 12, 14, 16, 18, 20, 22, 24]
CK = [16, 32, 44, 60, 64, 76, 80, 92, 96, 112, 128, 144, 192, 256, 384, 512]
MERGE = {80: 4703, 96: 6493, 112: 8351, 128: 10314, 144: 12352}
GCEIL = {44: 1092, 60: 4711, 76: 17613, 92: 61665}
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column1_visible(R, T):
    mask = (1 << (R.bit_length() + T + 3)) - 1
    row, vis = R << 1, []
    for t in range(T):
        if t % 2 == 0:
            vis.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return vis


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "bottleneck"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "bottleneck.c")], check=True)
    D = {}
    for W in WS:
        out = subprocess.run([str(exe), str(W), "512"] + [str(c) for c in CK], capture_output=True, text=True,
                             timeout=7200).stdout
        for w, t, d in re.findall(r"^I (\d+) (\d+) (\d+)$", out, re.M):
            D[(int(w), int(t))] = int(d)
        print(f"   W {W:2d}: " + " ".join(f"t{t}:{math.log2(D[(W, t)]):.2f}" for t in CK), flush=True)

    bad = [(t, D[(16, t)], v) for t, v in MERGE.items() if D[(16, t)] != v]
    mono = all(D[(W, a)] <= D[(W, b)] for W in WS for a, b in zip(CK, CK[1:])) and \
        all(D[(a, t)] <= D[(b, t)] for t in CK for a, b in zip(WS, WS[1:]))
    bound = all(D[(W, t)] <= min((1 << W) - 1, 1 << ((t + 1) // 2)) for W in WS for t in CK)
    ceil_bad = [(W, t, D[(W, t)], g) for t, g in GCEIL.items() for W in WS if D[(W, t)] > g]
    report("BN0 regression, monotone, counting bound, and the ladder's ceiling",
           not bad and mono and bound and not ceil_bad,
           f"regression differs {bad}; monotone {mono}; bound {bound}; ceiling broken {ceil_bad}")

    i64 = [math.log2(D[(W, 64)]) for W in (20, 22, 24)]
    verdict("BN1 at t = 64 the delivered information no longer depends on W (20, 22, 24 within 0.5 bits), <= 9.6",
            max(i64) - min(i64) <= 0.5 and max(i64) <= 9.6, ", ".join(f"{v:.2f}" for v in i64))
    rate = (math.log2(D[(24, 256)]) - math.log2(D[(24, 128)])) / 64
    verdict("BN2 at W = 24, I grows by at most 0.30 bits per visible bit from t = 128 to 256", rate <= 0.30,
            f"{rate:.3f} bits per visible bit")
    sat = {W: W - math.log2(D[(W, 512)]) for W in (16, 18, 20)}
    verdict("BN3 at t = 512 between 0.5 and 3 bits are still missing (W = 16, 18, 20)",
            all(0.5 <= v <= 3 for v in sat.values()), ", ".join(f"W {W}: {v:.2f} missing" for W, v in sat.items()))

    rng = random.Random(2026)
    T = 512
    arrivals = {j: [] for j in (8, 16, 24, 32)}
    for _ in range(2000):
        R = rng.getrandbits(40) | (1 << 39)
        base = column1_visible(R, T)
        for j in arrivals:
            other = column1_visible(R ^ (1 << (j - 1)), T)
            a = next((2 * i for i, (x, y) in enumerate(zip(base, other)) if x != y), None)
            arrivals[j].append(a)
    med, never = {}, {}
    for j, a in arrivals.items():
        seen = sorted(x for x in a if x is not None)
        never[j] = 1 - len(seen) / len(a)
        med[j] = seen[len(seen) // 2] if len(a) - len(seen) < len(a) / 2 else float("inf")
    js = sorted(med)
    xs, ys = js, [med[j] for j in js]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    verdict("BN4 median arrival grows at 1.5 to 3.5 steps per cell, and >= 5% of flips at j = 32 never arrive by 512",
            1.5 <= sl <= 3.5 and never[32] >= 0.05,
            f"slope {sl:.2f} steps per cell; medians " + ", ".join(f"j {j}: {med[j]}" for j in js)
            + "; not arrived " + ", ".join(f"j {j}: {never[j]:.1%}" for j in js))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
