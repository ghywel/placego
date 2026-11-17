#!/usr/bin/env python3
"""Independent truth-column validation of every one-block physical input.

One bit per assignment of the14 unknown initial cells8..21. No imported
update code, solver, or fresh search; compare the entire retained table.
"""
import argparse
import json
from pathlib import Path


def main():
    p=argparse.ArgumentParser();p.add_argument('--prior',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    records=json.loads(a.prior.read_text())
    count=1<<14;mask=(1<<count)-1
    row=[0]*6+[mask]
    for i in range(14):
        block=1<<i;col=((1<<block)-1)<<block;period=2*block
        while period<count:col|=col<<period;period*=2
        row.append(col)
    inputs=[];heads=[]
    for t in range(15):
        heads.append(row[0])
        if t<14:
            inputs.append(row[7])
            boundary=mask if t&1 else 0
            row=[(boundary if i==0 else row[i-1]) ^ (row[i]|row[i+1])
                 for i in range(len(row)-1)]
    good=mask
    for t in range(2,15,2):good&=heads[t] if t in (2,6) else mask^heads[t]
    def equal(cols,value):
        ok=mask
        for i,col in enumerate(cols):ok&=col if value>>i&1 else mask^col
        return ok
    ends=0
    for end in (32,64,96,56,88,120):ends|=equal(row,end)
    good&=ends
    covered=0;totals={}
    for r in records:
        observed=good & equal(inputs,r['word']) & equal(row,r['end'])
        expected=sum(1<<((root-64)>>7) for root in r['roots'])
        assert observed==expected, (r['word'],r['end'])
        assert not covered&observed
        covered|=observed
        totals[r['word']]=observed.bit_count()
    assert good==covered
    a.out.mkdir(parents=True,exist_ok=True)
    result={'all_initial_assignments':count,'accepted':good.bit_count(),
            'word_classes':len(records),'every_assignment_compared':True,
            'method':'Boolean truth columns independent of integer rows',
            'word_counts':totals}
    (a.out/'column-validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
