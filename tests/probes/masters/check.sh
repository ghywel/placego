#!/usr/bin/env bash
# The master tier scored (2026-09-12): every master scene through every shader of the family, on the
# source of truth (ffmpeg + libplacebo, the GLSL) and, when the Metal demo CLI is at hand, on the native
# engine too; hold and linear beside; every output scored against the exact truth with the ladder's own
# reading (analyze.py's parse / mean_interp: frames past the first five, phase-0 frames excluded).
#
#   ./check.sh <outroot> [scenes...]
#     STEMS="a b c"        shader stems (default: every scripts/shaders/*.glsl; the Metal side runs for the
#                          stems that have a graph under $GRAPHS)
#     SRC_FRAMES=96        source frames at 24 fps (the truth is their 60 fps rendering)
#     BG=flat|textured     the ground (flat = black, the demo's default and the instrument; textured = the showing)
#     TEXTURE=sines        the mover's texture
#     QUADDEMO=<cli> GRAPHS=<generated-family dir>   the Metal side (optional)
#     FFMPEG, PYTHON       the tools (a python3 with numpy)
#
# Output, under <outroot>/<bg>/<scene>/: src24.raw, truth60.raw (once), <label>.psnr per run, and
# <outroot>/<bg>/results.tsv  (scene, stem, host, ladder mean, min past 5, frames) -- table.py reads it.
set -u
OUTROOT="$1"; shift
SCENES="${*:-static bounce-constant bounce-oscillating bounce-hardjerk bounce-gravity bounce-masses breathe breathe-spin spin-constant spin-accelerating spin-pendulum roll-12 roll-12-fast roll-wagon}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
SHADERS="$(cd "$TESTS/../shaders" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"; PY="${PYTHON:-python3}"
SRC_FRAMES="${SRC_FRAMES:-96}"; BG="${BG:-flat}"; TEXTURE="${TEXTURE:-sines}"
W=1280; H=720
QUAD="${QUADDEMO:-}"; GRAPHS="${GRAPHS:-}"
if [ -z "${STEMS:-}" ]; then
  STEMS=""
  for g in "$SHADERS"/*.glsl; do
    s="$(basename "$g" .glsl)"; case "$s" in ._*) continue;; esac
    STEMS="$STEMS $s"
  done
fi
OUT="$OUTROOT/$BG"; mkdir -p "$OUT"
TSV="$OUT/results.tsv"; [ -f "$TSV" ] || printf 'scene\tstem\thost\tmean\tmin_past5\tframes\n' > "$TSV"

# <psnr stats> -> "mean min_past5 frames" by the ladder's reading
reading() { "$PY" "$HERE/reading.py" "$1" "$TESTS"; }

score_ffmpeg() {  # <dir> <label> <chain>
  local dir="$1" label="$2" chain="$3" stats="$1/$2.psnr"
  ( cd "$dir" && "$FFMPEG" -y -v error -init_hw_device vulkan=vk -filter_hw_device vk \
      -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 24 -i src24.raw \
      -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 60 -i truth60.raw \
      -filter_complex "[0:v]${chain}[ip];[ip]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]psnr=stats_file=$label.psnr" \
      -f null - ) 2> "$dir/$label.err" || { echo "  $label FAILED: $(head -1 "$dir/$label.err")"; return 1; }
  grep -q "compile status .error" "$dir/$label.err" && { echo "  $label: SHADER COMPILE ERROR"; return 1; }
  return 0
}
score_raw() {  # <dir> <label> <raw at 60>
  local dir="$1" label="$2" raw="$3"
  "$FFMPEG" -y -v error -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 60 -i "$raw" \
            -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 60 -i "$dir/truth60.raw" \
            -lavfi "[0:v]format=yuv420p[a];[1:v]format=yuv420p[b];[a][b]psnr=stats_file=$dir/$label.psnr" -f null - \
            2> "$dir/$label.err" || { echo "  $label: psnr failed"; return 1; }
  return 0
}
record() {  # <scene> <stem> <host> <stats>
  local r; r="$(reading "$4")" || return 1
  printf '%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "${r// /	}" >> "$TSV"      # the reading's three numbers as tab fields
  echo "  $(printf '%-40s %-8s' "$2" "$3") $r"
}
have() { grep -q "^$1	$2	$3	" "$TSV" 2>/dev/null; }

echo "master tier: bg $BG, texture $TEXTURE, $SRC_FRAMES source frames; stems:$STEMS"
for sc in $SCENES; do
  dir="$OUT/$sc"; mkdir -p "$dir"
  echo "== $sc"
  if [ ! -f "$dir/truth60.raw" ]; then
    "$PY" "$TESTS/masters.py" "$sc" --size ${W}x${H} --frames "$SRC_FRAMES" --src-fps 24 --out-fps 60 --settle 0 \
          --bg "$BG" --texture "$TEXTURE" --export-source "$dir/src24.raw" --export-truth "$dir/truth60.raw" > "$dir/export.log" 2>&1 \
      || { echo "  EXPORT FAILED"; tail -2 "$dir/export.log"; continue; }
  fi
  have "$sc" - hold   || { score_ffmpeg "$dir" hold   "format=yuv420p,fps=60" && record "$sc" - hold "$dir/hold.psnr"; }
  have "$sc" - linear || { score_ffmpeg "$dir" linear "format=yuv420p,libplacebo=fps=60:frame_mixer=linear" && record "$sc" - linear "$dir/linear.psnr"; }
  for stem in $STEMS; do
    if ! have "$sc" "$stem" placebo; then
      cp -f "$SHADERS/$stem.glsl" "$dir/_$stem.glsl"
      score_ffmpeg "$dir" "${stem}_placebo" "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_$stem.glsl" \
        && record "$sc" "$stem" placebo "$dir/${stem}_placebo.psnr"
      rm -f "$dir/_$stem.glsl"
    fi
    if [ -n "$QUAD" ] && [ -n "$GRAPHS" ] && [ -f "$GRAPHS/$stem/graph.json" ] && ! have "$sc" "$stem" metal; then
      "$QUAD" --graph "$GRAPHS/$stem" --input "$dir/src24.raw" --src-fps 24 --out-fps 60 --size ${W}x${H} \
              --export "$dir/${stem}_metal.raw" > /dev/null 2> "$dir/${stem}_metal.err" \
        && score_raw "$dir" "${stem}_metal" "$dir/${stem}_metal.raw" && record "$sc" "$stem" metal "$dir/${stem}_metal.psnr" \
        || echo "  ${stem} metal FAILED: $(head -1 "$dir/${stem}_metal.err")"
      rm -f "$dir/${stem}_metal.raw"
    fi
  done
  rm -f "$dir"/._*
done
echo "MASTER TIER DONE -> $TSV"
