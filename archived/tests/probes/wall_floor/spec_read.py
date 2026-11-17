#!/usr/bin/env python3
"""spec_read.py (Local, L1552): reads the specimens of wall_spec145: the route of (phase, depth) around each hit, how far the specimens agree with one another at each tick, and what lies just below 145."""
import re,collections
S=[];cur=None
for l in open('spec_run/out.txt'):
    if l.startswith('SPEC'):
        cur=[];S.append(cur);continue
    m=re.match(r'(-?\d+) (\d+) (\d+) ([#.]+)$',l)
    if m and cur is not None: cur.append((int(m[1]),int(m[2]),int(m[3]),m[4]))
print('specimens',len(S),'rows each',len(S[0]))
S=[s for s in S if len(s)==96]
# the hit is at index 0 relative: entry with i==0 is 47 before end -> find the row with depth>=145
routes=collections.Counter()
for s in S:
    routes[tuple((p,d) for i,d,p,_ in s if -12<=i<=14)]+=1
print('distinct routes around the hit',len(routes))
for r,c in routes.most_common(6):
    print(c,' '.join(f'{p}:{d}' for p,d in r))
ref=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
def lcp(a,b):
    k=0
    while k<len(a) and a[k]==b[k]: k+=1
    return k
print('tick: min and median common depth among specimens (rows top first)')
for i in range(-46,48,2):
    rows=[next(r for r in s if r[0]==i)[3] for s in S]
    base=rows[0]
    c=sorted(lcp(base,r) for r in rows[1:])
    print(i,'min',c[0],'med',c[len(c)//2],'distinct top-100',len({r[:100] for r in rows}),'top-200',len({r[:200] for r in rows}))
