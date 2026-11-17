#!/bin/bash
# THE QUALITY TIERS' COSTS on the Vulkan side (2026-10-01; the owner's rule: when several candidates are fit for purpose,
# performance decides, and candidates whose cost is very close collapse into one). Runs on macOS (MoltenVK) and Linux.
# probes/cost/timing.sh's method: an ffv1 FILE source made once (a lavfi or long-GOP source would time the decoder),
# -f null (no encoder), the labels INTERLEAVED over the rounds so drift cancels; linear is the pipeline's floor.
# Each candidate runs at the size it is chosen for: the 1080p files on 1080p sources, the -4k twins on 4K ones.
#
#   tiers.sh <outdir> <clip.mp4>... [ROUNDS=3 FPS=60 SECS=3 SHADERS=<dir> FFMPEG=...]
# The clip's height picks the twin (above 1080: -4k). One GPU job at a time; run alone.
set -u
OUT="${1:?outdir}"; shift; mkdir -p "$OUT"
FF="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"; FP="${FFPROBE:-$(dirname "$FF")/ffprobe}"
ROUNDS="${ROUNDS:-3}"; FPS="${FPS:-60}"; SECS="${SECS:-3}"
SH="${SHADERS:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../shaders" && pwd)}"
VP=bidirectional-interpolation-variational-propagated
LABELS="linear rec carry adopt lattice"
stem() { case "$1" in rec) echo "$VP";; carry) echo "$VP-global-cage-energy-carry";; adopt) echo "$VP-global-cage-energy-carry-adopt";;
                      lattice) echo "$VP-global-cage-energy-carry-adopt-lattice";; esac; }
now() { python3 -c 'import time; print(time.time())'; }
for CLIP in "$@"; do
  name="$(basename "${CLIP%.*}")"; h="$("$FP" -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$CLIP")"
  tw=""; [ "$h" -gt 1080 ] && tw="-4k"
  src="$OUT/src-$name.mkv"
  [ -s "$src" ] || "$FF" -y -hide_banner -loglevel error -i "$CLIP" -t "$SECS" -an -c:v ffv1 -threads 8 "$src" || exit 1
  for L in $LABELS; do
    [ "$L" = linear ] || cp -f "$SH/$(stem "$L")$tw.glsl" "$OUT/$L.glsl"
    : > "$OUT/times-$name-$L.txt"
  done
  echo "########## $name (${h}p, twin '${tw:-none}'): $("$FP" -v error -show_entries format=duration -of csv=p=0 "$src") s, $ROUNDS rounds, 24 -> $FPS"
  for r in $(seq 1 "$ROUNDS"); do
    for L in $LABELS; do
      if [ "$L" = linear ]; then MIX="frame_mixer=linear"; else MIX="frame_mixer=custom_n:custom_shader_path=$L.glsl"; fi
      s=$(now)
      ( cd "$OUT" && "$FF" -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "src-$name.mkv" \
          -vf "format=yuv420p,libplacebo=fps=$FPS:$MIX" -f null - ) 2> "$OUT/err-$L.txt" || { echo "  $L FAILED"; head -3 "$OUT/err-$L.txt"; }
      grep -q "compile status" "$OUT/err-$L.txt" && echo "  $L: A COMPILE ERROR (libplacebo fell back to its own mixer)"
      e=$(now)
      python3 -c "print(f'{$e - $s:.3f}')" >> "$OUT/times-$name-$L.txt"
    done
  done
  dur="$("$FP" -v error -show_entries format=duration -of csv=p=0 "$src")"   # the source's own length (a clip may be shorter)
  python3 - "$OUT" "$name" "$dur" "$FPS" $LABELS <<'PY'
import statistics, sys
out, name, secs, fps = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
n = round(secs * fps)                                    # output frames
med = {L: statistics.median(float(x) for x in open(f"{out}/times-{name}-{L}.txt").read().split()) for L in sys.argv[5:]}
for L, m in med.items():
    extra = "" if L == "linear" else f"   shader {1000 * (m - med['linear']) / n:6.2f} ms over linear"
    rel = "" if L in ("linear", "rec", "carry") else f"   vs the step before {100 * (m / med[{'adopt': 'carry', 'lattice': 'adopt'}[L]] - 1):+5.1f}%"
    print(f"  {L:8s} {1000 * m / n:6.2f} ms per output frame{extra}{rel}")
PY
done
