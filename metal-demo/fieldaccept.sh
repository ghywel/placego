#!/usr/bin/env bash
# P3 acceptance, part 2: the FIELD calibrations, through accelcheck.py --
# the same instrument, the same reference frames and full-scales as the
# ffmpeg-pipeline verification (HANDOFF reference numbers + the M2 run).
# Diag graphs are generated first via:
#   sed TRI_DIAG / *_DIAG_FS on the quad GLSL -> tests/gen_metal.py
# (see the driver in this repo's session notes; dirs under ~/np-work/diag).
#
#   ./fieldaccept.sh
#
# PASSES when the accel/jerk percentages land at the M2 ffmpeg-pipeline
# values (A4 6.6%, A5 2.5%, A6 2.4%, A7 1.8%, O5 5.6% @FS16, O6 0.7%;
# jerk O5 3.6% @FS8, A6 nulls ~-0.03 @FS2) within ~1pp.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$HERE/../tests"
FFMPEG="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}"
DIAG="$HOME/np-work/diag"
W=$HOME/np-work/fieldaccept; mkdir -p "$W"
export PATH="/opt/homebrew/bin:$PATH"
export PYTHONPATH="${PYTHONPATH:-$(echo "$HOME"/np-build/venv/lib/python*/site-packages)}"
. "$TESTS/scenes.sh"

render() { # graphdir case out
  "$FFMPEG" -y -v error -f lavfi -i "$(scene "$2" 24)" \
    -pix_fmt rgb48le -f rawvideo "$W/src.raw"
  ( cd "$HERE" && ./.build/release/QuadDemo --graph "$DIAG/$1" \
      --input "$W/src.raw" --export "$W/$3" --out-fps 24 --size 1280x720 2>/dev/null )
}

ac() { # case raw frame fs [FIELD]
  echo "--- ${5:-accel} $1 f$3 (FS=$4)"
  # JERK_CENTRE=0.5: the Metal host's 4-frame window at N:N is {k-1..k+2}
  # (centre +half an interval from slot 1); the ffmpeg queue sits on the
  # other side. See accelcheck's docstring and QUADDIRECTIONAL.md's
  # CORRECTION section.
  ( cd "$W" && SRC_FPS=24 OUT_FPS=24 FIELD="${5:-accel}" JERK_CENTRE=0.5 \
      python3 "$TESTS/accelcheck.py" "$1" "$2" "$3" "$4" | tail -4 )
}

echo "== acceleration field (metal, N:N) =="
for c in A4_accel_tex_a033 A5_accel_tex_a067 A6_accel_tex_a133 \
         A7_accel_tex_a167 O6_osc_tex_gentle; do
  render gen-accel-fs4 "$c" "acc_$c.raw"
done
render gen-accel-fs16 O5_osc_textured acc_O5.raw
ac A4_accel_tex_a033 acc_A4_accel_tex_a033.raw 9 4.0
ac A5_accel_tex_a067 acc_A5_accel_tex_a067.raw 12 4.0
ac A6_accel_tex_a133 acc_A6_accel_tex_a133.raw 12 4.0
ac A7_accel_tex_a167 acc_A7_accel_tex_a167.raw 12 4.0
ac O6_osc_tex_gentle acc_O6_osc_tex_gentle.raw 4 4.0
ac O5_osc_textured   acc_O5.raw 10 16.0

echo "== jerk field (metal, N:N) =="
render gen-jerk-fs8 O5_osc_textured jerk_O5.raw
render gen-jerk-fs2 A6_accel_tex_a133 jerk_A6.raw
ac O5_osc_textured jerk_O5.raw 10 8.0 jerk
ac A6_accel_tex_a133 jerk_A6.raw 9 2.0 jerk
ac A6_accel_tex_a133 jerk_A6.raw 12 2.0 jerk
