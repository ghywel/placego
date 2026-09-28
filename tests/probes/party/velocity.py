"""P0-P3: the recommendation's field against Vision's joints, on real children (PREDICTION.md).

For every whole-field record (2-px cells; once a second, plus every frame of a crossing), the Vision results at its
two frames (A = t - interval, B = t) are paired person to person, and for every joint confident in both:
    truth  d = joint(B) - joint(A)                    (Vision; independent of the field)
    field  f = median of the field in the 3x3 cells at joint(A)   (forward A -> B, defined on A's grid)
Rows go to $NP_SCRATCH/party-analysis/velocity.npz; `--table` prints the speed-binned scores.

    velocity.py [--table] [--limit N]
Columns: session, t, burst (the record is part of a crossing's every-frame run), ruler (px), joint, conf A, conf B,
dx, dy, fx, fy, still (the 5x5 window's largest |f|, for P0)."""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import partydata as pd  # noqa: E402

OUT = pd.NP / "party-analysis"
LAG = int(sys.argv[sys.argv.index("--lag") + 1]) if "--lag" in sys.argv else 0
OUT.mkdir(parents=True, exist_ok=True)


def collect(limit=None):
    rows = []
    for si, d in enumerate(pd.sessions()):
        vis = pd.vision(d)
        vt = np.array(sorted(vis))
        segs = pd.fields(d, "full")
        ts = np.concatenate([m["t"] for m in segs]) if segs else np.array([])
        n_rec = 0
        for m in segs:
            for k in range(len(m)):
                rec = m[k]
                t, iv = float(rec["t"]), float(rec["interval"])
                # a burst frame: another record within half a second (the 1 Hz schedule leaves a second between)
                near = np.abs(ts - t)
                burst = int(((near > 1e-6) & (near < 0.5)).any())
                # --lag k: score against Vision k frames EARLIER (the alignment check: the true pairing must win)
                sh = LAG * iv
                ka = np.searchsorted(vt, t - iv - sh)
                kb = np.searchsorted(vt, t - sh)
                def at(k, want):
                    for c in (k - 1, k, k + 1):
                        if 0 <= c < len(vt) and abs(vt[c] - want) < 0.002:
                            return vis[vt[c]]
                    return None
                A, B = at(ka, t - iv - sh), at(kb, t - sh)
                if A is None or B is None or not len(A) or not len(B):
                    continue
                uv = rec["uv"]
                for i, j in pd.match(A, B):
                    r = np.nanmax([pd.ruler(A[i]), pd.ruler(B[j])])
                    for jn in range(19):
                        ca, cb = A[i, jn, 2], B[j, jn, 2]
                        if not (ca > 0.3 and cb > 0.3):
                            continue
                        x, y = A[i, jn, :2]
                        f = pd.sample(uv, x, y, r=1)
                        if f is None:
                            continue
                        big = np.asarray(uv[int(y // 2) - 2:int(y // 2) + 3, int(x // 2) - 2:int(x // 2) + 3], np.float32)
                        still = float(np.hypot(big[..., 0], big[..., 1]).max())
                        dx, dy = B[j, jn, :2] - A[i, jn, :2]
                        rows.append((si, t, burst, r, jn, ca, cb, dx, dy, f[0], f[1], still))
                    for name, (ja, jb) in pd.BONES.items():
                        c = min(A[i, ja, 2], A[i, jb, 2], B[j, ja, 2], B[j, jb, 2])
                        if not c > 0.3:
                            continue
                        pa = (A[i, ja, :2] + A[i, jb, :2]) / 2
                        pb = (B[j, ja, :2] + B[j, jb, :2]) / 2
                        f = pd.sample(uv, pa[0], pa[1], r=1)
                        if f is None:
                            continue
                        big = np.asarray(uv[int(pa[1] // 2) - 2:int(pa[1] // 2) + 3, int(pa[0] // 2) - 2:int(pa[0] // 2) + 3], np.float32)
                        still = float(np.hypot(big[..., 0], big[..., 1]).max())
                        dx, dy = pb - pa
                        rows.append((si, t, burst, r, pd.BONE_IDS[name], c, c, dx, dy, f[0], f[1], still))
                n_rec += 1
                if limit and n_rec >= limit:
                    break
            if limit and n_rec >= limit:
                break
        print(f"{d.name}: {n_rec} field records scored, {len(rows)} joint rows so far", flush=True)
    a = np.array(rows, float)
    np.savez_compressed(OUT / ("velocity.npz" if LAG == 0 else f"velocity-lag{LAG}.npz"), rows=a)
    return a


BINS = [0, 1, 2, 4, 8, 16, 24, 36, 48, 1e9]


def table(a):
    si, t, burst, r, jn, ca, cb, dx, dy, fx, fy, still = a.T
    sp = np.hypot(dx, dy)
    fsp = np.hypot(fx, fy)
    err = np.hypot(fx - dx, fy - dy)
    gain = (fx * dx + fy * dy) / np.maximum(sp * sp, 1e-9)
    ang = np.degrees(np.abs(np.arctan2(fx * dy - fy * dx, fx * dx + fy * dy)))
    gross = err > np.maximum(3.0, 0.5 * sp)
    print(f"rows {len(a)}: burst {int(burst.sum())}, 1 Hz {int((burst == 0).sum())}")
    # P0: Vision's jitter where the field says still
    st = (still < 0.3) & (ca > 0.5) & (cb > 0.5)
    groups = {**{g: [pd.BONE_IDS[b] for b in bs] for g, bs in pd.BONE_GROUPS.items()}, **{"j:" + g: js for g, js in pd.GROUPS.items()}}
    for g, js in groups.items():
        m = st & np.isin(jn, js)
        if m.sum() > 20:
            print(f"P0 Vision jitter, {g:6s}: n {int(m.sum()):6d}  |d| p50 {np.median(sp[m]):.2f}  p90 {np.percentile(sp[m], 90):.2f}  "
                  f"RMS {np.sqrt(np.mean(sp[m] ** 2)):.2f} px")
    for label, sel in (("1 Hz (unbiased in time)", burst == 0), ("crossings (every frame)", burst == 1)):
        print(f"\n== {label}")
        for g, js in groups.items():
            if g.startswith("j:") and "--joints" not in sys.argv:
                continue
            print(f"  {g}")
            for lo, hi in zip(BINS[:-1], BINS[1:]):
                m = sel & np.isin(jn, js) & (sp >= lo) & (sp < hi)
                n = int(m.sum())
                if n < 15:
                    continue
                q1, q2, q3 = np.percentile(gain[m], [25, 50, 75])
                print(f"    {lo:4.0f}-{hi if hi < 1e8 else 99:<4.0f} px/f  n {n:6d}  gain p50 {q2:5.2f} [{q1:5.2f},{q3:5.2f}]  "
                      f"angle p50 {np.median(ang[m]):5.1f}  |f-d| p50 {np.median(err[m]):5.2f}  gross {100 * gross[m].mean():4.1f}%  "
                      f"|f|/|d| p50 {np.median(fsp[m] / np.maximum(sp[m], 1e-9)):4.2f}")


if __name__ == "__main__":
    lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    p = OUT / "velocity.npz"
    a = np.load(p)["rows"] if ("--table" in sys.argv and p.exists() and not lim) else collect(lim)
    table(a)
