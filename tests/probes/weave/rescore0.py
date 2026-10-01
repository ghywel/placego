"""NFRAME-LIMITS, the weave, lead 4's step 0: at a FINE level, does the truth out-score the print's aliases?

    rescore0.py [speeds=5,11,13,19] [textures=weave,noise]

weavesweep.py's sources (np-scratch/weave/sweep/src-<tex>-<v>.raw, 1280 x 720 x 48, 16-bit): the translating box. For
16 x 16 blocks of its core (32+ px inside), frames 10-30, the mean |S_k - S_k+1(shifted)| at the truth (v, 0) and at
the print's aliases (v +- 28, 0), (v +- 14, +-14), (v, +-28); at full resolution (integer shifts) and at 1/2 (2 x 2
averages, shifts halved). Per block: is the truth the lowest, and the margin (the nearest alias minus the truth).
Numbers only.
"""
import os
import pathlib
import sys

import numpy as np

W, H, N = 1280, 720, 48
BW, BH, X0, Y0 = 320, 202, 40.0, 259.0
SP = [float(s) for s in (sys.argv[1] if len(sys.argv) > 1 else "5,11,13,19").split(",")]
TX = (sys.argv[2] if len(sys.argv) > 2 else "weave,noise").split(",")
# weavesweep.py's sources: $NP_SCRATCH/weave/sweep, NP_SCRATCH defaulting to np-scratch beside the repository checkout
NP = pathlib.Path(os.environ.get("NP_SCRATCH", str(pathlib.Path(__file__).resolve().parents[5] / "np-scratch")))
D = str(NP / "weave/sweep")
ALIASES = [(28, 0), (-28, 0), (14, 14), (14, -14), (-14, 14), (-14, -14), (0, 28), (0, -28)]


def half(img):
    return 0.25 * (img[0::2, 0::2] + img[1::2, 0::2] + img[0::2, 1::2] + img[1::2, 1::2])


print(f"{'tex':6s} {'v':>3s} | {'full res: truth lowest / median margin':>40s} | {'1/2 res: truth lowest / median margin':>40s}")
for tex in TX:
    for v in SP:
        S = np.fromfile(f"{D}/src-{tex}-{v:g}.raw", "<u2").reshape(N, H, W).astype(np.float32) / 65535.0
        res = {}
        for lvl, sc in (("full", 1), ("half", 2)):
            wins, margins = 0, []
            for k in range(10, 31):
                a, b = (S[k], S[k + 1]) if sc == 1 else (half(S[k]), half(S[k + 1]))
                x0 = (X0 + v * k) / sc; y0 = Y0 / sc; bs = 16 // sc; inset = 32 // sc
                for by in range(int(y0 + inset), int(y0 + BH / sc - inset - bs), bs):
                    for bx in range(int(x0 + inset), int(x0 + BW / sc - inset - bs), bs):
                        blk = a[by:by + bs, bx:bx + bs]
                        def cost(dx, dy):
                            # EXACT shifts: integer at full resolution; bilinear sub-texel at 1/2 (an odd speed is a
                            # half texel there, and rounding would score the truth and the aliases unequally)
                            fx, fy = dx / sc, dy / sc
                            ix, iy = int(np.floor(fx)), int(np.floor(fy)); ax_, ay_ = fx - ix, fy - iy
                            y, x = by + iy, bx + ix
                            if y < 0 or x < 0 or y + bs + 1 > b.shape[0] or x + bs + 1 > b.shape[1]: return np.inf
                            p = ((1 - ax_) * (1 - ay_) * b[y:y + bs, x:x + bs] + ax_ * (1 - ay_) * b[y:y + bs, x + 1:x + bs + 1]
                                 + (1 - ax_) * ay_ * b[y + 1:y + bs + 1, x:x + bs] + ax_ * ay_ * b[y + 1:y + bs + 1, x + 1:x + bs + 1])
                            return float(np.mean(np.abs(blk - p)))
                        ct = cost(v, 0)
                        ca = [cost(v + ax, ay) for ax, ay in ALIASES]
                        ca = [c for c in ca if np.isfinite(c)]
                        if not ca: continue
                        wins += int(ct < min(ca)); margins.append(min(ca) - ct)
            res[lvl] = (100 * wins / max(len(margins), 1), float(np.median(margins)) if margins else float("nan"), len(margins))
        f = lambda l: f"{res[l][0]:5.1f}% / {res[l][1]:+.4f} ({res[l][2]} blocks)"
        print(f"{tex:6s} {v:3.0f} | {f('full'):>40s} | {f('half'):>40s}", flush=True)
