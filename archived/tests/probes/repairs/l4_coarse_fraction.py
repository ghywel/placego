#!/usr/bin/env python3
"""l4_coarse_fraction.py <workdir> [shader.glsl] [cases]: REPAIRS.md lead L4's cheap first step (2026-10-04).

The base's coarse search (1/16 resolution) steps 0.75, 0.375, 0.1875, 0.09375 and 0.046875 of its own texels, so its
result is m * 3/64 coarse texel for a whole number m, which is 0.75 m full-resolution px; the refine levels add whole
texels (2n px at the finest), so the base's flow is 0.75 m + 2n px. A motion of exactly 16 px/frame is then reachable
only if the coarse search returns m = 0 (mod 8). Its natural nearest answers are m = 21 or 22 (15.75 or 16.5 px).

This reads FLOW_S_AB raw: the shader's final pass (the reading tail's painter) is replaced by a dump of the 1/16
level's flow at each coarse cell's centre, rendered N:N (24 -> 24) to rgb48le, and decoded per coarse cell. The units
are CHECKED before anything is counted: every decoded value must be a whole number of 3/64 coarse texel (a wrong scale
or a bilinear blend would fail it). Counted over the moving cells (|flow| > 0.5 coarse texel) after a warm-up.

PREDICTION (REPAIRS.md, written before the run): on the four 16 px/frame cases m is mostly 21 or 22, and m = 0 (mod 8)
is rare. REFUTED by: m = 0 (mod 8) on most moving cells.
"""
import os, pathlib, re, subprocess, sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
TESTS = HERE.parents[1]
STEP = 3.0 / 64.0                       # the coarse search's finest step, in coarse texels
W, H, FPS, FRAMES, SKIP = 1280, 720, 24, 24, 4
FS = float(os.environ.get("FS", "8"))      # encoding: 0.5 + v / FS, v in coarse texels (+-4). The output passes an fp16 stage (1/2048 near 0.5): at FS 64 that rounded v to 1/32 coarse texel and the units check failed, rightly; at 8 it resolves 1/256


def probe_shader(src, dst):
    text = pathlib.Path(src).read_text(encoding="utf-8")
    i = text.rfind("vec4 hook() {")
    head = text.rfind("//!HOOK FRAME_MIX\n", 0, i)
    header = text[head:i]
    assert "//!WHEN read_view 0 >\n" in header and "//!BIND FRAME_MIX\n" in header, header[:300]
    tex = os.environ.get("LEVEL", "FLOW_S_AB")
    assert f"//!SAVE {tex}\n" in text
    header = header.replace("//!WHEN read_view 0 >\n", "")
    header = "".join(ln + "\n" for ln in header.splitlines() if not ln.startswith("//!BIND READ_"))
    header = header.replace("//!BIND FRAME_MIX\n", f"//!BIND FRAME_MIX\n//!BIND {tex}\n", 1)
    body = ("vec4 hook() {\n"
            f"    vec2 s = (floor(FRAME_MIX_pos * {tex}_size) + 0.5) / {tex}_size;   // the cell's own centre\n"
            f"    vec2 f = {tex}_tex(s).xy;\n    return vec4(0.5 + f / {FS}, 0.5, 1.0);\n}}\n")
    pathlib.Path(dst).write_text(text[:head] + header + body, encoding="utf-8", newline="\n")


def scene(case):
    r = subprocess.run(["bash", "-c", f'. "{TESTS}/scenes.sh"; scene {case} {FPS}'], capture_output=True, text=True)
    return r.stdout.strip()


def main():
    wd = pathlib.Path(sys.argv[1]); wd.mkdir(parents=True, exist_ok=True)
    src = (sys.argv[2] if len(sys.argv) > 2 else "") or str(TESTS.parent / "shaders" / "bidirectional-interpolation.glsl")
    cases = sys.argv[3].split(",") if len(sys.argv) > 3 else ["L7_textured_large", "M1_noise_large", "M2_period40",
                                                             "M3_period16_trap"]
    ff = os.environ.get("FFMPEG", "ffmpeg")
    shader = wd / "probe_flow_s.glsl"
    probe_shader(src, shader)
    env = dict(os.environ)
    if sys.platform == "darwin":
        env.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
        env.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
    print(f"shader {pathlib.Path(src).name}; m in units of 3/64 coarse texel (0.75 px); 16 px/frame = m 21.33")
    for case in cases:
        raw = wd / f"{case}.rgb48"
        p = subprocess.run([ff, "-nostdin", "-y", "-hide_banner", "-loglevel", "error", "-init_hw_device", "vulkan=vk",
                            "-filter_hw_device", "vk", "-f", "lavfi", "-i", scene(case), "-frames:v", str(FRAMES),
                            "-vf", f"libplacebo=fps={FPS}:frame_mixer=custom_n:custom_shader_path={shader},format=rgb48le",
                            "-f", "rawvideo", str(raw)], env=env, capture_output=True, text=True)
        a = np.fromfile(raw, dtype="<u2")
        n = a.size // (W * H * 3)
        if n < SKIP + 2:
            print(f"  {case}: only {n} frames ({p.stderr.strip()[:200]})"); continue
        a = a[:n * W * H * 3].reshape(n, H, W, 3).astype(np.float64) / 65535.0
        cells = a[SKIP:, 8::16, 8::16, :2]                       # one sample per coarse cell, at its centre
        v = (cells - 0.5) * FS                                    # coarse texels
        mx = v[..., 0] / STEP
        resid = np.abs(mx - np.round(mx))
        moving = np.abs(v[..., 0]) > 0.5
        if moving.sum() == 0:
            print(f"  {case}: no moving cells"); continue
        units_ok = np.percentile(resid[moving], 99) < 0.02
        m = np.round(mx[moving]).astype(int)
        mod8 = np.mean(m % 8 == 0)
        vals, cnt = np.unique(m, return_counts=True)
        top = sorted(zip(cnt, vals), reverse=True)[:4]
        print(f"  {case:18s} {moving.sum():5d} moving cells; units {'OK' if units_ok else 'FAIL (p99 resid %.3f)' % np.percentile(resid[moving], 99)}; "
              f"m = 0 (mod 8): {mod8 * 100:5.1f}%; commonest m: " +
              ", ".join(f"{v} ({c * 100 / moving.sum():.0f}%, {0.75 * v:.2f} px)" for c, v in top))


if __name__ == "__main__":
    main()
