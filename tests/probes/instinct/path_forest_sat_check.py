#!/usr/bin/env python3
"""B129/MI279 independent literal/order/rank checker and one-shot watchdog.

Imports no primary encoding or SAT solver. Frozen SAME2000 input only.
No overwrites/restarts; raw artifacts local. Parent60CPU/60wall/256MiB,
child45wall watchdog,25CPU soft/26CPU hard OS fallback.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time

START, WALL = time.process_time(), time.monotonic()
FROZEN_SHA = 'c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0'


def rss():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r if sys.platform == 'darwin' else r * 1024


def budget():
    if time.process_time()-START > 60 or time.monotonic()-WALL > 60 or rss() > 256*1024*1024:
        raise RuntimeError('checker cap')


@lru_cache(None)
def ways(n, low, total):
    if n == 0:
        return int(total == 0)
    if total < n*low or total > 122*n:
        return 0
    return sum(ways(n-1, v, total-v) for v in range(low, min(122, total//n)+1))


def rank(t):
    value, total, low = 0, 784, 68
    for n, x in zip(range(8, 0, -1), t):
        value += sum(ways(n-1, v, total-v) for v in range(low, x))
        low, total = x, total-x
    assert total == 0
    return value


def verify(t, bins):
    return (len(t) == len(bins) == 8 and all(bins) and
            Counter(v for b in bins for v in b) == Counter(range(1, 56, 2)) and
            [sum(b) for b in bins] == list(t))


def check_identity(t, got):
    if tuple(t) != tuple(got):
        raise ValueError('changed/missing/duplicate target')


def controls():
    t = (69,69,69,93,121,121,121,121)
    bins = [[1,3,5,7,9,11,33],[13,15,41],[17,21,31],[19,23,51],
            [25,43,53],[27,39,55],[29,45,47],[35,37,49]]
    assert verify(t, bins)
    mixed = [b[:] for b in bins]
    mixed[0].remove(1)
    mixed[-1].append(1)
    assert verify((68,69,69,93,121,121,121,122), mixed)
    bad = [b[:] for b in bins]
    bad[0][0] = bad[1][0]
    assert not verify(t, bad)
    bad = [b[:] for b in bins]
    bad[0][0], bad[1][0] = bad[1][0], bad[0][0]
    assert not verify(t, bad)
    try:
        check_identity(t, (69,69,69,95,119,121,121,121))
    except ValueError:
        pass
    else:
        raise AssertionError('identity guard')
    # Published lower witness: independent cardinality obstruction, NOT a
    # claim that the SAT instrument has solved the 26-token negative.
    def least_tokens(target, m):
        return next(k for k in range(m+1) if k % 2 == target % 2 and k*(2*m-k) >= target)
    assert 4*least_tokens(67,26)+4*least_tokens(102,26) == 28 > 26
    return dict(known_positive=True, arbitrary_bin_sizes=True, duplicates_rejected=True,
                wrong_sums_rejected=True, identity_guard=True, lower_witness_token_count=True)


def distribution(values):
    if not values:
        return {}
    a = sorted(values)
    return dict(n=len(a), total=sum(a), mean=sum(a)/len(a), min=a[0],
                p50=a[(len(a)-1)//2], p90=a[(len(a)-1)*90//100],
                p95=a[(len(a)-1)*95//100], p99=a[(len(a)-1)*99//100], max=a[-1])


def digest(path):
    data = path.read_bytes()
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def main():
    if len(sys.argv) != 3:
        raise SystemExit('usage: CHECKER FROZEN_B57_JSON LOCAL_PREFIX')
    frozen, prefix = Path(sys.argv[1]), Path(sys.argv[2])
    paths = {key: Path(str(prefix)+suffix) for key, suffix in
             [('input','.input.txt'),('stream','.jsonl'),('witnesses','.witness.jsonl'),
              ('stderr','.stderr.txt'),('report','.json')]}
    assert not any(p.exists() for p in paths.values()), 'refuse overwrite/restart'
    out, results, starts, end = {'status':'ERROR'}, [], [], None
    try:
        raw = frozen.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == FROZEN_SHA
        group = json.loads(raw)['groups'][1]
        records = group['rows']
        targets = [tuple(r['targets']) for r in records]
        assert len(targets) == len(set(targets)) == 2000 and group['seed'] == 20261017
        assert group['total_domain'] == ways(8,68,784) == 24688633
        for t, row in zip(targets, records):
            budget()
            assert tuple(sorted(t)) == t and 68 <= min(t) <= max(t) <= 122 and sum(t) == 784
            assert rank(t) == row['rank']
        out['checker_controls'] = controls()
        with paths['input'].open('x') as f:
            for t in targets:
                f.write(' '.join(map(str,t))+'\n')
        primary = Path(__file__).with_name('path_forest_sat_pilot.py')
        timed_out = False
        child_before = resource.getrusage(resource.RUSAGE_CHILDREN)
        with paths['stderr'].open('x') as err:
            try:
                proc = subprocess.run([sys.executable,str(primary),str(paths['input']),str(paths['stream'])],
                                      stderr=err, timeout=45, check=False)
                out['primary_exit_code'] = proc.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
                out['primary_exit_code'] = 'WATCHDOG'
        child_after = resource.getrusage(resource.RUSAGE_CHILDREN)
        out['child_cpu_seconds_including_unreported_cap_work'] = (
            child_after.ru_utime + child_after.ru_stime - child_before.ru_utime - child_before.ru_stime)
        for line in paths['stream'].read_text().splitlines():
            budget()
            row = json.loads(line)
            kind = row['kind']
            if kind == 'controls':
                assert 'primary_controls' not in out
                assert row['oracle_questions'] == 189 and row['fixed_assignments'] == row['wrong_bit_negatives'] == 126
                assert row['assumption_sequence'] == [True,False,True]
                assert row['duplicate_and_missing_assignment_rejected']
                assert row['full_width_fixed_positives'] == 2 and row['full_width_wrong_sum_rejected']
                out['primary_controls'] = row
            elif kind == 'model':
                assert 'model' not in out and 'primary_controls' in out
                out['model'] = row
            elif kind == 'start':
                assert len(starts) == len(results) and row['index'] == len(starts)
                check_identity(targets[len(starts)], row['target'])
                starts.append(row)
            elif kind == 'result':
                assert len(starts) == len(results)+1 and row['index'] == len(results)
                check_identity(targets[len(results)], row['target'])
                assert type(row['sat']) is bool or row['sat'] is None
                assert row['cpu_seconds'] >= 0 and row['stats']['conflicts'] >= 0
                if row['sat'] is True:
                    assert verify(row['target'], row['bins'])
                else:
                    assert row['bins'] is None
                assert not results or results[-1]['sat'] is True
                assert row['total_conflicts'] == sum(r['stats']['conflicts'] for r in results)+row['stats']['conflicts']
                results.append(row)
            elif kind == 'end':
                assert end is None
                end = row
            else:
                raise ValueError('unknown stream record')
        positives = [r for r in results if r['sat'] is True]
        out['literal_rows_checked'] = len(positives)
        out['all_attempted_stats'] = [r['stats'] for r in results]
        out['all_attempted_cpu_seconds'] = [r['cpu_seconds'] for r in results]
        out['attempted_conflict_distribution'] = distribution([r['stats']['conflicts'] for r in results])
        out['attempted_cpu_distribution'] = distribution([r['cpu_seconds'] for r in results])
        out['pending_target'] = starts[-1]['target'] if len(positives) < len(starts) else None
        out['primary_end'] = end
        out['unfinished_call_without_stats'] = len(starts) > len(results)
        with paths['witnesses'].open('x') as f:
            for r in positives:
                f.write(json.dumps({'target':r['target'],'bins':r['bins']},sort_keys=True,separators=(',',':'))+'\n')
        complete = (end is not None and end['status'] == 'COMPLETE_SAME_2000')
        if complete:
            assert len(positives) == len(results) == len(starts) == 2000 and out['primary_exit_code'] == 0
            out['status'] = 'COMPLETE_SAME_2000_LITERAL_CERTIFICATES'
        elif timed_out or not end:
            out['status'] = 'UNKNOWN_WATCHDOG_OR_OS_STOP'
        else:
            assert out['primary_exit_code'] != 0
            out['status'] = end['status']
        out['predictions'] = dict(all2000_no_cap=complete,
                                 full2000_search_cpu_at_most10sec=(complete and sum(r['cpu_seconds'] for r in results)<=10))
    except Exception as e:
        out.update(status='ERROR_OR_CAP',reason=type(e).__name__+': '+str(e))
    out.update(checker_cpu_seconds=time.process_time()-START,wall_seconds=time.monotonic()-WALL,
               checker_peak_rss_bytes=rss())
    out['artifacts'] = {k:digest(p) for k,p in paths.items() if k != 'report' and p.exists()}
    with paths['report'].open('x') as f:
        json.dump(out,f,sort_keys=True,separators=(',',':'))
        f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('all_attempted_stats','all_attempted_cpu_seconds')},sort_keys=True))
    return 0 if out['status']=='COMPLETE_SAME_2000_LITERAL_CERTIFICATES' else 2


if __name__ == '__main__':
    raise SystemExit(main())
