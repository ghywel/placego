#!/usr/bin/env bash
# The field tier (2026-09-12, SCENES-PLAN S4): the machine-read VELOCITY of the master scenes against the
# closed-form chord masters.py exports, on both hosts, through the instrument the record's field
# acceptance was calibrated on -- the picture path's own diagnostic (TRI_DIAG 7, full resolution, its
# full scale set here), built as fielddiag.py builds it. Rendered at exact N:N (24 -> 24), as fielddiag
# renders: the diagnostic is anchored per phase, and only at phase zero does its field sit on the source
# frame's own pixels (measured 2026-09-12: at 24 -> 60 the constant bounce read 0 in the mover's mask at
# every interior phase and 19.12 against a 19.20 chord at N:N; libplacebo runs the hook at N:N too, but
# for the boundary frames). Output frame k is read against truth_k, the chord from source frame k to
# k + 1; fieldcheck.py scores it and says if a neighbouring truth frame fits better.
#
#   ./fieldtier.sh <outroot> [scenes...]
#     STEM=quaddirectional-interpolation-propagated   FS=48 (px/interval full scale; the fast wheel's rim
#     reaches 38)   FRAMES="12 48 84"   N=96   BG=flat   FFMPEG PYTHON QUADDEMO (the Metal side; optional)
set -u
OUT="$1"; shift
SCENES="${*:-bounce-constant bounce-gravity breathe spin-constant spin-pendulum roll-12 roll-wagon}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
SHADERS="$(cd "$TESTS/../shaders" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"; PY="${PYTHON:-python3}"; QUAD="${QUADDEMO:-}"
export FFMPEG FFPROBE="${FFPROBE:-$(dirname "$FFMPEG")/ffprobe}"     # fieldcheck.py reads frames through them
STEM="${STEM:-quaddirectional-interpolation-propagated}"; FS="${FS:-48}"; FRAMES="${FRAMES:-12 48 84}"; N="${N:-96}"; BG="${BG:-flat}"
W=1280; H=720
mkdir -p "$OUT/graphs"
VAR="$OUT/graphs/${STEM}_vel_fs$FS"
[ -f "$VAR.glsl" ] || "$PY" "$HERE/diagvariant.py" "$SHADERS/$STEM.glsl" 7 VEL_DIAG_FS "$FS" "$VAR.glsl" || exit 1
if [ -n "$QUAD" ] && [ ! -f "$VAR/graph.json" ]; then
  PATH="/opt/homebrew/bin:$PATH" "$PY" "$TESTS/gen_metal.py" "$VAR.glsl" "$VAR" --compile > "$VAR.gen.log" 2>&1 \
    || { echo "graph build failed: $(tail -2 "$VAR.gen.log")"; exit 1; }
fi
TSV="$OUT/field.tsv"; [ -f "$TSV" ] || printf 'scene\thost\tk\tmedian_px\tp90_px\tgross_pct\tangle_deg\tv_true\tv_meas\tnote\n' > "$TSV"
echo "field tier: $STEM TRI_DIAG 7 at FS $FS, $BG ground, frames $FRAMES of $N"
for sc in $SCENES; do
  dir="$OUT/$sc"; mkdir -p "$dir"
  echo "== $sc"
  [ -f "$dir/src24.raw" ] || "$PY" "$TESTS/masters.py" "$sc" --size ${W}x${H} --frames "$N" --src-fps 24 --settle 0 --bg "$BG" \
      --export-source "$dir/src24.raw" --export-field "$dir/truth" > "$dir/export.log" 2>&1 || { echo "  export failed"; continue; }
  hosts=""
  if [ -n "$QUAD" ] && [ ! -f "$dir/metal.done" ]; then
    "$QUAD" --graph "$VAR" --param read_view=0 --input "$dir/src24.raw" --src-fps 24 --out-fps 24 --size ${W}x${H} \
            --export "$dir/metal.raw" > /dev/null 2> "$dir/metal.err" && touch "$dir/metal.done" || echo "  metal render failed: $(head -1 "$dir/metal.err")"
  fi
  if [ ! -f "$dir/placebo.done" ]; then
    "$FFMPEG" -y -v error -init_hw_device vulkan=vk -filter_hw_device vk -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -r 24 -i "$dir/src24.raw" \
      -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=$VAR.glsl,format=rgb48le" -f rawvideo "$dir/placebo.raw" \
      2> "$dir/placebo.err" && touch "$dir/placebo.done" || echo "  placebo render failed: $(head -1 "$dir/placebo.err")"
  fi
  for host in metal placebo; do
    for k in $FRAMES; do
      j=$k
      if [ ! -f "$dir/${host}_$k.png" ]; then
        [ -f "$dir/$host.raw" ] || continue
        "$FFMPEG" -y -v error -f rawvideo -pix_fmt rgb48le -s ${W}x${H} -i "$dir/$host.raw" -vf "select=eq(n\,$j)" -frames:v 1 -pix_fmt rgb48be "$dir/${host}_$k.png" 2>/dev/null || continue
      fi
      line="$("$PY" "$TESTS/fieldcheck.py" "$dir/${host}_$k.png" "$dir/truth" "$k" "$FS" 2>&1)"
      row="$(printf '%s\n' "$line" | grep "vs truth *$k:" | head -1)"
      note="$(printf '%s\n' "$line" | grep -E "NOTE|BROKEN" | head -1)"
      if [ -n "$row" ]; then
        med=$(printf '%s' "$row" | sed -E 's/.*median ([0-9.]+) px.*/\1/'); p90=$(printf '%s' "$row" | sed -E 's/.*p90 ([0-9.]+).*/\1/')
        gross=$(printf '%s' "$row" | sed -E 's/.*gross\(>2px\) *([0-9.]+)%.*/\1/'); ang=$(printf '%s' "$row" | sed -E 's/.*angle *([0-9.]+|nan) deg.*/\1/')
        vt=$(printf '%s' "$row" | sed -E 's/.*\|v\| true ([0-9.]+).*/\1/'); vm=$(printf '%s' "$row" | sed -E 's/.*meas ([0-9.]+).*/\1/')
        printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$sc" "$host" "$k" "$med" "$p90" "$gross" "$ang" "$vt" "$vm" "$note" >> "$TSV"
        echo "  $(printf '%-8s k=%-3s' "$host" "$k") median $med px  p90 $p90  gross $gross%  angle $ang deg  |v| true $vt meas $vm ${note:+ -- $note}"
      else
        echo "  $host k=$k: no reading -- $(printf '%s\n' "$line" | tail -1)"
      fi
    done
    rm -f "$dir/$host.raw"
  done
  rm -f "$dir"/._*
done
echo "FIELD TIER DONE -> $TSV"
