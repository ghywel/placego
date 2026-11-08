#!/usr/bin/env python3
"""Three frozen original-cone branch questions; native solvers/checkers exec separately."""
import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys
import e_short_guard as short
import physical_47 as phys
import physical_ancestry as anc

CASES = ('short-converse', 'past-copy', 'past-rightOR')


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path, value): path.write_text(json.dumps(value, indent=2)+'\n')


def formula(case):
    if case == 'short-converse':
        c, ids, n = short.build('253353')
        pulse = [ids[3][0]]
        assert c.count(pulse) == 1
        c = [cl for cl in c if cl != pulse]
        a, b, d = ids[11][5:8]
        c += [[-ids[3][0]], [a], [b, d], [-b, -d]]
        return c, ids, n, 45
    assert case in CASES
    wanted = anc.word_heads(phys.E+phys.A*4+phys.E, 1)
    assert max(wanted) == 193
    c, off, w = phys.generate(193, wanted)
    ids = [[off[t]+p for p in range(1, w-t+1)] for t in range(194)]
    a, b, d, e, f = ids[119][5:10]
    if case == 'past-copy': c += [[a], [b, d], [-b, -d]]
    else: c += [[-a], [-b], [-d], [e, f]]
    return c, ids, off[-1], 193


def prepare(out):
    for l, c, r, y in itertools.product((0, 1), repeat=4):
        vals={1:l, 2:c, 3:r, 4:y}
        assert short.satisfied(phys.gate(1, 2, 3, 4), vals) == (y == l^(c|r))
    common, ids, true = short.build('253353')
    common.remove([ids[3][0]])
    controls=[]
    for root, pq in ((52777231658405, (0,0)), (54421244276371, (0,1)), (57931849600863, (1,1))):
        vals, rr=short.assignment(root, ids, true)
        assert short.satisfied(common, vals) and rr==phys.scalar_rows(root,45,46)
        assert (rr[3]&1, rr[13]>>7&1)==pq and rr[10]>>7&1==0
        assert not short.satisfied(common+[[ids[3][0] if pq[0]==0 else -ids[3][0]]],vals)
        wrong=[root]
        for t in range(45): wrong.append(anc.step(wrong[-1],1-anc.drive(t)))
        assert wrong[1]&1 != rr[1]&1
        controls.append({'root':str(root),'P_Q':pq,'all_clauses_and_scalar':True,'wrong_pulse_and_phase_rejected':True})
    wanted=anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1)
    full, off, w=phys.generate(359,wanted)
    full_path=out/'full-target-original.cnf'
    digest=phys.dimacs(full_path,full,off[-1])
    assert digest['sha256']=='21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c'
    lookup={tuple(cl) for cl in full}
    past, po, pw=phys.generate(193,anc.word_heads(phys.E+phys.A*4+phys.E,1))
    mapping={1:1}
    for t in range(194):
        for p in range(1,pw-t+1): mapping[po[t]+p]=off[t]+p
    assert all(tuple(mapping[abs(v)]*(1 if v>0 else -1) for v in cl) in lookup for cl in past)
    translated=short.head_word('253353')
    assert all(wanted[t+108]==bool(bit) for t,bit in translated.items())
    for case in CASES:
        c, ids, n, h=formula(case)
        info=phys.dimacs(out/(case+'.cnf'),c,n)
        save(out/(case+'.input.json'),{'case':case,'height':h,'variables':n,'clauses':len(c),'cnf':info})
    (out/'unit.cnf').write_text('p cnf 1 2\n1 0\n-1 0\n')
    (out/'good.lrat').write_text('3 0 1 2 0\n')
    (out/'bad.lrat').write_text('3 0 1 1 0\n')
    (out/'hard.cnf').write_text('p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n')
    (out/'empty.drat').write_text('')
    save(out/'prepare.json',{'gate16':True,'controls':controls,'full_target_original':digest,
        'all_past_clauses_embed_original':True,'past_clauses':len(past),'short_phase_and_head_embedding':True})
    print('PREPARE_PASS')


def answer(out, case):
    text=(out.parent/(case+'-solve.stdout')).read_text()
    if 's UNSATISFIABLE' in text:return 'UNSAT'
    if 's SATISFIABLE' in text:return 'SAT'
    assert 's UNKNOWN' in text or 's INDETERMINATE' in text,text[-300:]
    return 'UNKNOWN'


def convert(out, case):
    if case!='hard' and answer(out,case)!='UNSAT':print('NO_UNSAT_PROOF',case);return
    clauses={}; index=0
    for line in (out/(case+'.cnf')).read_text().splitlines():
        if line.startswith(('c','p')) or not line.strip():continue
        values=list(map(int,line.split()));assert values[-1]==0
        index+=1;clauses[index]=values[:-1]
    with (out/(case+'.drat')).open('w') as f:
        for line in (out/(case+'.lrat')).read_text().splitlines():
            words=line.split()
            if not words or words[0]=='c':continue
            if words[1]=='d':
                assert words[-1]=='0'
                for token in words[2:-1]:
                    cl=clauses.pop(int(token))
                    f.write('d '+' '.join(map(str,cl))+' 0\n')
            else:
                nums=list(map(int,words));end=nums.index(0,1);cl=nums[1:end]
                assert nums[0] not in clauses
                clauses[nums[0]]=cl;f.write(' '.join(map(str,cl))+' 0\n')
    print('CONVERT_PASS',case)


def native(out, case, kind, binary):
    if case not in ('hard','unit-good','unit-bad','hard-empty') and answer(out,case)!='UNSAT':
        print('NO_UNSAT_PROOF',case);return
    if kind=='cake':
        base='unit' if case.startswith('unit-') else case
        proof='good' if case=='unit-good' else 'bad' if case=='unit-bad' else case
        cmd=[binary,'--CML_HEAP_SIZE=512','--CML_STACK_SIZE=64',str(out/(base+'.cnf')),str(out/(proof+'.lrat'))]
    else:
        base='hard' if case=='hard-empty' else case
        proof='empty' if case=='hard-empty' else case
        cmd=[binary,str(out/(base+'.cnf')),str(out/(proof+'.drat'))]
    os.execv(binary,cmd)


def check_controls(out):
    log=lambda name:(out.parent/(name+'.stdout')).read_text()
    assert 's VERIFIED UNSAT' in log('unit-good')
    assert 's VERIFIED UNSAT' not in log('unit-bad')
    assert 's VERIFIED UNSAT' in log('hard-cake')
    assert 's VERIFIED' in log('hard-drat')
    assert 's VERIFIED' not in log('hard-empty')
    save(out/'native-controls.json',{'LRAT_good':True,'LRAT_corrupt_hint_rejected':True,'generated_LRAT_and_converted_DRAT':True,'empty_DRAT_rejected':True})
    print('NATIVE_CONTROLS_PASS')


def validate(out, case):
    status=answer(out,case);c, ids, true, h=formula(case)
    result={'case':case,'answer':status,'cnf_sha256':sha(out/(case+'.cnf'))}
    if status=='UNSAT':
        assert 's VERIFIED UNSAT' in (out.parent/(case+'-cake.stdout')).read_text()
        assert 's VERIFIED' in (out.parent/(case+'-drat.stdout')).read_text()
        result.update({'LRAT_checked_original':True,'second_DRAT_checked_original':True,'lrat_sha256':sha(out/(case+'.lrat')),'drat_sha256':sha(out/(case+'.drat'))})
    elif status=='SAT':
        vals={}
        for line in (out.parent/(case+'-solve.stdout')).read_text().splitlines():
            if line.startswith('v '):
                for v in map(int,line.split()[1:]):
                    if v:assert abs(v) not in vals;vals[abs(v)]=v>0
        assert short.satisfied(c,vals)
        root=sum(int(vals[v])<<p for p,v in enumerate(ids[0]));rr=anc.rows(root,h)
        assert rr==phys.scalar_rows(root,h,h+1)
        assert all(bool(rr[t]>>p&1)==vals[v] for t,row in enumerate(ids) for p,v in enumerate(row))
        shift=0 if h==45 else 108;t=11+shift
        window=[rr[t]>>(p-1)&1 for p in range(6,11)];a,b,d,e,f=window
        pulse=rr[3+shift]&1;q=rr[13+shift]>>7&1
        assert rr[10+shift]>>7&1==0
        assert q==a^(int(b==d)&(e|f))==1
        if case=='short-converse':assert pulse==0 and a==1 and b!=d
        elif case=='past-copy':assert pulse==1 and a==1 and b!=d
        else:assert pulse==1 and a==b==d==0 and (e|f)==1
        assert anc.ancestry(rr[-1],h)['rows']==rr
        extended=anc.rows(root,359 if h==193 else 85)
        seam=extended[193] if h==193 else extended[85]
        m=85 if h==45 else 193
        def terms(j,start,end):
            values=[]
            for s in range(start,end):
                p=j+1-m+s;assert p>=1
                values.append((rr[s]>>(p-1)|rr[s]>>p)&1)
            return values
        pt=terms(83,3+shift,10+shift);qt=terms(80,5+shift,13+shift)
        assert sum(pt)%2==pulse and sum(qt)%2==q
        state=[rr[t]>>9&1,rr[t]>>10&1,rr[t+1]>>10&1,rr[t+1]>>11&1]
        top=[rr[t+2]>>(p-1)&1 for p in (11,10,9,8)]
        A,B,C,D=state;lowers=[]
        for r in top:
            upper=r^(C|D);lower=upper^(A|B)
            lowers.append(lower);A,B,C,D=lower,A,upper,C
        assert lowers==window[3::-1]
        result['witness']={'root':str(root),'row119_window':window,'P':pulse,'Q':q,
            'all_original_clauses':True,'all_cone_cells':True,'scalar_replay':True,'full_finite_ancestry':True,
            'actual_register':state,'actual_top_word':top,'P_terms':pt,'Q_terms':qt,'seam_hex':hex(seam),
            'rows_hex':[hex(x) for x in rr]}
        if h==193:
            wanted=anc.word_heads(phys.E+phys.A*4+phys.E,1)
            assert all((rr[t]&1)==v for t,v in wanted.items())
            future=anc.word_heads(phys.A*7+phys.E,193)
            failed=[t for t,v in future.items() if (extended[t]&1)!=v]
            result['future_A7_E']={'satisfied':not failed,'first_mismatching_head':min(failed) if failed else None,'all_mismatching_heads':failed}
            if not failed:
                full,off,w=phys.generate(359,anc.word_heads(phys.E+phys.A*4+phys.E+phys.A*7+phys.E,1))
                fullvals={1:True}
                for t in range(360):fullvals.update({off[t]+p:bool(extended[t]>>(p-1)&1) for p in range(1,w-t+1)})
                assert short.satisfied(full,fullvals) and extended==phys.scalar_rows(root,359,360)
                result['FULL_TARGET_FINITE_WITNESS']=True
    save(out/(case+'.result.json'),result)
    print(case,status, 'root='+result.get('witness',{}).get('root','-'),result.get('future_A7_E',''))


def main():
    p=argparse.ArgumentParser();p.add_argument('phase');p.add_argument('--out',type=Path,required=True)
    p.add_argument('--case');p.add_argument('--kind');p.add_argument('--binary');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    if a.phase=='prepare':prepare(a.out)
    elif a.phase=='convert':convert(a.out,a.case)
    elif a.phase=='native':native(a.out,a.case,a.kind,a.binary)
    elif a.phase=='controls':check_controls(a.out)
    elif a.phase=='validate':validate(a.out,a.case)
    else:raise ValueError(a.phase)


if __name__=='__main__':main()
