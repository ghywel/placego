#!/usr/bin/env python3
"""G26 preregistered RC1/RC2/RC3/CF, independent of Local's search.
OUTCOME: RC1 refuted at65; RC2/RC3 pass512 controls and255 Catalan checks.
CF rejects Rule30 clock compatibility.
Expected negative: sixteen visible bits followed by0 fails at depth65.
Unexpected check: Rule210's left-spreading and left-permutivity hypotheses.
"""
from math import comb

def inverse(tau,sigma,N):
    a=tau[:];b=sigma[:];row=[]
    for j in range(N):
        c=[a[t+1]^((1-a[t])&b[t]) for t in range(len(a)-1)]
        row.append(c[0]);b,a=a,c
    return row

def backwards(tau,sigma,N):
    row=[]
    for t in range(N-1,-1,-1):
        x=[tau[t],tau[t+1]^((1-tau[t])&sigma[t])]
        for v in row:x.append(v^((1-x[-1])&x[-2]))
        row=x[1:]
    return row

def visible(n):return 1 if n==0 else (n.bit_length()-1)%2

def main():
    N=512;word='1011000011111111';tau=[t%2 for t in range(N+1)]
    bad=[int(word[t//2]) if t%2==0 and t//2<16 else 0 for t in range(N+1)]
    row=inverse(tau,bad,N);assert row==backwards(tau,bad,N)
    first=next(j+1 for j,x in enumerate(row) if x);assert first==65
    print('RC1 REFUTED: first nonzero depth',first,'two independent inverses agree')
    x=[0]*(N+1);bits=0;pi=[];pi30=[];y=x[:]
    for t in range(N):
        assert all(v==0 for j,v in enumerate(x,1) if (t+j)%2==0)
        assert bits==sum(v<<j for j,v in enumerate(x))
        pi.append(x[0]);pi30.append(y[0]);assert t%2==0 or x[0]==0
        if t%2==0:assert 1-x[0]==visible(t//2)
        ext=[t%2]+x+[0];out=[(210>>(4*ext[j+2]+2*ext[j+1]+ext[j]))&1 for j in range(len(x)-1)]
        linear=[ext[j]^ext[j+2] for j in range(len(x)-1)];assert out==linear
        # bit0 is depth1; neighbour toward wall is the shifted-left term.
        mask=(1<<(len(x)-1))-1
        bits=((bits>>1)^((~bits)&((bits<<1)|(t%2))))&mask
        x=out
        ext30=[t%2]+y+[0];y=[(30>>(4*ext30[j+2]+2*ext30[j+1]+ext30[j]))&1 for j in range(len(y)-1)]
    assert any(pi30[t] for t in range(1,N,2))
    acc=0
    for n in range(1,N//2):
        k=n-1;acc^=(comb(2*k,k)//(k+1))%2
        assert 1-acc==visible(n)
    good=[visible(t//2) if t%2==0 else 0 for t in range(N+1)]
    assert not any(inverse(tau,good,N))
    assert not any(backwards(tau,good,N))
    table=[(210>>k)&1 for k in range(8)]
    assert table[0]==0 and table[1]==1
    assert all(table[k]^table[k+4]==1 for k in range(4))
    print('RC2/RC3 PASS:512 parity/linear/time controls;255 Catalan checks;512 zero-depth inverse controls')
    print('CF REJECTED: Rule30 empty-left clock compatibility fails')
    print('Unexpected hypothesis check PASS: f000=0, f001=1, four left-permutive pairs')

if __name__=='__main__':main()
