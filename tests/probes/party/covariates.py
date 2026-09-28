"""What sets the field's agreement with Vision on real bodies (reads velocity.py's rows; bone midpoints only).

The hypothesis under test (after P1 read 0.5-0.7 where synthetic scenes read 0.97): a coarse-to-fine blind spot. At
the coarse search a child's limb is about one texel wide, so a thin limb moving against a still background is seeded
with the background's zero and the refinement cannot reach it. If so:
  - H1: the gain rises with the child's size in the picture (the body ruler, px), at the same speed;
  - H2: the gain falls with the SCALE-FREE speed (displacement per frame in rulers), at the same size;
  - H3: the magnitude, not the direction, carries the loss (|f|/|d| well under 1 while the angle error is modest).
    covariates.py              the tables (1 Hz records; --crossings for the crossing runs, --all for both)"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

a = np.load(pd.NP / "party-analysis" / "velocity.npz")["rows"]
si, t, burst, r, jn, ca, cb, dx, dy, fx, fy, still = a.T
sel = (jn >= 100) & np.isfinite(r)
sel &= (burst == 1) if "--crossings" in sys.argv else ((burst == 0) if "--all" not in sys.argv else True)
sp = np.hypot(dx, dy)
fsp = np.hypot(fx, fy)
gain = (fx * dx + fy * dy) / np.maximum(sp * sp, 1e-9)
ratio = fsp / np.maximum(sp, 1e-9)
ang = np.degrees(np.abs(np.arctan2(fx * dy - fy * dx, fx * dx + fy * dy)))
rel = sp / np.maximum(r, 1)                      # displacement per frame in body rulers

limbs = np.isin(jn, [pd.BONE_IDS[b] for b in ("upperArmL", "upperArmR", "forearmL", "forearmR")])
print(f"rows {int(sel.sum())} (bone midpoints; {'crossings' if '--crossings' in sys.argv else '1 Hz' if '--all' not in sys.argv else 'all'})")


def cell(m):
    n = int(m.sum())
    return f"{np.median(gain[m]):5.2f} ({n:5d})" if n >= 20 else "    -       "


RB = [(0, 60), (60, 90), (90, 130), (130, 200), (200, 2000)]
SB = [(4, 8), (8, 16), (16, 32), (32, 64)]
print("\nH1: gain p50 (n) by body ruler (rows) x speed px/frame (columns), arms")
print("ruler px    " + "".join(f"{lo:>3}-{hi:<3} px/f      " for lo, hi in SB))
for lo, hi in RB:
    m0 = sel & limbs & (r >= lo) & (r < hi)
    print(f"{lo:4}-{hi:<5}   " + "  ".join(cell(m0 & (sp >= s0) & (sp < s1)) for s0, s1 in SB))

QB = [(0.02, 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 0.4), (0.4, 1.0)]
print("\nH2: by scale-free speed (displacement per frame / ruler), every bone group; gain p50 (n)")
print("group        " + "".join(f"{lo:.2f}-{hi:.2f}      " for lo, hi in QB))
for g, bs in pd.BONE_GROUPS.items():
    m0 = sel & np.isin(jn, [pd.BONE_IDS[b] for b in bs]) & (sp >= 3)
    print(f"{g:12} " + "  ".join(cell(m0 & (rel >= q0) & (rel < q1)) for q0, q1 in QB))

print("\nH3: magnitude vs direction, arms at 8-32 px/frame, by ruler")
for lo, hi in RB:
    m = sel & limbs & (r >= lo) & (r < hi) & (sp >= 8) & (sp < 32)
    if m.sum() >= 20:
        print(f"  ruler {lo:4}-{hi:<5}: |f|/|d| p50 {np.median(ratio[m]):.2f}  angle p50 {np.median(ang[m]):5.1f} deg  "
              f"gain p50 {np.median(gain[m]):.2f}  under-read (|f|<0.5|d|) {100 * (ratio[m] < 0.5).mean():4.1f}%  n {int(m.sum())}")
