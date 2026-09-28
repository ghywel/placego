#!/usr/bin/env python3
"""limblevels.py's per-level view for any ladder case that is a rectangle moving by a known law over a still background
(scenes.sh's _rect cases: the V/H period series among them). Scored inside the rectangle at frame A.

    rectlevels.py <shader.glsl> <case> <x-law> <y-law> <w> <h> [<case> ...]
        laws in t seconds, as scenes.sh writes them, e.g.  V3_stairs_sq24_v12 490 '100+288*t' 300 300
Per level: the gain along the true motion (median over the rectangle's interior cells), the share lost (< 0.5), the share
held (within 20%), the share pointing the WRONG way (gain < -0.2, the alias's signature), over the 24-frame clip."""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import limblevels as LL  # noqa: E402

shader = pathlib.Path(sys.argv[1])
LL.SHADER = shader
LL.dumps()
args = sys.argv[2:]
while args:
    case, xl, yl, w, h = args[:5]
    args = args[5:]
    w, h = int(w), int(h)
    pos = lambda law, k: int(round(eval(law, {"t": k / 24.0})))
    print(f"\n== {case} ({shader.name}): per level, in the rectangle")
    print("level   gain p50   lost   held   reversed")
    for tag, _, _ in LL.LEVELS:
        f = LL.render(case, tag)
        g_all = []
        for k in range(3, f.shape[0] - 2):
            xa, ya, xb, yb = pos(xl, k), pos(yl, k), pos(xl, k + 1), pos(yl, k + 1)
            d = np.array([xb - xa, yb - ya], float)
            if np.hypot(*d) < 0.5 or xa < 0 or ya < 0 or xa + w > LL.W or ya + h > LL.H:
                continue
            cells = f[k, ya + 8:ya + h - 8:4, xa + 8:xa + w - 8:4].reshape(-1, 2)
            with np.errstate(all="ignore"):              # macOS Accelerate raises spurious FP flags in matmul
                g_all.append(cells.astype(np.float64) @ d / (d @ d))
        g = np.concatenate(g_all)
        print(f"{tag:6}  {np.median(g):8.2f}  {100 * np.mean(g < 0.5):5.1f}%  {100 * np.mean(np.abs(g - 1) < 0.2):5.1f}%  "
              f"{100 * np.mean(g < -0.2):6.1f}%")
