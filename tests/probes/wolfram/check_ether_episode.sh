#!/bin/sh
# M(k) full check (Local, L1267): the catalog module and the portal form of Rule30EtherEpisode, each compiled in isolation
# and checked by the kit's unchanged Check.lean with five headlines, as check_ring_orbits.sh (L1131) does for Lemma R.
# Core imports only. Invoke from the lean/ directory of a kit at the verifier's commit, through
# `lake env sh check_ether_episode.sh CATALOG SUBMISSION CHECKER`, under run_capped.py --track-tree.
# The catalog form carries seven `#print axioms` lines, so its compiler output must equal the reviewed printout
# (out.txt 46d74cbb..., L1262/L1266); the portal form has none, so its output must be empty.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 - "$1" "$2" "$3" <<'PY'
from pathlib import Path
import hashlib, os, sys
out = Path(os.environ['CAPPED_OUT'])
pins = [('catalog', sys.argv[1], '2ea831a9de66fefc63e621a218f49e53ed4230f41a15577bfa8e4b01c3c95c22'),
        ('submission', sys.argv[2], '37733e44c5febb72abb0fd214a9839ca564f4f7ce55a4cbe566d42ee18cb584e'),
        ('checker', sys.argv[3], 'b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905')]
data = {}
for name, path, expected in pins:
    data[name] = Path(path).read_bytes()
    digest = hashlib.sha256(data[name]).hexdigest()
    print(name, 'sha256', digest, flush=True)
    if digest != expected:
        raise SystemExit('REFUSED: frozen ' + name + ' digest mismatch')
# The catalog module compiles under the root EtherEpisodeCert, so no output Ruliology/ shadows the kit's package.
(out / 'c' / 'src' / 'EtherEpisodeCert').mkdir(parents=True)
(out / 'c' / 'lib' / 'EtherEpisodeCert').mkdir(parents=True)
(out / 'c' / 'src' / 'EtherEpisodeCert' / 'Rule30EtherEpisode.lean').write_bytes(data['catalog'])
(out / 's' / 'src').mkdir(parents=True)
(out / 's' / 'lib').mkdir(parents=True)
(out / 's' / 'src' / 'Rule30Submission.lean').write_bytes(data['submission'])
(out / 'Check.lean').write_bytes(data['checker'])
PY
heads="episode_max episode_bound wit_episode episode_witness_finite witness_unique"
base_path="$LEAN_PATH"
for part in c s; do
  if [ "$part" = c ]; then
    mod=EtherEpisodeCert.Rule30EtherEpisode; file=EtherEpisodeCert/Rule30EtherEpisode; prefix=Ruliology.CellularAutomata.Rule30EtherEpisode
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
if part == 'c':
    digest = hashlib.sha256(compile_bytes).hexdigest()
    if digest != '46d74cbb446a32dd584adb9ed707422c6d60470c5594bc8ee4e3ca20612dd35c':
        print(compile_bytes.decode('utf-8', 'replace'))
        raise SystemExit('FAIL: catalog compiler output is not the reviewed axiom printout (' + digest + ')')
elif compile_bytes.strip():
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
echo ETHER_EPISODE_CHECK_PASS
