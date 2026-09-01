#!/usr/bin/env bash
# Regenerate generated*/ from the GLSL source of truth. Run after ANY edit
# to the quad shader (or its base + generator chain). Everything emitted
# here is generated material -- never hand-edited (METALPORT.md).
#
# Three graphs: the production shader, and the two field-overlay diag
# builds the demo UI exposes (TRI_DIAG=2 acceleration at FS=4, TRI_DIAG=5
# jerk at FS=8 -- the FS values the field verification used).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PATH="/opt/homebrew/bin:$PATH"
SRC="$HERE/../quaddirectional-interpolation.glsl"
GEN="$HERE/../tests/gen_metal.py"

python3 "$GEN" "$SRC" "$HERE/generated" --compile

TMP="$(mktemp -d)"
sed -e "s/const int TRI_DIAG = 0;/const int TRI_DIAG = 2;/" \
    -e "s/const float ACCEL_DIAG_FS = 2.0;/const float ACCEL_DIAG_FS = 4.0;/" \
    "$SRC" > "$TMP/accel.glsl"
python3 "$GEN" "$TMP/accel.glsl" "$HERE/generated-accel" --compile
sed -e "s/const int TRI_DIAG = 0;/const int TRI_DIAG = 5;/" \
    -e "s/const float JERK_DIAG_FS  = 2.0;/const float JERK_DIAG_FS  = 8.0;/" \
    "$SRC" > "$TMP/jerk.glsl"
python3 "$GEN" "$TMP/jerk.glsl" "$HERE/generated-jerk" --compile
rm -rf "$TMP"
