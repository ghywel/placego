#!/bin/bash
# What each offered shader COSTS, measured the way this project learned to measure it (2026-09-08, for the
# M-series drop-down: the owner should see that six frames is not free).
#
# The method, from the record: a lavfi source is up to 70% of a naive "shader time", so the source is an ffv1
# FILE rendered once; the output goes to -f null so no encoder is timed; and the shaders are INTERLEAVED over
# three rounds so thermal drift and driver warm-up cancel rather than accumulate onto whichever ran last.
# 720p, 24 -> 60, the ladder's O5_osc_textured (the field-calibration scene), 120 output frames.
# One GPU job at a time; run alone.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/metal-prep/timing"; mkdir -p "$G"
. "$SC/tests/scenes.sh"
SRC="$G/src.mkv"; SRCREL=src.mkv
if [ ! -s "$SRC" ]; then
  S="$(scene O5_osc_textured 24)"; S="${S//:d=1,/:d=3,}"
  ffmpeg.exe -y -hide_banner -loglevel error -f lavfi -i "$S" -c:v ffv1 "$SRC" || exit 1
fi
echo "########## TIMING start $(date +%T)  source $(stat -c %s "$SRC") bytes"
LABELS=(linear base2 prop2 vp2 tri quad quadp quint sext)
FILES=("" bidirectional-interpolation.glsl bidirectional-interpolation-propagated.glsl \
       bidirectional-interpolation-variational-propagated.glsl tridirectional-interpolation-propagated.glsl \
       quaddirectional-interpolation.glsl quaddirectional-interpolation-propagated.glsl \
       quintdirectional-interpolation-propagated.glsl sextdirectional-interpolation-propagated.glsl)
: > "$G/raw.txt"
for round in 1 2 3; do
  for i in "${!LABELS[@]}"; do
    lab=${LABELS[$i]}; f=${FILES[$i]}
    # A path inside a filter argument does not survive MSYS2 -> native ffmpeg.exe (the colon in "E:" is
    # ffmpeg's own option separator). bench.sh's remedy is the only one that works: copy the shader next to
    # the output and name it bare, running from there. Copying is outside the timed region.
    if [ -z "$f" ]; then VF="libplacebo=fps=60:frame_mixer=linear"
    else cp -f "$SC/shaders/$f" "$G/_shader.glsl"; VF="libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_shader.glsl"; fi
    t0=$(date +%s%3N)
    ( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk \
      -i "$SRCREL" -vf "$VF" -frames:v 120 -f null - ) 2>"$G/err_$lab" || { echo "  $lab FAILED"; head -2 "$G/err_$lab"; continue; }
    t1=$(date +%s%3N)
    echo "$lab $(( t1 - t0 ))" >> "$G/raw.txt"   # milliseconds; bc is not installed here
  done
  echo "  round $round done ($(date +%T))"
done
python - "$G/raw.txt" <<'PY'
import statistics, sys, collections
d = collections.defaultdict(list)
for line in open(sys.argv[1]):
    k, v = line.split(); d[k].append(float(v) / 1000.0)
base = statistics.median(d["linear"]) if "linear" in d else None
print(f"\n{'shader':8s} {'median s':>9} {'per frame ms':>13} {'x linear':>9}  (120 output frames, 720p, 24->60, ffv1 source, -f null)")
for k in ("linear", "base2", "prop2", "vp2", "tri", "quad", "quadp", "quint", "sext"):
    if k not in d: continue
    m = statistics.median(d[k])
    print(f"{k:8s} {m:9.2f} {m / 120 * 1000:13.1f} {m / base:9.2f}")
PY
echo "TIMING DONE $(date +%T)"
