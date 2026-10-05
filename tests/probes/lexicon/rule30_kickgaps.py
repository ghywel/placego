#!/usr/bin/env python3
"""rule30_kickgaps.py: are the wheel's kicks correlated in time? The gaps between departures, and which kind follows.

RUN-ON:     cpu (pure Python 3, standard library; seeded, fresh seeds)
COMMAND:    python3 tests/probes/lexicon/rule30_kickgaps.py [N=1500] [T=3000]
COST:       about three minutes on one core.

rule30_worldline.py's W2 found large white triangles 1.19 times as dense as usual on a line moving outwards at half a
cell per step from column 1 about 80 steps before a forward kick (PRIZE-PROBLEMS.md section 8.18): perhaps a wake
sent out by an earlier event. If so, departures should be correlated in time. rule30_chaos.py's D3 found consecutive
kicks' sizes nearly memoryless; their timing was not looked at.

PREDICTIONS, written 2026-10-05 before this script's first run:
  KC (control): at least 90% of departures in classes 32 and 52.
  G1 (blind): the gaps between consecutive departures are not memoryless: their distribution has a local peak, at
      least 20% above the mean of the gaps 10 steps either side, somewhere between 60 and 100 steps.
  G2 (blind): the next kick is forward more often when the gap from the previous departure lies between 70 and 90
      steps than overall, by at least 0.05.
  CF (counterfactual): with the departure times of each seed shuffled among that seed's own gaps (same gaps, random
      order), the class sequence loses any link to the gap: G2's difference falls within 0.03 of zero.
REFUTED-BY: KC or CF failing (the instrument); G1 or G2 failing.
"""
import pathlib, random, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
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


def fwd_gap_link(pairs):
    """pairs of (gap, next is forward): P(forward | 70 <= gap <= 90) - P(forward)."""
    if not pairs:
        return 0.0
    allf = sum(f for _, f in pairs) / len(pairs)
    sel = [f for g, f in pairs if 70 <= g <= 90]
    return (sum(sel) / len(sel) - allf) if sel else 0.0


def main():
    rng = random.Random(6060)
    classes = Counter()
    gaps = Counter()
    pairs, shuffled = [], []
    for _ in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, _w = tr.spacetime(R, T)
        col1 = [(r >> 1) & 1 for r in rows]
        ks = [k for k in tr.kicks(col1) if 300 <= k[0] <= T - 80]
        for k in ks:
            classes[k[2]] += 1
        seq = [(k[0], wk.notch((k[4] - k[1]) % P) > 0) for k in ks]
        g = [b[0] - a[0] for a, b in zip(seq, seq[1:])]
        f = [b[1] for b in seq[1:]]
        for gi in g:
            gaps[gi] += 1
        pairs += list(zip(g, f))
        gs = g[:]
        rng.shuffle(gs)
        shuffled += list(zip(gs, f))
    tot = sum(classes.values())
    report("KC at least 90% of departures in classes 32 and 52", (classes[32] + classes[52]) / tot >= 0.9,
           f"{classes[32] + classes[52]} of {tot}")
    peaks = []
    for x in range(60, 101):
        side = [gaps[y] for y in list(range(x - 10, x - 2)) + list(range(x + 3, x + 11))]
        m = sum(side) / len(side)
        if m and gaps[x] >= 1.2 * m and gaps[x] == max(gaps[y] for y in range(x - 2, x + 3)):
            peaks.append((x, gaps[x], round(m, 1)))
    print("   gap histogram (steps: count), 40 to 120 in steps of 4: "
          + " ".join(f"{x}:{sum(gaps[y] for y in range(x, x + 4))}" for x in range(40, 120, 4)), flush=True)
    verdict("G1 a local peak in the gaps between 60 and 100 steps", bool(peaks), f"peaks {peaks[:6]}")
    d = fwd_gap_link(pairs)
    verdict("G2 forward kicks are commoner after gaps of 70 to 90 steps, by at least 0.05", d >= 0.05,
            f"difference {d:+.3f} over {len(pairs)} consecutive pairs")
    dc = fwd_gap_link(shuffled)
    report("CF with gaps shuffled within each seed the link vanishes (within 0.03)", abs(dc) <= 0.03, f"{dc:+.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
