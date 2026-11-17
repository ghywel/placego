from pathlib import Path
import re,ast,json,sys
# Pure source-table comparison; no Rule30 evolution, GPU or Lean execution.
# Usage: task6_table_review.py EXTERNAL_LEAN PINNED_WIDTH6_LEAN
assert len(sys.argv)==3
root=Path(__file__).resolve().parents[3]
ext=Path(sys.argv[1]).read_text()
families=[]
for color,name in [('0','White'),('1','Black')]:
 block=ext.split('def param'+name+'Table :')[1].split('\n]')[0]
 for n,b,r,k,warm in re.findall(r'\((\d+),\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\)',block):
  families.append((color,int(r),format(int(b),'0'+n+'b')))
assert len(families)==22
out={'families':families,'overlap':{}}
for name,expect in [('A',48),('B',80)]:
 txt=(root/('reports/wolfram-agents/submissions/words-'+name+'/Rule30Submission.lean')).read_text()
 words=[]
 for block in re.findall(r'def words(?:8|10) :.*?:= \[(.*?)(?=\n\n)' ,txt,re.S):
  words+=[''.join(re.findall('[01]',x)) for x in re.findall(r'\(\d+,\s*\[([01,\s]+)\]\)',block)]
 assert len(words)==expect and len(set(words))==expect
 hits=[]
 for w in words:
  for c,r,u in families:
   q=len(w)-len(u)
   target=c*q+u
   if q>=r and any(w==target[i:]+target[:i] for i in range(len(w))):
    hits.append({'word':w,'family':c+'^q '+u,'threshold':r,'q':q,'literal':any(len(w)-len(v)>=r0 and w==c0*(len(w)-len(v))+v for c0,r0,v in families)});break
 out['overlap'][name]={'total':len(words),'covered_mod_rotation':len(hits),'literal':sum(x['literal'] for x in hits),'hits':hits}
txt=(root/'reports/wolfram-agents/submissions/channel-14/Pilot6.lean').read_text()
g=ast.literal_eval(re.search(r'def succ6 .*?:= (\[.*?\])',txt)[1]);assert len(g)==31
pats=ast.literal_eval(re.search(r'def col1Forbidden .*?:= (\[.*\])',Path(sys.argv[2]).read_text())[1].replace('true','1').replace('false','0'))
assert len(pats)==9
def run(s,p):
 for b in p:
  if s>=len(g):return None
  s=g[s][b]
 return s if s<len(g) else None
out['channel']=[{'word':''.join(map(str,p)),'from_start':run(0,p),'accepting_start_states':[s for s in range(31) if run(s,p) is not None]} for p in pats]
assert run(0,[1,1]) is None and run(0,[0]) is not None
out['controls']={'positive_zero':run(0,[0]),'negative_11':run(0,[1,1]),'table_cardinalities':[48,80,22,31,9]}
assert all(t!=0 for pair in g for t in pair)
assert all(not x['accepting_start_states'] or x['accepting_start_states']==[0] for x in out['channel'])
print(json.dumps(out,indent=2))
