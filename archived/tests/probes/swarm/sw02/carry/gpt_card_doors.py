#!/usr/bin/env python3
"""GC2837 fixed controls for cards 25,67,74,75,84,86; no census extension.

Predictions/counterfactuals and source pins are in gpt_card_plan.json and the
card review report. Data go only to CAPPED_OUT. No Wolfram or symbolic oracle.
"""
import contextlib
import io
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(os.environ['CAPPED_OUT'])


def F(n):
    return (n >> 1) ^ (n | (n << 1))


def arithmetic():
    cases = []
    for modulus in (1, 2, 3, 6, 12, 396):
        odd = modulus
        while odd % 2 == 0:
            odd //= 2
        order = 1
        while odd > 1 and pow(2, order, odd) != 1:
            order += 1
        for r in sorted({0, 1 % modulus, modulus - 1}):
            for base in (64, 128):
                k = order * (base // order + 1)
                sparse = sum(1 << (k + 8*order*j) for j in range(odd))
                K = k + 8*order*odd
                dense = (1 << K) * ((1 << K) - 1)
                assert sparse % modulus == dense % modulus == 0
                assert F(r+sparse) == F(r) + 7*sparse//2
                assert F(F(r+sparse)) == F(F(r)) + 25*sparse//4
                assert F(r+dense) == F(r) + 3*(1 << (2*K-1)) + (1 << (K-1))
                assert F(F(r+dense)) == F(F(r)) + 13*(1 << (2*K-2)) + 7*(1 << (K-2))
                cases.append({'m':modulus,'r':r,'k':k,'K':K,
                              'F_limits':[3.5,1.5],'F2_limits':[6.25,3.25]})
    # The automaton's state transition on either input is non-injective.
    action = {0:['b','c','c'],1:['a','a','a']}
    assert all(len(set(v)) < 3 for v in action.values())
    return {'exact_cases':cases,'automaton_state_transitions':action}


def birth_loop():
    profiles=[42,44,52,6,51,29,20,7,53,25,1,57,12,55,21,25,41,12,
              39,58,40,14,43,50,2,51,24,47,42,50,19,24,15,53,17,28,
              23,37,4,39,48,31,21,37,38,48,30,43,34,56,46,11,8,15,
              33,62,42,11,13,33,60,23,5,49,29,22,16,30,3,61,21,22,
              26,3,57,46,10,35,58,44,32,60,6,59]
    def cell(t,p,table=profiles):
        return (table[p%84] >> (t%6)) & 1
    def stencil(t,p,table):
        a,b,c=[cell(t,q,table) for q in (p-1,p,p+1)]
        return cell(t+1,p,table) == ((30 >> (4*a+2*b+c)) & 1)
    assert all(stencil(t,p,profiles) for t in range(6) for p in range(84))
    mutant=profiles.copy(); mutant[0] ^= 1
    assert not all(stencil(t,p,mutant) for t in range(6) for p in range(84))
    answer=[]
    for R in (0,1,4,16):
        a,b=-R-40,R+40
        rows=[{p:cell(0,p) if -R-20<=p<=R+20 else 0 for p in range(a,b+1)}]
        for _ in range(16):
            old=rows[-1]
            rows.append({p:old.get(p-1,0) ^ (old.get(p,0)|old.get(p+1,0))
                         for p in range(a,b+1)})
        assert rows[0][-1]==1
        assert all(rows[t][p]==cell(t,p) for t in range(17) for p in range(-R-1,R+2))
        def observation(t):
            return tuple(rows[t][p] for p in range(-R,R+1)), \
                   tuple(rows[t-4][p] for p in range(-R,R+1)),t%4
        assert observation(4)==observation(16)
        assert all(rows[t][0]==t%2 for t in range(17))
        def mismatch(t): return rows[t][1]^rows[t-4][1]
        assert all(mismatch(t)==0 and mismatch(t+1)==1 for t in (4,10))
        answer.append({'R':R,'same_observation':[4,16],'births':[4,10]})
    return {'stencils':504,'mutation_rejected':True,'finite_cutoffs':answer}


def widening():
    sys.path.insert(0,str(ROOT/'tests/probes/lexicon'))
    import rule30_rrl_boundary as b
    import rule30_rrl_factors as f
    log=io.StringIO()
    with contextlib.redirect_stdout(log):
        b.run()
        f.controls()
        f.trap()
    text=log.getvalue()
    assert '6 boundary-preserving 33-white constructions PASS' in text
    assert 'ZERO TRAP depth 5 exact maximum 3' in text
    return {'log':text,'scope':'same-GPT replay/self-check only'}


def erosion_control():
    # Independent Python reconstruction, separate tuple representation, s<=4.
    result=[]
    for phase in (0,1):
        lo=-48
        rows=[tuple(int((p+phase)%2==0) for p in range(lo,1))]
        for s in range(1,5):
            new=[];hist={}
            for row in rows:
                for a in (0,1):
                    for b in (0,1):
                        x=[0]*len(row)+[a,b]
                        for j in range(len(row)-1,-1,-1):
                            # Enumerate the inverse truth table, not the XOR inverse.
                            answers=[l for l in (0,1) if ((30>>(4*l+2*x[j+1]+x[j+2]))&1)==row[j]]
                            assert len(answers)==1;x[j]=answers[0]
                        e=lo-2
                        for j,v in enumerate(x):
                            p=lo-1+j
                            if v!=int((p+phase)%2==0):break
                            e=p
                        hist[-e]=hist.get(-e,0)+1;new.append(tuple(x))
            rows=new;lo-=1
            result.append([phase,s,len(rows),max(hist),hist[max(hist)]])
    cpp=(OUT/'erosion.stdout').read_text().splitlines()
    actual=[list(map(int,line.split())) for line in cpp if not line.startswith('CARD_')]
    assert result==[row for row in actual if row[1]<=4]
    return {'python_crosschecks':result,'cpp_rows':actual,
            'scope':'exact depths1..9 only; no all-s claim'}


def main():
    result={'arithmetic':arithmetic(),'birth':birth_loop(),
            'widening':widening(),'erosion':erosion_control()}
    (OUT/'card-controls.json').write_text(json.dumps(result,indent=2)+'\n')
    print('CARD_DOORS_FIXED_CONTROLS_PASS')


if __name__=='__main__':main()
