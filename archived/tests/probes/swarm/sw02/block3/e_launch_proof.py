#!/usr/bin/env python3
"""Direct exec of checker, so outer stage accounts its full live CPU."""
import json
import os
import sys
from pathlib import Path

root,word,checker=Path(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
result=next(x for x in json.loads((root/'result.json').read_text()) if x['word']==word)
launch=len(sys.argv)>4 and sys.argv[4]=='launch'
if launch:result=result.get('launch_control',{'answer':None})
if result['answer'] is False:
    p=root/(f'w{word}'+('-launch' if launch else ''))
    os.execv(checker,[checker,str(p.with_suffix('.cnf')),str(p.with_suffix('.drat'))])
print('NO_UNSAT_PROOF_REQUIRED',word,result['answer'])
