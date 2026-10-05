#!/usr/bin/env python3
"""rule30_wake.py: does a kick send a wake into the interior, and does the wake steer the next kick?

RUN-ON:     cpu (pure Python 3, standard library; seeded, fresh seeds)
COMMAND:    python3 tests/probes/lexicon/rule30_wake.py [clean] [N=1500] [T=3000]
COST:       about five minutes on one core.

rule30_worldline.py's W2 found large white triangles 1.19 times as dense as usual on a line moving outwards at half a
cell per step from column 1 about 80 steps before a forward kick. rule30_kickgaps.py could not test the obvious reading
(a wake sent out by the previous kick) because the phase bookkeeping links gaps and classes by itself. This test
anchors on each kick and looks forward from it, outside the domain, where the triangle lattice of section 8.18 does
not reach: the band a = 1 + (t - t1) / 2 +- 1 for t = t1 + 16 .. t1 + 40 (columns 9 to 21). It then compares the
next kick's direction within each class of the current kick, so the bookkeeping cannot produce a difference.

PREDICTIONS, written 2026-10-05 before this script's first run:
  KC  (control): at least 90% of departures in classes 32 and 52.
  WK1 (blind): a kick sends out a wake: the band after kicks of at least one class holds large triangles (size >= 4)
      at least 1.10 times as densely as the same band after random times.
  WK2 (blind): the wake steers the next kick: within the current kick's class (32 and 52 separately), the next kick
      is forward more often when the band holds at least one large triangle than when it holds none, by at least
      0.03 in both classes.
  CF  (counterfactual): the same comparison with the band taken at a random time between the two kicks, instead of
      right after the first, shows no difference (within 0.02 in both classes).
REFUTED-BY: KC or CF failing (the instrument); WK1 or WK2 failing.

OUTCOME of the first run, 2026-10-05 (N = 1500): KC passed (43,066 of 43,664). WK1 HELD (class 32: 1.198, class 52:
1.080). WK2 REFUTED as worded (class 32: +0.025, below 0.03; class 52: +0.227). CF FAILED (class 32 +0.018, class 52
+0.040): the instrument is not clean. The cause, seen after the run: the outgoing band crosses the NEXT wall's
incoming path (they meet at t = t1 + g/2, column 1 + g/4, inside the band for gaps g up to about 80), and forward walls
carry large triangles, so the band partly sees the next kick's own wall. This run therefore does not separate a wake
from the next wall.

ADDENDUM, written 2026-10-05 after the first run and before the second (python3 rule30_wake.py clean): the band is
cut to t = t1 + 16 .. t1 + 28 (columns 9 to 15), and only kick pairs with a gap of at least 70 steps are used, so the
next wall is at column 22 or beyond while the band is read.
  WK3 (blind): with the next wall out of reach, the band after class-32 kicks still holds large triangles at least
      1.10 times as densely as after random times.
  WK4 (blind): within class 52, the next kick is forward more often with a large triangle in the band than without,
      by at least 0.05.
  CF2 (counterfactual): the same comparison with the band at a random time at least 30 steps before the next kick
      shows no difference (within 0.02, both classes).
OUTCOME of the clean run, 2026-10-05 (N = 1500): WK3 HELD: with the next wall out of reach, the band after class-32
kicks holds large triangles 1.202 times as densely as after random times (16,800 pairs), and after class-52 kicks
1.393 times (13,418). Kicks do send triangle-carrying wakes into the interior. WK4 REFUTED: within class 52 the next
kick is forward slightly LESS often with a large triangle in the wake (-0.053; class 32: +0.002); the first run's
+0.227 was the next wall's crossing. CF2 FAILED (class 52: +0.041), so links at the 0.05 level are not trustworthy in
this design. Wakes: yes. Steering: no evidence.
"""
import pathlib, random, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_nums = [a for a in sys.argv[1:] if a != "clean"]
N = int(_nums[0]) if len(_nums) > 0 else 1500
T = int(_nums[1]) if len(_nums) > 1 else 3000
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_triangles as tr                         # noqa: E402
import rule30_wallkind as wk                          # noqa: E402
sys.argv = _argv
P = tr.P
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def wake(B, t0):
    return sum(1 for t in range(t0 + 16, t0 + 41) for a, n in B.get(t, []) if n >= 4 and abs(a - (1 + (t - t0) / 2)) <= 1)


def main():
    rng = random.Random(7171)
    classes = Counter()
    after = {32: [0, 0], 52: [0, 0]}
    ref = [0, 0]
    link = {32: {True: [0, 0], False: [0, 0]}, 52: {True: [0, 0], False: [0, 0]}}
    cf = {32: {True: [0, 0], False: [0, 0]}, 52: {True: [0, 0], False: [0, 0]}}
    for _ in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, _w = tr.spacetime(R, T)
        col1 = [(r >> 1) & 1 for r in rows]
        B = tr.births(rows)
        ks = [k for k in tr.kicks(col1) if 300 <= k[0] <= T - 120]
        for k in ks:
            classes[k[2]] += 1
        for a, b in zip(ks, ks[1:]):
            cl = a[2]
            if cl not in after:
                continue
            w = wake(B, a[0])
            after[cl][0] += w
            after[cl][1] += 1
            tr_ = rng.randrange(300, T - 120)
            ref[0] += wake(B, tr_)
            ref[1] += 1
            nxt_fwd = wk.notch((b[4] - b[1]) % P) > 0
            link[cl][w > 0][0] += nxt_fwd
            link[cl][w > 0][1] += 1
            if b[0] - a[0] > 2:
                tm = rng.randrange(a[0] + 1, b[0])
                wm = wake(B, tm)
                cf[cl][wm > 0][0] += nxt_fwd
                cf[cl][wm > 0][1] += 1
    tot = sum(classes.values())
    report("KC at least 90% of departures in classes 32 and 52", (classes[32] + classes[52]) / tot >= 0.9,
           f"{classes[32] + classes[52]} of {tot}")
    base = ref[0] / ref[1]
    rat = {cl: (v[0] / v[1]) / base for cl, v in after.items()}
    verdict("WK1 a wake: the band after kicks of some class is at least 1.10 x random", max(rat.values()) >= 1.10,
            ", ".join(f"class {cl}: {r:.3f}" for cl, r in rat.items()))

    def diff(tab, cl):
        y, n = tab[cl][True], tab[cl][False]
        return (y[0] / y[1] if y[1] else 0) - (n[0] / n[1] if n[1] else 0), y[1], n[1]
    d = {cl: diff(link, cl) for cl in link}
    verdict("WK2 the wake steers the next kick (forward more often, by >= 0.03, in both classes)",
            all(v[0] >= 0.03 for v in d.values()),
            "; ".join(f"class {cl}: {v[0]:+.3f} ({v[1]} with, {v[2]} without)" for cl, v in d.items()))
    dc = {cl: diff(cf, cl) for cl in cf}
    report("CF a band at a random time between the kicks shows no link (within 0.02)",
           all(abs(v[0]) <= 0.02 for v in dc.values()), "; ".join(f"class {cl}: {v[0]:+.3f}" for cl, v in dc.items()))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def wake_short(B, t0):
    return sum(1 for t in range(t0 + 16, t0 + 29) for a, n in B.get(t, []) if n >= 4 and abs(a - (1 + (t - t0) / 2)) <= 1)


def clean():
    rng = random.Random(7272)
    after = {32: [0, 0], 52: [0, 0]}
    ref = [0, 0]
    link = {32: {True: [0, 0], False: [0, 0]}, 52: {True: [0, 0], False: [0, 0]}}
    cf = {32: {True: [0, 0], False: [0, 0]}, 52: {True: [0, 0], False: [0, 0]}}
    for _ in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, _w = tr.spacetime(R, T)
        col1 = [(r >> 1) & 1 for r in rows]
        B = tr.births(rows)
        ks = [k for k in tr.kicks(col1) if 300 <= k[0] <= T - 120]
        for a, b in zip(ks, ks[1:]):
            cl = a[2]
            if cl not in after or b[0] - a[0] < 70:
                continue
            w = wake_short(B, a[0])
            after[cl][0] += w
            after[cl][1] += 1
            tr_ = rng.randrange(300, T - 120)
            ref[0] += wake_short(B, tr_)
            ref[1] += 1
            nxt_fwd = wk.notch((b[4] - b[1]) % P) > 0
            link[cl][w > 0][0] += nxt_fwd
            link[cl][w > 0][1] += 1
            hi = b[0] - 30 - 28
            if hi > a[0] + 1:
                tm = rng.randrange(a[0] + 1, hi)
                cf[cl][wake_short(B, tm) > 0][0] += nxt_fwd
                cf[cl][wake_short(B, tm) > 0][1] += 1
    base = ref[0] / ref[1]
    rat = {cl: (v[0] / v[1]) / base for cl, v in after.items()}
    verdict("WK3 with the next wall out of reach, class-32 kicks' band >= 1.10 x random", rat[32] >= 1.10,
            ", ".join(f"class {cl}: {r:.3f} ({after[cl][1]} pairs)" for cl, r in rat.items()))

    def diff(tab, cl):
        y, n = tab[cl][True], tab[cl][False]
        return (y[0] / y[1] if y[1] else 0) - (n[0] / n[1] if n[1] else 0), y[1], n[1]
    d = diff(link, 52)
    verdict("WK4 within class 52 a large triangle in the band makes the next kick forward more often, by >= 0.05",
            d[0] >= 0.05, f"{d[0]:+.3f} ({d[1]} with, {d[2]} without); class 32: {diff(link, 32)[0]:+.3f}")
    dc = {cl: diff(cf, cl) for cl in cf}
    report("CF2 a band at a random earlier time shows no link (within 0.02)", all(abs(v[0]) <= 0.02 for v in dc.values()),
           "; ".join(f"class {cl}: {v[0]:+.3f}" for cl, v in dc.items()))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    clean() if sys.argv[1:2] == ["clean"] else main()
