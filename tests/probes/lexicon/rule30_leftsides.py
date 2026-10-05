#!/usr/bin/env python3
"""rule30_leftsides.py: Rowland's question. Does Rule 30 have one left side, or several, depending on the seed?

RUN-ON:     cpu (pure Python 3, standard library; exact, with certificates)
COMMAND:    python3 tests/probes/lexicon/rule30_leftsides.py [LOGT=18] [K=160000] [SEEDS=40]
COST:       about three minutes on one core.

The question (Rowland, "Local nested structure in rule 30", Complex Systems 16, section 5; PRIOR-ART.md). Read from a
finite seed's left edge, every left diagonal E_e(t) = c(t, e - t) is eventually periodic. Is its eventual period
independent of the seed, so that there is "really only one left side of rule 30"? Rowland expects not. A period
doubles exactly when diagonal e - 1 is eventually white and diagonal e - 2 has an odd number of black cells per
period (his Proposition 2, Wolfram's observation). When the number is even, diagonal e has two possible eventual
periods, complements of each other, and the seed decides which. Rowland finds the first such place at his column
53209 (column 53208 eventually white, column 53207 of period 16), with further splits at his columns 58288 and 72577,
and surmises infinitely many left sides, "if in fact they do occur for some initial conditions". His column m is our
diagonal e = m - 1 (his column 1 is the black left edge, our E_0); LS0 checks this.

The method. Rule 30 is c' = l XOR (c OR r). Along the left diagonals, E_e(t) = E_(e-2)(t-1) XOR (E_(e-1)(t-1) OR
E_e(t-1)): each diagonal depends only on itself and the two nearer the edge. So the strip of diagonals 0 .. K-1 is a
closed system. Held as a K-bit integer V (bit e = E_e(t)), it evolves by V' = ((V << 2) XOR ((V << 1) OR V)) mod 2^K,
starting from the seed's cells, with no need to compute the rest of the pattern. The map is deterministic and the
strip is finite, so a single equality V_t = V_(t+P) proves that the strip is periodic with period dividing P for ever
after: a certificate. The strip of the first k diagonals is closed too, so each width has its own eventual cycle. Two
seeds have the same left side to width k exactly when their certified cycles at width k are the same set of strips
(the same cycle, perhaps at a different phase).

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run):
  LS0 (controls): (a) the strip map equals a direct Rule 30 simulation's left part, cell for cell, for 2,048 steps,
      for the single seed and two random seeds; (b) every seed's strip of width K is certified periodic within 2^LOGT
      steps; (c) for the single seed, diagonals 0 to 63 have the periods rule30_leftband.py recorded, and the
      eventually white diagonals below 2,048 are 2, 7, 28 and 399; (d) diagonal 53207 is eventually white and diagonal
      53206 has period 16 with an even number of black cells per period, so the first place two left sides can split is
      diagonal 53208, Rowland's column 53209.
  LS1 (blind): up to diagonal 53207 all SEEDS + 1 seeds (the single 1 and SEEDS random seeds) share one left side.
  LS2 (blind; Rowland's open question): at diagonal 53208 both continuations occur, each for at least 5 of the seeds.
      Finite seeds realise at least two left sides of Rule 30.
  LS3 (blind): the left sides keep splitting: at least 3 distinct left sides by diagonal 75,000, and at least 4 by
      diagonal K - 1.
REFUTED-BY: LS0 failing (the instrument); LS1, LS2 or LS3 failing.
"""
import random, sys

LOGT = int(sys.argv[1]) if len(sys.argv) > 1 else 18
K = int(sys.argv[2]) if len(sys.argv) > 2 else 160000
SEEDS = int(sys.argv[3]) if len(sys.argv) > 3 else 40
T = 1 << LOGT
KEEP = 1024                                            # the last KEEP strips are kept for the certificate
FAILS = 0
# rule30_leftband.py's single-seed periods for diagonals 0 .. 63 (from rule30_diagonals.py's recorded run)
DG_PERIODS = [1, 1, 1, 2, 1, 2, 2, 1, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 1, 8, 1, 8, 8, 8,
              8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def seed_int(cells):
    """cells[0] is the leftmost (black) cell; bit e of the result is E_e(0) = cell e."""
    return sum(b << e for e, b in enumerate(cells))


def strip_run(V, width, steps, keep=0):
    mask = (1 << width) - 1
    tail = []
    for t in range(steps):
        if t >= steps - keep:
            tail.append(V)
        V = ((V << 2) ^ ((V << 1) | V)) & mask
    return tail


def direct(cells, steps, width):
    """Direct Rule 30 from the seed (leftmost cell at x = 0); returns each step's strip of `width` left diagonals."""
    off = steps + 2
    row = sum(b << (off + x) for x, b in enumerate(cells))
    mask = (1 << (off + len(cells) + steps + 3)) - 1
    out = []
    for t in range(steps):
        out.append((row >> (off - t)) & ((1 << width) - 1))
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    return out


def certify(tail):
    """Smallest power of 2 P with tail[-1] == tail[-1 - P]: the strip is periodic from there on. Returns the cycle (in
    time order) or None."""
    P = 1
    while P < len(tail):
        if tail[-1] == tail[-1 - P]:
            return tail[-P:]
        P *= 2
    return None


def diag_seq(cycle, e):
    return [(v >> e) & 1 for v in cycle]


def period(seq):
    p = 1
    while p < len(seq) and any(seq[i] != seq[(i + p) % len(seq)] for i in range(len(seq))):
        p *= 2
    return p


def side(cycle, k):
    """The left side to width k (diagonals 0 .. k - 1): the cycle as a set of masked strips."""
    m = (1 << k) - 1
    return frozenset(v & m for v in cycle)


def main():
    rng = random.Random(2006)                          # the year of Rowland's paper
    seeds = [[1]]
    for _ in range(SEEDS):
        w = rng.randrange(1, 65)
        cells = [1] + [rng.getrandbits(1) for _ in range(w - 1)]
        while cells[-1] == 0:
            cells.pop()
        seeds.append(cells)
    # LS0 (a)
    ok_a = True
    for cells in seeds[:3]:
        d = direct(cells, 2048, 2048)
        V, mask = seed_int(cells), (1 << 2048) - 1
        for t in range(2048):
            ok_a &= V == d[t]
            V = ((V << 2) ^ ((V << 1) | V)) & mask
    cycles = []
    for n, cells in enumerate(seeds):
        cyc = certify(strip_run(seed_int(cells), K, T, KEEP))
        cycles.append(cyc)
        if n < 3 or n % 10 == 0:
            print(f"   seed {n} ({len(cells)} cells): certified cycle length {len(cyc) if cyc else None}", flush=True)
    ok_b = all(c is not None for c in cycles)
    one = cycles[0]
    per = [period(diag_seq(one, e)) for e in range(64)] if one else []
    union = 0
    for v in one or []:
        union |= v
    white = [e for e in range(K) if not (union >> e) & 1]
    ok_c = per == DG_PERIODS and [e for e in white if e < 2048] == [2, 7, 28, 399]
    branch = []                                        # eventually white diagonals with an even predecessor
    info = []
    for z in white:
        if z == 0 or z + 1 >= K:
            continue
        s = diag_seq(one, z - 1)
        p = period(s)
        blacks = sum(s[:p])
        info.append((z, p, blacks))
        if blacks % 2 == 0:
            branch.append(z + 1)
    p53206 = period(diag_seq(one, 53206)) if one and K > 53208 else None
    b53206 = sum(diag_seq(one, 53206)[:p53206]) if p53206 else None
    ok_d = 53207 in white and p53206 == 16 and b53206 is not None and b53206 % 2 == 0 and branch[:1] == [53208]
    report("LS0 controls: (a) strip map = direct Rule 30; (b) all strips certified; (c) the single seed's periods and "
           "white diagonals; (d) Rowland's first split at diagonal 53208", ok_a and ok_b and ok_c and ok_d,
           f"(a) {ok_a}; (b) {ok_b}; (c) {ok_c}; (d) {ok_d}: diagonal 53206 period {p53206}, {b53206} black per period")
    print("   eventually white diagonals of the single seed, with the period and black count of the one before: "
          + ", ".join(f"{z} ({p}, {b})" for z, p, b in info), flush=True)
    print(f"   branch points (diagonals that can split) below {K}: {branch}", flush=True)
    print(f"   the single seed's period at diagonal {K - 1}: {period(diag_seq(one, K - 1))}", flush=True)
    if not ok_b:
        print("\n1 OR MORE FAILURE(S)")
        sys.exit(1)

    def classes(k):
        groups = {}
        for n, c in enumerate(cycles):
            groups.setdefault(side(c, k), []).append(n)
        return sorted(groups.values(), key=lambda g: g[0])
    def branches(cyc):
        u = 0
        for v in cyc:
            u |= v
        out = []
        for z in range(1, K - 1):
            if not (u >> z) & 1:
                s = diag_seq(cyc, z - 1)
                if sum(s[:period(s)]) % 2 == 0:
                    out.append(z + 1)
        return out
    final = classes(K)
    allb = set(branch)
    for grp in final:
        b = branches(cycles[grp[0]])
        allb |= set(b)
        print(f"   left side of {len(grp)} seed(s) (first seed {grp[0]}): branch points {b}; period at diagonal "
              f"{K - 1}: {period(diag_seq(cycles[grp[0]], K - 1))}", flush=True)
    widths = sorted({53207, 53208, 53209, 75000, K} | {b + 1 for b in allb})
    counts = {}
    for k in widths:
        g = classes(k)
        counts[k] = g
        print(f"   width {k} (diagonals 0 to {k - 1}): {len(g)} left side(s); sizes {[len(x) for x in g]}; the single "
              f"seed in the side of size {len(next(x for x in g if 0 in x))}", flush=True)
    verdict("LS1 up to diagonal 53207 every seed has the same left side", len(counts[53208]) == 1,
            f"{len(counts[53208])} side(s)")
    g = counts[53209]
    verdict("LS2 at diagonal 53208 both continuations occur, each for at least 5 seeds",
            len(g) == 2 and min(len(x) for x in g) >= 5, f"sizes {[len(x) for x in g]}")
    verdict("LS3 at least 3 left sides by diagonal 75,000 and at least 4 by diagonal K - 1",
            len(counts[75000]) >= 3 and len(counts[K]) >= 4, f"{len(counts[75000])} and {len(counts[K])}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
