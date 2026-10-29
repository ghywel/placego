#!/bin/sh
# Sharp adjacent-return check (Local, L1155, for GPT's GC2138 source). One Lean 4.35 compile against the pipeline kit's
# prebuilt Mathlib, without lake, so nothing is resolved, fetched or rebuilt: LEAN_PATH is the packages' existing build
# directories. The output must be exactly the five axiom reports, with standard axioms only. Invoke as
#   SHARP_LEAN=<toolchain lean> KIT_ROOT=<pipeline kit root> sh check_sharp_adjacent.sh SOURCE
# under run_capped.py --track-tree.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${SHARP_LEAN:?select the installed 4.35 compiler explicitly}"
: "${KIT_ROOT:?the pipeline kit root with prebuilt .lake/packages}"
python3 - "$1" <<'PY'
from pathlib import Path
import hashlib, os, sys
source = Path(sys.argv[1]).read_bytes()
digest = hashlib.sha256(source).hexdigest()
print('SOURCE_SHA256', digest, flush=True)
if digest != '17679e3755d6d8b9fedf8f0f14d6e6dbade1f3367b6e0a10d257a00e998bdfb1':
    raise SystemExit('REFUSED: frozen source digest mismatch')
out = Path(os.environ['CAPPED_OUT']) / 'src'
out.mkdir()
(out / 'SharpAdjacentReturn.lean').write_bytes(source)
PY
path=""
for d in "$KIT_ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] || { echo "FAIL: missing package build $d"; exit 1; }
  path="$path${path:+:}$d"
done
export LEAN_PATH="$path"
"$SHARP_LEAN" --version
"$SHARP_LEAN" -j1 "$CAPPED_OUT/src/SharpAdjacentReturn.lean" > "$CAPPED_OUT/compiler.txt" 2>&1 \
  || { cat "$CAPPED_OUT/compiler.txt"; echo 'FAIL: compile'; exit 1; }
python3 - <<'PY'
from pathlib import Path
import os, re
text = (Path(os.environ['CAPPED_OUT']) / 'compiler.txt').read_text()
print(text, end='')
heads = ['basis_coordinates', 'positive_error_bound', 'sharp_return', 'same_sign_control', 'endpoint_control']
expected = ['SharpAdjacentReturn.' + h for h in heads]
line_re = re.compile(r"^'([\w.]+)' (?:depends on axioms: \[(.*)\]|does not depend on any axioms)$")
seen = []
for line in text.splitlines():
    if not line.strip():
        continue
    m = line_re.fullmatch(line)
    if not m:
        raise SystemExit('FAIL: unexpected compiler output: ' + line)
    axioms = {a.strip() for a in (m.group(2) or '').split(',') if a.strip()}
    if m.group(1) not in expected or not axioms <= {'propext', 'Classical.choice', 'Quot.sound'}:
        raise SystemExit('FAIL: unexpected name or axioms: ' + line)
    seen.append(m.group(1))
if sorted(seen) != sorted(expected):
    raise SystemExit('FAIL: missing or repeated axiom reports')
print('SHARP_ADJACENT_CHECK_PASS', flush=True)
PY
