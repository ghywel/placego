#!/usr/bin/env python3
"""rule30_walls.py: the wheel's particle is a domain wall. Its speed, its phase lock, the shift it carries, and
whether an episode's shift is the sum of its walls' shifts. Also a census of wheels for other traces.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_walls.py [W=11] [T=2048]
COST:       a few minutes on one core.

An exploratory look (2026-10-05, 11,437 slips, not recorded) gave the average particle: the share of slips in which
each cell is off the domain, aligned at the moment t1 the departure reaches column 1. Its 90% cells run diagonally
from column 10 about 19 steps before t1 to column 1 at t1, and the arrivals sit at only two phases of the wheel,
(t1 - d) mod 56 = 32 (6,054) or 52 (5,164). Behind the front the departures form a checkerboard of near-certain and
near-zero cells, which is what a time-shifted copy of the wheel looks like against the wheel. So the particle looks
like a domain wall between two phases. V1 and L1 below record what was seen; B1 and B2 are new, and blind.

Method. Columns 0..12 over T steps from every right half up to W cells; locked ones are set aside. The domain D is
built from the training half (R divisible by 7), as in rule30_slips.py. A slip at phase d starts where column 1
first leaves D at phase d (time t1); its class is a = (t1 - d) mod 56.
  Shift of a wall. Over t1 + 2 .. t1 + 20 in columns 1..3, the phase d' that best fits D. The class's shift s_a is the
  commonest d' - d over the training slips of that class.
  Episode accounting. From t1, a running phase phi: at each departure of column 1 from D at phase phi (the first one,
  then the next one after it), phi += s_a for the departure's class a, until the next exact window. The episode is
  predicted when phi equals that window's phase. A departure of an unknown class ends the prediction (counted as
  failed).

PREDICTIONS, written 2026-10-05 before this script's first run:
  V1 (seen, recorded as a check): in the average particle, the first time each column 1..10 reaches 90% fits a line of
     slope -2 steps per column, within [-2.4, -1.6]: a speed of half a cell per step.
  L1 (seen, recorded as a check): at least 90% of slips arrive in two classes.
  B1 (blind): each of the two main classes carries one shift: at least 80% of its test slips have d' - d = s_a, and the
     best fit agrees with D on at least 90% of those cells.
  B2 (blind): adding up the walls' shifts predicts the episode's total shift for at least 80% of episodes.
  CF (the noise control that rule30_slips.py lacked): the same average image, aligned at random times inside exact
     windows (no slip), has no cell in columns 1..6 reaching 50%. The particle's diagonal is defined at 90%; single
     domain cells in columns 5 and 6 are impure enough that a 10% threshold would test the domain, not the particle.
  S  (the random-chaos step, a census, blind): of the traces 0, 1, 001, 011, 0011, 0111, 00011, 00101, 000111, at least
     one other than 01 turns a wheel of its own. Its column 1 then has a sharp line (S >= 10) at a frequency that is
     not a multiple of 1 / (trace period), within 0.002.
  E1 (blind; the owner's tangent, 2026-10-05: "electron orbits, and how electrons jump between orbits ... is the wheel
     fixed or can its size vary?"): column 1's orbits are discrete: the wheel U, the second wheel U2 (both period 56),
     and the locks of period 4 and 14. Each 56-step window of column 1, over every right half up to W cells (locked ones
     included), is classified as U, U2 (a rotation of the word), L4 or L14 (period 4 or 14), or none. E1: jumps between
     U and U2 (consecutive classified windows of one column, gaps ignored) occur in both directions.
  E2 (blind): the locks absorb: no jump from L4 or L14 to U or U2.
REFUTED-BY: CF failing (the instrument); B1, B2, S, E1 or E2 failing; V1 or L1 failing would mean the exploratory look
  misled.

OUTCOME of the first run, 2026-10-05 (W = 11, T = 2048; 11,437 test slips in the image):
  CF passed (the highest cell 0.215 over 5,051 random alignments). V1 HELD (slope -2.19; first 90% at columns 1..10:
  0, -1, -4, -5, -10, -13, -14, -15, -16, -19). L1 HELD (98.1%: classes 32 x 6,054, 52 x 5,164, 42 x 215, 12 x 4).
  B1 REFUTED: class 32's commonest shift, 26, holds in 56.7% of slips, and class 52's, 30, in 35.6%. Where the shift
  matches, the fit behind the wall is 1.000, an exact shifted wheel. B2 REFUTED: 545 of 11,064 episodes (4.9%).
  S REFUTED: no other trace turns a wheel of its own. Every highest line sits at a multiple of 1/p (001 and 011 at 1/3,
  0011 at 1/4, 00011 at 1/5, 00101 at 2/5, 0111 and 000111 at 1/2), and traces 0 and 1 show no line. Among the
  traces tried, only 01 makes a wheel of its own.
  E1 and E2 REFUTED, with a correction to their framing. The jumps are U2 -> U 193 times, U -> U2 never, and L4 -> U
  once; there are no L14 windows. That is because U2 HAS LEAST PERIOD 14 (it is 00010011001101 four times): U2 is the
  14-lock, not a second wheel, and the classifier tested for U2 before L14. So E1's jumps run between the 14-step
  lock and the 56-step wheel, one way only: the lock decays into the wheel and is never re-entered here. E2 fails on
  one jump out of the 4-lock.
  Added after the first run, as measurements (the second and third runs, identical otherwise): the shifts per class
  differ by multiples of 10 steps, the wheel's block. A delay of D steps turns the wheel's angle by -17 D / 56 of a
  turn. In notches of 1/28 turn, class 32 kicks +3 (x561), +4 (x227), +5 (x124), +2 (x54), +6 (x47); class 42 kicks
  +2 (x27), +3 (x12), +1 (x1); class 52 kicks -3 (x278), -5 (x226), -1 (x162), -4 (x68), -6 (x61). Every kick is a
  whole number of notches, and the sign is set by the class: two species of wall, forward and backward.
"""
import math, random, sys, pathlib
from collections import Counter, defaultdict

W = int(sys.argv[1]) if len(sys.argv) > 1 else 11
T = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
P, M = 56, 12

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
import rule30_twosided as ts                           # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def spacetime(R):
    mask = (1 << (R.bit_length() + T + 3)) - 1
    row, rows = R << 1, []
    for t in range(T):
        rows.append(row & ((1 << (M + 1)) - 1))
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return rows


def cell(st, t, i):
    return (st[t] >> i) & 1


def phases(st):
    out = []
    for a in range(0, T - P + 1, P):
        d = next((d for d in range(P) if all(cell(st, a + t, 1) == U[(t - d) % P] for t in range(P))), None)
        out.append(d)
    return out


def locked(st):
    last_bad = max([t for t in range(T - P) if cell(st, t, 1) != cell(st, t + P, 1)], default=-1)
    return last_bad < T - P - 400


def best_phase(st, D, lo, hi, cols=(1, 2, 3)):
    best, agree = None, -1
    for d in range(P):
        a = sum(cell(st, t, i) == D[i][(t - d) % P] for t in range(lo, hi) for i in cols)
        if a > agree:
            best, agree = d, a
    return best, agree / ((hi - lo) * len(cols))


def departure(st, D, phi, t0, t_end):
    return next((t for t in range(t0, t_end) if cell(st, t, 1) != D[1][(t - phi) % P]), None)


def col1_line(trace, n=1024, nR=512):
    """Highest spectral line of column 1 for a trace (Wiener-Khinchin, M = n/4 lags, as rule30_spectrum_fine.py)."""
    Ml = n // 4
    agree, ones = [0] * (Ml + 1), 0
    for R in range(nR):
        b = ts.column1(R, trace, n)
        x = sum(v << k for k, v in enumerate(b))
        ones += bin(x).count("1")
        for j in range(Ml + 1):
            agree[j] += n - j - bin((x ^ (x >> j)) & ((1 << (n - j)) - 1)).count("1")
    mean = (2 * ones - nR * n) / (nR * n)
    C = [(2 * a - nR * (n - j)) / (nR * (n - j)) - mean * mean for j, a in enumerate(agree)]
    win = [(1 + math.cos(math.pi * j / (Ml + 1))) / 2 * C[j] for j in range(Ml + 1)]
    best = (0.0, -1e9)
    for i in range(1, 2500):
        f = i * 0.0002
        s = C[0] + 2 * sum(win[j] * math.cos(2 * math.pi * f * j) for j in range(1, Ml + 1))
        if s > best[1]:
            best = (f, s)
    return best


def main():
    train, test = [], []
    for R in range(1 << W):
        st = spacetime(R)
        if locked(st):
            continue
        (train if R % 7 == 0 else test).append((st, phases(st)))
    votes = [[[0, 0] for _ in range(P)] for _ in range(M + 1)]
    for st, ph in train:
        for k, d in enumerate(ph):
            if d is None:
                continue
            for t in range(k * P, k * P + P):
                for i in range(M + 1):
                    votes[i][(t - d) % P][cell(st, t, i)] += 1
    D = [[0 if v[0] >= v[1] else 1 for v in votes[i]] for i in range(M + 1)]

    def slips(data):
        for st, ph in data:
            for k in range(1, len(ph)):
                d = ph[k - 1]
                if d is not None and ph[k] is None:
                    t1 = departure(st, D, d, k * P, min(T, (k + 1) * P))
                    if t1 is not None:
                        yield st, ph, k, d, t1

    shifts = defaultdict(Counter)                         # the shift table, from the training half
    for st, ph, k, d, t1 in slips(train):
        if t1 + 20 <= T:
            dd, _ = best_phase(st, D, t1 + 2, t1 + 20)
            shifts[(t1 - d) % P][(dd - d) % P] += 1
    s_a = {a: c.most_common(1)[0][0] for a, c in shifts.items() if sum(c.values()) >= 20}

    img = [[0] * (M + 1) for _ in range(44)]
    n, classes, b1 = 0, Counter(), defaultdict(lambda: [0, 0, 0.0])
    ep_n = ep_ok = 0
    for st, ph, k, d, t1 in slips(test):
        a = (t1 - d) % P
        if t1 - 36 >= 0 and t1 + 8 <= T:
            n += 1
            classes[a] += 1
            for r, t in enumerate(range(t1 - 36, t1 + 8)):
                for i in range(M + 1):
                    img[r][i] += cell(st, t, i) != D[i][(t - d) % P]
        if t1 + 20 <= T and a in s_a:
            dd, fit = best_phase(st, D, t1 + 2, t1 + 20)
            rec = b1[a]
            rec[0] += 1
            if (dd - d) % P == s_a[a]:
                rec[1] += 1
                rec[2] += fit
        nxt = next(((j, ph[j]) for j in range(k + 1, len(ph)) if ph[j] is not None), None)
        if nxt is None:
            continue
        ep_n += 1
        phi, t, end = d, t1, nxt[0] * P
        ok = True
        while t is not None and t < end:
            c = (t - phi) % P
            if c not in s_a:
                ok = False
                break
            phi = (phi + s_a[c]) % P
            t = departure(st, D, phi, t + 1, end)
        ep_ok += ok and phi == nxt[1]

    # CF: the same image aligned at random times inside exact windows
    rng = random.Random(8)
    cf = [[0] * 7 for _ in range(44)]
    cf_n = 0
    for st, ph in test:
        exact = [k for k, d in enumerate(ph) if d is not None]
        for _ in range(3):
            if not exact:
                break
            k = rng.choice(exact)
            d = ph[k]
            t1 = k * P + rng.randrange(P)
            if t1 - 36 < 0 or t1 + 8 > T:
                continue
            cf_n += 1
            for r, t in enumerate(range(t1 - 36, t1 + 8)):
                for i in range(1, 7):
                    cf[r][i] += cell(st, t, i) != D[i][(t - d) % P]
    worst = max(cf[r][i] / cf_n for r in range(44) for i in range(1, 7))
    report("CF aligned at random times inside exact windows, no cell in columns 1..6 reaching 50%", worst < 0.50,
           f"highest {worst:.3f} over {cf_n} alignments")

    first90 = []
    for i in range(1, 11):
        r = next((r for r in range(44) if img[r][i] / n >= 0.9), None)
        first90.append((i, None if r is None else r - 36))
    pts = [(i, t) for i, t in first90 if t is not None]
    mi = sum(i for i, _ in pts) / len(pts)
    mt = sum(t for _, t in pts) / len(pts)
    slope = sum((i - mi) * (t - mt) for i, t in pts) / sum((i - mi) ** 2 for i, _ in pts)
    verdict("V1 (seen) the front moves at half a cell per step: slope in [-2.4, -1.6] steps per column",
            len(pts) == 10 and -2.4 <= slope <= -1.6, f"slope {slope:.2f}; first 90% per column {first90}")
    top2 = sum(c for _, c in classes.most_common(2)) / n
    verdict("L1 (seen) two arrival classes hold at least 90% of slips", top2 >= 0.90,
            f"{top2:.1%}; classes {classes.most_common(4)}")
    main2 = [a for a, _ in classes.most_common(2)]
    parts, held = [], True
    for a in main2:
        tot, hit, fit = b1[a]
        share = hit / tot if tot else 0.0
        mfit = fit / hit if hit else 0.0
        held &= share >= 0.80 and mfit >= 0.90
        parts.append(f"class {a}: shift {s_a.get(a)} in {share:.1%} of {tot}, fit {mfit:.3f}")
    verdict("B1 each main class carries one shift", held, "; ".join(parts))
    verdict("B2 the walls' shifts add up to the episode's shift", ep_n > 0 and ep_ok / ep_n >= 0.80,
            f"{ep_ok} of {ep_n} episodes ({ep_ok / ep_n:.1%})")
    print("   shift table from the training half (class: shift, slips): "
          + ", ".join(f"{a}: {s_a[a]} ({sum(shifts[a].values())})" for a in sorted(s_a)), flush=True)
    print("   shift distributions in the training half (a measurement, added after the first run): "
          + "; ".join(f"class {a}: " + ", ".join(f"{d}: {v}" for d, v in shifts[a].most_common(5)) for a in sorted(s_a)),
          flush=True)

    def notches(delta):
        """A delay of delta steps turns the wheel's angle by -17 delta / 56 of a turn; in notches of 2/56 = 1/28."""
        k = (-17 * delta) % P
        k = k - P if k > P // 2 else k
        return k / 2
    print("   the same as kicks to the wheel's angle, in notches of 1/28 turn (a measurement, added after the first run): "
          + "; ".join(f"class {a}: " + ", ".join(f"{notches(d):+g} (x{v})" for d, v in shifts[a].most_common(5))
                      for a in sorted(s_a)), flush=True)

    print("\n   the random-chaos step, a census of wheels: column 1's highest line for each trace", flush=True)
    own = []
    for name in ("01", "0", "1", "001", "011", "0011", "0111", "00011", "00101", "000111"):
        trace = tuple(int(c) for c in name)
        f, s = col1_line(trace)
        p = len(trace)
        on_grid = min(abs(f - k / p) for k in range(p + 1)) <= 0.002
        print(f"      trace {name:>6}: line at f = {f:.4f} (S = {s:.1f}){'' if on_grid else '  <- not a multiple of 1/' + str(p)}",
              flush=True)
        if name != "01" and s >= 10 and not on_grid:
            own.append(name)
    verdict("S another trace turns a wheel of its own", bool(own), f"{own}")

    print("\n   the owner's tangent: orbits and jumps. Column 1's 56-step windows over every right half up to W cells:",
          flush=True)
    U2 = [int(c) for c in wl.U2]
    rotU = {tuple(U[(t - d) % P] for t in range(P)) for d in range(P)}
    rotU2 = {tuple(U2[(t - d) % P] for t in range(P)) for d in range(P)}

    def kind(w):
        if w in rotU:
            return "U"
        if w in rotU2:
            return "U2"
        if all(w[t] == w[t + 4] for t in range(P - 4)):
            return "L4"
        if all(w[t] == w[t + 14] for t in range(P - 14)):
            return "L14"
        return None
    seen, jumps = Counter(), Counter()
    for R in range(1 << W):
        c = ts.column1(R, (0, 1), T)
        ks = [kind(tuple(c[a:a + P])) for a in range(0, T - P + 1, P)]
        seen.update(k for k in ks if k)
        last = None
        for k in ks:
            if k is None:
                continue
            if last is not None and k != last:
                jumps[(last, k)] += 1
            last = k
    print("      windows by orbit: " + ", ".join(f"{k}: {v}" for k, v in seen.most_common()), flush=True)
    print("      jumps (from -> to): " + ", ".join(f"{a}->{b}: {v}" for (a, b), v in jumps.most_common()), flush=True)
    verdict("E1 jumps between the two wheels occur both ways", jumps[("U", "U2")] > 0 and jumps[("U2", "U")] > 0,
            f"U->U2 {jumps[('U', 'U2')]}, U2->U {jumps[('U2', 'U')]}")
    out_of_lock = sum(v for (a, b), v in jumps.items() if a in ("L4", "L14") and b in ("U", "U2"))
    verdict("E2 the locks absorb (no jump from a lock back to a wheel)", out_of_lock == 0, f"{out_of_lock} such jumps")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
