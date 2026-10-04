#!/usr/bin/env python3
"""THE TRUST GATE ON A ROTATING EXACT PRINT (2026-10-01): why R3_rot_tex loses 7 dB with the uniqueness test in place.

    r3diag.py <workdir> <trust variant.glsl> <control.glsl>

R3 is the ladder's textured rotation: a wobbly disc (radius about 150) carrying an exact sin x sin print of period 40 px,
turning by theta = 2.56 T^2 (T in seconds), so the rim's speed ramps from 0 to about 32 px/frame over the second. Its
24 source frames (scenes.sh, 24 fps) run at N:N through diagnostic copies of the variant (the cell's flow just before the
gate, the gate's decided vector and its flag, the final field) and of the control (the final field), read at the 1/8
grid through the reading tail. The truth is the disc's rigid rotation between the pair's two instants; the pairing
convention (k with k + 1, or k - 1 with k) is the one under which the control reads the slow interior better. Reported
by radius band (inside 130 px): the share of cells the gate replaced, the median error of the flow it replaced and of
its replacement, and the final fields' median errors and gross shares (over 2 px), the variant's against the control's.
"""
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
work = pathlib.Path(sys.argv[1]).resolve(); work.mkdir(parents=True, exist_ok=True)
VAR, CTL = pathlib.Path(sys.argv[2]).read_text(), pathlib.Path(sys.argv[3]).read_text()
FF = os.environ.get("FFMPEG", str(pathlib.Path.home() / "np-build/ffmpeg/ffmpeg"))
if sys.platform == "darwin":
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H, CX, CY = 1280, 720, 640.0, 360.0
lavfi = subprocess.run(["bash", "-c", f"cd '{TESTS}' && source ./scenes.sh >/dev/null 2>&1; scene R3_rot_tex 24"],
                       capture_output=True, text=True).stdout.strip()
assert lavfi.startswith("nullsrc"), lavfi[:200]
src = work / "r3.raw"
if not src.exists():
    r = subprocess.run([FF, "-v", "error", "-f", "lavfi", "-i", lavfi, "-f", "rawvideo", "-pix_fmt", "gray16le", str(src)],
                       capture_output=True)
    assert r.returncode == 0, r.stderr[:300]


def tapped(t, desc, binds, expr):
    t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
    if desc:
        hits = [m.start() for m in re.finditer(re.escape("//!DESC " + desc), t)]
        assert hits, desc
        nxt = t.index("\n//!HOOK", hits[-1]) + 1
        tap = ("//!HOOK FRAME_MIX\n//!BIND HOOKED\n" + "".join(f"//!BIND {b}\n" for b in binds) +
               "//!SAVE DIAG_TAP\n//!WIDTH HOOKED.w 8 /\n//!HEIGHT HOOKED.h 8 /\n//!COMPONENTS 2\n//!DESC [diag] tap\n"
               f"vec4 hook() {{\n    vec2 p = HOOKED_pos;\n    ivec2 c8 = ivec2(gl_FragCoord.xy);\n    return vec4({expr}, 0.0, 0.0);\n}}\n\n")
        t = t[:nxt] + tap + t[nxt:]
        a = "//!BIND HOOKED\n//!BIND FLOW_H_AB\n//!SAVE READ_FIELD\n"; assert t.count(a) == 1
        t = t.replace(a, "//!BIND HOOKED\n//!BIND DIAG_TAP\n//!SAVE READ_FIELD\n")
        b = "    return vec4(FLOW_H_AB_tex(HOOKED_pos).xy * 2.0, 0.0, 1.0);\n"; assert t.count(b) == 1
        t = t.replace(b, "    return vec4(texelFetch(DIAG_TAP_raw, ivec2(gl_FragCoord.xy), 0).xy, 0.0, 1.0);\n")
    return t


def run(shader):
    (work / "_d.glsl").write_text(shader)
    r = subprocess.run([FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo",
                        "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf",
                        "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_d.glsl,format=rgb48le",
                        "-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], cwd=work, capture_output=True)
    assert r.returncode == 0 and b"compile status" not in r.stderr, r.stderr[:300]
    f = np.frombuffer(r.stdout, np.uint16).reshape(-1, H, W, 3)[:, 4::8, 4::8, :2].astype(np.float64)
    return (f / 65535.0 - 0.5) * 64.0                                 # (frames, 90, 160, 2) px


Q = "texelFetch(FLOW_Q_AB_raw, ivec2(p * FLOW_Q_AB_size), 0).xy * 4.0"
h_in = run(tapped(VAR, "[alias] each quarter-level cell takes its cheaper hypothesis over the four scans (BA)", ["FLOW_Q_AB"], Q))
dec = run(tapped(VAR, "[trust] the first honest level (AB)", ["TG_AB"], "texelFetch(TG_AB_raw, c8, 0).xy * 4.0"))
flag = run(tapped(VAR, "[trust] the first honest level (AB)", ["TG_AB"], "vec2(texelFetch(TG_AB_raw, c8, 0).z * 10.0, 0.0)"))[..., 0] > 5
fv, fc = run(tapped(VAR, None, [], None)), run(tapped(CTL, None, [], None))
n = min(len(h_in), len(dec), len(fv), len(fc))
ys, xs = np.mgrid[0:90, 0:160]
dx, dy = xs * 8 + 4.5 - CX, ys * 8 + 4.5 - CY
rad = np.hypot(dx, dy)


def truth(k0, k1):
    """the displacement of a material point from frame k0 to frame k1 at the cell centres"""
    t0, t1 = 2.56 * (k0 / 24.0) ** 2, 2.56 * (k1 / 24.0) ** 2
    ph = t0 - t1                                                       # d1 = M(t0 - t1) d0, M = [[c, s], [-s, c]]
    c, s = np.cos(ph), np.sin(ph)
    return np.stack([c * dx + s * dy - dx, -s * dx + c * dy - dy], axis=-1)


def err(f, k, conv):
    tr = truth(k, k + 1) if conv == 0 else truth(k - 1, k)
    return np.hypot(*(f[k] - tr).transpose(2, 0, 1))


conv = min((0, 1), key=lambda c: np.median([np.median(err(fc, k, c)[(rad < 60)]) for k in range(3, n - 3)]))
print(f"pairing: frame k with {'k + 1' if conv == 0 else 'k - 1'}; {n} frames")
print(f"{'band':>10s} | {'replaced':>8s} | {'flow in: err':>12s} {'replacement':>11s} (median, replaced cells) | "
      f"{'final: trust':>12s} {'control':>8s} (median err)  gross trust / control")
for lo, hi in ((0, 50), (50, 90), (90, 130)):
    rep, ein, erp, ev, ec, gv, gc = [], [], [], [], [], [], []
    for k in range(3, n - 3):
        m = (rad >= lo) & (rad < hi)
        e_in, e_dec, e_v, e_c = err(h_in, k, conv), err(dec, k, conv), err(fv, k, conv), err(fc, k, conv)
        r = flag[k] & m
        rep.append(r.sum() / m.sum()); ein += list(e_in[r]); erp += list(e_dec[r])
        ev += list(e_v[m]); ec += list(e_c[m])
    ev, ec = np.array(ev), np.array(ec)
    md = lambda a: f"{np.median(a):6.2f}" if len(a) else "    --"
    print(f"{lo:4d}-{hi:<4d} px | {100 * np.mean(rep):7.1f}% | {md(ein):>12s} {md(erp):>11s}                          | "
          f"{md(ev):>12s} {md(ec):>8s}               {100 * (ev > 2).mean():5.1f}% / {100 * (ec > 2).mean():5.1f}%")
