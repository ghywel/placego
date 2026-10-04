#!/usr/bin/env python3
"""C2's study (2026-10-01): on real footage, does the final flow EXPLAIN the frames' difference where the cut gate fires?

    cutstat.py <out.tsv> files <video> [<video> ...]     each whole file (SECS caps the length)
    cutstat.py <out.tsv> census <census log>             the census's 40 extracts (halfrate.py's sources; FOOTAGE)
    cutstat.py summary <tsv> [<tsv> ...]                 the tables again, over several runs' rows

Every source runs as halfrate.py feeds it (scale=1280:-2, timestamps forced to 24 fps) through a diagnostic copy of the
player's default (STEM, default the shipped file) with tests/cut_motion.py's SCENE_RES pass added and its numbers
copied into the reading tail (read_view 4): x = the cut statistic (SCENE_DIFF) x 100 - 16, y = SCENE_RES's ratio
(what the final flow leaves of the difference, over the difference unmoved) x 20 - 16. It runs at 48 fps, so output
frame 2k + 1 lies inside the pair (k, k + 1); an 8 x 8 crop at the centre is read. The ground truth is ffmpeg's scdet
score for frame k + 1 (its change from k): a CUT at 10 or more (its default threshold), NOT one under 5, ambiguous
between. Written: one row per pair (source, k, statistic, ratio, score); printed: the gate's firings split by the
truth, the ratio's spread in each, and for each candidate CUT_EXPLAINED the cuts still held and the non-cuts released.
A segment's first pair (k = 0) is left out of every table: scdet has no earlier difference to compare it with, and
scores it as a change from nothing (a synthetic pan's first pair read as a "cut").
"""
import json
import os
import pathlib
import random
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
sys.path.insert(0, str(TESTS))
import cut_motion                                                                # noqa: E402

FF = os.environ.get("FFMPEG", str(pathlib.Path.home() / "np-build/ffmpeg/ffmpeg"))
FFPROBE = os.environ.get("FFPROBE", FF[:-6] + "ffprobe" if FF.endswith("ffmpeg") else "ffprobe")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
STEM = os.environ.get("STEM", str(TESTS.parent / "shaders" /
                                  "bidirectional-interpolation-variational-propagated-global-cage-energy-carry-adopt-lattice.glsl"))
SUMMARY = sys.argv[1] == "summary"
out = pathlib.Path(sys.argv[2 if SUMMARY else 1]).resolve()
WORK = out.parent / (out.stem + "-work")
if not SUMMARY: WORK.mkdir(parents=True, exist_ok=True)

# the diagnostic shader
t = cut_motion.add_scene_res(pathlib.Path(STEM).read_text())
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
a = "//!DESC [cut] the scene-cut statistic, motion-compensated"
nxt = t.index("\n//!HOOK", t.index(a)) + 1
tap = ("//!HOOK FRAME_MIX\n//!BIND HOOKED\n//!BIND SCENE_DIFF\n//!BIND SCENE_RES\n//!SAVE DIAG_TAP\n//!WIDTH HOOKED.w 8 /\n"
       "//!HEIGHT HOOKED.h 8 /\n//!COMPONENTS 2\n//!DESC [diag] the cut statistic and the motion-compensated ratio\n"
       "vec4 hook() {\n    vec2 r = SCENE_RES_tex(vec2(0.5)).rg;\n"
       "    return vec4(SCENE_DIFF_tex(vec2(0.5)).r * 100.0 - 16.0, r.r / max(r.g, 1.0e-4) * 20.0 - 16.0, 0.0, 0.0);\n}\n\n")
t = t[:nxt] + tap + t[nxt:]
b = "//!BIND HOOKED\n//!BIND FLOW_H_AB\n//!SAVE READ_FIELD\n"; assert t.count(b) == 1
t = t.replace(b, "//!BIND HOOKED\n//!BIND DIAG_TAP\n//!SAVE READ_FIELD\n")
b = "    return vec4(FLOW_H_AB_tex(HOOKED_pos).xy * 2.0, 0.0, 1.0);\n"; assert t.count(b) == 1
t = t.replace(b, "    return vec4(DIAG_TAP_tex(HOOKED_pos).xy, 0.0, 1.0);\n")
if not SUMMARY: (WORK / "_cut.glsl").write_text(t)


def segment(video, t0, secs):
    """[(k, statistic, ratio, score)] for the pairs (k, k + 1) of the segment"""
    w, h = [int(x) for x in subprocess.run([FFPROBE, "-v", "error", "-select_streams", "v:0", "-show_entries",
                                            "stream=width,height", "-of", "csv=p=0", str(video)],
                                           capture_output=True, text=True).stdout.strip().split(",")[:2]]
    H = int(round(1280 * h / w / 2)) * 2
    cut = ["-ss", f"{t0:.2f}"] + (["-t", f"{secs:.2f}"] if secs else [])
    r = subprocess.run([FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", *cut, "-i", str(video),
                        "-vf", f"scale=1280:-2,setpts=N/24/TB,format=yuv420p,libplacebo=fps=48:frame_mixer=custom_n:"
                               f"custom_shader_path=_cut.glsl,format=rgb48le,crop=8:8:636:{H // 2 - 4}",
                        "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"], cwd=WORK, capture_output=True)
    if r.returncode or b"compile status" in r.stderr: sys.exit(f"ffmpeg failed: {r.stderr[:300]}")
    px = np.frombuffer(r.stdout, np.uint16).reshape(-1, 8, 8, 3)[:, 4, 4, :2].astype(np.float64)
    u = (px / 65535.0 - 0.5) * 64.0
    sd, ra = (u[:, 0] + 16.0) / 100.0, (u[:, 1] + 16.0) / 20.0
    m = subprocess.run([FF, "-v", "error", *cut, "-i", str(video), "-vf",
                        "scale=1280:-2,setpts=N/24/TB,scdet=threshold=10,metadata=print:file=-", "-f", "null", "-"],
                       capture_output=True, text=True).stdout
    scores = [float(x) for x in re.findall(r"lavfi\.scd\.score=([\d.]+)", m)]
    rows = []
    for k in range(len(scores) - 1):
        j = 2 * k + 1
        if j >= len(sd): break
        rows.append((k, float(sd[j]), float(ra[j]), scores[k + 1]))
    return rows


jobs = []
if SUMMARY: pass
elif sys.argv[2] == "files":
    for v in sys.argv[3:]: jobs.append((pathlib.Path(v).name, pathlib.Path(v).resolve(), 0.0, float(os.environ.get("SECS", "0"))))
else:
    V = (".mkv", ".mp4", ".m4v", ".avi", ".mov")

    def pick(root, n, seed):                                       # the census driver's choice, verbatim
        folders = sorted(p for p in pathlib.Path(root).iterdir() if p.is_dir())
        o = []
        for f in random.Random(seed).sample(folders, min(n, len(folders))):
            vids = [p for p in f.rglob("*") if p.suffix.lower() in V and p.stat().st_size > 50e6]
            if vids: o.append(max(vids, key=lambda p: p.stat().st_size))
        return o
    FOOTAGE = os.environ.get("FOOTAGE", "/footage")
    paths = {p.stem: p for p in pick(f"{FOOTAGE}/Movies", 12, 20260930) + pick(f"{FOOTAGE}/Anime", 4, 20260930)
             + pick(f"{FOOTAGE}/Shows", 4, 20260930)}
    for line in open(sys.argv[3]):
        if not line.startswith("JSON "): continue
        d = json.loads(line[5:])
        if d["video"] not in paths: continue
        for ex in d["extracts"]:
            jobs.append((f"{d['video'][:40]}@{ex['t0']:.0f}", paths[d["video"]], ex["t0"], (ex["frames"] + 4) / 24.0))

allr = []
if SUMMARY:
    for p in sys.argv[2:]:
        for line in open(p).read().splitlines()[1:]:
            c = line.split("\t")
            allr.append((int(c[1]), float(c[2]), float(c[3]), float(c[4])))
else:
  with open(out, "w") as f:
    f.write("source\tk\tstatistic\tratio\tscore\n")
    for name, video, t0, secs in jobs:
        rows = segment(video, t0, secs)
        for k, sd, ra, sc in rows:
            f.write(f"{name}\t{k}\t{sd:.4f}\t{ra:.4f}\t{sc:.3f}\n")
        rows = [r for r in rows if r[0] > 0]
        fired = [r for r in rows if r[1] > 0.125]
        print(f"{name:46s} pairs {len(rows):5d}  cuts {sum(r[3] >= 10 for r in rows):3d}  gate fires {len(fired):3d} "
              f"(on cuts {sum(r[3] >= 10 for r in fired)})", flush=True)
        allr += rows

A = np.array([r[1:] for r in allr if r[0] > 0])
sd, ra, sc = A[:, 0], A[:, 1], A[:, 2]
fire = sd > 0.125
cut, notcut = sc >= 10, sc < 5
print(f"\nALL: {len(A)} pairs; cuts (score >= 10) {cut.sum()}, ambiguous (5-10) {((sc >= 5) & (sc < 10)).sum()}")
print(f"the gate fires on {fire.sum()}: cuts {(fire & cut).sum()} (recall {100 * (fire & cut).sum() / max(cut.sum(), 1):.0f}%), "
      f"non-cuts {(fire & notcut).sum()}, ambiguous {(fire & ~cut & ~notcut).sum()}")
q = lambda x: " ".join(f"{v:.2f}" for v in np.percentile(x, [0, 10, 50, 90, 100])) if len(x) else "--"
print(f"the ratio where the gate fires, percentiles 0/10/50/90/100:  cuts  {q(ra[fire & cut])}")
print(f"                                                            non-cuts  {q(ra[fire & notcut])}")
print(f"the ratio on every cut (fired or not):                               {q(ra[cut])}")
print(f"\n{'CUT_EXPLAINED':>13s} | cuts the gate fires on, still held | non-cuts it fires on, released")
for thr in (0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8):
    held = (fire & cut & (ra > thr)).sum(); rel = (fire & notcut & (ra <= thr)).sum()
    print(f"{thr:13.1f} | {held:4d} of {(fire & cut).sum():4d} | {rel:4d} of {(fire & notcut).sum():4d}")
