#!/usr/bin/env python3
"""rule30_cloud_gc1156_check.py: Cloud's targeted (tier 2) check of GPT's GC1156 carrying step on Local's sharp
depth-132 witness (d = 132, L = 17, phase 0, T = 148, in rule30_local_record_traces.txt): the visible sample at tick
148 is not masked (148 is even), yet every exterior beyond the stored 145-cell right prefix keeps it white and the left
cell at depth 149 black, by the sixteen completions of sites 146..149 and by a three-valued set propagation in which
the unknown front never reaches column 1 before tick 149 (CL356).

RUN-ON:     cpu (Python 3 standard library; seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1156_check.py

WHAT. (1) The block's trace, visible word and left row are replayed (clamped run of the right prefix; leftward relation
from the trace), the band 132..148 read, and depth 149 computed from c[0..148]. (2) The sixteen completions of sites
146..149 (zeros beyond), each run clamped: c[148] and the left cell at depth 149 recorded; c[t] for t <= 144 cannot
change (light cone), c[145..148] may. (3) Set propagation: sites 146 and beyond unknown, cells in {0, 1, ?}, the rule
x' = l XOR (c OR r) evaluated on sets (OR is 1 when either side is 1, 0 when both are 0, else ?; XOR with ? is ?); the
first unknown site at each tick to 149 and whether c[148] is determined. (4) The unclamped run of the forced left row,
the wall cell and the right prefix: the clock holds to tick 149, and breaks first at 149 once depth 149 is made white.

PREDICTIONS (CL356, written before the run). P1: the stored left row is reproduced, 132..148 white, 149 black (0.9).
P2: all sixteen completions keep c[148] = 0 and depth 149 black (0.8). P3: the propagation determines c[148] = 0 and
the first unknown site stays >= 82 through tick 149 (0.7). P4: clock to 149; first break at 149 with depth 149 white
(0.85). Counterfactual: a completion with c[148] = 1 would be an exterior that extends the sharp 17 to 18 at depth 132
and refute Local's exact value, so P2 is also a check of the census. Unexpected check: how many completions change any
of c[145..147] while leaving c[148] alone. Record searched: unmasked endpoint, set propagation, enclosure (ledgers
only).
"""
import itertools
lines=open('tests/probes/lexicon/rule30_local_record_traces.txt').read().split('\n')
i=[k for k,l in enumerate(lines) if l.startswith('d=132 L=17 phase=0 T=148 status=exact')][0]
blk={l.split('=')[0]:l.split('=')[1] for l in lines[i+1:i+5]}
TR=[int(b) for b in blk['trace']]; VIS=[int(b) for b in blk['visible']]; LEFT=[int(b) for b in blk['left']]
R=[int(b) for b in blk['right']]; assert len(R)==145 and len(TR)==149 and len(LEFT)==148
def column1(right,T):
    row=list(right)+[0]*(T+2); c=[]
    for t in range(T):
        c.append(row[0]); w=t%2
        row=[(row[j-1] if j else w)^(row[j]|row[j+1]) for j in range(len(row)-1)]
    return c
def left_row(c,K):
    T=len(c); prev=[t%2 for t in range(T)]; prev2=list(c); out=[]
    for k in range(1,K+1):
        cur=[prev[t+1]^(prev[t]|prev2[t]) for t in range(T-k)]
        out.append(cur[0]); prev2,prev=prev,cur
    return out
c=column1(R,149); assert c==TR, 'trace replay differs'
vis=[c[t] for t in range(0,149,2)]; assert vis[:len(VIS)]==VIS   # Local's visible word stops at tick 146 (74 bits)
print('    visible word: Local stores',len(VIS),'bits (ticks 0..146); the even samples to 148 agree on them')
L=left_row(c+[0],149)        # c[149] is masked (odd tick); K = 149 needs the wall to tick 149
print('(1) stored left row reproduced:',L[:148]==LEFT,'| 132..148 white:',all(L[k-1]==0 for k in range(132,149)),
      '| depth 149:','black' if L[148] else 'WHITE')
keep=0; changed_early=0; depth149=set()
for bits in itertools.product((0,1),repeat=4):
    R2=R+list(bits); c2=column1(R2,149); L2=left_row(c2+[0],149)
    assert c2[:145]==c[:145]
    if c2[148]==0: keep+=1
    if c2[145:148]!=c[145:148]: changed_early+=1
    depth149.add(L2[148])
print('(2) completions keeping c[148] = 0:',keep,'of 16 | depth 149 values seen:',sorted(depth149),
      '| completions changing c[145..147]:',changed_early)
U=None
def OR(a,b):
    if a==1 or b==1: return 1
    if a==0 and b==0: return 0
    return U
def XOR(a,b):
    if a is U or b is U: return U
    return a^b
row=R+[U]*300; first=[]; cset=[]
for t in range(150):
    cset.append(row[0]); first.append(next((j+1 for j,v in enumerate(row) if v is U),None))
    w=t%2; row=[XOR(row[j-1] if j else w,OR(row[j],row[j+1])) for j in range(len(row)-1)]
print('(3) set propagation: c[148] =',cset[148],'| first unknown site, min over ticks 0..149:',min(first[:150]),
      '| at tick 149:',first[149],'| samples c[0..148] all determined:',all(v is not U for v in cset[:149]))
def unclamped(left,right,T):
    row=left[::-1]+[0]+list(right)+[0]*(T+2); z=len(left); out=[]
    for t in range(T+1):
        out.append(row[z]); row=[(row[j-1] if j else 0)^(row[j]|row[j+1]) for j in range(1,len(row)-1)]; z-=1
    return out
col0=unclamped(L,R,149); bad=[t for t in range(150) if col0[t]!=t%2]
Lw=L[:]; Lw[148]=0; badw=[t for t in range(150) if unclamped(Lw,R,149)[t]!=t%2]
print('(4) forced left row keeps the clock to 149:',not bad,'| with depth 149 white, first break at tick:',badw[:3])
