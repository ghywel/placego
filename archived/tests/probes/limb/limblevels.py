#!/usr/bin/env python3
"""WHICH PYRAMID LEVEL LOSES THE LIMB? K1 (textured still wall) against K2 (flat dark wall), level by level.

levels.py's trick (tests/probes/weird/): replace a shader's final hook with a dump of one level's saved flow --
FLOW_S_AB (1/16), FLOW_E_AB_RAW (1/8, before propagation), FLOW_E_AB (1/8, after), FLOW_Q_AB (1/4), FLOW_H_AB (1/2)
-- scaled to full-res px per source frame and encoded as 0.5 + f * 0.5 / FS (FS = 80 px: the limb reaches 60).
Rendered at N:N (24 -> 24), read back raw (rgb48le), and scored INSIDE THE LIMB at frame A against its known
displacement (the case's law, rounded per frame as overlay places it). Output k's pair is (k, k+1) (the engine's
N:N window; the alignment is checked: the other pairing is printed beside it and must lose).

    limblevels.py [shader.glsl]     default: the recommendation
Per level and speed band: the limb's median gain (the field projected on the truth), the share of its cells that
read under half the truth's length ("lost"), and the share within 20% ("held")."""
import os
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
TESTS = HERE.parent.parent
SC = TESTS.parent
FF = os.environ.get("FFMPEG", str(pathlib.Path(os.environ.get("FFDIR", str(pathlib.Path.home() / "np-build/ffmpeg"))) / "ffmpeg"))
NP = pathlib.Path(os.environ.get("NP_SCRATCH", str(SC.parent.parent / "np-scratch")))
G = NP / "limb" / "levels"
G.mkdir(parents=True, exist_ok=True)
W, H, FS = 1280, 720, 80.0
LEVELS = [("S", "FLOW_S_AB", 16.0), ("Eraw", "FLOW_E_AB_RAW", 8.0), ("E", "FLOW_E_AB", 8.0),
          ("Q", "FLOW_Q_AB", 4.0), ("H", "FLOW_H_AB", 2.0)]
SHADER = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].endswith(".glsl") else SC / "shaders" / "bidirectional-interpolation-variational-propagated.glsl"


def dumps():
    text = SHADER.read_text(encoding="utf-8")
    i = text.rfind("vec4 hook() {")
    head = text.rfind("//!HOOK FRAME_MIX\n", 0, i)
    header = text[head:i]
    assert "//!WHEN read_view 0 >\n" in header and "//!BIND FRAME_MIX\n" in header, header[:300]
    header = header.replace("//!WHEN read_view 0 >\n", "")
    header = "".join(ln + "\n" for ln in header.splitlines() if not ln.startswith("//!BIND READ_"))
    for tag, name, scale in LEVELS:
        assert f"//!SAVE {name}\n" in text, name
        h = header.replace("//!BIND FRAME_MIX\n", f"//!BIND FRAME_MIX\n//!BIND {name}\n", 1)
        assert h.count("//!BIND ") == 2, h
        body = (f"vec4 hook() {{\n    vec2 f = {name}_tex(FRAME_MIX_pos).xy * {scale};\n"
                f"    return vec4(0.5 + f * (0.5 / {FS}), 0.5, 1.0);\n}}\n")
        (G / f"level_{tag}.glsl").write_bytes((text[:head] + h + body).encode("utf-8"))


def scene(case):
    # an edge case first (scene_edge), else a ladder case (scene)
    out = subprocess.run(["bash", "-c", f". '{TESTS}/scenes.sh'; s=\"$(scene_edge {case} 24)\"; "
                          f"case \"$s\" in ''|UNKNOWN_CASE) s=\"$(scene {case} 24)\";; esac; echo \"$s\""],
                         capture_output=True, text=True)
    assert out.stdout.strip() and "UNKNOWN" not in out.stdout, out.stderr
    return out.stdout.strip()


def render(case, tag):
    raw = G / f"{case}_{tag}.rgb48"
    r = subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk",
                        "-f", "lavfi", "-i", scene(case), "-vf",
                        f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=level_{tag}.glsl,format=rgb48le",
                        "-f", "rawvideo", str(raw)], cwd=str(G), capture_output=True, text=True)
    a = np.fromfile(raw, dtype="<u2")
    n = a.size // (W * H * 3)
    assert n >= 20, f"{case} {tag}: {n} frames; {r.stderr[:300]}"
    a = a[: n * W * H * 3].reshape(n, H, W, 3).astype(np.float32) / 65535.0
    return (a[..., :2] - 0.5) * (2 * FS)                    # (n, H, W, 2) px per source frame


def xpos(k):                                                # overlay's x for source frame k (t = k / 24), rounded
    t = k / 24.0
    return int(round(100 + 288 * t + 576 * t * t))


def score(case, f, shift):
    """Per speed band: gain p50, lost share, held share, over the limb's cells at frame A = k + shift."""
    rows = []
    for k in range(2, f.shape[0] - 2):
        a, b = k + shift, k + shift + 1
        xa, xb = xpos(a), xpos(b)
        d = xb - xa
        if xa < 0 or xa + 48 > W:
            continue
        cells = f[k, 262:458:4, xa + 2:xa + 46:4]            # the limb's interior at frame A, 2 px in from its edge
        u = cells[..., 0].ravel()
        gain = u / d
        rows.append((d, np.median(gain), np.mean(gain < 0.5), np.mean(np.abs(gain - 1) < 0.2)))
    return np.array(rows)


if __name__ == "__main__":
    dumps()
    bands = [(12, 18), (18, 24), (24, 30), (30, 36), (36, 42), (42, 48), (48, 61)]
    cases = [a for a in sys.argv[2:] if a.startswith("K")] or ["K1_limb_sweep_wall", "K2_limb_sweep_dark"]
    for case in cases:
        print(f"\n== {case} ({SHADER.name}): per level, gain p50 / lost (<0.5) / held (within 20%) in the limb")
        print("level  pairing  " + "".join(f"{lo}-{hi} px/f".ljust(20) for lo, hi in bands))
        for tag, _, _ in LEVELS:
            f = render(case, tag)
            for shift, label in ((0, "(k,k+1)"), (-1, "(k-1,k)")):
                s = score(case, f, shift)
                cells = []
                for lo, hi in bands:
                    m = (s[:, 0] >= lo) & (s[:, 0] < hi)
                    cells.append(f"{np.median(s[m, 1]):5.2f}/{100 * s[m, 2].mean():3.0f}%/{100 * s[m, 3].mean():3.0f}%" if m.any() else "-")
                print(f"{tag:6} {label:8} " + "".join(c.ljust(20) for c in cells))
