"""ENERGY-TRANSFER.md 3.6c: the local test -- flagged CELLS against unflagged cells of the same speed.

    census_local.py <census log> [stem=bidirectional-interpolation-variational-propagated-global-cage-energy-carry]

3.6b compared whole frames and found the census's flagged frames no harder than any other frame moving as much. A
frame-level proxy cannot separate a local reversal from a pan, and a whole-frame PSNR dilutes a local cost. So, per
8-px cell, over the census's own seeded sources and extracts (read from its log; the same 45-s windows):
  1. the four-frame field at N:N, RGB in, 1280 wide: census.py's own reader and detector. The cell mask here must
     reproduce census.detect's cell count on EVERY frame, and its local frames must equal the log's (the guards);
  2. the half-rate interpolation (even frames kept, 12 -> 24, the Cadence default through libplacebo) against the
     REAL odd frames, luma (the Y plane of yuv420p, as the psnr filter reads it): each cell's mean squared error;
  3. an odd frame n bridges real frames n - 1 and n + 1; a cell is FLAGGED when the detector's core mask (after the
     3-of-8-neighbours rule) holds it at frame n - 1 or n in a frame classed local (16+ cells, not global).
     PRE = the mask before the neighbour rule (secondary);
  4. the matching variable is the cell's own speed: the mean of the field's |u| at n - 1 and n + 1 (one sample per
     cell: the field is computed on 8-px cells), in 2 px/frame bands up to 24;
  5. out: frames within 3 of a cut and the first and last 4 frames (the census's rules), cells within 16 px of the
     frame border, and any extract whose even frames (exact source frames) read under 40 dB (the alignment control).
Cell PSNRs go into 0.05-dB histograms per band and label, so medians are exact to 0.05 dB. Numbers only.
The control that must not move: the unflagged cells split at random into halves A and B, within 0.3 dB per band.
"""
import json
import os
import pathlib
import random
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
sys.argv, _argv = [sys.argv[0], "import"], sys.argv            # census.py acts on argv[1]; 'import' is neither mode
sys.path.insert(0, str(HERE.parent)); import census             # noqa: E402  (the census's own reader and detector)
sys.argv = _argv
SHADERS = HERE.parents[3] / "shaders"
FF = census.FF
WORK = census.WORK
log = sys.argv[1]
stem = sys.argv[2] if len(sys.argv) > 2 else "bidirectional-interpolation-variational-propagated-global-cage-energy-carry"
(WORK / "_interp.glsl").write_text((SHADERS / f"{stem}.glsl").read_text())
SECS = 45.0                                                     # the census driver's window (census.py film v 2 45 seed)
BANDS = np.arange(0, 26, 2.0)                                   # 0-2 ... 22-24
BINS = np.arange(0, 100.05, 0.05)
LABELS = ("flag", "pre", "A", "B")


def cellmask(F, k):
    """census.detect's per-cell test at frame k, verbatim: (q before the neighbour rule, core after it)"""
    a, b = F[k - 1], F[k + 2]
    d = b - a; dn = np.linalg.norm(d, axis=-1) + 1e-9
    ua, ub = (a * d).sum(-1) / dn, (b * d).sum(-1) / dn
    q = (ua < -census.VMIN) & (ub > census.VMIN) & (dn > census.DMIN) & (np.abs(ua + ub) < 0.5 * (ub - ua))
    a2, b3 = F[k - 2], F[k + 3]
    q &= (np.linalg.norm(a2 - a, axis=-1) < 0.5 * np.linalg.norm(a, axis=-1)) & \
         (np.linalg.norm(b3 - b, axis=-1) < 0.5 * np.linalg.norm(b, axis=-1))
    nb = sum(np.roll(np.roll(q, dy, 0), dx, 1) for dy in (-1, 0, 1) for dx in (-1, 0, 1)) - q
    return q, q & (nb >= 3)


V = (".mkv", ".mp4", ".m4v", ".avi", ".mov")


def pick(root, n, seed):                                        # the census driver's choice, verbatim
    folders = sorted(p for p in pathlib.Path(root).iterdir() if p.is_dir())
    out = []
    for f in random.Random(seed).sample(folders, min(n, len(folders))):
        vids = [p for p in f.rglob("*") if p.suffix.lower() in V and p.stat().st_size > 50e6]
        if vids: out.append(max(vids, key=lambda p: p.stat().st_size))
    return out


FOOTAGE = os.environ.get("FOOTAGE", "/footage")                 # the footage pool, read-only (the container's mount)
paths = {p.stem: p for p in pick(f"{FOOTAGE}/Movies", 12, 20260930) + pick(f"{FOOTAGE}/Anime", 4, 20260930)
         + pick(f"{FOOTAGE}/Shows", 4, 20260930)}


def ystream(cmd, fb):
    p = subprocess.Popen(cmd, cwd=WORK, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        yield buf
    p.wait()


H = {lab: np.zeros((len(BANDS) - 1, len(BINS) - 1)) for lab in LABELS}
per_src = []
rng = np.random.default_rng(20260930)
guard_fail = 0
for line in open(log):
    if not line.startswith("JSON "): continue
    d = json.loads(line[5:])
    video = paths.get(d["video"])
    if video is None: print(f"  (no path for {d['video']})", flush=True); continue
    pr = json.loads(subprocess.run([census.FP, "-v", "error", "-select_streams", "v:0", "-show_entries",
                                    "stream=width,height,r_frame_rate", "-of", "json", str(video)],
                                   capture_output=True, text=True).stdout)["streams"][0]
    w = 1280; h = int(round(int(pr["height"]) * w / int(pr["width"]) / 2)) * 2; fps = pr["r_frame_rate"]
    Hs = {lab: np.zeros_like(H[lab]) for lab in LABELS}
    for ex in d["extracts"]:
        t0 = ex["t0"]
        inargs = ["-ss", f"{t0:.2f}", "-t", f"{SECS}", "-i", str(video)]
        raw = subprocess.run([FF, "-v", "error"] + inargs + ["-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"],
                             capture_output=True).stdout
        th = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(np.float32) / 255
        cuts = {k for k in range(1, len(th)) if np.abs(th[k] - th[k - 1]).mean() > 0.12}
        F = list(census.field_frames(inargs, fps, w, h))
        rows = census.detect(F, frozenset(cuts))
        ch, cw = h // 8, w // 8
        flag = np.zeros((len(F), ch, cw), bool); pre = np.zeros_like(flag)
        # THE GUARDS: the mask reproduces census.detect's count on every frame, and the local frames equal the log's
        for k, n_ev, total, kind in rows:
            if total == 0: continue
            q, core = cellmask(F, k)
            if int(core.sum()) != n_ev: guard_fail += 1
            if kind == "local": flag[k] = core[:ch, :cw]; pre[k] = q[:ch, :cw]
        local_here = [r[0] for r in rows if r[3] == "local"]
        match = local_here == ex["local_at"]
        # the half-rate interpolation and the real frames, Y planes, in lockstep
        ip = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk"] + inargs + [
              "-vf", f"scale={w}:{h},setpts=N/24/TB,select='not(mod(n\\,2))',setpts=N/12/TB,format=yuv420p,"
                     f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_interp.glsl,format=yuv420p,extractplanes=y",
              "-fps_mode", "passthrough", "-f", "rawvideo", "-"]
        # -fps_mode passthrough on both (2026-09-30): without it each process's raw output was converted back to the
        # SOURCE's frame rate, and on the 25 and 29.97 fps sources the pairing slipped (the even-frame control read
        # 12-23 dB and dropped all six extracts). halfrate.py pairs inside one graph and never had the problem.
        rl = [FF, "-v", "error"] + inargs + ["-vf", f"scale={w}:{h},setpts=N/24/TB,format=yuv420p,extractplanes=y",
                                             "-fps_mode", "passthrough", "-f", "rawvideo", "-"]
        fb = w * h; even = []; n_cells = 0
        bad = {c + dk for c in cuts for dk in range(-3, 4)}
        spd = [np.linalg.norm(f, axis=-1)[:ch, :cw] for f in F]
        B = 2                                                    # 16 px of border, in cells
        for n, (bi, br) in enumerate(zip(ystream(ip, fb), ystream(rl, fb))):
            a = np.frombuffer(bi, np.uint8).reshape(h, w).astype(np.float32)
            r = np.frombuffer(br, np.uint8).reshape(h, w).astype(np.float32)
            if n % 2 == 0:
                if 6 <= n <= len(F) - 6 and n % 10 == 0:
                    mse = float(np.mean((a - r) ** 2)) / 255 ** 2; even.append(99.0 if mse == 0 else -10 * np.log10(mse))
                continue
            if n < 5 or n > len(F) - 6 or n + 1 >= len(F) or n in bad: continue
            e = ((a - r) ** 2)[:ch * 8, :cw * 8].reshape(ch, 8, cw, 8).mean(axis=(1, 3)) / 255 ** 2
            p = np.where(e > 0, -10 * np.log10(np.maximum(e, 1e-10)), 99.0)[B:-B, B:-B]
            s = ((spd[n - 1] + spd[n + 1]) / 2)[B:-B, B:-B]
            fl = (flag[n - 1] | flag[n])[B:-B, B:-B]; pr_ = (pre[n - 1] | pre[n])[B:-B, B:-B]
            half = rng.random(fl.shape) < 0.5
            bi_ = np.clip(np.digitize(s, BANDS) - 1, 0, len(BANDS) - 2); ok = s < BANDS[-1]
            for lab, m in (("flag", fl), ("pre", pr_), ("A", ~fl & half), ("B", ~fl & ~half)):
                m = m & ok
                if m.any(): np.add.at(Hs[lab], (bi_[m], np.clip(np.digitize(p[m], BINS) - 1, 0, len(BINS) - 2)), 1)
            n_cells += fl.size
        ctrl = float(np.median(even)) if even else float("nan")
        okx = ctrl >= 40
        print(f"{d['video'][:48]:50s} {t0:6.0f}: {len(F)} frames, {len(cuts)} cuts, local frames {len(local_here)} "
              f"(log {len(ex['local_at'])}, {'MATCH' if match else 'MISMATCH'}), even control {ctrl:.2f} dB"
              + ("" if okx else "  ALIGNMENT? extract dropped"), flush=True)
        if okx:
            for lab in LABELS: H[lab] += Hs[lab]
            per_src.append((d["video"], t0, {lab: Hs[lab].copy() for lab in LABELS}))
        for lab in LABELS: Hs[lab][:] = 0                        # per extract, kept or dropped


def med(hist):
    c = np.cumsum(hist); n = c[-1] if len(c) else 0
    if n == 0: return float("nan"), 0
    return float(BINS[np.searchsorted(c, n / 2)] + 0.025), int(n)


def table(Hh, title):
    print(f"\n{title}\n{'band px/f':>10s} | {'flagged':>15s} {'pre-rule':>15s} {'unflagged A':>15s} {'unflagged B':>15s} | flag-A   A-B")
    gaps, ab = [], []
    for i in range(len(BANDS) - 1):
        m = {lab: med(Hh[lab][i]) for lab in LABELS}
        c = lambda lab: f"{m[lab][0]:6.2f} ({m[lab][1]:6d})"
        g = m["flag"][0] - (m["A"][0] + m["B"][0]) / 2; x = m["A"][0] - m["B"][0]
        print(f"{BANDS[i]:4.0f}-{BANDS[i + 1]:<4.0f} | {c('flag')} {c('pre')} {c('A')} {c('B')} | {g:+6.2f} {x:+6.2f}")
        if m["flag"][1] >= 50 and m["A"][1] + m["B"][1] >= 50: gaps.append((i, g))
        if m["A"][1] >= 50 and m["B"][1] >= 50: ab.append(abs(x))
    return gaps, ab


# the histograms, so batches of sources can be merged later (np.load, sum, table)
np.savez(WORK / f"local_{pathlib.Path(log).stem}.npz", bands=BANDS, bins=BINS, **{f"all_{lab}": H[lab] for lab in LABELS},
         **{f"src{i}_{lab}": Hh[lab] for i, (_, _, Hh) in enumerate(per_src) for lab in LABELS},
         names=np.array([f"{v}@{t0:.0f}" for v, t0, _ in per_src]))
gaps, ab = table(H, "ALL extracts: median cell PSNR-Y dB (cells), by the cell's own speed")
print(f"\nguards: {guard_fail} frames where the mask's count differed from census.detect's (must be 0)")
if gaps:
    G = np.array([g for _, g in gaps]); half = len(G) // 2
    print(f"L1: mean flagged - unflagged gap over {len(G)} bands holding 50+ cells of each: {G.mean():+.2f} dB "
          f"(pre-registered: at most -2.0) -> {'PASSED' if G.mean() <= -2 else 'MISSED'}")
    if len(G) >= 2:
        print(f"L2: slower half {G[:half].mean():+.2f}, faster half {G[half:].mean():+.2f} dB "
              f"-> {'PASSED' if G[half:].mean() < G[:half].mean() else 'MISSED'} (the gap grows with speed)")
print(f"CONTROL (A vs B, must stay within 0.3 dB in every band): max |A - B| {max(ab) if ab else float('nan'):.2f} dB "
      f"-> {'HELD' if ab and max(ab) <= 0.3 else 'MOVED'}")
print("\nper source (mean flagged - unflagged gap over its bands with 50+ cells of each):")
for v, t0, Hh in per_src:
    gs = []
    for i in range(len(BANDS) - 1):
        f, nf = med(Hh["flag"][i]); u, nu = med(Hh["A"][i] + Hh["B"][i])
        if nf >= 50 and nu >= 50: gs.append(f - u)
    print(f"  {v[:48]:50s} {t0:6.0f}: {np.mean(gs):+6.2f} dB over {len(gs)} bands" if gs else f"  {v[:48]:50s} {t0:6.0f}: --")
