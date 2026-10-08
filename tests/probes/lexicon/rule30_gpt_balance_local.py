"""GC483 signed-pair identity and finite-seed obstruction, bounded controls.
P0 MUST: signed non-flipping weight is +1 on000/101, -1 on010/011, zero elsewhere.
P1 MUST: finite truncations of G4's seven-cell cycle match its centre for T=4,8,16,32;
         centre spin sum=-T/2 and signed weight sum=-T/4.
CF0: every nonzero finite seed has |spin sum| <= 1 at every prefix; must fail.
Unexpected: biased prefixes are genuine finite seeds with a black centre, not infinite ring data.
Independent controls: literal decimal rule table vs XOR/OR; ring vs full-line set evolution.
REFUTED-BY: a local identity mismatch, cone mismatch or incorrect specified cycle.
"""
def f(l,c,r):return (30>>(4*l+2*c+r))&1
def evolve(a):
    if not a:return set()
    return {i for i in range(min(a)-1,max(a)+2) if f(int(i-1 in a),int(i in a),int(i+1 in a))}
if __name__=='__main__':
    expected={(0,0,0):1,(1,0,1):1,(0,1,0):-1,(0,1,1):-1}
    for l in (0,1):
        for c in (0,1):
            for r in (0,1):
                nxt=f(l,c,r);assert nxt==(l^(c|r))
                weight=(1-2*c)*int(c==nxt)
                assert weight==expected.get((l,c,r),0)
                assert (1-2*c)+(1-2*nxt)==2*weight
    cycle=[1,67,100,63]
    for a,b in zip(cycle,cycle[1:]+cycle[:1]):
        out=sum(f((a>>((i-1)%7))&1,(a>>i)&1,(a>>((i+1)%7))&1)<<i for i in range(7))
        assert out==b
    for T in (4,8,16,32):
        a={i for i in range(-T,T+1) if i%7==0}; assert 0 in a
        spins=[];weights=[]
        for t in range(T):
            c=int(0 in a);assert c==(cycle[t%4]&1)
            spins.append(1-2*c)
            if t%2==0:
                weights.append((1-2*c)*int(c==f(int(-1 in a),c,int(1 in a))))
            a=evolve(a)
        assert sum(spins)==-T//2 and sum(weights)==-T//4
        print('T',T,'spin sum',sum(spins),'signed pair sum',sum(weights))
    assert abs(sum(spins))>1
    print('PASS:8 local identities,4 ring steps,60 finite-prefix samples; CF refuted; black-centre guard PASS')
