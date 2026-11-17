"""Score a machine acceleration (read_view 5) or velocity (4) frame of the rotating disc against its analytic truth
(NFRAME-LIMITS.md, "Lead B"; the disc is the _blobt scene of scenes.sh at 720p, or the 4K render of it). Read the
frame through the exact path (format=rgb48le inside the graph) with READ_MACHINE_FS_ACC raised so the rim fits.

    discaccel.py <v.png (rgb48le)> <field: acc|vel> <fps_eff> [FS] [W H cx cy R omega]

The disc turns at omega rad/s about (cx, cy); a point at radius r has speed omega r px/s and centripetal
acceleration omega^2 r px/s^2 toward the centre. Per source interval at fps_eff: v = omega r / fps,
a = omega^2 r / fps^2. Velocity is tangential (the sign follows the render: angle increasing with T).
Bands of radius; per band the median ratio of the reading along the truth, the median angle to the truth,
and the fraction within 30 degrees.
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
png = pathlib.Path(sys.argv[1]); field = sys.argv[2]; fps = float(sys.argv[3])
FS = float(sys.argv[4]) if len(sys.argv) > 4 else (32.0 if field == "vel" else 16.0)
W, H, cx, cy, R, omega = (int(sys.argv[5]), int(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10])) if len(sys.argv) > 10 else (3840, 2160, 1920.0, 1080.0, 450.0, np.pi)
raw = subprocess.run([FF, "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], capture_output=True, check=True).stdout
im = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
meas = np.stack([(im[..., 0] - 0.5) * 2 * FS, (im[..., 1] - 0.5) * 2 * FS], -1)
YY, XX = np.mgrid[0:H, 0:W]
dx = XX - cx; dy = YY - cy; r = np.hypot(dx, dy)
if field == "vel":
    # tangential: for angle increasing with time in screen coordinates (y down), v = omega * (-dy, dx) / fps
    tr = np.stack([-dy, dx], -1) * (omega / fps)
else:
    tr = -np.stack([dx, dy], -1) * (omega ** 2 / fps ** 2)
# the render's orientation is not assumed: the sign that fits the outer band best is reported and used
tn = np.linalg.norm(tr, axis=-1)
outer = (r > 0.6 * R) & (r < 0.9 * R)
s = np.sign(np.median((meas[outer] * tr[outer]).sum(-1)))
tr = tr * s
along = (meas * tr).sum(-1) / np.maximum(tn, 1e-9) ** 2
cosang = (meas * tr).sum(-1) / (np.linalg.norm(meas, axis=-1) * tn + 1e-9)
ang = np.degrees(np.arccos(np.clip(cosang, -1, 1)))
print("  %s, fps_eff %g, sign %+d; truth at the rim: %.2f px/interval%s" % (field, fps, int(s), tn[r < R].max(), "" if field == "vel" else "^2"))
print("  radius band      truth   along-ratio   angle(deg)   within30")
for lo, hi in ((0.1, 0.3), (0.3, 0.5), (0.5, 0.7), (0.7, 0.85), (0.85, 0.97)):
    sel = (r >= lo * R) & (r < hi * R)
    print("  %4.2f-%4.2f R   %6.2f      %5.2f        %5.1f       %4.0f%%" % (lo, hi, np.median(tn[sel]), np.median(along[sel]), np.median(ang[sel]), 100 * (ang[sel] < 30).mean()))
