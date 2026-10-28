#!/usr/bin/env python3
"""GC2034 fixed finite-completion experiment; no random samples or scope growth."""
import hashlib,itertools,json,os
from pathlib import Path
T=8;W=8;N=2*T
CASES={'even_triangle':'10000001','odd_triangle':'11000001',
       'staircase_rain':'00101011','period_three':'10010010',
       'black_cap':'01111110','irregular_control':'01101001'}
FULL=(1<<(1<<N))-1
TRUTH=(0,1,1,1,1,0,0,0)
def variable(j):
    block=1<<j
    return int.from_bytes(bytes(sum(((a*8+b)>>j&1)<<b for b in range(8)) for a in range((1<<N)//8)),'little')
def scalar(word,tail,t):
    a=list(map(int,word))+[tail>>j&1 for j in range(N)]
    for _ in range(t):a=[TRUTH[4*l+2*c+r] for l,c,r in zip(a,a[1:],a[2:])]
    return a[:W]
def bits(code):return ''.join(str(code>>j&1) for j in range(W))
def analyse(row,t,word):
    masks=[FULL]
    for col in row[:W]:masks=[m & (col if b else FULL^col) for b in (0,1) for m in masks]
    # In this construction appending a variable adds its bit as the most significant bit.
    support=[i for i,m in enumerate(masks) if m]
    known={j:int(v==FULL) for j,v in enumerate(row[:W]) if v in (0,FULL)}
    assert sum(m.bit_count() for m in masks)==1<<N
    checks=0
    for code in support:
        m=masks[code];a=(m&-m).bit_length()-1
        assert scalar(word,a,t)==[code>>j&1 for j in range(W)];checks+=1
    projections={0:{0}}
    minimal=[]
    for k in range(1,5):
        for sites in itertools.combinations(range(W),k):
            mask=sum(1<<j for j in sites);seen={code&mask for code in support};projections[mask]=seen
            if k==1:continue
            for vals in itertools.product((0,1),repeat=k):
                p=sum(v<<j for j,v in zip(sites,vals))
                if p in seen:continue
                if all((p & ~(1<<j)) in projections[mask & ~(1<<j)] for j in sites):
                    minimal.append({'sites':list(sites),'forbidden':''.join(map(str,vals))})
    affine=[]
    for mask in range(1,1<<W):
        if mask.bit_count()<2 or any(mask>>j&1 for j in known):continue
        vals={(mask&code).bit_count()%2 for code in support}
        if len(vals)==1:affine.append({'sites':[j for j in range(W) if mask>>j&1],'xor':next(iter(vals))})
    return {'t':t,'start_x':t,'known':known,'support_count':len(support),
        'independent_box':1<<(W-len(known)), 'support':[bits(i) for i in support],
        'weights':[masks[i].bit_count() for i in support],
        'minimal_forbidden_through4':minimal,'affine_relations':affine,'scalar_witness_checks':checks}
def main():
    vs=[variable(j) for j in range(N)];result=[];literal=0
    for name,word in CASES.items():
        row=[FULL if b=='1' else 0 for b in word]+vs;levels=[]
        for t in range(T+1):
            q=analyse(row,t,word);levels.append(q)
            if t<=3:
                for tail in range(1<<(2*t)):
                    assert scalar(word,tail,t)==[(v>>tail)&1 for v in row[:W]];literal+=1
            if t<T:row=[l^(c|r) for l,c,r in zip(row,row[1:],row[2:])]
        result.append({'name':name,'word':word,'levels':levels})
    # Established correlation-recovery positive control, both values of the transported bit.
    for a,r,s in itertools.product((0,1),repeat=3):
        row=[a,1,0,r,s]
        for _ in range(2):row=[TRUTH[4*l+2*c+r] for l,c,r in zip(row,row[1:],row[2:])]
        assert row==[a]
    # A fully unconstrained initial cone must realize every output word: inverse solve one step.
    for out in range(256):
        for right in range(4):
            row=[0]*10;row[8]=right&1;row[9]=right>>1
            for j in reversed(range(8)):row[j]=(out>>j&1)^(row[j+1]|row[j+2])
            assert [TRUTH[4*l+2*c+r] for l,c,r in zip(row,row[1:],row[2:])]==[out>>j&1 for j in range(8)]
    report={'status':'PASS','width':W,'horizon':T,'right_variables':N,'cases':result,
        'literal_controls':literal,'inverse_controls':1024,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(report,indent=2)+'\n')
    for c in result:
        print(c['name'],c['word'])
        for q in c['levels']:
            print(q['t'], ''.join(str(q['known'].get(j,'?')) for j in range(W)),q['support_count'],q['independent_box'],len(q['minimal_forbidden_through4']),len(q['affine_relations']))
    print('PASS',literal,'literal controls')
if __name__=='__main__':main()
