#!/usr/bin/env python3
"""GC1923: small exact observer diagnostic, owner-authorized Intel, no M5 launch.

Population: zero-wall lanes W=8,12,16,20, every free diary of length W/2.
Target: actual physical x(W+1,1), after the free diary. Observe before this target;
compare k=1,2,3,4,6 (k<=W/2) initial near/far cells and oldest/newest diary bits.
Two separate populations: all lanes; lanes passing the even check at time W.
That selection is available at cutoff W, before target W+1. All earlier ticks
are built into each lane. Uniform lane weights, not uniform future-class weights.
Exact observation-class optima are retrospective information diagnostics, NOT
trained predictions, unseen-test scores or efficient algorithms.

Record searched: record_find.py 'alternat.*(merg|wall)|boundary.*inject|wall.*collision'
'predict|forecast|far.edge|conductor'. Read L983-985; L955 and GC1894; GC1899;
GC1901; GC1907; GC1922. L942 asks death, not this next physical odd target.
No novelty claim. Retain all rows and exact ambiguous pair witnesses.

PREDICTIONS frozen before execution:
P1 (blind): in passing-W population, far4 accuracy exceeds newest-diary4 by >=.05
    at BOTH W16 and W20. Counterfactual: merely reordering the information offers
    no such advantage. A miss refutes this specific advantage, not all witnesses.
P2 (blind): far6 is NOT exactly sufficient at W20 in passing-W population.
    One actual equal-feature/opposite-target pair proves failure at that width.
C1: packed Rule30 versus independent literal truth-table evolution, all lanes.
C2: triangular inverse versus forward bit-forcing inverse, all lanes; prefix replay.
C3: complete diary and complete initial row each determine target exactly.
C4: refined observation never increases exact probability error or reduces accuracy.
C5: GC1922 eight-triple accuracy and probability-score table, exact fractions.
C6: replace OR by XOR: two singleton truth tables differ, negative control caught.
U1 unexpected boundary check: half-line merging versus open line. Fixed0, fixed1,
    alternating0/1 each tested on ALL 8-bit starts through time4. Open-line outputs
    must be injective. Hypothesis 'alternating wall forbids any merger' predicted
    FALSE; preserve first exact pair, same future boundary for both histories.
Boundary census is an instrument/analogy control, not survival or new theorem.

CAPS: one process/thread, stdlib, <=1360 lanes, W<=20,horizon21; 256 boundary
starts x4 schedules x4 updates; every output JSON <1MiB; no generated code/files
outside CAPPED_OUT; wrapper CPU30s,wall45s,RSS256MiB,file2MiB,disk8MiB,
launch free+inactive>=2048MiB,floor1024MiB,swap growth<=128MiB. Stop on any
control failure or cap; no retry/scope expansion. Analytical allocation <8MiB
plus Python runtime, no GPU. Supervisor samples RSS/pressure, not system peaks.
"""
import collections, fractions, hashlib, json, os, pathlib, time
F = fractions.Fraction
WIDTHS = (8,12,16,20)
KS = (1,2,3,4,6)

def step(r,b=0):
    return (r >> 1) ^ (r | ((r << 1) | b))

def literal(r,b=0):
    out=0
    for j in range(max(1,r.bit_length()+1)):
        left=(r>>(j+1))&1; center=(r>>j)&1
        right=b if j==0 else (r>>(j-1))&1
        out |= ((30 >> (4*left+2*center+right))&1)<<j
    return out

def inverse(a):
    older=[0]*len(a); col=list(a); row=0
    for j in range(len(a)):
        row |= col[0]<<j
        nxt=[col[t+1] ^ (col[t]|older[t]) for t in range(len(col)-1)]
        older,col=col,nxt
    return row

def inverse_forward(a):
    row=0
    for t,bit in enumerate(a):
        r=row
        for _ in range(t): r=literal(r)
        if (r&1)!=bit: row ^= 1<<t
    return row

def metrics(pairs):
    groups={}; first={}; conflict=None
    for ident,key,y in pairs:
        groups.setdefault(key,[0,0])[y]+=1
        if conflict is None and (key,1-y) in first:
            conflict={'feature':key,'case0':first[(key,1-y)],'case1':ident,
                      'outcome0':1-y,'outcome1':y}
        first.setdefault((key,y),ident)
    n=len(pairs)
    if not n: return {'n':0,'status':'EMPTY'}
    hit=F(sum(max(v) for v in groups.values()),n)
    error=sum((F(a*b,a+b) for a,b in groups.values()),F(0))/n
    pure=sum(sum(v) for v in groups.values() if 0 in v)
    return {'n':n,'classes':len(groups),'accuracy':str(hit),'accuracy_float':float(hit),
            'squared_error':str(error),'squared_error_float':float(error),
            'certain_coverage':str(F(pure,n)),'conflict':conflict}

def main():
    dest=pathlib.Path(os.environ['CAPPED_OUT']); start=time.monotonic()
    controls={}
    triples=[(l,c,r,l^(c|r)) for l in (0,1) for c in (0,1) for r in (0,1)]
    for name,feature,acc,err in [
        ('none',lambda l,c,r:0,F(1,2),F(1,4)),
        ('CR',lambda l,c,r:2*c+r,F(1,2),F(1,4)),
        ('L',lambda l,c,r:l,F(3,4),F(3,16)),
        ('LC',lambda l,c,r:2*l+c,F(3,4),F(1,8)),
        ('LCR',lambda l,c,r:4*l+2*c+r,F(1),F(0))]:
        m=metrics([(i,feature(l,c,r),y) for i,(l,c,r,y) in enumerate(triples)])
        assert F(m['accuracy'])==acc and F(m['squared_error'])==err
    controls['C5']='PASS: five exact probability controls'
    assert any((l^(c|r)) != (l^c^r) for l,c,r,_ in triples)
    controls['C6']='PASS: XOR mutant rejected'
    allrows=[]; records=[]; totals=0
    for w in WIDTHS:
        cases=[]; n=w//2
        for lane in range(1<<n):
            a=[1 if t%2==0 else (lane>>(t//2))&1 for t in range(w)]
            row=inverse(a); assert row==inverse_forward(a)
            r=row; trace=[]
            for t in range(w+2):
                trace.append(r&1)
                if t<=w:
                    nxt=step(r); assert nxt==literal(r); r=nxt
            assert trace[:w]==a
            case={'W':w,'lane':lane,'start':row,'pass_W':trace[w],
                  'target':trace[w+1],'trace':trace}
            cases.append(case); records.append(case); totals+=1
        assert len({c['start'] for c in cases})==len(cases)
        for pop in ('all','passing_W'):
            selected=[c for c in cases if pop=='all' or c['pass_W']]
            for name in ('full_diary','full_start','none'):
                q=metrics([(c['lane'],c['lane'] if name=='full_diary' else c['start'] if name=='full_start' else 0,c['target']) for c in selected])
                if name!='none' and q['n']: assert q['accuracy']=='1'
                allrows.append({'W':w,'population':pop,'observer':name,'k':n if name=='full_diary' else w if name=='full_start' else 0,**q})
            for name in ('near_start','far_start','oldest_diary','newest_diary'):
                prev=None
                for k in KS:
                    if k>n: continue
                    def feature(c):
                        source=c['start'] if 'start' in name else c['lane']
                        shift=w-k if name=='far_start' else n-k if name=='newest_diary' else 0
                        return (source>>shift)&((1<<k)-1)
                    q=metrics([(c['lane'],feature(c),c['target']) for c in selected])
                    if prev and q['n']:
                        assert F(q['accuracy'])>=F(prev['accuracy'])
                        assert F(q['squared_error'])<=F(prev['squared_error'])
                    prev=q
                    allrows.append({'W':w,'population':pop,'observer':name,'k':k,**q})
    controls.update(C1='PASS: all packed/literal physical updates',C2='PASS: two inverses and prefix replay for every lane',C3='PASS: full descriptions exact',C4='PASS: every nested observer refinement')
    boundary=[]
    for name,wall in [('zero',lambda t:0),('one',lambda t:1),('alt0',lambda t:t%2),('alt1',lambda t:1-t%2)]:
        states=list(range(256)); first=None
        for t in range(1,5):
            states=[step(r,wall(t-1)) for r in states]
            for i,r0 in enumerate(range(256)):
                r=r0
                for s in range(t): r=literal(r,wall(s))
                assert r==states[i]
            seen={}
            for i,r in enumerate(states):
                if r in seen and first is None:
                    first={'time':t,'start_a':seen[r],'start_b':i,'common_row':r}
                seen.setdefault(r,i)
            boundary.append({'wall':name,'time':t,'distinct_rows':len(seen),'first_collision':first})
    # Open line: int bits are fixed physical coordinates, room for left growth.
    states=[s<<6 for s in range(256)]
    for t in range(1,5):
        states=[(r<<1) ^ (r | (r>>1)) for r in states]
        assert len(set(states))==256
    assert all(any(q['wall']==name and q['first_collision'] for q in boundary) for name in ('alt0','alt1'))
    controls['U1']='PASS: alternating walls merge, open line injective over named domain'
    def get(w,name,k): return next(r for r in allrows if r['W']==w and r['population']=='passing_W' and r['observer']==name and r['k']==k)
    diffs={str(w):str(F(get(w,'far_start',4)['accuracy'])-F(get(w,'newest_diary',4)['accuracy'])) for w in (16,20)}
    predictions={'P1':{'verdict':'HELD' if all(F(v)>=F(1,20) for v in diffs.values()) else 'REFUTED','accuracy_advantages':diffs},
                 'P2':{'verdict':'HELD' if get(20,'far_start',6)['conflict'] else 'REFUTED','conflict':get(20,'far_start',6)['conflict']}}
    payload={'status':'COMPLETE','controls':controls,'predictions':predictions,'lanes':totals,'rows':allrows,'cases':records,'boundary':boundary,'elapsed_s':time.monotonic()-start,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    raw=json.dumps(payload,indent=2)+'\n'; assert len(raw.encode())<1048576
    (dest/'result.json').write_text(raw)
    print(json.dumps({'status':payload['status'],'controls':controls,'predictions':predictions,'lanes':totals,'rows':len(allrows),'elapsed_s':payload['elapsed_s']}))
if __name__=='__main__': main()
