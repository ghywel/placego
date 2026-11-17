"""ENERGY-TRANSFER.md 1.4 in simulation, the reading: the pendulum's energy from the field, frame by frame.

    pendulumfit.py <pendulum.json> <render dir>

The field: the four-frame propagated shader's raw velocity (read_view 4) at N:N, RGB in, with the zero check on the
still wall. Per frame (the clip's first and last three out: the window's edges):
  speed  = |median (u, v)| over the bob (its truth centre places the mask only, radius R - 10);
  height = (the lowest point) - (the bob's MEASURED centroid): pixels brighter than 0.62 within R + 15 of where it is
           (the bob is ramped 0.4-1.0, the wall 0-0.3, linear: 0.66+ and 0-0.58 after the sRGB transform);
  E      = 1/2 speed^2 + g height, against the truth's constant.
Pre-registered in ENERGY-TRANSFER.md 1.4 (806b219): E1 E constant within 5 percent (max - min over mean); E2 the kinetic
energy at the bottom of the swing within 5 percent of the truth.
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
P = json.load(open(sys.argv[1])); d = pathlib.Path(sys.argv[2])
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H = 1280, 720
G, L, R = P["g"], P["L"], P["R"]; st = P["states"]; ybot = P["pivot"][1] + L

t = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
(d / "_vel.glsl").write_text(s)
def run(chain):
    raw = subprocess.run([FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-framerate", "24",
                          "-i", "f%04d.png", "-vf", chain + ",format=rgb48le", "-f", "rawvideo", "-"], cwd=d, capture_output=True,
                         check=True).stdout
    fb = W * H * 6
    return [np.frombuffer(raw[i * fb:(i + 1) * fb], np.uint16).reshape(H, W, 3) for i in range(len(raw) // fb)]
pics = run("format=rgb48le")
fld = run("format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl")
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)
k0 = len(fld) // 2; cx, cy = st[k0]["c"]
away = (xx - cx) ** 2 + (yy - cy) ** 2 > (R + 60) ** 2
z = float(np.median(fld[k0][..., 0][away])) / 65535.0
if abs(z - 0.5) > 0.0005: sys.exit(f"READ PATH BROKEN: the still wall reads {z:.4f}, not 0.5")

rows = []
for k in range(3, len(fld) - 3):
    cx, cy = st[k]["c"]
    m = (xx - cx) ** 2 + (yy - cy) ** 2 < (R - 10) ** 2
    f = fld[k].astype(np.float32) / 65535.0
    u = np.median((f[..., 0][m] - 0.5) * 64.0); v = np.median((f[..., 1][m] - 0.5) * 64.0)
    spd = math.hypot(u, v)
    pic = pics[k][..., 0].astype(np.float32) / 65535.0
    # 0.62: the render's sRGB transform lifts the wall's 0-0.3 (linear) to 0-0.58 and the bob's 0.4 to 0.66; the first
    # threshold (0.35, in linear terms) let the wall into the centroid and read the bottom of the swing ~5 px high
    near = ((xx - cx) ** 2 + (yy - cy) ** 2 < (R + 15) ** 2) & (pic > 0.62)
    ym = float(yy[near].mean())
    h = ybot - ym
    E = 0.5 * spd * spd + G * h
    rows.append((k, spd, st[k]["speed"], h, st[k]["h"], E, st[k]["E"]))
E = np.array([r[5] for r in rows]); Et = st[0]["E"]
print(f"# pendulum: L {L:.0f} px, g {G} px/frame^2, from {math.degrees(st[0]['theta']):.0f} deg; truth E/m {Et:.2f} (px/frame)^2, constant")
print(f"  E1 measured E: mean {E.mean():.2f} ({(E.mean() / Et - 1) * 100:+.1f} % of truth), max - min {E.max() - E.min():.2f} = "
      f"{(E.max() - E.min()) / E.mean() * 100:.1f} % of the mean; p5-p95 {np.percentile(E, 5):.2f}..{np.percentile(E, 95):.2f}")
bottom = [r for r in rows if r[4] < 0.05 * L * (1 - math.cos(st[0]['theta']))]
ke = [(0.5 * r[1] ** 2, 0.5 * r[2] ** 2) for r in bottom]
print(f"  E2 kinetic energy at the bottom ({len(bottom)} frames): read {np.mean([a for a, b in ke]):.2f}, truth "
      f"{np.mean([b for a, b in ke]):.2f} ({(np.mean([a for a, b in ke]) / np.mean([b for a, b in ke]) - 1) * 100:+.1f} %)")
print(f"  speed read/truth over the swing: median {np.median([r[1] / r[2] for r in rows if r[2] > 3]):.3f}; "
      f"height error median {np.median([r[3] - r[4] for r in rows]):+.2f} px (p90 |err| {np.percentile([abs(r[3] - r[4]) for r in rows], 90):.2f})")
worst = max(rows, key=lambda r: abs(r[5] - Et))
print(f"  the worst frame: k {worst[0]} (speed read {worst[1]:.2f} truth {worst[2]:.2f}; height read {worst[3]:.1f} truth {worst[4]:.1f}; "
      f"E {worst[5]:.1f} vs {Et:.1f})")
bad = [r for r in rows if r[2] > 8 and r[1] < 0.8 * r[2]]
print(f"  speed DROPOUTS (read < 80 % of a truth above 8 px/frame): {len(bad)} of {sum(1 for r in rows if r[2] > 8)} frames: "
      + " ".join(f"k{r[0]}:{r[1]:.1f}/{r[2]:.1f}" for r in bad))
good = [r for r in rows if not (r[2] > 8 and r[1] < 0.8 * r[2])]
Eg = np.array([r[5] for r in good])
print(f"  without the dropouts ({len(good)} frames): E mean {Eg.mean():.2f} ({(Eg.mean() / Et - 1) * 100:+.1f} %), "
      f"max - min {(Eg.max() - Eg.min()) / Eg.mean() * 100:.1f} % of the mean, p5-p95 {np.percentile(Eg, 5):.1f}..{np.percentile(Eg, 95):.1f}")
