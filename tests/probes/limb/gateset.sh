#!/bin/bash
# The full-ladder gate for any set of shaders against a named control, on this Mac: the propagated family is not
# bit-reproducible under MoltenVK, so every shader runs the whole ladder RUNS times and gatetable.py compares the
# per-case means (never a single run's hundredth). gate.sh was EDGE_PROP's own; this is the general form, made to
# gate a switch on top of the player's default (the cage) rather than on the bare recommendation.
#
#   CONTROL=cage TAG=cage-energy ./gateset.sh "cage:<path> cagee:<path> ..." [runs]
#       -> $NP_SCRATCH/limb/gate-<TAG>/run{1..N}/..., run{N}-all.txt, gate-table.txt
#
# Give the shader paths as absolute paths: they are checked from the directory you run in, then used from tests/.
#
# 2026-09-30: bench.sh now sources tests/mvk-env.sh, whose two MoltenVK switches make a Mac ladder repeat within
# 0.01 dB (TESTING.md, the end), so a single run is a valid gate there, as on Linux: give 1 as [runs]. The three-run
# reasoning above is kept as it was written.
#
# Copy the files somewhere nothing regenerates them first: a bench that reads a file being rewritten measures a
# mixture.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
NP="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
G="$NP/limb/gate${TAG:+-$TAG}"; mkdir -p "$G"
RUNS="${2:-3}"; CONTROL="${CONTROL:-vp}"
export FFMPEG="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
read -r -a SET <<< "$1"
for s in "${SET[@]}"; do [ -s "${s#*:}" ] || { echo "missing: ${s#*:}"; exit 1; }; done
case " ${SET[*]} " in *" $CONTROL:"*) ;; *) echo "the control '$CONTROL' is not in the set"; exit 1;; esac
cd "$TESTS"
echo "gate start $(date +%T), $RUNS runs, control $CONTROL, at $(git -C "$TESTS" rev-parse --short HEAD)"
for s in "${SET[@]}"; do echo "  ${s%%:*}  $(shasum -a 256 "${s#*:}" | cut -c1-12)  ${s#*:}"; done
for r in $(seq 1 "$RUNS"); do
  for s in "${SET[@]}"; do
    t0=$(date +%s)
    OUTROOT="$G/run$r" bash ./bench.sh all "${s#*:}" "${s%%:*}" </dev/null 2>&1 | grep -iE "FAIL|error" | head -2 | sed "s/^/  [${s%%:*} run $r] /"
    echo "  run $r ${s%%:*}: $(( $(date +%s) - t0 )) s ($(date +%T))"
  done
  OUTROOT="$G/run$r" "$PY" ./analyze.py --variants > "$G/run$r-all.txt" 2>&1
done
"$PY" "$HERE/gatetable.py" "$G" "$RUNS" -all "$CONTROL" | tee "$G/gate-table.txt"
echo "GATE DONE $(date +%T)"
