#!/usr/bin/env python3
"""Exact local propagation on the diagnostic's grid; no image modification.

Frozen specification in reports/rule30-staircase-investigation.md.
No branching search or invented red-cell values: retain a value only when
every locally compatible Rule30 quadruple has it. Unknowns may remain.
"""
import json
import resource
import signal
import sys


resource.setrlimit(resource.RLIMIT_CPU, (20,20))
resource.setrlimit(resource.RLIMIT_FSIZE, (2*1024**2,2*1024**2))
signal.alarm(30)
source = json.load(open(sys.argv[1]))['grid_light_is_1']
assert len(source) == 32 and all(len(s)==32 for s in source)
domains = [{0,1} if b=='?' else {int(b)} for row in source for b in row]
quads = [(r*32+c-1,r*32+c,r*32+c+1,(r+1)*32+c)
         for r in range(31) for c in range(1,31)]
allowed = [(l,c,r,l^(c|r)) for l in (0,1) for c in (0,1) for r in (0,1)]
initial = sum(len(d)==2 for d in domains)
deductions=[]
for sweep in range(1025):
    changed=False
    for q in quads:
        compatible=[v for v in allowed if all(v[i] in domains[q[i]] for i in range(4))]
        assert compatible, ('Inconsistent extraction',q)
        for i,cell in enumerate(q):
            reduced={v[i] for v in compatible}
            if reduced != domains[cell]:
                deductions.append({'cell':divmod(cell,32),'value':sorted(reduced),'equation':q})
                domains[cell]=reduced
                changed=True
    if not changed:break
else:raise AssertionError('Propagation did not terminate within its finite bound')
grid=[''.join(str(next(iter(d))) if len(d)==1 else '?' for d in domains[r*32:(r+1)*32]) for r in range(32)]
print(json.dumps({'initial_unknown':initial,'remaining_unknown':sum(len(d)==2 for d in domains),
                  'sweeps':sweep+1,'grid':grid,'deductions':deductions,
                  'peak_rss_host_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
