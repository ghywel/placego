"""NFRAME-LIMITS, the weave: the outline's motion carried inward (E1, E2).

    weaveedge.py <workdir> [speeds=3,5,11,13,19] [textures=weave,noise]

weavesweep.py's scene (a 320 x 202 box translating horizontally over a flat ground, 48 frames at 24). The box
region is GIVEN (the one question: is the outline's motion good enough to draw the interior with?). The motion is
the median of the field (the four-frame shader's read_view 4 at N:N, RGB in) over the box's EDGE RING, 0-16 px
inside its boundary, at the field frame of the interval (the k + 1 convention). Each interpolated frame at
t = k + a is the box drawn from source frames k and k + 1 (the 8-bit frames the shader receives), each moved by that
motion to t and blended (1 - a, a); outside the box, the default's own frame. Scored on the box (grown 4 px)
against the closed form, beside the default (read at 16 bits) and linear. Numbers only.
"""
import math
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
SPEEDS = [float(s) for s in (sys.argv[2] if len(sys.argv) > 2 else "3,5,11,13,19").split(",")]
TEXS = (sys.argv[3] if len(sys.argv) > 3 else "weave,noise").split(",")
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H, N = 1280, 720, 48
BW, BH, X0, Y0 = 320, 202, 40.0, 259.0
REC = "bidirectional-interpolation-variational-propagated-global-cage-energy-carry"
(work / "_rec.glsl").write_text((SHADERS / f"{REC}.glsl").read_text())
t_ = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s_, n_ = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t_); assert n_ == 1
(work / "_vel.glsl").write_text(s_)
ys_, xs_ = np.mgrid[0:H, 0:W]
XX, YY = xs_ + 0.5, ys_ + 0.5


def frame(tex, v, t):                                             # weavesweep.py's scene, verbatim
    x0, y0 = X0 + v * t, Y0
    covx = masters.clamp01(np.minimum(x0 + BW, XX + 0.5) - np.maximum(x0, XX - 0.5))
    covy = masters.clamp01(np.minimum(y0 + BH, YY + 0.5) - np.maximum(y0, YY - 0.5))
    inside = masters.clamp01(masters.tex_value(tex, XX - x0, YY - y0) * 0.9 + 0.05)
    return inside * covx * covy


def box(v, t, grow):
    x0 = X0 + v * t
    return (XX > x0 - grow) & (XX < x0 + BW + grow) & (YY > Y0 - grow) & (YY < Y0 + BH + grow)


def ff(inp, rate, vf, pix):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
           "gray16le", "-s", f"{W}x{H}", "-r", str(rate), "-i", str(inp), "-vf", vf, "-fps_mode", "passthrough",
           "-f", "rawvideo", "-pix_fmt", pix, "-"]
    r = subprocess.run(cmd, cwd=work, capture_output=True)
    if r.returncode or b"compile status" in r.stderr: sys.exit(f"ffmpeg failed: {r.stderr[:300]}")
    return r.stdout


def sample(img, X, Y):                                            # bilinear, pixel centres at +0.5
    x = X - 0.5; y = Y - 0.5
    x0 = np.floor(x).astype(np.int64); y0 = np.floor(y).astype(np.int64); fx = x - x0; fy = y - y0
    x0c, x1c = np.clip(x0, 0, W - 1), np.clip(x0 + 1, 0, W - 1); y0c, y1c = np.clip(y0, 0, H - 1), np.clip(y0 + 1, 0, H - 1)
    return ((1 - fx) * (1 - fy) * img[y0c, x0c] + fx * (1 - fy) * img[y0c, x1c]
            + (1 - fx) * fy * img[y1c, x0c] + fx * fy * img[y1c, x1c])


print(f"{'tex':6s} {'v':>4s} | {'edge-ring motion':>18s} {'ring gross':>10s} | {'default':>7s} {'edge warp':>9s} {'linear':>7s} "
      f"{'edge - default':>14s}   (PSNR-Y on the box, dB)")
for tex in TEXS:
    for v in SPEEDS:
        src = work / f"src-{tex}-{v:g}.raw"
        if not src.exists():
            with open(src, "wb") as f:
                for k in range(N): f.write(np.floor(frame(tex, v, float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2").tobytes())
        fr = np.frombuffer(ff(src, 24, "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl,"
                              "format=rgb48le", "rgb48le"), np.uint16).reshape(-1, H, W, 3)
        vel = {}; rg = []
        for k in range(1, min(len(fr), N)):
            u = (fr[k][..., :2].astype(np.float32) / 65535.0 - 0.5) * 64.0
            ring = box(v, float(k), 0.0) & ~box(v, float(k), -16.0)
            vel[k] = np.median(u[ring], axis=0)
            rg.append(float((np.hypot(u[..., 0][ring] - v, u[..., 1][ring]) > 2).mean()))
        if max(abs(x[0]) for x in vel.values()) < 0.3: sys.exit(f"the field read ZERO at {v} px/frame: the read path is broken")
        y8 = np.frombuffer(subprocess.run([FF, "-v", "error", "-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24",
                                           "-i", str(src), "-vf", "format=yuv420p,extractplanes=y", "-f", "rawvideo", "-pix_fmt",
                                           "gray", "-"], capture_output=True, check=True).stdout, np.uint8).reshape(-1, H, W)
        S = lambda k: np.clip((y8[k].astype(np.float32) - 16) / 219, 0, 1)
        rec = np.frombuffer(ff(src, 24, "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_rec.glsl:"
                                 "format=gray16le", "gray16le"), "<u2").reshape(-1, H, W)
        lin = np.frombuffer(ff(src, 24, "format=yuv420p,libplacebo=fps=60:frame_mixer=linear:format=gray16le", "gray16le"),
                            "<u2").reshape(-1, H, W)
        ps = {"default": [], "edge": [], "linear": []}; mv = []
        for n in range(8, min(len(rec), len(lin)) - 8):
            if n % 5 == 0: continue
            t = n * 24 / 60; k = int(math.floor(t)); a = t - k
            if k + 1 not in vel: continue
            d = vel[k + 1]; mv.append(d)                       # the interval's motion, the field's k + 1 convention
            tr = frame(tex, v, t); m = box(v, t, 4.0)
            img = rec[n].astype(np.float64) / 65535.0
            reg = box(v, t, 0.0)                              # the given region at t
            v0 = sample(S(k), XX[reg] - a * d[0], YY[reg] - a * d[1])
            v1 = sample(S(k + 1), XX[reg] + (1 - a) * d[0], YY[reg] + (1 - a) * d[1])
            edge = img.copy(); edge[reg] = (1 - a) * v0 + a * v1
            for name, im in (("default", img), ("edge", edge), ("linear", lin[n].astype(np.float64) / 65535.0)):
                mse = float(np.mean((im[m] - tr[m]) ** 2)); ps[name].append(99.0 if mse == 0 else 10 * math.log10(1 / mse))
        md = np.median(np.array(mv), axis=0)
        pd, pe, pl = (np.median(ps[x]) for x in ("default", "edge", "linear"))
        print(f"{tex:6s} {v:4.0f} | ({md[0]:+7.2f},{md[1]:+6.2f})   {100 * np.median(rg):9.1f}% | {pd:7.2f} {pe:9.2f} {pl:7.2f} "
              f"{pe - pd:+14.2f}", flush=True)
