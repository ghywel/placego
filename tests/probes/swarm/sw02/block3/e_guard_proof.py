#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
root,t,checker=Path(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
r=next(x for x in json.loads((root/'guard-result.json').read_text())['proofs'] if x['time']==t)
if r['answer'] is False:
    stem=root/f'guard{t}'
    os.execv(checker,[checker,str(stem.with_suffix('.cnf')),str(stem.with_suffix('.drat'))])
print('NO_UNSAT_PROOF',t,r['answer'])
