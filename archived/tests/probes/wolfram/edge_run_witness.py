#!/usr/bin/env python3
"""GC2154 fixed256-tick extraction, j14..18, seed1. See edge-density account.
P before run: >=2 filled white runs and root coefficients[0,0,1]. CF: <=1 or mismatch.
Unexpected: retain individual run-factor orders; do not assume minimum1.
Known R_step/run mechanism + original1b82d8 geometric_exact, not a new valuation theorem.
No period search, expanded horizon or automatic retry. Independent polynomial long division.
"""
import json

H=256

def order(p):
    if not p:
        return H
    n=0
    while p.bit_count()%2==0:
        q,r=0,p
        while r.bit_length()>1:
            d=r.bit_length()-2
            q^=1<<d
            r^=3<<d
        assert r==0
        p=q
        n+=1
    return n

def root_coeff(p,k):
    return sum((p>>t)&1 for t in range(H) if t&k==k)%2

def main():
    streams={j:[] for j in range(14,19)}
    x,row=1,{0:1}
    for t in range(H+1):
        physical=sum(v<<(t-p) for p,v in row.items())
        assert physical&((1<<19)-1)==x
        for j in streams:
            streams[j].append((x>>j)&1)
        if t<H:
            x=(x ^ ((x<<1)|(x<<2)))&((1<<19)-1)
            row={p:row.get(p-1,0) ^ (row.get(p,0)|row.get(p+1,0))
                 for p in range(-t-1,t+2)}
    for a in streams.values():
        assert a[H]==a[0]
    for j in range(16,19):
        assert all(streams[j][t+1]^streams[j][t] ==
                   (streams[j-1][t]|streams[j-2][t]) for t in range(H))
    s,b,h=[streams[j] for j in [16,17,18]]
    g=[s[t]|b[t] for t in range(H)]
    assert s[0]==0 and s[H-1]==1
    filled=[]
    t=0
    while t<H:
        if s[t]:
            t+=1
            continue
        a=t
        while t<H and s[t]==0:
            t+=1
        length=t-a
        assert all(b[u]==b[a] for u in range(a,t))
        if b[a]:
            factor=((1<<length)-1)<<a
            expected=(length&-length)-1
            assert order(factor)==expected
            filled.append({'start':a,'length':length,'factor_order':expected,
                           'root_coefficients':[root_coeff(factor,k) for k in range(3)]})
    poly=lambda a:sum(v<<t for t,v in enumerate(a[:H]))
    ps,pg,ph=poly(s),poly(g),poly(h)
    reconstructed=ps
    for r in filled:
        reconstructed^=((1<<r['length'])-1)<<r['start']
    assert reconstructed==pg
    assert [order(ps),order(pg),order(ph)]==[127,2,1]
    coeff=[root_coeff(pg,k) for k in range(3)]
    assert coeff==[0,0,1] and len(filled)>=2
    minimum=min(r['factor_order'] for r in filled)
    print(json.dumps({'bounds':{'H':H,'diagonals':list(streams),'seed':1},
        'controls':{'physical_rows':H+1,'three_gate_equations':True,'cycle_closure':True,
                    'whole_white_run_constancy':True,'polynomial_identity':True,
                    'long_division_orders':[127,2,1]},
        'prediction_held':True,'forcing_root_coefficients':coeff,'filled_runs':filled,
        'minimum_individual_factor_order':minimum,
        'minimum_order_term_count':sum(r['factor_order']==minimum for r in filled),
        'time_words':{str(j):''.join(map(str,a[:H])) for j,a in streams.items()}},indent=2))

if __name__=='__main__':
    main()
