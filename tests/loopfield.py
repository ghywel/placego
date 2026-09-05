#!/usr/bin/env python3
"""Score a turn of machine readings of a loop against its steady truth: the mean, the mode, and the hit fraction.

    loopfield.py <loopdir> [N0=80] [NF=80]

<loopdir> is loop_torus.py's output with rv4/v<N0>..v<N0+NF-1>.png added (the machine velocity field,
read_view 4, 0.5 + px / 64, read through the EXACT path: format=rgb48le inside the filter graph; the
zero level off the object is checked). The field is scored at its own resolution, 8-px cells (READ_FIELD
is 1/8 res), one cell in from the silhouette.

Per cell, over the turn:
  hit fraction      how many of the NF readings are within 2 px (and 3 px) of the truth
  single frame      the reading at frame N0+20, for scale, and the per-frame trend (a reading with memory,
                    read_view 7 in the variants that have one, converges or does not over the turn)
  mean              of the NF readings (with its convergence at 1, 2, 4, 8, 16, NF/2 frames)
  median            coordinate-wise
  trimmed mean      of the readings within 3 px of the median
  mode              the peak of a 1-px 2D histogram of the readings, refined by mean shift (radius 1.5 px)
  mode over 3x3     the same over the cell and its eight neighbours (9 NF readings)
  oracle            the reading closest to the truth -- not an estimator, the floor any estimator could reach
  static backdrop   on a bg=tex loop, the reading's speckle where the truth is zero (median, p95 of |reading|)
each scored by the median |error|, its 90th percentile, the gross fraction (> 2 px), the magnitude ratio
and the angle, and written to <loopdir>/loopfield/ as .npy and as pictures (fieldpaint.py) with the truth,
the error maps and the hit map.

Why a mode: a block-matching tracker on a texture whose periods it cannot hold at its coarse levels does
not read truth-plus-noise; it reads the truth some of the time and an alias the rest, and the aliases are
not symmetric about the truth, so no mean of them converges. The consensus of the turn does, wherever the
truth is the most common reading (NFRAME-LIMITS.md, "The phase-locked consensus").
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

import fieldpaint

T = pathlib.Path(sys.argv[1])
N0 = int(sys.argv[2]) if len(sys.argv) > 2 else 80
NF = int(sys.argv[3]) if len(sys.argv) > 3 else 80
FF = os.environ.get("FFMPEG", "ffmpeg")
W, H, FS, C = 1280, 720, 32.0, 8
truth = np.load(T / "truth" / "truth_bwd.npy"); mask = np.load(T / "truth" / "mask.npy")


def cells(A):
    return A[:(H // C) * C, :(W // C) * C].reshape(H // C, C, W // C, C, -1).mean(axis=(1, 3))


tr = cells(np.where(mask[..., None], truth, 0.0)); cov = cells(mask[..., None].astype(np.float32))[..., 0]
valid = cov > 0.999
m = valid.copy()
for dy in (-1, 0, 1):
    for dx in (-1, 0, 1):
        m &= np.roll(np.roll(valid, dy, 0), dx, 1)
off = ~mask
for dy in (-8, 8):
    for dx in (-8, 8):
        off &= ~np.roll(np.roll(mask, dy, 0), dx, 1)

RV = os.environ.get("RV", "rv4")          # the frames folder: rv4 (the per-frame field) or another read_view
p = subprocess.Popen([FF, "-v", "error", "-framerate", "24", "-start_number", str(N0), "-i", str(T / RV / "v%03d.png"), "-frames:v", str(NF),
                      "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], stdout=subprocess.PIPE)
stack = np.zeros((NF, H // C, W // C, 2), np.float32); n = H * W * 6
for k in range(NF):
    b = p.stdout.read(n); assert len(b) == n, "frame %d short: %d bytes" % (k, len(b))
    im = np.frombuffer(b, np.uint16).reshape(H, W, 3)[..., :2].astype(np.float32) / 65535.0
    if k == 0:
        z = np.median(im[off], axis=0)
        if np.any(np.abs(z - 0.5) > 0.0005):
            sys.exit("  READ PATH BROKEN: the zero level off the object reads (%.4f, %.4f) instead of 0.5; render with format=rgb48le inside the filter graph" % tuple(z))
    stack[k] = cells((im - 0.5) * 2 * FS)
p.wait()

tn = np.linalg.norm(tr, axis=-1)
err = np.linalg.norm(stack - tr[None], axis=-1)
hit2 = (err < 2.0).mean(axis=0); hit3 = (err < 3.0).mean(axis=0)
print("loopfield %s: frames %d..%d, %d cells, |v| true median %.2f px/frame" % (T.name, N0, N0 + NF - 1, m.sum(), np.median(tn[m])))
print("  hit fraction (within 2 px): median %.2f  p25 %.2f  p75 %.2f  cells > 0.5: %.1f%% | within 3 px: median %.2f, > 0.5: %.1f%%" % (
    np.median(hit2[m]), np.percentile(hit2[m], 25), np.percentile(hit2[m], 75), 100 * (hit2[m] > 0.5).mean(), np.median(hit3[m]), 100 * (hit3[m] > 0.5).mean()))
for lo, hi in ((0, 5), (5, 10), (10, 15), (15, 25)):
    s = m & (tn >= lo) & (tn < hi)
    if s.sum() > 20:
        print("     |v| in [%2d,%2d): %5d cells  hit2 median %.2f  hit3 median %.2f" % (lo, hi, s.sum(), np.median(hit2[s]), np.median(hit3[s])))


def score(E, name):
    e = np.linalg.norm(E - tr, axis=-1)[m]; en = np.linalg.norm(E, axis=-1)[m]; t = tn[m]
    mv = t > 1.0
    cosang = (E[m][mv] * tr[m][mv]).sum(1) / (en[mv] * t[mv] + 1e-9)
    ang = np.degrees(np.arccos(np.clip(cosang, -1, 1)))
    print("  %-20s median |err| %.3f px  p90 %.3f  gross(>2) %4.1f%%  |est|/|true| %.3f  angle %.1f deg" % (
        name, np.median(e), np.percentile(e, 90), 100 * (e > 2.0).mean(), np.median(en[mv] / t[mv]), np.median(ang)))


def meanshift(s, x0, r=1.5, it=4):
    x = x0
    for _ in range(it):
        near = np.linalg.norm(s - x, axis=1) < r
        if near.sum() == 0: break
        x = s[near].mean(axis=0)
    return x


def mode_of(s):
    q = np.round(s).astype(int); keys = q[:, 0] * 1000 + q[:, 1]
    u, cnt = np.unique(keys, return_counts=True)
    return meanshift(s, s[keys == u[np.argmax(cnt)]].mean(axis=0))


mean = stack.mean(axis=0); med = np.median(stack, axis=0)
w = (np.linalg.norm(stack - med[None], axis=-1) < 3.0).astype(np.float32)
trim = (stack * w[..., None]).sum(axis=0) / np.maximum(w.sum(axis=0), 1)[..., None]
mode = np.zeros_like(mean); pmode = np.zeros_like(mean)
for i, j in zip(*np.nonzero(m)):
    mode[i, j] = mode_of(stack[:, i, j])
    blk = stack[:, max(i - 1, 0):i + 2, max(j - 1, 0):j + 2]; vb = valid[max(i - 1, 0):i + 2, max(j - 1, 0):j + 2]
    pmode[i, j] = mode_of(blk[:, vb].reshape(-1, 2))
best = stack[np.argmin(err, axis=0), np.arange(H // C)[:, None], np.arange(W // C)[None, :]]
score(stack[min(20, NF - 1)], "single frame")
# the trend frame by frame, for a reading with memory (read_view 7): the error of each frame's field
meds = np.median(err[:, m], axis=1)
print("  per-frame median |err|: " + "  ".join("f%d %.2f" % (N0 + k, meds[k]) for k in sorted({0, 2, 5, 10, 20, 40, NF // 2, NF - 1}) if k < NF))
for k in sorted({1, 2, 4, 8, 16, NF // 2}):
    if k < NF: score(stack[:k].mean(axis=0), "mean of %d frames" % k)
score(mean, "mean of the turn")
score(med, "median")
score(trim, "trimmed mean")
score(mode, "mode")
score(pmode, "mode over 3x3")
score(best, "oracle best frame")
# the static backdrop (bg=tex loops): the reading should be zero there; its speckle is the p95 of |reading|
bp = T / "truth" / "back.npy"
if bp.exists() and np.load(bp).any():
    back = cells(np.load(bp)[..., None].astype(np.float32))[..., 0] > 0.999
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            back &= np.roll(np.roll(cells(np.load(bp)[..., None].astype(np.float32))[..., 0] > 0.999, dy, 0), dx, 1)
    bn = np.linalg.norm(stack[:, back], axis=-1)
    print("  static backdrop (%d cells): |reading| median %.3f px  p95 %.3f  max %.2f  (fraction above 1 px: %.1f%%)" % (
        back.sum(), np.median(bn), np.percentile(bn, 95), bn.max(), 100 * (bn > 1.0).mean()))

OUT = T / "loopfield"; OUT.mkdir(exist_ok=True)
for name, F in (("mean", mean), ("median", med), ("mode", mode), ("pmode", pmode), ("hit2", hit2[..., None])):
    np.save(OUT / ("%s.npy" % name), F)
lum = fieldpaint.load_rgb24(T / "src.mkv", W, H, select=N0 + min(20, NF - 1))[..., 0].astype(np.float32) / 255.0
for name, F in (("mean", mean), ("mode", mode), ("pmode", pmode)):
    G = fieldpaint.up8(np.where(m[..., None], F, 0.0))
    fieldpaint.png(OUT / ("%s.png" % name), fieldpaint.paint(G, lum))
    fieldpaint.png(OUT / ("err-%s.png" % name), fieldpaint.paint_err(np.where(mask[..., None], G - truth, 0.0), mask))
fieldpaint.png(OUT / "single.png", fieldpaint.paint(fieldpaint.up8(np.where(m[..., None], stack[min(20, NF - 1)], 0.0)), lum))
fieldpaint.png(OUT / "truth.png", fieldpaint.paint(np.where(mask[..., None], truth, 0.0), lum))
fieldpaint.png(OUT / "hit.png", np.repeat(np.repeat(np.clip(hit2, 0, 1), C, axis=0), C, axis=1)[..., None].repeat(3, axis=-1).astype(np.float32).__mul__(255).astype(np.uint8))
print("  wrote %s (npy + png: mean, mode, pmode, single, truth, err-*, hit)" % OUT)
