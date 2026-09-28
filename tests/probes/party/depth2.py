"""P4, the truth rebuilt: the field's divergence and curl over a child's body against a RIGID fit of the child's head
and torso in Vision's raw joints.

depth.py's truth (the body ruler's log rate) moves when a limb rises as much as when the child comes closer. Here the
truth is a similarity fit (scale s, rotation theta, shift) between the head-and-torso joints (nose, eyes, ears, neck,
shoulders, root, hips: 11 points, no limbs) at frames k - D and k + D, kept only where the fit is near rigid (its
residual under RES_MAX of the body ruler), so a scale change there is depth, not pose:
    truth divergence = 2 ln(s) / (2 D dt)        THREEDIMENSIONAL.md 2.2: div = 2 sigma, sigma = -Z'/Z = d ln s/dt
    truth curl       = 2 theta / (2 D dt)        a rigid image-plane rotation at omega has curl 2 omega
The field side is the party app's pooled robust affine fit over the child's core cells (frames' body[2], body[3],
per second), averaged over the same frames. Vision and the field share nothing but the pictures.

    depth2.py [--d 4] [--res 0.04]     rows -> $NP_SCRATCH/party-analysis/depth2.npz, then the scores"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

D = int(sys.argv[sys.argv.index("--d") + 1]) if "--d" in sys.argv else 4
RES_MAX = float(sys.argv[sys.argv.index("--res") + 1]) if "--res" in sys.argv else 0.04
RIGID = [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14]


def collect():
    rows = []          # session, id, t, ruler, body div, body curl, body samples, 19 x (x, y, c)
    for si, d in enumerate(pd.sessions()):
        vis = pd.vision(d)
        vt = np.array(sorted(vis))
        for o in pd.jsonl(d, "frames"):
            t = o["t"]
            k = np.searchsorted(vt, t)
            V = None
            for c in (k - 1, k, k + 1):
                if 0 <= c < len(vt) and abs(vt[c] - t) < 0.002:
                    V = vis[vt[c]]
            if V is None or not len(V):
                continue
            for tr in o["tracks"]:
                if tr["state"] != "live":
                    continue
                nk = np.array(tr["joints"][5][:2], float)
                best, bd = None, 1e9
                for p in V:
                    if p[5, 2] > 0.3:
                        dist = np.hypot(*(p[5, :2] - nk))
                        if dist < bd:
                            best, bd = p, dist
                if best is None:
                    continue
                r = pd.ruler(best)
                if not np.isfinite(r) or bd > 0.3 * r:
                    continue
                b = tr["body"]
                rows.append((si, tr["id"], t, r, b[2], b[3], b[5], *best.ravel()))
        print(f"{d.name}: {len(rows)} rows so far", flush=True)
    a = np.array(rows, float)
    np.savez_compressed(pd.NP / "party-analysis" / "depth2.npz", rows=a)
    return a


def similarity(P, Q):
    """Scale, rotation (rad) and RMS residual of the best similarity map P -> Q (2D Umeyama)."""
    mp, mq = P.mean(0), Q.mean(0)
    X, Y = P - mp, Q - mq
    vx = (X ** 2).sum() / len(P)
    S = Y.T @ X / len(P)
    U, sv, Vt = np.linalg.svd(S)
    dd = np.sign(np.linalg.det(U @ Vt))
    R = U @ np.diag([1, dd]) @ Vt
    s = (sv[0] + dd * sv[1]) / vx
    res = np.sqrt(((Y - s * (X @ R.T)) ** 2).sum(1).mean())
    return s, np.arctan2(R[1, 0], R[0, 0]), res


def score(a):
    out = []
    keys = a[:, 0] * 1e6 + a[:, 1]
    for key in np.unique(keys):
        m = a[keys == key]
        m = m[np.argsort(m[:, 2])]
        t = m[:, 2]
        J = m[:, 7:].reshape(-1, 19, 3)
        for k in range(D, len(m) - D, 2):
            ka, kb = k - D, k + D
            span = t[kb] - t[ka]
            if abs(span - 2 * D / 30) > 1.5 / 30:
                continue                                         # a gap in the track
            ok = [j for j in RIGID if J[ka, j, 2] > 0.4 and J[kb, j, 2] > 0.4]
            if len(ok) < 6:
                continue
            s, th, res = similarity(J[ka, ok, :2], J[kb, ok, :2])
            r = m[k, 3]
            if not (0.5 < s < 2) or res > RES_MAX * r:
                continue
            w = slice(ka, kb + 1)
            if m[w, 6].min() < 20:
                continue
            out.append((2 * np.log(s) / span, 2 * th / span, np.mean(m[w, 4]), np.mean(m[w, 5]), res / r, r))
    o = np.array(out)
    tdiv, tcurl, fdiv, fcurl, rel, r = o.T
    print(f"near-rigid windows {len(o)} (D {D} frames each side, head-and-torso fit residual < {RES_MAX} ruler)")
    for name, tv, fv in (("divergence (depth)", tdiv, fdiv), ("curl (image-plane turn)", tcurl, fcurl)):
        print(f"  {name}")
        for lo in (0.0, 0.2, 0.4, 0.8, 1.6):
            m = np.abs(tv) >= lo
            if m.sum() < 30:
                continue
            c = np.corrcoef(tv[m], fv[m])[0, 1]
            g = np.sum(tv[m] * fv[m]) / np.sum(tv[m] ** 2)
            ag = np.mean(np.sign(tv[m]) == np.sign(fv[m]))
            print(f"    |truth| >= {lo:.1f}/s: n {int(m.sum()):6d}  corr {c:5.2f}  gain {g:5.2f}  sign agreement {100 * ag:4.1f}%  "
                  f"truth p50 |{np.median(np.abs(tv[m])):.3f}|/s  field p50 |{np.median(np.abs(fv[m])):.3f}|/s")
        # the dilution test: a halo of fixed width dilutes a small body's gradient more than a large one's
        for lo_r, hi_r in ((0, 110), (110, 140), (140, 180), (180, 250), (250, 5000)):
            m = (np.abs(tv) >= 0.3) & (r >= lo_r) & (r < hi_r)
            if m.sum() < 30:
                continue
            g = np.sum(tv[m] * fv[m]) / np.sum(tv[m] ** 2)
            print(f"      ruler {lo_r:4}-{hi_r:<4} px, |truth| >= 0.3/s: n {int(m.sum()):5d}  gain {g:5.2f}  "
                  f"corr {np.corrcoef(tv[m], fv[m])[0, 1]:5.2f}")


if __name__ == "__main__":
    p = pd.NP / "party-analysis" / "depth2.npz"
    a = np.load(p)["rows"] if ("--score" in sys.argv and p.exists()) else collect()
    score(a)
