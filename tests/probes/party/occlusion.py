"""Which motion wins where one child passes in front of another (P3, and the interpolator's occlusion question).

For every whole-field record of a crossing run, every pair of Vision people whose TORSO boxes overlap: the front child
is the one with the larger body ruler (nearer the camera; a child's size varies, so pairs whose rulers differ by less
than FRONT_MIN are left out as undecided). In the overlap box, the field's median vector is compared with the two
children's torso displacements (Vision, A -> B; the torso midpoint moves by the mean of neck and root): which is
nearer? The picture's correct answer there is the FRONT child's motion (its surface is what both frames show).
Only pairs whose two motions differ by >= DIFF px are scored (otherwise the question has no answer).

    occlusion.py [--front 1.15] [--diff 3]"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

FRONT_MIN = float(sys.argv[sys.argv.index("--front") + 1]) if "--front" in sys.argv else 1.15
DIFF = float(sys.argv[sys.argv.index("--diff") + 1]) if "--diff" in sys.argv else 3.0
TORSO = [5, 6, 7, 12, 13, 14]


def box(p):
    js = [p[j, :2] for j in TORSO if p[j, 2] > 0.3]
    if len(js) < 4:
        return None
    a = np.array(js)
    return a.min(0), a.max(0)


res = []            # front err, back err, |front - back| motion, ruler ratio, overlap area share, front/back speeds
for si, d in enumerate(pd.sessions()):
    vis = pd.vision(d)
    vt = np.array(sorted(vis))
    def at(want):
        c = np.searchsorted(vt, want)
        for x in (c - 1, c, c + 1):
            if 0 <= x < len(vt) and abs(vt[x] - want) < 0.002:
                return vis[vt[x]]
        return None
    segs = pd.fields(d, "full")
    ts = np.concatenate([m["t"] for m in segs]) if segs else np.array([])
    for m in segs:
        for k in range(len(m)):
            t, iv = float(m["t"][k]), float(m["interval"][k])
            near = np.abs(ts - t)
            if not ((near > 1e-6) & (near < 0.5)).any():
                continue                                 # crossing runs only
            A, B = at(t - iv), at(t)
            if A is None or B is None or len(A) < 2:
                continue
            pairs = dict(pd.match(A, B))
            uv = None
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    if i not in pairs or j not in pairs:
                        continue
                    bi, bj = box(A[i]), box(A[j])
                    if bi is None or bj is None:
                        continue
                    lo = np.maximum(bi[0], bj[0])
                    hi = np.minimum(bi[1], bj[1])
                    if (hi - lo).min() < 8:
                        continue                          # no real overlap
                    ri, rj = pd.ruler(A[i]), pd.ruler(A[j])
                    if not (np.isfinite(ri) and np.isfinite(rj)):
                        continue
                    if max(ri, rj) / min(ri, rj) < FRONT_MIN:
                        continue
                    f_, b_ = (i, j) if ri > rj else (j, i)
                    def torso_move(q):
                        a, b = A[q], B[pairs[q]]
                        if min(a[5, 2], a[12, 2], b[5, 2], b[12, 2]) < 0.3:
                            return None
                        return ((b[5, :2] + b[12, :2]) - (a[5, :2] + a[12, :2])) / 2
                    mf, mb = torso_move(f_), torso_move(b_)
                    if mf is None or mb is None or np.hypot(*(mf - mb)) < DIFF:
                        continue
                    if uv is None:
                        uv = np.asarray(m["uv"][k], np.float32)
                    x0, y0 = (lo // 2).astype(int)
                    x1, y1 = (hi // 2).astype(int)
                    win = uv[y0:y1 + 1, x0:x1 + 1].reshape(-1, 2)
                    if len(win) < 9:
                        continue
                    fv = np.median(win, 0)
                    area = (hi - lo).prod() / min((bi[1] - bi[0]).prod(), (bj[1] - bj[0]).prod())
                    res.append((np.hypot(*(fv - mf)), np.hypot(*(fv - mb)), np.hypot(*(mf - mb)), max(ri, rj) / min(ri, rj),
                                area, np.hypot(*mf), np.hypot(*mb)))
    print(f"{d.name}: {len(res)} overlaps so far", flush=True)

r = np.array(res)
ef, eb, dm, ratio, area, sf, sb = r.T
print(f"\noverlapping torsos with distinct motions (>= {DIFF} px apart), front = the larger ruler (>= {FRONT_MIN}x): n {len(r)}")
print(f"  the field in the overlap is nearer the FRONT child's motion in {100 * np.mean(ef < eb):.1f}% "
      f"(median error to front {np.median(ef):.2f} px, to back {np.median(eb):.2f} px)")
for lo_, hi_ in ((1.15, 1.3), (1.3, 1.6), (1.6, 10)):
    mm = (ratio >= lo_) & (ratio < hi_)
    if mm.sum() >= 20:
        print(f"  size ratio {lo_:.2f}-{hi_:.2f}: n {int(mm.sum()):5d}  front wins {100 * np.mean(ef[mm] < eb[mm]):5.1f}%")
for lo_, hi_ in ((3, 6), (6, 12), (12, 100)):
    mm = (dm >= lo_) & (dm < hi_)
    if mm.sum() >= 20:
        print(f"  motions {lo_}-{hi_} px apart: n {int(mm.sum()):5d}  front wins {100 * np.mean(ef[mm] < eb[mm]):5.1f}%  "
              f"(the moving one wins: {100 * np.mean(np.where(sf[mm] > sb[mm], ef[mm] < eb[mm], eb[mm] < ef[mm])):5.1f}%)")
