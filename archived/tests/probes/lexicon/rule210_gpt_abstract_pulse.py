"""GC477 abstract diagonal-circuit induction guard, not actual orbit census.
P1: odd deviation equals initial background gate from tau+1+2j onwards.
P2: even candidate diagonal 2j is zero from tau+2j onwards.
C0: XOR recurrence matches decimal Rule210 for all 8 triples.
C1: abstract prefixes match32 actual mirrored-background vector controls.
CF0: permanent first even deviation must refute at least one settling claim.
Unexpected: arbitrary post-tau predecessor b histories, not necessarily G65.
REFUTED-BY: any mismatch; retain first witness without weakening P1/P2.
OUTCOME: corrected P1/P2 PASS10880 abstract cases; C0 PASS8,C1 PASS32.
Permanent-pulse CF rejected. First version omitted shared b from diagonal1
left input and gave a false counterexample; corrected and retained in record.
"""

def orbit(tau,w,post,bits,permanent=False):
    n=2*w+1;T=tau+2*w+6
    y=[0]*(n+1);y[n]=1
    x=[1]+[(bits>>(k-1))&1 for k in range(1,n+1)]
    Y=[y];X=[x]
    for s in range(T):
        b=0 if s<tau else (1 if s==tau else ((post>>(s-tau-1))&1 if s<=tau+4 else 0))
        yn=[];xn=[]
        for k in range(n+1):
            yl=(0 if k==0 else b) if k<2 else y[k-2]
            xl=(0 if k==0 else b) if k<2 else x[k-2]
            yc=b if k==0 else y[k-1];xc=b if k==0 else x[k-1]
            yn.append((210>>(4*yl+2*yc+y[k]))&1)
            xn.append((210>>(4*xl+2*xc+x[k]))&1)
        if permanent:xn[0]=1
        y,x=yn,xn;Y.append(y);X.append(x)
    return Y,X

def violations(Y,X,tau,w):
    odd=[];even=[]
    for j in range(w+1):
        k=2*j+1
        for s in range(tau+1+2*j,len(Y)):
            if (X[s][k]^Y[s][k])!=Y[0][k]:odd.append((j,s))
    for j in range(1,w+1):
        for s in range(tau+2*j,len(Y)):
            if X[s][2*j]:even.append((j,s))
    return odd,even

if __name__=='__main__':
    for l in (0,1):
        for c in (0,1):
            for r in (0,1):assert ((210>>(4*l+2*c+r))&1)==(l^((1-c)*r))
    count=odd_bad=even_bad=0;first=None
    for tau in range(4):
        for w in range(4):
            for post in range(16):
                for bits in range(1<<(2*w+1)):
                    Y,X=orbit(tau,w,post,bits)
                    odd,even=violations(Y,X,tau,w)
                    if first is None and (odd or even):first=(tau,w,post,bits,odd[:1],even[:1])
                    odd_bad+=bool(odd);even_bad+=bool(even);count+=1
    Y,X=orbit(0,1,0,0,True);cf=violations(Y,X,0,1)
    assert cf[0] or cf[1]
    from rule210_gpt_first_pulse import run
    causal=0
    for mask in range(16):
        left={-k for j,k in enumerate((1,3,5,7)) if mask>>j&1}
        seed={i for i in range(1,21) if i%6 in (1,5)}
        seed.symmetric_difference_update({-k for k in left});seed|=left
        e=2;y=run(seed,12)
        tau=next(s for s in range(e) if y[s][e-1-s])
        w=0
        while e+1+2*w not in seed:w+=1
        n=2*w+1
        post=sum(y[tau+1+j][e-2-tau-j]<<j for j in range(4))
        for bits in (0,(1<<n)-1):
            altered={i for i in seed if i<e or i>e+n}|{e}
            altered|={e+k for k in range(1,n+1) if bits>>(k-1)&1}
            x=run(altered,tau+5);Y,X=orbit(tau,w,post,bits)
            for s in range(tau+6):
                for k in range(n+1):
                    assert Y[s][k]==y[s][e+k-s]
                    assert X[s][k]==x[s][e+k-s]
            causal+=1
    assert causal==32
    print('actual causal controls',causal)
    print('abstract cases' ,count,'odd failures',odd_bad,'even failures',even_bad,'first mismatch',first,'permanent-pulse CF',cf[0][:1],cf[1][:1])
