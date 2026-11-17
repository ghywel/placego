#!/usr/bin/env python3
"""GC408: audit a prospective toolkit threshold application to RR's event.
Before run: the event is not increasing in initially black free cells, even
with wall phase0 and target white cell fixed. Eight assignments for d2,L1.
Control scalar XOR-OR vs literal Rule30 truth table. Unexpected check: added
black bit cannot be the initial wall bit or prescribed white cell.
Trusted imported175c needs an increasing family; no recheck of that theorem.
OUTCOME: eight controls PASS. Membership is neither increasing nor decreasing:
01000 has wall trace010, adding black at+1 gives01010 with trace000;
00000 fails, adding black at-1 gives01000 and passes. Targets/wall0 fixed.
Finite SAT is not an infinite-wall extension; no RR solver duplication.
"""
import itertools,json
TABLE={(l,c,r):(30 >> ((l<<2)|(c<<1)|r))&1
       for l,c,r in itertools.product((0,1),repeat=3)}


def trace(bits,literal=False):
    row=list(bits);out=[row[2]]
    for t in range(2):
        row=[TABLE[tuple(row[i-1:i+2])] if literal else row[i-1]^(row[i]|row[i+1])
             for i in range(1,len(row)-1)]
        out.append(row[1-t])
    return out


def main():
    event={};rows={}
    for a,b,c in itertools.product((0,1),repeat=3):
        row=[0,a,0,b,c]
        tr=trace(row);assert tr==trace(row,True)
        event[(a,b,c)]=tr==[0,1,0];rows[(a,b,c)]=row
    down=[];up=[]
    for key,ok in event.items():
        for i in range(3):
            if key[i]:continue
            larger=list(key);larger[i]=1;larger=tuple(larger)
            if ok and not event[larger]:down.append((key,larger))
            if not ok and event[larger]:up.append((key,larger))
    assert down and up
    print(json.dumps({'free_assignments':8,'scalar_truth_table':'PASS',
        'increasing':not bool(down),'decreasing':not bool(up),
        'true_then_false_rows':[rows[k] for k in down[0]],
        'true_then_false_traces':[trace(rows[k]) for k in down[0]],
        'false_then_true_rows':[rows[k] for k in up[0]]},indent=2))


if __name__=='__main__':main()
