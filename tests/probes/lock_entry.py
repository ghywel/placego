#!/usr/bin/env python3
"""L1326 T46 (Local, 2026-11-02): how does every alignment's clean front lock onto the one orbit U?
reports/rule30-genealogy.md section 50 (predictions written first). Run: python3 tests/probes/lock_entry.py PHASE U_FILE

For every alignment (P1024: theta in 0..1023; 480: (a, q), a in 0..29, q in 0..31, one per class of its 960), the clean
start (row = the phase's tail at that alignment, black edge above) runs to tick 2,480. Recorded: the first tick at which
the 8-cell state (class, window; bit j-1 = D_(R-j)) lies in U, and that state; the first tick at which the class lies
on U's class set; and any tick after entry with the state outside U.
"""
import os
import sys
import runpy
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name, ufile = sys.argv[1], sys.argv[2]
p, cols, _ = g['phases']()[name]; NC = len(cols)
W = 8; TA = 2480; DA = 2 * TA + 16; MA = (1 << DA) - 1
U = set()
for line in open(ufile):
    if not line.startswith('#') and line.strip():
        c, w = line.split(); U.add((int(c), int(w, 2)))
UC = {c for c, w in U}
rev = [int(format(v, '0%db' % W)[::-1], 2) for v in range(1 << W)]
if name == 'P1024':
    col0 = cols[0]
    base = [sum(((col0 >> ((k + 195 * n) % p)) & 1) << n for n in range(DA)) for k in range(p)]
    aligns = list(range(p))
    def arow(al, t):
        return base[(al + t) % p]
    def acls(al, R, t):
        return (al + t + 195 * R) % p
else:
    pat = [''.join(str((cols[n] >> k) & 1) for n in range(NC)) for k in range(p)]
    reps = DA // NC + 2; abase = {}
    def arow(al, t):
        key = (al[0], (t + al[1]) % p)
        if key not in abase:
            s0 = pat[key[1]]; s0 = (s0[key[0]:] + s0[:key[0]]) * reps
            abase[key] = int(s0[:DA][::-1], 2)
        return abase[key]
    def acls(al, R, t):
        return ((R + al[0]) % NC) * p + (t + al[1]) % p
    aligns = [(a, q) for a in range(30) for q in range(p)]
entry = []; first = Counter(); classfirst = []; lead = []; leave = 0; never = 0
for al in aligns:
    x = arow(al, 0); te = None; tc = None
    for t in range(TA + 1):
        d = x ^ arow(al, t); R = d.bit_length() - 1
        if R >= 12:
            c = acls(al, R, t); st = (c, rev[(d >> (R - W)) & 255])
            if tc is None and c in UC:
                tc = t
            if te is None and st in U:
                te = t; first[st] += 1
            elif te is not None and st not in U:
                leave += 1
        x = (x ^ ((x << 1) | (x << 2) | 3)) & MA
    if te is None:
        never += 1; continue
    entry.append(te); classfirst.append(tc); lead.append(te - tc)
def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(q * len(v)))]
print('%s: %d alignments; never entered U by tick %d: %d; ticks after entry outside U: %d' % (name, len(aligns), TA, never, leave), flush=True)
print('   entry tick: min %d, median %d, 90%% %d, max %d' % (min(entry), pct(entry, 0.5), pct(entry, 0.9), max(entry)), flush=True)
print('   class first on the cycle: median tick %d; window locks this many ticks later: median %d, 10%% %d, max %d; '
      'alignments with the class first by >= 10 ticks: %d' % (pct(classfirst, 0.5), pct(lead, 0.5), pct(lead, 0.1),
      max(lead), sum(1 for v in lead if v >= 10)), flush=True)
print('   distinct first states in U: %d; the most common: %s' % (len(first), first.most_common(8)), flush=True)
print('LOCK_ENTRY_DONE')
