#!/usr/bin/env python3
"""Exact two-tick prehistory conditioned on spatial marker1110.
Construction already in G236 / rule30_gpt_entry_image.py; this extends
its first-missing-prefix search to all residuals.
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
    # Complete proper-residual structure; registered in RULE30-GPT before this run.
    proper=set(todo)-{frozenset(),full}
    graph={q:[advance(edges,q,b) for b in '01' if advance(edges,q,b) in proper]
           for q in proper}
    rev={q:[] for q in proper}
    for q,rs in graph.items():
        for r in rs:rev[r].append(q)
    reached=set();order=[]
    def dfs(q):
        reached.add(q)
        for r in graph[q]:
            if r not in reached:dfs(r)
        order.append(q)
    for q in proper:
        if q not in reached:dfs(q)
    reached=set();comps=[]
    for q in reversed(order):
        if q in reached:continue
        comp={q};queue=[q];reached.add(q)
        for r in queue:
            for t in rev[r]:
                if t not in reached:reached.add(t);comp.add(t);queue.append(t)
        comps.append(comp)
    def reach(q):
        found={q};queue=[q]
        for r in queue:
            for t in graph[r]:
                if t not in found:found.add(t);queue.append(t)
        return found
    closure={q:reach(q) for q in proper}
    for comp in comps:
        for q in comp:
            assert comp=={r for r in proper if r in closure[q] and q in closure[r]}
    recurrent=[c for c in comps if len(c)>1 or next(iter(c)) in graph[next(iter(c))]]
    print('Proper recurrent SCCs (size, internal branching):',
          sorted((len(c),sum(sum(r in c for r in graph[q])>1 for q in c)) for c in recurrent))
    for q in todo:
        for b in '01':
            assert advance(edges,full-q,b)==full-advance(edges,q,b)
    print('Independent mutual reachability and complement controls PASS')
    for comp in recurrent:
        for q in sorted(comp,key=lambda q:(len(seen[q]),seen[q])):
            if sum(r in comp for r in graph[q])<2:continue
            def path(start,end):
                visit={start};queue=[(start,'')]
                for r,w in queue:
                    if r==end:return w
                    for b in '01':
                        t=advance(edges,r,b)
                        if t in comp and t not in visit:visit.add(t);queue.append((t,w+b))
                raise AssertionError('SCC path missing')
            loops=[b+path(advance(edges,q,b),q) for b in '01']
            print('Branching witness: entry',seen[q],'source states',sorted(q),'loops',loops)
            for w in loops:assert advance(edges,q,w)==q
            return

if __name__=='__main__':main()
