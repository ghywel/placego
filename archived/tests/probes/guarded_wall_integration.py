#!/usr/bin/env python3
"""GC2399: fixed D13/k0 exporter integration, single process, no SAT solver."""
import hashlib
import json
import os
from pathlib import Path
import runpy
import sys

here = Path(__file__).resolve().parent
out = Path(os.environ['CAPPED_OUT'])
states_path = Path(os.environ['GUARDED_STATES'])
saved = sys.argv[:]
sys.argv = ['guarded_wall_export.py','--states',str(states_path),'--out',str(out/'export'),'--D','13','--k','0']
try:
    runpy.run_path(str(here/'guarded_wall_export.py'),run_name='__main__')
finally:
    sys.argv = saved
dest = out/'export'
receipt = json.loads((dest/'receipt.json').read_text())
raw = (dest/'original.cnf').read_bytes()
assert hashlib.sha256(raw).hexdigest() == receipt['base']['sha256']
lines = raw.decode().splitlines()
assert lines[0] == 'p cnf 28672 95233'
assert len(lines)-1 == 95233
for line in lines[1:]:
    lits = list(map(int,line.split()))
    assert lits[-1] == 0 and all(1 <= abs(v) <= 28672 for v in lits[:-1])
states = {(int(c),int(w,2)) for line in states_path.read_text().splitlines()
          if line and not line.startswith('#') for c,w in [line.split()]}
obligations = [json.loads(line) for line in (dest/'obligations.jsonl').read_text().splitlines()]
assert len(obligations) == 389
assert {(o['phase'],o['word']) for o in obligations} == states
for o in obligations:
    assert (o['j'],o['depth'],o['contradiction_horizon']) == (2,12,3)
    assert (o['time']-390) % 1024 == o['phase']
    assert o['original_sha256'] == receipt['base']['sha256']
    assert o['negated_clause_units'] == [[-lit] for lit in o['clause']]
    assert len(o['clause']) == 9
    assignment = {abs(unit[0]): unit[0] > 0 for unit in o['negated_clause_units']}
    assert len(assignment) == 9
    assert not any(assignment[abs(lit)] == (lit > 0) for lit in o['clause'])
summary = {'status':'INTEGRATION_CHECKED_NOT_CLAUSE_CERTIFIED',
           'base_sha256':receipt['base']['sha256'],'variables':28672,
           'original_clauses':95233,'obligations':389,
           'solver_calls':0,'source_claim':'unmodified upward_rigid.cnf generator'}
(out/'integration.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print('GUARDED_INTEGRATION_DONE')
