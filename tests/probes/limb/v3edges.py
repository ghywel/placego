#!/usr/bin/env python3
"""WHERE DOES V3's ANSWER LIVE, AND DOES IT SPREAD? The half-period alias (V3_stairs_sq24_v12: 13 bright bars, period 24,
on black, 300 x 300, moving DOWN 12 px a frame) is decided by its two END bars alone: under the true +12 every bar has
a partner, under the alias -12 the top bar vanishes and a bottom one appears from nowhere. Everything between is a tie.
v3phase.sh found the committed shader bimodal over start phase (offset 108 held in 3 of 3 runs, 112 and 120 flipped in
3 of 3, the rest decided run to run by the Mac's own nondeterminism -- a true tie, broken by noise).

This draws, per frame and per pyramid level (limblevels.py's dumps: S, E before and after propagation, Q, H), the
field's vertical gain in each of the patch's 13 bar-bands from the top edge down: '+' within 40% of the truth, '-'
the alias (gain < -0.6), '0' near zero (|gain| < 0.3), '.' anything else. Columns 40 px in from the sides.

    v3edges.py <shader.glsl> [offset ...]      default offsets 108 (held) 112 (flipped)
    v3edges.py <shader.glsl> --up ...           the motion mirrored (up; gains still along the truth)
    v3edges.py <shader.glsl> --b1 [offset ...]   B1_alias_over_pan instead (200-px patch, 8 bands)
    v3edges.py <shader.glsl> 108 --cells 8     also every 1/8-level cell of the patch at frame 8, before and
                                               after the propagation (the vertical flow in px, one digit per
                                               cell: its value / 4 rounded, so 3 = +12, -3 = -12)"""
import pathlib
import subprocess
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import limblevels as LL  # noqa: E402

LAW = "100+288*T"
args = [a for a in sys.argv[1:]]
CASE, SIZE, NBANDS = "V3_stairs_sq24_v12", 300, 13
UPW = "--up" in args       # the motion mirrored: the patch starts 288 px lower and moves UP (truth -12)
if UPW:
    args.remove("--up")
if "--b1" in args:          # B1_alias_over_pan: the same bars in a 200-px patch over a panning background
    args.remove("--b1")
    CASE, SIZE, NBANDS, LAW = "B1_alias_over_pan", 200, 8, "100+288*t"
CELLS = None
if "--cells" in args:
    i = args.index("--cells"); CELLS = int(args[i + 1]); del args[i:i + 2]
shader = pathlib.Path(args[0])
offsets = [int(a) for a in args[1:]] or [108, 112]
LL.SHADER = shader
LL.dumps()
base = LL.scene(CASE)
assert base.count(LAW) in (1, 3), base


def render(off, tag):
    s = base.replace(LAW, f"{off + 288}{LAW[3:].replace('+', '-')}" if UPW else f"{off}{LAW[3:]}")
    raw = LL.G / f"v3e_{CASE[:2]}_{off}_{tag}.rgb48"
    r = subprocess.run([LL.FF, "-y", "-hide_banner", "-loglevel", "error", "-init_hw_device", "vulkan=vk",
                        "-filter_hw_device", "vk", "-f", "lavfi", "-i", s, "-vf",
                        f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=level_{tag}.glsl,format=rgb48le",
                        "-f", "rawvideo", str(raw)], cwd=str(LL.G), capture_output=True, text=True)
    a = np.fromfile(raw, dtype="<u2")
    n = a.size // (LL.W * LL.H * 3)
    assert n >= 20, f"{off} {tag}: {n} frames; {r.stderr[:300]}"
    a = a[: n * LL.W * LL.H * 3].reshape(n, LL.H, LL.W, 3).astype(np.float32) / 65535.0
    return (a[..., :2] - 0.5) * (2 * LL.FS)


def glyph(g):
    return "+" if abs(g - 1) < 0.4 else "-" if g < -0.6 else "0" if abs(g) < 0.3 else "."


for off in offsets:
    F = {tag: render(off, tag) for tag, _, _ in LL.LEVELS}
    n = min(f.shape[0] for f in F.values())
    print(f"\n== {shader.name}, {CASE[:2]} start offset {off}: gain per bar-band, top edge -> bottom edge")
    print("frame  " + "  ".join(f"{tag:{NBANDS}}" for tag, _, _ in LL.LEVELS) + "  whole-patch gain p50 per level")
    for k in range(2, n - 2):
        ya = off + 288 - 12 * k if UPW else off + 12 * k
        if ya + SIZE > LL.H:
            break
        row, meds = [], []
        for tag, _, _ in LL.LEVELS:
            v = F[tag][k, ya:ya + SIZE, 490 + 40:490 + SIZE - 40, 1] / (-12.0 if UPW else 12.0)   # the gain along the truth, rows of the patch at A
            band = [np.median(v[24 * b:24 * b + 24]) for b in range(NBANDS)]  # the last band is the last bar alone
            row.append("".join(glyph(g) for g in band))
            meds.append(np.median(v))
        print(f"{k:5}  " + "  ".join(f"{s:{NBANDS}}" for s in row) + "  " + " ".join(f"{m:+5.2f}" for m in meds))

    if CELLS is not None:
        k = CELLS; ya = off + 12 * k
        print(f"\n   cells at frame {k} (rows: 1/8-level cells top -> bottom of the patch; digit = round(v / 4); x = beyond +-9)")
        for tag in ("Eraw", "E"):
            f = F[tag][k]
            lines = []
            for cy in range(ya // 8, (ya + SIZE) // 8 + 1):
                row = ""
                for cx in range((490 + 40) // 8, (490 + SIZE - 40) // 8):
                    v = f[cy * 8 + 4, cx * 8 + 4, 1]
                    q = int(round(v / 4.0))
                    row += "x" if abs(q) > 9 else ("+" if q > 0 else "-" if q < 0 else " ") + str(abs(q))
                lines.append(row)
            print(f"   {tag}:")
            for ln in lines:
                print("     " + ln)
