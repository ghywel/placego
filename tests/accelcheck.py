#!/usr/bin/env python3
"""Calibrate the tridirectional shader's ACCELERATION FIELD against truth.

    ./accelcheck.py <case> <raw16-file> <frame> <accel_diag_fs> [x y w h]

WHY THIS EXISTS. The tridirectional shader's real output is not the
interpolated picture -- it is a per-texel flow field that encodes acceleration
as well as velocity (see ../TRIDIRECTIONAL.md, "what this is actually for").
A field offered as a measurement has to be calibrated: not "does it look
plausible" but "what does it read, in px/interval^2, against a value we know
analytically, and how far out is it".

The O-series scenes exist for exactly this. Their motion is
x(t) = X0 + A*sin(w*t), so the true acceleration is

    a(t) = -A * w^2 * sin(w*t)      px/s^2

and dividing by fps^2 puts it in the shader's own units of px per source
interval squared. Nothing here is inferred from the render; the truth comes
from the scene definition.

WHAT IT COMPARES AGAINST. The shader's estimate is a QUADRATIC FIT through
three frames, so the value it reports is the acceleration at the fit's centre
-- the middle frame of the window, slot 1 -- not at the output timestamp. For
a sinusoid those differ, and comparing against the wrong instant would
manufacture an error that is really a timing mistake. Slot 1's time is derived
below from the same window rule the patch uses.

READING THE PIXELS. TRI_DIAG=2 encodes the field as
0.5 + (a / ACCEL_DIAG_FS) * 0.5 in R and G. Render to 16-bit
(-pix_fmt rgb48le) so the quantisation floor is ACCEL_DIAG_FS/32768 rather
than ACCEL_DIAG_FS/128 -- at 8 bits the encoding is coarser than the thing
being measured on quiet content, which would put the instrument's own
resolution into the error bars.
"""
import math
import pathlib
import re
import sys

if len(sys.argv) < 5:
    sys.exit(__doc__.strip().splitlines()[2].strip())

case = sys.argv[1]
raw = pathlib.Path(sys.argv[2])
frame = int(sys.argv[3])
fs = float(sys.argv[4])
W, H = 1280, 720
box = tuple(int(v) for v in sys.argv[5:9]) if len(sys.argv) >= 9 else None

import os
SRC_FPS = float(os.environ.get("SRC_FPS", "24"))
# FIELD selects which derivative the render encodes and which truth to
# compare against: "accel" (TRI_DIAG=2, px/interval^2 -- the default) or
# "jerk" (the quad shader's TRI_DIAG=5, px/interval^3). Same encoding, same
# readback; only the analytic truth changes. For x = A*sin(w*t) the jerk is
# -A*w^3*cos(w*t) -- ninety degrees out of phase with acceleration, so the
# O-series' acceleration zero-crossings are its jerk PEAKS, which is exactly
# where a jerk field earns its keep. Constant-acceleration scenes (A-series,
# F2) have jerk identically zero: the null case.
FIELD = os.environ.get("FIELD", "accel")
# N:N is the flow-field use case: the output coincides with source frames, so
# s = 0, the picture is an exact passthrough, and the anchor lands on the
# current frame -- a CENTRED second difference rather than an off-centre one.
OUT_FPS = float(os.environ.get("OUT_FPS", "60"))

# Motion parameters read from tests/scenes.sh rather than duplicated by hand.
# Two families carry analytic acceleration, and they cover different bands:
#
#   OSCILLATION (O-series), x = X0 + A*sin(w*t): acceleration sweeps its whole
#   range within one scene, which is what makes a calibration CURVE possible
#   from a single render. Peaks at 2.7-13.2 px/interval^2.
#
#   CONSTANT ACCELERATION (A-series, F2), x = C*t^2: acceleration is 2*C, the
#   same at every instant. Lower value per render -- one point, not a curve --
#   but these sit at 0.67/1.33/1.92 px/interval^2, which is exactly the band
#   real footage occupies (mean |a| 0.55-1.5) and exactly where the field is
#   known to be least reliable. They are also the EASIEST possible truth:
#   with `a` constant in time, the fit-centre correction below cannot
#   contribute any error at all, so a reading here isolates the estimator from
#   the timing.
scenes = (pathlib.Path(__file__).resolve().parent / "scenes.sh").read_text()

osc = re.search(rf"{re.escape(case)}\)\s*_rect '(\d+)\+(\d+)\*sin\(([\d.]+)\*T\)'"
                r"\s*'(\d+)' (\d+) (\d+)", scenes)
# Bare `C*T*T` (A1-A3, F2) and the general quadratic `X0-B*T+C*T*T` used by
# the textured A4-A7 twins, whose linear term is what keeps velocity inside
# the search's reach while holding acceleration constant.
const = re.search(rf"{re.escape(case)}\)\s*_rect '([\d.]+)\*T\*T'"
                  r"\s*'(\d+)' (\d+) (\d+)", scenes)
quad = re.search(rf"{re.escape(case)}\)\s*_rect "
                 r"'([\d.]+)([+-][\d.]+)\*T([+-][\d.]+)\*T\*T'"
                 r"\s*'(\d+)' (\d+) (\d+)", scenes)
# The Fourier-boundary blob under quadratic translation (F2). Flat interior,
# so the field lives only on the irregular boundary -- coverage will be low
# and that is the scene's point: multi-orientation edges, no straight lines.
blobq = re.search(rf"{re.escape(case)}\)\s*_blob '([\d.]+)\+([\d.]+)\*T\*T'"
                  r"\s*'(\d+)' '[^']*' (\d+)", scenes)
if blobq:
    qx0, accel_c, bcy, brad = (float(blobq.group(1)), float(blobq.group(2)),
                               float(blobq.group(3)), int(blobq.group(4)))
    qb = 0.0
    x0 = amp = w_rad = 0.0
    # Box around the blob: the flat interior reads zero and drops below the
    # live floor automatically, so a generous box costs nothing.
    y0, bw, bh = bcy - brad - 24, 2 * (brad + 24), 2 * (brad + 24)
elif quad:
    qx0, qb, accel_c, y0, bw, bh = (float(quad.group(1)), float(quad.group(2)),
                                    float(quad.group(3)), float(quad.group(4)),
                                    int(quad.group(5)), int(quad.group(6)))
    x0 = amp = w_rad = 0.0
elif osc:
    x0, amp, w_rad, y0, bw, bh = (float(osc.group(1)), float(osc.group(2)),
                                  float(osc.group(3)), float(osc.group(4)),
                                  int(osc.group(5)), int(osc.group(6)))
    accel_c = qx0 = qb = None
elif const:
    accel_c, y0, bw, bh = (float(const.group(1)), float(const.group(2)),
                           int(const.group(3)), int(const.group(4)))
    x0 = amp = w_rad = qx0 = qb = 0.0
else:
    sys.exit(f"{case}: no analytic acceleration (needs an O-series sinusoid "
             f"or a C*T*T constant-acceleration scene), or scenes.sh changed "
             f"shape")

# --- the instant the shader's estimate actually describes -------------------
# The window is {S_k, S_k+1, S_k+2} when the output sits in the LATTER half of
# its source interval (the nearest third frame is then the one ahead), and
# {S_k-1, S_k, S_k+1} otherwise. Slot 1 -- the fit's centre, and the frame
# whose two outgoing flows the acceleration is solved from -- is the later
# straddling frame in the first case and the earlier one in the second.
t_out = frame / OUT_FPS
k = math.floor(t_out * SRC_FPS)
tau = t_out * SRC_FPS - k
t_slot1 = ((k + 1) if tau > 0.5 else k) / SRC_FPS

# True value at that instant, converted to px per source interval^N.
# For x = C*t^2 the acceleration is 2*C, exact for ANY finite-difference
# estimator and independent of the instant -- which is why the A-series
# numbers never needed the correction below.
#
# THE ESTIMATOR MEASURES A DISCRETE DIFFERENCE, NOT A DERIVATIVE
# (2026-09-01). The quadratic fit through 3 unit-spaced samples has second
# derivative equal to the central second difference; the exact cubic
# through 4 has third derivative equal to the third difference. On a
# sinusoid those are NOT the continuous derivatives this tool originally
# compared against:
#
#   D2[A sin](t1)  = -4 A sin^2(w/2) sin(w t1)          same phase,
#                                                       (sin/x)^2 attenuated
#   D3[A sin](tc)  = -8 A sin^3(w/2) cos(w tc)          centred at the
#                                                       WINDOW CENTRE tc,
#                                                       not at slot 1
#
# with w in rad/interval. Comparing the jerk field against the continuous
# derivative at slot 1 manufactured an oscillating "error" of +-32% of
# peak on O5 whose zero-crossing at f10 was mistaken for a 3.4% calibration
# -- discovered when the native Metal port (METALPORT.md) disagreed with
# the ffmpeg pipeline by a 1-frame phase and BOTH matched this discrete
# model to <=0.5% (metal) / <=3% (ffmpeg). Against the discrete truth the
# accel O-series also improves: O5's published 5.6% contained ~3.5pp of
# pure attenuation.
#
# The window centre depends on which side of the output the host's 4-frame
# window sits, and the two verified hosts differ AT EXACT N:N: the ffmpeg
# queue supplies {k-2..k+1} (centre = t_slot1 - 0.5 intervals), the Metal
# host {k-1..k+2} (centre = t_slot1 + 0.5). JERK_CENTRE (in source
# intervals, relative to t_slot1) selects it; the default -0.5 describes
# the ffmpeg pipeline, the instrument's historical subject. Set
# JERK_CENTRE=0.5 for metal-demo exports. Fitted, not assumed: each host's
# measured curve matches its centre to the residuals quoted above.
theta = w_rad / (2.0 * SRC_FPS)
JERK_CENTRE = float(os.environ.get("JERK_CENTRE", "-0.5"))
if FIELD == "jerk":
    a_true_x = (0.0 if accel_c is not None else
                -8.0 * amp * math.sin(theta) ** 3
                * math.cos(w_rad * (t_slot1 + JERK_CENTRE / SRC_FPS)))
elif accel_c is None:
    a_true_x = -4.0 * amp * math.sin(theta) ** 2 * math.sin(w_rad * t_slot1)
else:
    a_true_x = 2.0 * accel_c / (SRC_FPS ** 2)

# Where the object is at that instant, so the sample window follows it.
if box is None:
    if accel_c is None:
        cx = x0 + amp * math.sin(w_rad * t_slot1)
    else:
        cx = qx0 + qb * t_slot1 + accel_c * t_slot1 * t_slot1
    if blobq:
        # Blob: centre the box on the blob, no inset -- the signal IS the
        # boundary, and the interior self-excludes via the live floor.
        box = (int(cx - bw / 2), int(y0), bw, bh)
    else:
        inset = 12  # stay clear of the boundary, where the estimate is gated
        box = (int(cx + inset), int(y0 + inset), bw - 2 * inset, bh - 2 * inset)

# --- decode the frame -------------------------------------------------------
data = raw.read_bytes()
fsz = W * H * 6                      # rgb48le
nfr = len(data) // fsz
# The raw may hold the whole rendered sequence, so index into it by output
# frame number rather than assuming a single-frame file. That lets one render
# feed a whole calibration sweep instead of one render per sample.
idx = frame if nfr > 1 else 0
if idx >= nfr:
    sys.exit(f"{raw}: holds {nfr} frames, asked for {frame}")
fr = data[idx * fsz:(idx + 1) * fsz]

bx, by, bw_, bh_ = box
xs, ys = [], []
for yy in range(by, by + bh_):
    row = yy * W * 6
    for xx in range(bx, bx + bw_, 3):        # every 3rd texel: plenty, and quick
        o = row + xx * 6
        r = int.from_bytes(fr[o:o + 2], "little")
        g = int.from_bytes(fr[o + 2:o + 4], "little")
        xs.append((r / 65535.0 - 0.5) * 2.0 * fs)
        ys.append((g / 65535.0 - 0.5) * 2.0 * fs)

if not xs:
    sys.exit("empty sample window")
n_all = len(xs)

# COVERAGE AND CONDITIONAL ACCURACY, not a single average. The field is
# SPARSE by construction: it reads zero wherever there is nothing to measure
# (no matchable texture) or wherever the trust gate discarded the estimate,
# and both are correct behaviours rather than errors. Averaging across those
# zeros reports a large error for a field that is accurate everywhere it
# actually speaks -- an earlier version of this script did exactly that and
# called a 6%-accurate reading "100% error".
#
# So: what fraction of the window carries a reading at all, and how accurate
# is it where it does. That is also how the field would be used -- masked to
# valid texels -- so it is the number that matters.
FLOOR = 2.0 * fs / 65535 * 8      # a few quantisation codes above zero
live = [v for v in xs if abs(v) > FLOOR]
cov = len(live) / n_all * 100.0

print(f"case            {case}")
print(f"output frame    {frame}  (t = {t_out:.4f}s, tau = {tau:.2f})")
print(f"fit centre      slot 1 at t = {t_slot1:.4f}s")
print(f"sample window   x {bx}..{bx + bw_}, y {by}..{by + bh_}  ({n_all} texels)")
print()
unit = "px/interval^3" if FIELD == "jerk" else "px/interval^2"
print(f"true    {'j' if FIELD == 'jerk' else 'a'}_x     "
      f"{a_true_x:+.3f} {unit}")
print(f"coverage        {cov:.1f}% of texels carry a reading "
      f"(|a| > {FLOOR:.4f})")

if not live:
    print("measured        nothing above the floor -- no field here")
    sys.exit(0)

live.sort()
m = len(live)
med = live[m // 2]
q1, q3 = live[m // 4], live[(3 * m) // 4]
print(f"measured a_x    {med:+.3f} median of live texels"
      f"   [{q1:+.3f}, {q3:+.3f}] IQR")
print(f"measured a_y    {sum(ys) / len(ys):+.3f} mean over all"
      f"     (truth: 0.000, motion is pure x)")
print()
err = med - a_true_x
rel = (abs(err) / abs(a_true_x) * 100.0) if abs(a_true_x) > 1e-9 else float("nan")
print(f"error where it reads   {err:+.3f} px/interval^2"
      + (f"   ({rel:.1f}% of true)" if rel == rel else ""))
print(f"quantisation           {2 * fs / 65535:.5f} px/interval^2 per code at "
      f"ACCEL_DIAG_FS={fs} in 16-bit")
