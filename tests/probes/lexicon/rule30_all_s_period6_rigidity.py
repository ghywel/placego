"""GC687: preregistered92dc35ba; fixed temporal-six domain only.

Prediction: one live84-cycle and one infinite entrance. Counterfactual: raw
branching supplies independent infinite tails. Outcome:594 raw branches,
none live;20 entrances, one surviving;3714 literal controls.
"""
import json
from collections import deque,Counter
from rule30_all_s_period6 import children,literal_children,bit
prefixes={(42,c):[42,c] for c in range(64) if [bit(c,t) for t in (0,2,4)]==[1,0,0]}
for required in (1,1,0,1):
    prefixes={(b,c):row+[c] for (a,b),row in prefixes.items() for c in children(a,b) if bit(c,0)==required}
graph={};queue=deque(prefixes)
while queue:
    p=queue.popleft()
    if p in graph:continue
    cs=children(*p);assert cs==literal_children(*p)
    graph[p]=[(p[1],c) for c in cs];queue.extend(graph[p])
# Independent greatest fixed-point iteration, rather than GC686's degree queue.
live=set(graph);rounds=0
while True:
    following={p for p in live if any(c in live for c in graph[p])}
    if following==live:break
    rounds+=1;live=following
out=Counter(sum(c in live for c in graph[p]) for p in live)
incoming=Counter(sum(p in graph[q] for q in live) for p in live)
cycles=[];remaining=set(live)
if out==Counter({1:len(live)}):
    while remaining:
        p=min(remaining);path=[];seen={}
        while p not in seen:
            seen[p]=len(path);path.append(p)
            p=next(c for c in graph[p] if c in live)
        cycles.append(len(path)-seen[p]);remaining.difference_update(path)
result=dict(reachable=len(graph),live=len(live),pruning_rounds=rounds,
 live_outdegree=dict(out),live_indegree=dict(incoming),cycle_lengths=cycles,
 entrance_count=len(prefixes),live_entrances=[list(p) for p in prefixes if p in live],
 raw_branch_vertices=sum(len(v)>1 for v in graph.values()),
 live_branch_vertices=sum(sum(c in live for c in graph[p])>1 for p in live),
 pair_controls=len(graph))
# Retain all entrance paths; pair deduplication must not hide different prefixes.
rows=[[42,c] for c in range(64) if [bit(c,t) for t in (0,2,4)]==[1,0,0]]
for required in (1,1,0,1):
    rows=[row+[c] for row in rows for c in children(*row[-2:]) if bit(c,0)==required]
valid=[r for r in rows if tuple(r[-2:]) in live]
assert len(rows)==20 and valid==[[42,11,13,33,60,23]]
assert out==incoming==Counter({1:84}) and cycles==[84]
result.update(all_entrance_paths=len(rows),surviving_entrance_paths=valid)
print(json.dumps(result,sort_keys=True))
