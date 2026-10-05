#!/usr/bin/env python3
"""rule30_lattice.py: the owner's graph of same-size triangles. The wheel's domain holds a lattice of white
triangles; is a kick a dislocation of that lattice, and can the kick be read from the triangles alone?

RUN-ON:     cpu (pure Python 3, standard library; seeded random right halves)
COMMAND:    python3 tests/probes/lexicon/rule30_lattice.py [N=800] [T=3000]
COST:       about five minutes on one core. Writes rule30_lattice.png next to this script.

rule30_triangles.py (PRIZE-PROBLEMS.md section 8.18) fixed the objects (every white triangle is exact, set by its
birth) and the kicks (departures of column 1 from the wheel U, absolute phase D). Its lattice test TK3 compared whole
56-step windows next to a kick and was spoiled by the walls themselves. Here the lattice is learned first and the
test uses only births clear of the wall.

The lattice. During exact windows (column 1 equal to U at phase D), a birth of a triangle of size n at column a and
time t sits at phase phi = (t - D) mod 56. Over all exact windows, the frequency of a site (phi, a, n) is the share
of windows in which that birth occurs. The lattice is the set of sites with frequency at least 0.5.
Chains, the owner's graph. Join a birth (t, a, n) to (t + 56, a, n) when both occur: same size, same column, one
period apart. A chain's length is its number of births.

PREDICTIONS, written 2026-10-05 before this script's first run:
  LT1 (blind; a rigid lattice next to column 0): in columns 2 to 4, at least 90% of the births in exact windows sit
      on lattice sites, and those sites have frequency at least 0.9.
  LT2 (blind; a kick is a dislocation): for kicks re-locked at a new phase D' != D, births in columns 2 to 4 at times
      t1 - 30 .. t1 - 8 (before the wall reaches column 4) lie on the lattice at the old phase D (at least 80% of
      them, pooled), births at t2 .. t2 + 24 (after re-locking) lie on it at the new phase D' (at least 80%), and the
      same post-kick births lie on it at the old phase D at least 0.3 less often.
  LT3 (blind; the kick read from triangles): for each such kick, the shift Delta in 0..55 that puts the most post-kick
      births on the lattice (read at phase D + Delta) equals D' - D (mod 56) in at least 80% of kicks.
  LT4 (blind; the lattice is firm at the wall of column 0 and soft further in): the mean chain length of births in
      exact stretches falls from column 2 to column 6.
REFUTED-BY: LT1 to LT4 failing. (The kick detector's control is rule30_triangles.py's KC, rerun here as KC.)
  (A smoke test at toy size, N = 6 and T = 600, ran after these predictions were written and before the commit; its
  output was seen and changed nothing here.)
"""
import pathlib, random, sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_triangles as tr                         # noqa: E402
sys.argv = _argv
P, U, ROT = tr.P, tr.U, tr.ROT
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def exact_windows(col1):
    """(start, absolute phase) of every 56-step window of column 1 equal to U at some phase, on a 56-step grid."""
    out = []
    for k in range(len(col1) // P):
        w = tuple(col1[k * P:(k + 1) * P])
        if w in ROT:
            out.append((k * P, (ROT[w] + k * P) % P))
    return out


def main():
    rng = random.Random(2027)
    data = []
    for _ in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, _w = tr.spacetime(R, T)
        col1 = [(r >> 1) & 1 for r in rows]
        data.append((rows, col1, tr.births(rows), tr.kicks(col1)))
    half = N // 2                                        # learn the lattice on the first half, test on the second
    freq, nwin = Counter(), 0
    for rows, col1, B, K in data[:half]:
        for start, D in exact_windows(col1):
            nwin += 1
            seen = {((t - D) % P, a, n) for t in range(start, start + P) for a, n in B.get(t, []) if a + n - 1 <= 8}
            freq.update(seen)
    lattice = {site for site, c in freq.items() if c / nwin >= 0.5}
    print(f"   lattice learned from {nwin} exact windows: {len(lattice)} sites; by column: "
          + ", ".join(f"{a}: {sum(1 for s in lattice if s[1] == a)}" for a in range(2, 9)), flush=True)

    classes = Counter()
    on = tot = 0
    hi_sites = True
    pre_on = pre_tot = post_on = post_tot = post_old = 0
    lt3_ok = lt3_n = 0
    chains = defaultdict(list)
    for rows, col1, B, K in data[half:]:
        for start, D in exact_windows(col1):
            for t in range(start, start + P):
                for a, n in B.get(t, []):
                    if 2 <= a and a + n - 1 <= 4:
                        tot += 1
                        site = ((t - D) % P, a, n)
                        if site in lattice:
                            on += 1
                            hi_sites &= freq[site] / nwin >= 0.9
        for (t1, D, cl, t2, D2) in K:
            if 300 <= t1 <= T - 80:
                classes[cl] += 1
            if not (300 <= t1 <= T - 80) or D2 == D:
                continue
            for t in range(t1 - 30, t1 - 7):
                for a, n in B.get(t, []):
                    if a + n - 1 <= 4:
                        pre_tot += 1
                        pre_on += ((t - D) % P, a, n) in lattice
            post = [(t, a, n) for t in range(t2, t2 + 25) for a, n in B.get(t, []) if a + n - 1 <= 4]
            for t, a, n in post:
                post_tot += 1
                post_on += ((t - D2) % P, a, n) in lattice
                post_old += ((t - D) % P, a, n) in lattice
            if post:
                score = [sum(((t - D - dl) % P, a, n) in lattice for t, a, n in post) for dl in range(P)]
                best = max(range(P), key=lambda dl: score[dl])
                lt3_n += 1
                lt3_ok += best == (D2 - D) % P
        # chains in exact stretches (consecutive exact windows on the grid, same phase)
        ex = dict(exact_windows(col1))
        for t, items in B.items():
            for a, n in items:
                if 2 <= a <= 6 and (t // P) * P in ex and (t // P - 1) * P not in ex or True:
                    pass
        births_set = {(t, a, n) for t, items in B.items() for a, n in items if 2 <= a <= 6}
        for (t, a, n) in births_set:
            k = (t // P) * P
            if k not in ex or (t - P, a, n) in births_set and (k - P) in ex:
                continue                                  # not the first of its chain inside an exact stretch
            length, u = 1, t
            while (u + P, a, n) in births_set and ((u + P) // P) * P in ex:
                length += 1
                u += P
            chains[a].append(length)
    tot_cl = sum(classes.values())
    report("KC the detector: at least 90% of departures in classes 32 and 52",
           tot_cl > 0 and (classes[32] + classes[52]) / tot_cl >= 0.9, f"{classes[32] + classes[52]} of {tot_cl}")
    verdict("LT1 a rigid lattice in columns 2-4 (>= 90% of births on sites of frequency >= 0.9)",
            tot > 0 and on / tot >= 0.9 and hi_sites, f"{on} of {tot} on the lattice ({on / max(tot, 1):.1%}); "
            f"all those sites at frequency >= 0.9: {hi_sites}")
    verdict("LT2 a kick is a dislocation (old phase before >= 80%, new phase after >= 80%, old phase after 0.3 lower)",
            pre_tot and post_tot and pre_on / pre_tot >= 0.8 and post_on / post_tot >= 0.8
            and post_on / post_tot - post_old / post_tot >= 0.3,
            f"before at D {pre_on / max(pre_tot, 1):.1%} of {pre_tot}; after at D' {post_on / max(post_tot, 1):.1%}, "
            f"at D {post_old / max(post_tot, 1):.1%} of {post_tot}")
    verdict("LT3 the kick read from triangles equals D' - D in at least 80% of kicks", lt3_n and lt3_ok / lt3_n >= 0.8,
            f"{lt3_ok} of {lt3_n} ({lt3_ok / max(lt3_n, 1):.1%})")
    means = {a: sum(v) / len(v) for a, v in chains.items() if v}
    cols = sorted(means)
    verdict("LT4 mean chain length falls from column 2 to column 6", means.get(2, 0) > means.get(6, 0)
            and all(means[b] <= means[a] * 1.05 for a, b in zip(cols, cols[1:])),
            ", ".join(f"column {a}: {means[a]:.2f} ({len(chains[a])} chains)" for a in cols))

    # Figure: left, the lattice in the wheel's frame (56 phases down, columns 1..16 across): each cell is coloured by
    # the commonest size of triangle covering it in exact windows, faded by how often it is covered. Right, an example
    # space-time around a kick (columns 0..60), triangles coloured by size, the departure and re-locking marked in red.
    cover = defaultdict(Counter)
    for rows, col1, B, K in data[:half]:
        for start, D in exact_windows(col1):
            for t in range(start, start + P):
                for a, n in B.get(t, []):
                    if a > 16:
                        continue
                    for h in range((n + 1) // 2):
                        for j in range(a + h, min(a + n - h, 17)):
                            cover[((t + h - D) % P, j)][min(n, 8)] += 1
    def colour(n):
        return {2: (250, 200, 60), 3: (240, 140, 40)}.get(n, (90, 150, 240) if n <= 6 else (40, 80, 200))
    left = []
    for phi in range(P):
        line = []
        for c in range(17):
            cnt = cover.get((phi, c))
            if not cnt:
                line.append((250, 250, 250))
                continue
            n, v = cnt.most_common(1)[0]
            f = min(1.0, sum(cnt.values()) / nwin)
            r, g, b = colour(n)
            line.append((int(250 - (250 - r) * f), int(250 - (250 - g) * f), int(250 - (250 - b) * f)))
        left.append(line)
    right = []
    for rows, col1, B, K in data[half:]:
        good = [k for k in K if 400 <= k[0] <= T - 200 and k[3] - k[0] < 120 and k[4] != k[1]]
        if not good:
            continue
        t1, D, cl, t2, D2 = good[0]
        lo, hi = t1 - 112, t2 + 112
        inside = {}
        for t in range(lo - 40, hi):
            for a, n in B.get(t, []):
                for h in range((n + 1) // 2):
                    for j in range(a + h, a + n - h):
                        inside[(t + h, j)] = n
        for t in range(lo, hi):
            line = []
            for c in range(61):
                if c <= 1 and t in (t1, t2):
                    line.append((230, 20, 20))
                elif (rows[t] >> c) & 1:
                    line.append((30, 30, 30))
                elif (t, c) in inside:
                    line.append(colour(min(inside[(t, c)], 8)))
                else:
                    line.append((250, 250, 250))
            right.append(line)
        break
    S = 4
    w = (17 + 3 + 61) * S
    h = max(len(left), len(right)) * S
    pix = [255] * (w * h * 3)
    def put(x0, block):
        for y, line in enumerate(block):
            for x, rgb in enumerate(line):
                for dy in range(S):
                    for dx in range(S):
                        o = ((y * S + dy) * w + (x0 + x) * S + dx) * 3
                        pix[o:o + 3] = list(rgb)
    put(0, left)
    put(20, right)
    tr.png(HERE / "rule30_lattice.png", pix, w, h)
    print("   wrote rule30_lattice.png: left, the lattice of triangles in the wheel's frame (56 phases down, columns 0..16"
          " across; yellow size 2, orange 3, blue 4-6, dark blue 7+; faded where rare); right, a space-time around a"
          " kick (columns 0..60; red marks at the departure and at re-locking)")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
