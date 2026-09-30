"""ENERGY-TRANSFER.md 3.1, the free first look: do the saved per-frame picture scores dip at the bounces?

    impactdips.py <batch dir, e.g. np-scratch/ladder2/batch1/textured> [scenes=bounce-constant,bounce-gravity,...]

The master tier (2026-09-12) kept, for every scene and shader, the per-frame PSNR of the 24 -> 60 output against
the truth (<scene>/<stem>[_<host>].psnr, 240 frames), not the pictures. The wall hits are exact in the scene's own
closed form (masters.py's trajectory(): the segment start times, in source frames). Output frame n (1-based) samples
law time (n - 1) * 24 / 60. Each output frame is binned by its distance to the nearest wall hit, in source frames,
and the median PSNR per bin is printed for hold, linear and every shader on each host. A corner-cutting family
shows a dip in the 0-0.5 bin that hold and linear show too, and that the smooth frames do not.

This is a proxy, not the step's measure: 3.1 pre-registered the miss DISTANCE of the drawn ball at the wall, which
needs the pictures. It says whether the effect is there and how large, before a render is spent on it.
"""
import math
import pathlib
import re
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import masters                                                              # noqa: E402  (tests/masters.py)

batch = pathlib.Path(sys.argv[1])
scenes = (sys.argv[2] if len(sys.argv) > 2 else "bounce-constant,bounce-gravity,bounce-masses,bounce-hardjerk").split(",")
W, H = 1280, 720
table = {name: (kind, p) for name, kind, p, *_ in masters.masters(W, H)}
BINS = [(0, 0.5), (0.5, 1), (1, 2), (2, 99)]

for name in scenes:
    kind, b = table[name]
    segs = masters.trajectory(b, float(W), float(H))
    hits = np.array([sg[0] for sg in segs[1:]])                                # each segment after the first starts at a wall
    d = pathlib.Path(batch) / name
    files = sorted(d.glob("*.psnr"))
    print(f"\n# {name}: {len(hits)} wall hits in {b.frames} source frames (first {', '.join(f'{h:.2f}' for h in hits[:4])} ...)")
    print(f"{'stem':62s} " + " ".join(f"{f'{lo}-{hi}':>8s}" for lo, hi in BINS) + "   dip")
    for f in files:
        vals = []
        for line in f.read_text().splitlines():
            m = re.match(r"n:(\d+) .*psnr_y:([\d.inf]+)", line)
            if m: vals.append((int(m.group(1)), float(m.group(2))))
        if not vals: continue
        n = np.array([v[0] for v in vals]); ps = np.array([v[1] for v in vals])
        t = (n - 1) * 24 / 60
        keep = (n > 5) & np.isfinite(ps) & (ps < 99)                          # analyze.py's rule: past the first five
        dist = np.array([np.min(np.abs(hits - x)) if len(hits) else 99 for x in t])
        med = []
        for lo, hi in BINS:
            sel = keep & (dist >= lo) & (dist < hi)
            med.append(np.median(ps[sel]) if sel.any() else math.nan)
        print(f"{f.stem:62s} " + " ".join(f"{m:8.2f}" for m in med) + f"   {med[0] - med[-1]:+6.2f}")
