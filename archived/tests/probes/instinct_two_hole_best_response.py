#!/usr/bin/env python3
"""B206 / MI402: same-domain minimum-physical-error count feedback.
RUN-ON: CPU, standard-library Python. COST: 5 CPU second cap.
COMMAND: python3 tests/probes/instinct_two_hole_best_response.py
Preregistration MI402; outcome MI403. One n9 target, same45 count states.
Predict strict descent fails; inspect all minimum-error choices, and the
lexicographically first minimizer's whole graph. Independent physical map,
1680 partition count, zero-error equivalence, old policy's2-cycle control.
Unexpected check distinguishes universal/existential strict progress from
termination. No broader domain or retry. Analysis oracle, not a theorem.
The source below was executed once from a temporary file; copied unchanged
here for reproducibility with this metadata header added after the run.
"""
import ast,itertools as it,json,time
from pathlib import Path
start=time.process_time()
# Import only the existing definitions; do not replay its prior experiment.
source=ast.parse(Path('tests/probes/instinct_two_hole_feedback.py').read_text())
keep=[n for n in source.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef)) and (not isinstance(n,ast.FunctionDef) or n.name in ('partitions','independent'))]
ns={};exec(compile(ast.Module(body=keep,type_ignores=[]),'prior-definitions','exec'),ns)
parts=tuple(ns['partitions'](9,(3,3,3)));assert len(parts)==1680
pool=(0,1,2,4,5,7,8,9,10);target=(15,15,16)
def counts(P):return tuple((sum(j>=3 for j in B),sum(j>=5 for j in B)) for B in P)
def error(P):return sum(abs(sum(pool[j] for j in B)-u) for B,u in zip(P,target))
row=[(k,l) for k in range(4) for l in range(k+1)]
states=tuple(x for x in it.product(row,repeat=3) if sum(k for k,l in x)==6 and sum(l for k,l in x)==4);assert len(states)==45
fibres={};E={};mins={}
for K in states:
 w=tuple(u-k-l for u,(k,l) in zip(target,K));Ps=[P for P in parts if tuple(map(sum,P))==w]
 assert Ps;fibres[K]=Ps;E[K]=min(map(error,Ps));mins[K]=[P for P in Ps if error(P)==E[K]]
physical=ns['independent'](pool,(3,3,3),target);assert len(physical)==10
inv={x:i for i,x in enumerate(pool)};goalcounts={counts(tuple(tuple(inv[x] for x in B) for B in P)) for P in physical}
assert {K for K in states if E[K]==0}==goalcounts
bad_all=[];bad_some=[];F={};old={};levels={}
for K in states:
 succ={counts(P) for P in mins[K]};assert succ<=set(states)
 levels[E[K]]=levels.get(E[K],0)+1
 F[K]=counts(mins[K][0]);old[K]=counts(fibres[K][0])
 if E[K]>0:
  if any(E[S]>=E[K] for S in succ):bad_all.append((K,E[K],[(S,E[S]) for S in sorted(succ)]))
  if not any(E[S]<E[K] for S in succ):bad_some.append((K,E[K],[(S,E[S]) for S in sorted(succ)]))
def cycles(F):
 cs=set();basin={}
 for K in states:
  seen={};path=[];S=K
  while S not in seen:seen[S]=len(path);path.append(S);S=F[S]
  c=tuple(path[seen[S]:]);c=min(c[i:]+c[:i] for i in range(len(c)))
  cs.add(c);basin[c]=basin.get(c,0)+1
 return [{'length':len(c),'basin':basin[c],'states':c,'errors':[E[s] for s in c]} for c in sorted(cs)]
oldcycles=cycles(old);assert len(oldcycles)==1 and oldcycles[0]['length']==2
assert time.process_time()-start<5
print(json.dumps({'states':len(states),'physical_partitions':len(physical),'error_levels':levels,'universal_strict_failures':len(bad_all),'existential_strict_failures':len(bad_some),'first_failure':bad_all[0] if bad_all else None,'first_existential_failure':bad_some[0] if bad_some else None,'best_error_lex_cycles':cycles(F),'controls':'passed','cpu_seconds':time.process_time()-start},indent=2))
