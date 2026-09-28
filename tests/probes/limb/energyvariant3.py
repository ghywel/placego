#!/usr/bin/env python3
"""The texture-energy channel, ENGINEERING form: the same smoothed statistic as energyvariant2.py's dense prototype
(a Gaussian, sigma 12 px, mean of the 2-px gradient magnitude), computed ONCE per frame instead of per coarse texel.

energyvariant2.py took each coarse and 1/8 texel's energy from 625 taps (x3 luma reads) and cost x4 the
recommendation. Here, per frame (A = HOOKED, B = NEXT), three small passes at QUARTER resolution:
    ENERGY_x_Q0   each 4 x 4 block's 2-px gradient magnitude on a dense 2 x 2 tap grid (12 luma reads)
    ENERGY_x_Q1   a horizontal Gaussian, sigma 3 quarter-res texels = 12 px, 13 taps
    ENERGY_x      the vertical pass
and the coarse (1/16) and 1/8 luma passes carry one bilinear sample of ENERGY_x in .g. The field is smooth at sigma 12,
so sampling it at 8- or 16-px texel centres does not alias. The coarse and 1/8 SADs, and the 1/8 level's
post-propagation data check, add W |dE| exactly as in the prototype.

    energyvariant3.py <in.glsl> <out.glsl> [W_S] [W_E]      (defaults 8, 1)"""
import sys

src, dst = sys.argv[1], sys.argv[2]
ws = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
we = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
t = open(src, encoding="utf-8").read()


def must(old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, f"{n} x (want {count}): {old[:90]!r}"
    t = t.replace(old, new)


sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))   # tests/
import coarse_energy  # noqa: E402  (the transform lives there, shared with gen_variational.py's COARSE_ENERGY=1)

t = coarse_energy.add(t, ws, we)
open(dst, "w", encoding="utf-8").write(t)
print(f"wrote {dst} (W_S {ws:g}, W_E {we:g}); passes {t.count('//!HOOK')}")
