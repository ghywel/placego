#!/usr/bin/env python3
"""The cadence of a source: how much of it is held drawings, and in what pattern (2026-09-19).

    cadence.py <source> [start-seconds] [duration-seconds]     (FFMPEG in the environment, or ~/np-build/ffmpeg)

Reads ffmpeg's per-frame scene score (the select filter's `scene`, a normalised whole-frame difference from the
previous frame) over the window and classifies every frame as a MOVE or a HELD copy of the previous one. The
rule is RELATIVE, because an absolute threshold does not survive a real encoder: in the on-twos stretches of the
anime episode to hand, held drawings scored 0.0056 after the encoder and small real moves 0.0126 (measured
2026-09-19), and a dialogue scene's real mouth movements score 0.001 while a static hold's encoder noise scores
0.0002. So a frame is HELD when its score is below a fraction (HELD_RATIO, 0.35) of the local level of change --
the 80th percentile of the scores in a sliding window of two seconds -- and above nothing.
CALIBRATED 2026-09-19 on the pool: a live-action episode (which holds nothing) reads 27% of its moving frames
as twos/threes at a ratio of 0.15 and 16% at 0.08, while two anime episodes read 50-53% and 44-45% -- the
anime figure is stable where the control falls, so 0.08 is the default and 16% is the false floor to read
every figure against. A pattern detector (periodicity, as the pulldown detectors do) is the way past that
floor; this tool is the survey instrument, not the detector. Also: the static rule -- a static shot whose
local level is itself noise classifies as all held, which is right (nothing moved) and harmless (nothing to
interpolate), and it is reported separately as STATIC so it does not inflate the cadence figures.

The pattern is read from the run lengths of held frames between moves: a run of 0 held frames after a move is
content on ones, 1 is twos, 2 is threes, 3 or more is a hold. The report gives, for the moving frames (static
shots excluded), the share of source intervals that fall in each class, and the fraction of the window's frames
that a cadence-aware interpolator would treat differently from a two-frame one (every frame in a twos or threes
run). A window across cuts is fine: a cut is a move.
"""
import os, re, subprocess, sys, statistics

FF = os.environ.get("FFMPEG", os.path.expanduser("~/np-build/ffmpeg/ffmpeg"))
HELD_RATIO = float(os.environ.get("HELD_RATIO", "0.08"))
STATIC_LEVEL = float(os.environ.get("STATIC_LEVEL", "0.0015"))   # a local level below this is a static shot (encoder noise only)
WIN = 48                                                          # the sliding window, frames (two seconds at 24)

def scores(src, start, dur):
    cmd = [FF, "-hide_banner", "-nostats", "-loglevel", "info"]
    if start: cmd += ["-ss", str(start)]
    if dur: cmd += ["-t", str(dur)]
    cmd += ["-i", src, "-map", "0:v:0", "-vf", "select='gt(scene,-1)',metadata=print:key=lavfi.scene_score:file=-", "-f", "null", "-"]
    out = subprocess.run(cmd, capture_output=True, text=True, errors="replace", stdin=subprocess.DEVNULL).stdout
    return [float(m) for m in re.findall(r"scene_score=([0-9.eE+-]+)", out)]

def classify(v):
    n = len(v)
    held, static = [False] * n, [False] * n
    for i in range(n):
        lo, hi = max(0, i - WIN // 2), min(n, i + WIN // 2)
        w = sorted(v[lo:hi])
        level = w[int(0.8 * (len(w) - 1))]
        static[i] = level < STATIC_LEVEL
        held[i] = v[i] < HELD_RATIO * level
    return held, static

def main():
    src = sys.argv[1]; start = sys.argv[2] if len(sys.argv) > 2 else None; dur = sys.argv[3] if len(sys.argv) > 3 else None
    v = scores(src, start, dur)
    if len(v) < WIN: print("too few frames"); return
    v[0] = 1.0                                                   # the first frame is a move by definition
    held, static = classify(v)
    n = len(v)
    # run lengths of held frames following each move, moving shots only
    runs = []; run = 0; in_static = False
    for i in range(n):
        if static[i]: in_static = True; run = 0; continue
        if held[i] and not in_static: run += 1
        else:
            if i > 0 and not in_static: runs.append(run)
            run = 0; in_static = False
    classes = {"ones": 0, "twos": 0, "threes": 0, "holds": 0}
    for r in runs:
        classes["ones" if r == 0 else "twos" if r == 1 else "threes" if r == 2 else "holds"] += 1
    total = sum(classes.values()) or 1
    frames_cadence = sum(r + 1 for r in runs if r in (1, 2))
    moving_frames = sum(1 for s in static if not s)
    print(f"{os.path.basename(src)[:60]}")
    print(f"  frames {n}, static-shot frames {n - moving_frames} ({100 * (n - moving_frames) / n:.0f}%), moving-shot frames {moving_frames}")
    print(f"  intervals in moving shots: {total};  ones {100 * classes['ones'] / total:.0f}%  twos {100 * classes['twos'] / total:.0f}%  threes {100 * classes['threes'] / total:.0f}%  longer holds {100 * classes['holds'] / total:.0f}%")
    print(f"  frames a cadence-aware interpolator treats differently (in twos/threes runs): {100 * frames_cadence / max(1, moving_frames):.0f}% of moving-shot frames")
    if runs:
        print(f"  median held run {statistics.median(runs):.0f}, p90 {sorted(runs)[int(0.9 * (len(runs) - 1))]}")

if __name__ == "__main__":
    main()
