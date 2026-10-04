"""ENERGY-TRANSFER.md 3.6b: do the census's flagged frames matter? The half-rate test, real ground truth, no camera.

    halfrate.py <census log> [stem=bidirectional-interpolation-variational-propagated-global-cage-energy-carry]

For every extract the census scanned (the same seeded choice of sources and the same start times, from its log): keep
the EVEN frames (12 fps from 24), interpolate the odd frames back with the shader through libplacebo, and score each
output frame against the REAL frame, PSNR-Y (ffmpeg's psnr, 1280 wide). An odd frame n is labelled:
  short  -- the census flagged n - 1 or n inside a run of <= 4 frames (impact-like)
  long   -- ... inside a longer run (oscillation, flicker, alias)
  none   -- neither
Numbers only; runs in the research container with the footage mounted read-only at /footage (FOOTAGE names
another root). PER_FRAME=<file> (2026-10-01) also writes every odd frame's PSNR-Y, one row per frame (source, t0, k,
label, PSNR), so two shaders can be compared frame by frame: a change that touches a few frames (a cut gate) does
not move a median.
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
SHADERS = HERE.parents[3] / "shaders"
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
WORK = pathlib.Path(os.environ.get("CENSUS_WORK", "/tmp/census")); WORK.mkdir(parents=True, exist_ok=True)
log = sys.argv[1]
stem = sys.argv[2] if len(sys.argv) > 2 else "bidirectional-interpolation-variational-propagated-global-cage-energy-carry"
(WORK / "_interp.glsl").write_text((pathlib.Path(stem) if stem.endswith(".glsl") else SHADERS / f"{stem}.glsl").read_text())   # a path, or a stem
V = (".mkv", ".mp4", ".m4v", ".avi", ".mov")


def pick(root, n, seed):                                   # the census driver's choice, verbatim
    folders = sorted(p for p in pathlib.Path(root).iterdir() if p.is_dir())
    out = []
    for f in random.Random(seed).sample(folders, min(n, len(folders))):
        vids = [p for p in f.rglob("*") if p.suffix.lower() in V and p.stat().st_size > 50e6]
        if vids: out.append(max(vids, key=lambda p: p.stat().st_size))
    return out


FOOTAGE = os.environ.get("FOOTAGE", "/footage")                 # the footage pool, read-only (the container's mount)
paths = {p.stem: p for p in pick(f"{FOOTAGE}/Movies", 12, 20260930) + pick(f"{FOOTAGE}/Anime", 4, 20260930)
         + pick(f"{FOOTAGE}/Shows", 4, 20260930)}


def runs(frames):
    out, cur = [], []
    for k in sorted(frames):
        if cur and k == cur[-1] + 1: cur.append(k)
        else:
            if cur: out.append(cur)
            cur = [k]
    if cur: out.append(cur)
    return out


tot = {"none": [], "short": [], "long": []}
PF = open(os.environ["PER_FRAME"], "w") if os.environ.get("PER_FRAME") else None
ALLF = []                                                   # (motion proxy, label, psnr) for the matched comparison
print(f"{'source':50s} {'t0':>6s} | {'none':>13s} {'short':>13s} {'long':>13s}   median PSNR-Y dB (count)")
for line in open(log):
    if not line.startswith("JSON "): continue
    d = json.loads(line[5:])
    video = paths.get(d["video"])
    if video is None: print(f"  (no path for {d['video']})"); continue
    for ex in d["extracts"]:
        t0, n = ex["t0"], ex["frames"]
        secs = (n + 4) / 24.0
        short, long_ = set(), set()
        for r in runs(ex["local_at"]):
            (short if len(r) <= 4 else long_).update(r)
        stats = WORK / "halfrate.psnr"
        fc = (f"[0:v]scale=1280:-2,setpts=N/24/TB,select='not(mod(n\\,2))',setpts=N/12/TB,format=yuv420p,"
              f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_interp.glsl,format=yuv420p[ip];"
              f"[1:v]scale=1280:-2,setpts=N/24/TB,format=yuv420p[or];[ip][or]psnr=stats_file=halfrate.psnr")
        subprocess.run([FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk",
                        "-ss", f"{t0:.2f}", "-t", f"{secs:.2f}", "-i", str(video),
                        "-ss", f"{t0:.2f}", "-t", f"{secs:.2f}", "-i", str(video),
                        "-filter_complex", fc, "-f", "null", "-"], cwd=WORK, capture_output=True)
        # THE MOTION PROXY (the confound: the detector needs fast motion, and fast frames are harder anyway): the mean
        # absolute difference between the two real frames an odd frame bridges (n - 1, n + 1), on a 160-wide thumbnail
        raw = subprocess.run([FF, "-v", "error", "-ss", f"{t0:.2f}", "-t", f"{secs:.2f}", "-i", str(video),
                              "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
        th = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(np.float32) / 255
        ps = {}
        for l in stats.read_text().splitlines():
            m = re.match(r"n:(\d+) .*psnr_y:([\d.inf]+)", l)
            if m: ps[int(m.group(1)) - 1] = float(m.group(2)) if m.group(2) != "inf" else 99.0
        groups = {"none": [], "short": [], "long": []}
        # THE CONTROL (the PSNR-alignment trap): even output frames ARE source frames, so they must score high; a low
        # even median means the two streams are misaligned and every odd number is nonsense
        even = [v for k, v in ps.items() if k % 2 == 0 and 6 <= k <= n - 6]
        for k, v in ps.items():
            if k % 2 == 0 or k < 6 or k > n - 6: continue       # odd frames only: the interpolated ones
            lab = "long" if (k - 1 in long_ or k in long_) else "short" if (k - 1 in short or k in short) else "none"
            groups[lab].append(v)
            if PF: PF.write(f"{d['video'][:48]}\t{t0:.0f}\t{k}\t{lab}\t{v:.3f}\n")
            if 0 < k < len(th) - 1: ALLF.append((float(np.abs(th[k + 1] - th[k - 1]).mean()), lab, v))
        for g in groups: tot[g] += groups[g]
        cell = lambda g: f"{np.median(groups[g]):6.2f} ({len(groups[g]):3d})" if groups[g] else "     --      "
        ctrl = np.median(even) if even else float("nan")
        print(f"{d['video'][:48]:50s} {t0:6.0f} | {cell('none')} {cell('short')} {cell('long')}   even (control) {ctrl:6.2f}"
              + ("   ALIGNMENT?" if ctrl < 40 else ""), flush=True)
cellt = lambda g: f"{np.median(tot[g]):6.2f} ({len(tot[g])})" if tot[g] else "--"
print(f"\nALL odd frames: none {cellt('none')}; short (impact-like) {cellt('short')}; long {cellt('long')}")
# THE MATCHED COMPARISON: odd frames in five bands of the motion proxy (quintiles over all), labels compared WITHIN a band
if ALLF:
    mp = np.array([a[0] for a in ALLF]); edges = np.percentile(mp, [0, 20, 40, 60, 80, 100])
    print("\nmotion-matched (quintiles of the bridged pair's mean abs difference): median PSNR-Y (count)")
    print(f"{'band':>16s} | {'none':>13s} {'short':>13s} {'long':>13s} | short-none  long-none")
    ds, dl = [], []
    for b in range(5):
        lo, hi = edges[b], edges[b + 1]
        sel = [a for a in ALLF if lo <= a[0] <= hi]
        g = {lab: [a[2] for a in sel if a[1] == lab] for lab in ("none", "short", "long")}
        med = {lab: (np.median(v) if len(v) >= 10 else float("nan")) for lab, v in g.items()}
        c = lambda lab: f"{med[lab]:6.2f} ({len(g[lab]):4d})"
        print(f"{lo:7.4f}-{hi:7.4f} | {c('none')} {c('short')} {c('long')} | {med['short'] - med['none']:+9.2f}  {med['long'] - med['none']:+9.2f}")
        if not np.isnan(med["short"] - med["none"]): ds.append(med["short"] - med["none"])
        if not np.isnan(med["long"] - med["none"]): dl.append(med["long"] - med["none"])
    print(f"mean within-band gap: short {np.mean(ds):+.2f} dB over {len(ds)} bands; long {np.mean(dl):+.2f} dB over {len(dl)} bands")
