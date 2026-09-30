"""ENERGY-TRANSFER.md 3.1: how far short of the wall each shader draws the box at a bounce -- the miss distance.

    corner.py <scene> <workdir> [src_frames=240] [labels=hold,linear,bi,rec,quad]

Exports the master scene's 24 fps source once (masters.py, flat black ground, 1280x720), renders it to 60 fps
through each label, PIPES every output frame straight into the measurement (nothing is stored), and finds the
box's edges in each frame: a column or row belongs to the box when at least 8 of its pixels are brighter than
0.03 on the black ground. The truth is the scene's closed form (masters.bounce_centre), never an image.

For each output frame near a wall hit, the error on the WALL SIDE is the drawn edge minus the true edge, signed so
negative = short of where the box really is (towards the room), positive = beyond it (towards the wall). The
CHORD model is the straight line between the true positions at the two source frames either side: what a pure
two-frame constant-velocity interpolator draws. Output frame n (0-based) samples law time n * 24 / 60.

Pre-registered in ENERGY-TRANSFER.md before this ran (see "3.1, the miss distance"):
  P1 the control: hold on output frames that land exactly on a source frame reads within 1 px of the truth;
  P2 on smooth frames (> 2 source frames from any hit) rec and quad read within 1 px (median |error|);
  P3 at frames within 0.5 source frames of a hit, the plain two-frame shader follows the chord: its median
     wall-side error within 30 percent of the chord's;
  P4 the four-frame shader falls shorter of the wall than the chord does LESS often than not (median error
     closer to zero than the chord's).
"""
import math
import os
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
SHADERS = TESTS.parent / "shaders"
sys.path.insert(0, str(TESTS))
import masters                                                                   # noqa: E402

scene = sys.argv[1]
work = pathlib.Path(sys.argv[2]); work.mkdir(parents=True, exist_ok=True)
N = int(sys.argv[3]) if len(sys.argv) > 3 else 240
labels = (sys.argv[4] if len(sys.argv) > 4 else "hold,linear,bi,rec,quad").split(",")
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
PY = os.environ.get("PYTHON", sys.executable)
W, H = 1280, 720
CHAINS = {
    "hold":   "format=yuv420p,fps=60",
    "linear": "format=yuv420p,libplacebo=fps=60:frame_mixer=linear",
    "bi":     "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_bi.glsl",
    "rec":    "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_rec.glsl",
    "quad":   "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_quad.glsl",
}
STEMS = {"bi": "bidirectional-interpolation", "rec": "bidirectional-interpolation-variational-propagated",
         "quad": "quaddirectional-interpolation-propagated"}

src = work / "src24.raw"
if not src.exists():
    subprocess.run([PY, str(TESTS / "masters.py"), scene, "--size", f"{W}x{H}", "--frames", str(N), "--src-fps", "24",
                    "--out-fps", "60", "--settle", "0", "--bg", "flat", "--texture", "sines", "--export-source", str(src)],
                   check=True, stdout=subprocess.DEVNULL)
for k, stem in STEMS.items():
    (work / f"_{k}.glsl").write_text((SHADERS / f"{stem}.glsl").read_text())

# the closed form: the box's centre, its half size, the wall hits and which wall each was
table = {name: (kind, p) for name, kind, p, *_ in masters.masters(W, H)}
kind, b = table[scene]
segs = masters.trajectory(b, float(W), float(H))
hw, hh = b.w / 2, b.h / 2
def centre(t): return masters.bounce_centre(b, segs, t)
hits = []
for sg in segs[1:]:
    t0, x, y = sg[0], sg[1], sg[2]
    wall = min((abs(x - hw), "left"), (abs(x - (W - hw)), "right"), (abs(y - hh), "top"), (abs(y - (H - hh)), "bottom"))[1]
    hits.append((t0, wall))
hits = [h for h in hits if h[0] < N - 1]

def edges_true(t):
    x, y = centre(t); return np.array([x - hw, x + hw, y - hh, y + hh])     # left, right, top, bottom (pixel edges)

def edges_chord(t):
    k = math.floor(t); f = t - k
    a, c = np.array(centre(k)), np.array(centre(k + 1))
    x, y = a + f * (c - a); return np.array([x - hw, x + hw, y - hh, y + hh])

SIDE = {"left": (0, -1), "right": (1, +1), "top": (2, -1), "bottom": (3, +1)}    # edge index, sign towards the wall

def measure(label):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk",
           "-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src),
           "-vf", CHAINS[label] + ",format=rgb48le", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fb = W * H * 6; out = []
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        im = np.frombuffer(buf, np.uint16).reshape(H, W, 3).max(-1).astype(np.float32) / 65535.0
        on = im > 0.03
        cols = np.nonzero(on.sum(0) >= 8)[0]; rows = np.nonzero(on.sum(1) >= 8)[0]
        out.append([cols[0], cols[-1] + 1, rows[0], rows[-1] + 1] if len(cols) and len(rows) else [np.nan] * 4)
    err = p.stderr.read().decode()
    p.wait()
    if p.returncode != 0 or "compile status" in err and "error" in err:
        sys.exit(f"{label}: ffmpeg failed: {err[:300]}")
    return np.array(out, float)

rows = []
print(f"# {scene}: {N} source frames, {len(hits)} wall hits ({', '.join(f'{t:.2f} {w}' for t, w in hits[:5])} ...)")
res = {}
for label in labels:
    e = measure(label)
    n = np.arange(len(e)); t = n * 24 / 60
    near, smooth, chord_near, ctrl = [], [], [], []
    for i, ti in enumerate(t):
        if ti >= N - 1 or np.isnan(e[i, 0]): continue
        d = [(abs(ti - h), h, w) for h, w in hits]
        dist, h, wall = min(d) if d else (99, None, None)
        tr = edges_true(ti)
        if abs(ti - round(ti)) < 1e-9 and label == "hold":
            ctrl.append(np.abs(e[i] - tr).max())
        if dist < 0.5:
            idx, sg = SIDE[wall]
            near.append(sg * (e[i, idx] - tr[idx]))
            chord_near.append(sg * (edges_chord(ti)[idx] - tr[idx]))
        elif dist > 2:
            smooth.append(np.abs(e[i] - tr).max())
    near, chord_near, smooth = np.array(near), np.array(chord_near), np.array(smooth)
    res[label] = (near, chord_near, smooth, ctrl)
    line = (f"{label:7s} impact frames {len(near):3d}: median {np.median(near):+6.2f} px, worst short {near.min():+6.2f}, "
            f"worst beyond {near.max():+6.2f} | chord median {np.median(chord_near):+6.2f}, worst {chord_near.min():+6.2f}"
            f" | smooth median |err| {np.median(smooth):5.2f} px ({len(smooth)} frames)")
    if ctrl: line += f" | CONTROL on-source frames max |err| {max(ctrl):.2f} px ({len(ctrl)})"
    print(line, flush=True)
