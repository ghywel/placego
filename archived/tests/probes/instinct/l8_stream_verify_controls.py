#!/usr/bin/env python3
"""MI481 frozen small controls. No production stream or full census.
20wall seconds, first failure, one invocation. Five known-positive fixture towns.
"""
import copy,importlib.util,itertools,json,time
from pathlib import Path
import l8_stream_verify as V
START=time.monotonic()
def guard():assert time.monotonic()-START<20,'wall cap'
def encoded(rows):return [json.dumps(r)+'\n' for r in rows]
def footer(m,lo,n):return {'m':m,'l1':lo,'towns':n,'end':'DONE','stats':{'tiled':n,'unknown':0,'impossible':0,'greedy':0}}
def rejected(rows,m=26,lo=84):
    guard()
    try:V.check_chunk(encoded(rows),m,lo)
    except V.AuditError:return True
    return False

def main():
    rectangles=0
    for k,b,r in itertools.product(range(4),range(5),range(5)):
        guard();brute=sum(sum(x)==r for x in itertools.combinations_with_replacement(range(b+1),k))
        assert V.rectangle(k,b,r)==brute
        rectangles+=1
    assert rectangles==100 and len(V.specs())==285
    # Complete known-positive E26_l84 domain, the five partitions of surplus4.
    towns=[(84,84,84,84,84,84,84,88),(84,84,84,84,84,84,85,87),
           (84,84,84,84,84,84,86,86),(84,84,84,84,84,85,85,86),
           (84,84,84,84,85,85,85,85)]
    assert V.expected(26,84)==len(towns)==5
    # Use the existing proposer only to PREPARE tiny positive witnesses.
    source=Path(__file__).parents[1]/'cloud_reads/l8_certificates.py'
    spec=importlib.util.spec_from_file_location('fixture_proposer',source)
    M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
    rows=[];nodes=0
    for t in towns:
        guard();a,n,g=M.solve(26,t,1);assert isinstance(a,list)
        rows.append({'m':26,'town':list(t),'a':''.join(map(str,a))});nodes+=n
    good=rows+[footer(26,84,5)]
    assert V.check_chunk(encoded(good),26,84)==5
    # Permuting bin labels is mathematically irrelevant.
    relabel=copy.deepcopy(good)
    for row in relabel[:-1]:row['a']=''.join(str(7-int(c)) for c in row['a'])
    assert V.check_chunk(encoded(relabel),26,84)==5
    mutations={}
    bad=copy.deepcopy(good);bad[2]=copy.deepcopy(bad[1]);mutations['duplicate replaces omitted, same row count']=bad
    bad=copy.deepcopy(good);del bad[2];mutations['missing target']=bad
    bad=copy.deepcopy(good);bad[0]['a']='0'*26;mutations['bad assignment']=bad
    bad=copy.deepcopy(good);bad[0]['town'][0]=83;mutations['wrong chunk']=bad
    mutations['missing DONE']=copy.deepcopy(good[:-1])
    mutations['record after DONE']=copy.deepcopy(good+[good[0]])
    bad=copy.deepcopy(good);bad[0]={'m':26,'town':list(towns[0]),'r':'U'};mutations['unknown']=bad
    bad=copy.deepcopy(good);bad[0]={'m':26,'town':list(towns[0]),'r':'X'};mutations['impossible']=bad
    bad=copy.deepcopy(good);bad[-1]['towns']=4;mutations['footer mismatch']=bad
    for label,bad in mutations.items():assert rejected(bad),label
    assert V.expected(32,68)==0
    assert V.check_chunk(encoded([footer(32,68,0)]),32,68)==0
    assert rejected([],32,68),'missing empty chunk DONE'
    # The old per-record tiling and total-count conditions still accept
    # every row of the duplicate/omission mutation; coverage alone rejects it.
    dup=mutations['duplicate replaces omitted, same row count'][:-1]
    assert len(dup)==5
    for row in dup:
        sums=[0]*8
        for i,c in enumerate(row['a']):sums[int(c)]+=51-2*i
        assert sorted(sums)==row['town']
    print(json.dumps({'result':'FROZEN CONTROLS PASS','rectangles':rectangles,'manifest_chunks':285,
      'positive_towns':5,'fixture_solver_nodes':nodes,'negative_mutations':len(mutations),
      'duplicate_omission_preserves_old_validity_and_count':True,'empty_chunk_and_bin_relabel':'PASS',
      'seconds':time.monotonic()-START}),flush=True)
if __name__=='__main__':main()
