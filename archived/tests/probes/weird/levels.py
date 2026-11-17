#!/usr/bin/env python3
"""WHICH PYRAMID LEVEL DO THE WRONG VECTORS COME FROM? (2026-09-10, the third cheap test.)

flowvis.py replaces a shader's final hook() with a dump of FLOW_H_AB, the finest level's flow. The shader
saves its flow at EVERY level, so the same trick exposes each one: FLOW_S_AB (1/16 res), FLOW_E_AB_RAW (1/8,
before propagation), FLOW_E_AB (1/8, after), FLOW_Q_AB (1/4), FLOW_H_AB (1/2). Each is stored in its own
level's texel units, so it is scaled by the level factor to full-resolution px per source frame (flowvis
multiplies H by 2.0, which is the precedent). Encoded as 0.5 + f * 0.5/32, the same +-32 px full scale as
read_view 4, so weird.load decodes it unchanged.

Scored on three scenes against the analytic truth: the spiral, which reads to 1% at the output and is the
UNITS CHECK (a wrong level scale shows as a gain of 8 or 0.5); and the jelly and vortex at their failing
rates. The number per level is the failing fraction: samples whose direction is >45 degrees off, among
truth speeds >1 px/frame. If the fraction is already there at S, the coarse search is where it enters; if it
appears at E, propagation; if only at Q or H, refinement.

  levels.py shaders | render | score | all
"""
import os
import pathlib
import subprocess
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # weird.py is beside this file
import weird
from weird import G, SC, W, H, FPS, FRAMES, SKIP, FS_VEL, load

LEVELS = [("S", "FLOW_S_AB", 16.0), ("Eraw", "FLOW_E_AB_RAW", 8.0), ("E", "FLOW_E_AB", 8.0),
          ("Q", "FLOW_Q_AB", 4.0), ("Hh", "FLOW_H_AB", 2.0)]
SCENES = [("spiral", weird.spiral()), ("jellyK0.72", weird.jelly(0.72)), ("vortexW1.2", weird.vortex(1.2))]


def shaders():
    text = (SC / "shaders" / "quaddirectional-interpolation-propagated.glsl").read_text(encoding="utf-8")
    i = text.rfind("vec4 hook() {")
    assert i > 0
    for tag, name, scale in LEVELS:
        assert f"//!SAVE {name}\n" in text, name
        body = (f"vec4 hook() {{\n    vec2 f = {name}_tex(FRAME_MIX_pos).xy * {scale};\n"
                f"    return vec4(0.5 + f * (0.5 / {FS_VEL}), 0.5, 1.0);\n}}\n")
        # the final pass is the reading tail's painter: it neither binds the flow textures nor runs at all
        # when read_view is 0 (//!WHEN read_view 0 >). Bind the level's texture into it and drop the gate,
        # or the pass is skipped and the picture gets scored as a flow -- which happened, silently.
        head = text.rfind("//!HOOK FRAME_MIX\n", 0, i)
        header = text[head:i]
        assert "//!WHEN read_view 0 >\n" in header and "//!BIND FRAME_MIX\n" in header, header[:300]
        header = header.replace("//!WHEN read_view 0 >\n", "")
        # and drop the binds of the reading tail's own textures: their passes are gated on read_view too, so
        # they were never produced, and a pass whose bound texture does not exist is skipped without a word
        header = "".join(ln + "\n" for ln in header.splitlines() if not ln.startswith("//!BIND READ_"))
        header = header.replace("//!BIND FRAME_MIX\n", f"//!BIND FRAME_MIX\n//!BIND {name}\n", 1)
        assert header.count("//!BIND ") == 2, header
        (G / f"level_{tag}.glsl").write_text(text[:head] + header + body, encoding="utf-8", newline="\n")
        print(f"  level_{tag}.glsl <- {name} x {scale:g}")


def render(scene, expr, tag):
    out = G / f"{scene}_L{tag}"
    if out.exists():
        for f in out.glob("*.png"):
            f.unlink()
    out.mkdir(parents=True, exist_ok=True)
    esc = expr.replace(",", "\\,").replace(";", "\\;")
    graph = f"nullsrc=s={W}x{H}:r=24:d=3,format=gray,geq=lum='{esc}',format=yuv420p"
    r = subprocess.run(["ffmpeg.exe", "-y", "-hide_banner", "-loglevel", "error", "-init_hw_device", "vulkan=vk",
                        "-filter_hw_device", "vk", "-f", "lavfi", "-i", graph,
                        "-vf", f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=level_{tag}.glsl,format=rgb48le",
                        "-frames:v", str(FRAMES), str(out / "f%03d.png")], cwd=str(G), capture_output=True, text=True)
    n = len(list(out.glob("f*.png")))
    print(f"  {scene:11s} level {tag:4s} {n} frames" + ("" if n == FRAMES else f"  SHORT: {r.stderr[:200]}"), flush=True)
    assert n == FRAMES


def score():
    step = 4
    Y, X = np.mgrid[0:H, 0:W]
    Xs, Ys = X[::step, ::step].astype(float), Y[::step, ::step].astype(float)
    print(f"\n{'scene':12s} {'level':6s} {'u gain':>7} {'u corr':>7} {'v gain':>7} {'v corr':>7} {'resid':>7} {'failing':>8}")
    for scene, (expr, truth) in SCENES:
        for tag, name, scale in LEVELS:
            ru, rv, tu, tv = [], [], [], []
            for k in range(SKIP, FRAMES):
                tr = truth(k / FPS, Xs, Ys)
                m = tr["mask"]
                v = load(G / f"{scene}_L{tag}" / f"f{k + 1:03d}.png", FS_VEL)[::step, ::step]
                ru.append(v[..., 0][m]); rv.append(v[..., 1][m]); tu.append(tr["u"][m]); tv.append(tr["v"][m])
            ru, rv, tu, tv = map(np.concatenate, (ru, rv, tu, tv))
            fu, fv = weird.fit(ru, tu), weird.fit(rv, tv)
            moving = np.hypot(tu, tv) > 1.0
            ang = np.degrees(np.abs(np.arctan2(ru * tv - rv * tu, ru * tu + rv * tv)))
            failing = np.mean(ang[moving] > 45)
            resid = np.sqrt(np.mean((np.hypot(ru - tu, rv - tv))[moving] ** 2))
            print(f"{scene:12s} {tag:6s} {fu['gain']:7.3f} {fu['corr']:7.3f} {fv['gain']:7.3f} {fv['corr']:7.3f} {resid:7.2f} {failing:8.3f}")
        print()
    print("LEVELS DONE")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode in ("shaders", "all"):
        shaders()
    if mode in ("render", "all"):
        for scene, (expr, _) in SCENES:
            for tag, _, _ in LEVELS:
                render(scene, expr, tag)
    if mode in ("score", "all"):
        score()
