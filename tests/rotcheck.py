#!/usr/bin/env python3
"""Calibrate the acceleration field against ROTATIONAL truth (R2_rot_accel).

    ./rotcheck.py <raw16-file> <frame> <accel_diag_fs>

WHY THIS EXISTS. Every calibration so far has been translational: one true
acceleration vector shared by every texel of the object, so a median over
the window against a scalar truth was the right statistic. Rotation breaks
both halves of that. The true acceleration of a texel at position p on a
body rotating about centre c with angle theta(t) is

    a(p) = alpha * J * (p - c)  -  omega^2 * (p - c)

(J = 90-degree rotation; alpha = theta'', omega = theta') -- a VECTOR FIELD
that varies in direction and magnitude across the object: tangential spin-up
plus centripetal pull, both growing linearly with radius. So this tool
compares texel by texel, and reports the median RELATIVE VECTOR error
|a_meas - a_true| / |a_true| over live texels, plus the magnitude ratio and
the angular error separately -- a matcher could get the size right and the
direction wrong, and one number would hide it.

Rotation is also the first case where the block matcher's own model is
stressed: a patch on a rotating body TURNS between frames as well as
translating, and SAD matching only models the translation. Small per-frame
angles approximate translation locally; the approximation degrades with
omega. R2's spin-up sweeps that degradation within one scene: rim speed
grows from 0 to ~32 px/frame, and the rim exits the coarse search's ~23
px/frame reach around frame 17 -- calibrate below that, and treat anything
later as a reach test rather than a rotation test.

Scene parameters are parsed from tests/scenes.sh (theta = C*T^2 about a
fixed centre), never duplicated by hand. Truth is evaluated at slot 1's
instant, same window rule as accelcheck.py.
"""
import math
import os
import pathlib
import re
import sys

if len(sys.argv) < 4:
    sys.exit(__doc__.strip().splitlines()[2].strip())

raw = pathlib.Path(sys.argv[1])
# Optional 4th arg: which rotation scene (default R2). R3_rot_tex shares
# R2's motion exactly -- only the interior texture differs.
CASE = sys.argv[4] if len(sys.argv) > 4 else "R2_rot_accel"
frame = int(sys.argv[2])
fs = float(sys.argv[3])
W, H = 1280, 720

SRC_FPS = float(os.environ.get("SRC_FPS", "24"))
OUT_FPS = float(os.environ.get("OUT_FPS", "24"))

scenes = (pathlib.Path(__file__).resolve().parent / "scenes.sh").read_text()
m = re.search(rf"{re.escape(CASE)}\)\s*_blobt? '(\d+)' '(\d+)' '([\d.]+)\*T\*T' (\d+)",
              scenes)
if not m:
    sys.exit(f"{CASE}: not found in scenes.sh, or its shape changed")
cx, cy, C, R = float(m.group(1)), float(m.group(2)), float(m.group(3)), int(m.group(4))

# Slot 1's instant (the fit centre), same rule as accelcheck.py.
t_out = frame / OUT_FPS
k = math.floor(t_out * SRC_FPS)
tau = t_out * SRC_FPS - k
t1 = ((k + 1) if tau > 0.5 else k) / SRC_FPS

alpha = 2.0 * C                 # rad/s^2, constant
omega = 2.0 * C * t1            # rad/s at the fit centre
# Convert to the shader's units once: px/s^2 -> px/interval^2 is /fps^2.
a_scale = 1.0 / (SRC_FPS ** 2)

data = raw.read_bytes()
fsz = W * H * 6
nfr = len(data) // fsz
idx = frame if nfr > 1 else 0
if idx >= nfr:
    sys.exit(f"{raw}: holds {nfr} frames, asked for {frame}")
fr = data[idx * fsz:(idx + 1) * fsz]

FLOOR = 2.0 * fs / 65535 * 8
rel, magr, ang = [], [], []
n_all = 0
lo, hi = int(0.5 * R), int(1.45 * R)     # generous annulus; live mask decides
for yy in range(int(cy) - hi, int(cy) + hi, 2):
    row = yy * W * 6
    for xx in range(int(cx) - hi, int(cx) + hi, 2):
        rx, ry = xx - cx, yy - cy
        rr = math.hypot(rx, ry)
        if rr < lo or rr > hi:
            continue
        n_all += 1
        o = row + xx * 6
        ax = (int.from_bytes(fr[o:o + 2], "little") / 65535.0 - 0.5) * 2.0 * fs
        ay = (int.from_bytes(fr[o + 2:o + 4], "little") / 65535.0 - 0.5) * 2.0 * fs
        if math.hypot(ax, ay) <= FLOOR:
            continue
        # Truth at this texel: tangential alpha*J*r plus centripetal -w^2*r,
        # in px/interval^2. J*(rx,ry) = (-ry, rx).
        tx = (alpha * -ry - omega * omega * rx) * a_scale
        ty = (alpha * rx - omega * omega * ry) * a_scale
        tm = math.hypot(tx, ty)
        if tm < 1e-9:
            continue
        dm = math.hypot(ax - tx, ay - ty)
        rel.append(dm / tm)
        mm = math.hypot(ax, ay)
        magr.append(mm / tm)
        dot = max(-1.0, min(1.0, (ax * tx + ay * ty) / (mm * tm)))
        ang.append(math.degrees(math.acos(dot)))

print(f"frame {frame}  t_slot1 {t1:.4f}s  omega {omega:.3f} rad/s  "
      f"rim speed {omega * R / SRC_FPS:.1f} px/frame")
print(f"truth at rim    |a| = {math.hypot(alpha, omega * omega) * R * a_scale:.3f} "
      f"px/interval^2 (tangential {alpha * R * a_scale:.3f}, "
      f"centripetal {omega * omega * R * a_scale:.3f})")
if not rel:
    print(f"coverage        0.0% of {n_all} annulus texels -- no field here")
    sys.exit(0)
rel.sort(); magr.sort(); ang.sort()
n = len(rel)
print(f"coverage        {100.0 * n / n_all:.1f}% of {n_all} annulus texels")
print(f"vector error    median {100 * rel[n // 2]:.1f}%   "
      f"IQR [{100 * rel[n // 4]:.1f}%, {100 * rel[(3 * n) // 4]:.1f}%]")
print(f"magnitude ratio median {magr[n // 2]:.3f}   (1.0 = exact)")
print(f"angular error   median {ang[n // 2]:.1f} deg")
