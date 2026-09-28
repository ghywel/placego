"""The party recording's loaders: the first REAL content with an independent answer key.

The recording (2026-09-27, 13:00-15:17, about 2 h 20 min in four sessions) is a live camera watching children play,
run through the shipped recommendation's field (bidirectional-interpolation-variational-propagated, FLOW_H_AB: the
two-frame forward flow A -> B at half resolution, 2-px cells, source px, +y down) on a Metal host (the party app,
LilysParty, whose recorder wrote it -- PartyApp/Recorder.swift in that tree documents every format). Beside the field,
and independent of it, Apple's Vision 2D body pose ran on the same frames: 19 joints per person with confidences.
NO PICTURE WAS RECORDED -- numbers only (the guests are other families' children); nothing here may ever write one.

Layout of one session folder (party-<date>-<time>-<pid>/, NNN the ten-minute segment):
    session.json            the build, the args, the source size (1280x960), hostT0
    vision-NNN.jsonl        {t: capture host s, ms, size, people: [19 x [x, y, c]]}, one per Vision result (~30 Hz)
    frames-NNN.jsonl        per processed frame: the solver's fused tracks (NOT independent of the field: the solver
                            fuses it), the puppets, timings, "crossing" (two torsos overlap)
    field-q-NNN.bin         every processed frame, the field averaged over 4x4 cells (8-px cells, 160x120)
    field-full-NNN.bin      the whole field (2-px cells, 640x480) once a second, and EVERY frame through a crossing
    sys-NNN.jsonl           once a second: pacing, CPU, memory, the camera's exposure and ISO, the show's state
    pose3d-NNN.jsonl        (the first two sessions only) Apple's 3D body pose at 2 Hz
A field record: a 32-byte header (magic LPF1, w u16, h u16, cell f32, interval f32, t f64, seq u32, pad u32) and
w*h*(u, v) float16, the displacement of the content at each cell centre from frame A (t - interval) to B (t).

Data root: $PARTY_DIR, else $NP_SCRATCH/lillys/party-2026-09-27 (NP_SCRATCH defaults to this Mac's np-scratch)."""
import glob
import json
import os
import pathlib

import numpy as np

NP = pathlib.Path(os.environ.get("NP_SCRATCH", "/Volumes/extnvme/nframe-project/np-scratch"))
ROOT = pathlib.Path(os.environ.get("PARTY_DIR", NP / "lillys" / "party-2026-09-27"))

JOINTS = ["nose", "leftEye", "rightEye", "leftEar", "rightEar", "neck", "leftShoulder", "rightShoulder", "leftElbow",
          "rightElbow", "leftWrist", "rightWrist", "root", "leftHip", "rightHip", "leftKnee", "rightKnee", "leftAnkle",
          "rightAnkle"]
GROUPS = {"head": [0, 1, 2, 3, 4], "torso": [5, 6, 7, 12, 13, 14], "elbows": [8, 9], "wrists": [10, 11],
          "knees": [15, 16], "ankles": [17, 18]}
GROUP_OF = {j: g for g, js in GROUPS.items() for j in js}
# bone midpoints, the comparison's main points (a joint sits at a limb's end or edge, where a field window is half
# background; the middle of a rigid segment moves by exactly the mean of its ends, and its window is inside the limb)
BONES = {"torso": (5, 12), "upperArmL": (6, 8), "upperArmR": (7, 9), "forearmL": (8, 10), "forearmR": (9, 11),
         "thighL": (13, 15), "thighR": (14, 16), "shinL": (15, 17), "shinR": (16, 18)}
BONE_GROUPS = {"torso": ["torso"], "upper arms": ["upperArmL", "upperArmR"], "forearms": ["forearmL", "forearmR"],
               "thighs": ["thighL", "thighR"], "shins": ["shinL", "shinR"]}
BONE_IDS = {name: 100 + k for k, name in enumerate(BONES)}          # the row code of a bone midpoint (joints are 0-18)
# the body ruler's segments (the party app's: the third-longest of these is robust to foreshortening of a few)
SEGMENTS = [(6, 8), (8, 10), (7, 9), (9, 11), (13, 15), (15, 17), (14, 16), (16, 18), (6, 7), (13, 14), (5, 12)]


def sessions():
    return sorted(p for p in ROOT.glob("party-*") if (p / "session.json").exists())


def info(d):
    return json.loads((pathlib.Path(d) / "session.json").read_text())


def jsonl(d, stream):
    """Every record of one stream, in order, across its segments (a line cut short by a crash is skipped)."""
    for p in sorted(glob.glob(str(pathlib.Path(d) / f"{stream}-[0-9][0-9][0-9].jsonl"))):
        with open(p) as f:
            for ln in f:
                if ln.strip():
                    try:
                        yield json.loads(ln)
                    except json.JSONDecodeError:
                        pass


def field_dtype(w, h):
    return np.dtype([("magic", "S4"), ("w", "<u2"), ("h", "<u2"), ("cell", "<f4"), ("interval", "<f4"), ("t", "<f8"),
                     ("seq", "<u4"), ("pad", "<u4"), ("uv", "<f2", (h, w, 2))])


def fields(d, kind="full"):
    """The field records of one kind ("full" or "q") as memory-mapped structured arrays, one per segment file, each
    record's uv (h, w, 2) float16 in source px; a trailing partial record (a crash) is left out."""
    out = []
    for p in sorted(glob.glob(str(pathlib.Path(d) / f"field-{kind}-[0-9][0-9][0-9].bin"))):
        with open(p, "rb") as f:
            head = f.read(32)
        if len(head) < 32 or head[:4] != b"LPF1":
            continue
        w, h = np.frombuffer(head[4:8], "<u2")
        dt = field_dtype(int(w), int(h))
        n = os.path.getsize(p) // dt.itemsize
        if n:
            m = np.memmap(p, dtype=dt, mode="r", shape=(n,))
            assert (m["magic"][: min(n, 50)] == b"LPF1").all(), p
            out.append(m)
    return out


def vision(d):
    """Vision's raw results: {round(t, 4): (N, 19, 3) array}, and the sorted times."""
    idx = {}
    for o in jsonl(d, "vision"):
        ps = o.get("people") or []
        arr = np.array([[[np.nan if v is None else v for v in j] for j in p] for p in ps], float).reshape(-1, 19, 3)
        idx[round(o["t"], 4)] = arr
    return idx


def ruler(p, conf=0.3):
    """The body ruler of one pose (19 x 3): the third-longest visible segment of the eleven, source px; nan if fewer
    than three segments are visible."""
    ls = [np.hypot(*(p[a, :2] - p[b, :2])) for a, b in SEGMENTS if p[a, 2] > conf and p[b, 2] > conf]
    ls = sorted(ls, reverse=True)
    return ls[2] if len(ls) >= 3 else np.nan


def match(A, B, conf=0.3):
    """Pair the people of two Vision results by their neck (else the mean of their confident joints): greedy nearest,
    within 0.6 of the larger body ruler. Returns [(i, j)]."""
    def centre(p):
        if p[5, 2] > conf:
            return p[5, :2]
        m = p[:, 2] > conf
        return p[m, :2].mean(0) if m.any() else None
    ca = [centre(p) for p in A]
    cb = [centre(p) for p in B]
    pairs = []
    for i, a in enumerate(ca):
        for j, b in enumerate(cb):
            if a is None or b is None:
                continue
            r = np.nanmax([ruler(A[i]), ruler(B[j]), 40.0])
            dist = np.hypot(*(a - b))
            if dist < 0.6 * r:
                pairs.append((dist, i, j))
    used_i, used_j, out = set(), set(), []
    for dist, i, j in sorted(pairs):
        if i not in used_i and j not in used_j:
            out.append((i, j))
            used_i.add(i)
            used_j.add(j)
    return out


def sample(uv, x, y, cell=2.0, r=1):
    """The field's median vector in the (2r+1)^2 cells around source point (x, y) (cell centres at (i + 0.5) * cell);
    None outside the grid."""
    h, w = uv.shape[:2]
    i, j = int(x // cell), int(y // cell)
    if i - r < 0 or j - r < 0 or i + r >= w or j + r >= h:
        return None
    win = np.asarray(uv[j - r:j + r + 1, i - r:i + r + 1], np.float32).reshape(-1, 2)
    return np.median(win, axis=0)
