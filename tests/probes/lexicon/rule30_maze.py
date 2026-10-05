#!/usr/bin/env python3
"""rule30_maze.py: the owner's maze. From a random cell, with no map, what is the most efficient way back to the apex?

RUN-ON:     cpu (pure Python 3, standard library; seeded)
COMMAND:    python3 tests/probes/lexicon/rule30_maze.py [T=2048] [STARTS=2000]
COST:       about two minutes on one core.

The owner (2026-10-05): "Given some random initial starting position in the pyramid, and without knowledge about the
structure the walker is in, what is the most efficient way to trace a path to the origin single point, as if the
structure were a maze?"

The maze. Black cells are corridors and white cells are walls. A walker at (t, x) may move up to one of its three
parents (t-1, x-1), (t-1, x), (t-1, x+1), the lightning's moves reversed. It sees nothing until it looks at a cell, one
look per cell. Every move climbs one row, so no route from row t is shorter than t moves.

Proved here, for any rule that keeps white-white-white white (Rule 30 does), grown from a single black cell:
  P1. Every black cell below the apex has a black parent, since three white parents would make it white.
  P2. So a walker on black can always climb onto black. Cells outside the pyramid are white, so it never leaves the
      pyramid, and row 0's only black cell is the apex: EVERY climb on black reaches the apex in exactly t moves, the
      shortest possible, with no map, no memory and no backtracking. The maze has no dead ends going up.
  P3. Looks: look at one parent; if it is black, climb. Otherwise look at a second; if it is black, climb. Otherwise the
      third is black by P1, so climb without looking. At most two looks per row.
For Rule 30, c' = l XOR (c OR r), the parents of a black cell are 100, 011, 010 or 001 (left, middle, right). If these
four were equally likely (the coin model), looking at the middle or the right parent first would cost 1.5 looks per
row on average, and the left first 1.75. A walker that does not know P1 must look at the third parent too: 1.75 with
the middle first.
Going down, the maze is different. A black cell's children are all white exactly when the cells two and one to its left
are black and one of the two to its right is black (from the rule): 3/16 of the time in the coin model. So a downward
walker without a map meets dead ends, although by P1 every black cell can be reached from the apex. Lightning works
this way: the stepped leader branches downwards and most branches die; the return stroke climbs the one channel that
connected.
A random pyramid (independent cells, black edges) has no P1: a black cell whose three parents are white is a dead
end, and whether a black cell connects to the apex at all is directed site percolation, with three parents per site.
No published threshold for this lattice was found (a search, 2026-10-05); the square lattice with two parents has
0.7055.

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run):
  MZ0 (controls, exact): on Rule 30 to depth T every black cell connects upwards to the apex (P1), and STARTS climbs
      from random black cells all reach it in exactly t moves, for each strategy; on a random pyramid the connected set
      computed row by row agrees with a depth-first search from 200 random black cells.
  MZ1 (blind; the coin model): on Rule 30 the parent patterns 100, 011, 010, 001 of black cells each have share
      0.25 +- 0.01, and the climbing walkers use 1.5 +- 0.05 looks per row looking middle first, 1.5 +- 0.05 right
      first, 1.75 +- 0.05 left first, and 1.75 +- 0.05 middle, left, right without P1.
  MZ2 (blind; the arrow of time): going down, the share of Rule 30's black cells with no black child is 3/16 +- 0.01.
  MZ3 (counterfactual, blind): a random pyramid with Rule 30's interior density is a real maze. Fewer than half of its
      interior black cells at depth T connect to the apex; a climber without backtracking (middle, left, right) gets
      stuck before the apex from more than 90% of the connected starts; a depth-first search with marks (Tremaux)
      always gets there from a connected start (within 200 reads per row, a cap set to bound the run), but reads more
      than 2 cells per row on the median.
  MZ4 (blind; the threshold): on random pyramids the share of interior black cells at depth T that connect to the
      apex is below 1% at density 0.35 and above 20% at density 0.60.
  MZ5 (the chaos step, blind): flipping 1% of Rule 30's interior cells at random makes dead ends (P1 fails), but most
      of the maze stays connected: between 50% and 99.9% of the interior black cells at depth T still connect.
REFUTED-BY: MZ0 failing (the instrument or the proof); MZ1 to MZ5 failing.
"""
import random, sys

T = int(sys.argv[1]) if len(sys.argv) > 1 else 2048
STARTS = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def bit(row, x):
    return (row >> (x + T)) & 1                        # bit x + T holds cell x


def rule30_rows():
    rows, row, mask = [], 1 << T, (1 << (2 * T + 1)) - 1
    for _ in range(T):
        rows.append(row)
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    return rows


def bernoulli_word(p, nbits, rng, k=16):
    """nbits independent bits, each 1 with probability p rounded to k binary digits."""
    q = round(p * (1 << k))
    x = 0
    for j in range(k):                                 # from the least significant digit of q up
        r = rng.getrandbits(nbits)
        x = (x | r) if (q >> j) & 1 else (x & r)
    return x


def random_rows(p, rng):
    rows = []
    for t in range(T):
        cone = ((1 << (2 * t + 1)) - 1) << (T - t)     # cells -t .. t
        edges = (1 << (T - t)) | (1 << (T + t))
        rows.append((bernoulli_word(p, 2 * T + 1, rng) & cone) | edges)
    return rows


def flipped(rows, share, rng):
    out = [rows[0], rows[1]]
    for t in range(2, T):
        interior = ((1 << (2 * t - 1)) - 1) << (T - t + 1)   # cells -t+1 .. t-1
        out.append(rows[t] ^ (bernoulli_word(share, 2 * T + 1, rng) & interior))
    return out


def connected(rows):
    conn = [rows[0] & (1 << T)]
    for t in range(1, T):
        c = conn[-1]
        conn.append(rows[t] & (c | (c << 1) | (c >> 1)))
    return conn


def interior_share(rows, conn, t):
    interior = ((1 << (2 * t - 1)) - 1) << (T - t + 1)
    b = bin(rows[t] & interior).count("1")
    return bin(conn[t] & interior).count("1") / b if b else float("nan")


def random_black(rows, rng, t):
    while True:
        x = rng.randrange(-t + 1, t)
        if bit(rows[t], x):
            return x


def climb(rows, t, x, order, use_p1):
    """Climb without backtracking. order lists the parent offsets to look at. Returns (looks, moves, reached apex)."""
    looks = moves = 0
    while t > 0:
        for k, dx in enumerate(order):
            if use_p1 and k == len(order) - 1:
                ok = True                              # by P1 the last parent is black: climb without looking
            else:
                looks += 1
                ok = bit(rows[t - 1], x + dx)
            if ok:
                t, x, moves = t - 1, x + dx, moves + 1
                break
        else:
            return looks, moves, False
    return looks, moves, x == 0


def dfs(rows, t0, x0, cap=None):
    """Depth-first search upwards with marks (each cell read at most once), giving up after cap reads. Returns
    (cells read, reached apex)."""
    seen = {(t0, x0)}
    stack, reads = [(t0, x0)], 0
    while stack and (cap is None or reads < cap):
        t, x = stack.pop()
        if t == 0:
            return reads, x == 0
        for dx in (1, -1, 0):                          # pushed so that the middle is tried first, then left, right
            c = (t - 1, x + dx)
            if c not in seen:
                seen.add(c)
                reads += 1
                if bit(rows[t - 1], x + dx):
                    stack.append(c)
    return reads, False


def main():
    rng = random.Random(1735)                          # the year the bridges of Konigsberg problem was settled
    r30 = rule30_rows()
    c30 = connected(r30)
    allconn = all(c30[t] == r30[t] for t in range(T))
    starts = []
    for _ in range(STARTS):
        t = rng.randrange(T // 2, T)
        starts.append((t, random_black(r30, rng, t)))
    strategies = [("middle, left, then right unseen (P1)", (0, -1, 1), True),
                  ("right, middle, then left unseen (P1)", (1, 0, -1), True),
                  ("left, middle, then right unseen (P1)", (-1, 0, 1), True),
                  ("middle, left, right, all looked at (no P1)", (0, -1, 1), False)]
    perrow, exact = {}, True
    for name, order, p1 in strategies:
        L = M = 0
        for t, x in starts:
            looks, moves, ok = climb(r30, t, x, order, p1)
            exact &= ok and moves == t
            L += looks
            M += moves
        perrow[name] = L / M
    # the random-pyramid control for the connected set
    density = sum(bin(r30[t]).count("1") - 2 for t in range(2, T)) / sum(2 * t - 1 for t in range(2, T))
    rp = random_rows(density, rng)
    cp = connected(rp)
    agree = 0
    for _ in range(200):
        t = rng.randrange(T // 8, T // 4)              # shallower, to keep the searches short
        x = random_black(rp, rng, t)
        agree += dfs(rp, t, x)[1] == bool(bit(cp[t], x))
    report("MZ0 Rule 30: every black cell connects to the apex, and every climb reaches it in exactly t moves; random "
           "pyramid: row-by-row connectivity agrees with depth-first search", allconn and exact and agree == 200,
           f"all connected {allconn}; climbs exact {exact}; agreement {agree} of 200")

    pat = {p: 0 for p in ("100", "011", "010", "001", "other")}
    dead = blacks = 0
    for t in range(2, T - 1):                          # whole rows at once: bit x + T of each word is about cell x
        b = r30[t] & (((1 << (2 * t - 1)) - 1) << (T - t + 1))
        up, down = r30[t - 1], r30[t + 1]
        L, M, R = up << 1, up, up >> 1                 # the parents at x - 1, x, x + 1, aligned with x
        blacks += bin(b).count("1")
        for key, word in (("100", L & ~M & ~R), ("011", ~L & M & R), ("010", ~L & M & ~R), ("001", ~L & ~M & R)):
            pat[key] += bin(b & word).count("1")
        dead += bin(b & ~((down << 1) | down | (down >> 1))).count("1")
    pat["other"] = blacks - sum(pat.values())
    shares = {k: v / blacks for k, v in pat.items()}
    print("   Rule 30's black cells, parent patterns (left, middle, right): "
          + ", ".join(f"{k} {v:.4f}" for k, v in shares.items()), flush=True)
    for name, v in perrow.items():
        print(f"   looks per row, {name}: {v:.4f}", flush=True)
    names = [s[0] for s in strategies]
    want = [1.5, 1.5, 1.75, 1.75]
    ok1 = all(abs(shares[k] - 0.25) <= 0.01 for k in ("100", "011", "010", "001")) and \
        all(abs(perrow[n] - w) <= 0.05 for n, w in zip(names, want))
    verdict("MZ1 the coin model: parent patterns 0.25 each; 1.5, 1.5, 1.75, 1.75 looks per row", ok1)
    verdict("MZ2 going down, 3/16 of Rule 30's black cells are dead ends", abs(dead / blacks - 3 / 16) <= 0.01,
            f"{dead / blacks:.4f}")

    sh = interior_share(rp, cp, T - 1)
    stuck = capped = n = 0
    meds = []
    tries = 0
    while n < 200 and tries < 100000:
        tries += 1
        t = rng.randrange(T // 2, T)
        x = random_black(rp, rng, t)
        if not bit(cp[t], x):
            continue
        n += 1
        stuck += not climb(rp, t, x, (0, -1, 1), False)[2]
        r, ok = dfs(rp, t, x, cap=200 * t)
        capped += not ok
        meds.append(r / t)
    meds.sort()
    med = meds[len(meds) // 2] if meds else float("nan")
    print(f"   random pyramid (density {density:.4f}): {sh:.4f} of interior black cells at depth {T} connect; climbs "
          f"without backtracking stuck from {stuck} of {n} connected starts; depth-first search reads {med:.2f} cells "
          f"per row on the median, and gave up (at 200 reads per row) on {capped}", flush=True)
    verdict("MZ3 a random pyramid is a real maze: under half connect, over 90% of climbs stuck, search always succeeds "
            "but reads over 2 per row", sh < 0.5 and n > 0 and stuck > 0.9 * n and capped == 0 and med > 2,
            f"{sh:.4f}, {stuck} of {n}, gave up {capped}, {med:.2f}")

    sweep = {}
    for p in (0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65):
        rows = random_rows(p, rng)
        sweep[p] = interior_share(rows, connected(rows), T - 1)
    print("   share of interior black cells at depth T connected to the apex, by density: "
          + ", ".join(f"{p:.2f}: {v:.4f}" for p, v in sweep.items()), flush=True)
    verdict("MZ4 the threshold: below 1% at density 0.35, above 20% at 0.60", sweep[0.35] < 0.01 and sweep[0.60] > 0.2,
            f"{sweep[0.35]:.4f}, {sweep[0.60]:.4f}")

    pf = flipped(r30, 0.01, rng)
    cf = connected(pf)
    shf = interior_share(pf, cf, T - 1)
    verdict("MZ5 the chaos step: 1% flips leave between 50% and 99.9% of the interior black cells connected",
            0.5 <= shf <= 0.999, f"{shf:.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
