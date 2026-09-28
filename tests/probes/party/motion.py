"""Real human motion as the interpolator's input: how far does a limb leave the straight line between frames?

Vision's RAW joints at 30 fps are the truth (independent of any field; the bone midpoints, which average two joints).
Decimate to a lower rate and rebuild the dropped frames from the kept ones, as each order of the shader family would:
  - hold      the nearest kept frame (no motion compensation)
  - linear    the straight line between the two kept neighbours (the two-frame, constant-velocity family)
  - cubic     the cubic through four kept frames (the four-frame quad's order; Catmull-Rom on the kept samples)
and score each against the frame Vision actually saw. Vision's own noise enters every predictor, and is measured on
still bodies (the floor row), so a predictor's excess over the floor is the motion's own departure from its model.
Also: speed and turning statistics of real limbs (the temporal seed's premise is that motion persists frame to frame).

    motion.py             the series from frames + vision -> $NP_SCRATCH/party-analysis/motion.npz, then the tables
    motion.py --score     the tables from the saved series"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

BN = list(pd.BONES)


def series():
    tracks = {}                          # (session, id) -> list of (t, ruler, 9 x (x, y, ok))
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
                mids = []
                for name in BN:
                    a, b = pd.BONES[name]
                    ok = min(best[a, 2], best[b, 2]) > 0.3
                    m = (best[a, :2] + best[b, :2]) / 2
                    mids.append((m[0], m[1], float(ok)))
                tracks.setdefault((si, tr["id"]), []).append((t, r, mids))
        print(f"{d.name}: {len(tracks)} tracks so far", flush=True)
    # flatten: session, id, t, ruler, then 9 x (x, y, ok)
    rows = [(k[0], k[1], t, r, *np.ravel(m)) for k, v in tracks.items() for t, r, m in v]
    a = np.array(rows, float)
    np.savez_compressed(pd.NP / "party-analysis" / "motion.npz", rows=a)
    return a


def runs(a):
    """Unbroken 30 fps runs per track: arrays (t, ruler, (n, 9, 3))."""
    out = []
    keys = a[:, 0] * 1e6 + a[:, 1]
    for key in np.unique(keys):
        m = a[keys == key]
        m = m[np.argsort(m[:, 2])]
        br = np.where(np.diff(m[:, 2]) > 1.5 / 30)[0] + 1
        for seg in np.split(m, br):
            if len(seg) >= 12:
                out.append((seg[:, 2], seg[:, 3], seg[:, 4:].reshape(-1, 9, 3)))
    return out


def catmull(p0, p1, p2, p3, u):
    return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u * u + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)


def score(a):
    R = runs(a)
    print(f"runs {len(R)}, frames {sum(len(r[0]) for r in R)}")
    groups = {g: [BN.index(b) for b in bs] for g, bs in pd.BONE_GROUPS.items()}
    # speed statistics (px/frame at 1280x960, 30 fps; and in rulers per frame)
    print("\nSPEED of bone midpoints, px/frame (1280x960, 30 fps): p50 / p90 / p99 / max; share over 16 / 24 / 36")
    for g, ix in groups.items():
        v = []
        vr = []
        for t, r, P in R:
            for b in ix:
                ok = (P[1:, b, 2] > 0) & (P[:-1, b, 2] > 0)
                s = np.hypot(*(P[1:, b, :2] - P[:-1, b, :2]).T)[ok]
                v.append(s)
                vr.append(s / r[1:][ok])
        v = np.concatenate(v)
        vr = np.concatenate(vr)
        print(f"  {g:10} n {len(v):7d}  {np.percentile(v, 50):5.1f} / {np.percentile(v, 90):5.1f} / {np.percentile(v, 99):5.1f} / "
              f"{v.max():6.1f}   over 16: {100 * (v > 16).mean():4.1f}%  24: {100 * (v > 24).mean():4.1f}%  36: {100 * (v > 36).mean():4.2f}%"
              f"   rulers/frame p90 {np.percentile(vr, 90):.3f}")
    # the interpolators, at decimation factors 2 (15 -> 30) and 3 (10 -> 30)
    for D in (2, 3):
        print(f"\nREBUILT FRAMES: keep every {D}th frame (30 -> {30 // D} fps), rebuild the rest; px error p50 / p90 "
              f"(moving: the mid-frame's local speed >= 4 px/frame at 30 fps)")
        for g, ix in groups.items():
            errs = {"hold": [], "linear": [], "cubic": []}
            for t, r, P in R:
                n = len(t)
                for s0 in range(0, n - 3 * D - 1):
                    k0, k1, k2, k3 = s0, s0 + D, s0 + 2 * D, s0 + 3 * D
                    for j in range(1, D):
                        kt = k1 + j
                        for b in ix:
                            if not all(P[k, b, 2] > 0 for k in (k0, k1, k2, k3, kt, kt - 1, kt + 1)):
                                continue
                            spd = np.hypot(*(P[kt + 1, b, :2] - P[kt - 1, b, :2])) / 2
                            if spd < 4:
                                continue
                            u = j / D
                            truth = P[kt, b, :2]
                            hold = P[k1, b, :2] if u < 0.5 else P[k2, b, :2]
                            lin = P[k1, b, :2] + u * (P[k2, b, :2] - P[k1, b, :2])
                            cub = catmull(P[k0, b, :2], P[k1, b, :2], P[k2, b, :2], P[k3, b, :2], u)
                            errs["hold"].append(np.hypot(*(hold - truth)))
                            errs["linear"].append(np.hypot(*(lin - truth)))
                            errs["cubic"].append(np.hypot(*(cub - truth)))
            if errs["linear"]:
                line = "  ".join(f"{k} {np.percentile(v, 50):5.2f} / {np.percentile(v, 90):5.2f}" for k, v in errs.items())
                win = np.mean(np.array(errs["cubic"]) < np.array(errs["linear"]))
                print(f"  {g:10} n {len(errs['linear']):7d}  {line}   cubic beats linear in {100 * win:4.1f}%")
    # turning: how often a moving limb reverses (the temporal seed's premise is persistence)
    print("\nTURNING: per moving frame (|v| >= 4 px/frame both sides), the angle between consecutive displacements")
    for g, ix in groups.items():
        angs = []
        for t, r, P in R:
            for b in ix:
                ok = (P[2:, b, 2] > 0) & (P[1:-1, b, 2] > 0) & (P[:-2, b, 2] > 0)
                v1 = P[1:-1, b, :2] - P[:-2, b, :2]
                v2 = P[2:, b, :2] - P[1:-1, b, :2]
                s1, s2 = np.hypot(*v1.T), np.hypot(*v2.T)
                m = ok & (s1 >= 4) & (s2 >= 4)
                c = (v1[m] * v2[m]).sum(1) / (s1[m] * s2[m])
                angs.append(np.degrees(np.arccos(np.clip(c, -1, 1))))
        angs = np.concatenate(angs)
        print(f"  {g:10} n {len(angs):7d}  turn p50 {np.percentile(angs, 50):5.1f} deg  p90 {np.percentile(angs, 90):5.1f}  "
              f"over 90 deg (a reversal) {100 * (angs > 90).mean():4.1f}%")


if __name__ == "__main__":
    p = pd.NP / "party-analysis" / "motion.npz"
    a = np.load(p)["rows"] if ("--score" in sys.argv and p.exists()) else series()
    score(a)
