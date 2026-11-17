"""ENERGY-TRANSFER.md stage 0d: the carry's ANCHORS on the weave -- is the truth the best basin at the box's edge?

    anchors.py <clip>:<v px/frame> [...]      (clips in np-scratch, weavesweep.py's sources wrapped as ffv1)

The 1/8 level emulated exactly as tests/probes/limb/ambiguity.py emulates it (the carry's offline twin: luma at each
1/8 texel's centre, 5 x 5 SAD, every integer shift within +-3 texels, a rival behind a ridge, the margin). For the
translating box (x0 = 40 + v k, y0 = 259, 320 x 202; the truth (0, v/8) texels), per cell:
  - TRUTH: the best shift within half a texel of the truth;
  - ALIAS: the best shift anywhere else;
  - an ANCHOR (the carry's word): a textured cell with no rival or a margin of at least 0.05, the carry's TAU. These
    are the cells the carry carries FROM.
Edge cells: centre inside the box and within 16 px of its boundary. Interior: more than 32 px inside. Every other
frame of 2-19. Numbers only.
"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1] / "limb"))
import ambiguity as AM                                                            # noqa: E402
import limblevels as LL                                                           # noqa: E402

BW, BH, X0, Y0 = 320, 202, 40.0, 259.0
print(f"{'clip':22s} {'cells':>6s} | {'edge: truth / alias / anchors (truth among them)':>52s} | {'interior: truth / alias / anchors (truth)':>46s}")
for spec in sys.argv[1:]:
    f, v = spec.rsplit(":", 1); v = float(v)
    fr = AM.clip_frames(LL.NP / f, 0.0)
    tally = {g: np.zeros(4) for g in ("edge", "int")}                         # cells, truth, alias, anchors-with-truth / anchors
    anch = {g: np.zeros(2) for g in ("edge", "int")}
    for k in range(2, 19, 2):
        m, rg, d1y, d1x = AM.analyse(fr, k)
        H8, W8 = m.shape
        cy, cx = np.mgrid[0:H8, 0:W8].astype(np.float64) * 8 + 4.0            # the 1/8 texel's centre (a pixel corner)
        x0 = X0 + v * k
        inside = (cx > x0) & (cx < x0 + BW) & (cy > Y0) & (cy < Y0 + BH)
        dist = np.minimum.reduce([cx - x0, x0 + BW - cx, cy - Y0, Y0 + BH - cy])
        tex = rg >= 0.02
        truth = (np.abs(d1x - v / 8) <= 0.5) & (d1y == 0)
        anchor = tex & (m >= 0.05)
        for g, sel in (("edge", inside & (dist <= 16) & tex), ("int", inside & (dist > 32) & tex)):
            tally[g] += [sel.sum(), (sel & truth).sum(), (sel & ~truth).sum(), 0]
            anch[g] += [(sel & anchor).sum(), (sel & anchor & truth).sum()]
    def cell(g):
        n, tr, al, _ = tally[g]; na, nat = anch[g]
        return f"{100 * tr / max(n, 1):5.1f}% / {100 * al / max(n, 1):5.1f}% / {100 * na / max(n, 1):5.1f}% ({100 * nat / max(na, 1):5.1f}%)"
    print(f"{f.split('/')[-1][:20] + ' ' + str(int(v)):22s} {int(tally['edge'][0] + tally['int'][0]):6d} | {cell('edge'):>52s} | {cell('int'):>46s}", flush=True)
