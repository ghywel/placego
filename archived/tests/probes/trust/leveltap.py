#!/usr/bin/env python3
"""THE PER-LEVEL TRUST GATE, step T0 (2026-10-01): where a fine print's lock enters, level by level, and what each
later stage does to it. The diagnosis before the build (ENERGY-TRANSFER.md, "The per-level trust gate").

    leveltap.py <workdir> <shader.glsl> [speeds=5,11,19] [textures=weave,noise] [taps=all|label,label,...]

The scene is weavesweep.py's (tests/probes/weave): a textured box translating horizontally at v px/frame over black,
1280 x 720, 48 frames at 24; WEAVE_FULL=1 makes the print fill the frame and pan (weavesweep's full-frame mode). For
each TAP, a diagnostic copy of the shader is made: a pass inserted right after the named pass copies one quantity,
in full-resolution px, into DIAG_TAP at the 1/8 grid (an exact texelFetch / imageLoad of its own level's texel, so a
coarser level is not blurred by the copy), and the reading tail's READ_FIELD is re-pointed to it (flowtap.py's
method; read_view 4, the raw machine field, 0.5 + px / 64). It is read at N:N (fps=24), RGB in.

Per tap, over the region (the box eroded 32 px, its CORE; the frame less a 32-px border with WEAVE_FULL=1), frames
6..41: the median vector, the gross fraction (|u - (v, 0)| > 2 px), and the three commonest vectors (rounded to 1 px)
with their shares. Quantities that are not velocities (the 1/8 level's basin margin, the print gate's flag) are put
in x with y = 0 and read as numbers. Numbers only; the sources stay in the workdir.
"""
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
sys.path.insert(0, str(TESTS))
import masters                                                                   # noqa: E402

work = pathlib.Path(sys.argv[1]).resolve(); work.mkdir(parents=True, exist_ok=True)
SHADER = pathlib.Path(sys.argv[2]).read_text()
SPEEDS = [float(s) for s in (sys.argv[3] if len(sys.argv) > 3 else "5,11,19").split(",")]
TEXS = (sys.argv[4] if len(sys.argv) > 4 else "weave,noise").split(",")
WANT = (sys.argv[5] if len(sys.argv) > 5 else "all").split(",")
FF = os.environ.get("FFMPEG", str(pathlib.Path.home() / "np-build/ffmpeg/ffmpeg"))
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # tests/mvk-env.sh
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H, N = 1280, 720, 48
FULL = os.environ.get("WEAVE_FULL") == "1"
BW, BH, X0, Y0 = (8000, 1200, -3000.0, -200.0) if FULL else (320, 202, 40.0, 259.0)
ys_, xs_ = np.mgrid[0:H, 0:W]
XX, YY = xs_ + 0.5, ys_ + 0.5

# (label, the pass after which to tap (a //!DESC substring; the LAST match), extra binds, a GLSL expression giving
# vec2 in full-resolution px at the 1/8 cell `c8` (ivec2) whose normalised centre is `p`)
TAPS = [
    ("G", "[global] the frame's dominant shift", ["GLOBAL_SHIFT"], "texelFetch(GLOBAL_SHIFT_raw, ivec2(0), 0).xy * 16.0"),
    ("S.a", "[high] coarse flow search A->B and B->A (1/16 res)", ["FLOW_S_AB"],
     "texelFetch(FLOW_S_AB_raw, ivec2(p * FLOW_S_AB_size), 0).xy * 16.0"),
    ("S.b", "[high] coarse flow search A->B and B->A (1/16 res)", ["FLOW_S_AB"],
     "texelFetch(FLOW_S_AB_raw, ivec2(p * FLOW_S_AB_size), 0).zw * 16.0"),
    ("S.c", "[high] coarse flow search A->B and B->A (1/16 res)", ["FLOW_S_AB", "FLOW_S_AB_CACHE2"],
     "imageLoad(FLOW_S_AB_CACHE2, ivec2(p * FLOW_S_AB_size)).xy * 16.0"),
    ("S.g", "[high] coarse flow search A->B and B->A (1/16 res)", ["FLOW_S_AB", "FLOW_S_AB_CACHE2"],
     "imageLoad(FLOW_S_AB_CACHE2, ivec2(p * FLOW_S_AB_size)).zw * 16.0"),
    ("AE.best", "[alias] the 1/8 level's two basins", ["ALIAS_E_AB"], "texelFetch(ALIAS_E_AB_raw, c8, 0).xy * 8.0"),
    ("AE.rival", "[alias] the 1/8 level's two basins", ["ALIAS_E_AB"], "texelFetch(ALIAS_E_AB_raw, c8, 0).zw * 8.0"),
    ("AE.margin", "[alias] the 1/8 level's two basins", ["ALIAS_E_AB", "ALIAS_E_M_ST"],
     "vec2(min(imageLoad(ALIAS_E_M_ST, c8).x, 30.0), 0.0)"),
    ("E.raw", "[high] refine flow A->B (1/8 res)", ["FLOW_E_AB_RAW"], "texelFetch(FLOW_E_AB_RAW_raw, c8, 0).xy * 8.0"),
    ("E", "[prop12] three-way data check AB", ["FLOW_E_AB"], "texelFetch(FLOW_E_AB_raw, c8, 0).xy * 8.0"),
    ("Q.ref", "[high] refine flow A->B (1/4 res)", ["FLOW_Q_AB"],
     "texelFetch(FLOW_Q_AB_raw, ivec2(p * FLOW_Q_AB_size), 0).xy * 4.0"),
    ("Q.carry", "[alias] each quarter-level cell takes its cheaper hypothesis over the four scans (AB)", ["FLOW_Q_AB"],
     "texelFetch(FLOW_Q_AB_raw, ivec2(p * FLOW_Q_AB_size), 0).xy * 4.0"),
    ("Q.adopt", "[adopt] a locked print adopts its outline's motion (AB)", ["FLOW_Q_AB"],
     "texelFetch(FLOW_Q_AB_raw, ivec2(p * FLOW_Q_AB_size), 0).xy * 4.0"),
    ("PL.gate", "[print] the gate (AB and BA, fused)", ["PLAT_G"], "vec2(texelFetch(PLAT_G_raw, c8, 0).x * 10.0, 0.0)"),
    ("Q.lattice", "[print] apply (AB)", ["FLOW_Q_AB"],
     "texelFetch(FLOW_Q_AB_raw, ivec2(p * FLOW_Q_AB_size), 0).xy * 4.0"),
    ("H", None, [], None),                                       # the shader's own reading: FLOW_H_AB x 2
]
for extra in os.environ.get("TAPS_EXTRA", "").split(";"):      # label|desc|bind,bind|expr (for a variant's own passes)
    if extra.strip():
        lab, desc, binds, expr = extra.split("|")
        TAPS.append((lab, desc, binds.split(","), expr))


def tapped(label, desc, binds, expr):
    t = SHADER
    t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1, "read_view's default"
    if desc is None:
        return t
    hits = [m.start() for m in re.finditer(re.escape("//!DESC " + desc), t)]
    if not hits:
        return None                                            # this shader has no such pass
    nxt = t.index("\n//!HOOK", hits[-1]) + 1
    tap = ("//!HOOK FRAME_MIX\n//!BIND HOOKED\n" + "".join(f"//!BIND {b}\n" for b in binds) +
           "//!SAVE DIAG_TAP\n//!WIDTH HOOKED.w 8 /\n//!HEIGHT HOOKED.h 8 /\n//!COMPONENTS 2\n"
           f"//!DESC [diag] tap {label}\nvec4 hook() {{\n    vec2 p = HOOKED_pos;\n    ivec2 c8 = ivec2(gl_FragCoord.xy);\n"
           f"    return vec4({expr}, 0.0, 0.0);\n}}\n\n")
    t = t[:nxt] + tap + t[nxt:]
    a = "//!BIND HOOKED\n//!BIND FLOW_H_AB\n//!SAVE READ_FIELD\n"
    assert t.count(a) == 1, "the reading tail's READ_FIELD binding"
    t = t.replace(a, "//!BIND HOOKED\n//!BIND DIAG_TAP\n//!SAVE READ_FIELD\n")
    b = "    return vec4(FLOW_H_AB_tex(HOOKED_pos).xy * 2.0, 0.0, 1.0);\n"
    assert t.count(b) == 1, "the reading tail's READ_FIELD body"
    return t.replace(b, "    return vec4(texelFetch(DIAG_TAP_raw, ivec2(gl_FragCoord.xy), 0).xy, 0.0, 1.0);\n")


def texval(tex, u, v):
    if tex.startswith("weave:"):                                # weavesweep.py's weave:P
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
    return masters.clamp01(texval(tex, XX - x0, YY - y0) * 0.9 + 0.05) * covx * covy


def region(v, t):
    if FULL:
        return (XX > 32) & (XX < W - 32) & (YY > 32) & (YY < H - 32)
    x0 = X0 + v * t
    return (XX > x0 + 32) & (XX < x0 + BW - 32) & (YY > Y0 + 32) & (YY < Y0 + BH - 32)


def ff(src, shader):
    (work / "_tap.glsl").write_text(shader)
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
           "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf",
           "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_tap.glsl,format=rgb48le",
           "-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"]
    r = subprocess.run(cmd, cwd=work, capture_output=True)
    if r.returncode or b"compile status" in r.stderr or b"rror" in r.stderr:
        sys.exit(f"ffmpeg failed: {r.stderr[:400]}")
    return np.frombuffer(r.stdout, np.uint16).reshape(-1, H, W, 3)


print(f"{'layout':5s} {'tex':8s} {'v':>3s} {'tap':10s} | {'median':>15s} {'gross':>6s} | commonest (rounded px: share)")
for tex in TEXS:
    for v in SPEEDS:
        src = work / (("full-" if FULL else "") + f"src-{tex.replace(':', '-')}-{v:g}.raw")
        if not src.exists():
            with open(src, "wb") as f:
                for k in range(N): f.write(np.floor(frame(tex, v, float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2").tobytes())
        for label, desc, binds, expr in TAPS:
            if WANT != ["all"] and label not in WANT: continue
            sh = tapped(label, desc, binds, expr)
            if sh is None:
                print(f"{'full' if FULL else 'box':5s} {tex:8s} {v:3g} {label:10s} | (no such pass)"); continue
            fr = ff(src, sh)
            us, es = [], []
            for k in range(6, min(len(fr), N) - 6):
                m = region(v, float(k))
                m[(ys_ % 8) != 4] = False; m[(xs_ % 8) != 4] = False      # one sample per 1/8 cell
                u = (fr[k][..., :2].astype(np.float64) / 65535.0 - 0.5) * 64.0
                us.append(u[m]); es.append(np.hypot(u[m][:, 0] - v, u[m][:, 1]))
            u = np.concatenate(us); e = np.concatenate(es)
            med = np.median(u, axis=0)
            r = np.round(u).astype(int)
            keys, cnt = np.unique(r, axis=0, return_counts=True)
            top = np.argsort(-cnt)[:3]
            common = "  ".join(f"({keys[i][0]:+d},{keys[i][1]:+d}): {100 * cnt[i] / len(r):4.1f}%" for i in top)
            print(f"{'full' if FULL else 'box':5s} {tex:8s} {v:3g} {label:10s} | ({med[0]:+6.2f},{med[1]:+6.2f}) "
                  f"{100 * (e > 2).mean():5.1f}% | {common}", flush=True)
