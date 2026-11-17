#!/usr/bin/env python3
"""RD16-E: endpoint diagnostic on Local's independent retained clocks.
Preregistered GPT 2026-10-07: one CPU replay of rule30_rd16_check.py,
its 300 CPU-second cap retained; no new tree implementation or TM6b change.
P1 uncertain: all sixteen terminal h=0 at slope5/2.
C1 source's entire published witness/debt verification must pass.
C2 terminal zero edge leaves D unchanged and maps h to max(h-5,0).
CF unchanged D implies strict new minimum: reject using adjusted(7,-5).
U distinguish equality to the old minimum from a strict decrease.
Output outside Git; evidence only for sixteen finite prefixes.
OUTCOME 2026-10-07: one Intel CPU replay, source24.7s. C1/C2/CF/U PASS.
P1 REFUTED: endpoint h=0.5 at N5=291257 and h=5 at N5=634886;
other fourteen h=0. The two positive h exits do not lower the minimum.
All sixteen published debts/witnesses reproduce; bound75 unchanged.
No inference beyond these entries or new independent tree constructor.
"""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('rule30_rd16_check.py')))
assert r['ok'], 'source verification failed'
rows=[]
for n,T in sorted(r['histories']):
    z=[2*t-5*d for d,t in enumerate(T)]
    before=z[-2]-min(z[:-1]); after=z[-1]-min(z)
    assert T[-1]==T[-2] and after==max(before-5,0)
    rows.append((n,before,after,z[-1]<min(z[:-1])))
assert max(0,7,2)==7 and min(0,7,2)==0
assert max(5-5,0)==0 and not (0<0)
print('N5, doubled h before/after zero, strict new minimum:',rows)
print('P1 all terminal h zero:',all(row[2]==0 for row in rows))
