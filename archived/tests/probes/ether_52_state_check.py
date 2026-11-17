#!/usr/bin/env python3
"""GC2450: one same-tail/T600 export testing52 event timing vs actual frame repetition.
No graph generation, search, new tail or larger horizon. Parent oracle/control source
is pinned; independent packed/list orbits compare all14 frame cells on every tick.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource

HERE=Path(__file__).resolve().parent
PARENT_HASH='007321f1b4231e731621ef8e41bf73010f7a8973da9730506c494dab571c2eda'
p=HERE/'ether_retained_history_check.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()==PARENT_HASH
spec=importlib.util.spec_from_file_location('frozen_history_parent',p)
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
OUT=b.OUT
TAIL_HASH='5e9e0870f9730666926f49cefb51a48dcba13713da5fed48beb8c70a5b25f1e7'
TRACE_HASH='d190c2fb02ba25668036d184f5c3ed988e828ded2245bc9987472e7593298b7e'


def compare_cells(packed,scalar):
    b.need(packed==scalar,'all16 physical-offset cells')


def main():
    b.need(resource.getrlimit(resource.RLIMIT_CPU)[0]<=20,'process CPU cap')
    b.budget();kit=b.kit_control()
    bits=Path(os.environ['RETAINED_TAIL_BITS']).read_text().strip()
    b.need(len(bits)==1200 and set(bits)<=set('01'),'tail domain')
    b.need(hashlib.sha256(bits.encode()).hexdigest()==TAIL_HASH,'tail hash')
    old=Path(os.environ['RETAINED_T600_TRACE']).read_bytes()
    b.need(hashlib.sha256(old).hexdigest()==TRACE_HASH,'prior trace hash')
    old=json.loads(old)
    prefix_front_cone_max=max(t+old['front'][t] for t in range(559))
    b.need(prefix_front_cone_max<=489,'full prefix490 pre-entry front guard')
    T=600;lo0=-1232;hi0=1232;lo=lo0
    value=sum(int(ch)<<i for i,ch in enumerate(bits));TAB=b.TAB
    row=sum((TAB[x%7][0] if x<0 else (value>>x)&1) << (x-lo0) for x in range(lo0,hi0+1))
    cells=[TAB[x%7][0] if x<0 else (value>>x)&1 for x in range(lo0,hi0+1)]
    mask=(1 << (hi0-lo0+1))-1;anchor=-5
    trace=[]
    for t in range(T+1):
        get=lambda x:(row>>(x-lo0))&1
        gs=lambda x:cells[x-lo]
        # All queried physical frame cells must lie inside the shrinking valid cone.
        b.need(lo<=anchor-1 and anchor+14<=lo+len(cells)-1,'frame cone validity')
        packed=[get(anchor+i) for i in range(-1,15)]
        scalar=[gs(anchor+i) for i in range(-1,15)]
        compare_cells(packed,scalar)
        if t==15:control_packed,control_scalar=packed[:],scalar[:]
        word=sum(get(anchor+i) << (i-1) for i in range(1,14))
        u=get(anchor+14);state=t%4*(1 << 13)+word
        nxt_state,d=b.scalar_transition(state,u)
        n0,d0=b.scalar_transition(state,0);n1,d1=b.scalar_transition(state,1)
        active=(d==0 and ((word>>12)&1)==0)
        b.need(d0==d1==d and (n0!=n1)==active,'exact input sensitivity')
        b.need((n0^n1)==((1<<12) if active else 0),'sensitivity coordinate')
        b.need(anchor==old['anchor'][t],'retained anchor mismatch')
        L=next(x for x in range(-t,old['initial_front']+t+1) if gs(x)!=TAB[x%7][t%4])
        b.need(L==old['front'][t],'retained front mismatch')
        trace.append(dict(t=t,a=anchor,phase=t%4,word=word,u=u,d=d,L=L,
                          next_state=nxt_state,effective_u=u if active else None))
        if t==T:break
        row=((row<<1) ^ (row | (row>>1))) & mask
        cells=[cells[i-1] ^ (cells[i] | cells[i+1]) for i in range(1,len(cells)-1)]
        lo+=1;anchor+=d
        if t%32==0:b.budget()
    # The proposed abstraction must match actual next states, including re-anchoring.
    for t in range(T):
        b.need(trace[t]['next_state']==trace[t+1]['phase']*(1 << 13)+trace[t+1]['word'],'frame transition')
    # Corrupt one stored physical cell and require an oracle mismatch.
    bad=control_packed[:];bad[2]^=1
    try:compare_cells(bad,control_scalar)
    except ValueError as e:b.need(str(e)=='all16 physical-offset cells','wrong corruption failure')
    else:raise ValueError('corrupt frame accepted')
    events=[r['t'] for r in trace[1:] if r['a']!=trace[r['t']-1]['a']]
    b.need(events==[15,67,119,171,223,275,327,379,431,475,519],'retained event marks')
    fields=('phase','word','u','d')
    def key(r):return tuple(r[k] for k in fields)
    def masked_key(r):return (r['phase'],r['word'],r['effective_u'],r['d'])
    def state_key(r):return (r['phase'],r['word'])
    base=trace[15:67]
    comparisons=[]
    for j in range(8):
        block=trace[15+52*j:67+52*j]
        mismatch=[i for i,(r,s) in enumerate(zip(base,block)) if key(r)!=key(s)]
        detail=None
        if mismatch:
            i=mismatch[0];detail=dict(offset=i,t=block[i]['t'],
                fields=[k for k in fields if base[i][k]!=block[i][k]],
                base=base[i],actual=block[i])
        comparisons.append(dict(block=j,start=15+52*j,full_matches=52-len(mismatch),
            mismatching_offsets=mismatch,first_mismatch=detail,
            state_matches=sum((r['phase'],r['word'])==(s['phase'],s['word']) for r,s in zip(base,block)),
            input_matches=sum(r['u']==s['u'] for r,s in zip(base,block)),
            masked_matches=sum(masked_key(r)==masked_key(s) for r,s in zip(base,block))))
    depart=next((r for r in trace[15:559] if key(r)!=key(base[(r['t']-15)%52])),None)
    masked_depart=next((r for r in trace[15:559] if masked_key(r)!=masked_key(base[(r['t']-15)%52])),None)
    state_depart=next((r for r in trace[15:559] if state_key(r)!=state_key(base[(r['t']-15)%52])),None)
    endpoints=[dict(t=t,a=trace[t]['a'],phase=trace[t]['phase'],word=trace[t]['word'],u=trace[t]['u'])
        for t in [15,67,119,171,223,275,327,379,431,475,519,558]]
    closed=(trace[15]['phase'],trace[15]['word'])==(trace[67]['phase'],trace[67]['word'])
    drift=sum(r['d'] for r in base)
    guarded=[];unguarded=[]
    for t in range(599):
        r,s,z=trace[t:t+3]
        a0=(r['word']>>12)&1;a1=(s['word']>>12)&1
        violates=(r['u']==s['u']==z['u']==0 and a0==1 and a1==0)
        if violates:
            unguarded.append(t)
            if r['a']==s['a']==z['a']:guarded.append(t)
    b.need(not guarded,'fixed-column three-white law')
    result=dict(status='FINITE_FRAME_EXPORT_CHECKED',kit=kit,tail_sha256=TAIL_HASH,
        parent_sha256=PARENT_HASH,prior_trace_sha256=TRACE_HASH,T=T,
        cells_compared=16*601,frame_transitions_checked=600,events=events,
        prefix490_front_cone_max=prefix_front_cone_max,
        comparisons=comparisons,endpoints=endpoints,base_closed=closed,base_drift=drift,
        abstract52cycle=closed and drift==-7,
        first_periodic_extrapolation_departure=depart,
        first_effective_extrapolation_departure=masked_depart,first_state_extrapolation_departure=state_depart,
        base_effective_inputs=''.join('.' if r['effective_u'] is None else str(r['effective_u']) for r in base),
        base_active_input_count=sum(r['effective_u'] is not None for r in base),
        guarded_three_white_violations=guarded,unguarded_apparent_violations=unguarded,
        negative_control='one stored physical-cell mutation rejected',
        worker_cpu_s=b.cpu(),worker_wall_s=b.time.monotonic()-b.START_WALL)
    (OUT/'frame-trace.json').write_text(json.dumps(trace,separators=(',',':'))+'\n')
    (OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
