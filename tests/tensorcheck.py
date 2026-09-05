#!/usr/bin/env python3
"""Score a machine gradient-tensor frame (read_view 9) of a disc scene against its analytic divergence and curl.

    tensorcheck.py <v.png (rgb48le, mode 9)> <W> <H> <cx> <cy> <R> <divergence> <curl> [FS=0.5]

The two exact gates (NFRAME-LIMITS.md, "Lead E"): the zoom of manifolds.py, a flat disc expanding 0.6% a
frame (divergence 0.012, curl 0; R 330 at 1280x720), and the rotating disc of scenes.sh at 24 fps (curl
2 omega / fps = 0.2618 for pi rad/s, divergence 0; R 150). Per radius band: the median divergence, curl
and first shear against the truth, and the divergence's 10th-90th percentile spread.
"""
import os
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
png = sys.argv[1]; W, H = int(sys.argv[2]), int(sys.argv[3])
cx, cy, R = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
tdiv, tcurl = float(sys.argv[7]), float(sys.argv[8])
FS = float(sys.argv[9]) if len(sys.argv) > 9 else 0.5
raw = subprocess.run([FF, "-v", "error", "-i", png, "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], capture_output=True, check=True).stdout
im = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
d = (im - 0.5) * 2 * FS
YY, XX = np.mgrid[0:H, 0:W]; r = np.hypot(XX - cx, YY - cy)
print("  radius band    divergence (truth %+.4f)   curl (truth %+.4f)   shear    divergence p10..p90" % (tdiv, tcurl))
for lo, hi in ((0.1, 0.4), (0.4, 0.7), (0.7, 0.85)):
    s = (r >= lo * R) & (r < hi * R)
    print("  %.2f-%.2f R   %+.4f                   %+.4f               %+.4f   %+.4f..%+.4f" % (
        lo, hi, np.median(d[s, 0]), np.median(d[s, 1]), np.median(d[s, 2]), np.percentile(d[s, 0], 10), np.percentile(d[s, 0], 90)))
