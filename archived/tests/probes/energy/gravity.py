"""ENERGY-TRANSFER.md 1.1: the synthetic control for "free flight has constant acceleration and zero jerk".

    gravity.py <workdir> [src_frames=120] [stem=quaddirectional-interpolation-propagated]

The master scene bounce-gravity (a textured box on the flat black ground, 1280x720, 24 fps) falls under a
constant g between bounces: its acceleration is exactly (0, g) px/frame^2 and its jerk exactly zero, except at the
wall hits. The reading tail of the four-frame propagated shader is switched to machine acceleration (read_view 5,
full scale 16) and to machine jerk (read_view 6, full scale 8), as tests/probes/jerk/jerksweep.sh does. It renders
at N:N (24 -> 24), where the reading sits on the source frame's own pixels, and every frame is scored inside the
box (eroded 12 px) against the closed form (masters.py), for frames more than 2 source frames from any hit (a
four-frame window straddling a bounce sees an impulse, which is the point of 3, not of this).

The field's frame k is scored against truth frame k, k - 1 and k + 1, and the best-fitting offset is reported
(the field tier recorded an off-by-one on one host).

Pre-registered in ENERGY-TRANSFER.md 1.1 (commit ea58d47, before any of this ran): acceleration within 5 percent
of g; the jerk residual at the oscillations' level, 0.05-0.2 px/frame^3.
"""
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
SHADERS = TESTS.parent / "shaders"
sys.path.insert(0, str(TESTS))
import masters                                                                   # noqa: E402

work = pathlib.Path(sys.argv[1]); work.mkdir(parents=True, exist_ok=True)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 120
stem = sys.argv[3] if len(sys.argv) > 3 else "quaddirectional-interpolation-propagated"
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
PY = os.environ.get("PYTHON", sys.executable)
W, H = 1280, 720
FS = {5: 16.0, 6: 8.0}

src = work / "src24.raw"
if not src.exists():
    subprocess.run([PY, str(TESTS / "masters.py"), "bounce-gravity", "--size", f"{W}x{H}", "--frames", str(N), "--src-fps",
                    "24", "--out-fps", "24", "--settle", "0", "--bg", "flat", "--texture", "sines", "--export-source", str(src)],
                   check=True, stdout=subprocess.DEVNULL)

t = (SHADERS / f"{stem}.glsl").read_text()
for view in (5, 6):
    s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>" + str(view) + "\n", t); assert n == 1, n
    s, n = re.subn(r"^const float READ_MACHINE_FS_ACC = 2\.0;$", "const float READ_MACHINE_FS_ACC = 16.0;", s, flags=re.M); assert n == 1, n
    s, n = re.subn(r"^const float READ_MACHINE_FS_JERK = 2\.0;$", "const float READ_MACHINE_FS_JERK = 8.0;", s, flags=re.M); assert n == 1, n
    (work / f"_v{view}.glsl").write_text(s)

table = {name: (kind, p) for name, kind, p, *_ in masters.masters(W, H)}
_, b = table["bounce-gravity"]
segs = masters.trajectory(b, float(W), float(H))
g = b.speed[3]
hits = [sg[0] for sg in segs[1:]]
hw, hh = b.w / 2, b.h / 2
yy, xx = np.mgrid[0:H, 0:W]

def mask(k, er=12):
    x, y = masters.bounce_centre(b, segs, k)
    return (np.abs(xx - x) < hw - er) & (np.abs(yy - y) < hh - er)

def render(view):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk",
           "-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src),
           # RGB IN (portable, 2026-09-30): with yuv420p in, Linux/Mesa returns the field 8-bit limited range; the
           # first runs (M5, 0be8cea, 85fea8b) used yuv420p in, which read exactly there. RGB in also keeps the
           # source at 16 bits rather than 8.
           "-vf", f"format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_v{view}.glsl,format=rgb48le",
           "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fb = W * H * 6; out = []
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        im = np.frombuffer(buf, np.uint16).reshape(H, W, 3).astype(np.float32) / 65535.0
        out.append(np.stack([(im[..., 0] - 0.5) * 2 * FS[view], (im[..., 1] - 0.5) * 2 * FS[view]], -1))
    err = p.stderr.read().decode(); p.wait()
    if p.returncode != 0: sys.exit(f"view {view}: ffmpeg failed: {err[:300]}")
    return out

print(f"# bounce-gravity: {N} source frames, g = {g:.4f} px/frame^2 downward, hits at {', '.join(f'{h:.2f}' for h in hits if h < N)}")
acc = render(5)
jerk = render(6)
# THE INSTRUMENT CHECK: off the box the field is zero, encoded 0.5 (fieldcheck.py's alarm)
bg0 = ~mask(10, er=-40)
z = np.median(np.abs(acc[10][bg0]))
assert z < 0.01, f"READ PATH BROKEN: the acceleration off the box reads {z}"

for off in (-1, 0, 1):
    ax, ay, jx, jy, used = [], [], [], [], 0
    for k in range(4, min(len(acc), N) - 4):
        kk = k + off
        if min(abs(kk - h) for h in hits) <= 2: continue
        m = mask(kk)
        if m.sum() < 1000: continue
        a, j = acc[k][m], jerk[k][m]
        ax.append(np.median(a[:, 0])); ay.append(np.median(a[:, 1]))
        jx.append(np.median(j[:, 0])); jy.append(np.median(j[:, 1])); used += 1
    ax, ay, jx, jy = map(np.array, (ax, ay, jx, jy))
    print(f"truth offset {off:+d}: {used} free-flight frames | acc y median {np.median(ay):+.4f} ({np.median(ay) / g * 100:5.1f}% of g), "
          f"p10-p90 {np.percentile(ay, 10):+.3f}..{np.percentile(ay, 90):+.3f}; acc x median {np.median(ax):+.4f} | "
          f"jerk median ({np.median(jx):+.4f}, {np.median(jy):+.4f}), |jerk| p90 {np.percentile(np.hypot(jx, jy), 90):.4f} px/frame^3")
