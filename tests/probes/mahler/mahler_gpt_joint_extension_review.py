#!/usr/bin/env python3
"""GC1250, direct review of Mahler's proposed no-dead-end transfer.
COMMAND: python3 tests/probes/mahler/mahler_gpt_joint_extension_review.py
RUN-ON: Intel CPU, one standard-library process, <10s expected.
Record searched: Mahler AND converse -> GC1249/CL384, Cloud S13's probe.
No Cloud imports, no periodic witness search or census beyond depth9.
PREDICTIONS BEFORE FIRST RUN:
 J1 control: direct windows reproduce2,3,5,8,12,18,27,40,60 at depths1..9.
 J2 control: identity multiplier has no dead ends through parent depth8.
 J3 control: multiplier3 leaves exactly0 and2^(T-1) at depths1..9.
 B blind: e5 has a genuine nonzero joint dead end by parent depth8.
 CF must FAIL: no11 suffices for admissibility;10101 passes no11 but has
 an empty exact window (G51's known countercontrol).
 U unexpected: check and print all four exact child windows at the first
 e5 dead end, including equality or strict reversal of endpoints.
KILL TEST: a checked dead end kills direct no-dead-end transfer: HALT this
mechanism. An all-depth child-existence proof confirms it: ACT. Neither
finite persistence nor failure to find a dead end is such a proof.
INCONCLUSIVE (fixed before run): no dead end by8 and no proof -> HALT this
bounded mechanism line, without asserting the intersection is trivial.
REFUTED-BY: any J failure or CF non-rejection. B failure is retained, not
an instrument failure. Finding a dead end does not disprove a converse.
OUTCOME at registration: NOT RUN; append results and keep predictions.
OUTCOME 2026-10-14 22:16 BST, registered19944bff: J1-J3 PASS. CF rejected
10101 with bounds133/243 >=1/2. B HELD2 dead ends through8, first(T7,r9).
U prints exact child windows: child9 good, product45 bad; child137 bad,
product173 good. TIP HALT direct transfer. Exit0,0.090s. B's source outcome
was learned after writing B but before execution; this is reproduction.
ADDENDUM GC1251, predictions BEFORE execution of 'thirteen' mode:
 P13 blind-to-this-check: at some T<=8 no odd joint prefix survives for13.
 E exact control: even F_e(t) maps bijectively onto F_e(t-1) by3r/2,
 for e1,3,5,13 and t2..8. Identity must retain odd prefixes at every depth.
 U13 unexpected: display full13 residue sets and their minimum valuation,
 so a moving-zero-shadow pattern is checked directly.
 KILL: P13 plus E confirms ACT, develop finite-cutoff proof. E failure kills
 route/HALT. P13 failure with E intact is inconclusive/HALT this bounded
 attempt. No universal conclusion from the inconclusive outcome.
OUTCOME ADDENDUM at registration: NOT RUN.
OUTCOME ADDENDUM 2026-10-14 22:18 BST, registered30c56a34: E PASS28 exact
bijections. Identity retains odds. P13 HELD: first empty odd level7;
F13(6),F13(7) each have11 total members. Minimum nonzero valuation rises
from0 at6 to1 at7 and2 at8. TIP ACT finite-cutoff proof. Exit0,0.040s.
Post hoc certificate lists all13 length7 codes starting1 and avoiding11;
each has an empty input or13-product window. General reduction and finite
certificate filed as G296, awaiting independent review. No extrapolation
from finite persistence or assertion about Mahler's single integers.
"""
from fractions import Fraction as F
from time import perf_counter


def window(r,t):
    lo,hi=F(0),F(1,2)
    slope,offset=F(1),F(0)
    for _ in range(t):
        b=r%2
        r=(3*r+b)//2
        slope=3*slope/2
        offset=(3*offset+b)/2
        lo=max(lo,offset/slope)
        hi=min(hi,(offset+F(1,2))/slope)
    return lo,hi


def code(r,t):
    bits=''
    for _ in range(t):
        b=r%2; bits+=str(b); r=(3*r+b)//2
    return bits


def main():
    start=perf_counter()
    A={t:{r for r in range(1<<t) if (lambda z:z[0]<z[1])(window(r,t))}
       for t in range(1,10)}
    counts=[len(A[t]) for t in range(1,10)]
    assert counts==[2,3,5,8,12,18,27,40,60],counts
    print('J1 PASS',counts)
    assert all(any(c in A[t+1] for c in (r,r+(1<<t)))
               for t in range(1,9) for r in A[t])
    print('J2 PASS identity: every prefix extends through parent depth8')
    assert all({r for r in A[t] if 3*r%(1<<t) in A[t]}=={0,1<<(t-1)}
               for t in range(1,10))
    print('J3 PASS multiplier3: exactly two zero shadows through9')
    w='10101'
    r=next(r for r in range(32) if code(r,5)==w)
    lo,hi=window(r,5)
    assert '11' not in w and lo>=hi
    print('CF rejected no11-only criterion:',w,'residue',r,'bounds',lo,hi)
    found=[]
    for t in range(1,9):
        for r in sorted(A[t]):
            if 5*r%(1<<t) not in A[t]:
                continue
            cs=(r,r+(1<<t))
            if all(c not in A[t+1] or 5*c%(1<<(t+1)) not in A[t+1] for c in cs):
                assert r!=0
                found.append((t,r))
    if found:
        t,r=found[0]
        print('B HELD',len(found),'dead ends through8; first parent depth/residue:',t,r)
        for x in (r,5*r%(1<<t)):
            print('parent',x,'code',code(x,t),'window',window(x,t))
        for c in (r,r+(1<<t)):
            z=5*c%(1<<(t+1))
            wc,wz=window(c,t+1),window(z,t+1)
            assert wc[0]>=wc[1] or wz[0]>=wz[1]
            print('U child',c,'code',code(c,t+1),'window',wc,
                  '; product',z,'code',code(z,t+1),'window',wz)
        print('TIP: HALT direct no-dead-end transfer; intersection converse remains open')
    else:
        print('B FAILED: no dead end through8. TIP: HALT this bounded line, inconclusive')
    print('ALL JOINT-EXTENSION CONTROLS PASS; seconds',round(perf_counter()-start,3))

def thirteen():
    start=perf_counter()
    A={t:{r for r in range(1<<t) if (lambda z:z[0]<z[1])(window(r,t))}
       for t in range(1,9)}
    first=None
    comparisons=0
    for e in (1,3,5,13):
        sets={t:{r for r in A[t] if e*r%(1<<t) in A[t]} for t in range(1,9)}
        for t in range(2,9):
            even={r for r in sets[t] if r%2==0}
            image={3*(r//2)%(1<<(t-1)) for r in even}
            assert image==sets[t-1] and len(even)==len(sets[t-1]),(e,t)
            comparisons+=1
        if e==1:
            assert all(any(r%2 for r in sets[t]) for t in sets)
            print('Identity countercontrol PASS: odd points at every depth')
        if e==13:
            for t in range(1,9):
                odd=sorted(r for r in sets[t] if r%2)
                nz=sorted(r for r in sets[t] if r)
                vmin=min((r&-r).bit_length()-1 for r in nz)
                print('U13 depth',t,'joint',sorted(sets[t]),'odd',odd,'min v2',vmin)
                if not odd and first is None:
                    first=t
    print('E PASS',comparisons,'exact even-prefix bijections')
    if first:
        print('P13 HELD first odd extinction depth',first,'TIP ACT: finite-cutoff proof')
    else:
        print('P13 FAILED odds persist through8; TIP HALT bounded attempt, inconclusive')
    print('ALL THIRTEEN CONTROLS PASS; seconds',round(perf_counter()-start,3))

if __name__=='__main__':
    import sys
    if sys.argv[1:]==['thirteen']:
        thirteen()
    else:
        main()
