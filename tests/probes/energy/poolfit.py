"""ENERGY-TRANSFER.md 2.4 in simulation, the reading: does the field see the hidden spin of a pool shot?

    poolfit.py <states.json> <render dir>

The field: the four-frame propagated shader's raw velocity (read_view 4) at N:N, RGB in (portable), with the zero
check on the still table. Per frame k (the three either side of the hit left out: the window straddles the impact),
on the cue ball (its centre from the states, used ONLY to place the mask): the top-down orthographic sphere fit of
travel plus spin within 0.97 R (2.3's fix):
    u = tX + wy Z - wz Y,   v = tY + wz X - wx Z,   Z = -sqrt(R^2 - X^2 - Y^2)  (the visible top, towards the camera)
and from it the SLIP at the cloth contact, u_c = t + R (wy, -wx) (the contact at +R Z, as pool_sim.py). Compared
with the simulation's truth frame by frame.

Pre-registered in ENERGY-TRANSFER.md 2.4 (f15f653): P1 the departure angle from the rolling frames within 2 degrees
(roll 33.7, stun 60); P2 the slip clearly non-zero after the hit and near zero after t_s, the transition within 3
frames; P3 the velocity direction turning smoothly 60 -> 33.7 during sliding (roll), steady at 60 (stun).
"""
import json
import math
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
SHADERS = HERE.parents[3] / "shaders"
st = json.load(open(sys.argv[1])); d = pathlib.Path(sys.argv[2])
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H = 1280, 720
R = st["R"]; fr = st["frames"]; hit = st["hit_t"]; t_s = st["t_s"]

t = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
(d / "_vel.glsl").write_text(s)
cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-framerate", "24", "-i", "f%04d.png",
       "-vf", "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl,format=rgb48le",
       "-f", "rawvideo", "-"]
raw = subprocess.run(cmd, cwd=d, capture_output=True, check=True).stdout
fb = W * H * 6; nf = len(raw) // fb
fld = lambda k: np.frombuffer(raw[k * fb:(k + 1) * fb], np.uint16).reshape(H, W, 3)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
# THE INSTRUMENT CHECK: the still table away from both balls reads zero, encoded 0.5
k0 = nf // 2; away = np.ones((H, W), bool)
for b in ("cue", "obj"):
    cx, cy = fr[k0][b]["p"]; away &= (xx - cx) ** 2 + (yy - cy) ** 2 > (R + 40) ** 2
z = float(np.median(fld(k0)[..., 0][away])) / 65535.0
if abs(z - 0.5) > 0.0005: sys.exit(f"READ PATH BROKEN: the still table reads {z:.4f}, not 0.5")

ang = lambda v: math.degrees(math.atan2(-v[1], v[0]))
rows = []
print(f"# {st['shot']}: hit at t {hit:.2f}, rolling again at t {t_s:.2f}; truth ends at {st['cue_final_deg']:.1f} deg")
print(f"{'k':>3s} {'dir read':>8s} {'truth':>6s} | {'|t| read':>8s} {'truth':>6s} | {'slip read':>9s} {'truth':>6s}")
for k in range(4, nf - 4):
    if abs(k - hit) <= 3: continue
    cx, cy = fr[k]["cue"]["p"]
    X, Y = xx - cx, yy - cy; rr = np.hypot(X, Y)
    m = rr < 0.97 * R; m[::1] &= True
    sub = np.zeros_like(m); sub[::2, ::2] = True; m &= sub
    Z = -np.sqrt(np.clip(R * R - X * X - Y * Y, 0, None))
    im = fld(k).astype(np.float32) / 65535.0
    u = (im[..., 0] - 0.5) * 64.0; v = (im[..., 1] - 0.5) * 64.0
    Xs, Ys, Zs = X[m], Y[m], Z[m]; one, zero = np.ones_like(Xs), np.zeros_like(Xs)
    A = np.concatenate([np.stack([one, zero, zero, Zs, -Ys], 1), np.stack([zero, one, -Zs, zero, Xs], 1)])
    sol, *_ = np.linalg.lstsq(A, np.concatenate([u[m], v[m]]), rcond=None)
    tv, w = sol[:2], sol[2:]
    slip = tv + R * np.array([w[1], -w[0]])
    tr = fr[k]["cue"]
    rows.append((k, ang(tv), ang(tr["v"]), float(np.linalg.norm(tv)), float(np.linalg.norm(tr["v"])),
                 float(np.linalg.norm(slip)), tr["slip"]))
    r_ = rows[-1]
    print(f"{k:3d} {r_[1]:8.1f} {r_[2]:6.1f} | {r_[3]:8.2f} {r_[4]:6.2f} | {r_[5]:9.2f} {r_[6]:6.2f}")
after = [r for r in rows if r[0] > t_s + 3]
before = [r for r in rows if r[0] < hit - 3]
slide = [r for r in rows if hit + 3 < r[0] < t_s - 1]
dep = float(np.median([r[1] for r in after])) if after else math.nan
print(f"  P1 departure angle (median over {len(after)} rolling frames): read {dep:.1f} deg, truth {st['cue_final_deg']:.1f}")
if slide:
    thr = 0.3 * max(r[5] for r in slide)
    trans = next((r[0] for r in rows if r[0] > hit + 3 and r[5] < thr), None)
    print(f"  P2 slip: before the hit read {np.median([r[5] for r in before]):.2f} (truth {np.median([r[6] for r in before]):.2f}); sliding read "
          f"{np.median([r[5] for r in slide]):.2f} (truth {np.median([r[6] for r in slide]):.2f}); rolling read "
          f"{np.median([r[5] for r in after]):.2f} (truth 0); the slip first under 30 % of its sliding peak at k {trans} "
          f"(truth t_s {t_s:.2f})")
    print(f"  P3 direction during sliding: " + " ".join(f"{r[1]:.0f}" for r in slide) + "  (truth " +
          " ".join(f"{r[2]:.0f}" for r in slide) + ")")
