"""P4: depth from the field -- its divergence over a child's body against the child's growth in Vision's skeleton.

THREEDIMENSIONAL.md 2.2: a rigid fronto-parallel patch at depth Z has image scale s ~ 1/Z, so the field's divergence
over it is div = 2 sigma with sigma = -Z'/Z = d ln s / dt. The field side is the party app's own pooled estimator: a
robust (Huber, then Tukey) affine fit of the field over the child's core cells every frame (frames-NNN.jsonl,
tracks[].body = [vx, vy, div, curl, residual, samples], per SECOND). The truth side is independent of the field:
the child's body ruler in Vision's RAW joints (partydata.ruler, the third-longest of eleven segments), its log
fitted against time over a sliding window, doubled.

    depth.py [--window 0.5]      rows -> $NP_SCRATCH/party-analysis/depth.npz, then the scores
A fused track (the solver's, stable ids) supplies identity; its neck finds the Vision person each frame."""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

WIN = float(sys.argv[sys.argv.index("--window") + 1]) if "--window" in sys.argv else 0.5


def series():
    out = []                        # rows: session, id, t, ln ruler, body div (/s), body samples, crossing
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
                if tr["state"] != "live" or tr["body"][5] < 20:
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
                out.append((si, tr["id"], t, np.log(r), tr["body"][2], tr["body"][5], float(bool(o.get("crossing")))))
        print(f"{d.name}: {len(out)} rows so far", flush=True)
    a = np.array(out, float)
    np.savez_compressed(pd.NP / "party-analysis" / "depth.npz", rows=a)
    return a


def score(a):
    si, tid, t, lr, div, ns, cross = a.T
    rows = []
    for key in sorted(set(zip(si.tolist(), tid.tolist()))):
        m = (si == key[0]) & (tid == key[1])
        tt, ll, dd = t[m], lr[m], div[m]
        if len(tt) < 30:
            continue
        o = np.argsort(tt)
        tt, ll, dd, cc = tt[o], ll[o], dd[o], cross[m][o]
        lo = np.searchsorted(tt, tt - WIN / 2)
        hi = np.searchsorted(tt, tt + WIN / 2, side="right")
        for k in range(0, len(tt), 3):                                # every third frame: windows overlap anyway
            w = slice(lo[k], hi[k])
            if hi[k] - lo[k] < 10 or np.ptp(tt[w]) < 0.6 * WIN:
                continue
            slope = np.polyfit(tt[w] - tt[k], ll[w], 1)[0]           # d ln s / dt, per second
            rows.append((2 * slope, np.mean(dd[w]), cc[k]))
    r = np.array(rows)
    truth, field, cr = r.T
    print(f"windows {len(r)} (window {WIN} s; truth = 2 d ln(ruler)/dt, field = the body fit's divergence, both per s)")
    for lo in (0.0, 0.2, 0.4, 0.8):
        m = np.abs(truth) >= lo
        if m.sum() < 30:
            continue
        c = np.corrcoef(truth[m], field[m])[0, 1]
        g = np.sum(truth[m] * field[m]) / np.sum(truth[m] ** 2)
        agree = np.mean(np.sign(truth[m]) == np.sign(field[m]))
        print(f"  |truth| >= {lo:.1f}/s: n {int(m.sum()):6d}  corr {c:5.2f}  gain {g:5.2f}  sign agreement {100 * agree:4.1f}%  "
              f"field p50 |div| {np.median(np.abs(field[m])):.3f}/s  truth p50 {np.median(np.abs(truth[m])):.3f}/s")


if __name__ == "__main__":
    p = pd.NP / "party-analysis" / "depth.npz"
    a = np.load(p)["rows"] if ("--score" in sys.argv and p.exists()) else series()
    score(a)
