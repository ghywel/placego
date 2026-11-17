#!/usr/bin/env python3
"""rule30_leftsides.py: Rowland's question. Does Rule 30 have one left side, or several, depending on the seed?

RUN-ON:     cpu (pure Python 3, standard library; exact, with certificates)
COMMAND:    python3 tests/probes/lexicon/rule30_leftsides.py [LOGT=18] [K=160000] [SEEDS=40] | ... deeper |
            ... relphase | ... construct
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

OUTCOME of the first run, 2026-10-05 (LOGT = 18, K = 160,000, 41 seeds, 2 minutes 38 seconds): LS0 PASSED. (a) The
strip map matches direct Rule 30. (b) Every seed's strip is certified, each with a cycle of length 32. (c) The single
seed matches. (d) Diagonal 53207 is eventually white, and diagonal 53206 has period 16 with 6 black cells per period:
Rowland's column 53209 is our diagonal 53208, as assumed.
  The single seed's eventually white diagonals below 160,000, each with the period and black count of the diagonal
  before it: 2 (1, 1), 7 (2, 1), 28 (4, 3), 399 (8, 3), 53207 (16, 6), 58286 (16, 10), 87866 (16, 5). The odd ones
  double the period (to 32 at diagonal 87867, the period at 159,999). The even ones are the possible splits, at
  diagonals 53208 and 58287 (Rowland's columns 53209 and 58288).
  LS1 HELD. LS2 REFUTED and LS3 REFUTED: all 41 seeds have ONE left side, at every width up to 160,000, through
  both possible splits. If the seed decided each split by a fair coin, all 41 would agree at the first split with
  probability 2^-40, about 10^-12. So the choice is forced, or nearly so, at least for finite seeds of up to 64 cells.
  Rowland's alternative continuations exist as cycles of the strip map, but these seeds never reach them.

ADDENDUM, written 2026-10-05 after the first run and before the second (python3 rule30_leftsides.py deeper): why is the
choice forced, and for which rows? Diagonals depend only on diagonals nearer the edge, so the seed's information in
the chaotic core (farther from the edge) never reaches the band. A candidate mechanism: once diagonals e - 1 and e - 2
have settled, diagonal e settles at its next reset, so each settling time is locked to the rhythm of the diagonals
before it, and the seed is forgotten. At the split, diagonal 53208 is decided by the time of the last black cell of
diagonal 53207 (after it, 53208 is a running XOR of 53206), so the lock predicts that time's phase.
  LS4 (blind, uncertain): ten random rightful rows (all K diagonals random at t = 0, Rowland's general case) share
      the single seed's left side, as a cycle, to K.
  LS5 (blind): four wide finite seeds (10,000, 50,000, 100,000 and 150,000 random cells) share it too.
  LS6 (blind): the universality includes the phase: at time 2^LOGT - 1 every one of these seeds and five more small
      random seeds has exactly the single seed's strip.
  LS7 (blind; the mechanism): the last black cell of diagonal 53207 falls at the same phase mod 16 for all of them.
OUTCOME of the second run, 2026-10-05 (python3 rule30_leftsides.py deeper, 1 minute 45 seconds): every strip certified
(cycles of 32). At every width up to 160,000, all 20 rows share the single seed's left side: five small seeds, four
wide seeds (10,000 to 150,000 cells), and ten random rightful rows. LS4 HELD (10 of 10) and LS5 HELD (4 of 4): the
left side is one cycle even for Rowland's general case of an arbitrary right part. LS6 REFUTED: only the single seed
itself matches the single seed's strip at the same time. The rows sit at different phases of the one cycle. LS7
REFUTED, and ill-posed: the last black cell of diagonal 53207 falls at t = 70,960 to 71,169, with 12 different phases
mod 16. Because the rows sit at different phases of the cycle, the phase that matters is relative to each row's own
cycle, not absolute time. LS8 asks that.

ADDENDUM, written 2026-10-05 after the second run and before the third (python3 rule30_leftsides.py relphase): the
mechanism, measured relative to each row's own phase. For each row find the shift j with its strip at time T - 1
equal to the single seed's at time T - 1 - j (along the single seed's cycle), so the row runs j steps behind.
  LS8 (blind): the last black cell of diagonal 53207, less j, has the same phase mod 16 for all 20 rows: the decision
      at the split is locked to the cycle, whatever the row.
OUTCOME of the third run, 2026-10-05 (python3 rule30_leftsides.py relphase, 1 minute 47 seconds): LS8 HELD. The rows
run 0 to 25 steps behind the single seed, and once that is removed the last black cell of diagonal 53207 falls at
phase 11 mod 16 for all 20. The decision at the split is locked to the left side's own cycle, whatever the row: the
row is forgotten before the decision is made. That is why every row tried takes the same branch.

ADDENDUM, written 2026-10-05 after the third run and before the fourth (python3 rule30_leftsides.py construct): do
Rowland's other continuations occur for some initial conditions? A strip is the row itself in left-edge coordinates, so
any settled strip is a valid finite seed (at most K cells). Flip, in the single seed's settled strip, the cell of a
branch diagonal: the diagonal before it is white for ever, so nothing resets the flipped one, and the flip should
persist. A flip anywhere else should heal.
  LS9 (blind): flipping diagonal 53208 of the settled strip gives a finite seed whose left side agrees with the
      universal one to width 53208 and differs at width 53209. The other continuation is realised.
  LS10 (blind): the alternative side has its own branch points, Rowland's column 72577 (our diagonal 72576) among them.
      Flipping there, and separately at the universal side's second branch point 58287, gives finite seeds with at
      least 4 distinct left sides in all at width K.
  LS11 (control, blind): flipping a cell at diagonal 60000, not a branch point, heals: the seed's left side is the
      universal one at width K.
OUTCOME of the fourth run, 2026-10-05 (python3 rule30_leftsides.py construct, 24 seconds): LS9 HELD (the flip at 53208
persists: the same left side to width 53208, a different one at 53209). LS10 HELD: the alternative side's branch
points are 53208 and 72576 (Rowland's columns 53209 and 72577); the universal side's are 53208 and 58287 (his 58288).
Flipping at 72576 on the alternative side and at 58287 on the universal side gives 4 distinct certified left sides at
width 160,000, each realised by a finite seed of at most 160,000 cells. LS11 HELD (the flip at 60000 heals). So
Rowland's other continuations do occur for some initial conditions, as he surmised, but only for rows built for them:
every generic row tried (60 distinct rows) has the one universal left side.
"""
import random, sys

_nums = [a for a in sys.argv[1:] if a not in ("deeper", "relphase", "construct")]
LOGT = int(_nums[0]) if len(_nums) > 0 else 18
K = int(_nums[1]) if len(_nums) > 1 else 160000
SEEDS = int(_nums[2]) if len(_nums) > 2 else 40
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


def run_tracked(V, z):
    """strip_run to width K for T steps, also returning the last time diagonal z is black."""
    mask = (1 << K) - 1
    tail, last = [], None
    for t in range(T):
        if (V >> z) & 1:
            last = t
        if t >= T - KEEP:
            tail.append(V)
        V = ((V << 2) ^ ((V << 1) | V)) & mask
    return tail, last


def deeper():
    rng = random.Random(2007)
    z = 53207
    rows = [("the single 1", 1)]
    for k in range(5):
        w = rng.randrange(2, 65)
        rows.append((f"small seed {k + 1} ({w} cells)", 1 | (rng.getrandbits(w - 1) << 1)))
    for w in (10000, 50000, 100000, 150000):
        rows.append((f"wide seed of {w} cells", 1 | (rng.getrandbits(w - 1) << 1)))
    for k in range(10):
        rows.append((f"random rightful row {k + 1}", 1 | (rng.getrandbits(K - 1) << 1)))
    res = []
    for name, V0 in rows:
        tail, last = run_tracked(V0, z)
        cyc = certify(tail)
        res.append((name, tail[-1], cyc, last))
        print(f"   {name}: certified {cyc is not None} (cycle {len(cyc) if cyc else None}); last black of diagonal {z} "
              f"at t = {last}, phase {last % 16 if last is not None else None} mod 16", flush=True)
    ref = res[0]
    same = lambda r, k: r[2] is not None and side(r[2], k) == side(ref[2], k)
    for k in (53208, 53209, 58288, 75000, K):
        print(f"   width {k}: same left side as the single seed for {sum(same(r, k) for r in res)} of {len(res)}",
              flush=True)
    rr = [r for r in res if r[0].startswith("random rightful")]
    wide = [r for r in res if r[0].startswith("wide")]
    verdict("LS4 random rightful rows share the single seed's left side to K", all(same(r, K) for r in rr),
            f"{sum(same(r, K) for r in rr)} of {len(rr)}")
    verdict("LS5 wide finite seeds share it too", all(same(r, K) for r in wide),
            f"{sum(same(r, K) for r in wide)} of {len(wide)}")
    verdict("LS6 every strip equals the single seed's at the same time", all(r[1] == ref[1] for r in res),
            f"{sum(r[1] == ref[1] for r in res)} of {len(res)}")
    ph = {r[3] % 16 for r in res if r[3] is not None}
    verdict("LS7 the last black cell of diagonal 53207 has one phase mod 16 for all", len(ph) == 1,
            f"phases {sorted(ph)}")


def relphase():
    rng = random.Random(2007)                          # the same rows as deeper()
    z = 53207
    rows = [("the single 1", 1)]
    for k in range(5):
        w = rng.randrange(2, 65)
        rows.append((f"small seed {k + 1} ({w} cells)", 1 | (rng.getrandbits(w - 1) << 1)))
    for w in (10000, 50000, 100000, 150000):
        rows.append((f"wide seed of {w} cells", 1 | (rng.getrandbits(w - 1) << 1)))
    for k in range(10):
        rows.append((f"random rightful row {k + 1}", 1 | (rng.getrandbits(K - 1) << 1)))
    ref_tail, ref_last = run_tracked(rows[0][1], z)
    ref_cyc = certify(ref_tail)
    n = len(ref_cyc)
    phases = []
    for name, V0 in rows:
        tail, last = run_tracked(V0, z)
        v = tail[-1]
        j = next((j for j in range(n) if ref_cyc[(n - 1 - j) % n] == v), None)
        rel = (last - j) % 16 if j is not None and last is not None else None
        phases.append(rel)
        print(f"   {name}: last black of diagonal {z} at t = {last}; runs {j} steps behind the single seed; relative "
              f"phase {rel} mod 16", flush=True)
    verdict("LS8 the decision at the split is locked to the cycle (one relative phase mod 16)",
            None not in phases and len(set(phases)) == 1,
            f"relative phases {sorted(set(p for p in phases if p is not None))}")


def branch_points(cyc):
    u = 0
    for v in cyc:
        u |= v
    out = []
    for z in range(1, K - 1):
        if not (u >> z) & 1:
            sq = diag_seq(cyc, z - 1)
            if sum(sq[:period(sq)]) % 2 == 0:
                out.append(z + 1)
    return out


def construct():
    base = certify(strip_run(1, K, T, KEEP))
    settled = base[-1]
    bp = branch_points(base)
    print(f"   universal side: branch points {bp}", flush=True)
    sides = {"universal": base}

    def flipped(V, e, name):
        cyc = certify(strip_run(V ^ (1 << e), K, T, KEEP))
        sides[name] = cyc
        b = branch_points(cyc) if cyc else None
        print(f"   {name}: certified {cyc is not None}; branch points {b}", flush=True)
        return cyc
    alt = flipped(settled, 53208, "flip at 53208")
    same_below = alt is not None and side(alt, 53208) == side(base, 53208)
    differs = alt is not None and side(alt, 53209) != side(base, 53209)
    verdict("LS9 the flip at 53208 persists: same left side to width 53208, different at 53209",
            same_below and differs, f"same to 53208 {same_below}; differs at 53209 {differs}")
    abp = branch_points(alt) if alt else []
    if 72576 in abp:
        flipped(alt[-1], 72576, "flip at 53208, then at 72576")
    if 58287 in bp:
        flipped(settled, 58287, "flip at 58287")
    distinct = len({side(c, K) for c in sides.values() if c})
    verdict("LS10 the alternative side branches at 72576; at least 4 distinct left sides at width K",
            72576 in abp and distinct >= 4, f"alternative side's branch points {abp}; {distinct} distinct sides")
    heal = certify(strip_run(settled ^ (1 << 60000), K, T, KEEP))
    verdict("LS11 a flip at diagonal 60000 heals", heal is not None and side(heal, K) == side(base, K))
    width = settled.bit_length()
    print(f"   the constructed seeds have at most {width} cells (the settled strip's length)", flush=True)


if __name__ == "__main__":
    (construct if "construct" in sys.argv[1:] else relphase if "relphase" in sys.argv[1:]
     else deeper if "deeper" in sys.argv[1:] else main)()
