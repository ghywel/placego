#!/usr/bin/env python3
"""rule30_lightning.py: the owner's lightning. Path-trace through the pyramid from the top down, many times, and see how
it forks and where it reaches the bottom.

RUN-ON:     cpu (pure Python 3, standard library; seeded)
COMMAND:    python3 tests/probes/lexicon/rule30_lightning.py [T=512] [WALKS=20000] | rule30_lightning.py local
COST:       about five minutes on one core. Writes rule30_lightning.png next to this script.

The owner (2026-10-05): "take a lightning trace on the pyramid: from the top down run some sort of path-tracing walk
that reaches the bottom of a given pyramid, and repeat this a large number of times, seeing how the lightning forks
and reaches the bottom each time."

Black cells conduct, white cells resist. A walker allowed only on black cells would rarely get far (on a random
pattern all three cells below are white one time in eight), so two versions are used, as real lightning has both:
  The strike: the path of least resistance. Moving down one row per step to one of the three cells below, crossing a
    white cell costs 1 and a black cell 0. The least cost from the apex to every cell is computed exactly by dynamic
    programming, and so is the least-cost path to the bottom.
  The flicker: WALKS random walks from the apex, each step choosing one of the three cells below with weight 1 if it
    is black and 0.1 if white. Where they land on the bottom row, and how many different cells they use, show the
    forking.
Pyramids of depth T: Rule 30 from a single 1; random pyramids with each interior cell black with Rule 30's own interior
density and both edges black (Rule 30's edges are always black); and Rule 90 from a single 1 (the Sierpinski
triangle, also with black edges).

PREDICTIONS, written 2026-10-05 before this script's first run:
  LG0 (controls): on an all-black pyramid the strike costs 0 everywhere, and the flicker is a plain random walk:
      arrivals with mean 0 (within 3 standard errors) and variance 2T/3 (within 5%).
  LG1 (blind): the strike finds Rule 30 like a random pattern: its least cost from the apex to the bottom row's centre,
      per row, is within 15% of the mean over 20 random pyramids.
  LG2 (blind): Rule 90 resists far more: its least cost to the bottom centre, per row, is more than 1.3 times Rule
      30's (its black cells thin out like (3/4)^n).
  LG3 (blind, uncertain): the flicker on Rule 30 is pulled to the left, by the regular diagonal stripes on that side of
      the pyramid: mean arrival below -0.1 standard deviations, while the random pyramids' mean arrivals stay within
      +-0.05 standard deviations on average.
REFUTED-BY: LG0 failing (the instrument); LG1, LG2 or LG3 failing.

OUTCOME of the first run, 2026-10-05 (T = 512, 20,000 walks): LG0 passed (mean -0.23, variance 340.4 against 340.7).
Rule 30's interior density 0.5017.
  The strike: least cost to the bottom centre, in white cells, Rule 30 3, random pyramids 2 to 7 (mean 4.5), Rule 90
      256. LG1 REFUTED, by its design: the costs are small integers, so a 15% band cannot hold them; Rule 30's 3 lies
      inside the random range. LG2 HELD (Rule 90 85 times as resistant). The strike to the centre rides the always-black
      right edge for about 100 rows, then cuts back through the interior.
  The flicker: Rule 30's walks land at a mean of -35.7 (sd 17.8, 126 distinct cells, 21.4% of steps through white);
      five random pyramids at -1.5 to +1.7 (sd about 18); Rule 90 at +0.15 (92.7% white steps). LG3 HELD: Rule 30's
      lightning is pulled left by 2.0 sd, the random pyramids' by +0.013 on average. But the stated cause (the
      left side's stripes) was not tested, and the figure shows the beam tilting at a steady rate from the very top,
      far from the stripes. A local cause is likely: below a black cell Rule 30 makes the lower-left and lower-middle
      cells black half the time each, but the lower-right only a quarter of the time.

ADDENDUM, written 2026-10-05 after the first run and before the second (python3 rule30_lightning.py local):
  LG4 (blind; the drift is local): a Markov lightning, which knows only Rule 30's parent-to-child rule (at each step the
      walker's cell keeps its colour, its four neighbours are fresh coin flips, and the three cells below follow from
      Rule 30), drifts by within 0.015 cells per step of Rule 30's own -35.7 / 511 = -0.070.
  LG5 (blind): on the real Rule 30 pyramid the drift is steady: the mean step over rows 1 to 170, 171 to 340 and 341
      to 511 differs between thirds by less than 30% of the overall mean step.
"""
import math, pathlib, random, struct, sys, zlib

HERE = pathlib.Path(__file__).resolve().parent
_nums = [a for a in sys.argv[1:] if a != "local"]
T = int(_nums[0]) if len(_nums) > 0 else 512
WALKS = int(_nums[1]) if len(_nums) > 1 else 20000
EPS = 0.1
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def pyramid(rule):
    """Rows 0..T-1; row t is a list over x = -T .. T (index x + T); 1 = black."""
    W = 2 * T + 1
    row = 1 << T                                        # bit x + T
    mask = (1 << (W + 2)) - 1
    rows = []
    for _ in range(T):
        rows.append([(row >> i) & 1 for i in range(W)])
        l, r = row << 1, row >> 1                       # bit i gets cell i - 1 (l) and i + 1 (r)
        row = ((l ^ (row | r)) if rule == 30 else (l ^ r)) & mask
    return rows


def random_pyramid(density, rng):
    W = 2 * T + 1
    rows = []
    for t in range(T):
        rows.append([1 if (abs(x - T) == t) else (1 if abs(x - T) < t and rng.random() < density else 0)
                     for x in range(W)])
    return rows


def strike(rows):
    """Least white-cost from the apex to every cell (moves to x - 1, x, x + 1), and the least-cost path to the centre."""
    W = 2 * T + 1
    INF = 10 ** 9
    cost = [INF] * W
    cost[T] = 0 if rows[0][T] else 1
    back = []
    for t in range(1, T):
        new, bk = [INF] * W, [0] * W
        for x in range(T - t, T + t + 1):
            best, arg = INF, 0
            for dx in (-1, 0, 1):
                y = x - dx
                if 0 <= y < W and cost[y] < best:
                    best, arg = cost[y], y
            new[x] = best + (0 if rows[t][x] else 1)
            bk[x] = arg
        back.append(bk)
        cost = new
    path, x = [T], T
    for t in range(T - 1, 0, -1):
        x = back[t - 1][x]
        path.append(x)
    return cost, path[::-1]


def flicker(rows, rng, n):
    W = 2 * T + 1
    land, used = [], [set() for _ in range(T)]
    density = [[0] * W for _ in range(T)]
    whites = steps = 0
    for _ in range(n):
        x = T
        for t in range(1, T):
            cand = [y for y in (x - 1, x, x + 1) if T - t <= y <= T + t]
            w = [1.0 if rows[t][y] else EPS for y in cand]
            r, acc = rng.random() * sum(w), 0.0
            for y, wy in zip(cand, w):
                acc += wy
                if r <= acc:
                    x = y
                    break
            whites += not rows[t][x]
            steps += 1
            density[t][x] += 1
            used[t].add(x)
        land.append(x - T)
    m = sum(land) / n
    sd = math.sqrt(sum((v - m) ** 2 for v in land) / n)
    return m, sd, whites / steps, len(set(land)), density


def png(path, pix, w, h):
    raw = b"".join(b"\x00" + bytes(pix[y * w * 3:(y + 1) * w * 3]) for y in range(h))
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)
    pathlib.Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                                   + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def main():
    rng = random.Random(1752)                           # Franklin's kite
    W = 2 * T + 1
    allblack = [[1 if abs(x - T) <= t else 0 for x in range(W)] for t in range(T)]
    c0, _ = strike(allblack)
    m0, sd0, wh0, _, _ = flicker(allblack, rng, 4000)
    ok0 = max(c0[T - (T - 1):T + T]) == 0 and abs(m0) <= 3 * sd0 / math.sqrt(4000) \
        and abs(sd0 ** 2 / (2 * (T - 1) / 3) - 1) <= 0.05 and wh0 == 0
    report("LG0 all-black pyramid: the strike costs 0, the flicker is a plain random walk (variance 2T/3)", ok0,
           f"mean {m0:.2f}, variance {sd0 ** 2:.1f} against {2 * (T - 1) / 3:.1f}")

    r30 = pyramid(30)
    inside = sum(r30[t][x] for t in range(T) for x in range(T - t + 1, T + t))
    cells = sum(max(0, 2 * t - 1) for t in range(T))
    dens = inside / cells
    c30, p30 = strike(r30)
    r90 = pyramid(90)
    c90, p90 = strike(r90)
    rnd = [random_pyramid(dens, rng) for _ in range(20)]
    crnd = [strike(rp)[0][T] for rp in rnd]
    per = lambda c: c / (T - 1)
    mean_rnd = sum(crnd) / len(crnd)
    print(f"   Rule 30 interior density {dens:.4f}; least cost to the bottom centre per row: Rule 30 {per(c30[T]):.4f}, "
          f"random {per(mean_rnd):.4f} (range {per(min(crnd)):.4f} to {per(max(crnd)):.4f}), Rule 90 {per(c90[T]):.4f}",
          flush=True)
    lo30 = min(c30[T - (T - 1):T + T])
    print(f"   Rule 30 cheapest bottom cell costs {lo30} (at x = {c30.index(lo30) - T}); the strike to the centre wanders to "
          f"x between {min(p30) - T} and {max(p30) - T}", flush=True)
    verdict("LG1 the strike finds Rule 30 like a random pattern (within 15% of random, per row)",
            abs(c30[T] / mean_rnd - 1) <= 0.15, f"ratio {c30[T] / mean_rnd:.3f}")
    verdict("LG2 Rule 90 resists more than 1.3 times Rule 30", c90[T] > 1.3 * c30[T], f"ratio {c90[T] / max(c30[T], 1):.3f}")

    m30, sd30, wh30, nd30, dens30 = flicker(r30, rng, WALKS)
    print(f"   flicker on Rule 30: mean arrival {m30:+.2f}, sd {sd30:.2f}, white steps {wh30:.3f}, {nd30} distinct bottom "
          f"cells", flush=True)
    mr = []
    for rp in rnd[:5]:
        m, sd, wh, nd, _ = flicker(rp, rng, WALKS // 4)
        mr.append(m / sd)
        print(f"   flicker on a random pyramid: mean arrival {m:+.2f}, sd {sd:.2f}, white steps {wh:.3f}, {nd} distinct "
              f"bottom cells", flush=True)
    m90, sd90, wh90, nd90, dens90 = flicker(r90, rng, WALKS // 4)
    print(f"   flicker on Rule 90: mean arrival {m90:+.2f}, sd {sd90:.2f}, white steps {wh90:.3f}, {nd90} distinct bottom "
          f"cells", flush=True)
    verdict("LG3 Rule 30's flicker is pulled left (below -0.1 sd), random pyramids' within +-0.05 sd on average",
            m30 / sd30 < -0.1 and abs(sum(mr) / len(mr)) <= 0.05,
            f"Rule 30 {m30 / sd30:+.3f} sd; random {sum(mr) / len(mr):+.3f} sd on average")

    # Figure: Rule 30's pyramid in grey, the flicker's path density in warm colours, the strike to the centre in cyan.
    S = 1
    w, h = W, T
    pix = [255] * (w * h * 3)
    mx = max(max(r) for r in dens30[1:]) or 1
    for t in range(T):
        for x in range(W):
            o = (t * w + x) * 3
            d = dens30[t][x]
            if d:
                f = math.log1p(d) / math.log1p(mx)
                pix[o:o + 3] = [255, int(230 * (1 - f)), int(60 * (1 - f))]
            elif r30[t][x]:
                pix[o:o + 3] = [150, 150, 150]
            elif abs(x - T) <= t:
                pix[o:o + 3] = [235, 235, 235]
    for t, x in enumerate(p30):
        o = (t * w + x) * 3
        pix[o:o + 3] = [0, 160, 220]
    png(HERE / "rule30_lightning.png", pix, w, h)
    print("   wrote rule30_lightning.png: Rule 30's pyramid (black cells grey), the 20,000 flicker paths' density (yellow"
          " to red, log scale), and the strike's least-resistance path to the bottom centre (blue)")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def local():
    rng = random.Random(1753)
    n = WALKS
    total = 0
    for _ in range(n):
        c = 1                                            # the apex is black
        for _t in range(1, T):
            l2, l1, r1, r2 = (rng.getrandbits(1) for _ in range(4))
            kids = {-1: l2 ^ (l1 | c), 0: l1 ^ (c | r1), 1: c ^ (r1 | r2)}
            w = {dx: (1.0 if v else EPS) for dx, v in kids.items()}
            r, acc = rng.random() * sum(w.values()), 0.0
            for dx in (-1, 0, 1):
                acc += w[dx]
                if r <= acc:
                    total += dx
                    c = kids[dx]
                    break
    markov = total / (n * (T - 1))
    real = -35.72 / 511
    verdict("LG4 the Markov lightning drifts within 0.015 cells per step of Rule 30's -0.070", abs(markov - real) <= 0.015,
            f"Markov {markov:+.4f} cells per step; Rule 30 {real:+.4f}")
    r30 = pyramid(30)
    W = 2 * T + 1
    thirds = [[0, 0], [0, 0], [0, 0]]
    for _ in range(WALKS // 2):
        x = T
        for t in range(1, T):
            cand = [y for y in (x - 1, x, x + 1) if T - t <= y <= T + t]
            w = [1.0 if r30[t][y] else EPS for y in cand]
            r, acc = rng.random() * sum(w), 0.0
            for y, wy in zip(cand, w):
                acc += wy
                if r <= acc:
                    k = min(2, (t - 1) * 3 // (T - 1))
                    thirds[k][0] += y - x
                    thirds[k][1] += 1
                    x = y
                    break
    rates = [a / b for a, b in thirds]
    overall = sum(a for a, _ in thirds) / sum(b for _, b in thirds)
    verdict("LG5 the drift is steady (thirds within 30% of the overall mean step)",
            max(rates) - min(rates) < 0.3 * abs(overall), ", ".join(f"{r:+.4f}" for r in rates) + f"; overall {overall:+.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")


if __name__ == "__main__":
    local() if sys.argv[1:2] == ["local"] else main()
