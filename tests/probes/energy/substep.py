"""ENERGY-TRANSFER.md 5.1: the smallest one-frame step the field can see -- a cradle's middle ball moves ~1/3 px.

    substep.py <workdir> [steps=0.05,0.1,0.2,0.3,0.5,1.0] [stem=quaddirectional-interpolation-propagated] [sigma=0]

sigma: camera-like noise, in 8-bit levels, drawn fresh for every frame (seeded, so a rerun is identical). The first
run (2026-09-30) had none: static frames were bit-identical, the field read exactly 0 on them, and no threshold
exists without noise -- it measured the GAIN (63 percent at 0.05 px, 94 at 1 px) and the field's sub-pixel
quantum (1/32 px) instead.

Per step size s: 48 frames, 1280x720, black ground, two 300x300 squares of the masters' five-sine texture. The
MOVER holds still for frames 0-23 and stands s px to the right from frame 24 on; the CONTROL never moves. The
texture is the analytic function evaluated at the shifted coordinates, so a sub-pixel step is exact (no
resampling). Rendered at N:N (24 -> 24) through the four-frame propagated shader's reading tail: the raw field
(read_view 4) and the pooled reading (read_view 7), full scale 32 px/frame.

Scored inside each square (eroded 16 px): the median horizontal velocity per frame. The NOISE is the frame-to-frame
spread (std) of the control's median over frames 4-43 together with the mover's median on frames well away from
the step; the SIGNAL is the mover's largest |median| over frames 21-26 (a centred stencil shows a one-frame step
as s/2 on the frames either side of it; the four-frame fit spreads it). Detected when signal > 3 x noise.

Pre-registered in ENERGY-TRANSFER.md 5.1 (commit ea58d47, before any of this ran): the threshold lies between
0.2 and 0.5 px.
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
steps = [float(v) for v in (sys.argv[2] if len(sys.argv) > 2 else "0.05,0.1,0.2,0.3,0.5,1.0").split(",")]
stem = sys.argv[3] if len(sys.argv) > 3 else "quaddirectional-interpolation-propagated"
SIGMA = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
SIZES = [int(v) for v in (sys.argv[5] if len(sys.argv) > 5 else "268").split(",")]   # 5.2b: centred regions
# PORTABLE (2026-09-30): RGB into libplacebo, the source pre-quantised to 8-bit limited-range Y (what the yuv420p
# input did on the M5, and what phasestep.py assumes). With yuv420p in, Linux/Mesa returned the field 8-bit limited
# range (collide.py, c646384). The first M5 runs (9381f18) used yuv420p in and read exactly there.
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H, S, NF, STEP_AT = 1280, 720, 300, 48, 24
MOV = (200, 210); CTL = (780, 210)                                               # top-left corners
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)

t = (SHADERS / f"{stem}.glsl").read_text()
for view in (4, 7):
    s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>" + str(view) + "\n", t); assert n == 1, n
    (work / f"_v{view}.glsl").write_text(s)

def frame(shift):
    img = np.zeros((H, W))
    for (x0, y0), dx in ((MOV, shift), (CTL, 0.0)):
        inside = (xx >= x0 + dx) & (xx < x0 + dx + S) & (yy >= y0) & (yy < y0 + S)
        img = np.where(inside, masters.clamp01(masters.tex(xx - x0 - dx, yy - y0)), img)
    return img

def region(x0, y0, er=16):
    m = np.zeros((H, W), bool); m[y0 + er:y0 + S - er, x0 + er:x0 + S - er] = True; return m

def render(src, view):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk",
           "-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src),
           "-vf", f"format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_v{view}.glsl,format=rgb48le",
           "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fb = W * H * 6; out = []
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        im = np.frombuffer(buf, np.uint16).reshape(H, W, 3).astype(np.float32) / 65535.0
        if len(out) == 12:                                 # THE INSTRUMENT CHECK: the STATIC textured control square, on a
            # middle frame, reads zero, encoded 0.5. (The first version checked the black corner of frame 0: frame 0 is the
            # four-frame window's edge, and a matcher on the noisy black ground is not a zero reference -- it fired falsely.)
            z = float(np.median(im[CTL[1] + 40:CTL[1] + S - 40, CTL[0] + 40:CTL[0] + S - 40, 0]))
            if abs(z - 0.5) > 0.0005: sys.exit(f"READ PATH BROKEN: the static control reads {z:.4f}, not 0.5")
        out.append((im[..., 0] - 0.5) * 2 * 32.0)
    err = p.stderr.read().decode(); p.wait()
    if p.returncode != 0: sys.exit(f"view {view}: ffmpeg failed: {err[:300]}")
    return out

mm, mc = region(*MOV), region(*CTL)
print(f"# one-frame step at frame {STEP_AT}, {stem}, 24 -> 24, noise sigma {SIGMA:g}/255; medians inside each square (eroded 16 px)")
print(f"{'side':>4s} {'step px':>7s} {'view':>4s} | {'signal':>8s} {'at':>3s} | {'noise':>7s} | {'S/N':>6s} | detected | mover frames 20..27 (median u)")
for s in steps:
    src = work / f"step_{s:.3f}_n{SIGMA:g}_q8.raw"
    if not src.exists():
        a, bimg = frame(0.0), frame(s)
        rng = np.random.default_rng(20260930)
        with open(src, "wb") as f:
            for k in range(NF):
                img = (a if k < STEP_AT else bimg) + (rng.normal(0, SIGMA / 255.0, (H, W)) if SIGMA > 0 else 0)
                img = (np.round(16 + 219 * np.clip(img, 0, 1)) - 16) / 219
                f.write((np.clip(img, 0, 1) * 65535 + 0.5).astype("<u2").tobytes())
    for view in ((4,) if SIGMA > 0 else (4, 7)):
        u = render(src, view)
        for L in SIZES:
          o_ = (S - L) // 2
          mm = np.zeros((H, W), bool); mm[MOV[1] + o_:MOV[1] + o_ + L, MOV[0] + o_:MOV[0] + o_ + L] = True
          mc = np.zeros((H, W), bool); mc[CTL[1] + o_:CTL[1] + o_ + L, CTL[0] + o_:CTL[0] + o_ + L] = True
          mov = np.array([np.median(f[mm]) for f in u]); ctl = np.array([np.median(f[mc]) for f in u])
          quiet = [k for k in range(4, min(len(u), NF) - 4) if abs(k - STEP_AT) > 4]
          noise = np.std(np.concatenate([ctl[4:min(len(u), NF) - 4], mov[quiet]]))
          win = range(STEP_AT - 3, STEP_AT + 3)
          k_sig = max(win, key=lambda k: abs(mov[k])); sig = abs(mov[k_sig])
          sn = sig / noise if noise > 0 else float("inf")
          print(f"{L:4d} {s:7.3f} {view:4d} | {sig:8.4f} {k_sig:3d} | {noise:7.4f} | {sn:6.1f} | {'YES' if sn > 3 else 'no ':8s} | "
                + " ".join(f"{mov[k]:+.3f}" for k in range(20, 28)), flush=True)
