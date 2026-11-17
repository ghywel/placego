"""GC487 fixed binary-decimation signatures; not an automaticity test verdict.
Scope D=4, M=32, signatures a(2^d*n+r), n1..32, d0..4, r<2^d.
C0 MUST: decimal-set and integer Rule30 agree through max sampled index527.
C1 MUST: Thue-Morse signatures have exactly2 values; all supplied unequal
         signatures carry an actual differing positive index.
P1 BLIND: all31 Rule30 signatures are distinct at this fixed scope.
CF: finite distinct signatures prove an infinite kernel; reject by a finite-prefix
    extension that agrees on every sampled bit and is zero afterwards (automatic).
Unexpected: n>=1 avoids canonical-binary leading-zero ambiguity; output at n0
            is deliberately not used to distinguish machine states.
REFUTED-BY: control failure or any Rule30 signature collision.
No deeper kernel census, fitted growth rate, or general computation lower bound.
"""
from rule30_gpt_selected_potential import decimal_set_step

def signatures(a):
    return {(d,r):tuple(a((1<<d)*n+r) for n in range(1,33))
            for d in range(5) for r in range(1<<d)}
if __name__=='__main__':
    tm=signatures(lambda n:n.bit_count()&1);assert len(set(tm.values()))==2
    T=527;off=T+2;mask=(1<<(2*off+1))-1;row=1<<off;cells={0};bits=[]
    for t in range(T+1):
        assert {i-off for i in range(2*off+1) if row>>i&1}==cells
        bits.append((row>>off)&1)
        if t<T:row=((row<<1)^(row|(row>>1)))&mask;cells=decimal_set_step(cells)
    sig=signatures(lambda n:bits[n]);assert len(set(sig.values()))==31
    witnesses=[];items=list(sig.items())
    for i,(u,su) in enumerate(items):
        for v,sv in items[:i]:
            n=next(n for n in range(1,33) if su[n-1]!=sv[n-1])
            assert bits[(1<<u[0])*n+u[1]]!=bits[(1<<v[0])*n+v[1]]
            witnesses.append((u,v,n))
    finite=lambda n:bits[n] if n<len(bits) else 0
    assert signatures(finite)==sig and all(finite(n)==0 for n in (528,1024,1000000))
    print('Rule30 distinct',len(set(sig.values())),'Thue-Morse distinct',len(set(tm.values())))
    print('PASS528 independent rows;',len(witnesses),'positive-index distinguishing certificates; max witness n',max(w[2] for w in witnesses))
    print('All signatures',[(k,''.join(map(str,v))) for k,v in sig.items()])
    print('Finite zero-tail extension matches all samples; infinite-kernel CF inference rejected')
