#!/usr/bin/env python3
"""rule30_leftband.py: the band of short-period stripes along Rule 30's left edge. How wide is it, and how does it grow?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_leftband.py [LOGT=13] [EMAX=2048] | rule30_leftband.py front
COST:       about a minute on one core.

rule30_diagonals.py (PRIZE-PROBLEMS.md section 8.27) found that the left diagonals E_e(t) = c(t, e - t), the lines
parallel to the pyramid's left edge at distance e from it, are eventually periodic with tiny periods: at most 8 up to
e = 63. A left period can grow only just after an eventually-zero left diagonal (proved there), and those were at
e = 2, 7 and 28 only. Each diagonal becomes periodic after a transient of m_e steps, so the region left of the line
where the transients end, (t, x) with t >= m_(x + t), is a band of short-period stripes along the left edge. That
band shows in rule30_channels.png. At e = 63, m_e / e was 1.44 and still growing. Here the left diagonals are followed
to e = EMAX over 2^LOGT steps, for the single seed and, as the chaos step, for random finite seeds (the proof holds for
any finite seed, with e counted from the pattern's left edge, which moves left one cell per step).

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run):
  LB0 (control): for e <= 63 the periods and preperiods equal rule30_diagonals.py's (recorded there), and every period
      that grows does so just after an eventually-zero diagonal, for every e up to EMAX (proved).
  LB1 (blind): the eventually-zero diagonals keep coming, spaced roughly geometrically (2, 7, 28: ratios near 4): at
      least one more below 200 and at least one more between 200 and EMAX. The left period stays small: at most 64 at
      e = EMAX.
  LB2 (blind): the band grows linearly. Over e from EMAX/4 to the last e measured, m_e / e settles (its values at the
      last quarter's start and end differ by under 10%) at a constant c between 1.4 and 2.2, so the band's inner
      boundary moves at 1/c - 1, between -0.29 and -0.55 cells per step, and the band holds the fraction 1/(2c) of each
      row, between 0.23 and 0.36.
  LB3 (the chaos step, blind): three random 17-cell seeds (the centre cell black) also have eventually periodic left
      diagonals to e = EMAX / 2 with periods at most 64, and a band constant c in the same range [1.4, 2.2].
REFUTED-BY: LB0 failing (the instrument or the proof); LB1, LB2 or LB3 failing.

OUTCOME of the first run, 2026-10-05 (LOGT = 13, EMAX = 2048, 5 seconds): LB0 PASSED (e = 0 to 63 match; all of 0 to
2047 measured; the eventually-zero diagonals are e = 2, 7, 28 and 399, and the periods grow at 3, 8, 29 and 400 only).
The periods seen are 1, 2, 4, 8 and 16; 16 at e = 2047. Preperiods at e = 100, 500, 1000, 2047: 134, 635, 1275, 2685.
LB1 REFUTED: no eventually-zero diagonal between 29 and 398; the next after 28 is 399, so the gaps grow faster than
geometrically (5, 21, 371). The period at e = 2047 is 16 (within the bound). LB2 REFUTED on its range only: m_e / e
settles (1.307 at the last quarter's start, 1.312 at 2047) at c = 1.304, below the predicted 1.4 to 2.2. The band of
stripes holds the left 0.383 of every row, and its inner boundary moves left at 0.233 cells per step. LB3 REFUTED on
its range only: three random seeds (1000001110011, 10000111110101, 1000100100000011) have eventually periodic left
diagonals with periods at most 16 and THE SAME eventually-zero diagonals, 2, 7, 28 and 399, with c = 1.24, 1.23 and
1.30 (fitted through 0, which a seed's width biases). The band is universal: its stripes do not depend on the seed.

ADDENDUM, written 2026-10-05 after the first run and before the second (python3 rule30_leftband.py front): is the band
the part of the pyramid that the seed's information has not reached? Its boundary speed, 0.233, is close to the
leftward speeds of information found before (PRIZE-PROBLEMS.md section 8.17, 0.21 cells per step next to a clamped
column; section 8.19, 0.28 for a second seed on the open line).
  LB4 (blind): Rule 30 from 1 and from 11 (the extra cell on the right, so the left edge is the same) differ only
      right of a front that moves left at a speed within 0.02 of 0.233 (least squares over t from T/4 to T).
  LB5 (blind): the same front on a random background (two random rows differing in one cell, 10 trials over 2^LOGT
      steps) moves left at a speed within 0.02 of the band's: the band's edge is Rule 30's leftward speed of
      information.
"""
import random, sys

_nums = [a for a in sys.argv[1:] if a != "front"]
LOGT = int(_nums[0]) if len(_nums) > 0 else 13
EMAX = int(_nums[1]) if len(_nums) > 1 else 2048
T = 1 << LOGT
FAILS = 0
# rule30_diagonals.py's left diagonals 0 .. 63 (period, preperiod), from its recorded run at 2^18 steps
DG_LEFT = [(1, 0), (1, 1), (1, 2), (2, 2), (1, 2), (2, 2), (2, 2), (1, 0), (4, 2), (1, 5), (4, 6), (4, 8), (4, 6),
           (4, 10), (4, 11), (4, 13), (4, 16), (4, 15), (4, 20), (4, 18), (4, 23), (4, 23), (4, 25), (2, 24), (4, 27),
           (4, 28), (4, 29), (4, 30), (1, 31), (8, 30), (1, 33), (8, 34), (8, 36), (8, 36), (8, 40), (8, 37), (8, 46),
           (8, 41), (8, 48), (8, 50), (8, 55), (8, 52), (8, 57), (8, 56), (8, 61), (4, 59), (8, 64), (8, 62), (8, 71),
           (8, 65), (8, 73), (8, 74), (8, 76), (8, 75), (8, 78), (8, 78), (8, 82), (8, 79), (8, 84), (8, 85), (8, 86),
           (8, 87), (8, 87), (8, 91)]


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def pow2_period(S, n):
    """As rule30_diagonals.py's eventual test: the smallest power of 2 p with s[i] == s[i + p] from a preperiod on,
    the periodic part spanning at least two periods and a quarter of the window. Returns (p, pre) or (None, None)."""
    p = 1
    while 2 * p <= n:
        diff = (S ^ (S >> p)) & ((1 << (n - p)) - 1)
        pre = diff.bit_length()
        if n - pre >= max(2 * p, n // 4):
            return p, pre
        p *= 2
    return None, None


def left_diagonals(seed, emax):
    """seed: list of cells x = 0 .. w-1 (x = 0 is the leftmost, and black). Returns (period, preperiod, eventually 0)
    for left diagonals e = 0 .. emax-1, e counted from the pattern's left edge."""
    w = len(seed)
    off = T + 2                                        # bit off + x holds cell x
    row = sum(b << (off + x) for x, b in enumerate(seed))
    mask = (1 << (off + w + T + 3)) - 1
    M = (1 << emax) - 1
    wins = []
    for t in range(T):
        wins.append((row >> (off - t)) & M)            # bit e: cell x = e - t, the left edge being at x = -t
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    out = []
    for e in range(emax):
        S = int("".join("1" if (v >> e) & 1 else "0" for v in reversed(wins)), 2)
        p, pre = pow2_period(S, T)
        out.append((p, pre, p == 1 and not (wins[-1] >> e) & 1))
    return out


def band(diags, lo):
    """m_e / e at the start and end of the last quarter of the measured range, and the least-squares c (m_e ~ c e
    through 0) over e >= lo."""
    es = [e for e, (p, pre, _) in enumerate(diags) if p is not None and e >= lo]
    if not es:
        return None
    c = sum(e * diags[e][1] for e in es) / sum(e * e for e in es)
    q = es[-1] - (es[-1] - es[0]) // 4
    near = lambda e0: min(es, key=lambda e: abs(e - e0))
    a, b = near(q), es[-1]
    return c, diags[a][1] / a, diags[b][1] / b, es[-1]


def main():
    d = left_diagonals([1], EMAX)
    last = next((e for e in range(EMAX) if d[e][0] is None), EMAX) - 1    # the last of an unbroken run measured
    same = all((d[e][0], d[e][1]) == DG_LEFT[e] for e in range(64))
    zeros = [e for e, (_, _, z) in enumerate(d) if z]
    grows, ok = [], True
    for e in range(2, last + 1):
        if d[e][0] is None or d[e - 1][0] is None or d[e - 2][0] is None:
            ok = False
            break
        if d[e][0] > max(d[e - 1][0], d[e - 2][0]):
            grows.append(e)
            ok &= d[e - 1][2]
    report("LB0 left diagonals 0 to 63 as rule30_diagonals.py found; periods grow only after eventually-zero diagonals",
           same and ok, f"match {same}; measured to e = {last}; eventually zero at {zeros}; periods grow at {grows}")
    periods = sorted({p for p, _, _ in d if p})
    print(f"   periods seen: {periods}; period at e = {last}: {d[last][0]}; preperiods at e = 100, 500, 1000, {last}: "
          + ", ".join(str(d[e][1]) for e in (100, 500, 1000, last) if e <= last), flush=True)
    verdict("LB1 more eventually-zero diagonals below 200 and between 200 and EMAX; period at EMAX at most 64",
            any(28 < e < 200 for e in zeros) and any(200 <= e < EMAX for e in zeros) and (d[last][0] or 0) <= 64,
            f"eventually zero at {zeros}")
    b = band(d, EMAX // 4)
    c, ra, rb, eb = b
    settled = abs(rb - ra) / ra < 0.10
    print(f"   m_e / e: {ra:.3f} at the last quarter's start, {rb:.3f} at e = {eb}; least squares c = {c:.3f}: the "
          f"band's inner boundary moves at {1 / c - 1:+.3f} cells per step and holds {1 / (2 * c):.3f} of each row",
          flush=True)
    verdict("LB2 the band grows linearly with c between 1.4 and 2.2 (m_e / e settled within 10%)",
            settled and 1.4 <= c <= 2.2, f"c = {c:.3f}, settled {settled}")
    rng = random.Random(1919)
    held = True
    for k in range(3):
        seed = [rng.getrandbits(1) for _ in range(17)]
        seed[8] = 1
        first = seed.index(1)
        seed = seed[first:]
        while seed[-1] == 0:
            seed.pop()
        dk = left_diagonals(seed, EMAX // 2)
        ok_k = all(p is not None and p <= 64 for p, _, _ in dk)
        bk = band(dk, EMAX // 8)
        ck = bk[0] if bk else float("nan")
        zk = [e for e, (_, _, z) in enumerate(dk) if z]
        print(f"   random seed {''.join(map(str, seed))}: all periodic with periods <= 64 {ok_k} (largest "
              f"{max((p or 0) for p, _, _ in dk)}); eventually zero at {zk[:12]}{' ...' if len(zk) > 12 else ''}; "
              f"c = {ck:.3f}", flush=True)
        held &= ok_k and 1.4 <= ck <= 2.2
    verdict("LB3 the chaos step: random finite seeds have the same band (periods <= 64, c in [1.4, 2.2])", held)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def front_speed(a, b, width, off):
    """Run Rule 30 from rows a and b (bit off + x holds cell x) for T steps; return the least-squares slope of the
    leftmost differing cell's position against t, over t from T/4 to T."""
    mask = (1 << width) - 1
    pts = []
    for t in range(T):
        d = a ^ b
        if t >= T // 4 and d:
            low = (d & -d).bit_length() - 1             # the lowest set bit: the leftmost differing cell
            pts.append((t, low - off))
        a = ((a << 1) ^ (a | (a >> 1))) & mask
        b = ((b << 1) ^ (b | (b >> 1))) & mask
    mt = sum(t for t, _ in pts) / len(pts)
    mx = sum(x for _, x in pts) / len(pts)
    return sum((t - mt) * (x - mx) for t, x in pts) / sum((t - mt) ** 2 for t, _ in pts)


def front():
    v_band = 1 / 1.304 - 1                              # the first run's band boundary
    off, width = T + 2, 2 * T + 8
    v_seed = front_speed(1 << off, (1 << off) | (1 << (off + 1)), width, off)
    verdict("LB4 the seed's information front (1 against 11) moves at the band's speed within 0.02",
            abs(v_seed - v_band) <= 0.02, f"front {v_seed:+.4f}, band {v_band:+.4f} cells per step")
    rng = random.Random(1920)
    vs = []
    W = 4 * T + 8
    for _ in range(10):
        a = rng.getrandbits(W)
        b = a ^ (1 << (2 * T + 4))                      # one cell flipped in the middle
        vs.append(front_speed(a, b, W, 2 * T + 4))
    mean = sum(vs) / len(vs)
    print("   random-background fronts: " + ", ".join(f"{v:+.4f}" for v in vs), flush=True)
    verdict("LB5 the random-background front moves at the band's speed within 0.02", abs(mean - v_band) <= 0.02,
            f"mean {mean:+.4f}, band {v_band:+.4f}")


if __name__ == "__main__":
    front() if "front" in sys.argv[1:] else main()
