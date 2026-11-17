#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
root,word,checker=Path(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
r=next(x for x in json.loads((root/'prefix-result.json').read_text()) if x['word']==word)
if r['exact'] and not r['first_bad_from_prior']:
    stem=root/f'w{word}-prefix{r["first_bad"]}'
    os.execv(checker,[checker,str(stem.with_suffix('.cnf')),str(stem.with_suffix('.drat'))])
print('NO_NEW_EXACT_PROOF',word,r['exact'],r['first_bad'])
