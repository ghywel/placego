#!/usr/bin/env python3
"""GC2564: one standalone Lean component check, no kit build or solver."""
import ast,hashlib,json,os,re,resource,signal,subprocess,time
from pathlib import Path
OUT=Path(os.environ['CAPPED_OUT']);STOP=[];REPORT={'status':'STARTED','commands':[]}
p=Path(__file__).parents[1]/'ether_gap_solve.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d'
names={'save','cpu','thermal','command'}
sel=[n for n in ast.parse(p.read_bytes()).body if isinstance(n,ast.FunctionDef) and n.name in names]
assert len(sel)==4
exec(compile(ast.Module(body=sel,type_ignores=[]),str(p),'exec'),globals())
try:
 os.nice(10);resource.setrlimit(resource.RLIMIT_CPU,(10,90))
 for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda s,f:STOP.append(s))
 source=Path('tests/probes/lean/BoundaryForecast.lean')
 assert hashlib.sha256(source.read_bytes()).hexdigest()=='a88c8e40facfa0ebefd539bfaa84a03fc1d3ae862b9aef20b3b5a6d9f9b572ad'
 rc,text,why=command('lean-components',['/usr/local/bin/lean','-j1','-M384',str(source)],15,25)
 assert rc==0 and why=='EXIT', 'LEAN_COMPONENT_CHECK_FAILED'
 assert text.count('does not depend on any axioms')==6,text
 assert 'sorry' not in text and 'warning:' not in text,text
 REPORT.update(status='LEAN_COMPONENTS_PASS',scope='Known a10,0011 Boolean identities; conditional forecast transport; ignored-input existential filter; three saved moves. NOT full trajectory lift or closure certification.',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
 thermal();save();print(json.dumps(REPORT,indent=2))
except BaseException as e:
 REPORT.update(status='FAILED',failure=repr(e));save();raise
