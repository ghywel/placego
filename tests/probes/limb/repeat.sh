#!/bin/bash
# limb.sh N times (the propagated family is not bit-reproducible on the Mac's MoltenVK: a single run's band can
# move by several dB -- 22.0 vs 16.2 at 42-48 px on K2, the same file), then each mode's band means over the runs
# with their spread.
#   ./repeat.sh <case> <N>       SHADERS as for limb.sh
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CASE="${1:-K1_limb_sweep_wall}"; N="${2:-5}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$HERE/../../../../.." && pwd)/np-scratch}"
BASE="$NP_SCRATCH/limb/rep"
rm -rf "$BASE/$CASE"
for i in $(seq 1 "$N"); do
  OUTROOT="$BASE/$CASE/run$i" "$HERE/limb.sh" "$CASE" > "$BASE/$CASE.run$i.txt" 2>&1 || true
  mkdir -p "$BASE/$CASE"; mv "$BASE/$CASE.run$i.txt" "$BASE/$CASE/"
done
PY="${PY:-$HOME/np-build/venv/bin/python3}"
"$PY" - "$BASE/$CASE" "$N" <<'PY'
import sys, os, re, statistics, glob
root, N = sys.argv[1], int(sys.argv[2])
def load(p):
    d = {}
    for line in open(p, errors="replace"):
        m = re.search(r"psnr_y:([0-9.]+|inf)", line); n = re.match(r"n:(\d+)", line)
        if m and n: d[int(n.group(1))] = 99.0 if m.group(1) == "inf" else float(m.group(1))
    return d
def speed(n):
    return (288 + 1152 * (n - 1) / 60.0) / 24.0
bands = [(12, 18), (18, 24), (24, 30), (30, 36), (36, 42), (42, 48), (48, 61)]
runs = sorted(glob.glob(os.path.join(root, "run*", "*", "")))
modes = sorted({f[:-4] for r in runs for f in os.listdir(r) if f.endswith(".log") and not f.startswith(("_", "._"))})
modes = ["hold", "linear"] + [m for m in modes if m not in ("hold", "linear")]
print(f"== {os.path.basename(root)}: mean (sd) over {len(runs)} runs, PSNR Y in the box following the limb")
print("mode".ljust(52) + "".join(f"{lo}-{hi}".ljust(14) for lo, hi in bands))
for m in modes:
    cells = []
    for lo, hi in bands:
        per = []
        for r in runs:
            p = os.path.join(r, m + ".log")
            if not os.path.exists(p): continue
            v = [x for n, x in load(p).items() if n > 5 and n % 5 != 1 and lo <= speed(n) < hi]
            if v: per.append(statistics.mean(v))
        cells.append(f"{statistics.mean(per):5.2f} ({statistics.pstdev(per):4.2f})" if per else "-")
    print(m[:50].ljust(52) + "".join(c.ljust(14) for c in cells))
PY
