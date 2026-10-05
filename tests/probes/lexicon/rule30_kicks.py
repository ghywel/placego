#!/usr/bin/env python3
"""rule30_kicks.py: what sets the size of a kick to the wheel? The owner's rotation-and-translation lead.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_kicks.py [W=11] [T=2048]
COST:       a few minutes on one core.

Background (RULE30-PRIZE.md sections 8.4 to 8.11). Next to column 0 = 0101..., column 1 runs the wheel U, an exact
coding of the rotation by 17/56. Domain walls arrive from the interior at half a cell per step and kick the wheel's
angle by whole notches of 1/28 turn. A wall arrives at one of two phases (classes 32 and 52), and the class fixes
the kick's sign, but not its size (+2 to +6 notches, or -1 to -6). What sets the size has been open since section 8.8.
The owner (2026-10-05): "my mind drifts back to the interpolation shaders, which would always reveal an oscillating,
string-like hole at the centre under rotation, and under rotation and translation combined it would drift." Read
here, the wall is a string moving through a rotating pattern. If the domain's phase lags from column to column at a
rate other than the wall's speed, the mismatch the wall carries grows with the distance it travels. Then a kick's
size is set by where the wall formed. The alternative: the wall is a boundary between two domains that already
exist, and the kick is just the phase of the domain behind it, carried in.
The measurement, on rule30_walls.py's domain filter (columns 0 .. 12, domain D built from the training half, R
divisible by 7). For each test slip at old phase d, arriving at column 1 at time t1, of class a = (t1 - d) mod 56:
  - the kick: the new phase d' that best fits D over t1 + 2 .. t1 + 20 in columns 1 .. 3 (fit at least 0.95), in
    notches of 1/28 turn;
  - the outer phase: the phase that best fits D in columns 5 .. 10 over t1 - 6 .. t1 - 1, behind the wall, which is
    then between columns 4 and 2. A clean read has a fit of at least 0.9;
  - the origin: the farthest column, up to 12, along which the wall's first departures from D at phase d run in an
    unbroken diagonal back from column 1, each column within 4 steps of 2.19 steps per column;
  - the width: the steps from t1 until column 1 matches D at phase d' for 8 steps running.

PREDICTIONS, written 2026-10-05 before this script's first run:
  KK0 (controls, must hold): (a) the commonest kick in class 32 is +3 notches and in class 52 is -3, as
      rule30_walls.py found; (b) the estimator adds no information of its own: shuffling a feature within each class
      leaves H(kick | class, feature) within 0.1 bits of H(kick | class), for each feature below.
  KK1 (blind; the kick is carried in): the outer phase is read cleanly for at least half of the slips, and where it
      is, it gives the kick exactly in at least 70% of them.
  KK2 (blind; the owner's drift, tested as stated): the origin column tells at least 0.3 bits about the kick beyond the
      class, H(kick | class) - H(kick | class, origin) >= 0.3. My own expectation is that this fails, because a wall
      between two domains carries a fixed phase difference however far it travels.
  KK3 (blind): the width tells at least 0.3 bits beyond the class.
REFUTED-BY: KK0 failing (the instrument); KK1 to KK3 failing.

OUTCOME, 2026-10-05 (the first run, W = 11, T = 2048, 18 seconds; 11,437 test slips with a clean kick):
  KK0 PASSED: (a) class 32 kicks +3 x3431, +4 x1269, +5 x753, +2 x346, +6 x255; class 52 kicks -3 x1837, -5 x1454,
     -1 x987, -4 x435, -6 x305, -2 x146; (b) shuffled features stay within 0.002 bits of H(kick | class) = 1.929.
  KK1 REFUTED: the outer phase is read cleanly for 93% of slips, but gives the kick exactly in only 19.8%. It is off by
     +1 notch in 32% of them, and within 2 notches in 85%. So the kick is roughly carried in, not exactly.
  KK2 REFUTED as stated, with a real signal: the origin column tells 0.208 bits beyond the class. In class 32, walls
     traced to column 12 kick +6 in 218 of 304 cases, against +3 for those traced to 10 or 11. Distance travelled
     matters somewhat; it does not set the kick.
  KK3 VOID, not evidence: the width was 0 for every slip. Column 1 takes up its new phase at once, at the first step
     it leaves the old one, so this measure could not carry information.
  An exploratory look after the run (not a test; scratchpad, not kept as a probe). The domain behind a wall is not
  rigid. Read in bands of two columns (1-2, 3-4, .., 9-10) over the same windows after the arrival, the phase
  differs between bands by whole notches. The steps between bands move toward column 0 over the next 30 steps (in
  the commonest pattern, from columns 7-8 at t1 + 2 to columns 1-2 at t1 + 32). The probe's next mode tests that
  phase field, with predictions written first.

MODE field: is a kick's new phase carried in from outside, and how fast does its front move? The phase field:
for even t and each band of two columns (1-2, 3-4, 5-6, 7-8, 9-10), the phase of D that best fits the band over t ..
t + 8, kept if the fit is at least 0.9. For each slip (old phase d, new phase d', arrival t1 at column 1), search
the 30 steps before t1 for a time when an outer band (columns 5 or beyond) already shows d' while band 1-2 still
shows d.
PREDICTIONS for field, written 2026-10-05 after the outcome above and before field's first run:
  FD0 (control, must hold): the same search for a wrong phase (d' moved by a random nonzero number of notches) finds
      it at most half as often as it finds d'.
  FD1 (blind; carried in): d' is found in an outer band before it reaches column 1 in at least 80% of slips.
  FD2 (blind; the drift): its front moves inward. For each slip where it is found, the speed from the outermost band
      that shows it first to band 3-4 is between 0.15 and 0.6 cells per step (median over slips).

OUTCOME of field, 2026-10-05 (W = 10, 36 seconds, 5,704 slips): the new phase was found outside first in 536
  (9.4%), a wrong phase in 317 (5.6%), and the median front speed was 0.333 cells per step.
  FD0 FAILED: the control is not met (317 against a limit of 268). The outer bands' phase reads are too noisy to
     tell the right phase from a wrong one with confidence.
  FD1 REFUTED, and the refutation survives the instrument's weakness: the 9.4% is an upper bound, far below 80%. A
     kick's new phase is mostly not carried in from outside.
  FD2 VOID: its speeds were measured on detections that are mostly noise (FD0).
  So the kick is decided where the wall meets the wall of column 0, not carried in. Mode local tests that.

MODE local: is the kick decided locally, at the moment of arrival? For each slip, the pattern of columns 1 .. c in the
row at time t1 (the moment the wall reaches column 1), with the class. The slips are split at random into halves. A
table from the first half maps each (class, pattern) to its commonest kick, and falls back to the class's commonest
kick for a pattern it has not seen. It is scored on the second half.
PREDICTIONS for local, written 2026-10-05 after field's outcome and before local's first run:
  LC0 (control, must hold): the same table built from the row at t1 - 20, before the wall is near, does no better than
      the class alone (within 3 percentage points).
  LC1 (blind; the kick is local): for some c <= 8 the pattern predicts the kick in at least 90% of held-out slips.
  LC2 (blind): the class alone predicts it in at most 50% (the sizes vary within a class).

OUTCOME of local, 2026-10-05 (W = 11, 16 seconds, 11,437 slips, split in halves):
  LC0 PASSED: the row at t1 - 20 predicts 47.2%, exactly the class alone.
  LC1 REFUTED: the arrival pattern predicts 47.2% for c = 1 .. 4, 55.6% for 5 and 6, 56.2% for 7 and 8, and 59.3% for
     12. Columns 1 to 4 add nothing (at arrival they are fixed by the class); columns 5 to 12 add a little.
  LC2 HELD (47.2%).
  So the kick is not decided by what is near column 0 when the wall arrives. Together with KK1, KK2 and FD1, its
  size comes from beyond the coherent layer: it is the interior's information, entering through the boundary.
"""
import math, random, sys, pathlib
from collections import Counter, defaultdict

W = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 11
T = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 2048
P, M = 56, 12
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
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
        out.append(next((d for d in range(P) if all(cell(st, a + t, 1) == U[(t - d) % P] for t in range(P))), None))
    return out


def locked(st):
    last_bad = max([t for t in range(T - P) if cell(st, t, 1) != cell(st, t + P, 1)], default=-1)
    return last_bad < T - P - 400


def best_phase(st, D, lo, hi, cols):
    best, agree = None, -1
    for d in range(P):
        a = sum(cell(st, t, i) == D[i][(t - d) % P] for t in range(lo, hi) for i in cols)
        if a > agree:
            best, agree = d, a
    return best, agree / ((hi - lo) * len(cols))


def notches(delta):
    k = (-17 * delta) % P
    k = k - P if k > P // 2 else k
    return k // 2


def cond_entropy(pairs):
    """H(Y | X) in bits from (x, y) pairs (plug-in)."""
    by = defaultdict(Counter)
    for x, y in pairs:
        by[x][y] += 1
    n = len(pairs)
    h = 0.0
    for c in by.values():
        m = sum(c.values())
        h += m / n * -sum(v / m * math.log2(v / m) for v in c.values())
    return h


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

    rows = []                                          # (class, kick, outer kick or None, origin, width)
    for st, ph in test:
        for k in range(1, len(ph)):
            d = ph[k - 1]
            if d is None or ph[k] is not None:
                continue
            t1 = next((t for t in range(k * P, min(T, (k + 1) * P)) if cell(st, t, 1) != D[1][(t - d) % P]), None)
            if t1 is None or t1 - 40 < 0 or t1 + 30 > T:
                continue
            a = (t1 - d) % P
            dd, fit = best_phase(st, D, t1 + 2, t1 + 20, (1, 2, 3))
            if fit < 0.95:
                continue
            kick = notches(dd - d)
            do, ofit = best_phase(st, D, t1 - 6, t1, range(5, 11))
            okick = notches(do - d) if ofit >= 0.9 else None
            origin = 1
            prev = t1
            for i in range(2, M + 1):
                lo = t1 - round(2.19 * (i - 1)) - 4
                ti = next((t for t in range(max(0, lo), prev + 1) if cell(st, t, i) != D[i][(t - d) % P]), None)
                if ti is None or abs(ti - (t1 - 2.19 * (i - 1))) > 4:
                    break
                origin, prev = i, ti
            width = next((u for u in range(0, 24) if all(cell(st, t1 + u + v, 1) == D[1][(t1 + u + v - dd) % P]
                                                       for v in range(8))), 24)
            rows.append((a, kick, okick, origin, width))
    print(f"   {len(rows)} test slips with a clean kick (fit >= 0.95); classes "
          + ", ".join(f"{a}: {c}" for a, c in Counter(r[0] for r in rows).most_common(4)), flush=True)
    for a in (32, 52):
        ks = Counter(r[1] for r in rows if r[0] == a)
        print(f"   class {a}: kicks " + ", ".join(f"{k:+d} x{v}" for k, v in ks.most_common(7)), flush=True)
    top = {a: Counter(r[1] for r in rows if r[0] == a).most_common(1)[0][0] for a in (32, 52)}
    report("KK0a the commonest kick is +3 in class 32 and -3 in class 52", top[32] == 3 and top[52] == -3,
           f"class 32: {top[32]:+d}, class 52: {top[52]:+d}")

    base = cond_entropy([(r[0], r[1]) for r in rows])
    rng = random.Random(1)
    feats = {"origin": 3, "width": 4}
    gain, shuf_ok = {}, True
    for name, j in feats.items():
        h = cond_entropy([((r[0], r[j]), r[1]) for r in rows])
        gain[name] = base - h
        by_class = defaultdict(list)
        for r in rows:
            by_class[r[0]].append(r[j])
        for v in by_class.values():
            rng.shuffle(v)
        it = {a: iter(v) for a, v in by_class.items()}
        hs = cond_entropy([((r[0], next(it[r[0]])), r[1]) for r in rows])
        shuf_ok &= abs(base - hs) <= 0.1
        dist = Counter(r[j] for r in rows)
        print(f"   {name}: H(kick | class) {base:.3f} bits, with {name} {h:.3f} (gain {base - h:.3f}), shuffled "
              f"{hs:.3f}; values " + ", ".join(f"{k}: {v}" for k, v in sorted(dist.items())), flush=True)
    report("KK0b shuffling a feature within its class adds no information (within 0.1 bits)", shuf_ok)

    clean = [r for r in rows if r[2] is not None]
    hit = sum(r[2] == r[1] for r in clean)
    print(f"   outer phase: clean reads {len(clean)} of {len(rows)}; exact {hit}; "
          f"off by: " + ", ".join(f"{k:+d} x{v}" for k, v in Counter(r[1] - r[2] for r in clean).most_common(6)),
          flush=True)
    verdict("KK1 the kick is carried in: clean outer reads for half the slips, and exact in 70% of those",
            len(clean) >= 0.5 * len(rows) and hit >= 0.7 * len(clean),
            f"{len(clean) / len(rows):.1%} clean, {hit / max(len(clean), 1):.1%} exact")
    verdict("KK2 the owner's drift: the origin column tells at least 0.3 bits beyond the class", gain["origin"] >= 0.3,
            f"gain {gain['origin']:.3f} bits")
    verdict("KK3 the width tells at least 0.3 bits beyond the class", gain["width"] >= 0.3,
            f"gain {gain['width']:.3f} bits")
    for name, j in feats.items():
        for a in (32, 52):
            tab = defaultdict(Counter)
            for r in rows:
                if r[0] == a:
                    tab[r[j]][r[1]] += 1
            print(f"   class {a}, kick by {name}: " + "; ".join(
                f"{x}: " + " ".join(f"{k:+d}x{v}" for k, v in c.most_common(3)) for x, c in sorted(tab.items())
                if sum(c.values()) >= 20), flush=True)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def field(wmax=10):
    train, test = [], []
    for R in range(1 << wmax):
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
    bands = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    rng = random.Random(2)
    n = found = wrong = 0
    speeds = []
    for st, ph in test:
        memo = {}

        def phi(b, t):
            if (b, t) not in memo:
                dd, fit = best_phase(st, D, t, t + 8, bands[b])
                memo[(b, t)] = dd if fit >= 0.9 else None
            return memo[(b, t)]
        for k in range(1, len(ph)):
            d = ph[k - 1]
            if d is None or ph[k] is not None:
                continue
            t1 = next((t for t in range(k * P, min(T, (k + 1) * P)) if cell(st, t, 1) != D[1][(t - d) % P]), None)
            if t1 is None or t1 - 40 < 0 or t1 + 30 > T:
                continue
            dd, fit = best_phase(st, D, t1 + 2, t1 + 20, (1, 2, 3))
            if fit < 0.95:
                continue
            n += 1
            shift = rng.choice([x for x in range(-6, 7) if x != 0])
            dw = (dd - 2 * shift * 33) % P            # moves the angle by `shift` notches (33 = 17^-1 mod 56, halved)
            first = {}
            hit_w = False
            for t in range(t1 - 30 - (t1 - 30) % 2, t1 - 1, 2):
                if phi(0, t) != d:
                    continue
                for b in (2, 3, 4):
                    v = phi(b, t)
                    if v == dd and b not in first:
                        first[b] = t
                    if v == dw:
                        hit_w = True
            if first:
                found += 1
                bo = max(first)
                t3 = next((t for t in range(first[bo], t1 + 1, 2) if phi(1, t) == dd), None)
                if t3 is not None and t3 > first[bo]:
                    speeds.append((2 * (bo - 1)) / (t3 - first[bo]))
            wrong += hit_w
    med = sorted(speeds)[len(speeds) // 2] if speeds else float("nan")
    print(f"   {n} slips; the new phase found outside first in {found} ({found / n:.1%}); a wrong phase in {wrong} "
          f"({wrong / n:.1%}); front speeds measured for {len(speeds)}, median {med:.3f} cells per step", flush=True)
    report("FD0 a wrong phase is found at most half as often", wrong <= 0.5 * found, f"{wrong} against {found}")
    verdict("FD1 the new phase is carried in from outside in at least 80% of slips", found >= 0.8 * n,
            f"{found / n:.1%}")
    verdict("FD2 its front moves inward at 0.15 to 0.6 cells per step (median)", 0.15 <= med <= 0.6, f"{med:.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def local():
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
    slips = []
    for st, ph in test:
        for k in range(1, len(ph)):
            d = ph[k - 1]
            if d is None or ph[k] is not None:
                continue
            t1 = next((t for t in range(k * P, min(T, (k + 1) * P)) if cell(st, t, 1) != D[1][(t - d) % P]), None)
            if t1 is None or t1 - 40 < 0 or t1 + 30 > T:
                continue
            dd, fit = best_phase(st, D, t1 + 2, t1 + 20, (1, 2, 3))
            if fit < 0.95:
                continue
            slips.append(((t1 - d) % P, notches(dd - d), st[t1] >> 1, st[t1 - 20] >> 1))
    rng = random.Random(3)
    rng.shuffle(slips)
    half = len(slips) // 2
    fit_set, score_set = slips[:half], slips[half:]
    cls = defaultdict(Counter)
    for a, k, _, _ in fit_set:
        cls[a][k] += 1
    cls_mode = {a: c.most_common(1)[0][0] for a, c in cls.items()}

    def accuracy(c, which):
        tab = defaultdict(Counter)
        for row in fit_set:
            tab[(row[0], row[which] & ((1 << c) - 1))][row[1]] += 1
        hit = 0
        for row in score_set:
            key = (row[0], row[which] & ((1 << c) - 1))
            guess = tab[key].most_common(1)[0][0] if key in tab else cls_mode.get(row[0], 0)
            hit += guess == row[1]
        return hit / len(score_set)
    base = sum(cls_mode.get(a, 0) == k for a, k, _, _ in score_set) / len(score_set)
    acc = {c: accuracy(c, 2) for c in range(1, 13)}
    early = accuracy(8, 3)
    print(f"   {len(slips)} slips; the class alone predicts {base:.1%}; the row at t1, columns 1 .. c: "
          + ", ".join(f"{c}: {v:.1%}" for c, v in acc.items()) + f"; the row at t1 - 20 (c = 8): {early:.1%}",
          flush=True)
    report("LC0 the row at t1 - 20 does no better than the class (within 3 points)", early <= base + 0.03,
           f"{early:.1%} against {base:.1%}")
    best_c = max((c for c in acc if c <= 8), key=lambda c: acc[c])
    verdict("LC1 for some c <= 8 the arrival pattern predicts the kick in at least 90%", acc[best_c] >= 0.90,
            f"best {acc[best_c]:.1%} at c = {best_c}")
    verdict("LC2 the class alone predicts at most 50%", base <= 0.50, f"{base:.1%}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    {"field": field, "local": local}.get(sys.argv[1] if len(sys.argv) > 1 else "", main)()
