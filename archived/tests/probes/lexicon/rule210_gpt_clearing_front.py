"""GC478 candidate clearing-front proof controls, not the proof itself.
P1: stronger odd and even settling by tau+j+1 on GC477 abstract cases.
C0: pair occupancy R=(1-P)Q has Rnext=(1-U)*(B XOR R).
C1: inductively constructed clearing witness t_j<=tau+j has P_j(t_j)=1,
R_j=0 from t_j to T_j-1 and pair01 at T_j=tau+j+1.
CF0: omit clearing, an incoming01 need not produce an outgoing01.
Unexpected: first failing background gate also has the candidate01 front.
REFUTED-BY: any identity, witness or sharper-settling mismatch.
OUTCOME:16 pair identities,10880 abstract cases and40064 front witnesses PASS;
omitted-clearing CF rejected. Candidate proof is in RULE30-GPT GC478.
"""
from rule210_gpt_abstract_pulse import orbit

def scalar(l,c,r):return (210>>(4*l+2*c+r))&1
if __name__=='__main__':
    local=0
    for U in (0,1):
        for B in (0,1):
            for P in (0,1):
                for Q in (0,1):
                    pp=scalar(U,B,P);qq=scalar(B,P,Q)
                    assert (1-pp)*qq==(1-U)*(B^((1-P)*Q));local+=1
    assert (scalar(0,1,0),scalar(1,0,1))==(0,0)
    cases=fronts=0
    for tau in range(4):
        for w in range(4):
            for post in range(16):
                for bits in range(1<<(2*w+1)):
                    Y,X=orbit(tau,w,post,bits);t=tau
                    for j in range(w+1):
                        if j and X[t][2*j]==0:t+=1
                        T=tau+j+1
                        assert t<=tau+j and X[t][2*j]==1
                        assert all((1-X[s][2*j])*X[s][2*j+1]==0 for s in range(t,T))
                        assert (X[T][2*j],X[T][2*j+1])==(0,1)
                        for s in range(T,len(Y)):
                            assert X[s][2*j]==0
                            assert (X[s][2*j+1]^Y[s][2*j+1])==Y[0][2*j+1]
                        fronts+=1
                    cases+=1
    print('PASS',local,'pair identities;',cases,'abstract cases;',fronts,
          'clearing-front witnesses; omitted-clearing CF rejected')
