#!/usr/bin/env python3
"""L581 defect controls: retain the complete right cone; UNKNOWN is not ABSENT.
No real solver call. Predictions and original failure in RULE30-GPT.md.
"""
import ast
import os
import tempfile
from pathlib import Path
from types import SimpleNamespace
source=Path('tests/probes/lexicon/rule30_relaxed_records_k.py').read_text()
nodes=[n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef)
       and n.name in ('right_half_for','simulate_glued')]
class Solver:
 def __init__(self,model,code=10):self.model=model;self.code=code
 def run(self,*args,**kwargs):return SimpleNamespace(returncode=self.code,stdout=self.model)
with tempfile.TemporaryDirectory() as d:
 env={'tempfile':tempfile,'DIR':d,'KISSAT':'mock','os':os,'subprocess':Solver('v 1 0')}
 exec(compile(ast.Module(body=nodes,type_ignores=[]),'lift-control','exec'),env)
 right=env['right_half_for']('1',0)
 assert right=={1:1}
 assert env['simulate_glued']({0:0},right,0,0,1,0,'1')[0]
 env['subprocess']=Solver('v 1 4 0')
 right=env['right_half_for']('0',1)
 assert right=={1:0,2:1}
 # Literal Rule30 at site1, black wall at t0: 1 XOR (0 OR 1)=0.
 assert 1^(right[1]|right[2])==0
 assert env['simulate_glued']({-1:1,0:1},right,1,1,1,0,'0')[0]
 assert not env['simulate_glued']({-1:1,0:1},{1:0},1,1,1,0,'0')[0]
 env['subprocess']=Solver('',20)
 assert env['right_half_for']('1',0) is None
 env['subprocess']=Solver('',0)
 try:env['right_half_for']('1',0)
 except RuntimeError as e:assert 'UNKNOWN' in str(e)
 else:raise AssertionError('UNKNOWN falsely treated as ABSENT')
print('PASS: both phases retain terminal source cell; omission countercontrol fails; UNKNOWN distinguished')
