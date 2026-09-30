"""ENERGY-TRANSFER.md 3.3-3.4: body-to-body collisions through the family, and the momentum ledger on the field.

    collide.py <workdir> [scenes=pair,cradle5,unequal] [shaders=hold,linear,rec,quad,carry] [bg=flat|textured]

3.3b: bg=textured puts the discs on the masters' dim five-sine ground; scene rows3 is three independent equal pairs
at y = 160, 360, 560 whose contacts fall at 26.2, 26.5, 26.8 source frames (three contact phases).

Written to run inside the claude-research container on the NAS's Arc (a single run is exact there), but it needs
only ffmpeg with libplacebo and numpy. FFMPEG in the environment.

THE SCENES: sliding textured discs (no roll: pucks, curling stones) on black, 1280x720, 24 fps, 60 source frames.
Each disc carries the masters' five-sine texture in its own frame, offset per disc so that no two look alike. Every
position is exact, from the laws of a 1-D elastic collision (masses as areas):
  pair     A (r 90) at 12 px/frame hits B (r 90) at rest: A stops, B leaves at 12
  cradle5  disc 1 (r 60) at 12 px/frame hits discs 2-5 (r 60) at rest and touching: 5 leaves at 12, 2-4 never move
  unequal  A (r 70) at 12 hits B (r 100) at rest: A -> (mA - mB)/(mA + mB) 12 = -4.11, B -> 2 mA/(mA + mB) 12 = +7.89
Truth at 60 fps samples the same law at t = n * 24 / 60.

1. Per shader: ffmpeg's psnr against the truth, per frame; the median over frames within 0.5 source frames of a
   contact against frames more than 2 from one.
2. The ledger: the four-frame propagated shader's raw velocity (read_view 4) at N:N; each disc's median velocity
   inside its disc (eroded 10 px) at every source frame, times its area. Transfer events are a frame k where one
   disc's momentum falls and another's rises by a matching amount (within 30 percent), with the momentum of the
   discs in between under 5 percent of the moved amount.

Pre-registered in ENERGY-TRANSFER.md 3.3-3.4 (before it ran): C1 contact frames dip 4-14 dB; C2 in cradle5 the
middle three read |v| < 0.2 on every frame, and one transfer event per contact goes from 1 to 5 across them; C3 in
unequal the total momentum is conserved within 10 percent across the contact.
"""
import json
import math
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
SHADERS = TESTS.parent / "shaders"
sys.path.insert(0, str(TESTS))
import masters                                                                   # noqa: E402

work = pathlib.Path(sys.argv[1]); work.mkdir(parents=True, exist_ok=True)
scenes = (sys.argv[2] if len(sys.argv) > 2 else "pair,cradle5,unequal").split(",")
shaders = [x for x in (sys.argv[3] if len(sys.argv) > 3 else "hold,linear,rec,quad,carry").split(",") if x]   # "" = the ledger only
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
BG = sys.argv[4] if len(sys.argv) > 4 else "flat"
W, H, NF, V = 1280, 720, 60, 12.0
STEMS = {"rec": "bidirectional-interpolation-variational-propagated",
         "quad": "quaddirectional-interpolation-propagated",
         "carry": "bidirectional-interpolation-variational-propagated-global-cage-energy-carry"}
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)


def build(name):
    """[(r, x0, v_before, v_after, t_contact)] per disc, the contact time, and the disc order along x"""
    if name == "pair":
        r = 90; xa, xb = 200.0, 700.0
        tc = ((xb - 2 * r) - xa) / V
        return [(r, xa, V, 0.0, tc), (r, xb, 0.0, V, tc)], [tc]
    if name == "cradle5":
        r = 60; rest = [400.0 + 2 * r * i for i in range(4)]                   # discs 2-5, touching
        x1 = 100.0; tc = ((rest[0] - 2 * r) - x1) / V
        discs = [(r, x1, V, 0.0, tc)] + [(r, x, 0.0, 0.0, tc) for x in rest[:3]] + [(r, rest[3], 0.0, V, tc)]
        return discs, [tc]
    if name == "unequal":
        ra, rb = 70, 100; ma, mb = ra * ra, rb * rb; xa, xb = 150.0, 650.0
        tc = ((xb - ra - rb) - xa) / V
        return [(ra, xa, V, (ma - mb) / (ma + mb) * V, tc), (rb, xb, 0.0, 2 * ma / (ma + mb) * V, tc)], [tc]
    if name == "rows3":
        r = 70; out = []; tcs = []
        for tc in (26.2, 26.5, 26.8):
            xb = 700.0; xa = (xb - 2 * r) - V * tc
            out += [(r, xa, V, 0.0, tc), (r, xb, 0.0, V, tc)]; tcs.append(tc)
        return out, tcs
    raise SystemExit(name)


def centre(d, t):
    r, x0, vb, va, tc = d
    return (x0 + vb * t) if t <= tc else (x0 + vb * tc + va * (t - tc))


ROWY = {}                                                  # disc index -> its row's y (rows3); 360 otherwise


def dy(i): return ROWY.get(i, 360)


def render(discs, t):
    img = np.zeros((H, W)) if BG == "flat" else masters.clamp01(masters.tex(xx, yy) * 0.35 + 0.1)
    for i, d in enumerate(discs):
        cx = centre(d, t); r = d[0]; y0 = dy(i)
        m = (xx - cx) ** 2 + (yy - y0) ** 2 < r * r
        img = np.where(m, masters.clamp01(masters.tex(xx - cx + 97 * i, yy - y0 + 53 * i)), img)
    return img


def write(path, discs, times):
    with open(path, "wb") as f:
        for t in times:
            f.write((np.clip(render(discs, t), 0, 1) * 65535 + 0.5).astype("<u2").tobytes())


def ffmpeg(args, **kw):
    return subprocess.run([FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk"] + args,
                          cwd=kw.get("cwd"), capture_output=True, check=True)


for k, stem in STEMS.items():
    (work / f"_{k}.glsl").write_text((SHADERS / f"{stem}.glsl").read_text())
t = (SHADERS / f"{STEMS['quad']}.glsl").read_text()
s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
(work / "_vel.glsl").write_text(s)
CHAIN = {"hold": "format=yuv420p,fps=60", "linear": "format=yuv420p,libplacebo=fps=60:frame_mixer=linear"}
for k in STEMS:
    CHAIN[k] = f"format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_{k}.glsl"
NOUT = int((NF - 1) * 60 / 24)
report = {}

for name in scenes:
    discs, contacts = build(name)
    ROWY.clear()
    if name == "rows3": ROWY.update({0: 160, 1: 160, 2: 360, 3: 360, 4: 560, 5: 560})
    d = work / name; d.mkdir(exist_ok=True)
    write(d / "src24.raw", discs, [float(k) for k in range(NF)])
    write(d / "truth60.raw", discs, [n * 24 / 60 for n in range(NOUT)])
    print(f"\n# {name}: {len(discs)} discs, contact at t = {', '.join(f'{c:.3f}' for c in contacts)} source frames", flush=True)
    rep = {"contacts": contacts, "psnr": {}}
    for sh in shaders:
        stats = d / f"{sh}.psnr"
        ffmpeg(["-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", "src24.raw",
                "-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "60", "-i", "truth60.raw",
                "-filter_complex", f"[0:v]{CHAIN[sh].replace('_' + sh, '../_' + sh)}[ip];[ip]format=yuv420p[a];"
                f"[1:v]format=yuv420p[b];[a][b]psnr=stats_file={sh}.psnr", "-f", "null", "-"], cwd=d)
        ps = {}
        for line in stats.read_text().splitlines():
            m = re.match(r"n:(\d+) .*psnr_y:([\d.inf]+)", line)
            if m: ps[int(m.group(1)) - 1] = float(m.group(2)) if m.group(2) != "inf" else 99.0
        near = [ps[n] for n in ps if n > 5 and min(abs(n * 24 / 60 - c) for c in contacts) < 0.5]
        smooth = [ps[n] for n in ps if n > 5 and min(abs(n * 24 / 60 - c) for c in contacts) > 2]
        rep["psnr"][sh] = (float(np.median(near)), float(np.median(smooth)), len(near))
        print(f"  {sh:6s} contact frames {np.median(near):6.2f} dB ({len(near)})   smooth {np.median(smooth):6.2f} dB   "
              f"dip {np.median(near) - np.median(smooth):+6.2f}", flush=True)
    # the ledger
    out = subprocess.run([FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo",
                          "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(d / "src24.raw"),
                          # RGB IN for a field read: with yuv420p in, libplacebo's output on Linux/Mesa came back 8-bit
                          # limited range (the Arc read a still disc at -0.63 and 12 px/frame at 10.16; the M5 read
                          # exactly), the read-path trap fieldcheck.py alarms on. The picture scores keep yuv420p.
                          "-vf", "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=../_vel.glsl,"
                          "format=rgb48le", "-f", "rawvideo", "-"], cwd=d, capture_output=True, check=True).stdout
    fb = W * H * 6; nfld = len(out) // fb
    # THE INSTRUMENT CHECK (fieldcheck.py's): off the discs the field is exactly zero, encoded 0.5
    im0 = np.frombuffer(out[(nfld // 2) * fb:(nfld // 2 + 1) * fb], np.uint16).reshape(H, W, 3)
    z = float(np.median(im0[:100, :100, 0])) / 65535.0          # a corner no disc reaches: black, or the still ground
    if abs(z - 0.5) > 0.0005:
        sys.exit(f"READ PATH BROKEN: the zero level off the discs reads {z:.4f}, not 0.5 (an 8-bit or limited-range intermediate)")
    vel = np.zeros((nfld, len(discs))); true_v = np.zeros((nfld, len(discs)))
    area = np.array([math.pi * dd[0] ** 2 for dd in discs])
    for k in range(nfld):
        im = np.frombuffer(out[k * fb:(k + 1) * fb], np.uint16).reshape(H, W, 3)
        u = (im[..., 0].astype(np.float32) / 65535.0 - 0.5) * 64.0
        for i, dd in enumerate(discs):
            cx = centre(dd, float(k)); r = dd[0] - 10
            m = (xx - cx) ** 2 + (yy - dy(i)) ** 2 < r * r
            vel[k, i] = float(np.median(u[m]))
            true_v[k, i] = centre(dd, k + 0.5) - centre(dd, k - 0.5)
    P = vel * area; Pt = true_v * area
    print(f"  ledger (field median u per disc, px/frame; truth in brackets), frames around the contact:")
    kc = int(contacts[0])
    for k in range(max(0, kc - 3), min(nfld, kc + 5)):
        print("    k %2d  " % k + "  ".join(f"{vel[k, i]:+6.2f} [{true_v[k, i]:+6.2f}]" for i in range(len(discs)))
              + f"   total p {P[k].sum() / 1000:+8.1f}k [{Pt[k].sum() / 1000:+8.1f}k]", flush=True)
    events = []
    EDGE = 3                                  # the four-frame window straddles the clip's first and last frames: not scored
    # rows3 holds three independent pairs whose contacts share frames: the ledger runs per row, or they hide each other
    groups = [[0, 1], [2, 3], [4, 5]] if name == "rows3" else [list(range(len(discs)))]
    for grp in groups:
      for k in range(1 + EDGE, nfld - EDGE):
        dp = P[k, grp] - P[k - 1, grp]
        i, j = grp[int(np.argmin(dp))], grp[int(np.argmax(dp))]
        moved = min(-(P[k, i] - P[k - 1, i]), P[k, j] - P[k - 1, j])
        if moved <= 0.2 * V * area[grp].max() or i == j: continue
        if abs((P[k - 1, i] - P[k, i]) - (P[k, j] - P[k - 1, j])) > 0.3 * max(P[k - 1, i] - P[k, i], P[k, j] - P[k - 1, j]): continue
        lo, hi = sorted((i, j))
        between = [abs(P[k, m]) for m in range(lo + 1, hi)]
        if all(b < 0.05 * moved for b in between):
            events.append((k, i, j, float(moved), hi - lo - 1))
    events.sort()
    # the centred estimate straddles a contact, so one transfer shows on two consecutive frames: merge those
    merged = []
    for e in events:
        if merged and e[0] == merged[-1][0] + 1 and e[1:3] == merged[-1][1:3]:
            m = merged[-1]; merged[-1] = (m[0], m[1], m[2], m[3] + e[3], m[4], m[5] + 1)
        else:
            merged.append(e + (1,))
    events = [(k, i, j, moved, nb) for k, i, j, moved, nb, _ in merged]
    for k, i, j, moved, nb in events:
        gap = abs(centre(discs[j], float(k)) - centre(discs[i], float(k)))
        print(f"  TRANSFER at k {k}: disc {i + 1} -> disc {j + 1}, {moved / 1000:.1f}k (area x px/frame), across {nb} still "
              f"disc(s); {gap:.0f} px apart, so the coupling ran faster than {gap:.0f} px/frame", flush=True)
    mid_max = float(np.abs(vel[EDGE:nfld - EDGE, 1:4]).max()) if name == "cradle5" else None
    if BG != "flat":
        gm = []
        for k in range(EDGE, nfld - EDGE, 5):
            im = np.frombuffer(out[k * fb:(k + 1) * fb], np.uint16).reshape(H, W, 3)
            u = (im[..., 0].astype(np.float32) / 65535.0 - 0.5) * 64.0
            away = np.ones((H, W), bool)
            for i, dd in enumerate(discs):
                away &= (xx - centre(dd, float(k))) ** 2 + (yy - dy(i)) ** 2 > (dd[0] + 40) ** 2
            gm.append(float(np.median(np.abs(u[away]))))
        print(f"  the still ground away from the discs: median |u| {max(gm):.4f} px/frame (worst sampled frame)")
    if name == "cradle5":
        full = np.abs(vel[:, 1:4]).max(1); worst = int(np.argmax(full))
        print(f"  cradle5: over ALL frames the middle discs' largest |v| is {full.max():.3f} at frame {worst} of {nfld}")
    if mid_max is not None: print(f"  cradle5: the middle three discs' largest |median v| over frames {EDGE}..{nfld - EDGE - 1} {mid_max:.3f} px/frame")
    before = P[max(0, kc - 3):kc - 1].sum(1).mean(); after = P[kc + 3:kc + 6].sum(1).mean()
    print(f"  total momentum before {before / 1000:+.1f}k, after {after / 1000:+.1f}k ({(after / before - 1) * 100:+.1f} %)")
    rep.update(events=events, mid_max=mid_max, p_before=float(before), p_after=float(after))
    report[name] = rep
(work / "report.json").write_text(json.dumps(report, indent=1))
