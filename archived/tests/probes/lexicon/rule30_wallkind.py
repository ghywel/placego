#!/usr/bin/env python3
"""rule30_wallkind.py: do the walls that kick the wheel forward carry the large white triangles?

RUN-ON:     cpu (pure Python 3, standard library; seeded random right halves, fresh seeds)
COMMAND:    python3 tests/probes/lexicon/rule30_wallkind.py [N=1200] [T=3000]
COST:       about five minutes on one core.

rule30_triangles.py (RULE30-PRIZE.md section 8.18) found the two wall species different: along the wall's path,
large triangles (size >= 4) are 1.47 times as dense as at random times for class-32 walls, and of normal density for
class-52 walls. An exploratory look (2026-10-05, 300 seeds, not recorded) then split kicks by direction: class-32
kicks were forward in 100% of 4,561 (commonest +4 notches), class-52 kicks backward or zero in 92.7% of 4,125
(commonest -6 and -4). So the triangle-carrying walls may be exactly the forward kicks. K1 records what was seen;
K2 and K3 are blind, on fresh seeds, splitting by the kick itself, not by its class.

Notches. A kick re-locks the wheel from phase D to D'; its size in notches (1/28 of a turn) is ((-17 (D' - D)) mod
56, taken in [-28, 27]) / 2, as in rule30_wheelspeed.py and rule30_chaos.py.

PREDICTIONS, written 2026-10-05 before this script's first run:
  KC (control): at least 90% of departures in classes 32 and 52.
  K1 (seen, recorded as a check): at least 95% of class-32 kicks are forward, and at least 85% of class-52 kicks are
      backward or zero.
  K2 (blind; direction, not class): along the wall's path (cells a = 1 + (t1 - t) / 2 +- 1, t from t1 - 20 to t1 - 4),
      births of size >= 4 are at least 1.25 times as dense as at random times before forward kicks, and at most 1.10
      times before backward kicks.
  K3 (blind; size): among forward kicks, those of 4 notches or more have a higher strip density of large triangles
      than those of 1 or 2 notches.
REFUTED-BY: KC failing (the instrument); K1, K2 or K3 failing.

OUTCOME of the first run, 2026-10-05 (N = 1200, T = 3000, fresh seeds): KC passed (35,048 of 35,571). K1 HELD: class
32 forward 100.0%, class 52 backward or zero 92.5%. K2 HELD: along the wall's path, large triangles are 1.396 times
as dense as at random times before forward kicks (20,210) and 1.032 times before backward kicks (13,466). K3 REFUTED:
1.369 for forward kicks of 4 notches or more (11,236), 1.409 for 1 or 2 notches (8,158). The walls that kick the
wheel forward carry the large triangles; how far they kick does not show in them.
"""
import pathlib, random, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_triangles as tr                         # noqa: E402
sys.argv = _argv
P = tr.P
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def notch(delta):
    k = (-17 * delta) % P
    k = k - P if k > P // 2 else k
    return k // 2


def strip_count(B, t1):
    return sum(1 for t in range(t1 - 20, t1 - 3) for a, n in B.get(t, [])
               if n >= 4 and abs(a - (1 + (t1 - t) / 2)) <= 1)


def main():
    rng = random.Random(4242)
    classes, dirs = Counter(), {32: Counter(), 52: Counter()}
    strip = {"fwd": [0, 0], "bwd": [0, 0], "big": [0, 0], "small": [0, 0]}
    ref_sum = ref_n = 0
    for _ in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, _w = tr.spacetime(R, T)
        col1 = [(r >> 1) & 1 for r in rows]
        B = tr.births(rows)
        for (t1, D, cl, t2, D2) in tr.kicks(col1):
            if not 300 <= t1 <= T - 80:
                continue
            classes[cl] += 1
            n = notch((D2 - D) % P)
            if cl in dirs:
                dirs[cl]["fwd" if n > 0 else ("zero" if n == 0 else "bwd")] += 1
            c = strip_count(B, t1)
            key = "fwd" if n > 0 else ("bwd" if n < 0 else None)
            if key:
                strip[key][0] += c
                strip[key][1] += 1
            if n >= 4:
                strip["big"][0] += c
                strip["big"][1] += 1
            elif 1 <= n <= 2:
                strip["small"][0] += c
                strip["small"][1] += 1
            for _ in range(2):
                tr_ = rng.randrange(300, T - 80)
                ref_sum += strip_count(B, tr_)
                ref_n += 1
    tot = sum(classes.values())
    report("KC at least 90% of departures in classes 32 and 52", (classes[32] + classes[52]) / tot >= 0.9,
           f"{classes[32] + classes[52]} of {tot}")
    f32 = dirs[32]["fwd"] / max(sum(dirs[32].values()), 1)
    b52 = (dirs[52]["bwd"] + dirs[52]["zero"]) / max(sum(dirs[52].values()), 1)
    verdict("K1 class 32 forward >= 95%, class 52 backward or zero >= 85%", f32 >= 0.95 and b52 >= 0.85,
            f"class 32 forward {f32:.1%}; class 52 backward or zero {b52:.1%}")
    ref = ref_sum / ref_n
    rat = {k: (v[0] / v[1]) / ref if v[1] else float("nan") for k, v in strip.items()}
    verdict("K2 forward kicks' strips >= 1.25 x random, backward <= 1.10", rat["fwd"] >= 1.25 and rat["bwd"] <= 1.10,
            f"forward {rat['fwd']:.3f} ({strip['fwd'][1]} kicks), backward {rat['bwd']:.3f} ({strip['bwd'][1]} kicks)")
    verdict("K3 forward kicks of >= 4 notches carry more than those of 1 or 2", rat["big"] > rat["small"],
            f">= 4 notches {rat['big']:.3f} ({strip['big'][1]}), 1-2 notches {rat['small']:.3f} ({strip['small'][1]})")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
