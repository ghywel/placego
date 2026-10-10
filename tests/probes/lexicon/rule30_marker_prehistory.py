#!/usr/bin/env python3
"""Exact two-tick prehistory conditioned on spatial marker1110.
Missing inference: does the marker itself erase the prehistory obstruction
in GC1009, or must a hidden representation retain an exterior relation?
Record searched: 1110|marker + prehistory|preimage|image.F -> GC608 only
relevant (short-return fifth bit), not this two-tick image.
Prediction: marker1110 alone is NOT sufficient for two-tick prehistory.
Counterfactual: its residual accepts every tail, localizing startup u's
failure entirely to its marker. Controls: literal whole prefix images
through output length10; arbitrary real images cannot be rejected.
Unexpected check: distinguish unconditional remote-tail surjectivity
(GC1006) from this conditioned language. No membership SAT or width scan.
"""
from itertools import product


def f(a,b,c):
    return a ^ (b|c)


def step(row,wall):
    return [f(wall if i==0 else row[i-1],row[i],row[i+1])
            for i in range(len(row)-1)]


def h(a,b,c,d,e):
    return f(f(a,b,c),f(b,c,d),f(c,d,e))


def image_language():
    edges=[]
    for q in range(16):
        a,b,c,d=[(q>>i)&1 for i in (3,2,1,0)]
        out=[set(),set()]
        for e in (0,1):out[h(a,b,c,d,e)].add(((q<<1)&15)|e)
        edges.append(out)
    return edges


def advance(edges,qs,word):
    for b in word:qs=frozenset(r for q in qs for r in edges[q][int(b)])
    return qs


def main():
    edges=image_language()
    root=frozenset(range(4,8)) # Remaining source a3..a6 = 01??.
    todo=[root];seen={root:''}
    for qs in todo:
        for bit in '01':
            nxt=advance(edges,qs,bit)
            if nxt not in seen:
                seen[nxt]=seen[qs]+bit;todo.append(nxt)
    print('reachable subsets',len(todo),'shortest rejected tail',repr(seen.get(frozenset())))
    # Direct independent rule-table control, no use of h or f.
    truth=(0,1,1,1,1,0,0,0)
    def literal_step(row,wall):
        return [truth[4*(wall if i==0 else row[i-1])+2*row[i]+row[i+1]]
                for i in range(len(row)-1)]
    for n in range(4,11):
        actual=set()
        for row in product((0,1),repeat=n+2):
            out=literal_step(literal_step(row,0),1)
            if out[:4]==[1,1,1,0]:actual.add(tuple(out[4:]))
        model={w for w in product((0,1),repeat=n-4) if advance(edges,root,w)}
        assert actual==model,(n,len(actual),len(model))
    # Unconditional bulk two-tick image has full remote-tail projection.
    full=frozenset(range(16))
    assert all(advance(edges,full,b)==full for b in '01')
    assert step(list(map(int,'00101000')),1)==list(map(int,'1110110'))
    assert not advance(edges,root,'110')
    assert advance(edges,root,'0101010')==full
    print('Literal marker-conditioned images through10 and unconditional full-tail control PASS')
    print('shortest universal residual prefix',next((seen[q] for q in todo if q==full),None))
    # Print only shortest rejection; full automaton reproducible from source.

if __name__=='__main__':main()
