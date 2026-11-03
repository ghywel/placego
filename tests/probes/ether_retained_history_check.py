#!/usr/bin/env python3
"""GC2446: CHECK ONLY Local's retained S13 certificate and replay ONE retained T600 tail.
No graph builder, search, producer, new tail or larger horizon. See frozen report.
"""
import ast
import collections
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import struct
import subprocess
import re
import time

def cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() - START_CPU + r.ru_utime + r.ru_stime

def budget():
    global LAST_THERMAL
    if cpu() > 15 or time.monotonic() - START_WALL > 35:
        raise RuntimeError('FROZEN_INTERNAL_BUDGET_STOP')
    if time.monotonic() - LAST_THERMAL >= 2:

        def cap():
            resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
        r = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True, timeout=3, preexec_fn=cap)
        with (OUT / 'thermal.txt').open('a') as f:
            f.write(r.stdout + r.stderr)
        limits = re.findall('CPU_(?:Speed|Scheduler)_Limit\\s*=\\s*(\\d+)', r.stdout + r.stderr)
        if r.returncode or len(limits) != 2 or any((x != '100' for x in limits)):
            raise RuntimeError('THERMAL_MONITOR_STOP')
        LAST_THERMAL = time.monotonic()

def need(ok, text):
    if not ok:
        raise ValueError(text)

def scalar_transition(v, u):
    """Independent cells at absolute offsets, then explicit new-anchor transport."""
    phase, bits = divmod(v, 1 << S)
    cells = {x: TAB[(2 + x) % 7][phase] for x in range(-8, 1)}
    cells.update({x: bits >> x - 1 & 1 for x in range(1, S + 1)})
    cells[S + 1] = u
    nxt = {x: cells[x - 1] ^ (cells[x] | cells[x + 1]) for x in range(-7, S + 1)}
    phase2 = (phase + 1) % 4
    anchor = -7 if nxt[0] != TAB[2][phase2] else 0
    need(all((nxt[x] == TAB[(2 + x) % 7][phase2] for x in range(-7, 0))), 'ether locality')
    word = [nxt[anchor + i] for i in range(1, S + 1)]
    return (phase2 * (1 << S) + sum((b << i for i, b in enumerate(word))), anchor)

def verify(h, cycle):
    need(len(h) == N and all((type(x) is int for x in h)), 'potential integer domain')
    digest = hashlib.sha256()
    minimum = 10 ** 10
    for v in range(N):
        for u in (0, 1):
            w, d = scalar_transition(v, u)
            slack = h[v] + 44 * d + 7 - h[w]
            need(slack >= 0, 'potential inequality')
            minimum = min(minimum, slack)
            digest.update(struct.pack('<IBIi', v, u, w, d))
        if v % 1024 == 0:
            budget()
    drift = 0
    for i, (v, u, d) in enumerate(cycle):
        w, actual = scalar_transition(v, u)
        need((w, actual) == (cycle[(i + 1) % len(cycle)][0], d), 'cycle transition')
        drift += d
    need(drift == -7 and len(cycle) == 44, 'attainment')
    return dict(edges=2 * N, graph_sha256=digest.hexdigest(), minimum_slack=minimum, cycle_ticks=len(cycle), cycle_drift=drift)

def history_control():
    """Image of all five-cell initial rows, compared to hand 5-bit-history law."""
    image = set()
    for row in itertools.product((0, 1), repeat=5):
        mid = [row[i - 1] ^ (row[i] | row[i + 1]) for i in (1, 2, 3)]
        u2 = mid[0] ^ (mid[1] | mid[2])
        image.add((row[1], mid[0], row[2], mid[1], u2))
    predicted = set()
    for a, b, u, v, w in itertools.product((0, 1), repeat=5):
        good = (u == 0 or v == 1 - a) and (v == 0 or w == 1 - b) and (not (u == v == 0 and a == 1) or w == 1 - b)
        if good:
            predicted.add((a, b, u, v, w))
    need(image == predicted and len(image) == 16, 'two-tick history image')
    need((1, 0, 0, 0, 0) not in image, 'displayed fake cycle forbidden')
    bad = [(1, 0, 1, 1, 1), (0, 0, 0, 1, 0), (1, 0, 0, 0, 0)]
    need(all((x not in image for x in bad)), 'history negative controls')
    return dict(initial_rows=32, histories=16, exact_local_image=True, forbidden_examples=bad)

def kit_control():
    p = Path(os.environ['STRIP_KIT_SOURCE'])
    raw = p.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == KIT_HASH, 'kit source hash')
    text = raw.decode()
    table = text.split('def etherTable')[1].split(':=', 1)[1].split('/--', 1)[0]
    table = ast.literal_eval(table.replace('false', '0').replace('true', '1').strip())
    need(tuple((tuple(x) for x in table)) == TAB, 'kit ether table')
    wall = text.split('def wallStates')[1].split(':=', 1)[1].split('/-- Closure under', 1)[0]
    wall = ast.literal_eval(wall.replace('false', '0').replace('true', '1').strip())
    states = {ph * (1 << S) + sum((b << i for i, b in enumerate(word))) for ph, word in wall}
    need(len(states) == 109, 'kit wall states')
    for v in states:
        for u in (0, 1):
            w, d = scalar_transition(v, u)
            need(w in states and d == 0, 'kit wall closure')
    return dict(kit_source_sha256=KIT_HASH, wall_states=109, wall_inputs_checked=218)
S=13
N=4 << S
TAB=((0,0,1,1),(0,1,1,0),(1,1,0,1),(0,1,0,1),(0,0,1,1),(0,0,0,1),(0,0,0,1))
KIT_HASH='9413bfbf7b8d53f8320160d28b1c8ec7644a12369bcc224be9405415c27e282d'
START_CPU=time.process_time()
START_WALL=time.monotonic()
LAST_THERMAL=-10.0
OUT=Path(os.environ['CAPPED_OUT'])
TAIL_RECORD_HASH='596f189dfe0ac6d5069f48d317dc96f8c9ac0c630757f7459b083964653f567b'
CERT_HASH='f935aa2fd9f5de55ba51c771f7b93e84f3bddecb422651fea54f6dbb6486ae79'


def replay_tail(walls):
    import re
    p=Path(os.environ['INVASION_TAIL_RECORD'])
    raw=p.read_bytes()
    need(hashlib.sha256(raw).hexdigest()==TAIL_RECORD_HASH,'tail record changed')
    line=next(l for l in raw.decode().splitlines() if 'tail bits 0..1199 as hex' in l)
    value=int(line.rsplit(':',1)[1].strip(),16)
    need(value < 1 << 1200,'tail width')
    bits=''.join(str((value >> i)&1) for i in range(1200))
    tail_hash=hashlib.sha256(bits.encode()).hexdigest()
    need(tail_hash.startswith('5e9e0870f9730666'),'tail digest')
    (OUT/'tail.bits').write_text(bits+'\n')
    T=600
    lo0=-2*T-32;hi0=2*T+32
    refs=[sum(TAB[x%7][ph] << (x-lo0) for x in range(lo0,hi0+1)) for ph in range(4)]
    row=sum((TAB[x%7][0] if x<0 else ((value>>x)&1)) << (x-lo0) for x in range(lo0,hi0+1))
    cells=[TAB[x%7][0] if x<0 else ((value>>x)&1) for x in range(lo0,hi0+1)]
    lo=lo0;mask=(1 << (hi0-lo0+1))-1
    initial=next(x for x in range(1200) if ((value>>x)&1)!=TAB[x%7][0])
    need(initial<=10,'unexpected initial front')
    packed_front=[];scalar_front=[];first_wall=None;anchor=-5;anchor0=anchor
    anchor_path=[];shifts=[];halo_checks=0
    def wall_at(t,L,get):
        found=[]
        for a in range(L-13,L):
            if a%7!=2:continue
            word=sum(get(a+i) << (i-1) for i in range(1,14))
            if (t%4,word) in walls:found.append((a,word))
        return found
    pi=json.loads(__import__('gzip').decompress(Path(os.environ['LOCAL_STRIP_CERT']).read_bytes()))['pi']
    h0=pi[sum(((row >> (anchor+i-lo0))&1) << (i-1) for i in range(1,14))]
    for t in range(T+1):
        query_lo=-t;query_hi=initial+t
        need(lo<=query_lo and query_hi<=lo+len(cells)-1,'finite cone validity')
        crop=((1 << (query_hi-query_lo+1))-1) << (query_lo-lo0)
        diff=(row ^ refs[t%4]) & crop
        need(diff!=0,'front unexpectedly absent')
        L=(diff & -diff).bit_length()-1+lo0
        Ls=next(x for x in range(query_lo,query_hi+1) if cells[x-lo]!=TAB[x%7][t%4])
        need(L==Ls,'scalar/packed front')
        packed_front.append(L);scalar_front.append(Ls)
        get=lambda x:(row >> (x-lo0))&1
        gs=lambda x:cells[x-lo]
        wp=wall_at(t,L,get);ws=wall_at(t,L,gs)
        need(wp==ws,'scalar/packed wall entry')
        if wp and first_wall is None:first_wall=dict(t=t,L=L,anchors=wp)
        anchor_path.append(anchor)
        st=t%4*(1 << S)+sum(get(anchor+i) << (i-1) for i in range(1,14))
        need(44*(anchor-anchor0)+7*t>=pi[st]-h0,'telescoping bound actual path')
        need(anchor>=anchor0-7*((t+55)//44) and L>=anchor+1,'uniform finite envelope')
        if t==T:break
        changed=(get(anchor-1) ^ (get(anchor) | get(anchor+1))) != TAB[2][(t+1)%4]
        nxt=((row<<1) ^ (row | (row>>1))) & mask
        if changed:
            old=anchor;anchor-=7
            # Actual next input and all seven discarded known cells, no fresh choices.
            for j in range(7):
                x=old+S-6+j
                expected=get(x-1) ^ (get(x)|get(x+1))
                need(((nxt>>(x-lo0))&1)==expected,'reanchor known halo transport')
                halo_checks+=1
            shifts.append(t+1)
        row=nxt
        cells=[cells[i-1] ^ (cells[i] | cells[i+1]) for i in range(1,len(cells)-1)]
        lo+=1
        if t%32==0:budget()
    need([packed_front[t] for t in (150,300,450,600)]==[-21,-43,-62,-80],'retained marks changed')
    if first_wall:
        a=first_wall['anchors'][0][0]
        need(all(a<L<=a+13 for L in packed_front[first_wall['t']:]),'postentry pinning')
    trace=dict(tail_sha256=tail_hash,tail_record_sha256=TAIL_RECORD_HASH,T=T,
        initial_front=initial,front=packed_front,anchor=anchor_path,shifts=shifts,
        halo_cells_checked=halo_checks,first_wall=first_wall,min_front=min(packed_front),
        final_front=packed_front[-1],initial_potential=h0)
    (OUT/'trace.json').write_text(json.dumps(trace,indent=2)+'\n')
    return {k:v for k,v in trace.items() if k not in ('front','anchor','shifts')}


def main():
    import gzip
    need(resource.getrlimit(resource.RLIMIT_CPU)[0]<=20,'process CPU cap')
    budget()
    kit=kit_control()
    b=Path(os.environ['LOCAL_STRIP_CERT']).read_bytes()
    need(hashlib.sha256(b).hexdigest()==CERT_HASH,'certificate input hash')
    data=json.loads(gzip.decompress(b))
    need(data['S']==13 and data['weights']=='44*drift+7','certificate metadata')
    cycle=[[ph*(1 << S)+word,u,scalar_transition(ph*(1 << S)+word,u)[1]] for ph,word,u in data['cycle']]
    pot=verify(data['pi'],cycle)
    need(min(data['pi'])==-385 and max(data['pi'])==0,'potential range')
    wrong=data['pi'][:];wrong[cycle[0][0]]+=100000
    try:verify(wrong,cycle)
    except ValueError as e:need(str(e)=='potential inequality','wrong corruption failure')
    else:raise ValueError('corrupted potential accepted')
    w,_=scalar_transition(cycle[0][0],cycle[0][1])
    need(w != (cycle[1][0]^1),'cycle-link negative control')
    txt=Path(os.environ['STRIP_KIT_SOURCE']).read_text()
    wall=ast.literal_eval(txt.split('def wallStates')[1].split(':=',1)[1].split('/-- Closure under',1)[0].replace('false','0').replace('true','1').strip())
    walls={(ph,sum(v << i for i,v in enumerate(word))) for ph,word in wall}
    result=dict(status='RETAINED_CERTIFICATE_CHECKED',certificate_sha256=CERT_HASH,
        potential=pot,potential_range=[-385,0],kit=kit,history=history_control(),
        tail=replay_tail(walls),negative_controls='corrupt potential rejected; corrupt cycle link rejected',
        worker_cpu_s=cpu(),worker_wall_s=time.monotonic()-START_WALL)
    (OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
