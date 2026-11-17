"""Is the tensor's under-read on real bodies the party app's body fit or the field itself?

depth2.py scored the app's pooled fit (its core cells, Huber then Tukey) and read divergence at ~0.46 of truth and
curl at ~0.3. Here the estimator is replaced: for every whole-field record, a plain least-squares affine fit of the
RAW field (2-px cells) over the child's torso (the quadrilateral shoulders-hips, shrunk to INNER of itself about its
centre, so no cell sits on the body's edge) gives divergence and curl per frame. The truth is depth2's: a similarity
fit of the head-and-torso joints between Vision's frames k - D and k + D, near-rigid windows only.

    torso_fit.py [--inner 0.6]       the scores (1 Hz records and crossing runs together)"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402
from depth2 import RIGID, similarity  # noqa: E402

INNER = float(sys.argv[sys.argv.index("--inner") + 1]) if "--inner" in sys.argv else 0.6
D = 4


def inside(poly, x, y):
    """Points inside a convex quadrilateral (vertices in order)."""
    s = None
    for k in range(4):
        (x1, y1), (x2, y2) = poly[k], poly[(k + 1) % 4]
        c = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
        s = (c >= 0) if s is None else (s & (c >= 0))
    s2 = None
    for k in range(4):
        (x1, y1), (x2, y2) = poly[k], poly[(k + 1) % 4]
        c = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
        s2 = (c <= 0) if s2 is None else (s2 & (c <= 0))
    return s | s2


rows = []
for si, d in enumerate(pd.sessions()):
    vis = pd.vision(d)
    vt = np.array(sorted(vis))
    def at(want):
        c = np.searchsorted(vt, want)
        for x in (c - 1, c, c + 1):
            if 0 <= x < len(vt) and abs(vt[x] - want) < 0.002:
                return vis[vt[x]]
        return None
    for m in pd.fields(d, "full"):
        for k in range(len(m)):
            t, iv = float(m["t"][k]), float(m["interval"][k])
            A = at(t - iv)
            Ea, Eb = at(t - iv - D / 30), at(t - iv + D / 30)
            if A is None or Ea is None or Eb is None or not len(A):
                continue
            uv = None
            for p in A:
                if min(p[6, 2], p[7, 2], p[13, 2], p[14, 2]) < 0.5:
                    continue
                r = pd.ruler(p)
                if not np.isfinite(r):
                    continue
                # the same child at k - D and k + D: nearest neck
                def near(V):
                    best, bd = None, 1e9
                    for q in V:
                        if q[5, 2] > 0.3 and p[5, 2] > 0.3:
                            dd = np.hypot(*(q[5, :2] - p[5, :2]))
                            if dd < bd:
                                best, bd = q, dd
                    return best if bd < 0.4 * r else None
                qa, qb = near(Ea), near(Eb)
                if qa is None or qb is None:
                    continue
                ok = [j for j in RIGID if qa[j, 2] > 0.4 and qb[j, 2] > 0.4]
                if len(ok) < 6:
                    continue
                s, th, res = similarity(qa[ok, :2], qb[ok, :2])
                if not (0.5 < s < 2) or res > 0.04 * r:
                    continue
                span = 2 * D / 30
                quad = np.array([p[6, :2], p[7, :2], p[14, :2], p[13, :2]])
                c0 = quad.mean(0)
                quad = c0 + INNER * (quad - c0)
                x0, y0 = np.floor(quad.min(0) / 2).astype(int)
                x1, y1 = np.ceil(quad.max(0) / 2).astype(int)
                if uv is None:
                    uv = np.asarray(m["uv"][k], np.float32)
                H, W = uv.shape[:2]
                x0, y0, x1, y1 = max(x0, 0), max(y0, 0), min(x1, W - 1), min(y1, H - 1)
                if x1 - x0 < 3 or y1 - y0 < 3:
                    continue
                gx, gy = np.meshgrid(np.arange(x0, x1 + 1), np.arange(y0, y1 + 1))
                px, py = (gx + 0.5) * 2, (gy + 0.5) * 2
                inn = inside(quad, px, py)
                if inn.sum() < 30:
                    continue
                X = np.stack([np.ones(inn.sum()), px[inn] - c0[0], py[inn] - c0[1]], 1)
                U = uv[gy[inn], gx[inn]]
                cu = np.linalg.lstsq(X, U[:, 0], rcond=None)[0]
                cv = np.linalg.lstsq(X, U[:, 1], rcond=None)[0]
                div = (cu[1] + cv[2]) / iv                 # per second
                curl = (cv[1] - cu[2]) / iv
                rows.append((2 * np.log(s) / span, 2 * th / span, div, curl, r, int(inn.sum())))
    print(f"{d.name}: {len(rows)} torsos so far", flush=True)

o = np.array(rows)
tdiv, tcurl, fdiv, fcurl, r, n = o.T
print(f"torso fits {len(o)} (inner {INNER} of the shoulder-hip quadrilateral, plain least squares on the raw field)")
for name, tv, fv in (("divergence", tdiv, fdiv), ("curl", tcurl, fcurl)):
    for lo in (0.2, 0.4, 0.8):
        mm = np.abs(tv) >= lo
        if mm.sum() < 30:
            continue
        g = np.sum(tv[mm] * fv[mm]) / np.sum(tv[mm] ** 2)
        print(f"  {name:10} |truth| >= {lo}/s: n {int(mm.sum()):5d}  corr {np.corrcoef(tv[mm], fv[mm])[0, 1]:5.2f}  gain {g:5.2f}  "
              f"sign {100 * np.mean(np.sign(tv[mm]) == np.sign(fv[mm])):4.1f}%")
np.savez_compressed(pd.NP / "party-analysis" / "torso_fit.npz", rows=o)
