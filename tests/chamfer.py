#!/usr/bin/env python3
"""The chamfer line distance for realbench outputs: the metric the animation literature uses instead of
PSNR (Chen and Zwicker, ECCV 2022; see shaders/animation/ANI-PRIOR-ART.md).

    ./chamfer.py <outroot> <segment-seconds> <label> [label...]

For each synthesised frame (the odd frames of ref_<s>.mkv), the line art of the truth and of the
reconstruction are extracted the same way (luma gradient above 12/255 per pixel), each gets a distance
transform (exact, by iterative dilation up to 40 px), and the chamfer distance is the mean, over the
truth's line pixels, of the distance to the nearest reconstructed line pixel, plus the same the other way,
halved. In pixels: 0 is a perfect line drawing; a double line or a torn line shows as distance, where PSNR
shows only luma error. Also printed: the line-pixel count ratio (a shattered drawing has more line).
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg"); FP = os.environ.get("FFPROBE", "ffprobe")
root = pathlib.Path(sys.argv[1]); seg = sys.argv[2]; labels = sys.argv[3:]
RMAX = 40


def frames(path):
    wh = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
                        capture_output=True, text=True, check=True).stdout.strip().split(",")
    W, H = int(wh[0]), int(wh[1])
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.uint8); n = len(a) // (W * H)
    return a[:n * W * H].reshape(n, H, W).astype(np.float64)


def lines(f):
    gx = np.zeros_like(f); gy = np.zeros_like(f)
    gx[:, 1:-1] = (f[:, 2:] - f[:, :-2]) * 0.5; gy[1:-1, :] = (f[2:, :] - f[:-2, :]) * 0.5
    return np.hypot(gx, gy) > 12.0


def dist(mask):
    """Distance to the nearest True pixel, by iterative 4/8-neighbour dilation (chamfer 1-1), capped."""
    d = np.full(mask.shape, float(RMAX)); m = mask.copy(); d[m] = 0.0
    for r in range(1, RMAX):
        grown = m | np.roll(m, 1, 0) | np.roll(m, -1, 0) | np.roll(m, 1, 1) | np.roll(m, -1, 1)
        new = grown & ~m
        if not new.any(): break
        d[new] = r; m = grown
    return d


ref = frames(root / ("ref_%s.mkv" % seg)); n = len(ref)
odd = [k for k in range(1, n - 1, 2)]
rl = {k: lines(ref[k]) for k in odd}; rd = {k: dist(rl[k]) for k in odd}
print("  segment %s: chamfer line distance over %d synthesised frames (px; lower is better)" % (seg, len(odd)))
for label in labels:
    out = frames(root / ("o_%s_%s.mkv" % (label, seg))); m = min(len(out), n)
    cds = []; ratios = []
    for k in odd:
        if k >= m: break
        ol = lines(out[k]); od = dist(ol)
        if rl[k].sum() < 50 or ol.sum() < 50: continue
        cds.append(0.5 * (od[rl[k]].mean() + rd[k][ol].mean())); ratios.append(ol.sum() / rl[k].sum())
    print("    %-14s chamfer %.3f px   line-pixel ratio %.2f" % (label, float(np.mean(cds)), float(np.mean(ratios))))
