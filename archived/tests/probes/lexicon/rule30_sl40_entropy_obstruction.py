#!/usr/bin/env python3
"""GC1007: exact entropy obstruction to actual closure of its full SCC.
Predictions and interpretation in RULE30-GPT.md; no new language query.
"""
import runpy
from fractions import Fraction as F
s=runpy.run_path('tests/probes/lexicon/rule30_sl40_branch.py')
group=next(c for c in s['components'] if len(c)==79)
E=s['edges']; z=F(109,100)
assert 109**2500 > (2**309)*(100**2500)  # log2(z)>0.1236 exactly.
v={q:F(1) for q in group}
for k in range(12):
 u={q:sum((v[r]/z**(3 if g=='S' else 5)
           for g,r in E[q].items() if r in v),F(0)) for q in group}
 if k==11:
  assert all(u[q]>v[q] for q in group)
  print('Exact M*v>v on79 states after12 iterations; log2(1.09)>0.1236')
 v=u
# Control: same graph counting one tick per gap uses different edge weights.
assert sum(len('001' if g=='S' else '00001') for g in 'SLLLSLSL')==34
assert sum(len('001' if g=='S' else '00001') for g in 'LLSLSL')==26
print('Elapsed-visible-length controls PASS; full recurrent component cannot be actual')

# Finite missing-factor bound using the existing SQ6 word-count ceiling.
# Its printed four-decimal entropy is <0.1237; ratio135663 is <10^6.
b=F(10898,10000); C=1000000
assert 10898**10000 > 2**1237*10000**10000
v={q:F(1) for q in group}
def M(v):
 return {q:sum((v[r]/z**(3 if g=='S' else 5)
                for g,r in E[q].items() if r in v),F(0)) for q in group}
for _ in range(79):v=M(v)
u=M(v);r=min(u[q]/v[q] for q in group)
assert r>1
root='1000010010000100100001'
a=v[root]/max(v.values()); total=F(C)/(1-b/z)
assert a*r**1024 > total
print('Exact finite obstruction: some internal path has absent W factor of length41..5120')
