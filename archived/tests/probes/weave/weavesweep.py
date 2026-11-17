"""NFRAME-LIMITS, the weave: where the field's lock on a 2D periodic print begins.

    weavesweep.py <workdir> [speeds=2,4,6,8,10,12,14,16,18,20,24] [textures=noise,weave]

A 320 x 202 textured box translating HORIZONTALLY at a constant v px/frame over a flat (black) ground, 1280 x 720,
48 source frames at 24 (the box starts at x = 40 and wraps nowhere: 47 v <= 920). For each speed and texture:
  - the field: the four-frame shader's raw velocity (read_view 4) at N:N, RGB in, against the true (v, 0) over the box
    eroded 12 px: median |error|, the gross fraction (|error| > 2 px), and the median measured vector;
  - the picture: the Cadence default at 24 -> 60 (8-bit input, read at 16 bits: the equal-footing path) and linear,
    PSNR-Y over the box region at t (grown 4 px) against the closed form, interpolated frames only.
The zero-level alarm: a field that reads zero on a moving box is a broken read path. Numbers only.
WEAVE_FULL=1 (2026-10-01): the print fills the frame and pans; scored over the whole frame.
WEAVE_SCALE=s (2026-10-01, the 4K twins): every length times s -- the frame, the box, the speeds, the print (sampled at
1/s) -- so a `scale_shader.py <s>` twin (REC_SHADER) sees exactly the 1280 x 720 case in its own texels. Speeds are
given in the ORIGINAL pixels. The field is not read at s > 1 (the instrument's full scale is the unscaled quad's).
REC_METAL=<graph dir> (2026-10-01, the Metal port): the default's column through the Metal engine instead (QUADDEMO,
the demo's CLI), fed the SAME 8-bit frames (the source through yuv420p, then rgb48le) and read as its green channel.
REC_RGBIN=1: the default's libplacebo column fed those same rgb48le frames (the control for REC_METAL: the engines
compared on identical input).
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
RINGS = "--rings" in sys.argv; sys.argv = [x for x in sys.argv if x != "--rings"]
SPEEDS = [float(s) for s in (sys.argv[2] if len(sys.argv) > 2 else "2,4,6,8,10,12,14,16,18,20,24").split(",")]
TEXS = (sys.argv[3] if len(sys.argv) > 3 else "noise,weave").split(",")
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
SC = int(os.environ.get("WEAVE_SCALE", "1"))
W, H, N = 1280 * SC, 720 * SC, 48
BW, BH, X0, Y0 = 320 * SC, 202 * SC, 40.0 * SC, 259.0 * SC
# WEAVE_FULL=1 (2026-10-01, the lattice's cost cap): the print fills the whole frame and pans (the box far larger than it)
FULL = os.environ.get("WEAVE_FULL") == "1"
if FULL:
    BW, BH, X0, Y0 = 8000 * SC, 1200 * SC, -3000.0 * SC, -200.0 * SC
REC = "bidirectional-interpolation-variational-propagated-global-cage-energy-carry"
# REC_SHADER (stage 0c): a path to a variant scored in the default's place; the shipped default otherwise
(work / "_rec.glsl").write_text(pathlib.Path(os.environ["REC_SHADER"]).read_text() if os.environ.get("REC_SHADER")
                                else (SHADERS / f"{REC}.glsl").read_text())
# FIELD_STEM (stage 0a, 2026-09-30): the shader whose field is read; the quad by default (tonight's instrument)
FIELD_STEM = os.environ.get("FIELD_STEM", "quaddirectional-interpolation-propagated")
# FIELD_SHADER (stage 0f): a path to a diagnostic file whose read_view default is already 4 (flowtap.py), used as is
if os.environ.get("FIELD_SHADER"):
    s_ = pathlib.Path(os.environ["FIELD_SHADER"]).read_text()
    assert re.search(r"//!PARAM read_view\n(?://!.*\n)+4\n", s_), "FIELD_SHADER: read_view's default is not 4"
else:
    t_ = (SHADERS / f"{FIELD_STEM}.glsl").read_text()
    s_, n_ = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t_); assert n_ == 1
(work / "_vel.glsl").write_text(s_)
ys_, xs_ = np.mgrid[0:H, 0:W]
XX, YY = xs_ + 0.5, ys_ + 0.5


def texval(tex, u, v):
    """masters' textures, plus weave:P, the masters' weave with thread period P (checker 2P) in place of 14"""
    if tex.startswith("weave:"):
        P = float(tex.split(":")[1])
        a = 0.5 + 0.5 * np.sin(2 * np.pi * u / P); b = 0.5 + 0.5 * np.sin(2 * np.pi * v / P)
        over = ((np.floor(u / P).astype(np.int64) + np.floor(v / P).astype(np.int64)) % 2) == 0
        thread = np.where(over, a * 0.7 + b * 0.3, b * 0.7 + a * 0.3)
        return 0.15 + 0.7 * thread + 0.1 * (masters.vnoise(u / 3, v / 3) - 0.5)
    return masters.tex_value(tex, u, v)


def frame(tex, v, t):
    x0, y0 = X0 + v * t, Y0
    covx = masters.clamp01(np.minimum(x0 + BW, XX + 0.5) - np.maximum(x0, XX - 0.5))
    covy = masters.clamp01(np.minimum(y0 + BH, YY + 0.5) - np.maximum(y0, YY - 0.5))
    inside = masters.clamp01(texval(tex, (XX - x0) / SC, (YY - y0) / SC) * 0.9 + 0.05)
    return inside * covx * covy


def box(v, t, grow):
    x0 = X0 + v * t
    return (XX > x0 - grow) & (XX < x0 + BW + grow) & (YY > Y0 - grow) & (YY < Y0 + BH + grow)


def ff(inp, rate, vf, pix, nbytes):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
           "gray16le", "-s", f"{W}x{H}", "-r", str(rate), "-i", str(inp), "-vf", vf, "-fps_mode", "passthrough",
           "-f", "rawvideo", "-pix_fmt", pix, "-"]
    r = subprocess.run(cmd, cwd=work, capture_output=True)
    if r.returncode or b"compile status" in r.stderr: sys.exit(f"ffmpeg failed: {r.stderr[:300]}")
    return r.stdout


print(f"{'tex':6s} {'v':>4s} | {'field med err':>13s} {'gross':>6s} {'measured (median)':>18s} | "
      f"{'default':>7s} {'linear':>7s} {'default-linear':>14s}   (PSNR-Y on the box, dB)")
for tex in TEXS:
    for v0 in SPEEDS:
        v = v0 * SC
        assert FULL or X0 + v * (N - 1) + BW <= W, f"the box leaves the frame at v = {v}"
        src = work / (("full-" if FULL else "") + (f"src-{tex.replace(':', '-')}-{v0:g}.raw" if SC == 1 else f"src{SC}x-{tex.replace(':', '-')}-{v0:g}.raw"))
        if not src.exists():
            with open(src, "wb") as f:
                for k in range(N): f.write(np.floor(frame(tex, v, float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2").tobytes())
        # the field
        raw = b"" if SC > 1 else ff(src, 24, "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl,format=rgb48le",
                 "rgb48le", 0)
        fr = np.frombuffer(raw, np.uint16).reshape(-1, H, W, 3)
        errs, gross, meas = [], [], []
        rg = {"ring": [], "core": []}                         # --rings: the edge ring (0-16 px inside) and the core (32+ inside)
        for k in range(6, min(len(fr), N) - 6):
            u = (fr[k][..., :2].astype(np.float32) / 65535.0 - 0.5) * 64.0
            m = box(v, float(k), -12.0)
            e = np.hypot(u[..., 0][m] - v, u[..., 1][m])
            errs.append(np.median(e)); gross.append(float((e > 2).mean())); meas.append(np.median(u[m], axis=0))
            if RINGS:
                for name, mm in (("ring", box(v, float(k), 0.0) & ~box(v, float(k), -16.0)), ("core", box(v, float(k), -32.0))):
                    ee = np.hypot(u[..., 0][mm] - v, u[..., 1][mm]); rg[name].append(float((ee > 2).mean()))
        mv = np.median(np.array(meas), axis=0) if meas else np.zeros(2)
        if errs and v >= 2 and np.hypot(*mv) < 0.3 and np.median(errs) > 0.8 * v:
            sys.exit(f"the field read ZERO on a box moving {v} px/frame: the read path is broken")
        # the picture, equal footing: the default read at 16 bits; linear the same way
        outs = {}
        for name, mix in (("default", "frame_mixer=custom_n:custom_shader_path=_rec.glsl"), ("linear", "frame_mixer=linear")):
            if name == "default" and os.environ.get("REC_METAL"):
                rgb = work / "_metal_in.raw"; mo = work / "_metal_out.raw"
                subprocess.run([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24",
                                "-i", str(src), "-vf", "format=yuv420p,format=rgb48le", "-f", "rawvideo", str(rgb)], check=True)
                r = subprocess.run([os.environ["QUADDEMO"], "--graph", os.environ["REC_METAL"], "--input", str(rgb),
                                    "--export", str(mo), "--size", f"{W}x{H}"], capture_output=True)
                if r.returncode: sys.exit(f"the Metal engine failed: {r.stderr[-300:]}")
                outs[name] = np.fromfile(mo, "<u2").reshape(-1, H, W, 3)[..., 1].copy(); rgb.unlink(); mo.unlink()
                continue
            if name == "default" and os.environ.get("REC_RGBIN") == "1":
                r16 = ff(src, 24, f"format=yuv420p,format=rgb48le,libplacebo=fps=60:{mix}:format=gray16le", "gray16le", 0)
            else:
                r16 = ff(src, 24, f"format=yuv420p,libplacebo=fps=60:{mix}:format=gray16le", "gray16le", 0)
            outs[name] = np.frombuffer(r16, "<u2").reshape(-1, H, W)
        ps = {"default": [], "linear": []}
        for n in range(8, min(len(outs["default"]), len(outs["linear"])) - 8):
            if n % 5 == 0: continue
            t = n * 24 / 60; tr = frame(tex, v, t); m = box(v, t, 4.0 * SC)
            for name in ps:
                d = outs[name][n].astype(np.float64) / 65535.0 - tr
                mse = float(np.mean(d[m] ** 2)); ps[name].append(99.0 if mse == 0 else 10 * math.log10(1 / mse))
        pd, pl = np.median(ps["default"]), np.median(ps["linear"])
        print(f"{tex:6s} {v0:4.0f} | {np.median(errs) if errs else float('nan'):13.2f} {100 * np.median(gross):5.1f}% ({mv[0]:+7.2f},{mv[1]:+7.2f})    | "
              f"{pd:7.2f} {pl:7.2f} {pd - pl:+14.2f}"
              + (f"   gross: edge ring {100 * np.median(rg['ring']):5.1f}%, core {100 * np.median(rg['core']):5.1f}%" if RINGS else ""), flush=True)
