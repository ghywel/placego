"""Score a machine-read derivative field against an oscillation's analytic law (2026-09-08).

    snapcheck.py <order> <frames dir with f%03d.png> <fs> <A px> <Omega rad/s> <x0> <y0> <side> [erode=20]

order 1 velocity, 2 acceleration, 3 jerk, 4 snap. The scene is an O-case from scenes.sh: a square of side
`side` whose LEFT edge is at x0 + A sin(Omega t), top at y0, t in seconds at 24 fps. The k-th derivative of
position per frame^k is A (Omega/24)^k times cos or sin as appropriate. The field is decoded from the PNG's
R channel as (v - 0.5) * 2 fs px/frame^k (the machine encoding), averaged over the square eroded by `erode`
px so the boundary's own ambiguity is not scored.

Reported, and this is the point: the least-squares GAIN against the truth, the CORRELATION, and the RESIDUAL
after the best-fit gain -- the residual is the honest noise estimate, because a flat background has no
estimator noise at all to measure a floor from (the first version of this script tried, got exactly zero,
and would have reported an infinite signal-to-noise). Signal-to-noise is peak truth over residual rms.

USE A TEXTURED SCENE. On a flat square the interior carries no features, the field there is whatever
propagation fills in, and the mean over the square is near zero however good the estimator is: that is what
this script measured on O2_osc_medium before the scene was changed to O5_osc_textured, and it read a gain of
0.035 on a field the record calibrates to 6% error.
"""
import math
import pathlib
import subprocess
import sys
import os

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
order = int(sys.argv[1])
d = pathlib.Path(sys.argv[2])
fs = float(sys.argv[3])
A = float(sys.argv[4]); Om = float(sys.argv[5])
x0 = float(sys.argv[6]); y0 = float(sys.argv[7]); side = float(sys.argv[8])
erode = float(sys.argv[9]) if len(sys.argv) > 9 else 20.0
W, H = 1280, 720
NAME = {1: "velocity", 2: "acceleration", 3: "jerk", 4: "snap"}[order]


def load(png):
    raw = subprocess.run([FF, "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
    return (a - 0.5) * 2 * fs


w = Om / 24.0
rows = []
for png in sorted(d.glob("f*.png")):
    n = int(png.stem[1:]) - 1                       # ffmpeg numbers output frames from 1
    if n < 6:
        continue                                    # the window's start-up holds
    ph = Om * (n / 24.0)
    truth = {1: A * w * math.cos(ph), 2: -A * w * w * math.sin(ph),
             3: -A * w ** 3 * math.cos(ph), 4: A * w ** 4 * math.sin(ph)}[order]
    f = load(png)
    cx = x0 + A * math.sin(ph)
    xs, xe = int(cx + erode), int(cx + side - erode)
    ys, ye = int(y0 + erode), int(y0 + side - erode)
    rows.append((n, truth, float(f[ys:ye, xs:xe, 0].mean())))

tr = np.array([r[1] for r in rows]); me = np.array([r[2] for r in rows])
gain = float((tr * me).sum() / max((tr * tr).sum(), 1e-12))
corr = float(np.corrcoef(tr, me)[0, 1]) if tr.std() > 0 and me.std() > 0 else float("nan")
resid = me - gain * tr
peak = A * w ** order
print(f"== {NAME}: {len(rows)} frames, FS {fs:g}, A {A:g} px, Omega {Om:g} rad/s (w {w:.4f} rad/frame), "
      f"peak truth {peak:.3f} px/frame^{order}")
for n, truth, meas in rows[::4]:
    print(f"   frame {n:3d}: truth {truth:8.3f}   measured {meas:8.3f}")
print(f"   gain {gain:.3f}   correlation {corr:.3f}   residual rms {resid.std():.3f} px/frame^{order}   "
      f"peak truth / residual = {peak / max(resid.std(), 1e-9):.2f}   "
      f"measured rms / residual = {me.std() / max(resid.std(), 1e-9):.2f}")
