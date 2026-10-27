#!/usr/bin/env python3
"""DQ-023 fixed cut/repair experiment, GC1939. No adaptive widening.
Run only through run_capped.py; CAPPED_OUT is required. Literal scalar and
packed engines independently evolve all cases. Output local windows -4..4.
Radius 288 exceeds the horizon plus recorded radius; no periodic wrapping.
"""
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import time

HORIZON = 256
RADIUS = 288
N = 2 * RADIUS + 1
MASK = (1 << N) - 1
CUTS = (14, 15, 16, 21, 22, 23)
DEADLINES = (15, 16, 21, 22, 23, 28)
RIGHT = '0000110110001101000'
# Literal outputs for input 000,001,...,111, independent of XOR formula.
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
ETHER = ((0,0,1,1),(0,1,1,0),(1,1,0,1),(0,1,0,1),
         (0,0,1,1),(0,0,0,1),(0,0,0,1))
last_guard = 0.0
pressure_samples = []


def guard(force=False):
    global last_guard
    now = time.monotonic()
    if not force and now-last_guard < 1:
        return
    last_guard = now
    p = subprocess.run(['sysctl','-n','kern.memorystatus_vm_pressure_level'],
                       capture_output=True, text=True, check=True, timeout=5)
    level = int(p.stdout)
    pressure_samples.append(level)
    if level != 1:
        raise RuntimeError('OS memory pressure is not normal')
    # A sampled combined CPU stop complements the supervisor's child limit.
    u = resource.getrusage(resource.RUSAGE_SELF)
    c = resource.getrusage(resource.RUSAGE_CHILDREN)
    if u.ru_utime+u.ru_stime+c.ru_utime+c.ru_stime > 110:
        raise RuntimeError('worker plus helper CPU stop')


def initial(cut, edits=()):
    row = [0]*N
    for d in range(1, RADIUS+1):
        row[RADIUS-d] = int((cut is None or d <= cut) and d%7 in (0,1,2))
    row[RADIUS] = 1
    for p, bit in enumerate(RIGHT, 1):
        row[RADIUS+p] = int(bit) ^ int(p in edits)
    return row


def scalar_step(row):
    # Explicit exterior whites. Errors at the far boundary cannot reach the
    # recorded window within HORIZON, even for the reference/diagnostic.
    ext = [0]+row+[0]
    return [TABLE[4*ext[j]+2*ext[j+1]+ext[j+2]] for j in range(N)]


def pack(row):
    return sum(bit << j for j, bit in enumerate(row))


def packed_step(row):
    return ((row << 1) ^ (row | (row >> 1))) & MASK


def history(row, engine, diagnostic=False):
    traces = []
    state = row[:] if engine == 'scalar' else pack(row)
    failure = None
    hard = None
    for t in range(HORIZON+1):
        if engine == 'scalar':
            window = state[RADIUS-4:RADIUS+5]
        else:
            window = [(state >> j)&1 for j in range(RADIUS-4,RADIUS+5)]
        traces.append(''.join(map(str,window)))
        if not diagnostic and window[4] != 1-t%2:
            failure = t
            break
        if diagnostic and t < HORIZON and t%2 == 0 and window[3] == 0:
            hard = t+1
            break
        if t == HORIZON:
            break
        state = scalar_step(state) if engine == 'scalar' else packed_step(state)
        if diagnostic:
            if engine == 'scalar':
                state[RADIUS] = t%2
            else:
                state = (state & ~(1 << RADIUS)) | ((t%2) << RADIUS)
    return {'failure':failure,'H':hard,'windows_minus4_to4':traces}


def checked(row, diagnostic=False):
    guard()
    a = history(row, 'scalar', diagnostic)
    b = history(row, 'packed', diagnostic)
    assert a == b, 'independent histories disagree'
    return a


def main():
    out = Path(os.environ['CAPPED_OUT'])
    guard(True)
    # Coordinates from the external Lean definitions, independent tabulation.
    assert all(ETHER[(3+6*d)%7][1] == int(d%7 in (0,1,2))
               for d in range(1,RADIUS+1))
    assert ''.join(str(ETHER[(3+p)%7][1]) for p in range(1,7)) == RIGHT[:6]
    assert RIGHT[6:] == '0110001101000'
    assert all(TABLE[4*l+2*c+r] == (l ^ (c|r))
               for l,c,r in itertools.product((0,1), repeat=3))
    reference = checked(initial(None))
    assert reference['failure'] is None
    # Instrument control: cuts 16..20 are the same row, not five cases.
    assert all(initial(k) == initial(16) for k in (17,18,19,20))
    duplicate = checked(initial(20))
    assert duplicate == checked(initial(16))
    cuts = []
    with (out/'cases.jsonl').open('x') as fh:
        for cut,d in zip(CUTS,DEADLINES):
            baseline = checked(initial(cut))
            assert baseline['failure'] == d, (cut,baseline['failure'],d)
            diagnostic = checked(initial(cut), True)
            h = diagnostic['H']
            assert h is None or h >= d
            item = {'cut':cut,'d':d,'H':h,'baseline':baseline,
                    'diagnostic':diagnostic,'searched':h is None or h>d,
                    'cases':0,'repairs':[]}
            if item['searched']:
                edits = [()] + [(p,) for p in range(1,20)] + list(itertools.combinations(range(1,20),2))
                for edit in edits:
                    hist = checked(initial(cut,edit))
                    f = hist['failure']
                    assert h is None or (f is not None and f <= h)
                    record = {'cut':cut,'edits':edit,**hist}
                    fh.write(json.dumps(record,separators=(',',':'))+'\n')
                    fh.flush()
                    item['cases'] += 1
                    if f is None or f>d:
                        item['repairs'].append({'edits':edit,'failure':f})
            cuts.append(item)
            (out/'partial.json').write_text(json.dumps(cuts))
    # Transfer is read from this same declared domain; no extra simulations.
    repairs = {tuple(r['edits']) for c in cuts for r in c['repairs']}
    transfer = [{'edits':e, 'repaired_cuts':[c['cut'] for c in cuts
                if any(tuple(r['edits'])==e for r in c['repairs'])]} for e in sorted(repairs)]
    result = {'status':'COMPLETE','controls':'PASS','horizon':HORIZON,
              'reference':reference,'duplicate_cut_control':'PASS',
              'cuts':cuts,'transfer':transfer,'prediction_P':bool(repairs),
              'cases_searched':sum(c['cases'] for c in cuts),
              'pressure_levels':pressure_samples,
              'interpretation':'finite repair only; no eternal-clock claim'}
    (out/'result.json').write_text(json.dumps(result,indent=1)+'\n')
    print(json.dumps({k:result[k] for k in ('status','controls','prediction_P','cases_searched')}))
    for c in cuts:
        print(json.dumps({'cut':c['cut'],'d':c['d'],'H':c['H'],
                          'repairs':len(c['repairs']),
                          'best_failure':max((r['failure'] or HORIZON+1 for r in c['repairs']),default=c['d'])}))


if __name__ == '__main__':
    main()
