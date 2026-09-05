"""The silhouette-capture profile: the measurement along the truth, by distance from the object's rim
(NFRAME-LIMITS.md, "Lead A"). The aperture scene of manifolds.py is the case it was built for.

    rimprofile.py <v.png (rgb48le, mode 4)> <truthdir> <frame> [fs=32]

Bands 3-8, 8-16, 16-24, 24-32, 32-48, 48-64, 64-96, 96-131 px from the nearest off-object pixel; per band
the median of (meas . t_hat) / |truth| where |truth| > 1 px, and the median |error|.
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
png = pathlib.Path(sys.argv[1]); tdir = pathlib.Path(sys.argv[2]); frame = int(sys.argv[3])
fs = float(sys.argv[4]) if len(sys.argv) > 4 else 32.0
raw = subprocess.run([FF, "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], capture_output=True, check=True).stdout
tr = np.load(tdir / ("truth_%03d.npy" % frame)); mk = np.load(tdir / ("mask_%03d.npy" % frame))
H, W = mk.shape
im = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
meas = np.stack([(im[..., 0] - 0.5) * 2 * fs, (im[..., 1] - 0.5) * 2 * fs], -1)
# distance from the rim by successive erosion (cheap: dilate the off-object set band by band)
dist = np.full((H, W), 999, np.int32)
off = ~mk
cur = off.copy()
for d in range(1, 132):
    nxt = cur.copy()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        nxt |= np.roll(np.roll(cur, dy, 0), dx, 1)
    ring = nxt & ~cur & mk
    dist[ring] = d
    cur = nxt
tn = np.linalg.norm(tr, axis=-1)
ok = mk & ~np.isnan(tr[..., 0]) & (tn > 1.0)
along = (meas * tr).sum(-1) / np.maximum(tn, 1e-9) ** 2
err = np.linalg.norm(meas - np.nan_to_num(tr), axis=-1)
bands = [(3, 8), (8, 16), (16, 24), (24, 32), (32, 48), (48, 64), (64, 96), (96, 131)]
row = []; rowe = []
for lo, hi in bands:
    s = ok & (dist >= lo) & (dist < hi)
    row.append(np.median(along[s]) if s.sum() > 50 else np.nan); rowe.append(np.median(err[s]) if s.sum() > 50 else np.nan)
print("  along the truth by rim distance (%s): %s" % (", ".join("%d-%d" % b for b in bands), "  ".join("%.2f" % r for r in row)))
print("  median |err| by band:                  %s" % "  ".join("%.2f" % r for r in rowe))
