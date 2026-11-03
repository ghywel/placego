#!/bin/sh
# Ether-zero full check (Local, L1346, NIGHT-TASKS A1): the catalog module EtherEdgeZero.lean and its portal form, each
# compiled in isolation and checked by the kit's unchanged Check.lean with four headlines (L1351), as check_ether_episode.sh does.
# Core imports only. Invoke from the lean/ directory of a kit at the verifier's commit, through
# `lake env sh check_ether_episode.sh CATALOG SUBMISSION CHECKER`, under run_capped.py --track-tree.
# The verifier's image 15 is kit 93d98bbe; Rule30Ether and its closure there are byte-identical to kit main c42f6e5.
# Neither source prints, so both compiler outputs must be empty. Invoke from the lean/ directory of a kit at 93d98bbe.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" "$2" "$3" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
pins = [('catalog', sys.argv[1], '4787092702a8744f3376c0fa074991f641df98fd3cf3ab7885536e508fd53773'),
        ('submission', sys.argv[2], '4a2688b0c03fd1274aa0a2381f98b5405f7fb42ab0a1bde1c1472bcf6db07018'),
        ('checker', sys.argv[3], 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905')]
data = {}
for name, path, expected in pins:
    data[name] = Path(path).read_bytes()
    digest = hashlib.sha256(data[name]).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
# The catalog module compiles under the root EtherZeroCert, so no output Ruliology/ shadows the kit's package.
(out / 'c' / 'src' / 'EtherZeroCert').mkdir(parents=True)
(out / 'c' / 'lib' / 'EtherZeroCert').mkdir(parents=True)
(out / 'c' / 'src' / 'EtherZeroCert' / 'EtherEdgeZero.lean').write_bytes(data['catalog'])
(out / 's' / 'src').mkdir(parents=True)
(out / 's' / 'lib').mkdir(parents=True)
(out / 's' / 'src' / 'Rule30Submission.lean').write_bytes(data['submission'])
(out / 'Check.lean').write_bytes(data['checker'])
PY
heads="edge_pinned edge_pinned_tail trap_two_sided wall_ne_ref_all"
base_path="$LEAN_PATH"
for part in c s; do
  if [ "$part" = c ]; then
    mod=EtherZeroCert.EtherEdgeZero; file=EtherZeroCert/EtherEdgeZero; prefix=Ruliology.CellularAutomata.EtherEdgeZero
  else
    mod=Rule30Submission; file=Rule30Submission; prefix=Rule30Submission
  fi
  export LEAN_PATH="$CAPPED_OUT/$part/lib:$base_path"
  lean -j1 --root="$CAPPED_OUT/$part/src" -o "$CAPPED_OUT/$part/lib/$file.olean" "$CAPPED_OUT/$part/src/$file.lean" \
    > "$CAPPED_OUT/$part-compile.txt" 2>&1
  args=""
  for h in $heads; do args="$args --headline $prefix.$h"; done
  lean -j1 --root="$CAPPED_OUT" --run "$CAPPED_OUT/Check.lean" $mod --claim partial $args > "$CAPPED_OUT/$part-check.json"
  python3 - "$part" "$mod" "$prefix" "$heads" <<'PY'
from pathlib import Path
import hashlib, json, os, sys
part, mod, prefix, heads = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split()
out = Path(os.environ['CAPPED_OUT'])
compile_bytes = (out / (part + '-compile.txt')).read_bytes()
if compile_bytes.strip():
    print(compile_bytes.decode('utf-8', 'replace'))
    raise SystemExit('FAIL: compiler output for ' + part)
raw = (out / (part + '-check.json')).read_text()
print(raw, end='')
lines = [line for line in raw.splitlines() if line.startswith('{')]
if len(lines) != 1:
    raise SystemExit('FAIL: expected exactly one checker JSON line for ' + part)
r = json.loads(lines[0])
expected = {prefix + '.' + h for h in heads}
got = r.get('headlines', [])
if r.get('module') != mod or r.get('verdict') != 'pass' or r.get('replay', {}).get('ok') is not True:
    raise SystemExit('FAIL: module/verdict/replay for ' + part)
if r.get('importsStatements') is not True or r.get('newAxioms'):
    raise SystemExit('FAIL: official import/new axiom guard for ' + part)
if {h.get('name') for h in got} != expected or len(got) != len(expected) or any(h.get('ok') is not True for h in got):
    raise SystemExit('FAIL: exact headline outcomes for ' + part)
if any(d.get('standardAxioms') is not True for d in r.get('declared', [])):
    raise SystemExit('FAIL: nonstandard declared constant for ' + part)
print('PART_PASS', part, flush=True)
PY
done
echo ETHER_ZERO_CHECK_PASS
