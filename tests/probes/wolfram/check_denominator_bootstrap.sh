#!/bin/sh
# One core-only check of the finite-deadline component. Run under run_capped.py.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
: "${HORIZON_LEAN:?select the already installed compiler explicitly}"
python3 - "$1" <<'PY'
import hashlib, os, sys
from pathlib import Path
source=Path(sys.argv[1]).read_bytes()
expected='c9c8cbe4b3eb9b46cb7f87e32c26668c6a4245bd82a1a7d5a2ef6e2c4d4ae729'
actual=hashlib.sha256(source).hexdigest()
if actual != expected:
    raise SystemExit('REFUSED: source digest '+actual)
out=Path(os.environ['CAPPED_OUT'])/'src'
out.mkdir()
(out/'DenominatorBootstrap.lean').write_bytes(source)
print('SOURCE_SHA256',actual,flush=True)
PY
"$HORIZON_LEAN" --version
"$HORIZON_LEAN" -j1 --root="$CAPPED_OUT/src" "$CAPPED_OUT/src/DenominatorBootstrap.lean" \
  > "$CAPPED_OUT/compiler.txt" 2>&1 || { cat "$CAPPED_OUT/compiler.txt"; exit 1; }
python3 - <<'PY'
import os, re
from pathlib import Path
out=Path(os.environ['CAPPED_OUT'])
text=(out/'compiler.txt').read_text()
print(text,end='')
heads=['four_steps','final_deadline','final_visit_contradiction']
expected={'DenominatorBootstrap.'+h for h in heads}
pattern=re.compile(r"^'([\w.]+)' (?:depends on axioms: \[(.*)\]|does not depend on any axioms)$")
seen=[]
for line in text.splitlines():
    if not line.strip(): continue
    match=pattern.fullmatch(line)
    if not match: raise SystemExit('FAIL: unexpected compiler output')
    name=match.group(1)
    axes={v.strip() for v in (match.group(2) or '').split(',') if v.strip()}
    if name not in expected or not axes <= {'propext','Classical.choice','Quot.sound'}:
        raise SystemExit('FAIL: unexpected name/axioms')
    seen.append(name)
if len(seen)!=len(expected) or set(seen)!=expected:
    raise SystemExit('FAIL: missing or duplicated theorem axiom reports')
print('DENOMINATOR_BOOTSTRAP_PASS')
PY
