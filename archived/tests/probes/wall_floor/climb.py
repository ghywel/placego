#!/usr/bin/env python3
"""climb.py (Local, L1542): the climb of a deviation through a strip, from the rule of L1542. strips: one word per phase by offset, in backward-tick order; going back, the phase steps down. Cells '?' are not strip cells. Reports the slowest and fastest climb from the floor to offset 10 with no retreats, and the retreat sites on the slowest path."""
import json,sys
sys.setrecursionlimit(100000)
def load():
    S={}
    a=[''.join('#' if b else '.' for b in v) for v in json.load(open('lock45.json'))]
    S['AB 45']=([a[0][::-1],a[1][::-1]],41)
    b=json.load(open('lock136.json'))
    S['AAB 136']=([b[5][::-1],b[3][::-1],b[1][::-1]],132)
    c=[l.strip()[::-1] for l in open('ref6.txt') if l.strip()]
    S['third 175']=(c,None)
    return S
def options(row,D):
    """allowed rises, and whether a retreat is possible; row by offset"""
    x=lambda k:row[k]=='#'
    if not x(D-1): return [5],False
    if not x(D):
        if not x(D+1): return [4],False
        return [3],True
    if x(D+1) or x(D+2): return [4,3],False
    return [4],True
for name,(rows,c) in load().items():
    P=len(rows)
    maxD=min(len(r) for r in rows)-4
    memo={}
    def T(ph,D,mode):
        if D<=10: return 0
        key=(ph,D,mode)
        if key in memo: return memo[key]
        if any(rows[ph][k]=='?' for k in range(D-1,D+3)):
            memo[key]=None; return None
        rs,ret=options(rows[ph],D)
        vals=[]
        for r in rs:
            v=T((ph-1)%P,D-r,mode)
            if v is not None: vals.append(1+v)
        memo[key]=(max if mode=='slow' else min)(vals) if vals else None
        return memo[key]
    # first offset with strip cells around it in every phase
    starts=[]
    for ph in range(P):
        for D in range(maxD,10,-1):
            if all(rows[ph][k]!='?' for k in range(D-1,D+3)):
                starts.append((ph,D)); break
    res=[(ph,D,T(ph,D,'slow'),T(ph,D,'fast')) for ph,D in starts]
    # retreat sites by offset
    sites=sum(1 for ph in range(P) for D in range(11,maxD) if all(rows[ph][k]!='?' for k in range(D-1,D+3)) and options(rows[ph],D)[1])
    white=sum(rows[ph][k]=='.' for ph in range(P) for k in range(11,maxD))/(P*(maxD-11))
    print(name,'phase, start offset, slowest, fastest:',res,'| retreat sites',sites,'of',P*(maxD-11),'| white cells',round(white,3))
