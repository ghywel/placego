#!/usr/bin/env python3
"""WHAT THE CARRY SEES AT A PATTERN'S END (2026-09-28): B1 moving up holds 21.8 on the cage with the carry, moving down
25.3, and v3edges.py shows the 1/8 level choosing "down" in BOTH directions -- so moving down the carry has nothing to
do, and moving up it must carry the ends' answer through the whole patch, and only half does. This dumps, per quarter-
level cell of a shader built with ALIAS_CARRY, the carry's own inputs and output, so the ends can be read cell by cell:

    b1 / b2   the cell's two basins (ALIAS_Q1_AB_ST, ALIAS_Q_AB_ST.xy)
    state     f flat (breaks the scans), o one basin (a hard anchor), t tied (both data costs exactly 0),
              1 / 2 which basin is better by a margin (a soft anchor)
    h / out   the level's flow before the PICK and after it
    tot       which basin the four scans' sum prefers (1 / 2, '=' level)
Glyphs for a flow in quarter texels (12 px = 3): u = (0, -3), d = (0, +3), b = the background's (-2, 0), 0 = still,
'.' anything else; the truth is u moving up, d moving down.

    ownerdump.py <carry-shader.glsl> [--up] [--case B1_alias_over_pan] [--start 100] [--frames 8,9,10] [--numbers]
    --numbers   also the values themselves, at three columns, for the rows at the patch's two ends (first frame)

What it found (NFRAME-LIMITS.md, "The aperture in the carry"): the ends' cells held the right vertical answer with a
junk horizontal part, and the whole-vector penalty carried the clean wrong alias in from the top."""
import pathlib
import subprocess
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import limblevels as LL  # noqa: E402

args = sys.argv[1:]


def opt(name, default):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return default


UP = "--up" in args
if UP:
    args.remove("--up")
NUMBERS = "--numbers" in args
if NUMBERS:
    args.remove("--numbers")
CASE = opt("--case", "B1_alias_over_pan")
START = int(opt("--start", "100"))
FRAMES = [int(x) for x in opt("--frames", "8,9,10").split(",")]
SIZE = 200 if CASE.startswith("B1") else 300
LAW = "100+288*t" if CASE.startswith("B1") else "100+288*T"
shader = pathlib.Path(args[0])
text = shader.read_text(encoding="utf-8")
assert "//!SAVE ALIAS_Q_AB\n" in text, "not a carry shader"
SC = 64.0          # quarter texels: encoded 0.5 + v / (2 * SC)

# the PICK keeps the level's flow before it in ALIAS_OUT.zw (the cached path returns .xy, so the output is unchanged)
a = "    vec4 result = vec4(h, 0.0, 0.0);\n"
assert text.count(a) == 2, text.count(a)
text = text.replace(a, "    vec4 result = vec4(h, h);\n")
b4, b5 = "result = vec4(pick, 0.0, 0.0);", "result = vec4(pick + dot(h - pick, w) * w, 0.0, 0.0);"   # builds 4 / 5+
b, rb = (b4, "result = vec4(pick, h);") if text.count(b4) == 2 else (b5, "result = vec4(pick + dot(h - pick, w) * w, h);")
assert text.count(b) == 2, "the PICK's switch line is neither build 4's nor build 5's"
text = text.replace(b, rb)

i = text.rfind("vec4 hook() {")
head = text.rfind("//!HOOK FRAME_MIX\n", 0, i)
header = text[head:i]
assert "//!WHEN read_view 0 >\n" in header and "//!BIND FRAME_MIX\n" in header
header = header.replace("//!WHEN read_view 0 >\n", "")
header = "".join(ln + "\n" for ln in header.splitlines() if not ln.startswith("//!BIND READ_"))
binds = "".join(f"//!BIND {n}\n" for n in ("ALIAS_Q_AB_ST", "ALIAS_Q1_AB_ST", "ALIAS_OUT_AB_ST", "ALIAS_HF_AB_ST",
                                           "ALIAS_HB_AB_ST", "ALIAS_VF_AB_ST", "ALIAS_VB_AB_ST", "LUMA_A_Q"))
header = header.replace("//!BIND FRAME_MIX\n", "//!BIND FRAME_MIX\n" + binds, 1)
MODES = {
    "b1": "vec3(q1.xy, 0.0)",
    "b2": "vec3(q.xy, 0.0)",
    "st": "vec3(q.z, min(q.w, 30.0), tot.y - tot.x)",
    "ho": "vec3(o.zw, 0.0)",
    "ou": "vec3(o.xy, 0.0)",
}
G = LL.G
for m, expr in MODES.items():
    body = ("vec4 hook() {\n"
            "    ivec2 c = ivec2(FRAME_MIX_pos * LUMA_A_Q_size);\n"
            "    vec4 q = imageLoad(ALIAS_Q_AB_ST, c), q1 = imageLoad(ALIAS_Q1_AB_ST, c), o = imageLoad(ALIAS_OUT_AB_ST, c);\n"
            "    vec2 tot = imageLoad(ALIAS_HF_AB_ST, c).xy + imageLoad(ALIAS_HB_AB_ST, c).xy\n"
            "             + imageLoad(ALIAS_VF_AB_ST, c).xy + imageLoad(ALIAS_VB_AB_ST, c).xy - 3.0 * q.zw;\n"
            f"    vec3 v = {expr};\n"
            f"    return vec4(clamp(0.5 + v / {2 * SC}, 0.0, 1.0), 1.0);\n}}\n")
    (G / f"owner_{m}.glsl").write_bytes((text[:head] + header + body).encode("utf-8"))

base = LL.scene(CASE)
assert base.count(LAW) in (1, 3), base
s = base.replace(LAW, f"{START + 288}{LAW[3:].replace('+', '-')}" if UP else f"{START}{LAW[3:]}")


def render(m):
    raw = G / f"owner_{m}.rgb48"
    r = subprocess.run([LL.FF, "-y", "-hide_banner", "-loglevel", "error", "-init_hw_device", "vulkan=vk",
                        "-filter_hw_device", "vk", "-f", "lavfi", "-i", s, "-vf",
                        f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=owner_{m}.glsl,format=rgb48le",
                        "-f", "rawvideo", str(raw)], cwd=str(G), capture_output=True, text=True)
    x = np.fromfile(raw, dtype="<u2")
    n = x.size // (LL.W * LL.H * 3)
    assert n >= 20, f"{m}: {n} frames; {r.stderr[:400]}"
    x = x[: n * LL.W * LL.H * 3].reshape(n, LL.H, LL.W, 3).astype(np.float32) / 65535.0
    return (x - 0.5) * (2 * SC)


F = {m: render(m) for m in MODES}


def glyph(v):
    x, y = v
    near = lambda p, q: abs(x - p) <= 0.75 and abs(y - q) <= 0.75
    return "u" if near(0, -3) else "d" if near(0, 3) else "b" if near(-2, 0) else "0" if near(0, 0) else "."


def state(v):
    z, w, dt = v
    if z < -0.5:
        return "f"
    if w > 29:
        return "o"
    if abs(z) < 1e-3 and abs(w) < 1e-3:
        return "t"
    return "1" if z < w else "2"


print(f"== {shader.name}: {CASE} start {START} {'UP' if UP else 'DOWN'}; quarter-level cells from 3 above the patch "
      f"to 3 below, columns across it (every other cell)")
for k in FRAMES:
    ya = START + 288 - 12 * k if UP else START + 12 * k
    rows = range(ya // 4 - 3, (ya + SIZE) // 4 + 4)
    cols = range(490 // 4 - 3, (490 + SIZE) // 4 + 4, 2)
    print(f"\n-- frame {k}: patch rows {ya}..{ya + SIZE} (cells {ya // 4}..{(ya + SIZE) // 4})")
    print(f"{'cell':>5}  {'b1':{len(cols)}}  {'b2':{len(cols)}}  {'state':{len(cols)}}  {'scans':{len(cols)}}  "
          f"{'h':{len(cols)}}  {'out':{len(cols)}}")
    for r in rows:
        py = r * 4 + 2
        g = lambda m, fn, ch=None: "".join(fn(F[m][k, py, c * 4 + 2][:2] if ch is None else F[m][k, py, c * 4 + 2][ch])
                                           for c in cols)
        b1 = g("b1", glyph); b2 = g("b2", glyph)
        st = "".join(state(F["st"][k, py, c * 4 + 2]) for c in cols)
        sc = "".join("=" if abs(F["st"][k, py, c * 4 + 2][2]) < 1e-3 else ("2" if F["st"][k, py, c * 4 + 2][2] < 0 else "1")
                     for c in cols)
        h = "".join(glyph(F["ho"][k, py, c * 4 + 2][:2]) for c in cols)
        out = g("ou", glyph)
        mark = "<" if r == ya // 4 or r == (ya + SIZE) // 4 else " "
        print(f"{r:5}{mark} {b1}  {b2}  {st}  {sc}  {h}  {out}")

if NUMBERS:
    k = FRAMES[0]
    ya = START + 288 - 12 * k if UP else START + 12 * k
    print(f"\n-- frame {k}: numbers at columns 135, 145, 155 (quarter texels): b1 | b2 | D1 D2 | scans t2-t1 | h | out")
    for r in list(range(ya // 4 - 3, ya // 4 + 6)) + list(range((ya + SIZE) // 4 - 6, (ya + SIZE) // 4 + 3)):
        py = r * 4 + 2
        cells = []
        for c in (135, 145, 155):
            px = c * 4 + 2
            b1 = F["b1"][k, py, px]; b2 = F["b2"][k, py, px]; st = F["st"][k, py, px]; ho = F["ho"][k, py, px]; ou = F["ou"][k, py, px]
            cells.append(f"({b1[0]:+.0f},{b1[1]:+.0f})|({b2[0]:+.0f},{b2[1]:+.0f})|{st[0]:.2f} {st[1]:.2f}|{st[2]:+.2f}|({ho[0]:+.1f},{ho[1]:+.1f})|({ou[0]:+.1f},{ou[1]:+.1f})")
        print(f"{r:5} " + "   ".join(cells))
