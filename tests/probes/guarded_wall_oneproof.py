#!/usr/bin/env python3
"""GC2400: one original-plus-negated-clause LRAT obligation, fixed phase882/word0."""
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import time

out = Path(os.environ['CAPPED_OUT'])
src = Path(os.environ['GUARDED_EXPORT'])
base = (src/'original.cnf').read_bytes()
assert hashlib.sha256(base).hexdigest() == 'fcb4dd1374cc63643a22caf0f1f1ebdefb124a6114173cb65722387f55861e96'
obs = [json.loads(line) for line in (src/'obligations.jsonl').read_text().splitlines()]
selected = [o for o in obs if (o['phase'],o['word']) == (882,0)]
assert len(selected) == 1
o = selected[0]
assert (o['j'],o['time'],o['depth']) == (2,248,12)
assert o['original_sha256'] == hashlib.sha256(base).hexdigest()
header, body = base.split(b'\n',1)
assert header == b'p cnf 28672 95233'
units = b''.join(('%d 0\n' % u[0]).encode() for u in o['negated_clause_units'])
target = out/'original-plus-negation.cnf'
target.write_bytes(b'p cnf 28672 95242\n'+body+units)
(out/'obligation.json').write_text(json.dumps(o,indent=2)+'\n')
report = {'original_sha256':hashlib.sha256(base).hexdigest(),
          'target_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
          'phase':882,'word':0,'commands':[]}


def limited():
    resource.setrlimit(resource.RLIMIT_CPU,(5,5))


def command(name,args):
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    start=time.monotonic()
    with (out/(name+'.out')).open('wb') as f:
        p=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT,timeout=6,preexec_fn=limited)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    rec={'name':name,'rc':p.returncode,'wall_s':time.monotonic()-start,
         'cpu_s':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime}
    report['commands'].append(rec)
    (out/'proof-receipt.json').write_text(json.dumps(report,indent=2)+'\n')
    return p.returncode,(out/(name+'.out')).read_text()


proof=out/'clause.lrat'
rc,_=command('solve',['/usr/local/bin/cadical','--lrat','--no-binary','-q',str(target),str(proof)])
assert rc == 20, ('not certified UNSAT',rc)
rc,text=command('check',['/usr/local/bin/cake_lpr','--CML_HEAP_SIZE=64','--CML_STACK_SIZE=32',str(target),str(proof)])
assert rc == 0 and 's VERIFIED UNSAT' in text
empty=out/'empty.lrat';empty.write_bytes(b'')
rc,text=command('reject-empty',['/usr/local/bin/cake_lpr','--CML_HEAP_SIZE=64','--CML_STACK_SIZE=32',str(target),str(empty)])
assert 's VERIFIED UNSAT' not in text and rc != 0
report['status']='ONE_CLAUSE_IMPLICATION_LRAT_CHECKED'
report['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
report['proof_bytes']=proof.stat().st_size
(out/'proof-receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
print('GUARDED_ONEPROOF_DONE')
