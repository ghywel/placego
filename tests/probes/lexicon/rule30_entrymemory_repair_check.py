# Specific GC1035 repair check; no SAT calls. Before running:
# P1 independently packed propagation reproduces identical 190 terminal states.
# Unexpected P2: the two images first coincide before failed gate62 (uncertain).
# Countercontrol: after failure, retaining the old site6 boundary is invalid (GC1035).
# Retain first equality time, not a larger width/horizon sweep.
# OUTCOME: P1 PASS; P2 HELD: first equality59, maximum387, terminal190.
# Joint projection sites7/8 = {01,10,11}; actual histories not enumerated.
# Run from repository root. Inputs are the retained CL204 rows in the ledger.
import re
from pathlib import Path
s=Path('CHAT-LEDGER.md').read_text().split('## CL204')[1]
starts=[]
for lead,n in [('0',19),('1',31)]:
 line=next(l for l in s.splitlines() if 'leading '+lead+', '+str(n)+' states:' in l)
 ws=re.findall(r'\b[01]{12}\b',line);assert len(ws)==n
 starts.append({sum(int(c)<<j for j,c in enumerate('100110'+w)) for w in ws})
S=[set(x) for x in starts];first=None;maxn=0
samples={30+4*k:1 for k in range(10)};samples.update({70:0,72:0,74:1})
for t in range(30,76):
 if S[0]==S[1] and first is None:first=t
 maxn=max(maxn,*map(len,S))
 if t==75:break
 for k in range(2):
  if t in samples:S[k]={r for r in S[k] if (r&1)==samples[t]}
  if t%4==2 and t<=62:S[k]={r for r in S[k] if ((r>>6)&1)==int(t==62)}
  S[k]={(((p<<1)|(t%2))^(p|(p>>1)))&((1<<18)-1) for r in S[k] for p in (r,r|(1<<18))}
assert S[0]==S[1] and len(S[0])==190
print('PASS terminal190, first equal before filters at',first,'maximum states',maxn)
print('pair78',sorted({((r>>6)&1,(r>>7)&1) for r in S[0]}))
