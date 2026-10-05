#!/usr/bin/env python3
"""rule30_worldline.py: can a forward kick be foreseen from the triangles along its wall's path, far back?

RUN-ON:     cpu (pure Python 3, standard library; seeded, fresh seeds)
COMMAND:    python3 tests/probes/lexicon/rule30_worldline.py [N=1200] [T=3000]
COST:       about five minutes on one core.

rule30_wallkind.py (PRIZE-PROBLEMS.md section 8.18) found that along the last part of a wall's path (t from t1 - 20 to
t1 - 4, cells a = 1 + (t1 - t) / 2 +- 1, the wall moving at half a cell per step), large white triangles (size >= 4)
are 1.40 times as dense as at random times before forward kicks and 1.03 times before backward ones.
rule30_triangles.py's TK1 found no foretelling in a box of the interior (columns 12 to 30, t1 - 48 .. t1 - 13), but
that box mixes the wall's path with everything around it. Here the wall's path is followed further back, where it
is still deep in the interior: t from t1 - 60 to t1 - 21, cells 11 to 31.

PREDICTIONS, written 2026-10-05 before this script's first run:
  KC (control): at least 90% of departures in classes 32 and 52.
  W0 (control, a re-check of K2 on fresh seeds): on the near part of the path the forward kicks' ratio is at least
      1.25 and the backward kicks' at most 1.10.
  W1 (blind): on the far part of the path (t1 - 60 .. t1 - 21) the forward kicks' ratio is at least 1.15: large
      triangles foretell a forward kick 20 to 60 steps ahead, along the line the wall will travel.
  W2 (blind; the counterfactual): the same far band mirrored to the other slope (cells a = 1 + (t - t1 + 80) / 2,
      which no wall arriving at t1 travels) shows no excess for forward kicks: ratio within 0.9 to 1.1.
REFUTED-BY: KC or W0 failing (the instrument); W1 or W2 failing.

OUTCOME of the first run, 2026-10-05 (N = 1200, T = 3000, fresh seeds): KC passed (34,711 of 35,177). W0 passed:
forward 1.389, backward 1.042 on the near path. W1 REFUTED: on the far path the forward ratio is 1.019 (backward
1.061): large triangles do not foretell a forward kick 20 to 60 steps ahead along its wall's line. W2 REFUTED, which is
the interesting part: the "mirrored" band shows 1.186 for forward kicks. That band is a line moving right at half a
cell per step from column 1 at t1 - 80, which is where a disturbance sent outwards by an earlier kick, about 80 steps
before, would travel. So forward kicks may follow earlier events that send a triangle-carrying wake into the interior:
kicks correlated in time. Not tested here; a lead (PRIZE-PROBLEMS.md section 8.18).
"""
import pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
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


def band(B, t1, lo, hi, line):
    return sum(1 for t in range(t1 - lo, t1 - hi + 1) for a, n in B.get(t, []) if n >= 4 and abs(a - line(t1, t)) <= 1)


NEAR = (20, 4, lambda t1, t: 1 + (t1 - t) / 2)
FAR = (60, 21, lambda t1, t: 1 + (t1 - t) / 2)
MIRROR = (60, 21, lambda t1, t: 1 + (t - t1 + 80) / 2)


def main():
    rng = random.Random(5151)
    classes = {}
    sums = {k: {"fwd": [0, 0], "bwd": [0, 0], "ref": [0, 0]} for k in ("near", "far", "mirror")}
    for _ in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, _w = tr.spacetime(R, T)
        col1 = [(r >> 1) & 1 for r in rows]
        B = tr.births(rows)
        for (t1, D, cl, t2, D2) in tr.kicks(col1):
            if not 300 <= t1 <= T - 80:
                continue
            classes[cl] = classes.get(cl, 0) + 1
            n = wk.notch((D2 - D) % P)
            kind = "fwd" if n > 0 else ("bwd" if n < 0 else None)
            refs = [rng.randrange(300, T - 80) for _ in range(2)]
            for name, (lo, hi, line) in (("near", NEAR), ("far", FAR), ("mirror", MIRROR)):
                if kind:
                    sums[name][kind][0] += band(B, t1, lo, hi, line)
                    sums[name][kind][1] += 1
                for r_ in refs:
                    sums[name]["ref"][0] += band(B, r_, lo, hi, line)
                    sums[name]["ref"][1] += 1
    tot = sum(classes.values())
    report("KC at least 90% of departures in classes 32 and 52",
           (classes.get(32, 0) + classes.get(52, 0)) / tot >= 0.9, f"{classes.get(32, 0) + classes.get(52, 0)} of {tot}")

    def ratio(name, kind):
        s = sums[name]
        return (s[kind][0] / s[kind][1]) / (s["ref"][0] / s["ref"][1])
    rn_f, rn_b = ratio("near", "fwd"), ratio("near", "bwd")
    report("W0 near path: forward >= 1.25, backward <= 1.10 (fresh seeds)", rn_f >= 1.25 and rn_b <= 1.10,
           f"forward {rn_f:.3f}, backward {rn_b:.3f}")
    rf_f, rf_b = ratio("far", "fwd"), ratio("far", "bwd")
    verdict("W1 far path (t1 - 60 .. t1 - 21): forward kicks' ratio >= 1.15", rf_f >= 1.15,
            f"forward {rf_f:.3f}, backward {rf_b:.3f}")
    rm_f = ratio("mirror", "fwd")
    verdict("W2 the mirrored band shows no excess for forward kicks (0.9 to 1.1)", 0.9 <= rm_f <= 1.1, f"{rm_f:.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
