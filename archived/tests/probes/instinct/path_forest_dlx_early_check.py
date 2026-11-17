#!/usr/bin/env python3
"""B134/MI288: ORIGINAL SAME2000 fixed early-check pilot, phased CPU costs.

Independent literal/rank/fullMITM/GF helpers; first3 traces pinned to B133.
No policy ladder/retries. Native30CPU/50wall,60wall watchdog,256MiB checks.
Usage: FILE BINARY FROZEN_B57_JSON RETAINED_B133_PREFIX LOCAL_PREFIX
OUTCOME MI289:239 rows checked;target240 state cap,no repair/fullsample result.
"""
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time
import path_forest_unrestricted_pilot as check
from path_forest_dlx_hoist_check import validate_trace,trace_checker_controls


def main():
    if len(sys.argv)!=5:raise SystemExit(__doc__)
    binary,frozen,baseline,prefix=map(Path,sys.argv[1:])
    paths={k:Path(str(prefix)+s) for k,s in [('stream','.txt'),('trace','.trace.txt'),('primary','.primary.json'),
             ('catalogue','.catalogue.tsv'),('input','.input.txt'),('report','.json')]}
    assert not any(p.exists() for p in paths.values()),'refuse overwrite/restart'
    out,nodes,early_traces={'status':'ERROR'},[],{}
    try:
        retained={s:Path(str(baseline)+s).read_bytes() for s in ('.primary.json','.txt','.trace.txt')}
        for suffix,want in [('.primary.json','4a3753ef5b85e373a0f62f9716dfc5acfacce8fd29e15bdfce7effb8d818e620'),
                            ('.txt','6734b3b5f19cd497feff271e49272c5aa9f3e7635b791270f6451687584c2246'),
                            ('.trace.txt','4e1263197c9db1abe1af36d67a5376531192105a13b5c19e38acd88b7fca4147')]:
            assert hashlib.sha256(retained[suffix]).hexdigest()==want
        old=json.loads(retained['.primary.json']);assert old['status']=='COMPLETE_FIRST3_PAIRS'
        old_rows={}
        for line in retained['.txt'].decode().splitlines()[1:]:
            v=list(map(int,line.split()))
            if v[0]==1:old_rows[v[1]]=v[2:]
        for line in retained['.trace.txt'].decode().splitlines():
            v=list(map(int,line.split()))
            if v[0]==1:early_traces[v[1]]=v
        raw=frozen.read_bytes()
        assert hashlib.sha256(raw).hexdigest()=='c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0'
        g=json.loads(raw)['groups'][1];records=g['rows'];targets=[tuple(r['targets']) for r in records]
        assert len(targets)==len(set(targets))==2000 and g['seed']==20261017
        assert g['total_domain']==check.ways(8,68,784)==24688633
        for t,r in zip(targets,records):
            check.budget();assert tuple(sorted(t))==t and min(t)>=68 and max(t)<=122 and sum(t)==784
            assert check.rank_original(t)==r['rank']
        out['literal_checker_controls']=check.controls();out['trace_checker_controls']=trace_checker_controls()
        with paths['input'].open('x') as f:
            for t in targets:f.write(' '.join(map(str,t))+'\n')
        child_before=resource.getrusage(resource.RUSAGE_CHILDREN)
        with paths['input'].open() as inp,paths['stream'].open('x') as stream,paths['primary'].open('x') as err:
            proc=subprocess.run([str(binary.resolve()),str(paths['catalogue']),str(paths['trace'])],stdin=inp,stdout=stream,stderr=err,timeout=60,check=False)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=after.ru_utime+after.ru_stime-child_before.ru_utime-child_before.ru_stime
        p=json.loads(paths['primary'].read_text());out['primary']=p
        assert (proc.returncode==0)==(p['status']=='COMPLETE_SAME_2000')
        assert p['status']!='ERROR' and p['control_nodes']>0
        out['catalogue_verification']=check.catalogue_check(paths['catalogue'])
        with paths['stream'].open() as f:
            assert f.readline()=='# B134 fixed early DLX m28:8 targets;8(size,tokens);nodes\n'
            for line in f:
                check.budget();v=list(map(int,line.split()));assert len(v)==45
                i=len(nodes);t=tuple(v[:8]);check.check_identity(targets[i],t);offset,bins=8,[]
                for _ in range(8):
                    n=v[offset];offset+=1;assert 1<=n<=28
                    bins.append(v[offset:offset+n]);offset+=n
                assert offset==44 and v[-1]>0 and check.verify_partition(t,bins)
                if i<3:assert v==old_rows[i]
                nodes.append(v[-1])
        trace_seen=set()
        for line in paths['trace'].read_text().splitlines():
            v=list(map(int,line.split()));assert v[0]==1 and 0<=v[1]<min(3,len(nodes))
            i=v[1];assert i not in trace_seen;trace_seen.add(i);assert v==early_traces[i]
            validate_trace(targets[i],[v[j:j+5] for j in range(3,len(v),5)])
        out['prefix_trace_equivalence_checked']=min(3,len(nodes))
        assert trace_seen==set(range(min(3,len(nodes))))
        assert len(nodes)==p['completed']==len(p['query_phases_us'])==len(p['query_updates'])==len(p['query_prunes'])
        assert nodes==p['query_nodes'] and sum(nodes)+p['pending_nodes']==p['pilot_attempted_nodes']
        complete=p['status']=='COMPLETE_SAME_2000'
        if complete:
            assert len(nodes)==2000 and not p['pending_target'] and p['restored']==p['matrices']+2
            out['status']='COMPLETE_SAME_2000_LITERAL_CERTIFICATES'
        else:
            if p['pending_target']:check.check_identity(targets[len(nodes)],p['pending_target'])
            out['status']='PRIMARY_NEGATIVE_UNCONFIRMED' if p['status']=='FIRST_NO_WITNESS' else p['status']
        phase_names=['construction','snapshot','search','restoration','destruction','case_total']
        phase_totals={name:sum(row[j] for row in p['query_phases_us']) for j,name in enumerate(phase_names)}
        assert all(len(row)==6 and min(row)>=0 and sum(row[:5])<=row[5]+5 for row in p['query_phases_us'])
        nonsearch=sum(phase_totals[k] for k in ('construction','snapshot','restoration','destruction'))
        out['completed_phase_totals_us']=phase_totals
        out['completed_nonsearch_fraction']=nonsearch/phase_totals['case_total'] if phase_totals['case_total'] else None
        out['all_completed_nodes']=nodes
        out['completed_node_distribution']=check.distribution(nodes)
        out['completed_case_cpu_us_distribution']=check.distribution([row[5] for row in p['query_phases_us']])
        out['completed_updates_distribution']=check.distribution(p['query_updates'])
        out['pilot_attempted_link_updates']=p['link_updates']-p['control_updates']
        out['predictions']={'all2000_no_caps':complete,
             'full2000_loop_cpu_at_most25sec':complete and p['search_loop_cpu_seconds']<=25,
             'full2000_nonsearch_at_least_half':complete and out['completed_nonsearch_fraction']>=0.5}
    except subprocess.TimeoutExpired:
        out.update(status='UNKNOWN_WATCHDOG',unfinished_native_statistics_unavailable=True)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=after.ru_utime+after.ru_stime-child_before.ru_utime-child_before.ru_stime
    except Exception as e:out.update(status='ERROR_OR_CAP',reason=type(e).__name__+': '+str(e))
    out.update(checker_cpu_seconds=time.process_time()-check.START,wall_seconds=time.monotonic()-check.WALL,
               checker_peak_rss_bytes=check.rss(),literal_rows_checked=len(nodes))
    out['artifacts']={k:check.digest(p) for k,p in paths.items() if k!='report' and p.exists()}
    with paths['report'].open('x') as f:json.dump(out,f,sort_keys=True,separators=(',',':'));f.write('\n')
    brief={k:v for k,v in out.items() if k not in ('primary','all_completed_nodes')}
    if 'primary' in out:brief['primary_summary']={k:v for k,v in out['primary'].items() if k not in ('query_nodes','query_updates','query_prunes','query_phases_us')}
    print(json.dumps(brief,sort_keys=True));return 0 if out['status']=='COMPLETE_SAME_2000_LITERAL_CERTIFICATES' else 2


if __name__=='__main__':raise SystemExit(main())
