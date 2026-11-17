#!/usr/bin/env python3
"""GC2020: extend retained A/B histories left, certify crystals, explain jumps.

No new ancestry choice. Exact left-tail certificate from a four-state block-map
orbit, not a fit to a finite string. See the frozen report for bounds and scope.
"""
import base64
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys

LO, HI, DEPTH, FUTURE = -8192, 320, 512, 64
TRUTH=(0,1,1,1,1,0,0,0)
VIEW_SHA='dad1581eaef43dd20a6b3e6345fd7a99d90aaa1affc788cd540998b5a4811ea6'
RESULT_SHA='1284192f3abeaf27d4321ec48576a5163570a1a2bc304a3a715cfda9b352da6c'


def min_period(v):
    for p in range(1,len(v)+1):
        if len(v)%p==0 and all(v[i]==v[i%p] for i in range(len(v))):return v[:p]
    raise AssertionError


def main():
    folder=Path(sys.argv[1]);out=Path(os.environ['CAPPED_OUT'])
    vb=(folder/'view.json').read_bytes();rb=(folder/'result.json').read_bytes()
    assert hashlib.sha256(vb).hexdigest()==VIEW_SHA
    assert hashlib.sha256(rb).hexdigest()==RESULT_SHA
    old=json.loads(vb);retained=json.loads(rb)
    ob={n:base64.b64decode(old[n]) for n in ('a','b')}
    def oldbit(n,t,x):
        i=x-old['x0'];return (ob[n][(t-old['t0'])*old['stride']+i//8]>>(7-i%8))&1
    width=HI-LO+1
    seed=bytearray(width);seed[-LO]=1
    histories={};certificates={};events={};counts={'overlap':0,'update':0,'background':0,'jump':0}
    for name in ('a','b'):
        rows=[seed]
        cert=[{'depth':0,'left_period':1,'left_pattern':[0],'first_defect':0,'left_end':-1,
               'right_period':1,'right_pattern':[0],'right_first':1,'width':1}]
        jumps=[]
        for d in range(1,DEPTH+1):
            y=rows[-1];prev=cert[-1]
            rp=1 if name=='a' else retained['selected_tail_periods'][d]
            tail=[0] if name=='a' else [oldbit(name,-d,i) for i in range(1,rp+1)]
            row=bytearray(width)
            for x in range(1,HI+1):row[x-LO]=tail[(x-1)%rp]
            for x in range(0,LO-1,-1):
                i=x-LO;row[i]=y[i+1]^(row[i+1]|row[i+2])
            for x in range(old['x0'],old['x0']+old['w']):
                assert row[x-LO]==oldbit(name,-d,x);counts['overlap']+=1
            for i in range(1,width-1):
                assert y[i]==TRUTH[4*row[i-1]+2*row[i]+row[i+1]];counts['update']+=1

            # Parent pair states at q-spaced positions inside the child's
            # certified left ray. Repeated state = exact periodic continuation
            # to minus infinity, since the inverse recurrence is deterministic.
            q=prev['left_period'];anchor=prev['left_end']
            assert anchor-5*q>LO, 'left certificate exceeds frozen window'
            state=(row[anchor-LO],row[anchor+1-LO]);orbit=[];pos=anchor
            while state not in orbit:
                orbit.append(state)
                for x in range(pos,pos-q,-1):
                    c,r=state;state=(prev['left_pattern'][x%q]^(c|r),c)
                pos-=q
                assert state==(row[pos-LO],row[pos+1-LO])
            mu=orbit.index(state);lam=len(orbit)-mu
            period=q*lam;safe=anchor-mu*q
            assert period<=4096 and safe-period>=LO, 'left period/window cap'
            pattern=[None]*period
            for x in range(safe-period+1,safe+1):pattern[x%period]=row[x-LO]
            pattern=min_period(pattern);period=len(pattern)
            for x in range(LO,safe+1):assert row[x-LO]==pattern[x%period]
            first=safe+1
            while first<=HI and row[first-LO]==pattern[first%period]:first+=1
            assert first<=HI and first>LO+128, 'left front not safely visible'
            assert row[first-LO]!=pattern[first%period]
            for x in range(math.lcm(q,period)):
                assert prev['left_pattern'][x%q]==TRUTH[4*pattern[(x-1)%period]+2*pattern[x%period]+pattern[(x+1)%period]]
                counts['background']+=1
            for x in range(1-d,HI+1):assert row[x-LO]==tail[(x-1)%rp]
            assert row[-d-LO]!=tail[(-d-1)%rp]

            J=prev['first_defect']-first
            assert J>=-1
            erased={'masked':0,'cancelled':0,'already_equal':0}
            # Exact discrepancy equation through the first surviving output.
            for x in range(first-1,prev['first_defect']+1):
                dl=row[x-1-LO]^pattern[(x-1)%period]
                dc=row[x-LO]^pattern[x%period]
                dr=row[x+1-LO]^pattern[(x+1)%period]
                do=(row[x-LO]|row[x+1-LO])^(pattern[x%period]|pattern[(x+1)%period])
                actual=y[x-LO]^prev['left_pattern'][x%q]
                assert actual==dl^do
                if x<prev['first_defect']:
                    assert actual==0
                    key='cancelled' if dl else ('masked' if dc or dr else 'already_equal')
                    erased[key]+=1
                else:assert actual==1
                counts['jump']+=1
            assert sum(erased.values())==J+1
            if J==-1:assert pattern[(first-1)%period]==0
            if J>=0:assert pattern[(first-1)%period]==1
            cur={'depth':d,'left_period':period,'left_pattern':pattern,'first_defect':first,
                 'left_end':first-1,'right_period':rp,'right_pattern':tail,'right_first':1-d,
                 'width':max(0,-d-first+1),'jump_backward':J,'period_changed':period!=q,
                 'anchor':anchor,'block_period':q,'orbit':[list(s) for s in orbit],
                 'cycle_start':mu,'cycle_length':lam,'safe_left_anchor':safe}
            jumps.append({'depth':d,'parent_first':first,'child_first':prev['first_defect'],
                          'jump':J,'left_period_before':q,'left_period_after':period,**erased})
            rows.append(row);cert.append(cur)
        histories[name]=rows;certificates[name]=cert;events[name]=jumps
        print(name,'left frontier at 512',cert[-1]['left_end'],'max jump',max(j['jump'] for j in jumps),flush=True)

    # Common future, computed on the expanded initial row. The black support
    # remains far from these finite boundaries throughout the 64 requested ticks.
    future=[];row=seed
    for t in range(1,FUTURE+1):
        nxt=bytearray(width)
        for i in range(1,width-1):nxt[i]=TRUTH[4*row[i-1]+2*row[i]+row[i+1]]
        future.append(nxt);row=nxt
    def pack(rows):
        raw=bytearray()
        for row in rows:
            for i in range(0,width,8):
                b=0
                for j in range(8):b=(b<<1)|(row[i+j] if i+j<width else 0)
                raw.append(b)
        return base64.b64encode(gzip.compress(bytes(raw),mtime=0)).decode()
    top={n:sorted(events[n],key=lambda j:(-j['jump'],j['depth']))[:8] for n in ('a','b')}
    payload={'x0':LO,'w':width,'t0':-DEPTH,'h':DEPTH+FUTURE+1,'stride':(width+7)//8,
             'encoding':'gzip-base64','failure':38,'top_jumps':top,
             'fronts':{n:[{k:c[k] for k in ('depth','first_defect','left_end','right_first','width','left_period','jump_backward') if k in c} for c in certificates[n]] for n in ('a','b')},
             'left_patterns':{n:[c['left_pattern'] for c in certificates[n]] for n in ('a','b')}}
    for n in ('a','b'):payload[n]=pack(list(reversed(histories[n]))+future)
    (out/'view.json').write_text(json.dumps(payload,separators=(',',':')))
    (out/'certificates.json').write_text(json.dumps({'input_view_sha256':VIEW_SHA,'rows':certificates,'events':events},separators=(',',':')))
    summary={'checks':counts,'top_jumps':top,'at_depths':{n:[{k:c[k] for k in ('depth','first_defect','left_end','width','left_period','right_period')} for c in certificates[n] if c['depth'] in (1,2,3,32,64,128,256,384,512)] for n in ('a','b')},
             'jumps_at_constant_period':{n:sum(j['jump']>1 and j['left_period_before']==j['left_period_after'] for j in events[n]) for n in ('a','b')}}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary))


if __name__=='__main__':main()
