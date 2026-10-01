#!/bin/bash
# The full-ladder gate for EDGE_PROP (the 1/8 propagation made motion-edge aware; gen_variational.py), on this Mac:
# the propagated family is not bit-reproducible under MoltenVK, so each shader runs the whole 42-case ladder THREE
# times and the per-case means are compared (never a single run's hundredth). The control is regenerated and must
# reproduce the committed recommendation byte-for-byte below its banner, or every delta is against the wrong file.
#
#   ./gate.sh [runs]        -> $NP_SCRATCH/limb/gate/run{1..N}/..., gate-table.txt
#
# 2026-09-30: bench.sh now sources tests/mvk-env.sh, whose two MoltenVK switches make a Mac ladder repeat within
# 0.01 dB (TESTING.md, the end), so a single run is a valid gate there, as on Linux: give 1 as [runs]. The three-run
# reasoning above is kept as it was written. probes/limb/gateset.sh is the general form of this gate.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
SH="$TESTS/../shaders"
NP="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
G="$NP/limb/gate"; mkdir -p "$G"
RUNS="${1:-3}"
export FFMPEG="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
cd "$TESTS"
ZERO_SEED=1 "$PY" gen_variational.py "0,0,8,4" 0.3 0.08 "$G/vp.glsl" 0 "0,0,2,0" "$SH/bidirectional-interpolation-propagated.glsl" >/dev/null
EDGE_PROP=1 ZERO_SEED=1 "$PY" gen_variational.py "0,0,8,4" 0.3 0.08 "$G/edgeprop.glsl" 0 "0,0,2,0" "$SH/bidirectional-interpolation-propagated.glsl" >/dev/null
cmp -s "$G/vp.glsl" "$SH/bidirectional-interpolation-variational-propagated.glsl" \
  && echo "control reproduces the committed recommendation" || { echo "CONTROL DIFFERS -- stopping"; exit 1; }
echo "gate start $(date +%T), $RUNS runs, at $(git -C "$TESTS" rev-parse --short HEAD)"
for r in $(seq 1 "$RUNS"); do
  for v in vp edgeprop; do
    t0=$(date +%s)
    OUTROOT="$G/run$r" bash ./bench.sh all "$G/$v.glsl" "$v" </dev/null 2>&1 | grep -iE "FAIL|error" | head -2 | sed "s/^/  [$v run $r] /"
    echo "  run $r $v: $(( $(date +%s) - t0 )) s ($(date +%T))"
  done
  OUTROOT="$G/run$r" "$PY" ./analyze.py --variants > "$G/run$r.txt" 2>&1
done
"$PY" - "$G" "$RUNS" <<'PY' | tee "$G/gate-table.txt"
import re, sys, statistics
G, R = sys.argv[1], int(sys.argv[2])
per = {}
for r in range(1, R + 1):
    for ln in open(f"{G}/run{r}.txt"):
        m = re.match(r"^(\S+)\s+([\d.inf-]+)\s+([\d.inf-]+)\s+\|\s+([\d.inf-]+)\s+([\d.inf-]+)\s*$", ln)
        if m:                         # labels sort as: edgeprop, vp
            c = m.group(1)
            vals = [float(x) if x not in ("-", "inf") else float("nan") for x in m.groups()[1:]]
            per.setdefault(c, []).append(vals)
print(f"{'case':24}{'linear':>8}{'vp':>9}{'edgeprop':>10}{'delta':>8}{'spread vp/ep':>15}")
cap = 40.0
rows = []
for c, runs in sorted(per.items()):
    lin = statistics.mean(v[1] for v in runs)
    ep = [v[2] for v in runs]; vp = [v[3] for v in runs]
    mvp, mep = statistics.mean(vp), statistics.mean(ep)
    rows.append((c, lin, mvp, mep))
    flag = "  <<" if mep - mvp < -0.3 else ("  >>" if mep - mvp > 0.3 else "")
    print(f"{c:24}{lin:8.2f}{mvp:9.2f}{mep:10.2f}{mep - mvp:+8.2f}{max(vp) - min(vp):8.2f}/{max(ep) - min(ep):5.2f}{flag}")
cv = statistics.mean(min(r[2], cap) for r in rows); ce = statistics.mean(min(r[3], cap) for r in rows)
down = [r[0] for r in rows if r[3] - r[2] < -0.3]; up = [r[0] for r in rows if r[3] - r[2] > 0.3]
print(f"\ncases {len(rows)}; capped-at-40 mean: vp {cv:.3f}  edgeprop {ce:.3f}  delta {ce - cv:+.3f}")
print(f"down > 0.3 dB: {len(down)} {down}\nup > 0.3 dB: {len(up)} {up}")
PY
echo "GATE DONE $(date +%T)"
