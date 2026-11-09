"""GC2793: quotient/pump certificates and all-length G1 test on the already-saved finite DFAs.
G1 means an INTERNAL 5-run of length >=4 adjacent to an internal run of length1:
contains 3 5^{>=4} 3 5 3 or 3 5 3 5^{>=4} 3. The three width18 basis words are exempt.
No larger window, matrix, word cutoff or physical census is constructed.
"""
import collections,json,sys
from pathlib import Path
src,dst=Path(sys.argv[1]),Path(sys.argv[2]);dst.mkdir(exist_ok=True)
F={'33','3553','3535353'};prefixes={w[:i] for w in F for i in range(len(w)+1)}
patterns=['35555353','35355553'];loops=[5,7]

def walk(tr,w,s=0):
    for a in w:
        s=tr[s][a=='5']
        if s<0:return -1
    return s

def quotient(original,tr):
    relation={0:0};todo=[0]
    for i in todo:
        for k,j in enumerate(original[i]):
            q=tr[relation[i]][k]
            assert (j<0)==(q<0)
            if j>=0:
                if j not in relation:relation[j]=q;todo.append(j)
                else:assert relation[j]==q
    assert len(relation)==len(original)
    return [relation[i] for i in range(len(original))]

def pump(tr,u,v,z):
    if not u or not v or not z:return None
    a,b=walk(tr,u),walk(tr,u[1:])
    if a<0 or b<0 or (walk(tr,v,a),walk(tr,v,b))!=(a,b):return None
    if walk(tr,z,a)>=0 or walk(tr,z[:-1],a)<0 or walk(tr,z,b)<0:return None
    return {'pair':[a,b],'after_cycle':[walk(tr,v,a),walk(tr,v,b)],'terminal_full':-1,'terminal_suffix':walk(tr,z,b)}

def next_monitor(active,c):
    new={(0,0),(1,0)}
    for i,k in active:
        if patterns[i][k]==c:
            if k+1==len(patterns[i]):return None
            new.add((i,k+1))
        if k==loops[i] and c=='5':new.add((i,k))
    return tuple(sorted(new))

def all_g1(tr):
    initial=((0,0),(1,0));states=[];index={};parent=[]
    def add(key,p,c):
        if key not in index:
            assert len(index)<500000,'G1_PRODUCT_CAP';index[key]=len(states);states.append(key);parent.append((p,c))
        return index[key]
    for k,c in enumerate('35'):
        assert tr[0][k]>=0
        add((tr[0][k],0,next_monitor(initial,c),c if c in prefixes else '#'),-1,c)
    for i,(p,s,active,base) in enumerate(states):
        for k,c in enumerate('35'):
            a,b=tr[p][k],tr[s][k];m=next_monitor(active,c)
            if m is None:continue  # G1 already present, so no violating continuation.
            t=base+c;t=t if t in prefixes else '#'
            if a<0 and b>=0 and t not in F:
                w=c;j=i
                while j>=0:j,d=parent[j];w=d+w
                assert walk(tr,w)<0 and walk(tr,w[:-1])>=0 and walk(tr,w[1:])>=0
                return {'holds':False,'counterexample':w,'product_states':len(states)}
            if a>=0:
                assert b>=0
                add((a,b,m,t),i,c)
    return {'holds':True,'product_states':len(states),'all_lengths':True}

summary=[]
for w in [16,18,20,22,24,26,28]:
    original=[list(map(int,l.split())) for l in (src/f'dfa-{w}.txt').read_text().splitlines()]
    tr=json.loads((src/f'min-dfa-{w}.json').read_text());a=json.loads((src/f'analysis-{w}.json').read_text())
    result={'width':w,'quotient_map':quotient(original,tr),'g1':all_g1(tr)}
    b=a['forbidden_basis']
    if b['infinite']:
        cert=pump(tr,b['prefix'],b['cycle'],b['suffix']);assert cert is not None
        assert pump(tr,b['prefix'],'',b['suffix']) is None
        assert pump(tr,b['prefix'],b['cycle'],b['suffix'][:-1]) is None
        result['pump']={**cert,**{k:b[k] for k in ['prefix','cycle','suffix']}}
    r=a['reversal_counterexample']
    if r:assert walk(original,r)<0 and walk(original,r[::-1])>=0
    result['reversal_counterexample']=r
    (dst/f'patterns-{w}.json').write_text(json.dumps(result,indent=2)+'\n')
    summary.append({k:v for k,v in result.items() if k!='quotient_map'})
    print('PATTERN',w,'G1',result['g1'],'pump',result.get('pump'),flush=True)
(dst/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print('S16_PATTERN_CERTIFICATES_PASS',flush=True)
