#!/usr/bin/env python3
"""GC442: fixed width7,T48,t28 G222 allocation, no scan.
EB1 MUST HOLD: class regrouping + literal boundary = literal H pair.
EB2 BLIND: at least one actual same-count00/11 pair is matched.
CF MUST FAIL: dropping unmatched/boundary residual preserves nonzero pair.
Unexpected synthetic multiplicity control: n00=2,n11=3,n01=n10=1.
Independent actual word label from current state modulo4. OUTCOME: NOT RUN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_boundary_loss import threshold


def coefficients(F):
    K=F[0]-2*F[1]+F[2]
    return (3*F[0]-2*F[1]-F[2])/4,(3*F[2]-2*F[1]-F[0])/4,K


def grouped(n,F):
    U,V,K=coefficients(F)
    M=min(n['00'],n['11'])
    curvature=(2*M-n['01']-n['10'])*K/4
    residual=(n['00']-M)*U+(n['11']-M)*V
    direct=n['00']*U+n['11']*V-(n['01']+n['10'])*K/4
    assert direct==curvature+residual
    return M,curvature,residual


def main():
    w,T,t=7,48,28
    rows=states_at(w,T)
    f=backward(T)
    classes=defaultdict(Counter)
    boundary=Fraction()
    details=[]
    for x,a in rows[t]:
        y,b=x,a
        bits=[]
        alive=True
        for k in (t,t+1):
            if not alive:break
            bit=y%2;bits.append(str(bit));b+=bit
            y=(3*y+1)//2 if bit else y//2
            alive=3**b>=2**(k+1)
        literal=(f[t+2][b] if alive else Fraction())-f[t][a]
        if a>=threshold(t+1):
            assert len(bits)==2
            word=''.join(bits)
            assert word=={0:'00',1:'10',2:'01',3:'11'}[x%4]
            classes[a][word]+=1
            F=[f[t+2][a+j] for j in range(3)]
            assert literal==F[int(bits[0])+int(bits[1])]-sum((F[0],2*F[1],F[2]))/4
        else:boundary+=literal
        details.append(dict(count=a,word=''.join(bits),interior=a>=threshold(t+1),alive=alive,delta=str(literal)))
    matched=0;curvature=residual=Fraction();summary=[]
    for a,n in sorted(classes.items()):
        M,C,R=grouped(n,[f[t+2][a+j] for j in range(3)])
        matched+=M;curvature+=C;residual+=R
        summary.append(dict(count=a,words=dict(n),matched=M,curvature=str(C),residual=str(R)))
    literal=sum((f[t+2][a] for _,a in rows[t+2]),Fraction())-sum((f[t][a] for _,a in rows[t]),Fraction())
    assert literal==curvature+residual+boundary
    synthetic=Counter({'00':2,'11':3,'01':1,'10':1})
    assert grouped(synthetic,[Fraction(0),Fraction(1,4),Fraction(1)])==(2,Fraction(1,4),Fraction(5,8))
    print(json.dumps(dict(w=w,T=T,t=t,parents=details,classes=summary,matched=matched,
                          curvature=str(curvature),residual=str(residual),boundary=str(boundary),pair=str(literal),
                          controls='PASS',blind_matching=matched>0,
                          drop_residual_refuted=literal!=curvature),indent=2))


if __name__=='__main__':main()
