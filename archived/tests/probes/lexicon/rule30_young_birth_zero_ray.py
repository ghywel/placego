"""GC1199: one existing age-1 witness, with its tail terminated by zeros.
PREDICTIONS BEFORE RUN, 2026-10-13 19:55 BST.
Record searched: 125 with zero.ray|zero.tail|first.failure|termination
->2 endpoint-mask hits1file; GC1170/1184, GC1197/98 and L682/683 read.
No solver, record maximization, exact membership or Local witness-field replay.
Y1 MUST: zero-ray prefix agrees with the published witness trace at
all its 145 supplied ticks; integer and literal lookup evolution agree.
Y2 BLIND (.5): the zero ray first fails the black clock at tick146;
report the actual first clock failure and first certified phase1 cut,
consuming white samples only while earlier clock tests passed.
Y3 MUST: toggling only depth146 leaves ticks0..144 fixed and flips145;
toggling only147 leaves0..145 fixed and flips146. The four boundary
packets must separate the next free visible sample from the next clock.
CF: the finite band ending145 fixes the observation at145 too; Y3
must refute this. Unexpected: a clock failure of the all-zero tail at
146 is not an exclusion of all extensions of the length22 band;
its outside-band depth147 may repair that clock. Report this explicitly.
INSTRUMENT REPAIR after first control failure, 19:55 BST: fixture trace
is the RIGHT trace, not the LEFT neighbour trace. Comparing it directly
failed Y1 before any verdict output. Convert it by left=1 at black
ticks, left=1-right at white ticks (G25); no input or blind prediction
changed. Retain this failed instrument check. A second check caught
the fixture's raw trace having146 samples, including the unused final
white sample at145: compare only the originally promised0..144.
Stop: one fixture, four boundary packets, ticks0..200 inclusive;
retain OPEN at the cap, no widening or right-language oracle.
OUTCOME (2026-10-13 19:57 BST, Intel CPU, below1s): Y1/Y3 PASS
after the two retained fixture-schema repairs. Y2 HELD: the zero
ray's first black-clock failure is146. However its first certified
phase1 cut occurs earlier, at145: the38-bit word
00100100001000010000100001000010000101. Both packets with depth146=0
produce this cut regardless of147; packets with146=1 have no listed
cut before their first clock failure. Zero147 gives clock failure146;
one147 repairs146 and gives first failure150 (for either146 value).
Thus the first cut is an all-tail endpoint guard for this fixed prefix,
while the zero-ray clock failure alone is not. No cap widening ran.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
TABLE=(0,1,1,1,1,0,0,0)

def integer_trace(row,p,cap):
    n=sum(v<<j for j,v in enumerate(row));out=[]
    for t in range(cap+1):
        out.append(n&1)
        n=(n>>1) ^ (n | ((n<<1)|((t+p)&1)))
    return out

def literal_trace(row,p,cap):
    row=list(row)+[0]*(cap+3);out=[]
    for t in range(cap+1):
        out.append(row[0]);x=[(t+p)&1]+row+[0]
        row=[TABLE[4*x[j+1]+2*x[j]+x[j-1]] for j in range(1,len(x)-1)]
    return out

def cuts(p):
    phase=None;out=[]
    for line in (ROOT/'tests/probes/lexicon/rule30_local_mfw44.txt').read_text().splitlines():
        if line.startswith('## phase '):phase=int(line.split()[2].rstrip(':'))
        elif line and set(line)<={'0','1'} and phase==p:out.append(line)
    return out

def verdict(x,p,words):
    vis='';first_cut=None;clock=None
    for t,b in enumerate(x):
        if (t+p)&1:
            if b!=1:clock=t;break
        else:
            vis+=str(1-b)
            if first_cut is None:
                hit=next((w for w in words if vis.endswith(w)),None)
                if hit:first_cut=(t,hit)
    return {'clock':clock,'cut':first_cut,'last_legal_tick':len(x)-1 if clock is None else clock-1}

def main():
    w=next(r for r in json.loads((ROOT/'site/wolframcollatzmahler/data/records.json').read_text())['rows'] if r['depth']==125)
    p=w['phase'];cap=200
    row=list(map(int,w['left'][:124]))+[0]*(cap+3-124)
    xs={}
    for a,b in ((0,0),(0,1),(1,0),(1,1)):
        y=row.copy();y[145]=a;y[146]=b
        x=integer_trace(y,p,cap);assert x==literal_trace(y,p,cap)
        expected=[1 if (t+p)&1 else 1-int(v) for t,v in enumerate(w['trace'])]
        assert x[:145]==expected[:145];xs[a,b]=x
    assert xs[0,0][:145]==xs[1,0][:145] and xs[0,0][145]!=xs[1,0][145]
    assert xs[0,0][:146]==xs[0,1][:146] and xs[0,0][146]!=xs[0,1][146]
    print('Y1 integer versus literal and supplied horizon PASS; Y3 two boundary pivots PASS')
    for key,x in xs.items():
        v=verdict(x,p,cuts(p));v['ticks145..148']=''.join(map(str,x[145:149]));print(key,v)
    print('Y2 predicted first zero-ray clock failure146:',xs[0,0][146]!=1)
    print('Unexpected boundary repair at146:',xs[0,0][146],xs[0,1][146])

if __name__=='__main__':main()
