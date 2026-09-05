#!/bin/bash
# The phase-locked test: render a looping torus with an exactly stationary velocity field, read the
# machine field of its middle turn through the EXACT path, and score the turn's readings as a
# distribution (loopfield.py: the mean, the mode, the hit fraction).
#
#   ./loop.sh <name> [shade=0.25] [turn=80] [tex=m1|broad] [shader=../shaders/quaddirectional-interpolation-propagated.glsl]
#
# Output under $OUTROOT/<name> (default ${TMPDIR:-/tmp}/interp-loop/<name>): src.mkv, truth/, rv4/ (the
# machine frames, 16-bit PNG), loopfield/ (scores as printed, .npy fields, pictures). Set FFMPEG= to the
# patched build (the libplacebo FRAME_MIX hook). Requires a Vulkan device.
#
# A turn of 80 frames takes about two minutes on an RX 6600: ten seconds to render, eighty to read, fifteen
# to score. NFRAME-LIMITS.md, "The phase-locked consensus", has the numbers this reproduces.
set -u
NAME="${1:?name}"; SHADE="${2:-0.25}"; TURN="${3:-80}"; TEX="${4:-m1}"
SHADER="${5:-../shaders/quaddirectional-interpolation-propagated.glsl}"
FFMPEG="${FFMPEG:-ffmpeg}"
OUTROOT="${OUTROOT:-${TMPDIR:-/tmp}/interp-loop}"
HERE="$(cd "$(dirname "$0")" && pwd)"
T="$OUTROOT/$NAME"; mkdir -p "$T/rv4"
N0=$TURN; N1=$((2 * TURN - 1))

echo "== render + truth ($NAME: shade $SHADE, turn $TURN, texture $TEX)"
FFMPEG="$FFMPEG" python3 "$HERE/loop_torus.py" "$T" "$SHADE" "$TURN" "$TEX" | grep -v "^  frame" || exit 1

echo "== the machine field of the middle turn (frames $N0..$N1), read_view 4, format=rgb48le inside the graph"
sed '/^\/\/!PARAM read_view/,/^$/ s/^0$/4/' "$SHADER" > "$T/rv4/c.glsl"
grep -A5 "^//!PARAM read_view" "$T/rv4/c.glsl" | grep -q "^4$" || { echo "read_view patch failed"; exit 1; }
( cd "$T/rv4" && "$FFMPEG" -y -hide_banner -loglevel info -init_hw_device vulkan=vk -filter_hw_device vk -i "$T/src.mkv" \
    -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=c.glsl,select='between(n\,$N0\,$N1)',format=rgb48le" \
    -start_number "$N0" -frames:v "$TURN" "v%03d.png" ) 2>"$T/rv4/err"
echo "   $(ls "$T/rv4"/v*.png 2>/dev/null | wc -l) frames; compile errors $(grep -c 'compile status .error' "$T/rv4/err"), parse errors $(grep -c 'Error parsing' "$T/rv4/err"), hook skips $(grep -c 'hook skipped' "$T/rv4/err")"
[ "$(ls "$T/rv4"/v*.png 2>/dev/null | wc -l)" = "$TURN" ] || { echo "the read produced the wrong number of frames; see $T/rv4/err"; exit 1; }

echo "== the turn as a distribution"
FFMPEG="$FFMPEG" python3 "$HERE/loopfield.py" "$T" "$N0" "$TURN" || exit 1
