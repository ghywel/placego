#!/usr/bin/env python3
"""GC2105: byte-preserving arc assembly; --check verifies the committed result without writing."""
from pathlib import Path
import re,ast,hashlib,json
root=Path(__file__).resolve().parents[3]
folder=root/'reports/wolfram-agents/submissions/arc-codes'
wrapper=(root/'tests/probes/wolfram/check_arc_integration.sh').read_text()
expected=ast.literal_eval(re.search(r'^expected = (\{.*\})$',wrapper,re.M).group(1))
imports=[];parts=[];heads=[]
for name,digest in expected.items():
 data=(folder/(name+'.lean')).read_bytes();assert hashlib.sha256(data).hexdigest()==digest,name
 s=data.decode();n=s.index('namespace ');prefix=s[:n]
 for imp in re.findall(r'^import (\S+)\s*$',prefix,re.M):
  if not imp.startswith('Arc') and imp not in imports: imports.append(imp)
 rest=re.sub(r'^import \S+\s*$','',prefix,flags=re.M)
 rest=re.sub(r'/\-!.*?\-/','',rest,flags=re.S)
 assert not rest.strip(),(name,rest)
 body=s[n:].strip()
 heads+=['Rule30Submission.'+x for x in re.findall(r'^#print axioms (\S+)\s*$',body,re.M)]
 body=re.sub(r'^#print axioms \S+\s*\n','',body,flags=re.M)
 parts.append('/- Component: '+name+'; proof body retained from the reviewed integration. -/\n'+body)
assert len(heads)==40 and len(set(heads))==40
header='''/-!
# Finite-step irrational rotation codes excluded beside a Rule 30 clock

For an initial row with a leftmost black cell at -L and an alternating column0 from time0,
its visible neighbour evol x (2*s) 1 cannot eventually code a finite-step irrational circle
rotation whose continued-fraction digits exceed2^(r+1) arbitrarily late. Here r counts the
supplied endpoint labels; no minimality is assumed. Arbitrary changes at those endpoints
and concrete unions of k half-open intervals are included, the latter with threshold2^(2*k+1).

The proof constructs breaks from the physical window-Jen bound, labels their signed lifted
mismatch intervals, and uses a finite pigeonhole argument plus continuant determinant spacing.
The growing previous denominator pays the fixed margin at the stated digit threshold.

This is the formal delivery of the record's Theorem E-double-prime, with the finite-endpoint
extension already in G131/G132. It does not exclude all irrational rotation codings, prove an
arbitrary physical-clock restart, or solve a prize problem. Classical coding and continued-
fraction ingredients are prior art. See the companion essay for precise scope and provenance.
-/
'''
s='\n'.join('import '+x for x in imports)+'\n\n'+header+'\nnamespace Rule30Submission\n\n'+'\n\n'.join(parts)+'\n\n'+ '\n'.join('#print axioms '+x for x in heads)+'\n\nend Rule30Submission\n'
assert not re.search(r'^import Arc',s,re.M)
assert not re.search(r'\b(?:sorry|native_decide|bv_decide|skipKernelTC)\b',s)
source_path=folder/'Rule30Submission.lean'
if '--check' in __import__('sys').argv:
 assert source_path.read_text()==s,'assembled source differs'
else:
 source_path.write_text(s)
manifest={'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'source_bytes':len(s.encode()),'components':expected,'public_imports':imports,'printed_headlines':heads,'physical_headlines':heads[-4:],'transformation':'Remove top component imports/header docs and axiom-print commands; preserve each complete namespace/proof body exactly; deduplicate public imports; wrap in Rule30Submission; print the same40 names with prefix. New single-file import/namespace context is unvalidated.'}
manifest_text=json.dumps(manifest,indent=2)+'\n'
if '--check' in __import__('sys').argv:
 assert (folder/'assembly.json').read_text()==manifest_text,'assembly manifest differs'
else:
 (folder/'assembly.json').write_text(manifest_text)
print(manifest['source_sha256'],manifest['source_bytes']);print('\n'.join(imports))

prose=(folder/'essay-prose.md').read_text()
assert prose.count('%%LEAN%%')==1
prose=prose.replace(' This essay is currently a preparation draft, not a report that these cells ran.','')
essay=prose.replace('%%LEAN%%',json.dumps(s,ensure_ascii=False)[1:-1])
if '--check' in __import__('sys').argv:
 assert (folder/'essay.md').read_text()==essay,'essay source binding differs'
else:
 (folder/'essay.md').write_text(essay)
