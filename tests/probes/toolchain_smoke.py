#!/usr/bin/env python3
"""Known-answer tool installation controls (GC2343, 2026-11-01).

Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tests/probes/toolchain_smoke.py.
Small installation checks only; no research census. Requires the tools in TOOLS.md.
Each external command has a 30-second timeout; cake_lpr heap and stack are 32 MiB each.
"""
import importlib.metadata as md, json, subprocess, tempfile
from pathlib import Path
import numpy as np, scipy.linalg as la, sympy as sp, networkx as nx, gmpy2, mpmath, z3, cvc5
from pysat.formula import CNF
from pysat.examples.genhard import PHP
from pysat.solvers import Solver
packages=['numpy','scipy','sympy','networkx','gmpy2','mpmath','python-sat','z3-solver','cvc5','certifi']
report={'packages':{n:md.version(n) for n in packages}}
assert np.array_equal(np.array([[1,2],[3,4]])@np.array([1,1]),[3,7])
assert np.allclose(la.solve([[2,0],[0,4]],[4,8]),[2,2])
x=sp.Symbol('x'); assert sp.expand((x+1)**2)==x*x+2*x+1
assert nx.shortest_path_length(nx.path_graph(5),0,4)==4
assert int(gmpy2.invert(3,65536))==43691
assert mpmath.sqrt(4)==2
cnf=PHP(nof_holes=4)
for name in ['cadical195','glucose4','minisat22']:
 with Solver(name=name,bootstrap_with=cnf.clauses) as s: assert not s.solve()
 with Solver(name=name,bootstrap_with=[[1,2]]) as s: assert s.solve()
b=z3.BitVec('x',16);s=z3.Solver();s.add(3*b==1);assert s.check()==z3.sat and s.model()[b].as_long()==43691
c=cvc5.Solver();c.setLogic('QF_BV');c.setOption('produce-models','true');sort=c.mkBitVectorSort(16);b=c.mkConst(sort,'x');c.assertFormula(c.mkTerm(cvc5.Kind.EQUAL,c.mkTerm(cvc5.Kind.BITVECTOR_MULT,c.mkBitVector(16,3),b),c.mkBitVector(16,1)));assert c.checkSat().isSat() and int(c.getValue(b).getBitVectorValue(10))==43691
report['python_known_answers']='PASS'
def run(args,input=None):
 p=subprocess.run(args,input=input,text=True,capture_output=True,timeout=30);return p.returncode,p.stdout+p.stderr
with tempfile.TemporaryDirectory() as d:
 p=Path(d);cnf.to_file(p/'php.cnf')
 rc,out=run(['cadical','--lrat','--no-binary',str(p/'php.cnf'),str(p/'php.lrat')]);assert rc==20,(rc,out)
 rc,out=run(['cake_lpr','--CML_HEAP_SIZE=32','--CML_STACK_SIZE=32',str(p/'php.cnf'),str(p/'php.lrat')]);assert 's VERIFIED UNSAT' in out,(rc,out)
 (p/'unit.cnf').write_text('p cnf 1 2\n1 0\n-1 0\n');(p/'good.lrat').write_text('3 0 1 2 0\n');(p/'bad.lrat').write_text('3 0 1 1 0\n')
 for filename,expected in [('good.lrat',True),('bad.lrat',False)]:
  rc,out=run(['cake_lpr','--CML_HEAP_SIZE=32','--CML_STACK_SIZE=32',str(p/'unit.cnf'),str(p/filename)]);assert ('s VERIFIED UNSAT' in out)==expected,(filename,rc,out)
 rc,out=run(['cadical','--no-binary',str(p/'php.cnf'),str(p/'php.drat')]);assert rc==20
 rc,out=run(['drat-trim',str(p/'php.cnf'),str(p/'php.drat')]);assert 's VERIFIED' in out,(rc,out)
 (p/'empty.drat').write_text('');rc,out=run(['drat-trim',str(p/'php.cnf'),str(p/'empty.drat')]);assert 's VERIFIED' not in out
 (p/'tiny.lean').write_text('example : 2 + 2 = 4 := by decide\n#print axioms Nat.add_comm\n')
 rc,out=run(['lean','+leanprover/lean4:v4.35.0',str(p/'tiny.lean')]);assert rc==0,(rc,out)
report['cadical_lrat_cake_good_and_corrupt_hint']='PASS';report['drat_good_and_empty']='PASS';report['lean_4_35_kernel']='PASS'
rc,out=run(['gp','-q','-f'],input='print(valuation(3^100-1,2));print(lift(Mod(3,2^16)^(-1)));quit\n');assert rc==0 and out.split()==['4','43691'],(rc,out)
report['pari_known_answers']='PASS'
print(json.dumps(report,indent=2))
