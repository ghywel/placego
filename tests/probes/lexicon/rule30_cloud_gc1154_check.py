#!/usr/bin/env python3
"""rule30_cloud_gc1154_check.py: Cloud's targeted (tier 2) check of the carrying step of GPT's GC1154 comparators: a
visible word (column 1 at the white-wall ticks) that is periodic with period m over a window fixes the left cells the
window determines, and those cells have white gaps at most 4m - 2, by Theorem B of RULE30-PRIZE.md section 8.54
(P-periodic columns 0 and 1 give left zero runs at most 2P - 2) applied to the fully periodic trace of full period
2m (CL356).

RUN-ON:     cpu (Python 3 standard library; seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1154_check.py

WHAT. For m = 1..5 and every one of the 2^m visible blocks: (1) the fully periodic trace (visible word the block
repeated, odd samples 0) is run leftward to depth 240 from a white-wall anchor and the largest white gap of the left row
at time 0 is compared with 4m - 2; (2) the odd samples are then drawn at random (eight draws) and the left row compared
cell by cell with (1): the masked samples must not move a single cell; (3) fixedness: a window of C visible samples
followed by random samples (eight draws) must give the same first 2C left cells as the periodic trace, and may differ
beyond.

PREDICTIONS (CL356, written before the run; the same step was run inline earlier today and is here made a probe). P1:
every block of every m = 1..5 has gap <= 4m - 2, with equality for some block at m = 2 (0.85). P2: no odd sample moves a
left cell (0.95). P3: the first 2C cells agree for every window and draw (0.9). Counterfactual: a gap above 4m - 2
would mean Theorem B does not carry to the visible-period setting and GC1154's comparator could exclude a real record
word. Unexpected check: the largest gap found for each m, against the bound; is the bound ever tight beyond m = 2?
Record searched: Theorem B, 4m-2, visible period (ledgers only). NOTE: the first run of this file had the two starting
columns of left_row swapped (column 1 in the XOR, the wall in the OR); its part (2) caught that at once (496 draws moved
a cell), the columns were put right and the run below is the corrected one.
"""
import random, itertools
random.seed(20261011)
def left_row(c,K):   # column by column: x(-k,t) = x(-k+1,t+1) XOR (x(-k+1,t) OR x(-k+2,t))
    T=len(c); prev=[t%2 for t in range(T)]; prev2=list(c); out=[]   # prev = column -k+1, prev2 = column -k+2
    for k in range(1,K+1):
        cur=[prev[t+1]^(prev[t]|prev2[t]) for t in range(T-k)]
        out.append(cur[0]); prev2,prev=prev,cur
    return out
def trace(vis,odd,T):   # vis[j] = c[2j], odd[j] = c[2j+1]
    return [vis[t//2] if t%2==0 else odd[t//2] for t in range(T)]
def gaps(L):
    g=0; m=0
    for b in L:
        if b==0: g+=1; m=max(m,g)
        else: g=0
    return m
K=240; T=K+2; bad1=bad2=bad3=0; tight=[]
for m in range(1,6):
    worst=0
    for block in itertools.product((0,1),repeat=m):
        vis=[block[j%m] for j in range(T//2+1)]
        L0=left_row(trace(vis,[0]*(T//2+1),T),K); g=gaps(L0); worst=max(worst,g)
        if g>4*m-2: bad1+=1; print('   GAP ABOVE BOUND m',m,'block',block,'gap',g)
        for _ in range(8):
            odd=[random.randint(0,1) for _ in range(T//2+1)]
            if left_row(trace(vis,odd,T),K)!=L0: bad2+=1
        for C in (m+3,2*m+5,4*m):
            for _ in range(8):
                vis2=vis[:C]+[random.randint(0,1) for _ in range(T//2+1-C)]
                L2=left_row(trace(vis2,[0]*(T//2+1),T),K)
                if L2[:2*C]!=L0[:2*C]: bad3+=1
    if worst==4*m-2: tight.append(m)
    print('m = %d | blocks %2d | largest white gap %2d | bound 4m-2 = %2d | %s'
          %(m,2**m,worst,4*m-2,'ok' if worst<=4*m-2 else 'FAIL'))
print('(1) gaps above the bound:',bad1,'| tight at m =',tight)
print('(2) odd-sample draws that moved a left cell:',bad2)
print('(3) windows whose first 2C cells differed from the periodic trace:',bad3)
