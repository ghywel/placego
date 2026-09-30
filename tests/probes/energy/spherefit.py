"""ENERGY-TRANSFER.md 2.3, the measurement: recover a ball's 3D spin from the 2-D field by a sphere fit.

    spherefit.py <render dir (f0001.png ...)> <truth: vertical|sight> [deg_per_frame=2]

The field: the four-frame propagated shader's raw velocity (read_view 4, full scale 32), at N:N (24 -> 24), on the
16-bit PNG sequence sphere_blender.py rendered. The ball's centre and radius from the picture (> 0.02 on black).

The model, in image axes (X right, Y down, Z into the screen; the visible hemisphere at Z = -sqrt(R^2 - X^2 - Y^2),
orthographic): a surface point's velocity is omega x r, projected
    u = omega_y Z - omega_z Y,     v = omega_z X - omega_x Z,
linear in omega = (omega_x, omega_y, omega_z) rad/frame. Solved by least squares over every 4th pixel within 0.9 R
(the limb foreshortens the flow to nothing), per frame; the median over frames 4-43 reported. Beside it, the curl
over the field's 8-px grid inside 0.7 R, halved: what a 2-D reading says the spin is.

Truth, from Blender's axes (world x -> image X, world z up -> image -Y, world y (depth) -> image Z):
    vertical (spin about world z, an axis IN the image plane):  omega = (0, -w, 0)
    sight    (spin about world y, the line of sight):           omega = (0, 0, +w)      w = deg_per_frame in radians
"""
import math
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
SHADERS = HERE.parents[3] / "shaders"
d = pathlib.Path(sys.argv[1]); case = sys.argv[2]
deg = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
w = math.radians(deg)
ROLL = case == "roll"
if ROLL: w = 0.02                                                 # sphere_blender.py's roll: v/R rad/frame
# roll, from above: world x -> X, world y -> -Y, world z (up, towards the camera) -> -Z; omega about world +y -> (0, -w, 0)
# tilt: world (0, 1, 1)/sqrt 2 -> image (0, -1, 1)/sqrt 2; persp: the vertical case through a perspective camera
truth = {"vertical": np.array([0, -w, 0]), "sight": np.array([0, 0, w]), "roll": np.array([0, -w, 0]),
         "tilt": w * np.array([0, -1, 1]) / math.sqrt(2), "persp": np.array([0, -w, 0])}[case]
T_TRUE = np.array([5.0, 0.0])                                    # roll: px/frame along X
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H = 1280, 720

t = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
(d / "_vel.glsl").write_text(s)

def run(chain):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-framerate", "24",
           "-i", "f%04d.png", "-vf", chain + ",format=rgb48le", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, cwd=d, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fb = W * H * 6; out = []
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        out.append(np.frombuffer(buf, np.uint16).reshape(H, W, 3).astype(np.float32) / 65535.0)
    err = p.stderr.read().decode(); p.wait()
    if p.returncode != 0: sys.exit(f"ffmpeg failed: {err[:300]}")
    return out

pic = run("format=rgb48le")[0][..., 0]
m = pic > 0.02
ys, xs = np.nonzero(m); cx, cy = xs.mean(), ys.mean(); R = math.sqrt(m.sum() / math.pi)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
X, Y = xx - cx, yy - cy
rr = np.hypot(X, Y)
# the fit's reach (fraction of R). From above, a rolling ball's spin is the CONTRAST between the top (t + omega R) and
# the limb (t): ill-conditioned when the fit stops short of the limb (0.9 R: a 1 % flatter profile moved omega
# by -5 %). FIT_R=0.97 takes it to where the field still reads 100.5 % (the band check, 2026-09-30).
FIT_R = float(os.environ.get("FIT_R", "0.9"))
PF = float(os.environ.get("PERSP_F", "0"))                   # focal length in px: the pinhole model (0 = orthographic)
fit_m = (rr < FIT_R * R); fit_m[::4, :] &= True
sub = np.zeros_like(fit_m); sub[::4, ::4] = True; fit_m &= sub
Z = -np.sqrt(np.clip(R * R - X * X - Y * Y, 0, None))
curl_m = rr < 0.7 * R

fld = run("format=yuv420p,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl")
pics = run("format=rgb48le") if ROLL else None
fits, curls, trans, shares = [], [], [], []
for k in range(4, min(len(fld), 44)):
    u = (fld[k][..., 0] - 0.5) * 2 * 32.0; v = (fld[k][..., 1] - 0.5) * 2 * 32.0
    if ROLL:                                                     # the ball moves: its centre from THIS frame
        mk = pics[k][..., 0] > 0.02; ys_, xs_ = np.nonzero(mk); cx, cy = xs_.mean(), ys_.mean()
        X, Y = xx - cx, yy - cy; rr = np.hypot(X, Y)
        Z = -np.sqrt(np.clip(R * R - X * X - Y * Y, 0, None))
        fit_m = (rr < FIT_R * R) & sub; curl_m = rr < 0.7 * R
    Xs, Ys, Zs = X[fit_m], Y[fit_m], Z[fit_m]
    one, zero = np.ones_like(Xs), np.zeros_like(Xs)
    if PF:                                                       # the PINHOLE sphere (2026-09-30): R = 1, the centre at
        # (0, 0, D) with D from the silhouette (sin(alpha) = 1/D, tan(alpha) = r_px / f); each pixel's ray meets the
        # sphere at P, the spin moves it at omega x (P - C), and the image velocity is f (V P_z - P V_z) / P_z^2
        D = 1 / math.sin(math.atan(R / PF))
        dvec = np.stack([Xs, Ys, np.full_like(Xs, PF)], 1); dvec /= np.linalg.norm(dvec, axis=1)[:, None]
        b_ = dvec[:, 2] * D; disc = b_ * b_ - (D * D - 1)
        ok = disc > 0; dvec, b_, disc = dvec[ok], b_[ok], disc[ok]
        P = (b_ - np.sqrt(disc))[:, None] * dvec; rx, ry, rz = P[:, 0], P[:, 1], P[:, 2] - D
        Px, Py, Pz = P[:, 0], P[:, 1], P[:, 2]; k2 = PF / Pz ** 2
        A = np.concatenate([np.stack([-Px * ry * k2, (Pz * rz + Px * rx) * k2, -PF * ry / Pz], 1),
                            np.stack([(-Pz * rz - Py * ry) * k2, Py * rx * k2, PF * rx / Pz], 1)])
        bvec = np.concatenate([u[fit_m][ok], v[fit_m][ok]])
        sol, *_ = np.linalg.lstsq(A, bvec, rcond=None); fits.append(sol)
        h = 8
        curl = ((np.roll(v, -h, 1) - np.roll(v, h, 1)) - (np.roll(u, -h, 0) - np.roll(u, h, 0))) / (2 * h)
        curls.append(np.median(curl[curl_m]) / 2)
        continue
    if ROLL:                                                     # u = tX + wy Z - wz Y ; v = tY + wz X - wx Z
        A = np.concatenate([np.stack([one, zero, zero, Zs, -Ys], 1), np.stack([zero, one, -Zs, zero, Xs], 1)])
    else:
        A = np.concatenate([np.stack([zero, Zs, -Ys], 1), np.stack([-Zs, zero, Xs], 1)])
    bvec = np.concatenate([u[fit_m], v[fit_m]])
    sol, *_ = np.linalg.lstsq(A, bvec, rcond=None)
    om = sol[2:] if ROLL else sol
    fits.append(om)
    if ROLL:
        t_ = sol[:2]; trans.append(t_)
        ke_t = 0.5 * (t_ @ t_); ke_r = 0.5 * 0.4 * R * R * (om @ om)       # per unit mass
        shares.append(ke_r / (ke_t + ke_r))
    h = 8
    curl = ((np.roll(v, -h, 1) - np.roll(v, h, 1)) - (np.roll(u, -h, 0) - np.roll(u, h, 0))) / (2 * h)
    curls.append(np.median(curl[curl_m]) / 2)
F = np.median(np.array(fits), axis=0); C = float(np.median(curls))
cos = float(F @ truth / (np.linalg.norm(F) * np.linalg.norm(truth)))
print(f"# {d.name} ({case}): ball centre ({cx:.1f}, {cy:.1f}), R {R:.1f} px; truth omega {truth.round(5)} rad/frame")
print(f"  sphere fit: omega ({F[0]:+.5f}, {F[1]:+.5f}, {F[2]:+.5f}); |omega| {np.linalg.norm(F):.5f} = "
      f"{np.linalg.norm(F) / w * 100:.1f}% of truth; axis error {math.degrees(math.acos(max(-1, min(1, cos)))):.1f} deg; "
      f"frame spread (std of |omega|) {np.std([np.linalg.norm(f) for f in fits]):.5f}")
if ROLL:
    Tm = np.median(np.array(trans), axis=0)
    print(f"  translation ({Tm[0]:+.3f}, {Tm[1]:+.3f}) px/frame = {np.linalg.norm(Tm) / np.linalg.norm(T_TRUE) * 100:.1f}% of truth"
          f" (5.000, 0); spin share of the kinetic energy {np.median(shares):.4f} (truth 2/7 = {2 / 7:.4f}); "
          f"frame spread {np.std(shares):.4f}")
print(f"  curl / 2 (what a 2-D reading calls the spin): {C:+.5f} rad/frame = {C / w * 100:+.1f}% of |truth| "
      f"(truth's line-of-sight part: {truth[2]:+.5f})")
