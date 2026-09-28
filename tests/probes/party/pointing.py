"""The arm pointed at the camera (the owner at the party, ~13:45: "when the arm is straight at the camera, there are no
arm bones visible so its tricky to infer a hand"): the extreme of the bone-length depth rule, a limb along Z.

An EPISODE: the shoulder confident (>0.5) while the arm's 2D length (shoulder-elbow + elbow-wrist, or shoulder-wrist
where the elbow is lost) falls under COLLAPSE of that child's own typical arm (its p90 over the track) for at least
3 frames at 30 Hz (depth2.npz: every tracked child's raw Vision joints). Then:
  (a) how often and how long; which modes the show was in (sys lines);
  (b) what Vision does with the wrist: keeps it (collapsed onto the shoulder), lowers its confidence, or loses it;
  (c) the field's LOOMING at the shoulder (field-q, 8-px cells: the divergence of a 5 x 5 cell window centred on the
      shoulder, per frame) in the frames entering and leaving the episode: an arm reaching toward the camera grows
      in the picture (div > 0), retracting it shrinks (div < 0) -- against the same child's frames outside episodes;
  (d) Apple's 3D pose where it exists (the first two sessions): the wrist's depth against the shoulder's.

    pointing.py [--collapse 0.35]"""
import bisect
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

COLLAPSE = float(sys.argv[sys.argv.index("--collapse") + 1]) if "--collapse" in sys.argv else 0.35
a = np.load(pd.NP / "party-analysis" / "depth2.npz")["rows"]
si, tid, t, ruler = a[:, 0], a[:, 1], a[:, 2], a[:, 3]
J = a[:, 7:].reshape(-1, 19, 3)
keys = si * 1e6 + tid
SIDES = {"left": (6, 8, 10), "right": (7, 9, 11)}

episodes = []            # (session, id, side, t0, t1, n frames, wrist conf median, wrist kept share)
series = {}              # (session, id, side) -> (t, collapsed flags) for the looming windows
for k in np.unique(keys):
    m = np.where(keys == k)[0]
    m = m[np.argsort(t[m])]
    for side, (sh, el, wr) in SIDES.items():
        cs, ce, cw = J[m, sh, 2], J[m, el, 2], J[m, wr, 2]
        l_se = np.linalg.norm(J[m, el, :2] - J[m, sh, :2], axis=1)
        l_ew = np.linalg.norm(J[m, wr, :2] - J[m, el, :2], axis=1)
        l_sw = np.linalg.norm(J[m, wr, :2] - J[m, sh, :2], axis=1)
        arm = np.where((ce > 0.3) & (cw > 0.3), l_se + l_ew, np.where(cw > 0.3, l_sw, np.where(ce > 0.3, 2 * l_se, 0.0)))
        good = (cs > 0.5) & (ce > 0.3) & (cw > 0.3)
        if good.sum() < 60:
            continue
        typ = np.percentile(arm[good], 90)
        col = (cs > 0.5) & (arm < COLLAPSE * typ)
        series[(int(si[m[0]]), int(tid[m[0]]), side)] = (t[m], col, m)
        # runs of >= 3 consecutive collapsed frames (no gap > 2 frames in time)
        i = 0
        while i < len(m):
            if not col[i]:
                i += 1
                continue
            j = i
            while j + 1 < len(m) and col[j + 1] and t[m[j + 1]] - t[m[j]] < 0.1:
                j += 1
            if j - i + 1 >= 3:
                episodes.append((int(si[m[i]]), int(tid[m[i]]), side, t[m[i]], t[m[j]], j - i + 1,
                                 float(np.median(cw[i:j + 1])), float(np.mean(cw[i:j + 1] > 0.3))))
            i = j + 1
print(f"(a) episodes (arm under {COLLAPSE} of its own typical length, shoulder confident, >= 3 frames): {len(episodes)}")
if episodes:
    E = np.array([(e[3], e[4], e[5], e[6], e[7]) for e in episodes])
    dur = E[:, 1] - E[:, 0]
    total_min = sum(np.ptp(v[0]) for v in series.values()) / 60
    print(f"    {len(episodes) / total_min:.2f} per child-arm-minute of tracking; duration p50 {np.median(dur):.2f} s p90 {np.percentile(dur, 90):.2f} s")
    print(f"(b) the wrist during an episode: confidence p50 {np.median(E[:, 3]):.2f}; kept (conf > 0.3) in {100 * np.mean(E[:, 4]):.0f}% of episode frames")
# the mode per episode from the sys lines
modes = {}
for sidx, d in enumerate(pd.sessions()):
    tt, mm = [], []
    for o in pd.jsonl(d, "sys"):
        tt.append(o["t"]); mm.append(o.get("mode"))
    modes[sidx] = (np.array(tt), mm)
cnt = {}
for e in episodes:
    tt, mm = modes[e[0]]
    k = min(max(bisect.bisect_left(tt, e[3]), 0), len(mm) - 1)
    cnt[mm[k]] = cnt.get(mm[k], 0) + 1
print("    by the show's mode: " + ", ".join(f"{k} {v}" for k, v in sorted(cnt.items(), key=lambda kv: -kv[1])))


# (c) looming at the shoulder from field-q around episode starts and ends
def div_at(uv, cell, x, y, r=2):
    h, w = uv.shape[:2]
    i, j = int(x // cell), int(y // cell)
    if i - r - 1 < 0 or j - r - 1 < 0 or i + r + 1 >= w or j + r + 1 >= h:
        return np.nan
    win = np.asarray(uv[j - r - 1:j + r + 2, i - r - 1:i + r + 2], np.float32)
    du = (win[1:-1, 2:, 0] - win[1:-1, :-2, 0]) / (2 * cell)
    dv = (win[2:, 1:-1, 1] - win[:-2, 1:-1, 1]) / (2 * cell)
    return float(np.mean(du + dv))            # per frame


fq = {}
for sidx, d in enumerate(pd.sessions()):
    segs = pd.fields(d, "q")
    ts = [np.asarray(s_["t"]) for s_ in segs]
    fq[sidx] = (segs, ts)


def field_at(sidx, when):
    segs, ts = fq[sidx]
    for s_, tt in zip(segs, ts):
        k = np.searchsorted(tt, when)
        for c in (k - 1, k):
            if 0 <= c < len(tt) and abs(tt[c] - when) < 0.002:
                return s_["uv"][c], float(s_["cell"][c])
    return None, None


enter, leave, inside, base = [], [], [], []
rng = np.random.default_rng(0)
for e in episodes:
    tt, col, m = series[(e[0], e[1], e[2])]
    sh = SIDES[e[2]][0]
    i0 = int(np.searchsorted(tt, e[3])); i1 = int(np.searchsorted(tt, e[4]))
    for lst, idxs in ((enter, range(max(0, i0 - 4), i0 + 1)), (leave, range(i1, min(len(tt), i1 + 5))),
                      (inside, range(i0 + 1, i1))):
        for ii in idxs:
            uv, cell = field_at(e[0], tt[ii])
            if uv is not None:
                x, y = J[m[ii], sh, :2]
                lst.append(div_at(uv, cell, x, y))
# the baseline: random frames of the same children's shoulders outside episodes
for key, (tt, col, m) in list(series.items())[:400]:
    sh = SIDES[key[2]][0]
    for ii in rng.choice(np.where(~col)[0], size=min(10, int((~col).sum())), replace=False):
        uv, cell = field_at(key[0], tt[ii])
        if uv is not None:
            x, y = J[m[ii], sh, :2]
            base.append(div_at(uv, cell, x, y))
for name, v in (("entering (the 4 frames before and the first)", enter), ("inside", inside),
                ("leaving (the last and the 4 after)", leave), ("baseline (outside episodes)", base)):
    v = np.array([x for x in v if np.isfinite(x)])
    if len(v):
        print(f"(c) the field's divergence at the shoulder, {name}: n {len(v)}  mean {np.mean(v) * 100:+.2f}%/frame  "
              f"p50 {np.median(v) * 100:+.2f}  share > +1%/frame {100 * np.mean(v > 0.01):.0f}%  share < -1% {100 * np.mean(v < -0.01):.0f}%")
