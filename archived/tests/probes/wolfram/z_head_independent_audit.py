#!/usr/bin/env python3
"""GC1995: independent complete finite audit of D's carrying direction.

Observe the literal word01000010001 at even times0..20 from a right row
beginning000. Its cone has21 cells, so enumerate ALL2^18 remaining bits.
No reset classifier, gap table, Local evaluator, solver or sampling is used.
Expected3072 hits, all beginning000100111. Any exception stops with evidence.
The bounded supervisor provides CAPPED_OUT; this script is frozen before use.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import numpy as np

TABLE = np.array([0, 1, 1, 1, 1, 0, 0, 0], dtype=np.uint8)
TARGET = int('01000010001', 2)
N = 1 << 18
BATCH = 1024


def scalar(row, t):
    return [int(TABLE[4*(t % 2 if i == 0 else row[i-1])+2*row[i]+row[i+1]])
            for i in range(len(row)-1)]


def observation(row):
    row = list(row)
    out = []
    for t in range(len(row)):
        if t % 2 == 0:
            out.append(str(row[0]))
        if len(row) > 1:
            row = scalar(row, t)
    return ''.join(out)


def parents(y, phase):
    found = []
    for c,r in itertools.product((0,1),repeat=2):
        x=[0]*(len(y)+1)
        x[-2:] = [c,r]
        for j in range(len(y)-1,0,-1):
            x[j-1] = y[j] ^ (x[j] | x[j+1])
        if scalar(x,phase)==y:
            found.append(x)
    return found


def main():
    out=Path(os.environ['CAPPED_OUT'])/'artifacts'
    out.mkdir(exist_ok=False)
    rec={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'numpy_version':np.__version__,'width':21,'free_bits':18,'physical_horizon':20,
         'target':'01000010001','checked':0,'matches':0,'exceptions':[],
         'matching_first6_tail_histogram':{},'first_matching_rows':[]}
    # Independent literal characterization of the rule's eight triples.
    ones={(0,0,1),(0,1,0),(0,1,1),(1,0,0)}
    assert all(int(TABLE[4*a+2*b+c])==int((a,b,c) in ones)
               for a,b,c in itertools.product((0,1),repeat=3))
    matching_rows=[]
    for start in range(0,N,BATCH):
        ids=np.arange(start,min(start+BATCH,N),dtype=np.uint32)
        initial=np.zeros((len(ids),21),dtype=np.uint8)
        initial[:,3:]=((ids[:,None]>>np.arange(17,-1,-1,dtype=np.int32))&1).astype(np.uint8)
        row=initial.copy()
        seen=np.zeros(len(ids),dtype=np.uint16)
        for t in range(21):
            if t%2==0:
                seen=(seen<<1)|row[:,0]
            if t<20:
                left=np.empty((len(ids),row.shape[1]-1),dtype=np.uint8)
                left[:,0]=t%2
                left[:,1:]=row[:,:-2]
                row=TABLE[4*left+2*row[:,:-1]+row[:,1:]]
        hits=np.flatnonzero(seen==TARGET)
        rec['checked']+=len(ids)
        for k in hits:
            bits=''.join(map(str,initial[k].tolist()))
            assert observation(initial[k].tolist())==rec['target']
            rec['matches']+=1
            matching_rows.append(bits)
            head=bits[3:9]
            hist=rec['matching_first6_tail_histogram']
            hist[head]=hist.get(head,0)+1
            if len(rec['first_matching_rows'])<4:
                rec['first_matching_rows'].append(bits)
            if head!='100111':
                rec['exceptions'].append(bits)
                (out/'result.json').write_text(json.dumps(rec,indent=2)+'\n')
                raise AssertionError('D carrying implication refuted')
    assert rec['checked']==N and rec['matches']==3072 and not rec['exceptions']
    # Construct an initial z witness, then check it through all22 physical ticks.
    witness=None
    for text in matching_rows:
        y=list(map(int,text))
        for odd in parents(y,1):
            for initial in parents(odd,0):
                if initial[0]==0 and observation(initial)=='001000010001':
                    witness=''.join(map(str,initial))
                    break
            if witness:break
        if witness:break
    assert witness is not None
    rec['z_initial_witness']={'row':witness,'outside_right':'zero',
                              'visible':observation(list(map(int,witness)))}
    rec['passed']=True
    (out/'result.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec),flush=True)

if __name__=='__main__':
    main()
