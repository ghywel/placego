#!/usr/bin/env python3
"""scar.py (Local, L1534): GPT's quotient for the three closed sets. Each window is cut into its strip (cells that do not vary in its phase) and its scar (the low cells that do). Per phase: scar states, the number of different responses to the four lower states, and where the four states merge."""
import json
from reachlib import *
from clos import nxt
def nat(s): return sum(1<<i for i,c in enumerate(s) if c=='#')
def merge(s):
    T=set(STATES)
    for i,ch in enumerate(s):
        c=1 if ch=='#' else 0
        T={(c^(p1|p2),p1) for p1,p2 in T}
        if len(T)==1: return i
    return None
def run(name,groups):
    w=len(groups[0][0])
    print(name,'width',w)
    for p,ws in enumerate(groups):
        hi=max(i for i in range(w) if len({x[i] for x in ws})>1)
        outs=sorted({len({nxt(nat(s),w,q) for q in STATES}) for s in ws})
        ms=sorted({merge(s) for s in ws})
        print(f'  phase {p}: scar states {len(ws)}, scar cells {hi+1}, offset of the highest {w-1-hi}, responses {outs}, merge index {ms[0]} to {ms[-1]}')
s45=[''.join('#' if b else '.' for b in v) for v in json.load(open('lock45.json'))]
run('AB lock',[[s45[0],s45[2]],[s45[1],s45[3]]])
s136=json.load(open('lock136.json'))
run('AAB lock',[[s136[4],s136[5]],[s136[2],s136[3]],[s136[0],s136[1]]])
d=json.load(open('lock175.json'))
run('third lock',[d[str(i)] for i in range(6)])
