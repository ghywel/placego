"""ENERGY-TRANSFER.md 3.6: an impact census -- how often a local velocity reversal falls inside one frame interval.

    census.py controls <workdir>
    census.py film <video> <extracts> <seconds> <seed>          (prints one summary line per extract; numbers only)

The field: the four-frame propagated shader's raw velocity (read_view 4) at N:N, RGB in, 1280 wide (height by the
aspect), read per 8-px cell (every 8th pixel of the upsampled field). An EVENT at frame k: at least MIN_CELLS
contiguous-ish cells (a cell counts when 3+ of its 8 neighbours also qualify) whose velocity at k - 1 and k + 2 point
in opposite directions along the line of the change, both faster than 2 px/frame, the change over 4 px/frame,
and SYMMETRIC (|ua + ub| < 0.5 (ub - ua): comparable speeds either side, not an edge arriving), and PERSISTENT
(k - 2 like k - 1, k + 3 like k + 2: steady motion either side). The clip's first and last 4 frames are not scored.
Reversals over 20 percent of the cells are GLOBAL (camera shake, a whip pan) and counted apart. Frames within 3 of a
cut (a mean absolute luma change over 0.12 on a 160-wide thumbnail) are left out. Numbers only: nothing of the
footage is written or shown.
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
SHADERS = TESTS.parent / "shaders"
FF = os.environ.get("FFMPEG", "ffmpeg"); FP = os.environ.get("FFPROBE", "ffprobe")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
MIN_CELLS, VMIN, DMIN, GLOBAL = 16, 2.0, 4.0, 0.20
WORK = pathlib.Path(os.environ.get("CENSUS_WORK", "/tmp/census")); WORK.mkdir(parents=True, exist_ok=True)
t = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
(WORK / "_vel.glsl").write_text(s)


def field_frames(inargs, fps, w, h):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk"] + inargs + [
           "-vf", f"scale={w}:{h},format=rgb48le,libplacebo=fps={fps}:frame_mixer=custom_n:custom_shader_path=_vel.glsl,"
                  "format=rgb48le", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, cwd=WORK, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    fb = w * h * 6
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        im = np.frombuffer(buf, np.uint16).reshape(h, w, 3)[4::8, 4::8, :2].astype(np.float32) / 65535.0
        yield (im - 0.5) * 64.0
    p.wait()


def detect(fields, cuts=frozenset()):
    """per frame k: (n_event_cells, n_cells, 'local'|'global'|None)"""
    F = list(fields); out = []
    EDGE = 4                                             # the four-frame window runs off the clip's first and last frames
    for k in range(1, len(F) - 2):
        if k < EDGE or k > len(F) - EDGE - 2: out.append((k, 0, 0, None)); continue
        if any(abs(k - c) <= 3 for c in cuts): out.append((k, 0, 0, None)); continue
        a, b = F[k - 1], F[k + 2]
        d = b - a; dn = np.linalg.norm(d, axis=-1) + 1e-9
        ua, ub = (a * d).sum(-1) / dn, (b * d).sum(-1) / dn          # both velocities along the line of the change
        # SYMMETRY (the first controls, 2026-09-30: bounce-constant fired on 51 of 93 frames at the box's LEADING
        # edge -- cells going from background noise to the box's speed): a reversal has comparable speeds either side,
        # |ua + ub| < 0.5 (ub - ua), which still admits an inelastic bounce down to a restitution of about 0.4
        q = (ua < -VMIN) & (ub > VMIN) & (dn > DMIN) & (np.abs(ua + ub) < 0.5 * (ub - ua))
        # PERSISTENCE (the second controls: small false events at an arriving edge still passed the symmetry): the
        # motion is steady either side of a real reversal -- k-2 like k-1, and k+3 like k+2
        a2, b3 = F[k - 2], F[k + 3]
        q &= (np.linalg.norm(a2 - a, axis=-1) < 0.5 * np.linalg.norm(a, axis=-1)) & \
             (np.linalg.norm(b3 - b, axis=-1) < 0.5 * np.linalg.norm(b, axis=-1))
        nb = sum(np.roll(np.roll(q, dy, 0), dx, 1) for dy in (-1, 0, 1) for dx in (-1, 0, 1)) - q
        core = q & (nb >= 3)
        n_ev = int(core.sum()); total = q.size
        kind = None
        if n_ev >= MIN_CELLS: kind = "global" if n_ev > GLOBAL * total else "local"
        out.append((k, n_ev, total, kind))
    return out


def summarise(tag, rows):
    used = [r for r in rows if r[3] is not None or r[1] >= 0]
    loc = [r for r in rows if r[3] == "local"]; glob = [r for r in rows if r[3] == "global"]
    n = len(rows)
    print(f"{tag}: {n} frames; local events {len(loc)} ({100 * len(loc) / max(n, 1):.2f} %); global {len(glob)} "
          f"({100 * len(glob) / max(n, 1):.2f} %); at frames {[r[0] for r in loc][:12]}", flush=True)
    return {"frames": n, "local": len(loc), "global": len(glob), "local_at": [r[0] for r in loc]}


if sys.argv[1] == "controls":
    sys.path.insert(0, str(TESTS)); import masters                  # noqa: E402
    d = pathlib.Path(sys.argv[2]); d.mkdir(parents=True, exist_ok=True)
    res = {}
    for sc in ("bounce-constant", "static", "spin-constant"):
        src = d / f"{sc}.raw"
        if not src.exists():
            subprocess.run([sys.executable, str(TESTS / "masters.py"), sc, "--size", "1280x720", "--frames", "96",
                            "--src-fps", "24", "--out-fps", "24", "--settle", "0", "--bg", "textured", "--texture", "sines",
                            "--export-source", str(src)], check=True, stdout=subprocess.DEVNULL)
        rows = detect(field_frames(["-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", "1280x720", "-r", "24", "-i", str(src)],
                                   24, 1280, 720))
        res[sc] = summarise(f"CONTROL {sc}", rows)
    table = {nm: (kind, p) for nm, kind, p, *_ in masters.masters(1280, 720)}
    _, b = table["bounce-constant"]
    hits = [sg[0] for sg in masters.trajectory(b, 1280.0, 720.0)[1:] if sg[0] < 94]
    print(f"  bounce-constant's wall hits (closed form): {[round(h, 2) for h in hits]}")
    at = res["bounce-constant"]["local_at"]
    missed = [h for h in hits if not any(abs(k - h) <= 1.5 for k in at)]
    false = [k for k in at if min(abs(k - h) for h in hits) > 2]
    print(f"  bounce: hits missed {missed}; events more than 2 frames from a hit {false}")
    ok = not missed and not false and res["static"]["local"] == 0 and res["spin-constant"]["local"] == 0
    print("CONTROLS " + ("PASSED" if ok else "FAILED -- stop: the census cannot be trusted"))
    sys.exit(0 if ok else 3)

if sys.argv[1] == "film":
    video, nx, secs, seed = sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5])
    pr = json.loads(subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries",
                                    "stream=width,height,r_frame_rate:format=duration", "-of", "json", video],
                                   capture_output=True, text=True).stdout)
    st = pr["streams"][0]; dur = float(pr["format"]["duration"]); fps = st["r_frame_rate"]
    W0, H0 = int(st["width"]), int(st["height"]); w = 1280; h = int(round(H0 * w / W0 / 2)) * 2
    rng = random.Random(seed)
    name = pathlib.Path(video).stem
    allr = {"video": name, "fps": fps, "extracts": []}
    for i in range(nx):
        t0 = rng.uniform(0.1, 0.9) * max(dur - secs, 1)
        inargs = ["-ss", f"{t0:.2f}", "-t", f"{secs}", "-i", video]
        # cuts from a thumbnail's mean absolute change
        raw = subprocess.run([FF, "-v", "error"] + inargs + ["-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"],
                             capture_output=True).stdout
        th = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(np.float32) / 255
        cuts = {k for k in range(1, len(th)) if np.abs(th[k] - th[k - 1]).mean() > 0.12}
        rows = detect(field_frames(inargs, fps, w, h), frozenset(cuts))
        r = summarise(f"{name} @ {t0:.0f}s ({len(cuts)} cuts)", rows); r["t0"] = t0; r["cuts"] = len(cuts)
        allr["extracts"].append(r)
    print("JSON " + json.dumps(allr))
