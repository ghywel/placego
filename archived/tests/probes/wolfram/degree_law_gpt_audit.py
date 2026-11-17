#!/usr/bin/env python3
"""GC2031: bounded independent symbolic audit of L1072. No NumPy/Mobius truth transform.
Boolean polynomials are sets of variable masks, XOR is symmetric difference,
product is mask union with parity cancellation (x_i^2=x_i).
Frozen: full iterates t<=6; z-frame identities m<=6; literal-rule controls t<=4;
Rules90/150 remain linear. No scope expansion or automatic rerun.
"""
import hashlib,json,os
from pathlib import Path
Z=frozenset();ONE=frozenset((0,))
def var(i):return frozenset((1<<i,))
def mul(a,b):
    out=set()
    for x in a:
        for y in b:
            q=x|y
            if q in out:out.remove(q)
            else:out.add(q)
    return frozenset(out)
def r30(a,b,c):return a^b^c^mul(b,c)
def step(row,rule=30):
    return [(r30(a,b,c) if rule==30 else a^c if rule==90 else a^b^c)
            for a,b,c in zip(row,row[1:],row[2:])]
def value(poly,bits):return sum((mask&bits)==mask for mask in poly)%2
def literal(rule,t,bits):
    row=[bits>>j&1 for j in range(2*t+1)]
    for _ in range(t):row=[rule>>(4*a+2*b+c)&1 for a,b,c in zip(row,row[1:],row[2:])]
    return row[0]
def dz(poly,j):return frozenset(mask^(1<<j) for mask in poly if mask>>j&1)
def zstep(row):
    return [Z]+[row[j+2]^row[j+1]^row[j]^mul(row[j+1],row[j]) for j in range(1,len(row)-2)]+[Z,Z]
def zhistory(row,k):
    h=[row]
    for _ in range(k):h.append(zstep(h[-1]))
    return h
def system(m):
    row=[Z for _ in range(4*m+5)]
    for i in range(m):row[2*i+1]=var(i)
    # Solve each pivot symbolically, once: its coefficient in the constraint is1.
    for k in range(m-1):
        h=zhistory(row,k);row[2*k+2]=h[-1][1]^h[-1][2]
        h=zhistory(row,k);assert h[-1][1]==h[-1][2]
    return row,zhistory(row,m-1)
def main():
    rows=[];controls=0
    for t in range(1,7):
        h=[[var(i) for i in range(2*t+1)]]
        for _ in range(t):h.append(step(h[-1]))
        f=h[-1][0];deg=max(q.bit_count() for q in f);tops=sorted(q for q in f if q.bit_count()==deg)
        want=2 if t==1 else 2*t-1
        assert deg==want
        if t>=3:assert tops==[((1<<(2*t+1))-1)^3]
        if t==2:assert tops==[26,28]
        prod=ONE
        # At time k row index j represents global coordinate -t+k+j.
        for k in range(t):prod=mul(prod,ONE^h[k][2*t-1-2*k])
        assert dz(f,2*t)==prod
        if t<=4:
            for bits in range(1<<(2*t+1)):
                assert value(f,bits)==literal(30,t,bits);controls+=1
        rows.append({'t':t,'degree':deg,'terms':len(f),'top_missing':[[j-t for j in range(2*t+1) if not(q>>j&1)] for q in tops]})
    for rule in (90,150):
        for t in range(1,7):
            row=[var(i) for i in range(2*t+1)]
            for _ in range(t):row=step(row,rule)
            assert max(q.bit_count() for q in row[0])==1
    zchecks=0
    for m in range(1,7):
        row,h=system(m);phi=h[m-1][1]^h[m-1][2]
        W={k:h[k][2*m-2*k] for k in range(1,m)}
        assert ((1<<m)-1) in phi
        assert all(((1<<m)-1) in w for w in W.values())
        if m==1:assert phi==var(0);continue
        sr,sh=system(m-1);P=sh[m-2][1]^sh[m-2][2]
        assert row[2*m-2]==P
        Ws={i:sh[i][2*(m-1)-2*i] for i in range(1,m-1)}
        rhs=(ONE if m%2 else Z)^(P if (m-1)%2 else Z)
        for w in Ws.values():rhs^=w
        assert dz(phi,m-1)==rhs;zchecks+=1
        for k,w in W.items():
            rhs=(ONE if k%2 else Z)^(P if k%2 else Z)
            for i in range(1,k):rhs^=Ws[i]
            assert dz(w,m-1)==rhs;zchecks+=1
    result={'status':'PASS','full_iterates':rows,'literal_cases':controls,'z_recursion_identities':zchecks,
            'linear_controls':'Rules90/150 t1..6','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
