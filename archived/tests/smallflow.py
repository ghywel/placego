"""The small-flow floor: the measurement along the truth by |truth| band, per axis, on a machine frame
(NFRAME-LIMITS.md, "Lead A"). The zoom scene of manifolds.py is the case it was built for; BORDER=<px> in the
environment leaves a margin at the frame edge unscored.

    smallflow.py <v.png (rgb48le, mode 4)> <truthdir> <frame> [fs=32]
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
# stay well inside the object
m = mk.copy()
for dy in range(-6, 7):
    for dx in range(-6, 7):
        m &= np.roll(np.roll(mk, dy, 0), dx, 1)
m &= ~np.isnan(tr[..., 0])
B = int(os.environ.get("BORDER", "0"))
if B > 0:
    m[:B, :] = False; m[-B:, :] = False; m[:, :B] = False; m[:, -B:] = False
tn = np.linalg.norm(tr, axis=-1)
along = (meas * tr).sum(-1) / np.maximum(tn, 1e-9) ** 2
bands = [(0.25, 0.5), (0.5, 0.75), (0.75, 1.0), (1.0, 1.5), (1.5, 2.0), (2.0, 3.0)]
rows = []
for lo, hi in bands:
    s = m & (tn >= lo) & (tn < hi)
    if s.sum() < 200:
        rows.append("   -  "); continue
    # per-axis ratio where that axis carries most of the flow
    sx = s & (np.abs(tr[..., 0]) > 0.8 * tn); sy = s & (np.abs(tr[..., 1]) > 0.8 * tn)
    rx = np.median(meas[sx][:, 0] / tr[sx][:, 0]) if sx.sum() > 100 else np.nan
    ry = np.median(meas[sy][:, 1] / tr[sy][:, 1]) if sy.sum() > 100 else np.nan
    rows.append("%.2f(x%.2f y%.2f)" % (np.median(along[s]), rx, ry))
print("  along truth by |v| band (%s): %s" % (", ".join("%.2f-%.2f" % b for b in bands), "  ".join(rows)))
