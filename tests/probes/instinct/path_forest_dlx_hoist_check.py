#!/usr/bin/env python3
"""B133/MI286 independent exact-state-trace/literal checker, SAME first3.

Paired late/early arms; replay of PASSING B132 is a new equivalence control,
not a retry of failed B131. No target expansion or automatic fullsample run.
Usage: FILE BINARY FROZEN_B57_JSON RETAINED_B132_PREFIX LOCAL_OUTPUT_PREFIX
"""
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time
import path_forest_unrestricted_pilot as check

ODDS=list(range(1,56,2))
ALL=(1<<28)-1


def validate_trace(target,states):
    lower=[next(k for k in range(1,29) if k%2==t%2 and sum(ODDS[-k:])>=t) for t in target]
    stack=[]
    for i,s in enumerate(states):
        used,left,tokens,minimum,rejected=s
        assert 0<=used<=ALL and 0<=left<256
        assert tokens==28-used.bit_count()
        assert minimum==sum(lower[b] for b in range(8) if left>>b&1)
        assert rejected==int(tokens<minimum)
        assert sum(target[b] for b in range(8) if left>>b&1)==sum(v for j,v in enumerate(ODDS) if not used>>j&1)
        depth=8-left.bit_count()
        if i==0:
            assert depth==0 and used==0 and left==255
        else:
            assert 0<depth<=len(stack)
            parent=stack[depth-1]
            assert not parent[4]
            removed=parent[1]^left
            assert removed and removed&(removed-1)==0 and parent[1]&removed and left==parent[1]^removed
            assert used&parent[0]==parent[0]
            added=used^parent[0]
            assert added and sum(v for j,v in enumerate(ODDS) if added>>j&1)==target[removed.bit_length()-1]
        stack=stack[:depth]+[s]
    assert states and states[-1][0]==ALL and states[-1][1:]==[0,0,0,0]


def trace_checker_controls():
    t=[69,69,69,93,121,121,121,121]
    bins=[[1,3,5,7,9,11,33],[13,15,41],[17,21,31],[19,23,51],
          [25,43,53],[27,39,55],[29,45,47],[35,37,49]]
    lower=[next(k for k in range(1,29) if k%2==x%2 and sum(ODDS[-k:])>=x) for x in t]
    states=[];used,left=0,255
    for depth in range(9):
        states.append([used,left,28-used.bit_count(),sum(lower[b] for b in range(8) if left>>b&1),0])
        if depth<8:
            used|=sum(1<<((v-1)//2) for v in bins[depth]);left^=1<<depth
    validate_trace(t,states)
    corrupted=[s[:] for s in states];corrupted[3][2]+=1
    for bad in (states[:-1],corrupted):
        try:validate_trace(t,bad)
        except (AssertionError,StopIteration):pass
        else:raise AssertionError('trace rejection control')
    return dict(valid_complete_trace_accepted=True,incomplete_trace_rejected=True,arithmetic_corruption_rejected=True)


def main():
    if len(sys.argv)!=5:raise SystemExit(__doc__)
    binary,frozen,baseline,prefix=map(Path,sys.argv[1:])
    paths={k:Path(str(prefix)+s) for k,s in [('stream','.txt'),('trace','.trace.txt'),('primary','.primary.json'),
             ('catalogue','.catalogue.tsv'),('input','.input.txt'),('report','.json')]}
    assert not any(p.exists() for p in paths.values()),'refuse overwrite/restart'
    out,rows,traces={'status':'ERROR'}, {}, {}
    try:
        old_primary=Path(str(baseline)+'.primary.json').read_bytes()
        old_stream=Path(str(baseline)+'.txt').read_bytes()
        assert hashlib.sha256(old_primary).hexdigest()=='31cfbb1f0441827879d6f55e8428a3a636a060de929228285f90b7df8eb747d2'
        assert hashlib.sha256(old_stream).hexdigest()=='0c7e8bc78742c07fffc3850f7480deede8dc2192f1bc356f9f4ce1a5313bd417'
        old=json.loads(old_primary);assert old['status']=='COMPLETE_SAME_FIRST3'
        old_rows=[list(map(int,line.split())) for line in old_stream.decode().splitlines()[1:]]
        raw=frozen.read_bytes()
        assert hashlib.sha256(raw).hexdigest()=='c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0'
        group=json.loads(raw)['groups'][1];records=group['rows'][:3];targets=[tuple(r['targets']) for r in records]
        assert len(group['rows'])==2000 and group['seed']==20261017 and group['total_domain']==check.ways(8,68,784)==24688633
        for t,r in zip(targets,records):
            assert tuple(sorted(t))==t and 68<=min(t)<=max(t)<=122 and sum(t)==784 and check.rank_original(t)==r['rank']
        out['literal_checker_controls']=check.controls();out['trace_checker_controls']=trace_checker_controls()
        with paths['input'].open('x') as f:
            for t in targets:f.write(' '.join(map(str,t))+'\n')
        child_before=resource.getrusage(resource.RUSAGE_CHILDREN)
        with paths['input'].open() as inp,paths['stream'].open('x') as stream,paths['primary'].open('x') as err:
            proc=subprocess.run([str(binary.resolve()),str(paths['catalogue']),str(paths['trace'])],stdin=inp,stdout=stream,stderr=err,timeout=45,check=False)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=after.ru_utime+after.ru_stime-child_before.ru_utime-child_before.ru_stime
        p=json.loads(paths['primary'].read_text());out['primary']=p
        assert (proc.returncode==0)==(p['status']=='COMPLETE_FIRST3_PAIRS')
        assert p['status']!='ERROR' and p['control_nodes']>0
        out['catalogue_verification']=check.catalogue_check(paths['catalogue'])
        order=[]
        with paths['stream'].open() as f:
            assert f.readline()=='# B133 paired DLX:arm,index,targets;8(size,tokens);nodes\n'
            for line in f:
                v=list(map(int,line.split()));assert len(v)==47
                arm,index=v[:2];key=(arm,index);assert key not in rows and arm in (0,1) and index in range(3)
                check.check_identity(targets[index],v[2:10]);offset,bins=10,[]
                for _ in range(8):
                    n=v[offset];offset+=1;assert 1<=n<=28
                    bins.append(v[offset:offset+n]);offset+=n
                assert offset==46 and check.verify_partition(targets[index],bins)
                assert v[2:]==old_rows[index]  # actual witness AND counted nodes, not just SAT
                rows[key]=v[2:];order.append(key)
        traceorder=[]
        for line in paths['trace'].read_text().splitlines():
            check.budget();v=list(map(int,line.split()));arm,index,n=v[:3];key=(arm,index)
            assert key in rows and key not in traces and len(v)==3+5*n
            states=[v[i:i+5] for i in range(3,len(v),5)]
            validate_trace(targets[index],states)
            assert n==rows[key][-1]==p['query_nodes'][arm][index]
            assert sum(s[4] for s in states)==p['query_prunes'][arm][index]
            traces[key]=states;traceorder.append(key)
        expected=[(0,0),(1,0),(1,1),(0,1),(0,2),(1,2)]
        complete=p['status']=='COMPLETE_FIRST3_PAIRS'
        if complete:
            assert order==traceorder==expected and len(rows)==len(traces)==6 and p['completed_pairs']==3
            for i in range(3):assert traces[0,i]==traces[1,i] and rows[0,i]==rows[1,i]
            assert p['restored']==p['matrices']+2 and not p['pending_target'] and not p['pending_nodes']
            assert sum(map(sum,p['query_nodes']))==p['pilot_attempted_nodes']
            out['status']='COMPLETE_EXACT_TRACE_EQUIVALENT_FIRST3'
        else:out['status']=p['status']
        out['literal_rows_checked']=len(rows);out['trace_states_checked']=sum(map(len,traces.values()))
        out['late_updates']=sum(p['query_updates'][0]);out['early_updates']=sum(p['query_updates'][1])
        out['late_case_cpu_us']=sum(p['query_cpu_us'][0]);out['early_case_cpu_us']=sum(p['query_cpu_us'][1])
        out['predictions']={'all_exact_traces_and_witnesses_match':complete,
             'early_updates_at_most_quarter_late':complete and 4*out['early_updates']<=out['late_updates'],
             'early_case_cpu_less_than_late':complete and out['early_case_cpu_us']<out['late_case_cpu_us']}
    except subprocess.TimeoutExpired:
        out.update(status='UNKNOWN_WATCHDOG',unfinished_native_statistics_unavailable=True)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=after.ru_utime+after.ru_stime-child_before.ru_utime-child_before.ru_stime
    except Exception as e:out.update(status='ERROR_OR_CAP',reason=type(e).__name__+': '+str(e))
    out.update(checker_cpu_seconds=time.process_time()-check.START,wall_seconds=time.monotonic()-check.WALL,checker_peak_rss_bytes=check.rss())
    out['artifacts']={k:check.digest(p) for k,p in paths.items() if k!='report' and p.exists()}
    with paths['report'].open('x') as f:json.dump(out,f,sort_keys=True,separators=(',',':'));f.write('\n')
    print(json.dumps(out,sort_keys=True));return 0 if out['status']=='COMPLETE_EXACT_TRACE_EQUIVALENT_FIRST3' else 2


if __name__=='__main__':raise SystemExit(main())
