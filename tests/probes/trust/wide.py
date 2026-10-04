#!/usr/bin/env python3
"""THE PER-LEVEL TRUST GATE, step T2 offline (2026-10-01): the first honest level's wide search, emulated.

    wide.py <t0 workdir> [speeds=3,5,11,13,15,16,17,19] [textures=weave,noise] [lambdas=0,0.0005,0.002,0.008]

Reads leveltap.py's box sources (src-<tex>-<v>.raw, gray16le 1280 x 720, 48 frames). Builds the quarter level as the
shader does (the point sample: the 2 x 2 pixels at each texel's centre) and, for every quarter texel of the box's core
(32+ px inside) on frames 10..37, searches EVERY whole-texel offset within +-6 texels (+-24 px; 13 x 13 = 169): the
cost is the 5 x 5 window's mean absolute difference plus lambda times the offset's length in px (the small-motion
prior), and the best is refined by a parabola in x and y. Reported per speed and lambda: the share of texels within
2 px of the truth (v, 0), the gross share (more than 2 px off), the share on a TRUE ALIAS of the weave (the truth
plus a lattice vector, (14, 14) and (14, -14) as the basis, within 2 px) -- which the lattice re-score can then turn
into the truth -- and the commonest vectors. Numbers only.

RANK=full (T2b): the quarter level only OFFERS candidates. Its three best DISTINCT minima (local minima of the 13 x 13
cost surface, at least 2 texels apart, each refined by its parabola) are ranked at FULL resolution: the 16 x 16 block
centred on the texel, the mean absolute difference against frame k + 1 sampled bilinearly at the candidate, refined
over +-0.5 px in quarter-pixel steps; the lowest wins. Every second texel in x and y, every third frame (the cost).
"""
import os
import pathlib
import sys

import numpy as np

work = pathlib.Path(sys.argv[1])
SPEEDS = [float(s) for s in (sys.argv[2] if len(sys.argv) > 2 else "3,5,11,13,15,16,17,19").split(",")]
TEXS = (sys.argv[3] if len(sys.argv) > 3 else "weave,noise").split(",")
LAMS = [float(x) for x in (sys.argv[4] if len(sys.argv) > 4 else "0,0.0005,0.002,0.008").split(",")]
W, H, N = 1280, 720, 48
BW, BH, X0, Y0 = 320, 202, 40.0, 259.0
R = 6                                                  # +-6 quarter texels
offs = [(dx, dy) for dy in range(-R, R + 1) for dx in range(-R, R + 1)]


def quarter(img):
    q = 0.25 * (img[1::4, 1::4] + img[1::4, 2::4] + img[2::4, 1::4] + img[2::4, 2::4])
    return q[:H // 4, :W // 4]


def win_mean(a, r=2):
    c = np.pad(a, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    h, w = a.shape
    y0 = np.clip(np.arange(h) - r, 0, h); y1 = np.clip(np.arange(h) + r + 1, 0, h)
    x0 = np.clip(np.arange(w) - r, 0, w); x1 = np.clip(np.arange(w) + r + 1, 0, w)
    return (c[y1][:, x1] - c[y0][:, x1] - c[y1][:, x0] + c[y0][:, x0]) / ((y1 - y0)[:, None] * (x1 - x0)[None, :])


def shifted(b, dx, dy):
    """b sampled at (x + dx, y + dy), edge-clamped"""
    h, w = b.shape
    ys = np.clip(np.arange(h) + dy, 0, h - 1); xs = np.clip(np.arange(w) + dx, 0, w - 1)
    return b[ys][:, xs]


RANK = os.environ.get("RANK") == "full"


def bil(img, x, y):
    """img sampled at continuous pixel coordinates (pixel centres at i + 0.5), arrays x, y"""
    h, w = img.shape
    fx, fy = x - 0.5, y - 0.5
    x0 = np.floor(fx).astype(int); y0 = np.floor(fy).astype(int)
    ax, ay = fx - x0, fy - y0
    x0c, x1c = np.clip(x0, 0, w - 1), np.clip(x0 + 1, 0, w - 1); y0c, y1c = np.clip(y0, 0, h - 1), np.clip(y0 + 1, 0, h - 1)
    return ((img[y0c, x0c] * (1 - ax) + img[y0c, x1c] * ax) * (1 - ay) + (img[y1c, x0c] * (1 - ax) + img[y1c, x1c] * ax) * ay)


def rank_full(A, B, costs, qxs, qys):
    """for each texel: the 3 best distinct local minima of its 13 x 13 surface, ranked by full-resolution SAD"""
    side = 2 * R + 1
    out = []
    by_, bx_ = np.mgrid[-8:8, -8:8]
    for qx, qy in zip(qxs, qys):
        c = costs[:, qy, qx].reshape(side, side)
        pad = np.pad(c, 1, constant_values=np.inf)
        nb = np.min(np.stack([pad[1 + dy:1 + dy + side, 1 + dx:1 + dx + side] for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                              if dx or dy]), axis=0)
        mins = [(c[j, i], i - R, j - R) for j in range(side) for i in range(side) if c[j, i] <= nb[j, i]]
        mins.sort()
        picked = []
        for cc, i, j in mins:
            if all(max(abs(i - p[0]), abs(j - p[1])) >= 2 for p in picked): picked.append((i, j))
            if len(picked) == 3: break
        cx, cy = qx * 4 + 2.0, qy * 4 + 2.0
        ya, xa = cy + by_ + 0.5 - 0.5, cx + bx_ + 0.5 - 0.5
        blk = A[(ya).astype(int), (xa).astype(int)]
        best, bu = 1e9, (0.0, 0.0)
        for i, j in picked:
            for ry in np.arange(-0.5, 0.51, 0.25):
                for rx in np.arange(-0.5, 0.51, 0.25):
                    dx, dy = 4 * i + rx, 4 * j + ry
                    sc = np.abs(blk - bil(B, xa + 0.5 + dx, ya + 0.5 + dy)).mean()
                    if sc < best: best, bu = sc, (dx, dy)
        out.append(bu)
    return np.array(out, dtype=np.float64).reshape(-1, 2)


def is_alias(u, v, tol=2.0):
    """u: (n, 2) vectors; is u - (v, 0) a lattice vector of the weave (basis (14, 14), (14, -14))?"""
    d = u - np.array([v, 0.0])
    a = (d[:, 0] + d[:, 1]) / 28.0; b = (d[:, 0] - d[:, 1]) / 28.0      # d = a (14, 14) + b (14, -14)
    ra, rb = np.round(a), np.round(b)
    back = np.stack([14 * (ra + rb), 14 * (ra - rb)], axis=1)
    return np.hypot(*(d - back).T) <= tol


print(f"{'tex':6s} {'v':>3s} {'lambda':>7s} | {'right':>6s} {'gross':>6s} {'alias':>6s} | commonest (px: share)")
for tex in TEXS:
    for v in SPEEDS:
        src = work / f"src-{tex}-{v:g}.raw"
        if not src.exists():
            print(f"{tex:6s} {v:3g}  (no source; run leveltap.py at this speed first)"); continue
        fr = np.fromfile(src, "<u2").reshape(-1, H, W).astype(np.float64) / 65535.0
        for lam in LAMS:
            us = []
            for k in range(10, 38):
                a, b = quarter(fr[k]), quarter(fr[k + 1])
                costs = np.stack([win_mean(np.abs(a - shifted(b, dx, dy))) + lam * 4.0 * np.hypot(dx, dy)
                                  for dx, dy in offs])                     # (169, h, w)
                i = costs.argmin(0)
                bx = np.array([o[0] for o in offs])[i].astype(np.float64)
                by = np.array([o[1] for o in offs])[i].astype(np.float64)
                # the parabola in x and y around the best whole offset (inside the grid only)
                def cost_at(dx, dy):
                    j = (np.clip(dy, -R, R) + R) * (2 * R + 1) + (np.clip(dx, -R, R) + R)
                    return np.take_along_axis(costs, j[None].astype(int), 0)[0]
                ix, iy = bx.astype(int), by.astype(int)
                c0 = cost_at(ix, iy)
                for axis in (0, 1):
                    lo = cost_at(ix - (axis == 0), iy - (axis == 1)); hi = cost_at(ix + (axis == 0), iy + (axis == 1))
                    den = lo - 2 * c0 + hi
                    edge = (ix if axis == 0 else iy)
                    ok = (np.abs(edge) < R) & (den > 1e-9)
                    sub = np.where(ok, 0.5 * (lo - hi) / np.where(ok, den, 1), 0.0)
                    if axis == 0: bx = bx + np.clip(sub, -0.5, 0.5)
                    else: by = by + np.clip(sub, -0.5, 0.5)
                qy, qx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
                px, py = qx * 4 + 2.0, qy * 4 + 2.0
                x0 = X0 + v * k
                core = (px > x0 + 32) & (px < x0 + BW - 32) & (py > Y0 + 32) & (py < Y0 + BH - 32)
                if RANK:
                    if k % 3: continue
                    core &= (qx % 2 == 0) & (qy % 2 == 0)
                    us.append(rank_full(fr[k], fr[k + 1], costs, qx[core], qy[core]))
                    continue
                us.append(np.stack([bx[core] * 4, by[core] * 4], axis=1))
            u = np.concatenate(us)
            e = np.hypot(u[:, 0] - v, u[:, 1])
            al = is_alias(u, v) & (e > 2)
            r = np.round(u).astype(int)
            keys, cnt = np.unique(r, axis=0, return_counts=True)
            top = np.argsort(-cnt)[:3]
            common = "  ".join(f"({keys[i][0]:+d},{keys[i][1]:+d}): {100 * cnt[i] / len(r):4.1f}%" for i in top)
            print(f"{tex:6s} {v:3g} {lam:7.4f} | {100 * (e <= 2).mean():5.1f}% {100 * (e > 2).mean():5.1f}% "
                  f"{100 * al.mean():5.1f}% | {common}", flush=True)
