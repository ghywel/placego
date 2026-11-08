#!/usr/bin/env python3
"""Fail-closed controls/seed preparation for L1594's serial Intel job."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import subprocess
import networkx as nx


def words(path):
    data = path.read_bytes()
    assert len(data) % 8 == 0
    return list(struct.unpack('<'+'Q'*(len(data)//8), data))


def parts(prefix):
    n, count = map(int, Path(str(prefix)+'.count').read_text().split())
    a = []
    for k in range(count):
        a += words(Path(str(prefix)+f'.part{k:03d}.bin'))
    assert len(a) == n and a == sorted(set(a))
    return a


def scalar_moves(word, width):
    ans = set()
    for a in (0, 1):
        for b in (0, 1):
            row = [0]+[(word >> k) & 1 for k in range(width)]+[a,b]
            middle = [1]+[row[k-1] ^ (row[k] | row[k+1]) for k in range(1,width+2)]
            final = [middle[k-1] ^ (middle[k] | middle[k+1]) for k in range(1,width+1)]
            ans.add(sum(x << k for k,x in enumerate(final)))
    return ans


def graph_rows(a, width):
    members = set(a)
    moves = {x: scalar_moves(x,width) for x in a}
    g = nx.DiGraph()
    g.add_nodes_from(a)
    g.add_edges_from((x,y) for x in a for y in moves[x] if y in members)
    cyclic = [s for s in nx.strongly_connected_components(g)
              if len(s)>1 or g.has_edge(next(iter(s)),next(iter(s)))]
    result = []
    for s in cyclic:
        first = min(s)
        level = {first:0}; todo=[first]
        for x in todo:
            for y in g[x]:
                if y in s and y not in level:level[y]=level[x]+1;todo.append(y)
        d = 0
        for x in s:
            for y in g[x]:
                if y in s:d=math.gcd(d,abs(level[x]+1-level[y]))
        cl=[set() for _ in range(d)]
        for x in s:cl[level[x]%d].add(x&1)
        locked=all(len(c)==1 for c in cl)
        p=0;word=''
        if locked:
            full=''.join(str(next(iter(c))) for c in cl)
            p=next(k for k in range(1,d+1) if d%k==0 and full==full[:k]*(d//k))
            word=full[:p]
        leaks=sum(y not in s for x in s for y in moves[x])
        result.append({'first':first,'nodes':len(s),'edges':g.subgraph(s).number_of_edges(),
                       'gcd':d,'locked':int(locked),'closed':int(leaks==0),
                       'primitive_period':p,'primitive_word':word,'leaks':leaks})
    return sorted(result,key=lambda r:r['first'])


def projected(rows):
    return sorted([{k:r[k] for k in ('first','nodes','edges','gcd','locked','closed',
                                    'primitive_period','primitive_word')}
                   for r in rows],key=lambda r:r['first'])


def read_scc(path,width):
    return [json.loads(l) for l in path.read_text().splitlines()
            if json.loads(l).get('W')==width and json.loads(l).get('stage')=='CORE']


def control(args):
    root=Path(os.environ['CAPPED_OUT']); folder=root/'controls';folder.mkdir()
    line=next(x for x in args.targets.read_text().splitlines() if x.startswith('lock7 '))
    fields=line.split();seed=list(map(int,fields[3:]));assert len(seed)==66
    lineb=next(x for x in args.targets.read_text().splitlines() if x.startswith('lock7b '))
    lockb=list(map(int,lineb.split()[3:]));assert len(lockb)==33
    assert all(y in set(lockb) for x in lockb for y in scalar_moves(x,45))
    rowsb=graph_rows(lockb,45);assert rowsb and all(r['primitive_period']==7 for r in rowsb)
    print('Independent33-window width45 closure/period control PASS',flush=True)
    seedfile=folder/'lock7.bin';seedfile.write_bytes(struct.pack('<66Q',*seed))
    for name,initial,width in [('whole',seed,30),('deleted',seed[1:],30)]:
        run=folder/name;run.mkdir();sf=run/'seed.bin';sf.write_bytes(struct.pack('<'+'Q'*len(initial),*initial))
        cmd=[str(args.binary),'--targets',str(args.targets),'--mode','xx','--no-lock7',
             '--resume',str(width),str(sf),'--wmax','32','--wreport','30',
             '--gapn','0','--over-max','0','--dump','--save-at','31','--out',str(run)]
        with (run/'stdout').open('w') as out:
            subprocess.run(cmd,stdout=out,check=True,timeout=60)
        state=set(initial)
        counts=[]
        for w in range(30,33):
            if w>30:state={x|(bit<<(w-1)) for x in state for bit in (0,1)}
            graph=nx.DiGraph();graph.add_nodes_from(state)
            graph.add_edges_from((x,y) for x in state for y in scalar_moves(x,w) if y in state)
            while True:
                dead=[x for x in graph if not graph.in_degree(x) or not graph.out_degree(x)]
                if not dead:break
                graph.remove_nodes_from(dead)
            state=set(graph)
            actual=words(run/f'core_{w}_xx.bin');assert actual==sorted(state)
            expected=graph_rows(actual,w)
            observed=read_scc(run/'scc_xx.jsonl',w)
            assert projected(expected)==projected(observed)
            if name=='whole':
                assert observed
                assert all(y in state for x in state for y in scalar_moves(x,w))
                assert {x & ((1<<30)-1) for x in state} <= set(seed)
                assert all(r['primitive_period']==7 for r in observed)
            counts.append([w,len(actual)])
        resumed=folder/(name+'-resume');resumed.mkdir()
        cmd=[str(args.binary),'--targets',str(args.targets),'--mode','xx','--no-lock7',
             '--resume-parts','31',str(run/'checkpoint_W31'),'--wmax','32','--wreport','31',
             '--gapn','0','--over-max','0','--dump','--out',str(resumed)]
        subprocess.run(cmd,stdout=subprocess.DEVNULL,check=True,timeout=60)
        assert (run/'core_32_xx.bin').read_bytes()==(resumed/'core_32_xx.bin').read_bytes()
        # A wrong CLOSED bit must fail the independent comparison.
        if observed:
            mutant=[dict(x) for x in observed];mutant[0]['closed']^=1
            assert projected(expected)!=projected(mutant)
        print(name,'independent closure/SCC/period/dump/checkpoint controls PASS',counts,flush=True)
    bad=folder/'missing'
    Path(str(bad)+'.count').write_bytes((folder/'whole/checkpoint_W31.count').read_bytes())
    cmd=[str(args.binary),'--targets',str(args.targets),'--mode','xx','--no-lock7',
         '--resume-parts','31',str(bad),'--wmax','32','--gapn','0','--out',str(folder)]
    test=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=30)
    assert test.returncode==2 and b'.part000.bin' in test.stderr
    print('Missing checkpoint part rejected PASS',flush=True)
    # New long-run CPU parser covers all documented ps time shapes.
    source=args.stage.read_text().split('plan=json.loads',1)[0]
    scope={};exec(compile(source,str(args.stage),'exec'),scope)
    for text,value in [('0:01.50',1.5),('180:00.00',10800),('03:00:00',10800),('1-00:00:01',86401)]:
        assert scope['ps_cpu'](text)==value
    telemetry=json.loads(Path(os.environ['CAPPED_MONITOR_CPU_FILE']).read_text())
    assert telemetry['cpu_s']>=0
    print('CPU telemetry and long-time parser controls PASS',flush=True)


def baseline(args):
    root=Path(os.environ['CAPPED_OUT']);base=args.baseline_root or root/'baseline'
    old=json.loads(args.prior.read_text());new=read_scc(base/'scc_xx.jsonl',40)
    assert len(old)==len(new)==22
    current={r['first']:r for r in new}
    for a in old:
        b=current[a['first']]
        # Ranks/parent ranks can permute when tied component sizes are sorted.
        for k,v in a.items():
            if k not in ('rank','parent'):assert b[k]==v,(k,a,b)
    h=hashlib.sha256();count=0
    n,parts_n=map(int,(base/'checkpoint_W40.count').read_text().split())
    for k in range(parts_n):
        data=(base/f'checkpoint_W40.part{k:03d}.bin').read_bytes();h.update(data);count+=len(data)
    assert n==20461951 and count==163695608
    assert h.hexdigest()=='f736b89dcf124e5917abf381caf46b0961631ca1c4749dbc7d6519c5ed363f85'
    allseeds=[]
    for rank,size,period,primitive in [(9,379,63,63),(15,78,21,7)]:
        a=parts(base/f'selected_W40_r{rank}');assert len(a)==size
        replay=graph_rows(a,40);assert len(replay)==1
        r=replay[0];oldrow=next(x for x in old if x['rank']==rank)
        assert r['gcd']==period and r['primitive_period']==primitive and not r['closed']
        for k in ('nodes','first','edges','gcd'):assert r[k]==oldrow[k]
        assert r['leaks']==oldrow['leak_core']+oldrow['leak_out']
        print('independent parent',rank,'gcd',period,'primitive',r['primitive_period'],'leaks',r['leaks'],flush=True)
        if primitive==7:allseeds+=a
    assert len(set(allseeds))==78
    (root/'Bseed.bin').write_bytes(struct.pack('<78Q',*sorted(allseeds)))
    (root/'baseline-check.json').write_text(json.dumps({'core40_sha256':h.hexdigest(),
        'legacy_rows_match':22,'selected_seed_windows':78,'excluded_primitive63_windows':379,
        'independent_seed_replay':True},indent=2)+'\n')
    print('Full40 exact legacy digest,22 rows and both independent parent controls PASS;78 primitive7 seeds',flush=True)


def finish(args):
    root=Path(os.environ['CAPPED_OUT']);out={}
    for arm in ('B','A'):
        path=root/arm/'scc_xx.jsonl'
        rows=[json.loads(l) for l in path.read_text().splitlines()] if path.exists() else []
        cores=[r for r in rows if r['stage']=='CORE']
        out[arm]={'largest_scc_width':max((r['W'] for r in cores),default=None),
                  'closed':[r for r in cores if r['closed']],
                  'period7k':[r for r in cores if r['locked'] and r['gcd']%7==0]}
    (root/'job-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:{'largest_scc_width':v['largest_scc_width'],'closed':len(v['closed'])}
                      for k,v in out.items()}),flush=True)


def resumeA(args):
    root=Path(os.environ['CAPPED_OUT'])
    if 'STOP discovery' in (root/'armB.stdout').read_text():
        print('STOP: new CLOSED component in armB; armA continuation not launched')
        return
    base=args.baseline_root or root/'baseline'
    os.execv(str(args.binary),[str(args.binary),'--targets',str(args.targets),
        '--mode','xx','--resume-parts','40',str(base/'checkpoint_W40'),
        '--wmax','50','--wreport','40','--gapn','0','--over-max','0',
        '--max-nodes','120000000','--stop-closed','--out',str(root/'A')])


def main():
    p=argparse.ArgumentParser();p.add_argument('phase',choices=['control','baseline','finish','resumeA'])
    p.add_argument('--binary',type=Path);p.add_argument('--targets',type=Path)
    p.add_argument('--prior',type=Path);p.add_argument('--stage',type=Path)
    p.add_argument('--baseline-root',type=Path)
    args=p.parse_args();globals()[args.phase](args)

if __name__=='__main__':main()
