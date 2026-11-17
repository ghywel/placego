"""ENERGY-TRANSFER.md 3.6, the census's second reading: flagged frames split into RUNS.

    census_runs.py < census log (the JSON lines census.py film prints)

A real impact shows on about three consecutive frames (the controls: 28-30, 39-41, 76-78 around each wall hit). A
run of flagged frames longer than MAXRUN is not one impact: an oscillation, a flicker, or the field's alias on a
periodic texture. This reading was added AFTER the first film showed runs of 12+ frames (2026-09-30), and it is
reported as such. The pre-registered number is the raw frame fraction, still printed beside it.
"""
import json
import sys

MAXRUN = 4


def runs(frames):
    out, cur = [], []
    for k in sorted(frames):
        if cur and k == cur[-1] + 1: cur.append(k)
        else:
            if cur: out.append(cur)
            cur = [k]
    if cur: out.append(cur)
    return out


tot = {"frames": 0, "flagged": 0, "impacts": 0, "impact_frames": 0, "long": 0, "long_frames": 0}
per_kind = {}
print(f"{'source':58s} {'frames':>6s} {'flagged %':>9s} {'impacts':>7s} {'per min':>7s} {'long runs':>9s} {'long %':>6s}")
for line in sys.stdin:
    if not line.startswith("JSON "): continue
    d = json.loads(line[5:])
    fps = eval(d["fps"]) if "/" in d["fps"] else float(d["fps"])
    for ex in d["extracts"]:
        rs = runs(ex["local_at"])
        imp = [r for r in rs if len(r) <= MAXRUN]; lng = [r for r in rs if len(r) > MAXRUN]
        n = ex["frames"]
        row = {"frames": n, "flagged": ex["local"], "impacts": len(imp), "impact_frames": sum(map(len, imp)),
               "long": len(lng), "long_frames": sum(map(len, lng))}
        for k in tot: tot[k] += row[k]
        mins = n / fps / 60
        print(f"{d['video'][:56]:58s} {n:6d} {100 * ex['local'] / max(n, 1):8.2f}% {len(imp):7d} {len(imp) / max(mins, 1e-9):7.1f} "
              f"{len(lng):9d} {100 * row['long_frames'] / max(n, 1):5.1f}%")
mins = tot["frames"] / 24 / 60
print(f"\nALL: {tot['frames']} frames (~{mins:.0f} min); flagged {100 * tot['flagged'] / tot['frames']:.2f} % (the pre-registered "
      f"number); impacts (runs <= {MAXRUN}) {tot['impacts']} = {tot['impacts'] / mins:.1f} per minute, covering "
      f"{100 * tot['impact_frames'] / tot['frames']:.2f} % of frames; long runs {tot['long']} covering "
      f"{100 * tot['long_frames'] / tot['frames']:.2f} %")
