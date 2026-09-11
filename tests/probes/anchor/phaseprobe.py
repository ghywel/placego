"""WHERE IN TIME IS THE READING STANDING? A phase probe for the human-reading tail (2026-09-09).

    phaseprobe.py <frames dir with f%03d.png> <mode acc|vel> <fs> <src_fps> <out_fps> <A> <Omega> <x0> <y0> <side>

The reading tail's acceleration is built on an ANCHOR slot, and `DIAG_HOLD_ANCHOR` pins that slot to a
LITERAL index so a displayed field does not strobe as the output phase crosses 0.5. A literal index is only
correct for the window it was chosen against; when the window changes, the reading silently measures a
different instant. This probe finds that instant without reading any of that code, so it cannot inherit its
assumption.

Method. The scene is an oscillation, so every derivative is a sinusoid of the same period. Output frame n
sits at tau_n = n * src_fps / out_fps source frames. Decode the field over the moving object, then SWEEP an
assumed measurement offset delta (in source-frame intervals) and correlate the measured series against the
analytic truth evaluated at tau_n + delta. The delta of maximum correlation is where the reading stands; a
correct reading peaks at delta = 0. The sweep is fine enough to resolve a fifth of an interval, and the
correlation curve is reported around the peak so a flat or double-peaked answer is visible rather than
hidden behind one number.

Controls this probe carries deliberately:
  * VELOCITY (mode vel) is computed from the straddle pair directly and never touches the anchor, so its
    delta must NOT move when the anchor changes. If it does, the change did more than intended.
  * the fitted gain is reported beside the correlation: a phase answer with a collapsed gain is not a phase
    answer, it is a broken decode.
"""
import math
import os
import pathlib
import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
d = pathlib.Path(sys.argv[1]); mode = sys.argv[2]; fs = float(sys.argv[3])
src_fps = float(sys.argv[4]); out_fps = float(sys.argv[5])
A = float(sys.argv[6]); Om = float(sys.argv[7])
x0 = float(sys.argv[8]); y0 = float(sys.argv[9]); side = float(sys.argv[10])
W, H = 1280, 720
w = Om / src_fps                      # rad per source frame


def truth(tau):
    """the field's analytic value at source-frame time tau: x(tau) = x0 + A sin(w tau)"""
    if mode == "vel":
        return A * w * math.cos(w * tau)
    return -A * w * w * math.sin(w * tau)


def load(png):
    raw = subprocess.run([FF, "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0
    return (a - 0.5) * 2 * fs


rows = []
for png in sorted(d.glob("f*.png")):
    n = int(png.stem[1:]) - 1                       # ffmpeg numbers output frames from 1
    tau = n * src_fps / out_fps
    if tau < 6:
        continue                                    # the window's start-up holds
    f = load(png)
    cx = x0 + A * math.sin(w * tau)
    xs, xe = int(cx + 40), int(cx + side - 40)
    ys, ye = int(y0 + 40), int(y0 + side - 40)
    rows.append((tau, float(f[ys:ye, xs:xe, 0].mean())))

taus = np.array([r[0] for r in rows]); meas = np.array([r[1] for r in rows])
if meas.std() < 1e-9:
    sys.exit(f"{mode}: the decoded field does not vary ({len(rows)} frames) -- no phase to find")

best = None
curve = []
for delta in np.arange(-3.0, 3.0001, 0.05):
    t = np.array([truth(x + delta) for x in taus])
    if t.std() < 1e-12:
        continue
    c = float(np.corrcoef(t, meas)[0, 1])
    g = float((t * meas).sum() / (t * t).sum())
    curve.append((delta, c, g))
    if best is None or c > best[1]:
        best = (delta, c, g)

delta, c, g = best
period = 2 * math.pi / w
print(f"== {mode}: {len(rows)} frames, {src_fps:g} -> {out_fps:g} fps, FS {fs:g}, "
      f"oscillation period {period:.2f} source frames")
print(f"   MEASUREMENT INSTANT delta = {delta:+.2f} source intervals   correlation {c:.4f}   gain {g:.3f}")
near = [x for x in curve if abs(x[0] - delta) <= 0.55]
print("   correlation around the peak: " + "  ".join(f"{x[0]:+.2f}:{x[1]:.3f}" for x in near[::2]))
print(f"   (a correct reading peaks at delta = 0.00; the curve is periodic in {period:.1f} intervals, "
      f"so |delta| < {period / 2:.1f} is unambiguous)")
