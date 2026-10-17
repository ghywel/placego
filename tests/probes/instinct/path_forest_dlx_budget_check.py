#!/usr/bin/env python3
"""B132/MI284: isolated static-budget diagnostic on SAME first3 B131 targets.

Unchanged B128 literal/rank/MITM/GF helpers, no search import.
Baseline is the RETAINED B131 report, pinned; never rerun the old pilot.
One new invocation, same caps, stopfirst, no overwrite/repair/full sample.
Usage: FILE BINARY FROZEN_B57_JSON BASELINE_PRIMARY_JSON LOCAL_PREFIX
"""
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time
import path_forest_unrestricted_pilot as check


def main():
    if len(sys.argv)!=5:
        raise SystemExit(__doc__)
    binary,frozen,baseline,prefix=map(Path,sys.argv[1:])
    paths={k:Path(str(prefix)+s) for k,s in [('stream','.txt'),('primary','.primary.json'),
             ('catalogue','.catalogue.tsv'),('input','.input.txt'),('report','.json')]}
    assert not any(p.exists() for p in paths.values()),'refuse overwrite/restart'
    out,nodes={'status':'ERROR'},[]
    try:
        oldraw=baseline.read_bytes()
        assert hashlib.sha256(oldraw).hexdigest()=='e9c6290554fe0689621cd9515b11ff2301fbc003ea176697bed3906ca96c8846'
        old=json.loads(oldraw)
        assert old['completed']==2 and old['pending_nodes']==200001 and old['status']=='UNKNOWN_CAP'
        raw=frozen.read_bytes()
        assert hashlib.sha256(raw).hexdigest()=='c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0'
        g=json.loads(raw)['groups'][1];records=g['rows'][:3];targets=[tuple(r['targets']) for r in records]
        assert len(g['rows'])==2000 and g['seed']==20261017 and g['total_domain']==check.ways(8,68,784)==24688633
        assert tuple(old['pending_target'])==targets[2]
        for t,r in zip(targets,records):
            assert tuple(sorted(t))==t and 68<=min(t)<=max(t)<=122 and sum(t)==784
            assert check.rank_original(t)==r['rank']
        out['controls']=check.controls()
        out['baseline_pending_nodes']=old['pending_nodes']
        with paths['input'].open('x') as f:
            for t in targets:f.write(' '.join(map(str,t))+'\n')
        child_before=resource.getrusage(resource.RUSAGE_CHILDREN)
        with paths['input'].open() as inp,paths['stream'].open('x') as stream,paths['primary'].open('x') as err:
            proc=subprocess.run([str(binary.resolve()),str(paths['catalogue'])],stdin=inp,stdout=stream,stderr=err,timeout=45,check=False)
        child_after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=child_after.ru_utime+child_after.ru_stime-child_before.ru_utime-child_before.ru_stime
        p=json.loads(paths['primary'].read_text());out['primary']=p
        assert (proc.returncode==0)==(p['status']=='COMPLETE_SAME_FIRST3')
        assert p['status']!='ERROR' and p['control_nodes']>0
        out['catalogue_verification']=check.catalogue_check(paths['catalogue'])
        with paths['stream'].open() as f:
            assert f.readline()=='# B132 static-budget DLX m28:first3 targets;8(size,tokens);nodes\n'
            for line in f:
                check.budget();v=list(map(int,line.split()));assert len(v)==45
                t=tuple(v[:8]);check.check_identity(targets[len(nodes)],t)
                offset,bins=8,[]
                for _ in range(8):
                    n=v[offset];offset+=1;assert 1<=n<=28
                    bins.append(v[offset:offset+n]);offset+=n
                assert offset==44 and v[-1]>0 and check.verify_partition(t,bins)
                nodes.append(v[-1])
        assert len(nodes)==p['completed']==len(p['query_cpu_us'])==len(p['query_updates'])==len(p['query_prunes'])
        assert nodes==p['query_nodes'] and sum(nodes)+p['pending_nodes']==p['pilot_attempted_nodes']
        complete=p['status']=='COMPLETE_SAME_FIRST3'
        if complete:
            assert len(nodes)==3 and not p['pending_target'] and p['restored']==p['matrices']+1
            out['status']='COMPLETE_FIRST3_LITERAL_CERTIFICATES'
        else:
            if p['pending_target']:check.check_identity(targets[len(nodes)],p['pending_target'])
            out['status']='PRIMARY_NEGATIVE_UNCONFIRMED' if p['status']=='FIRST_NO_WITNESS' else p['status']
        out['all_completed_nodes']=nodes
        out['pilot_attempted_updates']=p['link_updates']-p['control_updates']
        out['pilot_capacity_prunes']=p['capacity_prunes']-p['control_prunes']
        out['predictions']={'all3_no_cap':complete,'third_at_most5000_states':complete and nodes[2]<=5000,
                            'full3_loop_cpu_at_most_0_1sec':complete and p['search_loop_cpu_seconds']<=0.1}
    except subprocess.TimeoutExpired:
        out.update(status='UNKNOWN_WATCHDOG',unfinished_native_statistics_unavailable=True)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=after.ru_utime+after.ru_stime-child_before.ru_utime-child_before.ru_stime
    except Exception as e:
        out.update(status='ERROR_OR_CAP',reason=type(e).__name__+': '+str(e))
    out.update(checker_cpu_seconds=time.process_time()-check.START,wall_seconds=time.monotonic()-check.WALL,
               checker_peak_rss_bytes=check.rss(),literal_rows_checked=len(nodes))
    out['artifacts']={k:check.digest(p) for k,p in paths.items() if k!='report' and p.exists()}
    with paths['report'].open('x') as f:json.dump(out,f,sort_keys=True,separators=(',',':'));f.write('\n')
    print(json.dumps(out,sort_keys=True))
    return 0 if out['status']=='COMPLETE_FIRST3_LITERAL_CERTIFICATES' else 2


if __name__=='__main__':raise SystemExit(main())
