#!/bin/sh
# dev_compile_on_lib.sh (Local, L1171): one DEVELOPMENT compile of a single draft against an existing development
# library (copied, never modified), on Lean 4.35 with the pipeline kit's prebuilt builds and no lake. Not release
# evidence. Invoke as  SHARP_LEAN=<lean> KIT_ROOT=<kit> DEV_LIB=<lib> sh dev_compile_on_lib.sh SOURCE  under run_capped.py.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"; : "${SHARP_LEAN:?}"; : "${KIT_ROOT:?}"; : "${DEV_LIB:?}"
mkdir "$CAPPED_OUT/src" "$CAPPED_OUT/lib"
cp "$DEV_LIB"/*.olean "$CAPPED_OUT/lib/"
name=$(basename "$1" .lean)
cp "$1" "$CAPPED_OUT/src/$name.lean"
shasum -a 256 "$CAPPED_OUT/src/$name.lean"
lp="$CAPPED_OUT/lib:$KIT_ROOT/equivalents/.lake/build/lib/lean:$KIT_ROOT/lean/.lake/build/lib/lean"
for d in "$KIT_ROOT"/.lake/packages/*/.lake/build/lib/lean; do lp="$lp:$d"; done
export LEAN_PATH="$lp"
"$SHARP_LEAN" --version
if "$SHARP_LEAN" -j1 --root="$CAPPED_OUT/src" -o "$CAPPED_OUT/lib/$name.olean" "$CAPPED_OUT/src/$name.lean"; then
  echo "DEV_OK $name"
else
  rm -f "$CAPPED_OUT/lib/$name.olean"; echo "DEV_FAIL $name"; exit 1
fi
