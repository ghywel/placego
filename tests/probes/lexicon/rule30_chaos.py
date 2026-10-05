#!/usr/bin/env python3
"""rule30_chaos.py: is the wheel chaotic? The owner's question (2026-10-05): "Could the wheel be chaotic, like a
double pendulum?"

RUN-ON:     cpu (pure Python 3, standard library; exact, with seeded random right halves)
COMMAND:    python3 tests/probes/lexicon/rule30_chaos.py [N=1500] [T=4096]
COST:       about ten minutes on one core.

The picture so far: between kicks the wheel is an exact periodic rotation, so it is not chaotic in itself. The walls
that kick it come from the right side's interior, which is Rule 30's chaos. A double pendulum is chaotic in its own
variables: nearby starts part exponentially. The wheel's angle has no restoring force (section 8.9), so it is a
neutral coordinate, and nearby starts should part only like a random walk. Four tests:
  sensitivity  N seeded random right halves of 64 cells; the same with the cell at position 48 flipped. Column 1
               cannot change before time 47 (the light cone). After that the two wheels' angles are compared, both
               unwrapped from their last common exact window (as in rule30_wheelspeed.py).
  divergence   the mean squared angle difference against the time since divergence.
  memory       within one column 1, consecutive kicks (angle changes between exact windows, in notches).
  noise engine (the random-chaos step) columns 0..12 run by Rule 30 with column 0 clamped to 0101..., and column 13
               replaced by fresh coin flips at every step.

PREDICTIONS, written 2026-10-05 before this script's first run:
  C  (control, exact: the light cone): with the flip at position 48, column 1 is identical up to time 46 in every pair.
  D1 (blind): in at least 90% of pairs whose wheels are both exact in some window after time 1000, the angles differ
     there: the flip moves the wheel for good.
  D2 (blind): the mean squared angle difference grows as s^g with g in [0.7, 1.3] over s = 1..32 windows after the last
     common window (diffusive, as for a neutral angle, not exponential as for a double pendulum).
  D3 (blind): the kicks have no memory. The correlation between consecutive kicks lies in [-0.2, 0.2], and knowing the
     previous kick leaves at least 90% of the next kick's entropy.
  N1 (blind): with the noise engine the same wheel forms. At least 3% of windows are exact rotations of U, and among
     its kicks both signs occur, each in at least 20% of kicks.
REFUTED-BY: C failing (the harness); D1, D2, D3 or N1 failing.
"""
import math, random, sys, pathlib
from collections import Counter

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
T = int(sys.argv[2]) if len(sys.argv) > 2 else 4096
P, FLIP = 56, 48

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
ROT = {tuple(U[(t - d) % P] for t in range(P)): d for d in range(P)}
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column1(R, n):
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = R << 1, []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return out


def noise_column1(rng, n, width=13):
    """Columns 0..width-1 by Rule 30, column 0 clamped to 0101..., column `width` fresh coin flips every step."""
    mask = (1 << (width + 1)) - 1
    row, out = 0, []
    for t in range(n):
        row = (row & ~(1 << width)) | (rng.getrandbits(1) << width)
        out.append((row >> 1) & 1)
        new = ((row << 1) ^ (row | (row >> 1))) & mask
        row = (new & ~1 & ~(1 << width)) | ((t + 1) % 2)
    return out


def notch(delta):
    k = (-17 * delta) % P
    k = k - P if k > P // 2 else k
    return k // 2


def angles(c):
    """Exact windows' phases, and the unwrapped angle (notches) at each exact window, starting from 0."""
    ph = [ROT.get(tuple(c[k * P:(k + 1) * P])) for k in range(len(c) // P)]
    ex = [(k, d) for k, d in enumerate(ph) if d is not None]
    A, kicks, a = {}, [], 0
    if ex:
        A[ex[0][0]] = 0
    for (k, d), (k2, d2) in zip(ex, ex[1:]):
        n = notch((d2 - d) % P)
        kicks.append(n)
        a += n
        A[k2] = a
    return ph, A, kicks


def main():
    rng = random.Random(1914)
    pairs, light_bad, moved, moved_n = [], 0, 0, 0
    sq = Counter()
    sqn = Counter()
    all_kicks = []
    for _ in range(N):
        R = rng.getrandbits(64) | (1 << 63)
        c1 = column1(R, T)
        c2 = column1(R ^ (1 << (FLIP - 1)), T)            # bit FLIP-1 is the cell at position FLIP
        light_bad += c1[:FLIP - 1] != c2[:FLIP - 1]
        ph1, A1, k1 = angles(c1)
        ph2, A2, _ = angles(c2)
        all_kicks.append(k1)
        common = [k for k in range(len(ph1)) if ph1[k] is not None and ph1[k] == ph2[k] and
                  c1[k * P:(k + 1) * P] == c2[k * P:(k + 1) * P]]
        late = [k for k in range(1000 // P + 1, len(ph1)) if ph1[k] is not None and ph2[k] is not None]
        if late:
            moved_n += 1
            moved += any(ph1[k] != ph2[k] for k in late)
        # divergence: anchor at the last window where both are exact at the same phase before the paths split
        split = next((k for k in range(len(ph1)) if c1[k * P:(k + 1) * P] != c2[k * P:(k + 1) * P]), None)
        if split is None:
            continue
        anchors = [k for k in common if k < split]
        if not anchors:
            continue
        k0 = anchors[-1]
        for k in range(k0 + 1, len(ph1)):
            if k in A1 and k in A2 and k0 in A1 and k0 in A2:
                d = (A1[k] - A1[k0]) - (A2[k] - A2[k0])
                s = k - k0
                if s <= 32:
                    sq[s] += d * d
                    sqn[s] += 1
    report("C the light cone: column 1 unchanged up to time 46 in every pair", light_bad == 0,
           f"{light_bad} pairs changed early, of {N}")
    verdict("D1 the flip moves the wheel for good (angles differ after time 1000 in at least 90%)",
            moved_n > 0 and moved / moved_n >= 0.90, f"{moved} of {moved_n}")
    xs = [(s, sq[s] / sqn[s]) for s in range(1, 33) if sqn[s] >= 30 and sq[s] > 0]
    if len(xs) >= 3:
        lx = [math.log(s) for s, _ in xs]
        ly = [math.log(v) for _, v in xs]
        mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
        g = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    else:
        g = float("nan")
    verdict("D2 the angles part diffusively: mean squared difference grows as s^g, g in [0.7, 1.3]", 0.7 <= g <= 1.3,
            f"g = {g:.2f}; " + ", ".join(f"s {s}: {v:.1f}" for s, v in xs[:8]))

    pairs_k = [(a, b) for ks in all_kicks for a, b in zip(ks, ks[1:])]
    if pairs_k:
        ma = sum(a for a, _ in pairs_k) / len(pairs_k)
        mb = sum(b for _, b in pairs_k) / len(pairs_k)
        va = sum((a - ma) ** 2 for a, _ in pairs_k) / len(pairs_k)
        vb = sum((b - mb) ** 2 for _, b in pairs_k) / len(pairs_k)
        r = sum((a - ma) * (b - mb) for a, b in pairs_k) / len(pairs_k) / math.sqrt(va * vb) if va and vb else 0.0
        joint = Counter(pairs_k)
        nxt = Counter(b for _, b in pairs_k)
        prv = Counter(a for a, _ in pairs_k)
        n = len(pairs_k)
        H = -sum(v / n * math.log2(v / n) for v in nxt.values())
        Hc = -sum(v / n * math.log2(v / prv[a]) for (a, _), v in joint.items())
        keep = Hc / H if H else 1.0
    else:
        r, keep = float("nan"), float("nan")
    verdict("D3 the kicks have no memory (correlation in [-0.2, 0.2], at least 90% of the entropy left)",
            -0.2 <= r <= 0.2 and keep >= 0.90, f"correlation {r:+.3f}; entropy kept {keep:.1%} over {len(pairs_k)} pairs")

    nrng = random.Random(1915)
    exact = windows = 0
    kicks = []
    for _ in range(200):
        c = noise_column1(nrng, T)
        ph, _, k = angles(c)
        windows += len(ph)
        exact += sum(d is not None for d in ph)
        kicks += k
    pos = sum(1 for k in kicks if k > 0) / len(kicks) if kicks else 0.0
    neg = sum(1 for k in kicks if k < 0) / len(kicks) if kicks else 0.0
    verdict("N1 with the noise engine the same wheel forms, kicked both ways",
            exact / windows >= 0.03 and pos >= 0.20 and neg >= 0.20,
            f"exact U windows {exact / windows:.1%}; kicks forward {pos:.0%}, backward {neg:.0%}; commonest "
            + ", ".join(f"{k:+d} x{v}" for k, v in Counter(kicks).most_common(6)))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
