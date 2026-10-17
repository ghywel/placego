#!/usr/bin/env python3
"""B131/MI282: one SAME2000 DLX pilot, independent literal/catalogue checker.

Reuses the unchanged B128 checker FUNCTIONS, not any search/encoding.
Frozen SHA/all ranks/order, full MITM/GF catalogue, literal variable-size bins.
Refuses overwrites; one child invocation, first failure/cap stops, no repair.
Usage: FILE BINARY FROZEN_B57_JSON LOCAL_PREFIX
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
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    binary, frozen, prefix = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    paths = {k:Path(str(prefix)+s) for k,s in
             [('stream','.txt'),('primary','.primary.json'),('catalogue','.catalogue.tsv'),
              ('input','.input.txt'),('report','.json')]}
    assert not any(p.exists() for p in paths.values()), 'refuse overwrite/restart'
    out, nodes = {'status':'ERROR'}, []
    try:
        raw = frozen.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == 'c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0'
        g = json.loads(raw)['groups'][1]
        records = g['rows']; targets = [tuple(r['targets']) for r in records]
        assert len(targets) == len(set(targets)) == 2000 and g['seed'] == 20261017
        assert g['total_domain'] == check.ways(8,68,784) == 24688633
        for t,r in zip(targets,records):
            check.budget()
            assert tuple(sorted(t)) == t and min(t)>=68 and max(t)<=122 and sum(t)==784
            assert check.rank_original(t) == r['rank']
        out['controls'] = check.controls()
        with paths['input'].open('x') as f:
            for t in targets:
                f.write(' '.join(map(str,t))+'\n')
        child_before = resource.getrusage(resource.RUSAGE_CHILDREN)
        with paths['input'].open() as inp, paths['stream'].open('x') as stream, paths['primary'].open('x') as err:
            proc = subprocess.run([str(binary.resolve()),str(paths['catalogue'])],stdin=inp,stdout=stream,stderr=err,
                                  timeout=45,check=False)
        child_after = resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work'] = child_after.ru_utime+child_after.ru_stime-child_before.ru_utime-child_before.ru_stime
        p = json.loads(paths['primary'].read_text());out['primary']=p
        assert (proc.returncode==0) == (p['status']=='COMPLETE_SAME_2000')
        assert p['status']!='ERROR' and p['control_nodes']>0 and p['restored']>0
        out['catalogue_verification'] = check.catalogue_check(paths['catalogue'])
        with paths['stream'].open() as f:
            assert f.readline() == '# B131 DLX m28:8 targets;8(size,tokens);nodes\n'
            for line in f:
                check.budget()
                row = list(map(int,line.split()));assert len(row)==45
                t = tuple(row[:8]);check.check_identity(targets[len(nodes)],t)
                offset,bins=8,[]
                for _ in range(8):
                    n=row[offset];offset+=1
                    assert 1<=n<=28
                    bins.append(row[offset:offset+n]);offset+=n
                assert offset==44 and row[-1]>0 and check.verify_partition(t,bins)
                nodes.append(row[-1])
        assert len(nodes)==p['completed']==len(p['query_cpu_us'])==len(p['query_updates'])
        assert sum(nodes)+p['pending_nodes']==p['pilot_attempted_nodes']
        if p['status']=='COMPLETE_SAME_2000':
            assert len(nodes)==2000 and not p['pending_target']
            assert p['restored']==p['matrices']+1  # the separate nested audit adds one
            out['status']='COMPLETE_SAME_2000_LITERAL_CERTIFICATES'
        elif p['status']=='FIRST_NO_WITNESS':
            check.check_identity(targets[len(nodes)],p['pending_target'])
            out['status']='PRIMARY_NEGATIVE_NOT_INDEPENDENTLY_CONFIRMED'
        else:
            if p['pending_target']:
                check.check_identity(targets[len(nodes)],p['pending_target'])
            out['status']=p['status']
        out['all_completed_nodes']=nodes
        out['node_distribution_completed']=check.distribution(nodes)
        out['query_cpu_us_distribution_completed']=check.distribution(p['query_cpu_us'])
        out['query_updates_distribution_completed']=check.distribution(p['query_updates'])
        out['pilot_attempted_link_updates']=p['link_updates']-p['control_updates']
        complete=out['status']=='COMPLETE_SAME_2000_LITERAL_CERTIFICATES'
        out['predictions']=dict(all2000_no_caps=complete,
                                full2000_loop_cpu_at_most10sec=complete and p['search_loop_cpu_seconds']<=10)
    except subprocess.TimeoutExpired:
        out.update(status='UNKNOWN_WATCHDOG',unfinished_native_call_statistics_unavailable=True)
        child_after=resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_cap_work']=child_after.ru_utime+child_after.ru_stime-child_before.ru_utime-child_before.ru_stime
    except Exception as e:
        out.update(status='ERROR_OR_CAP',reason=type(e).__name__+': '+str(e))
    out.update(checker_cpu_seconds=time.process_time()-check.START,wall_seconds=time.monotonic()-check.WALL,
               checker_peak_rss_bytes=check.rss(),literal_rows_checked=len(nodes))
    out['artifacts']={k:check.digest(p) for k,p in paths.items() if k!='report' and p.exists()}
    with paths['report'].open('x') as f:
        json.dump(out,f,sort_keys=True,separators=(',',':'));f.write('\n')
    brief={k:v for k,v in out.items() if k not in ('primary','all_completed_nodes')}
    if 'primary' in out:
        brief['primary_summary']={k:v for k,v in out['primary'].items() if k not in ('query_cpu_us','query_updates')}
    print(json.dumps(brief,sort_keys=True))
    return 0 if out['status']=='COMPLETE_SAME_2000_LITERAL_CERTIFICATES' else 2


if __name__=='__main__':
    raise SystemExit(main())
