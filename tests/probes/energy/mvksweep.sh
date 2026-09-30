#!/usr/bin/env bash
# The MoltenVK settings sweep (TESTING.md, pre-registered 2026-09-30): does one of MoltenVK's own switches take the
# pendulum's random speed dropouts to zero? Runs pendulumfit.py RUNS times per setting and prints the dropout count of
# each run. macOS only (MoltenVK); the Arc under Linux has none to remove.
#
#   mvksweep.sh <pendulum.json> <frames dir> [runs=4] [setting names...]   (default: all)
#     FFMPEG (the research build), PYTHON (a python3 with numpy), VK_ICD_FILENAMES (MoltenVK's ICD)
set -u
J="$1"; D="$2"; RUNS="${3:-4}"; shift 3 2>/dev/null; ONLY=" $* "
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${PYTHON:-python3}"
SETTINGS=(
  "default:"
  "sync-submits:MVK_CONFIG_SYNCHRONOUS_QUEUE_SUBMITS=1"
  "heap-off:MVK_CONFIG_USE_MTLHEAP=0"
  "heap-on:MVK_CONFIG_USE_MTLHEAP=1"
  "fastmath-off:MVK_CONFIG_FAST_MATH_ENABLED=0"
  "argbuf-off:MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS=0"
  "argbuf-fastmath-off:MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS=0 MVK_CONFIG_FAST_MATH_ENABLED=0"
  "prefill:MVK_CONFIG_PREFILL_METAL_COMMAND_BUFFERS=1"
  "one-cmdbuf:MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE=1"
  "no-pooling:MVK_CONFIG_USE_COMMAND_POOLING=0"
  "no-concurrent-compile:MVK_CONFIG_SHOULD_MAXIMIZE_CONCURRENT_COMPILATION=0"
)
echo "== $(date +%T) MoltenVK sweep, $RUNS runs per setting, on $(system_profiler SPDisplaysDataType 2>/dev/null | awk -F': ' '/Chipset Model/ {print $2; exit}')"
for s in "${SETTINGS[@]}"; do
  name="${s%%:*}"; envs="${s#*:}"
  [ "$ONLY" = "  " ] || [[ "$ONLY" == *" $name "* ]] || continue
  counts=""
  for r in $(seq 1 "$RUNS"); do
    n=$(env MVK_DETERMINISTIC=0 $envs "$PY" "$HERE/pendulumfit.py" "$J" "$D" 2>&1 | sed -n 's/.*speed DROPOUTS[^:]*: \([0-9]*\) of.*/\1/p')
    counts="$counts ${n:-ERR}"
  done
  printf '  %-14s %-44s dropouts per run:%s\n' "$name" "${envs:-(none)}" "$counts"
done
echo "== $(date +%T) done"
