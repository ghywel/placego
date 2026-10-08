"""GC486 bounded generic skip-ahead audit; fixed singleton scope guard.
C0 MUST: ANF truth reconstruction equals literal decimal-rule evolution for all
         inputs in cones t1/2/4 (8/32/512 inputs), Rules30/90/150.
P1 BLIND: Rule30 algebraic degree grows strictly across t1,2,4.
CF: F30 squared equals the same rule applied to parents at distance2; must fail.
Linear controls: Rules90/150 squared equal distance2 dilations of themselves.
Unexpected: leftmost parent enters affinely with coefficient1 for every row,
            but changing it varies the input seed, so this is not a fixed-seed lower bound.
REFUTED-BY: reconstruction mismatch, a failed linear/affinity control, or non-increasing degree.
No conclusion about all algorithms, selected-orbit shortcuts, or unbounded degree.
"""
def f(rule,l,c,r):return (rule>>(4*l+2*c+r))&1
def output(rule,t,mask):
    row=[(mask>>i)&1 for i in range(2*t+1)]
    for _ in range(t):row=[f(rule,*row[i:i+3]) for i in range(len(row)-2)]
    return row[0]
def anf(values,n):
    a=values[:]
    for i in range(n):
        for mask in range(1<<n):
            if mask&(1<<i):a[mask]^=a[mask^(1<<i)]
    return a
if __name__=='__main__':
    degrees={};total=0
    for rule in (30,90,150):
        degrees[rule]=[]
        for t in (1,2,4):
            n=2*t+1;values=[output(rule,t,m) for m in range(1<<n)];a=anf(values,n)
            for m in range(1<<n):
                got=0;s=m
                while True:
                    got^=a[s]
                    if not s:break
                    s=(s-1)&m
                assert got==values[m];total+=1
            assert all(values[m]^values[m^1]==1 for m in range(1<<n))
            degree=max(m.bit_count() for m,b in enumerate(a) if b);degrees[rule].append(degree)
            print('rule',rule,'t',t,'degree',degree,'terms',sum(a))
            if rule==30 and t==2:
                print('Rule30 two-step ANF terms',[[i-2 for i in range(n) if m>>i&1] for m,b in enumerate(a) if b])
                for m in range(32):
                    aa,bb,cc,dd,ee=[(m>>i)&1 for i in range(5)]
                    explicit=aa^dd^ee^(bb*dd)^(cc*dd)^(bb*ee)^(cc*ee)^(dd*ee)^(bb*dd*ee)^(cc*dd*ee)
                    assert explicit==values[m]
        if rule in (90,150):
            assert degrees[rule]==[1,1,1]
            assert all(output(rule,2,m)==f(rule,m&1,(m>>2)&1,(m>>4)&1) for m in range(32))
    mismatches=[m for m in range(32) if output(30,2,m)!=f(30,m&1,(m>>2)&1,(m>>4)&1)]
    assert mismatches and output(30,2,4)==0 and f(30,0,1,0)==1
    assert degrees[30][0]<degrees[30][1]<degrees[30][2]
    print('PASS',total,'truth reconstructions; degrees',degrees,'dilation mismatches',len(mismatches),'singleton CF caught')
