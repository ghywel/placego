#!/usr/bin/env python3
"""One physical E A^4 E A^7 E history, with shared cone rows and checked UP.

No window growth or SAT-budget adaptation. Original CNF, reduction trace and
seams are exported. UNSAT without a proof checker remains uncertified.
"""
import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path
from pysat.solvers import Cadical195

A,E='25','33535555'


def raw_fibres(root):
    out={}
    for W in (38,39,40,41):
        path=root/'dfa2'/f'dfa_xx_W{W}_c0.txt';T={};sizes={}
        for line in path.read_text().splitlines():
            p=line.split();q=int(p[0]);sizes[q]=int(p[1])
            T[q]={int(a):int(b) for a,b in (x.split(':') for x in p[2:])}
        def step(q,w):
            for c in w:q=T.get(q,{}).get(int(c),-1)
            return q
        initial=step(0,E);raw={initial};todo=[initial]
        while todo:
            q=todo.pop();seen=set()
            while q not in seen:
                seen.add(q);v=step(q,E)
                if v>=0 and v not in raw:raw.add(v);todo.append(v)
                q=step(q,A)
        chain=[];q=initial
        while q not in [x['state'] for x in chain]:
            assert q>=0
            chain.append({'state':q,'size':sizes[q]})
            q=step(q,A*4+E+A*7+E)
        order=sorted(raw);v=tuple(order);seen={};values=[]
        while v not in seen:
            seen[v]=len(values);images=[step(q,E) for q in v]
            values.append(images);v=tuple(step(q,A) for q in v)
            assert len(values)<10000
        out[W]={'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                'initial':initial,'raw_order':order,'sizes':{q:sizes[q] for q in order},
                'cycle_chain':chain,'cycle_returns_to':q,
                'unary_mu':seen[v],'unary_period':len(values)-seen[v],
                'unary_images':values,
                'total_raw_resets':[n for n,im in enumerate(values)
                                    if im[0]>=0 and len(set(im))==1]}
    return out


def gate(a,b,c,d):
    # d = a XOR (b OR c), six prime clauses; signed inputs permitted.
    return [[-b,a,d],[-b,-a,-d],[-c,a,d],[-c,-a,-d],
            [b,c,-a,d],[b,c,a,-d]]


def generate(H,wanted,fixed=None):
    W=H+1;off=[1]
    for t in range(H+1):off.append(off[-1]+W-t)
    def v(t,x):return off[t]+x
    C=[[1]] # true constant, boundary is +/-1
    for t in range(H):
        for x in range(1,W-t):
            left=v(t,x-1) if x>1 else (1 if t%2==0 else -1)
            for clause in gate(left,v(t,x),v(t,x+1),v(t+1,x)):
                c=list(dict.fromkeys(clause))
                if not any(-a in c for a in c):C.append(c)
    C += [[v(t,1) if bit else -v(t,1)] for t,bit in sorted(wanted.items())]
    if fixed is not None:
        C += [[v(0,x) if (fixed>>(x-1))&1 else -v(0,x)] for x in range(1,W+1)]
    return C,off,W


def propagate(C):
    occur=collections.defaultdict(list);count=[];xor=[]
    for i,c in enumerate(C):
        count.append(len(c));x=0
        for a in c:occur[a].append(i);x^=a
        xor.append(x)
    sat=bytearray(len(C));vals={};log=[]
    todo=collections.deque((c[0],i) for i,c in enumerate(C) if len(c)==1)
    while todo:
        a,reason=todo.popleft();var=abs(a);value=a>0
        if var in vals:
            if vals[var]!=value:return vals,log,reason
            continue
        vals[var]=value;log.append([a,reason])
        for i in occur[a]:sat[i]=1
        for i in occur[-a]:
            if sat[i]:continue
            count[i]-=1;xor[i]^=-a
            if count[i]==0:return vals,log,i
            if count[i]==1:todo.append((xor[i],i))
    return vals,log,None


def replay_units(C,log,conflict):
    vals={}
    for a,i in log:
        assert a in C[i] and abs(a) not in vals
        for b in C[i]:
            if b!=a:assert abs(b) in vals and vals[abs(b)]!=(b>0)
        vals[abs(a)]=a>0
    if conflict is not None:
        assert all(abs(b) in vals and vals[abs(b)]!=(b>0) for b in C[conflict])
    return vals


def reduced(C,vals):
    D=[];names={}
    for c in C:
        if any(abs(a) in vals and vals[abs(a)]==(a>0) for a in c):continue
        d=[]
        for a in c:
            if abs(a) not in vals:
                j=names.setdefault(abs(a),len(names)+1);d.append(j if a>0 else -j)
        assert d
        D.append(d)
    return D,names


def dimacs(path,C,N):
    with path.open('w') as f:
        f.write(f'p cnf {N} {len(C)}\n')
        for c in C:f.write(' '.join(map(str,c))+' 0\n')
    assert path.stat().st_size<16*1024*1024
    return {'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}


def bit_rows(R,H):
    rows=[R]
    for t in range(H):R=((R<<1)|(t%2==0))^(R|(R>>1));rows.append(R)
    return rows


def scalar_rows(R,H,W):
    row=[bool((R>>(x-1))&1) for x in range(1,W+H+4)];out=[]
    for t in range(H+1):
        out.append(sum(int(v)<<x for x,v in enumerate(row)))
        row=[((t%2==0) if x==0 else row[x-1]) !=
             (row[x] or (row[x+1] if x+1<len(row) else False)) for x in range(len(row))]
    return out


def controls():
    for a,b,c,d in itertools.product((0,1),repeat=4):
        vals={1:a,2:b,3:c,4:d}
        ok=all(any(bool(vals[abs(l)])==(l>0) for l in cl) for cl in gate(1,2,3,4))
        assert ok==(d==(a^(b|c)))
    R,H=19,17;rows=bit_rows(R,H);assert rows==scalar_rows(R,H,H+1)
    wanted={t:bool(rows[t]&1) for t in range(1,H+1,2)}
    C,off,W=generate(H,wanted,R);vals,log,conf=propagate(C)
    assert conf is None and replay_units(C,log,conf)==vals
    with Cadical195(bootstrap_with=C) as solver:assert solver.solve()
    wanted[1]=not wanted[1]
    C,off,W=generate(H,wanted,R);vals,log,conf=propagate(C)
    assert conf is not None and replay_units(C,log,conf)==vals
    corrupt=[x[:] for x in log];corrupt[0][0]*=-1
    try:replay_units(C,corrupt,conf)
    except AssertionError:pass
    else:raise AssertionError('corrupt unit accepted')
    return {'truth_table':True,'phase_and_rows':True,'fixed_good':True,
            'fixed_wrong_bit_rejected':True,'corrupt_unit_rejected':True}


def main():
    p=argparse.ArgumentParser();p.add_argument('--packet',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    out={'controls':controls(),'raw_fibres':raw_fibres(a.packet)}
    (a.out/'fibres.json').write_text(json.dumps(out,indent=2)+'\n')
    gaps=E+A*4+E+A*7+E;black={0};s=0
    for g in gaps:s+=int(g);black.add(s)
    H=1+2*s;assert H==359
    wanted={1+2*j:j in black for j in range(s+1)}
    C,off,W=generate(H,wanted);N=off[-1]
    original=dimacs(a.out/'original.cnf',C,N)
    vals,log,conf=propagate(C);assert replay_units(C,log,conf)==vals
    (a.out/'unit-log.json').write_text(json.dumps({'log':log,'conflict':conf})+'\n')
    assert conf is None,'target unit contradiction: preserve evidence and stop before solve'
    D,names=reduced(C,vals);reduction=dimacs(a.out/'reduced.cnf',D,len(names))
    (a.out/'variable-map.json').write_text(json.dumps(names)+'\n')
    def seam(t):
        return {'tick':t,'cells':W-t,'forced':{x:int(vals[off[t]+x]) for x in range(1,W-t+1)
                   if off[t]+x in vals},'free':[x for x in range(1,W-t+1) if off[t]+x not in vals]}
    seams=[seam(t) for t in (1,69,193,359)]
    # Every target black after the first must carry the known prior corridor.
    corridors=[]
    for j in sorted(black-{0}):
        t=2*j-1
        assert all(vals.get(off[t]+x) is False for x in (1,2,3))
        corridors.append(t)
    r={'gap_word':gaps,'physical_horizon':H,'root_width':W,'original_variables':N,
       'original_clauses':len(C),'reduced_variables':len(names),'reduced_clauses':len(D),
       'forced_variables':len(vals),'original':original,'reduced':reduction,
       'seams':seams,'checked_corridor_ticks':corridors,'propagation_replay':True}
    print(json.dumps({'before_solve':{k:v for k,v in r.items() if k!='seams'},
                      'seam_counts':[(x['tick'],x['cells'],len(x['forced'])) for x in seams]}),flush=True)
    (a.out/'before-solve.json').write_text(json.dumps(r,indent=2)+'\n')
    with Cadical195(bootstrap_with=D) as S:
        S.conf_budget(60000);answer=S.solve_limited()
        r['answer']='SAT' if answer is True else 'UNSAT_UNCERTIFIED' if answer is False else 'UNKNOWN'
        r['stats']=S.accum_stats()
        if answer is True:
            model=set(S.get_model());v=dict(vals)
            v.update({old:new in model for old,new in names.items()})
            assert all(any(v.get(abs(l),False)==(l>0) for l in c) for c in C)
            R=sum(1<<(x-1) for x in range(1,W+1) if v.get(off[0]+x,False))
            rows=bit_rows(R,H);assert rows==scalar_rows(R,H,W)
            assert all(bool(rows[t]&1)==b for t,b in wanted.items())
            for t in range(H+1):
                assert all(bool((rows[t]>>(x-1))&1)==v.get(off[t]+x,False)
                           for x in range(1,W-t+1))
            r['witness']={'root_hex':hex(R),'root_bits':R.bit_length(),
                          'full_rows_at_seams':{t:hex(rows[t]) for t in (1,69,193,359)},
                          'original_CNF_replay':True,'scalar_replay':True,'bit_replay':True}
    (a.out/'physical.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({'answer':r['answer'],'stats':r['stats'],'witness':r.get('witness')}),flush=True)


if __name__=='__main__':main()
