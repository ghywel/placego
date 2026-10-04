#!/usr/bin/env python3
"""THE TRUST GATE'S DECISION, offline (2026-10-01, after R3): does a RELATIVE margin separate a real win from a tie?

    decide.py <out.txt> weave:<t0 workdir>:<speeds>  r3:<r3.raw>  ...

The GLSL form's decision, emulated per 1/8 cell (every second cell in x and y, every third frame from 4): the quarter
level's 13 x 13 offer (the 5 x 5 window's mean |a - b| plus 0.0005 per px) gives its three best distinct local minima at
whole quarter texels; each is refined over +-0.5 px in HALF-pixel steps on the 16 x 16 block centred on the cell at full
resolution (bilinear), as trust_gate.py does. The winner is the best; the runner-up is the best candidate more than 2 px
from it (a different basin). For every cell: is the winner right (within 2 px of the truth), and the RATIO
winner / runner-up. Sources: the weave box (weavesweep's sources in a leveltap workdir; the core 32+ px inside, truth
(v, 0)) and R3_rot_tex (r3diag.py's r3.raw; inside 130 px of the centre, truth the rigid rotation, frame k with k - 1).
Printed per source: the share of right winners, and the ratio's percentiles for right and for wrong winners; then for
candidate ratio thresholds, the right decisions kept and the wrong ones refused.
"""
import pathlib
import sys

import numpy as np

W, H = 1280, 720
R = 6
offs = [(dx, dy) for dy in range(-R, R + 1) for dx in range(-R, R + 1)]


def quarter(img):
    return (0.25 * (img[1::4, 1::4] + img[1::4, 2::4] + img[2::4, 1::4] + img[2::4, 2::4]))[:H // 4, :W // 4]


def bil(img, x, y):
    h, w = img.shape
    fx, fy = x - 0.5, y - 0.5
    x0 = np.floor(fx).astype(int); y0 = np.floor(fy).astype(int)
    ax, ay = fx - x0, fy - y0
    x0c, x1c = np.clip(x0, 0, w - 1), np.clip(x0 + 1, 0, w - 1); y0c, y1c = np.clip(y0, 0, h - 1), np.clip(y0 + 1, 0, h - 1)
    return (img[y0c, x0c] * (1 - ax) + img[y0c, x1c] * ax) * (1 - ay) + (img[y1c, x0c] * (1 - ax) + img[y1c, x1c] * ax) * ay


def cell_decision(A, B, qa, qb, cx, cy):
    """cx, cy: the 1/8 cell. Returns (winner px, winner score, runner-up score)"""
    qx, qy = 2 * cx, 2 * cy
    a25 = qa[qy - 2:qy + 3, qx - 2:qx + 3]
    if a25.shape != (5, 5): return None
    c = np.full((2 * R + 1, 2 * R + 1), np.inf)
    for dx, dy in offs:
        b25 = qb[qy - 2 + dy:qy + 3 + dy, qx - 2 + dx:qx + 3 + dx]
        if b25.shape == (5, 5): c[dy + R, dx + R] = np.abs(a25 - b25).mean() + 0.0005 * 4.0 * np.hypot(dx, dy)
    side = 2 * R + 1
    pad = np.pad(c, 1, constant_values=np.inf)
    nb = np.min(np.stack([pad[1 + j:1 + j + side, 1 + i:1 + i + side] for j in (-1, 0, 1) for i in (-1, 0, 1) if i or j]), 0)
    mins = sorted((c[j, i], i - R, j - R) for j in range(side) for i in range(side) if np.isfinite(c[j, i]) and c[j, i] <= nb[j, i])
    picked = []
    for _, i, j in mins:
        if all(max(abs(i - p[0]), abs(j - p[1])) >= 2 for p in picked): picked.append((i, j))
        if len(picked) == 3: break
    by, bx = np.mgrid[-8:8, -8:8]
    ya, xa = cy * 8 + 4 + by, cx * 8 + 4 + bx
    if ya.min() < 0 or xa.min() < 0 or ya.max() >= H or xa.max() >= W: return None
    blk = A[ya, xa]
    cands = []
    for i, j in picked:
        best = (np.inf, None)
        for ry in (-0.5, 0.0, 0.5):
            for rx in (-0.5, 0.0, 0.5):
                d = (4 * i + rx, 4 * j + ry)
                s = np.abs(blk - bil(B, xa + 0.5 + d[0], ya + 0.5 + d[1])).mean()
                if s < best[0]: best = (s, d)
        cands.append(best)
    cands.sort(key=lambda z: z[0])
    win = cands[0]
    ru = min((s for s, d in cands[1:] if max(abs(d[0] - win[1][0]), abs(d[1] - win[1][1])) > 2.0), default=np.inf)
    return np.array(win[1]), win[0], ru


def run(name, frames, truth, region):
    rows = []
    for k in range(4, len(frames) - 1, 3):
        A, B = frames[k], frames[k + 1]
        qa, qb = quarter(A), quarter(B)
        for cy in range(2, H // 8 - 2, 2):
            for cx in range(2, W // 8 - 2, 2):
                if not region(k, cx, cy): continue
                r = cell_decision(A, B, qa, qb, cx, cy)
                if r is None: continue
                d, s, ru = r
                tr = truth(k, cx, cy)
                rows.append((float(np.hypot(*(d - tr)) <= 2.0), s / ru if np.isfinite(ru) else 0.0))
    a = np.array(rows)
    right, ratio = a[:, 0] > 0.5, a[:, 1]
    q = lambda x: " ".join(f"{v:.2f}" for v in np.percentile(x, [5, 25, 50, 75, 95])) if len(x) else "--"
    print(f"{name:14s} cells {len(a):6d}  winner right {100 * right.mean():5.1f}%   ratio (5/25/50/75/95): "
          f"right {q(ratio[right])} | wrong {q(ratio[~right])}", flush=True)
    return right, ratio


out = []
for spec in sys.argv[2:]:
    kind, rest = spec.split(":", 1)
    if kind == "weave":
        wd, speeds = rest.rsplit(":", 1)
        for v in [float(x) for x in speeds.split(",")]:
            fr = np.fromfile(pathlib.Path(wd) / f"src-weave-{v:g}.raw", "<u2").reshape(-1, H, W).astype(np.float64) / 65535.0
            reg = lambda k, cx, cy, v=v: (cx * 8 + 4 > 40 + v * k + 32) and (cx * 8 + 4 < 40 + v * k + 320 - 32) and (259 + 32 < cy * 8 + 4 < 259 + 202 - 32)
            out.append((f"weave {v:g}",) + run(f"weave {v:g}", fr, lambda k, cx, cy, v=v: np.array([v, 0.0]), reg))
    elif kind == "r3":
        fr = np.fromfile(rest, "<u2").reshape(-1, H, W).astype(np.float64) / 65535.0

        def tr(k, cx, cy):                                      # the pair (k, k + 1) here: A = frame k, B = frame k + 1
            dx, dy = cx * 8 + 4.5 - 640.0, cy * 8 + 4.5 - 360.0
            t0, t1 = 2.56 * (k / 24.0) ** 2, 2.56 * ((k + 1) / 24.0) ** 2
            c, s = np.cos(t0 - t1), np.sin(t0 - t1)
            return np.array([c * dx + s * dy - dx, -s * dx + c * dy - dy])
        reg = lambda k, cx, cy: np.hypot(cx * 8 + 4.5 - 640, cy * 8 + 4.5 - 360) < 130
        out.append(("R3",) + run("R3", fr, tr, reg))
with open(sys.argv[1], "w") as f:
    print(f"\n{'threshold':>9s} | " + " | ".join(f"{n:>14s}" for n, _, _ in out) + "   (right kept / wrong refused, percent)")
    for th in (0.95, 0.9, 0.8, 0.7, 0.6, 0.5):
        cells = []
        for n, right, ratio in out:
            keep = ratio < th
            cells.append(f"{100 * (keep & right).sum() / max(right.sum(), 1):5.1f} / {100 * (~keep & ~right).sum() / max((~right).sum(), 1):5.1f}")
        line = f"{th:9.2f} | " + " | ".join(f"{c:>14s}" for c in cells)
        print(line); f.write(line + "\n")
