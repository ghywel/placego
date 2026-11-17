"""ENERGY-TRANSFER.md 4.1-4.2: does a held ball share its holder's motion, and does that name the holding hand
better than distance does?

    heldball.py <session folder> [<session folder> ...]

Reads a LilysParty session (the party recorder's frames-NNN.jsonl: every track's 19 joints at ~30 Hz, source px,
y down; wrists are joints 10 = the child's left, 11 = the child's right) and the live lab's telemetry.jsonl beside
it (the balls at 10 Hz: [child track, side 0 left / 1 right, x, y, radius, glowing px, held]). NUMBERS ONLY: no
picture is read or written, and the data never leaves the machine (the party-data privacy rule).

1. The clocks: the lab's t starts a few ms after the recorder's hostT0, so a ball sample at lab t is joined to the
   frame nearest dt = t + offset. The offset is FOUND, not assumed: the one (in -0.5..+0.5 s) at which the balls sit
   closest to a wrist of their child. That is the instrument check.
2. For each child's ball, velocities over consecutive samples (0.1 s) of the ball and of each wrist of that child;
   over sliding 1 s windows while the ball MOVES (its speed RMS above 150 px/s), the vector correlation of the
   ball's velocity with each wrist's, and the relative speed |v_ball - v_wrist| as a fraction of the ball's.
3. Per window, three answers to "which hand holds it": the tracker's (the telemetry side), the nearest wrist over
   the window, and the shared motion (the higher correlation). How often they agree.

Pre-registered in ENERGY-TRANSFER.md 4.1 (commit ea58d47): the holder's correlation above 0.8 and the other hand's
below 0.3 when a ball is clearly held and moving.
"""
import json
import math
import pathlib
import sys

import numpy as np

LW, RW = 10, 11
WIN, MINSPEED = 10, 150.0          # samples (1 s at 10 Hz); px/s


def load(session):
    s = pathlib.Path(session)
    frames = []                                                   # (dt, {track: (left xyc, right xyc)})
    for f in sorted(s.glob("frames-*.jsonl")):
        with open(f) as fh:
            for line in fh:
                if '"tracks":[]' in line: continue
                d = json.loads(line)
                tr = {}
                for t in d.get("tracks", []):
                    j = t.get("joints") or t.get("j")
                    if not j or len(j) < 12: continue
                    tr[t["id"]] = (j[LW], j[RW])
                if tr: frames.append((d["dt"], tr))
    balls = []                                                    # (t, track, side, x, y)
    for f in sorted((s / "lab").glob("telemetry*.jsonl")):
        with open(f) as fh:
            for line in fh:
                if '"poi"' not in line: continue
                d = json.loads(line)
                for b in d["poi"]:
                    if b[6] == 0: balls.append((d["t"], b[0], b[1], float(b[2]), float(b[3])))
    return frames, balls


def nearest(frames, times, t):
    i = np.searchsorted(times, t)
    best = min((k for k in (i - 1, i) if 0 <= k < len(times)), key=lambda k: abs(times[k] - t))
    return frames[best] if abs(times[best] - t) < 0.05 else None


def wrists_at(frames, times, track, t):
    f = nearest(frames, times, t)
    if f is None or track not in f[1]: return None
    (lx, ly, lc), (rx, ry, rc) = f[1][track]
    return (np.array([lx, ly]) if lc > 0.3 else None, np.array([rx, ry]) if rc > 0.3 else None)


def vcorr(a, b):
    a = a - a.mean(0); b = b - b.mean(0)
    den = math.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / den) if den > 0 else float("nan")


for session in sys.argv[1:]:
    frames, balls = load(session)
    times = np.array([f[0] for f in frames])
    print(f"\n# {pathlib.Path(session).name}: {len(frames)} frames with tracks, {len(balls)} ball sightings (seen, not held)")
    if not balls or not frames: continue
    # 1. the clock offset: the balls sit nearest a wrist of their own child
    best = None
    for off in np.arange(-0.5, 0.51, 0.05):
        d = []
        for t, tr, side, x, y in balls[::3]:
            w = wrists_at(frames, times, tr, t + off)
            if not w: continue
            ds = [np.hypot(*(p - (x, y))) for p in w if p is not None]
            if ds: d.append(min(ds))
        if len(d) > 20 and (best is None or np.median(d) < best[1]): best = (off, float(np.median(d)), len(d))
    off = best[0]
    print(f"  clock offset {off:+.2f} s: the median ball-to-nearest-wrist distance {best[1]:.0f} px ({best[2]} samples)")
    # 2. per child: velocities and windows
    agree = {"tracker~motion": [0, 0], "nearest~motion": [0, 0], "tracker~nearest": [0, 0]}
    hold_r, other_r, hold_rel, other_rel, nwin = [], [], [], [], 0
    for tr in sorted({b[1] for b in balls}):
        seq = [b for b in balls if b[1] == tr]
        rows = []
        for t, _, side, x, y in seq:
            w = wrists_at(frames, times, tr, t + off)
            if not w or w[0] is None or w[1] is None: continue
            rows.append((t, side, np.array([x, y]), w[0], w[1]))
        # consecutive samples ~0.1 s apart -> velocities
        vel = []
        for a, b in zip(rows, rows[1:]):
            dt = b[0] - a[0]
            if 0.05 < dt < 0.2:
                vel.append((b[0], b[1], (b[2] - a[2]) / dt, (b[3] - a[3]) / dt, (b[4] - a[4]) / dt,
                            np.hypot(*(b[2] - b[3])), np.hypot(*(b[2] - b[4]))))
        for i in range(0, len(vel) - WIN + 1, WIN // 2):
            w = vel[i:i + WIN]
            if w[-1][0] - w[0][0] > WIN * 0.15: continue                  # a gap inside the window
            vb = np.array([v[2] for v in w]); vl = np.array([v[3] for v in w]); vr = np.array([v[4] for v in w])
            if math.sqrt((vb ** 2).sum(1).mean()) < MINSPEED: continue      # the ball is not moving
            nwin += 1
            rl, rr = vcorr(vb, vl), vcorr(vb, vr)
            rel_l = math.sqrt(((vb - vl) ** 2).sum(1).mean() / (vb ** 2).sum(1).mean())
            rel_r = math.sqrt(((vb - vr) ** 2).sum(1).mean() / (vb ** 2).sum(1).mean())
            by_motion = 0 if rl > rr else 1
            by_near = 0 if np.median([v[5] for v in w]) < np.median([v[6] for v in w]) else 1
            by_tracker = int(round(np.mean([v[1] for v in w])))
            for k, (p, q) in {"tracker~motion": (by_tracker, by_motion), "nearest~motion": (by_near, by_motion),
                              "tracker~nearest": (by_tracker, by_near)}.items():
                agree[k][0] += p == q; agree[k][1] += 1
            (hold_r if by_motion == 0 else other_r).append(rl); (other_r if by_motion == 0 else hold_r).append(rr)
            (hold_rel if by_motion == 0 else other_rel).append(rel_l); (other_rel if by_motion == 0 else hold_rel).append(rel_r)
    if not nwin:
        print("  no window with a moving ball"); continue
    print(f"  {nwin} one-second windows with the ball moving (speed RMS > {MINSPEED:.0f} px/s)")
    print(f"  the better-correlated hand: r median {np.median(hold_r):.2f} (p25 {np.percentile(hold_r, 25):.2f}); "
          f"relative speed {np.median(hold_rel):.2f} of the ball's")
    print(f"  the other hand:             r median {np.median(other_r):.2f} (p75 {np.percentile(other_r, 75):.2f}); "
          f"relative speed {np.median(other_rel):.2f}")
    print(f"  windows with holder r > 0.8 and other < 0.3: {sum(1 for a, b in zip(hold_r, other_r) if a > 0.8 and b < 0.3)} of {nwin}")
    print("  agreement: " + ", ".join(f"{k} {a}/{n}" for k, (a, n) in agree.items()))
